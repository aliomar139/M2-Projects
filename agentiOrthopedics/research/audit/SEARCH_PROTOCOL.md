# Search protocol and execution record

Version 0.1, 23 October 2026. This working protocol was written during a corrective audit after exploratory searches had already begun. It is not a prospectively registered protocol. Changes in scope or criteria must be dated in this file.

## Questions and review design

The review maps how orthopedic decision-support research connects patient information to a treatment decision and to evidence of comparative patient benefit. A scoping review with structured methodological appraisal fits this broad question; use [PRISMA-ScR](https://www.prisma-statement.org/scoping) for reporting, the [PRISMA 2020 flow templates](https://www.prisma-statement.org/prisma-2020-flow-diagram) for selection accounting, and [PRISMA-S](https://www.prisma-statement.org/prisma-search) for search reporting. PRISMA is a reporting guideline; a flow diagram alone does not make a review systematic.

Two evidence streams must remain distinguishable:

- **Orthopedic evidence:** patient-specific treatment decision support, outcome prediction used for a treatment decision, comparative treatment effects or treatment-policy learning. Pure image classification belongs only where it materially informs the decision pathway.
- **Methodological context:** transferable causal inference, personalized policies, evidence retrieval and agent orchestration from other specialties. Contextual papers do not enter orthopedic prevalence denominators.

Existing reviews are comparators for novelty. Do not pool them with their primary studies as independent patient evidence.

## Working eligibility criteria

Include orthopedic or musculoskeletal human-health studies with an explicit patient-specific treatment-decision purpose, a defined model/framework/tool, and a relevant decision or patient outcome. Include simulations and conceptual frameworks in separately labeled evidence categories; they cannot establish clinical efficacy. Include cross-domain methodological studies only where a named component transfers to the thesis. Retain relevant systematic/scoping reviews in the review-comparison table.

Exclude from the primary orthopedic evidence stream unrelated specialties without a methodological rationale, administrative prediction with no treatment link, diagnosis-only benchmarks without a decision connection, nonresearch promotional material, and duplicate reports of the same study. Mark abstracts, protocols, preprints and missing full text separately rather than treating them as completed peer-reviewed evidence. No language restriction was applied to the searches; non-English records require a language-capable assessment before a final decision.

Use inception through **2026-10-23** as the working publication cutoff. For online-first papers, check the first public publication date and retain the later issue date separately. These eligibility rules still require calibration against sample records; no final candidate exclusions have been claimed.

## Executed PubMed searches

Database/platform: PubMed through NCBI E-utilities. Execution date: 2026-10-23. No language filter. Maximum export: 1,000 PMIDs per query, which exceeded the observed hit count in every query. All returned PMIDs were exported. EFetch XML contains source titles, authors, abstracts and publication types. Database indexing and future updates may change later rerun counts.

The exact full strings and request URLs are in [pubmed_search_log.csv](../../data/audit/pubmed_search_log.csv); the executable definitions are in [search_pubmed.py](../../scripts/corpus/search_pubmed.py), and unmodified responses are under [data/searches/first_pass](../../data/searches/first_pass/).

The shared orthopedic block is:

```text
(orthop*[Title/Abstract] OR arthroplast*[Title/Abstract] OR osteoarthritis[Title/Abstract] OR "musculoskeletal"[Title/Abstract])
```

Each query appends the exact publication-date restriction:

```text
("1800/01/01"[Date - Publication] : "2026/10/23"[Date - Publication])
```

| ID | Additional concepts | Hits / exported |
|---|---|---:|
| P1 | Decision support, treatment selection/recommendation; reviews or surveys | 216 / 216 |
| P2 | Causal inference/ML or individualized treatment; reviews or surveys | 151 / 151 |
| P3 | Agentic, multi-agent or AI agents; clinical/medicine/healthcare; reviews or surveys | 435 / 435 |
| P4 | Orthopedic causal forest, doubly robust, individualized/heterogeneous treatment effect or optimal treatment regime | 12 / 12 |

Total occurrences: 814. Unique PMIDs: 803. Repeated occurrences across searches: 11. Saved candidates retain every contributing search ID. DOI extraction uses the article's own `PubmedData/ArticleIdList`, excluding identifiers in its reference list.

These are targeted correction/novelty searches, not a sufficiently sensitive final search for every orthopedic AI application. The current free-text blocks can miss anatomical subspecialty names, MeSH-only indexing and different terminology. Before claiming an exhaustive review, expand controlled vocabulary and anatomy/treatment synonyms, test known relevant papers against each strategy, and document the amendments and additional yields. A librarian's PRESS review would strengthen this stage.

## Other searches and access

Supplementary web discovery used topic queries and exact titles, then consulted PubMed, publisher pages, official PRISMA material and journal/society sources. Results from general web search are discovery leads and cannot be relabeled as complete database exports. Selected exact queries included:

```text
orthopaedic treatment decision support artificial intelligence systematic review individualized treatment causal review
agentic AI orthopaedic systematic review multi agent clinical decision support
orthopedic clinical decision support knee osteoarthritis scoping review Cochrane 2026
orthopaedics artificial intelligence systematic review treatment recommendation causal inference
"Clinical Decision Support Tools for Predicting Outcomes in Patients Undergoing Total Knee Arthroplasty" systematic review
"AI Agents in Clinical Medicine" systematic review journal 2025
"Artificial intelligence fails to outperform orthopaedic surgeons" systematic review
"Machine-learning-based patient-specific prediction models for knee osteoarthritis" Jamshidi
"Meng" "2020" "near-optimal" treatment JMLR
"van der Weegen" "history-taking" artificial intelligence hip 2024
```

Google Scholar was attempted at `https://scholar.google.com/scholar?q=orthopedic+treatment+recommendation+systematic+review`; the tool could not access it. No Scholar yield, search completion or citation-chain screening is claimed. PubMed's browser search page also failed, so E-utilities supplied the executed searches instead. Direct shell network access initially failed inside the sandbox; permitted external API calls subsequently succeeded. An oversized EFetch URL failed and was replaced with batches of 100; final exports are complete for the four stated queries.

Embase, Scopus, Web of Science, CINAHL and IEEE Xplore have not been searched directly in this run. Do not insert zero records for these sources. Proposed extensions include orthopedic treatment-selection searches in Embase/Scopus and agent architecture searches in IEEE Xplore/ACM; adapt the syntax to each actual platform and record the executed query, date, yield and export before adding it to the flow diagram.

## Selection and data handling

Deduplicate by PMID, then normalized DOI, with title/year/author inspection for unresolved identities and related reports. Keep record-level and study-level identifiers distinct. Reconcile the 803 new candidates with the legacy 100 only after this step; do not add the totals blindly.

Pilot title/abstract criteria on a sample, record include/exclude/uncertain and one primary exclusion reason per excluded record, then assess full texts. Maintain a decision log and preserve source versions. A single assistant's assessment is not two independent reviewers; record the actual reviewer arrangement and adjudication. Do not invent independent assessment or registration.

Appraise prediction studies with an applicable prediction-model risk-of-bias framework, causal observational comparisons with an appropriate intervention framework, randomized studies with the applicable randomized-trial framework, and reviews with a review-specific appraisal. Verify the current tool version and scope before assigning ratings. A reporting checklist and a risk-of-bias tool answer different questions. No formal tool ratings have been assigned in this package.
