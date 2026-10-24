# Top 100 Research Papers for Agentic Orthopedic AI Treatment Recommendation

## Document Overview
This document provides a ranked summary of the top 100 research papers relevant to building an **Agentic AI System for Personalized Orthopedic Treatment Recommendation**. The papers are ranked by their relevance to key project components: agentic AI, large language models, clinical decision support systems, personalized treatment recommendation engines, case-based retrieval, and orthopedic outcome prediction.

---
## Executive Summary of Ranking Categories
- **Ranks 1–25 (Tier 1 - Highest Relevance):** Papers focusing directly on Agentic AI, LLM treatment recommendations, dynamic reinforcement learning, and orthopedic decision support systems.
- **Ranks 26–60 (Tier 2 - High Relevance):** Papers on machine learning outcome prediction (PROMs, MCID, revision risk), history-taking AI, and cross-domain recommender systems (hypertension, depression, oncology).
- **Ranks 61–100 (Tier 3 - Supporting Relevance):** Systematic reviews on orthopedic ML, risk of bias, transparency guidelines (TRIPOD, PROBAST), and specialized diagnostic/surgical planning tools.

---

## Ranked Literature Summaries (1 to 100)

### Rank 1: Closed-Loop digital therapeutics empowered by deep reinforcement learning and wearable sensing for precision orthopedic rehabilitation: a simulation-based proof-of-concept study
- **Relevance Score:** 105/100
- **Authors:** Jia-Hao Dong, Tao Chen, Zhongyu Peng
- **Year & Journal:** 2026 | *Frontiers in Rehabilitation Sciences* (SJR Quartile: 2.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** Deep reinforcement learning and wearable sensing can safely and dynamically personalize orthopedic rehabilitation strategies, potentially reducing re-injury rates and improving efficiency.
- **Simple Summary & Project Context:**
  Objective: Static, one-size-fits-all protocols in postoperative orthopedic rehabilitation fail to adapt to individual recovery dynamics, potentially leading to suboptimal rehabilitation efficiency or an elevated risk of secondary injury. To address this critical gap, we propose and provide a simulation-based proof-of-concept validation for a novel closed-loop management system that deeply integrates patient-generated health data (PGHD) with deep reinforcement learning (DRL), offering a potential technical pathway for real-time personalized optimization of rehabilitation regimens and continuous prediction of long-term functional outcomes.

Methods: A three-tier system architecture was constructed, comprising an intelligent sensing layer, an AI decision-making and prediction layer, and an interactive feedback layer. Through wearable inertial measurement units (IMUs) and surface electromyography (sEMG) devices, the system continuously collected multi-dimensional PGHD, including movement quality, training intensity, adherence, and pain feedback. These heterogeneous data were encoded into a comprehensive "patient state space" through a standardized feature engineering pipeline. A proximal policy optimization (PPO) algorithm was employed to train a DRL agent to learn the optimal policy for dynamically adjusting the next-cycle rehabilitation prescription (including exercise type, intensity, frequency, and progression pace). The agent aimed to maximize a hierarchical cumulative reward function that integrates short-term safety (ΔVAS pain score monitoring), mid-term adherence (training completion rate), and long-term functional improvement. Critically, a temporal convolutional network (TCN) prognostic module was deeply coupled with the DRL agent, providing prospective predictions of future functional recovery curves that inform the agent's long-term reward calculation, equipping the system with the capability of "making decisions based on predictions."

Results: A proof-of-concept validation was conducted in a simulated environment for a post-operative anterior cruciate ligament reconstruction (ACLR) scenario. The trained DRL agent demonstrated the ability to generate differentiated rehabilitation strategies: in stratified analysis, it prescribed distinct progression paces for virtual patients with fast vs. slow recovery trajectories. Under this simulation setting, compared with a static conservative protocol, the DRL-driven strategy reduced the simulated time to "safe return to light activity" by an average of 15% and, compared with a static aggressive protocol, relatively decreased simulated "re-injury" events by 40%. The mean absolute errors (MAEs) of the TCN prognostic module for predicting functional scores at 2, 4, and 8 weeks into the future were 3.2, 4.8, and 6.5 points (on a 100-point scale), respectively, outperforming the ARIMA, LSTM, and GRU baseline models. An ablation study confirmed the TCN module's independent contribution, as its removal led to a relative increase in the simulated re-injury rate.

Conclusion: This proof-of-concept study provides foundational evidence for the technical feasibility of a DRL-based closed-loop rehabilitation system. The proposed framework uniquely couples a wearable sensing layer with a symbiotic DRL-TCN architecture, demonstrating the potential to safely and dynamically personalize rehabilitation strategies in a simulated environment. These findings lay the groundwork for future prospective clinical trials, which are the necessary next step to validate safety, efficacy, and clinical utility in real-world settings.

© 2026 Dong, Chen and Peng.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/closedloop-digital-therapeutics-empowered-by-deep-dong-chen/31ad8aa7269a5f448638b8bb9d3f4c51/) | DOI: 10.3389/fresc.2026.1822939

---

### Rank 2: Artificial Intelligence and Musculoskeletal Surgical Applications
- **Relevance Score:** 100/100
- **Authors:** F. Oettl, Bálint Zsidai, Jacob F. Oeding, K. Samuelsson
- **Year & Journal:** 2025 | *HSS Journal®* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 19
- **Main Takeaway:** AI-assisted procedures in orthopedic surgery improve precision, efficiency, and patient outcomes while maintaining human clinical expertise.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) has emerged as a transformative force in orthopedic surgery. Potentially encompassing pre-, intra-, and postoperative processes, it can process complex medical imaging, provide real-time surgical guidance, and analyze large datasets for outcome prediction and optimization. AI has shown improvements in surgical precision, efficiency, and patient outcomes across orthopedic subspecialties, and large language models and agentic AI systems are expanding AI utility beyond surgical applications into areas such as clinical documentation, patient education, and autonomous decision support. The successful implementation of AI in orthopedic surgery requires careful attention to validation, regulatory compliance, and healthcare system integration. As these technologies continue to advance, maintaining the balance between innovation and patient safety remains crucial, with the ultimate goal of achieving more personalized, efficient, and equitable healthcare delivery while preserving the essential role of human clinical judgment. This review examines the current landscape and future trajectory of AI applications in orthopedic surgery, highlighting both technological advances and their clinical impact. Studies have suggested that AI-assisted procedures achieve higher accuracy and better functional outcomes compared to conventional methods, while reducing operative times and complications. However, these technologies are designed to augment rather than replace clinical expertise, serving as sophisticated tools to enhance surgeons' capabilities and improve patient care.

© The Author(s) 2025.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-and-musculoskeletal-surgical-oettl-zsidai/b710ae2742d4574ca049b9647b070dc5/) | DOI: 10.1177/15563316251339596

---

### Rank 3: The Application of Agentic Artificial Intelligence in Orthopaedics.
- **Relevance Score:** 100/100
- **Authors:** F. Billi, S. Bini
- **Year & Journal:** 2026 | *The Journal of bone and joint surgery. American volume* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 2
- **Main Takeaway:** Agentic AI in orthopaedics is poised to transform the practice, but its success depends on human-machine collaboration and aligning computational precision with the enduring human art of restoring motion and health.
- **Simple Summary & Project Context:**
  Background: Artificial intelligence (AI) in orthopaedics is shifting from passive interfaces in which a surgeon queries a large language model to an era of active participation in which a surgeon empowers a software platform to automate certain tasks on their behalf. The emerging new paradigm called agentic AI involves agents that move beyond decision support tools to becoming semi-autonomous collaborators in research, clinical, and rehabilitation tasks.

Purpose: The purpose of this review is to summarize how recent advances (April 2022 to October 2025) in automation, prediction, and augmentation agents are poised to transform the practice of orthopaedics; and to outline the conceptual, technical, and ethical foundations of this transition.

Recent findings: An agent is software that can process information and act independently to execute a set of defined tasks. It can seek knowledge, ask for help, deploy other software, and learn from its actions. Automation, prediction and augmentation agents can be leveraged in multi-agent and federated-learning architectures, working together to create coordinated ecosystems that can manage complex tasks and that improve with clinical use. Collectively, the output of such ecosystems is referred to as agentic AI. However, regulatory and ethical concerns underscore the need for transparency, equity, and the preservation of human agency within these frameworks.

Summary: Agentic AI marks a transition from passive tools that merely assist clinicians to autonomous systems that act alongside them. The success of this technology in orthopaedics will depend on the depth of human-machine collaboration they enable and how well they align computational precision with the enduring human art of restoring motion and health.

Copyright © 2026 by The Journal of Bone and Joint Surgery, Incorporated.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/the-application-of-agentic-artificial-intelligence-in-billi-bini/a9c2a35b7a0f5715b35d697d8863f420/) | DOI: 10.2106/jbjs.25.01497

---

### Rank 4: Large Language Model Predicts Surgeon Recommendations for Imaging and Surgery for Patients Presenting for Knee and Shoulder Complaints With 70% and 81% Accuracy Using Previsit Questionnaire Responses.
- **Relevance Score:** 100/100
- **Authors:** Ryan T. Halvorson, Timothy Keeley, K. Niknam, T. Zack, S. Majumdar, Brian T. Feeley, Alan L. Zhang, Drew A. Lansdown
- **Year & Journal:** 2026 | *Arthroscopy : the journal of arthroscopic & related surgery : official publication of the Arthroscopy Association of North America and the International Arthroscopy Association* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 1
- **Main Takeaway:** The pretrained large language model accurately predicts orthopaedic surgeon recommendations for imaging and surgery using previsit questionnaire responses for knee and shoulder complaints with 70% accuracy and 81% accuracy when augmented with radiology reports.
- **Simple Summary & Project Context:**
  Purpose: To validate the performance of a pretrained large language model (LLM) in predicting orthopaedic surgeon recommendations for management of newly referred patients, using free-text previsit questionnaire responses as input.

Methods: This retrospective cross-sectional study included new patients visiting an orthopaedic sports medicine clinic between 2020 and 2023. Using zero-shot prompting, the LLM analyzed previsit questionnaire responses (e.g., "When did you start to have pain?") to predict whether patients required advanced imaging and/or surgical intervention. The LLM was blinded to all other clinical information, including surgeon notes, physical exams, or referral data. Model predictions were evaluated with accuracy, sensitivity, and specificity in comparison to actual surgeon-generated plans. For a subset of patients who had undergone advanced imaging, the LLM was augmented with free-text radiology reports and asked to provide updated surgical recommendations.

Results: In the combined cohort of 1141 patients, the LLM predicted surgeon recommendation for advanced imaging with 70% accuracy, 83% sensitivity, and 64% specificity using previsit questionnaire responses alone. Imaging predictions were accurate for common diagnoses, including anterior cruciate ligament (ACL, 94%), meniscus (85%), and rotator cuff (80%) injuries but poor for knee (54%) and shoulder arthritis (66%). When augmented with imaging reports, the LLM predicted recommendations for surgery with 81% accuracy, 88% sensitivity, and 72% specificity. Surgical predictions were highly accurate for ACL (93%), meniscus (78%), rotator cuff (83%), and shoulder instability related pathologies (78%).

Conclusions: Using previsit questionnaire data from new orthopaedic patients with knee and shoulder complaints, the pretrained LLM showed 70% accuracy for imaging recommendations, and the augmented surgical-decision LLM showed 81% accuracy for surgical recommendations.

Level of evidence: Level III, retrospective diagnostic case-control study.

© 2026 the Arthroscopy Association of North America.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/large-language-model-predicts-surgeon-recommendations-halvorson-keeley/6746a55136c3577fad1a705f2dd7215b/) | DOI: 10.1002/arj.70016

---

### Rank 5: Assessing AI in Various Elements of Enhanced Recovery After Surgery (ERAS)-Guided Ankle Fracture Treatment: A Comparative Analysis with Expert Agreement
- **Relevance Score:** 95/100
- **Authors:** Rui Wang, Xuanming Situ, Xu Sun, Jinchang Zhan, Xi Liu
- **Year & Journal:** 2025 | *Journal of Multidisciplinary Healthcare* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** AI-powered LLMs, particularly ChatGPT, show promise in supporting clinical decision-making for ERAS-guided ankle fracture management, but further refinement and validation are needed to optimize AI-generated medical advice.
- **Simple Summary & Project Context:**
  Objective: This study aimed to assess and compare the performance of ChatGPT and iFlytek Spark, two AI-powered large language models (LLMs), in generating clinical recommendations aligned with expert consensus on Enhanced Recovery After Surgery (ERAS)-guided ankle fracture treatment. This study aims to determine the applicability and reliability of AI in supporting ERAS protocols for optimized patient outcomes.

Methods: A qualitative comparative analysis was conducted using 35 structured clinical questions derived from the Expert Consensus on Optimizing Ankle Fracture Treatment Protocols under ERAS Principles. Questions covered preoperative preparation, intraoperative management, postoperative pain control and rehabilitation, and complication management. Responses from ChatGPT and iFlytek Spark were independently evaluated by two experienced trauma orthopedic specialists based on clinical relevance, consistency with expert consensus, and depth of reasoning.

Results: ChatGPT demonstrated higher alignment with expert consensus (29/35 questions, 82.9%), particularly in comprehensive perioperative recommendations, detailed medical rationales, and structured treatment plans. However, discrepancies were noted in intraoperative blood pressure management and preoperative antiemetic selection. iFlytek Spark aligned with expert consensus in 22/35 questions (62.9%), but responses were often more generalized, less clinically detailed, and occasionally inconsistent with best practices. Agreement between ChatGPT and iFlytek Spark was observed in 23/35 questions (65.7%), with ChatGPT generally exhibiting greater specificity, timeliness, and precision in its recommendations.

Conclusion: AI-powered LLMs, particularly ChatGPT, show promise in supporting clinical decision-making for ERAS-guided ankle fracture management. While ChatGPT provided more accurate and contextually relevant responses, inconsistencies with expert consensus highlight the need for further refinement, validation, and clinical integration. iFlytek Spark's lower conformity suggests potential differences in training data and underlying algorithms, underscoring the variability in AI-generated medical advice. To optimize AI's role in orthopedic care, future research should focus on enhancing AI alignment with medical guidelines, improving model transparency, and integrating physician oversight to ensure safe and effective clinical applications.

© 2025 Wang et al.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/assessing-ai-in-various-elements-of-enhanced-recovery-wang-situ/ef645b8191595d0e9954d56670142544/) | DOI: 10.2147/jmdh.s508511

---

### Rank 6: AI-Generated Antibiotic Therapies for Acute Periprosthetic Joint Infections with Implant Retention in Comparison with an Interdisciplinary Team
- **Relevance Score:** 95/100
- **Authors:** A. A. Zellner, Tamaradoubra Tippa Tuburu, Alexander Franz, Jonas Roos, F. Fröschen, G. Hischebeth
- **Year & Journal:** 2025 | *Antibiotics* (SJR Quartile: 1.0)
- **Study Type & Citations:** meta-analysis | Citations: 2
- **Main Takeaway:** AI-generated antibiotic recommendations for periprosthetic joint infections show potential, but current incongruence with experienced interdisciplinary team recommendations hinder clinical implementation.
- **Simple Summary & Project Context:**
  Background: Periprosthetic joint infections (PJI) represent a serious complication following joint arthroplasty and require, in addition to surgical intervention, a targeted antibiotic therapy. The aim of this study was to compare microbiological recommendations for the antibiotic treatment of fictitious PJI patients generated by an artificial intelligence (AI) system with those of an interdisciplinary team (IT) consisting of microbiologists and orthopedic surgeons. The differences between the recommendations suggested by AI and the IT were analyzed with regard to the suggested agents and duration of antibiotic therapy. Methods: Based on meta-analyses, a cohort of 100 fictitious patients with acute early- and acute late-onset PJI was created, reflecting the typical demographic data, comorbidities and pathogen profiles of such a population. This information was input into the AI system ChatGPT (OpenAI, GPT-5 "Thinking mode" accessed via ChatGPT Plus, San Francisco, CA, USA) to generate corresponding recommendations. The objective was to use these profiles to obtain recommendations for definitive antibiotic therapy, including daily dosage, intravenous and oral treatment durations. Simultaneously, the same fictitious patient data were reviewed by the IT to produce their own recommendations. Results: The results revealed both concordances and discrepancies in the selection of antibiotics. Notably, in cases involving multidrug-resistant organisms and more complex clinical scenarios, the AI-generated recommendations were incongruent with those of the IT, with estimated percentage agreement ranging from 0-33%. In straightforward clinical scenarios with monomicrobial infections, AI reached an estimated percentage agreement of up to 57% (95%-CI [0.47-0.67]). Furthermore, AI consistently recommended 12 weeks of therapy duration vs. six weeks usually recommended by the IT. Conclusions: The study provides important insights into the potential and limitations of AI-assisted decision-making models in orthopedic infection treatments. Consultation of AI is universally accessible at all times of day, which may offer a significant advantage in the future for the treatment of PJI. This kind of application will be of particular interest for institutions without in-house microbiology services. However, from our perspective, the current level of incongruence between the AI-generated recommendations and those of an experienced interdisciplinary team remains too high for this approach to be clinically implemented at this time. Furthermore, AI lacks transparency regarding the sources it uses to inform about its decision-making and therapeutic recommendations, currently carries no legal weight and clinical implementation is severely hindered by restrictive privacy laws regarding health care data.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/aigenerated-antibiotic-therapies-for-acute-zellner-tuburu/e473d892220d5c2098f180b27f291b08/) | DOI: 10.3390/antibiotics15010025

---

### Rank 7: Artificial intelligence fails to outperform orthopaedic surgeons: A systematic review
- **Relevance Score:** 90/100
- **Authors:** Jemima Russell, Jamie Rosen, Martinique Vella-Baldacchino
- **Year & Journal:** 2025 | *Journal of Experimental Orthopaedics* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 3
- **Main Takeaway:** AI shows potential in supporting clinical efficiency and patient communication in orthopaedics, but concerns about bias, quality risks, overconfidence, and outdated information prevent it from replacing human expertise.
- **Simple Summary & Project Context:**
  Purpose: Artificial intelligence (AI) in orthopaedic surgery is increasingly applied to analyse clinical data, triage patients and interpret imaging with high accuracy. Orthopaedics surgery faces unique challenges, including high patient volumes, complex cases and prolonged waiting lists, highlighting the need for efficiency and decision support. To justify implementation, AI must demonstrate performance comparable to surgeons. This systematic review evaluates AI's performance relative to surgeons to determine its value as a complementary tool in orthopaedic practice.

Methods: This systematic review was conducted using OVID Medline. Relevant studies published up to 13 August 2025 were identified. Included studies were categorised into decision making, management plans, clinical knowledge, quality control, and answering patients' frequently asked questions (FAQs).

Results: Of 419 identified studies, 16 were eligible. ChatGPT showed high sensitivity in identifying patients achieving clinically meaningful improvements (97% vs. 90% for surgeons) but lower specificity (33% vs. 63%) and accuracy (65% vs. 76%). AI demonstrates comparable or superior performance to surgeons in emergency scenarios and answering patient FAQs, scoring higher across empathy, accuracy, completeness and overall quality (4.4 vs. 3.5-3.7). Residents outperformed AI in examinations (74.2% vs. 47.2%). AI showed limited accuracy in knee osteoarthritis radiographic staging (35% vs. >80%).

Conclusions: AI demonstrates the potential to support clinical efficiency and patient communication in orthopaedics. However, concerns about bias, quality risks, overconfidence and reliance on outdated information prevent it from replacing human expertise. Clinician-led design and validation are required to ensure safe and effective integration into clinical practice.

Level of Evidence: Level IV.

© 2025 The Author(s). Journal of Experimental Orthopaedics published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-fails-to-outperform-orthopaedic-russell-rosen/7a68c6763825543a936c9177f163933c/) | DOI: 10.1002/jeo2.70548

---

### Rank 8: ChatGPT in orthopedics: a narrative review exploring the potential of artificial intelligence in orthopedic practice
- **Relevance Score:** 88/100
- **Authors:** R. Giorgino, Mario Alessandri-Bonetti, A. Luca, Filippo Migliorini, N. Rossi, G. Peretti, L. Mangiavini
- **Year & Journal:** 2023 | *Frontiers in Surgery* (SJR Quartile: 2.0)
- **Study Type & Citations:** literature review | Citations: 66
- **Main Takeaway:** ChatGPT shows potential in orthopedics, but further research and development are needed to ensure its reliability, accuracy, and ethical use in patient care.
- **Simple Summary & Project Context:**
  The field of orthopedics faces complex challenges requiring quick and intricate decisions, with patient education and compliance playing crucial roles in treatment outcomes. Technological advancements in artificial intelligence (AI) can potentially enhance orthopedic care. ChatGPT, a natural language processing technology developed by OpenAI, has shown promise in various sectors, including healthcare. ChatGPT can facilitate patient information exchange in orthopedics, provide clinical decision support, and improve patient communication and education. It can assist in differential diagnosis, suggest appropriate imaging modalities, and optimize treatment plans based on evidence-based guidelines. However, ChatGPT has limitations, such as insufficient expertise in specialized domains and a lack of contextual understanding. The application of ChatGPT in orthopedics is still evolving, with studies exploring its potential in clinical decision-making, patient education, workflow optimization, and scientific literature. The results indicate both the benefits and limitations of ChatGPT, emphasizing the need for caution, ethical considerations, and human oversight. Addressing training data quality, biases, data privacy, and accountability challenges is crucial for responsible implementation. While ChatGPT has the potential to transform orthopedic healthcare, further research and development are necessary to ensure its reliability, accuracy, and ethical use in patient care.

© 2023 Giorgino, Alessandri-Bonetti, Luca, Migliorini, Rossi, Peretti and Mangiavini.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/chatgpt-in-orthopedics-a-narrative-review-exploring-the-giorgino-alessandri-bonetti/bebe084fbef955f2986775a11b68e11f/) | DOI: 10.3389/fsurg.2023.1284015

---

### Rank 9: Arthrosis diagnosis and treatment recommendations in clinical practice: an exploratory investigation with the generative AI model GPT-4
- **Relevance Score:** 88/100
- **Authors:** Stefano Pagano, Sabrina Holzapfel, T. Kappenschneider, Matthias Meyer, G. Maderbacher, Joachim Grifka, D. Holzapfel
- **Year & Journal:** 2023 | *Journal of Orthopaedics and Traumatology : Official Journal of the Italian Society of Orthopaedics and Traumatology* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 41
- **Main Takeaway:** ChatGPT-4 shows potential in diagnosing gonarthrosis and coxarthrosis and aligning treatment recommendations with orthopaedic specialists, but it is not meant to replace seasoned orthopaedic surgeons' expertise.
- **Simple Summary & Project Context:**
  Background: The spread of artificial intelligence (AI) has led to transformative advancements in diverse sectors, including healthcare. Specifically, generative writing systems have shown potential in various applications, but their effectiveness in clinical settings has been barely investigated. In this context, we evaluated the proficiency of ChatGPT-4 in diagnosing gonarthrosis and coxarthrosis and recommending appropriate treatments compared with orthopaedic specialists.

Methods: A retrospective review was conducted using anonymized medical records of 100 patients previously diagnosed with either knee or hip arthrosis. ChatGPT-4 was employed to analyse these historical records, formulating both a diagnosis and potential treatment suggestions. Subsequently, a comparative analysis was conducted to assess the concordance between the AI's conclusions and the original clinical decisions made by the physicians.

Results: In diagnostic evaluations, ChatGPT-4 consistently aligned with the conclusions previously drawn by physicians. In terms of treatment recommendations, there was an 83% agreement between the AI and orthopaedic specialists. The therapeutic concordance was verified by the calculation of a Cohen's Kappa coefficient of 0.580 (p < 0.001). This indicates a moderate-to-good level of agreement. In recommendations pertaining to surgical treatment, the AI demonstrated a sensitivity and specificity of 78% and 80%, respectively. Multivariable logistic regression demonstrated that the variables reduced quality of life (OR 49.97, p < 0.001) and start-up pain (OR 12.54, p = 0.028) have an influence on ChatGPT-4's recommendation for a surgery.

Conclusion: This study emphasises ChatGPT-4's notable potential in diagnosing conditions such as gonarthrosis and coxarthrosis and in aligning its treatment recommendations with those of orthopaedic specialists. However, it is crucial to acknowledge that AI tools such as ChatGPT-4 are not meant to replace the nuanced expertise and clinical judgment of seasoned orthopaedic surgeons, particularly in complex decision-making scenarios regarding treatment indications. Due to the exploratory nature of the study, further research with larger patient populations and more complex diagnoses is necessary to validate the findings and explore the broader potential of AI in healthcare.

Level of evidence: Level III evidence.

© 2023. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/arthrosis-diagnosis-and-treatment-recommendations-in-pagano-holzapfel/107e568650af57938c18272f74d1d571/) | DOI: 10.1186/s10195-023-00740-4

---

### Rank 10: “Dr. AI Will See You Now”: How Do ChatGPT-4 Treatment Recommendations Align With Orthopaedic Clinical Practice Guidelines?
- **Relevance Score:** 88/100
- **Authors:** Tanios Dagher, Emma Dwyer, Hayden P. Baker, S. Kalidoss, Jason A. Strelzow
- **Year & Journal:** 2024 | *Clinical Orthopaedics and Related Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 32
- **Main Takeaway:** ChatGPT-4 can generate accurate treatment plans aligned with clinical practice guidelines, but can make mistakes when integrating multiple patient factors and understanding disease severity and progression.
- **Simple Summary & Project Context:**
  Background: Artificial intelligence (AI) is engineered to emulate tasks that have historically required human interaction and intellect, including learning, pattern recognition, decision-making, and problem-solving. Although AI models like ChatGPT-4 have demonstrated satisfactory performance on medical licensing exams, suggesting a potential for supporting medical diagnostics and decision-making, no study of which we are aware has evaluated the ability of these tools to make treatment recommendations when given clinical vignettes and representative medical imaging of common orthopaedic conditions. As AI continues to advance, a thorough understanding of its strengths and limitations is necessary to inform safe and helpful integration into medical practice.

Questions/purposes: (1) What is the concordance between ChatGPT-4-generated treatment recommendations for common orthopaedic conditions with both the American Academy of Orthopaedic Surgeons (AAOS) clinical practice guidelines (CPGs) and an orthopaedic attending physician's treatment plan? (2) In what specific areas do the ChatGPT-4-generated treatment recommendations diverge from the AAOS CPGs?

Methods: Ten common orthopaedic conditions with associated AAOS CPGs were identified: carpal tunnel syndrome, distal radius fracture, glenohumeral joint osteoarthritis, rotator cuff injury, clavicle fracture, hip fracture, hip osteoarthritis, knee osteoarthritis, ACL injury, and acute Achilles rupture. For each condition, the medical records of 10 deidentified patients managed at our facility were used to construct clinical vignettes that each had an isolated, single diagnosis with adequate clarity. The vignettes also encompassed a range of diagnostic severity to evaluate more thoroughly adherence to the treatment guidelines outlined by the AAOS. These clinical vignettes were presented alongside representative radiographic imaging. The model was prompted to provide a single treatment plan recommendation. Each treatment plan was compared with established AAOS CPGs and to the treatment plan documented by the attending orthopaedic surgeon treating the specific patient. Vignettes where ChatGPT-4 recommendations diverged from CPGs were reviewed to identify patterns of error and summarized.

Results: ChatGPT-4 provided treatment recommendations in accordance with the AAOS CPGs in 90% (90 of 100) of clinical vignettes. Concordance between ChatGPT-generated plans and the plan recommended by the treating orthopaedic attending physician was 78% (78 of 100). One hundred percent (30 of 30) of ChatGPT-4 recommendations for fracture vignettes and hip and knee arthritis vignettes matched with CPG recommendations, whereas the model struggled most with recommendations for carpal tunnel syndrome (3 of 10 instances demonstrated discordance). ChatGPT-4 recommendations diverged from AAOS CPGs for three carpal tunnel syndrome vignettes; two ACL injury, rotator cuff injury, and glenohumeral joint osteoarthritis vignettes; as well as one acute Achilles rupture vignette. In these situations, ChatGPT-4 most often struggled to correctly interpret injury severity and progression, incorporate patient factors (such as lifestyle or comorbidities) into decision-making, and recognize a contraindication to surgery.

Conclusion: ChatGPT-4 can generate accurate treatment plans aligned with CPGs but can also make mistakes when it is required to integrate multiple patient factors into decision-making and understand disease severity and progression. Physicians must critically assess the full clinical picture when using AI tools to support their decision-making.

Clinical relevance: ChatGPT-4 may be used as an on-demand diagnostic companion, but patient-centered decision-making should continue to remain in the hands of the physician.

