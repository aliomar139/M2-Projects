# Study specification

Read [the README](../README.md) for progress. This file explains the study design.

Updated: 29 October 2026.

## What we are studying

We study current burnout symptoms, GenAI use, and study conditions among Lebanese university students studying in Lebanon or abroad.

The main prediction question is whether GenAI habits improve estimates of current burnout beyond study conditions alone. We can also examine whether answers tend to vary together. These associations do not tell us what causes burnout.

The survey collected all answers at one time. Future burnout and actual dropout would need later measurements.

## Who is included

The current export has 97 responses: 87 students answered Yes to enrollment at a university in Lebanon; 10 answered No. The researcher identified the No group as Lebanese students studying abroad.

On 28 October 2026, after data collection, the researcher changed the original location-based exclusion rule to retain both groups. Report this change in the methods. Q1 alone does not confirm nationality or overseas enrollment, and it does not identify public or private universities. Pooling the groups does not mean their study conditions are the same.

Keep the original responses and document any separate data-quality exclusions. The earlier goal of 300 to 500 responses was a planning target. Whether more recruitment is feasible and how much data the planned analysis needs remain open questions.

## What the survey measures

The [active questionnaire](../survey/questionnaire.md) has 43 questions:

- Q1 to Q20 cover student background, study conditions, GenAI use, routines, support, and thoughts about leaving or changing studies.
- Q21 to Q43 are the 23 core student Burnout Assessment Tool (BAT-S) items. The survey omits the 10 secondary complaint items.

Responses to BAT items range from 1 (Never) to 5 (Always). Higher scores mean more frequent symptoms; no BAT items in this survey use reverse scoring. The source questionnaire marks 12 items for the short form.

We retained the BAT item stems and anchors, with short explanations of selected words. Document those wording clarifications. The estimated completion time is about 5 minutes, based on one fast pilot completion of about 3 minutes.

## How we calculate burnout

| Score | Calculation | Role |
|---|---|---|
| `burnout_score` | Use the 12 selected items: calculate four dimension means, then average those means | Primary outcome |
| `burnout_score_23` | Use all 23 core items: calculate four dimension means, then average those means | Secondary outcome |

Both scores are complete in `data/prepared/burnout-data.sav`. See the [exact formulas](analysis-progress.md#2-burnout-scores-created).

The full-core score gives each dimension equal weight. A simple average of all 23 items would give extra weight to exhaustion because it has more items.

Earlier plans proposed Low below 2.25, Moderate from 2.25 to 3.40 inclusive, and High above 3.40. These are project-defined exploratory bands, with no validated diagnostic meaning for Lebanese students. The first experiment uses continuous scores and does not classify students into these bands.

## What the completed checks mean

The SPSS review records reliability, score distributions, correlations, and data checks. Cronbach's alpha measures how consistently items vary together. It does not prove that a scale is valid in Lebanon or that a prediction model works.

The earlier plan also proposed omega reliability estimates, confidence intervals, and possible factor analysis. These are not completed. Their methods and feasibility would need review for this sample. A high total alpha does not prove that all BAT items measure one dimension.

## What we plan to model

Follow [prediction-experiment.md](prediction-experiment.md) for the proposed first experiment: compare study-condition inputs with the same inputs plus GenAI questions. Start with a mean-score baseline, linear regression, and ridge regression.

Exclude timestamps, BAT items, and all BAT-derived scores from inputs. The proposed first experiment also leaves out enrollment location and continuation intention. Keep text answers and their numeric copies for checking, but use only one representation of each question in a model.

Keep encoding, scaling, and tuning inside the training data during evaluation. Report MAE and RMSE, with R-squared as a supporting measure. Explain uncertainty and the limits of internal validation. Do not treat repeated validation folds as independent datasets for Friedman/Nemenyi tests.

Earlier ideas included combined AI or infrastructure scores, tier classification, nonlinear models, and SHAP explanations. They are outside the proposed first experiment. The [historical blueprint](../archive/planning-notes/study-blueprint.md) keeps their formulas and conditions. Do not present them as completed or required work.

Continuation intention can be a separate concurrent research outcome; it does not measure actual later dropout. Any additional analysis needs a written purpose and should be reported separately.

## Consent and form settings

The [live survey](https://docs.google.com/forms/d/e/1FAIpQLSdsdMvfQbvm2ZosBR7LbEGYFOx7o_d2kO3tYsoN6CmSoaG07A/viewform?usp=dialog) exists, and the researcher reports that it works. This cleanup did not inspect its live settings.

Consent says participation is voluntary, asks for no direct identifiers, limits response access to the researcher developing the model, and explains that an individual submission cannot be located for withdrawal afterward. Google Forms may still process technical or submission metadata.

The saved generation script disables email collection and the one-response-per-user limit. Check the live form to confirm sign-in and response settings. This setup may allow repeat submissions. Editing the saved script does not update an existing form.

Researcher and ethics contact fields were omitted by project preference. Confirm applicable course or institutional requirements, a data-retention period, and whether recruitment continues. Preserve the wording used for collected responses; record any necessary later changes.

## Literature and reporting

`references/papers.csv` and `references/papers-dblp.xlsx` hold literature records. The historical blueprint includes paper summaries; verify the original papers before using those claims in the manuscript. This cleanup did not verify external sources.

Report recruitment, the change in the inclusion rule, scoring, missing-data handling, and any departures from the plan. Describe results as exploratory given the small sample and lack of an independent validation sample.

A later demo could show an estimated current symptom score. Any support suggestions need separate review: this survey did not test interventions or measure whether advice helped students.

Next: settle the open experiment choices in [the model plan](prediction-experiment.md#7-decisions-to-record-before-training).
