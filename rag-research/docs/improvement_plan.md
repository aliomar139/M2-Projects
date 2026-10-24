# Improvement Plan: Cascaded Blended RAG

## Starting point

Start with evaluation validity and provenance. The executed Kaggle notebook is important evidence and should be preserved, but its cascade cells currently simulate routing after computing all three retrievers for every query. The reported NQ stage latencies are hard-coded constants. The notebook also constructs its 15,119-document pool by including all documents judged relevant to the selected 500 evaluation queries. These choices make the current results useful for exploration, but not a valid measurement of live neural-call savings or a clean full-corpus held-out result.

The SciFact experiment has related issues: the CV script routes from `bm25_single_cache.json`, although the project describes Best Fields BM25; the static baseline is aggregated across all queries while the cascade is averaged over held-out folds; and latency is reconstructed from cached component timings. These need to be reconciled before revising paper claims.

## Work order

### Phase 1 — Freeze and label the existing evidence

- Preserve the executed notebook and its outputs as the original exploratory run.
- Record its exact query sample, candidate-pool construction, thresholds, retrieval metrics, and latency assumptions.
- Separate measured wall-clock execution from arithmetic latency estimates throughout project documents.
- Reconcile each number against its source artifact; remove unsupported numbers and claims.

**Completion condition:** One results ledger identifies every reported value, its source, protocol, and limitations.

### Phase 2 — Correct the evaluation protocol

- Remove query-label-dependent corpus construction. Evaluate against the full declared corpus, or define a corpus slice independently of evaluation qrels.
- Separate threshold development from final evaluation. Use validation folds for threshold selection and keep a held-out test set untouched; avoid sweeping thresholds and reporting the same queries as the final result.
- Decide whether the intended first stage is single-field BM25 or Best Fields BM25, then use that same variant in threshold tuning and evaluation.
- On SciFact, compute the static baseline on the exact same held-out queries as the cascade in every fold.
- Save fold-level metrics and per-query routing decisions, rankings, and timings.

**Completion condition:** A deterministic protocol with no qrel-informed candidate pool, no threshold selection on the final test set, and matched baselines.

### Phase 3 — Implement and time a real conditional cascade

- Wire BM25, the router, and the conditional dense/SPLADE fallback into one query-time path.
- Verify in instrumentation that early-exit queries do not call dense or SPLADE.
- Measure actual per-query elapsed time using warmups, repeated runs, and correct GPU synchronization; report p50, p95, and p99 as well as the mean.
- Record branch invocations, GPU time, and device details. Keep estimated costs clearly separate from observed latency.
- Fingerprint embedding and sparse-index caches by model, corpus, and document ordering.

**Completion condition:** The cascade is executed online and its skipped work and latency are directly observed.

### Phase 4 — Evaluate quality and operating trade-offs

- Compare BM25, dense, SPLADE, static RRF, and cascade on identical query/corpus splits. Include SPLADE as a strong single-retriever baseline because it exceeded RRF on the saved NQ retrieval metrics.
- Report hit/recall at useful cutoffs, nDCG, and a latency–quality curve. State the quality constraint before threshold tuning.
- Add per-query or bootstrap uncertainty and fold-level results.
- Evaluate downstream QA with the same generator, prompts, and context budget for static and cascaded retrieval; keep the existing SQuAD generator result separate unless it is rerun as a matched comparison.
- Test threshold transfer between at least one development collection and an untouched target collection.

**Completion condition:** The main claims are supported by matched retrieval and, if claiming RAG quality, matched QA results.

### Phase 5 — Consolidate the project narrative

After the evaluation is stable, rewrite the project-facing material from the results ledger: project-focused literature review, research paper, full report, README, project anchor, and oral-defense guide. Regenerate the DOCX/PDF versions from the approved source and verify they agree. Keep the original exploratory Kaggle notebook available and add a clean final reproduction notebook/script for the corrected experiments.

**Completion condition:** All documents use the same method description, metrics, threshold provenance, and limitations.

## Updated result and next work

The first corrected SciFact run is complete and recorded in `cascade_heldout_scifact.json`. It uses the full 5,183-document corpus, 809 train queries for threshold selection, and 300 held-out test queries. On the Tesla T4, static RRF reaches Recall@100 0.9610, nDCG@10 0.6984, and MAP@10 0.6538 at 53.63 ms mean measured latency. The 98%-of-static-training-recall constraint was not met by any tested gate. The runner correctly used static fallback: 0% test exits, 0 neural calls skipped, and 53.69 ms mean latency. Thus, the current gate has not demonstrated useful acceleration under the declared quality target.

