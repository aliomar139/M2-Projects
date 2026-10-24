# A defensible thesis contribution

Working proposal, 23 October 2026. This is a research design, not a claim that novelty or clinical efficacy has been established.

## Proposed question

For one defined orthopedic treatment decision, can a clinician-facing workflow distinguish predicted historical practice from estimated comparative patient benefit, expose when the data do not support a recommendation, and present a traceable explanation grounded in the available evidence?

Restrict the first empirical study to one condition, a clearly defined treatment choice, a baseline decision time and a fixed outcome horizon. Knee osteoarthritis is a reasonable candidate, but the dataset must determine the final scope. Do not promise an operative-versus-conservative comparison until access and measurement checks establish that both groups are available and comparable.

## What the literature already provides

Reviews already cover KOA decision-aid implementation, orthopedic causal inference, generative-AI applications and clinical agent architectures; see [CLOSEST_REVIEWS.md](CLOSEST_REVIEWS.md). Primary work has also learned diet/exercise treatment rules in knee OA and modeled heterogeneous effects of PROM monitoring after arthroplasty. These precedents rule out broad claims of being the first orthopedic personalized-treatment system or the first use of causal ML in the field.

The narrower opportunity is an explicitly evaluated connection between an identifiable comparative-benefit estimator and an evidence-grounded decision-support workflow. Whether this connection is underexplored remains a hypothesis until screening and full-text comparison establish its boundary.

## Review contribution

Code each eligible study along independent dimensions:

| Dimension | Values / questions |
|---|---|
| Decision target | Surgeon choice, prognosis under received treatment, comparative benefit, or treatment policy |
| Treatment structure | Single intervention, explicit alternatives, or sequential choices |
| Input timing | Pretreatment only, longitudinal history, or potentially leaked post-treatment information |
| Identification | Randomization or specified observational assumptions; adjustment rationale and overlap |
| Outcome | PROM, complications, survival, utility or agreement; time horizon and missingness |
| Evaluation | Internal/external prediction validation, causal/policy evaluation, prospective decision impact or patient outcomes |
| Architecture | Fixed workflow, retrieval, tool-calling agent or multi-agent coordination; what each component adds |
| Recommendation boundary | Uncertainty, inadequate support, near-equivalent options, patient preferences and clinician review |

An interpretable evidence map across these dimensions would be more specific than another broad catalogue of orthopedic AI. Its contribution should be described as the resulting findings once the coding is complete, rather than claimed in advance from the choice of taxonomy.

## Empirical benchmark

Use a common eligible population and information available at the same baseline time:

1. **Historical-choice baseline:** a supervised model predicts received treatment. Report agreement and calibration as behavior-prediction results.
2. **Outcome-model baseline:** predict observed outcomes using baseline characteristics and treatment. This is a useful benchmark, but causal interpretation still requires a design and assumptions.
3. **Comparative-benefit approach:** use an appropriate design and estimator, such as a cross-fitted doubly robust learner or causal forest, with a simpler treatment-interaction model as a comparator. Do not declare any estimator mandatory or automatically causal.
4. **Decision-support experiment:** compare a fixed, transparent workflow with a tool-enabled agent using the same retrieval corpus and numerical estimator. Add multi-agent coordination only if a defined task requires it, and compare its incremental value under matched resources.

For observational data, specify consistency, conditional exchangeability and positivity assumptions, the adjustment set and its rationale, baseline timing, treatment assignment window, follow-up and missing-data handling. CATE estimates conditional average benefit among similar patients; the actual individual counterfactual difference is not observable. Avoid presenting it as an individually verified effect.

Evaluate observed-outcome calibration and prediction error separately from policy value. Use an appropriate held-out policy evaluation procedure with uncertainty estimates and inspect propensity overlap, extreme weights, subgroup performance and sensitivity to unmeasured confounding. Include external or temporal validation where the dataset supports it. Decision curve analysis is useful for suitable threshold-based decisions; it does not replace causal policy evaluation for every treatment-selection problem.

Evaluate the agent layer on source support, retrieval errors, extraction accuracy, unsupported numerical claims, correct handling of missing information, latency and cost. The numerical tool supplies treatment-effect estimates; the language model must not invent them. An ablation should separate retrieval/tool access from coordination. Offline model performance cannot establish prospective patient benefit.

## Dataset feasibility gate

Before choosing OAI, a registry or an institutional cohort, inspect its schema and access terms. Confirm both treatment groups, eligible patients at a shared decision time, confounders, pretreatment PROMs, follow-up PROMs, treatment timing and adequate overlap. A registry containing only surgical recipients cannot identify surgical benefit over conservative care on its own. New postoperative monitoring or conservative-treatment questions may be more defensible if the data support them.

If comparative benefit is not identifiable, narrow the thesis to prognosis or use a suitable randomized/semisynthetic benchmark with its limits declared. Do not generate synthetic counterfactuals and then describe their validation as clinical evidence.

## Proposed contribution wording

> This thesis will map how orthopedic decision-support studies define treatment recommendation, distinguishing historical-choice prediction, prognosis and comparative-benefit estimation. For a defined clinical decision supported by suitable data, it will benchmark these approaches and evaluate whether an evidence-grounded agent workflow improves the traceability and reliability of clinician-facing outputs. Novelty will rest on the specific task, evidence analysis and controlled evaluation established against the closest prior studies.

## Claim-evidence map and self-review

| Claim or question | Evidence / answer | Status |
|---|---|---|
| Existing repository verification claims need correction | File hashes, all-PDF text inspection, source identity checks and original-text discrepancies | Supported by the audit |
| Orthopedic causal inference and personalized rules have prior work | Closest-review table; Widmer review; IDEA and PROM-monitoring studies | Supported; detailed primary-study appraisal still needed |
| Proposed integrated workflow is novel | No exhaustive comparison completed | Unproven; do not claim first-in-field |
| Writing distinguishes targets and evidence levels | Separate task, design, architecture and evaluation dimensions | Draft distinction established |
| Empirical effect exceeds baselines | No dataset experiment performed | Needs experiments |
| Evaluation is complete | Screening, appraisal, data access and benchmark remain incomplete | Needs further work |
| Method is identifiable and worth its complexity | Depends on cohort feasibility and matched agent ablations | Needs design validation |

The draft deliberately makes no numerical clinical-benefit or prevalence claim. A final thesis abstract should follow the completed extraction and experiments.
