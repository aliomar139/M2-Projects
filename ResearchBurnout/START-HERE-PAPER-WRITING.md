# Start here: research paper writing

Updated **19 November 2026**, Asia/Beirut. This file prepares a new chat to write the paper from the completed research. It is a writing handoff, not a request to restart modelling.

## Copy this into the next chat

> Read START-HERE-PAPER-WRITING.md, the current README and the validation report. We will write the paper on Overleaf in IEEE format, one section at a time. Use the student-burnout and explainable-AI papers in ExplainableAI_Student_Burnout_Papers/ as the domain and methodological basis. Organize that material in the style of my doctor's papers in KassemDanachPapers/md/, giving his approach priority for structure, argument flow and presentation. Use our verified study facts and results throughout. Apply the i-have-adhd, research-paper-writing, no-ai-slop and humanizer skills for understandable English. First inspect suitable papers from both collections, explain how they inform our work, and propose an outline. Then draft only our current section as LaTeX ready for Overleaf. Mark missing facts and citations clearly. Explain choices simply, one point at a time. Don't restart modelling or invent results, XAI analyses, citations, recruitment details or ethics approval. Include the workload-only baseline and unsuccessful comparisons honestly.

If the next chat has no workspace access, attach this file first. Supply the linked report and supporting files when needed; don't assume their contents are available merely because paths appear here.

## Confirmed writing preferences

| Item | User's instruction |
|---|---|
| Writing platform | Overleaf |
| Format | IEEE; the exact venue/template variant and page limit still need confirmation |
| Reference approach | Student-burnout/XAI papers supply the domain basis. The doctor's papers guide organization, argument flow, and terminology. Base all study claims on the verified methods and results. |
| Manuscript voice | Use clear, impersonal academic prose. Name the study, model, or procedure as the subject. Keep a single main point per paragraph, define technical terms where needed, and connect comparisons to the results they support. |
| Collaboration | Work section by section, revising the current section with the user before advancing |
| Assistant explanations | Simple language, short paragraphs and a clear next action; explain technical terms when needed |

These preferences supersede the earlier generic suggestion to start immediately with Methods. Begin by learning the doctor's paper structures and proposing an outline that fits this study. The user can select the first section; if no section is specified, start with Introduction. Methods can still be drafted earlier if the user asks.

## Combine the two reference collections

The user wants domain material organized in the professor's style. Use the collections together for each section:

| Source | Role in our paper |
|---|---|
| `KassemDanachPapers/` | Main guide to section organization, paragraph sequence, explanation of design choices, technical detail and presentation of comparisons |
| `ExplainableAI_Student_Burnout_Papers/` | Domain background and methodological guidance: burnout measurement, predictors, validation, interpretation and explainable-AI reporting |
| Our study records and verified results | What we actually measured, implemented and found; the basis for every claim about our study |

When the collections suggest different ways to organize material, favor the professor's pattern where it fits our study and the IEEE venue. Explain any change needed for scientific accuracy or template requirements. The domain papers help determine what needs to be addressed; the professor's papers guide how we arrange and explain it. Write original prose grounded in the cited sources and our own evidence.

Start the domain search with [the student-burnout/XAI paper index](ExplainableAI_Student_Burnout_Papers/PAPERS_INDEX.md). PDFs are currently in `ExplainableAI_Student_Burnout_Papers/pdfs/`; use Markdown versions if the user adds them. Downloads/conversions may still be in progress, so inspect the actual files and don't claim to have reviewed a paper from its index entry alone. The domain papers were not read in full while preparing this handoff.

For relevant domain papers, record these five items before using them:

1. Population, measured outcome, instrument and label/cutoff construction. Distinguish burnout from adjacent stress, depression and well-being outcomes.
2. Predictor sources and possible overlap with the outcome, including leakage risks.
3. Training, tuning and evaluation design, including whether validation used genuinely new participants.
4. Any explanation method and how the authors assessed or interpreted its explanations.
5. Metrics, limitations and verified publication/citation details, including whether the source is peer reviewed or a preprint.

