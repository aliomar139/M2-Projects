# Student burnout and GenAI research

> **Current status (18 November 2026):** many exploratory modelling comparisons are complete and the selected classifier is the eight-input Random Forest. Read [the current project handoff](docs/handoff.md) first, then the [synthetic generation example](classification/README.md#how-one-synthetic-profile-is-created).

Start here for the project overview. Use [work-plan.md](work-plan.md) for the task checklist.

Updated: 18 November 2026. Reading time: about 3 minutes.

## Where we are

We have 97 student responses. Data preparation, SPSS analyses and many model comparisons are complete. The selected eight-input Random Forest procedure averaged **87.1% High recall and 34.7% precision** in repeated real-student cross-validation. A final classifier is saved locally; its fit used all 97 real students and no synthetic training rows. The earlier CV metrics are not an independent evaluation of this final artifact.

Our question is: do students' GenAI habits help us estimate their current burnout symptoms, beyond what we can learn from their study conditions?

The survey measures everything at one time. It cannot tell us who will develop burnout later or prove that AI use causes burnout.

| Stage | Status |
|---|---|
| Create the 43-question survey and collect responses | Done; this modelling phase uses the existing 97 respondents |
| Prepare data and calculate both burnout scores | Done |
| Check score consistency, describe responses, and examine correlations | Done; detailed results are in the SPSS review |
| Train models and test prediction errors | Completed comparisons recorded in the handoff and progress log |
| Save the selected classifier | Done locally; model and metadata are ignored by Git |
| Write the final paper/presentation and consider a demo | Research results documented; final publication/demo completion is not established |

## What to do next

Read [the handoff](docs/handoff.md) and [current classification documentation](classification/README.md) before proposing work. Keep the selected model and recorded results. No experiment is currently running; agree on a specific next task before retraining, deleting outputs or changing models. The older checklist in [the work plan](work-plan.md) is explicitly historical.

## Which file should I read?

| If you want to... | Open this |
|---|---|
| Understand current models and possible next work | [Project handoff](docs/handoff.md) and [classification results](classification/README.md) |
| See completed analyses, formulas, and variable codes | [SPSS analysis review](docs/analysis-progress.md) |
| Understand the study design and limits | [Study specification](docs/study-design.md) |
| Find survey questions or the Google Forms script | [Active questionnaire](survey/questionnaire.md) |
| Return after a break or hand work to someone | [Project handoff](docs/handoff.md) |

The [BAT source questionnaire](survey/bat-source.md) preserves the instrument wording. It is a reference, not a progress report.

## Which data file should I use?

Use [`data/prepared/burnout-data.sav`](data/prepared/burnout-data.sav) for the next analysis. It contains 97 rows and 66 variables. The older saved report recorded no missing numeric values. The new model-readiness check found three missing AI-summary indicators and reconstructs them from original answers verified against the CSV, without changing the SAV file. See [the analysis guide](analysis/README.md#implementation-choices).

The primary target is `burnout_score`, calculated from 12 selected BAT items. The secondary target is `burnout_score_23`, which gives equal weight to the four full-core dimensions. Both scores are ready. Higher values on their 1 to 5 scale mean more frequent symptoms.

Keep all 97 students. Of these, 87 answered Yes to enrollment in Lebanon and 10 answered No. The researcher identified the No group as Lebanese students studying abroad; Q1 alone does not establish this.

See the [data folder guide](data/README.md) before running older scripts. The preparation syntax starts from an older file and writes a separate rebuild. That rebuild still needs the two documented corrections.

## Folder map

```text
ResearchBurnout/
  README.md                    Start here
  work-plan.md                 Task order and progress checklist
  docs/                        Plans, progress, and handoff
  survey/                      Active questions and BAT sources
  data/
    raw/                       Original response exports
    prepared/burnout-data.sav   Current working dataset
  analysis/
    scripts/                   SPSS preparation and Python data checker
    checks/                    Saved verification reports
    outputs/                   Saved SPSS tables and charts
  references/                  Literature search records
  archive/                     Older checkpoints, survey, and plans
```

Names use lowercase words separated by hyphens. Current work stays outside `archive/`; raw responses stay separate from prepared data.

The [data guide](data/README.md) explains which dataset to use. The [analysis guide](analysis/README.md) explains scripts and outputs. Literature records in `references/` help locate papers; verify the papers before citing their findings.

Next: open [the experiment run instructions](analysis/README.md#run-the-prediction-experiment).
