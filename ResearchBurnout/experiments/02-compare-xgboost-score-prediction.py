"""Separate exploratory XGBoost follow-up; original model results stay read-only."""
import argparse
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd

SPEC = importlib.util.spec_from_file_location('training', Path(__file__).with_name('01-compare-score-prediction-baselines.py'))
training = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(training)
ROOT = training.ROOT


def validate_followup(c):
    training.validate_config(c)
    reference = ROOT / c['reference_run']
    manifest = json.loads((reference / 'manifest.json').read_text())
    original = json.loads((reference / 'config.json').read_text())
    if manifest['status'] != 'complete':
        raise ValueError('The reference run must be complete.')
    for key in ['dataset_sha256', 'targets', 'input_sets', 'category_levels',
                'encoding', 'cv', 'prediction_range', 'baselines']:
        if c[key] != original[key]:
            raise ValueError(f'Follow-up differs from original comparison: {key}')
    if c['experiment_id'] != 'xgboost-followup-v1' or c['models_by_set'] != {
        'small_a': ['xgboost'], 'small_b': ['xgboost'], 'broad_c': [], 'broad_d': []}:
        raise ValueError('Expected XGBoost on Small A/B only.')
    if c['output_root'] != 'results/02-xgboost-score-prediction':
        raise ValueError('Follow-up must use the separate XGBoost output folder.')
    if c['comparisons'] != [['small_a', 'small_b', 'xgboost']]:
        raise ValueError('Expected one paired Small B versus Small A comparison.')
    # Do not silently compare with modified result files from a different experiment.
    if manifest['dataset_sha256'] != c['dataset_sha256']:
        raise ValueError('Reference source dataset differs.')
    return reference


def compare_with_original(c, out, reference):
    old = pd.read_csv(reference / 'held-out-predictions.csv')
    new = pd.read_csv(out / 'held-out-predictions.csv')
    folds = pd.read_csv(reference / 'outer-folds.csv').sort_values(['repeat', 'student_index']).reset_index(drop=True)
    new_folds = pd.read_csv(out / 'outer-folds.csv').sort_values(['repeat', 'student_index']).reset_index(drop=True)
    pd.testing.assert_frame_equal(folds, new_folds)
    keys = ['target', 'input_set', 'repeat', 'student_index', 'fold']
    ridge = old[(old.model == 'ridge') & old.input_set.isin(['small_a', 'small_b'])]
    xgb = new[new.model == 'xgboost']
    matched = xgb.merge(ridge, on=keys, suffixes=('_xgb', '_ridge'), validate='one_to_one')
    if len(matched) != len(xgb) or not np.allclose(matched.actual_xgb, matched.actual_ridge):
        raise ValueError('Predictions do not align with the original students and scores.')
    paired = []
    for key, group in matched.groupby(['target', 'input_set', 'repeat']):
        paired.append(dict(zip(['target', 'input_set', 'repeat'], key),
            xgboost_mae=group.absolute_error_xgb.mean(), ridge_mae=group.absolute_error_ridge.mean(),
            mae_difference=group.absolute_error_xgb.mean()-group.absolute_error_ridge.mean()))
    pairs = pd.DataFrame(paired)
    pairs.to_csv(out / 'xgboost-versus-original-ridge.csv', index=False)
    selected = pd.concat([ridge, xgb], ignore_index=True)
    selected['signed_error'] = selected.prediction-selected.actual
    selected['score_range'] = np.where(selected.actual < 2.5, 'below_2.5',
        np.where(selected.actual >= 4, '4_and_above', '2.5_to_below_4'))
    records = []
    for key, group in selected.groupby(['target', 'input_set', 'model', 'repeat', 'score_range']):
        records.append(dict(zip(['target', 'input_set', 'model', 'repeat', 'score_range'], key),
            n_students=group.student_index.nunique(), mae=group.absolute_error.mean(),
            mean_signed_error=group.signed_error.mean(),
            fraction_error_over_1=(group.absolute_error > 1).mean()))
    ranges = pd.DataFrame(records)
    ranges.to_csv(out / 'score-range-errors-by-repeat.csv', index=False)
    lines = ['# XGBoost follow-up comparison', '',
        'Exploratory follow-up chosen after inspecting the original results; not independent confirmation.',
        'Same real students, target definitions, outer folds and inner splits. No augmentation.',
        'Negative XGBoost-minus-ridge MAE differences favor XGBoost.', '',
        '| Outcome | Inputs | Ridge MAE | XGBoost MAE | Difference | Repetitions XGBoost improved |',
        '|---|---|---:|---:|---:|---:|']
    for (target, inputs), group in pairs.groupby(['target', 'input_set']):
        lines.append(f'| {target} | {inputs} | {group.ridge_mae.mean():.4f} | '
            f'{group.xgboost_mae.mean():.4f} | {group.mae_difference.mean():+.4f} | '
            f'{(group.mae_difference < 0).sum()}/{len(group)} |')
    lines += ['', '## Errors across measured-score ranges', '',
        'Ranges below 2.5, 2.5 to below 4, and 4 or above are descriptive only, not clinical categories.',
        'These checks were motivated by observed extreme-score errors. Small group counts limit conclusions.',
        'Numbers below average per-repetition metrics; repetitions reuse students, not independent samples.',
        'Negative signed error means underestimation; positive means overestimation.', '',
        '| Outcome | Inputs | Model | Measured range | Students | MAE | Signed error | Fraction error >1 |',
        '|---|---|---|---|---:|---:|---:|---:|']
    for key, group in ranges.groupby(['target', 'input_set', 'model', 'score_range']):
        lines.append('| ' + ' | '.join(key) +
            f' | {group.n_students.iloc[0]} | {group.mae.mean():.3f} | '
            f'{group.mean_signed_error.mean():+.3f} | {group.fraction_error_over_1.mean():.1%} |')
    lines += ['', 'Do not interpret split-to-split consistency as statistical significance or clinical utility.',
        'No final deployment model or weights are saved. Original run files and source SAV are unchanged.']
    (out / 'comparison-with-original.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    config_path = ROOT / 'experiments/02-compare-xgboost-score-prediction-settings.json'
    c = json.loads(config_path.read_text(encoding='utf-8'))
    reference = validate_followup(c)
    df = training.load_data(c)
    print('Validated separate XGBoost follow-up and original experiment alignment.', flush=True)
    if args.check_only:
        return
    out = ROOT / c['output_root'] / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    training.run(c, df, config_path, out)
    manifest_path = out / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest.update(status='running', followup_script_sha256=training.sha256(__file__),
        reference_run=c['reference_run'], reference_manifest_sha256=training.sha256(reference/'manifest.json'),
        reference_predictions_sha256=training.sha256(reference/'held-out-predictions.csv'),
        interpretation=c['interpretation'])
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    try:
        compare_with_original(c, out, reference)
        manifest['status'] = 'complete'
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