Use those observations to choose relevant literature and describe our methods clearly. Keep differences in populations, labels and metrics visible when comparing studies. Check original paper contents and publication records before treating index descriptions or a file named "verified" as evidence.

### What we can currently say about XAI

The new literature collection does not establish that our own study performed explainable-AI analyses. Existing records describe feature-selection rankings and prediction-error diagnostics; they do not establish completed SHAP or LIME experiments. Check actual outputs before making a more specific claim. Don't rename those diagnostics as validated XAI results or present earlier planned explainability work as completed.

If the chosen paper scope needs an additional explanation analysis, identify that as a separate proposed task for the user. The current writing task does not authorize new experiments. Literature can inform the background and limitations without changing what our study has already done.

## Required writing skills and clear English

Use all four skills requested by the user when available. Read their instructions; if a new chat cannot access the skill files, follow the concrete guidance here and state that the files weren't loaded.

| Skill | Job |
|---|---|
| `i-have-adhd` | Make discussion easy to act on: state the current section, explain one point at a time, use short paragraphs, define jargon and give one next action. Keep visible lists to five items where practical. |
| `research-paper-writing` | Plan each section, keep one main message per paragraph, connect claims to evidence and review the draft from a skeptical reader's perspective. |
| `no-ai-slop` | Edit out filler, inflated claims, vague wording and tangled sentences while preserving the intended meaning and the writer's voice. |
| `humanizer` | Review rhythm, repetition, stock phrasing and unnecessary formatting; make the prose read naturally without changing facts or technical meaning. |

On this machine, the skill files are under `C:/Users/user/.agents/skills/` for `i-have-adhd`, `no-ai-slop` and `humanizer`, and `C:/Users/user/.codex/skills/research-paper-writing/SKILL.md` for the academic-writing skill. Each named agent skill has its own `SKILL.md` in its directory.

Draft clear academic English, explain essential technical terms at first use and prefer familiar words when they are precise. Preserve uncertainty, citations and numerical values during editing. Natural prose does not require invented anecdotes, casual language or stronger conclusions. Keep mathematical notation and necessary methodological detail.

For each section, plan the evidence and structure, draft the LaTeX, then apply the two editing skills and recheck the claims. Put brief plain-English explanations outside the manuscript text. Keep drafting notes, paragraph-role labels and editorial comments out of the final Overleaf section. Formatting and scientific accuracy take precedence over stylistic changes that would alter meaning.

## Read these five files first

All links are relative to this project root.

| Order | File | Why it matters |
|---|---|---|
| 1 | [README.md](README.md) | Current project goal, results, structure and commands |
| 2 | [Latest validation report](results/25-random-forest-validation-report.md) | Main verified model comparisons, chance test, uncertainty and limits |
| 3 | [Current project handoff](research/09-current-project-handoff.md) | Scoring formulas, inputs, decisions and historical context |
| 4 | [Analysis and experiment history](research/06-data-analysis-and-experiment-history.md) | SPSS results, regression findings and unsuccessful experiments |
| 5 | [Student questionnaire](research/02-student-survey-questionnaire.md) | Exact questions, response options and consent wording |

Older plans sometimes say training has not begun, propose different score bands, or point to old directories. Those statements are historical. Use current reports, configurations and this handoff for the present state.

## Current state and writing goal

Data preparation, SPSS analyses, many modelling comparisons and the latest validation are complete enough to start an **exploratory paper**. A manuscript and final presentation have not been established as complete. Further model searches are not a prerequisite for writing.

The study asks whether students' GenAI habits help estimate **current burnout symptoms beyond study conditions alone**. Keep that question visible even when discussing the later High-symptom classification experiments.

Possible working title: **Student Burnout, Study Conditions and GenAI Use: An Exploratory Prediction Study**. This is a draft title. Overleaf and IEEE format are confirmed; the exact venue, page limit and final scope remain undecided.

