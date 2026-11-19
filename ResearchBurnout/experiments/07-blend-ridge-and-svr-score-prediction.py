"""Nested selection of a weighted-ridge / high-priority SVR prediction blend."""
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('kernels', Path(__file__).with_name('06-compare-svr-and-kernel-score-prediction.py'))
kernels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernels)
priority, training = kernels.priority, kernels.training


def fit_ridge(base, cols, X, y, choice):
    return priority.fit_ridge(base, cols, X, y, choice['alpha'], choice['factor'], 4)


def fit_svr(X, y, choice):
    return kernels.estimator('svr', choice['parameters']).fit(X, y,
        sample_weight=priority.weights(y, choice['factor'], 4))


def choose_blend(y, ridge, svr, ordinary_mae, config):
    high = np.asarray(y) >= 4
    candidates = []
    for share in config['svr_shares']:
        prediction = (1-share)*ridge+share*svr
        error = np.abs(np.asarray(y)-prediction)
        candidates.append({'svr_share': share, 'mae': float(error.mean()),
            'high_mae': float(error[high].mean()) if high.any() else None})
    eligible = [c for c in candidates if c['mae'] <= ordinary_mae+config['inner_overall_mae_tolerance']+1e-12]
    assert eligible and any(c['svr_share'] == 0 for c in eligible)
    chosen = min(eligible, key=lambda c: (c['high_mae'] if high.any() else c['mae'], c['mae'], c['svr_share']))
    return chosen, candidates


