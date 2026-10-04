# Lebanon Student Burnout Survey Questionnaire

**Current instrument:** 69 items: all 33 non-BAT questions and both persistence questions from v2, one enrollment eligibility question, and all 33 items from the supplied student BAT questionnaire.
**Target cohort:** Undergraduate and graduate students enrolled at universities in Lebanon.
**Estimated completion time:** To be established by a pilot; all items are retained for now.
**Instrument note:** Supplied BAT item wording and 1 to 5 response anchors are retained. The 23 BAT-C core items form the primary continuous outcome; the 10 secondary complaint items are scored separately. Question codes outside the generation script support data management and analysis.

## Participant information and consent

> You are invited to take part in a study of student burnout, generative AI use, study habits, and study conditions in Lebanon. Participation is voluntary. The survey is designed not to request names or email addresses; the form platform may collect technical or submission metadata depending on its settings. You may stop before submitting. Data will be analyzed for academic research. For questions about the study or your rights as a participant, use the contact information supplied by the research team.

**Consent:** By choosing to continue, you confirm that you have read the information above and agree to participate. If you do not consent, do not submit the survey.

## Section A: Eligibility

### Question 1 (ELIGIBLE_LEBANON)

**Are you currently enrolled as a student at a university in Lebanon?**

*Response type: Required single choice*

- Yes
- No

## Section B: Socio-Demographics & Infrastructure Context (Questions 2-11)

*Captures baseline academic standing, discipline, and localized Lebanese environmental and infrastructure friction.*

---

### **Question 2 (DEM_LEVEL)**
* **Question Text:** What is your current university academic standing / level?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Freshman / First Year
  2. `[ ]` Sophomore / Second Year
  3. `[ ]` Junior / Third Year
  4. `[ ]` Senior / Fourth Year +
  5. `[ ]` Master's / Postgraduate

---