A defensible paper story is that the study compared current-symptom prediction approaches on a small survey sample, examined their trade-offs, and tested a selected warning procedure against simple baselines and shuffled labels. The eight-input Random Forest exceeded the shuffled-label evaluations, but did not demonstrate a warning advantage over workload alone. The baseline's observed advantage remains uncertain. This is not evidence that AI causes burnout, that AI inputs add a proven warning benefit, or that a clinical screening system is ready.

Keep numerical-score prediction and High-symptom warnings as distinct tasks. Decide how much regression belongs in the main paper versus supplementary material after agreeing on the paper's scope; don't silently drop it or compare regression error with classifier recall.

## Use the doctor's papers as the main structural reference

Start with [the local paper index](KassemDanachPapers/PAPERS_INDEX.md), then read a small, relevant selection from `KassemDanachPapers/md/`. The collection is the user's chosen main reference for how to organize and present the work. Combine those structural patterns with the domain-methodology observations from the burnout/XAI collection.

An initial inspection of the following papers' headings and openings identified useful examples. This was not a full review of the collection; read the relevant sections before relying on their paragraph structure or technical content.

| Markdown filename in `KassemDanachPapers/md/` | What to study |
|---|---|
| `Advanced Optimization in E-Commerce Logistics - Combining Matheuristics With Random Forests for Hub Location Efficiency.md` | IEEE Access presentation: Introduction split into Context, Challenges, Contributions and Paper Structure; explicit problem/scope, experimental framework and performance evaluation |
| `Towards Accurate Fake News Detection - Evaluating Machine Learning Approaches and Feature Selection Strategies.md` | ML comparison structure: literature review; data collection, standardization, classifiers, feature selection and metrics; results grouped by model families and selection approaches |
| `Machine Learning for Smart Grid Stability - Enhancing Reliability in Renewable Energy Integration.md` | Background, aims, research questions and contributions; separate preprocessing, models, tuning, training/evaluation and trade-off analysis |
| `An Explainable Data-Driven Optimization Framework for Industrial Predictive Maintenance Scheduling.md` | Separation of data/problem context, labels/targets, predictive modelling and uncertainty; adapt only the parts relevant to our completed study |

For each section we write, inspect the corresponding section in two or more suitable professor papers and identify its paragraph roles: for example, context, problem, gap, objective, evidence or limitation. Read the relevant burnout/XAI papers for that section's domain content. Explain briefly which sources guide the content and which professor-paper patterns guide its organization, then use that mapping to draft our section.

Base the organization and presentation strongly on these examples while writing original, study-specific prose. Our study is an exploratory survey/model comparison; don't invent an optimization formulation, algorithm, module, hypothesis test, causal design or successful result merely because a reference paper contains one. Cite the doctor's work where it supports a relevant scholarly claim, with verified bibliographic details; structural inspiration alone does not make every paper a required citation.

Markdown conversion can misorder headings, tables or equations. Check the matching PDF when exact organization, notation or layout matters. Some inspected examples use other journals' formats; borrow their reasoning and presentation choices while following the chosen IEEE template's actual requirements.

## Overleaf and section-by-section workflow

1. Read suitable papers from both collections and propose a short paper story plus an IEEE-suitable outline, with the professor's organization as the primary guide.
2. For the current section only, provide a mini-outline and a short source mapping: the domain methods/content being used, the professor's structural pattern and our supporting evidence. Keep commentary separate from manuscript prose.
3. Draft that section as paste-ready LaTeX with appropriate section/subsection commands and stable labels, references and citation keys. Save a Markdown reading copy alongside it with the same filename stem. Keep both versions in sync during revisions, including citations and any placeholders. Reuse existing terminology and notation across sections.
4. Apply the requested writing/editing skills, recheck factual meaning and list only that section's unresolved facts, evidence needs and citation placeholders. Revise the section with the user before moving on.
5. Maintain a small record of completed/current/next sections and agreed terminology so another turn does not restart the discussion or rewrite settled material unnecessarily.

