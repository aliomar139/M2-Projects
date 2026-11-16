# Analysis files

## Boruta input selection (16 November 2026)

Separate [results](../classification/boruta-outputs/20261116T082517133758Z/results.md). **Keep current RF (87.1% recall/34.7% precision, F2 .667848).** Boruta from all 23 inputs retains 2–5 variables per outer fit but gives F2-tuned 72.9%/36.1%, .604040, 22.2 false warnings, or recall-guarded 82.4%/32.6%, .630103, 29.0 warnings. Original nested folds, real-only training selection, complete variable groups, independent original forest/weight/augmentation/threshold tuning; copied reference predictions. Initial 125 selector fits/5,894 selector iterations plus 3,600 inner/40 outer prediction fits. Only Boruta 0.4.3 added; previous versions/data/results preserved. See [method and verification](../classification/README.md#boruta-selection-from-all-23-inputs-16-november-2026). No independent cohort or deployment model.

## RF input-combination comparison (16 November 2026)

Separate [results](../classification/input-comparison-outputs/20261116T075921907598Z/results.md). **Keep selected RF: 87.1% recall, 34.7% precision, F2 .667848, 28.0 false warnings.** The alternative eight inputs with stress/avoidance give 72.9%/37.3% under F2 tuning or 81.2%/32.5% under a recall guard. Eight selected from 23 give 72.9%/37.9% or 83.5%/33.5%, respectively. All new F2 scores are lower; guarded approaches also add false warnings. Same original nested folds, training-only grouped variable ranking/generation/preprocessing and independently retuned original forest/weight/augmentation/threshold grids. Initial 7,300 inner/104 outer fits; current RF scores reproduced. Saved outputs and [verification record](../classification/input-comparison-outputs/20261116T075921907598Z/verification.json) preserve the comparison. No earlier results/source changes or deployment model. See [classification instructions](../classification/README.md#alternative-input-combinations-16-november-2026).

## 23-input SVC comparison (16 November 2026)

Completed separate [23-input SVC results](../classification/svc23-outputs/20261116T072730431772Z/results.md). Recall-guard SVC improves versus its eight-input counterpart: recall 80.0% to 83.5%, precision 33.4% to 35.4%, F2 .624572 to .655506, false warnings 27.2 to 26.2. Its F2-focused alternative gives 76.5% recall / 40.4% precision, F2 .646090 and 19.4 warnings. **Keep RF for High detection:** 87.1%/34.7%, F2 .667848, 28.0 warnings. Same 36-setting search space and original nested folds, independently tuned on 23 existing variables (37 encoded columns), real-only training. Initial 3,600 inner/35 outer fits; independent checks of all 2,425 predictions, 900 settings, 62,758 threshold candidates, 50 choices and hashes passed, including 140 selected inner/35 outer independent refits. Previous SVC/RF results and source data remain unchanged. See [classification instructions](../classification/README.md).

## RBF SVC classification comparison (16 November 2026)

Completed separate [SVC results](../classification/svc-outputs/20261116T070622236133Z/results.md). **Keep the selected RF.** SVC's inner-F2 procedure reaches 78.8% recall / 36.2% precision, F2 .637154, 23.6 false warnings; its recall guard reaches 80.0% / 33.4%, .624572, 27.2 warnings. Selected RF remains 87.1% / 34.7%, .667848, 28.0 warnings. Same eight inputs and original 5x5 outer / four inner folds; real-only SVC, 36 C/gamma/High-weight combinations and exact inner margin threshold tuning. Initial run: 3,600 inner and 37 outer fits. Verification passed for 1,455 predictions, 900 candidate score sets, 71,604 threshold candidates, 50 decisions, original folds/controls and all metrics/hashes; independently refitted 148 selected inner and 37 outer models and reproduced scores. No added inputs/data, package changes, deployment fit or replacement of the RF. See [classification instructions](../classification/README.md).

## TabPFN threshold refinement and RF mixture (14 November 2026)

Completed separate [exact-threshold](../classification/tabpfn-threshold-outputs/20261114T125820967153Z/results.md) and [RF–TabPFN mixture](../classification/tabpfn-voting-outputs/20261114T125820967153Z/results.md) comparisons using verified saved inner/outer endpoint scores; no endpoint refits. **Keep the selected RF:** 87.1% recall / 34.7% precision, F2 .667848, 28.0 false warnings. Exact TabPFN guard gives 88.2% / 31.2%, .645250, 33.2 false warnings; mixture guard gives 83.5% / 36.8%, .665290, 24.6 false warnings. Exact TabPFN F2 and mixture F2 rules give 74.1% / 81.2% recall respectively and lower F2. Original 5x5 outer / four inner folds, eight questions and >=4 outcome retained; thresholds and RF shares 1/.75/.5/0 selected inside training only. RF-only exact controls isolate threshold effects. Independent verification passed for all 5,820 saved prediction rows, 10,061 candidate rows and 150 decisions, including contexts/folds, endpoint reconstruction, metrics and unchanged hashes. No calibration, new data, deployment fit or replacement of previous results. Details: [classification instructions](../classification/README.md).

## Local TabPFN-2 classification comparison (14 November 2026)

Completed separate [TabPFN-2 results](../classification/tabpfn-outputs/20261114T124506935366Z/results.md). **Keep the selected RF.** With the same eight inputs and original 5x5 outer / four inner folds, TabPFN's inner-F2 rule gives 81.2% recall / 36.5% precision, F2 .651386 and 24.2 false warnings; its recall guard gives 89.4% / 26.1%, .598623 and 44.0 false warnings. Current RF remains 87.1% / 34.7%, .667848 and 28.0. Ranking improves (AP .615797 vs .526861; ROC AUC .846176 vs .808971), but the tested warning rules do not justify replacement. Public original v2 weights, fixed eight estimators, 125 local CPU context fits, no synthetic survey rows or new inputs. Independent verification passed for all 1,455 predictions, 525 threshold candidates, 50 decisions, metrics, folds and source hashes. Separate environment/output folders preserve previous experiments; no deployment fit or independent cohort. See [classification instructions](../classification/README.md).

## RF backward question selection (14 November 2026)

Completed separate [backward-selection experiment](../classification/backward-selection-outputs/20261114T122443497555Z/results.md), retaining all earlier results. Starting at eight inputs, training-only one-question removals were accepted by strict F2 improvement or by fewer FP while retaining current inner recall. Both new rules achieved 82.4% outer High recall, versus the selected RF's 87.1%; F2 was .641302/.647200 versus .667848. False warnings fell to 27.2/26.2 from 28.0. Keep the current selected eight-question RF. All 345 evaluated subsets, 7,245 threshold rows, 79 backward steps, final selections, predictions/metrics, original folds, full-eight reference and hashes passed independent verification. This is a greedy comparison conditional on existing RF settings, not exhaustive subset/model optimization. See [classification instructions](../classification/README.md).

## RF training-only question selection (14 November 2026)

Separate [4/6/8-question experiment](../classification/question-selection-outputs/20261113T220427919147Z/results.md) completed without changing the selected RF or earlier outputs. Both inner selection rules averaged 85.9% High recall/35.2% precision and 27.0 false warnings, with F2 .6662/.6664, versus the current eight-question RF's 87.1%/34.7%, 28.0 and .6678. All eight questions were retained in 20/25 F2 selections and 23/25 recall-guard selections. Keep the selected eight-question RF for High detection. Question ranking was learned from real training students separately within every inner/outer fit; current RF settings, weights and augmentation were retained. All predictions, summaries, candidate decisions, 125 independently refitted rankings, original folds/recipes and source hashes were checked. This is a conditional selection experiment, not an exhaustive test of every subset or selector. See [classification instructions](../classification/README.md).

## Selected RF false-warning inspection (13 November 2026)

Completed [descriptive inspection](../classification/error-analysis-outputs/20261113T215342740935Z/findings.md) of the current 87.1%-recall RF. Of 80 Below-high students, 39 were warned at least once and 27 in >=3/5 repetitions; only six of the 39 scored 3.5..<4. Of 140 repeated false-warning events, 114 (81.4%) involved scores below 3.5. Correctly warned High students reported higher workload/AI dependence and lower university support on average, but these are outcome-selected descriptive groups, not validated feature importance. One High student was never detected (score 4.083, workload 4, AI dependence 2). All score-band counts, unique-student comparisons, category distributions, nearest peers and source hashes were independently checked. No model or metric changed. A training-only subset comparison using existing inputs is a proposed next experiment, not a demonstrated improvement. See [classification instructions](../classification/README.md).

## Current selected RF plus logistic comparison (13 November 2026)

A separate [ensemble run](../classification/voting-outputs/20261113T203744495093Z/results.md) tested the user's current 87.1%-recall RF with real-only Small B logistic. The recall-guard mixture gave 85.9% recall/35.7% precision, F2 .669893 and 26.4 false warnings, versus the RF's 87.1%/34.7%, .667848 and 28.0. RF-only finer thresholds retained 87.1% recall and reduced mean false warnings to 27.8 (one fewer across all five repetitions). Pure F2 mixture selection reduced recall to 83.5%. These are small trade-offs; no substantial upgrade at the original recall was established. Keep the current selected RF and the regression blend. All predictions, metrics, mixture algebra, inner selections, error comparisons, folds and source hashes were independently verified; see [classification instructions](../classification/README.md).

## Focused Random Forest tuning (13 November 2026)

Completed separate [classification tuning run](../classification/forest-tuning-outputs/20261113T154534173272Z/results.md) on the existing eight Small B inputs and identical nested folds. Expanded F2 tuning gave 84.7% High recall/37.1% precision, F2 .673 and 24.6 false warnings, versus the user's selected RF at 87.1%/34.7%, .668 and 28.0. The inner-recall-constrained procedure gave 82.4%/38.0%, .668 and 22.8; its >=85% training target was not guaranteed on outer students. These are modest detection/false-warning trade-offs, not improvements across all metrics. Retain the selected RF for the user's High-detection priority and keep the regression blend unchanged. All predictions, metrics, candidate threshold arithmetic, selection rules, original folds/pools and source hashes passed independent verification. Full details: [classification instructions](../classification/README.md) and [analysis progress](../docs/analysis-progress.md).

## Selected classification model

The user selected Small B Random Forest with training-selected augmentation: 87.1% High recall, 34.7% precision, F2 .668 and 28.0 false warnings per 80 Below-high students. These average five repetitions of the same 97 students. The existing blend remains the numerical score predictor. See [classification instructions](../classification/README.md) for the retained experiment and results.

## Synthetic binary warning experiment (reviewed 13 November 2026)

Completed separate run: [results](../classification/augmentation-outputs/20261112T125001425382Z/results.md). Logistic regression, forest, XGBoost and histogram boosting were trained on Small B/Broad D with constrained, unique synthetic High training profiles. Only real held-out students were evaluated. Small B XGBoost with training-selected augmentation led mean F2 at .670 (85.9% recall, 35.8% precision), versus real-only XGBoost's .642 (83.5%/33.4%). Against the existing threshold-tuned blend (.653, 80.0%/37.8%), it detected one more High student but added four false warnings on average. This is a modest exploratory classification trade-off, not improved score MAE or an independently confirmed winner. The user's selected score-prediction blend remains unchanged. All predictions, metric summaries, tuning choices, synthetic provenance and source hashes were independently checked. Read [classification instructions](../classification/README.md) and [analysis progress](../docs/analysis-progress.md) for details.

## Selected score model and binary warnings (12 November 2026)

The user selected the fixed 50/50 High-priority Small B ridge / Broad D SVR blend for the high-score trade-off (historical regression MAE .6160 overall/.6422 High). No deployment artifact has been saved. A separate binary warning comparison is complete in `classification/binary-outputs/20261112T115553112588Z/`: all four classifier families and a refitted blend share new stratified nested folds. The blend with a training-selected warning trigger achieved 80.0% recall/37.8% precision, almost tied with Small B logistic at 78.8%/39.0%. These are classification metrics on new folds, not reduced regression errors. False warnings remain substantial. Read [classification instructions](../classification/README.md) and [analysis progress](../docs/analysis-progress.md) before interpreting or rerunning.

## Removed PCA/PLS and dependent loss-tuning experiments

The runners, configurations and output folders were deleted on 16 November 2026 at the user's request. Their methods, numerical results and limitations remain in [the analysis progress record](../docs/analysis-progress.md#overall-mae-loss-tuning-completed-11-november-2026) for the paper and presentation.

We tested PLS, PCA + ridge and PCA + SVR on Small B/Broad D with training-only extraction and nested validation. Broad D ordinary PCA + ridge achieved .5748 overall/.8991 High MAE. High-priority PCA + ridge achieved .6026/.6638 on Broad D and .6339/.6274 on Small B; neither improved both errors over the fixed ridge/SVR blend (.6160/.6422). PCA therefore did improve ordinary overall MAE; its high-score trade-off did not replace the selected blend.

The dependent loss-tuning bundle included refined PCA + ridge alongside boosting/Huber/median models and required the deleted extraction artifacts. It was removed as a coupled experiment rather than leaving a broken runner. Refined Broad D PCA + ridge gave .5755/.8969 overall/High MAE; Broad D Huber boosting gave .6102/1.0514. The full historical tables, including non-PCA methods, remain in the progress record. These deleted runs cannot be reopened or rerun from the remaining files.

## Existing-question selection and fit diagnostics (2 November 2026)

Completed run: `analysis/outputs/feature-selection-experiments/20261102T163807090063Z/`. Small B high-priority Elastic Net achieved .6232 overall/.6442 High MAE. Broad D high-priority question-selected SVR achieved .6438/.6312. The earlier fixed blend was .6160/.6422, so neither new option improved both metrics over it. Broad D selected SVR had an average in-sample/outer-fold MAE gap around .20; these diagnostics describe generalization differences, not proof of the cause. Read [analysis progress](../docs/analysis-progress.md) for the full table and limitations.

Run `.\.venv\Scripts\python.exe analysis/scripts/train-feature-selection.py` from the repository root. Settings: [feature-selection-config.json](feature-selection-config.json). Runs go under `analysis/outputs/feature-selection-experiments/`, excluded from Git. Require a complete manifest before interpreting results. No extra dependency is needed.

Elastic Net and question-selected SVR use Small B/Broad D, the primary continuous target, original five outer folds repeated five times and four inner folds. No survey variables, BAT predictors, engineered interactions or synthetic records are added. Standard category encoding and scaling are fitted in training folds. SVR selection ranks original questions by an Elastic Net fitted only to that training group, retaining all encoded columns for a chosen question. Ranking uses the coefficient L2 norm divided by the square root of the encoded-column count, with stable questionnaire-order ties. Selection counts are 4/8/all, deduplicated per set. All inputs remain eligible.

The selector has fixed alpha .03/l1 ratio .8. Direct Elastic Net tunes alpha .001/.01/.1/1 and l1 ratio .2/.8/1. SVR retains the previous C/gamma/epsilon grid. Each family compares training-only normalized high-score weights 1/2/4. Ordinary minimizes mean inner-fold overall MAE at factor 1. High-priority minimizes pooled inner High MAE within .05 pooled overall MAE of ordinary, with ordinary fallback without High cases. The inner tolerance is not an outer-error guarantee.

Reports include pooled repetition errors, matched differences against saved ridge/SVR, the saved fixed ensemble reference, per-fold training/inner/outer MAE, question frequencies, selected questions and all tuning candidates. Training MAE is in-sample and optimistically biased; a train/validation gap alone cannot prove memorization or an information limit. Solvers stop the run on convergence warnings. Runtime assertions check original folds, complete finite predictions, score alignment and unchanged source files. This is another exploratory same-sample follow-up, not independent validation of a final winner. No deployment model is saved.

## Ridge/SVR prediction blend (2 November 2026)

Completed run: `analysis/outputs/ensemble-experiments/20261102T163006135317Z/`. The fixed 50/50 blend achieved .6160 overall/.6422 High MAE, modestly lower than either endpoint (.6282/.6649 ridge; .6282/.6705 SVR). The inner-selected blend achieved .6343/.6664 and did not improve both errors over either endpoint. Endpoint predictions and original splits reproduced; source hashes were unchanged. Read [analysis progress](../docs/analysis-progress.md) for the distinction between fixed and selected blending.

Run `.\.venv\Scripts\python.exe analysis/scripts/train-ensemble.py` from the repository root. Settings: [ensemble-config.json](ensemble-config.json). Each run writes a separate folder under `analysis/outputs/ensemble-experiments/`, excluded from Git. Only interpret a run with a complete manifest.

The comparison combines the previous high-priority Small B ridge and Broad D SVR. It uses the existing survey inputs and primary continuous target; no new survey variables, BAT predictors or synthetic records are added. Each base model retains its original inner tuning and training-only preprocessing. Within each outer training group, the selected base models produce four-fold inner out-of-fold predictions. Candidate SVR shares are 0/.25/.5/.75/1, with ridge taking the remainder. The blend averages each model's clipped 1–5 prediction.

Select the share minimizing pooled inner High MAE subject to overall MAE within .05 of ordinary Small B ridge's pooled inner MAE; ties use overall MAE then smaller SVR share. Without High students, minimize overall MAE. Endpoint shares are allowed, so selection may return one base model. The same inner predictions inform base hyperparameters and blend share; the original excluded outer groups evaluate the complete selection procedure. No share is selected by looking at pooled outer predictions. A fixed 50/50 blend is reported separately as a preselected reference.

Outputs include endpoint and blend predictions, repeat/summary metrics, matched changes versus each endpoint, per-fold choices and candidates, error-complementarity diagnostics, configs and source hashes. Descriptive diagnostics compare endpoint signed-error correlation, opposite signs, and large-error overlap; they do not select settings. Endpoint predictions and original outer folds must reproduce. This is another exploratory same-sample follow-up, not independent validation of a final winner. No deployment model is saved.

## SVR and kernel ridge with existing inputs (2 November 2026)

Completed run: `analysis/outputs/kernel-experiments/20261102T160828159897Z/`. None of the eight new procedures improved overall MAE over input-matched ordinary ridge. Broad D high-priority SVR produced .6282 overall MAE and .6705 High MAE; compare .5933/.9281 for ordinary Broad D ridge and .6282/.6649 for earlier Small B weighted ridge. Read [analysis progress](../docs/analysis-progress.md) for the full comparison. Raw kernel ridge here has no fitted intercept or target centering.

Run `.\.venv\Scripts\python.exe analysis/scripts/train-kernels.py` from the repository root. Configuration: [kernel-config.json](kernel-config.json). Each run creates a separate folder under `analysis/outputs/kernel-experiments/`, excluded from Git. Open a completed run's `results.md`; its manifest must say `complete`.

The primary continuous score is predicted from the existing Small B and Broad D inputs. There are no added questionnaire variables, BAT predictors, engineered interactions, or synthetic records in this experiment. Existing one-hot category encoding and standard scaling are reused and fitted inside training folds. SVR and kernel ridge use RBF kernels to learn nonlinear relationships internally. The source survey does not change.

Original five outer folds, repeated five times, and four inner folds are retained. SVR tunes C, gamma and epsilon; kernel ridge tunes alpha and gamma. Both compare normalized High (actual >=4) sample-weight factors 1/2/4. Ordinary selection minimizes mean inner-fold MAE with factor 1. High-priority selection minimizes pooled inner High MAE among candidates within .05 pooled overall MAE of ordinary, with a fallback to ordinary without High students. The tolerance is an analytical choice and does not guarantee the same bound on outer error. Scaling uses unweighted training statistics, matching the previous ridge approach.

Files include real held-out predictions, original outer assignments, per-repetition and summary metrics, paired differences from saved ordinary ridge, all inner candidate metrics and selected settings, configs and source hashes. Runtime assertions check complete per-student predictions, finite outputs, original fold alignment, and unchanged source files. This exploratory follow-up is not independent validation, and no deployment model or weights are saved.

## Synthetic training data for regression (2 November 2026)

Run `.\.venv\Scripts\python.exe analysis/scripts/train-augmentation.py` from the repository root. Settings are in [augmentation-config.json](augmentation-config.json). Completed run: `analysis/outputs/augmentation-experiments/20261102T153249814079Z/`; open `results.md`. This is a separate follow-up on Small B linear/ridge regression and the primary continuous score, not classification.

The comparison fits real-only data, real data plus duplicated eligible students, and real data plus local interpolations. Neighbors must have identical sleep/study categories, similar numeric answers and nearby scores in the same sampling band. Inputs stay in legal ranges. Generated scores are interpolated estimates, not measured BAT scores. Augmentation is repeated inside every inner training fit; only real excluded students are evaluated. Original folds, ridge tuning and unaugmented predictions are reproduced.

Files include settings and source hashes, real held-out predictions, metrics and paired differences, tuning, generation counts, and `outer-training-real-and-synthetic.csv`. That last file contains the actual training tables with `synthetic`, parent row indices and interpolation fractions; it repeats records across model fits and is not one independent survey dataset. Output folders are excluded from Git. Source SAV/SPSS data and earlier runs are unchanged. No deployment model is saved.

Interpolation improved high-score MAE but worsened overall and lower-score MAE. Ridge overall MAE changed .5883 to .5972 and high-score MAE .9329 to .7783. Duplication alone reached high-score MAE .8081, so much of the benefit can be obtained by changing training emphasis. The generator found no eligible Low pairs; every generated outer-training example was High. Do not describe these records as additional participants or clinically validated responses. See [the analysis record](../docs/analysis-progress.md) for all six comparisons.

## Removed fixed-interaction experiment

The interaction runner, configuration, tests, cached bytecode and outputs were deleted on 16 November 2026 at the user's request. We tested workload-by-sleep-category terms and centered AI-dependence-by-offloading terms in linear/ridge regression, keeping the original main effects and nested folds.

Primary linear overall/High MAE changed from .6155/.7622 to .6131/.8356; ridge changed from .5883/.9329 to .5872/.9011. Overall gains were tiny and linear high-score errors worsened. The full results and limitations remain in [the progress record](../docs/analysis-progress.md#fixed-interactions-in-linear-and-ridge-regression). This does not establish that all interactions are unhelpful. No runnable interaction experiment remains.

## High-score-priority ridge follow-up (2 November 2026)

Configuration: `analysis/high-score-config.json`. Run `analysis/scripts/test-high-score.py` for software checks and `analysis/scripts/train-high-score.py` for the experiment, using the project Python environment. Each run writes a separate timestamped folder under **`analysis/outputs/high-score-experiments/`**. Participant-level outputs are excluded from Git. Original data and completed runs are read-only.

This exploratory follow-up prioritizes measured scores >=4, a descriptive boundary rather than a clinical cutoff. It uses Small B and both burnout outcomes, preserving the original outer and inner splits. It tests relative high-score training weights 1/2/4 and the original six ridge alphas. Each training fold calculates weights from its own labels only, normalizes them to mean one, and fits the existing category/scaling pipeline. Scaling is unweighted and uses training students only, as in the original workflow. The sample weights reach the ridge estimator; no students are duplicated or generated.

Inner selection first finds ordinary ridge by mean inner-fold overall MAE, reproducing the original procedure. Candidates whose pooled inner overall MAE is at most .05 points worse than that ordinary ridge are eligible; among them, choose lowest pooled inner high-score MAE, breaking ties by overall MAE, lower weight, then lower alpha. The chosen candidate may have weight 1. If no high-score students occur in the outer training set, use ordinary ridge. The .05 tolerance is a recorded analytical guardrail, not an established practical or clinical standard. It is not enforced by looking at outer-test results.

The report includes high-score MAE, signed error, mean underestimation, overall/lower-score MAE, and descriptive precision/recall and false positives at the same boundary. The numerical goal is reduced high-score MAE without outer overall MAE increasing more than .05, reported per repetition and in aggregate. No claim of independent confirmation, clinical detection, or significant improvement follows from this same-sample follow-up. Repetitions share students. Ordinary-ridge outer predictions must match the saved original predictions or the run stops. Fold alignment and unchanged source hashes are also verified.

Open a completed run's `results.md` first. The folder also contains predictions, per-repetition metrics, paired changes, every inner candidate's metrics and selected settings, source configuration, and a manifest. No final model or weights are saved.

## Saved-prediction diagnostics

Run `analysis/scripts/diagnose-predictions.py` using the project Python environment to inspect the existing completed original and XGBoost runs. It fits no models. It writes a new timestamped folder under `analysis/outputs/diagnostics/` containing `findings.md`, prediction-spread summaries, student errors and input values, similar-student matches, tuning counts, and a source-hash manifest. Participant-level outputs are excluded from Git. It requires the two local source run folders named in the script.

The similarity definition is fixed in the script: equal weight for eight Small B questions, differences divided by four on six 1–5 items, and 0/1 mismatches on sleep and study-hour categories. Matching excludes the same student and resolves ties by row order. It is descriptive exploration using all students, not an additional cross-validation score or proof of causation. The script includes distance self-checks and verifies saved predictions, score alignment, and unchanged source files.

## Separate XGBoost follow-up (2 November 2026)

After reviewing the original real-data results, we added an exploratory XGBoost comparison for **Small A and Small B only**, for both burnout targets. It reuses the original five repetitions, five outer folds, four inner folds, input encoding, and 1–5 prediction bounds. No synthetic students or oversampling are used. This is a follow-up chosen after seeing results, not independent confirmation.

Configuration: `analysis/xgboost-config.json`. The original configuration and run are retained. The shared training engine adds optional XGBoost support; the separate runner verifies alignment with the original completed run before fitting.

```powershell
.\.venv\Scripts\python.exe -m pip install -r analysis/requirements-xgboost.txt
.\.venv\Scripts\python.exe analysis/scripts/train-xgboost.py --check-only
.\.venv\Scripts\python.exe analysis/scripts/test-xgboost.py
.\.venv\Scripts\python.exe analysis/scripts/train-xgboost.py
```

Each run creates a new folder under **`analysis/outputs/xgboost-experiments/`**, excluded from Git because it contains individual predictions. Open `comparison-with-original.md` first, then `results.md`. Original model-run and SPSS files are not overwritten. This workflow evaluates models; it does not save a final deployment pipeline.

The four inner tuning candidates combine tree depths 1/2 with 50/150 trees. Learning rate is .05, minimum child weight 5, and L2 penalty 10; CPU execution uses one thread. Selection uses MAE only inside training groups. No early stopping or outer-test feedback is used. These choices are a limited follow-up grid, not established optimal values. Parameter definitions: [official XGBoost documentation](https://xgboost.readthedocs.io/en/stable/parameter.html).

Additional outputs compare XGBoost with the original Small A/B ridge predictions after checking student, target, and fold alignment. `score-range-errors-by-repeat.csv` reports MAE, signed error, and the fraction of errors over one point. The descriptive ranges **below 2.5**, **2.5 to below 4**, and **4 or above** are not clinical categories or new targets. These ranges were selected to inspect the extreme-score problem seen in the first results. Negative signed error means underestimation. Repetitions reuse students; their variation is not a confidence interval.

Only treat the full follow-up as complete when its manifest says `complete` and the comparison report exists. The SAV and original predictions remain read-only.

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
