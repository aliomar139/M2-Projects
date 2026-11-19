"""Descriptive analysis of saved predictions; never fit or change a model."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT/'results/01-score-prediction-baselines/20261102T083420352990Z'
XGBOOST = ROOT/'results/02-xgboost-score-prediction/20261102T093101705609Z'
spec = importlib.util.spec_from_file_location('training', Path(__file__).with_name('01-compare-score-prediction-baselines.py'))
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)


def similarity_matrix(frame, numeric, categorical):
    # Fixed survey ranges, equal weight per question; never use outcomes in distances.
    differences = [np.abs(frame[col].to_numpy()[:, None]-frame[col].to_numpy()[None, :])/4
                   for col in numeric]
    differences += [(frame[col].to_numpy()[:, None] != frame[col].to_numpy()[None, :]).astype(float)
                    for col in categorical]
    distances = np.mean(differences, axis=0)
    np.fill_diagonal(distances, np.inf)
    return distances


def self_check():
    frame = pd.DataFrame({'n': [1, 1, 5], 'cat': [1, 1, 2]})
    distances = similarity_matrix(frame, ['n'], ['cat'])
    assert distances[0, 1] == 0 and distances[0, 2] == 1
    assert np.isinf(distances.diagonal()).all()
    assert np.array_equal(distances, distances.T)


def student_summary(predictions, inputs):
    selected = predictions[(predictions.target == 'burnout_score') &
        (predictions.input_set == inputs) & (predictions.model == 'ridge')].copy()
    assert not selected.duplicated(['student_index', 'repeat']).any()
    assert selected.groupby('student_index')['repeat'].apply(set).apply(
        lambda x: x == {1, 2, 3, 4, 5}).all()
    selected['signed_error'] = selected.prediction-selected.actual
    result = selected.groupby('student_index').agg(actual=('actual', 'first'),
        average_prediction=('prediction', 'mean'), mae=('absolute_error', 'mean'),
        signed_error=('signed_error', 'mean'), prediction_min=('prediction', 'min'),
        prediction_max=('prediction', 'max'))
    assert len(result) == 97
    return result


def main():
    self_check()
    sources = [ROOT/'data/03-prepared-student-burnout-data.sav', ORIGINAL/'held-out-predictions.csv',
        ORIGINAL/'tuning.json', ORIGINAL/'outer-folds.csv', XGBOOST/'held-out-predictions.csv',
        XGBOOST/'tuning.json', XGBOOST/'outer-folds.csv']
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in sources}
    for folder in [ORIGINAL, XGBOOST]:
        assert json.loads((folder/'manifest.json').read_text())['status'] == 'complete'
    c = json.loads((ORIGINAL/'config.json').read_text())
    data = training.load_data(c)
    data.index = np.arange(1, len(data)+1)
    data.index.name = 'student_index'
    original = pd.read_csv(ORIGINAL/'held-out-predictions.csv')
    xgb = pd.read_csv(XGBOOST/'held-out-predictions.csv')
    # Both runs must evaluate identical students/folds. Ignore CSV row ordering.
    sort = ['repeat', 'student_index']
    pd.testing.assert_frame_equal(pd.read_csv(ORIGINAL/'outer-folds.csv').sort_values(sort).reset_index(drop=True),
        pd.read_csv(XGBOOST/'outer-folds.csv').sort_values(sort).reset_index(drop=True))
    predictions = pd.concat([original, xgb[xgb.model == 'xgboost']], ignore_index=True)
    assert not predictions.duplicated(['target', 'input_set', 'model', 'repeat', 'student_index']).any()
    for _, group in predictions.groupby(['target', 'input_set', 'model', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        assert np.allclose(group.actual, data.loc[group.student_index, group.target.iloc[0]])
        assert np.allclose(group.absolute_error, (group.prediction-group.actual).abs())
    out = ROOT/'results/03-score-prediction-errors'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    spread = []
    for key, group in predictions.groupby(['target', 'input_set', 'model', 'repeat']):
        spread.append(dict(zip(['target', 'input_set', 'model', 'repeat'], key),
            actual_sd=group.actual.std(), prediction_sd=group.prediction.std(),
            sd_ratio=group.prediction.std()/group.actual.std(), prediction_min=group.prediction.min(),
            prediction_max=group.prediction.max(), mae=group.absolute_error.mean(),
            correlation=group.actual.corr(group.prediction) if group.prediction.std() > 1e-10 else np.nan))
    spread = pd.DataFrame(spread)
    spread.to_csv(out/'prediction-spread-by-repeat.csv', index=False)
    small, broad = student_summary(original, 'small_b'), student_summary(original, 'broad_d')
    features = c['input_sets']['small_b']
    students = small.add_prefix('small_b_').join(broad[['mae', 'average_prediction']].add_prefix('broad_d_'))
    students['broad_minus_small_mae'] = students.broad_d_mae-students.small_b_mae
    students = students.join(data[features+['study_hours', 'sleep_duration']]).sort_values('small_b_mae', ascending=False)
    students.to_csv(out/'student-errors-and-inputs.csv')
    numeric = [col for col in features if col not in c['category_levels']]
    categorical = [col for col in features if col in c['category_levels']]
    distances = similarity_matrix(data, numeric, categorical)
    assert distances.shape == (97, 97) and np.allclose(distances, distances.T)
    neighbors = []
    for position, (student, row) in enumerate(data.iterrows()):
        # Stable row order resolves ties; list all equal-distance candidates separately by count.
        nearest = np.argsort(distances[position], kind='stable')[:3]
        for rank, peer_position in enumerate(nearest, 1):
            peer = int(data.index[peer_position])
            neighbors.append({'student_index': student, 'neighbor_rank': rank, 'peer_index': peer,
                'distance': distances[position, peer_position],
                'ties_at_distance': int(np.isclose(distances[position], distances[position, peer_position]).sum()),
                'actual': row.burnout_score, 'peer_actual': data.loc[peer, 'burnout_score'],
                'actual_score_gap': abs(row.burnout_score-data.loc[peer, 'burnout_score']),
                'student_mae': small.loc[student, 'mae'], 'peer_mae': small.loc[peer, 'mae']})
    neighbors = pd.DataFrame(neighbors)
    neighbors.to_csv(out/'similar-student-pairs.csv', index=False)
    pair_inputs = []
    for row in neighbors[neighbors.neighbor_rank == 1].itertuples():
        for role, index in [('student', row.student_index), ('nearest_peer', row.peer_index)]:
            pair_inputs.append({'query_student': row.student_index, 'role': role, 'student_index': index,
                'actual': data.loc[index, 'burnout_score'], **data.loc[index, features].to_dict()})
    pd.DataFrame(pair_inputs).to_csv(out/'nearest-pair-inputs.csv', index=False)
    tuning = []
    for folder in [ORIGINAL, XGBOOST]:
        for record in json.loads((folder/'tuning.json').read_text()):
            for key, value in record['parameters'].items():
                tuning.append({'target': record['target'], 'input_set': record['input_set'],
                    'model': record['model'], 'parameter': key.split('__')[-1], 'value': value})
    tuning = pd.DataFrame(tuning).groupby(['target', 'input_set', 'model', 'parameter', 'value']).size().reset_index(name='fold_count')
    tuning.to_csv(out/'selected-tuning-counts.csv', index=False)
    lines = ['# Prediction diagnostics', '', '2 November 2026. Descriptive follow-up; no models fitted.', '',
        '## 1. Are predictions compressed?', '',
        'The ratio below is predicted-score standard deviation divided by actual-score standard deviation, averaged across repetitions.',
        'A ratio below 1 means predictions are less spread out. This alone does not establish the cause or justify expanding predictions.', '',
        '| Inputs | Method | Actual SD | Predicted SD | Spread ratio | MAE |', '|---|---|---:|---:|---:|---:|']
    for key, group in spread[spread.target == 'burnout_score'].groupby(['input_set', 'model']):
        lines.append(f'| {key[0]} | {key[1]} | {group.actual_sd.mean():.3f} | {group.prediction_sd.mean():.3f} | {group.sd_ratio.mean():.3f} | {group.mae.mean():.3f} |')
    lines += ['', '## 2. Difficult students and broader inputs', '',
        'Top ten ranked by Small B ridge mean absolute error over five repetitions. Negative broad-minus-small error means Broad D helped.', '',
        '| Student | Actual | Small B prediction | Small B MAE | Broad D MAE | Difference |',
        '|---|---:|---:|---:|---:|---:|']
    for index, row in students.head(10).iterrows():
        lines.append(f'| {index} | {row.small_b_actual:.3f} | {row.small_b_average_prediction:.3f} | {row.small_b_mae:.3f} | {row.broad_d_mae:.3f} | {row.broad_minus_small_mae:+.3f} |')
    hard = students[students.small_b_mae > 1]
    lines += ['', f'{len(hard)} students have Small B mean absolute error above one point. Broad D improves MAE for '
        f'{(hard.broad_minus_small_mae < 0).sum()} of these students; this is a descriptive count, not an independent test.', '',
        '## 3. Students with similar answers', '',
        'Similarity was fixed before calculating matches: equal weight for each of the eight Small B questions. For the six 1–5 questions, use absolute difference / 4. For sleep and study-hour categories, use 0 if identical and 1 otherwise. Average these eight distances. Smaller means more similar; no BAT scores enter the distance.',
        'This is a simple Gower-style descriptive distance. A category mismatch is treated equally regardless of the number of category steps. Other reasonable distance definitions could produce different matches.',
        'Search uses all 97 students, excludes self, returns three neighbors, and resolves ties by saved row order. It is an exploratory inspection, not a new prediction-performance evaluation. Similar is not identical, and matches do not establish missing causes.', '',
        '| Difficult student | Nearest peer | Distance (0–1) | Actual | Peer actual | Score gap | Peer MAE |',
        '|---|---|---:|---:|---:|---:|---:|']
    nearest = neighbors[neighbors.neighbor_rank == 1].set_index('student_index')
    for index in students.head(10).index:
        row = nearest.loc[index]
        lines.append(f'| {index} | {int(row.peer_index)} | {row.distance:.3f} | {row.actual:.3f} | {row.peer_actual:.3f} | {row.actual_score_gap:.3f} | {row.peer_mae:.3f} |')
    lines += ['', 'Exact input combinations shared by multiple students:', '']
    exact = data.groupby(features).burnout_score.agg(['count', 'min', 'max'])
    exact = exact[exact['count'] > 1]
    lines += [f'{len(exact)} duplicated input patterns, covering {int(exact["count"].sum())} students. '
        + (f'Largest observed within-pattern score gap: {(exact["max"]-exact["min"]).max():.3f}.' if len(exact) else 'No exact duplicates found.'), '',
        'The raw BAT scores and original CSV were checked during data loading; no score formula was changed.', '',
        '## 4. What settings were selected?', '',
        'Counts below cover 25 outer fits per method/input/target. Settings were selected by inner validation, not by this diagnostics script.', '',
        '| Inputs | Model | Parameter | Value | Folds |', '|---|---|---|---:|---:|']
    for row in tuning[tuning.target == 'burnout_score'].itertuples():
        lines.append(f'| {row.input_set} | {row.model} | {row.parameter} | {row.value:g} | {row.fold_count} |')
    lines += ['', 'Strong penalties or shallow trees can compress predictions, but frequent selection means these settings won the tested inner-validation comparison. It does not prove that relaxing them improves new-student performance.', '',
        '## 5. How to use these findings', '',
        'Keep the completed evaluations as research evidence. Do not stretch predictions toward 1 or 5 using the evaluation answers, delete hard students, or generate artificial labels to make this table look better.',
        'Compare spread with errors: more variable predictions are not automatically more accurate. Similar answers with different outcomes indicate ambiguity in these inputs, not proof that respondents are unreliable or an algorithm cannot learn any useful pattern.',
        'Any next model or weighting experiment is exploratory and should be specified separately. Additional real data or richer inputs may help, but their benefit has not been measured here. No clinical warning threshold or intervention effect is established.', '',
        '## Files', '', 'All CSVs in this folder contain descriptive diagnostics from saved predictions. Student indices refer to original SAV row order, not sorted Excel rows. No timestamps are exported. Repetitions reuse the same students.']
    (out/'findings.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    assert all(training.sha256(ROOT/path) == value for path, value in hashes.items())
    manifest = {'status': 'complete', 'created_utc': datetime.now(timezone.utc).isoformat(),
        'models_trained': False, 'source_files_unchanged': True, 'source_sha256': hashes,
        'script_sha256': training.sha256(__file__), 'students': len(data),
        'similarity': 'Equal-question-weight fixed-range distance; numeric /4; categorical mismatch; exclude self; stable ties.'}
    (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print(f'Complete: {out}')
    print((out/'findings.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    main()