Use the user's selected IEEE Overleaf template when available. Until its exact venue and conference/journal variant are known, keep section content portable; don't assume a particular class option, author block or page limit. Don't manually imitate section numbering from an extracted PDF. Don't claim LaTeX was compiled or an Overleaf project was edited unless that actually happened.

When supplying cited text, provide verified BibTeX entries or clearly marked citation placeholders alongside the current section. Don't invent sources to make LaTeX appear complete. Save Abstract and final Conclusion for after the substantive sections settle; the reference-led outline determines how the other sections are grouped and ordered.

## Study facts for Methods

| Item | Supported information |
|---|---|
| Design | Cross-sectional survey: one measurement occasion, no later burnout outcome |
| Sample | 97 real respondents; the prepared SAV has 97 rows and 66 variables |
| Location item | 87 answered Yes to enrollment in Lebanon; 10 answered No |
| Inclusion decision | The researcher identified the No group as Lebanese students studying abroad and retained them. The design record dates the change from the original location exclusion rule to 28 October 2026, after collection. Q1 alone does not establish nationality or overseas enrollment. |
| Questionnaire | 20 non-BAT questions followed by 23 BAT-S core items, Q1–Q43 |

Use [the study-design record](research/01-study-goals-and-design.md) for the inclusion change and wording adaptations, but treat its old modelling plans as historical. The record notes short explanations added to selected BAT words; report those adaptations accurately.

### Data and scoring

Working data: [data/03-prepared-student-burnout-data.sav](data/03-prepared-student-burnout-data.sav). Original CSV: [data/01-original-student-survey.csv](data/01-original-student-survey.csv). Read [data preparation and corrections](research/13-dataset-preparation-and-corrections.md) before describing cleaning.

The loader reconstructs three missing `ai_use_summaries` indicators from original multi-select answers verified against the raw CSV. It does this in memory without changing the SAV. This is exact reconstruction, not statistical imputation. Earlier saved checks describe an earlier checking state; don't repeat their blanket no-missing-values claim without this qualification.

BAT answers range from 1 to 5, with higher values meaning more frequent symptoms. No BAT items use reverse scoring here. The primary `burnout_score` uses these 12 items:

| Dimension | Items |
|---|---|
| Exhaustion | BAT21, BAT23, BAT24 |
| Mental distance | BAT29, BAT31, BAT33 |
| Cognitive impairment | BAT34, BAT37, BAT38 |
| Emotional impairment | BAT39, BAT40, BAT43 |

Average the three items within each dimension, then average the four dimension means. The secondary `burnout_score_23` uses all 23 core items, again averaging the four dimension means equally. It is **not** a simple mean of 23 items because the dimensions have different item counts.

The current binary target is **High: primary score >=4**, with 17 students, versus **Below-high: score <4**, with 80 students. These are study-defined groups, not validated clinical diagnoses; Below-high does not mean no symptoms or no risk. Historical three-group classification used Low [1,2), Middle [2,4), High [4,5], with counts 6/74/17. Don't substitute earlier proposed cutoffs into the final experiments.

### Completed SPSS work

Reliability, descriptives, Explore outputs and exploratory correlations are documented. Total-item Cronbach's alpha was .900 for the 12 selected items and .944 for all 23 items. Alpha measures consistency, not clinical validity, prediction accuracy or proof of one underlying dimension. The full-item alpha is not exactly the reliability of the dimension-weighted secondary score.

Verify exact descriptive/correlation values in the analysis history before copying them. They are same-sample exploratory associations, not causal effects or proof that a feature improves prediction. Don't present planned omega or factor analyses as completed.

## Experiments: what belongs in the paper

The scripts/settings in `experiments/` share numbers in a useful reading order, not an exact chronology. [The file catalog](research/12-file-renaming-catalog.csv) maps older names.