Copyright © 2024 by the Association of Bone and Joint Surgeons.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/%E2%80%9Cdr-ai-will-see-you-now%E2%80%9D-how-do-chatgpt4-treatment-dagher-dwyer/e45f163f66fa5618ab007992218e5d9c/) | DOI: 10.1097/corr.0000000000003234

---

### Rank 11: Reinforcement Learning-Based Personalized Depression Treatment Using Synthetic Data and Real-Time Decision Support
- **Relevance Score:** 85/100
- **Authors:** R. de Filippis, Abdullah Al Foysal
- **Year & Journal:** 2025 | *OALib* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 0
- **Main Takeaway:** Reinforcement Learning-based personalized depression treatment using synthetic data and real-time decision support can optimize antidepressant treatment strategies, reducing side effects and healthcare costs.
- **Simple Summary & Project Context:**
  Depression treatment often involves a complex and lengthy trial-and-error process, where clinicians sequentially prescribe medications to identify the most effective treatment for each patient.This approach can lead to delayed recovery, unnecessary side effects, and increased healthcare costs.To address this challenge, we present a Reinforcement Learning (RL)-based framework designed to optimize antidepressant treatment strategies through dynamic, patient-specific decision-making.The proposed system leverages synthetically generated patient data to simulate real-world treatment scenarios while ensuring privacy and scalability.A synthetic depression patient simulator was developed to model daily symptom trajectories influenced by medication type, dosage, adherence, side effects, and stochastic life events.This simulated data allowed the training of a deep Q-learning agent within a custom-built reinforcement learning environment.The agent learned to recommend treatment adjustments or continuations based on temporal symptom patterns and treatment history.Key components of the framework include experience replay, target model updates, and an epsilon-greedy exploration strategy to balance exploration and exploitation during training.The system was evaluated using unseen synthetic patients to assess generalization performance.Comprehensive visual analyses were conducted to characterize the symptom distribution, medication assignment, agent reward dynamics, and real-time treatment recommendations.The real-time recommendation system demonstrated the ability to provide timely, personalized treatment suggestions, switching medications when appropriate and maintaining stability when patient symptoms improved.The model's decision-making process is closely aligned with clinical reasoning, supporting its potential as a decision support tool in precision psychiatry.This study offers a privacypreserving, scalable, and clinically relevant pathway for optimizing depression How to cite this paper: de
- **Reference Link:** [Consensus Link](https://consensus.app/papers/reinforcement-learningbased-personalized-depression-filippis-foysal/df9cfaa7520e592394c4a2101967f0b6/) | DOI: 10.4236/oalib.1113959

---

### Rank 12: Personalized Antidepressant Treatment Recommendation Using Reinforcement Learning and Predictive Modelling on Synthetic Patient Data
- **Relevance Score:** 80/100
- **Authors:** R. de Filippis, Abdullah Al Foysal
- **Year & Journal:** 2025 | *OALib* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 0
- **Main Takeaway:** This study developed a clinical decision support system that personalizes antidepressant treatment selection using synthetic patient data, predictive modeling, and reinforcement learning, aiming to reduce patient suffering and improve treatment success.
- **Simple Summary & Project Context:**
  This study presents a comprehensive clinical decision support system aimed at personalizing antidepressant treatment selection using synthetic patient data, predictive modelling, and reinforcement learning.Traditional antidepressant prescribing often relies on trial-and-error methods, which can result in prolonged patient suffering and delayed treatment success, particularly in treatment-resistant depression.To address the limitations posed by data scarcity and privacy constraints in psychiatric research, we developed a robust synthetic patient data generator that simulates realistic clinical, genetic, and treatment response profiles.These synthetic datasets capture essential features such as age, gender, baseline depression severity, genetic markers (5HTTLPR, BDNF, COMT, FKBP5), treatment history, and comorbidities including anxiety and chronic pain.We employed Gradient Boosting and Neural Network classifiers to predict treatment response probabilities based on individual patient profiles.These models achieved moderate classification accuracy, with a tendency to predict responders more reliably than non-responders.To further optimize treatment strategies, we integrated a Dueling DQN Reinforcement Learning agent trained within a custom-designed environment that simulates multi-step treatment processes, side effect profiles, and severity progression.While the reinforcement learning agent successfully optimized sequential treatment selections and reduced symptom severity, it did not achieve remission under the current reward configuration, suggesting the need for further reward function tuning.An enhanced clinical decision support system was developed to generate top treatment recommendations with natural language explanations, facilitating transparent and interpretable clinical guidance.This research demonstrates the po-How to cite this paper: de
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-antidepressant-treatment-recommendation-filippis-foysal/300781caf22a571891d5feb3f8306cd5/) | DOI: 10.4236/oalib.1113957

---

### Rank 13: A Doctor Assistance Tool: Personalized Healthcare Treatment Recommendations Journey from Deep Reinforcement Learning to Generative AI
- **Relevance Score:** 78/100
- **Authors:** Gautam Kumar
- **Year & Journal:** 2024 | *2024 3rd Edition of IEEE Delhi Section Flagship Conference (DELCON)* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 4
- **Main Takeaway:** The Personalized Treatment Healthcare Recommendation System (PTHRS) outperforms baseline Deep Reinforcement Learning techniques in personalized treatment recommendations, achieving an accuracy of 66% and clinical validation success rate of 80%.
- **Simple Summary & Project Context:**
  In personalized patient healthcare treatment recommendation, the goal is to recommend the most suitable course of treatment for an individual patient based on patient-specific data, including prior medical history, electronic health records (EHR), genetic information, lifestyle factors, and treatment outcomes. This study aims to extend the paradigm of personalized treatment recommendations from Deep Reinforcement Learning (DRL) to Generative Artificial Intelligence (GenAI). A DRL algorithm is employed to derive the best policy for personalized treatment recommendations. At the same time, the Med-PaLM-2 large language model (LLM) is used to generate diagnosis reports tailored to the individual patient. I propose a Personalized Treatment Healthcare Recommendation System (PTHRS), using a fine-tuned Med-PaLM-2 model on the Intensive Care Unit (ICU) dataset and the Medical Information Mart for Intensive Care (MIMIC-III) dataset. The system is designed to formulate the best treatment policies and generate clinical documentation, including discharge summaries, progress notes, customer care notes, treatments, healthcare, medication, doctor consultations, nutrition, exercise, and medical reports. These documents capture essential information and generate personalized recommendations for diagnosis and treatment plans. Experimental results prove that the model achieves an accuracy of 66%, a BLEU score of 0.66, and a clinical validation success rate of 80%, outperforming baseline DRL techniques in generating the best policies for personalized treatment recommendations.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-doctor-assistance-tool-personalized-healthcare-kumar/02cce44ac31d5196b03b79ec222e7810/) | DOI: 10.1109/delcon64804.2024.10866814

---

### Rank 14: Biopsychosocial based machine learning models predict patient improvement after total knee arthroplasty
- **Relevance Score:** 70/100
- **Authors:** Karen Ribbons, Jodie A. Cochrane, Sarah Johnson, Adrian Wills, Elizabeth Ditton, David Dewar, M. Broadhead, I. Chan, M. Dixon, C. Dunkley, Richard Harbury, Aleksandar Jovanović, A. Leong, P. Summersell, C. Todhunter, R. Verheul, Michael Pollack, Rohan Walker, Michael Nilsson
- **Year & Journal:** 2025 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 8
- **Main Takeaway:** Machine learning models using biopsychosocial features can predict patient improvement in quality-of-life and knee symptomology after total knee arthroplasty.
- **Simple Summary & Project Context:**
  Total knee arthroplasty (TKA) is an effective treatment for end stage osteoarthritis. However, biopsychosocial features are not routinely considered in TKA clinical decision-making, despite increasing evidence to support their role in patient recovery. We have developed a more holistic model of patient care by using machine learning and Bayesian inference methods to build patient-centred predictive models, enhanced by a comprehensive battery of biopsychosocial features. Data from 863 patients with TKA (mean age 68 years (SD 8), 50% women), identified between 2019 and 2022 from four hospitals in NSW, Australia, was included in model development. Predictive models for improvement in patient quality-of-life and knee symptomology at three months post-TKA were developed, as measured by a change in the Short Form-12 Physical Composite Score (PCS) or Western Ontario and McMasters Universities Osteoarthritis Index (WOMAC), respectively. Retained predictive variables in the quality-of-life model included pre-surgery PCS, knee symptomology, nutrition, alcohol consumption, employment, committed action, pain improvement expectation, pain in other places, and hand grip strength. Retained variables for the knee symptomology model were comparable, but also included pre-surgery WOMAC, pain catastrophizing, and exhaustion. Bayesian machine learning methods generated predictive distributions, enabling outcomes and uncertainty to be determined on an individual basis to further inform decision-making.

© 2025. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/biopsychosocial-based-machine-learning-models-predict-ribbons-cochrane/e0648fa9ab8853c7b371c0cd2c7106fe/) | DOI: 10.1038/s41598-025-88560-w

---

### Rank 15: Artificial Intelligence in Orthopaedics: Clinical Performance, Limitations, and Translational Readiness—A Review
- **Relevance Score:** 70/100
- **Authors:** W. Glinkowski, Antonina Spalińska, Agnieszka Wołk, Krzysztof Wołk
- **Year & Journal:** 2026 | *Journal of Clinical Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 7
- **Main Takeaway:** AI in orthopaedics shows promise in detecting bone fractures and improving preoperative planning, but its widespread use is limited by limited multicenter validation, dataset bias, algorithmic opacity, and immature regulatory frameworks.
- **Simple Summary & Project Context:**
  Background/Objectives: Musculoskeletal disorders and their surgical treatment significantly affect global disability, healthcare utilization, and costs. Artificial intelligence (AI) is a key enabler of data-driven musculoskeletal care. Their applications include diagnostic imaging, surgical planning, risk prediction, rehabilitation, and digital health ecosystems. This narrative review synthesizes current evidence on the use of AI in orthopaedics and musculoskeletal care across five areas: diagnostic imaging, surgical planning and intraoperative augmentation, predictive analytics and patient-reported outcomes, rehabilitation intelligence and teleorthopaedics, and system-level management. An additional task is to identify translational gaps and priorities for safe, ethical, and equitable implementation of AI. Methods: A structured narrative review was conducted using targeted searches in PubMed, Scopus, and Web of Science supplemented by semantic and citation-based explorations in Semantic Scholar, OpenAlex, and Google Scholar. The main search period was January 2019 to December 2025. The retrieved peer-reviewed articles were analyzed for clinical relevance to human musculoskeletal care, quantitative outcomes, and the translational implications of the results. From the broader pool of eligible publications, 40 clinically relevant studies were selected for detailed synthesis covering imaging, surgical planning, predictive modeling, rehabilitation, and system-level applications. Owing to the significant heterogeneity in the model architectures, datasets, and endpoints, the results were organized into five predefined thematic areas. Results: The most mature evidence is for AI-assisted detection of bone fractures on radiographs, identification of implants, and use of sizing templates in preoperative planning for arthroplasty, where deep learning systems have achieved expert-level diagnostic performance (e.g., fracture detection sensitivity of approximately 90% and specificity of approximately 92% and implant identification accuracy of 97-99%) and improved the accuracy of preoperative planning compared to conventional templating. AI-based planning increases the likelihood of reducing intraoperative corrections, shortening surgery time, reducing blood loss, and improving the final functional outcomes. Predictive models can support the stratification of risk for complications, rehospitalizations, and patient-reported outcomes, although external validation remains limited and is often single-center at this stage of research. Emerging applications in rehabilitation and teleorthopaedics, including sensor-based monitoring and learning systems integrated with Patient-Reported Outcome Measures (PROMs), are conceptually promising, but are mainly limited to feasibility or pilot studies. Conclusions: AI is beginning to influence musculoskeletal care, moving beyond pattern recognition toward integrated, patient-centered decision support throughout the perioperative and rehabilitation periods. Its widespread use remains constrained by limited multicenter validation, dataset bias, algorithmic opacity, and immature regulatory and governance frameworks. Future work should prioritize prospective multicenter impact studies, repeatable revalidation of local models, integration of PROM and teleorthopedic data with health learning systems, and adaptation to changing regulatory requirements to enable safe, ethical, effective, and equitable implementation in routine orthopedic practice.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-orthopaedics-clinical-glinkowski-spali%C5%84ska/809c2851e6c8596a851661bb9693eb0b/) | DOI: 10.3390/jcm15051751

---

### Rank 16: Personalized Diabetes Treatment Support Using Large Language Models Fine-Tuned on Electronic Health Records: Development and Evaluation Study
- **Relevance Score:** 70/100
- **Authors:** Sheng He, Yu Zhang, Jiaxi Li
- **Year & Journal:** 2026 | *JMIR Formative Research* (SJR Quartile: 2.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** Fine-tuned GLM4-9B shows strong potential as a clinical decision support tool for personalized diabetes care, providing reference recommendations that may improve clinician efficiency and decision quality.
- **Simple Summary & Project Context:**
  Background: Effective diabetes management requires individualized treatment strategies tailored to patients' clinical characteristics. With recent advances in artificial intelligence, large language models (LLMs) offer new opportunities to enhance clinical decision support, particularly in generating personalized recommendations.

Objective: This study aimed to develop and evaluate an LLM-based outpatient treatment support system for diabetes and examine its potential value in routine clinical decision-making.

Methods: Three compact LLMs (Llama 3.1-8B, Qwen3-8B, and GLM4-9B) were fine-tuned on deidentified outpatient electronic health records using a parameter-efficient low-rank adaptation approach. The optimized models were embedded into a prototype hospital information system via a retrieval-augmented generation framework to generate individualized treatment recommendations, laboratory test suggestions, and medication prompts based on demographic and clinical data.

Results: Among the models evaluated, the fine-tuned GLM4-9B demonstrated the strongest performance, producing clinically reasonable treatment plans and appropriate laboratory test recommendations and medication suggestions. It achieved a mean Bilingual Evaluation Understudy for 4-grams score of 67.93 (SD 2.74) and mean scores of 44.30 (SD 3.91) for Recall-Oriented Understudy for Gisting Evaluation for overlap of unigrams, 27.34 (SD 1.85) for Recall-Oriented Understudy for Gisting Evaluation for overlap of bigrams, and 37.67 (SD 2.88) for Recall-Oriented Understudy for Gisting Evaluation for Longest Common Subsequence.

Conclusions: The fine-tuned GLM4-9B shows strong potential as a clinical decision support tool for personalized diabetes care. It can provide reference recommendations that may improve clinician efficiency and support decision quality. Future work should focus on enhancing medication guidance, expanding data sources, and improving adaptability in cases involving complex comorbidities.

© Shenyang He, Yu Zhang, Jiaxi Li. Originally published in JMIR Formative Research (https://formative.jmir.org).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-diabetes-treatment-support-using-large-he-zhang/cbbf59459108564bba29cb205d9505d3/) | DOI: 10.2196/71541

---

### Rank 17: Predicting patient outcomes and risk for revision surgery after hip and knee replacement surgery: study protocol for a comparison of modelling approaches using the Swiss National Joint Registry (SIRIS)
- **Relevance Score:** 70/100
- **Authors:** Léonie Hofstetter, Nathalie Schweyckart, C. Seiler, Christian Brand, L. Rosella, Mazda Farshad, M. Puhan, C. Hincapié
- **Year & Journal:** 2025 | *Diagnostic and Prognostic Research* (SJR Quartile: Not specified)
- **Study Type & Citations:** other | Citations: 3
- **Main Takeaway:** Machine learning algorithms can improve the prediction of patient outcomes and revision surgery risk after hip and knee replacement surgery, but their performance needs further validation.
- **Simple Summary & Project Context:**
  Background: Prediction of postoperative patient-reported outcomes and risk for revision surgery after total hip arthroplasty (THA) or total knee arthroplasty (TKA) can inform clinical decision-making, health resource allocation, and care planning. Machine learning (ML) algorithms are increasingly used as an alternative to traditional logistic regression (LR) prediction, but there is uncertainty about their superiority in overall model performance. The aim of this study is to compare the predictive performance of LR with different ML approaches for predicting patient outcomes and risk for revision surgery after THA and TKA.

Methods: A population-based historical cohort study will be developed using routinely collected data from all primary and revision THA and TKA procedures performed in Switzerland and registered in the Swiss National Joint Registry (SIRIS). Patients of age ≥ 18 years with surgery for primary osteoarthritis from 01 January 2015 up to 31 December 2023 will be included. Outcomes of interest will be (1) 12-month postoperative poor pain outcome (defined as < 50% improvement of pain or < 3 absolute reduction in pain on a 11-point (0 to 10) numeric rating scale) and poor satisfaction outcome, and (2) early revision within 5 years after primary surgery. Prespecified predictor variables will include demographic characteristics, comorbidity score, patient-reported health status measures, and surgical variables. Measures of overall predictive accuracy, discrimination, and calibration will be used to compare predictive performance, and decision curve analysis performed to evaluate the clinical usefulness of models. The models will be internally validated using cross-validation and externally validated using geographical validation. Development of the models will be informed by the updated Transparent Reporting of a multivariable prediction model for Individual Prognosis or Diagnosis (TRIPOD + AI) statement.

Discussion: This study will develop, validate, and compare prediction models for postoperative patient-reported outcomes and risk for revision surgery after THA and TKA using SIRIS data.

© 2025. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/predicting-patient-outcomes-and-risk-for-revision-surgery-hofstetter-schweyckart/2827356bab4153f79920c53f77c97c0b/) | DOI: 10.1186/s41512-025-00200-z

---

### Rank 18: Artificial intelligence models cannot yet replace experts in providing patient education for shoulder and elbow orthopaedic pathologies: a systematic review and meta-analysis
- **Relevance Score:** 70/100
- **Authors:** J. Dworsky-Fried, Matthew Mellon, Preksha Rathod, James Yan, Moin Khan
- **Year & Journal:** 2026 | *Annals of Joint* (SJR Quartile: 3.0)
- **Study Type & Citations:** meta-analysis | Citations: 2
- **Main Takeaway:** AI algorithms show promising accuracy in providing patient education for shoulder and elbow orthopaedic pathologies, but should not replace experts due to poor readability, quality, and value.
- **Simple Summary & Project Context:**
  Background: AI and machine learning (ML) have diverse applications in orthopedic surgery, such as for diagnosis of disease, surgical assistance, and outcome prediction. When used as adjuncts, AI has a potential to reduce clinical workload, improve workflow and aid in clinical decision making. The objective of this systematic review is to evaluate current literature on artificial intelligence (AI) to assess effectiveness in developing responses to inquiries related to orthopaedic upper extremity pathologies.

Methods: Three databases (PubMed, MEDLINE, EMBASE) were searched for studies involving AI and questions in shoulder and elbow orthopedics. Inclusion criteria included papers related to shoulder and elbow, human studies, use of AI models, published in English language and at any level of evidence. Data on response accuracy, reliability and quality, as well as area under the curve (AUC) of the given AI algorithm, were recorded. Meta-analyses were conducted on both the accuracy and AUC of AI algorithms on relevant studies. Risk of bias was assessed using the Quality Assessment of Diagnostic Accuracy Studies (QUADAS-2).

Results: A total of 16 studies were included in this review. Nine studies used a version of ChatGPT, one study used GoogleBard, and the remaining seven studies used a variety of AI learning models. The overall pooled accuracy of responses developed by AI models was 78%, and the pooled mean AUC of included AI algorithms was 86%. AI algorithms performed inferiorly compared to experts. The overall quality and readability of AI responses were poor.

Conclusions: AI algorithms assessed in our study demonstrated a promising degree of accuracy and performance. However, AI responses were found to be inferior to experts and had poor readability, quality, and value to the patient. In its current state of technology, AI is a powerful tool that can be used in conjunction with experts to augment patient education, however, it should not be utilized independently.

© AME Publishing Company.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-models-cannot-yet-replace-dworsky-fried-mellon/b83506a6fd3c52a78d7acc130a3afb3d/) | DOI: 10.21037/aoj-25-38

---

### Rank 19: Artificial intelligence in orthopaedics: Clinical decision support, medical imaging, surgical planning, and outcome prediction
- **Relevance Score:** 70/100
- **Authors:** Anirudh Dwajan, Dr. Manas Ranjan Patro, Amber Agarwal, Mary Lalhmingmawii
- **Year & Journal:** 2026 | *World Journal of Clinical Cases* (SJR Quartile: Not specified)
- **Study Type & Citations:** literature review | Citations: 1
- **Main Takeaway:** AI is revolutionizing orthopaedic practice by improving diagnostic accuracy, clinical decision-making, surgical planning, and postoperative monitoring, but its widespread adoption faces challenges.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) is increasingly transforming orthopaedic practice by enhancing diagnostic accuracy, clinical decision-making, surgical planning, and postoperative monitoring. Advances in computational modelling, imaging analysis, and predictive analytics now enable clinicians to process complex multimodal datasets derived from radiological imaging, clinical records, biomechanical parameters, and patient-reported outcomes. These technologies are being applied across multiple orthopaedic subspecialties, including trauma, spine surgery, arthroplasty, sports medicine, oncology, infection, and rehabilitation. AI-driven systems have demonstrated strong performance in fracture detection, implant assessment, tumour characterisation, infection diagnosis, and prediction of surgical outcomes, often matching or exceeding conventional analytical approaches. In operative settings, integration with robotics, navigation platforms, and augmented visualisation systems improves procedural precision, reproducibility, and intraoperative decision support. Predictive models also assist clinicians in risk stratification, patient selection, complication forecasting, and personalised rehabilitation planning. Despite these promising developments, widespread clinical implementation remains limited by challenges related to dataset variability, algorithm transparency, regulatory oversight, cost, and concerns regarding bias and data privacy. Ongoing multicentre validation studies, development of explainable computational frameworks, and global collaboration will be essential for safe and equitable adoption. AI is unlikely to replace orthopaedic clinicians but is expected to function as a powerful adjunct that enhances clinical judgement and supports precision-based musculoskeletal care. Continued technological refinement and responsible integration into clinical workflows will determine its long-term impact on patient outcomes and healthcare delivery.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-orthopaedics-clinical-dwajan-patro/06455aa630665a8e8e04229cf21cbc0f/) | DOI: 10.12998/wjcc.v14.i17.120192

---

### Rank 20: Explainable machine learning for orthopedic decision-making: predicting functional outcomes of total hip replacement from gait biomechanics
- **Relevance Score:** 70/100
- **Authors:** B. Stetter, J. Dully, Felix Stief, Jana Holder, H. Steingrebe, F. Zaucke, Stefan Sell, S. van Drongelen, Thorsten Stein
- **Year & Journal:** 2025 | *Arthritis Research & Therapy* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 1
- **Main Takeaway:** Machine learning can help predict postoperative gait recovery in hip osteoarthritis patients, potentially guiding personalized treatment strategies.
- **Simple Summary & Project Context:**
  This study aimed to identify subpopulations of patients with hip osteoarthritis who exhibit distinct adaptations in gait biomechanics, and to evaluate subpopulation-specific effects of total hip replacement on gait biomechanics. Three datasets were analyzed: (1) a cohort of 109 unilateral hip osteoarthritis patients before total hip replacement, (2) a subset of the first dataset of 63 patients re-evaluated after total hip replacement and (3) a control group of 56 healthy individuals. For all participants, three-dimensional joint angle and moment waveforms of the pelvis, ipsilateral hip and knee, as well as sagittal-plane ankle motion and the foot progression angle, were obtained. The analytical framework integrated k-means clustering, support vector machine classifiers, Shapley Additive exPlanations, and statistical waveform analyses. Clustering of the pre-operative dataset revealed three distinct subpopulations characterized by unique patterns in gait kinematics and joint moments. These subpopulations also differed in age, Kellgren-Lawrence score, and walking speed. Prior to total hip replacement, between 51.4% and 85.2% of hip osteoarthritis patients were classified as pathologic; following surgery, this proportion decreased to 27.8% - 51.8%. Hip flexion and rotation angles and moments were identified as the most important features for patient classification. The magnitude of gait improvement after total hip replacement varied across subpopulations, indicating subpopulation-specific responses to surgical intervention. In conclusion, patients with hip osteoarthritis demonstrate distinct subpopulation-specific gait adaptations, both before and after total hip replacement. Preoperative classification of patients into the identified subpopulations using machine learning approaches may facilitate the prediction of postoperative gait recovery and support the development of personalized treatment and rehabilitation strategies.

© 2025. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/explainable-machine-learning-for-orthopedic-stetter-dully/374cab1e99165e43b4bf9003236ed0b8/) | DOI: 10.1186/s13075-025-03709-2

---

### Rank 21: Prior-informed optimization of treatment recommendation via bandit algorithms trained on large language model-processed historical records
- **Relevance Score:** 70/100
- **Authors:** Saman Nessari, Ali Bozorgi-Amiri
- **Year & Journal:** 2025 | *ArXiv* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 1
- **Main Takeaway:** Our system combines Large Language Models, CTGANs, T-learners, and contextual bandits to provide customized treatment recommendations for individual patients, outperforming other reference methods.
- **Simple Summary & Project Context:**
  Current medical practice depends on standardized treatment frameworks and empirical methodologies that neglect individual patient variations, leading to suboptimal health outcomes. We develop a comprehensive system integrating Large Language Models (LLMs), Conditional Tabular Generative Adversarial Networks (CTGAN), T-learner counterfactual models, and contextual bandit approaches to provide customized, data-informed clinical recommendations. The approach utilizes LLMs to process unstructured medical narratives into structured datasets (93.2% accuracy), uses CTGANs to produce realistic synthetic patient data (55% accuracy via two-sample verification), deploys T-learners to forecast patient-specific treatment responses (84.3% accuracy), and integrates prior-informed contextual bandits to enhance online therapeutic selection by effectively balancing exploration of new possibilities with exploitation of existing knowledge. Testing on stage III colon cancer datasets revealed that our KernelUCB approach obtained 0.60-0.61 average reward scores across 5,000 rounds, exceeding other reference methods. This comprehensive system overcomes cold-start limitations in online learning environments, improves computational effectiveness, and constitutes notable progress toward individualized medicine adapted to specific patient characteristics.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/priorinformed-optimization-of-treatment-recommendation-nessari-bozorgi-amiri/a4116cb68b5354cd8bd3ba41262e1b1b/) | DOI: 10.48550/arxiv.2510.19014

---

### Rank 22: Can Machine Learning Algorithms Predict Which Patients Will Achieve Minimally Clinically Important Differences From Total Joint Arthroplasty?
- **Relevance Score:** 65/100
- **Authors:** M. Fontana, S. Lyman, G. K. Sarker, D. Padgett, C. MacLean
- **Year & Journal:** 2019 | *Clinical Orthopaedics and Related Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 169
- **Main Takeaway:** Machine learning algorithms can predict 2-year postsurgical minimally clinically important differences in total joint arthroplasty patients, potentially improving clinical decision-making and patient care.
- **Simple Summary & Project Context:**
  Background: Identifying patients at risk of not achieving meaningful gains in long-term postsurgical patient-reported outcome measures (PROMs) is important for improving patient monitoring and facilitating presurgical decision support. Machine learning may help automatically select and weigh many predictors to create models that maximize predictive power. However, these techniques are underused among studies of total joint arthroplasty (TJA) patients, particularly those exploring changes in postsurgical PROMs. QUESTION/PURPOSES: (1) To evaluate whether machine learning algorithms, applied to hospital registry data, could predict patients who would not achieve a minimally clinically important difference (MCID) in four PROMs 2 years after TJA; (2) to explore how predictive ability changes as more information is included in modeling; and (3) to identify which variables drive the predictive power of these models.

Methods: Data from a single, high-volume institution's TJA registry were used for this study. We identified 7239 hip and 6480 knee TJAs between 2007 and 2012, which, for at least one PROM, patients had completed both baseline and 2-year followup surveys (among 19,187 TJAs in our registry and 43,313 total TJAs). In all, 12,203 registry TJAs had valid SF-36 physical component scores (PCS) and mental component scores (MCS) at baseline and 2 years; 7085 and 6205 had valid Hip and Knee Disability and Osteoarthritis Outcome Scores for joint replacement (HOOS JR and KOOS JR scores), respectively. Supervised machine learning refers to a class of algorithms that links a mapping of inputs to an output based on many input-output examples. We trained three of the most popular such algorithms (logistic least absolute shrinkage and selection operator (LASSO), random forest, and linear support vector machine) to predict 2-year postsurgical MCIDs. We incrementally considered predictors available at four time points: (1) before the decision to have surgery, (2) before surgery, (3) before discharge, and (4) immediately after discharge. We evaluated the performance of each model using area under the receiver operating characteristic (AUROC) statistics on a validation sample composed of a random 20% subsample of TJAs excluded from modeling. We also considered abbreviated models that only used baseline PROMs and procedure as predictors (to isolate their predictive power). We further directly evaluated which variables were ranked by each model as most predictive of 2-year MCIDs.

