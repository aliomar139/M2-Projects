# Top 30 Orthopedic AI Papers — Plain-Language Summaries

## How to read this report

The papers are listed in the same order as the Top 30 Excel file. Each paper is explained using four short parts:

- **What they studied:** The question and method.
- **What they found:** The main result.
- **Simple meaning:** Why the result may be useful.
- **Main caution:** What the study does not prove.

Two PDFs in the local folder are incorrect. The files for papers 11 and 13 contain different documents. Their summaries were therefore checked using the official online records.

**One useful term:** AUROC is a common score for how well a model separates two groups, such as patients who improve and patients who do not. A score of 0.5 is no better than chance; a score of 1.0 is perfect on the tested data.

---

## 1. The Application of Agentic Artificial Intelligence in Orthopaedics

**Citation:** Billi F, Bini S. *The Journal of Bone and Joint Surgery*. 2026. DOI: `10.2106/JBJS.25.01497`  
**Source:** [Local PDF](./top_100_papers/003_The_Application_of_Agentic_Artificial_Intelligence.pdf)

**What they studied:** This is a review of “AI agents” in orthopedics. An AI agent is a system that can plan several steps, use software tools, and complete a defined task instead of only answering one question.

**What they found:** The authors describe possible agents for routine office work, outcome prediction, research, rehabilitation, and clinical support. They also discuss privacy, fairness, safety, and the need for doctors to remain in control.

**Simple meaning:** AI agents may eventually help connect many parts of orthopedic care and reduce repetitive work.

**Main caution:** No agent was tested on real patients. This paper presents a future plan, not proof that agentic AI improves care.

## 2. Closed-Loop Digital Therapeutics Using Wearable Sensors

**Citation:** Dong J, Chen T, Peng Z. *Frontiers in Rehabilitation Sciences*. 2026. DOI: `10.3389/fresc.2026.1822939`  
**Source:** [Local PDF](./top_100_papers/001_Closed-Loop_digital_therapeutics_empowered_by_deep.pdf)

**What they studied:** The authors designed a computer-simulated rehabilitation system for patients after ACL surgery. Wearable sensors would track movement and muscle activity, while AI would change the exercises according to the patient’s progress.

**What they found:** In the simulation, the adaptive program allowed safe light activity 15% sooner than a cautious fixed program. It also produced 40% fewer simulated reinjuries than an aggressive fixed program.

**Simple meaning:** A future rehabilitation app could adjust exercises as a patient improves, like a digital therapist that responds to new data.

**Main caution:** These were simulated patients. The reported benefits have not yet been confirmed in real people.

## 3. Predicting Surgeon Recommendations From Patient Questionnaires

**Citation:** Halvorson RT et al. *Arthroscopy*. 2026. DOI: `10.1002/arj.70016`  
**Source:** [Local PDF](./top_100_papers/004_Large_Language_Model_Predicts_Surgeon_Recommendati.pdf)

**What they studied:** A language model read questionnaires from 1,141 new patients with knee or shoulder problems. It tried to predict whether the surgeon would request advanced imaging or recommend surgery.

**What they found:** It predicted imaging recommendations correctly in 70% of cases. When imaging reports were also available, it predicted surgical recommendations correctly in 81% of cases. Results varied between diagnoses.

**Simple meaning:** The way patients describe their symptoms contains useful information that AI can recognize.

**Main caution:** The AI learned to copy past surgeon decisions. The study did not prove that those decisions were the best treatment for each patient.

## 4. ChatGPT-4 and Orthopedic Treatment Guidelines

**Citation:** Dagher T et al. *Clinical Orthopaedics and Related Research*. 2024. DOI: `10.1097/CORR.0000000000003234`  
**Source:** [Local PDF](./top_100_papers/010_“Dr._AI_Will_See_You_Now”_How_Do_ChatGPT-4_Treatme.pdf)

**What they studied:** ChatGPT-4 received 100 clear example cases covering 10 common orthopedic conditions. Each case included a short history and an image. The model had to recommend one treatment.

