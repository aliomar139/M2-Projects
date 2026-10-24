# Five shared additional dimensions across the ten reviews

Updated: 24 October 2026.

**There are five proposed dimensions in total, evaluated against all ten reviews.** These replace the previous 50 paper-specific proposals. The same N1–N5 identifiers are used throughout the comparison and the individual notes.

The reference set is the ten reviews listed in [the comparison report](10_Review_Papers_Dimension_Analysis.md), not the entire 85-record survey library. “New” means **no explicit discussion of the defined dimension was found in any of these ten checked main articles**, including embedded tables and figure captions. These are proposed additions to the ten-review comparison, not claims of first-in-field novelty.

## N1. Causal comparison of alternative treatment benefits

**Question:** For a patient with given baseline characteristics, what difference in outcome is expected from choosing treatment A rather than treatment B?

Extract whether a review explicitly examines counterfactual treatment-outcome estimation, defines a treatment contrast and outcome horizon, and discusses adjustment for the factors influencing treatment assignment. Predicting what a surgeon chose, predicting recovery in operated patients, and forecasting who will eventually undergo surgery do not establish this dimension.

**Example:** Estimate the difference in expected 12-month functional improvement under surgery and conservative care, under stated causal assumptions.

**Possible fields:** treatment alternatives; outcome and horizon; target population; estimand; pretreatment adjustment variables; identification assumptions; estimator.

**Cross-paper finding:** No explicit methodological discussion of this comparison was found in the ten main articles. Han et al. uses “causality” in discussing legal responsibility, which is a different subject.

## N2. Empirical treatment support and a binding recommendation gate

**Question:** Do the data contain sufficiently comparable patients receiving each candidate treatment to support this particular comparison?

Extract whether the system assesses treatment positivity/common support and withholds a comparative recommendation when the alternative lacks empirical support. General external validation, prediction confidence, clinician supervision, and saying that a system has limitations do not constitute this gate.

**Example:** If essentially no patients with a given clinical profile received conservative treatment, flag the surgery-versus-conservative comparison as unsupported rather than confidently extrapolating it.

**Possible fields:** treatment-group overlap; propensity/support diagnostics; decision threshold; refusal action; explanation; unsupported recommendation rate.

**Cross-paper finding:** No explicit positivity/common-support assessment coupled to treatment recommendation gating was found in any of the ten articles.

## N3. Sensitivity of recommendations to unmeasured confounding

**Question:** How strongly would an unrecorded factor have to influence treatment selection and outcomes to overturn the estimated benefit or recommended option?

Extract whether a review discusses sensitivity analysis or bounds for unmeasured treatment-selection confounding. Broad dataset bias, demographic fairness, overfitting, and geographic dataset shift are different issues and already appear in the reviews.

**Example:** Assess whether an apparent advantage for surgery remains under plausible differences in unrecorded patient motivation or clinical severity.

**Possible fields:** omitted-factor assumptions; sensitivity parameter; effect bounds; treatment-rank reversal; robustness threshold.

**Cross-paper finding:** No explicit discussion of hidden-confounding sensitivity for comparative treatment recommendations was found in any of the ten articles.

## N4. Informative loss of follow-up outcomes

**Question:** Would the treatment comparison change if patients with unobserved follow-up outcomes systematically recovered differently from those who returned?

Extract whether a review examines outcome-dependent follow-up loss, missing-not-at-random assumptions, and sensitivity of treatment comparisons to those assumptions. Generic missing baseline values, missing data preprocessing, and a model's tolerance of incomplete inputs do not establish this dimension.

**Example:** Test how estimated improvement changes when patients who did not complete a 12-month PROM questionnaire are assumed to have worse or better outcomes than otherwise similar respondents.

**Possible fields:** follow-up observation mechanism; missingness by treatment; observed predictors of follow-up; assumptions; sensitivity scenarios; effect on comparative conclusions.

**Cross-paper finding:** No explicit discussion of this outcome-dependent follow-up mechanism and its consequences for treatment comparisons was found across the ten articles. Cochrane and Longo mention generic missing values; those mentions were checked and are not being presented as absent.

## N5. Treatment option sets that distinguish similarity from insufficient evidence

**Question:** Does the system distinguish clinically similar expected benefit from an imprecise or unsupported comparison, instead of always forcing a single winner?

Extract whether the review discusses returning a set of treatments using a prespecified clinical equivalence/indifference margin, with separate labels for similar benefit, insufficient precision, and unsupported comparison. General uncertainty reporting, listing management alternatives, or a nonsignificant study result is insufficient. A nonsignificant difference does not establish equivalence.

