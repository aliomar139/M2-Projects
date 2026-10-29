# Research Project Handoff

## Project status

Update on 2026-10-28: the local response export contains 97 submissions, and saved SPSS work includes reliability, descriptive, and correlation analyses. The researcher clarified that the 10 respondents who answered No to Question 1 are Lebanese students studying abroad and should be retained alongside the 87 who answered Yes. All 97 remain in the pooled cohort, subject to separately documented data-quality rules. This clarification supersedes the original location-based exclusion rule after data collection.

The target cohort is Lebanese university students studying in Lebanon or abroad. Question 1 records enrollment at a university in Lebanon; its answer is not an exclusion criterion. Nationality and overseas enrollment are based on the researcher's recruitment information, as the question itself does not establish them. University ownership/sector was not collected, so Question 1 cannot identify private-university students or establish equivalent study conditions between groups.

The 43-question Google Form has been generated, and the researcher reports that it works. Responses have been collected; whether further recruitment is ongoing has not been confirmed. Live survey: [open the live survey](https://docs.google.com/forms/d/e/1FAIpQLSdsdMvfQbvm2ZosBR7LbEGYFOx7o_d2kO3tYsoN6CmSoaG07A/viewform?usp=dialog). The web/browser tools in the prior chat could not inspect the live Google Form, so its live settings were not independently verified.

The [active questionnaire](lebanon-student-burnout-survey-questions.md) is the source of truth for the questions and Apps Script generator. The [study blueprint](research-study-blueprint-and-specification.md) records the methodology, score definitions, psychometric plan, feature constraints, and modeling metrics.

## Instrument and scoring

The saved analyses and exact results are documented in [SPSS_Analysis_Review.md](SPSS_Analysis_Review.md). The current output uses all 97 respondents and contains five alpha analyses, score descriptives, a histogram, one Pearson correlation, seven Spearman correlation procedures covering 11 burnout associations, and frequency summaries. All five alphas, score means/standard deviations, and the 12 burnout correlation coefficients (11 Spearman plus one Pearson) were independently reproduced from the local CSV. No adjusted regression or prediction model is present in the saved output. The next substantive step is to specify a small adjusted association model after finalizing coding and covariate roles.

- 43 questions total: 20 non-BAT items plus all 23 core BAT-S items. The 10 secondary complaint items are omitted.
- Primary outcome: marked 12-item BAT-S short form, with three items per dimension and an equal-weight mean of the four dimension means.
- The 23-item core score is secondary. The researcher reports completing `exhaustion_23 = MEAN.8(BAT21 TO BAT28)` and `mental_distance_23 = MEAN.5(BAT29, BAT30, BAT31, BAT32, BAT33)`. The local SAV file contains `exhaustion_23`, but not yet `mental_distance_23`; the latter may need saving from the working SPSS session. Full-core cognitive and emotional means and the equal-weight 23-item composite remain to be calculated.
- Risk tiers (<2.25, 2.25 to 3.40, >3.40) are project-defined exploratory bands, not published norms, empirical tertiles, validated Lebanese student cutoffs, or diagnostic thresholds.
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
2. Confirm whether further recruitment is ongoing. Do not change survey items after responses are collected.
3. Preserve an untouched response export and create a data dictionary. Retain both Yes and No responses to Question 1 in the pooled cohort. Preserve the enrollment-location response for sample description; apply any other data-quality exclusions separately and document them.
4. Preserve the marked 12 BAT-S short-form score as the primary continuous outcome. Finish the remaining full-core domain means (cognitive impairment: BAT34–BAT38; emotional impairment: BAT39–BAT43), then calculate the equal-weight mean of all four full-core domain means as the secondary 23-item score. Treat risk tiers as exploratory.
5. Assess response distributions and reliability, then run leakage-safe regression. Evaluate classification only if class counts support it. These cross-sectional responses measure concurrent associations, not future burnout or dropout.

Legacy files in `old framework/data/` predate this instrument and contain no responses to the active BAT-S survey. Literature files are `PaperMetadata.csv` and `PaperMetadataDblp.xlsx`.
