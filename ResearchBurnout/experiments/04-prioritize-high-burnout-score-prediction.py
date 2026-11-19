"""Nested weighted-ridge follow-up. No source data or previous runs are overwritten."""
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('training', Path(__file__).with_name('01-compare-score-prediction-baselines.py'))
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)


def weights(y, factor, boundary):
    values = np.where(np.asarray(y) >= boundary, factor, 1.0)
    return values/values.mean()


def fit_ridge(base, cols, X, y, alpha, factor, boundary):
    wrapped, _ = training.make_model(base, cols, 'ridge')
    pipeline = wrapped.estimator
    pipeline.set_params(model__alpha=alpha)
    pipeline.fit(X, y, model__sample_weight=weights(y, factor, boundary))
    return pipeline


def predict(model, X):
    raw = model.predict(X)
    return raw, np.clip(raw, 1, 5)


def choose_candidates(candidates, tolerance):
    ordinary = min((c for c in candidates if c['factor'] == 1), key=lambda c: c['fold_mean_mae'])
    eligible = [c for c in candidates if c['overall_mae'] <= ordinary['overall_mae']+tolerance+1e-12]
    if ordinary['high_mae'] is None:
        return ordinary, ordinary
    chosen = min(eligible, key=lambda c: (c['high_mae'], c['overall_mae'], c['factor'], c['alpha']))
    return ordinary, chosen


def inner_select(base, config, cols, X, y, inner):
    candidates = []
    boundary = config['high_score_boundary']
    for factor in config['relative_high_weights']:
        for alpha in config['ridge_alphas']:
            oof = np.full(len(y), np.nan)
            fold_mae = []
            for train, valid in inner:
                assert not set(train) & set(valid)
                model = fit_ridge(base, cols, X.iloc[train], y.iloc[train], alpha, factor, boundary)
                _, prediction = predict(model, X.iloc[valid])
                oof[valid] = prediction
                fold_mae.append(float(np.abs(y.iloc[valid].to_numpy()-prediction).mean()))
            assert np.isfinite(oof).all()
            error = np.abs(y.to_numpy()-oof)
            high = y.to_numpy() >= boundary
            candidates.append({'factor': factor, 'alpha': alpha,
                'fold_mean_mae': float(np.mean(fold_mae)), 'overall_mae': float(error.mean()),
                'high_mae': float(error[high].mean()) if high.any() else None,
                'high_students': int(high.sum())})
    ordinary, chosen = choose_candidates(candidates, config['inner_overall_mae_tolerance'])
    return ordinary, chosen, candidates


def group_metrics(group, boundary):
    actual = group.actual.to_numpy()
    pred = group.prediction.to_numpy()
    signed = pred-actual
    high = actual >= boundary
    flagged = pred >= boundary
    tp = int((high & flagged).sum())
    return {'n': len(group), 'high_n': int(high.sum()),
        **training.metrics(actual, pred),
        'high_mae': float(np.abs(signed[high]).mean()) if high.any() else None,
        'high_signed_error': float(signed[high].mean()) if high.any() else None,
        'high_mean_underestimation': float(np.maximum(-signed[high], 0).mean()) if high.any() else None,
        'high_recall': tp/int(high.sum()) if high.any() else None,
        'high_precision': tp/int(flagged.sum()) if flagged.any() else None,
        'true_positive_count': tp, 'flagged_count': int(flagged.sum()),
        'false_positive_count': int((flagged & ~high).sum()),
        'false_positive_rate': int((flagged & ~high).sum())/int((~high).sum()) if (~high).any() else None,
        'lower_mae': float(np.abs(signed[actual < 2.5]).mean()) if (actual < 2.5).any() else None}


