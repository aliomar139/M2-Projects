# Repository evidence audit

Date: 23 October 2026. Scope: the root review and progress tracker, the 100-record manifest, every local PDF, existing audit CSV, archived search exports, Crossref records and available original article XML.

## Findings that change the current review

The statement that all 100 papers have verified full text is unsupported. File existence was confused with article identity. Text extraction and inspection found:

| Document class | Count | Meaning |
|---|---:|---|
| Candidate matching article text | 58 | Includes publisher layouts and author/preprint versions; critical appraisal remains separate |
| Locally generated summary | 38 | Contains corpus branding, metadata and summaries; cannot replace the article |
| Confirmed wrong document | 3 | Ranks 22, 44 and 61 |
| Supplement only | 1 | Rank 29; main article XML recovered separately |

The first automated count found 36 summaries. Whitespace normalization exposed two additional summaries, ranks 4 and 51, whose branding spans lines. The final audit count is 38.

- Rank 22 is a CMS joint-replacement quality-measure document rather than the Fontana paper named in the manifest.
- Rank 44 is *The WEKA Workbench*, rather than the Jamshidi knee osteoarthritis article.
- Rank 61 contains Liu et al., DOI `10.1002/sim.9491`, which is the intended paper at rank 86. The two files have the same SHA-256 hash, although their manifest DOIs differ.
- Rank 29 contains supporting information. Its original main text is retained in [data/audit/fulltext_xml/029.xml](../../data/audit/fulltext_xml/029.xml) with a matching DOI.

These classifications concern the supplied files. A wrong file does not mean the cited paper is invalid or ineligible.

## Metadata and provenance

Crossref supplied records for 96 of the 99 manifest DOIs. Ranks 21 and 65 use arXiv identifiers and require preprint-specific verification; rank 49 was unavailable from Crossref in this run. Rank 100 has no DOI. A Crossref `journal-article` type establishes deposited metadata, not peer-review quality or lack of retraction. Preprints, conference papers, abstracts and protocols require their own publication-status categories.

Both first-online and issue dates are retained. Examples include Woo et al. (online 2024; issue 2025), Cochrane et al. (online 2020; issue 2021), and Lee et al.'s HCC study (2024 publication despite the 2023 DOI suffix). A DOI suffix is not a publication date. Do not force a single year convention without declaring it.

The archived exports contain 117 and 96 rows, for 213 occurrences. Exact DOI matching, with normalized-title fallback for missing DOIs, yields 186 keys and 27 repeat occurrences. Every current manifest record links to at least one archived row. This reconstructs export lineage; it does not establish the original database search counts, search strings, exclusion reasons or selection procedure. The 86 export keys outside the selected 100 have no documented exclusion decisions in the inspected files.

## Corrections supported by original text

| Existing review claim | Source check | Required correction |
|---|---|---|
| Russell review is a meta-analysis of 43 studies | Rank 7, PDF pp. 1-3: 16 eligible studies; task-based synthesis | Correct study count and synthesis type |
| Stetter uses XGBoost and an AUROC over 0.82 as its main result | Rank 20, PDF pp. 1 and 4: k-means, SVM, SHAP and waveform analyses | Describe actual model and target; do not reuse the unverified benchmark |
| Truhn uses 100 MRI reports and three surgeons | Rank 50, PDF p. 1: 20 reports and two surgeons | Correct population and assessment design |
| Zmudzki pilot has N=312 and 79.5% accuracy | Rank 75, PDF pp. 1-2: 17 new patients; 14/17 clinician-profile consistency | Correct sample size and metric; published 2025 |
| PAI paper is Hu et al., Translational Behavioral Medicine, N=180, d=0.51 | Rank 79, PDF pp. 1-2: DeRubeis et al., PLOS ONE, 2014; N=154; d=0.58 in the specified subgroup | Replace citation and restrict effect-size interpretation to the reported subgroup |
| DeepSurv is a 2016 journal paper | Rank 78, PDF p. 1 and deposited metadata: BMC Medical Research Methodology, 2018 | Use the journal citation; distinguish any earlier version |
| Clinician-advice experiment is Benrimoh et al., N=142 | Rank 80, PDF p. 1: Jacobs et al.; 220 clinicians | Correct attribution and sample |
| Rank 97 is Lee et al., four European centers, N=1850, external-center deterioration | Rank 97, PDF pp. 1-2 and 9: Yang et al., 2025, one Chinese institution, N=210, external validation lacking | Remove the invented multicenter comparison |

Further corrections may emerge from the remaining extractions. This table is not an exhaustive erratum.

## Claims that cannot currently be reproduced

The 78/22 domain split, 24% imitation fraction, fewer-than-4% treatment-effect fraction, calibration/DCA percentages, geographic-validation percentages and claim of zero prospective orthopedic multi-agent trials lack a reproducible study-level coding table in the inspected repository. Suspend these numerical claims until the corrected corpus has defined eligibility, denominators, coding rules and reviewer adjudication. Do not generalize proportions from this curated collection to the entire field.

The previous statement that causal forests or doubly robust learners are mandatory is too strong. Credible causal questions require identification assumptions and an appropriate design; several estimators or randomized designs can serve that purpose. A model family alone does not establish causality. Likewise, poor prognosis after surgery does not establish that conservative care would produce a better outcome.

## Repair order

1. Keep the original files, but flag the review's current verification and quantitative synthesis claims.
2. Retrieve original texts for the 41 queued records and resolve their identities.
3. Screen the new search candidates and reconcile overlap with the legacy corpus by DOI and PMID.
4. Complete extraction, appraisal and independent checks before recalculating synthesis statistics or writing a final abstract.

Reproducibility: `audit_corpus.py` builds the file audit; `verify_sources.py` saves metadata and open XML; `build_review_tables.py` builds lineage and the extraction matrix. API retrieval logs and saved responses permit inspection without repeating network calls. No author, sample size or missing method is silently filled from a generated summary.
