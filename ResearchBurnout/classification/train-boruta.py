"""Nested, confirmed-only Boruta selection from existing non-BAT inputs."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

from boruta import BorutaPy
import boruta.boruta_py
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('comparison',Path(__file__).with_name('train-input-comparison.py'))
comparison=importlib.util.module_from_spec(spec);spec.loader.exec_module(comparison)
augmentation,binary,training=comparison.augmentation,comparison.binary,comparison.training


def select_inputs(c,base,X,y,seed):
    cols=list(X)
    encoded,_,groups=comparison.questions.selection.encode(base,cols,X,X)
    selector=BorutaPy(RandomForestClassifier(n_jobs=1,random_state=seed,**c['selector_forest']),
        random_state=seed,verbose=0,**c['selector']).fit(encoded,np.asarray(y))
    selected=[col for col in cols if np.any(selector.support_[groups==col])]
    assert set(selected)<=set(cols) and len(selector.support_)==encoded.shape[1]
    return selected, {'encoded_groups':groups.tolist(),'confirmed':selector.support_.tolist(),
        'tentative':selector.support_weak_.tolist(),'ranking':selector.ranking_.tolist(),
        'importance_history':np.where(np.isfinite(selector.importance_history_),selector.importance_history_,None).tolist(),
        'forest_iterations':int(len(selector.importance_history_)-1)}


def prepare(base,cols,X,y,valid,gen,ratio):
    added=min(len(gen),int(np.ceil(np.count_nonzero(y==1)*ratio)))
    labels=np.r_[y,np.ones(added,dtype=int)]
    if not cols:
        return np.zeros((len(labels),1)),np.zeros((len(valid),1)),labels
    augmented=pd.concat([X[cols],gen[cols].iloc[:added]],ignore_index=True)
    Xt,Xv=augmentation.kernels.transform(base,cols,augmented,valid[cols])
    return Xt,Xv,labels


def fit_scores(params,factor,seed,Xt,Xv,labels,empty):
    model=DummyClassifier(strategy='prior') if empty else binary.classifier('forest',params,seed)
    model.fit(Xt,labels,sample_weight=augmentation.priority.weights(labels,factor,1))
    return binary.probabilities(model,Xv)


def run_job(args):
    c,base,search,generator,data,rep,fold,train,test,old=args
    with threadpool_limits(limits=1):
        broad=base['input_sets']['broad_d'];X=data[broad].iloc[train]
        y=(data.burnout_score.iloc[train].to_numpy()>=4).astype(int)
        seed=base['cv']['inner_seed']+rep*100+fold
        inner=list(StratifiedKFold(4,shuffle=True,random_state=seed).split(train,y))
        parts={r:[] for r in c['ratios']};contexts=[];synthetic=[];assignments=[]
        for number,(tr,va) in enumerate(inner+[(np.arange(len(train)),np.array([],dtype=int))],1):
            number=number if number<=4 else 0
            assert not set(train[tr])&set(test) and not set(tr)&set(va)
            selector_seed=seed*10+number
            cols,details=select_inputs(c,base,X.iloc[tr],y[tr],selector_seed)
            gen,provenance,stats=augmentation.pool(X.iloc[tr],y[tr],base,generator,
                generator['seed']+rep*10000+fold*100+number)
            context={'repeat':rep,'fold':fold,'inner_fold':number}
            contexts.append({**context,'training_ids':(train[tr]+1).tolist(),'selector_seed':selector_seed,
                             'selected_inputs':cols,'selector':details,'generation':stats})
            synthetic.extend({**context,**row} for row in provenance)
            valid=X.iloc[va] if number else data[broad].iloc[test]
            if not number:outer={};outer_cols=cols
            for ratio in c['ratios']:
                prepared=prepare(base,cols,X.iloc[tr],y[tr],valid,gen,ratio)
                if number:parts[ratio].append((va,*prepared,not cols))
                else:outer[ratio]=prepared
            if number:
                assignments.extend({'input_set':'small_b',**context,'student_index':int(train[i]+1)} for i in va)
        minimum=old['chosen']['chosen_threshold']['recall'];candidates=[];inner_fits=0
        for ratio in c['ratios']:
            for factor in search['relative_high_weights']:
                for params in ParameterGrid(search['grids']['forest']):
                    oof=np.full(len(train),np.nan);seen=np.zeros(len(train),dtype=int)
                    for va,Xt,Xv,labels,empty in parts[ratio]:
                        oof[va]=fit_scores(params,factor,seed,Xt,Xv,labels,empty);seen[va]+=1;inner_fits+=1
                    assert np.isfinite(oof).all() and (seen==1).all()
                    index=len(candidates)
                    options=[{'candidate_index':index,'ratio':ratio,'threshold':t,**binary.metrics(y,oof>=t)}
                             for t in search['probability_thresholds']]
                    candidates.append({'candidate_index':index,'ratio':ratio,'factor':factor,'parameters':params,
                        'inner_scores':oof.tolist(),'f2_choice':comparison.choose(options),
                        'guard_choice':comparison.choose(options,minimum)})
        assert len(candidates)==36
        choices={'f2':comparison.choose([r['f2_choice'] for r in candidates]),
                 'recall_guard':comparison.choose([r['guard_choice'] for r in candidates],minimum)}
        predictions=[];cache={}
        for policy,choice in choices.items():
            index=choice['candidate_index'];candidate=candidates[index]
            if index not in cache:
                Xt,Xv,labels=outer[candidate['ratio']]
                cache[index]=fit_scores(candidate['parameters'],candidate['factor'],seed,Xt,Xv,labels,not outer_cols)
            predictions.extend({'input_set':'boruta23','model':'forest','augmentation':policy,'repeat':rep,'fold':fold,
                'student_index':int(i+1),'actual_class':int(data.burnout_score.iloc[i]>=4),
                'actual_score':float(data.burnout_score.iloc[i]),'warning_score':float(s),
                'threshold':choice['threshold'],'predicted_class':int(s>=choice['threshold'])} for i,s in zip(test,cache[index]))
        tuning={'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),'minimum_recall':minimum,
                'candidates':candidates,'choices':choices,'outer_selected_inputs':outer_cols}
        return predictions,tuning,contexts,synthetic,assignments,inner_fits,len(cache)


def report(result,out):
    rows=[]
    for (variant,policy,rep),g in result.groupby(['input_set','augmentation','repeat']):
        assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
        rows.append({'variant':variant,'policy':policy,'repeat':rep,**binary.metrics(g.actual_class,g.predicted_class),
            'average_precision':float(augmentation.average_precision_score(g.actual_class,g.warning_score)),
            'roc_auc':float(augmentation.roc_auc_score(g.actual_class,g.warning_score))})
    repeats=pd.DataFrame(rows);repeats.to_csv(out/'repeat-metrics.csv',index=False)
    summary=repeats.groupby(['variant','policy']).mean(numeric_only=True).drop(columns='repeat');summary.to_csv(out/'metrics-summary.csv')
    repeats[['variant','policy','repeat','tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
    pairs=[]
    for row in repeats[repeats.variant=='boruta23'].itertuples():
        old=repeats[(repeats.variant=='current8_control')&(repeats['repeat']==row.repeat)].iloc[0]
        pairs.append({'policy':row.policy,'repeat':row.repeat,**{k:getattr(row,k)-old[k] for k in ['recall','precision','f2','tp','fp']}})
    pd.DataFrame(pairs).to_csv(out/'paired-comparisons.csv',index=False)
    lines=['# Boruta selection from 23 existing inputs','',
        '97 real students; primary score >=4: 17 High, 80 Below-high. Original 5x5 stratified outer/four inner folds.',
        'Official BorutaPy 0.4.3, fixed 100 trees, max_iter=50 (at most 49 forest iterations), perc=100, alpha=.05, two_step=True.',
        'Selector forest: depth 5, min_samples_leaf=2, class_weight=balanced. Fit on training-only encoded real answers, never synthetic labels.',
        'Retain whole variables with any confirmed encoded column; tentative columns excluded. Retained categorical variables keep all dummy columns. No fixed variable count.',
        'A zero-confirmed context uses weighted training-class prior predictions, with no selected inputs. It does not silently select another variable.',
        'Generate constrained pools on all 23 real training variables, then project onto selected inputs. Projected duplicates may occur; synthetic labels are inferred assumptions.',
        'Tune the original 36 RF depth/leaf/High-weight/augmentation-ratio settings and .05-step thresholds inside training. F2 and recall-guard policies retain previous tie rules.',
        'Guard requires recorded current RF inner recall, not guaranteed outer recall. Reference current RF scores are copied, not retrained.','',
        '| Inputs | Rule | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | AUC |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for (variant,policy),r in summary.iterrows():
        lines.append(f'| {variant} | {policy} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.6f} | {r.roc_auc:.6f} |')
    lines+=['','Counts average five dependent repetitions of the same 97 people. This is one fixed selector setup, not all possible subsets or proof of population relevance.',
        'Encoded-column Boruta followed by whole-variable expansion is not a group-level significance test. Tentative status and impurity-importance biases remain limitations.',
        'Repeated same-sample exploration is not independent validation. No new survey questions, BAT inputs, source-data changes, deployment artifact or clinical probabilities.']
    (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return summary


def main():
    cp=ROOT/'classification/boruta-config.json';c=json.loads(cp.read_text());ref=ROOT/c['reference_run']
    rm=json.loads((ref/'manifest.json').read_text());assert rm['status']=='complete'
    base=json.loads((ref/'reference-config.json').read_text());search=json.loads((ref/'binary-config.json').read_text())
    generator=json.loads((ref/'config.json').read_text())['generator']
    modules=[comparison,comparison.questions,augmentation,binary,binary.ensemble,training,augmentation.kernels,
             augmentation.priority,comparison.questions.selection]
    helpers={Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    assert training.sha256(augmentation.__file__)==rm['script_sha256']
    assert all(helpers[k]==h for k,h in rm['helper_sha256'].items())
    assert all(version(p)==v for p,v in rm['packages'].items())
    assert all(training.sha256(ROOT/p)==h for p,h in rm['source_sha256'].items())
    data=training.load_data(base);y=(data.burnout_score.to_numpy()>=4).astype(int);broad=base['input_sets']['broad_d']
    assert len(data)==97 and len(broad)==23 and np.bincount(y).tolist()==[80,17]
    assert not any(col.startswith('BAT') or 'burnout' in col or col=='leave_intention' for col in broad)
    old=pd.read_csv(ref/'held-out-predictions.csv')
    current=old[(old.input_set=='small_b')&(old.model=='forest')&(old.augmentation=='inner_selected_ratio')].copy()
    current['input_set']='current8_control';current['augmentation']='f2'
    recipes=json.loads((ref/'tuning.json').read_text())
    paths=[cp,Path(__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [Path(m.__file__) for m in modules]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','binary-config.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv']]
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',c),('reference-config',base),('search-config',search),('generator-config',generator)]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest={'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,
        'packages':{p:version(p) for p in [*rm['packages'],'Boruta','scipy']},
        'boruta_implementation_sha256':training.sha256(boruta.boruta_py.__file__),'deployment_model_saved':False}
    mp=out/'manifest.json';mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Output: {out}',flush=True)
    try:
        jobs=[];folds=[]
        for rep,seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                old=next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio'
                    and r['repeat']==rep and r['fold']==fold)
                jobs.append((c,base,search,generator,data,rep,fold,train,test,old))
                folds.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
        outer=pd.DataFrame(folds);pd.testing.assert_frame_equal(outer,pd.read_csv(ref/'outer-folds.csv'))
        predictions=[];tuning=[];contexts=[];synthetic=[];assignments=[];ni=no=0
        with ProcessPoolExecutor(max_workers=c['workers']) as executor:
            futures=[executor.submit(run_job,job) for job in jobs]
            for count,future in enumerate(as_completed(futures),1):
                p,t,x,g,a,i,o=future.result();predictions.extend(p);tuning.append(t);contexts.extend(x);synthetic.extend(g);assignments.extend(a);ni+=i;no+=o
                print(f'Completed {count}/25: Boruta selections and nested RF tuning',flush=True)
        inner=pd.DataFrame(assignments);expected=pd.read_csv(ref/'inner-folds.csv');expected=expected[expected.input_set=='small_b']
        order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True)[list(expected)],expected.sort_values(order).reset_index(drop=True))
        result=pd.concat([pd.DataFrame(predictions),current],ignore_index=True).sort_values(['input_set','augmentation','repeat','fold','student_index']).reset_index(drop=True)
        assert len(result)==1455 and not result.duplicated(['input_set','augmentation','repeat','student_index']).any()
        np.testing.assert_array_equal(result.predicted_class,result.warning_score>=result.threshold)
        np.testing.assert_allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1],atol=1e-12,rtol=0)
        result.to_csv(out/'held-out-predictions.csv',index=False);outer.to_csv(out/'outer-folds.csv',index=False);inner.to_csv(out/'inner-folds.csv',index=False)
        pd.DataFrame(synthetic).to_csv(out/'synthetic-pools.csv',index=False)
        tuning.sort(key=lambda r:(r['repeat'],r['fold']));contexts.sort(key=lambda r:(r['repeat'],r['fold'],r['inner_fold']))
        for name,value in [('tuning',tuning),('training-contexts',contexts)]:
            (out/f'{name}.json').write_text(json.dumps(value,indent=2),encoding='utf-8')
        counts=pd.DataFrame([{'repeat':r['repeat'],'fold':r['fold'],'inner_fold':r['inner_fold'],'selected_count':len(r['selected_inputs']),
                             'selected_inputs':'|'.join(r['selected_inputs']),'forest_iterations':r['selector']['forest_iterations']} for r in contexts])
        counts.to_csv(out/'selection-counts.csv',index=False)
        selected=pd.DataFrame([{'repeat':r['repeat'],'fold':r['fold'],'variable':col} for r in contexts if r['inner_fold']==0 for col in r['selected_inputs']],columns=['repeat','fold','variable'])
        selected.to_csv(out/'selected-inputs.csv',index=False)
        selected.groupby('variable').size().rename('outer_fits_selected').to_csv(out/'selection-frequency.csv')
        summary=report(result,out)
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,real_participants=97,
            selector_fits=len(contexts),selector_forest_iterations=sum(r['selector']['forest_iterations'] for r in contexts),
            zero_selected_contexts=int((counts.selected_count==0).sum()),inner_fits=ni,outer_fits=no,candidate_settings=900)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Complete: {out}\n{summary[["recall","precision","f2","tp","fp"]].to_string()}',flush=True)


if __name__=='__main__':main()
