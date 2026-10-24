# Results Ledger — Existing Runs

This ledger preserves existing project results while separating execution evidence from evaluation validity. “Executed” means code ran and produced the recorded output; it does not by itself mean the protocol is unbiased or the metric is a live end-to-end measurement.

## Kaggle Natural Questions notebook

Source: [executed reproduction notebook](../notebooks/reproduction.ipynb), cells 1–3. The notebook loads 500 BEIR NQ queries and reports the executed outputs below.

### Retriever ablation

| Retriever | Hit@5 | Hit@20 | nDCG@10 |
|:--|--:|--:|--:|
| BM25 | 0.6700 | 0.8440 | 0.5433 |
| Dense MiniLM | 0.8060 | 0.9600 | 0.6751 |
| SPLADE | 0.8900 | 0.9820 | 0.7589 |
| Three-way RRF | 0.8300 | 0.9720 | 0.7094 |

**Protocol caveats:** The code builds `pool_corpus` from the first 15,000 corpus records and then adds every document appearing in the selected queries’ qrels. It uses these qrels to define the candidate corpus. This is not a clean full-corpus BEIR test. The code computes all three branch rankings for all queries before applying the cascade decision.

### Default cascade run

| Thresholds τhigh, τgap, τidf | Exits | Hit@5 | Hit@20 | nDCG@10 | Reported latency |
|:--|--:|--:|--:|--:|--:|
| 22, 3.5, 3.0 | 92.4% | 0.6940 | 0.8800 | 0.5625 | 14.3 ms |

The notebook reports static RRF at Hit@5 0.8300, Hit@20 0.9720, nDCG@10 0.7094, and 67.0 ms; BM25 at 0.6700, 0.8440, 0.5433, and 10.0 ms. The 10/12/45 ms component latencies are constants in the notebook, so the cascade latency is calculated, not timed.

### Threshold sensitivity sweep

| Configuration | Thresholds τhigh, τgap, τidf | Exits | Hit@5 | Hit@20 | nDCG@10 | Calculated latency |
|:--|:--|--:|--:|--:|--:|--:|
| Conservative | 28, 6, 3.5 | 73.2% | 0.730 | 0.918 | 0.6115 | 25.3 ms |
| Balanced | 25, 5, 3.5 | 84.2% | 0.710 | 0.894 | 0.5851 | 19.0 ms |
| Moderate | 23, 4, 3.0 | 90.0% | 0.702 | 0.884 | 0.5704 | 15.7 ms |
| Aggressive | 21, 3, 3.0 | 94.2% | 0.692 | 0.872 | 0.5584 | 13.3 ms |

**Interpretation:** The executed ranking results show a quality–exit-rate trade-off on this qrels-filtered candidate pool. These are in-sample threshold sweep values from the same 500 queries, not held-out threshold generalization. Because the notebook precomputes all branches, exits are simulated and do not demonstrate skipped encoder calls.

## SciFact cached-results experiment

Sources: `cascaded-blended-rag/results/cv_cascaded_results.json` and `experiments/07_tune_cascade_cv.py`.

| System | Recall@100 | nDCG@10 | Reported mean latency | Exits |
|:--|--:|--:|--:|--:|
| Static RRF | 0.9610 | 0.7032 | 90.87 ms | 0% |
| Cascade | 0.9001 | 0.6613 | 30.20 ms | 84% |

**Protocol caveats:** The script reads the single-field BM25 cache, uses the test query/qrels collection for its threshold cross-validation, and compares held-out cascade averages with a full-query static baseline. Latencies are reconstructed from cached component timings; the script does not execute a conditional neural fallback. Keep this as legacy exploratory evidence, not the final held-out result.

## Other saved retrieval results

Sources: `squad_replication_results.json`, `trec_covid_replication_results.json`.

| Dataset / metric | BM25 | Dense | SPLADE | Three-way RRF |
|:--|--:|--:|--:|--:|
| SQuAD v1.1 Hit@10 (500 questions) | 0.906 | 0.954 | 0.988 | 0.964 |
| SQuAD v1.1 nDCG@10 | 0.7630 | 0.7576 | 0.8648 | 0.8298 |
| TREC-COVID nDCG@10 | 0.4998 | 0.5904 | 0.6403 | 0.6463 |

These are static retriever results, not cascade evaluations. The SQuAD FLAN-T5-XXL generation scores are a separate experiment and do not measure answer quality under cascade versus static retrieval.

## Corrected held-out SciFact run

