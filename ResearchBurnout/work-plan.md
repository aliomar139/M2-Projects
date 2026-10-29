# Work plan

Start with Step 1: write down the first experiment settings before training.

Drafted: 29 October 2026. Reading time: about 3 minutes.

## Where we are

We have 97 real student responses. Data preparation, both burnout scores, and the initial SPSS analyses are complete. No prediction models have been trained or evaluated.

The aim is to estimate current burnout symptoms and test whether GenAI habits improve predictions beyond the selected study conditions. The survey cannot establish causes or predict future burnout without later measurements.

## First experiment at a glance

| Choice | Proposed starting point |
|---|---|
| Dataset | `data/prepared/burnout-data.sav`, all 97 students |
| Main target | `burnout_score`, the 12-item BAT score |
| Inputs | Set A: five study-condition questions. Set B: the same questions plus three GenAI questions |
| Comparison | Mean and median baselines, linear regression, ridge, and a small Random Forest regressor |
| Evaluation | Five-fold cross-validation repeated five times; preprocessing and tuning inside training groups |
| Main error measure | MAE: average absolute error in burnout-score points |

Ridge is the preferred starting candidate, not a proven winner. Random Forest and the median baseline are recommended additions to the earlier proposal. Record the final choices in Step 1.

The [experiment document](docs/prediction-experiment.md) lists the exact inputs and evaluation details. The [model review](docs/model-review.md) explains the recommendations and literature.

## 1. Record the experiment settings

Status: next task. Allow about 15 minutes for an initial review; resolving open choices may take longer.

- [ ] Specify targets, input sets, and compared models.
- [ ] Choose category references, unseen-category handling, and the prediction-range policy.
- [ ] Fix random seeds, small tuning grids, and how to summarize uncertainty.
- [ ] Define how we will judge useful improvement; do not invent a clinical cutoff.
- [ ] Save the settings in `analysis/experiment-config.json`.

Done when: the configuration fully describes the first experiment before we examine prediction results. The configuration file does not exist yet.

## 2. Build the training workflow

Status: not started.

- [ ] Set up and record the Python dependencies needed to read SAV files and train models.
- [ ] Load the corrected dataset and verify required columns, valid scores, and missing values.
- [ ] Build training-only preprocessing for numeric and category inputs.
- [ ] Implement the agreed models, shared outer splits, and inner tuning.
- [ ] Save the workflow as `analysis/scripts/train-models.py`, with a documented run command.

Done when: checks confirm that no BAT items or BAT-derived scores enter the predictors, training and evaluation students stay separate, and someone else can rerun the workflow.

If algorithm selection is part of the final training procedure, include that selection inside the inner validation step when evaluating the selected procedure.

## 3. Run the real-data comparison

Status: not started.

- [ ] Run both input sets with identical outer evaluation groups.
- [ ] Save predictions made for students excluded from training.
- [ ] Report MAE, RMSE, and R-squared, including paired differences between Sets A and B.
- [ ] Plot predicted against measured scores and inspect large errors.

Done when: `analysis/outputs/` contains reproducible prediction tables, error summaries, and plots. Record the configuration and software versions with the results. Keep existing SPSS output intact.

No generated students belong in this first run. We need this result to judge whether augmentation helps later.

## 4. Review the evidence

Status: not started.

- [ ] Check whether learned models improve on the constant-score baselines.
- [ ] Check whether GenAI inputs improve errors consistently across evaluation splits.
- [ ] Inspect stability, influential cases, and errors for higher burnout scores.
- [ ] Repeat the agreed workflow using `burnout_score_23` as a secondary check.

Done when: we can explain what improves prediction, what remains uncertain, and whether conclusions change with the secondary score. Repeated folds share students; their spread is not automatically a confidence interval.

Prefer a simpler model when performance is similar. Report honestly if no model beats the baseline or if GenAI inputs do not help.

## 5. Write the results and choose follow-up work

Status: not started.

Update [analysis progress](docs/analysis-progress.md) with the actual model results and limitations. Write the methods and results from saved outputs rather than memory. Mark completed tasks here and record any changes to the experiment.

After reviewing the real-data results, decide whether to test augmentation as a separate experiment. Fit any generator only on training students, including inside inner validation; evaluate on untouched real students. Synthetic records do not increase the participant count or belong in the survey reliability and correlation analyses.

A demo comes after evaluation. Claims about future burnout or advice that reduces burnout need additional evidence.

## Do this next

Open [the proposed input table](docs/prediction-experiment.md#2-compare-two-sets-of-inputs). Spend about 2 minutes checking that these are the answers we want the model to use.