Results: The three machine learning algorithms performed in the poor-to-good range for predicting 2-year MCIDs, with AUROCs ranging from 0.60 to 0.89. They performed virtually identically for a given PROM and time point. AUROCs for the logistic LASSO models for predicting SF-36 PCS 2-year MCIDs at the four time points were: 0.69, 0.78, 0.78, and 0.78, respectively; for SF-36 MCS 2-year MCIDs, AUROCs were: 0.63, 0.89, 0.89, and 0.88; for HOOS JR 2-year MCIDs: 0.67, 0.78, 0.77, and 0.77; for KOOS JR 2-year MCIDs: 0.61, 0.75, 0.75, and 0.75. Before-surgery models performed in the fair-to-good range and consistently ranked the associated baseline PROM as among the most important predictors. Abbreviated LASSO models performed worse than the full before-surgery models, though they retained much of the predictive power of the full before-surgery models.

Conclusions: Machine learning has the potential to improve clinical decision-making and patient care by helping to prioritize resources for postsurgical monitoring and informing presurgical discussions of likely outcomes of TJA. Applied to presurgical registry data, such models can predict, with fair-to-good ability, 2-year postsurgical MCIDs. Although we report all parameters of our best-performing models, they cannot simply be applied off-the-shelf without proper testing. Our analyses indicate that machine learning holds much promise for predicting orthopaedic outcomes. LEVEL OF EVIDENCE: Level III, diagnostic study.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/can-machine-learning-algorithms-predict-which-patients-fontana-lyman/ba7b631f1e32547d9d65691e8c192ace/) | DOI: 10.1097/corr.0000000000000687

---

### Rank 23: Predicting patient-reported outcomes following hip and knee replacement surgery using supervised machine learning
- **Relevance Score:** 65/100
- **Authors:** Manuel B. Huber, Christoph F. Kurz, R. Leidl
- **Year & Journal:** 2019 | *BMC Medical Informatics and Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 112
- **Main Takeaway:** Supervised machine-learning implementations like extreme gradient boosting can provide better performance than linear models for predicting patient-reported outcomes after hip and knee replacement surgery.
- **Simple Summary & Project Context:**
  Background: Machine-learning classifiers mostly offer good predictive performance and are increasingly used to support shared decision-making in clinical practice. Focusing on performance and practicability, this study evaluates prediction of patient-reported outcomes (PROs) by eight supervised classifiers including a linear model, following hip and knee replacement surgery.

Methods: NHS PRO data (130,945 observations) from April 2015 to April 2017 were used to train and test eight classifiers to predict binary postoperative improvement based on minimal important differences. Area under the receiver operating characteristic, J-statistic and several other metrics were calculated. The dependent outcomes were generic and disease-specific improvement based on the EQ-5D-3L visual analogue scale (VAS) as well as the Oxford Hip and Knee Score (Q score).

Results: The area under the receiver operating characteristic of the best training models was around 0.87 (VAS) and 0.78 (Q score) for hip replacement, while it was around 0.86 (VAS) and 0.70 (Q score) for knee replacement surgery. Extreme gradient boosting, random forests, multistep elastic net and linear model provided the highest overall J-statistics. Based on variable importance, the most important predictors for post-operative outcomes were preoperative VAS, Q score and single Q score dimensions. Sensitivity analysis for hip replacement VAS evaluated the influence of minimal important difference, patient selection criteria as well as additional data years. Together with a small benchmark of the NHS prediction model, robustness of our results was confirmed.

Conclusions: Supervised machine-learning implementations, like extreme gradient boosting, can provide better performance than linear models and should be considered, when high predictive performance is needed. Preoperative VAS, Q score and specific dimensions like limping are the most important predictors for postoperative hip and knee PROMs.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/predicting-patientreported-outcomes-following-hip-and-huber-kurz/89d4e66bf53650cbb4cac79a73c6f004/) | DOI: 10.1186/s12911-018-0731-6

---

### Rank 24: What Is the Accuracy of Three Different Machine Learning Techniques to Predict Clinical Outcomes After Shoulder Arthroplasty?
- **Relevance Score:** 65/100
- **Authors:** Vikas Kumar, Christopher P. Roche, Steve Overman, Ryan W. Simovitch, P. Flurin, T. Wright, J. Zuckerman, Howard D. Routman, Ankur Teredesai
- **Year & Journal:** 2020 | *Clinical Orthopaedics & Related Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 65
- **Main Takeaway:** Machine learning techniques can accurately predict clinical outcomes after shoulder arthroplasty and accurately risk-stratify patients, aiding in decision-making for improved outcomes.
- **Simple Summary & Project Context:**
  Background: Machine learning techniques can identify complex relationships in large healthcare datasets and build prediction models that better inform physicians in ways that can assist in patient treatment decision-making. In the domain of shoulder arthroplasty, machine learning appears to have the potential to anticipate patients' results after surgery, but this has not been well explored.

Questions/purposes: (1) What is the accuracy of machine learning to predict the American Shoulder and Elbow Surgery (ASES), University of California Los Angeles (UCLA), Constant, global shoulder function, and VAS pain scores, as well as active abduction, forward flexion, and external rotation at 1 year, 2 to 3 years, 3 to 5 years, and more than 5 years after anatomic total shoulder arthroplasty (aTSA) or reverse total shoulder arthroplasty (rTSA)? (2) What is the accuracy of machine learning to identify whether a patient will achieve clinical improvement that exceeds the minimum clinically important difference (MCID) threshold for each outcome measure? (3) What is the accuracy of machine learning to identify whether a patient will achieve clinical improvement that exceeds the substantial clinical benefit threshold for each outcome measure?

Methods: A machine learning analysis was conducted on a database of 7811 patients undergoing shoulder arthroplasty of one prosthesis design to create predictive models for multiple clinical outcome measures. Excluding patients with revisions, fracture indications, and hemiarthroplasty resulted in 6210 eligible primary aTSA and rTSA patients, of whom 4782 patients with 11,198 postoperative follow-up visits had sufficient preoperative, intraoperative, and postoperative data to train and test the predictive models. Preoperative clinical data from 1895 primary aTSA patients and 2887 primary rTSA patients were analyzed using three commercially available supervised machine learning techniques: linear regression, XGBoost, and Wide and Deep, to train and test predictive models for the ASES, UCLA, Constant, global shoulder function, and VAS pain scores, as well as active abduction, forward flexion, and external rotation. Our primary study goal was to quantify the accuracy of three machine learning techniques to predict each outcome measure at multiple postoperative timepoints after aTSA and rTSA using the mean absolute error between the actual and predicted values. Our secondary study goals were to identify whether a patient would experience clinical improvement greater than the MCID and substantial clinical benefit anchor-based thresholds of patient satisfaction for each outcome measure as quantified by the model classification parameters of precision, recall, accuracy, and area under the receiver operating curve.

Results: Each machine learning technique demonstrated similar accuracy to predict each outcome measure at each postoperative point for both aTSA and rTSA, though small differences in prediction accuracy were observed between techniques. Across all postsurgical timepoints, the Wide and Deep technique was associated with the smallest mean absolute error and predicted the postoperative ASES score to ± 10.1 to 11.3 points, the UCLA score to ± 2.5 to 3.4, the Constant score to ± 7.3 to 7.9, the global shoulder function score to ± 1.0 to 1.4, the VAS pain score to ± 1.2 to 1.4, active abduction to ± 18 to 21°, forward elevation to ± 15 to 17°, and external rotation to ± 10 to 12°. These models also accurately identified the patients who did and did not achieve clinical improvement that exceeded the MCID (93% to 99% accuracy for patient-reported outcome measures (PROMs) and 85% to 94% for pain, function, and ROM measures) and substantial clinical benefit (82% to 93% accuracy for PROMs and 78% to 90% for pain, function, and ROM measures) thresholds.

Conclusions: Machine learning techniques can use preoperative data to accurately predict clinical outcomes at multiple postoperative points after shoulder arthroplasty and accurately risk-stratify patients by preoperatively identifying who may and who may not achieve MCID and substantial clinical benefit improvement thresholds for each outcome measure.

Clinical relevance: Three different commercially available machine learning techniques were used to train and test models that predicted clinical outcomes after aTSA and rTSA; this device-type comparison was performed to demonstrate how predictive modeling techniques can be used in the near future to help answer unsolved clinical questions and augment decision-making to improve outcomes after shoulder arthroplasty.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/what-is-the-accuracy-of-three-different-machine-learning-kumar-roche/d7f8f169aa5e54b697d5563f685ce407/) | DOI: 10.1097/corr.0000000000001263

---

### Rank 25: Advanced decision‐making using patient‐reported outcome measures in total joint replacement
- **Relevance Score:** 65/100
- **Authors:** P. Jayakumar, K. Bozic
- **Year & Journal:** 2020 | *Journal of Orthopaedic Research®* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 53
- **Main Takeaway:** A shared decision-making tool using patient-reported outcomes and clinical data can personalize total joint replacement risks and benefits, improving decision quality and patient satisfaction.
- **Simple Summary & Project Context:**
  Up to one-third of total joint replacement (TJR) procedures may be performed inappropriately in a subset of patients who remain dissatisfied with their outcomes, stressing the importance of shared decision-making. Patient-reported outcome measures capture physical, emotional, and social aspects of health and wellbeing from the patient's perspective. Powerful computer systems capable of performing highly sophisticated analysis using different types of data, including patient-derived data, such as patient-reported outcomes, may eliminate guess work, generating impactful metrics to better inform the decision-making process. We have created a shared decision-making tool which generates personalized predictions of risks and benefits from TJR based on patient-reported outcomes as well as clinical and demographic data. We present the protocol for a randomized controlled trial designed to assess the impact of this tool on decision quality, level of shared decision-making, and patient and process outcomes. We also discuss current concepts in this field and highlight opportunities leveraging patient-reported data and artificial intelligence for decision support across the care continuum.

© 2020 Orthopaedic Research Society. Published by Wiley Periodicals, Inc.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/advanced-decision%E2%80%90making-using-patient%E2%80%90reported-jayakumar-bozic/2fb746e1d02b5d208e1d3e2598cf5aea/) | DOI: 10.1002/jor.24614

---

### Rank 26: AI in Orthopedic Research: A Comprehensive Review
- **Relevance Score:** 65/100
- **Authors:** A. Mısır, A. Yuce
- **Year & Journal:** 2025 | *Journal of Orthopaedic Research®* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 35
- **Main Takeaway:** AI is revolutionizing orthopedic research and clinical practice by improving diagnostic accuracy, optimizing treatment strategies, and streamlining clinical workflows, but challenges like data heterogeneity and algorithmic bias remain.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) is revolutionizing orthopedic research and clinical practice by enhancing diagnostic accuracy, optimizing treatment strategies, and streamlining clinical workflows. Recent advances in deep learning have enabled the development of algorithms that detect fractures, grade osteoarthritis, and identify subtle pathologies in radiographic and magnetic resonance images with performance comparable to expert clinicians. These AI-driven systems reduce missed diagnoses and provide objective, reproducible assessments that facilitate early intervention and personalized treatment planning. Moreover, AI has made significant strides in predictive analytics by integrating diverse patient data-including gait and imaging features-to forecast surgical outcomes, implant survivorship, and rehabilitation trajectories. Emerging applications in robotics, augmented reality, digital twin technologies, and exoskeleton control promise to further transform preoperative planning and intraoperative guidance. Despite these promising developments, challenges such as data heterogeneity, algorithmic bias, and the "black box" nature of many models-as well as issues with robust validation-remain. This comprehensive review synthesizes current developments, critically examines limitations, and outlines future directions for integrating AI into musculoskeletal care.

© 2025 Orthopaedic Research Society.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/ai-in-orthopedic-research-a-comprehensive-review-m%C4%B1s%C4%B1r-yuce/559c57caf9265926b3b2a0ca2b0e89ae/) | DOI: 10.1002/jor.26109

---

### Rank 27: Application of Machine Learning to Improve Appropriateness of Treatment in an Orthopaedic Setting of Personalized Medicine
- **Relevance Score:** 65/100
- **Authors:** F. Milella, Lorenzo Famiglini, G. Banfi, F. Cabitza
- **Year & Journal:** 2022 | *Journal of Personalized Medicine* (SJR Quartile: 2.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 12
- **Main Takeaway:** Machine learning models and decision trees can effectively predict patients who will not benefit from surgery, aiding in pre-surgical shared decision-making in personalized medicine.
- **Simple Summary & Project Context:**
  The rise of personalized medicine and its remarkable advancements have revealed new requirements for the availability of appropriate medical decision-making models. Computer science is an area that plays an essential role in the field of personalized medicine, where one of the goals is to provide algorithms and tools to extrapolate knowledge and improve the decision-support process. The minimum clinically important difference (MCID) is the smallest change in PROM scores that patients perceive as meaningful. Treatment that does not achieve the minimum level of improvement is considered inappropriate as well as a potential waste of resources. Using the MCID threshold to identify patients who fail to achieve the minimum change in PROM that results in a meaningful outcome may aid in pre-surgical shared decision-making. The decision tree algorithm is a method for extracting valuable information and providing further meaningful information to the domain expert that supports the decision-making. In the present study, different tools based on machine learning were developed. On the one hand, we compared three XGBoost models to predict the non-achievement of the MCID at six months post-operation in the SF-12 physical score. The prediction score threshold was set to 0.75 to provide three decision-making areas on the basis of the high confidence (HC) intervals; the minority class was re-balanced by weighting the positive class to penalize the loss function (XGBoost cost-sensitive), oversampling the minority class (XGBoost with SMOTE), and re-sampling the negative class (XGBoost with undersampling). On the other hand, we modeled the data through a decision tree (assessment tree), based on different complexity levels, to identify the hidden pattern and to provide a new way to understand possible relationships between the gathered features and the several outcomes. The results showed that all the proposed models were effective as binary classifiers, as they showed moderate predictive performance both regarding the minority or positive class (i.e., our targeted patients, those who will not benefit from surgery) and the negative class. The decision tree visualization can be exploited during the patient assessment status to better understand if those patients will benefit or not from the medical intervention. Both of these tools can come in handy for increasing knowledge about the patient's psychophysical state and for creating an increasingly specialized assessment of the individual patient.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/application-of-machine-learning-to-improve-milella-famiglini/77e45b50a8595435ae16818337d57df0/) | DOI: 10.3390/jpm12101706

---

### Rank 28: Revolutionizing total hip arthroplasty: The role of artificial intelligence and machine learning
- **Relevance Score:** 65/100
- **Authors:** U. Longo, S. de Salvatore, Alice Piccolomini, N. S. Ullman, G. Salvatore, Margaux D'Hooghe, M. Saccomanno, Kristian Samuelsson, R. Papalia, Ayoosh Pareek
- **Year & Journal:** 2025 | *Journal of Experimental Orthopaedics* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 11
- **Main Takeaway:** AI and machine learning models show potential in predicting post-operative outcomes in total hip arthroplasty, optimizing clinical decision-making and reducing time, cost, and complexity.
- **Simple Summary & Project Context:**
  Purpose: There has been substantial growth in the literature describing the effectiveness of artificial intelligence (AI) and machine learning (ML) applications in total hip arthroplasty (THA); these models have shown the potential to predict post-operative outcomes using algorithmic analysis of acquired data and can ultimately optimize clinical decision-making while reducing time, cost and complexity. The aim of this review is to analyze the most updated articles on AI/ML applications in THA as well as present the potential of these tools in optimizing patient care and THA outcomes.

Methods: A comprehensive search was completed through August 2024, according to the PRISMA guidelines. Publications were searched using the Scopus, Medline, EMBASE, CENTRAL and CINAHL databases. Pertinent findings and patterns in AI/ML methods utilization, as well as their applications, were quantitatively summarized and described using frequencies, averages and proportions. This study used a modified eight-item Methodological Index for Non-Randomized Studies (MINORS) checklist for quality assessment.

Results: Nineteen articles were eligible for this study. The selected studies were published between 2016 and 2024. Out of the various ML algorithms, four models have proven to be particularly significant and were used in almost 20% of the studies, including elastic net penalized logistic regression, artificial neural network, convolutional neural network (CNN) and multiple linear regression. The highest area under the curve (=1) was reported in the preoperative planning outcome variable and utilized CNN. All 20 studies demonstrated a high level of quality and low risk of bias, with a modified MINORS score of at least 7/8 (88%).

Conclusions: Developments in AI/ML prediction models in THA are rapidly increasing. There is clear potential for these tools to assist in all stages of surgical care as well as in challenges at the broader hospital administrative level and patient-specific level.

Level of Evidence: Level III.

© 2025 The Author(s). Journal of Experimental Orthopaedics published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/revolutionizing-total-hip-arthroplasty-the-role-of-longo-salvatore/ca8a7ee68d4751c5bce67678963ab905/) | DOI: 10.1002/jeo2.70195

---

### Rank 29: Personalized Medication for Chronic Diseases Using Multimodal Data‐Driven Chain‐of‐Decisions
- **Relevance Score:** 65/100
- **Authors:** Xiao-Li Chu, Yiheng Ye, Siqiao Tang, Miaoru Han, Guowei Wang, Shuai Lin, Bing-Zhen Sun, Qing-Chun Huang, Yan Zhang, Xiao-Han Chu, Kun Bao
- **Year & Journal:** 2025 | *Advanced Science* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 9
- **Main Takeaway:** The Multimodal Data-Driven Chain-of-Decisions (MDD-CoD) framework effectively personalizes medication regimens for chronic diseases by integrating patient characteristics and medication properties.
- **Simple Summary & Project Context:**
  The precise matching of medication regimens to individual patients, known as personalized medication, is critical for the effective management of chronic diseases. Traditional machine learning-based models for personalized medication regimens typically rely solely on either clinical macro-phenotypes or molecular-level drug characteristics. It remains challenging to capture the patient-medication relationship from a comprehensive perspective that integrates individual patient characteristics with macro- and micro-level properties of the medication. Determining patient-medication relationships constitutes a three-stage sequential decision process from a clinical decision-making perspective. Therefore, inspired by Chain-of-Thought prompting, which simulates the decision-making process of human experts, a Multimodal Data-Driven Chain-of-Decisions (MDD-CoD) framework is proposed, where three-stage deep learning tasks are sequentially organized to reflect upstream-downstream logical dependencies, thereby forming a coherent clinical decision-making process. The model incorporates multimodal clinical phenotype data, multi-attribute medication data, and insights from clinical experts. Performance evaluation of the model involved comprehensive experiments utilizing five datasets covering four chronic diseases sourced from three hospitals. The dataset comprises information from chronic kidney disease (CKD), membranous nephropathy (MN), rheumatoid arthritis (RA), colorectal cancer (CRC), and knee osteoarthritis (KOA), totaling 3173 unimodal, 502 multimodal, and 2187 medication records from 3675 patients. Experimental results demonstrate that the framework achieves enhanced predictive performance in personalized medication decision-making based on individual patient disease characteristics, surpassing the strongest baseline across all tasks. This framework serves as a foundational model for clinical mixed data, with improved generalization and interpretability in cross-disease personalized decision-making tasks. It offers a scalable solution for the implementation of personalized medication regimens for chronic diseases.

© 2025 The Author(s). Advanced Science published by Wiley‐VCH GmbH.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-medication-for-chronic-diseases-using-chu-ye/c41edb0a63395481aaadeafcd895b958/) | DOI: 10.1002/advs.202504079

---

### Rank 30: Machine learning models for predicting treatment outcomes in chronic non-specific back pain patients undergoing lumbar extension traction
- **Relevance Score:** 65/100
- **Authors:** I. Moustafa, D. Ozsahin, M. T. Mustapha, S. Zadeh, I. Khowailed, P. Oakley, D. Harrison
- **Year & Journal:** 2026 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** Machine learning models, particularly XGBoost and Random Forest, effectively predict lumbar extension traction outcomes in chronic non-specific low back pain patients, supporting personalized treatment strategies.
- **Simple Summary & Project Context:**
  Conservative treatment for chronic non-specific low back pain (CLBP) includes lumbar extension traction (LET) to re-align lumbar lordosis (LL). This study explores the use of machine learning (ML) models to predict post-treatment outcomes in patients with CLBP undergoing LET and how these predictions can support clinical decision-making. We utilized a retrospective database of 431 consecutive patients with uncomplicated CLBP. Post-treatment variables predicted included LL, NRS pain score, and Oswestry Disability Index (ODI). Input model variables included pre-treatment LL, sacral base angle (SBA), ratio of LL/SBA fit type, NRS, ODI, frequency, duration, LET compliance, and demographic variables of age and BMI. Initial variables were analyzed to predict post-treatment outcomes. Three ML models—Random Forest (RF), XGBoost, and Multilayer Perceptron (MLP)—were employed to handle both continuous and categorical variables, and performance was evaluated for predictive accuracy. Factors affecting outcomes were identified using Shapley Additive Explanations. Treatment was a multimodal spine rehabilitation program featuring LET applied 3–6 times per week, varied between 4 and 10 weeks, and follow-up was performed at the end of care. Improvements in LL, NRS, and ODI were − 11.5° to − 23.6°, 7.3/10 to 3.3/10, and 33.2% to 10.4%, respectively. Among the ML models, XGBoost demonstrated the highest predictive accuracy for lumbar lordotic angle (R2 = 0.728) and pain score (R2 = 0.648), while Random Forest slightly outperformed XGBoost for ODI (0.631 vs. 0.616). MLP performed poorly for ODI predictions (R2 = 0.201), indicating difficulty in capturing functional disability patterns. SHAP analysis identified fit type, compliance, traction frequency, pre-treatment lumbar curve, and BMI as the most influential predictors. These predictors offer actionable insight for clinical decision-making by allowing clinicians to stratify patients based on predicted responsiveness, tailor LET frequency and duration, and educate patients on the importance of compliance. This study demonstrates that ML models, particularly XGBoost and Random Forest, can effectively predict LET outcomes, supporting personalized treatment strategies for CLBP patients.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-models-for-predicting-treatment-moustafa-ozsahin/b24505cf4c0c5dd480e5eb5986ed5709/) | DOI: 10.1038/s41598-026-38059-9

---

### Rank 31: Development of Machine Learning–based Algorithms to Predict the 2- and 5-year Risk of TKA After Tibial Plateau Fracture Treatment
- **Relevance Score:** 65/100
- **Authors:** N. Assink, Maria P. Gonzalez-Perrino, Raul Santana-Trejo, J. Doornberg, H. Hoekstra, J. Kraeima, F. IJpma
- **Year & Journal:** 2025 | *Clinical Orthopaedics and Related Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** cross-sectional study | Citations: 4
- **Main Takeaway:** Machine-learning algorithms, particularly logistic regression, can accurately predict the 2- and 5-year risk of TKA conversion in patients with tibial plateau fractures, supporting clinical decision-making and patient counseling.
- **Simple Summary & Project Context:**
  Background: When faced with a severe intraarticular injury like a tibial plateau fracture, patients count on surgeons to make an accurate estimation of prognosis. Unfortunately, there are few tools available that enable precise, personalized prognosis estimation tailored to each patient's unique circumstances, including their individual and fracture-specific characteristics. In this study, we developed and validated a clinical prediction model using machine-learning algorithms for the 2- and 5-year risk of TKA after tibia plateau fractures.

Questions/purposes: Can machine learning-based probability calculators estimate the probability of 2- and 5-year risk of conversion to TKA in patients with a tibial plateau fracture?

Methods: A multicenter, cross-sectional study was performed in six hospitals in patients treated for a tibial plateau fracture between 2003 to 2019. In total, 2057 patients were eligible for inclusion and were sent informed consent and a questionnaire to inquire whether they underwent conversion to TKA. For 56% (1160 of 2057), status of conversion to TKA was accounted for at a minimum of 2 years, and 53% (1082 of 2057) were accounted for at a minimum of 5 years. The mean follow-up among responders was 6 ± 4 years after injury. An analysis of nonresponders found that responders were slightly older than nonresponders (53 ± 16 years versus 51 ± 17 years; p = 0.001), they were more often women (68% [788 of 1160] versus 58% [523 of 897]; p = 0.001), they were treated nonoperatively less often (30% [346 of 1160] versus 43% [387 of 897]; p = 0.001), and they had larger fracture gaps (6.4 ± 6.3 mm versus 4.2 ± 5.2 mm; p < 0.001) and step-offs (6.3 ± 5.7 mm versus 4.5 ± 4.7 mm; p < 0.001). AO Foundation/Orthopaedic Trauma Association (AO/OTA) fracture classification did not differ between nonresponders and responders (B1 11% versus 15%, B2 16% versus 19%, B3 45% versus 39%, C2 6% versus 8%, C3 22% versus 17%; p = 0.26). A total of 70% (814 of 1160) of patients were treated with open reduction and internal fixation, whereas 30% (346 of 1160) of patients were treated nonoperatively with a cast. Most fractures (80% [930 of 1160]) were AO/OTA type B fractures, and 20% (230 of 1160) were type C. Of these patients, 7% (79 of 1160) and 10% (109 of 1082) underwent conversion to a TKA at 2- and 5-year follow-up, respectively. Patient characteristics were retrieved from electronic patient records, and imaging data were shared with the initiating center from which fracture characteristics were determined. Obtained features derived from follow-up questionnaires, electronic patient records, and radiographic assessments were eligible for development of the prediction model. The first step consisted of data cleaning and included simple type formatting and standardization of numerical columns. Subsequent feature selection consisted of a review of the published evidence and expert opinion. This was followed by bivariate analysis of the identified features. The features for the models included: age, gender, BMI, AO/OTA fracture classification, fracture displacement (gap, step-off), medial proximal tibial alignment, and posterior proximal tibial alignment. The data set was used to train three models: logistic regression, random forest, and XGBoost. Logistic regression models linear relationships, random forest handles nonlinear complexities with decision trees, and XGBoost excels with sequential error correction and regularization. The models were tested using a sixfold validation approach by training the model on data from five (of six) respective medical centers and validating it against the remaining center that was left out for training. Performance was assessed by the area under the receiver operating characteristic curve (AUC), which measures a model's ability to distinguish between classes. AUC varies between 0 and 1, with values closer to 1 indicating better performance. To ensure robust and reliable results, we used bootstrapping as a resampling technique. In addition, calibration curves were plotted, and calibration was assessed with the calibration slope and intercept. The calibration plot compares the estimated probabilities with the observed probabilities for the primary outcome. Calibration slope evaluates alignment between predicted probabilities and observed outcomes (1 = perfect, < 1 = overfit, > 1 = underfit). Calibration intercept indicates bias (0 = perfect, negative = underestimation, positive = overestimation). Last, the Brier score, measuring the mean squared error of predicted probabilities (0 = perfect), was calculated.

Results: There were no differences among the models in terms of sensitivity and specificity; the AUCs for each overlapped broadly and ranged from 0.76 to 0.83. Calibration was most optimal in logistic regression for both 2- and 5-year models, with slopes of 0.82 (random forest 0.60, XGBoost 0.26) and 0.95 (random forest 0.85, XGBoost 0.48) and intercepts of 0.01 for both (random forest 0.01 to 0.02; XGBoost 0.05 to 0.07). Brier score was similar between models varying between 0.06 to 0.09. Given that its performance metrics were highest, we chose the logistic regression algorithm as the final prediction model. The web application providing the prediction tool is freely available and can be accessed through: https://3dtrauma.shinyapps.io/tka_prediction/ .

Conclusion: In this study, a personalized risk assessment tool was developed to support clinical decision-making and patient counseling. Our findings demonstrate that machine-learning algorithms, particularly logistic regression, can provide accurate and reliable predictions of TKA conversion at 2 and 5 years after a tibial plateau fracture. In addition, it provides a useful prognostic tool for surgeons who perform fracture surgery that can be used quickly and easily with patients in the clinic or emergency department once it complies with medical device regulations. External validation is needed to assess performance in other institutions and countries; to account for patient and surgeon preferences, resources, and cultures; and to further strengthen its clinical applicability.

Level of evidence: Level III, therapeutic study.

Copyright © 2025 The Author(s). Published by Wolters Kluwer Health, Inc. on behalf of the Association of Bone and Joint Surgeons.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/development-of-machine-learning%E2%80%93based-algorithms-to-assink-gonzalez-perrino/424ff15c2a7b5f79a139f65a381241cd/) | DOI: 10.1097/corr.0000000000003442

---

### Rank 32: Artificial intelligence in orthopedics: current applications, challenges, and future directions
- **Relevance Score:** 65/100
- **Authors:** Sang Yoon Kim, Byung Sun Choi, Hyuk-Soo Han, D. Ro
- **Year & Journal:** 2026 | *Knee Surgery & Related Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 3
- **Main Takeaway:** Artificial intelligence in orthopedics shows promise, but its clinical impact depends on life-cycle governance, demonstrated net benefit, and reliability and implementation science over retrospective benchmark performance.
- **Simple Summary & Project Context:**
  Background: Artificial intelligence research in orthopedics has grown rapidly, yet a substantial gap remains between technical development and clinical translation. This narrative review summarizes current applications of artificial intelligence in orthopedic practice and highlights barriers to implementation.

