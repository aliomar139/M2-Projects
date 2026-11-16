"""Reconstruct input-comparison decisions and independently refit selected forests."""
import importlib.util
import json
from pathlib import Path
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import confusion_matrix, precision_score, recall_score, fbeta_score, average_precision_score, roc_auc_score
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

spec=importlib.util.spec_from_file_location('comparison',Path(__file__).with_name('train-input-comparison.py'))
comparison=importlib.util.module_from_spec(spec);spec.loader.exec_module(comparison)
ROOT, training, augmentation = comparison.ROOT, comparison.training, comparison.augmentation


def measurements(y, prediction):
    tn,fp,fn,tp=confusion_matrix(y,prediction,labels=[0,1]).ravel()
    return {'tp':int(tp),'fp':int(fp),'fn':int(fn),'tn':int(tn),
        'recall':float(recall_score(y,prediction,zero_division=0)),
        'precision':float(precision_score(y,prediction,zero_division=0)),
        'f2':float(fbeta_score(y,prediction,beta=2,zero_division=0))}


def independently_choose(options, minimum=None):
    eligible=[r for r in options if minimum is None or r['recall']>=minimum]
    if minimum is None:
        key=lambda r:(-r['f2'],-r['precision'],-r['recall'],-r['threshold'],r['ratio'],r['candidate_index'])
    else:
        key=lambda r:(r['fp'],-r['recall'],-r['precision'],-r['f2'],-r['threshold'],r['ratio'],r['candidate_index'])
    assert eligible
    return sorted(eligible,key=key)[0]


def check_choice(actual, expected):
    assert all(np.isclose(actual[k],v,rtol=0,atol=1e-12) for k,v in expected.items()),(actual,expected)


