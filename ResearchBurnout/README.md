# Student burnout and GenAI research

Start here for the project overview. Use [work-plan.md](work-plan.md) for the task checklist.

Updated: 29 October 2026. Reading time: about 3 minutes.

## Where we are

We have 97 student responses. Data preparation and the first SPSS analyses are complete. **We have not trained or tested a prediction model yet.**

Our question is: do students' GenAI habits help us estimate their current burnout symptoms, beyond what we can learn from their study conditions?

The survey measures everything at one time. It cannot tell us who will develop burnout later or prove that AI use causes burnout.

| Stage | Status |
|---|---|
| Create the 43-question survey and collect responses | Done for the current 97-response export; further recruitment status is unknown |
| Prepare data and calculate both burnout scores | Done |
| Check score consistency, describe responses, and examine correlations | Done; detailed results are in the SPSS review |
| Train models and test prediction errors | Not started |
| Write the final results and consider a demo | Later |

## What to do next

Follow [the work plan](work-plan.md). The next task is to record the first experiment settings in `analysis/experiment-config.json` before training.

The draft work plan includes the recommended median baseline and small Random Forest comparison. Record final settings before running models; no training has started.

## Which file should I read?

| If you want to... | Open this |
|---|---|
| Understand the next experiment | [Prediction experiment](docs/prediction-experiment.md) |
| See completed analyses, formulas, and variable codes | [SPSS analysis review](docs/analysis-progress.md) |
| Understand the study design and limits | [Study specification](docs/study-design.md) |
| Find survey questions or the Google Forms script | [Active questionnaire](survey/questionnaire.md) |
| Return after a break or hand work to someone | [Project handoff](docs/handoff.md) |

The [BAT source questionnaire](survey/bat-source.md) preserves the instrument wording. It is a reference, not a progress report.

## Which data file should I use?

Use [`data/prepared/burnout-data.sav`](data/prepared/burnout-data.sav) for the next analysis. It contains 97 rows and 66 variables. The saved check report shows no missing numeric values and no errors in the score or category checks.

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

Next: open [Step 1 of the work plan](work-plan.md#1-record-the-experiment-settings).
