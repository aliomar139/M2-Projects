# Research Project Handoff

## Project status

The 43-question Google Form has been generated, and the researcher reports that it works. Recruitment status has not been confirmed. Live survey: [open the live survey](https://docs.google.com/forms/d/e/1FAIpQLSdsdMvfQbvm2ZosBR7LbEGYFOx7o_d2kO3tYsoN6CmSoaG07A/viewform?usp=dialog). The web/browser tools in the prior chat could not inspect the live Google Form, so its live settings were not independently verified.

The [active questionnaire](lebanon-student-burnout-survey-questions.md) is the source of truth for the questions and Apps Script generator. The [study blueprint](research-study-blueprint-and-specification.md) records the methodology, score definitions, psychometric plan, feature constraints, and modeling metrics.

## Instrument and scoring

- 43 questions total: 20 non-BAT items plus all 23 core BAT-S items. The 10 secondary complaint items are omitted.
- Primary outcome: marked 12-item BAT-S short form, with three items per dimension and an equal-weight mean of the four dimension means.
- The 23-item core score is secondary. Risk tiers (<2.25, 2.25 to 3.40, >3.40) are project-defined exploratory bands, not published norms, empirical tertiles, validated Lebanese student cutoffs, or diagnostic thresholds.
- Estimated completion time: about 5 minutes; one fast pilot completion took about 3 minutes.
- Simple parenthetical definitions were added after ?procrastinate? and ?cynical?; response anchors remain 1 (Never) to 5 (Always).

## Consent, privacy, and deployment

- The consent text says participation is voluntary, takes about 5 minutes, requests no direct identifiers, and response access is limited to the researcher developing the model. Google Forms may process technical/submission metadata. Individual submissions cannot be located for withdrawal after submission.
- The Apps Script disables email collection and the one-response-per-user limit. This should allow responses without sign-in but may allow repeat submissions. Confirm both settings in the live form.
- Researcher/ethics contact fields were omitted at the user's request. No ethics approval status was provided; any applicable course or institutional requirements remain to be confirmed.
- Data-retention period has not been specified.
- Live form was not inspectable in the prior session. Confirm the participant-facing description and response settings directly in Google Forms before recruitment. Editing the embedded Apps Script does not update an already-created form; make any needed wording changes directly in Google Forms.

## Next steps

1. Confirm live form settings, participant-facing description, and any applicable course/institution requirements. Set a data-retention period.
2. Confirm whether recruitment has started. Do not change survey items after responses are collected.
3. Preserve an untouched response export and create a data dictionary. The form does not automatically end for an ineligible response; exclude No responses during cleaning.
4. Score the marked 12 BAT-S short-form items as the primary continuous outcome; calculate the 23-item core score as secondary. Treat risk tiers as exploratory.
5. Assess response distributions and reliability, then run leakage-safe regression. Evaluate classification only if class counts support it. These cross-sectional responses measure concurrent associations, not future burnout or dropout.

Legacy files in `old framework/data/` predate this instrument and contain no responses to the active BAT-S survey. Literature files are `PaperMetadata.csv` and `PaperMetadataDblp.xlsx`.
