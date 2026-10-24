# Candidate new dimensions for the orthopedic treatment-support review

**Current ten-review requirement (24 October 2026):** use [the five shared dimensions](Surveys/review_dimensions/Five_Shared_New_Dimensions.md), checked across all ten selected reviews. There are five in total. The seven candidates below belong to the separate broader-library research exploration and are not seven additional dimensions for that ten-review task.

Prepared for the professor's 24 October 2026 tasks. Evidence checked through 23 October 2026.

## What can currently be claimed

The requested five new dimensions are developed below as **seven candidate joint evaluation dimensions**. None is established as never studied. Each combines known ideas into a specific, testable question about patient-specific orthopedic treatment decisions. The full-text review and wider database search remain incomplete, and a narrow search returning zero records cannot establish novelty.

Calibration, external validation, uncertainty, explanation, fairness, workflow integration, PROMs and human oversight already appear in existing reviews. They are not proposed as new dimensions on their own. The working [dimension inventory](Surveys/dimensions.md) contains 85 papers, with eleven focused checks of original charting/comparison frameworks; automated mappings elsewhere still require adjudication.

Two recovered cross-domain surveys further restrict novelty: [Rathod et al.](https://doi.org/10.1007/s44163-026-01187-2) already compares treatment-recommender paradigms, validation, transparency, scalability and explanation; [Kaul et al.](https://doi.org/10.1007/s44163-026-01733-y) explicitly examines sequential state/action/reward design, off-policy evaluation, safety and clinical/nonclinical objectives. Neither broad benchmarking nor adding patient preferences is new by itself. Both originals are now in the Surveys source folder.

Seven targeted PubMed searches, N1-N7, are saved in [novelty_search_log.csv](../data/reviews/novelty_search_log.csv). They produced 0, 13, 5, 0, 1, 10 and 2 hits respectively. These are terminology probes, not exhaustive novelty tests. All returned citations are retained in [novelty_search_matches.csv](../data/reviews/novelty_search_matches.csv) and [raw responses](../data/searches/novelty/). Several hits use ambiguous terms: N5's single result concerns multiagent chemotherapy, not collaborating AI agents.

## N1. Does the system withhold a recommendation when comparative benefit is not identifiable?

**Unit of analysis:** one patient, decision time and candidate treatment pair.

Examine whether an agent checks the treatment contrast, pretreatment adjustment set, time zero, overlap and relevant follow-up before it communicates a comparative-benefit recommendation. Assess whether the gate remains binding through the final clinician-facing response. Merely displaying a confidence interval does not satisfy this dimension.

**Operational fields:** treatment contrast; baseline alignment; stated identification assumptions; overlap threshold; missing-confounder handling; numerical tool output; final response action; reason for withholding a recommendation.

**Evaluation:** construct supported and unsupported cases; measure appropriate withholding, unsupported recommendation frequency, false withholding on supported cases, and whether the explanation accurately reflects the numerical tool's limits. An overlap diagnostic alone cannot prove absence of unmeasured confounding.

**Existing overlap:** [Widmer et al.](https://doi.org/10.1530/EOR-2025-0266) reviews causal frameworks and adjustment in orthopedics. The [target-trial guide](https://pubmed.ncbi.nlm.nih.gov/42287372/) discusses baseline alignment and eligibility. These components are established. The candidate contribution is the measured enforcement of those conditions through an orthopedic agent's recommendation, rather than a new causal estimator. N1 returned zero hits under its exact query; novelty remains unproven.

## N2. Can each recommendation be traced to both clinical evidence and the estimated treatment contrast?

**Unit of analysis:** each treatment-benefit claim in the final output.

Distinguish two chains: the guideline/article supporting a clinical assertion, and the dataset version, cohort definition, estimand, estimator and uncertainty calculation supporting a numerical benefit claim. Test whether the output uses the correct chain for each assertion. A valid citation to a guideline does not establish the validity of a patient-specific numerical effect.

**Operational fields:** source/version/date; cited passage or recommendation identifier; cohort and estimator version; treatment labels and units; outcome horizon; stated effect; claim-to-source correspondence; conflicts and their resolution.

**Evaluation:** change a guideline version while freezing the estimator, and then update the estimator while freezing the guideline. Measure unsupported numerical claims, mismatched horizons, stale citations and incorrect source attribution. Keep clinician review in the study design.

**Existing overlap:** [Woo et al.](https://pubmed.ncbi.nlm.nih.gov/39521391/) evaluates orthopedic evidence retrieval and agent augmentation; [the arthroplasty evidence map](https://pubmed.ncbi.nlm.nih.gov/42791908/) already emphasizes auditable outputs and model-state distinctions. The proposed dimension concerns the connection between the two chains. N2's 13 hits include conventional reviews and clinical comparisons; their presence does not establish an implemented dual-chain audit, and their absence from this narrow use case does not prove novelty.

## N3. Does the system distinguish similar treatment benefit from insufficient knowledge?

**Unit of analysis:** a patient-specific set of clinically feasible options.

Separate three cases: options have sufficiently similar estimated benefit under a predefined clinical margin; the available data cannot distinguish options with useful precision; or a causal comparison lacks support. Evaluate what the system recommends in each case and how it incorporates patient preferences.

**Operational fields:** eligible options; clinical equivalence/indifference margin; effect scale and horizon; interval or posterior criterion; data-support status; preference weights; returned option set; explanation of why multiple options remain.

**Evaluation:** measure inappropriate forced choices, false equivalence declarations, inappropriate preference trade-offs when a comparison is unsupported, and agreement with prespecified decision rules. A nonsignificant difference is not proof of equivalence.

**Existing overlap:** [Meng et al.](https://www.jmlr.org/papers/v21/20-334.html) already develops near-optimal treatment sets. [Research on uncertainty in hip-infection revision decisions](https://pubmed.ncbi.nlm.nih.gov/28403859/) and patient-preference research also precede this project. The proposed contribution would be an explicit orthopedic evaluation distinguishing these different reasons for returning multiple options. N3 returned five records; this dimension is a refinement of established concepts, with novelty unproven.

## N4. How do clinical-note extraction errors propagate into treatment recommendations?

**Unit of analysis:** paired versions of the same case with a controlled information perturbation.

Link errors in extracting pretreatment variables to changes in estimated comparative benefit, guideline eligibility and the final recommendation. Compare innocuous wording changes with clinically consequential changes such as laterality, units, symptom timing, contraindications or PROM scale direction.

**Operational fields:** source note; ground-truth structured fields; extracted values and units; perturbation type; intermediate model inputs; effect/ranking change; final recommendation change; clinician-detected error.

**Evaluation:** report extraction error rates alongside recommendation changes caused by extraction errors, clinically meaningful changes in estimated effect, and recovery after correction. Separate this from prediction-model instability and from changes caused by genuinely new clinical information.

**Existing overlap:** the KOA LLM review [Ma et al.](https://pubmed.ncbi.nlm.nih.gov/41346991/) already discusses prompt sensitivity and output reliability. The arthroplasty evidence map also includes information extraction. The proposed dimension follows a documented extraction error through a comparative-benefit pipeline, rather than merely measuring answer consistency. N4 returned zero records under the exact query; broader terminology and primary-study checks remain necessary.

## N5. What does agent coordination add when tools and resources are held constant?

**Unit of analysis:** the same orthopedic decision task under matched system configurations.

Compare a fixed workflow, a single agent and a coordinated agent team using the same source corpus, numerical estimator, model backbone, cases and declared compute budget. Record whether handoffs change the treatment labels, baseline time, effect units or outcome definition.

**Operational fields:** agent roles; handoff schema; tool availability; allowed calls; model/version; token/runtime budget; estimator inputs and outputs; semantic mismatches; final task performance and cost.

**Evaluation:** separate gains due to retrieval and tools from gains due to coordination; measure errors introduced at handoffs and whether observed gains survive matched-resource comparisons. No universal team size is assumed.

**Existing overlap:** [Gorenshtein et al.'s cited preprint](https://doi.org/10.1101/2025.08.22.25334232) already compares architectures and notes that tools can explain some gains. Orthopedic agent concept reviews also cover coordination. The candidate extension is a controlled orthopedic comparative-benefit benchmark with semantic handoff checks. N5's chemotherapy false positive demonstrates why term matching needs manual review. Novelty is unproven.

## N6. Can the system localize why a treatment recommendation changed after an update?

**Unit of analysis:** the same case evaluated before and after one component changes.

Track changes separately for a hospital/cohort shift, a guideline update, an estimator update and an LLM/prompt update. Ask whether the system can attribute a recommendation change to the right component while retaining comparability of treatment and outcome definitions.

**Operational fields:** component versions; frozen/adapted model state; source hospital; guideline date; outcome horizon; recommendation; identified change cause; overlap/calibration state; revision authorization and audit trail.

**Evaluation:** use controlled component substitutions. Report recommendation changes by cause, attribution errors, failures to detect changed support and changes that persist after reverting a component. A desirable recommendation change must be distinguished from instability.

**Existing overlap:** frozen versus redeveloped models, temporal validity and deployment monitoring are already explicit in [the arthroplasty evidence map](https://pubmed.ncbi.nlm.nih.gov/42791908/). The proposed dimension concerns attribution across the whole recommendation workflow. N6 returned ten records, many concerning guideline updates rather than AI update attribution. This is a candidate operational extension, not a new concept of drift.

## N7. Do clinician overrides create identifiable feedback effects in later recommendations?

**Unit of analysis:** a logged recommendation, clinician decision and subsequent outcome, followed across system versions.

Distinguish an override caused by a missing contraindication, a patient preference, disagreement about evidence, or distrust of the tool. Examine whether using those decisions as future labels would teach clinician imitation, correct a missing feature, or introduce selection bias. Do not treat override frequency alone as a quality score.

**Operational fields:** recommendation and support status; override reason; patient choice; final treatment; observed follow-up/missingness; model update policy; whether override information enters the model; clinician workload and retention of independent judgment.

**Evaluation:** use an observational logging or simulation study first; assess re-estimated policy value with appropriate confounding/selection assumptions, subgroup differences, and the extent to which later models learn overrides without their reasons. Offline changes cannot establish prospective patient benefit.

**Existing overlap:** [Jacobs et al.](https://doi.org/10.1038/s41398-021-01224-x) studies clinician responses to ML advice outside orthopedics. N7 also found [AI-induced deskilling in orthopedic surgery](https://pubmed.ncbi.nlm.nih.gov/42842895/), which directly overlaps the human-judgment component. The candidate extension is the documented link between override reasons, subsequent treatment/outcome selection and future model updates. Novelty remains unproven.

## How to choose five for the thesis

N1-N5 are the initial shortlist because they can be evaluated within a bounded retrospective or semisynthetic workflow, if suitable data and source cases exist. N6-N7 require version history or longitudinal deployment logs; retain them as secondary dimensions unless those data become available. This is a feasibility recommendation, not evidence that the first five are novel.

For each selected dimension, finish the full-text review, inspect supplementary extraction forms, search alternative terms and wider databases, and compare the exact operational measure with prior primary studies. If a prior paper already implements it, classify the contribution as replication, orthopedic adaptation or improved evaluation. Use the final evidence to replace “candidate” with a supported, narrowly worded claim.
