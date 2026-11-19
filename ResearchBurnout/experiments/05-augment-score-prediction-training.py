"""Training-only local interpolation for continuous-score prediction."""
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin, clone
from sklearn.model_selection import GridSearchCV, KFold

ROOT = Path(__file__).resolve().parents[1]


def import_script(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


training = import_script('training', '01-compare-score-prediction-baselines.py')
priority = import_script('priority', '04-prioritize-high-burnout-score-prediction.py')


def augment(X, y, method, generator, seed):
    if method not in ['none', 'duplicate', 'interpolate']:
        raise ValueError('Unknown augmentation method.')
    values = np.asarray(y, dtype=float)
    if len(X) != len(values) or not np.isfinite(values).all():
        raise ValueError('Invalid training rows.')
    cats = generator['same_categories']
    nums = [col for col in X if col not in cats]
    if not np.isin(X[nums], [1, 2, 3, 4, 5]).all():
        raise ValueError('Expected original 1-5 numeric items.')
    original = X.reset_index(drop=True).copy()
    table = original.assign(score=values, synthetic=False, parent_a=np.asarray(X.index)+1,
        parent_b=np.asarray(X.index)+1, fraction=0.)
    if method == 'none':
        return original, values.copy(), table
    bands = np.where(values < 2, 0, np.where(values < 4, 1, 2))
    numeric_values = X[nums].to_numpy(float)
    category_values = X[cats].to_numpy()
    rng = np.random.default_rng(seed)
    generated = []
    max_count = int(np.bincount(bands, minlength=3).max())
    for band in generator['eligible_bands']:
        indices = np.flatnonzero(bands == band)
        pairs = {}
        for i in indices:
            eligible = []
            for j in indices:
                if i == j or not np.array_equal(category_values[i], category_values[j]):
                    continue
                differences = np.abs(numeric_values[i]-numeric_values[j])
                if (abs(values[i]-values[j]) <= generator['max_absolute_score_gap']
                    and differences.max() <= generator['max_numeric_item_gap']
                    and (differences/4).mean() <= generator['max_mean_normalized_numeric_distance']):
                    eligible.append(((differences/4).mean(), j))
            if eligible:
                pairs[i] = [j for _, j in sorted(eligible)[:generator['nearest_neighbors']]]
        count = min(max_count-len(indices), generator['max_added_per_band_relative_to_real']*len(indices))
        if not pairs:
            continue
        anchors = sorted(pairs)
        for _ in range(max(0, count)):
            a = int(rng.choice(anchors))
            b = int(rng.choice(pairs[a]))
            fraction = float(rng.uniform(*generator['interpolation_fraction']))
            row = X.iloc[a].copy()
            if method == 'interpolate':
                row[nums] = np.floor((1-fraction)*numeric_values[a]
                    +fraction*numeric_values[b]+.5)
                score = (1-fraction)*values[a]+fraction*values[b]
            else:
                score = values[a]
                fraction = 0.
            row = row.to_dict()
            row.update(score=float(score), synthetic=True, parent_a=int(X.index[a]+1),
                parent_b=int(X.index[b]+1), fraction=fraction)
            generated.append(row)
    if generated:
        table = pd.concat([table, pd.DataFrame(generated)], ignore_index=True)
    assert np.isin(table[nums], [1, 2, 3, 4, 5]).all()
    assert table.score.between(1, 5).all()
    assert set(table.parent_a) <= set(np.asarray(X.index)+1)
    assert set(table.parent_b) <= set(np.asarray(X.index)+1)
    return table[list(X)].copy(), table.score.to_numpy(), table


class AugmentedRegressor(RegressorMixin, BaseEstimator):
    def __init__(self, estimator, method='none', generator=None, seed=618033):
        self.estimator = estimator
        self.method = method
        self.generator = generator
        self.seed = seed

    def fit(self, X, y):
        augmented_X, augmented_y, self.training_rows_ = augment(X, y, self.method, self.generator, self.seed)
        self.estimator_ = clone(self.estimator).fit(augmented_X, augmented_y)
        return self

    def predict_raw(self, X):
        return self.estimator_.predict_raw(X)

    def predict(self, X):
        return self.estimator_.predict(X)


def make_model(base, config, cols, family):
    model, grid = training.make_model(base, cols, family)
    # GridSearchCV clones this entire estimator: generation occurs anew inside every inner fit.
    wrapped = AugmentedRegressor(model, generator=config['generator'], seed=config['seed'])
    return wrapped, {'estimator__'+key: values for key, values in grid.items()}


def summarize(predictions, out):
    rows = []
    for key, group in predictions.groupby(['family', 'method', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        rows.append(dict(zip(['family', 'method', 'repeat'], key), **priority.group_metrics(group, 4)))
    repeats = pd.DataFrame(rows)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(['family', 'method']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    pairs = []
    for family, part in repeats.groupby('family'):
        reference = part[part.method == 'none'].set_index('repeat')
        duplicate = part[part.method == 'duplicate'].set_index('repeat')
        for method in ['duplicate', 'interpolate']:
            for row in part[part.method == method].itertuples():
                pairs.append({'family': family, 'method': method, 'repeat': row.repeat,
                    'mae_minus_no_augmentation': row.mae-reference.loc[row.repeat, 'mae'],
                    'high_mae_minus_no_augmentation': row.high_mae-reference.loc[row.repeat, 'high_mae'],
                    'mae_minus_duplication': row.mae-duplicate.loc[row.repeat, 'mae']})
    pairs = pd.DataFrame(pairs)
    pairs.to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Synthetic-data regression follow-up', '',
        'Small B inputs; primary continuous 12-item burnout score. Same original five outer folds repeated five times, four inner folds.',
        'Only real excluded students are evaluated. Synthetic target values are interpolated, not observed questionnaire scores.',
        'Neighbor search, generation, encoding, scaling and ridge tuning occur inside each training fit. No synthetic records enter evaluation.',
        'Low <2 and High >=4 are descriptive generation strata, not classification targets or clinical categories.', '',
        'The lower-score error below uses actual scores <2.5, consistent with previous regression diagnostics; generation uses the stricter <2 band.', '',
        '| Family | Training method | Overall MAE | RMSE | High-score MAE | High underestimation | Lower-score MAE |',
        '|---|---|---:|---:|---:|---:|---:|']
    for (family, method), row in summary.iterrows():
        lines.append(f'| {family} | {method} | {row.mae:.4f} | {row.rmse:.4f} | {row.high_mae:.4f} | '
            f'{row.high_mean_underestimation:.4f} | {row.lower_mae:.4f} |')
    lines += ['', '## Paired changes', '',
        'Negative changes mean smaller errors. Repetitions reuse the same real students, so are not independent replications.', '',
        '| Family | Method | MAE change vs none | High MAE change vs none | MAE change vs duplicates | Repetitions with lower MAE vs none |',
        '|---|---|---:|---:|---:|---:|']
    for (family, method), group in pairs.groupby(['family', 'method']):
        lines.append(f'| {family} | {method} | {group.mae_minus_no_augmentation.mean():+.4f} | '
            f'{group.high_mae_minus_no_augmentation.mean():+.4f} | {group.mae_minus_duplication.mean():+.4f} | '
            f'{(group.mae_minus_no_augmentation < 0).sum()}/{len(group)} |')
    lines += ['', '## Generation assumptions and limits', '',
        'Eligible neighbors share sleep/study-hour categories and sampling band, have score gaps <=.75, numeric item gaps <=2, and mean normalized numeric distance <=.25. '
        'Choose among three nearest eligible neighbors; interpolate both inputs and target with a common fraction .2-.8. '
        'Round 1-5 input items to legal integer values. Categories remain unchanged. If no eligible pair exists, generate nothing for that band.',
        'Only Low/High strata are augmented, with at most twice the real stratum count added and no more than needed to reach the largest stratum count. '
        'This changes training emphasis. Duplication uses the same eligible anchors/counts as a control; any gain may be reweighting rather than new information.',
        'Rounded input vectors can repeat existing vectors. Generated records are pseudo-observations, not actual students, validated response patterns, or independent evidence. '
        'Their continuous labels need not be attainable exact 12-item questionnaire means. Local interpolation is an assumption about the response surface, not confirmed psychological truth.',
        'Do not append these records to the survey export or SPSS reliability/correlation analyses. All saved generated rows have training-fold parent provenance. '
        'No final deployment model is saved. This follow-up was selected after previous results and needs independent confirmation.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'experiments/05-augment-score-prediction-training-settings.json'
    config = json.loads(config_path.read_text())
    reference = ROOT/config['reference_run']
    assert json.loads((reference/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    assert config['target'] == 'burnout_score' and config['input_set'] == 'small_b'
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in [ROOT/base['dataset'],
        reference/'config.json', reference/'held-out-predictions.csv', reference/'outer-folds.csv']}
    data = training.load_data(base)
    old = pd.read_csv(reference/'held-out-predictions.csv')
    cols = base['input_sets'][config['input_set']]
    y = data[config['target']]
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    (out/'config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')
    (out/'reference-config.json').write_text(json.dumps(base, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'engine_sha256': training.sha256(training.__file__),
        'metric_helper_sha256': training.sha256(priority.__file__), 'source_sha256': hashes,
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']},
        'interpretation': config['interpretation'], 'real_participants': 97}
    path = out/'manifest.json'
    path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, generated, counts, tuning, folds = [], [], [], [], []
    try:
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(KFold(base['cv']['outer_folds'], shuffle=True, random_state=seed).split(data), 1):
                print(f'Repetition {rep}/5, fold {fold}/5: real/duplicate/interpolated regression', flush=True)
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1)} for i in test)
                inner = list(KFold(base['cv']['inner_folds'], shuffle=True,
                    random_state=base['cv']['inner_seed']+rep*100+fold).split(train))
                for family in config['families']:
                    for method in config['methods']:
                        model, grid = make_model(base, config, cols, family)
                        model.set_params(method=method)
                        if grid:
                            search = GridSearchCV(model, grid, cv=inner, scoring='neg_mean_absolute_error',
                                n_jobs=1, error_score='raise', refit=True)
                            search.fit(data[cols].iloc[train], y.iloc[train])
                            model = search.best_estimator_
                            tuning.append({'family': family, 'method': method, 'repeat': rep, 'fold': fold,
                                'parameters': search.best_params_, 'inner_mae': float(-search.best_score_)})
                        else:
                            model.fit(data[cols].iloc[train], y.iloc[train])
                        raw, pred = model.predict_raw(data[cols].iloc[test]), model.predict(data[cols].iloc[test])
                        if method == 'none':
                            reference_rows = old[(old.target == config['target']) & (old.input_set == 'small_b') &
                                (old.model == family) & (old['repeat'] == rep) & (old.fold == fold)].set_index('student_index')
                            assert len(reference_rows) == len(test)
                            if not np.allclose(pred, reference_rows.loc[test+1, 'prediction'], atol=1e-8, rtol=1e-8):
                                raise ValueError('Unaugmented predictions differ from original experiment.')
                        rows = model.training_rows_
                        assert not set(rows.parent_a) & set(test+1)
                        assert not set(rows.parent_b) & set(test+1)
                        counts.append({'family': family, 'method': method, 'repeat': rep, 'fold': fold,
                            'real_rows': len(train), 'synthetic_rows': int(rows.synthetic.sum()),
                            'unique_added_input_vectors': int(rows[rows.synthetic][cols].drop_duplicates().shape[0])})
                        if method != 'none':
                            generated.append(rows.assign(family=family, method=method, repeat=rep, fold=fold))
                        for idx, actual, prediction, unbounded in zip(test, y.iloc[test], pred, raw):
                            predictions.append({'family': family, 'method': method, 'repeat': rep, 'fold': fold,
                                'student_index': int(idx+1), 'actual': float(actual), 'prediction': float(prediction),
                                'raw_prediction': float(unbounded), 'absolute_error': float(abs(actual-prediction))})
        fold_table = pd.DataFrame(folds)
        order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        result = pd.DataFrame(predictions)
        assert not result.duplicated(['family', 'method', 'repeat', 'student_index']).any()
        result.to_csv(out/'held-out-real-predictions.csv', index=False)
        pd.concat(generated, ignore_index=True).to_csv(out/'outer-training-real-and-synthetic.csv', index=False)
        pd.DataFrame(counts).to_csv(out/'generation-counts.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        summarize(result, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, ordinary_models_reproduced=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
