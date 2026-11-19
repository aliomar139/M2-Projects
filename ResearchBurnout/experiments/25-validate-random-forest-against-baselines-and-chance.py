"""Rebuild only selected-RF evidence; checkpoint full-procedure permutations."""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import time
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('augmentation', Path(__file__).with_name('11-augment-high-burnout-classifiers.py'))
aug = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aug)
binary, training = aug.binary, aug.training


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def labels_for(y, permutation, seed):
    if permutation == 0:
        return y.copy()
    # One student-level shuffle, reused unchanged in every CV repetition.
    return np.random.default_rng(np.random.SeedSequence([seed, permutation])).permutation(y)


def outer_splits(y, base, search):
    for rep, seed in enumerate(base['cv']['outer_seeds'], 1):
        for fold, (train, test) in enumerate(StratifiedKFold(search['outer_folds'],
                shuffle=True, random_state=seed).split(np.zeros(len(y)), y), 1):
            yield rep, fold, train, test


def random_expected(y, fold_ids, decisions):
    """Expected confusion counts conditional on each fold's warning count."""
    y, fold_ids, decisions = map(np.asarray, (y, fold_ids, decisions))
    tp = fp = 0.
    for fold in np.unique(fold_ids):
        mask = fold_ids == fold
        k = int(decisions[mask].sum())
        tp += k * y[mask].mean()
        fp += k * (1-y[mask]).mean()
    high, low = int(y.sum()), int((1-y).sum())
    return {'tp': tp, 'fp': fp, 'fn': high-tp, 'tn': low-fp,
            'recall': tp/high, 'precision': tp/(tp+fp) if tp+fp else 0.,
            'specificity': (low-fp)/low, 'balanced_accuracy': (tp/high+(low-fp)/low)/2,
            'flagged': tp+fp, 'f2': 5*tp/(5*tp+4*(high-tp)+fp)}


def permutation_pvalue(observed, null):
    values = np.asarray(null, dtype=float)
    return float((1+np.count_nonzero(values >= observed))/(1+len(values)))


