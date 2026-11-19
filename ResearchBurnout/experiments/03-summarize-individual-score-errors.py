"""Summarize existing held-out predictions; fit no models."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'results/01-score-prediction-baselines/20261102T083420352990Z'


def summarize(df):
    selected = df[
        (df['target'] == 'burnout_score')
        & (df['input_set'] == 'small_b')
        & (df['model'] == 'ridge')
    ].copy()
    if selected.duplicated(['student_index', 'repeat']).any():
        raise ValueError('Duplicate student/repetition predictions.')
    if selected['student_index'].nunique() != 97:
        raise ValueError('Expected 97 students.')
    for _, group in selected.groupby('student_index'):
        if set(group['repeat']) != {1, 2, 3, 4, 5} or group['actual'].nunique() != 1:
            raise ValueError('Expected five repetitions and a consistent measured score.')
    if selected[['actual', 'prediction', 'absolute_error']].isna().any().any():
        raise ValueError('Missing prediction or score.')
    calculated = (selected['prediction'] - selected['actual']).abs()
    if not ((calculated-selected['absolute_error']).abs() < 1e-10).all():
        raise ValueError('Saved absolute errors do not match predictions.')
    selected['signed_error'] = selected['prediction'] - selected['actual']
    summary = selected.groupby('student_index').agg(
        actual_score=('actual', 'first'),
        average_prediction=('prediction', 'mean'),
        average_absolute_error=('absolute_error', 'mean'),
        average_signed_error=('signed_error', 'mean'),
        smallest_prediction=('prediction', 'min'),
        largest_prediction=('prediction', 'max'),
    ).reset_index()
    return summary.sort_values(['average_absolute_error', 'student_index'], ascending=[False, True])


def main():
    import json
    if json.loads((RUN/'manifest.json').read_text())['status'] != 'complete':
        raise ValueError('Source experiment is not complete.')
    result = summarize(pd.read_csv(RUN/'held-out-predictions.csv'))
    output = RUN/'student-errors-small-b-ridge.csv'
    result.to_csv(output, index=False)
    print(result.head(10).round(3).to_string(index=False))
    print(f'\nStudents with average absolute error above 1 point: '
          f'{(result.average_absolute_error > 1).sum()}/97')
    print(f'Saved: {output}')


if __name__ == '__main__':
    main()
