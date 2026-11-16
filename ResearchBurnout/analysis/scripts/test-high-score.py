"""Software checks for the separate high-score-priority experiment."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

spec = importlib.util.spec_from_file_location('priority', Path(__file__).with_name('train-high-score.py'))
priority = importlib.util.module_from_spec(spec)
spec.loader.exec_module(priority)
BASE = json.loads((priority.ROOT/'analysis/experiment-config.json').read_text())
CONFIG = json.loads((priority.ROOT/'analysis/high-score-config.json').read_text())


class PriorityTests(unittest.TestCase):
    def test_relative_weights_and_normalization(self):
        w = priority.weights([2, 3, 4, 5], 4, 4)
        self.assertAlmostEqual(w.mean(), 1)
        self.assertAlmostEqual(w[2]/w[0], 4)
        np.testing.assert_allclose(priority.weights([2, 3, 4], 1, 4), 1)

    def test_guardrail_prevents_large_overall_loss(self):
        candidates = [
            dict(factor=1, alpha=100, fold_mean_mae=.5, overall_mae=.5, high_mae=1),
            dict(factor=2, alpha=100, fold_mean_mae=.54, overall_mae=.54, high_mae=.8),
            dict(factor=4, alpha=10, fold_mean_mae=.7, overall_mae=.7, high_mae=.3)]
        ordinary, chosen = priority.choose_candidates(candidates, .05)
        self.assertEqual(ordinary['factor'], 1)
        self.assertEqual(chosen['factor'], 2)
        for c in candidates:
            c['high_mae'] = None
        ordinary, chosen = priority.choose_candidates(candidates, .05)
        self.assertEqual(ordinary, chosen)

    def test_inner_search_and_training_only_pipeline(self):
        X = pd.DataFrame({'workload': [1., 2., 3., 4., 5., 2., 3., 4., 5., 1., 3., 4.]})
        y = pd.Series([1.5, 2, 3, 4, 5, 2, 3, 4, 4.5, 2, 3.5, 4.2])
        config = dict(CONFIG, ridge_alphas=[1, 100])
        ordinary, selected, candidates = priority.inner_select(BASE, config, list(X), X, y,
            list(KFold(3, shuffle=True, random_state=17).split(X)))
        self.assertEqual(len(candidates), 6)
        self.assertLessEqual(selected['overall_mae'], ordinary['overall_mae']+.05+1e-12)
        model = priority.fit_ridge(BASE, list(X), X.iloc[:5], y.iloc[:5], 1, 4, 4)
        np.testing.assert_allclose(model.named_steps['scale'].mean_, [3])
        _, prediction = priority.predict(model, pd.DataFrame({'workload': [1000]}))
        self.assertTrue(1 <= prediction[0] <= 5)
        np.testing.assert_allclose(model.named_steps['scale'].mean_, [3])

    def test_high_metrics_and_false_alarms(self):
        frame = pd.DataFrame({'actual': [5., 4., 2., 3.], 'prediction': [4.5, 3.5, 4.2, 3.]})
        m = priority.group_metrics(frame, 4)
        self.assertAlmostEqual(m['high_mae'], .5)
        self.assertAlmostEqual(m['high_mean_underestimation'], .5)
        self.assertAlmostEqual(m['high_recall'], .5)
        self.assertAlmostEqual(m['high_precision'], .5)
        self.assertEqual(m['false_positive_count'], 1)
        self.assertAlmostEqual(m['false_positive_rate'], .5)


if __name__ == '__main__':
    unittest.main()
