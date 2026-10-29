# Research data

Use [prepared/burnout-data.sav](prepared/burnout-data.sav) for the next analysis. It contains 97 students and 66 variables, including both burnout scores and the numeric question codes.

## Which files belong here?

| File | Purpose |
|---|---|
| [prepared/burnout-data.sav](prepared/burnout-data.sav) | Corrected working dataset |
| [raw/survey-responses.xlsx](raw/survey-responses.xlsx) | Collected response workbook; preserve the original |
| [raw/survey-export-spss.csv](raw/survey-export-spss.csv) | CSV export used to verify SPSS answers; preserve the original |

Keep raw exports unchanged. Put derived datasets in `prepared/` and give any experimental rebuild a separate name.

Older SPSS checkpoints live in [archive/data/](../archive/data/). Responses to the previous questionnaire live in [archive/previous-survey/data/](../archive/previous-survey/data/README.md). They are not responses to the active survey.

## Checks and corrections

The saved [data-check report](../analysis/checks/data-checks.json) records no score errors, category-indicator errors, missing numeric values, or numeric differences from the CSV. The [variable metadata](../analysis/checks/variable-metadata.json) records labels, types, and display settings.

Two cells were corrected after the earlier SPSS checkpoint. Read [the correction details](../docs/analysis-progress.md#7-corrections-and-final-verification) before rebuilding data.

The [analysis guide](../analysis/README.md) explains script requirements. Saved reports describe the dataset when checked; verify any changed dataset again.

Next: read [the model inputs](../docs/prediction-experiment.md#2-compare-two-sets-of-inputs).