Source: [`cascade_heldout_scifact.json`](../cascade_heldout_scifact.json), produced by `experiments/08_evaluate_cascade_heldout.py` on Kaggle with a Tesla T4. It uses all 5,183 SciFact corpus documents, 809 train queries for threshold selection, and 300 held-out test queries. It uses Best Fields BM25 consistently and compares static three-way RRF with the cascade on the same test queries. This is the first live conditional-path evaluation in the project.

| System | Recall@100 | nDCG@10 | MAP@10 | Mean latency | P50 | P95 | P99 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Static three-way RRF | 0.9610 | 0.6984 | 0.6538 | 53.63 ms | 51.21 ms | 82.38 ms | 89.35 ms |
| Cascade (static fallback) | 0.9610 | 0.6984 | 0.6538 | 53.69 ms | 51.21 ms | 80.02 ms | 90.39 ms |

| Single retriever | Recall@100 | nDCG@10 | MAP@10 |
|:--|--:|--:|--:|
| Best Fields BM25 | 0.8706 | 0.6369 | 0.5908 |
| Dense MiniLM | 0.9250 | 0.6451 | 0.5959 |
| SPLADE | 0.9320 | 0.7024 | 0.6590 |

**Selection outcome:** the predeclared training constraint was 98% of static training Recall@100. Static training recall was 0.95838, so the target was approximately 0.93920. None of the tested thresholds met it. The runner therefore selected no threshold and used static RRF for all test queries. The test cascade had 0% early exits, skipped 0 Dense calls and 0 SPLADE calls, and invoked each neural retriever 300 times. Its latency is effectively equal to static RRF; this run demonstrates no retrieval-cost reduction from the current gate under the stated quality constraint.

**Interpretation and limits:** the protocol is held out and matched, and latency is measured on the Kaggle T4 with CUDA synchronization. It is a single timing pass, so treat percentiles and mean as initial hardware-specific measurements. Train-only frontier (`threshold_frontier_scifact.json`): all 90 candidates were evaluated on the 809 training queries. None meets the 0.93922 Recall@100 target. Training Recall@100 ranges from 0.9111 to 0.9286; exit rates range from 78.74% to 96.42%. The best-recall point is 0.9286 at 79.48% exits, still 0.0106 below target. Candidate latency is estimated on training data and is not evidence of held-out savings. The result is evidence that the tested gate/grid did not meet its objective, not evidence that no possible gate can. the protocol is held out and matched, and latency is measured on the Kaggle T4 with CUDA synchronization. It is a single timing pass, so treat percentiles and mean as initial hardware-specific measurements. The output does not include the per-threshold training quality/exit table, so it cannot show the best achievable quality–cost point outside the 98% constraint. The result is evidence that the tested gate/grid did not meet its objective, not evidence that no possible gate can.

## Train-only threshold frontier

Train-only frontier (`threshold_frontier_scifact.json`): all 90 candidates were evaluated on the 809 training queries. None meets the 0.93922 Recall@100 target. Training Recall@100 ranges from 0.9111 to 0.9286; exit rates range from 78.74% to 96.42%. The best-recall point is 0.9286 at 79.48% exits, still 0.0106 below target. Candidate latency is estimated on training data and is not evidence of held-out savings.

**Next:** inspect feature calibration and add stronger routing baselines, then select any revised policy on development data only. Evaluate the revised policy on untouched queries with repeated latency measurements. A GPU is needed only for fresh Dense or SPLADE rankings; reuse Kaggle caches if available., add a train-only threshold diagnostic that records each grid point's Recall@100, exit rate, and estimated latency. Plot the training quality–exit frontier and state the trade-off transparently. If no useful point exists, redesign or recalibrate the gate, then evaluate the revised rule on the untouched SciFact test queries or a newly reserved test split. A GPU is needed for fresh neural retrieval passes; the SciFact corpus encoding caches may be reused only if the same Kaggle session and files are preserved.



## Learned escalation-risk router: first held-out attempt

Source: `results/learned_cascade_heldout_scifact.json`, produced on a Tesla T4 using a Random Forest trained on 809 train-only examples. The routing threshold was calibrated from five-fold out-of-fold training predictions.

| System | Recall@100 | nDCG@10 | MAP@10 | Mean latency | Early exits |
|:--|--:|--:|--:|--:|--:|
| Static three-way RRF | 0.9610 | 0.6984 | 0.6538 | 56.01 ms | 0% |
| Learned gate + static escalation | 0.9346 | 0.6694 | 0.6200 | 61.48 ms | 70.67% |