**Example:** Present two treatments as similarly beneficial only when the evidence supports similarity within the chosen clinical margin. Otherwise label the comparison inconclusive or unsupported.

**Possible fields:** eligible treatments; clinical margin; effect scale/horizon; interval/posterior criterion; support status; returned set; reason for retaining multiple options.

**Cross-paper finding:** No explicit discussion of this distinction or such treatment-option-set criteria was found in the ten articles.

## Cross-paper verification matrix

**ND = no explicit discussion of the precisely defined dimension found in the checked main article.** ND is a scoped reading judgment, not proof of universal absence or field-wide novelty.

| Review | N1: causal benefit | N2: support gate | N3: hidden confounding | N4: informative follow-up loss | N5: similarity/inconclusiveness sets |
|---|---|---|---|---|---|
| R1 — Cochrane 2026 | ND | ND | ND | ND | ND |
| R2 — Longo 2024 | ND | ND | ND | ND | ND |
| R3 — Russell 2025 | ND | ND | ND | ND | ND |
| R4 — Glinkowski 2026 | ND | ND | ND | ND | ND |
| R5 — Kim 2026 | ND | ND | ND | ND | ND |
| R6 — Oettl 2025, musculoskeletal surgery | ND | ND | ND | ND | ND |
| R7 — Giorgino 2023 | ND | ND | ND | ND | ND |
| R8 — Oettl online 2025/issue 2026, generative AI | ND | ND | ND | ND | ND |
| R9 — Han 2025 | ND | ND | ND | ND | ND |
| R10 — Farhadi 2022 | ND | ND | ND | ND | ND |

## Closest existing discussions checked

| Review | Already-covered subjects that must not be mistaken for the five additions |
|---|---|
| R1 | Personalized predictions, matching, Markov models, generic missing-value handling, patient preferences, and decision-aid outcome measures. Its nonsignificant implementation result is not a treatment-equivalence framework. |
| R2 | Postoperative prediction, progression to surgery, model validation, and handling missing input values. These do not provide causal contrasts, treatment-support gates, or informative-outcome-loss analyses. |
| R3 | Surgeon agreement, management alternatives, confidence errors, incomplete EHRs, and demographic bias. No formal equivalence/indifference decision rule is discussed. |
| R4 | Risk/PROM prediction, predictive uncertainty, fairness, external validation, and digital twins. Predictive reliability alone does not establish causal identification or treatment support. |
| R5 | Calibration, uncertainty, generalization, retrieval, lifecycle monitoring, and handoff quality. These covered topics are excluded from the shared additions. |
| R6 | Outcome prediction, agents, safety, explainability, monitoring, and oversight. No formal causal support gate or clinically defined treatment-equivalence set is discussed. |
| R7 | Treatment suggestions, evidence checking, hallucinations, model limitations, and supervision. These do not provide the five defined comparative-treatment methods. |
| R8 | Generative planning, agents, shared decisions, validation, and adaptive rehabilitation. These do not establish counterfactual treatment identification or a clinical-equivalence decision framework. |
| R9 | Surgical optimization, reinforcement learning, Bayesian predictive uncertainty, multimodal models, and legal causality. Their presence is not treated as discussion of causal comparative-benefit methodology. |
| R10 | Prognosis, PROM/MCID prediction, presenting alternatives, validation, and monitoring. Predicting meaningful improvement after one intervention is different from identifying its advantage over another. |

## Why these are five distinct axes

N1 defines **what comparative benefit is estimated**. N2 examines **whether both alternatives have empirical support**. N3 examines **robustness to unrecorded treatment-selection factors**. N4 examines **bias from selectively observed outcomes**. N5 defines **how similar, uncertain, or unsupported options are communicated**. They are related parts of a treatment-support system, but have separate extraction questions and evaluation criteria.

## Evidence and limits

The [verification audit](verification_audit.md) searches the same five concepts in every article, records contextual matches, and preserves source hashes and checked-text paths. Search matches were interpreted in context; neither a zero keyword count nor a generic related word alone decides coverage.

Separately hosted supplements and all cited primary studies were not exhaustively audited. These dimensions draw on established causal inference, missing-data, and decision-analysis concepts. The wider project already contains related methodological literature; do not describe these as five inventions or as absent from every orthopedic review.

The separate [broader-library candidate document](../../new_dimensions.md) concerns a different evidence set and remains distinct from this ten-paper comparison.
