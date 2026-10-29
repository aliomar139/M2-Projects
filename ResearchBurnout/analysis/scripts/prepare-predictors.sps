* Earlier preparation workflow: writes a separate rebuilt file, not the corrected working dataset.
* Update CD for your checkout. The two documented corrections still need to be applied to a rebuild.
* Run on the saved project dataset; save results to a separate file.
CD 'C:/Users/user/Desktop/M2-Porjects/ResearchBurnout'.
GET FILE='archive/data/burnout-before-corrections.sav'.

RECODE major
 ('STEM (Engineering, Computer Science, Math, Physical Sciences)'=1)
 ('Health Sciences / Medicine / Nursing / Pharmacy'=2)
 ('Business / Economics / Finance'=3)
 ('Humanities, Social Sciences, or Law'=4)
 ('Arts & Design'=5) INTO major_code.
VALUE LABELS major_code
 1 'STEM' 2 'Health Sciences / Medicine / Nursing / Pharmacy'
 3 'Business / Economics / Finance'
 4 'Humanities, Social Sciences, or Law' 5 'Arts & Design'.

* Match GPA category names, avoiding differences in dash characters.
COMPUTE gpa_code=$SYSMIS.
IF INDEX(LTRIM(GPA),'Academic Warning')=1 gpa_code=1.
IF INDEX(LTRIM(GPA),'Satisfactory')=1 gpa_code=2.
IF INDEX(LTRIM(GPA),'Good')=1 gpa_code=3.
IF INDEX(LTRIM(GPA),'Excellent')=1 gpa_code=4.
VALUE LABELS gpa_code 1 'Academic Warning / Passing'
 2 'Satisfactory' 3 'Good' 4 'Excellent'.

RECODE electricity
 ('Less than 2 hours daily / Minimal impact'=1)
 ('2 to 5 hours daily'=2) ('5 to 8 hours daily'=3)
 ('More than 8 hours daily (Severe disruption)'=4)
 INTO electricity_code.
VALUE LABELS electricity_code
 1 'Less than 2 hours daily / Minimal impact'
 2 '2 to 5 hours daily' 3 '5 to 8 hours daily'
 4 'More than 8 hours daily (Severe disruption)'.

RECODE study_hours ('Less than 5 hours'=1) ('5 to 10 hours'=2)
 ('11 to 20 hours'=3) ('More than 20 hours'=4) INTO study_hours_code.
VALUE LABELS study_hours_code 1 'Less than 5 hours' 2 '5 to 10 hours'
 3 '11 to 20 hours' 4 'More than 20 hours'.

RECODE sleep_duration ('Less than 5 hours'=1) ('5 to 6 hours'=2)
 ('7 to 8 hours'=3) ('More than 8 hours'=4) INTO sleep_duration_code.
VALUE LABELS sleep_duration_code 1 'Less than 5 hours' 2 '5 to 6 hours'
 3 '7 to 8 hours' 4 'More than 8 hours'.

* Q9 permits multiple selections: one indicator for each use case.
COMPUTE ai_use_concepts=(INDEX(ai_use_cases,'Concept explanation & brainstorming')>0).
COMPUTE ai_use_writing=(INDEX(ai_use_cases,'Essay writing, grammar polishing, or drafting')>0).
COMPUTE ai_use_coding=(INDEX(ai_use_cases,'Coding, debugging, or technical problem solving')>0).
COMPUTE ai_use_summaries=(INDEX(ai_use_cases,'Summarizing articles / lecture slides')>0).
COMPUTE ai_use_solutions=(INDEX(ai_use_cases,'Direct solution generation for assignments/homework')>0).
VALUE LABELS ai_use_concepts ai_use_writing ai_use_coding ai_use_summaries
 ai_use_solutions 0 'Not selected' 1 'Selected'.

VARIABLE LABELS major_code 'Major / field of study'
 gpa_code 'Self-reported GPA category'
 electricity_code 'Daily electricity disruption category'
 study_hours_code 'Weekly independent study hours category'
 sleep_duration_code 'Nightly sleep duration category'
 ai_use_concepts 'AI: concept explanation and brainstorming'
 ai_use_writing 'AI: writing, grammar polishing or drafting'
 ai_use_coding 'AI: coding, debugging or technical problem solving'
 ai_use_summaries 'AI: summarizing articles or lecture slides'
 ai_use_solutions 'AI: direct assignment or homework solutions'.

VALUE LABELS enrolled_lebanon 0 'No' 1 'Yes'.
VALUE LABELS academic_level_code
 1 'Freshman / First Year' 2 'Sophomore / Second Year'
 3 'Junior / Third Year' 4 'Senior / Fourth Year +'
 5 "Master's / Postgraduate".
VARIABLE LEVEL enrolled_lebanon major_code ai_use_concepts ai_use_writing
 ai_use_coding ai_use_summaries ai_use_solutions (NOMINAL).
VARIABLE LEVEL academic_level_code gpa_code electricity_code
 study_hours_code sleep_duration_code (ORDINAL).
FORMATS enrolled_lebanon academic_level_code major_code gpa_code
 electricity_code study_hours_code sleep_duration_code ai_use_concepts
 ai_use_writing ai_use_coding ai_use_summaries ai_use_solutions (F1.0).
EXECUTE.

SAVE OUTFILE='data/prepared/burnout-data-rebuilt.sav'
 /COMPRESSED.

* Review counts and original-to-new category mappings; no inferential tests.
FREQUENCIES VARIABLES=enrolled_lebanon academic_level_code major_code gpa_code
 electricity_code study_hours_code sleep_duration_code ai_use_concepts
 ai_use_writing ai_use_coding ai_use_summaries ai_use_solutions.
CROSSTABS /TABLES=major BY major_code /CELLS=COUNT.
CROSSTABS /TABLES=GPA BY gpa_code /CELLS=COUNT.
CROSSTABS /TABLES=electricity BY electricity_code /CELLS=COUNT.
CROSSTABS /TABLES=study_hours BY study_hours_code /CELLS=COUNT.
CROSSTABS /TABLES=sleep_duration BY sleep_duration_code /CELLS=COUNT.
