# Dimensions reported in the working survey library

Updated 23 October 2026. A dimension is a study characteristic, comparison axis, model/evaluation property or implementation theme that a review charts or discusses. Review methodology is recorded separately from clinical/model dimensions. This inventory covers every paper in the working library, including explicitly marked cross-domain context.

**Evidence levels:** `confirmed_charted_or_compared` = checked in the named original table or method section; `candidate_table_field` and `candidate_section_theme` = machine-mapped structure requiring adjudication; `discussion_mention_only` = a text mention, not proof of systematic extraction; `abstract_mention_only` = abstract evidence only; `not_located_in_available_text` = no match found, not demonstrated absence; `unknown_fulltext_unavailable` = original text unavailable. These labels must not be collapsed into present/absent prevalence estimates.

Eleven close comparators have focused assistant checks. None has independent second-reviewer confirmation. Supplementary extraction forms and image-only tables can contain dimensions not recovered from the available XML/PDF text; no semantically exhaustive “all dimensions” claim is made.

## Dimension codebook

| Code | Dimension |
|---|---|
| D01 | Clinical condition and anatomical scope |
| D02 | Decision task and care stage |
| D03 | Treatment options and comparators |
| D04 | Study design and evidence level |
| D05 | Population and sample size |
| D06 | Data source, setting and geography |
| D07 | Input features and modalities |
| D08 | Outcomes and PROM instruments |
| D09 | Follow-up and assessment horizon |
| D10 | Model family and LLM backbone |
| D11 | Agent architecture, roles and coordination |
| D12 | Retrieval, tools and evidence sources |
| D13 | Historical-choice versus comparative-benefit target |
| D14 | Causal identification and target trial design |
| D15 | Confounder selection and adjustment |
| D16 | Treatment overlap and positivity |
| D17 | Missingness, attrition and selection |
| D18 | Time zero and information leakage |
| D19 | Frozen model versus redevelopment |
| D20 | External and geographic validation |
| D21 | Temporal validation and drift |
| D22 | Calibration and proper scoring |
| D23 | Uncertainty, abstention and unsupported inputs |
| D24 | Decision utility and policy value |
| D25 | Explanation and interpretability |
| D26 | Subgroup fairness and equity |
| D27 | Patient preferences and shared decisions |
| D28 | Workflow, end users and usability |
| D29 | Prospective impact and patient benefit |
| D30 | Costs, latency and resource burden |
| D31 | Reproducibility and availability |
| D32 | Safety, privacy and accountability |
| D33 | Risk of bias and reporting quality |
| D34 | Review search, selection and synthesis |
| D35 | Patient-state representation and history |
| D36 | Action space, dose and scheduling |
| D37 | Rewards and multiple clinical/nonclinical objectives |
| D38 | Recommendation paradigm and information basis |
| D39 | Reference standard and comparator validity |
| D40 | Performance measures and comparison criteria |
| D41 | Unit of analysis and dependent evidence |

## Paper-by-paper inventory

<a id="legacy_019"></a>
### LEGACY_019: Artificial intelligence in orthopaedics: Clinical decision support, medical imaging, surgical planning, and outcome prediction

