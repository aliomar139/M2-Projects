# Research utilities

Run commands from the repository root. The folder layout is shared through `repo_paths.py`; it resolves earlier paths and consolidated source copies using `data/source_aliases.json`.

## Rebuild existing deliverables

```powershell
python scripts/surveys/extract_dimensions.py
python scripts/surveys/build_prisma.py
python scripts/surveys/build_survey_index.py
```

These commands use existing local inputs. Dimension extraction still distinguishes checked fields from machine-mapped candidates. It regenerates PDF text under `data/reviews/pdf_text/`, which is disposable and ignored by Git.

## Search and source retrieval

| Utility | Purpose |
|---|---|
| `surveys/collect_surveys.py` | Run/cache the review queries and assemble native PubMed records |
| `surveys/build_survey_library.py` | Assemble the working library and recover available original XML |
| `surveys/recover_survey_pdfs.py` | Try official publisher PDFs with DOI identity checks |
| `surveys/check_novelty.py` | Run/cache the seven terminology checks |
| `corpus/audit_corpus.py` | Inspect the original 100 logical source records, including archived summary/wrong files |
| `corpus/verify_sources.py` | Retrieve Crossref and available original article metadata/text |
| `corpus/search_pubmed.py` | Run/cache the first-pass queries |
| `corpus/retrieve_additions.py` | Retrieve selected anchor records and available XML |
| `corpus/build_review_tables.py` | Build the initial audit's extraction/lineage tables |

Search utilities require network access. Their original 23 October cutoff is preserved; explicitly version the protocol and exports before changing that cutoff. Do not rerun a search and silently describe it as the earlier search.

`maintenance/` contains the one-time migration and validation utilities. The migration refuses to run again after its completed log exists. It is not a routine research step.
