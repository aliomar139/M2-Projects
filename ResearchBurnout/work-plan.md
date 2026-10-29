# Work plan

Resume at Step 3: run the prepared real-data experiment. Steps 1 and 2 are complete.

Updated: 29 October 2026. Reading time: about 5 minutes.

## Where we are

We have 97 real student responses. Data preparation, both burnout scores, and the initial SPSS analyses are complete. No prediction models have been trained or evaluated.

The aim is to estimate current burnout symptoms and test whether GenAI habits improve predictions beyond the selected study conditions. The survey cannot establish causes or predict future burnout without later measurements.

## Next agent: start here

Preparation is complete. Do not rebuild the experiment or select new input sets before running the agreed comparison. No completed real-data model-run folder was present at this handoff.

1. Check `analysis/outputs/model-runs/` for a run added since this handoff. If a manifest says `complete`, inspect its results before starting another run. A `failed` or `running` manifest is not proof of completed results.
2. From the repository root, run the checks below. The last check completed five tests successfully; `pip check` reported no broken requirements.
3. If checks pass and no completed study run exists, run the full comparison with the final command below.
4. Read the new run's `manifest.json`, `results.md`, and `paired-comparisons.csv`. Continue with Steps 4 and 5 here.

```powershell
.\.venv\Scripts\python.exe analysis/scripts/train-models.py --check-only
.\.venv\Scripts\python.exe analysis/scripts/test-training.py
.\.venv\Scripts\python.exe -m pip check

# Full research run, after the checks above pass:
.\.venv\Scripts\python.exe analysis/scripts/train-models.py
```

If the environment is missing, recreate it using [the analysis instructions](analysis/README.md#run-the-prediction-experiment) and `analysis/requirements-lock.txt`. The source hashes in the configuration deliberately stop a run if the working dataset changes. Investigate a mismatch; do not simply replace the expected hash to bypass the check.

## Files the next agent needs

| File | Purpose |
|---|---|
| [experiment-config.json](analysis/experiment-config.json) | Fixed inputs, targets, model families, seeds, tuning grids, and evaluation policy |
| [train-models.py](analysis/scripts/train-models.py) and [test-training.py](analysis/scripts/test-training.py) | Complete workflow and software checks |
| [Analysis guide](analysis/README.md) | Environment setup, commands, output meanings, and limitations |
| [Model-readiness report](analysis/checks/model-readiness.json) | Verified source hashes and the three reconstructed indicators |
| [Prediction experiment](docs/prediction-experiment.md) and [model review](docs/model-review.md) | Research design and reasons for the model choices |

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
| Dataset | `data/prepared/burnout-data.sav`, all 97 students |
| Main target | `burnout_score`, the 12-item BAT score |
| Inputs | Small A/B: selected conditions without/with selected GenAI questions. Broad C/D: all suitable background and condition questions without/with all GenAI questions |
| Comparison | Small A/B: linear regression, ridge, and a small Random Forest. Broad C/D: ridge only. Shared mean and median baselines |
| Evaluation | Five-fold cross-validation repeated five times; preprocessing and tuning inside training groups |
| Main error measure | MAE: average absolute error in burnout-score points |

Ridge is the preferred starting candidate, not a proven winner. The small and broad comparisons are included in the work scope. Keep Q20 as a separate possible outcome and exclude all BAT-derived predictors. The implementation choices are recorded in the configuration; document later changes as separate experiments.

The [experiment document](docs/prediction-experiment.md) lists the exact inputs and evaluation details. The [model review](docs/model-review.md) explains the recommendations and literature.

## 1. Record the experiment settings

Status: settings recorded before training in `analysis/experiment-config.json`. No clinical usefulness threshold is available; interpret gains descriptively.

- [x] Define the small A/B and broad C/D input sets and their model comparisons in the experiment document.
- [x] Choose category references, unseen-category handling, and the prediction-range policy.
- [x] Fix random seeds, small tuning grids, and how to summarize uncertainty.
- [x] Record lower paired MAE as numerical improvement; leave practical usefulness unresolved rather than inventing a cutoff.
- [x] Save the settings in `analysis/experiment-config.json`.

Done when: the configuration fully describes the first experiment before we examine prediction results. The configuration now exists; changes after seeing results must be recorded as later experiments.

## 2. Build the training workflow

Status: complete. Real-data validation passed after reconstructing three missing AI-summary indicators from verified original answers in memory. The source SAV is unchanged. Software checks cover the pipeline and reports; the full study run is still pending.

- [x] Set up and record the Python dependencies needed to read SAV files and train models.
- [x] Load the working dataset, verify columns and scores, and explicitly reconstruct three derived indicators from original selections checked against the CSV.
- [x] Build training-only preprocessing for numeric and category inputs.
- [x] Implement the agreed models, shared outer splits, and inner tuning.
- [x] Save the workflow as `analysis/scripts/train-models.py`, with a documented run command.

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

Update [analysis progress](docs/analysis-progress.md) with the actual model results and limitations. Write the methods and results from saved outputs rather than memory. Mark completed tasks here and record any changes to the experiment.

After reviewing the real-data results, decide whether to test augmentation as a separate experiment. Fit any generator only on training students, including inside inner validation; evaluate on untouched real students. Synthetic records do not increase the participant count or belong in the survey reliability and correlation analyses.

A demo comes after evaluation. Claims about future burnout or advice that reduces burnout need additional evidence.

## Do this next

Run the `--check-only` command in ?Next agent: start here,? then proceed to the full run if no completed run already exists.