The learned gate skipped 212 Dense and 212 SPLADE test-query invocations, but test Recall@100 retained only 97.25% of static RRF and mean latency was 5.47 ms slower. Average router computation was about 21.04 ms per query, which erased the savings from skipped neural work. Training OOF calibration predicted 0.9842 of static recall with a 76.76% exit rate; the held-out result did not reproduce that quality level. This is an implementation diagnostic, not a successful efficiency result.

**Engineering follow-up:** profile feature extraction and model inference separately; compare much smaller/cheaper predictors and calibrate with a larger safety margin using training data only. After choosing an implementation, evaluate it on a fresh untouched split. Do not tune a new threshold against this already inspected test result.

## Compact router comparison (train-only nested CV)

`results/compact_router_cv_scifact.json` compares compact predictors using nested cross-validation over the 809 SciFact training queries. Each outer fold's threshold was selected only from its inner training folds to target 99% of static BM25+Dense+SPLADE RRF recall. The original held-out test qrels were not used. Values below are pooled outer-fold results; inference timings are local one-row model prediction only, not end-to-end Kaggle latency.

| Predictor | Early exits | Recall@100 / static | Local prediction |
|:--|--:|--:|--:|
| Depth-2 decision tree | 49.69% | 99.22% | 0.060 ms |
| Ridge | 49.20% | 99.36% | 0.144 ms |
| 32-tree ExtraTrees | 55.25% | 99.49% | 1.188 ms |
| 300-tree Random Forest reference | 60.94% | 99.32% | 9.779 ms |

Fold results vary, and some outer folds fall below the 99% target. Treat this as a development comparison, not a guarantee. A local microbenchmark measured feature construction at about 0.006 ms, the 300-tree predictor at about 9.6 ms, Ridge at about 0.14 ms, and a depth-2 tree at about 0.06 ms per query. These CPU-only figures are not directly comparable to the prior Kaggle route timings; the recorded ~21 ms route time combines feature construction and prediction. All 809 SciFact training queries have already participated in nested CV/model comparison, and the original 300-query test set has already been inspected, so neither is a new untouched final test. The local TREC-COVID fast loader is also unsuitable as an independent test corpus because it selects relevant documents using qrels. A valid next evaluation needs an independent dataset with an unfiltered corpus and a predeclared protocol. That retrieval evaluation needs Kaggle GPU access for Dense/SPLADE unless matching validated caches can be reused.

## Cross-dataset transfer evaluation: SciFact-trained Ridge on NFCorpus

Artifact: `results/ridge_transfer_nfcorpus.json`; script: `experiments/11_evaluate_ridge_transfer_nfcorpus.py`. It freezes a `StandardScaler + Ridge(alpha=10)` router and threshold using SciFact train examples, then evaluates on the official BEIR NFCorpus test split. Train-only calibration gave threshold 0.06379, 55.25% OOF exits, and 99.36% pooled OOF recall relative to static RRF. The evaluator used the full 3,633-document corpus, read relevance grades after routing, validated the dataset archive MD5, used a corpus-specific cache directory, and measured two warmed timing passes on a Tesla T4.

| System | Recall@100 | nDCG@10 | MAP@10 | Mean latency | p50 | p95 | p99 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Static RRF | 0.3147 | 0.3452 | 0.1304 | 25.04 ms | 23.44 ms | 35.02 ms | 38.54 ms |
| Frozen Ridge cascade | 0.2681 | 0.3203 | 0.1235 | 13.56 ms | 8.89 ms | 33.23 ms | 38.05 ms |

The router exited on 220/323 queries (68.11%) and skipped 220 Dense plus 220 SPLADE calls per measured pass. Mean latency fell 45.8%, while Recall@100 fell 0.0466 absolute, retaining 85.2% of static RRF. nDCG retained 92.8%; MAP retained 94.8%. p95 latency improved only 5.1%, and p99 1.3%. The cascade is materially faster on average but fails the near-static-recall goal under cross-dataset transfer. Treat this as a negative transfer/quality trade-off result, not a successful quality-preserving speedup. The test set is now inspected; do not tune this result and present it as held out again.

BEIR lists NFCorpus as a 3.6K-document corpus with train/dev/test splits ([official BEIR dataset list](https://github.com/beir-cellar/beir/wiki/Datasets-available)). The source archive is `cascade_source_bundle_nfcorpus_ridge_v1.zip`; its Kaggle dataset name was `cascade-source-bundle-nfcorpus-ridge-v1`. The script downloads NFCorpus itself and writes the result to `results/ridge_transfer_nfcorpus.json`.