Main body: Current work converges on three domains: machine learning for structured perioperative risk prediction, deep learning for standardized musculoskeletal imaging, and large language models for workflow and decision support. Applications such as automated fracture detection, Kellgren-Lawrence grading for osteoarthritis, and transfusion risk modeling are approaching clinical maturity. However, routine adoption is limited by algorithmic opacity, performance degradation in new clinical environments, and poor fit within existing workflows. We argue that progress should shift from increasing model complexity toward rigorous evaluation, including external validation on independent cohorts. In addition, probability calibration and uncertainty estimation are important for trustworthy risk communication. Future directions may include multimodal "digital twin" approaches that integrate electronic medical records, imaging phenotypes, and intraoperative data into patient-specific trajectories.

Conclusions: The clinical impact of artificial intelligence in orthopedics will depend on life-cycle governance and demonstrated net benefit, prioritizing reliability and implementation science over retrospective benchmark performance.

© 2026. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-orthopedics-current-kim-choi/fc35fa85504c5c24a423cbff7ae91a17/) | DOI: 10.1186/s43019-026-00317-5

---

### Rank 33: A practical guide to the implementation of artificial intelligence in orthopaedic research—Part 3: How orthopaedic research benefits from the implementation of artificial intelligence
- **Relevance Score:** 65/100
- **Authors:** J. Pruneski, Ayoosh Pareek, Bálint Zsidai, Jacob F. Oeding, Jonathan D. Hughes, F. Oettl, Philipp W. Winkler, Thomas Tischer, Elmar Herbst, A. Grassi, M. Hirschmann, C. Ley, Yinan Yu, Kristian Samuelsson
- **Year & Journal:** 2025 | *Journal of Experimental Orthopaedics* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 3
- **Main Takeaway:** AI implementation in orthopaedics offers benefits in image evaluation, surgical planning, outcome prediction, cohort identification, and administrative tasks, while addressing challenges in producing high-quality AI-based research.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) encompasses the development of systems that can perform human-like tasks, such as treatment guidance, decision-making, pattern recognition and understanding language. Within AI, machine learning and deep learning play pivotal roles in diagnosis and outcome prediction, while natural language processing aids in synthesising large datasets from the electronic medical record. In orthopaedics, AI has demonstrated success in various areas, including image evaluation, surgical planning, outcome prediction, cohort identification and administrative tasks. The purpose of this manuscript was to provide an overview of the benefits of AI implementation within the field of orthopaedics. An additional goal was to address the challenges associated with producing high quality AI-based research in a rapidly developing field.

Level of Evidence: Level IV.

© 2025 The Author(s). Journal of Experimental Orthopaedics published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-practical-guide-to-the-implementation-of-artificial-pruneski-pareek/a667ac7ac541568095441017d8cc2743/) | DOI: 10.1002/jeo2.70481

---

### Rank 34: Machine learning for predicting outcomes, complications and resource utilisation after hip arthroscopy: A systematic review.
- **Relevance Score:** 65/100
- **Authors:** Madison Lee, Vera Zakhari, A. Shanmugaraj, Lakshmanan Sivasundaram, N. Horner
- **Year & Journal:** 2026 | *Knee surgery, sports traumatology, arthroscopy : official journal of the ESSKA* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 2
- **Main Takeaway:** Machine learning models in hip arthroscopy show variable performance in predicting outcomes and complications, with most studies reporting no significant difference to traditional regression.
- **Simple Summary & Project Context:**
  Purpose: Machine learning (ML) algorithms are increasingly used to predict outcomes in orthopaedic surgery, but their utility in hip arthroscopy remains unclear. This study aimed to (1) evaluate ML models for predicting outcomes, complications, and resource use following hip arthroscopy, (2) compare ML performance to traditional statistical methods, and (3) critically appraise the quality of existing literature.

Methods: A systematic search of PUBMED, MEDLINE, EMBASE and the Cochrane Central Register of Controlled Trials was conducted on 4 April 2023. Included studies used ML models for clinical prediction in hip arthroscopy. Data on study design, outcomes, model development, validation and adherence to TRIPOD guidelines were extracted.

Results: Seventeen studies involving 37,549 patients (52.8% female; mean age 34.4 ± 6.1 years) were included. ML was used to predict clinical outcomes (47.1%), adverse events (47.1%) and resource utilisation (5.9%). The median area under the curve was 0.66 (range 0.5-0.94) for clinical outcomes and 0.7 (range 0.6-0.9) for adverse events. Resource utilisation was reported with a root-mean-square error of $3800, a logarithmic error of 0.2, and R² of 0.8. Only four studies compared ML to traditional regression; two found no difference, while two favoured ML. On average, studies met 12.3 of the 22 TRIPOD criteria, with only 29.4% meeting more than two-thirds.

Conclusion: ML models in hip arthroscopy show variable performance in predicting outcomes and complications. Furthermore, most studies comparing ML models to traditional regression did not report any significant difference. Lastly, variability in adherence to TRIPOD guidelines highlights the need for future studies to improve transparency and reporting in the development of ML algorithms for hip arthroscopy. Given the potential of ML models in enhancing clinical decision-making for hip arthroscopy, along with the findings of the current study, their application should be used with caution.

Level of evidence: Level IV, systematic review of level II-IV studies.

© 2026 European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-for-predicting-outcomes-complications-lee-zakhari/a612e8e121955f0cb6a628a505966e12/) | DOI: 10.1002/ksa.70304

---

### Rank 35: Implementation of clinical decision support tools for treatment selection in knee osteoarthritis: a scoping review
- **Relevance Score:** 65/100
- **Authors:** Jodie A. Cochrane, Oliver Roberts, Karen Ribbons, Ross Clark, Hao-Pua Yong, T. Tan, Lynn Thwin, Ying-Ying Leung, M. H. Liow, B. Y. Tan, Michael Nilsson
- **Year & Journal:** 2026 | *Therapeutic Advances in Musculoskeletal Disease* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 0
- **Main Takeaway:** Personalised decision aids for knee osteoarthritis show promise in supporting patient-centered decision-making, but their clinical utility is limited by limited transparency in model development and implementation.
- **Simple Summary & Project Context:**
  Knee osteoarthritis (KOA) presents heterogeneous phenotypes, motivating a need for clinicians to deliver targeted therapies. There is a plethora of options that can be encompassed in KOA treatment regimes. Clinical decision support (CDS) tools that incorporate individual patient data have the capacity to tailor treatments to meet a patient's individual needs and assist with clinical decision-making. We aim to identify and evaluate CDS tools for individuals with KOA that use individualised prediction models to guide intervention decisions. A scoping review of the literature. A systematic search of six electronic databases, including Ovid Embase, Ovid Medline, Cochrane, CHINAL Ultimate, Scopus and Web of Science, was conducted for articles published between January 1, 2010 and May 17, 2024. Two reviewers independently screened articles and extracted data on study design, tool implementation and underlying prediction models. Eligible studies implemented personalised decision aids, designed to support clinical decisions regarding KOA interventions. The search yielded 5376 publications, of which 2445 were duplicates, leaving 2931 for screening. After title/abstract and full-text reviews, 14 studies were included in the final analysis, with one added through citation searching. Ten distinct decision aids were identified across the included studies. Most studies originated from the United States. Fewer than half of the decision aids included personalised information about non-surgical alternatives. Outcomes such as knee pain and physical function were the most commonly addressed, while psychosocial and financial impacts were rarely reported. Limited details were provided about the development and functionality of the underlying prediction models. Personalised decision aids for KOA show promise in supporting patient-centred decision-making. However, their clinical utility is constrained by limited transparency in model development and implementation. Future studies should emphasise the inclusion of non-surgical treatment options, early-stage KOA patients and personalised outcomes beyond pain and function to enhance their relevance and impact in clinical practice.

© The Author(s), 2026.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/implementation-of-clinical-decision-support-tools-for-cochrane-roberts/3b3650b6eaee50a4ad6168cd15260d2e/) | DOI: 10.1177/1759720x251407070

---

### Rank 36: A Hierarchical Machine Learning–Based Framework for Clinical Decision Support in Foot Orthosis Prescription: Algorithm Development and Validation Study
- **Relevance Score:** 65/100
- **Authors:** Ji-Yong Jung, Wooyeol Yang, Jung-Ja Kim
- **Year & Journal:** 2026 | *JMIR Medical Informatics* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** The hierarchical machine learning-based clinical decision support framework supports multicomponent foot orthosis prescription under variable information availability, potentially supporting clinician decision-making in routine outpatient practice.
- **Simple Summary & Project Context:**
  Background: Foot orthosis prescription is a complex clinical decision-making process that involves selecting and combining multiple structural, functional, and material components based on heterogeneous biomechanical information. In routine outpatient practice, detailed biomechanical assessments are often incomplete, creating substantial variability in prescription decisions, and limiting the applicability of conventional machine learning (ML) models that assume fixed feature availability.

Objective: This study aimed to develop and evaluate a hierarchical ML-based clinical decision support framework for foot orthosis prescription that accommodates variable clinical information availability, supports multilabel prescription decisions, and incorporates safety-oriented recommendation strategies for routine outpatient practice.

Methods: A retrospective observational study was conducted using 6462 visit-level clinical encounters collected from a single institution between 2015 and 2020. Orthotic prescription was formulated as a multilabel prediction task involving 15 prescription components. A hierarchical modeling framework was implemented, consisting of a basic decision level using routinely available demographic and alignment variables, and an advanced level incorporating subtalar joint inversion and eversion range of motion measurements when available. Tree-based gradient boosting models were evaluated using 5-fold stratified grouped cross-validation. Model performance was assessed using component-wise area under the receiver operating characteristic curve (AUROC), area under the precision-recall curve (AUPRC), positive predictive value (PPV), macro-averaged Hamming loss, Top-K hit, and coverage rates based on probabilities calibrated using internal grouped Platt scaling, and component-specific safety-oriented threshold calibration.

Results: The hierarchical models demonstrated consistent predictive performance across both decision levels, although precision-recall-based analyses indicated greater variability for low-prevalence prescription components. The Level 4 and Level 8 models achieved mean component-wise AUROC values of 0.792 and 0.816, respectively, with macro-averaged Hamming loss of 0.113 and 0.111. Using component-specific Platt scaling within the 5-fold stratified grouped cross-validation framework, Top-K analysis demonstrated a Top-1 hit rate of 86.7% and a Top-3 hit rate of 97.4%. When all prescribed components were considered, Top-K coverage reached 71.7% at Top-3 and increased to 97.0% at Top-8. Safety-oriented threshold calibration was performed separately for each prescription component, selecting the threshold that achieved the highest sensitivity while maintaining a specificity of at least 95%. Under this component-specific calibration strategy, the aggregated operating profile achieved a microaveraged specificity of 96.00% with a microaveraged sensitivity of 28.71%. Age-stratified analyses revealed distinct feature-importance patterns between pediatric and adult populations.

Conclusions: The proposed hierarchical clinical decision support framework supported multicomponent foot orthosis prescription under variable information availability commonly encountered in outpatient practice. By generating ranked component-wise recommendations and high-confidence threshold-calibrated outputs, the framework may support clinician decision-making in routine orthotic practice. Further prospective validation will be required to determine its clinical utility.

© Ji-Yong Jung, Wooyeol Yang, Jung-Ja Kim. Originally published in JMIR Medical Informatics (https://medinform.jmir.org).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-hierarchical-machine-learning%E2%80%93based-framework-for-jung-yang/b542cfb4c52e534e9e9524495f8a66bd/) | DOI: 10.2196/92831

---

### Rank 37: A practical guide to the implementation of AI in orthopaedic research – part 1: opportunities in clinical application and overcoming existing challenges
- **Relevance Score:** 63/100
- **Authors:** Bálint Zsidai, Ann-Sophie Hilkert, Janina Kaarre, E. Narup, E. Senorski, A. Grassi, C. Ley, U. Longo, E. Herbst, M. Hirschmann, Sebastian Kopf, R. Seil, Thomas Tischer, K. Samuelsson, Robert Feldt
- **Year & Journal:** 2023 | *Journal of Experimental Orthopaedics* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 54
- **Main Takeaway:** AI has the potential to revolutionize orthopaedic research, but ensuring safe and ethical deployment requires understanding key concepts, biases, and clinical safety concerns.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) has the potential to transform medical research by improving disease diagnosis, clinical decision-making, and outcome prediction. Despite the rapid adoption of AI and machine learning (ML) in other domains and industry, deployment in medical research and clinical practice poses several challenges due to the inherent characteristics and barriers of the healthcare sector. Therefore, researchers aiming to perform AI-intensive studies require a fundamental understanding of the key concepts, biases, and clinical safety concerns associated with the use of AI. Through the analysis of large, multimodal datasets, AI has the potential to revolutionize orthopaedic research, with new insights regarding the optimal diagnosis and management of patients affected musculoskeletal injury and disease. The article is the first in a series introducing fundamental concepts and best practices to guide healthcare professionals and researcher interested in performing AI-intensive orthopaedic research studies. The vast potential of AI in orthopaedics is illustrated through examples involving disease- or injury-specific outcome prediction, medical image analysis, clinical decision support systems and digital twin technology. Furthermore, it is essential to address the role of human involvement in training unbiased, generalizable AI models, their explainability in high-risk clinical settings and the implementation of expert oversight and clinical safety measures for failure. In conclusion, the opportunities and challenges of AI in medicine are presented to ensure the safe and ethical deployment of AI models for orthopaedic research and clinical application. Level of evidence IV.

© 2023. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-practical-guide-to-the-implementation-of-ai-in-zsidai-hilkert/c7e52b728f7852d0882299f46dc0da17/) | DOI: 10.1186/s40634-023-00683-z

---

### Rank 38: Artificial intelligence in total and unicompartmental knee arthroplasty
- **Relevance Score:** 63/100
- **Authors:** U. Longo, S. de Salvatore, Federica Valente, Mariajose Villa Corta, Bruno Violante, Kristian Samuelsson
- **Year & Journal:** 2024 | *BMC Musculoskeletal Disorders* (SJR Quartile: 2.0)
- **Study Type & Citations:** systematic review | Citations: 21
- **Main Takeaway:** AI/ML models in total and unicompartmental knee arthroplasty can improve patient-centered decision-making and outcome prediction by generating patient-specific risk models.
- **Simple Summary & Project Context:**
  The application of Artificial intelligence (AI) and machine learning (ML) tools in total (TKA) and unicompartmental knee arthroplasty (UKA) emerges with the potential to improve patient-centered decision-making and outcome prediction in orthopedics, as ML algorithms can generate patient-specific risk models. This review aims to evaluate the potential of the application of AI/ML models in the prediction of TKA outcomes and the identification of populations at risk.An extensive search in the following databases: MEDLINE, Scopus, Cinahl, Google Scholar, and EMBASE was conducted using the PIOS approach to formulate the research question. The PRISMA guideline was used for reporting the evidence of the data extracted. A modified eight-item MINORS checklist was employed for the quality assessment. The databases were screened from the inception to June 2022.Forty-four out of the 542 initially selected articles were eligible for the data analysis; 5 further articles were identified and added to the review from the PUBMED database, for a total of 49 articles included. A total of 2,595,780 patients were identified, with an overall average age of the patients of 70.2 years ± 7.9 years old. The five most common AI/ML models identified in the selected articles were: RF, in 38.77% of studies; GBM, in 36.73% of studies; ANN in 34.7% of articles; LR, in 32.65%; SVM in 26.53% of articles.This systematic review evaluated the possible uses of AI/ML models in TKA, highlighting their potential to lead to more accurate predictions, less time-consuming data processing, and improved decision-making, all while minimizing user input bias to provide risk-based patient-specific care.

© 2024. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-total-and-unicompartmental-longo-salvatore/185d07e998cf57c787b103c25d174114/) | DOI: 10.1186/s12891-024-07516-9

---

### Rank 39: Initial clinical experience with a predictive clinical decision support tool for anatomic and reverse total shoulder arthroplasty
- **Relevance Score:** 63/100
- **Authors:** Chelsey Simmons, Jessica Degrasse, S. Polakovic, William R. Aibinder, Thomas W. Throckmorton, Mayo Noerdlinger, R. Papandrea, Scott Trenhaile, Bradley S. Schoch, Bruno Gobbato, Howard D. Routman, Moby Parsons, Christopher P. Roche
- **Year & Journal:** 2023 | *European Journal of Orthopaedic Surgery & Traumatology* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 11
- **Main Takeaway:** Machine learning-based clinical decision support tools for anatomic and reverse total shoulder arthroplasty show potential for improved patient outcomes and surgeon satisfaction when used responsibly.
- **Simple Summary & Project Context:**
  Purpose: Clinical decision support tools (CDSTs) are software that generate patient-specific assessments that can be used to better inform healthcare provider decision making. Machine learning (ML)-based CDSTs have recently been developed for anatomic (aTSA) and reverse (rTSA) total shoulder arthroplasty to facilitate more data-driven, evidence-based decision making. Using this shoulder CDST as an example, this external validation study provides an overview of how ML-based algorithms are developed and discusses the limitations of these tools.

Methods: An external validation for a novel CDST was conducted on 243 patients (120F/123M) who received a personalized prediction prior to surgery and had short-term clinical follow-up from 3 months to 2 years after primary aTSA (n = 43) or rTSA (n = 200). The outcome score and active range of motion predictions were compared to each patient's actual result at each timepoint, with the accuracy quantified by the mean absolute error (MAE).

Results: The results of this external validation demonstrate the CDST accuracy to be similar (within 10%) or better than the MAEs from the published internal validation. A few predictive models were observed to have substantially lower MAEs than the internal validation, specifically, Constant (31.6% better), active abduction (22.5% better), global shoulder function (20.0% better), active external rotation (19.0% better), and active forward elevation (16.2% better), which is encouraging; however, the sample size was small.

Conclusion: A greater understanding of the limitations of ML-based CDSTs will facilitate more responsible use and build trust and confidence, potentially leading to greater adoption. As CDSTs evolve, we anticipate greater shared decision making between the patient and surgeon with the aim of achieving even better outcomes and greater levels of patient satisfaction.

© 2023. The Author(s), under exclusive licence to Springer-Verlag France SAS, part of Springer Nature.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/initial-clinical-experience-with-a-predictive-clinical-simmons-degrasse/23903bd5ab4f5bb5a0f9594311fee1b2/) | DOI: 10.1007/s00590-023-03796-4

---

### Rank 40: Patient preferences as human factors for health data recommender systems and shared decision making in orthopaedic practice
- **Relevance Score:** 63/100
- **Authors:** Akanksha Singh, Benjamin L. Schooley, S. Floyd, Stephen Pill, John M. Brooks
- **Year & Journal:** 2023 | *Frontiers in Digital Health* (SJR Quartile: 1.0)
- **Study Type & Citations:** mixed methods study | Citations: 8
- **Main Takeaway:** Inclusion of patient treatment outcome preferences in Health Recommender Systems can improve treatment recommendations and enhance patient treatment profiles in electronic health records.
- **Simple Summary & Project Context:**
  Background: A core set of requirements for designing AI-based Health Recommender Systems (HRS) is a thorough understanding of human factors in a decision-making process. Patient preferences regarding treatment outcomes can be one important human factor. For orthopaedic medicine, limited communication may occur between a patient and a provider during the short duration of a clinical visit, limiting the opportunity for the patient to express treatment outcome preferences (TOP). This may occur despite patient preferences having a significant impact on achieving patient satisfaction, shared decision making and treatment success. Inclusion of patient preferences during patient intake and/or during the early phases of patient contact and information gathering can lead to better treatment recommendations.

Aim: We aim to explore patient treatment outcome preferences as significant human factors in treatment decision making in orthopedics. The goal of this research is to design, build, and test an app that collects baseline TOPs across orthopaedic outcomes and reports this information to providers during a clinical visit. This data may also be used to inform the design of HRSs for orthopaedic treatment decision making.

Methods: We created a mobile app to collect TOPs using a direct weighting (DW) technique. We used a mixed methods approach to pilot test the app with 23 first-time orthopaedic visit patients presenting with joint pain and/or function deficiency by presenting the app for utilization and conducting qualitative interviews and quantitative surveys post utilization.

Results: The study validated five core TOP domains, with most users dividing their 100-point DW allocation across 1-3 domains. The tool received moderate to high usability scores. Thematic analysis of patient interviews provides insights into TOPs that are important to patients, how they can be communicated effectively, and incorporated into a clinical visit with meaningful patient-provider communication that leads to shared decision making.

Conclusion: Patient TOPs may be important human factors to consider in determining treatment options that may be helpful for automating patient treatment recommendations. We conclude that inclusion of patient TOPs to inform the design of HRSs results in creating more robust patient treatment profiles in the EHR thus enhancing opportunities for treatment recommendations and future AI applications.

© 2023 Singh, Schooley, Floyd, Pill and Brooks.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/patient-preferences-as-human-factors-for-health-data-singh-schooley/03f3f77fdcf95c1cb6bf4a5544a8c754/) | DOI: 10.3389/fdgth.2023.1137066

---

### Rank 41: Stratified care in hip arthroscopy: can we predict successful and unsuccessful outcomes? Development and external temporal validation of multivariable prediction models
- **Relevance Score:** 63/100
- **Authors:** Lasse Ishøi, K. Thorborg, T. Kallemose, J. Kemp, M. Reiman, M. Nielsen, P. Hölmich
- **Year & Journal:** 2023 | *British Journal of Sports Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 7
- **Main Takeaway:** Common clinical variables can predict the probability of having an unsuccessful outcome 1 year after hip arthroscopy, aiding shared decision-making between surgeon and patient.
- **Simple Summary & Project Context:**
  Objective: Although hip arthroscopy is a widely adopted treatment option for hip-related pain, it is unknown whether preoperative clinical information can be used to assist surgical decision-making to avoid offering surgery to patients with limited potential for a successful outcome. We aimed to develop and validate clinical prediction models to identify patients more likely to have an unsuccessful or successful outcome 1 year post hip arthroscopy based on the patient acceptable symptom state.

Methods: Patient records were extracted from the Danish Hip Arthroscopy Registry (DHAR). A priori, 26 common clinical variables from DHAR were selected as prognostic factors, including demographics, radiographic parameters of hip morphology and self-reported measures. We used 1082 hip arthroscopy patients (surgery performed 25 April 2012 to 4 October 2017) to develop the clinical prediction models based on logistic regression analyses. The development models were internally validated using bootstrapping and shrinkage before temporal external validation was performed using 464 hip arthroscopy patients (surgery performed 5 October 2017 to 13 May 2019).

Results: The prediction model for unsuccessful outcomes showed best and acceptable predictive performance on the external validation dataset for all multiple imputations (Nagelkerke R2 range: 0.25-0.26) and calibration (intercept range: -0.10 to -0.11; slope range: 1.06-1.09), and acceptable discrimination (area under the curve range: 0.76-0.77). The prediction model for successful outcomes did not calibrate well, while also showing poor discrimination.

Conclusion: Common clinical variables including demographics, radiographic parameters of hip morphology and self-reported measures were able to predict the probability of having an unsuccessful outcome 1 year after hip arthroscopy, while the model for successful outcome showed unacceptable accuracy. The externally validated prediction model can be used to support clinical evaluation and shared decision making by informing the orthopaedic surgeon and patient about the risk of an unsuccessful outcome, and thus when surgery may not be appropriate.

© Author(s) (or their employer(s)) 2023. No commercial re-use. See rights and permissions. Published by BMJ.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/stratified-care-in-hip-arthroscopy-can-we-predict-ish%C3%B8i-thorborg/44795465ac7c580ea13d07967dd2231c/) | DOI: 10.1136/bjsports-2022-105534

---

### Rank 42: Decision curve analysis to evaluate the clinical benefit of prediction models
- **Relevance Score:** 60/100
- **Authors:** A. Vickers, F. Holland
- **Year & Journal:** 2021 | *The spine journal : official journal of the North American Spine Society* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 330
- **Main Takeaway:** Decision curve analysis is a useful method to determine the clinical benefit of prediction models in orthopedic decision-making, aiding in informed decision-making.
- **Simple Summary & Project Context:**
  This paper (2021) presents key findings on decision curve analysis to evaluate the clinical benefit of prediction models. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/decision-curve-analysis-to-evaluate-the-clinical-benefit-vickers-holland/cbb13a43f3d05e0697ea7b6705760771/) | DOI: 10.1016/j.spinee.2021.02.024

---

### Rank 43: Artificial Intelligence and Orthopaedics: An Introduction for Clinicians.
- **Relevance Score:** 60/100
- **Authors:** Thomas G. Myers, P. Ramkumar, B. Ricciardi, K. Urish, Jens Kipper, C. Ketonis
- **Year & Journal:** 2020 | *The Journal of bone and joint surgery. American volume* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 179
- **Main Takeaway:** AI in orthopaedics can improve care and reduce physician burnout, but ethical issues and clinical superiority need to be addressed.
- **Simple Summary & Project Context:**
  ➤ Artificial intelligence (AI) provides machines with the ability to perform tasks using algorithms governed by pattern recognition and self-correction on large amounts of data to narrow options in order to avoid errors. ➤ The 4 things necessary for AI in medicine include big data sets, powerful computers, cloud computing, and open source algorithmic development. ➤ The use of AI in health care continues to expand, and its impact on orthopaedic surgery can already be found in diverse areas such as image recognition, risk prediction, patient-specific payment models, and clinical decision-making. ➤ Just as the business of medicine was once considered outside the domain of the orthopaedic surgeon, emerging technologies such as AI warrant ownership, leverage, and application by the orthopaedic surgeon to improve the care that we provide to the patients we serve. ➤ AI could provide solutions to factors contributing to physician burnout and medical mistakes. However, challenges regarding the ethical deployment, regulation, and the clinical superiority of AI over traditional statistics and decision-making remain to be resolved.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-and-orthopaedics-an-myers-ramkumar/186587edaeb052b98304297747506eeb/) | DOI: 10.2106/jbjs.19.01128

---

### Rank 44: Machine-learning-based patient-specific prediction models for knee osteoarthritis
- **Relevance Score:** 60/100
- **Authors:** Ali Jamshidi, J. Pelletier, J. Martel-Pelletier
- **Year & Journal:** 2018 | *Nature Reviews Rheumatology* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 175
- **Main Takeaway:** Machine learning and data mining can improve patient-specific prediction models for knee osteoarthritis, leading to improved clinical decision-making and precision medicine.
- **Simple Summary & Project Context:**
  Osteoarthritis (OA) is an extremely common musculoskeletal disease. However, current guidelines are not well suited for diagnosing patients in the early stages of disease and do not discriminate patients for whom the disease might progress rapidly. The most important hurdle in OA management is identifying and classifying patients who will benefit most from treatment. Further efforts are needed in patient subgrouping and developing prediction models. Conventional statistical modelling approaches exist; however, these models are limited in the amount of information they can adequately process. Comprehensive patient-specific prediction models need to be developed. Approaches such as data mining and machine learning should aid in the development of such models. Although a challenging task, technology is now available that should enable subgrouping of patients with OA and lead to improved clinical decision-making and precision medicine.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machinelearningbased-patientspecific-prediction-jamshidi-pelletier/ed4c802f04a8576592a546a7abfccb11/) | DOI: 10.1038/s41584-018-0130-5

---

### Rank 45: Using Machine Learning to Predict Clinical Outcomes After Shoulder Arthroplasty with a Minimal Feature Set.
- **Relevance Score:** 60/100
- **Authors:** Vikas Kumar, Christopher P. Roche, Steve Overman, Ryan W. Simovitch, P. Flurin, T. Wright, J. Zuckerman, Howard D. Routman, Ankur Teredesai
- **Year & Journal:** 2020 | *Journal of shoulder and elbow surgery* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 66
- **Main Takeaway:** Machine learning models with both full and minimal feature sets can accurately predict clinical outcomes after shoulder arthroplasty, improving decision-making during surgical consultations.
- **Simple Summary & Project Context:**
  This paper (2020) presents key findings on using machine learning to predict clinical outcomes after shoulder arthroplasty with a minimal feature set.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/using-machine-learning-to-predict-clinical-outcomes-after-kumar-roche/20705904395a548a8ff52667d9671687/) | DOI: 10.1016/j.jse.2020.07.042

---

### Rank 46: Machine Learning for the Orthopaedic Surgeon
- **Relevance Score:** 60/100
- **Authors:** D. Alsoof, Christopher L. Mcdonald, Eren O. Kuris, Alan H. Daniels
- **Year & Journal:** 2022 | *The Journal of Bone and Joint Surgery* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 35
- **Main Takeaway:** Machine learning has potential applications in orthopaedics, including radiographic diagnosis, gait analysis, implant identification, and patient outcome prediction, but limitations hinder widespread use in daily clinical environments.
- **Simple Summary & Project Context:**
  ➤: Machine learning is a subset of artificial intelligence in which computer algorithms are trained to make classifications and predictions based on patterns in data. The utilization of these techniques is rapidly expanding in the field of orthopaedic research.