def run_fold(args):
    out, permutation, rep, fold = args
    out = Path(out)
    c = read(out/'config.json')
    base, search, source = [read(out/f'{name}.json') for name in ['base-config', 'binary-config', 'augmentation-config']]
    data = training.load_data(base)
    actual = (data.burnout_score.to_numpy() >= 4).astype(int)
    y = labels_for(actual, permutation, c['permutation_seed'])
    train, test = next((tr, te) for r, f, tr, te in outer_splits(y, base, search) if (r, f) == (rep, fold))
    assert not set(train) & set(test)
    cols = base['input_sets']['small_b']
    X, yt = data[cols].iloc[train], y[train]
    seed = base['cv']['inner_seed']+rep*100+fold
    inner = list(StratifiedKFold(search['inner_folds'], shuffle=True, random_state=seed).split(X, yt))
    started = time.monotonic()
    with threadpool_limits(limits=1):
        warnings.filterwarnings('error', category=ConvergenceWarning)
        pools, generation, inner_memberships = [], [], []

        def generate(frame, target, pool_seed, number):
            gen, provenance, stats = aug.pool(frame, target, base, source['generator'], pool_seed)
            allowed = set(frame.index+1)
            assert all(p['parent_a'] in allowed and p['parent_b'] in allowed
                       and y[p['parent_a']-1] == y[p['parent_b']-1] == 1 for p in provenance)
            generation.append({'inner_fold': number, 'seed': pool_seed, **stats,
                               **({'profiles': provenance} if permutation == 0 else {})})
            return gen

        for number, (tr, va) in enumerate(inner, 1):
            assert not set(tr) & set(va)
            gen = generate(X.iloc[tr], yt[tr], source['generator']['seed']+rep*10000+fold*100+number, number)
            pools.append((tr, va, gen))
            inner_memberships.append({'inner_fold': number, 'train': (train[tr]+1).tolist(),
                                      'validation': (train[va]+1).tolist()})
        gen = generate(X, yt, source['generator']['seed']+rep*10000+fold*100, 0)
        candidates, choices, parts_zero = [], [], None
        for ratio in [0, *source['ratios']]:
            parts = []
            for tr, va, generated in pools:
                Xt, Xv, labels, _ = aug.prepare(X.iloc[tr], yt[tr], X.iloc[va], generated, ratio, base)
                parts.append((va, Xt, Xv, labels))
            chosen, records = aug.search(search, 'forest', parts, yt, seed)
            candidates.extend({'ratio': ratio, **r} for r in records)
            choices.append((ratio, chosen))
            if ratio == 0:
                parts_zero = parts
        ratio, chosen = max(choices, key=lambda item: (*aug.choice_key(item[1]), -item[0]))
        # Independently check global tie ordering across all 36 candidates.
        control = max(candidates, key=lambda r: (*aug.choice_key(r), -r['ratio']))
        assert control == {'ratio': ratio, **chosen}

        def fit_scores(ratio_value, choice):
            Xt, Xv, labels, added = aug.prepare(X, yt, data[cols].iloc[test], gen, ratio_value, base)
            model = binary.classifier('forest', choice['parameters'], seed).fit(Xt, labels,
                sample_weight=aug.priority.weights(labels, choice['factor'], 1))
            return binary.probabilities(model, Xv), added

        scores, added = fit_scores(ratio, chosen)
        predictions = []

        def save(method, values, threshold):
            for idx, score in zip(test, values):
                predictions.append({'method': method, 'repeat': rep, 'fold': fold,
                    'student_index': int(idx+1), 'actual_class': int(y[idx]),
                    'warning_score': float(score), 'threshold': float(threshold),
                    'predicted_class': int(score >= threshold)})

        save('selected_rf', scores, chosen['chosen_threshold']['threshold'])
        if permutation == 0:
            zero = choices[0][1]
            zs, _ = fit_scores(0, zero)
            save('real_only_rf', zs, zero['chosen_threshold']['threshold'])
            workload = []
            for factor in c['workload_baseline']['relative_high_weights']:
                oof = np.full(len(train), np.nan)
                for (tr, va), (valid, Xt, Xv, labels) in zip(inner, parts_zero):
                    assert np.array_equal(va, valid)
                    wt, wv = aug.kernels.transform(base, ['workload'], X[['workload']].iloc[tr], X[['workload']].iloc[va])
                    model = LogisticRegression(C=c['workload_baseline']['C'], max_iter=10000).fit(wt, yt[tr],
                        sample_weight=aug.priority.weights(yt[tr], factor, 1))
                    oof[va] = binary.probabilities(model, wv)
                best, thresholds = binary.best_threshold(yt, oof, search['probability_thresholds'])
                workload.append({'factor': factor, 'chosen_threshold': best, 'threshold_candidates': thresholds})
            wc = max(workload, key=aug.choice_key)
            wt, wv = aug.kernels.transform(base, ['workload'], X[['workload']], data[['workload']].iloc[test])
            model = LogisticRegression(C=c['workload_baseline']['C'], max_iter=10000).fit(wt, yt,
                sample_weight=aug.priority.weights(yt, wc['factor'], 1))
            save('workload_logistic', binary.probabilities(model, wv), wc['chosen_threshold']['threshold'])
        else:
            workload, wc = [], None
        compact = [{k: v for k, v in r.items() if k != 'threshold_candidates'} for r in candidates]
        result = {'permutation': permutation, 'repeat': rep, 'fold': fold,
            'train': (train+1).tolist(), 'test': (test+1).tolist(),
            'inner_memberships': inner_memberships, 'label_sha256': __import__('hashlib').sha256(y.tobytes()).hexdigest(),
            'selected': {'ratio': ratio, **{k: v for k, v in chosen.items() if k != 'threshold_candidates'}},
            'synthetic_added': added, 'candidates': candidates if permutation == 0 else compact,
            'workload_candidates': workload, 'workload_selected': wc,
            'predictions': predictions, 'generation': generation,
            'seconds': time.monotonic()-started}
        write(out/'folds'/f'p{permutation:03d}-r{rep}-f{fold}.json', result)
        return permutation, rep, fold, result['seconds']


def metrics_frame(predictions):
    rows = []
    for (method, rep), g in predictions.groupby(['method', 'repeat']):
        assert len(g) == 97 and g.student_index.nunique() == 97 and g.actual_class.sum() == 17
        rows.append({'method': method, 'repeat': int(rep), **binary.metrics(g.actual_class, g.predicted_class),
            'roc_auc': float(roc_auc_score(g.actual_class, g.warning_score)),
            'average_precision': float(average_precision_score(g.actual_class, g.warning_score))})
    return pd.DataFrame(rows)