| Experiment group | What it tested | Reporting role |
|---|---|---|
| 00–04 | Preparation, baseline score regression, XGBoost, error diagnosis, high-score weighting | Establish the score-prediction problem and errors at the extremes |
| 05–08 | Regression augmentation, SVR/kernel methods, Ridge/SVR blend, input selection | Explain the score-prediction trade-offs and recorded blend choice |
| 09–14 | Three-group then binary classification, augmentation, RF tuning, voting, error analysis | Explain the move to High-symptom detection and false-warning cost |
| 15–22 | Question selection/removal, TabPFN/refinements, SVC, input combinations, Boruta | Group measured alternatives and unsuccessful attempts; avoid a long parameter-search diary |
| 23–25 | Final-fit export, synthetic-profile check, real-student baseline/chance validation | Distinguish the recorded model recipe, simulation and verified evaluation |

Some older PCA/PLS, interaction, mixed loss-tuning and other follow-up artifacts were deliberately deleted before the reorganization. Their documented findings remain in the history. Don't restore deleted experiments or claim their outputs were freshly reverified.

The recorded numerical-score research predictor is a fixed 50/50 weighted-Ridge/high-priority-SVR blend: overall MAE .6160 and High-score MAE .6422, in score points. It balances overall and High-score errors; it is not the lowest-error method under every objective. Its detailed historical run folder is absent here and no final trained blend was exported.

For the original GenAI question, inspect the existing matched input comparisons: Small A/B without/with selected AI inputs and Broad C/D without/with broader AI inputs. Don't infer incremental AI value from RF-versus-chance performance or the workload-only comparison, which changes both the model and its inputs. Don't invent a new experiment to fill the narrative.

## Latest verified classification evidence

The selected Small B RF uses **workload, sleep category, study-hours category, financial strain, university support, AI frequency, AI dependence and AI offloading**. Sleep/study codes are categories, not literal hours. BAT items, BAT-derived dimensions/scores, timestamps and Q20 continuation intention are excluded as predictors.

| Procedure | Recall | Precision | High detected /17 | False warnings /80 | Balanced accuracy |
|---|---:|---:|---:|---:|---:|
| Selected eight-input RF procedure | 87.1% | 34.7% | 14.8 | 28.0 | 76.0% |
| Eight-input RF without augmentation | 84.7% | 32.7% | 14.4 | 29.6 | 73.9% |
| Workload-only logistic baseline | 94.1% | 36.4% | 16.0 | 28.0 | 79.6% |
| Random, same within-fold warning count | 44.6% | 17.7% | 7.58 | 35.22 | 50.3% |
| Warn everyone | 100.0% | 17.5% | 17.0 | 80.0 | 50.0% |

The no-warning baseline misses all 17 High students, with zero false warnings and 82.5% ordinary accuracy. This shows why ordinary accuracy alone is unsuitable. RF's 87.1% figure is **recall**, not accuracy. Counts above average five repetitions of the same 97 people; fractional counts are not a literal single confusion matrix or extra participants.

RF F2 is .667848, ROC AUC .808971 and average precision .526861. Workload-only F2 is .714286, ROC AUC .823971 and average precision .423095. Workload alone has the better observed warning rule, while RF has higher average precision. Don't claim either improves every measure or that the workload model's superiority is established.

### Evaluation and selection

Five stratified outer folds were repeated with five fixed seeds; four inner folds selected settings within each outer training group. All learned preprocessing, class weighting, augmentation and threshold tuning stayed inside training. Only excluded real students supplied evaluation predictions.

RF candidates used 100 trees, depth 2/3, minimum leaf 5/10, normalized relative High weights 1/2/4, augmentation ratios 0/.5/1 and thresholds from 0 to 1 in .05 steps. Inner selection maximized F2, then precision, recall, higher threshold and lower augmentation, retaining stable grid order for remaining ties. Settings can vary across folds. The workload baseline used fixed logistic C=1 with training-only standardization and inner-selected weight/threshold. Check the actual settings/scripts before drafting exact details.