➤: There are several domains in which machine learning has application to orthopaedics, including radiographic diagnosis, gait analysis, implant identification, and patient outcome prediction.

➤: Several limitations prevent the widespread use of machine learning in the daily clinical environment. However, future work can overcome these issues and enable machine learning tools to be a useful adjunct for orthopaedic surgeons in their clinical decision-making.

Copyright © 2022 by The Journal of Bone and Joint Surgery, Incorporated.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-for-the-orthopaedic-surgeon-alsoof-mcdonald/2548c3490ad657998acaa170998ed8eb/) | DOI: 10.2106/jbjs.21.01305

---

### Rank 47: Clinical Decision Support Tools for Predicting Outcomes in Patients Undergoing Total Knee Arthroplasty: A Systematic Review.
- **Relevance Score:** 60/100
- **Authors:** Jodie A. Cochrane, Traci Flynn, A. Wills, F. Walker, M. Nilsson, Sarah Johnson
- **Year & Journal:** 2020 | *The Journal of arthroplasty* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 16
- **Main Takeaway:** Clinical decision support tools show promise in predicting total knee arthroplasty outcomes, but more research is needed to confirm their clinical applicability and interpretation.
- **Simple Summary & Project Context:**
  This paper (2020) presents key findings on clinical decision support tools for predicting outcomes in patients undergoing total knee arthroplasty: a systematic review.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/clinical-decision-support-tools-for-predicting-outcomes-cochrane-flynn/cb3389740d445a68919520b30eac9092/) | DOI: 10.1016/j.arth.2020.10.053

---

### Rank 48: How to Develop and Validate Prediction Models for Orthopedic Outcomes
- **Relevance Score:** 60/100
- **Authors:** I. Zaniletti, D. Larson, D. Lewallen, D. Berry, H. Maradit Kremers
- **Year & Journal:** 2022 | *The Journal of arthroplasty* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 13
- **Main Takeaway:** Prediction models can be valuable tools for supporting surgical decision-making in arthroplasty, but require robust construction and validation for widespread adoption in clinical practice.
- **Simple Summary & Project Context:**
  This paper (2022) presents key findings on how to develop and validate prediction models for orthopedic outcomes. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/how-to-develop-and-validate-prediction-models-for-zaniletti-larson/82d328c8719c59f5a73aa44dde1b9415/) | DOI: 10.1016/j.arth.2022.12.032

---

### Rank 49: Is orthopaedics entering the age of generative AI?—A narrative review of current applications challenges and future directions
- **Relevance Score:** 60/100
- **Authors:** F. Oettl, J. Pruneski, Bálint Zsidai, Yinan Yu, Ting Cong, Thomas Tischer, M. Hirschmann, Kristian Samuelsson
- **Year & Journal:** 2025 | *Knee Surgery, Sports Traumatology, Arthroscopy* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 7
- **Main Takeaway:** Generative AI in orthopaedics has the potential to enhance surgical precision, democratize advanced planning, and improve patient outcomes, but challenges like data bias and regulatory oversight must be overcome for safe implementation.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) in medicine is undergoing a pivotal transformation, evolving from discriminative models that classify data to generative AI systems capable of creating novel content. Generative AI is a type of artificial intelligence that can learn from and mimic large amounts of data to create content such as text, images, music, videos, code, and more. The generative AI paradigm relies on advanced architectures, including large language models (LLMs), which are likely to redefine key processes in the practice of clinical medicine. The imaging- and procedure-heavy specialty of orthopaedic surgery is uniquely positioned to benefit from innovations in spatial reasoning, biomechanical analysis, and procedural planning using generative AI. Key applications are rapidly emerging, like streamlining clinical workflows through automated documentation, the mediation of patient-provider communication and enhanced interpretability of complex medical information. While an exciting field the current evidence base is quite limited. The continued integration of these technologies promises to enhance surgical precision, democratise access to advanced planning, and ultimately improve patient outcomes. However, realising this potential requires overcoming significant challenges related to the 'black box' nature of models, data bias, and evolving regulatory oversight. Rigorous clinical validation through prospective trials will be essential to ensure the safe, effective, and equitable implementation of generative AI in the future of orthopaedic care. LEVEL OF EVIDENCE: Level V.

© 2025 The Author(s). Knee Surgery, Sports Traumatology, Arthroscopy published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/is-orthopaedics-entering-the-age-of-generative-ai%E2%80%94a-oettl-pruneski/63d580fa5c17518c92f7f8e47fc10386/) | DOI: 10.1002/ksa.70145

---

### Rank 50: A pilot study on the efficacy of GPT-4 in providing orthopedic treatment recommendations from MRI reports
- **Relevance Score:** 58/100
- **Authors:** D. Truhn, Christian D. Weber, B. Braun, K. Bressem, Jakob Nikolas Kather, C. Kuhl, S. Nebelung
- **Year & Journal:** 2023 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** cross-sectional study | Citations: 75
- **Main Takeaway:** GPT-4 provides largely accurate and clinically useful treatment recommendations for common knee and shoulder conditions, but may be inadequate in certain situations.
- **Simple Summary & Project Context:**
  Large language models (LLMs) have shown potential in various applications, including clinical practice. However, their accuracy and utility in providing treatment recommendations for orthopedic conditions remain to be investigated. Thus, this pilot study aims to evaluate the validity of treatment recommendations generated by GPT-4 for common knee and shoulder orthopedic conditions using anonymized clinical MRI reports. A retrospective analysis was conducted using 20 anonymized clinical MRI reports, with varying severity and complexity. Treatment recommendations were elicited from GPT-4 and evaluated by two board-certified specialty-trained senior orthopedic surgeons. Their evaluation focused on semiquantitative gradings of accuracy and clinical utility and potential limitations of the LLM-generated recommendations. GPT-4 provided treatment recommendations for 20 patients (mean age, 50 years ± 19 [standard deviation]; 12 men) with acute and chronic knee and shoulder conditions. The LLM produced largely accurate and clinically useful recommendations. However, limited awareness of a patient's overall situation, a tendency to incorrectly appreciate treatment urgency, and largely schematic and unspecific treatment recommendations were observed and may reduce its clinical usefulness. In conclusion, LLM-based treatment recommendations are largely adequate and not prone to 'hallucinations', yet inadequate in particular situations. Critical guidance by healthcare professionals is obligatory, and independent use by patients is discouraged, given the dependency on precise data input.

© 2023. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-pilot-study-on-the-efficacy-of-gpt4-in-providing-truhn-weber/36f077dfc90f51b6a1b5cb927429450f/) | DOI: 10.1038/s41598-023-47500-2

---

### Rank 51: Custom Large Language Models Improve Accuracy: Comparing Retrieval Augmented Generation and Artificial Intelligence Agents to Non-Custom Models for Evidence-Based Medicine.
- **Relevance Score:** 58/100
- **Authors:** Joshua J. Woo, Andrew J Yang, Reena J. Olsen, Sayyida S. Hasan, D. Nawabi, Benedict U. Nwachukwu, Riley J. Williams, Prem N. Ramkumar
- **Year & Journal:** 2024 | *Arthroscopy : the journal of arthroscopic & related surgery : official publication of the Arthroscopy Association of North America and the International Arthroscopy Association* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 55
- **Main Takeaway:** Custom Large Language Models (LLMs) using Retrieval Augmented Generation (RAG) and Agentic Augmentation improve accuracy in delivering accurate information in orthopaedic care.
- **Simple Summary & Project Context:**
  This paper (2024) presents key findings on custom large language models improve accuracy: comparing retrieval augmented generation and artificial intelligence agents to non-custom models for evidence-based medicine.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/custom-large-language-models-improve-accuracy-comparing-woo-yang/08801f63c7f45c33ad7be27b2bbd565e/) | DOI: 10.1016/j.arthro.2024.10.042

---

### Rank 52: Revolutionizing orthopedic care: The impact of ai in predictive analysis, surgical precision, and personalized rehabilitation
- **Relevance Score:** 58/100
- **Authors:** Amit Lakhani
- **Year & Journal:** 2024 | *The Journal of Community Health Management* (SJR Quartile: Not specified)
- **Study Type & Citations:** literature review | Citations: 3
- **Main Takeaway:** AI in orthopedics revolutionizes preoperative planning, surgical precision, and personalized rehabilitation, improving patient outcomes and quality of life.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) is transforming the field of orthopedics, significantly impacting predictive analysis, surgical management, and rehabilitation programs. This review explores the multifaceted role of AI in enhancing orthopedic care, focusing on its application in personalized treatment plans, surgical precision, and remote rehabilitation. Predictive analytics in orthopedics, powered by AI, have revolutionized preoperative planning by forecasting surgical outcomes and potential complications, enabling clinicians to tailor surgical strategies to individual patient needs. AI's integration into surgical procedures, particularly in robotics-assisted and minimally invasive surgeries, has enhanced precision, reduced operative times, and improved patient safety, resulting in faster recovery and better outcomes.AI-driven rehabilitation programs offer personalized exercise regimens, real-time feedback, and remote monitoring, making high-quality rehabilitation accessible to patients regardless of location. These applications adapt to individual patient progress, providing customized exercise plans that optimize recovery while minimizing the risk of reinjury. Additionally, AI-powered rehabilitation tools enhance patient engagement through gamification and interactive features, leading to higher adherence to rehabilitation protocols.The review highlights key studies demonstrating the efficacy of AI in these areas, underscoring its potential to revolutionize orthopedic care. By leveraging AI's capabilities, clinicians can provide more accurate diagnoses, implement effective surgical interventions, and offer personalized rehabilitation solutions, ultimately improving patient outcomes and quality of life. As AI technology continues to advance, its role in orthopedics is expected to expand, offering increasingly innovative and effective solutions for both surgical and non-surgical patient care.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/revolutionizing-orthopedic-care-the-impact-of-ai-in-lakhani/7b5d04348b5a586a8f1f62d43f465f8b/) | DOI: 10.18231/j.jchm.2024.022

---

### Rank 53: Artificial intelligence in orthopaedics: Enhanced examinations, ambient intelligence and the future of clinical practice
- **Relevance Score:** 55/100
- **Authors:** A. Bouterse, J. Pruneski, F. Oettl, Bálint Zsidai, Thomas Tischer, U. G. Longo, R. Seil, M. Hirschmann, Kristian Samuelsson
- **Year & Journal:** 2026 | *Knee Surgery, Sports Traumatology, Arthroscopy* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 1
- **Main Takeaway:** AI-augmented vision systems, smart exam rooms, and automated clinical summaries can revolutionize orthopaedic care by increasing information, streamlining workflows, and improving patient understanding and compliance.
- **Simple Summary & Project Context:**
  Artificial intelligence (AI) continues to rapidly transform the practice of medicine, with clinicians increasingly adopting data-driven decision-making aids and diagnostic support tools. Orthopaedic physicians are well poised to harness the capabilities of AI, with an abundance of quantifiable imaging, biomechanical data, and structured clinical parameters lending themselves to algorithmic interpretation and automation. Namely, AI-augmented vision systems may increase the breadth of information readily available to clinicians, whereas smart exam rooms and automated clinical summaries may soon streamline clinical workflows to decrease administrative burden and allow more time for direct patient care. Personalised education materials and visual aids may improve patient understanding and compliance, with the aim of optimising patient outcomes. Generative medical and orthopaedic event models may soon alter decision-making heuristics and improve patient counselling. While the widespread adaptation of AI into clinical practices is not without limitations, physicians will likely come to share an increasingly symbiotic relationship with these platforms throughout their continued evolution. Accordingly, it is imperative that current and future orthopaedic practitioners become well-versed in harnessing the capabilities of AI and continue to identify new avenues for such technologies to benefit clinicians and patients alike. As such, the current manuscript provides a narrative review of the potential future applications of AI within orthopaedic practices by exploring current and developing technologies and detailing how the continued integration of AI-powered systems may serve to revolutionise the delivery of orthopaedic care. LEVEL OF EVIDENCE: Level V.

© 2026 The Author(s). Knee Surgery, Sports Traumatology, Arthroscopy published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-orthopaedics-enhanced-bouterse-pruneski/1a3391eca3635b34a9b3a802614df03f/) | DOI: 10.1002/ksa.70339

---

### Rank 54: A theoretical model of health management using data-driven decision-making: the future of precision medicine and health
- **Relevance Score:** 50/100
- **Authors:** E. Kriegová, M. Kudělka, M. Radvanský, J. Gallo
- **Year & Journal:** 2021 | *Journal of Translational Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 26
- **Main Takeaway:** The health trajectories management methodology, based on electronic health records, can help predict patients' future health risks and influence beneficial healthcare decisions.
- **Simple Summary & Project Context:**
  Background: The burden of chronic and societal diseases is affected by many risk factors that can change over time. The minimalisation of disease-associated risk factors may contribute to long-term health. Therefore, new data-driven health management should be used in clinical decision-making in order to minimise future individual risks of disease and adverse health effects.

Methods: We aimed to develop a health trajectories (HT) management methodology based on electronic health records (EHR) and analysing overlapping groups of patients who share a similar risk of developing a particular disease or experiencing specific adverse health effects. Formal concept analysis (FCA) was applied to identify and visualise overlapping patient groups, as well as for decision-making. To demonstrate its capabilities, the theoretical model presented uses genuine data from a local total knee arthroplasty (TKA) register (a total of 1885 patients) and shows the influence of step by step changes in five lifestyle factors (BMI, smoking, activity, sports and long-distance walking) on the risk of early reoperation after TKA.

Results: The theoretical model of HT management demonstrates the potential of using EHR data to make data-driven recommendations to support both patients' and physicians' decision-making. The model example developed from the TKA register acts as a clinical decision-making tool, built to show surgeons and patients the likelihood of early reoperation after TKA and how the likelihood changes when factors are modified. The presented data-driven tool suits an individualised approach to health management because it quantifies the impact of various combinations of factors on the early reoperation rate after TKA and shows alternative combinations of factors that may change the reoperation risk.

Conclusion: This theoretical model introduces future HT management as an understandable way of conceiving patients' futures with a view to positively (or negatively) changing their behaviour. The model's ability to influence beneficial health care decision-making to improve patient outcomes should be proved using various real-world data from EHR datasets.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-theoretical-model-of-health-management-using-datadriven-kriegov%C3%A1-kud%C4%9Blka/72d1d84128f65c09b26fd60689de8ed0/) | DOI: 10.1186/s12967-021-02714-8

---

### Rank 55: Personalized Mortality Prediction Driven by Electronic Medical Data and a Patient Similarity Metric
- **Relevance Score:** 45/100
- **Authors:** Joon Lee, D. Maslove, J. Dubin
- **Year & Journal:** 2015 | *PLoS ONE* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 164
- **Main Takeaway:** Analyzing only similar patients for training in clinical outcome prediction models improves predictive performance, but using too few similar patients may degrade performance due to small sample sizes.
- **Simple Summary & Project Context:**
  Background: Clinical outcome prediction normally employs static, one-size-fits-all models that perform well for the average patient but are sub-optimal for individual patients with unique characteristics. In the era of digital healthcare, it is feasible to dynamically personalize decision support by identifying and analyzing similar past patients, in a way that is analogous to personalized product recommendation in e-commerce. Our objectives were: 1) to prove that analyzing only similar patients leads to better outcome prediction performance than analyzing all available patients, and 2) to characterize the trade-off between training data size and the degree of similarity between the training data and the index patient for whom prediction is to be made.

Methods and findings: We deployed a cosine-similarity-based patient similarity metric (PSM) to an intensive care unit (ICU) database to identify patients that are most similar to each patient and subsequently to custom-build 30-day mortality prediction models. Rich clinical and administrative data from the first day in the ICU from 17,152 adult ICU admissions were analyzed. The results confirmed that using data from only a small subset of most similar patients for training improves predictive performance in comparison with using data from all available patients. The results also showed that when too few similar patients are used for training, predictive performance degrades due to the effects of small sample sizes. Our PSM-based approach outperformed well-known ICU severity of illness scores. Although the improved prediction performance is achieved at the cost of increased computational burden, Big Data technologies can help realize personalized data-driven decision support at the point of care.

Conclusions: The present study provides crucial empirical evidence for the promising potential of personalized data-driven decision support systems. With the increasing adoption of electronic medical record (EMR) systems, our novel medical data analytics contributes to meaningful use of EMR data.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-mortality-prediction-driven-by-electronic-lee-maslove/3c0e0c25e70f56c2984734d31c680e8f/) | DOI: 10.1371/journal.pone.0127428

---

### Rank 56: Exploratory application of machine learning methods on patient reported data in the development of supervised models for predicting outcomes
- **Relevance Score:** 45/100
- **Authors:** Deepika Verma, Duncan Jansen, Kerstin Bach, M. Poel, P. Mork, W. d'Hollosy
- **Year & Journal:** 2022 | *BMC Medical Informatics and Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 22
- **Main Takeaway:** Machine learning methods can effectively predict short-term patient outcomes from patient-reported outcome measurements (PROMs), supporting clinical decision making in clinical practice.
- **Simple Summary & Project Context:**
  Background: Patient-reported outcome measurements (PROMs) are commonly used in clinical practice to support clinical decision making. However, few studies have investigated machine learning methods for predicting PROMs outcomes and thereby support clinical decision making.

Objective: This study investigates to what extent different machine learning methods, applied to two different PROMs datasets, can predict outcomes among patients with non-specific neck and/or low back pain.

Methods: Using two datasets consisting of PROMs from (1) care-seeking low back pain patients in primary care who participated in a randomized controlled trial, and (2) patients with neck and/or low back pain referred to multidisciplinary biopsychosocial rehabilitation, we present data science methods for data prepossessing and evaluate selected regression and classification methods for predicting patient outcomes.

Results: The results show that there is a potential for machine learning to predict and classify PROMs. The prediction models based on baseline measurements perform well, and the number of predictors can be reduced, which is an advantage for implementation in decision support scenarios. The classification task shows that the dataset does not contain all necessary predictors for the care type classification. Overall, the work presents generalizable machine learning pipelines that can be adapted to other PROMs datasets.

Conclusion: This study demonstrates the potential of PROMs in predicting short-term patient outcomes. Our results indicate that machine learning methods can be used to exploit the predictive value of PROMs and thereby support clinical decision making, given that the PROMs hold enough predictive power.

© 2022. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/exploratory-application-of-machine-learning-methods-on-verma-jansen/4ece91a35c5b52d5a4c1f0e21fe3d13b/) | DOI: 10.1186/s12911-022-01973-9

---

### Rank 57: Personalized decision making for coronary artery disease treatment using offline reinforcement learning
- **Relevance Score:** 45/100
- **Authors:** P. Ghasemi, M. Greenberg, D. Southern, Bing Li, James A. White, Joon Lee
- **Year & Journal:** 2025 | *NPJ Digital Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 17
- **Main Takeaway:** Reinforcement learning (RL) can optimize treatment decisions for patients with obstructive coronary artery disease, outperforming physician-based decision making and achieving up to 32% improvement in expected rewards.
- **Simple Summary & Project Context:**
  Choosing optimal revascularization strategies for patients with obstructive coronary artery disease (CAD) remains a clinical challenge. While randomized controlled trials offer population-level insights, gaps remain regarding personalized decision-making for individual patients. We applied off-policy reinforcement learning (RL) to a composite data model from 41,328 unique patients with angiography-confirmed obstructive CAD. In an offline setting, we estimated optimal treatment policies and evaluated these policies using weighted importance sampling. Our findings indicate that RL-guided therapy decisions outperformed physician-based decision making, with RL policies achieving up to 32% improvement in expected rewards based on composite major cardiovascular events outcomes. Additionally, we introduced methods to ensure that RL CAD treatment policies remain compatible with locally achievable clinical practice models, presenting an interpretable RL policy with a limited number of states. Overall, this novel RL-based clinical decision support tool, RL4CAD, demonstrates potential to optimize care in patients with obstructive CAD referred for invasive coronary angiography.

© 2025. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-decision-making-for-coronary-artery-disease-ghasemi-greenberg/8e668b978a4c5f42b9f93c5a7e47bee1/) | DOI: 10.1038/s41746-025-01498-1

---

### Rank 58: Artificial Intelligence in Depression-Medication Enhancement (AID-ME): A Cluster Randomized Trial of a Deep-Learning-Enabled Clinical Decision Support System for Personalized Depression Treatment Selection and Management.
- **Relevance Score:** 45/100
- **Authors:** D. Benrimoh, Kate Whitmore, Maud Richard, Grace Golden, Kelly Perlman, Sara Jalali, Timothy Friesen, Y. Barkat, J. Mehltretter, Robert Fratila, Caitrin Armstrong, Sonia Israel, Christina Popescu, Jordan F. Karp, Sagar V. Parikh, Shirin Golchi, Erica E. M. Moodie, Jun-Wei Shen, Anthony J. Gifuni, Manuela Ferrari, Mamta Sapra, S. Kloiber, Georges-F. Pinard, B. W. Dunlop, Karl Looper, Mohini Ranganathan, M. Enault, Serge Beaulieu, S. Rej, F. Hersson-Edery, Warren Steiner, A. Anacleto, S. Qassim, R. McGuire-Snieckus, H. Margolese
- **Year & Journal:** 2025 | *The Journal of clinical psychiatry* (SJR Quartile: 1.0)
- **Study Type & Citations:** rct | Citations: 9
- **Main Takeaway:** AI-enabled clinical decision support systems can potentially improve outcomes in moderate and greater severity major depressive disorder by personalizing treatment selection and management.
- **Simple Summary & Project Context:**
  Background: There has been increasing interest in the use of artificial intelligence (AI)-enabled clinical decision support systems (CDSS) for the personalization of major depressive disorder (MDD) treatment selection and management, but clinical studies are lacking. We tested whether a CDSS that combines an AI which predicts remission probabilities for individual antidepressants and a clinical algorithm based on treatment can improve MDD outcomes.

Methods: This was a multicenter, cluster randomized, patient-and-rater blinded and clinician-partially-blinded, active-controlled trial that recruited outpatient adults with moderate or greater severity MDD. All patients had access to a patient portal to complete questionnaires. Clinicians in the active group had access to the CDSS; clinicians in the active-control group received patient questionnaires; both groups received guideline training. Primary outcome was remission (<11 points on the Montgomery-Asberg Depression Rating Scale [MADRS]) at study exit.

Results: Forty-seven clinicians were recruited at 9 sites. Of 74 eligible patients, 61 patients completed a postbaseline MADRS and were analyzed. There were no differences in baseline MADRS (P = .153). There were more remitters in the active (n = 12, 28.6%) than in the active-control (0%) group (P = .012, Fisher's exact). Of 3 serious adverse events, none were caused by the CDSS. Speed of improvement was higher in the active than the control group (1.26 vs 0.37, P = .03).

Conclusions: While limited by sample size and the lack of primary care clinicians, these results demonstrate preliminary evidence that longitudinal use of an AI-CDSS can improve outcomes in moderate and greater severity MDD.

Trial Registration: ClinicalTrials.gov identifier: NCT04655924.

© Copyright 2025 Physicians Postgraduate Press, Inc.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-in-depressionmedication-benrimoh-whitmore/33d6d55c8a77524cad9e04d584445fcc/) | DOI: 10.4088/jcp.24m15634

---

### Rank 59: Evidence Based Gait Analysis Interpretation Tools (EB-GAIT) treatment recommendation and outcome prediction models to support decision-making based on clinical gait analysis data
- **Relevance Score:** 45/100
- **Authors:** Michael H. Schwartz, Andrew G. Georgiadis
- **Year & Journal:** 2025 | *PLOS One* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 3
- **Main Takeaway:** EB-GAIT, a machine learning framework, can improve treatment outcomes and reduce surgeries in clinical gait analysis, offering a promising tool for precision medicine.
- **Simple Summary & Project Context:**
  Clinical gait analysis (CGA) has historically relied on clinician experience and judgment, leading to modest, stagnant, and unpredictable outcomes. This paper introduces Evidence-Based Gait Analysis Interpretation Tools (EB-GAIT), a novel framework leveraging machine learning to support treatment decisions. The core of EB-GAIT consists of two key components: (1) treatment recommendation models, which are models that estimate the probability of specific surgeries based on historical standard-of-practice (SOP), and (2) treatment outcome models, which predict changes in patient characteristics following treatment or natural history. Using Bayesian Additive Regression Trees (BART), we developed and validated treatment recommendation models for 12 common surgeries that account for more than 95% of the surgery recorded in our CGA center's database. These models demonstrated high balanced accuracy, sensitivity, and specificity. We used Shapley values for the models to enhances interpretability and allow clinicians and patients to understand the factors driving treatment recommendations. We also developed treatment outcome models for over 20 common outcome measures. These models were found to be unbiased, with reliable prediction intervals and accuracy comparable to experimental measurement error. We illustrated the application of EB-GAIT through a case study, showcasing its utility in providing treatment recommendations and outcome predictions. We then use simulations to show that combining recommendation and outcome models offers the possibility to improve outcomes for treated limbs, maintain outcomes for untreated limbs, and reduce the number of surgeries performed. For example, under the counterfactual situation where femoral derotation osteotomies are administered only when they align with historical standard of practice (> 50% probability of surgery) and are predicted to improve the Gait Deviation Index (change > 7.5 points), the model predicts a 11 percentage point reduction in surgeries (26% limbs currently, 15% limbs simulated), a 6 point improvement in Gait Deviation Index among treated limbs (6 currently, 12 simulated), and no change in Gait Deviation Index for untreated limbs (2 currently, 2 simulated). EB-GAIT represents a significant step toward precision medicine in CGA, offering a promising tool to enhance treatment outcomes and patient care. The EB-GAIT approach addresses the limitations of the conventional CGA interpretation method, offering a more structured and data-driven decision-making process. EB-GAIT is not intended to replace clinical judgment but to supplement it, providing clinicians with a second opinion grounded in historical data and predictive analytics. While the models perform well, their effectiveness is constrained by historical variability in treatment decisions and the inherent complexity of patient outcomes. Future efforts should focus on refining model inputs, incorporating surgical details, and pooling data from multiple centers to improve generalizability.

Copyright: © 2025 Schwartz, Georgiadis. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/evidence-based-gait-analysis-interpretation-tools-ebgait-schwartz-georgiadis/8fab8a14b7515ef0b23a64d6b8c7f29b/) | DOI: 10.1371/journal.pone.0328036

---

### Rank 60: A Reinforcement Learning Framework for Real-Time Personalized Treatment Planning in Clinical Environments
- **Relevance Score:** 45/100
- **Authors:** Leela Prasad Gorrepati, Ravi Teja Potla
- **Year & Journal:** 2025 | *Engineering, Technology & Applied Science Research* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 3
- **Main Takeaway:** The Reinforcement Learning framework optimizes personalized healthcare treatment strategies for individual patients, achieving 93.6% accuracy and enhancing safety compliance while reducing treatment cycles and enhancing safety compliance.
- **Simple Summary & Project Context:**
  This paper presents a Reinforcement Learning (RL) framework for real-time, personalized healthcare, aiming to optimize the treatment strategies for individual patients using longitudinal clinical data. The system models the patient-treatment environment as a Partially Observable Markov Decision Process (POMDP), allowing decision-making under uncertainty while integrating multimodal patient information, including Electronic Health Records (EHRs), lab tests, and imaging data. A deep policy network, trained through Proximal Policy Optimization (PPO), dynamically chooses the optimal interventions by balancing the long-term clinical outcomes, risks, costs, and adherence to medical guidelines. The framework combines a model-based simulator for off-policy data augmentation, auxiliary risk predictors to enhance the safety-aware optimization, and interpretable mechanisms to facilitate the clinician trust. Evaluated on more than 50,000 patient records and simulated environments, the proposed model surpassed the existing methods in accuracy, F1-score, Receiver Operating Characteristic-Area Under the Curve (ROC-AUC), and treatment efficiency. Specifically, it achieved 93.6% accuracy and a 0.937 F1-score while reducing the treatment cycles and enhancing safety compliance. These findings highlight the potential of RL to offer adaptive and interpretable decision support in clinical settings, although more real-world testing is necessary to confirm this result.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-reinforcement-learning-framework-for-realtime-gorrepati-potla/95fdf7a42848571c93bebd1917fa0c08/) | DOI: 10.48084/etasr.12390

---