def collect(out):
    c = read(out/'config.json')
    real = [read(p) for p in sorted((out/'folds').glob('p000-*.json'))]
    if len(real) != 25:
        return None
    predictions = pd.DataFrame([p for f in real for p in f['predictions']])
    selected = predictions[predictions.method == 'selected_rf']
    for method, value in [('warn_everyone', 1), ('warn_nobody', 0)]:
        p = selected.copy()
        p['method'], p['warning_score'], p['threshold'], p['predicted_class'] = method, float(value), .5, value
        predictions = pd.concat([predictions, p], ignore_index=True)
    repeats = metrics_frame(predictions)
    random_rows = []
    for rep, g in selected.groupby('repeat'):
        random_rows.append({'method': 'random_same_warning_count', 'repeat': int(rep),
                            **random_expected(g.actual_class, g.fold, g.predicted_class)})
    repeats = pd.concat([repeats, pd.DataFrame(random_rows)], ignore_index=True)
    predictions.to_csv(out/'held-out-predictions.csv', index=False)
    repeats.to_csv(out/'repeat-metrics.csv', index=False)
    summary = repeats.groupby('method').mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    observed = float(summary.loc['selected_rf', 'balanced_accuracy'])
    historical = {'recall': 0.8705882352941177, 'precision': 0.3465639230,
                  'f2': 0.6678476490, 'tp': 14.8, 'fp': 28.,
                  'average_precision': .5268606663, 'roc_auc': .8089705882}
    match = {k: bool(np.isclose(summary.loc['selected_rf', k], v, atol=1e-9, rtol=0)) for k, v in historical.items()}
    null_rows = []
    for perm in range(1, c['permutations']+1):
        files = sorted((out/'folds').glob(f'p{perm:03d}-*.json'))
        if len(files) != 25:
            continue
        p = pd.DataFrame([p for path in files for p in read(path)['predictions']])
        m = metrics_frame(p).mean(numeric_only=True)
        null_rows.append({'permutation': perm, **{k: float(m[k]) for k in ['balanced_accuracy', 'recall', 'precision', 'f2']}})
    pd.DataFrame(null_rows).to_csv(out/'permutation-metrics.csv', index=False)
    result = {'historical_metric_match': match, 'observed_balanced_accuracy': observed,
        'permutations_completed': len(null_rows), 'permutations_requested': c['permutations'],
        'pvalue': permutation_pvalue(observed, [r['balanced_accuracy'] for r in null_rows]) if null_rows else None,
        'pvalue_is_final': len(null_rows) == c['permutations'],
        'historical_selection_bias_accounted_for': False}
    write(out/'evaluation-summary.json', result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, help='Resume an existing audit directory')
    parser.add_argument('--stage', choices=['pilot', 'real', 'permutations', 'collect'], default='real')
    args = parser.parse_args()
    config_path = ROOT/'experiments/25-validate-random-forest-against-baselines-and-chance-settings.json'
    c = read(config_path)
    out = args.out
    if out is None:
        out = ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        (out/'folds').mkdir(parents=True, exist_ok=False)
        write(out/'config.json', c)
        for name, key in [('base-config', 'base_config'), ('binary-config', 'binary_config'), ('augmentation-config', 'augmentation_config')]:
            write(out/f'{name}.json', read(ROOT/c[key]))
        paths = [Path(__file__), config_path, ROOT/c['base_config'], ROOT/c['binary_config'], ROOT/c['augmentation_config']]
        paths += [Path(m.__file__) for m in [aug, binary, binary.ensemble, training, aug.kernels, aug.priority]]
        base = read(ROOT/c['base_config'])
        paths += [ROOT/base['dataset'], ROOT/base['derived_indicator_reconstruction']['raw_csv']]
        write(out/'manifest.json', {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
            'source_sha256': {str(p.relative_to(ROOT)): training.sha256(p) for p in paths},
            'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'scipy', 'pyreadstat', 'xgboost', 'threadpoolctl']},
            'historical_outputs_recovered': False, 'scope': 'Regenerated selected eight-input RF only; previous output folders remain absent.',
            'final_model_replaced': False, 'real_students': 97, 'permutation_unit': 'student', 'stage': args.stage})
    else:
        out = out.resolve()
        c = read(out/'config.json')
    print(f'Audit directory: {out}', flush=True)
    manifest = read(out/'manifest.json')
    assert all(training.sha256(ROOT/p) == h for p, h in manifest['source_sha256'].items()), 'Sources changed since audit creation'
    if args.stage == 'collect':
        print(json.dumps(collect(out), indent=2), flush=True)
        return
    perms = [0] if args.stage in ['pilot', 'real'] else list(range(1, c['permutations']+1))
    jobs = [(str(out), p, r, f) for p in perms for r in range(1, 6) for f in range(1, 6)
            if not (out/'folds'/f'p{p:03d}-r{r}-f{f}.json').exists()]
    if args.stage == 'pilot':
        jobs = jobs[:1]
    write(out/'manifest.json', {**manifest, 'stage': args.stage, 'status': 'running'})
    try:
        with ProcessPoolExecutor(max_workers=c['workers']) as executor:
            futures = [executor.submit(run_fold, job) for job in jobs]
            for done, future in enumerate(as_completed(futures), 1):
                p, r, f, seconds = future.result()
                print(f'{done}/{len(jobs)}: permutation {p}, repeat {r}, fold {f}, {seconds:.1f}s', flush=True)
                if args.stage == 'permutations' and done % 25 == 0:
                    collect(out)
        result = collect(out)
        assert all(training.sha256(ROOT/p) == h for p, h in manifest['source_sha256'].items())
        if result and not all(result['historical_metric_match'].values()):
            raise AssertionError('Regenerated RF metrics differ from history; investigate before interpreting permutations')
        complete = bool(result and result['pvalue_is_final'])
        write(out/'manifest.json', {**manifest, 'stage': args.stage, 'status': 'complete' if complete else 'partial',
            'source_files_unchanged': True, 'updated_utc': datetime.now(timezone.utc).isoformat(),
            'completed_folds': len(list((out/'folds').glob('*.json')))})
        print(json.dumps(result, indent=2), flush=True)
    except Exception as exc:
        write(out/'manifest.json', {**manifest, 'stage': args.stage, 'status': 'failed', 'error': str(exc)})
        raise


if __name__ == '__main__':
    main()