[Citation record](records/LEGACY_019.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: metadata_only. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_026"></a>
### LEGACY_026: AI in Orthopedic Research: A Comprehensive Review.

[Citation record](records/LEGACY_026.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Treatment options and comparators; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Workflow, end users and usability; Reproducibility and availability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_034"></a>
### LEGACY_034: Machine learning for predicting outcomes, complications and resource utilisation after hip arthroscopy: A systematic review.

[Citation record](records/LEGACY_034.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: systematic_review.

Abstract signals only: Decision task and care stage; Study design and evidence level; Outcomes and PROM instruments; Model family and LLM backbone; Retrieval, tools and evidence sources; Costs, latency and resource burden; Risk of bias and reporting quality.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_044"></a>
### LEGACY_044: Machine-learning-based patient-specific prediction models for knee osteoarthritis.

[Citation record](records/LEGACY_044.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Model family and LLM backbone; Subgroup fairness and equity.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_046"></a>
### LEGACY_046: Machine Learning for the Orthopaedic Surgeon

[Citation record](records/LEGACY_046.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: metadata_only. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_052"></a>
### LEGACY_052: Revolutionizing orthopedic care: The impact of ai in predictive analysis, surgical precision, and personalized rehabilitation

[Citation record](records/LEGACY_052.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: metadata_only. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="legacy_064"></a>
### LEGACY_064: AI-augmented personalized treatment in healthcare a comprehensive survey of models benchmarking and deployment challenges

[Citation record](records/LEGACY_064.md) | [PDF](sources/LEGACY_064.pdf)

Stream: cross_domain_methodological_context. Source basis: fulltext_pdf_text. Publication category: narrative_or_other_review_pending_full_method_check.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Data source, setting and geography; Input features and modalities; Model family and LLM backbone; External and geographic validation; Explanation and interpretability; Costs, latency and resource burden; Reproducibility and availability; Safety, privacy and accountability; Review search, selection and synthesis; Recommendation paradigm and information basis; Performance measures and comparison criteria.

Evidence locator: PDF pp. 6-9; Tables 4-10; benchmarking and provenance sections.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="legacy_068"></a>
### LEGACY_068: A survey on deep reinforcement learning for personalized treatment featuring challenges and a theoretical framework

[Citation record](records/LEGACY_068.md) | [PDF](sources/LEGACY_068.pdf)

Stream: cross_domain_methodological_context. Source basis: fulltext_pdf_text. Publication category: narrative_or_other_review_pending_full_method_check.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Treatment options and comparators; Data source, setting and geography; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Decision utility and policy value; Patient preferences and shared decisions; Safety, privacy and accountability; Review search, selection and synthesis; Patient-state representation and history; Action space, dose and scheduling; Rewards and multiple clinical/nonclinical objectives.

Evidence locator: PDF pp. 6-7, 21-22, 25-26; Tables 3-5; state/action/reward and multi-objective sections.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="legacy_069"></a>
### LEGACY_069: Causal machine learning for predicting treatment outcomes

[Citation record](records/LEGACY_069.md) | [PDF](sources/LEGACY_069.pdf)

Stream: cross_domain_methodological_context. Source basis: fulltext_pdf_text. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="legacy_099"></a>
### LEGACY_099: AI in physical rehabilitation of traumatological and orthopedic patients: existing technologies and their clinical effectiveness. A review

[Citation record](records/LEGACY_099.md) | [PDF](sources/LEGACY_099.pdf)

Stream: orthopedic_review_working_selection. Source basis: fulltext_pdf_text. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_21750352"></a>
### PMID_21750352: Computer-based medical decision support system in diagnosis and treatment of musculoskeletal disorders and injuries.

[Citation record](records/PMID_21750352.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Model family and LLM backbone; Costs, latency and resource burden.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_26667939"></a>
### PMID_26667939: Clinical Decision Support Tools for Selecting Interventions for Patients with Disabling Musculoskeletal Disorders: A Scoping Review.

[Citation record](records/PMID_26667939.md) | [readable original text](sources/PMID_26667939.html) | [XML](sources/PMID_26667939.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Additional structure-mapped candidates requiring confirmation: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Population and sample size; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Reproducibility and availability; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_31994752"></a>
### PMID_31994752: Advanced decision-making using patient-reported outcome measures in total joint replacement.

[Citation record](records/PMID_31994752.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Outcomes and PROM instruments; Retrieval, tools and evidence sources; Patient preferences and shared decisions; Reproducibility and availability.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_32379124"></a>
### PMID_32379124: Artificial Intelligence and Orthopaedics: An Introduction for Clinicians.

[Citation record](records/PMID_32379124.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: conceptual_or_methods_guide.

Abstract signals only: Decision task and care stage; Model family and LLM backbone; Retrieval, tools and evidence sources; Safety, privacy and accountability.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_32797983"></a>
### PMID_32797983: Use of Machine Learning and Artificial Intelligence to Drive Personalized Medicine Approaches for Spine Care.

[Citation record](records/PMID_32797983.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Treatment options and comparators; Data source, setting and geography; Model family and LLM backbone.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_33198106"></a>
### PMID_33198106: Compilation and Analysis of Web-Based Orthopedic Personalized Predictive Tools: A Scoping Review.

[Citation record](records/PMID_33198106.md) | [readable original text](sources/PMID_33198106.html) | [XML](sources/PMID_33198106.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Input features and modalities; Outcomes and PROM instruments; Historical-choice versus comparative-benefit target.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_33288388"></a>
### PMID_33288388: Clinical Decision Support Tools for Predicting Outcomes in Patients Undergoing Total Knee Arthroplasty: A Systematic Review.

[Citation record](records/PMID_33288388.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: systematic_review.

Abstract signals only: Decision task and care stage; Population and sample size; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_33323681"></a>
### PMID_33323681: Artificial Intelligence for the Orthopaedic Surgeon: An Overview of Potential Benefits, Limitations, and Clinical Applications.

[Citation record](records/PMID_33323681.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Model family and LLM backbone; Historical-choice versus comparative-benefit target.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_33933587"></a>
### PMID_33933587: Multivariable models in orthopaedic research: a methodological review of covariate selection and causal relationships.

[Citation record](records/PMID_33933587.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Input features and modalities; Model family and LLM backbone; Causal identification and target trial design; Confounder selection and adjustment.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_34305383"></a>
### PMID_34305383: Decision Support Systems in Temporomandibular Joint Osteoarthritis: A review of Data Science and Artificial Intelligence Applications.

[Citation record](records/PMID_34305383.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Input features and modalities; Model family and LLM backbone; Retrieval, tools and evidence sources.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_34522738"></a>
### PMID_34522738: Artificial Learning and Machine Learning Decision Guidance Applications in Total Hip and Knee Arthroplasty: A Systematic Review.

[Citation record](records/PMID_34522738.md) | [readable original text](sources/PMID_34522738.html) | [XML](sources/PMID_34522738.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: systematic_review.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_35238790"></a>
### PMID_35238790: State of the Art of Machine Learning–Enabled Clinical Decision Support in Intensive Care Units: Literature Review

[Citation record](records/PMID_35238790.md) | [PDF](sources/PMID_35238790.pdf) | [readable original text](sources/PMID_35238790.html) | [XML](sources/PMID_35238790.xml)

Stream: cross_domain_methodological_context. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Outcomes and PROM instruments; Model family and LLM backbone; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_35455625"></a>
### PMID_35455625: Artificial Intelligence-Driven Prediction Modeling and Decision Making in Spine Surgery Using Hybrid Machine Learning Models.

[Citation record](records/PMID_35455625.md) | [readable original text](sources/PMID_35455625.html) | [XML](sources/PMID_35455625.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Treatment options and comparators; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_35491420"></a>
### PMID_35491420: Artificial intelligence in knee arthroplasty: current concept of the available clinical applications.

[Citation record](records/PMID_35491420.md) | [readable original text](sources/PMID_35491420.html) | [XML](sources/PMID_35491420.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Model family and LLM backbone; Historical-choice versus comparative-benefit target.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_36572235"></a>
### PMID_36572235: How to Develop and Validate Prediction Models for Orthopedic Outcomes.

[Citation record](records/PMID_36572235.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Outcomes and PROM instruments; Model family and LLM backbone.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_37937083"></a>
### PMID_37937083: Arthritis Foundation/HSS Workshop on Hip Osteoarthritis, Part 4: Nonoperative Options, Machine Learning in Predicting Total Hip Arthroplasty, Robotics, and Phenotyping to Guide Precision Rehabilitation.

[Citation record](records/PMID_37937083.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: conceptual_or_methods_guide.

Abstract signals only: Decision task and care stage.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_37968370"></a>
### PMID_37968370: A practical guide to the implementation of AI in orthopaedic research - part 1: opportunities in clinical application and overcoming existing challenges.

[Citation record](records/PMID_37968370.md) | [PDF](sources/PMID_37968370.pdf) | [readable original text](sources/PMID_37968370.html) | [XML](sources/PMID_37968370.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: conceptual_or_methods_guide.

Additional structure-mapped candidates requiring confirmation: Clinical condition and anatomical scope; Decision task and care stage; Outcomes and PROM instruments; Model family and LLM backbone; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_38026475"></a>
### PMID_38026475: ChatGPT in orthopedics: a narrative review exploring the potential of artificial intelligence in orthopedic practice.

[Citation record](records/PMID_38026475.md) | [PDF](sources/PMID_38026475.pdf) | [readable original text](sources/PMID_38026475.html) | [XML](sources/PMID_38026475.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Historical-choice versus comparative-benefit target; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_38466797"></a>
### PMID_38466797: Enabling Personalized Medicine in Orthopaedic Surgery Through Artificial Intelligence: A Critical Analysis Review.

[Citation record](records/PMID_38466797.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; External and geographic validation; Costs, latency and resource burden; Safety, privacy and accountability; Reference standard and comparator validity.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_38712416"></a>
### PMID_38712416: Clinical applications of AI-prediction tools in spine surgery: a narrative review.

[Citation record](records/PMID_38712416.md) | [PDF](sources/PMID_38712416.pdf)

Stream: orthopedic_review_working_selection. Source basis: fulltext_pdf_text. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_38991098"></a>
### PMID_38991098: Machine Learning-Assisted Decision Making in Orthopaedic Oncology.

[Citation record](records/PMID_38991098.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Outcomes and PROM instruments; Model family and LLM backbone; Retrieval, tools and evidence sources; Explanation and interpretability; Safety, privacy and accountability.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_39034416"></a>
### PMID_39034416: Artificial intelligence in total and unicompartmental knee arthroplasty.

[Citation record](records/PMID_39034416.md) | [PDF](sources/PMID_39034416.pdf) | [readable original text](sources/PMID_39034416.html) | [XML](sources/PMID_39034416.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Population and sample size; Data source, setting and geography; Input features and modalities; Model family and LLM backbone; Retrieval, tools and evidence sources; Historical-choice versus comparative-benefit target; Reproducibility and availability; Risk of bias and reporting quality; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_39199775"></a>
### PMID_39199775: Toward Fully Automated Personalized Orthopedic Treatments: Innovations and Interdisciplinary Gaps.

[Citation record](records/PMID_39199775.md) | [readable original text](sources/PMID_39199775.html) | [XML](sources/PMID_39199775.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Model family and LLM backbone.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_39204872"></a>
### PMID_39204872: Musculoskeletal Disorder (MSD) Health Data Collection, Personalized Management and Exchange Using Fast Healthcare Interoperability Resources (FHIR).

[Citation record](records/PMID_39204872.md) | [readable original text](sources/PMID_39204872.html) | [XML](sources/PMID_39204872.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Data source, setting and geography; Input features and modalities; Costs, latency and resource burden; Reproducibility and availability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_39502973"></a>
### PMID_39502973: Knee Arthroscopy in the Era of Precision Medicine: A Comprehensive Review of Tailored Approaches and Emerging Technologies.

[Citation record](records/PMID_39502973.md) | [readable original text](sources/PMID_39502973.html) | [XML](sources/PMID_39502973.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Model family and LLM backbone; Historical-choice versus comparative-benefit target.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_39592855"></a>
### PMID_39592855: A Primer on Reinforcement Learning in Medicine for Clinicians

[Citation record](records/PMID_39592855.md) | [PDF](sources/PMID_39592855.pdf) | [readable original text](sources/PMID_39592855.html) | [XML](sources/PMID_39592855.xml)

Stream: cross_domain_methodological_context. Source basis: fulltext_xml. Publication category: conceptual_or_methods_guide.

Additional structure-mapped candidates requiring confirmation: Model family and LLM backbone; Historical-choice versus comparative-benefit target; Patient-state representation and history; Rewards and multiple clinical/nonclinical objectives.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_40123682"></a>
### PMID_40123682: Revolutionizing total hip arthroplasty: The role of artificial intelligence and machine learning

[Citation record](records/PMID_40123682.md) | [PDF](sources/PMID_40123682.pdf) | [readable original text](sources/PMID_40123682.html) | [XML](sources/PMID_40123682.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Population and sample size; Data source, setting and geography; Input features and modalities; Outcomes and PROM instruments; Follow-up and assessment horizon; Historical-choice versus comparative-benefit target; Costs, latency and resource burden; Reproducibility and availability; Risk of bias and reporting quality; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_40405922"></a>
### PMID_40405922: Artificial Intelligence and Musculoskeletal Surgical Applications.

[Citation record](records/PMID_40405922.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Prospective impact and patient benefit; Costs, latency and resource burden; Safety, privacy and accountability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_40838224"></a>
### PMID_40838224: Artificial intelligence and machine learning in spine care: Advancing precision diagnosis, treatment, and rehabilitation.

[Citation record](records/PMID_40838224.md) | [readable original text](sources/PMID_40838224.html) | [XML](sources/PMID_40838224.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Treatment options and comparators; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Costs, latency and resource burden; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_40909853"></a>
### PMID_40909853: AI Agents in Clinical Medicine: A Systematic Review.

[Citation record](records/PMID_40909853.md) | [readable original text](sources/PMID_40909853.html) | [XML](sources/PMID_40909853.xml)

Stream: cross_domain_methodological_context. Source basis: fulltext_xml. Publication category: preprint_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Population and sample size; Data source, setting and geography; Model family and LLM backbone; Agent architecture, roles and coordination; Retrieval, tools and evidence sources; External and geographic validation; Reference standard and comparator validity.

Evidence locator: Tables 1-3; cited version is a preprint.

Additional structure-mapped candidates requiring confirmation: Outcomes and PROM instruments; Historical-choice versus comparative-benefit target; Reproducibility and availability; Risk of bias and reporting quality; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41088452"></a>
### PMID_41088452: Artificial intelligence in total knee arthroplasty: clinical applications and implications.

[Citation record](records/PMID_41088452.md) | [readable original text](sources/PMID_41088452.html) | [XML](sources/PMID_41088452.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Study design and evidence level; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Subgroup fairness and equity; Reproducibility and availability; Safety, privacy and accountability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41103258"></a>
### PMID_41103258: Artificial intelligence agents in orthopaedics: Concepts, capabilities and the road ahead.

[Citation record](records/PMID_41103258.md) | [readable original text](sources/PMID_41103258.html) | [XML](sources/PMID_41103258.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Workflow, end users and usability; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41127763"></a>
### PMID_41127763: AI-Enhanced Surgical Decision-Making in Orthopedics: From Preoperative Planning to Intraoperative Guidance and Real-Time Adaptation.

[Citation record](records/PMID_41127763.md) | [readable original text](sources/PMID_41127763.html) | [XML](sources/PMID_41127763.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41144723"></a>
### PMID_41144723: Is orthopaedics entering the age of generative AI?-A narrative review of current applications challenges and future directions.

[Citation record](records/PMID_41144723.md) | [PDF](sources/PMID_41144723.pdf) | [readable original text](sources/PMID_41144723.html) | [XML](sources/PMID_41144723.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Historical-choice versus comparative-benefit target; Reproducibility and availability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41174934"></a>
### PMID_41174934: Precision medicine in orthopaedics: A review of current technologies and future directions.

[Citation record](records/PMID_41174934.md) | [readable original text](sources/PMID_41174934.html) | [XML](sources/PMID_41174934.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Model family and LLM backbone; Historical-choice versus comparative-benefit target; Reproducibility and availability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41180563"></a>
### PMID_41180563: A practical guide to the implementation of artificial intelligence in orthopaedic research-Part 3: How orthopaedic research benefits from the implementation of artificial intelligence.

[Citation record](records/PMID_41180563.md) | [PDF](sources/PMID_41180563.pdf) | [readable original text](sources/PMID_41180563.html) | [XML](sources/PMID_41180563.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: conceptual_or_methods_guide.

Additional structure-mapped candidates requiring confirmation: Outcomes and PROM instruments; Reproducibility and availability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41245704"></a>
### PMID_41245704: Artificial intelligence fails to outperform orthopaedic surgeons: A systematic review.

[Citation record](records/PMID_41245704.md) | [PDF](sources/PMID_41245704.pdf) | [readable original text](sources/PMID_41245704.html) | [XML](sources/PMID_41245704.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: systematic_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Data source, setting and geography; Model family and LLM backbone; Reference standard and comparator validity; Performance measures and comparison criteria.

Evidence locator: Table 1; Methods: Screening and data extraction.

Additional structure-mapped candidates requiring confirmation: Historical-choice versus comparative-benefit target; Reproducibility and availability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41245724"></a>
### PMID_41245724: Artificial intelligence algorithms in orthopaedics: A narrative review of methods and clinical applications.

[Citation record](records/PMID_41245724.md) | [readable original text](sources/PMID_41245724.html) | [XML](sources/PMID_41245724.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Treatment options and comparators; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Costs, latency and resource burden; Safety, privacy and accountability; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41346991"></a>
### PMID_41346991: Clinical applications of large language models in knee osteoarthritis: a systematic review.

[Citation record](records/PMID_41346991.md) | [readable original text](sources/PMID_41346991.html) | [XML](sources/PMID_41346991.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: systematic_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Population and sample size; Model family and LLM backbone; Risk of bias and reporting quality; Performance measures and comparison criteria.

Evidence locator: Tables 1-2; Methods: data extraction and synthesis.

Additional structure-mapped candidates requiring confirmation: Data source, setting and geography; Outcomes and PROM instruments; Historical-choice versus comparative-benefit target; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41407055"></a>
### PMID_41407055: Artificial Intelligence-Driven Decision-Making for Knee Joint Manipulation Following Primary Total Knee Arthroplasty.

[Citation record](records/PMID_41407055.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_41490410"></a>
### PMID_41490410: The Application of Agentic Artificial Intelligence in Orthopaedics.

[Citation record](records/PMID_41490410.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: conceptual_or_methods_guide.

Abstract signals only: Decision task and care stage; Model family and LLM backbone; Agent architecture, roles and coordination; Retrieval, tools and evidence sources; Subgroup fairness and equity; Safety, privacy and accountability.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_41536317"></a>
### PMID_41536317: Artificial intelligence in spine care: A scoping review of treatment applications.

[Citation record](records/PMID_41536317.md) | [readable original text](sources/PMID_41536317.html) | [XML](sources/PMID_41536317.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Treatment options and comparators; Study design and evidence level; Population and sample size; Data source, setting and geography; Outcomes and PROM instruments; Follow-up and assessment horizon; Model family and LLM backbone; Workflow, end users and usability; Risk of bias and reporting quality; Performance measures and comparison criteria.

Evidence locator: Methods: Data Extraction; Tables 2-4.

Additional structure-mapped candidates requiring confirmation: Historical-choice versus comparative-benefit target; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41568289"></a>
### PMID_41568289: Implementation of clinical decision support tools for treatment selection in knee osteoarthritis: a scoping review.

[Citation record](records/PMID_41568289.md) | [PDF](sources/PMID_41568289.pdf) | [readable original text](sources/PMID_41568289.html) | [XML](sources/PMID_41568289.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Treatment options and comparators; Study design and evidence level; Population and sample size; Data source, setting and geography; Input features and modalities; Outcomes and PROM instruments; Follow-up and assessment horizon; Model family and LLM backbone; Workflow, end users and usability; Prospective impact and patient benefit; Performance measures and comparison criteria.

Evidence locator: Tables 1-3; Methods: data extraction and data items.

Additional structure-mapped candidates requiring confirmation: Historical-choice versus comparative-benefit target; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41607969"></a>
### PMID_41607969: Artificial Intelligence for Predicting Postoperative Complications in Orthopedics: A Review of Clinical Applications, Challenges, and Future Directions.

[Citation record](records/PMID_41607969.md) | [readable original text](sources/PMID_41607969.html) | [XML](sources/PMID_41607969.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Missingness, attrition and selection; Calibration and proper scoring; Risk of bias and reporting quality.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41614143"></a>
### PMID_41614143: Application of artificial intelligence in postoperative orthopedic rehabilitation: a scoping review.

[Citation record](records/PMID_41614143.md) | [readable original text](sources/PMID_41614143.html) | [XML](sources/PMID_41614143.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Population and sample size; Data source, setting and geography; Model family and LLM backbone.

Evidence locator: Table 1; Methods: data extraction.

Additional structure-mapped candidates requiring confirmation: Treatment options and comparators; External and geographic validation; Calibration and proper scoring; Safety, privacy and accountability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41657679"></a>
### PMID_41657679: Artificial intelligence models cannot yet replace experts in providing patient education for shoulder and elbow orthopaedic pathologies: a systematic review and meta-analysis.

[Citation record](records/PMID_41657679.md) | [PDF](sources/PMID_41657679.pdf) | [readable original text](sources/PMID_41657679.html) | [XML](sources/PMID_41657679.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: systematic_review.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Outcomes and PROM instruments; Model family and LLM backbone; Risk of bias and reporting quality; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41705361"></a>
### PMID_41705361: Artificial intelligence in orthopaedics: Enhanced examinations, ambient intelligence and the future of clinical practice.

[Citation record](records/PMID_41705361.md) | [PDF](sources/PMID_41705361.pdf) | [readable original text](sources/PMID_41705361.html) | [XML](sources/PMID_41705361.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Input features and modalities; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Reproducibility and availability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41720113"></a>
### PMID_41720113: Strategic Integration of Artificial Intelligence in Musculoskeletal Interventions: Scope, Success, and Pursuit of Personalized Precision Care Models.

[Citation record](records/PMID_41720113.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Treatment options and comparators; Population and sample size; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Retrieval, tools and evidence sources; Historical-choice versus comparative-benefit target; External and geographic validation; Explanation and interpretability; Workflow, end users and usability; Costs, latency and resource burden; Safety, privacy and accountability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_41738015"></a>
### PMID_41738015: Medical large language models and systems in the clinical application of spinal diseases: Current status, challenges, and future prospects.

[Citation record](records/PMID_41738015.md) | [readable original text](sources/PMID_41738015.html) | [XML](sources/PMID_41738015.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Input features and modalities; Model family and LLM backbone; Retrieval, tools and evidence sources; Subgroup fairness and equity; Workflow, end users and usability; Reproducibility and availability; Safety, privacy and accountability; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41749766"></a>
### PMID_41749766: When Intuition Meets the Algorithm: Medico-Legal Implications of Artificial Intelligence-Driven Decision-Making in Orthopedics.

[Citation record](records/PMID_41749766.md) | [readable original text](sources/PMID_41749766.html) | [XML](sources/PMID_41749766.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41827166"></a>
### PMID_41827166: Artificial Intelligence in Orthopaedics: Clinical Performance, Limitations, and Translational Readiness-A Review.

[Citation record](records/PMID_41827166.md) | [PDF](sources/PMID_41827166.pdf) | [readable original text](sources/PMID_41827166.html) | [XML](sources/PMID_41827166.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Historical-choice versus comparative-benefit target; Safety, privacy and accountability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41933417"></a>
### PMID_41933417: Artificial intelligence in orthopedics: current applications, challenges, and future directions.

[Citation record](records/PMID_41933417.md) | [PDF](sources/PMID_41933417.pdf) | [readable original text](sources/PMID_41933417.html) | [XML](sources/PMID_41933417.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Study design and evidence level; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Explanation and interpretability; Workflow, end users and usability; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_41973309"></a>
### PMID_41973309: Artificial Intelligence and its Current Role in Clinical Outcome Prediction, Musculoskeletal Imaging, and Economic and Ethical Considerations within Orthopedics and Sports Medicine.

[Citation record](records/PMID_41973309.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Outcomes and PROM instruments; Model family and LLM backbone; External and geographic validation; Workflow, end users and usability; Costs, latency and resource burden; Reproducibility and availability; Safety, privacy and accountability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_41973342"></a>
### PMID_41973342: Risk prediction in spine surgery: a scoping review of traditional models, artificial intelligence, and the challenge of clinical translation.

[Citation record](records/PMID_41973342.md) | [PDF](sources/PMID_41973342.pdf)

Stream: orthopedic_review_working_selection. Source basis: fulltext_pdf_text. Publication category: scoping_review.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42101555"></a>
### PMID_42101555: Digital twins and multimodal artificial intelligence in spine care: a scoping review of concepts, evidence, and translational barriers.

[Citation record](records/PMID_42101555.md) | [PDF](sources/PMID_42101555.pdf)

Stream: orthopedic_review_working_selection. Source basis: fulltext_pdf_text. Publication category: scoping_review.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42122313"></a>
### PMID_42122313: Exploring Artificial Intelligence in Orthopedic Surgery: A Review of Perception, Decision, and Execution Systems.

[Citation record](records/PMID_42122313.md) | [readable original text](sources/PMID_42122313.html) | [XML](sources/PMID_42122313.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Clinical condition and anatomical scope; Decision task and care stage; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Retrieval, tools and evidence sources; Historical-choice versus comparative-benefit target; Temporal validation and drift; Uncertainty, abstention and unsupported inputs; Reproducibility and availability; Safety, privacy and accountability; Risk of bias and reporting quality; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42245303"></a>
### PMID_42245303: From data to decisions: machine learning in predicting outcomes of robotic-assisted total knee arthroplasty.

[Citation record](records/PMID_42245303.md) | [readable original text](sources/PMID_42245303.html) | [XML](sources/PMID_42245303.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Population and sample size; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Explanation and interpretability; Subgroup fairness and equity; Costs, latency and resource burden; Risk of bias and reporting quality; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42278988"></a>
### PMID_42278988: Digital Twins in Orthopedics and Trauma: Concepts, Emerging Evidence, and Barriers to Clinical Translation.

[Citation record](records/PMID_42278988.md) | [readable original text](sources/PMID_42278988.html) | [XML](sources/PMID_42278988.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42287372"></a>
### PMID_42287372: Improving the design of observational studies in orthopaedics: a practical guide to target trial emulation.

[Citation record](records/PMID_42287372.md) | [readable original text](sources/PMID_42287372.html) | [XML](sources/PMID_42287372.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: conceptual_or_methods_guide.

Additional structure-mapped candidates requiring confirmation: Outcomes and PROM instruments; Follow-up and assessment horizon; Retrieval, tools and evidence sources; Causal identification and target trial design; Treatment overlap and positivity; Time zero and information leakage; Reproducibility and availability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42322047"></a>
### PMID_42322047: Clinical accuracy and applications of large language models in pediatric orthopedics: a systematic review.

[Citation record](records/PMID_42322047.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: systematic_review.

Abstract signals only: Clinical condition and anatomical scope; Decision task and care stage; Study design and evidence level; Model family and LLM backbone; Reproducibility and availability; Reference standard and comparator validity; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_42343897"></a>
### PMID_42343897: Artificial intelligence in orthopedic regenerative medicine: from design to clinical translational pathways.

[Citation record](records/PMID_42343897.md) | [readable original text](sources/PMID_42343897.html) | [XML](sources/PMID_42343897.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Model family and LLM backbone; External and geographic validation; Explanation and interpretability; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42383711"></a>
### PMID_42383711: Frameworks and methods for estimating the causal effect of clinical treatment in orthopaedics: a scoping review.

[Citation record](records/PMID_42383711.md) | [readable original text](sources/PMID_42383711.html) | [XML](sources/PMID_42383711.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: scoping_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Treatment options and comparators; Study design and evidence level; Population and sample size; Data source, setting and geography; Input features and modalities; Outcomes and PROM instruments; Causal identification and target trial design; Confounder selection and adjustment; Risk of bias and reporting quality.

Evidence locator: Tables 1-3; Methods: charting the data and risk appraisal.

Additional structure-mapped candidates requiring confirmation: Historical-choice versus comparative-benefit target; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42506117"></a>
### PMID_42506117: From One-Size-Fits-All to Data-Driven Recovery: A Narrative Review of Wearable Technologies Toward Personalized Rehabilitation After Total Hip and Knee Arthroplasty.

[Citation record](records/PMID_42506117.md) | [readable original text](sources/PMID_42506117.html) | [XML](sources/PMID_42506117.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Population and sample size; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Workflow, end users and usability; Reproducibility and availability; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42529139"></a>
### PMID_42529139: Artificial intelligence and big data for precision regenerative medicine in knee osteoarthritis: endotyping, responder prediction, and clinical translation.

[Citation record](records/PMID_42529139.md) | [readable original text](sources/PMID_42529139.html) | [XML](sources/PMID_42529139.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Input features and modalities; Historical-choice versus comparative-benefit target; External and geographic validation; Explanation and interpretability; Subgroup fairness and equity; Workflow, end users and usability; Prospective impact and patient benefit; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42536128"></a>
### PMID_42536128: Artificial intelligence in knee osteotomy: evolution of alignment assessment and surgical decision-making.

[Citation record](records/PMID_42536128.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Clinical condition and anatomical scope; Treatment options and comparators; Outcomes and PROM instruments; Model family and LLM backbone; Retrieval, tools and evidence sources; External and geographic validation; Explanation and interpretability; Workflow, end users and usability; Prospective impact and patient benefit; Reproducibility and availability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_42597887"></a>
### PMID_42597887: Artificial Intelligence-Guided Precision Orthobiologics in Musculoskeletal Conditions.

[Citation record](records/PMID_42597887.md) | [readable original text](sources/PMID_42597887.html) | [XML](sources/PMID_42597887.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: conceptual_or_methods_guide.

Additional structure-mapped candidates requiring confirmation: Outcomes and PROM instruments; Model family and LLM backbone; Explanation and interpretability; Safety, privacy and accountability.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42686880"></a>
### PMID_42686880: Large language models in the vertical integration of spine surgery workflow: a scoping review.

[Citation record](records/PMID_42686880.md) | [PDF](sources/PMID_42686880.pdf)

Stream: orthopedic_review_working_selection. Source basis: fulltext_pdf_text. Publication category: scoping_review.

Dimension extraction remains pending original-source assessment.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42739558"></a>
### PMID_42739558: Artificial Intelligence in Orthopaedics: Current Evidence and Clinical Translation Across the Patient Care Pathway.

[Citation record](records/PMID_42739558.md) | [readable original text](sources/PMID_42739558.html) | [XML](sources/PMID_42739558.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Study design and evidence level; Historical-choice versus comparative-benefit target; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42757394"></a>
### PMID_42757394: Generative Artificial Intelligence in Hip and Knee Arthroplasty: A Systematic Review of Emerging Clinical Applications in Patient Communication and Education, Documentation, and Decision Support.

[Citation record](records/PMID_42757394.md) | [readable original text](sources/PMID_42757394.html) | [XML](sources/PMID_42757394.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: systematic_review.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Model family and LLM backbone; Performance measures and comparison criteria.

Evidence locator: Methods: Synthesis Approach; Results: three application groups.

Additional structure-mapped candidates requiring confirmation: Reproducibility and availability; Review search, selection and synthesis.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42791908"></a>
### PMID_42791908: Artificial Intelligence in Arthroplasty: A Comprehensive Structured Critical Review and Descriptive Evidence Map of Validation, Uncertainty, and Workflow Integration.

[Citation record](records/PMID_42791908.md) | [readable original text](sources/PMID_42791908.html) | [XML](sources/PMID_42791908.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Checked charting/comparison dimensions: Clinical condition and anatomical scope; Decision task and care stage; Model family and LLM backbone; Frozen model versus redevelopment; External and geographic validation; Temporal validation and drift; Calibration and proper scoring; Uncertainty, abstention and unsupported inputs; Decision utility and policy value; Workflow, end users and usability; Prospective impact and patient benefit; Safety, privacy and accountability; Risk of bias and reporting quality; Unit of analysis and dependent evidence.

Evidence locator: Methods 2.5-2.6; Tables 1-6; Discussion 4.3-4.8.

Additional structure-mapped candidates requiring confirmation: Data source, setting and geography; Outcomes and PROM instruments; Historical-choice versus comparative-benefit target; Reproducibility and availability; Review search, selection and synthesis; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42793474"></a>
### PMID_42793474: Artificial Intelligence for Clinical Decision Support in Rural Spine Care: A Narrative Review.

[Citation record](records/PMID_42793474.md) | [readable original text](sources/PMID_42793474.html) | [XML](sources/PMID_42793474.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Clinical condition and anatomical scope; Decision task and care stage; Population and sample size; Data source, setting and geography; Model family and LLM backbone; Retrieval, tools and evidence sources; External and geographic validation; Subgroup fairness and equity; Safety, privacy and accountability; Performance measures and comparison criteria.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42824522"></a>
### PMID_42824522: Artificial Intelligence and Decision Support in Orthopaedic Emergencies: A Review.

[Citation record](records/PMID_42824522.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Data source, setting and geography; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; External and geographic validation; Explanation and interpretability; Workflow, end users and usability; Costs, latency and resource burden; Safety, privacy and accountability; Performance measures and comparison criteria.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_42851913"></a>
### PMID_42851913: Artificial intelligence in the biomechanics of knee osteoarthritis: biomechanical phenotyping, risk stratification, diagnosis, treatment and clinical translation-a narrative review.

[Citation record](records/PMID_42851913.md) | [readable original text](sources/PMID_42851913.html) | [XML](sources/PMID_42851913.xml)

Stream: orthopedic_review_working_selection. Source basis: fulltext_xml. Publication category: narrative_or_other_review_pending_full_method_check.

Additional structure-mapped candidates requiring confirmation: Decision task and care stage; Input features and modalities; Outcomes and PROM instruments; Historical-choice versus comparative-benefit target; External and geographic validation; Explanation and interpretability; Subgroup fairness and equity; Costs, latency and resource burden; Safety, privacy and accountability; Risk of bias and reporting quality.

Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.

<a id="pmid_42879167"></a>
### PMID_42879167: Artificial intelligence across the continuum of care for the aging musculoskeletal patient: From longitudinal phenotyping to personalized surgery and recovery monitoring.

[Citation record](records/PMID_42879167.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: narrative_or_other_review_pending_full_method_check.

Abstract signals only: Decision task and care stage; Treatment options and comparators; Study design and evidence level; Population and sample size; Data source, setting and geography; Input features and modalities; Outcomes and PROM instruments; Model family and LLM backbone; Historical-choice versus comparative-benefit target; Temporal validation and drift; Calibration and proper scoring; Uncertainty, abstention and unsupported inputs; Explanation and interpretability; Workflow, end users and usability; Prospective impact and patient benefit; Safety, privacy and accountability.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

<a id="pmid_42896011"></a>
### PMID_42896011: Propensity Score Methods and Target Trial Emulation in Orthopaedic Surgery: A Practical Guide to Causal Inference from Observational Data.

[Citation record](records/PMID_42896011.md) | Original main text still needed

Stream: orthopedic_review_working_selection. Source basis: abstract_only. Publication category: conceptual_or_methods_guide.

Abstract signals only: Input features and modalities; Outcomes and PROM instruments; Follow-up and assessment horizon; Model family and LLM backbone; Causal identification and target trial design; Confounder selection and adjustment; Treatment overlap and positivity; Time zero and information leakage; Reproducibility and availability; Reference standard and comparator validity.

**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.

