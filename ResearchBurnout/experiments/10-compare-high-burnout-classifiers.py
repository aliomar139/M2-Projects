"""Separate binary high-score warning comparison, including a refitted regression blend."""
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits
from xgboost import XGBClassifier

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ensemble', ROOT/'experiments/07-blend-ridge-and-svr-score-prediction.py')
ensemble = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ensemble)
training, priority, kernels = ensemble.training, ensemble.priority, ensemble.kernels


def metrics(actual, predicted):
    y, p = np.asarray(actual), np.asarray(predicted)
    tp, fp = int(((y == 1) & (p == 1)).sum()), int(((y == 0) & (p == 1)).sum())
    fn, tn = int(((y == 1) & (p == 0)).sum()), int(((y == 0) & (p == 0)).sum())
    precision = tp/(tp+fp) if tp+fp else 0.
    recall, specificity = tp/(tp+fn), tn/(tn+fp)
    return {'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn, 'flagged': tp+fp,
        'precision': precision, 'recall': recall, 'specificity': specificity,
        'false_positive_rate': 1-specificity, 'accuracy': (tp+tn)/len(y),
        'balanced_accuracy': (recall+specificity)/2,
        'f1': 2*tp/(2*tp+fn+fp) if 2*tp+fn+fp else 0.,
        'f2': 5*tp/(5*tp+4*fn+fp) if 5*tp+4*fn+fp else 0.}


def best_threshold(y, scores, thresholds):
    options = [{'threshold': t, **metrics(y, scores >= t)} for t in thresholds]
    return max(options, key=lambda c: (c['f2'], c['precision'], c['recall'], c['threshold'])), options


def classifier(family, params, seed):
    if family == 'logistic':
        return LogisticRegression(max_iter=10000, solver='lbfgs', **params)
    if family == 'forest':
        return RandomForestClassifier(n_estimators=100, n_jobs=1, random_state=seed, **params)
    if family == 'xgboost':
        return XGBClassifier(n_estimators=100, min_child_weight=5, reg_lambda=10,
            subsample=1, colsample_bytree=1, tree_method='hist', eval_metric='logloss',
            n_jobs=1, random_state=seed, **params)
    if family == 'histogram':
        return HistGradientBoostingClassifier(max_iter=100, learning_rate=.05,
            min_samples_leaf=10, early_stopping=False, categorical_features=None, random_state=seed, **params)
    raise ValueError(family)


def probabilities(model, X):
    assert np.array_equal(model.classes_, [0, 1])
    values = model.predict_proba(X)
    assert np.isfinite(values).all() and np.allclose(values.sum(axis=1), 1)
    assert ((values >= 0) & (values <= 1)).all()
    return values[:, 1]


def search(config, family, parts, y, seed):
    candidates = []
    for factor in config['relative_high_weights']:
        for params in ParameterGrid(config['grids'][family]):
            oof, seen = np.full(len(y), np.nan), np.zeros(len(y), dtype=int)
            for tr, va, Xt, Xv in parts:
                w = priority.weights(y[tr], factor, 1)
                model = classifier(family, params, seed).fit(Xt, y[tr], sample_weight=w)
                oof[va] = probabilities(model, Xv)
                seen[va] += 1
            assert np.isfinite(oof).all() and np.all(seen == 1)
            chosen, thresholds = best_threshold(y, oof, config['probability_thresholds'])
            candidates.append({'factor': factor, 'parameters': params, 'chosen_threshold': chosen,
                'threshold_candidates': thresholds})
    selected = max(candidates, key=lambda c: (c['chosen_threshold']['f2'], c['chosen_threshold']['precision'],
        c['chosen_threshold']['recall'], c['chosen_threshold']['threshold']))
    return selected, candidates


