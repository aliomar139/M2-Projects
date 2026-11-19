"""Software-only tests; no study models trained by these fixtures."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold

spec = importlib.util.spec_from_file_location('classification_train', Path(__file__).with_name('09-classify-low-middle-high-burnout.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
CONFIG = json.loads((module.ROOT/'experiments/09-classify-low-middle-high-burnout-settings.json').read_text())
BASE = json.loads((module.ROOT/CONFIG['reference_config']).read_text())


class ClassificationTests(unittest.TestCase):
    def test_boundaries_and_invalid_scores(self):
        np.testing.assert_equal(module.make_labels([1, 1.999, 2, 3.999, 4, 5]), [0, 0, 1, 1, 2, 2])
        for values in [[np.nan], [0], [5.1]]:
            with self.assertRaises(ValueError):
                module.make_labels(values)

    def test_majority_metrics_do_not_hide_missed_classes(self):
        y = np.repeat([0, 1, 2], [6, 74, 17])
        m = module.calculate_metrics(y, np.ones(97))
        self.assertAlmostEqual(m['accuracy'], 74/97)
        self.assertAlmostEqual(m['balanced_accuracy'], 1/3)
        self.assertEqual(m['high_recall'], 0)
        self.assertEqual(m['low_recall'], 0)

    def test_stratification_supports_both_inner_classes(self):
        y = np.repeat([0, 1, 2], [6, 74, 17])
        for train, test in StratifiedKFold(3, shuffle=True, random_state=17).split(np.zeros(97), y):
            self.assertFalse(set(train) & set(test))
            self.assertEqual((y[test] == 0).sum(), 2)
            for inner_train, inner_test in StratifiedKFold(2).split(np.zeros(len(train)), y[train]):
                self.assertTrue((np.bincount(y[train][inner_train], minlength=3) > 0).all())
                self.assertTrue((np.bincount(y[train][inner_test], minlength=3) > 0).all())

    def test_models_and_training_only_scaling(self):
        rng = np.random.default_rng(41)
        cols = BASE['input_sets']['small_b']
        X = pd.DataFrame({col: rng.choice(BASE['category_levels'].get(col, [1, 2, 3, 4, 5]), 30) for col in cols})
        y = np.tile([0, 1, 2], 10)
        for family in ['logistic', 'forest']:
            model, _ = module.make_model(BASE, CONFIG, cols, family)
            if family == 'forest':
                model.set_params(model__n_estimators=3, model__max_depth=2)
            model.fit(X.iloc[:24], y[:24])
            pred = model.predict(X.iloc[24:])
            self.assertTrue(np.isin(pred, [0, 1, 2]).all())
            self.assertTrue(np.allclose(model.predict_proba(X.iloc[24:]).sum(axis=1), 1))
            if family == 'logistic':
                expected = model.named_steps['encode'].transform(X.iloc[:24]).mean(axis=0)
                np.testing.assert_allclose(model.named_steps['scale'].mean_, expected)


if __name__ == '__main__':
    unittest.main()