**What they found:** Its answer matched AAOS treatment guidelines in 90% of cases and matched the treating surgeon in 78%. Mistakes often involved disease severity, other health problems, lifestyle, or reasons why surgery might be unsafe.

**Simple meaning:** ChatGPT can often recall the correct guideline for a straightforward case.

**Main caution:** Real patients are usually more complicated than these examples. A doctor must still review the recommendation.

## 5. Improving Medical Language Models With Guidelines and AI Agents

**Citation:** Woo JJ et al. *Arthroscopy*. 2024. DOI: `10.1016/j.arthro.2024.10.042`  
**Source:** [Local PDF](./top_100_papers/051_Custom_Large_Language_Models_Improve_Accuracy_Comp.pdf)

**What they studied:** Several language models answered 100 questions based on the AAOS ACL guideline. The researchers then gave the models direct access to the guideline and added AI agents that could check the work.

**What they found:** Models without the guideline scored below 60%. Giving them the relevant guideline text improved scores by about 40 percentage points on average. The best agent-based setup scored 95%.

**Simple meaning:** A medical AI is much more reliable when it can look up trusted documents instead of depending only on its memory.

**Main caution:** This was a question-answering test. It did not measure patient safety or results in a real clinic.

## 6. Causal Machine Learning for Choosing Treatments

**Citation:** Feuerriegel S et al. *Nature Medicine*. 2024. DOI: `10.1038/s41591-024-02902-1`  
**Source:** [Local PDF](./top_100_papers/069_Causal_machine_learning_for_predicting_treatment_o.pdf)

**What they studied:** This methods review explains how AI can estimate what might happen to the same type of patient under different treatments.

**What they found:** The paper describes several methods for estimating individual treatment effects. It stresses that AI cannot automatically remove bias from medical data. Researchers must still account for differences between patients, treatment timing, and missing patient groups.

**Simple meaning:** Predicting an outcome is not the same as deciding which treatment caused a better outcome. Causal methods try to answer the more useful treatment-choice question.

**Main caution:** These methods only give trustworthy answers when their assumptions and data quality are carefully checked.

## 7. DeepSurv: Predicting Long-Term Risk Under Different Treatments

**Citation:** Katzman JL et al. *BMC Medical Research Methodology*. 2018. DOI: `10.1186/s12874-018-0482-1`  
**Source:** [Local PDF](./top_100_papers/078_DeepSurv_personalized_treatment_recommender_system.pdf)

**What they studied:** DeepSurv is a neural-network model for predicting how long it may take before an event occurs, such as a complication or death. It can calculate risk under different treatment choices.

**What they found:** In simulated and real datasets, DeepSurv performed as well as or better than common survival-analysis methods. It could rank treatments according to the predicted risk for one patient.

**Simple meaning:** The method could help compare treatments when long-term timing matters, not only whether an event happens.

**Main caution:** The clinical examples were early demonstrations. With ordinary hospital data, hidden differences between treatment groups can still create misleading recommendations.

## 8. The Personalized Advantage Index

**Citation:** DeRubeis RJ et al. *PLOS ONE*. 2014. DOI: `10.1371/journal.pone.0083875`  
**Source:** [Local PDF](./top_100_papers/079_The_Personalized_Advantage_Index_Translating_Resea.pdf)

**What they studied:** The researchers used data from 154 patients with depression who were randomly assigned medication or cognitive therapy. They predicted each patient’s result under both treatments.

**What they found:** For 60% of patients, one treatment was predicted to have a meaningful advantage. Patients who happened to receive their predicted better treatment had better results than those who received the other treatment.

**Simple meaning:** The study shows a clear way to turn research data into a personalized comparison between two treatments.

**Main caution:** This was a depression study, not an orthopedic study. The same idea would need to be tested separately with orthopedic treatments.

## 9. Predicting Recovery After Total Knee Replacement

