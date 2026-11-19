"""Small checks for the new validation calculations and student-level splits."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score

spec = importlib.util.spec_from_file_location('validation', Path(__file__).with_name('25-validate-random-forest-against-baselines-and-chance.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ValidationTests(unittest.TestCase):
    def test_random_comparator_matches_enumerated_warning_sets(self):
        from itertools import combinations
        y = np.array([1, 0, 0, 1, 0])
        masks = []
        for pair in combinations(range(5), 2):
            p = np.zeros(5, dtype=int)
            p[list(pair)] = 1
            masks.append(v.binary.metrics(y, p))
        got = v.random_expected(y, np.ones(5), [1, 1, 0, 0, 0])
        for key in ['tp', 'fp', 'fn', 'tn', 'recall', 'precision', 'balanced_accuracy', 'f2']:
            self.assertAlmostEqual(got[key], np.mean([m[key] for m in masks]))

    def test_permutation_has_one_label_per_student_across_repetitions(self):
        y = np.r_[np.zeros(80, dtype=int), np.ones(17, dtype=int)]
        p = v.labels_for(y, 1, 20261118)
        np.testing.assert_array_equal(np.bincount(p), [80, 17])
        self.assertFalse(np.array_equal(y, p))
        np.testing.assert_array_equal(p, v.labels_for(y, 1, 20261118))
        np.testing.assert_array_equal(y, v.labels_for(y, 0, 20261118))
        self.assertFalse(np.array_equal(p, v.labels_for(y, 2, 20261118)))
        base = v.read(v.ROOT/'experiments/01-compare-score-prediction-baselines-settings.json')
        search = v.read(v.ROOT/'experiments/10-compare-high-burnout-classifiers-settings.json')
        seen = {}
        for rep, fold, tr, te in v.outer_splits(p, base, search):
            self.assertFalse(set(tr) & set(te))
            self.assertGreaterEqual(int(p[te].sum()), 3)
            seen.setdefault(rep, []).extend(te.tolist())
        for ids in seen.values():
            self.assertEqual(sorted(ids), list(range(97)))

    def test_pvalue_finite_correction_includes_ties(self):
        self.assertEqual(v.permutation_pvalue(.8, [.5, .6, .8]), .5)
        self.assertEqual(v.permutation_pvalue(.8, [.5, .6, .7]), .25)

    def test_metrics_match_sklearn_and_warning_extremes(self):
        y = np.r_[np.ones(17), np.zeros(80)]
        for p in [np.ones(97), np.zeros(97), np.r_[np.ones(15), np.zeros(2), np.ones(28), np.zeros(52)]]:
            self.assertAlmostEqual(v.binary.metrics(y, p)['balanced_accuracy'], balanced_accuracy_score(y, p))
        self.assertEqual(v.binary.metrics(y, np.ones(97))['recall'], 1)
        self.assertEqual(v.binary.metrics(y, np.ones(97))['balanced_accuracy'], .5)

    def test_paired_student_intervals_preserve_identical_models(self):
        spec = importlib.util.spec_from_file_location('report', Path(__file__).with_name('25-report-and-verify-random-forest-validation.py'))
        report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(report)
        y = np.r_[np.ones(17, dtype=int), np.zeros(80, dtype=int)]
        records = [{'method': method, 'repeat': rep, 'student_index': i+1,
                    'actual_class': int(value),
                    'predicted_class': int(1-value if i in [0, 1, *range(17, 37), 38+rep] else value)}
                   for method in ['selected_rf', 'real_only_rf', 'workload_logistic']
                   for rep in range(1, 6) for i, value in enumerate(y)]
        intervals = report.conditional_intervals(pd.DataFrame(records), {'bootstrap_seed': 5, 'bootstrap_samples': 20})
        absolute = intervals[~intervals.comparison.str.contains('minus')]
        paired = intervals[intervals.comparison.str.contains('minus')]
        self.assertTrue((absolute.lower < absolute.upper).all())
        np.testing.assert_array_equal(paired[['lower', 'upper']], 0)


if __name__ == '__main__':
    unittest.main()
