# Work plan

Organization updated 19 November 2026. See [the project README](../README.md) for current folders and commands. Timestamped paths below describe historical runs; the original verified validation namespace is preserved in the local results/99-original-workspace-and-verified-validation.zip archive. [The current readable validation report](../results/25-random-forest-validation-report.md) uses the new filenames.

## Latest status: 18 November 2026

Completed [the model-validation plan](11-random-forest-validation-plan.md); read [the verified report](../results/25-random-forest-validation-report.md). Missing historical outputs were regenerated for the selected RF only, reproducing all seven recorded RF means exactly. Workload-only logistic gives 94.1% recall/36.4% precision (16 High detections, 28 false warnings), versus RF 87.1%/34.7% (14.8 detections, 28 false warnings). Paired conditional intervals include zero; workload AP is lower (.423 versus RF .527), so do not claim uniform or independently confirmed superiority. All 199 complete student-label permutations finished: observed balanced accuracy .760294 versus null mean .495704/max .636103, corrected p=.005. This diagnostic does not account for the entire historical model search. Audit: `results/25-random-forest-validation/20261118T143652947217Z/`; 5,000 fold records/180,000 candidate choices checked, 125 real training pools regenerated, 25 selected real outer models refitted, one full real and one full null search replayed, all null metrics/p-value independently recomputed. Nine relevant tests pass. Source data, selected recipe and .35 final-model threshold are unchanged. Original trained binary/metadata remain missing; the recorded recipe/schema are preserved separately and no model backup is claimed. The following paragraphs record earlier work.