**Citation:** Ribbons K et al. *Scientific Reports*. 2025. DOI: `10.1038/s41598-025-88560-w`  
**Source:** [Local PDF](./top_100_papers/014_Biopsychosocial_based_machine_learning_models_pred.pdf)

**What they studied:** The study used data from 863 knee-replacement patients to predict improvement three months after surgery. It included medical information plus nutrition, employment, expectations, emotional response to pain, tiredness, and strength.

**What they found:** Eighteen factors were useful across the prediction models. The models explained up to 24% of the differences in quality-of-life improvement and 40% of the differences in knee-symptom improvement.

**Simple meaning:** Recovery depends on more than the knee itself. A patient’s mental, physical, and social situation can matter.

**Main caution:** Much of the difference between patients remained unexplained, and follow-up lasted only three months.

## 10. Explaining Different Walking Responses After Hip Replacement

**Citation:** Stetter BJ et al. *Arthritis Research & Therapy*. 2025. DOI: `10.1186/s13075-025-03709-2`  
**Source:** [Local PDF](./top_100_papers/020_Explainable_machine_learning_for_orthopedic_decisi.pdf)

**What they studied:** Researchers measured walking patterns in 109 people with hip arthritis. Sixty-three were measured again after hip replacement. AI grouped patients by their movement patterns and identified which movements separated the groups.

**What they found:** The patients formed three main movement groups. Surgery improved walking overall, but the amount and type of improvement differed between groups. Hip bending and rotation were important differences.

**Simple meaning:** Patients with the same diagnosis may move differently and may need different rehabilitation plans.

**Main caution:** The study examined walking mechanics, not overall satisfaction or quality of life. Detailed motion testing may also be difficult to provide in every clinic.

## 11. Predicting Meaningful Improvement After Hip or Knee Replacement