The separate recorded final all-data recipe is depth 3, leaf 10, High weight 2, threshold .35, seed 271828 and **zero augmentation**. Its original trained binary/metadata remain missing. The local [recipe/schema record](results/23-recorded-random-forest-recipe-and-schema.json) is not a model. CV evaluates a procedure, not an independent test of a model fitted on all 97 students. The measured score boundary 4 and the model's .35 warning threshold are different quantities; model outputs are uncalibrated.

### Chance and uncertainty checks

All **199** student-level label permutations reran the full RF procedure, including preprocessing, augmentation and inner selection. Each student's shuffled label stayed the same across repetitions; stratified folds were rebuilt consistently. The primary statistic was mean repetition balanced accuracy: real .760294, null mean .495704, null maximum .636103. None reached the real statistic, giving corrected p=(1+0)/(1+199)=.005.

This tests the fixed procedure under shuffled labels. It does **not** reproduce the complete historical search over models, features and human choices, prove external performance, establish clinical usefulness, or test RF superiority over workload.

The 2,000 bootstrap resamples kept each student's repeated predictions together and paired samples across models, with fixed observed class counts. RF's conditional 95% intervals are 70.6–100.0% recall, 27.9–42.7% precision and 66.4–83.8% balanced accuracy. RF-minus-workload intervals include zero for all three metrics. These intervals condition on existing fitted predictions and omit refitting, historical selection and external-population uncertainty; don't label them definitive deployment-performance intervals.

## Keep three synthetic-data facts separate

| Object | What happened | What it does not establish |
|---|---|---|
| Historical training augmentation | 2,720 synthetic profile instances across repeated training pools | 2,720 new independent students or one model trained on all of them |
| Recorded final RF fit | 97 real students, zero synthetic rows selected for that fit | An independent test of its final all-data performance |
| Separate synthetic inference check | 970 generated profiles, including 170 assumed High; 159/170 detected, giving 93.5% recall | 93.5% recall on new real students or an improvement over real-student CV |

The simulation's labels were inherited from same-class real parents already used in fitting. Synthetic people did not provide measured BAT scores. Put this check in a separate subsection or supplement; don't use it as the headline validation result. The selected RF procedure allowed augmentation during CV even though final all-data selection chose none.

## Evidence locations and file availability

