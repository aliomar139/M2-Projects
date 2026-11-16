"""Train-only selection of whole existing questions for the current RF recipe."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('augmentation', Path(__file__).with_name('train-augmentation.py'))
augmentation = importlib.util.module_from_spec(spec); spec.loader.exec_module(augmentation)
spec = importlib.util.spec_from_file_location('selection', ROOT/'analysis/scripts/train-feature-selection.py')
selection = importlib.util.module_from_spec(spec); spec.loader.exec_module(selection)
binary, training = augmentation.binary, augmentation.training


def ranked_questions(config, base, cols, X, y):
    Xt, _, groups = selection.encode(base, cols, X, X)
    model = LogisticRegression(C=config['selector_C'], max_iter=10000, solver='lbfgs').fit(Xt, y)
    strength = {col: float(np.linalg.norm(model.coef_[0, groups == col])/np.sqrt(sum(groups == col))) for col in cols}
    ranking = sorted(cols, key=lambda col: -strength[col])
    assert set(ranking) == set(cols) and all(np.isfinite(list(strength.values())))
    return ranking, strength


def choose(candidates, guard, minimum_recall):
    eligible = [r for r in candidates if not guard or r['recall'] >= minimum_recall]
    assert eligible
    if guard:
        return max(eligible, key=lambda r: (-r['fp'], r['recall'], r['precision'], r['f2'], r['threshold'], -r['question_count']))
    return max(eligible, key=lambda r: (r['f2'], r['precision'], r['recall'], r['threshold'], -r['question_count']))


def run_job(args):
    config, base, generator, thresholds, data, rep, fold, train, test, previous, expected = args
    with threadpool_limits(limits=1):
        warnings.filterwarnings('error', category=ConvergenceWarning)
        cols = base['input_sets'][config['input_set']]; X = data[cols].iloc[train]
        y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed']+rep*100+fold
        inner = list(StratifiedKFold(4, shuffle=True, random_state=seed).split(train, y))
        choice = previous['chosen']; oof = {n: np.full(len(y), np.nan) for n in config['question_counts']}
        rankings, assignments = [], []
        for number, (tr, va) in enumerate(inner+[(np.arange(len(train)), np.array([], dtype=int))], 1):
            number = number if number <= 4 else 0
            assert not set(tr) & set(va)
            ranking, strength = ranked_questions(config, base, cols, X.iloc[tr], y[tr])
            generated, _, _ = augmentation.pool(X.iloc[tr], y[tr], base, generator,
                generator['seed']+rep*10000+fold*100+number)
            added = min(len(generated), int(np.ceil(sum(y[tr])*previous['selected_ratio'])))
            augmented = pd.concat([X.iloc[tr], generated.iloc[:added]], ignore_index=True)
            labels = np.concatenate([y[tr], np.ones(added, dtype=int)])
            valid = X.iloc[va] if number else data[cols].iloc[test]
            Xt, Xv, groups = selection.encode(base, cols, augmented, valid)
            weights = augmentation.priority.weights(labels, choice['factor'], 1)
            rankings.append({'repeat':rep, 'fold':fold, 'inner_fold':number, 'real_training_ids':(train[tr]+1).tolist(),
                'ranking':ranking, 'strength':strength, 'synthetic_added':added})
            for n in config['question_counts']:
                mask = np.isin(groups, ranking[:n]); assert mask.any()
                model = binary.classifier('forest', choice['parameters'], seed).fit(Xt[:,mask], labels, sample_weight=weights)
                scores = binary.probabilities(model, Xv[:,mask])
                if number: oof[n][va] = scores
                elif n == 4: outer = {n:scores}
                else: outer[n] = scores
            if number:
                assignments.extend({'input_set':config['input_set'],'repeat':rep,'fold':fold,'inner_fold':number,
                    'student_index':int(train[i]+1)} for i in va)
        assert all(np.isfinite(scores).all() for scores in oof.values())
        observed = binary.metrics(y, oof[8] >= choice['chosen_threshold']['threshold'])
        assert all(np.isclose(observed[k], choice['chosen_threshold'][k],atol=1e-12,rtol=0) for k in observed)
        np.testing.assert_allclose(outer[8], expected.set_index('student_index').loc[test+1].warning_score,atol=1e-12,rtol=0)
        candidates = [{'question_count':n,'threshold':t, **binary.metrics(y,scores >= t)}
                      for n,scores in oof.items() for t in thresholds]
        minimum_recall = choice['chosen_threshold']['recall']
        choices = {'subset_f2':choose(candidates,False,minimum_recall),
                   'subset_recall_guard':choose(candidates,True,minimum_recall),
                   'full8_control':choose([r for r in candidates if r['question_count']==8],False,minimum_recall)}
        assert choices['full8_control']['threshold'] == choice['chosen_threshold']['threshold']
        assert choices['subset_f2']['f2'] >= choice['chosen_threshold']['f2']-1e-12
        assert choices['subset_recall_guard']['fp'] <= choice['chosen_threshold']['fp']
        predictions = []
        for method, selected in choices.items():
            for idx,score in zip(test,outer[selected['question_count']]):
                predictions.append({'input_set':config['input_set'],'model':'forest_question_selection','augmentation':method,
                    'repeat':rep,'fold':fold,'student_index':int(idx+1),'actual_class':int(data.burnout_score.iloc[idx]>=4),
                    'actual_score':float(data.burnout_score.iloc[idx]),'warning_score':float(score),
                    'threshold':selected['threshold'],'predicted_class':int(score>=selected['threshold'])})
        tuning = {'repeat':rep,'fold':fold,'inner_student_indices':(train+1).tolist(),'rf_recipe':previous,
            'inner_minimum_recall':minimum_recall,'oof_scores':{str(n):v.tolist() for n,v in oof.items()},
            'choices':choices,'candidates':candidates}
        return predictions,tuning,rankings,assignments


def main():
    config_path = ROOT/'classification/question-selection-config.json'; config = json.loads(config_path.read_text())
    ref = ROOT/config['reference_run']; manifest_ref = json.loads((ref/'manifest.json').read_text()); assert manifest_ref['status']=='complete'
    assert training.sha256(augmentation.__file__) == manifest_ref['script_sha256']
    base = json.loads((ref/'reference-config.json').read_text()); source_config = json.loads((ref/'config.json').read_text())
    binary_config = json.loads((ref/'binary-config.json').read_text())
    data = training.load_data(base); y = (data.burnout_score.to_numpy()>=4).astype(int)
    assert len(data)==97 and np.bincount(y).tolist()==[80,17]
    modules = [augmentation,binary,binary.ensemble,training,augmentation.kernels,augmentation.priority,selection]
    helpers = {Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    for name,digest in manifest_ref['helper_sha256'].items(): assert helpers[name]==digest
    packages = {p:version(p) for p in manifest_ref['packages']}; assert packages==manifest_ref['packages']
    assert all(training.sha256(ROOT/p)==h for p,h in manifest_ref['source_sha256'].items())
    predictions_ref = pd.read_csv(ref/'held-out-predictions.csv')
    current = predictions_ref[(predictions_ref.input_set=='small_b')&(predictions_ref.model=='forest')&(predictions_ref.augmentation=='inner_selected_ratio')]
    tuning_ref = json.loads((ref/'tuning.json').read_text())
    paths = [ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','binary-config.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv']]
    hashes = {str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',config),('reference-config',base),('generator-config',source_config['generator'])]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest = {'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':training.sha256(__file__),
        'config_sha256':training.sha256(config_path),'helper_sha256':helpers,'source_sha256':hashes,'packages':packages}
    manifest_path=out/'manifest.json';manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    try:
        jobs,folds=[],[]
        for rep,seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                assert not set(train)&set(test)
                folds.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                previous=next(r for r in tuning_ref if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                expected=current[(current['repeat']==rep)&(current.fold==fold)]
                jobs.append((config,base,source_config['generator'],binary_config['probability_thresholds'],data,rep,fold,train,test,previous,expected))
        fold_table=pd.DataFrame(folds);pd.testing.assert_frame_equal(fold_table,pd.read_csv(ref/'outer-folds.csv'))
        predictions,tuning,rankings,assignments=[],[],[],[]
        with ProcessPoolExecutor(max_workers=config['workers']) as executor:
            for count,(p,t,r,a) in enumerate(executor.map(run_job,jobs),1):
                predictions.extend(p);tuning.append(t);rankings.extend(r);assignments.extend(a)
                print(f'Completed {count}/25: training-only 4/6/8 question selection',flush=True)
        inner=pd.DataFrame(assignments);expected=pd.read_csv(ref/'inner-folds.csv');expected=expected[expected.input_set=='small_b'];order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True)[list(expected)],expected.sort_values(order).reset_index(drop=True))
        result=pd.concat([pd.DataFrame(predictions),current],ignore_index=True)
        assert len(result)==1940 and len(tuning)==25 and len(rankings)==125
        assert not result.duplicated(['augmentation','repeat','student_index']).any()
        assert np.array_equal(result.actual_class,(result.actual_score>=4).astype(int))
        assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
        assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv',index=False);fold_table.to_csv(out/'outer-folds.csv',index=False);inner.to_csv(out/'inner-folds.csv',index=False)
        (out/'tuning.json').write_text(json.dumps(tuning,indent=2),encoding='utf-8');(out/'rankings.json').write_text(json.dumps(rankings,indent=2),encoding='utf-8')
        rows=[];keys=['input_set','model','augmentation','repeat']
        for key,g in result.groupby(keys):
            assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
            rows.append(dict(zip(keys,key),**binary.metrics(g.actual_class,g.predicted_class),
                average_precision=float(augmentation.average_precision_score(g.actual_class,g.warning_score)),roc_auc=float(augmentation.roc_auc_score(g.actual_class,g.warning_score))))
        repeats=pd.DataFrame(rows);repeats.to_csv(out/'repeat-metrics.csv',index=False)
        summary=repeats.groupby(keys[:3]).mean(numeric_only=True).drop(columns='repeat');summary.to_csv(out/'metrics-summary.csv')
        repeats[keys+['tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
        changes=[];features=[]
        for r in repeats[repeats.augmentation.isin(['subset_f2','subset_recall_guard'])].itertuples():
            previous=repeats[(repeats['repeat']==r.repeat)&(repeats.augmentation=='inner_selected_ratio')].iloc[0]
            changes.append({'repeat':r.repeat,'procedure':r.augmentation,'f2_difference':r.f2-previous.f2,
                'recall_difference':r.recall-previous.recall,'precision_difference':r.precision-previous.precision,'false_warnings_difference':r.fp-previous.fp})
        for r in tuning:
            outer_rank=next(q for q in rankings if q['repeat']==r['repeat'] and q['fold']==r['fold'] and q['inner_fold']==0)
            for method,chosen in r['choices'].items():
                features.extend({'repeat':r['repeat'],'fold':r['fold'],'procedure':method,'question_count':chosen['question_count'],'question':col}
                    for col in outer_rank['ranking'][:chosen['question_count']])
        pd.DataFrame(changes).to_csv(out/'paired-comparisons.csv',index=False)
        pd.DataFrame(features).to_csv(out/'selected-questions.csv',index=False)
        lines=['# Current Random Forest: training-only question selection','',
            '97 real students; primary score >=4 (17 High) versus <4 (80 Below-high). Only real held-out students evaluate.',
            'Original 5x5 stratified outer / 4 inner folds. Current RF settings, High weights and augmentation ratios are frozen from each outer training group.',
            'Unweighted L2 logistic C=1 ranks grouped standardized coefficients on real training students only; ranking refits inside every inner training group.',
            'Compare 4/6/8 whole questions with the original .05-step warning thresholds. No question is globally chosen from prior error inspection.',
            'subset_f2 maximizes inner F2/precision/recall/threshold, then fewer questions. subset_recall_guard requires current RF inner recall and minimizes FP.',
            'Inner recall guards are not outer guarantees. Existing RF recipe selection and subset selection reuse inner folds; outer students remain excluded.',
            'Original full-eight synthetic pools are projected onto subsets; projected duplicates can occur. No new survey inputs or independent students.',
            'full8_control must reproduce the current RF scores, inner metrics and threshold. This tests question selection conditional on the existing RF recipe, not all possible subsets/settings.','',
            '| Procedure | Recall | Precision | F2 | Detected /17 | False warnings /80 | Average precision |',
            '|---|---:|---:|---:|---:|---:|---:|']
        for (_,_,method),r in summary.iterrows():lines.append(f'| {method} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.3f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.3f} |')
        lines+=['','Counts average five dependent repetitions, not independent cohorts. The logistic selector can miss nonlinear relevance; this is one specified selection method.',
            'Error inspection on the same 97 students motivated the experiment. Any gain remains exploratory and needs independent confirmation.',
            'Source SAV/CSV, prior outputs and selected models are unchanged. No deployment model, calibrated clinical probabilities or regression MAE improvement.']
        (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,full8_reference_reproduced=True,real_participants=97,deployment_model_saved=False)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Complete: {out}',flush=True)


if __name__=='__main__':main()
