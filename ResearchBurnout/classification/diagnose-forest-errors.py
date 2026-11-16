"""Descriptive inspection of the selected RF's saved real held-out errors; no fitting."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT/'classification/augmentation-outputs/20261112T125001425382Z'
spec = importlib.util.spec_from_file_location('augmentation', Path(__file__).with_name('train-augmentation.py'))
augmentation = importlib.util.module_from_spec(spec); spec.loader.exec_module(augmentation)
spec = importlib.util.spec_from_file_location('diagnostics', ROOT/'analysis/scripts/diagnose-predictions.py')
diagnostics = importlib.util.module_from_spec(spec); spec.loader.exec_module(diagnostics)
training = augmentation.training


def main():
    base = json.loads((REFERENCE/'reference-config.json').read_text())
    previous = json.loads((REFERENCE/'manifest.json').read_text()); assert previous['status'] == 'complete'
    assert training.sha256(augmentation.__file__) == previous['script_sha256']
    paths = [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [REFERENCE/name for name in ['manifest.json', 'reference-config.json', 'held-out-predictions.csv', 'outer-folds.csv']]
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in paths}
    assert all(training.sha256(ROOT/path) == digest for path, digest in previous['source_sha256'].items())
    data = training.load_data(base); data.index = np.arange(1, len(data)+1); data.index.name = 'student_index'
    cols = base['input_sets']['small_b']; categorical = [c for c in cols if c in base['category_levels']]
    numeric = [c for c in cols if c not in categorical]; assert len(cols) == 8 and len(numeric) == 6
    saved = pd.read_csv(REFERENCE/'held-out-predictions.csv')
    p = saved[(saved.input_set == 'small_b') & (saved.model == 'forest') & (saved.augmentation == 'inner_selected_ratio')].copy()
    assert len(p) == 485 and not p.duplicated(['repeat', 'student_index']).any()
    assert p.groupby('student_index')['repeat'].apply(set).apply(lambda s: s == {1,2,3,4,5}).all()
    assert np.allclose(p.actual_score, data.loc[p.student_index, 'burnout_score'])
    assert np.array_equal(p.actual_class, (p.actual_score >= 4).astype(int))
    assert np.array_equal(p.predicted_class, (p.warning_score >= p.threshold).astype(int))
    students = data[cols].copy(); students['actual_score'] = data.burnout_score
    students['actual_class'] = (students.actual_score >= 4).astype(int)
    students['warnings_out_of_5'] = p.groupby('student_index').predicted_class.sum().astype(int)
    students['warning_fraction'] = students.warnings_out_of_5/5
    students['ever_warned'] = students.warnings_out_of_5 > 0
    students['persistent_warning'] = students.warnings_out_of_5 >= 3
    masks = {
        'below_high_ever_false_warning': (students.actual_class == 0) & students.ever_warned,
        'below_high_persistent_false_warning': (students.actual_class == 0) & students.persistent_warning,
        'below_high_never_warned': (students.actual_class == 0) & ~students.ever_warned,
        'high_ever_correct_warning': (students.actual_class == 1) & students.ever_warned,
        'high_never_warned': (students.actual_class == 1) & ~students.ever_warned,
    }
    fp = students[masks['below_high_ever_false_warning']]
    tp = students[masks['high_ever_correct_warning']]
    assert len(students) == 97 and students.actual_class.sum() == 17
    assert students[students.actual_class == 0].warnings_out_of_5.sum() == 140
    assert students[students.actual_class == 1].warnings_out_of_5.sum() == 74
    bounds = [(1,2,'1 <= score < 2'), (2,3,'2 <= score < 3'), (3,3.5,'3 <= score < 3.5'),
              (3.5,3.75,'3.5 <= score < 3.75'), (3.75,4,'3.75 <= score < 4'), (4,5.01,'4 <= score <= 5')]
    bands = []
    for lower, upper, label in bounds:
        group = students[(students.actual_score >= lower) & (students.actual_score < upper)]
        bands.append({'score_band': label, 'students': len(group), 'ever_warned_students': int(group.ever_warned.sum()),
            'persistent_warning_students': int(group.persistent_warning.sum()), 'warning_events': int(group.warnings_out_of_5.sum()),
            'warning_rate_per_opportunity': float(group.warnings_out_of_5.sum()/(5*len(group))) if len(group) else None})
    assert sum(b['students'] for b in bands) == 97 and sum(b['warning_events'] for b in bands) == 214
    value_labels = {
        'study_hours_code': {1:'Less than 5 hours/week',2:'5-10 hours/week',3:'11-20 hours/week',4:'More than 20 hours/week'},
        'sleep_duration_code': {1:'Less than 5 hours/night',2:'5-6 hours/night',3:'7-8 hours/night',4:'More than 8 hours/night'},
    }
    comparisons, frequencies = [], []
    for group_name, mask in masks.items():
        group = students[mask]
        for col in numeric:
            v = group[col]
            comparisons.append({'group': group_name, 'feature': col, 'unique_students': len(group),
                'mean': float(v.mean()), 'median': float(v.median()), 'q1': float(v.quantile(.25)), 'q3': float(v.quantile(.75))})
        for col in cols:
            levels = base['category_levels'][col] if col in categorical else [1,2,3,4,5]
            for level in levels:
                n = int((group[col] == level).sum())
                frequencies.append({'group': group_name, 'feature': col, 'value': level,
                    'value_label': value_labels.get(col, {}).get(level, str(level)), 'count': n,
                    'group_students': len(group), 'fraction': n/len(group) if len(group) else None})
    diagnostics.self_check()
    distance = diagnostics.similarity_matrix(students[cols], numeric, categorical)
    neighbors, pairs = [], []
    for student_id, row in fp.iterrows():
        nearest = sorted(tp.index, key=lambda i:(distance[student_id-1, i-1], i))[:3]
        for rank, peer_id in enumerate(nearest, 1):
            neighbors.append({'student_index': student_id, 'actual_score': row.actual_score,
                'false_warnings_out_of_5': row.warnings_out_of_5, 'neighbor_rank': rank, 'peer_index': peer_id,
                'peer_score': students.loc[peer_id,'actual_score'], 'peer_warnings_out_of_5': students.loc[peer_id,'warnings_out_of_5'],
                'input_distance': float(distance[student_id-1,peer_id-1]),
                'score_gap': float(students.loc[peer_id,'actual_score']-row.actual_score)})
            if rank == 1:
                for role, index in [('false_warning_student', student_id),('correctly_warned_high_peer',peer_id)]:
                    pairs.append({'query_student': student_id, 'role': role, 'student_index': index,
                        'actual_score': students.loc[index,'actual_score'], **students.loc[index,cols].to_dict()})
    patterns = students.groupby(cols).actual_score.agg(['count','min','max'])
    conflicts = patterns[(patterns['count'] > 1) & (patterns['min'] < 4) & (patterns['max'] >= 4)].reset_index()
    out = ROOT/'classification/error-analysis-outputs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'); out.mkdir(parents=True,exist_ok=False)
    students.to_csv(out/'student-warning-summary.csv')
    p.to_csv(out/'held-out-predictions.csv',index=False)
    pd.DataFrame(bands).to_csv(out/'score-bands.csv',index=False)
    pd.DataFrame(comparisons).to_csv(out/'ordinal-feature-summaries.csv',index=False)
    pd.DataFrame(frequencies).to_csv(out/'answer-distributions.csv',index=False)
    pd.DataFrame(neighbors).to_csv(out/'nearest-high-peers.csv',index=False)
    pd.DataFrame(pairs).to_csv(out/'nearest-pair-inputs.csv',index=False)
    conflicts.to_csv(out/'identical-input-opposite-class-patterns.csv',index=False)
    counts = {name:int(mask.sum()) for name,mask in masks.items()}
    near = fp[fp.actual_score >= 3.5]; far = fp[fp.actual_score < 3]
    lines = ['# Selected Random Forest: false-warning inspection', '',
        'Current Small B RF with selected augmentation; primary measured score >=4 is High. No models trained or changed.',
        'All 97 students appear once in profile comparisons. Their five real held-out predictions measure warning persistence, not five independent students.', '',
        '## 1. How many distinct students are involved?', '',
        f'Of 80 Below-high students, {len(fp)} were falsely warned at least once, {counts["below_high_persistent_false_warning"]} in at least 3/5 repetitions, and {counts["below_high_never_warned"]} never.',
        f'Of 17 High students, {len(tp)} were detected at least once and {counts["high_never_warned"]} were never detected.',
        'Across five repetitions there were 140 false-warning events (28 average) and 74 correct-warning events (14.8 average).', '',
        '## 2. Are false warnings close to score 4?', '',
        '| Measured score band | Real students | Ever warned | Warned >=3/5 | Warning events across repetitions |',
        '|---|---:|---:|---:|---:|']
    for r in bands: lines.append(f'| {r["score_band"]} | {r["students"]} | {r["ever_warned_students"]} | {r["persistent_warning_students"]} | {r["warning_events"]} |')
    lines += ['', f'Among distinct falsely warned students, {len(near)}/{len(fp)} have scores >=3.5 and <4; {len(far)}/{len(fp)} score below 3.',
        f'Of the 140 false-warning events, {int(near.warnings_out_of_5.sum())} involve scores 3.5..<4 and {int(far.warnings_out_of_5.sum())} involve scores below 3.',
        'Nearness to the boundary does not make a false warning correct. Below-high is a study-defined score group, not proof of no symptoms or no need for support.', '',
        '## 3. Compare the six 1-5 answers', '',
        'Each mean counts each student once: falsely warned Below-high students versus High students correctly warned at least once. These outcome-selected groups are descriptive, not independent hypothesis tests or causal effects.', '',
        '| Input | False-warning group mean | Correctly warned High mean | High minus false-warning mean |',
        '|---|---:|---:|---:|']
    for col in numeric: lines.append(f'| {col} | {fp[col].mean():.2f} | {tp[col].mean():.2f} | {tp[col].mean()-fp[col].mean():+.2f} |')
    lines += ['', '## 4. Sleep and study-hour categories', '',
        'Category codes are compared as distributions, not averaged as if equally spaced numerical measurements.', '',
        '| Input and answer | False-warning group | Correctly warned High group |', '|---|---:|---:|']
    for col in categorical:
        for level in base['category_levels'][col]:
            a,b = int((fp[col] == level).sum()), int((tp[col] == level).sum())
            lines.append(f'| {col}: {value_labels[col][level]} | {a}/{len(fp)} ({a/len(fp):.1%}) | {b}/{len(tp)} ({b/len(tp):.1%}) |')
    lines += ['', '## 5. Persistent false warnings and their closest correctly warned High peers', '',
        'Distance uses all eight answers with equal question weight: six ordinal absolute gaps/4 and categorical sleep/study mismatch 0/1. No BAT score enters distance. Search uses all observed High peers, with ties by original row index; this is descriptive inspection, never a predictive validation result.', '',
        '| Student row | Actual score | False warnings /5 | Closest High row | High score | Input distance |',
        '|---|---:|---:|---|---:|---:|']
    nearest = pd.DataFrame(neighbors).query('neighbor_rank == 1').set_index('student_index')
    for index,row in fp.sort_values(['warnings_out_of_5','actual_score'],ascending=[False,True]).head(5).iterrows():
        peer = nearest.loc[index]
        lines.append(f'| {index} | {row.actual_score:.3f} | {int(row.warnings_out_of_5)} | {int(peer.peer_index)} | {peer.peer_score:.3f} | {peer.input_distance:.3f} |')
    lines += ['', f'{len(conflicts)} exact eight-answer patterns contain students on both sides of the >=4 boundary.',
        'Similar profiles with different measured outcomes show ambiguity in these answers, not proof of a hard performance ceiling, missing causes or unreliable respondents.', '',
        '## How to use this inspection', '',
        'Keep the current score boundary and selected model. Do not remove hard students, redefine High after inspecting errors, or treat group mean differences as validated feature importance.',
        'Any proposed feature selection, interaction, subgroup or threshold rule must be specified separately and learned inside training validation. Inspecting these same outer errors makes follow-up results exploratory; no improvement is claimed here.',
        'The CSVs retain original SAV row indices, not Excel sorting positions; no names or timestamps are exported. No new survey questions, synthetic records, interventions or clinical cutoff validation are established.']
    (out/'findings.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    assert all(training.sha256(ROOT/path) == digest for path,digest in hashes.items())
    manifest = {'status':'complete','created_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':training.sha256(__file__),
        'helper_sha256':{Path(m.__file__).name:training.sha256(m.__file__) for m in [augmentation,training,diagnostics]},
        'source_sha256':hashes,'source_files_unchanged':True,'models_trained':False,'real_students':97,
        'held_out_prediction_rows':485,'groups':counts,'scope':'Descriptive error analysis; unique-student feature summaries and repeated-warning counts.'}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Complete: {out}'); print((out/'findings.md').read_text(encoding='utf-8'))


if __name__ == '__main__': main()
