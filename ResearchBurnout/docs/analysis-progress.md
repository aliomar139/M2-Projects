# SPSS analysis review

Use this file for exact results and variable codes. For a short progress summary, open [the README](../README.md).

Analysis record: 28 October 2026. Language and navigation updated: 29 October 2026. Numerical results below are unchanged.

## Quick reading guide

Data preparation and the first analyses are complete. Both burnout scores are ready; no prediction model has been trained or evaluated.

| Need | Go to |
|---|---|
| Score formulas | [Section 2](#2-burnout-scores-created) |
| Reliability, averages, and correlations | [Section 3](#3-statistical-analyses-completed) |
| Question codes and labels | [Section 4](#4-preparing-the-non-bat-questions) |
| Corrections and saved data checks | [Section 7](#7-corrections-and-final-verification) |
| Proposed next experiment | [Model plan](prediction-experiment.md) |

Read one section at a time. You do not need every table to understand the next task.

## 1. Current status and files

We collected responses from **97 Lebanese university students** about GenAI use, study conditions, and burnout. The questionnaire contains 20 non-BAT questions and 23 Burnout Assessment Tool for Students (BAT-S) items.

**Data preparation and initial analyses are complete. The predictive model has not been fitted or evaluated yet.** The current data can support prediction of current burnout symptoms. Early warning of future burnout would require follow-up measurements, because all current answers were collected at the same time.

| File | Purpose |
|---|---|
| `data/prepared/burnout-data.sav` | **Current working dataset:** original responses, burnout scores, and numeric recodes |
| `analysis/outputs/descriptive-statistics.spv` | Shared output containing results and tables; continue saving results here |
| `archive/data/burnout-before-corrections.sav` | Earlier dataset retained as a backup |
| `archive/data/burnout-older-checkpoint.sav` | Older analysis checkpoint |
| `data/raw/survey-export-spss.csv` | Original response export used to verify answers |
| `analysis/scripts/prepare-predictors.sps` | Syntax that created the remaining numeric predictors and saved the prepared dataset |

The preparation syntax opens `archive/data/burnout-before-corrections.sav` and writes a separate `data/prepared/burnout-data-rebuilt.sav`. That rebuild still needs the two corrections documented in Section 7. Use the corrected `data/prepared/burnout-data.sav` for analysis.

All **97 respondents remain included**: 87 answered Yes to enrollment at a university in Lebanon and 10 answered No. The researcher identified the latter as Lebanese students studying abroad. Q1 records enrollment location, is not an exclusion rule, and does not identify public/private universities. Reviewed SPSS procedure notes showed no active filter, weighting, or split-file setting.

## 2. Burnout scores created

BAT responses run from **1 = Never** to **5 = Always**. Higher scores mean more frequent symptoms. We calculated two versions of burnout and kept them separate.

### Primary outcome: 12-item short form

Each dimension uses three selected items. The overall score averages the four dimension means.

| Variable | Dimension | Calculation |
|---|---|---|
| `exhaustion` | Exhaustion | `MEAN.3(BAT21, BAT23, BAT24)` |
| `mental_distance` | Disengagement from studies | `MEAN.3(BAT29, BAT31, BAT33)` |
| `cognitive_impairment` | Difficulties with attention and thinking | `MEAN.3(BAT34, BAT37, BAT38)` |
| `emotional_impairment` | Difficulties regulating emotional reactions | `MEAN.3(BAT39, BAT40, BAT43)` |
| `burnout_score` | Overall primary score | `MEAN.4(exhaustion, mental_distance, cognitive_impairment, emotional_impairment)` |

The saved scores were checked against these formulas. Because every dimension has three items, the overall score also equals the mean of the 12 selected items.

### Secondary outcome: full 23-item core

| Variable in the actual file | Items | Calculation |
|---|---|---|
| `exhaustion_23` | BAT21–BAT28: 8 items | `MEAN.8(BAT21 TO BAT28)` |
| `mental_distance_23` | BAT29–BAT33: 5 items | `MEAN.5(BAT29 TO BAT33)` |
| `congnitive_impairement_23` | BAT34–BAT38: 5 items | `MEAN.5(BAT34 TO BAT38)` |
| `emotional_impairment_23` | BAT39–BAT43: 5 items | `MEAN.5(BAT39 TO BAT43)` |
| `burnout_score_23` | Four full-core dimension means | `MEAN.4(exhaustion_23, mental_distance_23, congnitive_impairement_23, emotional_impairment_23)` |

**Naming detail:** `congnitive_impairement_23` is misspelled in the dataset. Its values are correct; use that exact name in syntax unless it is deliberately renamed.

In these formulas, `MEAN.3`, `MEAN.5`, and `MEAN.8` require all listed dimension items to be valid; `MEAN.4` requires all four dimension means. All ten calculated scores remain on the **1–5 scale**.

The secondary score gives each dimension equal weight. It is **not the simple mean of all 23 items**, which would give exhaustion more weight because it has eight items. The study plan names the 12-item score as primary and the 23-item score as secondary. Record any change before comparing models. Project-defined low/moderate/high bands are exploratory, not validated diagnostic thresholds for Lebanese students.

## 3. Statistical analyses completed

### Reliability: do the BAT items work consistently together?

We ran Cronbach's alpha for each dimension and both complete item sets, using the individual BAT items. The full-core analyses included Item Statistics, Item-Total Statistics, and Scale Statistics.

| Dimension or item set | Short-form items | Short-form alpha | Full-core items | Full-core alpha |
|---|---:|---:|---:|---:|
| Exhaustion | 3 | .781 | 8 | .909 |
| Mental distance | 3 | .733 | 5 | .820 |
| Cognitive impairment | 3 | .876 | 5 | .919 |
| Emotional impairment | 3 | .775 | 5 | .839 |
| All items together | 12 | .900 | 23 | .944 |

These results support internal consistency in this sample. **All items were retained.** Small increases in alpha after deleting an item were not used to alter the designated scales.

A corrected item–total correlation compares an item with the sum of the other items in the analyzed set, excluding itself. For the full-core dimensions, these correlations ranged from .562–.783 for exhaustion, .533–.677 for mental distance, .678–.861 for cognitive impairment, and .538–.725 for emotional impairment. Across all 23 items, the range was .382–.789.

Deleting BAT38 would change full-core cognitive alpha from .919 to .923; deleting BAT43 would change total 23-item alpha from .944 to .945. Neither small increase justified deletion. In the short form, deleting BAT43 would change emotional alpha from .775 to .797 and total alpha from .900 to .904; it was retained there too.

Alpha measures how consistently items vary together. It does not show prediction accuracy, prove validity, or prove that the four dimensions measure a single dimension. The 23-item alpha uses the individual items; it does not give the exact reliability of our score, which gives equal weight to each dimension.

### Descriptive statistics and Explore: how are scores distributed?

We produced frequencies and bar charts for BAT21–BAT43, descriptives for the short-form dimensions and overall score, and Explore output for both overall scores. Explore included descriptive statistics, histograms, stem-and-leaf plots, and boxplots.

| Short-form dimension | Mean | Standard deviation |
|---|---:|---:|
| Exhaustion | 3.430 | .934 |
| Mental distance | 2.986 | .908 |
| Cognitive impairment | 3.110 | 1.104 |
| Emotional impairment | 2.973 | .937 |

| Overall-score statistic | `burnout_score` | `burnout_score_23` |
|---|---:|---:|
| Valid N | 97 | 97 |
| Mean | 3.125 | 3.150 |
| Standard deviation | .795 | .765 |
| Median | 3.083 | 3.075 |
| Minimum | 1.417 | 1.444 |
| Maximum | 5.000 | 5.000 |
| Skewness | .176 | .288 |
| Excess kurtosis | −.164 | −.026 |

Both score distributions look roughly balanced, with a slightly longer tail toward higher scores. These summaries do not show an obvious need to transform the score. They do not replace formal distribution checks or later checks of regression errors. A score of 5 is valid; an extremes label in a plot is not a reason to exclude a student.

Scale Statistics in reliability output describe **item sums**, whereas our calculated score variables are **means on the 1–5 scale**. A mean near 3 is not a clinical diagnosis.

### Correlations: which individual questions are associated with burnout?

We ran exploratory Spearman correlations between the **primary `burnout_score`** and 11 non-BAT questions. Positive values mean that higher responses on that question tended to accompany higher burnout. These are separate associations, without adjustment for other predictors.

| Variable | Spearman rho | Two-tailed p |
|---|---:|---:|
| AI dependence | .377 | <.001 |
| AI offloading | .331 | <.001 |
| AI frequency | .220 | .030 |
| Perceived workload | .388 | <.001 |
| Academic stress | .367 | <.001 |
| Financial strain | .196 | .054 |
| University support | −.148 | .149 |
| Internet quality | −.059 | .564 |
| Avoidance/procrastination | .445 | <.001 |
| AI output verification | −.010 | .923 |
| Anxiety about AI accusations | .278 | .006 |

A Pearson correlation was also run for AI dependence and burnout: **r = .361, p < .001**. It agrees in direction with Spearman, but uses the same responses and is not independent confirmation.

The three-variable matrices also included:

| Predictor pair | Spearman rho | Two-tailed p |
|---|---:|---:|
| Workload and academic stress | .672 | <.001 |
| Financial strain and university support | .064 | .533 |
| Internet quality and avoidance | .112 | .277 |
| AI verification and AI anxiety | .416 | <.001 |

All saved correlations used 97 students and two-tailed tests, which check associations in either direction. SPSS used available pairs if values were missing. The output did not adjust for testing many associations or report confidence intervals. Avoidance had the strongest burnout correlation among the tested questions. Workload and stress were also closely related; check their overlap in a later model.

These results do not show causes or prediction accuracy. A p-value below .05 does not guarantee a useful model input, and a larger p-value does not prove an input is useless. The GenAI questions are separate items; we have not validated a combined AI scale.

## 4. Preparing the non-BAT questions

The first 20 questions describe different things, so we did not calculate one alpha across them. Their roles as model inputs or separate outcomes still need to be chosen.

For answers already stored as numbers, we added labels and corrected measurement settings. For text answers, we created numeric copies with labels. We kept every original text column. A label explains a number; a recode converts an answer into a number. Neither step tests a research question.

### Existing numeric questions

All the following are **Numeric, 0 decimals, Ordinal**. Their saved labels currently name the endpoints; values 2–4 are valid but have no display labels.

| Question | Variable | Label for 1 | Label for 5 |
|---|---|---|---|
| Q6 | `internet` | Very poor | Excellent |
| Q7 | `financial_strain` | No strain | Severe strain |
| Q8 | `ai_frequency` | Never | Daily |
| Q10 | `ai_dependence` | Strongly disagree | Strongly agree |
| Q11 | `ai_offloading` | Strongly disagree | Strongly agree |
| Q12 | `ai_verification` | Strongly disagree | Strongly agree |
| Q13 | `ai_anxiety` | Strongly disagree | Strongly agree |
| Q15 | `workload` | Strongly disagree | Strongly agree |
| Q17 | `academic_stress` | Strongly disagree | Strongly agree |
| Q18 | `avoidance` | Strongly disagree | Strongly agree |
| Q19 | `university_support` | Strongly disagree | Strongly agree |
| Q20 | `leave_intention` | Strongly disagree | Strongly agree |

The endpoints match the saved questionnaire. If the live form explicitly named options 2–4, add those exact labels later rather than inventing them. Their absence does not change calculations. Higher numbers represent more of each stated characteristic, including better internet and greater support where applicable.

### Text questions converted into numeric copies

Every new variable below is **Numeric, 0 decimals**, with labels matching these mappings.

| Original | New variable | Codes and labels | Measure |
|---|---|---|---|
| `eligible` | `enrolled_lebanon` | 0 = No; 1 = Yes | Nominal |
| `academic_level` | `academic_level_code` | 1 = Freshman / First Year; 2 = Sophomore / Second Year; 3 = Junior / Third Year; 4 = Senior / Fourth Year +; 5 = Master's / Postgraduate | Ordinal |
| `major` | `major_code` | 1 = STEM; 2 = Health Sciences / Medicine / Nursing / Pharmacy; 3 = Business / Economics / Finance; 4 = Humanities, Social Sciences, or Law; 5 = Arts & Design | Nominal |
| `GPA` | `gpa_code` | 1 = Academic Warning / Passing; 2 = Satisfactory; 3 = Good; 4 = Excellent | Ordinal |
| `electricity` | `electricity_code` | 1 = Less than 2 hours / Minimal impact; 2 = 2–5 hours; 3 = 5–8 hours; 4 = More than 8 hours / Severe disruption | Ordinal |
| `study_hours` | `study_hours_code` | 1 = Less than 5 hours; 2 = 5–10 hours; 3 = 11–20 hours; 4 = More than 20 hours per week | Ordinal |
| `sleep_duration` | `sleep_duration_code` | 1 = Less than 5 hours; 2 = 5–6 hours; 3 = 7–8 hours; 4 = More than 8 hours per night | Ordinal |

Nominal means categories have no numerical order: major 5 is not greater than major 1. Ordinal means categories have an order, but the gaps may differ. Study-hours code 3 means the 11 to 20 hour category, not three hours. The SPSS Ordinal setting does not choose how a regression model will use that variable.

### Q9: AI use cases

The export contains up to two selections per student in `ai_use_cases`. We created five separate indicators, each **Numeric, 0 decimals, Nominal**, with **0 = Not selected** and **1 = Selected**.

| New variable | Represents | Students selecting it |
|---|---|---:|
| `ai_use_concepts` | Concept explanation and brainstorming | 72 |
| `ai_use_writing` | Essay writing, grammar polishing, or drafting | 21 |
| `ai_use_coding` | Coding, debugging, or technical problem solving | 27 |
| `ai_use_summaries` | Summarizing articles or lecture slides | 37 |
| `ai_use_solutions` | Direct assignment/homework solutions | 16 |

21 students selected one use and 76 selected two. Counts overlap because two selections were allowed.

### BAT and score settings in Variable View

- **BAT21–BAT43:** Numeric, 0 decimals, Ordinal; 1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often, 5 = Always.
- **All ten calculated dimension and overall scores:** Numeric, 3 decimals, Scale, Values = None because decimal means are meaningful.
- **Original text columns and Timestamp:** retained unchanged. Use appropriate numeric copies for model preparation.

## 5. Sample description from frequency tables

Frequency analyses covered academic level, major, GPA, study hours, sleep, and electricity. The preparation syntax also requested frequencies and cross-tabulations to check recode mappings.

| Variable | Counts, out of 97 |
|---|---|
| Academic level | Freshman 8; Sophomore 21; Junior 12; Senior 13; Master's/Postgraduate 43 |
| Major | STEM 48; Health Sciences 19; Business 12; Humanities/Social Sciences/Law 16; Arts & Design 2 |
| GPA | Academic Warning/Passing 3; Satisfactory 25; Good 38; Excellent 31 |
| Study hours/week | Less than 5: 34; 5–10: 33; 11–20: 22; More than 20: 8 |
| Sleep hours/night | Less than 5: 12; 5–6: 50; 7–8: 35; More than 8: 0 |
| Electricity disruption hours/day | Less than 2: 65; 2–5: 25; 5–8: 3; More than 8: 4 |

These counts describe the 97 students in this sample. They do not describe all students. Some categories have very few students. If we combine categories for modeling, we need a clear reason based on their meaning.

## 6. What the checks establish

We checked reliability, score distributions, initial associations, and variable preparation. We have not completed regression, checks of regression errors, VIF/tolerance checks for input overlap, factor analysis, omega reliability estimates, or cross-validated predictions. Extra t-tests, ANOVA, or chi-square tests are not required before starting the planned prediction work.

## 7. Corrections and final verification

Two blanks were found in the earlier `burnout-before-corrections.sav` and carried into the first prepared file. The corrected working file was saved and checked again:

| Record | Variable | Correction and basis |
|---|---|---|
| Timestamp `2026/10/05 1:21:45 am EEST` (row 18 in the checked order) | `emotional_impairment` | Recalculated from BAT39, BAT40, BAT43: all three are 5, so the mean is 5 |
| Timestamp `2026/10/06 11:35:51 pm EEST` (row 65 in the checked order) | `internet` | Restored 3, matching the original CSV response |

Their cause is unknown. They were not missing survey answers. Use timestamps to identify these records if the row order changes.

The final saved-file check confirmed:

- **97 rows, 66 variables**, and no numeric system-missing values.
- All original numeric survey answers match the CSV.
- Every new category code matches its original text answer.
- Every AI-use indicator matches the student's selections.
- All ten dimension and overall scores match the intended calculations.
- Value labels, Nominal/Ordinal/Scale settings, and decimal formats match the plan above.
- Existing values differ from the earlier `burnout-before-corrections.sav` only in the two corrected cells; new variables were added separately.

The script `analysis/scripts/check-data.py` reads the SAV files and writes verification reports. It does not modify the dataset or the SPSS output.

## 8. Next step: define the first experiment

Follow [the model plan](prediction-experiment.md) for the proposed targets, inputs, encoding, and evaluation. Record its open decisions before training.

Keep the first model small because we have 97 students. Exclude BAT answers and BAT-derived scores from inputs. Use training data alone to fit preprocessing and choose tuning settings. Compare prediction errors with the training-mean baseline.

SPSS can support regression checks, while Python can support repeated cross-validation. Fit on the training students does not establish prediction accuracy.

## Terms used in this review

| Term | Plain meaning |
|---|---|
| Mean | Average |
| Standard deviation | How spread out scores are around the average |
| Correlation | How two answers tend to vary together; it does not establish cause |
| Cronbach's alpha | A measure of how consistently a group of items varies together |
| Predictor / outcome | Information used by a model / the value the model tries to estimate |

Next: open [the proposed input sets](prediction-experiment.md#2-compare-two-sets-of-inputs).