**Citation:** Fontana MA et al. *Clinical Orthopaedics and Related Research*. 2019. DOI: `10.1097/CORR.0000000000000687`  
**Evidence source:** [Verified publisher record](https://doi.org/10.1097/CORR.0000000000000687). The local PDF numbered `022` contains a different document and should be replaced.

**What they studied:** The researchers used records from 7,239 hip replacements and 6,480 knee replacements. Their models predicted which patients would not feel a meaningful improvement two years after surgery.

**What they found:** Model performance ranged from weak to strong depending on the outcome. Patients’ own health and symptom scores before surgery were among the most useful predictors. A short model using mainly those scores worked almost as well as larger models.

**Simple meaning:** A few well-chosen questions before surgery may help doctors explain a patient’s chance of improvement.

**Main caution:** Every patient in the study already had surgery. The models do not tell us whether surgery or nonsurgical care would have been better.

## 12. Predicting Results After Hip Arthroscopy

**Citation:** Ishøi L et al. *British Journal of Sports Medicine*. 2023. DOI: `10.1136/bjsports-2022-105534`  
**Source:** [Local PDF](./top_100_papers/041_Stratified_care_in_hip_arthroscopy_can_we_predict.pdf)

**What they studied:** A model was built with 1,082 hip-arthroscopy patients and tested on 464 later patients. It used 26 types of information, including patient details, X-rays, and self-reported symptoms.

**What they found:** The model was reasonably good at identifying patients at risk of an unsuccessful result after one year. It was poor at confidently identifying patients who would succeed.

**Simple meaning:** The tool may be more useful for warning about risk than for promising a good result.

**Main caution:** Predicting failure and predicting success are not simply opposite versions of the same task.

## 13. Personalized Prediction for Knee Osteoarthritis

**Citation:** Jamshidi A, Pelletier JP, Martel-Pelletier J. *Nature Reviews Rheumatology*. 2019. DOI: `10.1038/s41584-018-0130-5`  
**Evidence source:** [Verified PubMed record](https://pubmed.ncbi.nlm.nih.gov/30523334/). The local PDF numbered `044` is a WEKA software manual and should be replaced.

**What they studied:** This review looks at ways to combine symptoms, images, laboratory markers, and changes over time to understand knee osteoarthritis.

**What they found:** Knee osteoarthritis is not the same in every patient. AI may help identify groups that worsen quickly, detect disease earlier, and estimate who may benefit from a treatment. Clear models and careful choice of information are important.

**Simple meaning:** Better care may come from recognizing different types of knee arthritis instead of treating every patient as part of one group.

**Main caution:** The paper reviews ideas and earlier research. It does not test one new model on a new group of patients.

## 14. Predicting Shoulder-Replacement Results With Fewer Questions

**Citation:** Kumar V et al. *Journal of Shoulder and Elbow Surgery*. 2020. DOI: `10.1016/j.jse.2020.07.042`  
**Source:** [Local PDF](./top_100_papers/045_Using_Machine_Learning_to_Predict_Clinical_Outcome.pdf)

**What they studied:** Models were built from 5,774 shoulder replacements. A large model using 291 pieces of information was compared with a simpler model using only 19 preoperative inputs.

**What they found:** The smaller model predicted pain, movement, and function almost as accurately as the much larger model. For one common shoulder score, the average errors were about 12 points for both models.

**Simple meaning:** A useful clinical prediction may be possible without asking patients and staff to collect hundreds of details.

**Main caution:** The shorter model still needs testing in hospitals and patient groups that did not contribute to the original database.

## 15. Review of Prediction Tools After Total Knee Replacement

**Citation:** Cochrane JA et al. *The Journal of Arthroplasty*. 2020. DOI: `10.1016/j.arth.2020.10.053`  
**Source:** [Local PDF](./top_100_papers/047_Clinical_Decision_Support_Tools_for_Predicting_Out.pdf)

**What they studied:** This review examined 18 studies that tried to predict results after total knee replacement.

**What they found:** Studies used very different patient information and definitions of success. Most tools had limited accuracy. Only one reported strong discrimination above an AUROC of 0.80, and only two tested their models in a separate patient population.

**Simple meaning:** Many knee-replacement prediction tools have been created, but few are ready to be trusted in normal clinical care.

**Main caution:** A model that looks good where it was created may perform worse in another hospital. Independent testing is essential.

## 16. How to Build and Test Orthopedic Prediction Models

**Citation:** Zaniletti I et al. *The Journal of Arthroplasty*. 2023. DOI: `10.1016/j.arth.2022.12.032`  
**Source:** [Local PDF](./top_100_papers/048_How_to_Develop_and_Validate_Prediction_Models_for.pdf)

**What they studied:** This educational paper explains the correct steps for making a clinical prediction model.

**What they found:** Researchers should choose a useful clinical question, select the right patients, handle missing information, prevent the model from memorizing its training data, and test it on new patients. Accuracy alone is not enough; predicted risks must also match real risks.

**Simple meaning:** A prediction model needs careful design and independent testing before doctors should use it.

**Main caution:** The article is a guide. It does not present a new model or show that one tool improves patient care.

## 17. Decision Curve Analysis: Does a Model Help Decisions?

**Citation:** Vickers AJ, Holland F. *The Spine Journal*. 2021. DOI: `10.1016/j.spinee.2021.02.024`  
**Source:** [Local PDF](./top_100_papers/042_Decision_curve_analysis_to_evaluate_the_clinical_b.pdf)

**What they studied:** This methods paper explains “decision curve analysis,” a way to test whether acting on a model’s predictions would be better than treating everyone or treating no one.

**What they found:** A statistically accurate model may still be useless if its mistakes lead to harmful decisions. The method weighs the value of correct decisions against the harm of unnecessary treatment across different risk levels.

**Simple meaning:** The important question is not only “Is the prediction correct?” but also “Does using it lead to better choices?”

**Main caution:** The result depends on choosing sensible risk levels and clearly defining the medical action being considered.

## 18. AI Compared With Orthopedic Surgeons

**Citation:** Russell J, Rosen J, Vella-Baldacchino M. *Journal of Experimental Orthopaedics*. 2025. DOI: `10.1002/jeo2.70548`  
**Source:** [Local PDF](./top_100_papers/007_Artificial_intelligence_fails_to_outperform_orthop.pdf)

**What they studied:** This review included 16 studies that directly compared AI with orthopedic clinicians on knowledge, decisions, treatment plans, quality checks, or patient questions.

**What they found:** Performance depended on the task. AI did well in some emergency and patient-communication tasks. Clinicians did better on examinations and on some imaging tasks, including grading knee arthritis. No clear overall winner was found.

**Simple meaning:** AI may help with selected tasks, but it does not consistently perform better than orthopedic professionals.

**Main caution:** The studies used very different tests, so their results cannot be combined into one simple score.

## 19. How Ready Is Orthopedic AI for Clinical Use?

**Citation:** Glinkowski W et al. *Journal of Clinical Medicine*. 2026. DOI: `10.3390/jcm15051751`  
**Source:** [Local PDF](./top_100_papers/015_Artificial_Intelligence_in_Orthopaedics_Clinical_P.pdf)

**What they studied:** This review selected 40 studies covering medical images, surgical planning, outcome prediction, rehabilitation, remote care, and hospital management.

**What they found:** The best evidence is for focused tasks such as detecting fractures, identifying implants, and helping with surgical planning. Personalized predictions and rehabilitation systems are less mature. Many were tested in only one hospital and few were tested during real clinical work.

**Simple meaning:** Some narrow orthopedic AI tools are close to practical use, but systems that recommend personalized care need much more evidence.

**Main caution:** Good technical scores do not automatically prove patient benefit, fairness, safety, or easy integration into a hospital.

## 20. AI Across Musculoskeletal Surgery

**Citation:** Oettl FC et al. *HSS Journal*. 2025. DOI: `10.1177/15563316251339596`  
**Source:** [Local PDF](./top_100_papers/002_Artificial_Intelligence_and_Musculoskeletal_Surgic.pdf)

**What they studied:** This review describes AI before, during, and after musculoskeletal surgery. Topics include reading images, planning operations, robotics, predicting complications, writing notes, educating patients, and AI agents.

**What they found:** AI can improve speed or precision in some narrow tasks. However, costs, regulation, system integration, uneven evidence, and safety remain important problems.

**Simple meaning:** AI may support many steps of surgery, especially repetitive or data-heavy work.

**Main caution:** This paper summarizes other studies. It does not test one new AI system, and it supports keeping the surgeon responsible for final decisions.

## 21. GPT-4 Recommendations Based Only on MRI Reports

**Citation:** Truhn D et al. *Scientific Reports*. 2023. DOI: `10.1038/s41598-023-47500-2`  
**Source:** [Local PDF](./top_100_papers/050_A_pilot_study_on_the_efficacy_of_GPT-4_in_providin.pdf)

**What they studied:** GPT-4 read 20 anonymous knee and shoulder MRI reports and suggested treatments. Two orthopedic surgeons rated the answers.

**What they found:** Most answers were reasonable and useful, and major invented information was uncommon. However, the advice was often general. The model sometimes misunderstood urgency and lacked examination findings, patient goals, and other health information.

**Simple meaning:** GPT-4 may help draft possible next steps after an MRI report.

**Main caution:** An MRI report alone is not enough to choose treatment safely. The study was also very small, with only 20 reports.

## 22. Decision Tools for Choosing Knee-Arthritis Treatment

**Citation:** Cochrane JA et al. *Therapeutic Advances in Musculoskeletal Disease*. 2026. DOI: `10.1177/1759720X251407070`  
**Source:** [Local PDF](./top_100_papers/035_Implementation_of_clinical_decision_support_tools.pdf)

**What they studied:** This review searched six databases for tools that give personalized support when choosing treatment for knee osteoarthritis. It screened 5,376 records and included 15 studies describing 10 tools.

**What they found:** Most tools focused on pain and physical function. Fewer than half gave personalized information about nonsurgical choices. Mental, social, and financial outcomes were rarely considered. Many studies did not explain their methods well enough.

**Simple meaning:** Existing decision tools cover only part of what matters to patients with knee arthritis.

**Main caution:** A useful future tool should compare both surgical and nonsurgical options and clearly explain how it produces its estimates.

## 23. AI Support for Prescribing Foot Orthoses

**Citation:** Jung JY, Yang W, Kim JJ. *JMIR Medical Informatics*. 2026. DOI: `10.2196/92831`  
**Source:** [Local PDF](./top_100_papers/036_A_Hierarchical_Machine_Learning–Based_Framework_fo.pdf)

**What they studied:** Using 6,462 clinic visits, researchers trained AI to suggest 15 parts of a foot-orthosis prescription. A basic model used commonly available information. An advanced model added special foot-movement measurements when available.

**What they found:** The models showed moderate-to-good performance. The correct prescription component appeared as the first suggestion 86.7% of the time and within the first three suggestions 97.4% of the time.

**Simple meaning:** The system could give clinicians a short list of likely orthosis choices even when some measurements are missing.

**Main caution:** It learned to copy earlier prescriptions. The study did not show that its suggestions produced better patient outcomes.

## 24. Testing a Shoulder-Replacement Prediction Tool in New Patients

**Citation:** Simmons C et al. *European Journal of Orthopaedic Surgery & Traumatology*. 2023. DOI: `10.1007/s00590-023-03796-4`  
**Source:** [Local PDF](./top_100_papers/039_Initial_clinical_experience_with_a_predictive_clin.pdf)

**What they studied:** A shoulder-replacement prediction tool was tested in 243 patients: 43 received anatomic replacements and 200 received reverse replacements. Predictions were compared with results from three months to two years after surgery.

**What they found:** The tool’s errors were generally similar to, or smaller than, those reported during its earlier internal testing. It predicted several measures of shoulder function and movement reasonably well.

**Simple meaning:** The tool continued to work when tested in a separate group, which is an important step toward clinical use.

**Main caution:** Some patient groups were small. The study tested prediction accuracy, not whether showing the predictions improved decisions or satisfaction.

## 25. Recording Patient Preferences Before an Orthopedic Visit

**Citation:** Singh A et al. *Frontiers in Digital Health*. 2023. DOI: `10.3389/fdgth.2023.1137066`  
**Source:** [Local PDF](./top_100_papers/040_Patient_preferences_as_human_factors_for_health_da.pdf)

**What they studied:** Researchers created a phone app where patients divide 100 points among the treatment results that matter most to them. The app was tested with 23 first-time orthopedic patients.

**What they found:** Five main preference areas were identified. Most patients placed most of their points on only one to three priorities. Patients found the app reasonably easy to use, and interviews suggested it could focus the clinical conversation.

**Simple meaning:** Two patients with the same condition may want different results. A recommendation system should include those personal goals.

**Main caution:** This small study tested preference collection, not an AI recommendation or improvement in health outcomes.

## 26. Prediction Support for Chronic Musculoskeletal Pain Care

**Citation:** Zmudzki F et al. *JMIR Rehabilitation and Assistive Technologies*. 2025. DOI: `10.2196/65890`  
**Source:** [Local PDF](./top_100_papers/075_Machine_Learning_Clinical_Decision_Support_for_Int.pdf)

**What they studied:** Clinicians received AI-generated profiles for 17 new patients entering a team-based chronic-pain program. The profiles predicted activity, disability, pain, tiredness, and quality of life.

**What they found:** The profiles agreed with clinicians in 14 of 17 cases. Clinicians said they were helpful in 15 cases and discussed them with 8 patients.

**Simple meaning:** Prediction profiles may help a care team understand a patient and support a shared discussion.

**Main caution:** Seventeen patients are far too few to prove accuracy or better treatment results. This is an early feasibility study.

## 27. How AI Recommendations Can Affect Clinician Decisions

**Citation:** Jacobs ML et al. *Translational Psychiatry*. 2021. DOI: `10.1038/s41398-021-01224-x`  
**Source:** [Local PDF](./top_100_papers/080_How_machine-learning_recommendations_influence_cli.pdf)

**What they studied:** A total of 220 clinicians selected treatments for example psychiatry cases. Sometimes they saw an AI recommendation, with different kinds of explanations, and sometimes they worked without AI.

**What they found:** AI advice did not significantly improve agreement with experts. When the AI recommendation was wrong, a simple and believable explanation sometimes made clinicians less accurate than when they worked alone.

**Simple meaning:** Showing a doctor an AI answer does not automatically make the decision safer. A convincing explanation can make wrong advice look trustworthy.

**Main caution:** The study concerned antidepressant treatment, not orthopedics, but the warning about trusting AI applies to both fields.

## 28. Learning a Series of Treatment Decisions From Hospital Data

**Citation:** Abebe SL et al. *Machine Learning and Knowledge Extraction*. 2024. DOI: `10.3390/make6030088`  
**Source:** [Local PDF](./top_100_papers/076_Learning_Optimal_Dynamic_Treatment_Regime_from_Obs.pdf)

**What they studied:** This methods paper compared several tree-based AI approaches for choosing a sequence of treatments from observational medical records.

**What they found:** The methods tried to estimate which treatment should be chosen at each stage and what the outcome might have been under another choice. Their performance was compared using simulated treatment assignments and estimated alternative outcomes.

**Simple meaning:** The methods could eventually help with care that changes over time, such as trying rehabilitation before deciding on surgery.

**Main caution:** Ordinary medical records contain bias. The “best” unobserved treatment cannot be checked directly, so strong assumptions and careful testing are required.

## 29. Reinforcement Learning for Ranking Treatments

**Citation:** Liu M, Shen XT, Pan W. *Statistics in Medicine*. 2022. DOI: `10.1002/sim.9491`  
**Source:** [Local PDF](./top_100_papers/086_Deep_reinforcement_learning_for_personalized_treat.pdf)

**What they studied:** The authors created a reinforcement-learning method called PPORank. It ranks possible treatments for a person using many biological and clinical features. Tests used simulated data and cancer cell-line drug data.

**What they found:** The method ranked drugs better than the comparison methods in the reported experiments. It could update its ranking as new information became available.

**Simple meaning:** The technique offers one possible way to rank several treatments for one patient instead of predicting only a single outcome.

**Main caution:** It was not tested on real orthopedic patients. Orthopedic use would require safety rules, meaningful follow-up data, and prospective clinical testing.

## 30. Predicting Two-Year Results After Hip Arthroscopy

**Citation:** Yang G et al. *Journal of Experimental Orthopaedics*. 2025. DOI: `10.1002/jeo2.70477`  
**Source:** [Local PDF](./top_100_papers/097_Evaluation_of_centre‐specific_machine_learning_mod.pdf)

**What they studied:** This study used records from 210 hip-arthroscopy patients at one center. Three models predicted whether patients would have a meaningful improvement after two years.

**What they found:** The three models had reported AUROCs of 0.76, 0.89, and 0.99. Symptom duration, the starting activity score, joint-space width, and hip shape were important predictors. Random forest produced the highest score.

**Simple meaning:** Local patient records may help estimate who is likely to improve after hip arthroscopy.

**Main caution:** A score of 0.99 is unusually high and may mean the model learned this small dataset too closely. It must be tested independently in other hospitals.

---

## Overall message from the 30 papers

AI is already useful for focused tasks such as reading data, checking guidelines, predicting risk, and supporting conversations. However, most studies do **not** prove that AI can independently choose the best treatment for a patient.

The safest near-term use is as support for the clinician and patient:

1. Show the likely benefits and risks in clear language.
2. Compare more than one treatment when good data are available.
3. Include the patient’s goals and preferences.
4. Let the clinician check the recommendation and make the final decision with the patient.
5. Test the system on new patients and in real clinics before relying on it.
