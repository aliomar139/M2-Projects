# Second-pass extraction: status and interpretation

Date: 23 October 2026. The [matrix](../../data/audit/second_pass_matrix.csv) covers all 100 legacy citations. It includes identity, original-versus-summary source status, publication metadata and the requested extraction fields. Eighteen papers have focused assistant reading notes tied to PDF pages or named sections. The other entries remain explicitly pending; automatically located source passages are not completed appraisal.

## How to read the matrix

`assistant_focused_second_pass_completed` means that the indicated abstract/method/results or limitation sections were checked for the stated fields. It does not assert exhaustive line-by-line reading or independent reviewer confirmation. Fields not transcribed remain unknown. `source_passages_only_not_adjudicated` means candidate source passages exist but no final extraction is claimed. `blocked_original_text` means the supplied PDF is a summary or wrong document and matching main text was not recovered.

The matrix separates surgeon-choice imitation, outcome prediction, simulated/offline policies, causal-method perspectives and actual comparative designs. BART, random forests, survival networks and reinforcement learning do not become causal merely because of their names. The design, estimand and identification assumptions determine the interpretation.

## Findings affecting the thesis

Ribbons et al. predicts three-month postoperative PROM changes and uncertainty in a TKA cohort; this supports prognosis, not a conservative-versus-surgery benefit estimate. Huber et al. similarly predicts improvement among surgical recipients. Milella et al.'s MCID classifier cannot establish that a different treatment would improve outcomes without a comparator design.

EB-GAIT is especially relevant because it explicitly combines models of historical surgical practice with outcome models. Its counterfactual simulations require careful appraisal before treating simulated improvements as causal clinical benefits. It is a stronger architectural comparator than generic imaging classifiers.

The HCC two-stage system reports external validation and separates treatment ranking from survival prediction, but treatment-conditioned prognosis does not automatically identify comparative benefit. DeepSurv has the same general interpretive issue. The PAI example uses randomized depression-treatment data; its subgroup effect is not evidence that an orthopedic application will achieve the same benefit.

Dong et al.'s orthopedic rehabilitation gains occur in a simulated environment and use different static comparators for the reported recovery and reinjury percentages. Neither percentage is an observed patient outcome. The chronic musculoskeletal pain pilot by Zmudzki et al. assesses 17 new patients and clinician usefulness/concordance, rather than comparative treatment efficacy.

## Additional primary studies and anchors

Source records are retained in `additional_source_registry.csv`. The following are outside, or not represented by original text within, the legacy collection:

| Source | Evidence checked | Why it matters / next check |
|---|---|---|
| [van der Weegen et al.](https://pubmed.ncbi.nlm.nih.gov/38007205/), DOI 10.1016/j.arth.2023.11.022 | Verified bibliographic record and abstract; full text not recovered | Missing legacy anchor; historical-choice prediction. Check cohort partitioning and the exact denominators before repeating accuracy claims |
| [Meng et al., JMLR 2020](https://www.jmlr.org/papers/v21/20-334.html) | Original article XML and journal abstract; alternative near-optimal treatment sets | Useful methodological comparator; not an orthopedic clinical validation |
| [IDEA individualized rules](https://pubmed.ncbi.nlm.nih.gov/32144896/) | Abstract: 343 randomized trial participants; exercise/diet treatment rules, seven outcomes including WOMAC | Direct prior orthopedic ITR work; full-text methods, multiplicity, internal validation and availability of trial data require appraisal |
| [PROM-alert causal forest](https://pubmed.ncbi.nlm.nih.gov/37392619/) | Abstract: roughly 8,000 participants in a nine-hospital randomized trial | Heterogeneous effects concern remote monitoring after surgery; check exact sample and model validation in full text |
| [CSM surgical approaches](https://pubmed.ncbi.nlm.nih.gov/42066358/) | Abstract: 1,085 patients, multicenter observational data, doubly robust framework | Relevant surgical-choice comparator; full-text confounder handling, overlap and baseline timing remain unverified |
| [Woo et al.](https://pubmed.ncbi.nlm.nih.gov/39521391/) | Abstract and publication record; 100 ACL-guideline questions, RAG and agent augmentation | Evidence-grounding comparator; question-answer accuracy is distinct from treatment-effect estimation or patient benefit |
| [Halvorson et al.](https://pubmed.ncbi.nlm.nih.gov/41838559/) | Abstract and publication record; predicting actual surgeon plans | Imitation comparator; original main text still needed. Retain the source's unusual online/issue date ordering as a metadata issue |

## Remaining extraction and appraisal

Retrieve the 41 queued original texts; finish focused and full-method extraction for the other papers; inspect corrections/retractions where relevant; link related reports to studies; assess risk of bias using the appropriate current tools; and adjudicate eligibility and extracted fields. No paper has a formal risk-of-bias rating in this package. A second independent reviewer is still pending for every row.

Only after these steps should the project recompute percentages of causal approaches, calibration, decision-curve analysis, external validation or prospective deployment. The current matrix intentionally does not reproduce the legacy percentages.
