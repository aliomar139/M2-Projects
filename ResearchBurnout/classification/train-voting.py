"""Current selected RF plus logistic warning scores, with RF-only threshold controls."""
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
spec = importlib.util.spec_from_file_location('augmentation', Path(__file__).with_name('train-augmentation.py'))
augmentation = importlib.util.module_from_spec(spec); spec.loader.exec_module(augmentation)
binary, training = augmentation.binary, augmentation.training
METHODS = ['ensemble_f2', 'ensemble_recall_guard', 'rf_threshold_only_f2', 'rf_threshold_only_guard']


def select(options, method, minimum_recall):
    eligible = [r for r in options if (not method.startswith('rf_threshold_only') or r['rf_share'] == 1)
                and (not method.endswith('guard') or r['recall'] >= minimum_recall)]
    assert eligible
    if method.endswith('guard'):
        return max(eligible, key=lambda r: (-r['fp'], r['recall'], r['precision'], r['f2'], r['threshold'], r['rf_share']))
    return max(eligible, key=lambda r: (r['f2'], r['precision'], r['recall'], r['threshold'], r['rf_share']))


def run_job(args):
    config, base, generator, data, rep, fold, train, test, rf, lr, previous = args
    with threadpool_limits(limits=1):
        cols = base['input_sets'][config['input_set']]
        X = data[cols].iloc[train]; y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed']+rep*100+fold
        inner = list(StratifiedKFold(4, shuffle=True, random_state=seed).split(train, y))
        oof = {family: np.full(len(y), np.nan) for family in ['forest', 'logistic']}
        assignments = []
        for number, (tr, va) in enumerate(inner+[(np.arange(len(train)), np.array([], dtype=int))], 1):
            number = number if number <= 4 else 0
            assert not set(tr) & set(va)
            generated, _, _ = augmentation.pool(X.iloc[tr], y[tr], base, generator,
                generator['seed']+rep*10000+fold*100+number)
            valid = X.iloc[va] if number else data[cols].iloc[test]
            for family, choice, ratio in [('forest', rf['chosen'], rf['selected_ratio']), ('logistic', lr['chosen'], 0)]:
                Xt, Xv, labels, _ = augmentation.prepare(X.iloc[tr], y[tr], valid, generated, ratio, base)
                model = binary.classifier(family, choice['parameters'], seed).fit(Xt, labels,
                    sample_weight=augmentation.priority.weights(labels, choice['factor'], 1))
                scores = binary.probabilities(model, Xv)
                if number: oof[family][va] = scores
                elif family == 'forest': rf_test = scores
                else: lr_test = scores
            if number:
                assignments.extend({'input_set': config['input_set'], 'repeat': rep, 'fold': fold,
                    'inner_fold': number, 'student_index': int(train[i]+1)} for i in va)
        for family, choice, saved, actual in [('forest', rf['chosen'], previous['forest'], rf_test),
                                             ('logistic', lr['chosen'], previous['logistic'], lr_test)]:
            assert np.isfinite(oof[family]).all()
            observed = binary.metrics(y, oof[family] >= choice['chosen_threshold']['threshold'])
            assert all(np.isclose(observed[k], choice['chosen_threshold'][k], atol=1e-12, rtol=0) for k in observed)
            expected = saved.set_index('student_index').loc[test+1]
            np.testing.assert_allclose(actual, expected.warning_score, atol=1e-12, rtol=0)
        thresholds = [round(float(t), 3) for t in np.arange(0, 1+config['threshold_step']/2, config['threshold_step'])]
        options = []
        for share in config['rf_shares']:
            scores = share*oof['forest']+(1-share)*oof['logistic']
            options.extend({'rf_share': share, 'threshold': t, **binary.metrics(y, scores >= t)} for t in thresholds)
        minimum_recall = rf['chosen']['chosen_threshold']['recall']
        choices = {method: select(options, method, minimum_recall) for method in METHODS}
        assert choices['ensemble_f2']['f2'] >= rf['chosen']['chosen_threshold']['f2']-1e-12
        assert choices['ensemble_recall_guard']['fp'] <= rf['chosen']['chosen_threshold']['fp']
        predictions = []
        for method, choice in choices.items():
            scores = choice['rf_share']*rf_test+(1-choice['rf_share'])*lr_test
            for idx, score in zip(test, scores):
                predictions.append({'input_set': config['input_set'], 'model': 'forest_logistic', 'augmentation': method,
                    'repeat': rep, 'fold': fold, 'student_index': int(idx+1), 'actual_class': int(data.burnout_score.iloc[idx] >= 4),
                    'actual_score': float(data.burnout_score.iloc[idx]), 'warning_score': float(score),
                    'threshold': choice['threshold'], 'predicted_class': int(score >= choice['threshold'])})
        return predictions, {'repeat': rep, 'fold': fold, 'inner_student_indices': (train+1).tolist(),
            'rf_choice': rf, 'logistic_choice': lr, 'inner_rf_scores': oof['forest'].tolist(),
            'inner_logistic_scores': oof['logistic'].tolist(), 'inner_minimum_recall': minimum_recall,
            'choices': choices, 'candidates': options}, assignments


