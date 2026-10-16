# Literature Review Abstract

### Background
Musculoskeletal disorders represent the leading global contributor to surgical disability and healthcare expenditure. Artificial intelligence and machine learning offer significant potential to transform orthopedic care by progressing beyond population-level clinical guidelines toward personalized, data-driven clinical decision support and individualized treatment recommendation.

### Scope & Corpus
This state-of-the-art review systematically analyzed a curated corpus of 100 peer-reviewed research papers spanning 2014 to 2026, with 46% published between 2025 and 2026. A core literature subset of the Top 30 papers was identified and analyzed in depth based on ten explicit criteria evaluating methodological innovation, clinical relevance, causal capability, validation rigor, and agentic paradigm leadership.

### Current State of the Art
The literature demonstrates a clear evolutionary progression: computer vision achieves expert-level performance in radiographic fracture detection and Kellgren-Lawrence grading (Level 1); tree ensembles on registry data accurately stratify surgical risks (Level 2); and multimodal Bayesian models predict individualized patient-reported outcome measures (PROMs) and minimal clinically important differences (MCID) (Level 3). Concurrently, large language models predict historical surgeon recommendations from unstructured previsit intake text with 70% to 81% accuracy (Level 4), while custom retrieval-augmented generation (RAG) and emerging agentic frameworks (Levels 6–7) demonstrate initial feasibility in automating multi-step clinical workflows.

### Findings & Critical Synthesis
A critical conceptual distinction emerges between predicting historical clinician decisions (24% of corpus) and estimating counterfactual treatment effects (3% of corpus). Current orthopedic tools predominantly automate historical practice patterns rather than optimizing individual patient outcomes. Furthermore, a statistical audit reveals profound evaluation deficits: only 6% of studies report external validation, only 7% report calibration, and only 9% evaluate prospective clinical deployments, while multi-center evaluations demonstrate severe center-specific performance degradation.

### Conclusion
While predictive machine learning in orthopedics has achieved technical maturity in retrospective datasets, personalized treatment recommendation remains constrained by treatment-assignment confounding, absence of counterfactual reasoning, lack of EHR integration, and a near-total absence of prospective randomized trials. Bridging these methodological and translational gaps represents the essential frontier for safe, evidence-based orthopedic decision support.