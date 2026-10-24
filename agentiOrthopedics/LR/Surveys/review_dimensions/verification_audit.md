# Full-text verification audit

Date: 24 October 2026. Corrected scope: 10 reviews, 100 covered dimensions, FIVE shared proposed additions. The same five concepts are checked in every review, giving 50 paper-by-dimension coverage checks, not 50 new dimensions.

## What this audit establishes

The searches below support the conceptual reading recorded in Five_Shared_New_Dimensions.md. They do not independently prove absence. Nonzero hits require context review; zero hits do not rule out synonyms or implicit coverage. The shared report's nearest-topic explanation is the interpretation of those checks.

Search scope: main article body, embedded tables, and available figure captions. Bibliographies and separately hosted supplements are excluded. R6 was checked against full PMC HTML as well as its repository rendering. Extracted PDF page numbers, where present, are file page numbers rather than journal pagination.

Publisher/PMC metadata and review labels were checked online. Nine reviews also have downloaded Europe PMC JATS XML; R6's Europe PMC XML endpoint returned an error, so the complete PMC HTML and local body were used.

Search expressions are case-insensitive and normalized for whitespace/ligatures. Context excerpts are short audit aids, not a substitute for the source.

## Important rejected absence claims

- R1: nonsurgical alternatives, psychosocial outcomes, cost, and generic value of information already appear. Its value-of-information wording concerns decision-aid evaluation, not mathematical next-test selection; the latter was nevertheless not assigned as a new R1 dimension.
- R5: retrieval grounding, prompt injection, lifecycle monitoring, and preferences in clinical notes already appear.
- R8: adaptive rehabilitation and cost-effectiveness already appear.
- R9: multiobjective surgical optimization and Bayesian uncertainty already appear. Legal causality is not causal treatment-effect identification.
- Generic agent handoff quality is explicitly discussed in R5 and is excluded from the five shared additions.
- R1 and R2 mention generic missing values. These mentions do not discuss outcome-dependent follow-up loss. R1 also reports a nonsignificant study result, which is not a clinical-equivalence treatment-set criterion.

## R1

Source extraction: [full text](sources/PMC12816537.body.txt).
SHA-256 of extraction: `fffcb848ba69556545da632159b3c241d69a3c6b2828880449506cfbbd024f07`.
Checked main-text length: 46,572 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 1; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 1 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 1 |

Nonzero-match context notes (interpret alongside the report):

- `overlap\w*` occurs; example: "oid repeating text, overlapping colours resemble two or". A related word is not automatically the proposed capability.
- `missing\w*` occurs; example: "(i.e. dealing with missing values), model development and". A related word is not automatically the proposed capability.
- `non.?significan\w*` occurs; example: "al function scores (non-significant), decision readiness, decisional conflict,". A related word is not automatically the proposed capability.

## R2

Source extraction: [full text](sources/PMC11265144.body.txt).
SHA-256 of extraction: `6cc423fbf5f5bace817511b2b67c0b3a47de1b4676b9ccc801c5a3a41f9bc2c5`.
Checked main-text length: 65,071 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 1 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- `missing\w*` occurs; example: "ixed data types and missing values. gbm works". A related word is not automatically the proposed capability.

## R3

Source extraction: [full text](sources/PMC12616488.body.txt).
SHA-256 of extraction: `16e5a1480b4ed8626270bdd4d3c8fd73ff3dfbc0b051010896234c81f0e8488f`.
Checked main-text length: 19,711 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.

## R4

Source extraction: [full text](sources/PMC12985454.body.txt).
SHA-256 of extraction: `f38b64a37a84206f52b833e41773b340acd526710766cc06f39f5049183bcd7c`.
Checked main-text length: 39,384 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 1 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- `missing\w*` occurs; example: "ghts that are often missing from clinical reviews.". A related word is not automatically the proposed capability.

## R5

Source extraction: [full text](sources/PMC13047823.body.txt).
SHA-256 of extraction: `962b7154890e7ffdf7bae4ca27a16ee55514e042b10658548224040a433873df`.
Checked main-text length: 34,171 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.

## R6

Source extraction: [full text](sources/002.txt).
SHA-256 of extraction: `4a73a1ca430b92556248139ed98a5137b0ca2558f1340e86882c089439f3caca`.
Checked main-text length: 24,852 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.

## R7

Source extraction: [full text](sources/PMC10654618.body.txt).
SHA-256 of extraction: `399fbaee9862cae83fe9b265e3a73af93cda2fbecc33a1ebf64f94f9a0a391f7`.
Checked main-text length: 25,999 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.

## R8

Source extraction: [full text](sources/PMC12747601.body.txt).
SHA-256 of extraction: `e4382870bcdb303bc029b008e55e33f88b8889f1167fa6913b6b5091d72509c0`.
Checked main-text length: 20,402 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.

## R9

Source extraction: [full text](sources/Han_2025.body.txt).
SHA-256 of extraction: `e01e83248084c541f69cdfe39315ed45d28acc3bbd16f42bf99364225e9d6fc1`.
Checked main-text length: 89,324 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 1; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- `causal\w*` occurs; example: "the multifactorial causality in technologically mediated care. the". A related word is not automatically the proposed capability.

## R10

Source extraction: [full text](sources/PMC9797865.body.txt).
SHA-256 of extraction: `bd56cc0eeca72557737648f6058f0bc3dba1c3e4e52c3d7044a2925c0e39affd`.
Checked main-text length: 47,362 characters.

| Proposal | Concept searches | Main-text matches |
|---|---|---|
| N1 | causal | causal\w*: 0; counterfactual\w*: 0; propensity: 0; confound\w*: 0; doubly robust: 0; treatment effects?: 0 |
| N2 | support | positivity: 0; common support: 0; propensity: 0; treatment overlap: 0; overlap\w*: 0; identifiab\w*: 0; abstain\w*: 0; abstention: 0 |
| N3 | confounding | hidden confound\w*: 0; unmeasured confound\w*: 0; unobserved confound\w*: 0; sensitivity analys\w*: 0; confound\w*: 0 |
| N4 | dropout | missing not at random: 0; mnar: 0; informative missing\w*: 0; drop.?out: 0; loss to follow: 0; lost to follow: 0; missing\w*: 0 |
| N5 | sets | conformal: 0; prediction sets?: 0; treatment sets?: 0; near.?optimal: 0; multiple optimal: 0; statistical coverage: 0; equivalen\w*: 0; indifference: 0; non.?significan\w*: 0 |

Nonzero-match context notes (interpret alongside the report):

- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.
