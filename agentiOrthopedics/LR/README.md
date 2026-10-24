# Literature review deliverables for 24 October 2026

Prepared 23 October 2026. This folder follows the professor's requested names and adds source records, search logs and a clear status for unfinished evidence checks.

| Professor's task | Deliverable | Current status |
|---|---|---|
| Find and collect domain reviews | [Surveys](Surveys/README.md) | Expanded search; 85 working records, 57 with original main text; 28 originals still needed. Exhaustive identification and final eligibility are not complete |
| List dimensions per paper | [Surveys/dimensions.md](Surveys/dimensions.md) | All 85 records represented across 41 dimensions; eleven focused original-source checks; evidence levels distinguish confirmed fields, automated candidates and unknowns |
| Propose at least five new dimensions | [new_dimensions.md](new_dimensions.md) | Seven operational proposals with prior-work overlap, evaluation criteria and search checks; universal novelty not established |
| Apply PRISMA with a diagram | [prisma.md](prisma.md), [figure](prisma.png) | Search arithmetic reconciled; screening, eligibility and final inclusion explicitly pending |
| Abstract and introduction in `paper` | [paper.md](paper.md) | Student writing worksheet only, following the instruction that AI must not write these sections |

## Main enhancements over the earlier package

Three additional PubMed searches yielded 1,196 record occurrences and 1,189 distinct PMIDs. After reconciling the 153-PMID overlap with the earlier 803-record pool, there are 1,839 distinct search-derived PMIDs. The saved exports permit query and count verification.

The survey library adds several close competitors absent from the first seven-review comparison. In particular, an arthroplasty evidence map already examines frozen versus redeveloped models, calibration, uncertainty and workflow benefit; KOA LLM and spine-treatment reviews also cover important proposed themes. The new-dimension proposals account for that overlap.

Original sources are copied under `Surveys/sources/` while citation records, abstract-only entries and missing-text requests remain identifiable. Generated legacy summary PDFs and known wrong PDFs are not presented as original review articles. Source XML has been checked against the main article's DOI. Readable HTML views preserve available article text and tables, but figures/layout/references may be incomplete in those convenience views.

## Evidence and reproducibility

- [review_search_log.csv](../data/reviews/review_search_log.csv): exact new queries, date, platform, filters and yields.
- [review_search_candidates.csv](../data/reviews/review_search_candidates.csv): every record returned by the three added searches.
- [pubmed_source_records.csv](../data/reviews/pubmed_source_records.csv): merged native PubMed metadata and abstracts.
- [review_triage.csv](../data/reviews/review_triage.csv): rules-assisted navigation; final eligibility remains pending.
- [novelty_search_log.csv](../data/reviews/novelty_search_log.csv): seven targeted checks; zero hits do not prove novelty.
- [Surveys/survey_registry.csv](Surveys/survey_registry.csv): stable paper IDs, publication categories, source status and file paths.
- [Surveys/dimensions.csv](Surveys/dimensions.csv): dimension-level evidence status and source locators.
- [Surveys/dimension_coverage.csv](Surveys/dimension_coverage.csv): one row per paper for comparison.
- [Surveys/retrieval_queue.csv](Surveys/retrieval_queue.csv): missing original main texts.

Raw search exports are under [data/searches](../data/searches/), and the research utilities are under [scripts/surveys](../scripts/README.md). The previous [corrective audit package](../research/audit/README.md) remains available. Its historical numbers should not be overwritten with the new search numbers; they describe different stages.

The assignment asks for all reviews and at least five never-studied dimensions. This package expands coverage and makes the requested deliverables concrete, but does not misrepresent an incomplete search or a candidate idea as proof of either claim. No submission abstract or introduction has been generated here.
