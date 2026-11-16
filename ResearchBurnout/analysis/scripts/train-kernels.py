"""Existing survey inputs only: nested SVR/kernel-ridge comparison."""
from datetime import datetime, timezone
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import KFold, ParameterGrid
from sklearn.svm import SVR

import importlib.util

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('priority', Path(__file__).with_name('train-high-score.py'))
priority = importlib.util.module_from_spec(spec)
spec.loader.exec_module(priority)
training = priority.training


def estimator(family, params):
    if family == 'svr':
        return SVR(kernel='rbf', **params)
    if family == 'kernel_ridge':
        return KernelRidge(kernel='rbf', **params)
    raise ValueError(f'Unknown family: {family}')


def transform(base, cols, X_train, X_test):
    wrapped, _ = training.make_model(base, cols, 'ridge')
    preprocessing = wrapped.estimator[:-1]
    return preprocessing.fit_transform(X_train), preprocessing.transform(X_test)


def select(candidates, tolerance):
    ordinary = min((c for c in candidates if c['factor'] == 1), key=lambda c: c['fold_mean_mae'])
    if ordinary['high_mae'] is None:
        return ordinary, ordinary
    eligible = [c for c in candidates if c['mae'] <= ordinary['mae']+tolerance+1e-12]
    chosen = min(eligible, key=lambda c: (c['high_mae'], c['mae'], c['factor'], c['grid_index']))
    return ordinary, chosen


def inner_search(config, family, prepared, y):
    candidates = []
    high = np.asarray(y) >= config['high_boundary']
    for factor in config['relative_high_weights']:
        for index, params in enumerate(ParameterGrid(config['grids'][family])):
            oof = np.full(len(y), np.nan)
            fold_errors = []
            for train, valid, X_train, X_valid in prepared:
                model = estimator(family, params)
                sample_weights = priority.weights(np.asarray(y)[train], factor, config['high_boundary'])
                model.fit(X_train, np.asarray(y)[train], sample_weight=sample_weights)
                pred = np.clip(model.predict(X_valid), 1, 5)
                oof[valid] = pred
                fold_errors.append(float(np.abs(np.asarray(y)[valid]-pred).mean()))
            assert np.isfinite(oof).all()
            errors = np.abs(np.asarray(y)-oof)
            candidates.append({'factor': factor, 'parameters': params, 'grid_index': index,
                'fold_mean_mae': float(np.mean(fold_errors)), 'mae': float(errors.mean()),
                'high_mae': float(errors[high].mean()) if high.any() else None})
    ordinary, chosen = select(candidates, config['inner_overall_mae_tolerance'])
    return {'ordinary': ordinary, 'high_priority': chosen}, candidates


