"""Independently tune 23-input SVC; preserve eight-input SVC and RF references."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import average_precision_score,roc_auc_score
from sklearn.model_selection import ParameterGrid,StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('svc',Path(__file__).with_name('19-compare-eight-input-svc-warnings.py'))
svc=importlib.util.module_from_spec(spec);spec.loader.exec_module(svc)
binary,training,kernels=svc.binary,svc.training,svc.kernels


def main():
    cp=ROOT/'experiments/20-compare-twenty-three-input-svc-warnings-settings.json';c=json.loads(cp.read_text());ref=ROOT/c['comparison_run']
    rm=json.loads((ref/'manifest.json').read_text());assert rm['status']=='complete'
    assert all(training.sha256(ROOT/p)==h for p,h in rm['source_sha256'].items())
    packages={p:version(p) for p in rm['packages']};assert packages==rm['packages']
    source=json.loads((ref/'config.json').read_text());base=json.loads((ref/'reference-config.json').read_text())
    data=training.load_data(base);cols=base['input_sets'][c['input_set']];y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert len(data)==97 and len(cols)==23 and np.bincount(y).tolist()==[80,17]
    assert set(base['input_sets']['small_b'])<set(cols)
    assert not any(col.startswith('BAT') or 'burnout' in col or col=='leave_intention' for col in cols)
    assert source['grid']=={'C':[.1,1,10,100],'gamma':[.01,.1,1]} and source['relative_high_weights']==[1,2,4]
    previous=pd.read_csv(ref/'held-out-predictions.csv');assert len(previous)==1455
    old_tuning=json.loads((ref/'tuning.json').read_text())
    modules=[svc,binary,binary.ensemble,training,kernels,svc.priority]
    paths=[cp,Path(__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [Path(m.__file__) for m in modules]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv','verification.json']]
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',c),('search-config',source),('reference-config',base),('input-columns',cols)]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest={'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,
        'packages':packages,'real_participants':97,'input_count':23,'synthetic_rows':0,'deployment_model_saved':False}
    mp=out/'manifest.json';mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    predictions=[];tuning=[];outer_rows=[];assignments=[];inner_fit_count=0;outer_fit_count=0
    try:
        with threadpool_limits(limits=1):
            warnings.filterwarnings('error',category=ConvergenceWarning)
            warnings.filterwarnings('ignore',message='The `probability` parameter was deprecated.*',category=FutureWarning,module=r'sklearn\.svm\._base')
            for rep,seed in enumerate(base['cv']['outer_seeds'],1):
                for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                    assert not set(train)&set(test)
                    inner_seed=base['cv']['inner_seed']+rep*100+fold
                    inner=list(StratifiedKFold(4,shuffle=True,random_state=inner_seed).split(train,y[train]))
                    X=data[cols].iloc[train];parts=[]
                    for number,(tr,va) in enumerate(inner,1):
                        assert not set(train[tr])&set(train[va]) and not set(train[tr])&set(test)
                        Xt,Xv=kernels.transform(base,cols,X.iloc[tr],X.iloc[va]);parts.append((tr,va,Xt,Xv))
                        assignments.extend({'input_set':'broad_d','repeat':rep,'fold':fold,'inner_fold':number,'student_index':int(i+1)} for i in train[va])
                    old=next(r for r in old_tuning if r['repeat']==rep and r['fold']==fold)
                    assert old['training_ids']==(train+1).tolist()
                    minimum=old['minimum_recall'];candidates=[]
                    for factor in source['relative_high_weights']:
                        for params in ParameterGrid(source['grid']):
                            index=len(candidates);oof=np.full(len(train),np.nan);seen=np.zeros(len(train),dtype=int)
                            for tr,va,Xt,Xv in parts:
                                model=svc.fit(source,params,factor,Xt,y[train[tr]],inner_seed);inner_fit_count+=1
                                oof[va]=svc.scores(model,Xv);seen[va]+=1
                            assert np.isfinite(oof).all() and (seen==1).all()
                            thresholds=np.unique(np.r_[oof,0.,np.nextafter(oof.max(),np.inf)])
                            options=[{'candidate_index':index,'threshold':float(t),**binary.metrics(y[train],oof>=t)} for t in thresholds]
                            candidates.append({'candidate_index':index,'parameters':params,'factor':factor,'inner_scores':oof.tolist(),
                                'threshold_count':len(thresholds),'f2_choice':svc.choose(options),'guard_choice':svc.choose(options,minimum)})
                    assert len(candidates)==36
                    choices={'svc23_f2':svc.choose([r['f2_choice'] for r in candidates]),
                        'svc23_recall_guard':svc.choose([r['guard_choice'] for r in candidates],minimum)}
                    Xt,Xv=kernels.transform(base,cols,X,data[cols].iloc[test]);cache={}
                    assert all(a.shape[1]==Xt.shape[1] for _,_,a,_ in parts)
                    for method,choice in choices.items():
                        index=choice['candidate_index'];candidate=candidates[index]
                        if index not in cache:
                            model=svc.fit(source,candidate['parameters'],candidate['factor'],Xt,y[train],inner_seed);outer_fit_count+=1
                            cache[index]=svc.scores(model,Xv)
                        predictions.extend({'input_set':'broad_d','model':'rbf_svc','augmentation':method,'repeat':rep,'fold':fold,
                            'student_index':int(i+1),'actual_class':int(y[i]),'actual_score':float(data.burnout_score.iloc[i]),
                            'warning_score':float(s),'threshold':choice['threshold'],'predicted_class':int(s>=choice['threshold'])} for i,s in zip(test,cache[index]))
                    tuning.append({'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),'minimum_recall':minimum,
                        'encoded_features':Xt.shape[1],'candidates':candidates,'choices':choices})
                    outer_rows.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                    print(f'Completed {len(tuning)}/25: independently tuned 23-input SVC',flush=True)
        outer=pd.DataFrame(outer_rows);inner_table=pd.DataFrame(assignments)
        pd.testing.assert_frame_equal(outer,pd.read_csv(ref/'outer-folds.csv'))
        expected=pd.read_csv(ref/'inner-folds.csv').drop(columns='input_set');order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner_table.drop(columns='input_set').sort_values(order).reset_index(drop=True),expected.sort_values(order).reset_index(drop=True))
        result=pd.concat([pd.DataFrame(predictions),previous],ignore_index=True)
        assert len(result)==2425 and not result.duplicated(['augmentation','repeat','student_index']).any()
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
        for r in repeats[repeats.procedure.isin(['svc23_f2','svc23_recall_guard'])].itertuples():
            for reference in ['inner_selected_ratio','svc_f2' if r.procedure=='svc23_f2' else 'svc_recall_guard']:
                baseline=repeats[(repeats.procedure==reference)&(repeats['repeat']==r.repeat)].iloc[0]
                pairs.append({'procedure':r.procedure,'reference':reference,'repeat':r.repeat,**{k:getattr(r,k)-baseline[k] for k in ['recall','precision','f2','tp','fp']}})
        pd.DataFrame(pairs).to_csv(out/'paired-comparisons.csv',index=False)
        lines=['# RBF SVC: 23 versus eight existing inputs','',
            '97 real students, High primary score >=4 (17) versus Below-high <4 (80). Broad D has 23 input variables before categorical encoding.',
            'Same original five repeats of five stratified outer / four inner folds; fit encoding/scaling on real training members only. No augmentation, BAT predictors or new questionnaire features.',
            'Same 36-setting search space as eight-input SVC: C .1/1/10/100, gamma .01/.1/1, normalized relative High weights 1/2/4. Settings/thresholds independently selected for 23 inputs.',
            'Exact inner margin thresholds and identical F2/recall-guard tie rules. Guard retains RF recorded inner recall, not a guarantee on excluded students.',
            'Earlier eight-input SVC and selected RF scores copied unchanged; no reference retraining. Margins are uncalibrated, not probabilities.', '',
            '| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |',
            '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        for method,r in summary.iterrows():lines.append(f'| {method} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.6f} | {r.roc_auc:.6f} |')
        lines+=['','Five dependent repetitions reuse the same students. AP/AUC pool margins from different fold fits and are discrimination diagnostics. No independent/clinical validation.',
            'This compares two independently tuned input sets within the same fixed search space, not every possible SVC. Source data, earlier results and selected RF remain unchanged. No deployment fit.']
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