| Need | Where to look |
|---|---|
| Main results and uncertainty | [Comparison CSV](results/25-model-comparison-summary.csv), [paired comparisons](results/25-paired-model-comparisons.csv), [conditional intervals](results/25-conditional-student-uncertainty-intervals.csv) and the validation report |
| Figures | [RF confusion matrix](results/25-random-forest-confusion-matrix.png), [warning trade-offs](results/25-detections-versus-false-warnings.png), [shuffled-label comparison](results/25-real-model-versus-shuffled-labels.png) |
| Exact current methods/code | [Classification methods](research/07-classification-experiments-and-methods.md), [regression methods](research/08-score-prediction-experiments-and-methods.md), numbered scripts/settings in `experiments/` |
| Original validation namespace | Local `results/99-original-workspace-and-verified-validation.zip`, entry `classification/validation-outputs/20261118T143652947217Z/` |
| Literature leads | [Literature CSV](research/14-literature-search-records.csv), [DBLP workbook](research/15-literature-dblp-records.xlsx), [professor's paper index](KassemDanachPapers/PAPERS_INDEX.md) and [burnout/XAI paper index](ExplainableAI_Student_Burnout_Papers/PAPERS_INDEX.md) |

The archive contains original source/configurations and verified records with their original names/hashes. The current renamed scripts have different source hashes; don't substitute them into original verification checks. Older experiment outputs that were missing before archiving remain missing. Readable results copies preserve the numbers, with a path-update note in the report.

The latest audit checked 5,000 fold records, 180,000 candidate choices, all 125 real-training synthetic pools, 25 selected real outer refits, one full real/one full null search replay, and independent null metrics/p-value calculation. It did not refit every null model. After cleanup, 25 software/layout checks passed and one renamed-code validation fold reproduced the original predictions, choices and synthetic profiles exactly. Software verification is not external population validation.

Private records and archives are local and Git-ignored. Don't promise public data/model availability, original-artifact recovery or an available trained classifier merely because a historical path appears in a document.

## Paper content and first deliverable

The outline should accommodate the study motivation/research question, relevant literature, study design and methodology, measured results, discussion/limitations, and conclusion. Follow the reference-led outline when deciding whether data and experimental setup need separate sections or whether Results and Discussion should be combined. Fit the structure to the final IEEE venue and page budget.

Methods must cover participants, instrument/scoring, preparation, inputs, models and evaluation. Results must use the real tables and include workload alone; group lower-priority trials in supplementary material where appropriate. Discussion must explain false warnings, uncertain added value, small sample, repeated exploration and the lack of external validation. Introduction/Related Work need checked original sources and restrained novelty claims.

Lead with observed counts, rates and score errors in the Introduction. Report the paired uncertainty intervals in Results and Discussion.

The next chat's first deliverable is a compact mapping of relevant burnout/XAI methods and the professor's structural patterns, followed by a proposed outline for our IEEE paper. Give the professor's approach priority for organization. Then work on one chosen section in Overleaf-ready LaTeX using all four requested skills. Write Abstract and finalize Conclusion after the main content is settled, then check every major claim against evidence.

Verify literature claims against original papers before adding citations. Local summaries, publication indexes and abstracts are discovery aids, not automatic support for a claim. The professor's collection is the primary structural reference, while the burnout/XAI collection supplies domain-methodology guidance. Select scientific citations from relevant, verified contents in either collection. Authorship and the manuscript author list still need confirmation.

## Missing information to confirm while writing

| Topic | What must be confirmed |
|---|---|
| Submission details | Overleaf and IEEE format are confirmed. Confirm the exact venue, conference/journal template variant, word/page limit and any provided Overleaf project/template; confirm manuscript language if needed. |
| Authors and declarations | Ali Omar and Abdallah Mestrah, both affiliated with Lebanese University. Confirm author contributions, funding, and conflicts of interest. |
| Recruitment | The researcher shared the survey primarily through WhatsApp with Lebanese undergraduate and graduate students known to the researcher and their peers across multiple universities. Eligibility was inferred from the recruitment context and self-reported answers. The analysis retained all 97 exported submissions as distinct responses, dated 4–18 October 2026. Add the institution names, fielding dates, and invitation count if available. |
| Ethics and consent | The researcher confirmed that the study was not submitted for formal ethics review. The opening survey pages explained the study and voluntary participation. Respondents consented by continuing, and the form did not request names or contact information. |
| Reporting boundaries | Planned versus exploratory decisions, any registration, data-retention/sharing permissions and what can actually be made available |

Use `[TO CONFIRM: ...]` placeholders where needed and continue drafting supported parts. Don't label the study preregistered, representative, clinically validated or ready for deployment without evidence.

## Constraints for the next chat

Use `i-have-adhd`, `research-paper-writing`, `no-ai-slop` and `humanizer` throughout section drafting and revision. Explain things simply: short paragraphs, at most five visible steps at a time, and one concrete next action. The user wants understandable academic English and practical help writing.

Preserve data, labels, existing results, the recorded model recipe and user-requested deletions. Don't rerun experiments, change thresholds, collect extra data, restore deleted work, reorganize files again, commit, push or submit a paper merely because this handoff mentions possible future work. Ask for missing facts when necessary, but don't stop progress on sections that can already be written accurately.

**First writing task: map relevant burnout/XAI methodology into the professor's preferred structure, propose our IEEE outline, then develop one section at a time in clear Overleaf-ready LaTeX.**