def report(predictions, out):
    rows = []
    for key, group in predictions.groupby(['input_set', 'family', 'procedure', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        rows.append(dict(zip(['input_set', 'family', 'procedure', 'repeat'], key),
            **priority.group_metrics(group, 4)))
    repeats = pd.DataFrame(rows)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(['input_set', 'family', 'procedure']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    differences = []
    for row in repeats[repeats.family != 'reference_ridge'].itertuples():
        ref = repeats[(repeats.input_set == row.input_set) & (repeats.family == 'reference_ridge')
            & (repeats['repeat'] == row.repeat)].iloc[0]
        differences.append({'input_set': row.input_set, 'family': row.family, 'procedure': row.procedure,
            'repeat': row.repeat, 'mae_minus_reference': row.mae-ref.mae,
            'high_mae_minus_reference': row.high_mae-ref.high_mae})
    pd.DataFrame(differences).to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Kernel regression using existing survey inputs', '',
        'Primary continuous burnout_score, 97 real students, original five outer folds repeated five times, four inner folds.',
        'No new survey features, synthetic examples or BAT predictors. Standard category encoding/scaling uses training data only.',
        'Each family has ordinary overall-MAE tuning and a separate high-priority selection procedure.',
        'High-priority selects lowest inner high-score MAE within .05 pooled overall MAE of ordinary; the guard is not an outer-test guarantee.',
        'High means measured score >=4; lower means <2.5. These are descriptive groups, not clinical categories.', '',
        '| Inputs | Family | Procedure | MAE | RMSE | High MAE | High underestimation | Lower MAE |',
        '|---|---|---|---:|---:|---:|---:|---:|']
    for (inputs, family, procedure), row in summary.iterrows():
        lines.append(f'| {inputs} | {family} | {procedure} | {row.mae:.4f} | {row.rmse:.4f} | '
            f'{row.high_mae:.4f} | {row.high_mean_underestimation:.4f} | {row.lower_mae:.4f} |')
    lines += ['', 'Errors average five repetition metrics on the same students. Repetition spread is descriptive, not independent replication.',
        'This experiment was proposed after previous results. Searching more procedures can overfit this evaluation history; '
        'a best-looking outer result is exploratory, not unbiased evidence for a selected final model.',
        'Existing reference ridge predictions are copied for matched folds. Source datasets and earlier runs remain unchanged.',
        'No deployment model or weights were saved. Read repeat-metrics.csv and paired-comparisons.csv for stability.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'analysis/kernel-config.json'
    config = json.loads(config_path.read_text())
    reference = ROOT/config['reference_run']
    assert json.loads((reference/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    data = training.load_data(base)
    assert len(data) == 97
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in
        [ROOT/base['dataset'], reference/'config.json', reference/'outer-folds.csv', reference/'held-out-predictions.csv']}
    old = pd.read_csv(reference/'held-out-predictions.csv')
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    (out/'config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')
    (out/'reference-config.json').write_text(json.dumps(base, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'engine_sha256': training.sha256(training.__file__),
        'helper_sha256': training.sha256(priority.__file__), 'source_sha256': hashes,
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']},
        'real_participants': 97, 'augmentation': False, 'new_survey_features': False}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, folds = [], [], []
    try:
        y = data[config['target']]
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(KFold(base['cv']['outer_folds'], shuffle=True, random_state=seed).split(data), 1):
                assert not set(train) & set(test)
                print(f'Repetition {rep}/5, fold {fold}/5: SVR and kernel ridge, existing inputs only', flush=True)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1)} for i in test)
                inner = list(KFold(base['cv']['inner_folds'], shuffle=True,
                    random_state=base['cv']['inner_seed']+rep*100+fold).split(train))
                for inputs in config['input_sets']:
                    cols = base['input_sets'][inputs]
                    assert not any(col.startswith('BAT') or 'burnout' in col for col in cols)
                    X = data[cols].iloc[train]
                    prepared = []
                    for tr, va in inner:
                        assert not set(tr) & set(va)
                        Xt, Xv = transform(base, cols, X.iloc[tr], X.iloc[va])
                        prepared.append((tr, va, Xt, Xv))
                    Xt, Xtest = transform(base, cols, X, data[cols].iloc[test])
                    for family in config['grids']:
                        choices, candidates = inner_search(config, family, prepared, y.iloc[train])
                        tuning.append({'repeat': rep, 'fold': fold, 'input_set': inputs,
                            'family': family, 'chosen': choices, 'candidates': candidates})
                        for procedure, choice in choices.items():
                            model = estimator(family, choice['parameters'])
                            w = priority.weights(y.iloc[train], choice['factor'], config['high_boundary'])
                            model.fit(Xt, y.iloc[train], sample_weight=w)
                            raw = model.predict(Xtest)
                            pred = np.clip(raw, 1, 5)
                            assert np.isfinite(pred).all()
                            for idx, actual, prediction, unbounded in zip(test, y.iloc[test], pred, raw):
                                predictions.append({'input_set': inputs, 'family': family, 'procedure': procedure,
                                    'repeat': rep, 'fold': fold, 'student_index': int(idx+1), 'actual': float(actual),
                                    'prediction': float(prediction), 'raw_prediction': float(unbounded),
                                    'absolute_error': float(abs(actual-prediction))})
        fold_table = pd.DataFrame(folds)
        order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        refs = old[(old.target == config['target']) & old.input_set.isin(config['input_sets']) & (old.model == 'ridge')].copy()
        refs['family'], refs['procedure'] = 'reference_ridge', 'ordinary'
        predictions = pd.DataFrame(predictions)
        refs = refs[list(predictions)]
        predictions = pd.concat([predictions, refs], ignore_index=True)
        assert not predictions.duplicated(['input_set', 'family', 'procedure', 'repeat', 'student_index']).any()
        predictions.to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        report(predictions, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, original_folds_reproduced=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
