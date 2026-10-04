# Research Project Handoff

## Current source of truth

The active study is the Lebanon student burnout study described in these documents:

- [Research study blueprint](research-study-blueprint-and-specification.md) — research questions, design, analysis plan, validation strategy, and project status.
- [Lebanon student burnout questionnaire](lebanon-student-burnout-survey-questions.md) — the current 44-item survey instrument.

Use these two files as the main framework and questionnaire. The previous framework and instruments have been retained under [`old framework`](old%20framework/README.md) for reference; they are archived and are not the active study materials.

## Study at a glance

The study examines academic burnout among university students in Lebanon, including Generative AI reliance, cognitive offloading, and local socioeconomic and infrastructure stressors. The planned analysis combines survey-based burnout measurement, statistical analysis, and explainable machine learning. The study blueprint is the authority for the detailed methodology and any unresolved design decisions.

## Data and project status

- The old `data.csv` and `data.xlsx` have been moved to [`old framework/data`](old%20framework/data/README.md). Treat them as legacy data unless they are reviewed and explicitly approved for use in the current study.
- `PaperMetadata.csv` and `dblp_predicting_student_burnout.xlsx` remain at the project root as literature reference files.
- The current questionnaire is a proposed instrument. Confirm its measures, consent language, and survey timing before deployment, then collect/export data for the current study.
- Do not report model performance or study findings until the current study data have been analyzed.

## Immediate next steps

1. Reconcile the measures and item scoring in the questionnaire with the blueprint, especially the burnout outcome definition and predictor set.
2. Review ethics/consent requirements and verify the questionnaire's stated anonymity and completion-time claims before publishing it.
3. Finalize and deploy the questionnaire.
4. Collect responses, document the data dictionary, and preserve a clean raw export.
5. Conduct exploratory and statistical analyses, then train and evaluate the planned models using leakage-safe validation.
6. Record actual results, limitations, and decisions in the study report.
