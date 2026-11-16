"""Nested Elastic Net and original-question selection before SVR."""
from collections import Counter
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import KFold, ParameterGrid

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('kernels', Path(__file__).with_name('train-kernels.py'))
kernels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernels)
priority, training = kernels.priority, kernels.training


def encode(base, cols, train, valid):
    wrapped, _ = training.make_model(base, cols, 'ridge')
    preprocessing = wrapped.estimator[:-1]
    Xt, Xv = preprocessing.fit_transform(train), preprocessing.transform(valid)
    cats = [c for c in cols if c in base['category_levels']]
    groups = [c for c in cats for _ in base['category_levels'][c][1:]]+[c for c in cols if c not in cats]
    assert len(groups) == Xt.shape[1] and np.isfinite(Xt).all() and np.isfinite(Xv).all()
    return Xt, Xv, np.asarray(groups)


def elastic(config, parameters):
    return ElasticNet(**parameters, **config['solver'])


def ranked_questions(config, X, y, w, groups, cols):
    selector = elastic(config, {k: config['selector'][k] for k in ['alpha', 'l1_ratio']}).fit(X, y, sample_weight=w)
    importance = {c: float(np.linalg.norm(selector.coef_[groups == c])/np.sqrt((groups == c).sum())) for c in cols}
    return sorted(cols, key=lambda c: -importance[c])


def candidate_grid(config, kernel_config, family, cols):
    params = config['elastic_net'] if family == 'elastic_net' else kernel_config['grids']['svr']
    counts = [len(cols)] if family == 'elastic_net' else sorted(set(len(cols) if n == 'all' else min(n, len(cols)) for n in config['selector']['counts']))
    return [{'factor': f, 'parameters': p, 'question_count': n}
        for f in config['relative_high_weights'] for p in ParameterGrid(params) for n in counts]


def fit_model(config, family, X, y, w, parameters):
    model = elastic(config, parameters) if family == 'elastic_net' else kernels.estimator('svr', parameters)
    return model.fit(X, y, sample_weight=w)


def inner_search(config, kernel_config, base, cols, X, y, inner, family):
    prepared = {}
    for factor in config['relative_high_weights']:
        prepared[factor] = []
        for tr, va in inner:
            assert not set(tr) & set(va)
            Xt, Xv, groups = encode(base, cols, X.iloc[tr], X.iloc[va])
            w = priority.weights(y.iloc[tr], factor, 4)
            ranking = ranked_questions(config, Xt, y.iloc[tr], w, groups, cols) if family == 'selected_svr' else cols
            prepared[factor].append((tr, va, Xt, Xv, groups, w, ranking))
    candidates = []
    high = y.to_numpy() >= 4
    for index, candidate in enumerate(candidate_grid(config, kernel_config, family, cols)):
        oof, fold_errors = np.full(len(y), np.nan), []
        for tr, va, Xt, Xv, groups, w, ranking in prepared[candidate['factor']]:
            mask = np.isin(groups, ranking[:candidate['question_count']])
            model = fit_model(config, family, Xt[:, mask], y.iloc[tr], w, candidate['parameters'])
            pred = np.clip(model.predict(Xv[:, mask]), 1, 5)
            oof[va] = pred
            fold_errors.append(float(np.abs(y.iloc[va].to_numpy()-pred).mean()))
        assert np.isfinite(oof).all()
        error = np.abs(y.to_numpy()-oof)
        candidates.append({**candidate, 'grid_index': index, 'fold_mean_mae': float(np.mean(fold_errors)),
            'mae': float(error.mean()), 'high_mae': float(error[high].mean()) if high.any() else None})
    ordinary, high_priority = kernels.select(candidates, config['inner_overall_mae_tolerance'])
    return {'ordinary': ordinary, 'high_priority': high_priority}, candidates


