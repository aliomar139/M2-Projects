"""Separate nested RBF SVC comparison against the unchanged selected RF."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from sklearn.svm import SVC
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('binary',Path(__file__).with_name('10-compare-high-burnout-classifiers.py'))
binary=importlib.util.module_from_spec(spec);spec.loader.exec_module(binary)
training,kernels,priority=binary.training,binary.kernels,binary.priority


def fit(config,params,factor,X,y,seed):
    model=SVC(**config['fixed'],**params,random_state=seed).fit(X,y,sample_weight=priority.weights(y,factor,1))
    assert model.fit_status_==0 and np.array_equal(model.classes_,[0,1])
    return model


def scores(model,X):
    values=model.decision_function(X)
    assert values.shape==(len(X),) and np.isfinite(values).all()
    return values


def choose(rows,minimum=None):
    eligible=[r for r in rows if minimum is None or r['recall']>=minimum]
    assert eligible
    if minimum is None:
        return max(eligible,key=lambda r:(r['f2'],r['precision'],r['recall'],r['threshold'],-r['candidate_index']))
    return max(eligible,key=lambda r:(-r['fp'],r['recall'],r['precision'],r['f2'],r['threshold'],-r['candidate_index']))


def main():
    cp=ROOT/'experiments/19-compare-eight-input-svc-warnings-settings.json';c=json.loads(cp.read_text());ref=ROOT/c['reference_run']
    rm=json.loads((ref/'manifest.json').read_text());assert rm['status']=='complete'
    assert all(training.sha256(ROOT/p)==h for p,h in rm['source_sha256'].items())
    modules=[binary,binary.ensemble,training,kernels,priority]
    helpers={Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    assert all(helpers[k]==v for k,v in rm['helper_sha256'].items())
    packages={p:version(p) for p in rm['packages']};assert packages==rm['packages']
    base=json.loads((ref/'reference-config.json').read_text());data=training.load_data(base)
    cols=base['input_sets'][c['input_set']];y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert len(data)==97 and len(cols)==8 and np.bincount(y).tolist()==[80,17]
    assert c['fixed']['kernel']=='rbf' and not c['fixed']['probability']
    old=pd.read_csv(ref/'held-out-predictions.csv')
    current=old[(old.input_set=='small_b')&(old.model=='forest')&(old.augmentation=='inner_selected_ratio')].copy()
    assert len(current)==485
    recipes=json.loads((ref/'tuning.json').read_text())
    paths=[cp,Path(__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [Path(m.__file__) for m in modules]
    paths += [ref/name for name in ['manifest.json','reference-config.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv']]
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',c),('reference-config',base)]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest={'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,
        'helper_sha256':helpers,'packages':packages,'real_participants':97,'synthetic_rows':0,'deployment_model_saved':False}
    mp=out/'manifest.json';mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    predictions=[];tuning=[];outer_rows=[];assignments=[];inner_fit_count=0;outer_fit_count=0
    try:
        with threadpool_limits(limits=1):
            warnings.filterwarnings('error',category=ConvergenceWarning)
            for rep,seed in enumerate(base['cv']['outer_seeds'],1):
                for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                    assert not set(train)&set(test)
                    inner_seed=base['cv']['inner_seed']+rep*100+fold
                    inner=list(StratifiedKFold(4,shuffle=True,random_state=inner_seed).split(train,y[train]))
                    X=data[cols].iloc[train];parts=[]
                    for number,(tr,va) in enumerate(inner,1):
                        assert not set(train[tr])&set(train[va]) and not set(train[tr])&set(test)
                        Xt,Xv=kernels.transform(base,cols,X.iloc[tr],X.iloc[va]);parts.append((tr,va,Xt,Xv))
                        assignments.extend({'input_set':'small_b','repeat':rep,'fold':fold,'inner_fold':number,'student_index':int(i+1)} for i in train[va])
                    previous=next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                    minimum=previous['chosen']['chosen_threshold']['recall'];candidates=[]
                    for factor in c['relative_high_weights']:
                        for params in ParameterGrid(c['grid']):
                            index=len(candidates);oof=np.full(len(train),np.nan);seen=np.zeros(len(train),dtype=int)
                            for tr,va,Xt,Xv in parts:
                                model=fit(c,params,factor,Xt,y[train[tr]],inner_seed);inner_fit_count+=1
                                oof[va]=scores(model,Xv);seen[va]+=1
                            assert np.isfinite(oof).all() and (seen==1).all()
                            thresholds=np.unique(np.r_[oof,0.,np.nextafter(oof.max(),np.inf)])
                            options=[{'candidate_index':index,'threshold':float(t),**binary.metrics(y[train],oof>=t)} for t in thresholds]
                            candidates.append({'candidate_index':index,'parameters':params,'factor':factor,'inner_scores':oof.tolist(),
                                'threshold_count':len(thresholds),'f2_choice':choose(options),'guard_choice':choose(options,minimum)})
                    assert len(candidates)==36
                    choices={'svc_f2':choose([r['f2_choice'] for r in candidates]),
                        'svc_recall_guard':choose([r['guard_choice'] for r in candidates],minimum)}
                    Xt,Xv=kernels.transform(base,cols,X,data[cols].iloc[test]);cache={}
                    for method,choice in choices.items():
                        index=choice['candidate_index'];candidate=candidates[index]
                        if index not in cache:
                            model=fit(c,candidate['parameters'],candidate['factor'],Xt,y[train],inner_seed);outer_fit_count+=1
                            cache[index]=scores(model,Xv)
                        values=cache[index]
                        predictions.extend({'input_set':'small_b','model':'rbf_svc','augmentation':method,'repeat':rep,'fold':fold,
                            'student_index':int(i+1),'actual_class':int(y[i]),'actual_score':float(data.burnout_score.iloc[i]),
                            'warning_score':float(s),'threshold':choice['threshold'],'predicted_class':int(s>=choice['threshold'])} for i,s in zip(test,values))
                    tuning.append({'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),'minimum_recall':minimum,'candidates':candidates,'choices':choices})
                    outer_rows.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                    print(f'Completed {len(tuning)}/25: 36 SVC settings on four inner folds, then excluded-student evaluation',flush=True)
        outer=pd.DataFrame(outer_rows);inner_table=pd.DataFrame(assignments)
        pd.testing.assert_frame_equal(outer,pd.read_csv(ref/'outer-folds.csv'))
        expected=pd.read_csv(ref/'inner-folds.csv');expected=expected[expected.input_set=='small_b'];order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner_table.sort_values(order).reset_index(drop=True),expected.sort_values(order).reset_index(drop=True))
        result=pd.concat([pd.DataFrame(predictions),current],ignore_index=True)
        assert len(result)==1455 and not result.duplicated(['augmentation','repeat','student_index']).any()
        assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
        assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv',index=False)
        outer.to_csv(out/'outer-folds.csv',index=False);inner_table.to_csv(out/'inner-folds.csv',index=False)
        (out/'tuning.json').write_text(json.dumps(tuning,indent=2),encoding='utf-8')
        rows=[]
        for (method,rep),g in result.groupby(['augmentation','repeat']):
            assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
            rows.append({'procedure':method,'repeat':rep,**binary.metrics(g.actual_class,g.predicted_class),
                'average_precision':float(average_precision_score(g.actual_class,g.warning_score)),
                'roc_auc':float(roc_auc_score(g.actual_class,g.warning_score))})
        repeats=pd.DataFrame(rows);repeats.to_csv(out/'repeat-metrics.csv',index=False)
        summary=repeats.groupby('procedure').mean(numeric_only=True).drop(columns='repeat');summary.to_csv(out/'metrics-summary.csv')
        repeats[['procedure','repeat','tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
        pairs=[]
        for r in repeats[repeats.procedure!='inner_selected_ratio'].itertuples():
            baseline=repeats[(repeats.procedure=='inner_selected_ratio')&(repeats['repeat']==r.repeat)].iloc[0]
            pairs.append({'procedure':r.procedure,'repeat':r.repeat,**{k:getattr(r,k)-baseline[k] for k in ['recall','precision','f2','tp','fp']}})
        pd.DataFrame(pairs).to_csv(out/'paired-comparisons.csv',index=False)
        lines=['# RBF SVC: real-only High-score classification','',
            '97 real students, eight original Small B questions; High primary score >=4 (17) versus Below-high <4 (80). Selected RF reference copied unchanged.',
            'Original five repeats of five stratified outer folds and four inner folds. One-hot encoding/scaling fit on each real training group. No synthetic data or BAT predictors.',
            '36 settings: C .1/1/10/100, gamma .01/.1/1, normalized relative High weights 1/2/4. RBF kernel, no probability fitting, tol .001, max_iter 100000; convergence failures stop the run.',
            'Tune exact unique pooled inner decision margins plus 0 and an all-negative sentinel; classify >= threshold. Raw margins are not probabilities. No calibration.',
            'F2 rule jointly selects settings/threshold by F2, precision, recall, higher threshold, earlier candidate. Guard retains current RF recorded inner recall, minimizes FP, then recall/precision/F2/threshold/earlier candidate.',
            'Guard is an inner constraint, not an excluded-recall guarantee. All choices use training validation only; complete procedures evaluate on excluded students.', '',
            '| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |',
            '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        for method,r in summary.iterrows():lines.append(f'| {method} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.6f} | {r.roc_auc:.6f} |')
        lines+=['','Metrics average five dependent repetitions of the same students. AP/AUC pool margins across different fold fits and are ranking diagnostics, not calibrated risk estimates.',
            'Exploratory after many same-sample experiments; no independent cohort, clinical diagnosis or deployment model. Original selected RF/data/helpers/earlier outputs remain unchanged.']
        (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,
            inner_fits=inner_fit_count,outer_fits=outer_fit_count,candidate_settings=900,
            reconstructed_threshold_count=sum(r['threshold_count'] for t in tuning for r in t['candidates']))
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Complete: {out}\n{summary[["recall","precision","f2","tp","fp"]].to_string()}',flush=True)


if __name__=='__main__':main()