def blend_predictions(base, ridge_config, svr_config, data, train, test, inner):
    ridge_cols, svr_cols = base['input_sets']['small_b'], base['input_sets']['broad_d']
    Xridge, Xsvr, y = data[ridge_cols].iloc[train], data[svr_cols].iloc[train], data.burnout_score.iloc[train]
    _, ridge_choice, ridge_candidates = priority.inner_select(base, ridge_config, ridge_cols, Xridge, y, inner)
    prepared = [(tr, va, *kernels.transform(base, svr_cols, Xsvr.iloc[tr], Xsvr.iloc[va])) for tr, va in inner]
    svr_choices, svr_candidates = kernels.inner_search(svr_config, 'svr', prepared, y)
    svr_choice = svr_choices['high_priority']
    ro, so = np.full(len(y), np.nan), np.full(len(y), np.nan)
    for tr, va, Xt, Xv in prepared:
        ro[va] = priority.predict(ensemble.fit_ridge(base, ridge_cols, Xridge.iloc[tr], y.iloc[tr], ridge_choice), Xridge.iloc[va])[1]
        so[va] = np.clip(ensemble.fit_svr(Xt, y.iloc[tr], svr_choice).predict(Xv), 1, 5)
    assert np.isfinite(ro).all() and np.isfinite(so).all()
    assert np.isclose(np.abs(y.to_numpy()-ro).mean(), ridge_choice['overall_mae'])
    assert np.isclose(np.abs(y.to_numpy()-so).mean(), svr_choice['mae'])
    rp = priority.predict(ensemble.fit_ridge(base, ridge_cols, Xridge, y, ridge_choice), data[ridge_cols].iloc[test])[1]
    Xt, Xtest = kernels.transform(base, svr_cols, Xsvr, data[svr_cols].iloc[test])
    sp = np.clip(ensemble.fit_svr(Xt, y, svr_choice).predict(Xtest), 1, 5)
    return .5*(ro+so), .5*(rp+sp), {'ridge_choice': ridge_choice, 'svr_choice': svr_choice,
        'ridge_candidates': ridge_candidates, 'svr_candidates': svr_candidates}


