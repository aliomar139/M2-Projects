# Agentic AI for Personalized Orthopedic Treatment Recommendation: Literature Review & System Design

## Executive Summary

This document presents a comprehensive review of recent scientific literature and a proposed system design for an **Agentic AI Clinical Decision-Support System for Personalized Orthopedic Treatment Recommendation**.

The primary goal of this system is **not to replace physicians**, but to serve as an intelligent clinical partner. By analyzing historical patient data—including patient metadata, baseline symptoms, diagnostic imaging, treatments given, and long-term recovery outcomes—the AI agent identifies hidden patterns. When a new patient presents, the system finds similar past cases, evaluates potential treatment options (such as physical therapy, intra-articular injections, or surgical interventions), predicts the likelihood of recovery, verifies safety against clinical guidelines, and presents clear, transparent recommendations to the doctor.

---

## Part 1: Literature Review & Analysis of Existing Research

To build a grounded foundation, we analyzed **213 research papers** from recent medical and AI literature (including orthopedic AI studies and cross-domain clinical recommender systems). Below is a detailed breakdown answering the core literature analysis questions in simple, accessible language.

---

### 1. Data Used in Clinical & Orthopedic AI Studies

Existing studies rely on a combination of structured electronic health records (EHR), patient survey responses, and diagnostic measurements:

* **Demographics & Personal Details:** Age, sex, body mass index (BMI), employment physical demands, and social determinants of health (*Ogink et al., 2021; Abdelrahman et al., 2026*).
* **Symptoms & Examination:** Joint pain intensity (Visual Analog Scale / VAS score), duration of pain, limping, range of motion, prior conservative treatments (like physical therapy or steroid injections), and general medical co-conditions (*van der Weegen et al., 2023; Cochrane et al., 2026*).
* **Patient-Reported Outcome Measures (PROMs):** Standardized questionnaire scores that track joint function and quality of life before and after treatment, such as the **Oxford Knee Score (OKS)**, **Oxford Hip Score (OHS)**, **KOOS / HOOS**, **WOMAC**, and **EQ-5D** (*Abdelrahman et al., 2026; Kunze et al., 2021*).
* **Diagnostic Imaging & Morphological Data:** X-ray arthritis grades (such as the **Kellgren-Lawrence [KL] grade**), joint space narrowing measurements, MRI cartilage degradation status, and CT scan joint alignment (*Hinterwimmer et al., 2022; Jamshidi et al., 2021*).
* **Public Datasets & Registries:** Frequently used public research data include the **Osteoarthritis Initiative (OAI)**, national joint registries (e.g., UK NHS PROMs, Danish Hip Arthroscopy Registry), and hospital-wide EHR databases (*Jamshidi et al., 2021; Abdelrahman et al., 2026*).

---

### 2. AI Methodologies & Machine Learning Techniques

The literature uses five main categories of artificial intelligence models:

* **Supervised Machine Learning (Decision Trees):** Models like **XGBoost**, **Random Forest**, and **Support Vector Machines (SVM)** are the most common tools for predicting whether a surgery will succeed, whether complications will occur, or whether a patient needs surgery vs. non-surgical care (*van der Weegen et al., 2023; Ogink et al., 2021; Milella et al., 2022*).
* **Deep Learning & Computer Vision:** Convolutional Neural Networks (CNNs like ResNet) automatically assess X-rays for arthritis severity or fracture types. Survival neural networks (**DeepSurv**) predict how many years a joint replacement will last before needing repair (*Hinterwimmer et al., 2022; Jamshidi et al., 2021*).
* **Recommender Systems & Case-Based Reasoning (CBR):** Algorithms such as **k-Nearest Neighbors (k-NN)** calculate mathematical similarity between a new patient and past patients to recommend options based on what worked best for similar peers (*Milella et al., 2022; Domb et al., 2022*).
* **Reinforcement Learning (RL):** RL algorithms learn dynamic, multi-step treatment plans over time (e.g., adjusting physical therapy exercises weekly based on wearable sensor feedback) (*Dong et al., 2026; de Filippis & Foysal, 2025*).
* **Large Language Models (LLMs) & Agentic AI:** Advanced AI models (e.g., GPT-4, Bio-ClinicalBERT) process intake notes, summarize patient histories, extract structured data from text, and align suggestions with official medical guidelines (*Oettl et al., 2025; Billi & Bini, 2026; Halvorson et al., 2026; Dagher et al., 2024*).

---

### 3. Decision-Making Process in Literature

Existing clinical decision support systems generate recommendations using four main pathways:

* **Peer Cohort Matching:** The AI compares a new patient's profile against historical "patient twins" to see which treatment strategy produced the highest recovery rates (*Milella et al., 2022*).
* **Outcome Threshold Prediction:** The AI evaluates candidate treatments (e.g., physical therapy vs. injections vs. knee replacement) and predicts if the patient will achieve a **Minimal Clinically Important Difference (MCID)**—meaning a noticeable, meaningful improvement in daily life (*Kunze et al., 2021; Jang et al., 2024*).
* **Medical Guideline Safety Checks:** Data-driven recommendations are filtered through **Clinical Practice Guidelines (CPGs)**—such as AAOS guidelines—to filter out unsafe or inappropriate options (*Dagher et al., 2024; Pagano et al., 2023*).
* **Agentic AI Synthesis:** Modern agentic systems orchestrate multiple steps autonomously: reading patient intake responses, searching literature, predicting risks, and drafting clinical summaries for the doctor (*Oettl et al., 2025; Billi & Bini, 2026*).

---

### 4. Evaluation Metrics & How Performance is Measured

Studies evaluate AI performance using both technical statistical metrics and clinical benchmarks:

| Metric Category | Specific Benchmark / Measure | What It Means in Simple English |
| :--- | :--- | :--- |
| **Prediction Accuracy** | **ROC-AUC Score** (typically 0.70 – 0.95) | How well the AI distinguishes between patients who recover and those who do not. |
| **Error Rate** | **Mean Absolute Error (MAE)** | How close the AI's predicted pain/function score is to the patient's actual score. |
| **Clinical Success** | **MCID Achievement Accuracy** | Whether the AI correctly predicts if a patient gets a real, noticeable improvement. |
| **Doctor Concordance** | **Cohen's Kappa (kappa) & Agreement %** | How often the AI's suggestion matches what expert orthopedic surgeons choose. |

---

### 5. Limitations & Barriers in Current Literature

Despite promising research results, current orthopedic AI models face several real-world challenges:

1. **Risk of Bias & Poor Method Reporting:** Systematic reviews show that over **40% of orthopedic prediction models have a high risk of bias** (under PROBAST criteria) and fail to report methods transparently (under TRIPOD guidelines) (*Groot et al., 2021; Ogink et al., 2021*).
2. **Lack of Multi-Center Validation:** Less than 20% of models are tested on datasets from outside hospital systems. When tested on a new clinic's patients, accuracy often drops significantly (*Dwajan et al., 2026; Hinterwimmer et al., 2022*).
3. **Black-Box Opacity & Doctor Trust:** Deep learning models rarely explain *why* they made a recommendation. Without clear feature importance (such as **SHAP values**), doctors hesitate to trust the output (*Dwajan et al., 2026; Domb et al., 2022*).
4. **Hallucinations in General LLMs:** Off-the-shelf language models like ChatGPT can make mistakes or suggest treatments that contradict medical guidelines if they are not constrained by external medical knowledge (*Dagher et al., 2024; Pagano et al., 2023*).

---

## Part 2: Proposed Agentic AI Architecture for Orthopedic Treatment Recommendation

Based on the literature review, we design a **Multi-Agent Collaborative AI Architecture** specifically built for personalized orthopedic treatment recommendation.

---

### 1. Specialized AI Agents & Their Roles

The system uses five specialized AI modules that work together in a sequence:

* **Agent 1: Data Ingestion & Profiling Agent**
  * *Role:* Takes patient records (EHR text, surveys, X-ray reports) and extracts key information into a clean, standardized format.
* **Agent 2: Multi-Metric Case Retrieval Agent**
  * *Role:* Searches the historical hospital database to find the top 10–20 past patients ("patient twins") who most closely match the new patient using weighted vector distance.
* **Agent 3: Causal Outcome Prediction Agent**
  * *Role:* Evaluates each candidate treatment (e.g., Physical Therapy, Corticosteroid Injection, Joint Surgery) and calculates the mathematical probability that the patient will achieve significant recovery (MCID).
* **Agent 4: Guideline & Safety Guardrail Agent**
  * *Role:* Checks all treatment options against official medical guidelines (e.g., AAOS Clinical Practice Guidelines) to block any unsafe or contraindicated choices.
* **Agent 5: Explanation & Clinical Synthesis Agent**
  * *Role:* Uses a specialized language model to combine all predictions, retrieve similar past case stories, generate visual SHAP charts showing key drivers, and write a simple summary for the doctor.

---

### 2. Patient Dataset Structure (JSON Schema)

To train and run this agentic system, historical patient records must be stored in a structured JSON schema:

```json
{
  "patient_id": "ORTHO_10294",
  "demographics": {
    "age": 62,
    "gender": "Female",
    "bmi": 28.5,
    "activity_level": "Moderate"
  },
  "clinical_baseline": {
    "affected_joint": "Knee",
    "pain_score_vas": 7.0,
    "symptom_duration_months": 14,
    "kl_arthritis_grade": 3,
    "comorbidities": ["Hypertension", "Type_2_Diabetes"]
  },
  "baseline_proms": {
    "oxford_knee_score": 24,
    "eq5d_utility_index": 0.62
  },
  "treatment_given": {
    "category": "Conservative_Non_Surgical",
    "specific_option": "Hyaluronic_Acid_Injection_Plus_PT",
    "duration_weeks": 12
  },
  "treatment_outcomes": {
    "post_treatment_prom_12m": {
      "oxford_knee_score": 38,
      "score_improvement": 14,
      "mcid_achieved": true
    },
    "complications": "None",
    "required_surgery_within_3yr": false
  }
}
```

---

### 3. Similar Patient Retrieval Engine

To find similar past cases, the system uses a **weighted similarity distance equation**:

**Similarity Distance = sqrt( w1*(Age_diff)^2 + w2*(BMI_diff)^2 + w3*(KL_Grade_diff)^2 + w4*(Baseline_PROM_diff)^2 )**

* **Clinical Feature Weights:**
  * Baseline Functional Score (Oxford Score / KOOS): **35% weight** (Most critical predictor)
  * X-ray Arthritis Severity (KL Grade): **25% weight**
  * Body Mass Index (BMI): **20% weight**
  * Age & Comorbidity Level: **20% weight**

By applying these weights, the system ensures that "similarity" reflects true clinical comparability, rather than superficial demographic matches.

---

### 4. Treatment Effectiveness Prediction Strategy

Treatment success is measured using the **Minimal Clinically Important Difference (MCID)** threshold:

**Treatment Success = Successful (1) if (Post_Treatment_PROM - Baseline_PROM) >= MCID_Threshold, else Unsuccessful (0)**

For example, on the Oxford Knee Score (scale 0–48), an improvement of **>= 5 points** represents an MCID improvement. The prediction agent outputs the estimated percentage chance of hitting this goal for each potential treatment option.

---

### 5. Extension to Other Medical Domains

This agentic decision-support framework is modular and can be adapted to other clinical specialties by swapping domain-specific data and safety rules:

* **Hypertension & Cardiology:** Replaces joint scores with blood pressure logs and kidney function metrics; predicts optimal anti-hypertensive medication combinations (*Hu et al., 2023*).
* **Psychiatry & Depression:** Replaces joint X-rays with PHQ-9 depression scores and genetic markers; recommends optimal antidepressant selections (*de Filippis & Foysal, 2025*).
* **Oncology (Cancer Care):** Replaces orthopedic PROMs with tumor staging and genetic profiles; predicts chemotherapy response and metastasis risk (*Jiang et al., 2019*).
* **Chronic Disease Management:** Uses reinforcement learning to guide long-term treatment pathways for complex multi-organ conditions (*Upadhyay et al., 2026; Verboven et al., 2021*).

---

## Complete References (Selected Research Literature)

