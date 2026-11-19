"""Small software checks; artificial records here are not study data."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import uuid

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, KFold

spec = importlib.util.spec_from_file_location('followup', Path(__file__).with_name('02-compare-xgboost-score-prediction.py'))
followup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(followup)
CONFIG = json.loads((followup.ROOT/'experiments/02-compare-xgboost-score-prediction-settings.json').read_text())


class XGBoostTests(unittest.TestCase):
    def test_matches_reference_experiment(self):
        reference = json.loads((followup.ROOT/'experiments/01-compare-score-prediction-baselines-settings.json').read_text())
        manifest = {'status': 'complete', 'dataset_sha256': CONFIG['dataset_sha256']}
        def fixture(path):
            self.assertIn(path.name, ['manifest.json', 'config.json'])
            return json.dumps(manifest if path.name == 'manifest.json' else reference)
        # This software check must not require an unavailable historical study run.
        with patch.object(Path, 'read_text', autospec=True, side_effect=fixture):
            followup.validate_followup(CONFIG)
            c = json.loads(json.dumps(CONFIG))
            c['cv']['outer_seeds'][0] += 1
            with self.assertRaises(ValueError):
                followup.validate_followup(c)

    def test_pipeline_inner_search_and_bounds(self):
        rng = np.random.default_rng(81)
        X = pd.DataFrame({'workload': rng.integers(1, 6, 24),
                          'sleep_duration_code': rng.integers(1, 4, 24)})
        y = 2 + .25*X.workload.to_numpy()+rng.normal(0, .2, 24)
        model, grid = followup.training.make_model(CONFIG, list(X), 'xgboost')
        self.assertEqual(len(grid['estimator__model__max_depth']), 2)
        search = GridSearchCV(model, grid, scoring='neg_mean_absolute_error',
            cv=KFold(2, shuffle=True, random_state=1), error_score='raise')
        search.fit(X.iloc[:18], y[:18])
        predicted = search.predict(X.iloc[18:])
        self.assertTrue(np.isfinite(predicted).all())
        self.assertTrue(((predicted >= 1) & (predicted <= 5)).all())
        encoded = search.best_estimator_.estimator_.named_steps['encode']
        self.assertEqual(encoded.transform(X).shape[1], 4)

    def test_complete_reporting_with_artificial_fixture(self):
        c = json.loads(json.dumps(CONFIG))
        c['expected_rows'] = 20
        c['cv'].update(outer_folds=2, outer_seeds=[17], inner_folds=2)
        c['xgboost']['grid'] = {'max_depth': [1], 'n_estimators': [3]}
        rng = np.random.default_rng(61)
        columns = set(sum(c['input_sets'].values(), []))
        df = pd.DataFrame({col: rng.choice(c['category_levels'].get(col,
            [0, 1] if col == 'enrolled_lebanon' or col.startswith('ai_use_') else [1, 2, 3, 4, 5]), 20)
            for col in sorted(columns)})
        for target in c['targets']:
            df[target] = 2+.2*df.workload
        out = followup.ROOT/'results/99-software-test-runs'/('xgboost-test-'+uuid.uuid4().hex)
        followup.training.run(c, df, followup.ROOT/'experiments/02-compare-xgboost-score-prediction-settings.json', out)
        manifest = json.loads((out/'manifest.json').read_text())
        self.assertEqual(manifest['status'], 'complete')
        self.assertIn('xgboost', manifest['packages'])
        pairs = pd.read_csv(out/'paired-comparisons.csv')
        self.assertEqual(len(pairs), 10)
        self.assertTrue((out/'results.md').exists())


if __name__ == '__main__':
    unittest.main()
