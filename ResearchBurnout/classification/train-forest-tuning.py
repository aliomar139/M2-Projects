"""Focused RF search comparing F2 and minimum-FP subject to inner recall >=.85."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('augmentation', Path(__file__).with_name('train-augmentation.py'))
augmentation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(augmentation)
binary, training = augmentation.binary, augmentation.training
METHODS = ['expanded_f2', 'recall85_min_fp']


def threshold_key(t, method):
    if method == 'expanded_f2':
        return t['f2'], t['precision'], t['recall'], t['threshold']
    assert method == 'recall85_min_fp'
    return -t['fp'], t['recall'], t['precision'], t['f2'], t['threshold']


def choose(candidates, method, minimum_recall):
    options = []
    for number, candidate in enumerate(candidates):
        eligible = [t for t in candidate['threshold_candidates']
                    if method == 'expanded_f2' or t['recall'] >= minimum_recall]
        assert eligible, 'Threshold zero must permit the inner recall target'
        t = max(eligible, key=lambda row: threshold_key(row, method))
        options.append({'candidate_index': number, 'ratio': candidate['ratio'], 'factor': candidate['factor'],
                        'parameters': candidate['parameters'], 'chosen_threshold': t})
    return max(options, key=lambda c: (*threshold_key(c['chosen_threshold'], method), -c['ratio']))


def run_job(args):
    config, base, generator, data, rep, fold, train, test, expected_profiles, previous_choice = args
    with threadpool_limits(limits=1):
        cols = base['input_sets'][config['input_set']]
        assert len(cols) == 8 and not any(c.startswith('BAT') or 'burnout' in c for c in cols)
        X = data[cols].iloc[train]
        y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed']+rep*100+fold
        inner = list(StratifiedKFold(4, shuffle=True, random_state=seed).split(train, y))
        pools, profiles, counts, assignments = [], [], [], []
        for number, (tr, va) in enumerate(inner+[(np.arange(len(train)), np.array([], dtype=int))], 1):
            number = number if number <= 4 else 0
            assert not set(tr) & set(va)
            generated, provenance, stats = augmentation.pool(X.iloc[tr], y[tr], base, generator,
                generator['seed']+rep*10000+fold*100+number)
            context = {'input_set': config['input_set'], 'repeat': rep, 'fold': fold, 'inner_fold': number}
            actual = pd.DataFrame([{**context, **r} for r in provenance])
            expected = expected_profiles[expected_profiles.inner_fold == number]
            pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected[list(actual)].reset_index(drop=True))
            profiles.extend(actual.to_dict('records')); counts.append({**context, **stats})
            if number:
                pools.append((tr, va, generated))
                assignments.extend({**context, 'student_index': int(train[i]+1)} for i in va)
            else:
                outer_generated = generated
        thresholds = [round(float(t), 3) for t in np.arange(0, 1+config['threshold_step']/2, config['threshold_step'])]
        assert thresholds[0] == 0 and thresholds[-1] == 1
        candidates = []
        for ratio in config['ratios']:
            parts = [(va, *augmentation.prepare(X.iloc[tr], y[tr], X.iloc[va], generated, ratio, base)[:3])
                     for tr, va, generated in pools]
            for factor in config['relative_high_weights']:
                for params in ParameterGrid(config['grid']):
                    oof, seen = np.full(len(y), np.nan), np.zeros(len(y), dtype=int)
                    for va, Xt, Xv, labels in parts:
                        model = binary.classifier('forest', params, seed).fit(Xt, labels,
                            sample_weight=augmentation.priority.weights(labels, factor, 1))
                        oof[va] = binary.probabilities(model, Xv); seen[va] += 1
                    assert np.isfinite(oof).all() and np.all(seen == 1)
                    candidates.append({'ratio': ratio, 'factor': factor, 'parameters': params,
                        'oof_scores': oof.tolist(), 'threshold_candidates': [
                            {'threshold': t, **binary.metrics(y, oof >= t)} for t in thresholds]})
        assert len(candidates) == 108
        selected = {method: choose(candidates, method, config['minimum_inner_recall']) for method in METHODS}
        assert selected['expanded_f2']['chosen_threshold']['f2'] >= previous_choice['chosen']['chosen_threshold']['f2']-1e-12
        assert selected['recall85_min_fp']['chosen_threshold']['recall'] >= config['minimum_inner_recall']
        predictions, fit_cache = [], {}
        for method, choice in selected.items():
            candidate_index = choice['candidate_index']
            if candidate_index not in fit_cache:
                Xt, Xtest, labels, added = augmentation.prepare(X, y, data[cols].iloc[test], outer_generated, choice['ratio'], base)
                model = binary.classifier('forest', choice['parameters'], seed).fit(Xt, labels,
                    sample_weight=augmentation.priority.weights(labels, choice['factor'], 1))
                fit_cache[candidate_index] = binary.probabilities(model, Xtest), added
            scores, choice['added'] = fit_cache[candidate_index]
            for idx, score in zip(test, scores):
                threshold = choice['chosen_threshold']['threshold']
                predictions.append({'input_set': config['input_set'], 'model': 'forest', 'augmentation': method,
                    'repeat': rep, 'fold': fold, 'student_index': int(idx+1), 'actual_score': float(data.burnout_score.iloc[idx]),
                    'actual_class': int(data.burnout_score.iloc[idx] >= 4), 'warning_score': float(score),
                    'threshold': threshold, 'predicted_class': int(score >= threshold)})
        tuning = {'repeat': rep, 'fold': fold, 'inner_student_indices': (train+1).tolist(),
                  'chosen': selected, 'candidates': candidates}
        return predictions, tuning, profiles, counts, assignments


def main():
    config_path = ROOT/'classification/forest-tuning-config.json'
    config = json.loads(config_path.read_text()); ref = ROOT/config['reference_run']
    ref_manifest = json.loads((ref/'manifest.json').read_text()); assert ref_manifest['status'] == 'complete'
    assert training.sha256(augmentation.__file__) == ref_manifest['script_sha256']
    base = json.loads((ref/'reference-config.json').read_text())
    generator = json.loads((ref/'config.json').read_text())['generator']
    modules = [augmentation, binary, binary.ensemble, training, augmentation.kernels, augmentation.priority]
    helpers = {Path(m.__file__).name: training.sha256(m.__file__) for m in modules}
    for name, digest in ref_manifest['helper_sha256'].items(): assert helpers[name] == digest
    packages = {p: version(p) for p in ref_manifest['packages']}; assert packages == ref_manifest['packages']
    assert all(training.sha256(ROOT/p) == digest for p, digest in ref_manifest['source_sha256'].items())
    data = training.load_data(base); y = (data.burnout_score.to_numpy() >= 4).astype(int)
    assert len(data) == 97 and np.bincount(y).tolist() == [80, 17]
    old_profiles = pd.read_csv(ref/'synthetic-profiles.csv'); old_profiles = old_profiles[old_profiles.input_set == config['input_set']]
    old_tuning = json.loads((ref/'tuning.json').read_text())
    source_paths = [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    source_paths += [ref/name for name in ['manifest.json', 'config.json', 'binary-config.json', 'reference-config.json',
        'held-out-predictions.csv', 'outer-folds.csv', 'inner-folds.csv', 'tuning.json', 'synthetic-profiles.csv']]
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in source_paths}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'); out.mkdir(parents=True, exist_ok=False)
    for name, value in [('config', config), ('reference-config', base), ('generator-config', generator)]:
        (out/f'{name}.json').write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'config_sha256': training.sha256(config_path),
        'helper_sha256': helpers, 'source_sha256': hashes, 'packages': packages}
    manifest_path = out/'manifest.json'; manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    try:
        jobs, folds = [], []
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(StratifiedKFold(5, shuffle=True, random_state=seed).split(data, y), 1):
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1), 'actual_class': int(y[i])} for i in test)
                expected = old_profiles[(old_profiles['repeat'] == rep) & (old_profiles.fold == fold)]
                previous = next(r for r in old_tuning if r['input_set'] == config['input_set'] and r['model'] == 'forest'
                    and r['augmentation'] == 'inner_selected_ratio' and r['repeat'] == rep and r['fold'] == fold)
                jobs.append((config, base, generator, data, rep, fold, train, test, expected, previous))
        fold_table = pd.DataFrame(folds); order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(ref/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        predictions, tuning, profiles, counts, assignments = [], [], [], [], []
        with ProcessPoolExecutor(max_workers=config['workers']) as executor:
            futures = [executor.submit(run_job, job) for job in jobs]
            for count, future in enumerate(as_completed(futures), 1):
                p, t, s, c, a = future.result()
                predictions.extend(p); tuning.append(t); profiles.extend(s); counts.extend(c); assignments.extend(a)
                print(f'Completed {count}/25: expanded F2 and recall-constrained RF selection', flush=True)
        inner = pd.DataFrame(assignments); expected = pd.read_csv(ref/'inner-folds.csv')
        expected = expected[expected.input_set == config['input_set']]; order = ['repeat', 'fold', 'inner_fold', 'student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True)[list(expected)], expected.sort_values(order).reset_index(drop=True))
        old = pd.read_csv(ref/'held-out-predictions.csv')
        selected = old[((old.input_set == config['input_set']) & (old.model == 'forest') & old.augmentation.isin(['real_only', 'inner_selected_ratio'])) |
            ((old.model == 'ridge_svr_blend') & (old.augmentation == 'reference_inner_f2_threshold'))]
        result = pd.concat([pd.DataFrame(predictions), selected], ignore_index=True)
        assert len(result) == 2425 and len(tuning) == 25 and len(counts) == 125
        assert not result.duplicated(['input_set', 'model', 'augmentation', 'repeat', 'student_index']).any()
        assert np.array_equal(result.actual_class, (result.actual_score >= 4).astype(int))
        assert np.array_equal(result.predicted_class, (result.warning_score >= result.threshold).astype(int))
        assert np.allclose(result.actual_score, data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.sort_values(['augmentation', 'repeat', 'student_index']).to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False); inner.to_csv(out/'inner-folds.csv', index=False)
        pd.DataFrame(profiles).to_csv(out/'synthetic-profiles.csv', index=False)
        pd.DataFrame(counts).to_csv(out/'generation-counts.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        augmentation.report(result, out)
        repeats = pd.read_csv(out/'repeat-metrics.csv'); comparisons = []
        for row in repeats[repeats.augmentation.isin(METHODS)].itertuples():
            for other in repeats[(repeats['repeat'] == row.repeat) & ~repeats.augmentation.isin(METHODS)].itertuples():
                comparisons.append({'repeat': row.repeat, 'procedure': row.augmentation, 'reference': other.augmentation,
                    'f2_difference': row.f2-other.f2, 'recall_difference': row.recall-other.recall,
                    'precision_difference': row.precision-other.precision, 'false_warnings_difference': row.fp-other.fp})
        pd.DataFrame(comparisons).to_csv(out/'paired-comparisons.csv', index=False)
        summary = pd.read_csv(out/'metrics-summary.csv')
        lines = ['# Focused Small B Random Forest tuning', '',
            '97 real students: High >=4 (17), Below-high <4 (80). Only real held-out students evaluate.',
            'Identical 5x5 stratified outer / 4 inner folds and exactly reproduced synthetic training pools from the retained reference.',
            '108 model/weight/augmentation candidates per outer training group; 41 thresholds per candidate. RF has 100 trees and one computational thread.',
            'Depths 2/3/5, minimum leaf 5/10, max_features sqrt/1.0; High weights 1/2/4; augmentation none/half/full.',
            'expanded_f2 selects by inner F2/precision/recall/higher threshold/less augmentation, then stable grid order.',
            'recall85_min_fp requires inner recall >=.85, then selects fewer FP, higher recall/precision/F2/threshold and less augmentation.',
            'Both rules jointly select parameters, High weight, augmentation and threshold from the same inner candidates. No outer outcomes select settings.',
            'The inner recall constraint is not a guarantee about real excluded students; with 13 inner-OOF positives it requires 12/13, and with 14 it requires 12/14.', '',
            '| Procedure | Recall | Precision | F2 | Detected /17 | False warnings /80 | Average precision |',
            '|---|---:|---:|---:|---:|---:|---:|']
        for row in summary.itertuples():
            lines.append(f'| {row.augmentation} | {row.recall:.1%} | {row.precision:.1%} | {row.f2:.3f} | {row.tp:.1f} | {row.fp:.1f} | {row.average_precision:.3f} |')
        lines += ['', 'Means average five dependent repetitions of the same students; threshold changes are warning trade-offs, not improved numerical score MAE.',
            'Synthetic High labels are assumptions. Weighted classifier outputs are uncalibrated; repeated model exploration remains exploratory.',
            'Original source SAV/CSV, SPSS work and previous result folders are unchanged. No independent evaluation cohort, separate software test suite or deployment model.']
        (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
        assert all(training.sha256(ROOT/p) == digest for p, digest in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, reference_folds_reproduced=True,
            reference_synthetic_pools_reproduced=125, real_participants=97, deployment_model_saved=False)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc)); raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