### Rank 61: Deep Reinforcement Learning for Personalized Treatment Planning: Integrating AI into Clinical Decision-Making
- **Relevance Score:** 45/100
- **Authors:** N. Vasavya, Swapnil Saurav, Rupali Das, Y. Akhare, Jhansi Rani Ganapa, Avinash Kumar
- **Year & Journal:** 2025 | *Journal of Neonatal Surgery* (SJR Quartile: 4.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 2
- **Main Takeaway:** Deep Reinforcement Learning (DRL) can improve personalized treatment planning by dynamically adapting medication dosages based on individual patient profiles, outperforming traditional methods and supervised machine learning models.
- **Simple Summary & Project Context:**
  Personalized treatment planning is a critical challenge in clinical decision-making, where traditional heuristic-based approaches often fail to optimize patient-specific outcomes. This study explores the application of Deep Reinforcement Learning (DRL) to automate and enhance treatment recommendations, dynamically adapting medication dosages based on individual patient profiles. We developed a Proximal Policy Optimization (PPO)-based DRL model, trained on 10,000 patient records, and benchmarked it against traditional heuristic methods and supervised machine learning (ML) models (e.g., XGBoost). The PPO model outperformed all baselines, achieving a 91.2% success rate and 10.4 mg/dL Mean Absolute Error (MAE), significantly improving precision in treatment optimization. Furthermore, the model demonstrated strong adaptability across diverse patient groups, particularly in complex cases involving comorbidities, younger patients, and the elderly. SHAP analysis confirmed that the DRL model’s decision-making aligns with clinical intuition, relying primarily on age (32%), blood pressure (27%), BMI (22%), and blood glucose levels (19%). This enhances model transparency, a crucial factor for real-world adoption in healthcare. Despite its success, challenges such as data limitations, computational complexity, and real-world deployment constraints remain. Future research should focus on scaling the model to larger datasets, integrating with Electronic Health Record (EHR) systems, and conducting clinical trials to validate real-world applicability. Our findings highlight the potential of AI-driven personalized medicine, where DRL can serve as a powerful decision-support tool for clinicians, optimizing treatment efficacy, reducing risks, and ultimately improving patient outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/deep-reinforcement-learning-for-personalized-treatment-vasavya-saurav/944e1a474a9352278bf7580c5347342a/) | DOI: 10.52783/jns.v14.1940

---

### Rank 62: Simulating Personalized Treatment Pathways in Chronic Disease Management Using Reinforcement Learning and Synthetic Patient Data
- **Relevance Score:** 45/100
- **Authors:** Deepak Upadhyay, Nookala Venu, Deepak Suresh Asudani, Ansh Vadhera, Priyanshi Semwal, K. Sharma
- **Year & Journal:** 2026 | *2026 9th International Conference on Computational Intelligence in Data Science (ICCIDS)* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 1
- **Main Takeaway:** Reinforcement learning and synthetic patient data can improve personalized treatment plans for chronic disease management, reducing unsafe behavior and enhancing patient outcomes.
- **Simple Summary & Project Context:**
  We have created a method for developing personalized treatment plans using synthetic patient data and reinforcement learning; these methods can improve physician clinical decisions based on a patient's symptoms, adherence to their prescribed treatments and safety concerns. Our results show that as our model learns, it selects progressively better treatment options than before, avoids unsafe behavior, and helps patients across all characteristics (or patient profiles). Ablation studies also confirm that tracking symptoms and the prescribed medication schedule were key elements in achieving positive patient outcomes compared to other methodologies that are based on rules. Our trained model outperformed other models based on rules regarding reward, safety and symptom improvement. While the data used in the simulation environment, the results provide a level of realism that should aid clinicians wishing to develop new and safer treatment options.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/simulating-personalized-treatment-pathways-in-chronic-upadhyay-venu/40d6a5c190fe51a3b2f0662242fac1a2/) | DOI: 10.1109/iccids69108.2026.11407691

---

### Rank 63: Personalized Medical Recommendation System Using Collaborative Filtering
- **Relevance Score:** 45/100
- **Authors:** P. S, Maturu Thrissaptha Reddy, Ethakota Sruthi, Bhagath Kalyani, Mohamed Sithik M, R. S
- **Year & Journal:** 2026 | *2026 9th International Conference on Intelligent Computing and Control Systems (ICICCS)* (SJR Quartile: Not specified)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** This personalized medical recommendation system using collaborative filtering and supervised machine learning algorithms helps clinicians select effective treatment plans by suggesting treatment options based on similar past cases.
- **Simple Summary & Project Context:**
  The complexity of patient information and inconsistencies in treatment results are becoming a challenge to clinical decision-making in healthcare. This paper introduces an individualized medical recommendation system based on collaborative filtering and supervised machine learning algorithms to help clinicians select effective treatment plans. Anonymized clinical data, including demographic features, diagnostic codes, lab results, and treatment outcomes, is analyzed to compute patient similarity based on clinically weighted similarity measures. A combined collaborative filtering system is used to create treatment suggestions using effective results that have been seen in related patient profiles. Parallel to this, the prediction of the disease through the use of supervised classification models is used to enhance the accuracy of the diagnosis. The suggested system makes recommendations explainable as the suggestions are associated with evidence of similar cases in history. It is experimentally demonstrated that the disease prediction model has an accuracy of 96% with the help of a Support Vector Classifier and the recommendation module has F1-scores of up to 0.50. The suggested system is used to support clinical decisionmaking as it suggests treatment options based on the results of clinically comparable past occurrences.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-medical-recommendation-system-using-s-reddy/c95bec05c63d593ab343733d4f4f1240/) | DOI: 10.1109/iciccs67901.2026.11502878

---

### Rank 64: AI-augmented personalized treatment in healthcare a comprehensive survey of models benchmarking and deployment challenges
- **Relevance Score:** 45/100
- **Authors:** Vijayalaxmi N. Rathod, R. H. Goudar, Geetabai S. Hukkeri
- **Year & Journal:** 2026 | *Discover Artificial Intelligence* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 0
- **Main Takeaway:** This survey highlights the need for robust, transparent, and clinically viable personalized treatment recommendation systems in healthcare, addressing challenges in model interpretability, population generalizability, data privacy, and ethical compliance.
- **Simple Summary & Project Context:**
  Personalized Treatment Recommendation Systems (PTRS) are increasingly central to precision medicine, enabling data-driven selection of therapies tailored to individual patient characteristics, including clinical history, biological markers, and behavioral context. Despite rapid methodological advances, existing research remains fragmented, with limited consensus on evaluation practices and insufficient consideration of real-world deployment constraints. This survey provides a systematic and critical review of 60 peer-reviewed studies published between 2019 and 2024, selected using a PRISMA guided protocol from major scholarly databases. The reviewed literature is organized into a unified taxonomy encompassing content-based, collaborative filtering, knowledge-based, and hybrid treatment recommendation paradigms, with emphasis on their clinical applicability and algorithmic design. Recent advances in deep learning and reinforcement learning are examined for their role in improving adaptability and treatment personalization. To enable meaningful cross-study comparison, this work introduces a multidimensional benchmarking rubric that evaluates PTRS beyond predictive performance, incorporating criteria such as algorithmic rigor, clinical relevance, validation depth, data transparency, scalability, and explainability. The analysis reveals persistent challenges related to model interpretability, population generalizability, data privacy, and ethical compliance, which continue to hinder clinical adoption. Emerging solutions, including federated learning, explainable AI, and privacy-preserving architectures, are discussed as promising pathways toward trustworthy deployment. By synthesizing methodological trends, practical limitations, and evaluation gaps, this survey offers a structured foundation and forward-looking perspective for the development of robust, transparent, and clinically viable PTRS in modern healthcare.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/aiaugmented-personalized-treatment-in-healthcare-a-rathod-goudar/ef7219f92bd05820bee86bc95ec9d800/) | DOI: 10.1007/s44163-026-01187-2

---

### Rank 65: Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation
- **Relevance Score:** 45/100
- **Authors:** Xinyu Qin, Anil K. Sood, R. Yu, Sara Corvigno, E. Stur, Lu Wang
- **Year & Journal:** 2026 | *ArXiv* (SJR Quartile: Not specified)
- **Study Type & Citations:** Not specified | Citations: 0
- **Main Takeaway:** Our adaptive clinical decision support AI system, combining Treatment Effect estimation, Digital Twin simulation, and Reinforcement Learning, effectively recommends treatments for patients with ovarian cancer, maintaining low latency and minimal expert consultation.
- **Simple Summary & Project Context:**
  Clinical decision support AI systems (CDSASs) must adapt to evolving patient conditions in real-time while adhering to strict safety constraints. We present an online adaptive framework that integrates Treatment Effect (TE) estimation to quantify clinical benefits, a patient Digital Twin (DT) to simulate treatment trajectories, and Reinforcement Learning (RL) for sequential decision-making. The AI system is initially trained on historical medical records and operates in a continuous learning loop. To ensure safety, a rule-based module monitors vital signs and blocks contraindicated treatments. Cases with strong internal model disagreement are flagged for clinician review, simulated in our experiments via a pre-trained outcome model. We validate our framework using both a synthetic clinical simulator and a real-world ovarian cancer dataset from The Cancer Genome Atlas (TCGA). In both simulated and clinical settings, our method demonstrated superior effectiveness and stability in recommending treatments compared to standard computational baselines. Furthermore, the AI system maintains low latency and requires expert consultation for only a minority of cases in our experimental validation, demonstrating its potential as a safe, clinician-supervised tool for personalized medicine that continuously improves through practical use.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/treatment-response-optimized-clinical-decision-support-qin-sood/415acf620f775b91906efc292a59e0a5/) | DOI: 10.48550/arxiv.2606.17405

---

### Rank 66: Using Tree-Based Reinforcement Learning Methods to Support Personalized Decision-Making in Hand Treatment.
- **Relevance Score:** 45/100
- **Authors:** Yao Song, Lu Wang
- **Year & Journal:** 2025 | *Hand clinics* (SJR Quartile: 2.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** Tree-based reinforcement learning methods can optimize personalized hand treatment decisions by balancing competing clinical priorities and enhancing patient-centered care.
- **Simple Summary & Project Context:**
  This paper (2025) presents key findings on using tree-based reinforcement learning methods to support personalized decision-making in hand treatment.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/using-treebased-reinforcement-learning-methods-to-song-wang/0d11eb9436b957c8bbedaf217b183011/) | DOI: 10.1016/j.hcl.2025.08.002

---

### Rank 67: An Explainable Deep Learning Framework for Transparent and Personalized Recommendations in Clinical Decision-Making
- **Relevance Score:** 45/100
- **Authors:** A. V., V. N, S. Bhaskaran
- **Year & Journal:** 2026 | *International Journal of Drug Delivery Technology* (SJR Quartile: 3.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** The study develops an explicable deep learning framework for personalized drug delivery recommendations in clinical decision-making, enhancing accuracy and providing actionable insights for clinicians.
- **Simple Summary & Project Context:**
  We develop an explicable system of deep learning-assisted drug delivery recommendations in clinical decision-making to
meet the important requirement of interpretability in medical applications. The framework combines structured
longitudinal clinical data such as patient-medication interactions, clinical contents, and contextual data to produce specific
therapeutic guidance. The patient history is represented as learned embeddings, the temporal position signal, and candidate
drug options are represented as structured attributes; finally, they are combined using a Transformer layer to ensure that a
complicated dependence is captured. The model calculates compatibility scores of the state of a patient and a drug choice,
making it possible to recommend them personally with an explanation at multi-level. In addition, the model uses temporal
explanations based on attention, SHAP-based feature attribution, integrated gradients, and rule-based clinical reasoning
to provide better interpretability to clinicians. The training goal is a co-optimization of the accuracy of recommendations,
interpretability, regularization, and wall is safe which guarantees clinically plausible results. Experiments indicate that not
only does the framework enhance the performance of the recommendations, but the actionable insights into the decisionmaking process are also provided as well. The given approach makes the divide between black-box models of deep
learning and clinical application, providing a useful place of personalized medicine. The design is modular and can
integrate easily with current clinical processes and may minimize adverse drug events and enhance the patient outcomes.
The work contributes to the field by integrating the state-of-the-art methods of deep learning with thorough explainability,
which leads to building trust and acceptance in real-life healthcare environments.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/an-explainable-deep-learning-framework-for-transparent-v-n/c633126cb215552dbcad55a4f4ad7b5c/) | DOI: 10.25258/ijddt.16.30s.92

---

### Rank 68: A survey on deep reinforcement learning for personalized treatment featuring challenges and a theoretical framework
- **Relevance Score:** 45/100
- **Authors:** Bipasha Kaul, Rashmi Naveen Raj, Veena Mayya, Ramya D. Shetty
- **Year & Journal:** 2026 | *Discover Artificial Intelligence* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 0
- **Main Takeaway:** Deep reinforcement learning can optimize personalized treatment planning by balancing clinical and non-clinical objectives, enhancing safety in healthcare applications.
- **Simple Summary & Project Context:**
  Personalized treatment is a paradigm shift in the medical field that provides individualized treatment strategies based on comprehensive patient data including habitat, genomic, and medical profile, etc. Integrating this into the conventional clinical process involves collaborative strategic planning with stakeholders from diverse sectors. The scope of this survey is limited to studies that apply reinforcement learning, deep reinforcement learning, and multi-objective deep reinforcement learning to sequential decision making in personalized treatment. The review addresses these main questions: Why are reinforcement learning and its variants suitable for personalized treatment?How are these algorithms applied in clinical settings of various domains? How are states, actions and rewards defined? What are the requirements, challenges at every stage of model development for deploying these models in safety-critical healthcare applications? Early studies primarily focused on reinforcement learning with single objective, while more works have increasingly adopted deep variants to manage high-dimensional state-action spaces, and a sparse literature exists with multi-objective approach to address conflicting treatment options. Most existing research is concentrated on using publicly available MIMIC- III /IV dataset in ICU settings, oncology related resources including, The Cancer Genome Atlas, Genomics of Drug Sensitivity in Cancer, The Catalogue of Somatic Mutations In Cancer. To the best of our knowledge, this is the first survey to emphasize: (i) the need for multi-objective optimization with sequential personalized treatment planning, (ii) the integration of non-clinical objectives such as patient preferences, hospital infrastructure, insurance coverage, etc., and stake-holders into decision framework, (iii) the theoretical and conceptual model of a multi-modal multi-objective deep reinforcement learning aiming at optimizing the treatment regimes using a newly introduced time-weighted reward integration block to balance multiple, potentially conflicting clinical as well as non-clinical objectives.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-survey-on-deep-reinforcement-learning-for-personalized-kaul-raj/2b925f41c4e15e71bc5f97ecd208c94c/) | DOI: 10.1007/s44163-026-01733-y

---

### Rank 69: Causal machine learning for predicting treatment outcomes
- **Relevance Score:** 43/100
- **Authors:** S. Feuerriegel, Dennis Frauen, Valentyn Melnychuk, J. Schweisthal, Konstantin Hess, Alicia Curth, S. Bauer, Niki Kilbertus, Isaac S. Kohane, M. van der Schaar
- **Year & Journal:** 2024 | *Nature Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** other | Citations: 399
- **Main Takeaway:** Causal machine learning can predict treatment outcomes, enabling personalized clinical decision-making based on individual patient profiles.
- **Simple Summary & Project Context:**
  Causal machine learning (ML) offers flexible, data-driven methods for predicting treatment outcomes including efficacy and toxicity, thereby supporting the assessment and safety of drugs. A key benefit of causal ML is that it allows for estimating individualized treatment effects, so that clinical decision-making can be personalized to individual patient profiles. Causal ML can be used in combination with both clinical trial data and real-world data, such as clinical registries and electronic health records, but caution is needed to avoid biased or incorrect predictions. In this Perspective, we discuss the benefits of causal ML (relative to traditional statistical or ML approaches) and outline the key components and steps. Finally, we provide recommendations for the reliable use of causal ML and effective translation into the clinic.

© 2024. Springer Nature America, Inc.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/causal-machine-learning-for-predicting-treatment-feuerriegel-frauen/38bc675c1be6549d97e33848a33f9f9f/) | DOI: 10.1038/s41591-024-02902-1

---

### Rank 70: A Primer on Reinforcement Learning in Medicine for Clinicians
- **Relevance Score:** 43/100
- **Authors:** P. Jayaraman, J. Desman, Moein Sabounchi, G. Nadkarni, A. Sakhuja
- **Year & Journal:** 2024 | *NPJ Digital Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 116
- **Main Takeaway:** Reinforcement Learning (RL) enhances clinical decision-making by optimizing treatment strategies and personalized treatment plans, improving outcomes and resource efficiency for healthcare professionals.
- **Simple Summary & Project Context:**
  Reinforcement Learning (RL) is a machine learning paradigm that enhances clinical decision-making for healthcare professionals by addressing uncertainties and optimizing sequential treatment strategies. RL leverages patient-data to create personalized treatment plans, improving outcomes and resource efficiency. This review introduces RL to a clinical audience, exploring core concepts, potential applications, and challenges in integrating RL into clinical practice, offering insights into efficient, personalized, and effective patient care.

© 2024. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-primer-on-reinforcement-learning-in-medicine-for-jayaraman-desman/c27522bd18ea531d8b647ae69bdb5db3/) | DOI: 10.1038/s41746-024-01316-0

---

### Rank 71: A clinical decision support system for AI-assisted decision-making in response-adaptive radiotherapy (ARCliDS)
- **Relevance Score:** 43/100
- **Authors:** D. Niraula, Wenbo Sun, Jiong-Hua Jin, I. Dinov, K. Cuneo, J. Jamaluddin, M. Matuszak, Yi Luo, T. Lawrence, S. Jolly, R. T. Ten Haken, I. El Naqa
- **Year & Journal:** 2023 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 48
- **Main Takeaway:** ARCliDS, a web-based software, improves AI-assisted clinical decision-making in response-adaptive radiotherapy by maximizing tumor local control and minimizing side effects in oncology.
- **Simple Summary & Project Context:**
  Involvement of many variables, uncertainty in treatment response, and inter-patient heterogeneity challenge objective decision-making in dynamic treatment regime (DTR) in oncology. Advanced machine learning analytics in conjunction with information-rich dense multi-omics data have the ability to overcome such challenges. We have developed a comprehensive artificial intelligence (AI)-based optimal decision-making framework for assisting oncologists in DTR. In this work, we demonstrate the proposed framework to Knowledge Based Response-Adaptive Radiotherapy (KBR-ART) applications by developing an interactive software tool entitled Adaptive Radiotherapy Clinical Decision Support (ARCliDS). ARCliDS is composed of two main components: Artifcial RT Environment (ARTE) and Optimal Decision Maker (ODM). ARTE is designed as a Markov decision process and modeled via supervised learning. Given a patient's pre- and during-treatment information, ARTE can estimate treatment outcomes for a selected daily dosage value (radiation fraction size). ODM is formulated using reinforcement learning and is trained on ARTE. ODM can recommend optimal daily dosage adjustments to maximize the tumor local control probability and minimize the side effects. Graph Neural Networks (GNN) are applied to exploit the inter-feature relationships for improved modeling performance and a novel double GNN architecture is designed to avoid nonphysical treatment response. Datasets of size 117 and 292 were available from two clinical trials on adaptive RT in non-small cell lung cancer (NSCLC) patients and adaptive stereotactic body RT (SBRT) in hepatocellular carcinoma (HCC) patients, respectively. For training and validation, dense data with 297 features were available for 67 NSCLC patients and 110 features for 71 HCC patients. To increase the sample size for ODM training, we applied Generative Adversarial Networks to generate 10,000 synthetic patients. The ODM was trained on the synthetic patients and validated on the original dataset. We found that, Double GNN architecture was able to correct the nonphysical dose-response trend and improve ARCliDS recommendation. The average root mean squared difference (RMSD) between ARCliDS recommendation and reported clinical decisions using double GNNs were 0.61 [0.03] Gy/frac (mean [sem]) for adaptive RT in NSCLC patients and 2.96 [0.42] Gy/frac for adaptive SBRT HCC compared to the single GNN's RMSDs of 0.97 [0.12] Gy/frac and 4.75 [0.16] Gy/frac, respectively. Overall, For NSCLC and HCC, ARCliDS with double GNNs was able to reproduce 36% and 50% of the good clinical decisions (local control and no side effects) and improve 74% and 30% of the bad clinical decisions, respectively. In conclusion, ARCliDS is the first web-based software dedicated to assist KBR-ART with multi-omics data. ARCliDS can learn from the reported clinical decisions and facilitate AI-assisted clinical decision-making for improving the outcomes in DTR.

© 2023. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-clinical-decision-support-system-for-aiassisted-niraula-sun/38e9f346bf2255e7b5cddef38050f870/) | DOI: 10.1038/s41598-023-32032-6

---

### Rank 72: Personalized hypertension treatment recommendations by a data-driven model
- **Relevance Score:** 43/100
- **Authors:** Yang Hu, J. Huerta, Nicholas Cordella, Rebecca G Mishuris, I. Paschalidis
- **Year & Journal:** 2023 | *BMC Medical Informatics and Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 38
- **Main Takeaway:** Our data-driven approach for personalized hypertension treatment significantly improved blood pressure reduction compared to standard-of-care, with potential benefits of computational deprescribing.
- **Simple Summary & Project Context:**
  Background: Hypertension is a prevalent cardiovascular disease with severe longer-term implications. Conventional management based on clinical guidelines does not facilitate personalized treatment that accounts for a richer set of patient characteristics.

Methods: Records from 1/1/2012 to 1/1/2020 at the Boston Medical Center were used, selecting patients with either a hypertension diagnosis or meeting diagnostic criteria (≥ 130 mmHg systolic or ≥ 90 mmHg diastolic, n = 42,752). Models were developed to recommend a class of antihypertensive medications for each patient based on their characteristics. Regression immunized against outliers was combined with a nearest neighbor approach to associate with each patient an affinity group of other patients. This group was then used to make predictions of future Systolic Blood Pressure (SBP) under each prescription type. For each patient, we leveraged these predictions to select the class of medication that minimized their future predicted SBP.

Results: The proposed model, built with a distributionally robust learning procedure, leads to a reduction of 14.28 mmHg in SBP, on average. This reduction is 70.30% larger than the reduction achieved by the standard-of-care and 7.08% better than the corresponding reduction achieved by the 2nd best model which uses ordinary least squares regression. All derived models outperform following the previous prescription or the current ground truth prescription in the record. We randomly sampled and manually reviewed 350 patient records; 87.71% of these model-generated prescription recommendations passed a sanity check by clinicians.

Conclusion: Our data-driven approach for personalized hypertension treatment yielded significant improvement compared to the standard-of-care. The model implied potential benefits of computationally deprescribing and can support situations with clinical equipoise.

© 2023. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-hypertension-treatment-recommendations-by-hu-huerta/83242829369952298bb9c2e206ab8af1/) | DOI: 10.1186/s12911-023-02137-z

---

### Rank 73: Machine learning-based clinical decision support system for treatment recommendation and overall survival prediction of hepatocellular carcinoma: a multi-center study
- **Relevance Score:** 43/100
- **Authors:** K. Lee, G. Choi, J. Yun, Jonggi Choi, M. Goh, D. Sinn, Young-Joo Jin, M. A. Kim, S. Yu, Sangmi Jang, S. Lee, Jeong Won Jang, Jae Seung Lee, D. Y. Kim, Young Youn Cho, H. Kim, Sehwa Kim, Ji Hoon Kim, Namkug Kim, K. Kim
- **Year & Journal:** 2024 | *NPJ Digital Medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 37
- **Main Takeaway:** The machine learning-based clinical decision support system improves treatment recommendation accuracy and overall survival prediction in hepatocellular carcinoma patients, aiding physicians in making treatment decisions.
- **Simple Summary & Project Context:**
  The treatment decisions for patients with hepatocellular carcinoma are determined by a wide range of factors, and there is a significant difference between the recommendations of widely used staging systems and the actual initial treatment choices. Herein, we propose a machine learning-based clinical decision support system suitable for use in multi-center settings. We collected data from nine institutions in South Korea for training and validation datasets. The internal and external datasets included 935 and 1750 patients, respectively. We developed a model with 20 clinical variables consisting of two stages: the first stage which recommends initial treatment using an ensemble voting machine, and the second stage, which predicts post-treatment survival using a random survival forest algorithm. We derived the first and second treatment options from the results with the highest and the second-highest probabilities given by the ensemble model and predicted their post-treatment survival. When only the first treatment option was accepted, the mean accuracy of treatment recommendation in the internal and external datasets was 67.27% and 55.34%, respectively. The accuracy increased to 87.27% and 86.06%, respectively, when the second option was included as the correct answer. Harrell's C index, integrated time-dependent AUC curve, and integrated Brier score of survival prediction in the internal and external datasets were 0.8381 and 0.7767, 91.89 and 86.48, 0.12, and 0.14, respectively. The proposed system can assist physicians by providing data-driven predictions for reference from other larger institutions or other physicians within the same institution when making treatment decisions.

© 2024. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learningbased-clinical-decision-support-system-lee-choi/db61523de78851f483867584ac926794/) | DOI: 10.1038/s41746-023-00976-8

---

### Rank 74: Predicting Treatment Outcomes in Patients with Low Back Pain Using Gene Signature-Based Machine Learning Models
- **Relevance Score:** 43/100
- **Authors:** Youzhi Lian, Yin-Yu Shi, Haibin Shang, Hong-Sheng Zhan
- **Year & Journal:** 2024 | *Pain and Therapy* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 7
- **Main Takeaway:** Gene signature-based machine learning models using transcriptomic data from peripheral immune cells can effectively predict treatment outcomes in patients with low back pain, providing a basis for personalized treatment strategies.
- **Simple Summary & Project Context:**
  Introduction: Low back pain (LBP) is a significant global health burden, with variable treatment outcomes and an unclear underlying molecular mechanism. Effective prediction of treatment responses remains a challenge. In this study, we aimed to develop gene signature-based machine learning models using transcriptomic data from peripheral immune cells to predict treatment outcomes in patients with LBP.

Methods: The transcriptomic data of patients with LBP from peripheral immune cells were retrieved from the GEO database. Patients with LBP were recruited, and treatment outcomes were assessed after 3 months. Patients were classified into two groups: those with resolved pain and those with persistent pain. Differentially expressed genes (DEGs) between the two groups were identified through bioinformatic analysis. Key genes were selected using five machine learning models, including Lasso, Elastic Net, Random Forest, SVM, and GBM. These key genes were then used to train 45 machine learning models by combining nine different algorithms: Logistic Regression, K-Nearest Neighbors, Support Vector Machine, Decision Tree, Random Forest, Gradient Boosting Machine, Multilayer Perceptron, Naive Bayes, and Linear Discriminant Analysis. Five-fold cross-validation was employed to ensure robust model evaluation and minimize overfitting. In each fold, the dataset was split into training and validation sets, with model performance assessed using multiple metrics including accuracy, precision, recall, and F1 score. The final model performance was reported as the mean and standard deviation across all five folds, providing a more reliable estimate of the models' ability to predict LBP treatment outcomes using gene expression data from peripheral immune cells.

Results: A total of 61 DEGs were identified between patients with resolved and persistent pain. From these genes, 45 machine learning models were constructed using different combinations of feature selection methods and classification algorithms. The Elastic Net with Logistic Regression achieved the highest accuracy of 88.7% ± 8.0% (mean ± standard deviation), followed closely by Elastic Net with Linear Discriminant Analysis (88.7% ± 7.5%) and Lasso with Multilayer Perceptron (87.7% ± 6.7%). Overall, 15 models demonstrated robust performance with accuracy > 80%, suggesting the reliability of our machine learning approach in predicting LBP treatment outcomes. The SHapley Additive exPlanations (SHAP) method was used to visualize the contribution of core genes to model performance, highlighting their roles in predicting treatment outcomes.

Conclusion: The study demonstrates the potential of using transcriptomic data from peripheral immune cells and machine learning models to predict treatment outcomes in patients with LBP. The identification of key genes and the high accuracy of certain models provide a basis for future personalized treatment strategies in LBP management. Visualizing gene importance with SHAP adds interpretability to the predictive models, enhancing their clinical relevance.

© 2024. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/predicting-treatment-outcomes-in-patients-with-low-back-lian-shi/2899843493c757399ac38bd4ac5ab953/) | DOI: 10.1007/s40122-024-00700-8

---

### Rank 75: Machine Learning Clinical Decision Support for Interdisciplinary Multimodal Chronic Musculoskeletal Pain Treatment: Prospective Pilot Study of Patient Assessment and Prognostic Profile Validation
- **Relevance Score:** 43/100
- **Authors:** Fredrick Zmudzki, R. Smeets, Jan S. Groenewegen, E. van der Graaff
- **Year & Journal:** 2024 | *JMIR Rehabilitation and Assistive Technologies* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** Machine learning prognostic patient profiles show promise in improving clinical decision support and treatment outcomes for patients with chronic musculoskeletal pain.
- **Simple Summary & Project Context:**
  Background: Chronic musculoskeletal pain (CMP) impacts around 20% of people globally, resulting in patients living with pain, fatigue, restricted social and employment capacity, and reduced quality of life. Interdisciplinary multimodal pain treatment (IMPT) programs have been shown to provide positive and sustained outcomes where all other interventions have failed. IMPT programs combined with multidimensional machine learning predictive patient profiles aim to improve clinical decision support and personalized patient assessments, potentially leading to better treatment outcomes.

