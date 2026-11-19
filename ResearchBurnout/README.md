# Student burnout, study conditions and GenAI

Updated **19 November 2026**. This page explains the goal, completed work, main findings and file layout.

## Read these first

| What you want | File |
|---|---|
| Understand the latest findings | [Random Forest validation report](results/25-random-forest-validation-report.md) |
| See the completed analyses and experiments | [Full analysis history](research/06-data-analysis-and-experiment-history.md) |
| Continue work after a break | [Current project handoff](research/09-current-project-handoff.md) |
| Read the survey questions | [Student questionnaire](research/02-student-survey-questionnaire.md) |
| Find a renamed file | [Complete old-to-new file catalog](research/12-file-renaming-catalog.csv) |

## What is the goal?

We study whether university students' **GenAI habits help estimate current burnout symptoms**, beyond what their study conditions tell us.

The dataset contains **97 real students**. The questionnaire has 43 questions: 20 about background, study conditions and AI use, followed by 23 Burnout Assessment Tool for Students (BAT-S) items. All respondents are retained, including 10 whom the researcher identified as Lebanese students studying abroad.

Everyone answered at one point in time. The study can examine associations and estimate current symptoms; it cannot show that AI causes burnout or predict who will develop burnout later.

| Modelling task | Output | How we judge it |
|---|---|---|
| Score prediction, or regression | A burnout score on a 1–5 scale | Average size of errors; lower is better |
| High-symptom classification | A High / Below-high warning | High students caught and false warnings produced |

These tasks have different metrics. A classifier's recall cannot be compared directly with a score predictor's average error.

## What did we do?

1. **Prepared and checked the data.** We recoded answers, created both burnout scores and documented corrections. The working SAV has 97 rows and 66 variables. The Python loader reconstructs three missing AI-use indicators from their original answers in memory; it leaves the SAV unchanged.
2. **Completed SPSS analyses.** Reliability checks, descriptive statistics and exploratory correlations are recorded in the analysis history. Total-item Cronbach's alpha was .900 for the 12 selected BAT items and .944 for all 23 items. These measure consistency, not prediction accuracy or clinical validity.
3. **Compared numerical-score predictors.** Baselines, linear/Ridge regression, forests, XGBoost, high-score weighting, synthetic training examples, SVR/kernel methods, input selection and blends were tested. Predictions often underestimated the highest measured scores.
4. **Compared symptom-warning models.** We tested three-group classification, binary classifiers, augmentation, tuning, voting, question selection, SVC, TabPFN and Boruta. Some alternatives reduced false warnings while losing detections; others improved ranking without improving the chosen warning rule.
5. **Checked the selected RF against simple alternatives and chance.** We reproduced its real-student results, added a workload-only baseline, ran 199 complete shuffled-label evaluations, described uncertainty and independently checked the outputs.

The [analysis history](research/06-data-analysis-and-experiment-history.md) preserves unsuccessful experiments and earlier decisions. Some older code/outputs were deliberately deleted before this cleanup. Their findings remain historical records, not currently runnable experiments.

## What are the latest results?

### High-symptom warnings

The primary burnout score uses 12 selected BAT items. **High means measured score ≥4:** 17 students. The other 80 belong to Below-high. These are study-defined groups, not clinical diagnoses; Below-high does not mean symptom-free.

| Approach | High caught /17 | False warnings /80 | Recall | Precision |
|---|---:|---:|---:|---:|
| Selected eight-input Random Forest | 14.8 | 28 | 87.1% | 34.7% |
| Workload-only logistic baseline | 16.0 | 28 | 94.1% | 36.4% |
| Random warnings, approximately the RF's warning count | 7.6 | 35.2 | 44.6% | 17.7% |
| Warn everyone | 17.0 | 80 | 100.0% | 17.5% |

Counts average five repetitions of the same students, not additional people. **Recall** is the share of High students caught; **precision** is the share of warnings that are correct. Roughly two thirds of the RF's warnings are false relative to this study boundary.

RF exceeded all **199 shuffled-label evaluations**, with corrected **p=.005**. This supports association for this fixed procedure in this dataset. It does not account for every earlier model choice or establish performance on new students.

Workload alone had better warning results, so RF showed **no demonstrated warning advantage over that simple baseline**. Paired conditional uncertainty intervals include zero; this does not prove workload will always be superior. RF average precision was higher (.527 versus .423), so workload did not improve every ranking measure.

RF uses workload, sleep category, study-hours category, financial strain, university support, AI frequency, AI dependence and AI offloading. BAT items and BAT-derived scores never enter as predictors.

### Numerical score prediction

The recorded research choice remains a fixed 50/50 blend of weighted Ridge and high-priority SVR. Mean absolute error was **.616 points overall** and **.642 among High-score students**. This choice balances overall and high-score errors; it is not the winner under every objective. No final trained blend was exported, and its historical output folder is missing here.

### What does 93.5% synthetic recall mean?

That was a separate check on **970 artificial profiles**, derived from real students used to fit the saved model. Their labels were inherited assumptions. It is not a test on 970 new measured students and does not replace the **87.1% real-student cross-validation recall**.

The documented final RF fit used **97 real students and zero synthetic training rows**, because training selection chose no augmentation. Its recorded recipe is 100 trees, depth 3, minimum leaf size 10, relative High weight 2, seed 271828 and warning threshold .35. The original model and metadata remain missing here. The local recipe record is not a trained model.

## How are the files structured?

There are **four main project folders**, flat where practical:

