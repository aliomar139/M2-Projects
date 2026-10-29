"""Checks for leakage prevention, fixed bounds, and reproducible evaluation outputs."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import GridSearchCV, KFold

SCRIPT = Path(__file__).with_name('train-models.py')
spec = importlib.util.spec_from_file_location('training', SCRIPT)
training = importlib.util.module_from_spec(spec)
spec.loader.exec_module(training)
CONFIG = json.loads((SCRIPT.parents[1] / 'experiment-config.json').read_text())


class WorkflowTests(unittest.TestCase):
    def test_real_data_reconstruction_preserves_source(self):
        path = training.ROOT / CONFIG['dataset']
        original_hash = training.sha256(path)
        df = training.load_data(CONFIG)
        self.assertEqual(df.attrs['readiness']['reconstructed_count'], 3)
        self.assertEqual(int(df.ai_use_summaries.isna().sum()), 0)
        self.assertEqual(training.sha256(path), original_hash)

    def test_rejects_outcome_inputs(self):
        for forbidden in ['BAT21', 'burnout_score', 'Timestamp', 'leave_intention']:
            c = copy.deepcopy(CONFIG)
            c['input_sets']['small_a'].append(forbidden)
            with self.assertRaises(ValueError):
                training.validate_config(c)

    def test_bounds_apply_to_inner_scoring(self):
        X = pd.DataFrame({'x': [0, 1, 2, 3]})
        model = training.BoundedRegressor(DummyRegressor(strategy='constant', constant=8))
        grid = GridSearchCV(model, {}, cv=2, scoring='neg_mean_absolute_error')
        grid.fit(X, np.full(4, 4.0))
        self.assertAlmostEqual(grid.best_score_, -1.0)
        np.testing.assert_equal(grid.predict(X), 5)
        np.testing.assert_equal(grid.best_estimator_.predict_raw(X), 8)

    def test_scaler_uses_training_students_only(self):
        c = copy.deepcopy(CONFIG)
        X = pd.DataFrame({'workload': [1., 2., 3., 4.]})
        model, _ = training.make_model(c, ['workload'], 'ridge')
        model.fit(X.iloc[:3], np.array([2., 3., 4.]))
        scaler = model.estimator_.named_steps['scale']
        np.testing.assert_allclose(scaler.mean_, [2.])
        model.predict(pd.DataFrame({'workload': [1000.]}))
        np.testing.assert_allclose(scaler.mean_, [2.])

    def test_all_models_and_report_with_artificial_fixture(self):
        # These records exercise software only; they are never study participants.
        rng = np.random.default_rng(817)
        c = copy.deepcopy(CONFIG)
        c['expected_rows'] = 20
        c['cv'].update(outer_folds=2, outer_seeds=[17], inner_folds=2)
        c['ridge_alphas'] = [1, 10]
        c['forest'].update(n_estimators=3, max_depth=[2], min_samples_leaf=[2])
        df = pd.DataFrame()
        for col in sorted(set(sum(c['input_sets'].values(), []))):
            levels = c['category_levels'].get(col)
            if levels is None:
                levels = [0, 1] if col == 'enrolled_lebanon' or col.startswith('ai_use_') else [1, 2, 3, 4, 5]
            df[col] = rng.choice(levels, 20)
        for target in c['targets']:
            df[target] = np.clip(2 + .2 * df.workload + rng.normal(0, .2, 20), 1, 5)
        base = training.ROOT / 'tmp'
        base.mkdir(exist_ok=True)
        # TemporaryDirectory is avoided because this Windows sandbox restricts its ACLs.
        folder = base / ('workflow-test-' + __import__('uuid').uuid4().hex)
        training.run(c, df, SCRIPT.parents[1] / 'experiment-config.json', folder)
        manifest = json.loads((folder / 'manifest.json').read_text())
        self.assertEqual(manifest['status'], 'complete')
        predictions = pd.read_csv(folder / 'held-out-predictions.csv')
        self.assertEqual(len(predictions), 20 * 2 * 10)
        self.assertTrue(predictions.prediction.between(1, 5).all())
        pairs = pd.read_csv(folder / 'paired-comparisons.csv')
        self.assertEqual(len(pairs), 2 * (6 + 8 * 2))
        folds = pd.read_csv(folder / 'outer-folds.csv')
        self.assertEqual(folds.student_index.nunique(), 20)
        self.assertTrue((folder / 'results.md').is_file())


if __name__ == '__main__':
    unittest.main()
