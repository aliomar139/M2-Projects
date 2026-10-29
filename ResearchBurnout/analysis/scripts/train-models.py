"""Evaluate fixed model families on real held-out students; no deployment fit."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyreadstat
from sklearn.base import BaseEstimator, RegressorMixin, clone
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[2]


class BoundedRegressor(RegressorMixin, BaseEstimator):
    """Apply the same fixed bounds during inner selection and outer evaluation."""
    def __init__(self, estimator, lower=1.0, upper=5.0):
        self.estimator = estimator
        self.lower = lower
        self.upper = upper

    def fit(self, X, y):
        self.estimator_ = clone(self.estimator).fit(X, y)
        return self

    def predict_raw(self, X):
        return self.estimator_.predict(X)

    def predict(self, X):
        return np.clip(self.predict_raw(X), self.lower, self.upper)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_config(c):
    sets = c['input_sets']
    if set(sets) != {'small_a', 'small_b', 'broad_c', 'broad_d'}:
        raise ValueError('Expected the four agreed input sets.')
    allowed = {
        'enrolled_lebanon', 'academic_level_code', 'major_code', 'gpa_code',
        'electricity_code', 'internet', 'financial_strain', 'study_hours_code',
        'workload', 'sleep_duration_code', 'academic_stress', 'avoidance',
        'university_support', 'ai_frequency', 'ai_dependence', 'ai_offloading',
        'ai_verification', 'ai_anxiety', 'ai_use_concepts', 'ai_use_writing',
        'ai_use_coding', 'ai_use_summaries', 'ai_use_solutions',
    }
    for name, cols in sets.items():
        if len(set(cols)) != len(cols) or not set(cols) <= allowed:
            raise ValueError(f'Invalid or outcome-revealing inputs: {name}')
    for a, b in [('small_a', 'small_b'), ('broad_c', 'broad_d')]:
        if not set(sets[a]) < set(sets[b]):
            raise ValueError('The with-AI set must contain its context set.')
    if c['augmentation'] or c['prediction_range']['policy'].split()[0] != 'clip':
        raise ValueError('This script implements real data and clipped predictions only.')
    if c['targets'] != ['burnout_score', 'burnout_score_23']:
        raise ValueError('Unexpected targets.')
    if any(c['models_by_set'][k] != ['ridge'] for k in ['broad_c', 'broad_d']):
        raise ValueError('Broad comparison is ridge only.')


def load_data(c):
    path = ROOT / c['dataset']
    if sha256(path) != c['dataset_sha256']:
        raise ValueError('Dataset hash changed: review and version the configuration before continuing.')
    df, _ = pyreadstat.read_sav(str(path), apply_value_formats=False, user_missing=False)
    if df.shape != (c['expected_rows'], c['expected_columns']):
        raise ValueError(f'Dataset changed: expected 97 x 66, found {df.shape}')
    repair = c['derived_indicator_reconstruction']
    source, variable = repair['source'], repair['variable']
    raw = pd.read_csv(ROOT / repair['raw_csv'])
    # The raw CSV has Timestamp, then Q1..Q43; Q9 is its tenth column.
    if len(raw) != len(df) or not np.array_equal(raw.iloc[:, 0].astype(str), df['Timestamp'].astype(str)):
        raise ValueError('Raw CSV records do not align with SAV records.')
    if not np.array_equal(raw.iloc[:, 9].astype(str), df[source].astype(str)):
        raise ValueError('Original AI selections disagree with raw CSV.')
    expected = df[source].map(lambda answer: int(repair['selected_text'] in
        [part.strip() for part in answer.split(';')]))
    missing = df[variable].isna()
    if int(missing.sum()) != repair['expected_missing_count']:
        raise ValueError('Derived-indicator missing count changed; review before continuing.')
    if not np.array_equal(df.loc[~missing, variable], expected.loc[~missing]):
        raise ValueError('Nonmissing summary indicators disagree with original selections.')
    df.loc[missing, variable] = expected.loc[missing]
    df.attrs['readiness'] = {
        'source_dataset_changed': False, 'source_sha256': sha256(path),
        'raw_csv_sha256': sha256(ROOT / repair['raw_csv']),
        'reconstructed_variable': variable, 'reconstructed_count': int(missing.sum()),
        'basis': 'Original multi-choice answers exactly match the raw CSV; no statistical imputation.',
        'remaining_missing_model_values': 0,
    }
    cols = sorted(set(sum(c['input_sets'].values(), []) + c['targets']))
    if not set(cols) <= set(df):
        raise ValueError('Required columns are absent.')
    if not np.isfinite(df[cols].to_numpy(dtype=float)).all():
        raise ValueError('Missing or nonfinite values: investigate before fitting.')
    for col in cols:
        values = df[col].to_numpy()
        if col in c['targets']:
            if not ((values >= 1) & (values <= 5)).all():
                raise ValueError(f'Target outside 1-5: {col}')
        else:
            levels = c['category_levels'].get(col)
            if levels is None:
                levels = [0, 1] if col == 'enrolled_lebanon' or col.startswith('ai_use_') else [1, 2, 3, 4, 5]
            if not np.isin(values, levels).all():
                raise ValueError(f'Invalid survey codes: {col}')
    groups = {
        'exhaustion': [21, 23, 24], 'mental_distance': [29, 31, 33],
        'cognitive_impairment': [34, 37, 38], 'emotional_impairment': [39, 40, 43],
        'exhaustion_23': list(range(21, 29)), 'mental_distance_23': list(range(29, 34)),
        'congnitive_impairement_23': list(range(34, 39)),
        'emotional_impairment_23': list(range(39, 44)),
    }
    for col, items in groups.items():
        block = df[[f'BAT{i}' for i in items]].to_numpy(dtype=float)
        if not np.isin(block, [1, 2, 3, 4, 5]).all():
            raise ValueError('Missing or invalid BAT item.')
        if not np.allclose(df[col], block.mean(axis=1), atol=1e-10):
            raise ValueError(f'Score formula mismatch: {col}')
    for target, columns in [('burnout_score', list(groups)[:4]), ('burnout_score_23', list(groups)[4:])]:
        if not np.allclose(df[target], df[columns].mean(axis=1), atol=1e-10):
            raise ValueError(f'Score formula mismatch: {target}')
    return df


def make_model(c, cols, family):
    cats = [col for col in cols if col in c['category_levels']]
    nums = [col for col in cols if col not in cats]
    steps = []
    if cats:
        # Categories and reference codes come from the questionnaire, not held-out data.
        steps.append(('categories', OneHotEncoder(
            categories=[c['category_levels'][col] for col in cats],
            drop='first', handle_unknown='error', sparse_output=False), cats))
    if nums:
        steps.append(('numbers', 'passthrough', nums))
    pipeline = [('encode', ColumnTransformer(steps, remainder='drop'))]
    grid = {}
    if family == 'linear':
        model = LinearRegression()
    elif family == 'ridge':
        pipeline.append(('scale', StandardScaler()))
        model = Ridge()
        grid = {'estimator__model__alpha': c['ridge_alphas']}
    elif family == 'forest':
        f = c['forest']
        model = RandomForestRegressor(n_estimators=f['n_estimators'],
            max_features=f['max_features'], random_state=f['random_state'], n_jobs=1)
        grid = {'estimator__model__max_depth': f['max_depth'],
                'estimator__model__min_samples_leaf': f['min_samples_leaf']}
    else:
        raise ValueError(f'Unknown model family: {family}')
    pipeline.append(('model', model))
    bounds = c['prediction_range']
    return BoundedRegressor(Pipeline(pipeline), bounds['min'], bounds['max']), grid


def metrics(y, pred):
    return {'mae': float(mean_absolute_error(y, pred)),
            'rmse': float(np.sqrt(mean_squared_error(y, pred))),
            'r2': float(r2_score(y, pred))}


def summarize(predictions, c, out):
    keys = ['target', 'input_set', 'model', 'repeat']
    records = []
    for key, group in predictions.groupby(keys, sort=False):
        if len(group) != c['expected_rows'] or group['student_index'].nunique() != c['expected_rows']:
            raise ValueError('Each repetition must predict each student exactly once.')
        records.append(dict(zip(keys, key), **metrics(group.actual, group.prediction)))
    repeats = pd.DataFrame(records)
    repeats.to_csv(out / 'repeat-metrics.csv', index=False)
    summary = repeats.groupby(keys[:3])[['mae', 'rmse', 'r2']].agg(['mean', 'std', 'min', 'max'])
    summary.columns = ['_'.join(x) for x in summary.columns]
    summary.to_csv(out / 'metrics-summary.csv')
    differences = []
    for target in c['targets']:
        subset = repeats[repeats.target == target]
        for left, right, family in c['comparisons']:
            a = subset[(subset.input_set == left) & (subset.model == family)].set_index('repeat')
            b = subset[(subset.input_set == right) & (subset.model == family)].set_index('repeat')
            for rep in a.index:
                delta = float(b.loc[rep, 'mae'] - a.loc[rep, 'mae'])
                differences.append({'target': target, 'comparison': f'{right} minus {left}',
                    'model': family, 'repeat': rep, 'mae_difference': delta,
                    'relative_mae_change': delta / float(a.loc[rep, 'mae'])})
        for (input_set, family), group in subset[subset.input_set != 'baseline'].groupby(['input_set', 'model']):
            for base in c['baselines']:
                b = subset[(subset.input_set == 'baseline') & (subset.model == base)].set_index('repeat')
                for row in group.itertuples():
                    delta = row.mae - float(b.loc[row.repeat, 'mae'])
                    differences.append({'target': target, 'comparison': f'{input_set}/{family} minus baseline/{base}',
                        'model': family, 'repeat': row.repeat, 'mae_difference': delta,
                        'relative_mae_change': delta / float(b.loc[row.repeat, 'mae'])})
    pd.DataFrame(differences).to_csv(out / 'paired-comparisons.csv', index=False)
    # Plot repetition 1 only: do not pretend repeated predictions are independent students.
    for (target, input_set, family), group in predictions[predictions['repeat'] == 1].groupby(keys[:3]):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.scatter(group.actual, group.prediction, alpha=.6)
        ax.plot([1, 5], [1, 5], color='black', linestyle='--')
        ax.set(xlim=(.9, 5.1), ylim=(.9, 5.1), xlabel='Measured score', ylabel='Predicted score',
               title=f'{target}: {input_set}, {family}\nHeld-out predictions, repetition 1')
        fig.tight_layout()
        fig.savefig(out / f'{target}-{input_set}-{family}.png', dpi=150)
        plt.close(fig)
    report = ['# Experiment results', '', 'Negative paired MAE differences favor the named right-hand/new input set.',
        'Repetition ranges and standard deviations describe stability; they are not confidence intervals.',
        'These are prespecified family evaluations, not an unbiased estimate for an algorithm selected after seeing these results.',
        'No practical or clinical improvement threshold has been established.', '',
        '| Target | Inputs | Model | Mean MAE | Mean RMSE | Mean R-squared |', '|---|---|---|---:|---:|---:|']
    for (target, inputs, family), row in summary.iterrows():
        report.append(f'| {target} | {inputs} | {family} | {row.mae_mean:.4f} | {row.rmse_mean:.4f} | {row.r2_mean:.4f} |')
    (out / 'results.md').write_text('\n'.join(report) + '\n', encoding='utf-8')


def run(c, df, config_path, out):
    out.mkdir(parents=True, exist_ok=False)
    (out / 'config.json').write_text(json.dumps(c, indent=2) + '\n', encoding='utf-8')
    versions = {name: version(name) for name in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat', 'matplotlib']}
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version, 'packages': versions, 'dataset_sha256': sha256(ROOT / c['dataset']),
        'config_sha256': sha256(config_path), 'script_sha256': sha256(__file__),
        'data_preparation': df.attrs.get('readiness', {}),
        'row_count': len(df), 'row_index_note': '1-based SAV row order; no timestamps exported'}
    manifest_path = out / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    records, tuning, folds = [], [], []
    try:
        for rep, seed in enumerate(c['cv']['outer_seeds'], 1):
            outer = KFold(c['cv']['outer_folds'], shuffle=True, random_state=seed)
            for fold, (train, test) in enumerate(outer.split(df), 1):
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i + 1)} for i in test)
                inner = list(KFold(c['cv']['inner_folds'], shuffle=True,
                    random_state=c['cv']['inner_seed'] + rep * 100 + fold).split(train))
                print(f'Repetition {rep}/{len(c["cv"]["outer_seeds"])}, fold {fold}: fitting both targets', flush=True)
                for target in c['targets']:
                    y_train = df[target].iloc[train]
                    y_test = df[target].iloc[test].to_numpy()
                    jobs = [('baseline', base, []) for base in c['baselines']]
                    jobs += [(name, family, cols) for name, cols in c['input_sets'].items()
                             for family in c['models_by_set'][name]]
                    for name, family, cols in jobs:
                        if name == 'baseline':
                            model = DummyRegressor(strategy=family).fit(np.zeros((len(train), 1)), y_train)
                            raw = model.predict(np.zeros((len(test), 1)))
                            pred = raw
                        else:
                            model, grid = make_model(c, cols, family)
                            X_train, X_test = df[cols].iloc[train], df[cols].iloc[test]
                            if grid:
                                search = GridSearchCV(model, grid, scoring='neg_mean_absolute_error',
                                    cv=inner, n_jobs=1, error_score='raise', refit=True)
                                search.fit(X_train, y_train)
                                model = search.best_estimator_
                                tuning.append({'target': target, 'input_set': name, 'model': family,
                                    'repeat': rep, 'fold': fold, 'parameters': search.best_params_,
                                    'inner_mae': float(-search.best_score_)})
                            else:
                                model.fit(X_train, y_train)
                            raw, pred = model.predict_raw(X_test), model.predict(X_test)
                        for idx, actual, prediction, original in zip(test, y_test, pred, raw):
                            records.append({'target': target, 'input_set': name, 'model': family,
                                'repeat': rep, 'fold': fold, 'student_index': int(idx + 1),
                                'actual': float(actual), 'prediction': float(prediction),
                                'raw_prediction': float(original), 'absolute_error': float(abs(actual - prediction)),
                                'clipped': bool(prediction != original)})
        predictions = pd.DataFrame(records)
        predictions.to_csv(out / 'held-out-predictions.csv', index=False)
        pd.DataFrame(folds).to_csv(out / 'outer-folds.csv', index=False)
        (out / 'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        summarize(predictions, c, out)
        if sha256(ROOT / c['dataset']) != manifest['dataset_sha256']:
            raise RuntimeError('Source dataset changed during evaluation.')
        manifest['status'] = 'complete'
    except Exception as exc:
        manifest['status'] = 'failed'
        manifest['error'] = str(exc)
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT / 'analysis/experiment-config.json')
    parser.add_argument('--check-only', action='store_true', help='Validate source data and settings; fit no models.')
    parser.add_argument('--output', type=Path, help='New directory inside the configured output root.')
    args = parser.parse_args()
    c = json.loads(args.config.read_text(encoding='utf-8'))
    validate_config(c)
    df = load_data(c)
    print(f'Validated {len(df)} real students, four input sets, both target formulas.', flush=True)
    print('Reconstructed 3 missing summary-use indicators from original answers; source SAV unchanged.', flush=True)
    readiness_path = ROOT / 'analysis/checks/model-readiness.json'
    readiness_path.write_text(json.dumps(df.attrs['readiness'], indent=2) + '\n', encoding='utf-8')
    if args.check_only:
        return
    base = (ROOT / c['output_root']).resolve()
    out = args.output.resolve() if args.output else base / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    if not out.is_relative_to(base) or out == base:
        raise ValueError('Output must be a new directory beneath the configured model-runs folder.')
    run(c, df, args.config, out)
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