### Next implementation step

1. Completed: `threshold_frontier_scifact.json` records all 90 fixed-threshold candidates. None meets the 0.93922 train Recall@100 target.
2. Completed: `router_training_scifact.jsonl` contains 809 train-only examples with BM25 features and per-query recall gain from Dense+SPLADE escalation.
3. Completed first learned-router attempt: `results/learned_cascade_heldout_scifact.json` shows 70.67% exits but lower recall (0.9346 vs 0.9610) and slower latency (61.48 vs 56.01 ms). The Random Forest router alone averaged about 21 ms per query.
4. Completed: `results/compact_router_cv_scifact.json` compares shallow trees, Ridge, ExtraTrees, and the 300-tree reference with nested train-only CV and a 99% recall target. Ridge predicts in 0.14 ms locally with 49.20% exits and 99.36% pooled relative recall; ExtraTrees-32 gives 55.25% exits and 99.49% relative recall at 1.19 ms. Fold results vary, and neither result is a held-out guarantee.
5. Completed: the frozen SciFact-trained Ridge gate was evaluated on the official full NFCorpus test corpus. It exited on 68.11% of queries and cut mean latency 45.8%, but Recall@100 retained only 85.2% of static RRF (0.2681 vs. 0.3147); p95/p99 latency improved only 5.1%/1.3%. This is not a quality-preserving result. The NFCorpus test set is now inspected, so do not tune on it. Next, use a development split to diagnose or recalibrate the router, freeze the revised protocol, and evaluate on another untouched collection. Keep the current JSON as a transfer-failure case study.

## Current project position

Treat the existing NQ cascade sweep as exploratory: its pool uses qrels from the selected evaluation queries, its neural branches are precomputed before routing, and its latency is calculated from fixed component costs. Treat the SciFact cross-validation output as legacy exploratory evidence because it used a single-field BM25 cache and unmatched aggregate baselines. The new held-out SciFact run corrects those protocol issues but finds no qualifying gate in its tested threshold grid. Do not claim measured neural-call savings or answer-quality preservation for the current method.


## Recommended contribution to build next

The current cross-dataset result exposes the central implementation gap: a threshold calibrated on SciFact does not preserve its exit rate or recall on NFCorpus. The next method should treat cross-domain transfer as an untrusted starting point and add a target-development calibration stage.

### Candidate method: recall-constrained adaptive cascade

1. Run BM25, Dense, SPLADE, and static RRF offline on labeled development queries. Record each query's BM25 features, whether early exit would change its Recall@100, and the latency cost of escalation.
2. Fit a compact model to predict the *per-query recall gain from escalation*. Keep the frozen SciFact Ridge model as one baseline, alongside simple rules and a target-trained compact model.
3. Select the exit threshold using development queries only. Maximize skipped neural calls while requiring a predeclared recall floor against static RRF. Use a query bootstrap lower confidence bound for the constraint; if no threshold qualifies, set the policy to full RRF.
4. Freeze the model, threshold, feature code, and retrieval settings. Evaluate once on an untouched test collection and report quality, skipped calls, mean/p50/p95/p99 latency, and uncertainty on the same queries.
5. Add a shift safeguard: if target development features or predicted gains fall outside the calibration range, disable early exit and use full RRF.

This makes the research question concrete: **can target-side calibration and a conservative fallback recover useful neural-call savings under a stated recall constraint when a source-trained gate transfers poorly?** The NFCorpus test result remains a failure analysis; do not use its test labels or route outcomes to choose the revised policy. Use NFCorpus development data for calibration only, then select a different untouched collection for confirmation. Check the downloaded literature before making a novelty claim; this is a candidate contribution, not a verified novelty claim.

### Immediate next step

Prepare a development-calibration evaluator that saves per-query features, RRF rankings, BM25 rankings, branch timings, and decisions separately for development and test. Before another GPU run, confirm the target collection's split protocol and lock the recall floor and bootstrap procedure. The existing `11_evaluate_ridge_transfer_nfcorpus.py` is a test-only transfer script and should not be repurposed to tune on NFCorpus test.
