"""Verify nested Boruta decisions, provenance, metrics and selected-model refits."""
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

spec=importlib.util.spec_from_file_location('runner',Path(__file__).with_name('train-boruta.py'))
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
spec=importlib.util.spec_from_file_location('checks',Path(__file__).with_name('verify-input-comparison.py'))
checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)
ROOT,training,augmentation=runner.ROOT,runner.training,runner.augmentation


def main():
    out=ROOT/sys.argv[1];manifest=json.loads((out/'manifest.json').read_text());assert manifest['status']=='complete'
    assert all(training.sha256(ROOT/p)==h for p,h in manifest['source_sha256'].items())
    assert all(version(p)==v for p,v in manifest['packages'].items())
    assert training.sha256(runner.boruta.boruta_py.__file__)==manifest['boruta_implementation_sha256']
    c=json.loads((out/'config.json').read_text());base=json.loads((out/'reference-config.json').read_text())
    search=json.loads((out/'search-config.json').read_text());generator=json.loads((out/'generator-config.json').read_text())
    data=training.load_data(base);y=(data.burnout_score.to_numpy()>=4).astype(int);broad=base['input_sets']['broad_d']
    tuning=json.loads((out/'tuning.json').read_text());contexts=json.loads((out/'training-contexts.json').read_text())
    result=pd.read_csv(out/'held-out-predictions.csv');synthetic=pd.read_csv(out/'synthetic-pools.csv')
    ref=ROOT/c['reference_run'];recipes=json.loads((ref/'tuning.json').read_text())
    assert len(result)==1455 and len(tuning)==25 and len(contexts)==125
    assert not result.duplicated(['input_set','augmentation','repeat','student_index']).any()
    np.testing.assert_array_equal(result.actual_class,y[result.student_index.to_numpy()-1])
    np.testing.assert_allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1],atol=1e-12,rtol=0)
    np.testing.assert_array_equal(result.predicted_class,result.warning_score>=result.threshold)
    outer_rows=[];inner_rows=[];ni=no=selector_refits=thresholds_checked=0
    with threadpool_limits(limits=1):
        for rep,outer_seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=outer_seed).split(data,y),1):
                seed=base['cv']['inner_seed']+rep*100+fold
                inner=list(StratifiedKFold(4,shuffle=True,random_state=seed).split(train,y[train]))
                record=next(r for r in tuning if r['repeat']==rep and r['fold']==fold)
                assert record['training_ids']==(train+1).tolist()
                old=next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                assert record['minimum_recall']==old['chosen']['chosen_threshold']['recall']
                grid=[(ratio,factor,params) for ratio in c['ratios'] for factor in search['relative_high_weights'] for params in ParameterGrid(search['grids']['forest'])]
                assert [(r['ratio'],r['factor'],r['parameters']) for r in record['candidates']]==grid
                assert [r['candidate_index'] for r in record['candidates']]==list(range(36))
                f2=[];guard=[]
                for candidate in record['candidates']:
                    scores=np.asarray(candidate['inner_scores']);assert len(scores)==len(train) and np.isfinite(scores).all()
                    options=[{'candidate_index':candidate['candidate_index'],'ratio':candidate['ratio'],'threshold':t,
                              **checks.measurements(y[train],scores>=t)} for t in search['probability_thresholds']]
                    thresholds_checked+=len(options)
                    best=checks.independently_choose(options);guarded=checks.independently_choose(options,record['minimum_recall'])
                    checks.check_choice(candidate['f2_choice'],best);checks.check_choice(candidate['guard_choice'],guarded)
                    f2.append(best);guard.append(guarded)
                checks.check_choice(record['choices']['f2'],checks.independently_choose(f2))
                checks.check_choice(record['choices']['recall_guard'],checks.independently_choose(guard,record['minimum_recall']))
                chosen={r['candidate_index'] for r in record['choices'].values()}
                for number,(tr,va) in enumerate(inner+[(np.arange(len(train)),np.array([],dtype=int))],1):
                    number=number if number<=4 else 0
                    context=next(r for r in contexts if r['repeat']==rep and r['fold']==fold and r['inner_fold']==number)
                    assert context['training_ids']==(train[tr]+1).tolist() and not set(train[tr])&set(test) and not set(tr)&set(va)
                    assert context['selector_seed']==seed*10+number
                    X=data[broad].iloc[train[tr]];valid=data[broad].iloc[train[va] if number else test]
                    encoded,_,groups=runner.comparison.questions.selection.encode(base,broad,X,X)
                    details=context['selector'];assert details['encoded_groups']==groups.tolist() and encoded.shape[1]==37
                    confirmed=np.asarray(details['confirmed']);weak=np.asarray(details['tentative']);rank=np.asarray(details['ranking'])
                    assert confirmed.dtype==bool and weak.dtype==bool and len(confirmed)==37 and not (confirmed&weak).any()
                    assert (rank[confirmed]==1).all() and (rank[weak]==2).all()
                    cols=[col for col in broad if confirmed[groups==col].any()]
                    assert cols==context['selected_inputs']
                    history=np.asarray(details['importance_history'],dtype=float)
                    assert history.shape==(details['forest_iterations']+1,37) and 1<=details['forest_iterations']<c['selector']['max_iter']
                    if rep==1 and fold==1 and number in [0,1]:
                        selected,reproduced=runner.select_inputs(c,base,X,y[train[tr]],context['selector_seed'])
                        assert selected==cols
                        for key in ['confirmed','tentative','ranking','encoded_groups']:assert reproduced[key]==details[key]
                        np.testing.assert_allclose(np.asarray(reproduced['importance_history'],dtype=float),history,atol=1e-12,rtol=0,equal_nan=True)
                        selector_refits+=1
                    gen,provenance,stats=augmentation.pool(X,y[train[tr]],base,generator,generator['seed']+rep*10000+fold*100+number)
                    assert stats==context['generation']
                    saved=synthetic[(synthetic['repeat']==rep)&(synthetic.fold==fold)&(synthetic.inner_fold==number)]
                    np.testing.assert_array_equal(saved[broad].to_numpy(),gen.to_numpy())
                    if provenance:
                        pd.testing.assert_frame_equal(saved[['parent_a','parent_b']].reset_index(drop=True),pd.DataFrame(provenance)[['parent_a','parent_b']],check_dtype=False)
                    for row in provenance:
                        assert row['parent_a'] in train[tr]+1 and row['parent_b'] in train[tr]+1
                        assert y[row['parent_a']-1]==y[row['parent_b']-1]==1
                    if number:
                        inner_rows.extend({'input_set':'small_b','repeat':rep,'fold':fold,'inner_fold':number,'student_index':int(train[i]+1)} for i in va)
                    else:assert cols==record['outer_selected_inputs']
                    for index in chosen:
                        candidate=record['candidates'][index]
                        added=min(len(gen),int(np.ceil(sum(y[train[tr]])*candidate['ratio'])))
                        labels=np.r_[y[train[tr]],np.ones(added,dtype=int)]
                        if cols:
                            augmented=pd.concat([X[cols],gen[cols].iloc[:added]],ignore_index=True)
                            Xt,Xv=augmentation.kernels.transform(base,cols,augmented,valid[cols])
                            model=RandomForestClassifier(n_estimators=100,n_jobs=1,random_state=seed,**candidate['parameters'])
                        else:
                            Xt=np.zeros((len(labels),1));Xv=np.zeros((len(valid),1));model=DummyClassifier(strategy='prior')
                        weights=np.where(labels==1,candidate['factor'],1.).astype(float);weights/=weights.mean()
                        model.fit(Xt,labels,sample_weight=weights);scores=model.predict_proba(Xv)[:,list(model.classes_).index(1)]
                        if number:
                            ni+=1;np.testing.assert_allclose(scores,np.asarray(candidate['inner_scores'])[va],atol=1e-12,rtol=0)
                        else:
                            no+=1
                            for policy,choice in record['choices'].items():
                                if choice['candidate_index']!=index:continue
                                predictions=result[(result.input_set=='boruta23')&(result['repeat']==rep)&(result.fold==fold)&(result.augmentation==policy)].set_index('student_index').loc[test+1]
                                np.testing.assert_allclose(scores,predictions.warning_score,atol=1e-12,rtol=0)
                                assert np.allclose(predictions.threshold,choice['threshold'])
                outer_rows.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                print(f'Verified repeat {rep}, fold {fold}: decisions, contexts, generation and selected model refits',flush=True)
    pd.testing.assert_frame_equal(pd.DataFrame(outer_rows),pd.read_csv(out/'outer-folds.csv'))
    pd.testing.assert_frame_equal(pd.DataFrame(outer_rows),pd.read_csv(ref/'outer-folds.csv'))
    order=['repeat','fold','inner_fold','student_index'];actual=pd.DataFrame(inner_rows).sort_values(order).reset_index(drop=True)
    saved=pd.read_csv(out/'inner-folds.csv');pd.testing.assert_frame_equal(actual,saved[list(actual)].sort_values(order).reset_index(drop=True))
    old_inner=pd.read_csv(ref/'inner-folds.csv');old_inner=old_inner[old_inner.input_set=='small_b']
    pd.testing.assert_frame_equal(actual,old_inner.sort_values(order).reset_index(drop=True))
    old=pd.read_csv(ref/'held-out-predictions.csv');old=old[(old.input_set=='small_b')&(old.model=='forest')&(old.augmentation=='inner_selected_ratio')]
    key=['repeat','fold','student_index'];cols=key+['actual_class','actual_score','warning_score','threshold','predicted_class']
    pd.testing.assert_frame_equal(result[result.input_set=='current8_control'][cols].sort_values(key).reset_index(drop=True),old[cols].sort_values(key).reset_index(drop=True))
    metrics=pd.read_csv(out/'repeat-metrics.csv')
    for row in metrics.itertuples():
        g=result[(result.input_set==row.variant)&(result.augmentation==row.policy)&(result['repeat']==row.repeat)]
        assert len(g)==97 and g.student_index.nunique()==97
        observed=checks.measurements(g.actual_class,g.predicted_class)
        observed.update(average_precision=augmentation.average_precision_score(g.actual_class,g.warning_score),roc_auc=augmentation.roc_auc_score(g.actual_class,g.warning_score))
        assert all(np.isclose(getattr(row,k),v,atol=1e-12,rtol=0) for k,v in observed.items())
    summary=metrics.groupby(['variant','policy']).mean(numeric_only=True).drop(columns='repeat')
    pd.testing.assert_frame_equal(summary,pd.read_csv(out/'metrics-summary.csv').set_index(['variant','policy']))
    for row in pd.read_csv(out/'paired-comparisons.csv').itertuples():
        new=metrics[(metrics.variant=='boruta23')&(metrics.policy==row.policy)&(metrics['repeat']==row.repeat)].iloc[0]
        old=metrics[(metrics.variant=='current8_control')&(metrics['repeat']==row.repeat)].iloc[0]
        assert all(np.isclose(getattr(row,k),new[k]-old[k],atol=1e-12,rtol=0) for k in ['recall','precision','f2','tp','fp'])
    assert all(training.sha256(ROOT/p)==h for p,h in manifest['source_sha256'].items())
    verification={'status':'passed','prediction_rows':len(result),'threshold_candidates_checked':thresholds_checked,
        'choices_checked':50,'contexts_checked':125,'selected_inner_refits':ni,'selected_outer_refits':no,
        'selector_refits':selector_refits,'reference_scores_and_folds_verified':True,'sources_unchanged':True,
        'verification_script_sha256':training.sha256(__file__),
        'checks_helper_sha256':training.sha256(checks.__file__),
        'scope':'All candidate decision arithmetic, saved selector group mappings, contexts, generation/provenance, metrics and selected prediction-model refits checked. Boruta itself replayed for two predeclared first-group contexts only; unselected forests not refitted. No independent cohort.'}
    (out/'verification.json').write_text(json.dumps(verification,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(verification,indent=2),flush=True)


if __name__=='__main__':main()