### **Question 3 (DEM_MAJOR)**
* **Question Text:** What is your primary major / field of study?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` STEM (Engineering, Computer Science, Math, Physical Sciences)
  2. `[ ]` Health Sciences / Medicine / Nursing / Pharmacy
  3. `[ ]` Business / Economics / Finance
  4. `[ ]` Humanities, Social Sciences, or Law
  5. `[ ]` Arts & Design

---

### **Question 4 (DEM_GPA)**
* **Question Text:** What is your current cumulative GPA range (self-reported)?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Excellent (3.5 – 4.0 / Above 85%)
  2. `[ ]` Good (3.0 – 3.49 / 75% – 84%)
  3. `[ ]` Satisfactory (2.5 – 2.99 / 68% – 74%)
  4. `[ ]` Academic Warning / Passing (Below 2.5 / Below 68%)

---

### **Question 5 (INF_ELEC)**
* **Question Text:** How many hours of electricity outages / generator disruptions do you experience daily that affect your study time?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Less than 2 hours daily / Minimal impact
  2. `[ ]` 2 to 5 hours daily
  3. `[ ]` 5 to 8 hours daily
  4. `[ ]` More than 8 hours daily (Severe disruption)

---

### **Question 6 (INF_NET)**
* **Question Text:** How would you rate the quality and reliability of your internet connection during study/assignment hours?
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:**
  * **1** = Very Poor (Frequent disconnections, unusable)
  * **2** = Poor
  * **3** = Moderate
  * **4** = Good
  * **5** = Excellent (Stable, high-speed connection)

---

### **Question 7 (INF_FIN)**
* **Question Text:** What level of financial strain do you feel regarding your university studies (tuition, textbooks, transportation, living expenses)?
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:**
  * **1** = No Strain (Financially comfortable)
  * **2** = Minor Strain
  * **3** = Moderate Strain
  * **4** = High Strain
  * **5** = Severe Financial Strain (Threatens tuition/essentials)

---

### **Question 8 (INF_COMM)**
* **Question Text:** What is your average daily round-trip commute time to university?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Live on campus / Dorms
  2. `[ ]` Under 30 minutes
  3. `[ ]` 30 to 60 minutes
  4. `[ ]` 1 to 2 hours
  5. `[ ]` More than 2 hours daily

---

### **Question 9 (INF_EMP)**
* **Question Text:** What is your current employment status alongside your university studies?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Full-time student (Not employed)
  2. `[ ]` Part-time job (Under 15 hours/week)
  3. `[ ]` Part-time job (16–30 hours/week)
  4. `[ ]` Full-time job (30+ hours/week)

---

### **Question 10 (DIG_TIME)**
* **Question Text:** On average, how many hours per day do you spend looking at digital screens for academic work?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Less than 3 hours
  2. `[ ]` 3 to 5 hours
  3. `[ ]` 6 to 8 hours
  4. `[ ]` More than 8 hours daily

---

### **Question 11 (DIG_FATIGUE)**
* **Question Text:** "I experience physical eye strain, headaches, or physical digital fatigue from prolonged study screens."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:**
  * **1** = Strongly Disagree
  * **2** = Disagree
  * **3** = Neutral
  * **4** = Agree
  * **5** = Strongly Agree

---

## Section C: Generative AI Reliance & Cognitive Offloading (Questions 12-21)

*Measures frequency, usage modes, cognitive offloading habits, verification behavior, and integrity anxiety when using AI tools (e.g., ChatGPT, Claude, Gemini, DeepSeek).*

---

### **Question 12 (AI_FREQ)**
* **Question Text:** How frequently do you use Generative AI tools (e.g., ChatGPT, Claude, Gemini, DeepSeek) for your academic work?
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:**
  * **1** = Never
  * **2** = Rarely (A few times per semester)
  * **3** = Monthly
  * **4** = Weekly
  * **5** = Daily

---

### **Question 13 (AI_USE)**
* **Question Text:** What are your primary use cases for Generative AI in coursework? (Select up to 2):
* **Question Type:** Checkboxes (Max 2 Selection Limit) — *Required*
* **Response Options:**
  1. `[ ]` Concept explanation & brainstorming
  2. `[ ]` Essay writing, grammar polishing, or drafting
  3. `[ ]` Coding, debugging, or technical problem solving
  4. `[ ]` Summarizing articles / lecture slides
  5. `[ ]` Direct solution generation for assignments/homework

---

### **Question 14 (AI_COG)**
* **Question Text:** "I feel unprepared or unable to complete my academic assignments without using AI tools."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 15 (AI_CRIT)**
* **Question Text:** "I rely on AI to generate ideas, structures, or answers rather than thinking through them on my own."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 16 (AI_DEL)**
* **Question Text:** "When faced with a difficult academic prompt, my first reaction is to copy-paste it into an AI tool before attempting it myself."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 17 (AI_VERIF)**
* **Question Text:** "I thoroughly verify and fact-check AI-generated outputs before incorporating them into my academic work."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 18 (AI_EXAM)**
* **Question Text:** "I use AI tools to generate study summaries, practice questions, or explanations when preparing for exams."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 19 (AI_TRUST)**
* **Question Text:** "I believe Generative AI outputs are almost always accurate and superior to my own work."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 20 (AI_EFF)**
* **Question Text:** "Using AI tools saves me significant time during assignment preparation."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 21 (AI_ANX)**
* **Question Text:** "I worry about getting accused of plagiarism or flagged for AI usage even when using AI legitimately."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

## Section D: Academic Routine, Coping & Social Support (Questions 22-34)

*Evaluates independent study habits, class attendance, submission latency, coping strategies, and social/institutional support buffers.*

---

### **Question 22 (HAB_STUDY)**
* **Question Text:** On average, how many hours per week do you spend on independent study outside of class?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Less than 5 hours
  2. `[ ]` 5 to 10 hours
  3. `[ ]` 11 to 20 hours
  4. `[ ]` More than 20 hours

---

### **Question 23 (HAB_ATT)**
* **Question Text:** How consistent is your class attendance?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Always attend (> 90%)
  2. `[ ]` Mostly attend (75%–90%)
  3. `[ ]` Occasional absence (50%–74%)
  4. `[ ]` Frequent absence (< 50%)

---

### **Question 24 (HAB_LAT)**
* **Question Text:** What is your typical assignment submission timing?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Well before the deadline
  2. `[ ]` Right at the deadline
  3. `[ ]` Frequently late / Request extensions

---

### **Question 25 (HAB_WORK)**
* **Question Text:** "My current academic workload feels heavy and overwhelming."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 26 (WELL_SLEEP)**
* **Question Text:** What is your average nightly sleep duration during the university semester?
* **Question Type:** Single Choice (Multiple Choice) — *Required*
* **Response Options:**
  1. `[ ]` Less than 5 hours
  2. `[ ]` 5 to 6 hours
  3. `[ ]` 7 to 8 hours
  4. `[ ]` More than 8 hours

---

### **Question 27 (WELL_STR)**
* **Question Text:** "In recent weeks, I have felt overwhelmed, irritable, or panicked due to academic demands."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 28 (COP_ACT_1)**
* **Question Text:** "When facing academic stress, I actively break tasks into steps and make a plan of action."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 29 (COP_ACT_2)**
* **Question Text:** "I talk to professors, advisors, or classmates when I struggle with difficult coursework."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 30 (COP_AVOID_1)**
* **Question Text:** "When academic pressure gets too high, I procrastinate or avoid thinking about my schoolwork."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 31 (COP_AVOID_2)**
* **Question Text:** "I use social media, gaming, or entertainment to distract myself from academic stress."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 32 (SUP_INST)**
* **Question Text:** "I feel supported by my university administration and instructors when facing academic difficulties."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 33 (SUP_PEER)**
* **Question Text:** "I have a strong peer/friend network at university that helps me cope with academic stress."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

### **Question 34 (SUP_FAM)**
* **Question Text:** "My family understands and supports my academic goals and workload demands."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

## Section E: Complete Burnout Assessment Tool for Students (BAT-S) (Questions 35-67)

**Instructions:** The following statements are related to your studies and how you experience them. State how often each statement applies to you.

**Response scale:** 1 = Never; 2 = Rarely; 3 = Sometimes; 4 = Often; 5 = Always.

### Exhaustion

**Question 35 (Q35_BAT_EXH_01)**  
Due to my studies, I feel mentally exhausted.

**Question 36 (Q36_BAT_EXH_02)**  
Everything I do for my studies requires a great deal of effort.

**Question 37 (Q37_BAT_EXH_03)**  
After a day working on my study, I find it hard to recover my energy.

**Question 38 (Q38_BAT_EXH_04)**  
While working on my studies, I feel physically exhausted.

**Question 39 (Q39_BAT_EXH_05)**  
When I get up in the morning, I lack the energy to get started with my studies.

**Question 40 (Q40_BAT_EXH_06)**  
I want to be active when I am working on my studies but somehow, I am unable to manage.

**Question 41 (Q41_BAT_EXH_07)**  
When I exert myself for my studies, I quickly get tired.

**Question 42 (Q42_BAT_EXH_08)**  
At the end of a day of working on my studies, I feel mentally exhausted and drained.

### Mental Distance

**Question 43 (Q43_BAT_MD_01)**  
I struggle to find any enthusiasm for my studies.

**Question 44 (Q44_BAT_MD_02)**  
When I am working on my studies, I do not think much about what I am doing, and I function on autopilot.

**Question 45 (Q45_BAT_MD_03)**  
I feel a strong aversion towards my studies.

**Question 46 (Q46_BAT_MD_04)**  
I feel indifferent about my studies.

**Question 47 (Q47_BAT_MD_05)**  
I’m cynical about the importance of my studies.

### Cognitive Impairment

**Question 48 (Q48_BAT_COG_01)**  
When I am working on my studies, I have trouble staying focused.

**Question 49 (Q49_BAT_COG_02)**  
When I am working on my studies, I struggle to think clearly.

**Question 50 (Q50_BAT_COG_03)**  
I am forgetful and distracted when I am working on my studies.

**Question 51 (Q51_BAT_COG_04)**  
When I am working on my studies, I have trouble concentrating.

**Question 52 (Q52_BAT_COG_05)**  
I make mistakes while working on my studies because I have my mind on other things.

### Emotional Impairment

**Question 53 (Q53_BAT_EMO_01)**  
I feel unable to control my emotions.

**Question 54 (Q54_BAT_EMO_02)**  
I do not recognize myself in the way I react emotionally.

**Question 55 (Q55_BAT_EMO_03)**  
I become irritable when things don’t go my way.

**Question 56 (Q56_BAT_EMO_04)**  
I get upset or sad without knowing why.

**Question 57 (Q57_BAT_EMO_05)**  
I may overreact unintentionally.

### Psychological Distress

**Question 58 (Q58_BAT_DIST_01)**  
I have trouble falling or staying asleep.

**Question 59 (Q59_BAT_DIST_02)**  
I tend to worry.

**Question 60 (Q60_BAT_DIST_03)**  
I feel tense and stressed.

**Question 61 (Q61_BAT_DIST_04)**  
I feel anxious and/or suffer from panic attacks.

**Question 62 (Q62_BAT_DIST_05)**  
Noise and crowds disturb me.

### Psychosomatic Complaints

**Question 63 (Q63_BAT_PSY_01)**  
I suffer from palpitations or chest pain.

**Question 64 (Q64_BAT_PSY_02)**  
I suffer from stomach and/or intestinal complaints.

**Question 65 (Q65_BAT_PSY_03)**  
I suffer from headaches.

**Question 66 (Q66_BAT_PSY_04)**  
I suffer from muscle pain, for example in the neck, shoulder or back.

**Question 67 (Q67_BAT_PSY_05)**  
I often get sick.

---

## Section F: Academic Persistence & Motivation (Questions 68-69)

### Question 68 (MOT_INTR)
* **Question Text:** "I am intrinsically interested in the subjects I am studying in my degree program."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

### Question 69 (MOT_TURNOVER)
* **Question Text:** "I have seriously considered taking a leave of absence, switching majors, or dropping out due to academic stress."
* **Question Type:** Linear Scale (1 to 5) — *Required*
* **Scale Anchors:** **1** (Strongly Disagree)  $\longrightarrow$  **5** (Strongly Agree)

---

## Scoring and analysis notes

- Primary outcome: mean of the 23 BAT-C core items, retained as continuous.
- Report the four BAT-C dimensions separately: exhaustion (8), mental distance (5), cognitive impairment (5), and emotional impairment (5).
- Score psychological distress (5) and psychosomatic complaints (5) separately; exclude these items from the core score.
- Exclude all BAT items from predictor features when BAT-C is the target. Analyze intrinsic interest and continuation intention separately.
- Do not use the 2.50/3.60 or v2 2.25/3.40 bands as published BAT cutoffs. External thresholds must identify the exact instrument version and reference population and remain exploratory.

## BAT source and use

The BAT may be used without author permission; preserve its wording and response scale and cite Schaufeli, W. B., Desart, S., and De Witte, H. (2020), "Burnout Assessment Tool (BAT): Development, Validity, and Reliability," *International Journal of Environmental Research and Public Health*, 17(24), 9495, [doi:10.3390/ijerph17249495](https://pmc.ncbi.nlm.nih.gov/articles/PMC7766078/). Supplied source: [Burnout_Assessment_Tool_English_Questionnaire.md](Burnout_Assessment_Tool_English_Questionnaire.md).

## Google Forms creation script

Creates 69 items. Eligibility answers are recorded for exclusion during data cleaning. Review participant information, platform privacy settings, and ethics requirements before deployment.

```javascript
function createLebanonStudentBurnoutSurvey() {
  var form = FormApp.create("Lebanon Student Burnout and GenAI Survey");
  
  form.setDescription("Voluntary academic study of student burnout, generative AI use, study habits, and study conditions in Lebanon. This form does not request names or email addresses; platform settings may collect technical or submission metadata. Review participant information before deployment.");
  form.setAllowResponseEdits(false);
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);

  function addScale(title, minLabel, maxLabel, helpText) {
    var item = form.addScaleItem();
    item.setTitle(title).setBounds(1, 5).setLabels(minLabel, maxLabel).setRequired(true);
    if (helpText) item.setHelpText(helpText);
    return item;
  }

  function addMC(title, choices, helpText) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(title).setChoiceValues(choices).setRequired(true);
    if (helpText) item.setHelpText(helpText);
    return item;
  }

  form.addPageBreakItem().setTitle("Section A: Eligibility");
  addMC("Are you currently enrolled as a student at a university in Lebanon?", ["Yes", "No"]);
  form.addPageBreakItem().setTitle("Section B: Socio-Demographics and Infrastructure");

  // === SECTION A: Demographics & Infrastructure ===
  addMC("2. Academic Standing / Level", ["Freshman / First Year", "Sophomore / Second Year", "Junior / Third Year", "Senior / Fourth Year +", "Master's / Postgraduate"]);
  addMC("3. Major / Field of Study", ["STEM (Engineering, Computer Science, Math, Physical Sciences)", "Health Sciences / Medicine / Nursing / Pharmacy", "Business / Economics / Finance", "Humanities, Social Sciences, or Law", "Arts & Design"]);
  addMC("4. Current Cumulative GPA Tier (Self-Reported)", ["Excellent (3.5 – 4.0 / Above 85%)", "Good (3.0 – 3.49 / 75% – 84%)", "Satisfactory (2.5 – 2.99 / 68% – 74%)", "Academic Warning / Passing (Below 2.5 / Below 68%)"]);
  addMC("5. Daily Electricity Outages / Generator Disruption", ["Less than 2 hours daily / Minimal impact", "2 to 5 hours daily", "5 to 8 hours daily", "More than 8 hours daily (Severe disruption)"]);
  addScale("6. Internet Quality & Reliability During Study Hours", "Very Poor (Unusable)", "Excellent (High Speed)", "Frequent disconnections vs stable connection");
  addScale("7. Perceived Financial Strain", "No Strain", "Severe Strain", "Financially comfortable vs severe strain affecting tuition/essentials");
  addMC("8. Daily Round-Trip Commute Time to University", ["Live on campus / Dorms", "Under 30 minutes", "30 to 60 minutes", "1 to 2 hours", "More than 2 hours daily"]);
  addMC("9. Employment Status", ["Full-time student (Not employed)", "Part-time job (Under 15 hours/week)", "Part-time job (16–30 hours/week)", "Full-time job (30+ hours/week)"]);
  addMC("10. Daily Academic Screen Time", ["Less than 3 hours", "3 to 5 hours", "6 to 8 hours", "More than 8 hours daily"]);
  addScale("11. Physical Digital Fatigue", "Strongly Disagree", "Strongly Agree", "I experience eye strain or physical digital fatigue from prolonged study screens.");

  // === SECTION B: GenAI Reliance & Offloading ===
  form.addPageBreakItem().setTitle("Section C: Generative AI Reliance & Cognitive Offloading").setHelpText("Usage habits with AI tools (e.g., ChatGPT, Claude, Gemini, DeepSeek).");
  addScale("12. Generative AI Usage Frequency for Academic Work", "Never", "Daily", "How often do you use Generative AI tools for your coursework?");

  var cb = form.addCheckboxItem();
  cb.setTitle("13. Primary Use Cases for Generative AI in Coursework")
    .setHelpText("Select up to 2 primary ways you use AI tools.")
    .setChoiceValues(["Concept explanation & brainstorming", "Essay writing, grammar polishing, or drafting", "Coding, debugging, or technical problem solving", "Summarizing articles / lecture slides", "Direct solution generation for assignments/homework"])
    .setRequired(true);
  cb.setValidation(FormApp.createCheckboxValidation().requireSelectAtMost(2).setHelpText("Please select at most 2 choices.").build());

  addScale("14. Cognitive Reliance", "Strongly Disagree", "Strongly Agree", "I feel unprepared or unable to complete my academic assignments without using AI tools.");
  addScale("15. Critical Thinking Offloading", "Strongly Disagree", "Strongly Agree", "I rely on AI to generate ideas, structures, or answers rather than thinking through them on my own.");
  addScale("16. Task Delegation Habit", "Strongly Disagree", "Strongly Agree", "When faced with a difficult academic prompt, my first reaction is to copy-paste it into an AI tool before attempting it myself.");
  addScale("17. AI Output Verification", "Strongly Disagree", "Strongly Agree", "I thoroughly verify and fact-check AI-generated outputs before incorporating them into my academic work.");
  addScale("18. Exam Preparation Reliance", "Strongly Disagree", "Strongly Agree", "I use AI tools to generate study summaries, practice questions, or explanations when preparing for exams.");
  addScale("19. Perceived AI Accuracy Trust", "Strongly Disagree", "Strongly Agree", "I believe Generative AI outputs are almost always accurate and superior to my own work.");
  addScale("20. Perceived Time-Saving Benefit", "Strongly Disagree", "Strongly Agree", "Using AI tools saves me significant time during assignment preparation.");
  addScale("21. Academic Integrity Anxiety", "Strongly Disagree", "Strongly Agree", "I worry about getting accused of plagiarism or flagged for AI usage even when using AI legitimately.");

  // === SECTION C & D: Routine, Coping & Support ===
  form.addPageBreakItem().setTitle("Section D: Academic Routine, Coping & Social Support").setHelpText("Study habits, coping strategies, and support systems.");
  addMC("22. Average Weekly Independent Study Hours (Outside Class)", ["Less than 5 hours", "5 to 10 hours", "11 to 20 hours", "More than 20 hours"]);
  addMC("23. Class Attendance Consistency", ["Always (> 90%)", "Mostly (75–90%)", "Occasional absence (50–74%)", "Frequent absence (< 50%)"]);
  addMC("24. Assignment Submission Latency", ["Well before the deadline", "Right at the deadline", "Frequently late / Request extensions"]);
  addScale("25. Workload Intensity Perception", "Strongly Disagree", "Strongly Agree", "My current academic workload feels heavy and overwhelming.");
  addMC("26. Average Nightly Sleep Duration During Semester", ["Less than 5 hours", "5 to 6 hours", "7 to 8 hours", "More than 8 hours"]);
  addScale("27. Psychological Stress / Anxiety", "Strongly Disagree", "Strongly Agree", "In recent weeks, I have felt overwhelmed, irritable, or panicked due to academic demands.");
  addScale("28. Active Coping 1 (Planning)", "Strongly Disagree", "Strongly Agree", "When facing academic stress, I actively break tasks into steps and seek help or solutions.");
  addScale("29. Active Coping 2 (Help-Seeking)", "Strongly Disagree", "Strongly Agree", "I talk to professors, advisors, or classmates when I struggle with coursework.");
  addScale("30. Avoidant Coping 1 (Procrastination)", "Strongly Disagree", "Strongly Agree", "When academic pressure gets too high, I procrastinate or avoid thinking about my schoolwork.");
  addScale("31. Avoidant Coping 2 (Distraction)", "Strongly Disagree", "Strongly Agree", "I use social media, gaming, or entertainment to distract myself from academic stress.");
  addScale("32. Institutional/Faculty Support", "Strongly Disagree", "Strongly Agree", "I feel supported by my university administration and instructors when facing academic difficulties.");
  addScale("33. Peer Support Network", "Strongly Disagree", "Strongly Agree", "I have a strong peer/friend network at university that helps me cope with academic stress.");
  addScale("34. Family Support & Understanding", "Strongly Disagree", "Strongly Agree", "My family understands and supports my academic goals and workload demands.");

  // Complete supplied BAT before the separate persistence outcomes
  form.addPageBreakItem().setTitle("Complete Burnout Assessment Tool for Students (BAT-S)");
  addScale("Due to my studies, I feel mentally exhausted.", "Never", "Always");
  addScale("Everything I do for my studies requires a great deal of effort.", "Never", "Always");
  addScale("After a day working on my study, I find it hard to recover my energy.", "Never", "Always");
  addScale("While working on my studies, I feel physically exhausted.", "Never", "Always");
  addScale("When I get up in the morning, I lack the energy to get started with my studies.", "Never", "Always");
  addScale("I want to be active when I am working on my studies but somehow, I am unable to manage.", "Never", "Always");
  addScale("When I exert myself for my studies, I quickly get tired.", "Never", "Always");
  addScale("At the end of a day of working on my studies, I feel mentally exhausted and drained.", "Never", "Always");
  addScale("I struggle to find any enthusiasm for my studies.", "Never", "Always");
  addScale("When I am working on my studies, I do not think much about what I am doing, and I function on autopilot.", "Never", "Always");
  addScale("I feel a strong aversion towards my studies.", "Never", "Always");
  addScale("I feel indifferent about my studies.", "Never", "Always");
  addScale("I’m cynical about the importance of my studies.", "Never", "Always");
  addScale("When I am working on my studies, I have trouble staying focused.", "Never", "Always");
  addScale("When I am working on my studies, I struggle to think clearly.", "Never", "Always");
  addScale("I am forgetful and distracted when I am working on my studies.", "Never", "Always");
  addScale("When I am working on my studies, I have trouble concentrating.", "Never", "Always");
  addScale("I make mistakes while working on my studies because I have my mind on other things.", "Never", "Always");
  addScale("I feel unable to control my emotions.", "Never", "Always");
  addScale("I do not recognize myself in the way I react emotionally.", "Never", "Always");
  addScale("I become irritable when things don’t go my way.", "Never", "Always");
  addScale("I get upset or sad without knowing why.", "Never", "Always");
  addScale("I may overreact unintentionally.", "Never", "Always");
  addScale("I have trouble falling or staying asleep.", "Never", "Always");
  addScale("I tend to worry.", "Never", "Always");
  addScale("I feel tense and stressed.", "Never", "Always");
  addScale("I feel anxious and/or suffer from panic attacks.", "Never", "Always");
  addScale("Noise and crowds disturb me.", "Never", "Always");
  addScale("I suffer from palpitations or chest pain.", "Never", "Always");
  addScale("I suffer from stomach and/or intestinal complaints.", "Never", "Always");
  addScale("I suffer from headaches.", "Never", "Always");
  addScale("I suffer from muscle pain, for example in the neck, shoulder or back.", "Never", "Always");
  addScale("I often get sick.", "Never", "Always");

  // Non-BAT motivation and continuation outcomes
  form.addPageBreakItem().setTitle("Section F: Academic Persistence and Motivation");
  addScale("68. Intrinsic Subject Interest", "Strongly Disagree", "Strongly Agree", "I am intrinsically interested in the subjects I am studying in my degree program.");
  addScale("69. Continuation Intention", "Strongly Disagree", "Strongly Agree", "I have seriously considered taking a leave of absence, switching majors, or dropping out due to academic stress.");

  Logger.log("SUCCESS! Form Created.");
  Logger.log("Edit Link: " + form.getEditUrl());
  Logger.log("Public Form Link: " + form.getPublishedUrl());
}
```
