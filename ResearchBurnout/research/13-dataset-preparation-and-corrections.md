# Research data

Use [03-prepared-student-burnout-data.sav](../data/03-prepared-student-burnout-data.sav) for the next analysis. It contains 97 students and 66 variables, including both burnout scores and the numeric question codes.

## Which files belong here?

| File | Purpose |
|---|---|
| [03-prepared-student-burnout-data.sav](../data/03-prepared-student-burnout-data.sav) | Corrected working dataset |
| [02-original-student-survey-workbook.xlsx](../data/02-original-student-survey-workbook.xlsx) | Collected response workbook; preserve the original |
| [01-original-student-survey.csv](../data/01-original-student-survey.csv) | CSV export used to verify SPSS answers; preserve the original |

All data files now share the flat `data/` folder. Keep the original exports unchanged. The SPSS rebuild writes `04-experimental-predictor-rebuild.sav`, separate from the corrected working dataset.

Older SPSS checkpoints have prefixes `90-` and `91-` in [data/](../data/). Previous-survey responses have prefix `92-`; read [their history](97-previous-survey-data-guide.md). They are not responses to the active survey.

## Current model-readiness check

The new training workflow found three missing `ai_use_summaries` indicators in the SAV, despite the older report below. It verifies original Q9 answers against the raw CSV and reconstructs the missing indicators in memory. Two are Selected and one is Not selected. The SAV file is unchanged.

[model-readiness.json](../results/00-model-readiness-check.json) records this check. See [the analysis guide](08-score-prediction-experiments-and-methods.md#implementation-choices) for the exact handling. Both burnout scores passed recalculation checks.

## Checks and corrections

The saved [data-check report](../results/00-data-consistency-checks.json) records no score errors, category-indicator errors, missing numeric values, or numeric differences from the CSV. The [variable metadata](../results/00-spss-variable-dictionary.json) records labels, types, and display settings.

Two cells were corrected after the earlier SPSS checkpoint. Read [the correction details](06-data-analysis-and-experiment-history.md#7-corrections-and-final-verification) before rebuilding data.

The [analysis guide](08-score-prediction-experiments-and-methods.md) explains script requirements. Saved reports describe the dataset when checked; verify any changed dataset again.

Next: read [the model inputs](04-original-prediction-experiment-plan.md#2-compare-two-sets-of-inputs).