def summarize(result, diagnostics, features, out):
    rows = []
    for key, group in result.groupby(['input_set', 'family', 'procedure', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        high = group.actual >= 4
        rows.append(dict(zip(['input_set', 'family', 'procedure', 'repeat'], key),
            **priority.group_metrics(group, 4), high_within_half_point=float((group.loc[high, 'absolute_error'] <= .5).mean())))
    repeats = pd.DataFrame(rows)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(['input_set', 'family', 'procedure']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    diag = pd.DataFrame(diagnostics)
    diag.to_csv(out/'training-validation-diagnostics.csv', index=False)
    diag_summary = diag.groupby(['input_set', 'family', 'procedure']).mean(numeric_only=True).drop(columns=['repeat', 'fold'])
    diag_summary.to_csv(out/'diagnostics-summary.csv')
    pd.DataFrame(features).to_csv(out/'selected-question-frequency.csv', index=False)
    paired = []
    for row in repeats[repeats.family.isin(['elastic_net', 'selected_svr'])].itertuples():
        for ref_family, ref_procedure in [('reference_ridge', 'ordinary'), ('reference_svr', row.procedure)]:
            ref = repeats[(repeats.input_set == row.input_set) & (repeats.family == ref_family)
                & (repeats.procedure == ref_procedure) & (repeats['repeat'] == row.repeat)].iloc[0]
            paired.append({'input_set': row.input_set, 'family': row.family, 'procedure': row.procedure,
                'reference': ref_family+'/'+ref_procedure, 'repeat': row.repeat,
                'mae_difference': row.mae-ref.mae, 'high_mae_difference': row.high_mae-ref.high_mae})
    pd.DataFrame(paired).to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Existing-question selection experiment', '',
        'Primary continuous target, 97 real students, original five outer folds repeated five times with four inner folds.',
        'Elastic Net and question-selected SVR on Small B/Broad D. No new survey features, BAT predictors or synthetic records.',
        'Preprocessing, Elastic Net ranking, model tuning and weighting use training-only data inside inner folds.',
        'Selected SVR ranks whole original questions by grouped standardized Elastic Net coefficient strength; it keeps 4/8/all questions (deduplicated when counts coincide).',
        'Ordinary selection minimizes mean inner-fold MAE with factor 1. High-priority minimizes pooled High MAE within .05 pooled overall MAE of ordinary; factors 1/2/4.', '',
        '| Inputs | Family | Procedure | Overall MAE | High MAE | Lower MAE | High within .5 |',
        '|---|---|---|---:|---:|---:|---:|']
    for (inputs, family, procedure), row in summary.iterrows():
        lines.append(f'| {inputs} | {family} | {procedure} | {row.mae:.4f} | {row.high_mae:.4f} | {row.lower_mae:.4f} | {row.high_within_half_point:.1%} |')
    lines += ['', '## Training versus excluded-student error', '',
        'These are mean fold errors, not pooled repetition metrics. Training errors use the fitted training students and are optimistically biased.',
        'A gap describes fit versus evaluation performance; it cannot by itself prove that memorization, noise or insufficient inputs caused the errors.', '',
        '| Inputs | Family | Procedure | Training MAE | Inner selected MAE | Outer MAE | Outer minus training |',
        '|---|---|---|---:|---:|---:|---:|']
    for (inputs, family, procedure), row in diag_summary.iterrows():
        lines.append(f'| {inputs} | {family} | {procedure} | {row.training_mae:.4f} | {row.inner_mae:.4f} | {row.outer_mae:.4f} | {row.gap:.4f} |')
    lines += ['', 'High actual >=4; lower actual <2.5. Descriptive groups and within-.5 thresholds are not clinical criteria.',
        'References are copied previously saved predictions; the ensemble reference uses the existing union of inputs.',
        'All-question SVR remains eligible, so selected SVR is a selection procedure and does not necessarily drop inputs in every fit.',
        'Ranking uses L2 coefficient norm per question divided by sqrt(encoded column count); categories stay together. Zero-importance ties retain original question order.',
        'Repeated evaluations reuse the same students. Follow-up was proposed after previous results; outer-score comparisons do not independently validate a selected final model.',
        'Original data and earlier runs stay unchanged. No deployment model or weights saved.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    warnings.filterwarnings('error', category=ConvergenceWarning)
    path = ROOT/'analysis/feature-selection-config.json'
    config = json.loads(path.read_text())
    reference, kernel_run, ensemble_run = [ROOT/config[k] for k in ['reference_run', 'kernel_run', 'ensemble_run']]
    for folder in [reference, kernel_run, ensemble_run]:
        assert json.loads((folder/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    kernel_config = json.loads((kernel_run/'config.json').read_text())
    data = training.load_data(base)
    sources = [ROOT/base['dataset'], reference/'config.json', reference/'outer-folds.csv', reference/'held-out-predictions.csv',
        kernel_run/'config.json', kernel_run/'held-out-predictions.csv', ensemble_run/'held-out-predictions.csv']
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in sources}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    for name, settings in [('config', config), ('reference-config', base), ('kernel-config', kernel_config)]:
        (out/f'{name}.json').write_text(json.dumps(settings, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': hashes, 'script_sha256': training.sha256(__file__), 'engine_sha256': training.sha256(training.__file__),
        'kernel_helper_sha256': training.sha256(kernels.__file__), 'metric_helper_sha256': training.sha256(priority.__file__),
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']}, 'real_participants': 97}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, folds, diagnostics = [], [], [], []
    frequencies = Counter()
    try:
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(KFold(base['cv']['outer_folds'], shuffle=True, random_state=seed).split(data), 1):
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1)} for i in test)
                inner = list(KFold(base['cv']['inner_folds'], shuffle=True,
                    random_state=base['cv']['inner_seed']+rep*100+fold).split(train))
                for inputs in config['input_sets']:
                    print(f'Repetition {rep}/5, fold {fold}/5, {inputs}: Elastic Net and question-selected SVR', flush=True)
                    cols = base['input_sets'][inputs]
                    assert not any(c.startswith('BAT') or 'burnout' in c for c in cols)
                    X, y = data[cols].iloc[train], data[config['target']].iloc[train]
                    for family in ['elastic_net', 'selected_svr']:
                        choices, candidates = inner_search(config, kernel_config, base, cols, X, y, inner, family)
                        selected = {}
                        for procedure, choice in choices.items():
                            Xt, Xv, groups = encode(base, cols, X, data[cols].iloc[test])
                            w = priority.weights(y, choice['factor'], 4)
                            ranking = ranked_questions(config, Xt, y, w, groups, cols) if family == 'selected_svr' else cols
                            selected_cols = ranking[:choice['question_count']]
                            mask = np.isin(groups, selected_cols)
                            assert mask.any() and set(selected_cols) <= set(cols)
                            fitted = fit_model(config, family, Xt[:, mask], y, w, choice['parameters'])
                            if family == 'elastic_net':
                                selected_cols = [c for c in cols if np.any(np.abs(fitted.coef_[groups[mask] == c]) > 1e-10)]
                            selected[procedure] = selected_cols
                            for c in selected_cols:
                                frequencies[(inputs, family, procedure, c)] += 1
                            pred = np.clip(fitted.predict(Xv[:, mask]), 1, 5)
                            train_pred = np.clip(fitted.predict(Xt[:, mask]), 1, 5)
                            assert np.isfinite(pred).all() and np.isfinite(train_pred).all()
                            training_mae = float(np.abs(y.to_numpy()-train_pred).mean())
                            outer_mae = float(np.abs(data[config['target']].iloc[test].to_numpy()-pred).mean())
                            diagnostics.append({'input_set': inputs, 'family': family, 'procedure': procedure, 'repeat': rep, 'fold': fold,
                                'training_mae': training_mae, 'inner_mae': choice['mae'], 'outer_mae': outer_mae,
                                'gap': outer_mae-training_mae, 'selected_questions': len(selected_cols)})
                            for idx, actual, predicted in zip(test, data[config['target']].iloc[test], pred):
                                predictions.append({'input_set': inputs, 'family': family, 'procedure': procedure,
                                    'repeat': rep, 'fold': fold, 'student_index': int(idx+1), 'actual': float(actual),
                                    'prediction': float(predicted), 'absolute_error': float(abs(actual-predicted))})
                        tuning.append({'input_set': inputs, 'family': family, 'repeat': rep, 'fold': fold,
                            'chosen': choices, 'selected_questions': selected, 'candidates': candidates})
        fold_table = pd.DataFrame(folds)
        order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        result = pd.DataFrame(predictions)
        ridge = pd.read_csv(reference/'held-out-predictions.csv')
        ridge = ridge[(ridge.target == config['target']) & ridge.input_set.isin(config['input_sets']) & (ridge.model == 'ridge')].copy()
        ridge['family'], ridge['procedure'] = 'reference_ridge', 'ordinary'
        svr = pd.read_csv(kernel_run/'held-out-predictions.csv')
        svr = svr[(svr.family == 'svr') & svr.input_set.isin(config['input_sets'])].copy()
        svr['family'] = 'reference_svr'
        ensemble = pd.read_csv(ensemble_run/'held-out-predictions.csv')
        ensemble = ensemble[ensemble.procedure == 'fixed_half_blend'].copy()
        ensemble['input_set'], ensemble['family'], ensemble['procedure'] = 'combined_existing', 'reference_ensemble', 'fixed_half'
        for frame in [ridge, svr, ensemble]:
            result = pd.concat([result, frame[list(result)]], ignore_index=True)
        assert not result.duplicated(['input_set', 'family', 'procedure', 'repeat', 'student_index']).any()
        assert np.allclose(result.actual, data[config['target']].iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        features = [dict(zip(['input_set', 'family', 'procedure', 'question'], key), outer_fit_count=count, total_outer_fits=25)
            for key, count in frequencies.items()]
        summarize(result, diagnostics, features, out)
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