def main():
    config_path = ROOT/'classification/voting-config.json'; config = json.loads(config_path.read_text())
    ref = ROOT/config['reference_run']; rm = json.loads((ref/'manifest.json').read_text()); assert rm['status'] == 'complete'
    assert training.sha256(augmentation.__file__) == rm['script_sha256']
    modules = [augmentation, binary, binary.ensemble, training, augmentation.kernels, augmentation.priority]
    helpers = {Path(m.__file__).name: training.sha256(m.__file__) for m in modules}
    for name, digest in rm['helper_sha256'].items(): assert helpers[name] == digest
    packages = {p: version(p) for p in rm['packages']}; assert packages == rm['packages']
    assert all(training.sha256(ROOT/p) == h for p, h in rm['source_sha256'].items())
    base = json.loads((ref/'reference-config.json').read_text()); aug_config = json.loads((ref/'config.json').read_text())
    binary_ref = ROOT/aug_config['reference_run']
    old = pd.read_csv(ref/'held-out-predictions.csv'); oldt = json.loads((ref/'tuning.json').read_text())
    logistic_tuning = json.loads((binary_ref/'tuning.json').read_text())
    data = training.load_data(base); y = (data.burnout_score.to_numpy() >= 4).astype(int)
    assert len(data) == 97 and np.bincount(y).tolist() == [80, 17]
    rf_pred = old[(old.input_set == 'small_b') & (old.model == 'forest') & (old.augmentation == 'inner_selected_ratio')]
    lr_pred = old[(old.input_set == 'small_b') & (old.model == 'logistic') & (old.augmentation == 'real_only')]
    overlap = rf_pred.merge(lr_pred, on=['repeat', 'fold', 'student_index'], suffixes=('_rf', '_lr'), validate='one_to_one')
    assert len(overlap) == 485 and (overlap.actual_class_rf == overlap.actual_class_lr).all()
    overlap_rows = []
    for (rep, actual), g in overlap.groupby(['repeat', 'actual_class_rf']):
        a, b = g.predicted_class_rf != actual, g.predicted_class_lr != actual
        overlap_rows.append({'repeat': rep, 'actual_class': actual, 'both_wrong': int(sum(a & b)),
            'rf_wrong_logistic_right': int(sum(a & ~b)), 'rf_right_logistic_wrong': int(sum(~a & b)), 'both_right': int(sum(~a & ~b))})
    paths = [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv'], binary_ref/'tuning.json']
    paths += [ref/name for name in ['manifest.json', 'config.json', 'reference-config.json', 'held-out-predictions.csv',
                                  'outer-folds.csv', 'inner-folds.csv', 'tuning.json']]
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in paths}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'); out.mkdir(parents=True, exist_ok=False)
    for name, value in [('config', config), ('reference-config', base), ('generator-config', aug_config['generator'])]:
        (out/f'{name}.json').write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(), 'script_sha256': training.sha256(__file__),
        'config_sha256': training.sha256(config_path), 'helper_sha256': helpers, 'source_sha256': hashes, 'packages': packages}
    manifest_path = out/'manifest.json'; manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    try:
        jobs, folds = [], []
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(StratifiedKFold(5, shuffle=True, random_state=seed).split(data, y), 1):
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1), 'actual_class': int(y[i])} for i in test)
                rf = next(r for r in oldt if r['input_set'] == 'small_b' and r['model'] == 'forest' and r['augmentation'] == 'inner_selected_ratio' and r['repeat'] == rep and r['fold'] == fold)
                lr = next(r for r in logistic_tuning if r['input_set'] == 'small_b' and r['model'] == 'logistic' and r['repeat'] == rep and r['fold'] == fold)
                previous = {family: p[(p['repeat'] == rep) & (p.fold == fold)] for family, p in [('forest', rf_pred), ('logistic', lr_pred)]}
                jobs.append((config, base, aug_config['generator'], data, rep, fold, train, test, rf, lr, previous))
        fold_table = pd.DataFrame(folds); pd.testing.assert_frame_equal(fold_table, pd.read_csv(ref/'outer-folds.csv'))
        predictions, tuning, assignments = [], [], []
        with ProcessPoolExecutor(max_workers=config['workers']) as executor:
            for count, result in enumerate(executor.map(run_job, jobs), 1):
                p, t, a = result; predictions.extend(p); tuning.append(t); assignments.extend(a)
                print(f'Completed {count}/25: RF/logistic ensemble and threshold-only controls', flush=True)
        inner = pd.DataFrame(assignments); expected = pd.read_csv(ref/'inner-folds.csv'); expected = expected[expected.input_set == 'small_b']
        order = ['repeat', 'fold', 'inner_fold', 'student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True)[list(expected)], expected.sort_values(order).reset_index(drop=True))
        blend = old[(old.model == 'ridge_svr_blend') & (old.augmentation == 'reference_inner_f2_threshold')]
        result = pd.concat([pd.DataFrame(predictions), rf_pred, lr_pred, blend], ignore_index=True)
        assert len(result) == 3395 and len(tuning) == 25
        assert not result.duplicated(['input_set', 'model', 'augmentation', 'repeat', 'student_index']).any()
        assert np.array_equal(result.actual_class, (result.actual_score >= 4).astype(int))
        assert np.array_equal(result.predicted_class, (result.warning_score >= result.threshold).astype(int))
        assert np.allclose(result.actual_score, data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False); inner.to_csv(out/'inner-folds.csv', index=False)
        overlap.to_csv(out/'endpoint-error-comparison.csv', index=False)
        pd.DataFrame(overlap_rows).to_csv(out/'error-overlap.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        keys = ['input_set', 'model', 'augmentation', 'repeat']
        metrics = []
        for key, group in result.groupby(keys):
            assert len(group) == 97 and group.student_index.nunique() == 97 and group.actual_class.sum() == 17
            metrics.append(dict(zip(keys, key), **binary.metrics(group.actual_class, group.predicted_class),
                average_precision=float(augmentation.average_precision_score(group.actual_class, group.warning_score)),
                roc_auc=float(augmentation.roc_auc_score(group.actual_class, group.warning_score))))
        repeat_table = pd.DataFrame(metrics)
        repeat_table.to_csv(out/'repeat-metrics.csv', index=False)
        repeat_table.groupby(keys[:3]).mean(numeric_only=True).drop(columns='repeat').to_csv(out/'metrics-summary.csv')
        repeat_table[keys+['tp', 'fp', 'fn', 'tn']].to_csv(out/'confusion-matrices.csv', index=False)
        repeats = pd.read_csv(out/'repeat-metrics.csv'); comparisons = []
        for r in repeats[repeats.augmentation.isin(METHODS)].itertuples():
            references = ['inner_selected_ratio', 'real_only']
            if r.augmentation.startswith('ensemble_'): references.append('rf_threshold_only_guard' if r.augmentation.endswith('guard') else 'rf_threshold_only_f2')
            for method in references:
                other = repeats[(repeats['repeat'] == r.repeat) & (repeats.augmentation == method)].iloc[0]
                comparisons.append({'repeat': r.repeat, 'procedure': r.augmentation, 'reference': method,
                    'f2_difference': r.f2-other.f2, 'recall_difference': r.recall-other.recall,
                    'precision_difference': r.precision-other.precision, 'false_warnings_difference': r.fp-other.fp})
        pd.DataFrame(comparisons).to_csv(out/'paired-comparisons.csv', index=False)
        summary = pd.read_csv(out/'metrics-summary.csv')
        lines = ['# Current Random Forest plus logistic regression', '',
            '97 real students, High >=4 (17) versus Below-high <4 (80). Only real held-out evaluation.',
            'Same five repetitions of five stratified outer/four inner folds; selected RF and real-only logistic endpoint settings are retained.',
            'Endpoint settings and mixture selection reuse the same inner folds; outer students are excluded from the full selection process.',
            'Current endpoint outer predictions and recorded inner confusion metrics must reproduce exactly.',
            'RF shares 1/.9/.75/.5; warning thresholds 0..1 by .025. Raw weighted model scores are uncalibrated, not clinical probabilities.',
            'F2 rule maximizes inner F2/precision/recall/threshold/RF share. Recall guard requires at least the current RF inner recall, then minimizes FP.',
            'The recall guard is a training constraint, not a guarantee on excluded students. RF-only controls allow threshold tuning without mixing.', '',
            '| Procedure | Recall | Precision | F2 | Detected /17 | False warnings /80 | Average precision |',
            '|---|---:|---:|---:|---:|---:|---:|']
        for r in summary.itertuples(): lines.append(f'| {r.augmentation} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.3f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.3f} |')
        lines += ['', 'Metrics/counts average five dependent repetitions of the same students, not independent cohorts.',
            'Inspecting existing outer errors motivated this exploratory experiment. Any gain needs independent confirmation.',
            'No source SAV/CSV, earlier result folder or selected model was changed. No deployment model or calibrated risk probabilities.']
        (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, reference_folds_reproduced=True,
            endpoint_predictions_reproduced=True, real_participants=97, deployment_model_saved=False)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc)); raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat(); manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__': main()
