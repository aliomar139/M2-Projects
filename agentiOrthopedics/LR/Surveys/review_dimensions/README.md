# Review-dimension comparison

Start with [the complete report](10_Review_Papers_Dimension_Analysis.md).

It contains ten orthopedic review papers, ten discussed dimensions per paper, and **five shared additions across all ten reviews**. The same five definitions must be absent from every checked article. See [the five shared dimensions and verification matrix](Five_Shared_New_Dimensions.md). No claim of field-wide novelty is made.

[The verification audit](verification_audit.md) records full-text sources, hashes, search expressions, contextual checks, and report-completeness validation.

## Source files

| Report ID | Main source | Existing corpus rank |
|---|---|---|
| R1 | `sources/PMC12816537.xml` | 35 |
| R2 | `sources/PMC11265144.xml` | 38 |
| R3 | `sources/PMC12616488.xml` | 7 |
| R4 | `sources/PMC12985454.xml` | 15 |
| R5 | `sources/PMC13047823.xml` | 32 |
| R6 | Full [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12092413/) and `sources/002.txt` | 2 |
| R7 | `sources/PMC10654618.xml` | 8 |
| R8 | `sources/PMC12747601.xml` | 49 |
| R9 | `sources/Han_2025.xml` | Additional review |
| R10 | `sources/PMC9797865.xml`; `sources/Farhadi_2022.pdf` | Additional review |

XML files are complete open-access JATS records downloaded through the Europe PMC full-text API. `*.body.txt` files are readable extractions. `R*_checked_main_text.txt` files identify the exact main text searched by the audit, excluding bibliographies and supplementary stubs. R6's local rendering was corroborated against PMC; repository-added commentary was excluded.

Numbered text files are extractions of existing local PDFs used during selection. Some candidates were rejected because they contained only rendered abstracts/metadata. They are retained as screening evidence and are not part of the final ten-review analysis unless listed above.

## Reproduce the audit

Run `build_verification_audit.py` using a Python 3 interpreter. It uses only the Python standard library, validates 100 covered dimensions, five shared definitions, identical N1-N5 entries in all ten notes, and the 10-by-5 coverage matrix, and rebuilds the audit and checked-main-text extracts from the saved sources. The script does not independently decide semantic novelty.

Scope limitation: separately hosted supplements and the full texts of every cited primary study were not exhaustively checked. The proposals are review-relative gaps, not proof that nobody has investigated them.

## Individual notes and matching library records

Organized together on 24 October 2026. Eight papers overlap by DOI with the 85-record library. Han and Farhadi remain additional papers in this ten-review package; the library registry and its counts have not been changed.

| Paper | 10 covered dimensions + the shared five | Existing library record |
|---|---|---|
| 01 Cochrane 2026 Knee Osteoarthritis Decision Support | [Paper notes](<../review papers/01_Cochrane_2026_Knee_Osteoarthritis_Decision_Support.md>) | [Library record](../records/PMID_41568289.md) |
| 02 Longo 2024 Knee Arthroplasty AI | [Paper notes](<../review papers/02_Longo_2024_Knee_Arthroplasty_AI.md>) | [Library record](../records/PMID_39034416.md) |
| 03 Russell 2025 AI Compared With Orthopaedic Surgeons | [Paper notes](<../review papers/03_Russell_2025_AI_Compared_With_Orthopaedic_Surgeons.md>) | [Library record](../records/PMID_41245704.md) |
| 04 Glinkowski 2026 Orthopaedic AI Clinical Readiness | [Paper notes](<../review papers/04_Glinkowski_2026_Orthopaedic_AI_Clinical_Readiness.md>) | [Library record](../records/PMID_41827166.md) |
| 05 Kim 2026 Orthopedic AI Applications and Challenges | [Paper notes](<../review papers/05_Kim_2026_Orthopedic_AI_Applications_and_Challenges.md>) | [Library record](../records/PMID_41933417.md) |
| 06 Oettl 2025 Musculoskeletal Surgical AI | [Paper notes](<../review papers/06_Oettl_2025_Musculoskeletal_Surgical_AI.md>) | [Library record](../records/PMID_40405922.md) |
| 07 Giorgino 2023 ChatGPT in Orthopedics | [Paper notes](<../review papers/07_Giorgino_2023_ChatGPT_in_Orthopedics.md>) | [Library record](../records/PMID_38026475.md) |
| 08 Oettl 2025 2026 Generative AI in Orthopaedics | [Paper notes](<../review papers/08_Oettl_2025_2026_Generative_AI_in_Orthopaedics.md>) | [Library record](../records/PMID_41144723.md) |
| 09 Han 2025 AI in Orthopedic Surgery | [Paper notes](<../review papers/09_Han_2025_AI_in_Orthopedic_Surgery.md>) | Additional paper; outside the 85-record registry |
| 10 Farhadi 2022 AI Applications in Orthopaedic Surgery | [Paper notes](<../review papers/10_Farhadi_2022_AI_Applications_in_Orthopaedic_Surgery.md>) | Additional paper; outside the 85-record registry |

The full-text availability judgments in this package and the broader registry were made separately. For example, Oettl 2025 has a verified PMC reading in this package while the broader registry still marks its original file as needed. This organization does not silently change either evidence assessment.