Objective: We aimed to investigate integrating machine learning with IMPT programs and its potential contribution to clinical decision support and treatment outcomes for patients with CMP.

Methods: This prospective pilot study used a machine learning prognostic patient profile of 7 outcome measures across 4 clinically relevant domains, including activity or disability, pain, fatigue, and quality of life. Prognostic profiles were created for new IMPT patients in the Netherlands in November 2023 (N=17). New summary indicators were developed, including defined categories for positive, negative, and mixed prognostic profiles; an accuracy indicator with high, medium, and low levels based on weighted true- or false-positive values; and an indicator for consistently positive or negative outcomes. The consolidated reporting guidelines checklist for prognostic machine learning modeling studies was completed to provide transparency of data quality, model development methodology, and validation.

Results: The machine learning IMPT prognostic patient profiles demonstrated high accuracy and consistency in predicting patient outcomes. The profile, combined with extended new prognostic summary indicators, provided improved identification of patients with predicted positive, negative, and mixed outcomes, supporting more comprehensive assessment. Overall, 82.4% (14/17) of prognostic patient profiles were consistent with clinician assessments. Notably, clinician case notes indicated the stratified prognostic profiles were directly discussed with around half (8/17, 47.1%) of patients. Clinicians found the prognostic patient profiles helpful in 88.2% (15/17) of initial IMPT assessments to support shared clinician and patient decision-making and discussion of individualized treatment planning.

Conclusions: Machine learning prognostic patient profiles showed promising contributions for IMPT clinical decision support and improving treatment outcomes for patients with CMP. Further research is needed to validate these findings in larger, more diverse populations.

© Fredrick Zmudzki, Rob J E M Smeets, Jan S Groenewegen, Erik van der Graaff. Originally published in JMIR Rehabilitation and Assistive Technology (https://rehab.jmir.org).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-clinical-decision-support-for-zmudzki-smeets/f6dce48d51645d019d53fa61c62dd77d/) | DOI: 10.2196/65890

---

### Rank 76: Learning Optimal Dynamic Treatment Regime from Observational Clinical Data through Reinforcement Learning
- **Relevance Score:** 43/100
- **Authors:** S. Abebe, Irene Poli, Roger D. Jones, Debora Slanzi
- **Year & Journal:** 2024 | *Mach. Learn. Knowl. Extr.* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** Decision tree-based reinforcement learning algorithms show potential in determining optimal dynamic treatment regimes for personalized medicine, offering nuanced and effective treatment recommendations.
- **Simple Summary & Project Context:**
  In medicine, dynamic treatment regimes (DTRs) have emerged to guide personalized treatment decisions for patients, accounting for their unique characteristics. However, existing methods for determining optimal DTRs face limitations, often due to reliance on linear models unsuitable for complex disease analysis and a focus on outcome prediction over treatment effect estimation. To overcome these challenges, decision tree-based reinforcement learning approaches have been proposed. Our study aims to evaluate the performance and feasibility of such algorithms: tree-based reinforcement learning (T-RL), DTR-Causal Tree (DTR-CT), DTR-Causal Forest (DTR-CF), stochastic tree-based reinforcement learning (SL-RL), and Q-learning with Random Forest. Using real-world clinical data, we conducted experiments to compare algorithm performances. Evaluation metrics included the proportion of correctly assigned patients to recommended treatments and the empirical mean with standard deviation of expected counterfactual outcomes based on estimated optimal treatment strategies. This research not only highlights the potential of decision tree-based reinforcement learning for dynamic treatment regimes but also contributes to advancing personalized medicine by offering nuanced and effective treatment recommendations.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/learning-optimal-dynamic-treatment-regime-from-abebe-poli/35306f28ec905e0baea4c0961930cc99/) | DOI: 10.3390/make6030088

---

### Rank 77: Machine learning models to predict osteonecrosis in patients with femoral neck fractures undergoing internal fixation.
- **Relevance Score:** 43/100
- **Authors:** Bing-Chuan Liu, Guo-Jin Hou, Zhong-Wei Yang, Zhi-Shan Zhang, Fang Zhou, Yun Tian
- **Year & Journal:** 2024 | *Injury* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 4
- **Main Takeaway:** The logistic regression model effectively predicts osteonecrosis of the femoral head in patients with femoral neck fractures after internal fixation, aiding in clinical decision-making.
- **Simple Summary & Project Context:**
  This paper (2024) presents key findings on machine learning models to predict osteonecrosis in patients with femoral neck fractures undergoing internal fixation.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-models-to-predict-osteonecrosis-in-liu-hou/00da5104efff57eca12f8d59e0cd469b/) | DOI: 10.1016/j.injury.2024.111830

---

### Rank 78: DeepSurv: personalized treatment recommender system using a Cox proportional hazards deep neural network
- **Relevance Score:** 40/100
- **Authors:** Jared Katzman, Uri Shaham, A. Cloninger, Jonathan Bates, Tingting Jiang, Y. Kluger
- **Year & Journal:** 2016 | *BMC Medical Research Methodology* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 1917
- **Main Takeaway:** DeepSurv, a Cox proportional hazards deep neural network, effectively models patient characteristics and treatment effectiveness, providing personalized treatment recommendations and potentially increasing patient survival time.
- **Simple Summary & Project Context:**
  Background: Medical practitioners use survival models to explore and understand the relationships between patients' covariates (e.g. clinical and genetic features) and the effectiveness of various treatment options. Standard survival models like the linear Cox proportional hazards model require extensive feature engineering or prior medical knowledge to model treatment interaction at an individual level. While nonlinear survival methods, such as neural networks and survival forests, can inherently model these high-level interaction terms, they have yet to be shown as effective treatment recommender systems.

Methods: We introduce DeepSurv, a Cox proportional hazards deep neural network and state-of-the-art survival method for modeling interactions between a patient's covariates and treatment effectiveness in order to provide personalized treatment recommendations.

Results: We perform a number of experiments training DeepSurv on simulated and real survival data. We demonstrate that DeepSurv performs as well as or better than other state-of-the-art survival models and validate that DeepSurv successfully models increasingly complex relationships between a patient's covariates and their risk of failure. We then show how DeepSurv models the relationship between a patient's features and effectiveness of different treatment options to show how DeepSurv can be used to provide individual treatment recommendations. Finally, we train DeepSurv on real clinical studies to demonstrate how it's personalized treatment recommendations would increase the survival time of a set of patients.

Conclusions: The predictive and modeling capabilities of DeepSurv will enable medical researchers to use deep neural networks as a tool in their exploration, understanding, and prediction of the effects of a patient's characteristics on their risk of failure.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/deepsurv-personalized-treatment-recommender-system-katzman-shaham/43fa9a6d4d455ae5b23d60d42ca4f8d9/) | DOI: 10.1186/s12874-018-0482-1

---

### Rank 79: The Personalized Advantage Index: Translating Research on Prediction into Individualized Treatment Recommendations. A Demonstration
- **Relevance Score:** 40/100
- **Authors:** R. DeRubeis, Z. Cohen, Nicholas R. Forand, J. Fournier, L. Gelfand, Lorenzo Lorenzo‐Luaces
- **Year & Journal:** 2014 | *PLoS ONE* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 455
- **Main Takeaway:** The Personalized Advantage Index (PAI) effectively predicts treatment outcomes for 60% of patients, leading to superior outcomes in a randomized treatment comparison.
- **Simple Summary & Project Context:**
  Background: Advances in personalized medicine require the identification of variables that predict differential response to treatments as well as the development and refinement of methods to transform predictive information into actionable recommendations.

Objective: To illustrate and test a new method for integrating predictive information to aid in treatment selection, using data from a randomized treatment comparison.

Method: Data from a trial of antidepressant medications (N = 104) versus cognitive behavioral therapy (N = 50) for Major Depressive Disorder were used to produce predictions of post-treatment scores on the Hamilton Rating Scale for Depression (HRSD) in each of the two treatments for each of the 154 patients. The patient's own data were not used in the models that yielded these predictions. Five pre-randomization variables that predicted differential response (marital status, employment status, life events, comorbid personality disorder, and prior medication trials) were included in regression models, permitting the calculation of each patient's Personalized Advantage Index (PAI), in HRSD units.

Results: For 60% of the sample a clinically meaningful advantage (PAI≥3) was predicted for one of the treatments, relative to the other. When these patients were divided into those randomly assigned to their "Optimal" treatment versus those assigned to their "Non-optimal" treatment, outcomes in the former group were superior (d = 0.58, 95% CI .17-1.01).

Conclusions: This approach to treatment selection, implemented in the context of two equally effective treatments, yielded effects that, if obtained prospectively, would rival those routinely observed in comparisons of active versus control treatments.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/the-personalized-advantage-index-translating-research-on-derubeis-cohen/6d3bd1d125085eed97e80c271727a58a/) | DOI: 10.1371/journal.pone.0083875

---

### Rank 80: How machine-learning recommendations influence clinician treatment selections: the example of antidepressant selection
- **Relevance Score:** 40/100
- **Authors:** Maia L. Jacobs, M. Pradier, T. McCoy, R. Perlis, Finale Doshi-Velez, Krzysztof Z Gajos
- **Year & Journal:** 2021 | *Translational Psychiatry* (SJR Quartile: 1.0)
- **Study Type & Citations:** non-randomized experimental study | Citations: 292
- **Main Takeaway:** Interacting with machine-learning recommendations does not significantly improve clinician treatment selection accuracy, but incorrect recommendations and limited explanations may reduce accuracy.
- **Simple Summary & Project Context:**
  Decision support systems embodying machine learning models offer the promise of an improved standard of care for major depressive disorder, but little is known about how clinicians' treatment decisions will be influenced by machine learning recommendations and explanations. We used a within-subject factorial experiment to present 220 clinicians with patient vignettes, each with or without a machine-learning (ML) recommendation and one of the multiple forms of explanation. We found that interacting with ML recommendations did not significantly improve clinicians' treatment selection accuracy, assessed as concordance with expert psychopharmacologist consensus, compared to baseline scenarios in which clinicians made treatment decisions independently. Interacting with incorrect recommendations paired with explanations that included limited but easily interpretable information did lead to a significant reduction in treatment selection accuracy compared to baseline questions. These results suggest that incorrect ML recommendations may adversely impact clinician treatment selections and that explanations are insufficient for addressing overreliance on imperfect ML algorithms. More generally, our findings challenge the common assumption that clinicians interacting with ML tools will perform better than either clinicians or ML algorithms individually.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/how-machinelearning-recommendations-influence-jacobs-pradier/962940f8145e5f878bc019152692d81c/) | DOI: 10.1038/s41398-021-01224-x

---

### Rank 81: Prospective evaluation of a clinical decision support system in psychological therapy.
- **Relevance Score:** 40/100
- **Authors:** W. Lutz, Anne-Katharina Deisenhofer, Julian A. Rubel, Björn Bennemann, Julia Giesemann, Kaitlyn Poster, Brian Schwartz
- **Year & Journal:** 2021 | *Journal of consulting and clinical psychology* (SJR Quartile: 1.0)
- **Study Type & Citations:** rct | Citations: 120
- **Main Takeaway:** A clinical decision support system in psychological therapy can enhance patient outcomes when successfully implemented and incorporated into clinical practice.
- **Simple Summary & Project Context:**
  Objective: Thus far, most applications in precision mental health have not been evaluated prospectively. This article presents the results of a prospective randomized-controlled trial investigating the effects of a digital decision support and feedback system, which includes two components of patient-specific recommendations: (a) a clinical strategy recommendation and (b) adaptive recommendations for patients at risk for treatment failure.

Method: Therapist-patient dyads (N = 538) in a cognitive behavioral therapy outpatient clinic were randomized to either having access to a decision support system (intervention group; n = 335) or not (treatment as usual; n = 203). First, treatment strategy recommendations (problem-solving, motivation-oriented, or a mix of both strategies) for the first 10 sessions were evaluated. Second, the effect of psychometric feedback enhanced with clinical problem-solving tools on treatment outcome was investigated.

Results: The prospective evaluation showed a differential effect size of about 0.3 when therapists followed the recommended treatment strategy in the first 10 sessions. Moreover, the linear mixed models revealed therapist symptom awareness and therapist attitude and confidence as significant predictors of an outcome as well as therapist-rated usefulness of feedback as a significant moderator of the feedback-outcome and the not on track-outcome associations. However, no main effects were found for feedback.

Conclusions: The results demonstrate the importance of prospective studies and the high-quality implementation of digital decision support tools in clinical practice. Therapists seem to be able to learn from such systems and incorporate them into their clinical practice to enhance patient outcomes, but only when implementation is successful. (PsycInfo Database Record (c) 2022 APA, all rights reserved).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/prospective-evaluation-of-a-clinical-decision-support-lutz-deisenhofer/cf5623d8c14c562da54fcb40f49cf840/) | DOI: 10.1037/ccp0000642

---

### Rank 82: Clinical decision support of radiotherapy treatment planning: A data-driven machine learning strategy for patient-specific dosimetric decision making.
- **Relevance Score:** 40/100
- **Authors:** G. Valdes, C. Simone, Josephine Chen, A. Lin, S. Yom, A. Pattison, C. Carpenter, T. Solberg
- **Year & Journal:** 2017 | *Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 101
- **Main Takeaway:** This study developed a machine learning-based clinical decision support system that helps clinicians identify achievable historical treatment plans for new patients, enabling early dose tradeoffs and optimizing treatment for individual patients.
- **Simple Summary & Project Context:**
  This paper (2017) presents key findings on clinical decision support of radiotherapy treatment planning: a data-driven machine learning strategy for patient-specific dosimetric decision making.. It provides valuable data and insights on how AI models can assist in clinical decision support, predicting treatment efficacy, and matching patient characteristics to optimal outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/clinical-decision-support-of-radiotherapy-treatment-valdes-simone/c0c3a485c02955d7a23784c061e91b35/) | DOI: 10.1016/j.radonc.2017.10.014

---

### Rank 83: Personalized treatment selection in routine care: Integrating machine learning and statistical algorithms to recommend cognitive behavioral or psychodynamic therapy
- **Relevance Score:** 40/100
- **Authors:** Brian Schwartz, Z. Cohen, Julian A. Rubel, Dirk Zimmermann, W. Wittmann, W. Lutz
- **Year & Journal:** 2020 | *Psychotherapy Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 82
- **Main Takeaway:** A treatment selection algorithm using machine learning and statistical inference may improve treatment outcomes for some outpatients, but not all, and support therapists' clinical decision-making.
- **Simple Summary & Project Context:**
  Objective: This study aims at developing a treatment selection algorithm using a combination of machine learning and statistical inference to recommend patients' optimal treatment based on their pre-treatment characteristics. Methods: A disorder-heterogeneous, naturalistic sample of N = 1,379 outpatients treated with either cognitive behavioral therapy or psychodynamic therapy was analyzed. Based on a combination of random forest and linear regression, differential treatment response was modeled in the training data (n = 966) to indicate each individual's optimal treatment. A separate holdout dataset (n = 413) was used to evaluate personalized recommendations. Results: The difference in outcomes between patients treated with their optimal vs. non-optimal treatment was significant in the training data, but non-significant in the holdout data (b = -0.043, p = .280). However, for the 50% of patients with the largest predicted benefit of receiving their optimal treatment, the average percentage of change on the BSI in the holdout data was 52.6% for their optimal and 38.4% for their non-optimal treatment (p = .017; d = 0.33 [0.06, 0.61]). Conclusion: A treatment selection algorithm based on a combination of ML and statistical inference might improve treatment outcome for some, but not all outpatients and could support therapists' clinical decision-making.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalized-treatment-selection-in-routine-care-schwartz-cohen/e1ca21a2c4555ec29876a07b4e18415a/) | DOI: 10.1080/10503307.2020.1769219

---

### Rank 84: Discovery and Clinical Decision Support for Personalized Healthcare
- **Relevance Score:** 40/100
- **Authors:** Jinsung Yoon, C. Davtyan, M. van der Schaar
- **Year & Journal:** 2017 | *IEEE Journal of Biomedical and Health Informatics* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 79
- **Main Takeaway:** The discovery engine (DE) effectively discovers patient characteristics relevant for diagnosis and treatment recommendations, improving healthcare outcomes.
- **Simple Summary & Project Context:**
  With the advent of electronic health records, more data are continuously collected for individual patients, and more data are available for review from past patients. Despite this, it has not yet been possible to successfully use this data to systematically build clinical decision support systems that can produce personalized clinical recommendations to assist clinicians in providing individualized healthcare. In this paper, we present a novel approach, discovery engine (DE), that discovers which patient characteristics are most relevant for predicting the correct diagnosis and/or recommending the best treatment regimen for each patient. We demonstrate the performance of DE in two clinical settings: diagnosis of breast cancer as well as a personalized recommendation for a specific chemotherapy regimen for breast cancer patients. For each distinct clinical recommendation, different patient features are relevant; DE can discover these different relevant features and use them to recommend personalized clinical decisions. The DE approach achieves a 16.6% improvement over existing state-of-the-art recommendation algorithms regarding kappa coefficients for recommending the personalized chemotherapy regimens. For diagnostic predictions, the DE approach achieves a 2.18% and 4.20% improvement over existing state-of-the-art prediction algorithms regarding prediction error rate and false positive rate, respectively. We also demonstrate that the performance of our approach is robust against missing information and that the relevant features discovered by DE are confirmed by clinical references.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/discovery-and-clinical-decision-support-for-personalized-yoon-davtyan/6a9fb394cffd5fe48a4ddacda761ec6d/) | DOI: 10.1109/jbhi.2016.2574857

---

### Rank 85: State of the Art of Machine Learning–Enabled Clinical Decision Support in Intensive Care Units: Literature Review
- **Relevance Score:** 40/100
- **Authors:** Na Hong, Chun Liu, Jianwei Gao, Lin Han, Fengxiang Chang, Mengchun Gong, Longxiang Su
- **Year & Journal:** 2022 | *JMIR Medical Informatics* (SJR Quartile: 1.0)
- **Study Type & Citations:** systematic review | Citations: 76
- **Main Takeaway:** Machine learning-enabled clinical decision support in intensive care units can improve diagnosis, outcome prediction, risk event identification, and treatment decisions, but further development is needed.
- **Simple Summary & Project Context:**
  Background: Modern clinical care in intensive care units is full of rich data, and machine learning has great potential to support clinical decision-making. The development of intelligent machine learning-based clinical decision support systems is facing great opportunities and challenges. Clinical decision support systems may directly help clinicians accurately diagnose, predict outcomes, identify risk events, or decide treatments at the point of care.

Objective: We aimed to review the research and application of machine learning-enabled clinical decision support studies in intensive care units to help clinicians, researchers, developers, and policy makers better understand the advantages and limitations of machine learning-supported diagnosis, outcome prediction, risk event identification, and intensive care unit point-of-care recommendations.

Methods: We searched papers published in the PubMed database between January 1980 and October 2020. We defined selection criteria to identify papers that focused on machine learning-enabled clinical decision support studies in intensive care units and reviewed the following aspects: research topics, study cohorts, machine learning models, analysis variables, and evaluation metrics.

Results: A total of 643 papers were collected, and using our selection criteria, 97 studies were found. Studies were categorized into 4 topics-monitoring, detection, and diagnosis (13/97, 13.4%), early identification of clinical events (32/97, 33.0%), outcome prediction and prognosis assessment (46/97, 47.6%), and treatment decision (6/97, 6.2%). Of the 97 papers, 82 (84.5%) studies used data from adult patients, 9 (9.3%) studies used data from pediatric patients, and 6 (6.2%) studies used data from neonates. We found that 65 (67.0%) studies used data from a single center, and 32 (33.0%) studies used a multicenter data set; 88 (90.7%) studies used supervised learning, 3 (3.1%) studies used unsupervised learning, and 6 (6.2%) studies used reinforcement learning. Clinical variable categories, starting with the most frequently used, were demographic (n=74), laboratory values (n=59), vital signs (n=55), scores (n=48), ventilation parameters (n=43), comorbidities (n=27), medications (n=18), outcome (n=14), fluid balance (n=13), nonmedicine therapy (n=10), symptoms (n=7), and medical history (n=4). The most frequently adopted evaluation metrics for clinical data modeling studies included area under the receiver operating characteristic curve (n=61), sensitivity (n=51), specificity (n=41), accuracy (n=29), and positive predictive value (n=23).

Conclusions: Early identification of clinical and outcome prediction and prognosis assessment contributed to approximately 80% of studies included in this review. Using new algorithms to solve intensive care unit clinical problems by developing reinforcement learning, active learning, and time-series analysis methods for clinical decision support will be greater development prospects in the future.

©Na Hong, Chun Liu, Jianwei Gao, Lin Han, Fengxiang Chang, Mengchun Gong, Longxiang Su. Originally published in JMIR Medical Informatics (https://medinform.jmir.org), 03.03.2022.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/state-of-the-art-of-machine-learning%E2%80%93enabled-clinical-hong-liu/1883efd84e5154dc8b236342e2d02d65/) | DOI: 10.2196/28781

---

### Rank 86: Deep reinforcement learning for personalized treatment recommendation
- **Relevance Score:** 40/100
- **Authors:** Ming Liu, Xiao-Tong T. Shen, W. Pan
- **Year & Journal:** 2022 | *Statistics in medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** Not specified | Citations: 62
- **Main Takeaway:** Deep reinforcement learning (DRL)-based PPORank outperforms supervised learning methods in recommending personalized cancer treatments based on patient-specific molecular and clinical profiles.
- **Simple Summary & Project Context:**
  In precision medicine, the ultimate goal is to recommend the most effective treatment to an individual patient based on patient-specific molecular and clinical profiles, possibly high-dimensional. To advance cancer treatment, large-scale screenings of cancer cell lines against chemical compounds have been performed to help better understand the relationship between genomic features and drug response; existing machine learning approaches use exclusively supervised learning, including penalized regression and recommender systems. However, it would be more efficient to apply reinforcement learning to sequentially learn as data accrue, including selecting the most promising therapy for a patient given individual molecular and clinical features and then collecting and learning from the corresponding data. In this article, we propose a novel personalized ranking system called Proximal Policy Optimization Ranking (PPORank), which ranks the drugs based on their predicted effects per cell line (or patient) in the framework of deep reinforcement learning (DRL). Modeled as a Markov decision process, the proposed method learns to recommend the most suitable drugs sequentially and continuously over time. As a proof-of-concept, we conduct experiments on two large-scale cancer cell line data sets in addition to simulated data. The results demonstrate that the proposed DRL-based PPORank outperforms the state-of-the-art competitors based on supervised learning. Taken together, we conclude that novel methods in the framework of DRL have great potential for precision medicine and should be further studied.

© 2022 The Authors. Statistics in Medicine published by John Wiley & Sons Ltd.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/deep-reinforcement-learning-for-personalized-treatment-liu-shen/00bcdc32cdfb51b0a128c642c000bb57/) | DOI: 10.1002/sim.9491

---

### Rank 87: Quantum deep reinforcement learning for clinical decision support in oncology: application to adaptive radiotherapy
- **Relevance Score:** 40/100
- **Authors:** D. Niraula, J. Jamaluddin, M. Matuszak, R. T. Ten Haken, I. El Naqa
- **Year & Journal:** 2021 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 60
- **Main Takeaway:** Quantum deep reinforcement learning (qDRL) can potentially improve clinical radiotherapy decision-making by at least 10% compared to unaided clinical practice.
- **Simple Summary & Project Context:**
  Subtle differences in a patient's genetics and physiology may alter radiotherapy (RT) treatment responses, motivating the need for a more personalized treatment plan. Accordingly, we have developed a novel quantum deep reinforcement learning (qDRL) framework for clinical decision support that can estimate an individual patient's dose response mid-treatment and recommend an optimal dose adjustment. Our framework considers patients' specific information including biological, physical, genetic, clinical, and dosimetric factors. Recognizing that physicians must make decisions amidst uncertainty in RT treatment outcomes, we employed indeterministic quantum states to represent human decision making in a real-life scenario. We paired quantum decision states with a model-based deep q-learning algorithm to optimize the clinical decision-making process in RT. We trained our proposed qDRL framework on an institutional dataset of 67 stage III non-small cell lung cancer (NSCLC) patients treated on prospective adaptive protocols and independently validated our framework in an external multi-institutional dataset of 174 NSCLC patients. For a comprehensive evaluation, we compared three frameworks: DRL, qDRL trained in a Qiskit quantum computing simulator, and qDRL trained in an IBM quantum computer. Two metrics were considered to evaluate our framework: (1) similarity score, defined as the root mean square error between retrospective clinical decisions and the AI recommendations, and (2) self-evaluation scheme that compares retrospective clinical decisions and AI recommendations based on the improvement in the observed clinical outcomes. Our analysis shows that our framework, which takes into consideration individual patient dose response in its decision-making, can potentially improve clinical RT decision-making by at least about 10% compared to unaided clinical practice. Further validation of our novel quantitative approach in a prospective study will provide a necessary framework for improving the standard of care in personalized RT.

© 2021. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/quantum-deep-reinforcement-learning-for-clinical-niraula-jamaluddin/20990cda5bb057f396ebfd3e44b9804d/) | DOI: 10.1038/s41598-021-02910-y

---

### Rank 88: Therapy Decision Support Based on Recommender System Methods
- **Relevance Score:** 40/100
- **Authors:** Felix Gräßer, Stefanie Beckert, D. Küster, J. Schmitt, S. Abraham, H. Malberg, S. Zaunseder
- **Year & Journal:** 2017 | *Journal of Healthcare Engineering* (SJR Quartile: 2.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 52
- **Main Takeaway:** Both Collaborative Recommender and Demographic-based Recommender methods can improve therapy decision support, but their effectiveness depends on the availability of data and the patient's condition.
- **Simple Summary & Project Context:**
  We present a system for data-driven therapy decision support based on techniques from the field of recommender systems. Two methods for therapy recommendation, namely, Collaborative Recommender and Demographic-based Recommender, are proposed. Both algorithms aim to predict the individual response to different therapy options using diverse patient data and recommend the therapy which is assumed to provide the best outcome for a specific patient and time, that is, consultation. The proposed methods are evaluated using a clinical database incorporating patients suffering from the autoimmune skin disease psoriasis. The Collaborative Recommender proves to generate both better outcome predictions and recommendation quality. However, due to sparsity in the data, this approach cannot provide recommendations for the entire database. In contrast, the Demographic-based Recommender performs worse on average but covers more consultations. Consequently, both methods profit from a combination into an overall recommender system.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/therapy-decision-support-based-on-recommender-system-gr%C3%A4%C3%9Fer-beckert/0b9af661530f56dbb6f90144aa54178e/) | DOI: 10.1155/2017/8659460

---

### Rank 89: Machine Learning Predictive Model as Clinical Decision Support System in Orthodontic Treatment Planning
- **Relevance Score:** 40/100
- **Authors:** Jahnavi Prasad, Dharma R. Mallikarjunaiah, Akshai Shetty, Narayan H. Gandedkar, A. B. Chikkamuniswamy, P. C. Shivashankar
- **Year & Journal:** 2022 | *Dentistry Journal* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 43
- **Main Takeaway:** Machine Learning models show potential as a valuable Clinical Decision Support System in orthodontic diagnosis and treatment planning, with an average accuracy of 84%.
- **Simple Summary & Project Context:**
  Diagnosis and treatment planning forms the crux of orthodontics, which orthodontists gain with years of expertise. Machine Learning (ML), having the ability to learn by pattern recognition, can gain this expertise in a very short duration, ensuring reduced error, inter-intra clinician variability and good accuracy. Thus, the aim of this study was to construct an ML predictive model to predict a broader outline of the orthodontic diagnosis and treatment plan. The sample consisted of 700 case records of orthodontically treated patients in the past ten years. The data were split into a training and a test set. There were 33 input variables and 11 output variables. Four ML predictive model layers with seven algorithms were created. The test set was used to check the efficacy of the ML-predicted treatment plan and compared with that of the decision made by the expert orthodontists. The model showed an overall average accuracy of 84%, with the Decision Tree, Random Forest and XGB classifier algorithms showing the highest accuracy ranging from 87-93%. Yet in their infancy stages, Machine Learning models could become a valuable Clinical Decision Support System in orthodontic diagnosis and treatment planning in the future.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/machine-learning-predictive-model-as-clinical-decision-prasad-mallikarjunaiah/bb4afd128409572484b5cbfcab37daff/) | DOI: 10.3390/dj11010001

---

