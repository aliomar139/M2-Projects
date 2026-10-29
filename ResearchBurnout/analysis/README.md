# Analysis files

Open [the analysis progress report](../docs/analysis-progress.md) to understand completed work. No prediction model has been trained yet.

## Where to find things

| Folder | Contents |
|---|---|
| `scripts/` | Preparation syntax and data checker |
| `checks/` | Saved checks of values, scores, and variable settings |
| `outputs/` | SPSS tables and charts in `descriptive-statistics.spv` |

## Preparation script

[prepare-predictors.sps](scripts/prepare-predictors.sps) uses the earlier checkpoint in `archive/data/burnout-before-corrections.sav`. It creates numeric copies of question answers.

The script now writes `data/prepared/burnout-data-rebuilt.sav`, a separate output. It does not overwrite the corrected working dataset. A rebuild still needs the two corrections documented in [the progress report](../docs/analysis-progress.md#7-corrections-and-final-verification).

Before running it in SPSS, update its `CD` line to your repository folder. Its other file paths are relative to that folder.

## Data checker

[check-data.py](scripts/check-data.py) compares the current working data with the older checkpoint and the CSV export. It checks score calculations, category mappings, missing values, and metadata. It reads datasets without changing them and rewrites the two reports in `checks/`.

File paths now follow the new structure, and text-file handling supports Python 3. The checker still requires Windows and the IBM SPSS 23 I/O library at `C:/Program Files/IBM/SPSS/Statistics/23`. It is not a general-purpose Python-only checker.

The repository cleanup checked Python syntax and file paths. It did not rerun the SPSS data checks or regenerate results.

Next: review [the first model experiment](../docs/prediction-experiment.md).