Documentation handoff updated; no new experiment or model change. Start a new chat with [09-current-project-handoff.md](09-current-project-handoff.md). The [synthetic generation worked example](07-classification-experiments-and-methods.md#how-one-synthetic-profile-is-created) explains the exact six-answer interpolation/two-category-copy procedure and why the 2,720 historical training instances, zero synthetic rows in the final saved fit, and 970 inference-only profiles are different. Continue only with the next authorized task; no experiment is currently running.

Separate synthetic inference check completed in `results/24-synthetic-profile-check/20261117T130726203314Z/`. The frozen saved model predicted 970 novel constrained profiles (800 Below-high/170 High) labelled by same-class real parents: assumed-label recall 93.5%, precision 55.6%, F2 .822981, TP/FN 159/11, FP/TN 127/673. These are dependent synthetic neighbourhoods of parents already used in model fitting, not new measured students or improved real held-out performance. All provenance/constraints/metrics/persisted scores/hashes checked. No model retraining/replacement or threshold change; original 87.1% real CV recall remains the evaluation evidence. See [simulation details](07-classification-experiments-and-methods.md#saved-model-synthetic-profile-check-17-november-2026).

The selected classifier has been fitted on all 97 real students and saved to `results/23-selected-random-forest.joblib`, with metadata beside it. Original training-only selection chose depth 3/min leaf 10/High weight 2/threshold .35/ratio 0, with 100 trees and seed 271828. Zero augmentation was allowed; no synthetic rows were selected for this final fit. Existing 87.1% recall/34.7% precision remain earlier CV evidence, not a new performance estimate. Model and preprocessing load together; roundtrip/fresh-process checks reproduce all 97 scores and labels. Runner `experiments/23-save-selected-random-forest.py`, configuration `experiments/23-save-selected-random-forest-settings.json`, audit `results/23-selected-random-forest-fit/20261117T114817911532Z/`. These artifacts are ignored by Git; copy them separately for backup/sharing. The score-regression blend remains unexported. See [loading instructions](07-classification-experiments-and-methods.md#saved-final-classifier-17-november-2026). Next: use the saved artifact for authorized inference/demo work, preserving the evaluation limitations.

PCA/PLS extraction, fixed-interaction and their dependent mixed loss-tuning experiment code/configurations/outputs were removed at the user's request. Their historical methods and results remain in [analysis progress](06-data-analysis-and-experiment-history.md) for reporting. Older mentions below are historical records, not instructions to reopen or rerun those deleted artifacts. Current selected RF, source data, separate ridge/SVR blend and unrelated experiments are preserved.

Boruta-based RF selection completed separately in `results/22-boruta-input-selection/20261116T082517133758Z/`. **Keep current eight-input RF (87.1% recall/34.7% precision, F2 .667848, 28.0 false warnings).** Training-only confirmed Boruta selections from all 23 inputs retain 2–5 variables per outer fit. F2 rule reaches 72.9%/36.1%, .604040, 22.2 warnings; recall guard gives 82.4%/32.6%, .630103, 29.0 warnings. Neither improves the user's detection/false-warning priority. Same original nested folds, independently tuned original RF/weights/augmentation/threshold grid; 125 selector fits, 5,894 selector iterations, 3,600 inner/40 outer prediction fits. Results/support histories/provenance/metrics/verification stored separately; only Boruta 0.4.3 added, earlier source/results and dependency versions unchanged. Next: retain selected RF and this measured comparison. See [classification details](07-classification-experiments-and-methods.md#boruta-selection-from-all-23-inputs-16-november-2026).

Alternative RF input combinations completed separately in `results/21-random-forest-input-comparison/20261116T075921907598Z/`. **Keep current eight-input RF (87.1% recall/34.7% precision, F2 .667848).** Fixed alternative eight replacing AI frequency/study hours with academic stress/avoidance gives F2-tuned 72.9%/37.3% or guarded 81.2%/32.5%. Training-only selection of eight from 23 gives 72.9%/37.9% or guarded 83.5%/33.5%. Neither retains current recall or improves F2; guarded approaches add .6/.2 false warnings. Same original nested folds, independent tuning of original forest/weights/augmentation/threshold grids, 7,300 inner/104 outer initial fits; current reference scores reproduced. Separate predictions, tuning/rankings, generation provenance, metrics and verification preserve this experiment. No previous-result replacement or new observed students. Next: retain selected RF and this measured comparison; repeated use of the same 97 students remains exploratory. See [classification details](07-classification-experiments-and-methods.md#alternative-input-combinations-16-november-2026).

23-input RBF SVC completed separately in `results/20-twenty-three-input-svc/20261116T072730431772Z/`. **Keep RF for the current High-detection priority.** Broad-input recall guard improves versus eight-input SVC (83.5%/35.4% recall/precision vs 80.0%/33.4%; F2 .655506 vs .624572; warnings 26.2 vs 27.2), but RF remains 87.1%/34.7%, F2 .667848, 28.0 warnings. Broad-input F2 rule gives 76.5%/40.4%, F2 .646090, 19.4 warnings. Same independently tuned 36-setting grid and original nested folds, 23 original variables/37 encoded columns, real-only SVC; 3,600 inner/35 outer initial fits. All 2,425 predictions, 900 score sets, 62,758 threshold candidates, 50 choices, memberships/controls/metrics/hashes independently verified, including 140 inner/35 outer selected refits. Previous results/source/helpers unchanged; no deployment or independent validation. Next: retain this trade-off comparison and selected RF. See [analysis progress](06-data-analysis-and-experiment-history.md).

RBF SVC classification completed separately in `results/19-eight-input-svc/20261116T070622236133Z/`. **Keep the selected RF.** SVC inner-F2 gives 78.8% recall / 36.2% precision, F2 .637154 and 23.6 false warnings; guard gives 80.0% / 33.4%, .624572 and 27.2. RF remains 87.1% / 34.7%, .667848 and 28.0. Same eight questions, primary >=4 target, original nested folds, real-only SVC and 36 C/gamma/High-weight combinations with inner margin threshold tuning. Initial 3,600 inner / 37 outer fits; independent verification refitted 148 selected inner / 37 outer models and checked all 1,455 predictions, 900 candidate arrays, 71,604 threshold rows, 50 decisions, folds, metrics and hashes. No new data/features, package installation, deployment fit or replacement of previous results. Next: preserve the RF reference; the tested SVC procedures did not achieve the requested detection/false-warning improvement. See [analysis progress](06-data-analysis-and-experiment-history.md).

Precise TabPFN thresholds and RF–TabPFN mixtures completed separately in `results/18-tabpfn-threshold-refinement/20261114T125820967153Z/` and `results/18-tabpfn-voting-refinement/20261114T125820967153Z/`. **Keep the selected RF.** Exact TabPFN guard gives 88.2% recall / 31.2% precision, F2 .645250 and 33.2 false warnings versus RF 87.1% / 34.7%, .667848 and 28.0. Mixture guard gives 83.5% / 36.8%, .665290 and 24.6 false warnings. F2-only rules also fail to improve mean held-out F2. Both use verified frozen endpoint inner/outer scores, original nested folds, exact inner score thresholds and RF shares 1/.75/.5/0 with RF-only controls. No endpoint fits, calibration, added questions/students/synthetic generation or dependency changes. All 5,820 saved prediction rows, 10,061 candidate rows, 150 choices, contexts, folds, reconstructed scores, metrics and hashes passed independent verification. Earlier results/data and selected RF remain unchanged. Next: retain these measured trade-offs; inner optimization gains did not establish a better held-out warning procedure. See [analysis progress](06-data-analysis-and-experiment-history.md).

Local TabPFN-2 comparison completed separately in `results/17-tabpfn-comparison/20261114T124506935366Z/`. **Keep the selected RF.** TabPFN improves AP/AUC (.615797/.846176 vs RF .526861/.808971), but its inner-F2 warning rule loses High recall (81.2% vs 87.1%), while its recall guard adds 16 false warnings for .4 more High detections on average (89.4% recall, 44.0 false warnings vs RF 28.0). Both new F2 scores are lower (.651386/.598623 vs .667848). Used public v2 weights, eight fixed estimators, existing eight questions, real training students only, original nested folds and a separate local environment; no survey upload or deployment fit. All 1,455 predictions, 525 threshold candidates, 50 selections, metrics, folds and hashes passed independent verification. Old results and data remain unchanged. Next: preserve this experiment as evidence; finer threshold/calibration work would be a separate training-only comparison, not an already demonstrated improvement. See [analysis progress](06-data-analysis-and-experiment-history.md).

Backward RF question selection completed in the separate folder `results/16-backward-question-selection/20261114T122443497555Z/`. Original data, selected model and earlier outputs remain unchanged. Strict-F2 and recall-guard removal paths both achieved 82.4% High recall (14.0/17 detected) versus current 87.1% (14.8/17). F2 fell from .667848 to .641302/.647200; false warnings averaged 27.2/26.2 versus 28.0. Keep the current eight-question RF. The search evaluated 345 subsets across training folds; all 7,245 threshold rows, 79 backward steps, 75 final choices, predictions, metrics, folds, recipes and hashes were independently checked. The full-eight control reproduced current RF predictions. Next: retain this negative comparison as research evidence; it does not justify changing the selected model. Any further proposal should distinguish a new mechanism from the selection approaches already tested. See [analysis progress](06-data-analysis-and-experiment-history.md).

Training-only RF question selection completed separately: `results/15-four-six-eight-question-selection/20261113T220427919147Z/` (UTC folder date; completed 14 November in Beirut). F2-based and recall-guard selection among 4/6/8 existing questions both averaged 85.9% High recall/35.2% precision, 14.6 High detections and 27.0 false warnings, with F2 .666235/.666386. The current eight-question RF remains 87.1%/34.7%, 14.8 detections, 28.0 false warnings and .667848. All eight questions were retained in 20/25 F2 selections and 23/25 guarded selections. Keep the current selected RF. No model/data/previous output was replaced. All predictions/metrics, 1,575 candidate rows, 75 decisions, original folds/recipes and 125 independently refitted real-training-only rankings passed verification. Next: use this result when prioritizing further experiments; it does not support dropping questions under this selector. The outcome is specific to fixed-current-RF settings and this ranking method. Full details: [analysis progress](06-data-analysis-and-experiment-history.md).

Descriptive inspection of the selected RF completed in `results/14-random-forest-false-warnings/20261113T215342740935Z/`. There were 39 distinct Below-high students falsely warned at least once, including 27 warned in >=3/5 repetitions. Only six scored 3.5..<4; 81.4% of repeated false-warning events involved scores below 3.5. Correctly warned High profiles had higher workload/AI dependence and lower university support on average. These are descriptive comparisons; the RF already uses those inputs, and no simple fix is established. One High student (score 4.083) was missed in all repetitions despite workload 4 and AI dependence 2. Counts, eight-input comparisons, nearest peers and source hashes passed independent verification. No model was trained or changed. Next proposed experiment: compare a small set of existing-input subsets, with selection inside training validation and the current eight-input RF retained as reference. Do not use global group differences as validated selection rules or change the target boundary. See [analysis progress](06-data-analysis-and-experiment-history.md).

The current selected RF was compared with an RF/logistic ensemble in `results/13-random-forest-logistic-voting/20261113T203744495093Z/`. Guarded mixing gave 85.9% recall/35.7% precision, F2 .669893 and 26.4 false warnings, compared with 87.1%/34.7%, .667848 and 28.0 for the current RF. RF-only finer threshold selection retained 87.1% recall but reduced average false warnings only to 27.8. Pure F2 mixing gave 83.5% recall/37.2% precision, .666125 and 24.4 false warnings. No substantial improvement at the user's preferred recall was established. Preserve the current selected RF, retain the new results separately and treat the threshold refinement as a very small alternative. All 3,395 predictions, metric summaries, 4,100 inner candidates, 100 selections, endpoint comparisons, folds and source hashes were verified. No deployment model was saved. Next: review whether these small false-warning/detection trade-offs justify changing the selected procedure. See [analysis progress](06-data-analysis-and-experiment-history.md).

Focused Small B RF tuning completed separately in `results/12-random-forest-tuning/20261113T154534173272Z/`. Expanded F2 tuning reduced mean false warnings from 28.0 to 24.6 and improved precision from 34.7% to 37.1%, while recall fell from 87.1% to 84.7%; F2 rose slightly from .668 to .673. Requiring >=85% inner recall and then minimizing inner false positives yielded 82.4% outer recall/38.0% precision and 22.8 false warnings, F2 .668. The inner target is not an outer guarantee. No new procedure improved every main metric. Independent verification passed for all predictions/metrics, 2,700 candidate score sets, 110,700 threshold rows, 50 selections, reference folds/pools and unchanged sources. Keep the user's current RF for High detection and preserve both new alternatives as recorded trade-offs. Next: decide whether fewer false warnings justify the observed loss in High detections before changing the selected procedure. No final model or threshold has been fitted on all students. See [analysis progress](06-data-analysis-and-experiment-history.md).

The user selected Small B Random Forest with training-selected augmentation as the classification candidate: 87.1% High recall, 34.7% precision, F2 .668 and 28.0 false warnings per 80 Below-high students. Keep the retained augmentation experiment and the selected regression blend. No deployment artifact has been saved. Next: review the selected warning procedure's false-warning burden before fitting a final artifact.

Synthetic binary augmentation completed in `results/11-classifier-training-augmentation/20261112T125001425382Z/`, preserving all earlier results. All four classifier families used both existing input sets, with half/full batches and a training-only no/half/full batch selector. The leading mean F2 was Small B XGBoost with selected augmentation: .670, 85.9% High recall, 35.8% precision and 26.4 false warnings per 80 Below-high students. It modestly improved real-only XGBoost (.642, 83.5%/33.4%, 28.4 false warnings). Relative to the tuned blend (.653, 80.0%/37.8%, 22.4 false warnings), it caught one extra High student while making four extra false warnings on average. Only real students were evaluated; 2,720 profile instances across repeated training fits do not increase the real sample size. Independent verification passed for all predictions, summaries, tuning choices, generation provenance and source hashes. Next: compare the augmented XGBoost warning trade-off with the existing blend before choosing a final warning procedure. Retain the selected blend for numerical score prediction; these classification results do not improve its MAE. See [analysis progress](06-data-analysis-and-experiment-history.md).

The user selected the fixed 50/50 weighted-ridge / high-priority SVR blend for score prediction, prioritizing high-score students over the lowest overall MAE. Keep this research choice distinct from the ordinary PCA + ridge overall-error reference. Neither has a deployment artifact saved.

Binary High (>=4) / Below-high (<4) warnings completed separately: `results/10-high-burnout-classifiers/20261112T115553112588Z/`. Four classifier families used Small B/Broad D with inner F2 tuning of settings, weights and thresholds; the blend was refitted on identical new stratified folds. Tuned blend: 80.0% recall/37.8% precision, F2 .653, 22.4 false warnings per 80 Below-high students. Small B logistic was close: 78.8%/39.0%, F2 .651, 21.4 false warnings. No convincing new classifier winner over the threshold-tuned blend. The same blend at cutoff 4 had 25.9% recall/62.1% precision; warning-threshold adjustment improves detection, not score accuracy. All 9,700 predictions, metrics, threshold choices, fold exclusion and source hashes were checked. Next: review whether the false-warning burden is acceptable before fitting a final warning procedure; do not choose one fixed deployment threshold from outer results. Full details: [analysis progress](06-data-analysis-and-experiment-history.md).

Overall-MAE loss tuning completed separately: `analysis/outputs/loss-tuning-experiments/20261111T163814733223Z/`. Tuned boosting with squared/absolute/Huber losses, linear median and Huber regressions, and a finer PCA + ridge grid on both existing input sets. All settings and the additional family-selection procedure used inner validation only. None beat the previous Broad D ordinary PCA + ridge's .5748 overall MAE. Refined PCA + ridge was .5755/.8969 overall/High, and the best boosting option was .6102/1.0514. Broad D inner family selection gave .5850/.9443. Keep the earlier ordinary PCA + ridge as the overall-error reference and the fixed blend as the high-score trade-off reference; this run does not justify replacing them. All summaries, predictions, tuning/selection decisions and source hashes were checked; see [analysis progress](06-data-analysis-and-experiment-history.md).

Separate feature extraction completed: `analysis/outputs/extraction-experiments/20261111T113950457894Z/`. PLS, PCA + ridge and PCA + SVR were evaluated on Small B/Broad D with ordinary/high-priority tuning, preserving previous outputs. Broad D ordinary PCA + ridge achieved .5748 overall/.8991 High MAE, compared with .5933/.9281 for its original ridge. Broad D high-priority PCA + ridge achieved .6026/.6638; Small B high-priority PCA + ridge achieved .6339/.6274. The previous fixed blend remains .6160/.6422: neither new high-priority option beats both of those errors. Recommendation: retain Broad D high-priority PCA + ridge as a promising balance for comparison with the blend; do not declare an independently validated winner. Read [analysis progress](06-data-analysis-and-experiment-history.md) for all twelve procedures, checks and limitations. No new questionnaire inputs, synthetic students or deployment model were added.

Existing-question selection completed: `results/08-score-input-selection/20261102T163807090063Z/`. Small B high-priority Elastic Net achieved .6232 overall/.6442 High MAE; Broad D high-priority selected SVR achieved .6438/.6312. The previous fixed blend was .6160/.6422, so neither improves both metrics over that reference. Broad D selected SVR had in-sample/outer MAE gaps around .20, which describe generalization differences without proving a cause. Read [analysis progress](06-data-analysis-and-experiment-history.md) for all eight procedures and diagnostics. No new inputs, participants or synthetic records were added. Future work should use these diagnostics to target generalization rather than assume more model complexity will help.

Ridge/SVR blend completed: `results/07-ridge-and-svr-score-blend/20261102T163006135317Z/`. The fixed 50/50 blend achieved .6160 overall/.6422 High MAE, modestly better on both than weighted ridge and high-priority SVR individually. The automatically selected blend achieved .6343/.6664 and did not improve both metrics. Original splits and both endpoints reproduced; source data remained unchanged. Read [analysis progress](06-data-analysis-and-experiment-history.md) before treating the fixed blend as a final choice. Next: assess whether its modest gain and remaining high-score misses meet the research goal; any further tuning must remain inside training groups.

The latest CatBoost experiment files and outputs were removed at the user's request. The result was essentially tied with weighted ridge on high-score error and worse overall. Earlier experiments remain. The proposed ridge/SVR blend has now been evaluated as described above.

SVR/kernel-ridge follow-up completed: `results/06-svr-and-kernel-score-prediction/20261102T160828159897Z/`. Eight procedures used existing Small B/Broad D inputs only, with ordinary/high-priority selection and the original nested folds. No new survey variables or samples were added. None improved overall MAE over input-matched ordinary ridge. Broad D high-priority SVR achieved .6282 overall/.6705 High MAE, similar to the previous weighted ridge (.6282/.6649). Read the full table in [analysis progress](06-data-analysis-and-experiment-history.md) before another comparison. Possible later work includes target-centered kernel ridge and alternative boosting losses; no result for either is claimed here.

The requested synthetic-data regression follow-up completed in `results/05-score-training-augmentation/20261102T153249814079Z/`. Small B linear/ridge used real-only, duplicate-augmented and locally interpolated training data, with original nested splits and real-only evaluation. Ridge high-score MAE improved .9329 to .7783, but overall MAE worsened .5883 to .5972 and lower-score MAE worsened. Duplication alone explained much of the high-score gain. No eligible Low neighbors existed under the fixed constraints; generated examples were High only. Read [the analysis record](06-data-analysis-and-experiment-history.md) before deciding whether that trade-off suits the research goal. Next: compare the saved trade-offs and define acceptable high-score and overall errors before any further model selection; collect independent real responses for confirmation.

The separate three-class experiment completed in `results/09-three-group-classification/20261102T151940669629Z/`. Read `research/07-classification-experiments-and-methods.md` and its results before rerunning: class counts are 6/74/17, Broad D forest High recall averages 76.5% but High precision only 38.7%, and Low detection is weak. These are study-defined score bands, not clinical categories. No deployment model has been established.

Fixed-interaction linear/ridge comparison also completed in `analysis/outputs/interaction-experiments/20261102T145944836445Z/`. Overall MAE changes were tiny; linear interactions worsened high-score MAE. Read the updated analysis record before proposing more models. The current results do not demonstrate a reliable high-score warning system.

The high-score-priority ridge follow-up also completed in `results/04-high-score-weighting/20261102T144716191460Z/`. It reduced primary high-score MAE from .933 to .665, while increasing overall MAE from .588 to .628 and worsening lower-score errors. Recall at the descriptive >=4 boundary remains low (25.9%). Review [the analysis record](06-data-analysis-and-experiment-history.md) for this trade-off before further training or deployment decisions.

The original study run and a separate exploratory XGBoost follow-up are complete. Review [the updated analysis record](06-data-analysis-and-experiment-history.md#model-experiments-completed-2-november-2026) before starting another run. The checklists below preserve the earlier handoff; their pending-run statements are historical.

- Original run: `results/01-score-prediction-baselines/20261102T083420352990Z/`.
- XGBoost run: `results/02-xgboost-score-prediction/20261102T093101705609Z/`.
- XGBoost runner: `experiments/02-compare-xgboost-score-prediction.py`; configuration: `experiments/02-compare-xgboost-score-prediction-settings.json`.
- Small B ridge had lower average MAE than Small B XGBoost on both outcomes. Both struggled with extreme scores.

Next: interpret the completed comparison and its limitations before choosing a final research model or planning another experiment.

## Historical checklist: 29 October 2026

**Archive only.** Everything below records the plan before the first training run. Its unchecked boxes and pending statuses describe that date, not outstanding tasks today. The original run and many follow-ups have since completed. Use the latest status above and [the current handoff](09-current-project-handoff.md); do not execute the archived commands as an automatic next step.

## Historical position before the first run

At that time, we had 97 real student responses, prepared scores and initial SPSS analyses, but had not yet trained models. This was superseded by the completed runs recorded above.

The aim is to estimate current burnout symptoms and test whether GenAI habits improve predictions beyond the selected study conditions. The survey cannot establish causes or predict future burnout without later measurements.

## Archived first-run instructions

The following instructions applied to the October handoff, when preparation was complete and no real-data model run existed. They are retained for provenance, not current execution.

1. Check `results/01-score-prediction-baselines/` for a run added since this handoff. If a manifest says `complete`, inspect its results before starting another run. A `failed` or `running` manifest is not proof of completed results.
2. From the repository root, run the checks below. The last check completed five tests successfully; `pip check` reported no broken requirements.
3. If checks pass and no completed study run exists, run the full comparison with the final command below.
4. Read the new run's `manifest.json`, `results.md`, and `paired-comparisons.csv`. Continue with Steps 4 and 5 here.

```powershell
.\.venv\Scripts\python.exe experiments/01-compare-score-prediction-baselines.py --check-only
.\.venv\Scripts\python.exe experiments/test_01_score_prediction_workflow.py
.\.venv\Scripts\python.exe -m pip check

# Full research run, after the checks above pass:
.\.venv\Scripts\python.exe experiments/01-compare-score-prediction-baselines.py
```

If the environment is missing, recreate it using [the analysis instructions](08-score-prediction-experiments-and-methods.md#run-the-prediction-experiment) and `experiments/dependencies-pinned.txt`. The source hashes in the configuration deliberately stop a run if the working dataset changes. Investigate a mismatch; do not simply replace the expected hash to bypass the check.

## Files the next agent needs

| File | Purpose |
|---|---|
| [experiment-config.json](../experiments/01-compare-score-prediction-baselines-settings.json) | Fixed inputs, targets, model families, seeds, tuning grids, and evaluation policy |
| [01-compare-score-prediction-baselines.py](../experiments/01-compare-score-prediction-baselines.py) and [test_01_score_prediction_workflow.py](../experiments/test_01_score_prediction_workflow.py) | Complete workflow and software checks |
| [Analysis guide](08-score-prediction-experiments-and-methods.md) | Environment setup, commands, output meanings, and limitations |
| [Model-readiness report](../results/00-model-readiness-check.json) | Verified source hashes and the three reconstructed indicators |
| [Prediction experiment](04-original-prediction-experiment-plan.md) and [model review](05-original-model-selection-review.md) | Research design and reasons for the model choices |

The study run evaluates both burnout targets automatically. Step 4 asks you to review the secondary-target results, not run the same experiment a second time. Software-test records under `tmp/` are artificial fixtures and must never be reported as study results.

## Data issue already handled

The current SAV has three missing `ai_use_summaries` indicators, despite the older saved report recording no missing numeric values. Original Q9 answers are present and exactly match the raw CSV. The training loader reconstructs those three indicators in memory: two Selected and one Not selected.

This is a direct recode, not estimated survey answers. Do not drop the students, overwrite the SAV, rerun the older preparation script, or repeat repairs manually. The loader checks the missing count and known values and records the reconstruction. Both target scores passed formula checks.

## Compute: local first, Kaggle if needed

The user reports access to Kaggle with two GPUs of about 15 GB VRAM each. This is an available option for later experiments; no Kaggle notebook or upload has been prepared or tested.

The current scikit-learn linear, ridge, and Random Forest workflow runs on CPU. It does not use GPUs, so continue locally for the first comparison. GPU availability is not a reason to change the model families or add synthetic records before establishing the real-data results.

Two 15 GB GPUs have separate memory pools. A model does not automatically get one 30 GB memory pool; using both requires software that supports distributing work or model state across devices.

If a later experiment needs Kaggle:

1. Choose the GPU-dependent experiment for a research reason and record it separately, such as a pretrained tabular model or a generator comparison.
2. Prepare a private notebook and compatible dependencies. Recreate the repository layout under a writable working folder so the existing root-relative paths work; keep configuration and source hashes with the run.
3. Check permission and platform privacy settings before transferring participant-level data. The current consent limits access to the researcher developing the model; this note does not authorize a public dataset or notebook.
4. Verify the actual accelerator allocation and whether the chosen library can use one or both GPUs. Preserve training-only preprocessing and generation, shared splits, real-student evaluation, and the full run manifest.

Keep the real-data baseline separate from any later augmentation or new-model results. Moving computers must not silently change the experiment settings. CPU/GPU results may differ numerically; record package versions and device details.

## First experiment at a glance

| Choice | Proposed starting point |
|---|---|
| Dataset | `data/03-prepared-student-burnout-data.sav`, all 97 students |
| Main target | `burnout_score`, the 12-item BAT score |
| Inputs | Small A/B: selected conditions without/with selected GenAI questions. Broad C/D: all suitable background and condition questions without/with all GenAI questions |
| Comparison | Small A/B: linear regression, ridge, and a small Random Forest. Broad C/D: ridge only. Shared mean and median baselines |
| Evaluation | Five-fold cross-validation repeated five times; preprocessing and tuning inside training groups |
| Main error measure | MAE: average absolute error in burnout-score points |

Ridge is the preferred starting candidate, not a proven winner. The small and broad comparisons are included in the work scope. Keep Q20 as a separate possible outcome and exclude all BAT-derived predictors. The implementation choices are recorded in the configuration; document later changes as separate experiments.

The [experiment document](04-original-prediction-experiment-plan.md) lists the exact inputs and evaluation details. The [model review](05-original-model-selection-review.md) explains the recommendations and literature.

## 1. Record the experiment settings

Status: settings recorded before training in `experiments/01-compare-score-prediction-baselines-settings.json`. No clinical usefulness threshold is available; interpret gains descriptively.

- [x] Define the small A/B and broad C/D input sets and their model comparisons in the experiment document.
- [x] Choose category references, unseen-category handling, and the prediction-range policy.
- [x] Fix random seeds, small tuning grids, and how to summarize uncertainty.
- [x] Record lower paired MAE as numerical improvement; leave practical usefulness unresolved rather than inventing a cutoff.
- [x] Save the settings in `experiments/01-compare-score-prediction-baselines-settings.json`.

Done when: the configuration fully describes the first experiment before we examine prediction results. The configuration now exists; changes after seeing results must be recorded as later experiments.

## 2. Build the training workflow

Historical October status: workflow complete, full study run pending at that time. That run has since completed. Real-data validation reconstructed three missing AI-summary indicators from verified original answers in memory; the source SAV is unchanged.

- [x] Set up and record the Python dependencies needed to read SAV files and train models.
- [x] Load the working dataset, verify columns and scores, and explicitly reconstruct three derived indicators from original selections checked against the CSV.
- [x] Build training-only preprocessing for numeric and category inputs.
- [x] Implement the agreed models, shared outer splits, and inner tuning.
- [x] Save the workflow as `experiments/01-compare-score-prediction-baselines.py`, with a documented run command.

Done when: checks confirm that no BAT items or BAT-derived scores enter the predictors, training and evaluation students stay separate, and someone else can rerun the workflow.

If algorithm selection is part of the final training procedure, include that selection inside the inner validation step when evaluating the selected procedure.

## 3. Run the real-data comparison

Status: not started.

- [ ] Run all four input sets with identical outer evaluation groups; use ridge only for Broad C/D.
- [ ] Save predictions made for students excluded from training.
- [ ] Report MAE, RMSE, and R-squared, including paired differences for Small A/B and Broad C/D, plus small-versus-broad ridge comparisons.
- [ ] Plot predicted against measured scores and inspect large errors.

Done when: `analysis/outputs/` contains reproducible prediction tables, error summaries, and plots. Record the configuration and software versions with the results. Keep existing SPSS output intact.

No generated students belong in this first run. We need this result to judge whether augmentation helps later.

## 4. Review the evidence

Status: not started.

- [ ] Check whether learned models improve on the constant-score baselines.
- [ ] Check whether GenAI inputs help in both the small and broad comparisons, and whether the broader questionnaire improves ridge predictions.
- [ ] Inspect stability, influential cases, and errors for higher burnout scores.
- [ ] Review the `burnout_score_23` results generated automatically by the same run as a secondary check.

Done when: we can explain what improves prediction, what remains uncertain, and whether conclusions change with the secondary score. Repeated folds share students; their spread is not automatically a confidence interval.

Prefer a simpler model when performance is similar. Report honestly if no model beats the baseline or if GenAI inputs do not help.

## 5. Write the results and choose follow-up work

Status: not started.

Update [analysis progress](06-data-analysis-and-experiment-history.md) with the actual model results and limitations. Write the methods and results from saved outputs rather than memory. Mark completed tasks here and record any changes to the experiment.

After reviewing the real-data results, decide whether to test augmentation as a separate experiment. Fit any generator only on training students, including inside inner validation; evaluate on untouched real students. Synthetic records do not increase the participant count or belong in the survey reliability and correlation analyses.

A demo comes after evaluation. Claims about future burnout or advice that reduces burnout need additional evidence.

## Archived next step from October

The October next step was the readiness check followed by the first full run. Both were subsequently completed. For current work, read the latest status at the top of this file and `research/09-current-project-handoff.md`; no rerun is requested by this archived checklist.
