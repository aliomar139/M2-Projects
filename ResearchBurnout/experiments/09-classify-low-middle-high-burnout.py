"""Separate three-class symptom-band experiment, no changes to regression outputs."""
from datetime import datetime, timezone
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, confusion_matrix,
    f1_score, make_scorer, precision_recall_fscore_support)
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('training', ROOT/'experiments/01-compare-score-prediction-baselines.py')
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)
LABELS = [0, 1, 2]
NAMES = ['Low', 'Middle', 'High']


def make_labels(scores):
    values = np.asarray(scores, dtype=float)
    if not np.isfinite(values).all() or not ((values >= 1) & (values <= 5)).all():
        raise ValueError('Scores must be finite and within 1-5.')
    return np.where(values < 2, 0, np.where(values < 4, 1, 2))


def make_model(base, config, cols, family):
    categories = [col for col in cols if col in base['category_levels']]
    numbers = [col for col in cols if col not in categories]
    blocks = [('categories', OneHotEncoder(categories=[base['category_levels'][col] for col in categories],
        drop='first', handle_unknown='error', sparse_output=False), categories),
        ('numbers', 'passthrough', numbers)]
    steps = [('encode', ColumnTransformer(blocks, remainder='drop'))]
    if family == 'logistic':
        steps += [('scale', StandardScaler()), ('model', LogisticRegression(max_iter=5000, solver='lbfgs'))]
        grid = {'model__C': config['logistic_C'], 'model__class_weight': config['class_weights']}
    elif family == 'forest':
        f = config['forest']
        steps += [('model', RandomForestClassifier(n_estimators=f['n_estimators'],
            random_state=f['random_state'], n_jobs=1))]
        grid = {'model__max_depth': f['max_depth'], 'model__min_samples_leaf': f['min_samples_leaf'],
            'model__class_weight': config['class_weights']}
    else:
        raise ValueError(f'Unknown model: {family}')
    return Pipeline(steps), grid


def calculate_metrics(actual, predicted):
    precision, recall, f1, support = precision_recall_fscore_support(actual, predicted,
        labels=LABELS, zero_division=0)
    result = {'accuracy': accuracy_score(actual, predicted),
        'balanced_accuracy': balanced_accuracy_score(actual, predicted),
        'macro_f1': f1_score(actual, predicted, labels=LABELS, average='macro', zero_division=0)}
    for i, name in enumerate(NAMES):
        result.update({f'{name.lower()}_precision': precision[i], f'{name.lower()}_recall': recall[i],
            f'{name.lower()}_f1': f1[i], f'{name.lower()}_support': int(support[i])})
    a, p = np.asarray(actual), np.asarray(predicted)
    result['high_false_positive_rate'] = float(((p == 2) & (a != 2)).sum()/(a != 2).sum())
    return result


