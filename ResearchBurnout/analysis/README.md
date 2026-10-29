# Analysis files

Open [the analysis progress report](../docs/analysis-progress.md) to understand completed work. The experiment workflow is prepared; the full real-data model comparison has not been run.

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

## Run the prediction experiment

Use Python 3.12 from the repository root. The local `.venv` keeps these dependencies separate from other projects.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r analysis/requirements-lock.txt
.\.venv\Scripts\python.exe analysis/scripts/train-models.py --check-only
```

The check reads the current SAV file, validates all four input sets, checks allowed survey codes and missing values, and recalculates both target formulas. It fits no models and leaves source datasets unchanged. It writes `analysis/checks/model-readiness.json`.

Run the software checks separately:

```powershell
.\.venv\Scripts\python.exe analysis/scripts/test-training.py
```

The end-to-end software test uses artificial records only to exercise the code. Its output goes under ignored `tmp/` and is not study evidence.

When ready, run the complete real-data comparison:

```powershell
.\.venv\Scripts\python.exe analysis/scripts/train-models.py
```

Runtime depends on the computer; the script prints progress for each of the 25 outer folds. Both targets and all planned model/input combinations run. No synthetic records are generated for the study.

Each run creates a new folder under `analysis/outputs/model-runs/`. Existing runs and SPSS outputs are not overwritten. Run folders stay out of Git because they include individual scores and predictions.

| Output | What to read |
|---|---|
| `results.md` and `metrics-summary.csv` | Error summary for each target, model family, and input set |
| `repeat-metrics.csv` and `paired-comparisons.csv` | Per-repetition errors and changes; negative MAE differences favor the new set/model |
| `held-out-predictions.csv` and `outer-folds.csv` | Individual predictions and group membership, using SAV row indices rather than timestamps |
| `tuning.json` and PNG plots | Chosen inner settings and predicted-versus-measured plots for repetition 1 |
| `config.json` and `manifest.json` | Exact settings, package versions, source hashes, and completion status |

Only read a run as complete when `manifest.json` says `complete`. Individual predictions repeat across repetitions; calculate errors once per student within each repetition, as the script does.

## Implementation choices

[experiment-config.json](experiment-config.json) fixes the input sets, seeds, tuning grids, and output policy before training. Categories follow questionnaire codes, with the first listed category as reference. Invalid codes stop the run. Valid categories absent from a training fold have no learned effect; they remain an important limitation, especially for rare groups.

All encoded inputs are scaled for ridge using training statistics. Linear and forest inputs are not scaled. Outer splits and inner splits are shared across compared sets. Tuning uses MAE and the same fixed 1 to 5 clipping policy used for outer predictions; raw predictions are also retained.

The comparison reports prespecified model families separately. It does not choose and fit a deployment model or claim unbiased performance for a winner chosen from outer results. A final selection procedure would require selection inside inner validation or separate future evaluation.

There is no established minimum useful MAE gain. Report signed changes, relative changes, and repetition stability without inventing a practical or clinical success threshold. Repetition standard deviations and ranges are not confidence intervals.

The current SAV contains three missing `ai_use_summaries` indicators despite the older saved report. The workflow verifies original multi-choice answers against the raw CSV and reconstructs these three indicators in memory. This is a direct recode, not statistical imputation. It stops if the source hash, missing count, or known indicator values change. The readiness report and run manifest record this step.

The script checks score formulas using the source BAT columns but never uses those columns as model inputs. It fails on any remaining missing model values instead of dropping students or estimating survey answers. Original survey data is read only.

Software API references: [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) and [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).

Next: run the data check above, then run the experiment when ready.
