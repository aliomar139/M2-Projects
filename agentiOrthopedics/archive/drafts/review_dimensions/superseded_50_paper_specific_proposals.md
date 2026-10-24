# Superseded analysis: 50 paper-specific proposals

Archived 24 October 2026 after the requirement changed to five shared dimensions across all ten reviews. Use the current LR/Surveys/review_dimensions report.

# Ten review papers: covered dimensions and proposed additions

Prepared: 24 October 2026. Topic: AI-supported personalized orthopedic treatment decisions, outcome prediction, and agentic clinical decision support.

## How to interpret this analysis

- **Covered dimension:** a subject the review discusses, including limitations and future directions. Discussion does not mean the authors implemented or clinically validated it.
- **Proposed addition:** a defined dimension for which **no explicit discussion was found in the checked full article**, including its tables and figure captions. These are my proposals, not findings or recommendations attributed to the authors.
- **Novelty is relative to that paper.** None of these labels establishes novelty across the research field. Several proposals intentionally recur across reviews; there are 50 paper-specific entries, not 50 unique inventions.
- “Dimensions” means research/system capabilities or evaluation axes, not only patient-level input variables.
- I checked related concepts as well as keywords. A missing keyword alone is insufficient evidence of absence. Each proposal therefore identifies the nearest existing discussion and explains the distinction.
- Absence is an evidence-based reading judgment, not a mathematical guarantee. The boundary is the accessible main article and its embedded tables/captions; separately hosted supplementary files and the full texts of all cited studies were not exhaustively audited.

All ten selections are review articles. Narrative reviews are identified separately from systematic and scoping reviews. Eight are already in your 100-paper collection; two additional open-access reviews broaden the comparison. Original model-development papers are excluded.

## Selected papers

| ID | Review | Year | Review type | Relation to your project |
|---|---|---|---|---|
| R1 | Cochrane et al., Implementation of clinical decision support tools for treatment selection in knee osteoarthritis | 2026 | Scoping | Most direct match: personalized treatment decisions |
| R2 | Longo et al., Artificial intelligence in total and unicompartmental knee arthroplasty | 2024 | Systematic | Treatment-specific prediction and perioperative support |
| R3 | Russell et al., Artificial intelligence fails to outperform orthopaedic surgeons | 2025 | Systematic | Clinician comparison and recommendation reliability |
| R4 | Glinkowski et al., Artificial Intelligence in Orthopaedics: Clinical Performance, Limitations, and Translational Readiness | 2026 | Structured narrative | Clinical readiness across the care pathway |
| R5 | Kim et al., Artificial intelligence in orthopedics: current applications, challenges, and future directions | 2026 | Narrative | Data, models, implementation, and governance |
| R6 | Oettl et al., Artificial Intelligence and Musculoskeletal Surgical Applications | 2025 | Narrative | Surgical workflow, LLMs, and agentic systems |
| R7 | Giorgino et al., ChatGPT in orthopedics: a narrative review exploring the potential of artificial intelligence in orthopedic practice | 2023 | Narrative | Language-model decision support and limitations |
| R8 | Oettl et al., Is orthopaedics entering the age of generative AI? | 2025 online; 2026 issue | Narrative | Generative and agentic workflow architecture |
| R9 | Han et al., Artificial Intelligence in Orthopedic Surgery: Current Applications, Challenges, and Future Directions | 2025 | Broad narrative review | Algorithms, hardware, and clinical integration |
| R10 | Farhadi et al., Applications of artificial intelligence in orthopaedic surgery | 2022 | Narrative | Clinical use cases across five subspecialties |

R9 describes its synthesis as systematic in general wording, but is treated here as a broad narrative review rather than a protocol-driven systematic review.

R2 is categorized as “Research” on the publisher website and in the XML wrapper, but its actual study design is explicitly a systematic literature review, with a search, eligibility criteria, PRISMA flow, and quality appraisal. It is included on that substantive basis.

## R1. Cochrane et al. (2026)