def report(result, out):
    keys = ['input_set', 'model', 'procedure', 'repeat']
    records = []
    for key, group in result.groupby(keys):
        assert len(group) == 97 and group.student_index.nunique() == 97 and group.actual_class.sum() == 17
        records.append(dict(zip(keys, key), **metrics(group.actual_class, group.predicted_class),
            roc_auc=float(roc_auc_score(group.actual_class, group.warning_score)),
            average_precision=float(average_precision_score(group.actual_class, group.warning_score))))
    repeats = pd.DataFrame(records)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(keys[:3]).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    repeats[keys+['tp', 'fp', 'fn', 'tn']].to_csv(out/'confusion-matrices.csv', index=False)
    repeats.groupby(keys[:3])[['f2', 'recall', 'precision']].agg(['min', 'max', 'std']).to_csv(out/'repetition-stability.csv')
    differences = []
    for row in repeats[repeats.model.isin(['logistic', 'forest', 'xgboost', 'histogram'])].itertuples():
        for ref in ['fixed_score_4', 'inner_f2_threshold']:
            baseline = repeats[(repeats.model == 'ridge_svr_blend') & (repeats.procedure == ref) & (repeats['repeat'] == row.repeat)].iloc[0]
            differences.append({'input_set': row.input_set, 'model': row.model, 'procedure': row.procedure,
                'repeat': row.repeat, 'reference_blend': ref, 'f2_difference': row.f2-baseline.f2,
                'recall_difference': row.recall-baseline.recall, 'precision_difference': row.precision-baseline.precision})
    pd.DataFrame(differences).to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Binary high-score warning experiment', '',
        'High: primary burnout_score >=4 (17 students); Below-high: <4 (80 students). Study-defined, not clinical categories; below-high does not mean no risk.',
        '97 real students. Five stratified outer folds repeated five times, four stratified inner folds, shared by all models and refitted blend.',
        'New folds differ from earlier regression and three-class experiments; use within-run comparisons, not old MAE or classification results.',
        'Existing Small B (8) / Broad D (23) non-BAT inputs only. No synthetic students or new questions. All preprocessing and tuning are training-only.',
        'Primary selection maximizes pooled inner F2 = 5TP/(5TP+4FN+FP), prioritizing recall while penalizing false warnings. Ties: precision, recall, larger threshold, stable grid order.',
        'Classifiers jointly tune settings, normalized High weights 1/2/4 and thresholds. Same fitted model at .5 is a diagnostic, not a separately tuned .5 procedure.',
        'The refitted 50/50 blend retains prior High-MAE endpoint tuning; only its warning threshold is selected by inner F2. Threshold 4 is also reported.',
        'Classifier probability outputs are not calibrated risk estimates; the blend warning score is a burnout-score estimate, not a probability.', '',
        '| Inputs | Model | Procedure | Recall | Precision | F2 | False positive rate | TP /17 | FP /80 | Average precision |',
        '|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for (inputs, model, procedure), row in summary.sort_values('f2', ascending=False).iterrows():
        lines.append(f'| {inputs} | {model} | {procedure} | {row.recall:.1%} | {row.precision:.1%} | {row.f2:.3f} | '
            f'{row.false_positive_rate:.1%} | {row.tp:.1f} | {row.fp:.1f} | {row.average_precision:.3f} |')
    lines += ['', 'Counts and metrics average five repetitions on the same students. They are not five independent samples or integer counts for a single run.',
        'Flag-everyone and flag-no-one references expose misleading high recall and high accuracy. Accuracy alone is not a warning-system success criterion.',
        'No acceptable recall/precision or clinical utility threshold was established. Small High count and repeated exploration limit conclusions.',
        'Inner predictions are reused to choose settings and thresholds; excluded outer groups evaluate the complete procedure. Best-looking outer methods remain exploratory.',
        'No deployment model or independent validation. Source data and earlier experiments remain unchanged.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    warnings.filterwarnings('error', category=ConvergenceWarning)
    config_path = ROOT/'experiments/10-compare-high-burnout-classifiers-settings.json'
    config = json.loads(config_path.read_text())
    reference, old_blend = ROOT/config['reference_run'], ROOT/config['ensemble_run']
    for folder in [reference, old_blend]:
        assert json.loads((folder/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    ridge_config = json.loads((old_blend/'ridge-config.json').read_text())
    svr_config = json.loads((old_blend/'svr-config.json').read_text())
    data = training.load_data(base)
    y = (data[config['target_score']].to_numpy() >= config['high_boundary']).astype(int)
    assert len(data) == 97 and np.bincount(y).tolist() == config['expected_counts']
    assert config['target_score'] == 'burnout_score' and config['high_boundary'] == 4
    sources = [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    sources += [folder/name for folder in [reference, old_blend] for name in ['config.json', 'manifest.json', 'held-out-predictions.csv']]
    sources += [old_blend/'ridge-config.json', old_blend/'svr-config.json']
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in sources}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    for name, value in [('config', config), ('reference-config', base), ('ridge-config', ridge_config), ('svr-config', svr_config)]:
        (out/f'{name}.json').write_text(json.dumps(value, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'config_sha256': training.sha256(config_path),
        'helper_sha256': {Path(m.__file__).name: training.sha256(m.__file__) for m in [ensemble, training, priority, kernels]},
        'source_sha256': hashes, 'class_counts': {'below_high': 80, 'high': 17},
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat', 'xgboost', 'threadpoolctl']},
        'deployment_model_saved': False}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, folds, inner_folds = [], [], [], []
    def save(inputs, model, procedure, rep, fold, test, scores, threshold, kind):
        assert len(scores) == len(test) and np.isfinite(scores).all()
        for idx, score in zip(test, scores):
            predictions.append({'input_set': inputs, 'model': model, 'procedure': procedure, 'repeat': rep, 'fold': fold,
                'student_index': int(idx+1), 'actual_score': float(data[config['target_score']].iloc[idx]),
                'actual_class': int(y[idx]), 'warning_score': float(score), 'score_kind': kind,
                'threshold': float(threshold), 'predicted_class': int(score >= threshold)})
    try:
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            outer = StratifiedKFold(config['outer_folds'], shuffle=True, random_state=seed)
            for fold, (train, test) in enumerate(outer.split(data, y), 1):
                print(f'Repetition {rep}/5, fold {fold}/5: binary classifiers and matched ridge/SVR blend', flush=True)
                assert not set(train) & set(test)
                assert np.bincount(y[test], minlength=2).min() >= 3
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1), 'actual_class': int(y[i])} for i in test)
                seed_inner = base['cv']['inner_seed']+rep*100+fold
                inner = list(StratifiedKFold(config['inner_folds'], shuffle=True, random_state=seed_inner).split(train, y[train]))
                for inner_fold, (tr, va) in enumerate(inner, 1):
                    assert not set(tr) & set(va) and np.bincount(y[train][tr], minlength=2).min() >= 1
                    inner_folds.extend({'repeat': rep, 'outer_fold': fold, 'inner_fold': inner_fold,
                        'student_index': int(train[i]+1)} for i in va)
                save('baseline', 'none_flagged', 'fixed', rep, fold, test, np.zeros(len(test)), .5, 'constant')
                save('baseline', 'all_flagged', 'fixed', rep, fold, test, np.ones(len(test)), .5, 'constant')
                for inputs in config['input_sets']:
                    cols = base['input_sets'][inputs]
                    assert not any(c.startswith('BAT') or 'burnout' in c for c in cols)
                    X = data[cols].iloc[train]
                    parts = [(tr, va, *kernels.transform(base, cols, X.iloc[tr], X.iloc[va])) for tr, va in inner]
                    Xt, Xtest = kernels.transform(base, cols, X, data[cols].iloc[test])
                    for family in config['grids']:
                        chosen, candidates = search(config, family, parts, y[train], seed_inner)
                        fitted = classifier(family, chosen['parameters'], seed_inner).fit(Xt, y[train],
                            sample_weight=priority.weights(y[train], chosen['factor'], 1))
                        scores = probabilities(fitted, Xtest)
                        tuning.append({'input_set': inputs, 'model': family, 'repeat': rep, 'fold': fold,
                            'chosen': chosen, 'candidates': candidates})
                        save(inputs, family, 'inner_f2_threshold', rep, fold, test, scores, chosen['chosen_threshold']['threshold'], 'uncalibrated_probability')
                        save(inputs, family, 'same_params_at_0.5', rep, fold, test, scores, .5, 'uncalibrated_probability')
                blend_oof, blend_test, blend_tuning = blend_predictions(base, ridge_config, svr_config, data, train, test, inner)
                chosen, thresholds = best_threshold(y[train], blend_oof, config['blend_thresholds'])
                tuning.append({'input_set': 'combined_existing', 'model': 'ridge_svr_blend', 'repeat': rep, 'fold': fold,
                    'chosen_threshold': chosen, 'threshold_candidates': thresholds, **blend_tuning})
                save('combined_existing', 'ridge_svr_blend', 'inner_f2_threshold', rep, fold, test, blend_test, chosen['threshold'], 'burnout_score')
                save('combined_existing', 'ridge_svr_blend', 'fixed_score_4', rep, fold, test, blend_test, 4, 'burnout_score')
        result = pd.DataFrame(predictions)
        assert len(result) == 20*97*5
        assert not result.duplicated(['input_set', 'model', 'procedure', 'repeat', 'student_index']).any()
        assert np.array_equal(result.actual_class, (result.actual_score >= 4).astype(int))
        assert np.array_equal(result.predicted_class, (result.warning_score >= result.threshold).astype(int))
        assert np.allclose(result.actual_score, data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv', index=False)
        pd.DataFrame(folds).to_csv(out/'outer-folds.csv', index=False)
        pd.DataFrame(inner_folds).to_csv(out/'inner-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        report(result, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, matched_stratified_folds=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    with threadpool_limits(limits=1):
        main()
