# Research Project Handoff

## Current source of truth

- [Research study blueprint](research-study-blueprint-and-specification.md) defines the cross-sectional study, student BAT/BAT-C scoring, analysis plan, and project status.
- [Lebanon student burnout questionnaire](lebanon-student-burnout-survey-questions.md) is the active 69-item questionnaire and includes the Google Forms script.

The questionnaire contains 33 v2 study/context questions, two v2 persistence/motivation questions, one Lebanon enrollment eligibility item, and all 33 items from the supplied student BAT questionnaire. The BAT includes 23 core items and 10 secondary complaint items. Use the 23-item core mean as the continuous primary outcome; report its four dimensions and the two secondary complaint dimensions separately. External published thresholds do not validate cutoffs for Lebanese students; neither the earlier 2.50/3.60 nor v2 2.25/3.40 bands should be presented as published BAT thresholds.

## Data and status

- `old framework/data/data.csv` and `data.xlsx` are legacy exports from the prior questionnaire; they do not contain responses to the active BAT-S instrument.
- `PaperMetadata.csv` and `PaperMetadataDblp.xlsx` are the literature reference files.
- The active questionnaire has not yet been deployed as this 69-item version. The official BAT site permits free use without author permission; retain its wording and response scale, cite the development paper, and review ethics requirements, consent/privacy wording, eligibility handling, and pilot completion time before launch.
- The form records eligibility, but the provided script does not automatically end the survey for ineligible responses; filter those responses during cleaning.
- Treat continuation intention as a concurrent secondary outcome. The study cannot claim to predict future burnout or actual dropout without later follow-up data.

## Next steps

1. Cite the BAT development paper and preserve the complete instrument wording and response scale. Check institutional ethics and deployment requirements.
2. Pilot the form with Lebanese university students, review comprehension and completion time, and refine only the study-created items; keep BAT-S item wording and response anchors as supplied.
3. Deploy the final form and preserve an untouched raw export with a data dictionary.
4. Assess item distributions and reliability, then analyze the continuous BAT-C core score and its dimensions.
5. If sample size and outcome variation support it, fit a small pre-specified set of regression models with leakage-safe validation and report uncertainty.