1. **Abdelrahman, I., Selim, A., Davies, S., Roberts, A., Thomas, G., & Cool, P.** (2026). SRS108 - Predicting patient-reported outcome measures and evaluating the impact of pre-operative comorbidities on outcomes of hip and knee arthroplasty using supervised machine learning. *British Journal of Surgery*.
2. **Billi, F., & Bini, S.** (2026). The Application of Agentic Artificial Intelligence in Orthopaedics. *The Journal of Bone and Joint Surgery. American Volume*.
3. **Cochrane, J. A., Roberts, O., Ribbons, K., Clark, R., Yong, H. P., Tan, T., ... & Nilsson, M.** (2026). Implementation of clinical decision support tools for treatment selection in knee osteoarthritis: a scoping review. *Therapeutic Advances in Musculoskeletal Disease*.
4. **Dagher, T., Dwyer, E., Baker, H. P., Kalidoss, S., & Strelzow, J. A.** (2024). “Dr. AI Will See You Now”: How Do ChatGPT-4 Treatment Recommendations Align With Orthopaedic Clinical Practice Guidelines? *Clinical Orthopaedics and Related Research*.
5. **de Filippis, R., & Foysal, A. A.** (2025). Personalized Antidepressant Treatment Recommendation Using Reinforcement Learning and Predictive Modelling on Synthetic Patient Data. *OALib*.
6. **Domb, B., Ouyang, V. W., Go, C. C., Gornbein, J., Shapira, J., Meghpara, M. B., ... & Rosinsky, P.** (2022). Personalized Medicine Using Predictive Analytics: A Machine Learning-Based Prognostic Model for Patients Undergoing Hip Arthroscopy. *The American Journal of Sports Medicine*.
7. **Dong, J. H., Chen, T., & Peng, Z.** (2026). Closed-Loop digital therapeutics empowered by deep reinforcement learning and wearable sensing for precision orthopedic rehabilitation: a simulation-based proof-of-concept study. *Frontiers in Rehabilitation Sciences*.
8. **Dwajan, A., Patro, M. R., Agarwal, A., & Lalhmingmawii, M.** (2026). Artificial intelligence in orthopaedics: Clinical decision support, medical imaging, surgical planning, and outcome prediction. *World Journal of Clinical Cases*.
9. **Groot, O., Ogink, P., Lans, A., Twining, P. K., Kapoor, N. D., DiGiovanni, W. H., ... & Schwab, J.** (2021). Machine learning prediction models in orthopedic surgery: A systematic review in transparent reporting. *Journal of Orthopaedic Research*.
10. **Halvorson, R. T., Keeley, T., Niknam, K., Zack, T., Majumdar, S., Feeley, B. T., ... & Lansdown, D. A.** (2026). Large Language Model Predicts Surgeon Recommendations for Imaging and Surgery for Patients Presenting for Knee and Shoulder Complaints With 70% and 81% Accuracy Using Previsit Questionnaire Responses. *Arthroscopy*.
11. **Hinterwimmer, F., Lazic, I., Suren, C., Hirschmann, M., Pohlig, F., Rueckert, D., ... & von Eisenhart-Rothe, R.** (2022). Machine learning in knee arthroplasty: specific data are key—a systematic review. *Knee Surgery, Sports Traumatology, Arthroscopy*.
12. **Hu, Y., Huerta, J., Cordella, N., Mishuris, R. G., & Paschalidis, I.** (2023). Personalized hypertension treatment recommendations by a data-driven model. *BMC Medical Informatics and Decision Making*.
13. **Jamshidi, A., Pelletier, J., Labbe, A., Abram, F., Martel-Pelletier, J., & Droit, A.** (2021). Machine Learning–Based Individualized Survival Prediction Model for Total Knee Replacement in Osteoarthritis: Data From the Osteoarthritis Initiative. *Arthritis Care & Research*.
14. **Jang, S., Rosenstadt, J., Lee, E., & Kunze, K. N.** (2024). Artificial Intelligence for Clinically Meaningful Outcome Prediction in Orthopedic Research: Current Applications and Limitations. *Current Reviews in Musculoskeletal Medicine*.
15. **Jiang, X., Wells, A., Brufsky, A., & Neapolitan, R. E.** (2019). A clinical decision support system learned from data to personalize treatment recommendations towards preventing breast cancer metastasis. *PLoS ONE*.
16. **Kunze, K., Krivicich, L. M., Clapp, I., Bodendorfer, B., Nwachukwu, B. U., Chahla, J., & Nho, S.** (2021). Machine Learning Algorithms Predict Achievement of Clinically Significant Outcomes Following Orthopaedic Surgery: A Systematic Review. *Arthroscopy*.
17. **Milella, F., Famiglini, L., Banfi, G., & Cabitza, F.** (2022). Application of Machine Learning to Improve Appropriateness of Treatment in an Orthopaedic Setting of Personalized Medicine. *Journal of Personalized Medicine*.
18. **Oettl, F., Pruneski, J. A., Zsidai, B., Yu, Y., Cong, T., Feldt, R., ... & Samuelsson, K.** (2025). Artificial intelligence agents in orthopaedics: Concepts, capabilities and the road ahead. *Knee Surgery, Sports Traumatology, Arthroscopy*.
19. **Ogink, P., Groot, O., Karhade, A., Bongers, M., Oner, F. C., Verlaan, J., & Schwab, J.** (2021). Wide range of applications for machine-learning prediction models in orthopedic surgical outcome: a systematic review. *Acta Orthopaedica*.
20. **Pagano, S., Holzapfel, S., Kappenschneider, T., Meyer, M., Maderbacher, G., Grifka, J., & Holzapfel, D.** (2023). Arthrosis diagnosis and treatment recommendations in clinical practice: an exploratory investigation with the generative AI model GPT-4. *Journal of Orthopaedics and Traumatology*.
21. **Upadhyay, D., Venu, N., Asudani, D. S., Vadhera, A., Semwal, P., & Sharma, K.** (2026). Simulating Personalized Treatment Pathways in Chronic Disease Management Using Reinforcement Learning and Synthetic Patient Data. *IEEE ICCIDS*.
22. **van der Weegen, W., Warren, T., Das, D., Agricola, R., Timmers, T., & Siebelt, M.** (2023). Operative or Non-Operative Treatment is Predicted Accurately for Patients Who Have Hip Complaints Consulting an Orthopaedic Surgeon using Machine Learning Algorithms Trained with Pre-Hospital Acquired History-Taking Data. *The Journal of Arthroplasty*.
23. **Verboven, L., Calders, T., Callens, S., Black, J., Maartens, G., Dooley, K., ... & Van Rie, A.** (2021). A treatment recommender clinical decision support system for personalized medicine: method development and proof-of-concept for drug resistant tuberculosis. *BMC Medical Informatics and Decision Making*.
