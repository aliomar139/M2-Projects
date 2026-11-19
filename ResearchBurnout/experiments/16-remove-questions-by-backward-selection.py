"""Greedy backward whole-question selection with real-only nested evaluation."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('questions', Path(__file__).with_name('15-select-four-six-or-eight-questions.py'))
questions = importlib.util.module_from_spec(spec); spec.loader.exec_module(questions)
augmentation, selection, binary, training = questions.augmentation, questions.selection, questions.binary, questions.training
METHODS = ['backward_f2', 'backward_recall_guard']


def metric_key(t, guard):
    if guard: return -t['fp'], t['recall'], t['precision'], t['f2'], t['threshold']
    return t['f2'], t['precision'], t['recall'], t['threshold']


def run_job(args):
    config, base, generator, thresholds, data, rep, fold, train, test, previous, expected = args
    with threadpool_limits(limits=1):
        cols = base['input_sets'][config['input_set']]; assert len(cols) == 8
        X = data[cols].iloc[train]; y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed']+rep*100+fold
        inner = list(StratifiedKFold(4,shuffle=True,random_state=seed).split(train,y))
        recipe = previous['chosen']; ratio = previous['selected_ratio']
        parts, assignments, generation = [], [], []
        for number,(tr,va) in enumerate(inner,1):
            assert not set(tr)&set(va)
            gen,_,stats = augmentation.pool(X.iloc[tr],y[tr],base,generator,generator['seed']+rep*10000+fold*100+number)
            added = min(len(gen),int(np.ceil(sum(y[tr])*ratio)))
            combined = pd.concat([X.iloc[tr],gen.iloc[:added]],ignore_index=True)
            labels = np.concatenate([y[tr],np.ones(added,dtype=int)])
            Xt,Xv,groups = selection.encode(base,cols,combined,X.iloc[va])
            parts.append((va,Xt,Xv,groups,labels))
            generation.append({'repeat':rep,'fold':fold,'inner_fold':number,**stats,'added':added})
            assignments.extend({'input_set':config['input_set'],'repeat':rep,'fold':fold,'inner_fold':number,
                'student_index':int(train[i]+1)} for i in va)
        candidates, cache = [], {}
        def evaluate(subset):
            key = tuple(subset)
            if key in cache: return cache[key]
            scores, seen = np.full(len(y),np.nan),np.zeros(len(y),dtype=int)
            for va,Xt,Xv,groups,labels in parts:
                mask = np.isin(groups,subset)
                assert mask.any()
                model = binary.classifier('forest',recipe['parameters'],seed).fit(Xt[:,mask],labels,
                    sample_weight=augmentation.priority.weights(labels,recipe['factor'],1))
                scores[va] = binary.probabilities(model,Xv[:,mask]); seen[va] += 1
            assert np.isfinite(scores).all() and np.all(seen == 1)
            candidate = {'candidate_id':len(candidates),'questions':list(subset),'oof_scores':scores.tolist(),
                'threshold_candidates':[{'threshold':t,**binary.metrics(y,scores >= t)} for t in thresholds]}
            candidates.append(candidate); cache[key] = candidate
            return candidate
        minimum_recall = recipe['chosen_threshold']['recall']
        def best_threshold(candidate,guard):
            eligible = [t for t in candidate['threshold_candidates'] if not guard or t['recall'] >= minimum_recall]
            assert eligible
            return max(eligible,key=lambda t:metric_key(t,guard))
        full = evaluate(cols)
        observed = next(t for t in full['threshold_candidates'] if t['threshold'] == recipe['chosen_threshold']['threshold'])
        assert all(np.isclose(observed[k],recipe['chosen_threshold'][k],atol=1e-12,rtol=0) for k in observed)
        assert best_threshold(full,False) == observed
        paths,choices = {},{}
        for method in METHODS:
            guard = method.endswith('guard'); current = full; chosen = best_threshold(current,guard); steps = []
            while len(current['questions']) > config['minimum_questions']:
                removals = []
                for col in current['questions']:
                    child = evaluate([c for c in current['questions'] if c != col])
                    removals.append({'removed_question':col,'candidate_id':child['candidate_id'],
                                     'chosen_threshold':best_threshold(child,guard)})
                best = max(removals,key=lambda r:metric_key(r['chosen_threshold'],guard))
                improved = best['chosen_threshold']['fp'] < chosen['fp'] if guard else best['chosen_threshold']['f2'] > chosen['f2']+1e-12
                steps.append({'parent_id':current['candidate_id'],'parent_threshold':chosen,'removals':removals,
                    'best_removal':best,'accepted':bool(improved)})
                if not improved: break
                current = candidates[best['candidate_id']]; chosen = best['chosen_threshold']
            paths[method] = steps
            choices[method] = {'candidate_id':current['candidate_id'],'questions':current['questions'],'chosen_threshold':chosen}
        choices['full8_control'] = {'candidate_id':full['candidate_id'],'questions':cols,'chosen_threshold':observed}
        assert choices['backward_f2']['chosen_threshold']['f2'] >= observed['f2']-1e-12
        assert choices['backward_recall_guard']['chosen_threshold']['recall'] >= minimum_recall
        assert choices['backward_recall_guard']['chosen_threshold']['fp'] <= observed['fp']
        gen,_,stats = augmentation.pool(X,y,base,generator,generator['seed']+rep*10000+fold*100)
        added = min(len(gen),int(np.ceil(sum(y)*ratio)))
        generation.append({'repeat':rep,'fold':fold,'inner_fold':0,**stats,'added':added})
        combined = pd.concat([X,gen.iloc[:added]],ignore_index=True); labels = np.concatenate([y,np.ones(added,dtype=int)])
        Xt,Xv,groups = selection.encode(base,cols,combined,data[cols].iloc[test])
        predictions, outer_cache = [],{}
        for method,choice in choices.items():
            candidate_id = choice['candidate_id']
            if candidate_id not in outer_cache:
                mask = np.isin(groups,choice['questions'])
                model = binary.classifier('forest',recipe['parameters'],seed).fit(Xt[:,mask],labels,
                    sample_weight=augmentation.priority.weights(labels,recipe['factor'],1))
                outer_cache[candidate_id] = binary.probabilities(model,Xv[:,mask])
            scores = outer_cache[candidate_id]
            if method == 'full8_control':
                np.testing.assert_allclose(scores,expected.set_index('student_index').loc[test+1].warning_score,atol=1e-12,rtol=0)
            for idx,score in zip(test,scores):
                threshold = choice['chosen_threshold']['threshold']
                predictions.append({'input_set':config['input_set'],'model':'forest_backward_selection','augmentation':method,
                    'repeat':rep,'fold':fold,'student_index':int(idx+1),'actual_class':int(data.burnout_score.iloc[idx] >= 4),
                    'actual_score':float(data.burnout_score.iloc[idx]),'warning_score':float(score),
                    'threshold':threshold,'predicted_class':int(score >= threshold)})
        return predictions,{'repeat':rep,'fold':fold,'inner_student_indices':(train+1).tolist(),'rf_recipe':previous,
            'inner_minimum_recall':minimum_recall,'paths':paths,'choices':choices,'candidates':candidates},assignments,generation


def main():
    config_path = ROOT/'experiments/16-remove-questions-by-backward-selection-settings.json'; config = json.loads(config_path.read_text())
    ref = ROOT/config['reference_run']; rm = json.loads((ref/'manifest.json').read_text()); assert rm['status'] == 'complete'
    assert training.sha256(augmentation.__file__) == rm['script_sha256']
    modules = [questions,augmentation,binary,binary.ensemble,training,augmentation.kernels,augmentation.priority,selection]
    helpers = {Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    for name,digest in rm['helper_sha256'].items(): assert helpers[name] == digest
    packages = {p:version(p) for p in rm['packages']}; assert packages == rm['packages']
    assert all(training.sha256(ROOT/p) == h for p,h in rm['source_sha256'].items())
    base = json.loads((ref/'reference-config.json').read_text()); aug_config = json.loads((ref/'config.json').read_text())
    thresholds = json.loads((ref/'10-compare-high-burnout-classifiers-settings.json').read_text())['probability_thresholds']
    data = training.load_data(base); y = (data.burnout_score.to_numpy() >= 4).astype(int)
    assert len(data) == 97 and np.bincount(y).tolist() == [80,17]
    old = pd.read_csv(ref/'held-out-predictions.csv'); oldt = json.loads((ref/'tuning.json').read_text())
    current = old[(old.input_set == 'small_b')&(old.model == 'forest')&(old.augmentation == 'inner_selected_ratio')]
    paths = [ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','10-compare-high-burnout-classifiers-settings.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv']]
    hashes = {str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'); out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',config),('reference-config',base),('generator-config',aug_config['generator'])]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest = {'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':training.sha256(__file__),
        'config_sha256':training.sha256(config_path),'helper_sha256':helpers,'source_sha256':hashes,'packages':packages}
    manifest_path = out/'manifest.json'; manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    try:
        jobs,folds = [],[]
        for rep,seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                assert not set(train)&set(test)
                folds.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                previous = next(r for r in oldt if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                jobs.append((config,base,aug_config['generator'],thresholds,data,rep,fold,train,test,previous,current[(current['repeat']==rep)&(current.fold==fold)]))
        fold_table = pd.DataFrame(folds); pd.testing.assert_frame_equal(fold_table,pd.read_csv(ref/'outer-folds.csv'))
        predictions,tuning,assignments,generation = [],[],[],[]
        with ProcessPoolExecutor(max_workers=config['workers']) as executor:
            futures = [executor.submit(run_job,job) for job in jobs]
            for count,future in enumerate(as_completed(futures),1):
                p,t,a,g = future.result(); predictions.extend(p); tuning.append(t); assignments.extend(a); generation.extend(g)
                print(f'Completed {count}/25: backward F2 and recall-guard paths ({len(t["candidates"])} subsets)',flush=True)
        inner = pd.DataFrame(assignments); expected = pd.read_csv(ref/'inner-folds.csv'); expected = expected[expected.input_set=='small_b']; order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True)[list(expected)],expected.sort_values(order).reset_index(drop=True))
        result = pd.concat([pd.DataFrame(predictions),current],ignore_index=True)
        assert len(result)==1940 and len(tuning)==25 and len(generation)==125
        assert not result.duplicated(['augmentation','repeat','student_index']).any()
        assert np.array_equal(result.actual_class,(result.actual_score>=4).astype(int))
        assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
        assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv',index=False); fold_table.to_csv(out/'outer-folds.csv',index=False); inner.to_csv(out/'inner-folds.csv',index=False)
        pd.DataFrame(generation).to_csv(out/'generation-counts.csv',index=False)
        (out/'tuning.json').write_text(json.dumps(tuning,indent=2),encoding='utf-8')
        rows=[]; keys=['input_set','model','augmentation','repeat']
        for key,g in result.groupby(keys):
            assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
            rows.append(dict(zip(keys,key),**binary.metrics(g.actual_class,g.predicted_class),
                average_precision=float(augmentation.average_precision_score(g.actual_class,g.warning_score)),roc_auc=float(augmentation.roc_auc_score(g.actual_class,g.warning_score))))
        repeats=pd.DataFrame(rows); repeats.to_csv(out/'repeat-metrics.csv',index=False)
        summary=repeats.groupby(keys[:3]).mean(numeric_only=True).drop(columns='repeat'); summary.to_csv(out/'metrics-summary.csv')
        repeats[keys+['tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
        changes=[]; features=[]; sizes=[]
        for row in repeats[repeats.augmentation.isin(METHODS)].itertuples():
            refrow=repeats[(repeats['repeat']==row.repeat)&(repeats.augmentation=='inner_selected_ratio')].iloc[0]
            changes.append({'repeat':row.repeat,'procedure':row.augmentation,'f2_difference':row.f2-refrow.f2,
                'recall_difference':row.recall-refrow.recall,'precision_difference':row.precision-refrow.precision,'false_warnings_difference':row.fp-refrow.fp})
        for record in tuning:
            for method,choice in record['choices'].items():
                sizes.append({'repeat':record['repeat'],'fold':record['fold'],'procedure':method,'question_count':len(choice['questions']),
                    'accepted_removals':sum(s['accepted'] for s in record['paths'].get(method,[]))})
                features.extend({'repeat':record['repeat'],'fold':record['fold'],'procedure':method,'question':c} for c in choice['questions'])
        pd.DataFrame(changes).to_csv(out/'paired-comparisons.csv',index=False); pd.DataFrame(features).to_csv(out/'selected-questions.csv',index=False)
        pd.DataFrame(sizes).to_csv(out/'selected-question-counts.csv',index=False)
        lines=['# Current RF: backward whole-question selection','',
            '97 real students; primary score >=4 (17 High) versus <4 (80 Below-high). Only real excluded students evaluate.',
            'Original 5x5 stratified outer / 4 inner folds. Current RF settings, High weight and augmentation ratio remain fixed per outer training group.',
            'Start at eight questions; compare every one-question removal using pooled real inner predictions and original .05-step thresholds.',
            'F2 path accepts only strict F2 improvement >1e-12. Recall-guard path requires current RF inner recall, minimizes FP, and accepts only a strict FP reduction.',
            'Threshold ties use recorded metric order; child ties use original question order. Stop at first lack of strict improvement or one remaining question.',
            'Both greedy paths use training only; no global ranking/removal based on prior error tables. Full-eight control reproduces current RF.',
            'Frozen recipe selection and removal-path selection reuse original inner folds. This is conditional greedy selection, not exhaustive subset/model tuning.',
            'Original full-eight synthetic pools are projected onto subsets; projected duplicates can occur. Inner recall constraints do not guarantee outer recall.','',
            '| Procedure | Recall | Precision | F2 | Detected /17 | False warnings /80 | Average precision |',
            '|---|---:|---:|---:|---:|---:|---:|']
        for (_,_,method),row in summary.iterrows():lines.append(f'| {method} | {row.recall:.1%} | {row.precision:.1%} | {row.f2:.3f} | {row.tp:.1f} | {row.fp:.1f} | {row.average_precision:.3f} |')
        lines+=['',f'Subsets evaluated across all training groups: {sum(len(r["candidates"]) for r in tuning)} (cached within each group across paths).',
            'Counts average five dependent repetitions, not independent cohorts. Synthetic labels are assumptions; scores are uncalibrated.',
            'Original data, SPSS work, earlier results and selected models are unchanged. No deployment model or regression MAE improvement.',
            'Repeated inspection of these 97 students motivated this exploratory experiment; independent confirmation remains absent.']
        (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
        assert all(training.sha256(ROOT/path)==digest for path,digest in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,full8_reference_reproduced=True,
            candidate_subsets=sum(len(r['candidates']) for r in tuning),real_participants=97,deployment_model_saved=False)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc)); raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat(); manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Complete: {out}',flush=True)


if __name__=='__main__':main()
