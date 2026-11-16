"""Unique constrained binary-training augmentation, with untouched real-only evaluation."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('binary', Path(__file__).with_name('train-binary.py'))
binary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(binary)
training, kernels, priority = binary.training, binary.kernels, binary.priority


def pool(X, y, base, config, seed):
    cols = list(X)
    blocked = [c for c in cols if c in base['category_levels'] or c == 'enrolled_lebanon' or c.startswith('ai_use_')]
    ordinal = [c for c in cols if c not in blocked]
    original = X.to_numpy(dtype=int)
    oi = [cols.index(c) for c in ordinal]
    bi = [cols.index(c) for c in blocked]
    assert np.isin(original[:, oi], [1, 2, 3, 4, 5]).all()
    high = np.flatnonzero(y == 1)
    requested = len(high)
    neighbors = {}
    def distance(a, b):
        return float((np.abs(a[oi]-b[oi]).sum()/4 + (a[bi] != b[bi]).sum())/len(cols))
    for a in high:
        eligible = []
        for b in high:
            if a == b or np.max(np.abs(original[a, oi]-original[b, oi])) > config['max_ordinal_gap']:
                continue
            d = distance(original[a], original[b])
            if d <= config['max_parent_distance']:
                eligible.append((d, int(b)))
        if eligible:
            neighbors[int(a)] = [b for _, b in sorted(eligible)[:config['nearest_neighbors']]]
    rng = np.random.default_rng(seed)
    known = {tuple(row) for row in original}
    generated, provenance = [], []
    attempts = 0
    anchors = sorted(neighbors)
    while anchors and len(generated) < requested and attempts < requested*config['attempts_per_requested']:
        attempts += 1
        a = int(rng.choice(anchors))
        b = int(rng.choice(neighbors[a]))
        fraction = float(rng.uniform(*config['fraction_range']))
        row = original[a].copy()
        interpolated = (1-fraction)*original[a, oi] + fraction*original[b, oi]
        lower = np.floor(interpolated)
        row[oi] = (lower + (rng.random(len(oi)) < interpolated-lower)).astype(int)
        d = distance(row, original[a])
        key = tuple(row)
        if key in known or d > config['max_anchor_distance']:
            continue
        assert y[a] == y[b] == 1
        assert np.array_equal(row[bi], original[a, bi])
        assert np.isin(row[oi], [1, 2, 3, 4, 5]).all()
        known.add(key)
        generated.append(row)
        provenance.append(dict(zip(cols, row.tolist()), synthetic_class=1, label_inferred=True,
            parent_a=int(X.index[a]+1), parent_b=int(X.index[b]+1), fraction=fraction,
            parent_distance=distance(original[a], original[b]), anchor_distance=d,
            ordinal=int(len(generated)), in_half_batch=bool(len(generated) <= int(np.ceil(requested*.5)))))
    assert len({tuple(row) for row in generated}) == len(generated)
    assert not {tuple(row) for row in generated} & {tuple(row) for row in original}
    return pd.DataFrame(generated, columns=cols), provenance, {
        'training_n': len(X), 'real_high_n': requested, 'requested': requested,
        'generated': len(generated), 'attempts': attempts, 'eligible_anchors': len(anchors)}


def prepare(X, y, valid, generated, ratio, base):
    n = min(len(generated), int(np.ceil(np.count_nonzero(y == 1)*ratio)))
    augmented = pd.concat([X, generated.iloc[:n]], ignore_index=True)
    labels = np.concatenate([y, np.ones(n, dtype=int)])
    Xt, Xv = kernels.transform(base, list(X), augmented, valid)
    assert len(Xt) == len(labels) and np.isfinite(Xt).all() and np.isfinite(Xv).all()
    return Xt, Xv, labels, n


def search(reference, family, parts, y, seed):
    candidates = []
    for factor in reference['relative_high_weights']:
        for params in ParameterGrid(reference['grids'][family]):
            oof, seen = np.full(len(y), np.nan), np.zeros(len(y), dtype=int)
            for va, Xt, Xv, labels in parts:
                model = binary.classifier(family, params, seed).fit(Xt, labels,
                    sample_weight=priority.weights(labels, factor, 1))
                oof[va] = binary.probabilities(model, Xv)
                seen[va] += 1
            assert np.isfinite(oof).all() and np.all(seen == 1)
            chosen, thresholds = binary.best_threshold(y, oof, reference['probability_thresholds'])
            candidates.append({'factor': factor, 'parameters': params, 'chosen_threshold': chosen,
                'threshold_candidates': thresholds})
    return max(candidates, key=choice_key), candidates


def choice_key(choice):
    t = choice['chosen_threshold']
    return t['f2'], t['precision'], t['recall'], t['threshold']


def run_job(args):
    config, reference, base, data, rep, fold, train, test, inputs, old_tuning, old_predictions = args
    with threadpool_limits(limits=1):
        warnings.filterwarnings('error', category=ConvergenceWarning)
        cols = base['input_sets'][inputs]
        assert not any(c.startswith('BAT') or 'burnout' in c for c in cols)
        X = data[cols].iloc[train]
        y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed']+rep*100+fold
        inner = list(StratifiedKFold(reference['inner_folds'], shuffle=True, random_state=seed).split(train, y))
        generated_rows, generation, validation_rows, pools = [], [], [], []
        for number, (tr, va) in enumerate(inner, 1):
            assert not set(tr) & set(va)
            pool_seed = config['generator']['seed']+rep*10000+fold*100+number
            gen, provenance, stats = pool(X.iloc[tr], y[tr], base, config['generator'], pool_seed)
            pools.append((tr, va, gen))
            context = {'input_set': inputs, 'repeat': rep, 'fold': fold, 'inner_fold': number}
            generated_rows.extend([{**context, **row} for row in provenance])
            generation.append({**context, **stats})
            validation_rows.extend({**context, 'student_index': int(train[i]+1)} for i in va)
        gen, provenance, stats = pool(X, y, base, config['generator'],
            config['generator']['seed']+rep*10000+fold*100)
        context = {'input_set': inputs, 'repeat': rep, 'fold': fold, 'inner_fold': 0}
        generated_rows.extend([{**context, **row} for row in provenance])
        generation.append({**context, **stats})
        predictions, tuning = [], []
        fitted = {}
        for ratio in config['ratios']:
            parts = []
            for tr, va, inner_gen in pools:
                Xt, Xv, labels, _ = prepare(X.iloc[tr], y[tr], X.iloc[va], inner_gen, ratio, base)
                parts.append((va, Xt, Xv, labels))
            Xt, Xtest, labels, added = prepare(X, y, data[cols].iloc[test], gen, ratio, base)
            method = 'synthetic_half' if ratio == .5 else 'synthetic_full'
            for family in reference['grids']:
                chosen, candidates = search(reference, family, parts, y, seed)
                model = binary.classifier(family, chosen['parameters'], seed).fit(Xt, labels,
                    sample_weight=priority.weights(labels, chosen['factor'], 1))
                scores = binary.probabilities(model, Xtest)
                fitted[(family, ratio)] = chosen, scores
                tuning.append({'input_set': inputs, 'model': family, 'repeat': rep, 'fold': fold,
                    'augmentation': method, 'added': added, 'chosen': chosen, 'candidates': candidates})
                for idx, score in zip(test, scores):
                    predictions.append({'input_set': inputs, 'model': family, 'augmentation': method,
                        'repeat': rep, 'fold': fold, 'student_index': int(idx+1),
                        'actual_class': int(data.burnout_score.iloc[idx] >= 4), 'actual_score': float(data.burnout_score.iloc[idx]),
                        'warning_score': float(score), 'threshold': chosen['chosen_threshold']['threshold'],
                        'predicted_class': int(score >= chosen['chosen_threshold']['threshold'])})
        for family in reference['grids']:
            old = next(r for r in old_tuning if r['input_set'] == inputs and r['model'] == family and r['repeat'] == rep and r['fold'] == fold)
            alternatives = [(0, old['chosen'])]+[(ratio, fitted[(family, ratio)][0]) for ratio in config['ratios']]
            ratio, chosen = max(alternatives, key=lambda item: (*choice_key(item[1]), -item[0]))
            tuning.append({'input_set': inputs, 'model': family, 'repeat': rep, 'fold': fold,
                'augmentation': 'inner_selected_ratio', 'selected_ratio': ratio, 'chosen': chosen})
            if ratio:
                source = [r for r in predictions if r['model'] == family and r['augmentation'] == ('synthetic_half' if ratio == .5 else 'synthetic_full')]
            else:
                source = [dict(r, augmentation='real_only') for r in old_predictions if r['input_set'] == inputs and r['model'] == family
                    and r['repeat'] == rep and r['fold'] == fold and r['procedure'] == 'inner_f2_threshold']
            assert len(source) == len(test)
            predictions.extend([{k: v for k, v in dict(r, augmentation='inner_selected_ratio').items()
                if k not in ['procedure', 'score_kind']} for r in source])
        return predictions, tuning, generated_rows, generation, validation_rows


def report(result, out):
    keys = ['input_set', 'model', 'augmentation', 'repeat']
    rows = []
    for key, group in result.groupby(keys):
        assert len(group) == 97 and group.student_index.nunique() == 97 and group.actual_class.sum() == 17
        rows.append(dict(zip(keys, key), **binary.metrics(group.actual_class, group.predicted_class),
            average_precision=float(average_precision_score(group.actual_class, group.warning_score)),
            roc_auc=float(roc_auc_score(group.actual_class, group.warning_score))))
    repeats = pd.DataFrame(rows)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby(keys[:3]).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    repeats[keys+['tp', 'fp', 'fn', 'tn']].to_csv(out/'confusion-matrices.csv', index=False)
    changes = []
    for row in repeats[repeats.augmentation.isin(['synthetic_half', 'synthetic_full', 'inner_selected_ratio'])].itertuples():
        refs = repeats[(repeats['repeat'] == row.repeat) &
            (((repeats.model == row.model) & (repeats.input_set == row.input_set) & (repeats.augmentation == 'real_only')) |
             ((repeats.model == 'ridge_svr_blend') & (repeats.augmentation == 'reference_inner_f2_threshold')))]
        assert len(refs) == 2
        for ref in refs.itertuples():
            changes.append({'input_set': row.input_set, 'model': row.model, 'augmentation': row.augmentation,
                'repeat': row.repeat, 'reference': ref.model if ref.model == 'ridge_svr_blend' else 'matched_real_only',
                'f2_difference': row.f2-ref.f2, 'recall_difference': row.recall-ref.recall,
                'precision_difference': row.precision-ref.precision, 'false_warnings_difference': row.fp-ref.fp})
    pd.DataFrame(changes).to_csv(out/'paired-comparisons.csv', index=False)
    lines = ['# Unique synthetic-data binary-classification experiment', '',
        '97 real students, High >=4 (17) / Below-high <4 (80). Only real held-out students evaluated.',
        'Identical 5x5 stratified outer / 4 inner folds, models, grids, weights and F2 threshold tuning as the completed binary reference.',
        'Four classifier families on Small B/Broad D; half/full batches request ceil(.5/1 times real training High count). Constraints may produce fewer.',
        'Training High neighbors generate novel ordinal combinations using stochastic rounding; the joint categorical/binary block is copied from one parent.',
        'Duplicates of any real training or generated profile are rejected. No validation or test profiles are consulted during generation.',
        'Synthetic labels are inferred assumptions, not observed BAT scores. Real-only references are copied from unchanged saved results, with fold assignments verified.',
        'inner_selected_ratio chooses among 0/.5/1 using inner scores only. Best-looking fixed-ratio outer results remain exploratory.', '',
        '| Inputs | Model | Training | Recall | Precision | F2 | TP /17 | FP /80 | Average precision |',
        '|---|---|---|---:|---:|---:|---:|---:|---:|']
    for (inputs, model, aug), row in summary.sort_values('f2', ascending=False).iterrows():
        lines.append(f'| {inputs} | {model} | {aug} | {row.recall:.1%} | {row.precision:.1%} | {row.f2:.3f} | {row.tp:.1f} | {row.fp:.1f} | {row.average_precision:.3f} |')
    lines += ['', 'Counts/metrics average repeated evaluation of the same students, not independent replications. Undefined precision is zero.',
        'Generation also changes training emphasis; no matched-extra-weight control isolates the mechanism. Novel legal profiles do not establish realistic human responses or correct labels.',
        'Generated tables retain parent and fold provenance. Profiles can recur across different training folds; uniqueness is enforced within each fit.',
        'No synthetic records are appended to source SAV, SPSS analyses or evaluation data. No deployment model or calibrated clinical risk estimate.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'classification/augmentation-config.json'
    config = json.loads(config_path.read_text())
    reference_path = ROOT/config['reference_run']
    assert json.loads((reference_path/'manifest.json').read_text())['status'] == 'complete'
    reference = json.loads((reference_path/'config.json').read_text())
    base = json.loads((reference_path/'reference-config.json').read_text())
    data = training.load_data(base)
    y = (data.burnout_score.to_numpy() >= 4).astype(int)
    assert len(data) == 97 and np.bincount(y).tolist() == [80, 17]
    old = pd.read_csv(reference_path/'held-out-predictions.csv')
    old_tuning = json.loads((reference_path/'tuning.json').read_text())
    source_paths = [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    source_paths += [reference_path/name for name in ['manifest.json', 'config.json', 'reference-config.json',
        'held-out-predictions.csv', 'outer-folds.csv', 'inner-folds.csv', 'tuning.json']]
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in source_paths}
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    for name, value in [('config', config), ('binary-config', reference), ('reference-config', base)]:
        (out/f'{name}.json').write_text(json.dumps(value, indent=2), encoding='utf-8')
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': training.sha256(__file__), 'config_sha256': training.sha256(config_path),
        'source_sha256': hashes, 'helper_sha256': {Path(m.__file__).name: training.sha256(m.__file__)
            for m in [binary, binary.ensemble, training, kernels, priority]},
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'xgboost', 'pyreadstat', 'threadpoolctl']}}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, profiles, generation, folds, inner_folds, jobs = [], [], [], [], [], [], []
    try:
        for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
            for fold, (train, test) in enumerate(StratifiedKFold(reference['outer_folds'], shuffle=True, random_state=seed).split(data, y), 1):
                assert not set(train) & set(test)
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1), 'actual_class': int(y[i])} for i in test)
                for inputs in reference['input_sets']:
                    saved_choices = [{k: r[k] for k in ['input_set', 'model', 'repeat', 'fold', 'chosen']}
                        for r in old_tuning if r['input_set'] == inputs and r['repeat'] == rep and r['fold'] == fold]
                    jobs.append((config, reference, base, data, rep, fold, train, test, inputs, saved_choices,
                        old[(old['repeat'] == rep) & (old.fold == fold) & (old.input_set == inputs)].to_dict('records')))
        order = ['repeat', 'student_index']
        fold_table = pd.DataFrame(folds)
        pd.testing.assert_frame_equal(fold_table.sort_values(order).reset_index(drop=True),
            pd.read_csv(reference_path/'outer-folds.csv').sort_values(order).reset_index(drop=True))
        with ProcessPoolExecutor(max_workers=config['workers']) as executor:
            futures = {executor.submit(run_job, job): (job[4], job[5], job[8]) for job in jobs}
            for count, future in enumerate(as_completed(futures), 1):
                p, t, s, g, v = future.result()
                predictions.extend(p)
                tuning.extend(t)
                profiles.extend(s)
                generation.extend(g)
                inner_folds.extend(v)
                rep, fold, inputs = futures[future]
                print(f'Completed {count}/50: repetition {rep}, fold {fold}, {inputs}, all four classifiers at both synthetic levels', flush=True)
        inner_table = pd.DataFrame(inner_folds)
        keys = ['repeat', 'fold', 'inner_fold', 'student_index']
        expected = pd.read_csv(reference_path/'inner-folds.csv').rename(columns={'outer_fold': 'fold'})
        for _, group in inner_table.groupby('input_set'):
            pd.testing.assert_frame_equal(group[keys].sort_values(keys).reset_index(drop=True), expected[keys].sort_values(keys).reset_index(drop=True))
        result = pd.DataFrame(predictions)
        selected_old = old[(old.procedure == 'inner_f2_threshold') | (old.model == 'ridge_svr_blend') | (old.input_set == 'baseline')].copy()
        selected_old['augmentation'] = np.where(selected_old.model.isin(reference['grids']), 'real_only', 'reference_'+selected_old.procedure)
        result = pd.concat([result, selected_old[list(result)]], ignore_index=True)
        assert len(result) == 36*97*5
        assert not result.duplicated(['input_set', 'model', 'augmentation', 'repeat', 'student_index']).any()
        assert np.array_equal(result.actual_class, (result.actual_score >= 4).astype(int))
        assert np.array_equal(result.predicted_class, (result.warning_score >= result.threshold).astype(int))
        assert np.allclose(result.actual_score, data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result = result.sort_values(['input_set', 'model', 'augmentation', 'repeat', 'student_index'])
        result.to_csv(out/'held-out-predictions.csv', index=False)
        fold_table.to_csv(out/'outer-folds.csv', index=False)
        inner_table.to_csv(out/'inner-folds.csv', index=False)
        pd.DataFrame(profiles).to_csv(out/'synthetic-profiles.csv', index=False)
        pd.DataFrame(generation).to_csv(out/'generation-counts.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        report(result, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True, reference_folds_reproduced=True,
            synthetic_profile_instances=len(profiles), real_participants=97, deployment_model_saved=False)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