```text
ResearchBurnout/
  README.md       Project explanation and starting points
  research/       Design, questionnaire, methods, history and literature
  data/           Original exports, prepared SAV and marked older data
  experiments/    Numbered scripts, settings, tests and dependencies
  results/        Named findings, figures and local evidence archives
```

`.venv/` and `.vscode/` are local software/editor folders. Their internal names stay unchanged so they keep working. Python may create ignored cache folders or local test/run directories.

### Research and data

Research files **01–15** cover the current study and its records; **90–97** hold older planning and previous-survey material. The work history preserves past decisions rather than instructing you to rerun completed work.

| Data file | Role |
|---|---|
| [01-original-student-survey.csv](data/01-original-student-survey.csv) | Original CSV used to verify imported answers |
| `02-original-student-survey-workbook.xlsx` | Local original workbook, ignored by Git |
| [03-prepared-student-burnout-data.sav](data/03-prepared-student-burnout-data.sav) | Corrected working dataset |
| `90-...`, `91-...`, `92-...` | Older checkpoints or previous-survey responses; do not mix with current respondents |

The secondary burnout score uses all 23 BAT items, giving the four dimensions equal weight. It is not a simple mean of 23 items. Read [dataset preparation and corrections](research/13-dataset-preparation-and-corrections.md) before rebuilding. The SPSS preparation script writes a separate rebuild and still needs the documented corrections.

### Numbered experiments

Numbers identify an experiment family in a useful reading order, **not an exact chronology**. A script and its `-settings.json` share the same number/title. Tests begin with `test_` and the relevant experiment number.

| Numbers | Experiments |
|---|---|
| **00–04** | Data/SPSS preparation; score baselines; XGBoost; error diagnosis; high-score weighting |
| **05–08** | Score augmentation; SVR/kernel regression; Ridge/SVR blending; score-input selection |
| **09–14** | Three-group classification; binary classifiers; augmentation; forest tuning; voting; false-warning diagnosis |
| **15–22** | Question selection/removal; TabPFN/refinement; eight/23-input SVC; input comparisons; Boruta |
| **23–25** | Save selected RF; synthetic-profile check; real-student baseline/chance validation and reporting |

For example, `11-augment-high-burnout-classifiers.py` and `11-augment-high-burnout-classifiers-settings.json` belong together. Experiment **25** has separate execution, reporting/verification and software-test files with explanatory titles.

Read the [classification methods](research/07-classification-experiments-and-methods.md) or [regression methods](research/08-score-prediction-experiments-and-methods.md) before running older experiments. Many need historical local run folders that are absent; renaming does not recreate them. Experiment 25 can start from the supplied source data/configurations without those historical folders.

### Results and preserved evidence

Files starting **00-** contain SPSS/data checks. Files starting **25-** contain the latest validation findings and tables. Begin with:

| File | What it explains |
|---|---|
| [25-random-forest-validation-report.md](results/25-random-forest-validation-report.md) | Methods, comparisons, uncertainty and conclusions |
| [25-model-comparison-summary.csv](results/25-model-comparison-summary.csv) | Recall, precision, errors and ranking metrics |
| [25-real-model-versus-shuffled-labels.png](results/25-real-model-versus-shuffled-labels.png) | RF versus the 199 shuffled-label evaluations |
| [25-detections-versus-false-warnings.png](results/25-detections-versus-false-warnings.png) | The cost of catching more High students |
| [25-random-forest-confusion-matrix.png](results/25-random-forest-confusion-matrix.png) | Correct decisions, misses and false warnings |

The local archive `results/99-original-workspace-and-verified-validation.zip` preserves the **original files and validation namespace**: all 5,000 fold records, original source/configuration files, data, manifests and hashes, plus previous working notes/test artifacts. Internal archive names remain unchanged because the original verification records refer to those exact paths and bytes.

Readable copies have clear names in `results/`. Paths in the readable report now match the new layout; this is not a new scientific evaluation. For exact original hash checks, use the originals inside the archive. Extract to a separate folder, not over this project. The [file catalog](research/12-file-renaming-catalog.csv) records the moves; the local reorganization record preserves original fingerprints.

Private student predictions/frequencies, trained artifacts, full run folders and the archive stay ignored by Git. A new clone will not automatically contain them. Back up local evidence separately when moving machines; do not force-add participant-level records to repair documentation links.

## How do I run checks?

From the project root in PowerShell, use the existing `.venv` when available:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s experiments -p "test_*.py"
```

This runs 25 checks across six numbered suites: data reconstruction, artificial fixtures, pipelines, validation math, local links and preserved evidence. It does not repeat the full 199-permutation computation. Individual suites can also run directly, for example `experiments/test_25_random_forest_validation.py`.

For a fresh environment, `experiments/dependencies-pinned.txt` records main versions; `dependencies-xgboost.txt` includes that list and pinned XGBoost. Boruta has an additional dependency file. TabPFN used a separate environment/list and checkpoint; its heavy dependencies are unnecessary for core checks. SPSS utilities need the local SPSS installation and were not rerun during this cleanup.

Full experiment-25 execution creates a new timestamped folder under `results/25-random-forest-validation/`. Run its script with `--stage real`, then `--stage permutations --out <new-run-folder>`. Pass the same folder to its report/verification script. The previous computation took **about 6.7 hours** with four single-threaded workers.

## What remains open?

The paper and presentation still need their final form. Report the workload-only comparison and unsuccessful searches, without claiming eight inputs are necessary or AI adds a proven warning benefit.

There is no untouched real validation cohort, calibrated clinical probability or validated intervention. The sample remains 97 people, including only 17 High students. A demo would require separate recovery or an explicitly recorded fit of the missing trained model. Read the [current handoff](research/09-current-project-handoff.md) before further work.
