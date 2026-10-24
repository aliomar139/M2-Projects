# Professor-directed literature review revision

> **Later enhancement:** The [24 October task package](../../LR/README.md) adds review searches, original-source recoveries, per-paper dimensions, candidate new dimensions and an updated PRISMA figure. Counts below describe this earlier audit pass; consult `LR/` for the current survey-library status.

> **Repository layout, 24 October:** This folder contains the readable audit notes. Supporting tables and source evidence now live in [data/audit](../../data/audit/); scripts live in [scripts/corpus](../../scripts/README.md). The [current corpus catalog](../../papers/corpus/README.md) incorporates later source recoveries and consolidated file locations.

Audit and search date: **23 October 2026**. This package implements the repository audit and starts a prospective, reproducible review. It is **not a completed systematic review**.

The existing collection needs correction before its conclusions can support a thesis. Of 100 PDFs, 38 are locally generated summaries, three contain the wrong document, one contains supplementary material only, and 58 are candidate matching article texts. Open article XML was retrieved for 53 records, including the main text missing from the supplement-only record. Thus 59 corpus records currently have candidate matching main text in this package or the original collection; 41 need original-text retrieval.

Four prospective PubMed searches returned 814 records and 803 distinct PMIDs. The 11 repeat occurrences were removed by PMID. These are search candidates awaiting eligibility screening. The corpus matrix has 100 rows, with focused assistant second-pass notes for 18 papers. No independent second reviewer has assessed these notes.

## Read these first

| File | Purpose |
|---|---|
| [AUDIT_REPORT.md](AUDIT_REPORT.md) | Evidence problems, citation corrections and priorities |
| [SEARCH_PROTOCOL.md](SEARCH_PROTOCOL.md) | Scope, eligibility, exact search definitions and access limitations |
| [PRISMA_RECORD.md](PRISMA_RECORD.md) | Known counts, unknown historical counts and draft flow diagrams |
| [CLOSEST_REVIEWS.md](CLOSEST_REVIEWS.md) | Comparison against the strongest overlapping reviews |
| [THESIS_CONTRIBUTION.md](THESIS_CONTRIBUTION.md) | A narrower contribution and an evaluation plan |
| [SECOND_PASS_NOTES.md](SECOND_PASS_NOTES.md) | Extraction rules, focused findings and remaining work |

## Evidence tables

- [second_pass_matrix.csv](../../data/audit/second_pass_matrix.csv): all 100 citations, source status and checked/provisional extraction fields.
- [corpus_audit.csv](../../data/audit/corpus_audit.csv): file identity, document class, DOI checks and SHA-256 hashes.
- [source_verification.csv](../../data/audit/source_verification.csv): 96 retrieved Crossref records, three unavailable Crossref records and one missing DOI; separate publication dates and XML identities.
- [fulltext_retrieval_queue.csv](../../data/audit/fulltext_retrieval_queue.csv): 41 records requiring original main text.
- [pubmed_search_log.csv](../../data/audit/pubmed_search_log.csv): exact executed searches, dates, counts and API URLs.
- [new_pubmed_candidates.csv](../../data/audit/new_pubmed_candidates.csv): 803 unique candidate records, abstracts and pending decisions.
- [archive_lineage.csv](../../data/audit/archive_lineage.csv): 213 archived export rows linked back to the current manifest.
- [additional_source_registry.csv](../../data/audit/additional_source_registry.csv): source records for missing anchors, close reviews and competing primary studies.
- [source_passage_candidates.csv](../../data/audit/source_passage_candidates.csv): automatically located passages for 59 source texts. These are navigation aids, not validated extraction fields.

`data/audit/source_metadata/`, `data/audit/fulltext_xml/`, `data/audit/additional_sources/`, `data/searches/first_pass/` and `data/audit/page_text/` retain evidence for auditing. Exact duplicate sources resolve through `data/source_aliases.json`. Do not equate downloaded XML or an automatically located passage with completed critical appraisal. Unique originals and earlier workbooks are preserved.

## Remaining work

Complete candidate screening against the protocol, retrieve the remaining original texts, finish extraction and study-design-specific appraisal, and obtain an independent reviewer check. Google Scholar access failed in this session; Embase, Scopus and Web of Science searches have not been executed. Historical database counts cannot be recovered from the supplied exports alone. Journal metrics remain incomplete and must not substitute for article-level quality assessment.