def summarize(predictions, config, out):
    metrics, confusion = [], []
    for key, group in predictions.groupby(['input_set', 'model', 'repeat']):
        assert len(group) == 97 and group.student_index.nunique() == 97
        metrics.append(dict(zip(['input_set', 'model', 'repeat'], key),
            **calculate_metrics(group.actual_class, group.predicted_class)))
        matrix = confusion_matrix(group.actual_class, group.predicted_class, labels=LABELS)
        assert matrix.sum() == 97
        for i in LABELS:
            for j in LABELS:
                confusion.append(dict(zip(['input_set', 'model', 'repeat'], key),
                    actual=NAMES[i], predicted=NAMES[j], count=int(matrix[i, j])))
    metrics = pd.DataFrame(metrics)
    metrics.to_csv(out/'repeat-metrics.csv', index=False)
    pd.DataFrame(confusion).to_csv(out/'confusion-matrices.csv', index=False)
    summary = metrics.groupby(['input_set', 'model']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    stability = metrics.groupby(['input_set', 'model'])[['macro_f1', 'high_recall', 'accuracy']].agg(['min', 'max', 'std'])
    stability.to_csv(out/'repetition-stability.csv')
    lines = ['# Three-class symptom-band classification', '',
        'Exploratory labels: Low [1,2), Middle [2,4), High [4,5]. Not validated clinical categories.',
        '97 real students: Low 6, Middle 74, High 17. No synthetic records or oversampling.',
        'Three stratified outer folds repeated five times, with two-fold inner tuning on macro F1.',
        'Identical splits across classifiers; different from the earlier regression splits. All preprocessing and class-weight calculation use training students only.',
        'Numbers below average five complete-repetition metrics. Each repetition evaluates the same 97 students; these are not independent samples.',
        'Undefined class precision/F1 is reported as zero. No clinical or deployment success threshold has been established.', '',
        '| Inputs | Method | Accuracy | Macro F1 | Balanced accuracy | Low recall | Middle recall | High recall | High precision | High false-positive rate |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for (inputs, model), row in summary.iterrows():
        lines.append(f'| {inputs} | {model} | {row.accuracy:.1%} | {row.macro_f1:.3f} | '
            f'{row.balanced_accuracy:.1%} | {row.low_recall:.1%} | {row.middle_recall:.1%} | '
            f'{row.high_recall:.1%} | {row.high_precision:.1%} | {row.high_false_positive_rate:.1%} |')
    lines += ['', '## Confusion matrices by repetition', '',
        'Rows are measured classes; columns are predicted classes, in Low/Middle/High order. Each matrix totals 97.', '']
    for (inputs, model, repeat), group in predictions.groupby(['input_set', 'model', 'repeat']):
        matrix = confusion_matrix(group.actual_class, group.predicted_class, labels=LABELS)
        lines += [f'### {inputs}, {model}, repetition {repeat}', '',
            '| Actual / predicted | Low | Middle | High |', '|---|---:|---:|---:|']
        for name, row in zip(NAMES, matrix):
            lines.append(f'| {name} | {row[0]} | {row[1]} | {row[2]} |')
        lines += ['']
    lines += ['## Limits', '',
        'Only six Low students make its recall and precision highly uncertain; one student changes per-repetition Low recall by 16.7 percentage points.',
        'Reported High recall concerns the score-band label, not clinically diagnosed burnout. A high accuracy can coexist with missed High students.',
        'No threshold was optimized: predictions use the largest class probability. Changing thresholds or inputs after this run requires another explicitly exploratory experiment.',
        'Previously inspected data have guided this follow-up. Independent new student data are needed for confirmation. No final deployment model is saved.']
    (out/'results.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')


def main():
    config_path = ROOT/'experiments/09-classify-low-middle-high-burnout-settings.json'
    config = json.loads(config_path.read_text())
    base_path = ROOT/config['reference_config']
    base = json.loads(base_path.read_text())
    training.validate_config(base)
    assert config['target_score'] == 'burnout_score' and not config['augmentation']
    hashes = {str(p.relative_to(ROOT)): training.sha256(p) for p in [ROOT/base['dataset'], base_path]}
    df = training.load_data(base)
    y = make_labels(df[config['target_score']])
    counts = np.bincount(y, minlength=3)
    if counts.tolist() != config['expected_counts']:
        raise ValueError(f'Class counts changed: {counts}')
    print(f'Class counts: Low={counts[0]}, Middle={counts[1]}, High={counts[2]}', flush=True)
    out = ROOT/config['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out.mkdir(parents=True, exist_ok=False)
    (out/'config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')
    (out/'reference-config.json').write_text(json.dumps(base, indent=2), encoding='utf-8')
    pd.DataFrame({'class': NAMES, 'count': counts}).to_csv(out/'class-counts.csv', index=False)
    manifest = {'status': 'running', 'started_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': hashes, 'script_sha256': training.sha256(__file__),
        'loader_sha256': training.sha256(training.__file__), 'config_sha256': training.sha256(config_path),
        'packages': {p: version(p) for p in ['numpy', 'pandas', 'scikit-learn', 'pyreadstat']},
        'class_counts': dict(zip(NAMES, counts.tolist())), 'interpretation': config['interpretation'],
        'deployment_model_saved': False}
    manifest_path = out/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    predictions, tuning, folds = [], [], []
    scorer = make_scorer(f1_score, labels=LABELS, average='macro', zero_division=0)
    try:
        for rep, seed in enumerate(config['outer_seeds'], 1):
            outer = StratifiedKFold(config['outer_folds'], shuffle=True, random_state=seed)
            for fold, (train, test) in enumerate(outer.split(df, y), 1):
                assert not set(train) & set(test)
                print(f'Repetition {rep}/5, fold {fold}/3: three-class comparison', flush=True)
                if np.bincount(y[train], minlength=3).min() < config['inner_folds']:
                    raise ValueError('Not enough training students per class for inner splits.')
                inner = list(StratifiedKFold(config['inner_folds'], shuffle=True,
                    random_state=config['inner_seed']+rep*100+fold).split(df.iloc[train], y[train]))
                folds.extend({'repeat': rep, 'fold': fold, 'student_index': int(i+1), 'actual_class': int(y[i])} for i in test)
                jobs = [('baseline', 'majority', [])]+[(name, family, base['input_sets'][name])
                    for name in config['input_sets'] for family in ['logistic', 'forest']]
                for inputs, family, cols in jobs:
                    if family == 'majority':
                        model = DummyClassifier(strategy='most_frequent').fit(np.zeros((len(train), 1)), y[train])
                        Xtest = np.zeros((len(test), 1))
                    else:
                        model, grid = make_model(base, config, cols, family)
                        search = GridSearchCV(model, grid, scoring=scorer, cv=inner,
                            n_jobs=1, error_score='raise', refit=True)
                        search.fit(df[cols].iloc[train], y[train])
                        model = search.best_estimator_
                        tuning.append({'input_set': inputs, 'model': family, 'repeat': rep, 'fold': fold,
                            'parameters': search.best_params_, 'inner_macro_f1': float(search.best_score_)})
                        Xtest = df[cols].iloc[test]
                    pred = model.predict(Xtest)
                    probabilities = model.predict_proba(Xtest)
                    assert np.array_equal(model.classes_, LABELS)
                    assert np.allclose(probabilities.sum(axis=1), 1)
                    for idx, label, probs in zip(test, pred, probabilities):
                        predictions.append({'input_set': inputs, 'model': family, 'repeat': rep, 'fold': fold,
                            'student_index': int(idx+1), 'actual_score': float(df[config['target_score']].iloc[idx]),
                            'actual_class': int(y[idx]), 'predicted_class': int(label),
                            'p_low': float(probs[0]), 'p_middle': float(probs[1]), 'p_high': float(probs[2])})
        result = pd.DataFrame(predictions)
        assert not result.duplicated(['input_set', 'model', 'repeat', 'student_index']).any()
        result.to_csv(out/'held-out-predictions.csv', index=False)
        pd.DataFrame(folds).to_csv(out/'outer-folds.csv', index=False)
        (out/'tuning.json').write_text(json.dumps(tuning, indent=2), encoding='utf-8')
        summarize(result, config, out)
        assert all(training.sha256(ROOT/p) == h for p, h in hashes.items())
        manifest.update(status='complete', source_files_unchanged=True)
    except Exception as exc:
        manifest.update(status='failed', error=str(exc))
        raise
    finally:
        manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Complete: {out}', flush=True)


if __name__ == '__main__':
    main()