**Paper:** [Implementation of clinical decision support tools for treatment selection in knee osteoarthritis: a scoping review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12816537/). *Therapeutic Advances in Musculoskeletal Disease*, 18. DOI: [10.1177/1759720X251407070](https://doi.org/10.1177/1759720X251407070). Existing corpus rank: 35.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Decision-aid delivery format | Results: Decision aid features; Table 1 |
| 2 | Intended patient/clinician users | Results: Decision aid features |
| 3 | Surgical and nonsurgical treatment alternatives | Results and Discussion: Treatment options |
| 4 | Predicted pain outcomes | Results: Outcome measures; Table 3 |
| 5 | Physical function/activity outcomes | Results: Outcome measures; Table 3 |
| 6 | Quality of life/global health | Discussion: Prediction methods |
| 7 | Psychosocial outcomes, including their absence | Discussion: Prediction methods |
| 8 | Financial consequences of treatment | Discussion: Prediction methods |
| 9 | Demographic, clinical, and PROM inputs | Results: Predictive modelling; Table 3 |
| 10 | Model transparency, validation, and implementation reporting | Discussion: Transparency of reporting |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal comparative benefit:** estimate outcomes under surgery and nonsurgical care after adjustment for treatment-selection confounding. | Personalized prediction and matching are covered; identifying counterfactual treatment benefit is not explicitly examined. |
| N2 | **Guideline-grounded retrieval with claim citations:** retrieve guideline passages and link each treatment statement to its supporting passage. | Guidelines and possible chatbots appear, but a retrieval-and-citation mechanism is not discussed. |
| N3 | **Recommendation abstention:** withhold treatment ranking when a prespecified reliability threshold is not met. | Reporting and validation are covered; a formal no-recommendation action is not specified. |
| N4 | **Sequential treatment-policy evaluation:** compare adaptive sequences such as rehabilitation, reassessment, and escalation using offline policy evaluation. | Multiple treatment choices and Markov models appear; learning and evaluating adaptive decision policies is not discussed. |
| N5 | **Informative follow-up loss:** examine whether missing follow-up outcomes depend on recovery, and assess resulting bias. | Generic missing-value processing is mentioned; outcome-dependent dropout analysis is not. |

**Do not claim as new here:** nonsurgical alternatives, psychosocial outcomes, costs, reduced questionnaire burden, or broad “value of information.” These already appear, sometimes as gaps in the reviewed tools. Table 2 uses “value of information” as a decision-aid evaluation measure.

## R2. Longo et al. (2024)

**Paper:** [Artificial intelligence in total and unicompartmental knee arthroplasty](https://link.springer.com/article/10.1186/s12891-024-07516-9). *BMC Musculoskeletal Disorders*, 25:571. DOI: [10.1186/s12891-024-07516-9](https://doi.org/10.1186/s12891-024-07516-9). Existing corpus rank: 38.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Patient-reported pain/function improvement | Results: AI and ML methods; Table 2 |
| 2 | Postoperative complication prediction | Results: AI and ML methods; Discussion |
| 3 | Revision risk | Results: AI and ML methods |
| 4 | Patient satisfaction | Introduction; Discussion |
| 5 | Hospital length of stay | Introduction; Discussion |
| 6 | Treatment/hospital cost prediction | Discussion |
| 7 | Discharge destination | Discussion |
| 8 | Blood-transfusion risk | Discussion |
| 9 | OA progression and future arthroplasty | Discussion |
| 10 | Algorithm comparison and methodological quality | AI and ML methods; modified MINORS assessment |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal surgery-versus-conservative comparison:** estimate incremental treatment benefit, rather than only postoperative risk. | Predicting arthroplasty outcomes or future surgery does not identify the benefit of operating. |
| N2 | **Preference-weighted treatment utility:** let patients explicitly weight pain relief, recovery burden, and complication avoidance in ranking options. | Satisfaction and financial considerations are covered; patient-defined mathematical ranking weights are not. |
| N3 | **Statistically supported treatment sets:** return several plausibly best options when treatment differences are too uncertain for one winner. | Predictive performance is reviewed; uncertainty-controlled sets of competing treatments are not. |
| N4 | **Guideline-grounded retrieval:** support each candidate treatment with retrieved, traceable guideline evidence. | Clinical prediction and text extraction appear; retrieval-based guideline justification does not. |
| N5 | **Decision-based next-test selection:** choose the next measurement by its expected improvement in the treatment decision relative to its burden. | Feature selection and efficient prediction are covered; adaptive information acquisition for a pending decision is not. |

**Do not claim as new here:** monitoring, costs, patient satisfaction, minimal inputs, NLP, or validation.

## R3. Russell, Rosen, and Vella-Baldacchino (2025)

**Paper:** [Artificial intelligence fails to outperform orthopaedic surgeons: A systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12616488/). *Journal of Experimental Orthopaedics*, 12:e70548. DOI: [10.1002/jeo2.70548](https://doi.org/10.1002/jeo2.70548). Existing corpus rank: 7.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Patient identification and outcome-based selection | Results: Patient identification |
| 2 | Choice of surgical approach | Results: Surgical approach |
| 3 | Radiographic OA grading | Results: Radiograph reading |
| 4 | Management-plan guideline concordance | Results: Management plans |
| 5 | Examination/clinical knowledge performance | Results: Clinical knowledge |
| 6 | Quality of patient information | Results: Quality control |
| 7 | FAQ accuracy, completeness, and empathy | Results: Answering patient FAQs |
| 8 | Overconfidence and incorrect outputs | Discussion |
| 9 | Demographic/data bias | Discussion |
| 10 | Human-plus-AI evaluation and study heterogeneity | Discussion; Limitations |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal treatment benefit:** evaluate whether the suggested option improves patient outcomes relative to an alternative. | Agreement with surgeons and outcome classification are evaluated; counterfactual treatment-effect estimation is not. |
| N2 | **Patient-specific utility ranking:** score alternatives using each patient's explicit priorities. | Communication quality is covered; preference-weighted treatment optimization is not. |
| N3 | **Adaptive next-question/test selection:** request information according to its expected decision value. | Task accuracy is compared; adaptive acquisition of missing decision-relevant information is not discussed. |
| N4 | **Economic value of the decision-support service:** evaluate deployment costs against downstream health benefits and resource changes. | Efficiency is discussed; a cost-effectiveness evaluation framework is not explicitly developed or reviewed. |
| N5 | **Informative outcome missingness:** assess whether selective follow-up changes estimated treatment benefits. | Incomplete EHRs and demographic bias are discussed; outcome-dependent follow-up loss is not. |

**Do not claim as new here:** human-plus-AI comparisons, overconfidence, hallucinations, bias, updating guidance, or clinician involvement.

## R4. Glinkowski et al. (2026)

**Paper:** [Artificial Intelligence in Orthopaedics: Clinical Performance, Limitations, and Translational Readiness—A Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12985454/). *Journal of Clinical Medicine*, 15(5):1751. DOI: [10.3390/jcm15051751](https://doi.org/10.3390/jcm15051751). Existing corpus rank: 15.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Fracture/OA imaging analysis | Section 3.2 |
| 2 | Implant identification | Section 3.2; Table 2 |
| 3 | Arthroplasty planning/templating | Section 3.3 |
| 4 | Intraoperative augmentation/navigation | Section 3.3; Table 3 |
| 5 | Risk and PROM-based prediction | Section 3.4 |
| 6 | Rehabilitation intelligence | Section 3.5 |
| 7 | Teleorthopaedic care | Section 3.5; Table 5 |
| 8 | Explainability, fairness, and governance | Sections 3.6, 4.3, and 4.4 |
| 9 | Economic and implementation costs | Section 4.5 |
| 10 | External/prospective validation and readiness | Sections 4.1, 4.6, and 4.8 |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal treatment-effect comparison:** estimate benefit differences between competing treatments after confounding adjustment. | Risk stratification and digital twins are covered; causal identification of treatment differences is not. |
| N2 | **Patient-defined utility weights:** encode individual trade-offs between improvement, recovery time, and harm. | Patient-centered care is covered; explicit patient-weighted treatment objectives are not. |
| N3 | **Decision-based information acquisition:** select the next assessment by its expected impact on treatment choice. | Workflow speed and model efficiency are covered; decision-theoretic next-test selection is not. |
| N4 | **Outcome-dependent dropout analysis:** test the sensitivity of recovery predictions to informative follow-up loss. | Evidence limitations are discussed; this missing-outcome mechanism is not explicitly examined. |
| N5 | **Treatment-support/overlap diagnostics:** refuse comparisons when similar patients did not receive both candidate treatments. | External validity is covered; empirical support for a particular counterfactual comparison is not. |

**Do not claim as new here:** economics, digital twins, federated learning, SHAP/LIME, fairness, uncertainty, telehealth, or post-market monitoring.

## R5. Kim et al. (2026)

**Paper:** [Artificial intelligence in orthopedics: current applications, challenges, and future directions](https://link.springer.com/article/10.1186/s43019-026-00317-5). *Knee Surgery & Related Research*, 38:14. DOI: [10.1186/s43019-026-00317-5](https://doi.org/10.1186/s43019-026-00317-5). Existing corpus rank: 32.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | EHR, registry, and claims data | Clinical and imaging data sources |
| 2 | Imaging classification and measurement | Medical image analysis |
| 3 | LLM extraction/documentation | Large language models |
| 4 | Multimodal/digital-twin representations | Practical considerations and future directions |
| 5 | External and prospective evaluation | Study design and validation principles |
| 6 | Calibration and predictive uncertainty | Algorithmic opacity and explainability |
| 7 | Feature attribution/explainability | Algorithmic opacity and explainability |
| 8 | Prompt-injection/security vulnerabilities | Large language models |
| 9 | EHR/PACS integration and workflow burden | Workflow integration and implementation science |
| 10 | Fairness and lifecycle monitoring/versioning | Legal, regulatory, and ethical governance; Conclusion |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal comparative effectiveness:** distinguish predicted risk from the estimated effect of choosing another treatment. | Prediction and evaluation are covered; counterfactual identification and confounding adjustment are not. |
| N2 | **Preference-weighted treatment optimization:** use elicited patient priorities to change the ranking of options. | Preferences appear as information in clinical text; translating them into treatment-ranking objectives is not discussed. |
| N3 | **Value-based next-test selection:** acquire additional patient information only when expected decision benefit warrants it. | Workflow burden is covered; adaptive test selection by decision value is not. |
| N4 | **Hidden-confounding sensitivity:** report how strong an unmeasured factor must be to overturn a recommendation. | Generalization and fairness are covered; sensitivity to unmeasured treatment-selection confounding is not. |
| N5 | **Treatment-ranking stability:** measure whether small plausible input changes reverse the preferred treatment. | Calibration and feature ranking are covered; robustness of competing treatment rankings is not. |

**Do not claim as new here:** RAG/retrieval grounding, prompt-injection testing, model drift, auditability, uncertainty, or patient preferences in general.

## R6. Oettl et al. (2025)

**Paper:** [Artificial Intelligence and Musculoskeletal Surgical Applications](https://pmc.ncbi.nlm.nih.gov/articles/PMC12092413/). *HSS Journal*, 21(3):267–273. DOI: [10.1177/15563316251339596](https://doi.org/10.1177/15563316251339596). Existing corpus rank: 2.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Anatomical segmentation/reconstruction | Surgical Planning |
| 2 | Surgical-tool detection/tracking | Technical Foundations |
| 3 | Fracture classification | Technical Foundations |
| 4 | Implant planning and positioning | Surgical Planning; Clinical Examples |
| 5 | Spinal alignment assessment | Surgical Planning |
| 6 | Real-time intraoperative navigation | Intraoperative Navigation |
| 7 | Gait/wearable rehabilitation monitoring | Postoperative Monitoring |
| 8 | Complication detection/prediction | Postoperative Monitoring |
| 9 | LLM documentation and education | Emerging Technologies: LLMs |
| 10 | Agent autonomy, oversight, and safety | Emerging Technologies: Agentic AI |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal operative-versus-conservative benefit:** compare treatment alternatives using explicit confounding assumptions. | Outcome prediction and planning are covered; causal treatment-effect estimation is not. |
| N2 | **Patient-weighted utility:** rank options using explicit patient trade-offs. | Education and personalization are covered; elicited utility weights are not. |
| N3 | **Agent disagreement arbitration:** define how conflicting agent recommendations trigger adjudication or escalation. | Agentic autonomy and oversight are covered; a conflict-resolution mechanism is not discussed. |
| N4 | **Decision-based next-measurement selection:** select the next PROM, examination, or investigation by expected decision benefit. | Multimodal monitoring is covered; adaptive information acquisition is not. |
| N5 | **Informative outcome-loss sensitivity:** assess whether unobserved recovery outcomes systematically differ from observed ones. | Monitoring is covered; analysis of outcome-dependent follow-up loss is not. |

**Do not claim as new here:** agents, wearables, multimodal LLMs, explainability, continuous updates, or human oversight.

## R7. Giorgino et al. (2023)

**Paper:** [ChatGPT in orthopedics: a narrative review exploring the potential of artificial intelligence in orthopedic practice](https://www.frontiersin.org/journals/surgery/articles/10.3389/fsurg.2023.1284015/full). *Frontiers in Surgery*, 10:1284015. DOI: [10.3389/fsurg.2023.1284015](https://doi.org/10.3389/fsurg.2023.1284015). Existing corpus rank: 8.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Differential diagnosis/imaging suggestions | Introduction |
| 2 | Guideline-informed treatment suggestions | Introduction; Discussion 4.1 |
| 3 | Preoperative planning | Discussion 4.1 |
| 4 | Intraoperative support/postoperative rehabilitation | Discussion 4.1 |
| 5 | Patient education and information reliability | Discussion 4.2 |
| 6 | Medical knowledge/examination testing | Discussion 4.3: Challenging ChatGPT |
| 7 | Scientific writing and research integrity | Discussion 4.4 |
| 8 | Hallucinations/contextual reasoning limitations | Discussion 4.5 |
| 9 | Training-data quality and bias | Discussion 4.5 |
| 10 | Privacy, accountability, and human supervision | Discussion 4.5 |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal treatment-effect estimation:** connect language-based support to a model comparing alternative treatment outcomes. | Treatment suggestions are covered; identifying causal benefit is not. |
| N2 | **PROM/MCID-based option scoring:** estimate the probability of meaningful functional improvement separately for each option. | Rehabilitation and treatment advice are covered; quantitative PROM-threshold comparison is not. |
| N3 | **Calibrated abstention:** use measured reliability to decide when the system must withhold a recommendation. | Recognition of limitations and supervision are covered; a calibrated abstention policy is not. |
| N4 | **Adaptive information collection:** choose follow-up questions/tests according to expected improvement in the treatment decision. | Context limitations are covered; decision-based selection of the next information item is not. |
| N5 | **Economic evaluation of clinical use:** compare the cost of operating the system with its downstream clinical benefits. | Workflow efficiency is covered; formal cost-effectiveness analysis is not discussed. |

**Do not claim as new here:** hallucination control, checking source credibility, privacy, bias, patient education, or human oversight. N3 is specifically an operational abstention policy, not a claim that uncertainty was never mentioned.

## R8. Oettl et al. (online 2025; issue 2026)

**Paper:** [Is orthopaedics entering the age of generative AI?—A narrative review of current applications challenges and future directions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12747601/). *Knee Surgery, Sports Traumatology, Arthroscopy*, 34:370–377. DOI: [10.1002/ksa.70145](https://doi.org/10.1002/ksa.70145). Existing corpus rank: 49.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Patient-specific anatomical models | Surgical planning and simulation |
| 2 | Virtual surgical rehearsal | Surgical planning and simulation |
| 3 | Custom implant/prosthetic generation | Custom implant and prosthetic design |
| 4 | Automated clinical documentation | Clinical decision support systems |
| 5 | Agentic scheduling/administrative workflows | Clinical decision support systems |
| 6 | Patient communication and informed consent | Patient communication and informed consent |
| 7 | Multimodal training-data requirements | Technical considerations and implementation |
| 8 | EHR/PACS interoperability | Technical considerations and implementation |
| 9 | Clinical/technical output validation | Technical considerations; Future directions |
| 10 | Hallucinations, bias, regulation, and adoption | Challenges and limitations |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal treatment-benefit ranking:** rank interventions using confounding-aware outcome differences. | Generative planning and simulated anatomy are covered; causal comparison of clinical treatment alternatives is not. |
| N2 | **Claim-level guideline retrieval:** make each clinical claim traceable to an actual retrieved passage. | Evidence-based protocols are mentioned; a retrieval-and-citation verification mechanism is not discussed. |
| N3 | **Multi-agent conflict resolution:** explicitly adjudicate disagreements between retrieval, prediction, and safety agents. | Agentic workflows are covered; disagreement-handling rules are not. |
| N4 | **Patient-weighted multiobjective ranking:** translate individual recovery priorities into formal option rankings. | Shared decisions and lifestyle matching are covered; elicited quantitative utility weights are not. |
| N5 | **Ranking-robustness evaluation:** test treatment recommendations under plausible measurement/input perturbations. | General validation is covered; treatment-rank reversal under small input changes is not. |

**Do not claim as new here:** adaptive rehabilitation, wearables, robotics, informed consent, multicenter trials, or cost-effectiveness.

## R9. Han et al. (2025)

**Paper:** [Artificial Intelligence in Orthopedic Surgery: Current Applications, Challenges, and Future Directions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12188104/). *MedComm*, 6(7):e70260. DOI: [10.1002/mco2.70260](https://doi.org/10.1002/mco2.70260). Additional review, outside the original 100-paper manifest.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | Preoperative image analysis/reconstruction | Section 2.1.1 |
| 2 | Personalized surgical plans and paths | Section 2.1.2; Table 1 |
| 3 | Robotic intraoperative navigation/control | Section 2.2; Table 2 |
| 4 | Complication and readmission prediction | Section 2.3.1; Table 3 |
| 5 | Personalized rehabilitation guidance | Section 2.3.2 |
| 6 | Multimodal data fusion | Sections 3.1 and 5.1.2 |
| 7 | Hardware, sensors, and interoperability | Sections 3.2 and 3.3; Table 5 |
| 8 | Federated learning/data sharing | Section 3.1; Table 4 |
| 9 | Explainability and clinical trust | Section 3.3 |
| 10 | Consent, fairness, and legal responsibility | Section 4 |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal surgery-versus-nonsurgical comparison:** estimate whether operating adds benefit over conservative care. | Surgical optimization is covered; causal comparative effectiveness between these care strategies is not. |
| N2 | **Elicited patient-utility objectives:** set ranking weights from the patient's own priorities. | Multiobjective surgical optimization and autonomy are covered; patient-elicited utility weights are not. |
| N3 | **Decision-based information acquisition:** select additional assessments by expected decision improvement after accounting for burden. | Multimodal data and hardware acquisition are covered; decision-theoretic next-assessment selection is not. |
| N4 | **Guideline retrieval with evidence traceability:** attach verified guideline passages to treatment recommendations. | Multimodal LLMs are covered; guideline retrieval and claim-level evidence linkage are not. |
| N5 | **Counterfactual treatment-support checks:** detect when the records lack comparable patients receiving an alternative treatment. | Multicenter generalizability is covered; treatment positivity/common-support diagnostics are not. |

**Do not claim as new here:** reinforcement learning, multimodal LLMs, Bayesian uncertainty, federated learning, multiobjective optimization in general, or consent. The word “causality” appears in a legal-liability discussion; it is not a review of causal treatment-effect estimation.

## R10. Farhadi et al. (2022)

**Paper:** [Applications of artificial intelligence in orthopaedic surgery](https://www.frontiersin.org/journals/medical-technology/articles/10.3389/fmedt.2022.995526/full). *Frontiers in Medical Technology*, 4:995526. DOI: [10.3389/fmedt.2022.995526](https://doi.org/10.3389/fmedt.2022.995526). Additional review, outside the original 100-paper manifest.

### Ten covered dimensions

| # | Dimension discussed | Article locator |
|---|---|---|
| 1 | OA detection/staging | Joint reconstruction: Automated image-based diagnosis |
| 2 | Implant loosening/identification | Joint reconstruction: Automated implant evaluation |
| 3 | PROM/meaningful improvement prediction | Joint reconstruction: Clinical outcome prediction |
| 4 | Patient-specific presurgical workflows | Joint reconstruction: Improving surgeon workflow |
| 5 | Implant geometry/design optimization | Joint reconstruction: Implant research and development |
| 6 | Spine localization and diagnosis | Spine |
| 7 | Spine postoperative complication prediction | Spine: Postoperative complication prediction |
| 8 | Tumor diagnosis, survival, and segmentation | Orthopaedic oncology |
| 9 | Fracture detection and outcome prediction | Trauma |
| 10 | ACL/meniscal injury detection | Sports medicine |

### Five proposed additions: no explicit discussion found

| # | Proposed dimension and intended feature | Why it is separate from what the review already discusses |
|---|---|---|
| N1 | **Causal treatment-benefit estimation:** adjust treatment comparisons for confounding rather than rank options using prognosis alone. | Treatment alternatives and prognostic support are covered; identifying counterfactual treatment effects is not. |
| N2 | **Guideline-grounded language generation:** retrieve evidence and generate treatment explanations with claim-level citations. | Clinical decision-support interfaces are covered; this retrieval/generation architecture is not. |
| N3 | **Adaptive sequential treatment policies:** learn when to continue, change, or escalate care as patient status evolves. | Prediction and decision aids are covered; reinforcement-learning treatment sequencing is not. |
| N4 | **Patient-elicited utility ranking:** optimize recommendations using individual goals and risk trade-offs. | Patient-specific information is covered; explicit preference-weighted ranking is not. |
| N5 | **Calibrated recommendation abstention:** withhold a recommendation when a tested confidence rule indicates insufficient reliability. | Interpretability, validation, and monitoring are covered; a selective recommendation/refusal policy is not. |

**Do not claim as new here:** PROMs, MCID, costs, external validation, alternative treatment presentation, monitoring, or explainability.

## How to use these additions in your thesis

The additions are comparison dimensions for a literature matrix, not a claim that every absent dimension belongs in every system. Scope explains many absences: a surgical-imaging review need not discuss causal treatment selection.

For your intended system, the recurring candidate dimensions can be consolidated into:

1. Causal benefit across alternative treatments.
2. Explicit patient-preference objectives.
3. Evidence-grounded explanations.
4. Abstention and empirical support for recommendations.
5. Adaptive collection of decision-relevant information.
6. Sequential treatment decisions.
7. Robustness to missing follow-up, hidden confounding, and input perturbations.
8. Conflict resolution between agents.

This is my synthesis of the comparison, not evidence that these are unstudied across orthopedics. Before calling one a thesis contribution, search the wider field and define a feasible dataset, treatment contrast, outcome, and evaluation.

## Verification record and source limitations

- Full-text sources and the keyword/context audit are in `sources/` and `verification_audit.md` beside this report.
- Complete publisher/PMC article text was used. Existing repository summaries were orientation aids, not sufficient evidence for absence.
- The repository files at corpus ranks 3, 26, 34, and 47 examined during screening contain rendered abstract/metadata material with added repository sections. They were not used as full-text evidence for this report. This finding concerns those inspected files only.
- R6's local PDF is also a repository rendering, but contains the article body. Its substantive sections were cross-checked against the complete PMC article. Its repository-added “takeaway” and provenance sections are excluded from evidence.
- R8 has an online/issue-year distinction. Both years are shown rather than silently copying the manifest's year.
- A proposal is rejected as absent if the review already discusses the same concept, including as a limitation or future direction. More specific extensions are stated narrowly and distinguished from their already-covered parent topic.
- Separately hosted supplements and every cited primary paper remain outside the absence claim. New publication versions could also change this assessment.