### Rank 90: Medical recommender systems based on continuous-valued logic and multi-criteria decision operators, using interpretable neural networks
- **Relevance Score:** 40/100
- **Authors:** O. Csiszár, Thomas Schimper
- **Year & Journal:** 2021 | *BMC Medical Informatics and Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 43
- **Main Takeaway:** Our novel recommender system, using continuous-valued logic and multi-criteria decision operators, can predict the best therapy for patients with diabetes and heart insufficiency, improving healthcare quality while maintaining transparency and safety.
- **Simple Summary & Project Context:**
  Background: Out of the pressure of Digital Transformation, the major industrial domains are using advanced and efficient digital technologies to implement processes that are applied on a daily basis. Unfortunately, this still does not happen in the same way in the medical domain. For this reason, doctors usually do not have the time or knowledge to evaluate all alternative treatment options for each patient accurately and individually. However, physicians can reduce their workload by using recommender systems, still having every decision under control. In this way, they also get an insight into how other physicians make treatment decisions in each situation. In this work, we report the development of a novel recommender system that uses predicted outcomes based on continuous-valued logic and multi-criteria decision operators. The advantage of this methodology is that it is transparent, since the model outcomes emulate logical decision processes based on the hierarchy of relevant physiological parameters, and second, it is safer against adversarial attacks than conventional deep learning methods since it drastically reduces the number of trainable parameters.

Methods: We test our methodology in a patient population with diabetes and heart insufficiency that becomes a therapy (beta-blockers, ACE or Aspirin). The original database (Pakistan database) is publicly available and accessible via the internet. However, to explore methods to protect the patient's identity and guarantee data privacy we implemented a methodology on a variable-by-variable basis by fitting a sequence of regression models and drawing synthetic values from the corresponding predictive distributions using linear regressions and norm rank. Furthermore, we implemented a deep-learning model based on logical gates modeled by perceptrons with fixed weights and biases. While a first trainable layer automatically recognizes a meaningful parameter hierarchy, the implemented Logic-Operator Neuronal Network (LONN) simulates cognitive processes like a rational, logical thinking process, considering that this logic is joined by fuzziness, i.e., logical operations are not exact but essentially fuzzy due to the implemented continuous-valued operators. The predicted outcomes of the model (kind of therapy-ACE, Aspirin or beta-blocker- and expected therapy time of the patient) are then implemented in a recommender system that compares two different models: model 1 trained on a population excluding negative outcomes (patient group 1, with no patient dead and long therapy times) and a model 2 trained on the whole patient population (patient group 2). In this way, we provide a recommendation of the best possible therapy based on the outcome of the model and the confidence of this recommendation when the outcome of model 1 is compared with the outcome of model 2.

Results: With the applied method for data synthetization, we obtained an error of about 1% for all the relevant parameters. Furthermore, we demonstrate that the LONN models reach an accuracy of about 75%. After comparing the LONN models against conventional deep-learning models we observe that our implemented models are less accurate (accuracy loss of about 8%). However, the loss of accuracy is compensated by the fact that LONN models are transparent and safe because the freezing of training parameters makes them less prone to adversarial attacks. Finally, we predict the best therapy as well as the expected therapy time. We were able to predict individualized therapies, which were classified as optimal (binary value) when the prediction fully matched predictions made with models 1 and 2. The results provided by the recommender system are displayed using a graphical interface. The current is a proof of concept to improve the quality of the disease management, while the methods are continuously visualized to preserve transparency for the customers.

Conclusions: This work contributes to simplify administrative functions and boost the quality of management of patients improving the quality of healthcare with models that are both transparent and safe. Our methodology can be extended to different clinical scenarios where recommender systems can be applied. The acceptance and further development of the app is one of the next important steps and still requires further development depending on specific requirements of the health management, the physicians or health professionals, and the patent population.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/medical-recommender-systems-based-on-continuousvalued-csisz%C3%A1r-schimper/2645dc530f99540d94932c5dc3a954ba/) | DOI: 10.1186/s12911-021-01553-3

---

### Rank 91: Predicting Therapy Success and Costs for Personalized Treatment Recommendations Using Baseline Characteristics: Data-Driven Analysis
- **Relevance Score:** 40/100
- **Authors:** Vincent Bremer, Dennis Becker, S. Kolovos, Burkhardt Funk, W. V. van Breda, M. Hoogendoorn, H. Riper
- **Year & Journal:** 2018 | *Journal of Medical Internet Research* (SJR Quartile: 1.0)
- **Study Type & Citations:** rct | Citations: 36
- **Main Takeaway:** Personalized treatment recommendations can be provided at baseline using baseline data, potentially leading to improved decision-making, better outcomes, and reduced healthcare costs for patients with psychological disorders.
- **Simple Summary & Project Context:**
  Background: Different treatment alternatives exist for psychological disorders. Both clinical and cost effectiveness of treatment are crucial aspects for policy makers, therapists, and patients and thus play major roles for healthcare decision-making. At the start of an intervention, it is often not clear which specific individuals benefit most from a particular intervention alternative or how costs will be distributed on an individual patient level.

Objective: This study aimed at predicting the individual outcome and costs for patients before the start of an internet-based intervention. Based on these predictions, individualized treatment recommendations can be provided. Thus, we expand the discussion of personalized treatment recommendation.

Methods: Outcomes and costs were predicted based on baseline data of 350 patients from a two-arm randomized controlled trial that compared treatment as usual and blended therapy for depressive disorders. For this purpose, we evaluated various machine learning techniques, compared the predictive accuracy of these techniques, and revealed features that contributed most to the prediction performance. We then combined these predictions and utilized an incremental cost-effectiveness ratio in order to derive individual treatment recommendations before the start of treatment.

Results: Predicting clinical outcomes and costs is a challenging task that comes with high uncertainty when only utilizing baseline information. However, we were able to generate predictions that were more accurate than a predefined reference measure in the shape of mean outcome and cost values. Questionnaires that include anxiety or depression items and questions regarding the mobility of individuals and their energy levels contributed to the prediction performance. We then described how patients can be individually allocated to the most appropriate treatment type. For an incremental cost-effectiveness threshold of 25,000 €/quality-adjusted life year, we demonstrated that our recommendations would have led to slightly worse outcomes (1.98%), but with decreased cost (5.42%).

Conclusions: Our results indicate that it was feasible to provide personalized treatment recommendations at baseline and thus allocate patients to the most beneficial treatment type. This could potentially lead to improved decision-making, better outcomes for individuals, and reduced health care costs.

©Vincent Bremer, Dennis Becker, Spyros Kolovos, Burkhardt Funk, Ward van Breda, Mark Hoogendoorn, Heleen Riper. Originally published in the Journal of Medical Internet Research (http://www.jmir.org), 21.08.2018.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/predicting-therapy-success-and-costs-for-personalized-bremer-becker/bec29b3cd6ad513482292fd6c391002d/) | DOI: 10.2196/10275

---

### Rank 92: Bone mineral density response prediction following osteoporosis treatment using machine learning to aid personalized therapy
- **Relevance Score:** 40/100
- **Authors:** Thiraphat Tanphiriyakun, S. Rojanasthien, Piyapong Khumrin
- **Year & Journal:** 2021 | *Scientific Reports* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 27
- **Main Takeaway:** Our machine learning-based decision support system effectively predicts bone mineral density response after osteoporosis treatment, aiding in personalized therapy and improving bone health.
- **Simple Summary & Project Context:**
  Osteoporosis is a global health problem for ageing populations. The goals of osteoporosis treatment are to improve bone mineral density (BMD) and prevent fractures. One major obstacle that remains a great challenge to achieve the goals is how to select the best treatment regimen for individual patients. We developed a computational model from 8981 clinical variables, including demographic data, diagnoses, laboratory results, medications, and initial BMD results, taken from 10-year period of electronic medical records to predict BMD response after treatment. We trained 7 machine learning models with 13,562 osteoporosis treatment instances [comprising 5080 (37.46%) inadequate treatment responses and 8482 (62.54%) adequate responses] and selected the best model (Random Forests with area under the receiver operating curve of 0.70, accuracy of 0.69, precision of 0.70, and recall of 0.89) to individually predict treatment responses of 11 therapeutic regimens, then selected the best predicted regimen to compare with the actual regimen. The results showed that the average treatment response of the recommended regimens was 9.54% higher than the actual regimens. In summary, our novel approach using a machine learning-based decision support system is capable of predicting BMD response after osteoporosis treatment and personalising the most appropriate treatment regimen for an individual patient.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/bone-mineral-density-response-prediction-following-tanphiriyakun-rojanasthien/2abbbf5677a85a55835f57571cd45fb3/) | DOI: 10.1038/s41598-021-93152-5

---

### Rank 93: A treatment recommender clinical decision support system for personalized medicine: method development and proof-of-concept for drug resistant tuberculosis
- **Relevance Score:** 40/100
- **Authors:** Lennert Verboven, T. Calders, S. Callens, J. Black, G. Maartens, K. Dooley, S. Potgieter, R. Warren, K. Laukens, A. Van Rie
- **Year & Journal:** 2021 | *BMC Medical Informatics and Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 27
- **Main Takeaway:** Our novel treatment recommender CDSS successfully identifies optimal treatment regimens for drug-resistant tuberculosis patients, with 95% precision at one, but model overfitting reduces precision to 78% in real-life clinical settings.
- **Simple Summary & Project Context:**
  Background: Personalized medicine tailors care based on the patient's or pathogen's genotypic and phenotypic characteristics. An automated Clinical Decision Support System (CDSS) could help translate the genotypic and phenotypic characteristics into optimal treatment and thus facilitate implementation of individualized treatment by less experienced physicians.

Methods: We developed a hybrid knowledge- and data-driven treatment recommender CDSS. Stakeholders and experts first define the knowledge base by identifying and quantifying drug and regimen features for the prototype model input. In an iterative manner, feedback from experts is harvested to generate model training datasets, machine learning methods are applied to identify complex relations and patterns in the data, and model performance is assessed by estimating the precision at one, mean reciprocal rank and mean average precision. Once the model performance no longer iteratively increases, a validation dataset is used to assess model overfitting.

Results: We applied the novel methodology to develop a treatment recommender CDSS for individualized treatment of drug resistant tuberculosis as a proof of concept. Using input from stakeholders and three rounds of expert feedback on a dataset of 355 patients with 129 unique drug resistance profiles, the model had a 95% precision at 1 indicating that the highest ranked treatment regimen was considered appropriate by the experts in 95% of cases. Use of a validation data set however suggested substantial model overfitting, with a reduction in precision at 1 to 78%.

Conclusion: Our novel and flexible hybrid knowledge- and data-driven treatment recommender CDSS is a first step towards the automation of individualized treatment for personalized medicine. Further research should assess its value in fields other than drug resistant tuberculosis, develop solid statistical approaches to assess model performance, and evaluate their accuracy in real-life clinical settings.

© 2022. The Author(s).
- **Reference Link:** [Consensus Link](https://consensus.app/papers/a-treatment-recommender-clinical-decision-support-system-verboven-calders/432699309964554c8ad1ded44821c111/) | DOI: 10.1186/s12911-022-01790-0

---

### Rank 94: Personalization of Medical Treatment Decisions: Simplifying Complex Models while Maintaining Patient Health Outcomes
- **Relevance Score:** 40/100
- **Authors:** C. Weyant, M. Brandeau
- **Year & Journal:** 2021 | *Medical decision making : an international journal of the Society for Medical Decision Making* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 12
- **Main Takeaway:** Our machine learning method simplifies complex medical treatment decision models while maintaining patient health outcomes, making them more adoptable and improving equity in patient outcomes.
- **Simple Summary & Project Context:**
  Background: Personalizing medical treatments based on patient-specific risks and preferences can improve patient health. However, models to support personalized treatment decisions are often complex and difficult to interpret, limiting their clinical application.

Methods: We present a new method, using machine learning to create meta-models, for simplifying complex models for personalizing medical treatment decisions. We consider simple interpretable models, interpretable ensemble models, and noninterpretable ensemble models. We use variable selection with a penalty for patient-specific risks and/or preferences that are difficult, risky, or costly to obtain. We interpret the meta-models to the extent permitted by their model architectures. We illustrate our method by applying it to simplify a previously developed model for personalized selection of antipsychotic drugs for patients with schizophrenia.

Results: The best simplified interpretable, interpretable ensemble, and noninterpretable ensemble models contained at most half the number of patient-specific risks and preferences compared with the original model. The simplified models achieved 60.5% (95% credible interval [crI]: 55.2-65.4), 60.8% (95% crI: 55.5-65.7), and 83.8% (95% crI: 80.8-86.6), respectively, of the net health benefit of the original model (quality-adjusted life-years gained). Important variables in all models were similar and made intuitive sense. Computation time for the meta-models was orders of magnitude less than for the original model.

Limitations: The simplified models share the limitations of the original model (e.g., potential biases).

Conclusions: Our meta-modeling method is disease- and model- agnostic and can be used to simplify complex models for personalization, allowing for variable selection in addition to improved model interpretability and computational performance. Simplified models may be more likely to be adopted in clinical settings and can help improve equity in patient outcomes.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/personalization-of-medical-treatment-decisions-weyant-brandeau/8b389a3b786f5042a2d4909766a6412f/) | DOI: 10.1177/0272989x211037921

---

### Rank 95: Using artificial intelligence to develop a measure of orthopaedic treatment success from clinical notes
- **Relevance Score:** 40/100
- **Authors:** Sarah B. Floyd, Ahmed G. Almeldien, D. H. Smith, Benjamin L. Judkins, Claire E. Krohn, Z. Reynolds, Kyle J. Jeray, J. Obeid
- **Year & Journal:** 2025 | *Frontiers in Digital Health* (SJR Quartile: 1.0)
- **Study Type & Citations:** cross-sectional study | Citations: 7
- **Main Takeaway:** AI-based text classifiers can accurately distinguish between successful treatment outcomes and failures in clinical notes, potentially serving as a valuable data source for orthopaedic patients.
- **Simple Summary & Project Context:**
  Introduction: A readily available outcome measure that reflects the success of a patient's treatment is needed to demonstrate the value of orthopaedic interventions. Patient-reported outcome measures (PROMs) are survey-based instruments that collect joint-specific and general health perceptions on symptoms, functioning, and health-related quality of life. PROMs are considered the gold standard outcome measure in orthopaedic medicine, but their use is limited in real-world practice due to challenges with technology integration, the pace of clinic workflows, and patient compliance. Clinical notes generated during each encounter patients have with their physician contain rich information on current disease symptoms, rehabilitation progress, and unexpected complications. Artificial intelligence (AI) methods can be used to identify phrases of treatment success or failure captured in clinical notes and discern an indicator of treatment success for orthopaedic patients.

Methods: This was a cross-sectional analysis of clinical notes from a sample of patients with an acute shoulder injury. The study included adult patients presenting to a Level-1 Trauma Center and regional health system for an acute Proximal Humerus Fracture (PHF) between January 1, 2019 and December 31, 2021. We used the progress note from the office visit for PHF-related care (ICD10: S42.2XXX) or shoulder pain (ICD10: M45.2XXX) closest to 1-year after the injury date. Clinical notes were reviewed by an orthopaedic resident and labeled as treatment success or failure. A structured comparative analysis of classifiers including both machine and deep learning algorithms was performed.

Results: The final sample included 868 clinical notes from patients treated by 123 physicians across 35 departments within one regional health system. The study sample was stratified into 465 notes labeled as treatment success and 403 labeled as treatment failure. The Bio-ClinicalBERT model had the highest performance of 87% accuracy (AUC = 0.87 ± 0.04) in correctly distinguishing between treatment success and failure notes.

Discussion: Our results suggest that text classifiers applied to clinical notes are capable of differentiating patients with successful treatment outcomes with high levels of accuracy. This finding is encouraging, signaling that routinely collected clinical note content may serve as a data source to develop an outcome measure for orthopaedic patients.

© 2025 Floyd, Almeldien, Smith, Judkins, Krohn, Reynolds, Jeray and Obeid.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/using-artificial-intelligence-to-develop-a-measure-of-floyd-almeldien/e0c7725401b05ea3927a723cfbc1a9b3/) | DOI: 10.3389/fdgth.2025.1523953

---

### Rank 96: Artificial Intelligence and its Current Role in Clinical Outcome Prediction, Musculoskeletal Imaging, and Economic and Ethical Considerations within Orthopedics and Sports Medicine.
- **Relevance Score:** 40/100
- **Authors:** Emmett O'Malley, Brian M. Soth, Alex Capitano, A. Bensa, Joshua R. Eskew, Malik E. Dancy, Benedict U. Nwachukwu
- **Year & Journal:** 2026 | *Current reviews in musculoskeletal medicine* (SJR Quartile: 1.0)
- **Study Type & Citations:** literature review | Citations: 1
- **Main Takeaway:** AI models show promise in predicting patient outcomes, surgical complications, and healthcare utilization in orthopedics and sports medicine, but challenges in validation, accessibility, and ethical considerations remain.
- **Simple Summary & Project Context:**
  PURPOSE OF REVIEW: Artificial intelligence (AI) has emerged as a useful tool across the field of orthopedic surgery. This review highlights recent literature on AI’s role in surgical outcome prediction, musculoskeletal imaging, economic and ethical considerations, with a focus on its integration in sports medicine workflow and procedures. RECENT FINDINGS: Machine learning AI models have demonstrated superior accuracy in predicting orthopedic related patient-reported outcomes, surgical complications, and the utilization of healthcare compared to traditional, non-AI methods. Within imaging, AI applications now produce automated measurements for clinical and presurgical planning with precision equivalent to expert-level measurements. Large language AI models are increasingly used for clinical documentation, research workflows, and administrative support for healthcare delivery and effectiveness. Despite increasing integration of AI into orthopedics and its subspecialties, challenges in validation, accessibility due to cost, and ethical considerations remain. Orthopedic surgery and sports medicine are particularly well suited for AI applications due to their well-defined, measurable clinical outcomes. Emerging AI tools and models show promise in enhancing patient outcomes, surgical planning, and healthcare efficiency. Continued AI research must prioritize external validation, ethical implementation, and educational integration to ensure responsible, effective, and reproducible use.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/artificial-intelligence-and-its-current-role-in-clinical-omalley-soth/8d20467fd61e5cf6b6f19e733f19297f/) | DOI: 10.1007/s12178-026-10019-w

---

### Rank 97: Evaluation of centre‐specific machine learning models in predicting 2‐year outcomes of hip arthroscopy for mixed femoracetabular impingement syndrome
- **Relevance Score:** 40/100
- **Authors:** Gang Yang, Jiali Kang, Fan Hu, Yin Pei, Ding-Ge Liu, Zhi-Hua Zhang, Kaiping Liu, Langran Wang, Xi Gong, Haijun Wang, Shuangshuang Deng, Rui-jie Liu, Xin Zhang
- **Year & Journal:** 2025 | *Journal of Experimental Orthopaedics* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 1
- **Main Takeaway:** Random forest machine learning model accurately predicts patient-reported outcomes in hip arthroscopy for mixed femoracetabular impingement syndrome, with preoperative factors being the most important predictors.
- **Simple Summary & Project Context:**
  Purpose: To construct a centre-specific machine learning (ML) prediction model based on preoperative factors. It was hypothesised that the ML prediction model would accurately predict whether patient-reported outcome scores (PROs) over at least 2 years would reach the minimal clinically important difference (MCID).

Methods: A retrospective analysis was performed on mixed-type femoroacetabular impingement syndrome (FAIS) patients who had hip arthroscopy at our institution between 2016 and 2018. The primary outcome was the rate of achieving MCID in PROs assessed at least 2 years after surgery, PROs included the hip outcome score-activities of daily living (HOS-ADL), modified Harris Hip Score (mHHS), visual analogue scale (VAS) for pain and international hip outcome tool-12 (iHOT-12), assessed at a minimum of 2 years postoperatively. Preoperative patient features were selected using the least absolute shrinkage and selection operator (LASSO) algorithm. Three ML models were constructed using balanced sample data and optimal feature subsets: logistic regression (LR), support vector machine (SVM) and random forest (RF). Model performance was assessed using the area under the receiver operating characteristic curve (AUROC) and the concordance index (C-index). Model interpretations were conducted using the SHapley Additive explanation (SHAP) method.

Results: A total of 210 patients (48.1% female) were included. The LR, SVM, RF models had AUROC 0.76 (0.61-0.83), 0.89 (0.80-0.94), 0.99 (0.98-1.00), respectively, and C-index 0.74 (0.65-0.82), 0.86 (0.81-0.90), 0.95 (0.93-0.96), respectively. Preoperative symptom duration, preoperative HOS-ADL, hip joint space and preoperative alpha angle were identified as the most important predictors.

Conclusion: Among the three ML prediction models, RF performed best in predicting whether PROs reached MCID, demonstrating excellent discriminative ability, calibration and robustness. This indicates that individualised and robust ML prediction models for outcome prediction based on preoperative factors are feasible even with limited amounts of centre-specific data.

Level of Evidence: Level III.

© 2025 The Author(s). Journal of Experimental Orthopaedics published by John Wiley & Sons Ltd on behalf of European Society of Sports Traumatology, Knee Surgery and Arthroscopy.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/evaluation-of-centre%E2%80%90specific-machine-learning-models-in-yang-kang/469a757405e4508d918156c94e48c23f/) | DOI: 10.1002/jeo2.70477

---

### Rank 98: SRS108 - Predicting patient-reported outcome measures and evaluating the impact of pre-operative comorbidities on outcomes of hip and knee arthroplasty using supervised machine learning
- **Relevance Score:** 40/100
- **Authors:** Ibrahim Abdelrahman, Amr Selim, S. Davies, A. Roberts, Geraint Thomas, P. Cool
- **Year & Journal:** 2026 | *British Journal of Surgery* (SJR Quartile: 1.0)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** Machine learning models can predict clinically important improvement in hip and knee arthroplasty, with preoperative anxiety and depression linked to reduced likelihood of meaningful improvement.
- **Simple Summary & Project Context:**
  Machine learning (ML) is increasingly applied in orthopaedics for outcome prediction. This project aimed to develop and internally validate supervised ML models that predict clinically important improvement after primary hip and knee arthroplasty using NHS PROMs database, assess whether these data can reliably predict postoperative PROMs for policy making, and to evaluate the association of comorbidities with postoperative improvement.
 
 
 
 We analysed anonymised NHS England PROMs data from 2018/2019, including 37 725 hip and 43 639 knee replacements. Predictors included demographics, symptom duration, living arrangements, comorbidities, and baseline PROMs (Oxford Hip Score [OHS], Oxford Knee Score [OKS], EQ-5D-3L, and EQ-5D VAS). The primary outcome was OHS/OKS improvement, defined as ≥10 points or postoperative score ≥40. Five ML Models were tested with cross-validation.
 
 
 
 In hips, all models achieved high precision (0.91), recall (1.00), and F1 (0.95). ROC-AUC values ranged 0.67–0.70. For knees, precision was 0.81–0.82, recall 0.99–1.00, and F1 0.89–0.90, with ROC-AUC 0.64–0.66. SHAP analysis identified key predictors: pre-disability, baseline OHS, and limping for hips; and baseline OKS score, EQ-VAS, and disability for knees.
 
 
 
 ML models predicted hip outcomes moderately well but had lower discrimination for knees. The NHS PROMs dataset shows potential for ML and policy applications, though data quality improvements are needed, including standardised PROMs collection, better comorbidity coding, and separating unicompartmental from total knee outcomes. Preoperative anxiety and depression were linked with reduced likelihood of meaningful improvement and future studies should investigate the biological link underlying this correlation.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/srs108-predicting-patientreported-outcome-measures-and-abdelrahman-selim/23534e7b406c5095b182358555a7d4d4/) | DOI: 10.1093/bjs/znag018.105

---

### Rank 99: AI in physical rehabilitation of traumatological and orthopedic patients: existing technologies and their clinical effectiveness. A review
- **Relevance Score:** 40/100
- **Authors:** R. Nurlygayanov, L. T. Gilmutdinova, L. Marchenkova, J. A. Bogdanova, B. Gilmutdinov, A. R. Gilmutdinov, E. Faizova, Evgenia V. Semenova, D. Nurlygayanova
- **Year & Journal:** 2026 | *Bulletin of Rehabilitation Medicine* (SJR Quartile: Not specified)
- **Study Type & Citations:** systematic review | Citations: 0
- **Main Takeaway:** AI technologies have demonstrated real clinical value in predicting functional outcomes and predicting complications in trauma and orthopedic patients.
- **Simple Summary & Project Context:**
  INTRODUCTION. Artificial intelligence (AI) and machine learning represent a promising approach in the rehabilitation of trauma and orthopedic patients. The integration of predictive models and adaptive algorithms into rehabilitation practices enables personalized rehabilitation treatment and improves functional outcomes. 
AIM. To systematize and assess the evidence base for the use of AI technologies in the rehabilitation of patients following orthopedic and trauma interventions, including joint replacement, fracture fixation, and spinal surgery. 
МATERIALS AND METHODS. A narrative review of publications devoted to the use of machine learning algorithms, deep learning, convolutional and recurrent neural networks in the rehabilitation of traumatological and orthopedic patients was carried out. The search for sources was carried out between June 2025 and January 2026 in the international databases PubMed/MEDLINE, Scopus and Web of Science Core Collection for the period from January 2014 to February 2024. Studies were analyzed that included predictive models of functional outcomes, motion monitoring systems, and the prediction of complications and hospital stay. A primary search yielded 1247 publications, after removing duplicates and sequentially selecting by inclusion and exclusion criteria, 43 sources were selected for the final analysis, which formed the basis of this review. 
МAIN CONTENT OF THE REVIEW. Machine learning algorithms demonstrated high predictive accuracy in predicting functional outcomes after hip and knee arthroplasty (AUC 0.852–0.98), assessing fracture union (accuracy up to 0.98), predicting postoperative complications (AUC 0.810–0.835), and length of hospital stay (AUC 0.82–0.98). Hybrid CNN-RNN architectures outperformed traditional machine learning methods in predicting rehabilitation success: the weighted F1 score increased from 65 % to 74 %, and the mean absolute error decreased by 12 %. Random forest models achieved 90 % accuracy in predicting patient discharge. Wearable sensors with AI platforms provide personalized monitoring of motor patterns in real time. 
СONCLUSION. Artificial intelligence technologies in the rehabilitation of trauma and orthopedic patients have moved beyond experimental development and demonstrated real clinical value. The most significant predictors of functional recovery are age, functional status, range of motion, and cognitive status of the patient. Large-scale prospective studies with a high level of methodological rigor are needed for widespread clinical implementation.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/ai-in-physical-rehabilitation-of-traumatological-and-nurlygayanov-gilmutdinova/a1a602ae0e7f5db0b7f13587b3d3be4c/) | DOI: 10.38025/2078-1962-2026-25-3-83-92

---

### Rank 100: Medicine & Treatment Recommendation System using Deep Learning
- **Relevance Score:** 40/100
- **Authors:** Chetana Shashikant, P. Mahajan, Shimpi
- **Year & Journal:** Not specified | *Not specified* (SJR Quartile: Not specified)
- **Study Type & Citations:** theoretical, modeling, or simulation study | Citations: 0
- **Main Takeaway:** The Medicine & Treatment Recommendation System, using deep learning algorithms, effectively recommends personalized treatments based on patient data, medical history, symptoms, and diagnosis, reducing human error and improving patient outcomes.
- **Simple Summary & Project Context:**
  — The growing demand for personalized healthcare solutions has led to the development of intelligent systems that assist in medical decision-making. This project focuses on creating a Medicine Recommendation System that utilizes machine learning techniques to recommend suitable medicines based on user inputs such as symptoms or medical conditions. The system leverages a well-structured medical dataset to train a machine learning The integration of deep learning techniques into the healthcare domain has shown significant potential in improving decision-making processes for medical diagnoses and treatment planning. This paper presents a Medicine & Treatment Recommendation System leveraging deep learning algorithms to provide personalized treatment recommendations based on patient data, medical history, symptoms, and diagnosis. By utilizing advanced neural network architectures, such as convolutional neural networks (CNNs) for image-based diagnosis and recurrent neural networks (RNNs) for sequential data analysis, the system efficiently learns complex patterns from diverse healthcare datasets. These include patient demographics, lab test results, medical records, and clinical notes. The system aims to predict the most effective medicines or treatments tailored to individual patients, reducing human error, enhancing clinical decision support, and improving patient outcomes. By continuously updating and training on new datasets, the system ensures scalability and adaptability in evolving medical scenarios. A case study using a publicly available dataset demonstrates the efficacy of the proposed system, showing its capability to recommend accurate treatment plans for various medical conditions.
- **Reference Link:** [Consensus Link](https://consensus.app/papers/medicine-treatment-recommendation-system-using-deep-shashikant-mahajan/354b43dce4c754d89a4f184369a4febf/) 

---