def summarize(result, out):
    records, diagnostics = [], []
    for (procedure, rep), group in result.groupby(['procedure', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        high = group.actual >= 4
        records.append({'procedure': procedure, 'repeat': rep, **priority.group_metrics(group, 4),
            'high_within_half_point': float((group.loc[high, 'absolute_error'] <= .5).mean())})
    repeats = pd.DataFrame(records)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby('procedure').mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    wide = result[result.procedure.isin(['weighted_ridge', 'high_priority_svr'])].pivot(
        index=['repeat', 'student_index', 'actual'], columns='procedure', values='prediction').reset_index()
    wide['ridge_error'] = wide.weighted_ridge-wide.actual
    wide['svr_error'] = wide.high_priority_svr-wide.actual
    wide.to_csv(out/'endpoint-error-comparison.csv', index=False)
    for rep, group in wide.groupby('repeat'):
        for label, part in [('all', group), ('high', group[group.actual >= 4])]:
            a, b = part.ridge_error, part.svr_error
            diagnostics.append({'repeat': rep, 'group': label, 'n': len(part),
                'signed_error_correlation': float(a.corr(b)),
                'opposite_error_sign_fraction': float(((a*b) < 0).mean()),
                'both_errors_above_half_point': float(((a.abs() > .5) & (b.abs() > .5)).mean()),
                'ridge_smaller_error_fraction': float((a.abs() < b.abs()).mean()),
                'svr_smaller_error_fraction': float((b.abs() < a.abs()).mean())})
    diagnostics = pd.DataFrame(diagnostics)
    diagnostics.to_csv(out/'error-complementarity.csv', index=False)
    changes = []
    for row in repeats[repeats.procedure.isin(['selected_blend', 'fixed_half_blend'])].itertuples():
        for endpoint in ['weighted_ridge', 'high_priority_svr']:
            ref = repeats[(repeats.procedure == endpoint) & (repeats['repeat'] == row.repeat)].iloc[0]
            changes.append({'procedure': row.procedure, 'reference': endpoint, 'repeat': row.repeat,
                'mae_difference': row.mae-ref.mae, 'high_mae_difference': row.high_mae-ref.high_mae})
    pd.DataFrame(changes).to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Ridge/SVR ensemble experiment', '',
        'Primary continuous burnout_score, 97 real students, original five outer folds repeated five times with four inner folds.',
        'Ridge uses Small B; SVR uses Broad D. No new questionnaire variables, BAT predictors or synthetic students.',
        'Base-model parameters and high-score weights follow the previous inner-selection procedures. Their inner out-of-fold predictions select the mixing share.',
        'Blend = (1 - SVR share) * clipped ridge prediction + SVR share * clipped SVR prediction; shares 0/.25/.5/.75/1.',
        'Choose minimum inner High MAE subject to overall MAE <= ordinary ridge inner overall MAE + .05; ties favor overall MAE then smaller SVR share.',
        'Endpoint shares are allowed, so selection can return a single model. The .05 inner tolerance is not an outer-error guarantee.',
        'Fixed half blend is a separately reported preselected reference. All outer evaluation records are real students excluded from training.', '',
        '| Procedure | Overall MAE | High MAE | High underestimation | Lower MAE | High within .5 |',
        '|---|---:|---:|---:|---:|---:|']
    for procedure, row in summary.iterrows():
        lines.append(f'| {procedure} | {row.mae:.4f} | {row.high_mae:.4f} | {row.high_mean_underestimation:.4f} | '
            f'{row.lower_mae:.4f} | {row.high_within_half_point:.1%} |')
    lines += ['', '## Do the models make different mistakes?', '',
        'These descriptive diagnostics use excluded-student predictions and do not choose settings. Values average five repetition metrics.', '',
        '| Students | Error correlation | Opposite error signs | Both errors >.5 |', '|---|---:|---:|---:|']
    for label, row in diagnostics.groupby('group').mean(numeric_only=True).iterrows():
        lines.append(f'| {label} | {row.signed_error_correlation:.3f} | {row.opposite_error_sign_fraction:.1%} | {row.both_errors_above_half_point:.1%} |')
    lines += ['', 'High means measured >=4; lower means <2.5. Descriptive score groups and accuracy thresholds are not clinical criteria.',
        'Repetitions reuse the same students. This follow-up was selected after previous evaluation; best-looking outer results do not provide independent validation of a winner.',
        'Inner validation is reused to select base hyperparameters and mixing share; only the excluded outer groups evaluate the complete procedure.',
        'Previous endpoint predictions and original outer assignments must reproduce or execution stops. Source data and earlier runs are unchanged. No deployment model saved.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'experiments/07-blend-ridge-and-svr-score-prediction-settings.json'
    config = json.loads(config_path.read_text())
    reference, ridge_run, svr_run = [ROOT/config[key] for key in ['reference_run', 'ridge_run', 'svr_run']]
    for folder in [reference, ridge_run, svr_run]:
        assert json.loads((folder/'manifest.json').read_text())['status'] == 'complete'
    base = json.loads((reference/'config.json').read_text())
    ridge_config = json.loads((ridge_run/'config.json').read_text())
    svr_config = json.loads((svr_run/'config.json').read_text())
    data = training.load_data(base)
    paths = [ROOT/base['dataset'], reference/'config.json', reference/'outer-folds.csv',
        ridge_run/'config.json', ridge_run/'held-out-predictions.csv', svr_run/'config.json', svr_run/'held-out-predictions.csv']
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in paths}
    old_ridge = pd.read_csv(ridge_run/'held-out-predictions.csv')
    old_ridge = old_ridge[(old_ridge.target == config['target']) & (old_ridge.model == 'high_priority_ridge')]
    old_svr = pd.read_csv(svr_run/'held-out-predictions.csv')
    old_svr = old_svr[(old_svr.input_set == config['svr_inputs']) & (old_svr.family == 'svr') & (old_svr.procedure == 'high_priority')]
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    for name, settings in [('config', config), ('reference-config', base), ('ridge-config', ridge_config), ('svr-config', svr_config)]:
        (out/f'{name}.json').write_text(json.dumps(settings, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'engine_sha256': training.sha256(training.__file__),
        'ridge_helper_sha256': training.sha256(priority.__file__), 'kernel_helper_sha256': training.sha256(kernels.__file__),
        'source_sha256': hashes, 'real_participants': 97,
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']}}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, folds = [], [], []
    try:
        ridge_cols, svr_cols = [base['input_sets'][config[key]] for key in ['ridge_inputs', 'svr_inputs']]
        assert not any(col.startswith('BAT') or 'burnout' in col for col in ridge_cols+svr_cols)
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(KFold(base['cv']['outer_folds'], shuffle=True, random_state=seed).split(data), 1):
                print(f'Repetition {rep}/5, fold {fold}/5: tune ridge, SVR and blend inside training', flush=True)
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1)} for i in test)
                inner = list(KFold(base['cv']['inner_folds'], shuffle=True,
                    random_state=base['cv']['inner_seed']+rep*100+fold).split(train))
                Xridge, Xsvr, y = data[ridge_cols].iloc[train], data[svr_cols].iloc[train], data[config['target']].iloc[train]
                ordinary, ridge_choice, ridge_candidates = priority.inner_select(base, ridge_config, ridge_cols, Xridge, y, inner)
                prepared = []
                for tr, va in inner:
                    Xt, Xv = kernels.transform(base, svr_cols, Xsvr.iloc[tr], Xsvr.iloc[va])
                    prepared.append((tr, va, Xt, Xv))
                svr_choices, svr_candidates = kernels.inner_search(svr_config, 'svr', prepared, y)
                svr_choice = svr_choices['high_priority']
                ridge_oof, svr_oof = np.full(len(y), np.nan), np.full(len(y), np.nan)
                for tr, va, Xt, Xv in prepared:
                    fitted_ridge = fit_ridge(base, ridge_cols, Xridge.iloc[tr], y.iloc[tr], ridge_choice)
                    ridge_oof[va] = priority.predict(fitted_ridge, Xridge.iloc[va])[1]
                    svr_oof[va] = np.clip(fit_svr(Xt, y.iloc[tr], svr_choice).predict(Xv), 1, 5)
                assert np.isfinite(ridge_oof).all() and np.isfinite(svr_oof).all()
                assert np.isclose(np.abs(y.to_numpy()-ridge_oof).mean(), ridge_choice['overall_mae'])
                assert np.isclose(np.abs(y.to_numpy()-svr_oof).mean(), svr_choice['mae'])
                blend_choice, blend_candidates = choose_blend(y, ridge_oof, svr_oof, ordinary['overall_mae'], config)
                tuning.append({'repeat': rep, 'fold': fold, 'ridge_choice': ridge_choice, 'svr_choice': svr_choice,
                    'blend_choice': blend_choice, 'blend_candidates': blend_candidates,
                    'ordinary_ridge_inner_mae': ordinary['overall_mae'], 'ridge_candidates': ridge_candidates, 'svr_candidates': svr_candidates})
                ridge_pred = priority.predict(fit_ridge(base, ridge_cols, Xridge, y, ridge_choice), data[ridge_cols].iloc[test])[1]
                Xt, Xtest = kernels.transform(base, svr_cols, Xsvr, data[svr_cols].iloc[test])
                svr_pred = np.clip(fit_svr(Xt, y, svr_choice).predict(Xtest), 1, 5)
                for old, predicted in [(old_ridge, ridge_pred), (old_svr, svr_pred)]:
                    rows = old[(old['repeat'] == rep) & (old.fold == fold)].set_index('student_index')
                    assert len(rows) == len(test)
                    if not np.allclose(predicted, rows.loc[test+1, 'prediction'], atol=1e-8, rtol=1e-8):
                        raise ValueError('Endpoint predictions differ from prior experiment.')
                share = blend_choice['svr_share']
                outputs = {'weighted_ridge': ridge_pred, 'high_priority_svr': svr_pred,
                    'fixed_half_blend': .5*ridge_pred+.5*svr_pred, 'selected_blend': (1-share)*ridge_pred+share*svr_pred}
                for procedure, values in outputs.items():
                    assert np.isfinite(values).all() and ((values >= 1) & (values <= 5)).all()
                    for idx, actual, pred in zip(test, data[config['target']].iloc[test], values):
                        predictions.append({'procedure': procedure, 'repeat': rep, 'fold': fold,
                            'student_index': int(idx+1), 'actual': float(actual), 'prediction': float(pred),
                            'absolute_error': float(abs(actual-pred))})
        fold_table = pd.DataFrame(folds)
        order = ['repeat', 'student_index']
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        result = pd.DataFrame(predictions)
        assert not result.duplicated(['procedure', 'repeat', 'student_index']).any()
        result.to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        summarize(result, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, endpoints_reproduced=True, original_folds_reproduced=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
