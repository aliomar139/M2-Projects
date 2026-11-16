"""Exact-score thresholds and RF/TabPFN mixtures from verified saved contexts."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('binary',Path(__file__).with_name('train-binary.py'))
binary=importlib.util.module_from_spec(spec);spec.loader.exec_module(binary)
training=binary.training


def candidates(y, scores, share):
    assert np.isfinite(scores).all() and ((scores>=0)&(scores<=1)).all()
    thresholds=np.unique(np.r_[0.,scores,1.,np.nextafter(1.,np.inf)])
    return [{'rf_share':share,'threshold':float(t),**binary.metrics(y,scores>=t)} for t in thresholds]


def choose(rows, minimum=None):
    eligible=[r for r in rows if minimum is None or r['recall']>=minimum]
    assert eligible
    if minimum is None:
        return max(eligible,key=lambda r:(r['f2'],r['precision'],r['recall'],r['threshold'],r['rf_share']))
    return max(eligible,key=lambda r:(-r['fp'],r['recall'],r['precision'],r['f2'],r['threshold'],r['rf_share']))


def report(result,out):
    assert not result.duplicated(['augmentation','repeat','student_index']).any()
    assert np.array_equal(result.actual_class,(result.actual_score>=4).astype(int))
    assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
    result.to_csv(out/'held-out-predictions.csv',index=False)
    rows=[]
    for (method,rep),g in result.groupby(['augmentation','repeat']):
        assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
        rows.append({'procedure':method,'repeat':rep,**binary.metrics(g.actual_class,g.predicted_class),
            'average_precision':float(average_precision_score(g.actual_class,g.warning_score)),
            'roc_auc':float(roc_auc_score(g.actual_class,g.warning_score))})
    repeats=pd.DataFrame(rows);repeats.to_csv(out/'repeat-metrics.csv',index=False)
    summary=repeats.groupby('procedure').mean(numeric_only=True).drop(columns='repeat');summary.to_csv(out/'metrics-summary.csv')
    repeats[['procedure','repeat','tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
    paired=[]
    for r in repeats[repeats.procedure!='inner_selected_ratio'].itertuples():
        baseline=repeats[(repeats.procedure=='inner_selected_ratio')&(repeats['repeat']==r.repeat)].iloc[0]
        paired.append({'procedure':r.procedure,'repeat':r.repeat,**{k:getattr(r,k)-baseline[k] for k in ['recall','precision','f2','tp','fp']}})
    pd.DataFrame(paired).to_csv(out/'paired-comparisons.csv',index=False)
    return summary


def main():
    cp=ROOT/'classification/tabpfn-refinement-config.json';c=json.loads(cp.read_text())
    tab=ROOT/c['tabpfn_run'];rf=ROOT/c['rf_run']
    reference_manifests=[json.loads((p/'manifest.json').read_text()) for p in [tab,rf]]
    for m in reference_manifests:
        assert m['status']=='complete'
        assert all(training.sha256(ROOT/p)==h for p,h in m['source_sha256'].items())
    base=json.loads((rf/'reference-config.json').read_text());data=training.load_data(base)
    y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert len(data)==97 and np.bincount(y).tolist()==[80,17]
    tp=pd.read_csv(tab/'held-out-predictions.csv');rp=pd.read_csv(rf/'held-out-predictions.csv')
    current=tp[tp.augmentation=='inner_selected_ratio'].copy()
    oldrf=rp[rp.augmentation=='inner_selected_ratio'].copy()
    order=['repeat','student_index']
    pd.testing.assert_frame_equal(current.sort_values(order).reset_index(drop=True)[list(oldrf)],oldrf.sort_values(order).reset_index(drop=True))
    tab_predictions=tp[tp.augmentation=='tabpfn_f2'].copy()
    tab_tuning=json.loads((tab/'tuning.json').read_text());rf_tuning=json.loads((rf/'tuning.json').read_text())
    outer=pd.read_csv(tab/'outer-folds.csv');pd.testing.assert_frame_equal(outer,pd.read_csv(rf/'outer-folds.csv'))
    inner=pd.read_csv(tab/'inner-folds.csv');ri=pd.read_csv(rf/'inner-folds.csv');io=['repeat','fold','inner_fold','student_index']
    pd.testing.assert_frame_equal(inner.sort_values(io).reset_index(drop=True),ri.sort_values(io).reset_index(drop=True))
    paths=[cp,Path(__file__),Path(binary.__file__),Path(training.__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [p/name for p in [tab,rf] for name in ['manifest.json','tuning.json','held-out-predictions.csv','outer-folds.csv','inner-folds.csv']]
    paths += [rf/'reference-config.json',tab/'config.json',tab/'verification.json',rf/'verification.json']
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    contexts=[];fold_rows=[]
    for rep,seed in enumerate(base['cv']['outer_seeds'],1):
        for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
            tr=next(r for r in tab_tuning if r['repeat']==rep and r['fold']==fold)
            rr=next(r for r in rf_tuning if r['repeat']==rep and r['fold']==fold)
            assert tr['training_ids']==rr['inner_student_indices']==(train+1).tolist()
            assert tr['minimum_recall']==rr['inner_minimum_recall']
            minimum=tr['minimum_recall'];f=np.array(rr['inner_rf_scores']);t=np.array(tr['oof_scores'])
            assert len(f)==len(t)==len(train) and not set(train)&set(test)
            actual=binary.metrics(y[train],f>=rr['rf_choice']['chosen']['chosen_threshold']['threshold'])
            assert all(np.isclose(actual[k],rr['rf_choice']['chosen']['chosen_threshold'][k],atol=1e-12,rtol=0) for k in actual)
            for method,choice in tr['choices'].items():
                observed=binary.metrics(y[train],t>=choice['threshold'])
                assert all(np.isclose(observed[k],choice[k],atol=1e-12,rtol=0) for k in observed)
            expected=[]
            for number,(_,va) in enumerate(StratifiedKFold(4,shuffle=True,random_state=base['cv']['inner_seed']+rep*100+fold).split(train,y[train]),1):
                expected.extend({'input_set':'small_b','repeat':rep,'fold':fold,'inner_fold':number,'student_index':int(i+1)} for i in train[va])
            actual_inner=inner[(inner['repeat']==rep)&(inner.fold==fold)]
            pd.testing.assert_frame_equal(pd.DataFrame(expected).sort_values(io).reset_index(drop=True),actual_inner.sort_values(io).reset_index(drop=True))
            ftest=current[(current['repeat']==rep)&(current.fold==fold)].set_index('student_index').loc[test+1]
            ttest=tab_predictions[(tab_predictions['repeat']==rep)&(tab_predictions.fold==fold)].set_index('student_index').loc[test+1]
            assert np.array_equal(ftest.actual_class,y[test]) and np.array_equal(ttest.actual_class,y[test])
            contexts.append((rep,fold,train,test,f,t,ftest.warning_score.to_numpy(),ttest.warning_score.to_numpy(),minimum))
            fold_rows.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
    pd.testing.assert_frame_equal(pd.DataFrame(fold_rows),outer)
    timestamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    threshold_result=None
    for stage in ['threshold','voting']:
        out=ROOT/c[f'{stage}_output_root']/timestamp;out.mkdir(parents=True,exist_ok=False)
        (out/'config.json').write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8')
        (out/'reference-config.json').write_text(json.dumps(base,indent=2)+'\n',encoding='utf-8')
        m={'status':'running','stage':stage,'started_utc':datetime.now(timezone.utc).isoformat(),
            'source_sha256':hashes,'packages':{p:version(p) for p in ['numpy','pandas','scikit-learn','pyreadstat','xgboost','threadpoolctl']},
            'endpoint_refits':0,'new_synthetic_rows':0,'real_participants':97,'deployment_model_saved':False}
        manifest=out/'manifest.json';manifest.write_text(json.dumps(m,indent=2),encoding='utf-8')
        try:
            predictions=[];tuning=[]
            for rep,fold,train,test,f,t,fo,to,minimum in contexts:
                options=[]
                for share in ([0] if stage=='threshold' else c['rf_shares']):
                    options.extend(candidates(y[train],share*f+(1-share)*t,share))
                if stage=='threshold':
                    choices={'tabpfn_exact_f2':choose(options),'tabpfn_exact_guard':choose(options,minimum)}
                    previous=next(r for r in tab_tuning if r['repeat']==rep and r['fold']==fold)
                    assert choices['tabpfn_exact_f2']['f2']>=previous['choices']['tabpfn_f2']['f2']-1e-12
                    assert choices['tabpfn_exact_guard']['fp']<=previous['choices']['tabpfn_recall_guard']['fp']
                else:
                    pure=[r for r in options if r['rf_share']==1]
                    choices={'mixture_f2':choose(options),'mixture_guard':choose(options,minimum),
                        'rf_exact_f2':choose(pure),'rf_exact_guard':choose(pure,minimum)}
                    assert choices['mixture_f2']['f2']>=choices['rf_exact_f2']['f2']-1e-12
                    assert choices['mixture_guard']['fp']<=choices['rf_exact_guard']['fp']
                tuning.append({'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),'minimum_recall':minimum,
                    'inner_rf_scores':f.tolist(),'inner_tabpfn_scores':t.tolist(),'candidates':options,'choices':choices})
                for method,choice in choices.items():
                    scores=choice['rf_share']*fo+(1-choice['rf_share'])*to
                    predictions.extend({'input_set':'small_b','model':'tabpfn_exact' if stage=='threshold' else 'forest_tabpfn',
                        'augmentation':method,'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i]),
                        'actual_score':float(data.burnout_score.iloc[i]),'warning_score':float(s),
                        'threshold':choice['threshold'],'predicted_class':int(s>=choice['threshold'])} for i,s in zip(test,scores))
            new=pd.DataFrame(predictions)
            if stage=='threshold':threshold_result=new.copy();result=pd.concat([new,tp],ignore_index=True)
            else:result=pd.concat([new,threshold_result,current],ignore_index=True)
            assert len(result)==(2425 if stage=='threshold' else 3395)
            assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
            summary=report(result,out)
            outer.to_csv(out/'outer-folds.csv',index=False);inner.to_csv(out/'inner-folds.csv',index=False)
            (out/'tuning.json').write_text(json.dumps(tuning,indent=2),encoding='utf-8')
            lines=[f'# TabPFN {stage} refinement','',
                '97 real students, original eight Small B inputs, High >=4 (17) versus Below-high <4 (80).',
                'Original five repeats of five outer folds / four inner folds. Reuse verified frozen endpoint inner/outer scores; no new endpoint fits.',
                'Threshold candidates are every unique inner score plus 0, 1 and nextafter(1,+inf). Prediction uses >=. The last sentinel permits flagging nobody.',
                'F2 ties: precision, recall, higher threshold, RF share. Guard requires current RF recorded inner recall, minimizes FP, then recall/precision/F2/threshold/RF share.',
                'Guard is not a held-out recall guarantee. Only training-validation scores/labels choose thresholds and shares.',
                'RF retains selected training-only augmentation; TabPFN has no augmentation. Raw score mixtures are uncalibrated warning scores.', '',
                '| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |',
                '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
            for method,r in summary.iterrows():lines.append(f'| {method} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.6f} | {r.roc_auc:.6f} |')
            lines+=['','Mixtures use RF shares 1/.75/.5/0; pure RF exact-threshold controls isolate mixture effects.' if stage=='voting' else 'Compare exact thresholds with both unchanged original .05-grid TabPFN rules and the selected RF.',
                'Five repetitions reuse the same people. Many prior experiments motivated this exploratory comparison; no independent cohort, calibration or clinical validation.',
                'Current RF selection, source data and earlier outputs remain unchanged. Built with PriorLabs-TabPFN; original public TabPFN-2 checkpoint provenance/license remain in its reference run.']
            (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
            assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
            m.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,
                outer_groups=25,predictions=len(result),threshold_candidates=sum(len(r['candidates']) for r in tuning))
        except Exception as exc:
            m.update(status='failed',error=str(exc));raise
        finally:
            m['finished_utc']=datetime.now(timezone.utc).isoformat();manifest.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
        print(f'Complete: {out}\n{summary[["recall","precision","f2","tp","fp"]].to_string()}',flush=True)


if __name__=='__main__':main()