def main():
    out=ROOT/sys.argv[1];manifest=json.loads((out/'manifest.json').read_text());assert manifest['status']=='complete'
    assert all(training.sha256(ROOT/p)==h for p,h in manifest['source_sha256'].items())
    c=json.loads((out/'config.json').read_text());base=json.loads((out/'reference-config.json').read_text())
    search=json.loads((out/'search-config.json').read_text());generator=json.loads((out/'generator-config.json').read_text())
    data=training.load_data(base);y=(data.burnout_score.to_numpy()>=4).astype(int)
    result=pd.read_csv(out/'held-out-predictions.csv');tuning=json.loads((out/'tuning.json').read_text())
    contexts=json.loads((out/'training-contexts.json').read_text());synthetic=pd.read_csv(out/'synthetic-pools.csv')
    ref=ROOT/c['reference_run'];recipes=json.loads((ref/'tuning.json').read_text())
    assert len(result)==2425 and len(tuning)==75 and len(contexts)==375
    assert not result.duplicated(['input_set','augmentation','repeat','student_index']).any()
    np.testing.assert_array_equal(result.actual_class,y[result.student_index.to_numpy()-1])
    np.testing.assert_allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1],atol=1e-12,rtol=0)
    np.testing.assert_array_equal(result.predicted_class,result.warning_score>=result.threshold)
    all_outer=[];all_inner=[];threshold_count=inner_fits=outer_fits=0
    with threadpool_limits(limits=1):
        warnings.filterwarnings('error',category=ConvergenceWarning)
        for rep,outer_seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=outer_seed).split(data,y),1):
                seed=base['cv']['inner_seed']+rep*100+fold
                inner=list(StratifiedKFold(4,shuffle=True,random_state=seed).split(train,y[train]))
                old=next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest'
                    and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                all_outer.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                all_inner.extend({'input_set':'small_b','repeat':rep,'fold':fold,'inner_fold':n,'student_index':int(train[i]+1)}
                    for n,(_,va) in enumerate(inner,1) for i in va)
                for variant in ['current8_control','alternative8','ranked8_of23']:
                    record=next(r for r in tuning if r['repeat']==rep and r['fold']==fold and r['variant']==variant)
                    assert record['training_ids']==(train+1).tolist()
                    assert record['minimum_recall']==old['chosen']['chosen_threshold']['recall']
                    expected_grid = [(ratio,factor,params) for ratio in c['ratios']
                        for factor in search['relative_high_weights'] for params in ParameterGrid(search['grids']['forest'])]
                    if variant=='current8_control':
                        expected_grid=[(old['selected_ratio'],old['chosen']['factor'],old['chosen']['parameters'])]
                    assert [(r['ratio'],r['factor'],r['parameters']) for r in record['candidates']]==expected_grid
                    assert [r['candidate_index'] for r in record['candidates']]==list(range(len(expected_grid)))
                    f2_options=[];guard_options=[]
                    for candidate in record['candidates']:
                        scores=np.asarray(candidate['inner_scores']);assert len(scores)==len(train) and np.isfinite(scores).all()
                        options=[{'candidate_index':candidate['candidate_index'],'ratio':candidate['ratio'],'threshold':t,
                                  **measurements(y[train],scores>=t)} for t in search['probability_thresholds']]
                        threshold_count+=len(options)
                        best=independently_choose(options);guard=independently_choose(options,record['minimum_recall'])
                        check_choice(candidate['f2_choice'],best);check_choice(candidate['guard_choice'],guard)
                        f2_options.append(best);guard_options.append(guard)
                    check_choice(record['choices']['f2'],independently_choose(f2_options))
                    if variant!='current8_control':
                        check_choice(record['choices']['recall_guard'],independently_choose(guard_options,record['minimum_recall']))
                    chosen_indices={r['candidate_index'] for r in record['choices'].values()}
                    for number,(tr,va) in enumerate(inner+[(np.arange(len(train)),np.array([],dtype=int))],1):
                        number=number if number<=4 else 0
                        context=next(r for r in contexts if r['repeat']==rep and r['fold']==fold and r['variant']==variant and r['inner_fold']==number)
                        assert context['training_ids']==(train[tr]+1).tolist() and not set(train[tr])&set(test)
                        if variant=='ranked8_of23':
                            broad=base['input_sets']['broad_d']
                            ranking,strength=comparison.questions.ranked_questions(c,base,broad,data[broad].iloc[train[tr]],y[train[tr]])
                            assert context['ranking']==ranking
                            assert all(np.isclose(context['strength'][col],strength[col],atol=1e-12,rtol=0) for col in broad)
                            cols=[col for col in broad if col in ranking[:8]]
                        else:
                            cols=base['input_sets']['small_b'] if variant=='current8_control' else c['alternative_inputs']
                        assert cols==context['columns'] and len(cols)==8
                        X=data[cols].iloc[train[tr]];valid=data[cols].iloc[train[va] if number else test]
                        gen,provenance,stats=augmentation.pool(X,y[train[tr]],base,generator,generator['seed']+rep*10000+fold*100+number)
                        assert stats==context['generation']
                        saved=synthetic[(synthetic['repeat']==rep)&(synthetic.fold==fold)&(synthetic.variant==variant)&(synthetic.inner_fold==number)]
                        np.testing.assert_array_equal(saved[cols].to_numpy(),gen.to_numpy())
                        if provenance:
                            pd.testing.assert_frame_equal(saved[['parent_a','parent_b']].reset_index(drop=True),pd.DataFrame(provenance)[['parent_a','parent_b']],check_dtype=False)
                        for row in provenance:
                            assert row['parent_a'] in train[tr]+1 and row['parent_b'] in train[tr]+1
                            assert y[row['parent_a']-1]==y[row['parent_b']-1]==1
                        for index in chosen_indices:
                            candidate=record['candidates'][index];ratio=candidate['ratio']
                            Xt,Xv,labels,_=augmentation.prepare(X,y[train[tr]],valid,gen,ratio,base)
                            weights=np.where(labels==1,candidate['factor'],1.).astype(float);weights/=weights.mean()
                            model=RandomForestClassifier(n_estimators=100,n_jobs=1,random_state=seed,
                                **candidate['parameters']).fit(Xt,labels,sample_weight=weights)
                            scores=model.predict_proba(Xv)[:,list(model.classes_).index(1)]
                            if number:
                                inner_fits+=1
                                np.testing.assert_allclose(scores,np.asarray(candidate['inner_scores'])[va],rtol=0,atol=1e-12)
                            else:
                                outer_fits+=1
                                for policy,choice in record['choices'].items():
                                    if choice['candidate_index']!=index:continue
                                    saved_predictions=result[(result['repeat']==rep)&(result.fold==fold)&(result.input_set==variant)&(result.augmentation==policy)].set_index('student_index').loc[test+1]
                                    np.testing.assert_allclose(scores,saved_predictions.warning_score,atol=1e-12,rtol=0)
                                    assert np.allclose(saved_predictions.threshold,choice['threshold'])
                print(f'Verified repeat {rep}, fold {fold}: choices, training inputs, generation and selected refits',flush=True)
    order=['repeat','fold','inner_fold','student_index']
    pd.testing.assert_frame_equal(pd.DataFrame(all_outer),pd.read_csv(out/'outer-folds.csv'))
    pd.testing.assert_frame_equal(pd.DataFrame(all_outer),pd.read_csv(ref/'outer-folds.csv'))
    actual=pd.DataFrame(all_inner).sort_values(order).reset_index(drop=True)
    pd.testing.assert_frame_equal(actual,pd.read_csv(out/'inner-folds.csv').sort_values(order).reset_index(drop=True))
    old_inner=pd.read_csv(ref/'inner-folds.csv');old_inner=old_inner[old_inner.input_set=='small_b']
    pd.testing.assert_frame_equal(actual,old_inner.sort_values(order).reset_index(drop=True))
    old=pd.read_csv(ref/'held-out-predictions.csv');old=old[(old.input_set=='small_b')&(old.model=='forest')&(old.augmentation=='inner_selected_ratio')]
    key=['repeat','fold','student_index'];columns=key+['actual_class','actual_score','warning_score','threshold','predicted_class']
    control=result[result.input_set=='current8_control']
    pd.testing.assert_frame_equal(control[columns].sort_values(key).reset_index(drop=True),old[columns].sort_values(key).reset_index(drop=True))
    metrics=pd.read_csv(out/'repeat-metrics.csv')
    for row in metrics.itertuples():
        group=result[(result.input_set==row.variant)&(result.augmentation==row.policy)&(result['repeat']==row.repeat)]
        assert len(group)==97 and group.student_index.nunique()==97
        observed=measurements(group.actual_class,group.predicted_class)
        observed.update(average_precision=average_precision_score(group.actual_class,group.warning_score),roc_auc=roc_auc_score(group.actual_class,group.warning_score))
        assert all(np.isclose(getattr(row,k),v,atol=1e-12,rtol=0) for k,v in observed.items())
    summary=metrics.groupby(['variant','policy']).mean(numeric_only=True).drop(columns='repeat')
    pd.testing.assert_frame_equal(summary,pd.read_csv(out/'metrics-summary.csv').set_index(['variant','policy']))
    pairs=pd.read_csv(out/'paired-comparisons.csv')
    for row in pairs.itertuples():
        new=metrics[(metrics.variant==row.variant)&(metrics.policy==row.policy)&(metrics['repeat']==row.repeat)].iloc[0]
        old=metrics[(metrics.variant=='current8_control')&(metrics['repeat']==row.repeat)].iloc[0]
        assert all(np.isclose(getattr(row,k),new[k]-old[k],atol=1e-12,rtol=0) for k in ['recall','precision','f2','tp','fp'])
    assert all(training.sha256(ROOT/p)==h for p,h in manifest['source_sha256'].items())
    verification={'status':'passed','prediction_rows':len(result),'candidate_settings':sum(len(r['candidates']) for r in tuning),
        'threshold_candidates_checked':threshold_count,'choices_checked':sum(len(r['choices']) for r in tuning),
        'contexts_checked':len(contexts),'selected_inner_refits':inner_fits,'selected_outer_refits':outer_fits,
        'reference_scores_and_folds_reproduced':True,'sources_unchanged':True,
        'verification_script_sha256':training.sha256(__file__),
        'scope':'Independent sklearn metric/decision reconstruction, real-only selector context reproduction, generator/provenance reproduction and all selected inner/outer RF refits; unselected models not refitted. Not independent cohort validation.'}
    (out/'verification.json').write_text(json.dumps(verification,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(verification,indent=2),flush=True)


if __name__=='__main__':main()
