# Research Project Handoff

## Current source of truth

- [Research study blueprint](research-study-blueprint-and-specification.md) defines the cross-sectional study, student BAT-S scoring, analysis plan, and project status.
- [Lebanon student burnout questionnaire](lebanon-student-burnout-survey-questions.md) is the active 43-item questionnaire and includes the Google Forms script.

The questionnaire contains 20 non-BAT items and all 23 BAT-S core items; 10 secondary complaint items are omitted. The primary target uses the 12 starred short-form items (three per dimension), scored as an equal-weight mean of four subscale means. The 23-item core index is secondary. Requested tiers (<2.25, 2.25 to 3.40, >3.40) are project-defined exploratory bands, not published norms, empirical tertiles, validated Lebanese cutoffs, or diagnostic thresholds.

## Data and status

- `old framework/data/data.csv` and `data.xlsx` are legacy exports from the prior questionnaire; they do not contain responses to the active BAT-S instrument.
- `PaperMetadata.csv` and `PaperMetadataDblp.xlsx` are the literature reference files.
- The active questionnaire has not yet been deployed as this 43-question version. The supplied BAT source permits free use without author permission; retain its wording and response scale, cite the development paper, and review ethics requirements, consent/privacy wording, eligibility handling, and pilot completion time before launch.
- The form records eligibility, but the provided script does not automatically end the survey for ineligible responses; filter those responses during cleaning.
- Treat continuation intention as a concurrent secondary outcome. The study cannot claim to predict future burnout or actual dropout without later follow-up data.

## Next steps

1. Cite the BAT development paper and preserve the complete instrument wording and response scale. Check institutional ethics and deployment requirements.
2. Pilot the form with Lebanese university students, review comprehension and completion time, and refine only the study-created items; keep BAT-S item wording and response anchors as supplied.
3. Deploy the final form and preserve an untouched raw export with a data dictionary.
4. Assess item distributions and reliability, then analyze the continuous 12-item BAT-S index (with 23-item core as secondary) and its dimensions.
5. If sample size and outcome variation support it, fit a small pre-specified set of regression models with leakage-safe validation and report uncertainty.
