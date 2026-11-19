"""Verify checkpoints and write the selected-RF validation tables and figures."""
import argparse
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import time
from zoneinfo import ZoneInfo

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, balanced_accuracy_score, precision_score, recall_score, fbeta_score
from sklearn.model_selection import StratifiedKFold
from threadpoolctl import threadpool_limits

spec = importlib.util.spec_from_file_location('validation', Path(__file__).with_name('25-validate-random-forest-against-baselines-and-chance.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def conditional_intervals(predictions, config):
    """Class-stratified student resampling, retaining all repeated predictions."""
    methods = ['selected_rf', 'real_only_rf', 'workload_logistic']
    groups = {m: predictions[predictions.method == m].pivot(index='student_index', columns='repeat', values='predicted_class').to_numpy() for m in methods}
    actual = predictions.drop_duplicates('student_index').sort_values('student_index').actual_class.to_numpy()
    high, low = np.flatnonzero(actual == 1), np.flatnonzero(actual == 0)
    rng = np.random.default_rng(config['bootstrap_seed'])
    rows = []
    for sample in range(config['bootstrap_samples']):
        ids = np.r_[rng.choice(high, len(high), replace=True), rng.choice(low, len(low), replace=True)]
        y = actual[ids, None]
        for method, p in groups.items():
            p = p[ids]
            tp, fp = ((p == 1) & (y == 1)).sum(axis=0), ((p == 1) & (y == 0)).sum(axis=0)
            recall = tp/len(high)
            precision = np.divide(tp, tp+fp, out=np.zeros(5), where=(tp+fp) != 0)
            rows.append({'sample': sample, 'method': method, 'recall': float(recall.mean()),
                         'precision': float(precision.mean()), 'balanced_accuracy': float(((recall+1-fp/len(low))/2).mean())})
    frame = pd.DataFrame(rows)
    intervals = []
    for method in methods:
        for metric in ['recall', 'precision', 'balanced_accuracy']:
            values = frame.loc[frame.method == method, metric]
            lo, hi = np.quantile(values, [.025, .975])
            intervals.append({'comparison': method, 'metric': metric, 'lower': float(lo), 'upper': float(hi)})
    for other in ['real_only_rf', 'workload_logistic']:
        for metric in ['recall', 'precision', 'balanced_accuracy']:
            values = frame.loc[frame.method == 'selected_rf', metric].to_numpy()-frame.loc[frame.method == other, metric].to_numpy()
            lo, hi = np.quantile(values, [.025, .975])
            intervals.append({'comparison': f'selected_rf minus {other}', 'metric': metric, 'lower': float(lo), 'upper': float(hi)})
    return pd.DataFrame(intervals)


def verify(out, predictions):
    manifest, c = v.read(out/'manifest.json'), v.read(out/'config.json')
    assert all(v.training.sha256(v.ROOT/p) == h for p, h in manifest['source_sha256'].items())
    base, search, source = [v.read(out/f'{name}.json') for name in ['base-config', 'binary-config', 'augmentation-config']]
    data = v.training.load_data(base)
    actual = (data.burnout_score.to_numpy() >= 4).astype(int)
    files = sorted((out/'folds').glob('*.json'))
    assert len(files) == 25*(c['permutations']+1)
    selected_refits, candidates_checked, regenerated_pools = 0, 0, 0
    null_predictions = {}
    with threadpool_limits(limits=1):
        for path in files:
            r = v.read(path)
            y = v.labels_for(actual, r['permutation'], c['permutation_seed'])
            import hashlib
            assert r['label_sha256'] == hashlib.sha256(y.tobytes()).hexdigest()
            train, test = next((tr, te) for rep, fold, tr, te in v.outer_splits(y, base, search)
                               if (rep, fold) == (r['repeat'], r['fold']))
            assert r['train'] == (train+1).tolist() and r['test'] == (test+1).tolist()
            assert len(set(r['test'])) == len(test) and not set(r['train']) & set(r['test'])
            for inner in r['inner_memberships']:
                assert not set(inner['train']) & set(inner['validation'])
                assert set(inner['train']) | set(inner['validation']) == set(r['train'])
            chosen = max(r['candidates'], key=lambda x: (*v.aug.choice_key(x), -x['ratio']))
            assert r['selected'] == {k: val for k, val in chosen.items() if k != 'threshold_candidates'}
            for candidate in r['candidates']:
                counts = candidate['chosen_threshold']
                for threshold_row in candidate.get('threshold_candidates', [counts]):
                    assert threshold_row['tp']+threshold_row['fn'] == int(y[train].sum())
                    assert threshold_row['fp']+threshold_row['tn'] == int((1-y[train]).sum())
                    assert np.isclose(threshold_row['recall'], threshold_row['tp']/(threshold_row['tp']+threshold_row['fn']))
                    expected_precision = threshold_row['tp']/(threshold_row['tp']+threshold_row['fp']) if threshold_row['tp']+threshold_row['fp'] else 0
                    assert np.isclose(threshold_row['precision'], expected_precision)
                    assert np.isclose(threshold_row['f2'], 5*threshold_row['tp']/(5*threshold_row['tp']+4*threshold_row['fn']+threshold_row['fp']))
                if 'threshold_candidates' in candidate:
                    assert max(candidate['threshold_candidates'], key=lambda x: (x['f2'], x['precision'], x['recall'], x['threshold'])) == counts
                candidates_checked += 1
            for p in r['predictions']:
                assert p['student_index'] in r['test'] and p['actual_class'] == y[p['student_index']-1]
                assert 0 <= p['warning_score'] <= 1
                assert p['predicted_class'] == int(p['warning_score'] >= p['threshold'])
                if p['method'] == 'selected_rf':
                    assert p['threshold'] == r['selected']['chosen_threshold']['threshold']
            if r['permutation']:
                null_predictions.setdefault(r['permutation'], []).extend(r['predictions'])
                continue
            cols = base['input_sets']['small_b']
            X, yt = data[cols].iloc[train], y[train]
            for g in r['generation']:
                members = next((i['train'] for i in r['inner_memberships'] if i['inner_fold'] == g['inner_fold']), r['train'])
                allowed = set(members)
                for profile in g['profiles']:
                    assert profile['parent_a'] in allowed and profile['parent_b'] in allowed
                    assert y[profile['parent_a']-1] == y[profile['parent_b']-1] == 1
                gp, provenance, stats = v.aug.pool(data[cols].iloc[np.asarray(members)-1], y[np.asarray(members)-1],
                                                  base, source['generator'], g['seed'])
                assert provenance == g['profiles']
                assert all(stats[k] == g[k] for k in stats)
                regenerated_pools += 1
            gen, provenance, counts = v.aug.pool(X, yt, base, source['generator'],
                source['generator']['seed']+r['repeat']*10000+r['fold']*100)
            saved_gen = next(g for g in r['generation'] if g['inner_fold'] == 0)
            assert provenance == saved_gen['profiles']
            recipe = r['selected']
            Xt, Xv, labels, added = v.aug.prepare(X, yt, data[cols].iloc[test], gen, recipe['ratio'], base)
            seed = base['cv']['inner_seed']+r['repeat']*100+r['fold']
            model = v.binary.classifier('forest', recipe['parameters'], seed).fit(Xt, labels,
                sample_weight=v.aug.priority.weights(labels, recipe['factor'], 1))
            scores = v.binary.probabilities(model, Xv)
            saved = [p['warning_score'] for p in r['predictions'] if p['method'] == 'selected_rf']
            np.testing.assert_allclose(scores, saved, rtol=0, atol=1e-12)
            assert added == r['synthetic_added']
            selected_refits += 1
    independent = []
    for (method, rep), g in predictions.groupby(['method', 'repeat']):
        y, p = g.actual_class, g.predicted_class
        tn, fp, fn, tp = confusion_matrix(y, p, labels=[0, 1]).ravel()
        independent.append({'method': method, 'repeat': rep, 'tp': int(tp), 'fp': int(fp), 'fn': int(fn), 'tn': int(tn),
            'recall': float(recall_score(y, p, zero_division=0)), 'precision': float(precision_score(y, p, zero_division=0)),
            'balanced_accuracy': float(balanced_accuracy_score(y, p)), 'f2': float(fbeta_score(y, p, beta=2, zero_division=0))})
    independent = pd.DataFrame(independent).set_index(['method', 'repeat']).sort_index()
    saved = pd.read_csv(out/'repeat-metrics.csv').set_index(['method', 'repeat']).sort_index().loc[independent.index]
    np.testing.assert_allclose(independent, saved[list(independent)], atol=1e-12)
    independent.to_csv(out/'independently-verified-metrics.csv')
    null_rows = []
    for perm, records in sorted(null_predictions.items()):
        frame = pd.DataFrame(records)
        values = []
        for rep, group in frame.groupby('repeat'):
            assert len(group) == 97 and group.student_index.nunique() == 97
            y, p = group.actual_class, group.predicted_class
            values.append({'balanced_accuracy': balanced_accuracy_score(y, p),
                           'recall': recall_score(y, p, zero_division=0),
                           'precision': precision_score(y, p, zero_division=0),
                           'f2': fbeta_score(y, p, beta=2, zero_division=0)})
        null_rows.append({'permutation': perm, **pd.DataFrame(values).mean().to_dict()})
    verified_null = pd.DataFrame(null_rows).set_index('permutation').sort_index()
    saved_null = pd.read_csv(out/'permutation-metrics.csv').set_index('permutation').sort_index()
    np.testing.assert_allclose(verified_null, saved_null[list(verified_null)], atol=1e-12)
    evaluation = v.read(out/'evaluation-summary.json')
    observed = float(independent.loc['selected_rf', 'balanced_accuracy'].mean())
    assert np.isclose(evaluation['observed_balanced_accuracy'], observed)
    assert np.isclose(evaluation['pvalue'], v.permutation_pvalue(observed, verified_null.balanced_accuracy))
    verified_null.to_csv(out/'independently-verified-permutations.csv')
    # Replay one entire real and one entire null search, including inner tuning.
    refit = out/'verification-refits'
    (refit/'folds').mkdir(parents=True, exist_ok=True)
    for name in ['config', 'base-config', 'binary-config', 'augmentation-config']:
        v.write(refit/f'{name}.json', v.read(out/f'{name}.json'))
    for perm in [0, 1]:
        v.run_fold((str(refit), perm, 1, 1))
        original = v.read(out/'folds'/f'p{perm:03d}-r1-f1.json')
        replay = v.read(refit/'folds'/f'p{perm:03d}-r1-f1.json')
        assert {k: val for k, val in original.items() if k != 'seconds'} == {k: val for k, val in replay.items() if k != 'seconds'}
    return {'passed': True, 'fold_checkpoints': len(files), 'candidates_checked': candidates_checked,
            'selected_real_outer_refits': selected_refits, 'full_search_replays': 2,
            'real_training_pools_regenerated': regenerated_pools,
            'null_procedures_independently_scored': len(verified_null), 'permutation_pvalue_recomputed': True,
            'sklearn_metrics_recomputed': len(independent), 'source_hashes_unchanged': True,
            'scope_limit': 'Replayed full search for one real and one null fold, not all null fits. No independent population validation.'}


def figures(out, predictions, summary, null):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(null.balanced_accuracy, bins=20, color='#94a3b8', edgecolor='white')
    ax.axvline(summary.loc['selected_rf', 'balanced_accuracy'], color='#b91c1c', linewidth=2, label='Real-label RF')
    ax.set(xlabel='Mean balanced accuracy across five repetitions', ylabel='Shuffled-label evaluations',
           title='Does the fixed RF procedure beat shuffled labels?', xlim=(0, 1))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    fig.tight_layout(); fig.savefig(out/'permutation-test.png', dpi=180); plt.close(fig)
    rf = predictions[predictions.method == 'selected_rf']
    rows = []
    for threshold in np.linspace(0, 1, 101):
        values = [v.binary.metrics(g.actual_class, g.warning_score >= threshold) for _, g in rf.groupby('repeat')]
        rows.append({'threshold': float(threshold), **{k: float(np.mean([r[k] for r in values])) for k in ['tp', 'fp', 'recall', 'precision']}})
    curve = pd.DataFrame(rows); curve.to_csv(out/'descriptive-threshold-curve.csv', index=False)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(curve.fp, curve.tp, color='#2563eb')
    axes[0].scatter([summary.loc['selected_rf', 'fp']], [summary.loc['selected_rf', 'tp']], color='#b91c1c', label='Inner-selected fold thresholds', zorder=3)
    axes[0].set(xlabel='False warnings / 80 Below-high students', ylabel='High students detected / 17', title='Descriptive warning trade-off')
    axes[0].legend(fontsize=8)
    for m, label in [('selected_rf', 'Selected RF'), ('workload_logistic', 'Workload only')]:
        g = summary.loc[m]
        axes[1].scatter(g.fp, g.tp, label=label, s=70)
    axes[1].plot([0, 80], [0, 17], '--', color='#64748b', label='Random selection, expected')
    axes[1].set(xlabel='False warnings / 80', ylabel='High students detected / 17', title='Detection against false warnings', xlim=(0, 80), ylim=(0, 17.5))
    axes[1].legend(fontsize=8)
    fig.tight_layout(); fig.savefig(out/'warning-tradeoffs.png', dpi=180); plt.close(fig)
    g = summary.loc['selected_rf']
    fig, ax = plt.subplots(figsize=(5, 4))
    matrix = np.array([[g.tn, g.fp], [g.fn, g.tp]])
    ax.imshow(matrix, cmap='Blues', vmin=0)
    for (i, j), value in np.ndenumerate(matrix):
        ax.text(j, i, f'{value:.1f}', ha='center', va='center', fontsize=16,
                color='white' if value > .6*matrix.max() else 'black')
    ax.set(xticks=[0, 1], xticklabels=['No warning', 'Warning'], yticks=[0, 1],
           yticklabels=['Below-high', 'High'], xlabel='Model decision', ylabel='Measured group', title='RF mean confusion counts over five repetitions')
    fig.tight_layout(); fig.savefig(out/'confusion-matrix.png', dpi=180); plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('out', type=Path)
    parser.add_argument('--wait', action='store_true', help='Wait for the checkpointed permutation computation')
    args = parser.parse_args()
    out = args.out.resolve()
    while args.wait:
        current = v.read(out/'manifest.json')
        if current['status'] == 'failed':
            raise RuntimeError(current.get('error', 'Validation computation failed'))
        if current['status'] == 'complete':
            break
        time.sleep(30)
    evaluation = v.collect(out)
    assert evaluation and evaluation['pvalue_is_final'] and all(evaluation['historical_metric_match'].values())
    predictions = pd.read_csv(out/'held-out-predictions.csv')
    verification = verify(out, predictions)
    c = v.read(out/'config.json')
    intervals = conditional_intervals(predictions, c)
    intervals.to_csv(out/'conditional-student-bootstrap-intervals.csv', index=False)
    repeats = pd.read_csv(out/'repeat-metrics.csv')
    summary = pd.read_csv(out/'metrics-summary.csv').set_index('method')
    null = pd.read_csv(out/'permutation-metrics.csv')
    exceed = int((null.balanced_accuracy >= evaluation['observed_balanced_accuracy']).sum())
    figures(out, predictions, summary, null)
    rf = predictions[predictions.method == 'selected_rf'].copy()
    rf['false_warning'] = (rf.actual_class == 0) & (rf.predicted_class == 1)
    rf['missed_high'] = (rf.actual_class == 1) & (rf.predicted_class == 0)
    rf.groupby('student_index').agg(actual_class=('actual_class', 'first'), warnings=('predicted_class', 'sum'),
        false_warnings=('false_warning', 'sum'), missed_high=('missed_high', 'sum')).to_csv(out/'student-warning-frequency.csv')
    repeats.groupby('method')[['recall', 'precision', 'balanced_accuracy', 'tp', 'fp']].agg(['min', 'max']).to_csv(out/'repetition-ranges.csv')
    paired = []
    for other in ['real_only_rf', 'workload_logistic']:
        for rep in range(1, 6):
            a = repeats[(repeats.method == 'selected_rf') & (repeats['repeat'] == rep)].iloc[0]
            b = repeats[(repeats.method == other) & (repeats['repeat'] == rep)].iloc[0]
            paired.append({'comparison': f'selected_rf minus {other}', 'repeat': rep,
                           **{m: float(a[m]-b[m]) for m in ['recall', 'precision', 'balanced_accuracy', 'tp', 'fp', 'f2']}})
    pd.DataFrame(paired).to_csv(out/'paired-comparisons.csv', index=False)
    g = summary.loc['selected_rf']
    workload = summary.loc['workload_logistic']
    names = {'selected_rf': 'Selected eight-input RF', 'real_only_rf': 'Eight-input RF without augmentation',
             'workload_logistic': 'Workload-only logistic', 'random_same_warning_count': 'Random, same warning count',
             'warn_everyone': 'Warn everyone', 'warn_nobody': 'Warn nobody'}
    metric_names = {'recall': 'Recall', 'precision': 'Precision', 'balanced_accuracy': 'Balanced accuracy'}
    manifest = v.read(out/'manifest.json')
    elapsed = (datetime.fromisoformat(manifest['updated_utc'])-datetime.fromisoformat(manifest['started_utc'])).total_seconds()/3600
    lines = ['# Selected RF: validation report', '',
        'Completed: '+datetime.now(timezone.utc).astimezone(ZoneInfo('Asia/Beirut')).isoformat()+' (Asia/Beirut)', '',
        '## Finding', '',
        f'The regenerated selected procedure detects {g.tp:.1f} of 17 High students and produces {g.fp:.1f} false warnings among 80 Below-high students per repetition. Recall is {g.recall:.1%}; precision is {g.precision:.1%}. A warning remains uncertain for an individual student.', '',
        f'The workload-only logistic baseline detects {workload.tp:.1f}/17 with {workload.fp:.1f} false warnings: recall {workload.recall:.1%}, precision {workload.precision:.1%}. It has higher mean recall, precision, balanced accuracy and F2 than the selected RF at the same mean false-warning count in this comparison. This challenges a claim that the eight-input RF is needed for the warning task. Workload-only average precision is lower ({workload.average_precision:.3f} versus RF {g.average_precision:.3f}); performance at the chosen warning rule and ranking across all thresholds are different properties.', '',
        '## Methods and evidence recovery', '',
        'The historical prediction/model folders were absent and no copy was found in the local Desktop, Documents, Downloads or OneDrive searches, including Git-ignored files. The search found two 20-row artificial software fixtures; those are not study results. Some unrelated build and temporary folders were inaccessible. Original model files were not recovered or replaced. The raw CSV and prepared SAV hashes matched the recorded inputs. This run regenerated only the selected eight-input RF procedure and required baselines using the existing helpers and pinned main-package versions; it did not recreate every historical experiment.', '',
        'High means measured primary burnout_score >=4 (17 students), versus 80 Below-high students. These study-defined groups are not clinical diagnoses. All five original stratified five-fold repetitions and four inner folds were retained. Each training group selected depth 2/3, leaf size 5/10, normalized relative High weight 1/2/4, augmentation ratio 0/.5/1 and warning threshold 0..1 in .05 steps by inner F2, with original tie rules. Each forest has 100 trees. Only excluded real students contributed evaluation predictions; all synthetic parents and learned transformations stayed in training. The final all-data model recipe was not changed.', '',
        'The workload-only comparator used logistic regression with fixed C=1, training-only standardized workload and inner-selected relative High weight 1/2/4 and threshold from the same grid. The random comparator analytically selects the same warning count within each outer test fold. Its counts are expectations, and its nonlinear metrics are calculated from expected counts; it is a descriptive reference rather than a deployable rule or inferential test.', '',
        '## Matched comparisons', '',
        '| Procedure | Recall | Precision | High detected /17 | False warnings /80 | Balanced accuracy |',
        '|---|---:|---:|---:|---:|---:|']
    for m in ['selected_rf', 'real_only_rf', 'workload_logistic', 'random_same_warning_count', 'warn_everyone', 'warn_nobody']:
        r = summary.loc[m]
        lines.append(f'| {names[m]} | {r.recall:.1%} | {r.precision:.1%} | {r.tp:.2f} | {r.fp:.2f} | {r.balanced_accuracy:.1%} |')
    lines += ['', 'All seven recorded RF means reproduce: recall, precision, F2, true positives, false positives, average precision and ROC AUC. Counts and metrics average five repetitions of the same 97 people, not 485 independent students.', '',
        '| Learned procedure | F2 | ROC AUC | Average precision | Warnings /97 |',
        '|---|---:|---:|---:|---:|']
    for m in ['selected_rf', 'real_only_rf', 'workload_logistic']:
        r = summary.loc[m]
        lines.append(f'| {names[m]} | {r.f2:.3f} | {r.roc_auc:.3f} | {r.average_precision:.3f} | {r.flagged:.1f} |')
    lines += ['',
        '## Chance diagnostic', '',
        f'The predeclared statistic was mean repetition balanced accuracy. All {c["permutations"]} shuffles preserved overall class counts and assigned one shuffled label per student, shared across repetitions. Each null run rebuilt stratified folds and repeated the full RF preprocessing, augmentation and inner selection procedure. Real-label statistic: {evaluation["observed_balanced_accuracy"]:.6f}. Null mean: {null.balanced_accuracy.mean():.6f}; null range: {null.balanced_accuracy.min():.6f} to {null.balanced_accuracy.max():.6f}. Corrected one-sided permutation p-value: {evaluation["pvalue"]:.4f}.', '',
        f'{exceed} of {len(null)} shuffled-label evaluations reached or exceeded the real-label statistic. The finite-permutation correction gives (1+{exceed})/(1+{len(null)}) = {evaluation["pvalue"]:.4f}; a finite run cannot establish a zero p-value. This diagnostic concerns the fixed procedure in this dataset. It does not reproduce the entire historical search across algorithms, features and human decisions, so it cannot remove earlier selection optimism or establish useful precision, external performance, causality or clinical utility.', '',
        '## Uncertainty', '',
        'Repetition ranges describe split sensitivity. Conditional 95% percentile bootstrap intervals use 2,000 class-stratified student resamples, preserving all five predictions for each sampled student and using paired samples across methods. They condition on observed class counts and fitted predictions; they omit model refitting, historical selection and external-population uncertainty. They are not definitive confidence intervals for deployment performance.', '',
        '| RF metric | Conditional 95% interval |', '|---|---:|']
    for row in intervals[intervals.comparison == 'selected_rf'].itertuples():
        lines.append(f'| {metric_names[row.metric]} | {row.lower:.1%} to {row.upper:.1%} |')
    lines += ['', '| RF minus workload-only | Conditional 95% interval, percentage points |', '|---|---:|']
    for row in intervals[intervals.comparison == 'selected_rf minus workload_logistic'].itertuples():
        lines.append(f'| {metric_names[row.metric]} | {100*row.lower:.1f} to {100*row.upper:.1f} |')
    rf_repeats = repeats[repeats.method == 'selected_rf']
    lines += ['', f'RF recall ranges from {rf_repeats.recall.min():.1%} to {rf_repeats.recall.max():.1%} across repetitions; false warnings range from {rf_repeats.fp.min():.0f} to {rf_repeats.fp.max():.0f}. Every paired RF-minus-workload interval above includes zero. The observed workload advantage therefore remains uncertain under this conditional analysis.', '']
    lines += ['', '## Warning trade-off and synthetic check', '',
        'The threshold curve is descriptive: it applies common triggers to saved outer scores. The marked selected procedure used fold-specific inner-selected thresholds and need not lie on that common-threshold curve. No new threshold was selected from outer outcomes; the separately documented saved-model threshold remains .35.', '',
        'The historical 970-profile simulation (159/170 assumed High profiles detected, recall 93.5%) used profiles derived from training students and inherited labels. It remains a separate simulation, not new measured students, independent validation or a replacement for the reproduced 87.1% real cross-validation recall. Its missing historical outputs were not regenerated in this task.', '',
        '## Interpretation and remaining limits', '',
        'Recommendation: retain the historical RF artifact/recipe and report the workload-only comparator prominently. This evaluation provides no demonstrated warning advantage for the eight-input RF over workload alone. The baseline was proposed after inspecting historical results and remains exploratory; do not promote it to an independently validated replacement. Comparing different algorithms/input sets does not isolate the incremental value of AI inputs. Use the paired conditional intervals to describe uncertainty, not to claim definitive superiority.', '',
        'Only 17 real High students support these estimates, and many exploratory comparisons have reused all 97 respondents. New random splits cannot create an untouched cohort retrospectively. Freeze the chosen procedure before any future evaluation on new real students with measured BAT outcomes. This phase has no new recruitment, independent validation, calibrated clinical probabilities or validated intervention.', '',
        '## Historical comparisons to retain in the paper', '',
        'The project record describes SVC with eight/23 inputs, TabPFN and its threshold/mixture refinements, RF/logistic mixtures, expanded forest tuning, question-subset/backward selection and Boruta. These did not establish a uniform improvement for the chosen detection/false-warning priority. Some improved precision or ranking while losing detections or adding false warnings; group these trade-offs in the paper instead of presenting every unsuccessful parameter trial as a separate contribution.', '',
        'This validation regenerated the selected RF and simple baselines only. The earlier comparison outputs remain unavailable here, so their detailed tables are historical documentation rather than newly reverified evidence. Preserve their recorded methods/results in `research/07-classification-experiments-and-methods.md` and `research/06-data-analysis-and-experiment-history.md`; inspect original outputs before making new exact claims about them. Numerical-score regression remains a separate task and should not be ranked against classifier recall.', '',
        '## Verification and artifacts', '',
        f'Checks passed for all {verification["fold_checkpoints"]:,} fold checkpoints and {verification["candidates_checked"]:,} candidate selections. Verification independently scored all {verification["null_procedures_independently_scored"]} null procedures and recomputed the p-value, regenerated all {verification["real_training_pools_regenerated"]} real-training synthetic pools, refitted the {verification["selected_real_outer_refits"]} selected real outer models and replayed one full real and one full null search. It did not refit every null model. Source hashes remained unchanged.', '',
        f'Elapsed time from the first audit attempt to completed primary computation: {elapsed:.2f} hours, using four single-threaded workers for the full permutation stage. The pilot fold took 10.8 seconds alone; folds took longer under concurrent load. Runtime records are retained in every checkpoint.', '',
        f'Local audit: `{out.relative_to(v.ROOT).as_posix()}/`. Participant-level files remain excluded from Git. The tracked report contains aggregates only. Figures: `permutation-test.png`, `warning-tradeoffs.png`, `confusion-matrix.png`. Supporting CSVs contain the complete confusion counts, warning rates, metrics, paired comparisons, conditional intervals, descriptive threshold curve and student warning frequencies.', '',
        'The audit also preserves `frozen-recipe.json`: the eight-input schema, allowed codes, recorded 100-tree/depth-3/leaf-10/High-weight-2/.35-threshold/zero-augmentation recipe, configuration hash and package versions. The original model binary and metadata remain missing, so an original-artifact backup was not possible and no model-file hash is claimed. The recipe record is not a trained model.', '',
        'Methods references: [scikit-learn permutation testing](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html); [nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html).', '']
    text = '\n'.join(lines)
    (out/'report.md').write_text(text, encoding='utf-8')
    (v.ROOT/'results/25-random-forest-validation-report.md').write_text(text, encoding='utf-8')
    verification['artifact_sha256'] = {p.name: v.training.sha256(p) for p in out.iterdir() if p.is_file() and p.name not in ['verification.json', 'manifest.json']}
    verification['report_script_sha256'] = v.training.sha256(__file__)
    v.write(out/'verification.json', verification)
    manifest = v.read(out/'manifest.json')
    v.write(out/'manifest.json', {**manifest, 'report_verified': True, 'report_path': 'results/25-random-forest-validation-report.md',
                                 'report_script_sha256': verification['report_script_sha256']})
    print(json.dumps({'report': str(v.ROOT/'results/25-random-forest-validation-report.md'), 'verification': verification['passed']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