def summarize(predictions, config, out):
    records = []
    for key, group in predictions.groupby(['target', 'model', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        records.append(dict(zip(['target', 'model', 'repeat'], key),
            **group_metrics(group, config['high_score_boundary'])))
    repeats = pd.DataFrame(records)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(['target', 'model']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    paired = []
    for target, part in repeats.groupby('target'):
        a = part[part.model == 'ordinary_ridge'].set_index('repeat')
        b = part[part.model == 'high_priority_ridge'].set_index('repeat')
        for rep in a.index:
            high_delta = b.loc[rep, 'high_mae']-a.loc[rep, 'high_mae']
            overall_delta = b.loc[rep, 'mae']-a.loc[rep, 'mae']
            paired.append({'target': target, 'repeat': rep,
                'high_mae_difference': high_delta, 'overall_mae_difference': overall_delta,
                'numerical_goal_met': bool(high_delta < 0 and overall_delta <= config['inner_overall_mae_tolerance'])})
    pairs = pd.DataFrame(paired)
    pairs.to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# High-score-priority ridge follow-up', '',
        'Exploratory follow-up on the same 97 students after reviewing earlier results. No synthetic data.',
        'Measured/predicted scores >=4 define a descriptive evaluation group, not a clinical diagnosis.',
        'Weights and alpha were selected inside each outer training group. No outer-test answers were used to choose settings.',
        'The inner guardrail allows pooled overall MAE up to 0.05 points worse than ordinary ridge; this does not guarantee the outer guardrail holds.',
        'Signed error <0 means underestimation. Precision is undefined (NA) if nobody is flagged in a repetition.', '',
        '| Target | Model | Overall MAE | High-score MAE | High mean underestimation | High recall | False-positive rate | Lower-score MAE |',
        '|---|---|---:|---:|---:|---:|---:|---:|']
    for (target, model), row in summary.iterrows():
        lines.append(f'| {target} | {model} | {row.mae:.4f} | {row.high_mae:.4f} | '
            f'{row.high_mean_underestimation:.4f} | {row.high_recall:.1%} | {row.false_positive_rate:.1%} | {row.lower_mae:.4f} |')
    lines += ['', '## Paired changes (priority minus ordinary)', '',
        '| Target | Mean high-score MAE change | Mean overall MAE change | Repetitions meeting numerical goal |',
        '|---|---:|---:|---:|']
    for target, group in pairs.groupby('target'):
        lines.append(f'| {target} | {group.high_mae_difference.mean():+.4f} | {group.overall_mae_difference.mean():+.4f} | '
            f'{group.numerical_goal_met.sum()}/{len(group)} |')
    lines += ['', 'The numerical goal is lower high-score MAE with overall MAE increase <=0.05. This is an analytical choice, not clinical validation.',
        'Repetitions reuse students; ranges and differences are descriptive, not independent tests.',
        'A higher average prediction alone does not establish better detection. Review false positives and lower-score errors.',
        'No deployment model or weights are saved. Source SAV and previous runs are unchanged.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'experiments/04-prioritize-high-burnout-score-prediction-settings.json'
    config = json.loads(config_path.read_text())
    reference = ROOT/config['reference_run']
    assert json.loads((reference/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    assert config['targets'] == base['targets'] and config['ridge_alphas'] == base['ridge_alphas']
    assert config['relative_high_weights'] == [1., 2., 4.] and not config['augmentation']
    assert config['high_score_boundary'] == 4 and config['normalize_training_weights_to_mean_one']
    original = pd.read_csv(reference/'held-out-predictions.csv')
    source_hashes = {str(path.relative_to(ROOT)): training.sha256(path) for path in
        [ROOT/base['dataset'], reference/'held-out-predictions.csv', reference/'config.json', reference/'outer-folds.csv']}
    df = training.load_data(base)
    cols = base['input_sets'][config['input_set']]
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    (out/'config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')
    (out/'reference-config.json').write_text(json.dumps(base, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'engine_sha256': training.sha256(Path(training.__file__)),
        'source_sha256': source_hashes, 'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']},
        'interpretation': config['interpretation'], 'deployment_model_saved': False}
    records, tuning, fold_records = [], [], []
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    try:
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(KFold(5, shuffle=True, random_state=seed).split(df), 1):
                assert not set(train) & set(test)
                print(f'Repetition {rep}/5, fold {fold}: selecting high-priority ridge for both targets', flush=True)
                fold_records.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1)} for i in test)
                inner = list(KFold(4, shuffle=True, random_state=base['cv']['inner_seed']+rep*100+fold).split(train))
                for target in config['targets']:
                    X, y = df[cols].iloc[train], df[target].iloc[train]
                    ordinary, chosen, candidates = inner_select(base, config, cols, X, y, inner)
                    tuning.append({'target': target, 'repeat': rep, 'fold': fold,
                        'ordinary': ordinary, 'chosen': chosen, 'candidates': candidates})
                    for name, choice in [('ordinary_ridge', ordinary), ('high_priority_ridge', chosen)]:
                        model = fit_ridge(base, cols, X, y, choice['alpha'], choice['factor'], config['high_score_boundary'])
                        raw, pred = predict(model, df[cols].iloc[test])
                        if name == 'ordinary_ridge':
                            old = original[(original.target == target) & (original.input_set == config['input_set']) &
                                (original.model == 'ridge') & (original['repeat'] == rep) & (original.fold == fold)].set_index('student_index')
                            assert len(old) == len(test)
                            if not np.allclose(pred, old.loc[test+1, 'prediction'], atol=1e-8, rtol=1e-8):
                                raise ValueError('Ordinary ridge does not reproduce original predictions.')
                        for idx, actual, prediction, unbounded in zip(test, df[target].iloc[test], pred, raw):
                            records.append({'target': target, 'input_set': config['input_set'], 'model': name,
                                'repeat': rep, 'fold': fold, 'student_index': int(idx+1), 'actual': float(actual),
                                'prediction': float(prediction), 'raw_prediction': float(unbounded),
                                'absolute_error': float(abs(actual-prediction))})
        folds = pd.DataFrame(fold_records)
        order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(folds.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        predictions = pd.DataFrame(records)
        assert not predictions.duplicated(['target', 'model', 'repeat', 'student_index']).any()
        predictions.to_csv(out/'held-out-predictions.csv', index=False)
        folds.to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        summarize(predictions, config, out)
        assert all(training.sha256(ROOT/p) == h for p, h in source_hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, ordinary_reference_reproduced=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
