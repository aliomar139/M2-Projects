# SPSS analysis review

Use this file for exact results and variable codes. For a short progress summary, open [the README](../README.md).

## PCA and interaction artifact cleanup, 16 November 2026

At the user's request, removed the PCA/PLS extraction experiment and fixed-interaction experiment: runners, configurations, interaction tests, cached bytecode and output folders. The dependent mixed loss-tuning experiment was also removed because it contained refined PCA and imported the deleted extraction runner/read its outputs. Its boosting/Huber/median results are preserved below alongside its PCA results.

The original methods, exact result tables, interpretation and limitations remain in the historical sections below for the paper, presentation and questions. Paths in those marked sections identify former locations; they are not available files or current run instructions. Historical checks describe the checks performed before deletion. This cleanup does not mean PCA never improved a metric: ordinary Broad D PCA + ridge had .5748 overall MAE, while the selected score blend prioritized High-score performance. No experiment was retrained and no result was changed to make the deletion look favourable.

The selected eight-input Random Forest, its augmentation/verification dependencies, source data, separate ridge/SVR blend and unrelated experiments are preserved.

## Boruta RF selection completed, 16 November 2026

Separate [results](../classification/boruta-outputs/20261116T082517133758Z/results.md), runner `classification/train-boruta.py`, settings `classification/boruta-config.json`. **Retain current eight-input RF.** Confirmed-only Boruta from all 23 eligible inputs gives 72.9% recall/36.1% precision, F2 .604040, 12.4 detections/17 and 22.2 false warnings/80 under F2 tuning. Recall guard gives 82.4%/32.6%, .630103, 14.0 detections and 29.0 warnings. Current reference remains 87.1%/34.7%, .667848, 14.8 detections and 28.0 warnings. F2 saves 5.8 warnings but loses 2.4 detections; guard loses .8 detections and adds one warning. Means reuse five dependent repetitions of the same 97 students.

Boruta retains 2–5 variables in outer training fits (mean 3.56), not a fixed eight. Workload/academic stress appear in 25/25, AI dependence 20/25, avoidance 16/25; financial strain, university support and AI offloading each 1/25. Selection refits inside each original inner/outer training group on real answers only. Official BorutaPy 0.4.3: 100-tree, depth-5, min-leaf-2 balanced selector forest; max_iter 50, perc 100, alpha .05, two_step True, fixed context seeds. Any confirmed encoded column retains its complete source variable/dummy group; tentative inputs excluded. No zero-confirmed context occurred; a predeclared class-prior fallback handles that case without forcing another feature. This is not a group-level relevance significance test or a globally fitted final feature set.

Same original 5x5 stratified outer/four inner folds and primary score >=4 target (17 High/80 Below-high). Original 36 forest/depth/leaf/weight/augmentation settings and .05-step thresholds independently tune using inner predictions, under F2 and prior recall-guard tie rules. Guard constrains inner recall only. Constrained full-23 training synthetic pools are projected onto selected inputs; projected duplicates and inferred labels remain limitations. The whole procedure, including this generation domain, is evaluated; no isolated causal claim about Boruta alone. Real-only held-out evaluation; earlier reference scores copied after matching folds/hashes.

125 selector fits, 5,894 selector-forest iterations, 3,600 inner/40 outer prediction fits. Saved 900 candidate score sets, 50 choices, 1,455 predictions, 125 selector contexts with histories/supports, selected inputs, training memberships, generation profiles/parents, folds, paired metrics and hashes. [Verification record](../classification/boruta-outputs/20261116T082517133758Z/verification.json) details checks. Only Boruta 0.4.3 was installed; existing dependency versions and earlier helper/source/result files remain unchanged. No new questions/respondents, independent validation, clinical probabilities or deployment artifact. This one fixed selector setup did not improve the requested warning balance; it does not prove every feature-selection setup fails. Next: retain selected RF and preserve this comparison.

Boruta verification passed: all 18,900 threshold candidates, 50 choices, 125 saved selector/training contexts and generation/provenance records checked, together with original folds/copied reference scores, core metrics/AP/AUC, summaries, paired differences and unchanged source/package hashes. Independently refitted 160 selected inner/40 outer prediction models and reproduced scores. Replayed two predeclared Boruta contexts and reproduced support/rankings/histories; the other 123 selectors and unselected candidate models were not independently refitted. This is computational verification, not independent-cohort validation.

## RF input-combination comparison completed, 16 November 2026

Separate [results](../classification/input-comparison-outputs/20261116T075921907598Z/results.md), runner `classification/train-input-comparison.py`, settings `classification/input-comparison-config.json`. **Retain the current eight-input RF.** Replacing AI frequency/study hours with academic stress/avoidance gives 72.9% recall /37.3% precision, F2 .610528, 21.2 false warnings under F2 tuning; its recall guard gives 81.2%/32.5%, .624508, 28.6 warnings. Training-only selection of eight variables from all 23 gives 72.9%/37.9%, .612559, 20.8 warnings; its guard gives 83.5%/33.5%, .642739, 28.2 warnings. The reproduced current RF remains 87.1%/34.7%, .667848, 28.0 warnings. Neither new approach improves the requested detection/warning balance. All counts average five dependent repetitions.

Fixed alternative: workload, sleep duration, financial strain, university support, AI dependence, AI offloading, academic stress, avoidance. Automatic ranking reuses grouped standardized L2 logistic C=1 coefficients on real training members, refitted inside each inner and outer training group; retain eight variables with complete dummy groups, in original questionnaire order. It is one specified selector, not an exhaustive search or proof that nonlinear predictors are irrelevant. Each new input approach independently retunes original RF depth/leaf settings, High weight 1/2/4, augmentation ratio 0/.5/1 and original .05-step threshold grid. Selection/generation/preprocessing exclude held-out students. F2 and recall-guard rules follow [classification instructions](../classification/README.md#alternative-input-combinations-16-november-2026); guard constrains inner recall, not outer recall. Current eight control refits original selected recipes and reproduces saved scores/thresholds/inner metrics.

Same original 5x5 outer/four inner stratified folds; 97 real students, 17 primary score >=4 /80 below. Initial 7,300 inner/104 outer fits; saves 1,825 candidate score sets, 125 choices, 2,425 predictions, 375 training contexts, synthetic pools with parent provenance, selected input frequencies, folds, confusion matrices, paired changes and hashes. [Verification record](../classification/input-comparison-outputs/20261116T075921907598Z/verification.json) provides the independent checks. Original SAV/CSV, previous outputs/helpers and selected models remain unchanged. Synthetic labels are assumptions; no independent participants, clinical validation, extra questions or deployment model. Existing full-sample SPSS findings and many prior comparisons motivated this experiment, so results remain exploratory. Next: preserve this comparison and retain selected RF.

Verification passed for all 38,325 threshold candidates, 125 decisions and 375 training contexts, including reconstructed variable rankings, generated profiles/parents, original folds and control scores, core metrics/AP/AUC, summaries/paired changes and unchanged hashes. Independently refitted 416 selected inner and 104 outer forests and reproduced saved scores; unselected candidates were not refitted. This verifies computation, not independent-population performance.

## SVC with 23 existing input variables completed, 16 November 2026

Separate [results](../classification/svc23-outputs/20261116T072730431772Z/results.md). Runner `classification/train-svc23.py`, configuration `classification/svc23-config.json`. Selected RF, source SAV/CSV, helpers and earlier outputs are unchanged. The comparison adds no new questionnaire features or observed students: Broad D uses 23 previously collected/reconstructed variables, expanding to 37 encoded columns.

| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Selected eight-input RF | 87.1% | 34.7% | .667848 | 14.8 | 28.0 | .526861 | .808971 |
| Eight-input SVC, F2 | 78.8% | 36.2% | .637154 | 13.4 | 23.6 | .478095 | .780441 |
| 23-input SVC, F2 | 76.5% | 40.4% | .646090 | 13.0 | 19.4 | .496812 | .807647 |
| Eight-input SVC, recall guard | 80.0% | 33.4% | .624572 | 13.6 | 27.2 | .485409 | .788824 |
| 23-input SVC, recall guard | 83.5% | 35.4% | .655506 | 14.2 | 26.2 | .501249 | .804412 |

The 23-input guard improves all reported mean warning metrics versus the matching eight-input rule: +.6 High detections and one fewer false warning per evaluation; F2 improves in three of five dependent repetitions. Against RF, it loses .6 detections while saving 1.8 warnings and has lower F2. The 23-input F2 rule increases precision by 4.23 percentage points and removes 4.2 warnings versus its eight-input counterpart, but loses .4 detections. Versus RF it removes 8.6 warnings while losing 1.8 detections. Neither meets the combined aim of retaining roughly 87% recall with higher precision/fewer warnings. Keep selected RF for the user's High-detection priority; the new procedures remain trade-off alternatives.

### Method

Exact same 36-setting grid/fixed settings, normalized High weights, threshold rules and tie rules as the previous eight-input SVC. Independently tune C/gamma/weight/threshold on 23 inputs using original five outer seeds/five stratified folds and four inner folds. Encoding/scaling fit on real inner training members only. Primary score >=4: 17 High/80 Below-high. No augmentation, BAT predictors, new features or calibrated probability estimation. The recall guard uses the current RF recorded inner recall, which does not guarantee outer recall. Settings and threshold selection reuse inner predictions while excluded outer students evaluate complete procedures. Earlier eight-input SVC and RF predictions are copied exactly; no reference model is retrained. All 3,600 inner and 35 outer initial fits converged. A narrow filter suppresses only the known sklearn probability-parameter future-deprecation notice; convergence errors remain fatal. No package changes.

### Verification and artifacts

Saved 2,425 prediction rows, 25 repetition metrics, five summaries, confusion matrices, 20 paired changes against RF and matched eight-input SVC, all 900 candidate inner score sets with threshold records, 50 final choices, input list, original folds, configs/hashes. Independent verification reconstructed 62,758 threshold candidates and checked metrics/ties/choices, exact ordered training IDs/folds/inner minimum recall, copied reference predictions, score/class alignment, counts/AP/AUC, summaries/paired differences and unchanged source/reference/code hashes. It independently refitted 140 selected inner and 35 selected outer models and reproduced margins/labels and encoded feature counts. No separate software test suite or deployment model. These are five dependent repetitions of the same 97 students after many experiments; no independent or clinical validation. Next: retain RF as selected and preserve this broader-input SVC comparison as measured trade-off evidence.

## RBF SVC classification completed, 16 November 2026

Separate [results](../classification/svc-outputs/20261116T070622236133Z/results.md). Runner `classification/train-svc.py`; configuration `classification/svc-config.json`. **Selected model remains the existing RF with training-selected augmentation.** Original source data and all earlier experiment files are unchanged. This experiment uses SVC for binary classification, distinct from prior SVR score regression.

| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Selected RF | 87.1% | 34.7% | .667848 | 14.8 | 28.0 | .526861 | .808971 |
| RBF SVC, inner F2 | 78.8% | 36.2% | .637154 | 13.4 | 23.6 | .478095 | .780441 |
| RBF SVC, inner recall guard | 80.0% | 33.4% | .624572 | 13.6 | 27.2 | .485409 | .788824 |

The F2 rule removes 4.4 false warnings per evaluation on average but detects 1.4 fewer High students. Its F2 improves in one repetition and declines in four. Guard removes .8 false warnings and detects 1.2 fewer, with lower mean precision/F2 and lower F2 in all five repetitions. Neither achieves the improvement target of retaining roughly 87% recall while raising precision/reducing warnings. Training constraints do not guarantee excluded recall. All means reuse the same 97 real students over five dependent repetitions; this comparison is exploratory, not an independent clinical validation or proof that all SVC variants fail.

### Training and selection

Same eight Small B existing questions and original High boundary (primary BAT >=4; 17 High/80 Below-high). Original five outer seeds with five stratified folds each and four stratified inner folds. One-hot encoding and scaling fit inside each real training group. No augmentation, extra observed rows/features, BAT predictors or probability fitting. Raw decision-function margins are uncalibrated warning scores.

Grid: C .1/1/10/100, gamma .01/.1/1, relative High weights 1/2/4 normalized to mean one per fit: 36 settings per outer group. RBF, tol .001, max_iter 100000, cache_size 200; convergence problems fail the run. Exact threshold candidates are all unique pooled inner margins, 0 and nextafter(max,+inf); classify High at score >= threshold. F2 rule jointly selects settings/threshold using F2, precision, recall, higher threshold, earlier candidate. Guard requires current RF recorded inner recall, minimizes FP, then favors recall/precision/F2/threshold/earlier candidate. Settings and threshold reuse inner validation predictions; outer students remain excluded from the complete selection procedure. Same selected candidate shares a final fit across procedures. AP/AUC pool margins across different fold models and are discrimination diagnostics rather than individual risk probabilities.

Initial run fitted 3,600 inner and 37 outer models; all converged. Explicit probability=False produces a future-deprecation notice in installed scikit-learn 1.9.1, without enabling probability estimation. Reference RF scores/labels are copied exactly from its unchanged selected run, not refitted. No extra dependency was needed.

### Verification and saved artifacts

Saved 1,455 predictions, 15 repetition rows, three summaries, confusion matrices, ten paired differences, original inner/outer folds, 900 candidate inner score arrays with F2/guard threshold records, 50 final decisions, configs and source/helper/package hashes. Independent verification reconstructed all 71,604 threshold candidates and their metrics, tie rules and selections; checked folds/ordered training IDs, frozen RF minimum recall, exact RF controls, score/class alignment, counts/metrics/AP/AUC, summaries/paired changes and unchanged hashes. It independently refitted 148 selected inner and 37 selected outer models using independently calculated normalized weights, reproducing saved inner and excluded margins/labels. No separate software test suite or deployment model was produced. Next: retain RF as reference and this measured negative comparison; no gain beyond the selected model is claimed.

## Precise TabPFN thresholds and RF mixture completed, 14 November 2026

Two separate folders preserve previous experiments: [exact-threshold results](../classification/tabpfn-threshold-outputs/20261114T125820967153Z/results.md) and [mixture results](../classification/tabpfn-voting-outputs/20261114T125820967153Z/results.md). **The selected RF remains unchanged.** Runner `classification/train-tabpfn-refinement.py`; configuration `classification/tabpfn-refinement-config.json`.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Selected RF | 87.1% | 34.7% | .667848 | 14.8 | 28.0 |
| TabPFN exact threshold, F2 | 74.1% | 35.2% | .605718 | 12.6 | 23.2 |
| TabPFN exact threshold, recall guard | 88.2% | 31.2% | .645250 | 15.0 | 33.2 |
| RF–TabPFN mixture, F2 | 81.2% | 36.8% | .653446 | 13.8 | 23.8 |
| RF–TabPFN mixture, recall guard | 83.5% | 36.8% | .665290 | 14.2 | 24.6 |
| RF-only exact thresholds, both rules | 83.5% | 35.8% | .659129 | 14.2 | 25.6 |

Exact thresholds improve the old TabPFN guard's precision/F2 and false-warning count (44.0 down to 33.2), at a recall change from 89.4% to 88.2%. Compared with the selected RF, they add 5.2 false warnings for .2 more High detections. Mixture guard saves 3.4 false warnings at a cost of .6 detections, with slightly lower F2. The exact-threshold F2 rule does not generalize better despite non-decreasing chosen inner F2. The threshold-grid diagnostic identified opportunities on inner validation, not a held-out improvement guarantee. Five repetitions reuse the same 97 students; this remains exploratory after many experiments.

### Procedure and preservation

Reuse complete frozen endpoint predictions from `classification/tabpfn-outputs/20261114T124506935366Z/` and the RF endpoint in `classification/voting-outputs/20261113T203744495093Z/`. Match ordered training IDs, original five outer seeds/five folds and four inner folds, saved RF inner metrics and TabPFN inner choices before evaluating. The real SAV loader revalidates 97 students, both target formulas and indicator reconstruction. RF keeps its previously selected augmentation/weights/parameters; TabPFN keeps real-only contexts. No endpoint refit, new synthetic rows, feature additions, calibration, dependency changes or deployment fit.

Stage one evaluates every unique TabPFN inner score plus 0, 1 and the next float above 1 (all-negative sentinel). High prediction uses >=. Stage two evaluates the same exact-score rule separately for RF shares 1/.75/.5/0 and includes RF-only controls. F2 selection maximizes inner F2, precision, recall, higher threshold and RF share. Guard requires the selected RF's recorded inner recall, minimizes FP, then maximizes recall, precision, F2, threshold and RF share. These decisions use inner labels/scores only; inner recall constraints do not guarantee outer recall. Endpoint recipe selection and further tuning reuse the same inner folds, while outer students remain excluded. No probabilities are clinically calibrated.

Mixture F2 selected pure RF in 18/25 training groups, RF shares .75/.5/0 in 3/1/3; guarded mixing selected pure RF in 20/25 and .75/.5 in 4/1. No global mixture or threshold was chosen using outer labels. Conditional reuse of verified endpoint contexts avoids unnecessary retraining; these results compare specified decision procedures rather than new endpoint training algorithms.

### Verification

Exact stage: 2,425 predictions, 25 repetition metrics, five summaries, 2,014 inner candidate rows and 50 choices. Mixture stage: 3,395 predictions, 35 repetition metrics, seven summaries, 8,047 candidate rows and 100 choices. Both save configs/hashes, original folds, inner scores/candidates, selected shares/thresholds, confusion matrices and paired differences. Independent verification passed for all candidate boundaries, counts/metrics/ties, training IDs/fold memberships, saved endpoint scores, reconstructed outer mixtures, reference controls, predictions, summary/AP/AUC calculations, paired changes and unchanged source/code/reference hashes. No models were fitted during verification and no separate software test suite ran. Next: retain the selected RF and these separate trade-off results; neither comparison establishes a combined gain in High detection and false warnings. Built with PriorLabs-TabPFN; original public-v2 model provenance/license remain in its unchanged reference run.

## Local TabPFN-2 comparison completed, 14 November 2026

Separate [results](../classification/tabpfn-outputs/20261114T124506935366Z/results.md); runner `classification/train-tabpfn.py`, configuration `classification/tabpfn-config.json`. **Selected model remains Small B Random Forest + training-selected augmentation.** Source SAV/CSV, earlier outputs and original Python environment were preserved.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| Selected RF | 87.1% | 34.7% | .667848 | 14.8 | 28.0 | .526861 | .808971 |
| TabPFN-2, inner F2 | 81.2% | 36.5% | .651386 | 13.8 | 24.2 | .615797 | .846176 |
| TabPFN-2, inner recall guard | 89.4% | 26.1% | .598623 | 15.2 | 44.0 | .615797 | .846176 |

The pretrained model ranks students better in aggregate, but the F2 threshold loses one High detection on average; the guard gains .4 detections at the cost of 16 extra false warnings. Neither tested rule is a clear improvement for the selected warning system. Results average five dependent repetitions of the same 97 real students (17 High, 80 Below-high); repeated experiment selection remains exploratory.

Used public original TabPFN-2 weights, not gated current v3.5: eight fixed estimators, CPU, eight original Small B questions, no survey augmentation, external scaling/one-hot encoding, fine-tuning or hyperparameter search. Sleep/study are explicitly categorical. Each fit uses only its real training students as context. Original five outer seeds, five folds per seed and four inner folds were reproduced exactly: 100 inner + 25 outer context fits. Inner thresholds 0..1 by .05 maximize F2 or minimize false positives while retaining the current RF's recorded inner recall. No outer labels choose thresholds, and inner recall constraints do not guarantee outer recall. RF reference predictions were copied exactly from the selected augmentation experiment rather than refitted.

Checkpoint `tabpfn-v2-classifier-v2_default.ckpt`, public repository revision `275f19d2add9c2c0de38f9ebaded3856599fa2e7`, SHA-256 `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49`. Built with PriorLabs-TabPFN. Package TabPFN 10.0.0, PyTorch 2.14.1; separate `.venv-tabpfn` and dependency file preserve the original environment. Local offline inference; no survey upload. Official [model/license](https://huggingface.co/Prior-Labs/TabPFN-v2-clf) and [paper](https://www.nature.com/articles/s41586-024-08328-6); license/provenance and full environment freeze saved with outputs.

Independent arithmetic/decision verification passed: 1,455 predictions, 15 repetition metrics, three summaries, 525 threshold candidates, 50 selections, ten paired comparisons, original inner/outer folds, training membership, exact copied RF scores, score/class alignment and unchanged source/script/checkpoint hashes. All raw outputs remain separate in `classification/tabpfn-outputs/20261114T124506935366Z/`. No second model-fitting run, separate software test suite or deployment model. Next: retain this comparison; any finer threshold or calibration experiment must use training validation and preserve the selected RF reference. These results do not establish clinical risk probabilities or regression error improvement.

## Backward question selection completed, 14 November 2026

Completed separate [results](../classification/backward-selection-outputs/20261114T122443497555Z/results.md). Runner: `classification/train-backward-selection.py`; settings: `classification/backward-selection-config.json`. All previous results, selected models, source SAV/CSV and SPSS work were preserved. No global feature ranking or question removal was taken from the previous error inspection.

### Design

Each outer training group starts with all eight existing Small B questions. For a current subset, evaluate every possible one-question removal using the original four-fold real inner out-of-fold predictions and .05-step warning-threshold grid. Whole categorical questions retain all their encoded dummy columns. Identical subsets are cached across both search paths within the training group. The current RF's recorded tree parameters, High weight and augmentation ratio remain fixed, so this tests question removal conditional on the current recipe, not joint model retuning or exhaustive subset optimization. The RF's default sqrt feature sampling applies to the remaining encoded columns.

The `backward_f2` path chooses the best threshold by F2, precision, recall and higher threshold, then chooses the best child with remaining ties resolved by original question order. It accepts a removal only if inner F2 exceeds the current subset's by more than 1e-12. The `backward_recall_guard` path requires inner recall at least the current RF's recorded inner recall, selects fewer false positives with ties by recall, precision, F2 and higher threshold, and accepts a removal only if FP strictly decreases. It uses original question order for remaining child ties. Both paths stop at the first lack of strict objective improvement or one remaining question; a smaller model is never forced.

All removal, threshold, path and stopping choices use training data only. The same original five repetitions of five stratified outer/four inner folds and measured primary >=4 boundary are retained: 17 High and 80 Below-high real students. Current RF recipe selection and new removal selection reuse the inner folds, so inner improvements are optimistically selected. Fully excluded outer students evaluate the complete procedure. The training recall constraint is not an outer guarantee. Original full-eight synthetic pools are projected onto subsets and projected duplicates may occur; no additional survey inputs, independent students or new generation policy are introduced.

### Results

Counts and metrics below average five dependent evaluations of the same 97 students.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 | Average precision |
|---|---:|---:|---:|---:|---:|---:|
| Current eight-question RF | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 | .526861 |
| Full-eight reproduction control | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 | .526861 |
| Backward selection, strict F2 gain | 82.4% | 34.2% | .641302 | 14.0 | 27.2 | .531052 |
| Backward selection, recall guard / fewer FP | 82.4% | 34.9% | .647200 | 14.0 | **26.2** | .521441 |

Both paths detect .8 fewer High students per evaluation (recall down 4.7 percentage points). F2-path false warnings fall by only .8 and its precision declines about .5 points. Guarded-path false warnings fall by 1.8 and precision rises only about .2 points. F2 falls by .026546/.020648 respectively. Both paths have lower F2 in four repetitions and tie the current model in one; both lose one High detection in each of repetitions 2..5. These held-out results do not support replacing the current RF for the user's High-detection priority. The small change in average precision for the F2 path does not establish an overall warning-performance improvement.

Across the 25 training groups, 345 subsets were evaluated (with reuse across paths within a group). F2 selection ended with 8/7/6/5 questions in 12/10/2/1 groups. Guarded selection ended with 8/7/6/5 in 16/7/1/1 groups. No path needed to reach one question. Workload was retained in all 25 selections under each rule. These descriptive frequencies do not justify fixing a global subset from outer results. Strict inner gains did not transfer to improved outer F2; this result does not prove every alternative subset/selector fails or identify an unavoidable error floor.

### Artifacts and independent verification

The complete separate folder contains 1,940 held-out predictions across four procedures, 20 repetition metric rows, four summaries, confusion matrices, 345 saved inner score sets and 7,245 threshold metric rows, 79 recorded greedy steps with every sibling removal considered, 75 final decisions, chosen-question lists and counts, ten paired comparisons, original inner/outer assignments, generation counts, configs, package versions and source/helper/script hashes.

[Independent verification passed](../classification/backward-selection-outputs/20261114T122443497555Z/verification.json). It recomputed all held-out metrics including AP/AUC and every candidate's threshold confusion metrics from saved inner scores. It independently replayed all 79 backward steps, verifying the parent state, every permitted one-question child, metric ties, strict acceptance criteria, stopping conditions and final question sets. It checked every selected rule, cached-subset uniqueness, selected-question CSVs, paired differences, current RF recipes, original fold/training membership and generation counts. Full-eight scores and thresholds exactly reproduced the retained current RF, and source/code hashes remained unchanged. No second RF-fitting run, separate software test suite or deployment fit was performed.

### Decision

Keep the user's selected eight-question RF with training-selected augmentation. Retain this completed experiment separately, including the negative result, as requested. It tested greedy backward removal with the existing recipe; it did not examine every question combination or jointly retune the forest for every subset. The numerical score predictor remains the existing ridge/SVR blend. Any follow-up motivated by these repeatedly inspected 97 students is exploratory; synthetic labels remain assumptions and weighted scores are uncalibrated. No clinical diagnosis, independent validation or regression MAE improvement is claimed.

## Training-only question selection completed, 14 November 2026

Completed separate [results](../classification/question-selection-outputs/20261113T220427919147Z/results.md). Runner: `classification/train-question-selection.py`; settings: `classification/question-selection-config.json`. The folder uses the UTC start date 13 November; the run completed on 14 November in Beirut. The selected current RF, numerical regression blend, original data and prior experiment folders were preserved.

### What was tested

We compared 4, 6 and all 8 existing Small B questions. A fixed unweighted L2 logistic selector (C=1, lbfgs, max_iter=10000) ranks whole original questions from standardized encoded **real training rows only**. Strength is the coefficient L2 norm for a question divided by sqrt(its encoded-column count); ties use original questionnaire order. All encoded dummy columns belonging to a selected categorical question are retained. The selector is independently refitted inside each inner training group and then on the entire outer training group. No workload/AI/support questions are globally imposed from the prior error table.

For each outer training group, we retain the current RF's recorded training-selected tree parameters, High weight and augmentation ratio. Synthetic profiles are generated in the original full-eight space using original seeds/constraints, then projected onto question subsets; projected profiles can coincide even when full profiles are unique. This isolates question selection conditional on the current RF recipe, rather than performing another joint RF hyperparameter search. It is not an exhaustive comparison of all subsets or all ranking algorithms. Linear logistic ranking can miss nonlinear relevance.

Original five repetitions of five stratified outer/four inner folds and the original .05 warning-threshold grid are retained. The outcome remains primary measured score >=4 (17 High) versus <4 (80 Below-high), with only the 97 real students entering outer evaluation. `subset_f2` selects question count/threshold by inner F2, precision, recall, threshold and fewer questions. `subset_recall_guard` requires inner recall at least the current RF's recorded inner recall, then minimizes FP and favors recall, precision, F2, threshold and fewer questions. The guard is not a guarantee of outer recall. Current RF recipe selection and subset selection reuse inner folds; fully excluded outer students evaluate the whole process. A full-eight control must exactly reproduce current RF scores, inner metrics and thresholds.

### Results

Counts/metrics average five dependent repetitions of the same students, not independent cohorts.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 | Average precision |
|---|---:|---:|---:|---:|---:|---:|
| Current eight-question RF | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 | **.526861** |
| Full-eight reproduction control | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 | **.526861** |
| Selected question count, F2 | 85.9% | 35.2% | .666235 | 14.6 | **27.0** | .513705 |
| Selected question count, recall guard | 85.9% | 35.2% | .666386 | 14.6 | **27.0** | .519793 |

Both new rules remove one false warning per evaluation on average but detect .2 fewer High students (recall down 1.2 percentage points). Precision increases only about .5 points, while F2 and average precision decline slightly. The similar rounded means do not imply identical predictions: choices differ between procedures. F2 question selection is higher in two repetitions, lower in one and tied in two; guarded selection is lower in one and tied in four. The inner recall guard did not preserve current outer recall.

F2 selection chose four questions in 3/25 training groups, six in 2/25 and all eight in 20/25. Guarded selection chose four in 1/25, six in 1/25 and all eight in 23/25. Workload, AI dependence and university support were retained in every outer selection under both rules. These are descriptive selection frequencies, not validated feature importance or justification for fixing those three globally. Most inner fits retained the full question set under this selector.

### Verification and saved files

The separate folder contains 1,940 held-out predictions across four procedures, 20 repetition metric rows, four summaries, confusion matrices, 25 outer tuning records with 1,575 count/threshold candidates and 75 selected decisions, saved inner score arrays, 125 rankings/strengths/real-training IDs, selected whole-question lists, ten paired comparisons, original inner/outer assignments, configs, package versions and source/helper/script hashes.

[Independent verification passed](../classification/question-selection-outputs/20261113T220427919147Z/verification.json). It recalculated every held-out metric including AP/AUC, all inner candidate confusion counts and selection ties, paired changes and selected question lists. Every selector was independently refitted on verified real-only training IDs with no inner/outer evaluation student included; all 125 ranking orders and strengths matched. Recorded current RF recipes, original fold assignments, all-eight reference predictions and source/code hashes matched. No second RF-fitting run, separate software test suite or deployment fit was performed. Selector refits were verification, not new candidate searches.

### Decision

Keep the current eight-question RF for the user's priority of detecting High students. This ranking-based subset experiment did not produce a useful improvement at that priority. It does not establish that all feature-selection approaches fail or that these inputs impose a proven performance ceiling. No deployment threshold, target boundary or selected model was changed. Follow-ups motivated by these repeatedly inspected 97 students remain exploratory; synthetic labels are assumptions and warning scores are uncalibrated.

## Selected RF false-warning inspection completed, 13 November 2026

Completed separate descriptive [findings](../classification/error-analysis-outputs/20261113T215342740935Z/findings.md). Runner: `classification/diagnose-forest-errors.py`. It inspects saved predictions from the selected Small B RF with training-selected augmentation. No models, warning thresholds, inputs, scores, labels or previous experiment folders were changed. The current 87.1% recall/34.7% precision/F2 .668 reference is unchanged.

### How we counted

The original 97 students have five real held-out predictions each (485 rows). Feature comparisons count each student once, while warning frequency measures how consistently their five independently fitted outer models flag them. Repetitions reuse students and do not create independent participants. We compare Below-high students falsely warned at least once (39 unique students) with High students correctly warned at least once (16). CSVs also include persistent false warnings (>=3/5), Below-high never warned and High never warned groups. The six 1-5 inputs have means, medians and quartiles; sleep/study category codes are compared as answer distributions rather than averaged. No p-values, causal interpretations or validated feature-importance rankings are inferred from outcome-selected groups.

### Boundary and persistence findings

Of 80 Below-high students, 39 were warned at least once, 27 in at least three repetitions and 41 never. These generated 140 false-warning events (28 per repetition on average). Of 17 High students, 16 were detected at least once, 15 in at least three repetitions and one never; there were 74 correct-warning events (14.8 per repetition on average).

| Actual measured score | Real students | Warned at least once | Warned >=3/5 | Warning events across five repetitions |
|---|---:|---:|---:|---:|
| 1..<2 | 6 | 2 | 1 | 7 |
| 2..<3 | 35 | 14 | 10 | 50 |
| 3..<3.5 | 27 | 17 | 11 | 57 |
| 3.5..<3.75 | 6 | 3 | 3 | 14 |
| 3.75..<4 | 6 | 3 | 2 | 12 |
| 4..5 | 17 | 16 | 15 | 74 |

Only six of 39 distinct falsely warned students scored 3.5..<4 (15.4%). They account for 26/140 false-warning events (18.6%). Sixteen falsely warned students scored below 3, accounting for 57 events; 17 scored 3..<3.5, also accounting for 57 events. Thus 114/140 events (81.4%) involved scores below 3.5. False warnings are not primarily tiny crossings of the study's score-4 boundary. Nearness does not make a false warning correct, and Below-high does not establish absence of symptoms or a clinical diagnosis.

### Eight-input comparisons

| Input (1-5) | Mean in falsely warned Below-high group (39) | Mean in correctly warned High group (16) |
|---|---:|---:|
| Workload | 3.79 | 4.62 |
| Financial strain | 3.56 | 3.81 |
| University support | 2.31 | 1.81 |
| AI frequency | 4.28 | 4.69 |
| AI dependence | 3.08 | 3.81 |
| AI offloading | 3.08 | 3.56 |

The largest observed mean gaps among the six ordinal questions were workload (+.83 in the correctly warned High group), AI dependence (+.74) and university support (-.50). These observations do not establish significance, causation, validated selection rules or a model improvement. The RF already receives these questions. Among all 17 High students, including the missed student, means were 4.59 workload, 3.71 dependence and 1.82 support.

Sleep categories below 5 / 5-6 / 7-8 / above 8 hours contained 6/22/11/0 of the 39 false-warning students and 4/5/7/0 of the 16 correctly warned High students. Study-hour categories below 5 / 5-10 / 11-20 / above 20 weekly hours contained 12/14/10/3 and 6/5/2/3 respectively. These distributions overlap and do not support a universal simple cutoff. The High student never detected (original row 96) scored 4.083, with workload 4, AI dependence 2, AI offloading 2 and university support 2. A blanket high-AI-dependence requirement would fail to cover this case.

### Similar profiles and verification

For each falsely warned student, the script finds the three closest correctly warned High peers using the existing fixed mixed-feature distance: average of six absolute ordinal gaps/4 and two categorical mismatches. No BAT score enters the distance, but peer eligibility uses observed outcomes for this descriptive inspection. All 97 profiles are available to inspection; these comparisons must not be treated as new predictive validation or applied to model selection outside training folds. Ties use original row order. Five-times-warned examples include row 69 (actual 1.917), row 94 (2.083), row 30 (2.417), row 45 (2.750) and row 62 (2.833). Their closest High peers have distances .281/.312/.156/.188/.219. There were zero exact eight-answer patterns containing students on opposite sides of the label boundary. Approximate similarity with differing outcomes does not prove an unavoidable performance ceiling or identify missing causes.

Saved artifacts include all 97 student warning summaries with the eight inputs, 485 selected real held-out prediction rows, six score bands, 30 ordinal-summary rows, 190 answer-distribution rows, 117 nearest-peer rows, 78 paired input rows, exact-pattern checks, source/helper/script hashes and [verification](../classification/error-analysis-outputs/20261113T215342740935Z/verification.json). Independent checks reproduced all warning counts, unique-student groups, score bands, means/quantiles, category frequencies, nearest-three distances/ties, paired answers, pattern conflicts and unchanged source hashes. Original source SAV row indices are retained, with no names or timestamps exported. No new software test suite, model fitting or deployment change occurred.

### Proposed next step

A small RF input-subset comparison could test whether excluding some existing questions reduces noise. Retain all eight as the reference and learn any selection inside training validation; this is a proposal, not an improvement established by the error table. Do not select inputs globally from the table, remove difficult students, relabel cases, lower the measured High boundary or impose an AI-dependence veto. Any experiment motivated by these repeatedly inspected outer errors remains exploratory on 97 students. The selected model and its reported metrics remain unchanged.

## Current Random Forest plus logistic regression completed, 13 November 2026

Completed separate run: [results](../classification/voting-outputs/20261113T203744495093Z/results.md). Runner: `classification/train-voting.py`; settings: `classification/voting-config.json`. This experiment uses the user's current selected Small B RF with 87.1% recall, not the expanded-tuning RF. All original datasets and earlier outputs were preserved; the selected score-regression blend is unchanged.

### Error comparison and design

We compared current RF and real-only Small B logistic held-out errors on the same original stratified folds. Across five repetitions (not independent extra students), RF made 140 Below-high false warnings: logistic correctly left 56 of these unflagged and shared 84. Logistic also made 23 false warnings on Below-high cases the RF handled correctly. For High cases, both missed nine, logistic rescued two RF misses, RF rescued nine logistic misses and both detected 65. The same 97 students recur across these counts. This error inspection motivated an exploratory mixture experiment, not an independently confirmed improvement or a label-dependent correction rule.

Each outer training group retains its previously training-selected RF parameters, High weight and augmentation ratio, and real-only logistic parameters/High weight. Endpoints are refitted in each original inner training group to produce scores for inner excluded students, then fitted on the outer training group. Runtime checks reproduce original endpoint outer scores and recorded inner confusion metrics. Endpoint hyperparameters and mixture/threshold selection reuse the same four inner folds, so inner results are optimistically selected; only fully excluded outer students evaluate the complete procedure. No outer labels or scores choose a mixture or threshold.

The new score is `RF_share * RF_score + (1 - RF_share) * logistic_score`, with RF share 1/.9/.75/.5. These are weighted uncalibrated model outputs, not calibrated individual probabilities. The inputs remain the existing eight Small B answers, with measured primary score >=4 (17 High) versus <4 (80 Below-high). Generator seeds/constraints, original five repetitions of five outer/four inner folds and source data are unchanged; no new synthetic pool policy, features or students were introduced.

We select among 41 thresholds 0..1 by .025 using two rules. `ensemble_f2` maximizes inner F2, precision, recall, threshold and finally RF share. `ensemble_recall_guard` requires inner recall at least the current RF's recorded inner recall, minimizes FP, then favors recall, precision, F2, threshold and RF share. Its training recall constraint does not guarantee outer recall. Both have matched controls restricting RF share to 1, so threshold adjustment alone can be distinguished from mixing. Including share 1 and original thresholds guarantees an eligible reference choice, not improved outer results.

### Results

Metrics and counts average five dependent repetitions of the same 97 real students. Only real held-out students enter evaluation.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 | Average precision |
|---|---:|---:|---:|---:|---:|---:|
| Current selected RF | **87.1%** | 34.7% | .667848 | **14.8** | 28.0 | .526861 |
| RF-only finer threshold, F2 rule | **87.1%** | 34.8% | .669090 | **14.8** | 27.8 | .526861 |
| RF-only finer threshold, recall guard | **87.1%** | 34.8% | .669090 | **14.8** | 27.8 | .526861 |
| RF/logistic mixture, recall guard | 85.9% | 35.7% | **.669893** | 14.6 | 26.4 | .535924 |
| RF/logistic mixture, F2 rule | 83.5% | 37.2% | .666125 | 14.2 | 24.4 | .568017 |
| Real-only logistic reference | 78.8% | **39.0%** | .651360 | 13.4 | **21.4** | .553761 |
| Existing blend, tuned warning trigger | 80.0% | 37.8% | .652825 | 13.6 | 22.4 | **.576509** |

The recall-guard mixture removes 1.6 false warnings per evaluation but detects .2 fewer High students than the current RF. Its precision increases about 1.1 percentage points, recall falls about 1.2 points and F2 rises .002045. Relative to the RF-only threshold control, it removes 1.4 false warnings while detecting .2 fewer High students. The guarded ensemble chooses pure RF in 19/25 fits, RF share .9 in five and .75 in one. F2-selected mixing chooses pure RF in 16/25, .9 in four, .75 in one and .5 in four. The F2-selected ensemble improves average precision but loses more High recall; neither new mixture establishes a uniform improvement over the current RF.

Both RF-only threshold controls yield identical predictions and change only one false warning across all five repetitions: repetition 2 drops from 30 to 29 false positives with 16 High detections unchanged. Other repetitions are identical to the selected RF. This gives 27.8 rather than 28.0 mean false warnings and .669090 rather than .667848 mean F2. It is a tiny exploratory change, not evidence of a substantial upgrade or improved score ranking; average precision is unchanged because underlying RF scores are unchanged.

### Verification and current decision

The complete folder saves 3,395 predictions across seven procedures, 35 repetition metric rows, seven summaries, confusion matrices, 485 matched endpoint error-comparison rows, ten error-overlap rows, 25 outer training records containing endpoint choices/inner scores/all 4,100 share-threshold candidates/100 selected rules, 50 paired comparisons, inner/outer fold assignments, configs and hashes. [Independent verification passed](../classification/voting-outputs/20261113T203744495093Z/verification.json). It recomputed all reported metrics including AP/AUC, every inner candidate's threshold confusion arithmetic and selection ties, all mixed outer predictions directly from original endpoint scores, the error overlap, paired changes, original endpoint choices/folds and unchanged source/code hashes.

The first attempt completed fitting but its reused report helper expected a different reference set and stopped. The report was corrected, the run repeated, and verification confirmed identical predictions and tuning choices between attempts. The incomplete generated folder was removed after verification; the complete run above is the retained result. No separate software test suite, calibration or final deployment fit was performed.

Keep the user's selected current RF for High detection. The threshold-only refinement can be retained as a very small alternative; combining models did not establish a substantial upgrade at the same observed recall. A switch to guarded mixing would accept slightly fewer High detections for fewer false warnings. These choices should not be made by selecting a particular outer fold's settings or threshold. Scores remain uncalibrated, synthetic labels remain assumptions and repeated experimentation on 97 students remains exploratory. No numerical regression MAE improvement is claimed.

## Focused Random Forest tuning completed, 13 November 2026

Separate completed run: [results](../classification/forest-tuning-outputs/20261113T154534173272Z/results.md). Runner: `classification/train-forest-tuning.py`; settings: `classification/forest-tuning-config.json`. Source datasets, SPSS analyses, the selected RF and earlier result folders were preserved. The previously deleted balanced experiment was not restored.

### Question and procedure

We tested whether focused tuning of the selected Small B Random Forest could reduce false warnings while preserving High detection. Inputs remain the same eight existing answers; the target remains measured primary burnout score >=4 (17 real High) versus <4 (80 real Below-high). The 97 students, five repetitions of five stratified outer/four inner folds, generator constraints and generator seeds match the retained augmentation run. All 125 synthetic training pools reproduced the previously saved Small B profiles exactly. These 1,360 repeated-fit profile instances are not new independent students. No forced balancing or additional predictors were added.

Each outer training group compares 108 configurations: tree depth 2/3/5 x minimum leaf size 5/10 x `max_features` sqrt/all encoded columns x High weight 1/2/4 x augmentation none/half/full. Forests retain 100 trees, original deterministic model seeds and one computational thread. Each configuration produces four-fold real inner out-of-fold scores. The same scores support 41 warning thresholds, 0..1 in .025 steps, and two joint parameter/weight/augmentation/threshold selection rules:

1. `expanded_f2`: maximize inner F2; ties favor precision, recall, higher threshold, less augmentation and stable candidate order.
2. `recall85_min_fp`: require pooled real inner recall >=.85, then minimize false positives; ties favor recall, precision, F2, higher threshold, less augmentation and stable order.

With 13/14 High students in each outer training group, the inner recall target requires detecting 12: 92.3% or 85.7%. Threshold zero guarantees an eligible candidate. This is a training constraint, not a guarantee on excluded students. Preprocessing, sample weighting, generation and all selections use training data only; outer students evaluate the complete rule. The expanded grid contains the previous settings and thresholds, and its best inner F2 must be at least the old selected procedure's. Higher optimized inner F2 does not guarantee better outer performance.

### Results

All means below average five dependent repetitions of the same students. Fractional counts describe those averages.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 | Average precision |
|---|---:|---:|---:|---:|---:|---:|
| Current RF, selected augmentation | **87.1%** | 34.7% | .667848 | **14.8** | 28.0 | .526861 |
| RF, expanded F2 tuning | 84.7% | 37.1% | **.673374** | 14.4 | 24.6 | .484384 |
| RF, inner recall constraint then minimum FP | 82.4% | **38.0%** | .667767 | 14.0 | **22.8** | .492527 |
| RF, real-only reference | 84.7% | 32.7% | .642644 | 14.4 | 29.6 | .482449 |
| Existing blend, training-selected trigger | 80.0% | 37.8% | .652825 | 13.6 | 22.4 | .576509 |

Expanded F2 tuning increased precision by 2.4 percentage points and reduced false warnings by 3.4 at a cost of .4 fewer High detections per evaluation. Its recall fell by 2.4 points, while mean F2 increased by .005526. F2 was higher in three repetitions and lower in two; false warnings were lower in all five. Repetition recall ranged 76.5%..88.2%, and F2 .5963..7212. This is a modest mean trade-off, not an independently confirmed improvement.

The constrained rule reduced false warnings by 5.2 and increased precision by 3.4 points, at a cost of .8 fewer High detections: a 4.7-point recall decrease. Its 82.4% outer recall did not meet the 85% inner target, illustrating the lack of an outer guarantee. F2 was effectively tied with the selected procedure, slightly lower before rounding. Its repetition recall ranged 70.6%..88.2%. Both new rules had lower average precision than the selected RF, so the changes do not demonstrate a uniform gain in discrimination. Adjustments concern classification warnings, not regression MAE or validated clinical risk.

Both rules selected augmentation none/half/full in 8/10/7 of the 25 fits (the selected configurations need not be identical). Expanded F2 selected depth 2/3/5 in 16/4/5 fits and sqrt/all encoded inputs in 13/12; the constrained rule selected depth 2/3/5 in 15/4/6 and sqrt/all in 17/8. Warning thresholds ranged .175..625 and .150..600 respectively. These frequencies and ranges are descriptive; they must not be used to choose one final setting by looking at outer performance.

### Artifacts and independent checks

The complete folder contains 2,425 held-out predictions across five procedures, 25 repetition metric rows, five summaries, confusion matrices, 30 paired comparisons, all 2,700 candidates with saved inner scores and 110,700 threshold metric rows, 50 chosen outer training configurations, original inner/outer assignments, generated profiles/counts, configs, package versions and hashes. Real-only RF, the selected augmentation RF and the threshold-tuned blend are unchanged matched-fold references.

[Independent verification passed](../classification/forest-tuning-outputs/20261113T154534173272Z/verification.json). It recalculated all held-out metrics including tied-score average precision and ROC AUC; reconstructed every candidate's threshold confusion counts/metrics from saved inner scores; independently checked both global selection rules and ties, all 50 winners, selected thresholds and 30 paired changes. It reproduced all 25 previous selected candidates' inner threshold metrics, all 125 generator pools, original fold assignments and unchanged reference predictions. Source/code hashes, training-only parent provenance, categorical blocks, ordinal interpolation, distances, answer domains and within-pool novelty passed. One generated profile instance coincidentally matched an excluded real profile, as in the retained reference; excluded profiles were not consulted during generation or used to filter rows. No second model fitting run or separate software test suite was performed.

### Current decision

Retain the user's selected RF with training-selected augmentation for the priority of catching High students. Keep expanded F2 tuning as a recorded alternative with fewer false warnings and slightly fewer detections. A switch would be an explicit choice of trade-off, not a clear improvement on every main metric. The numerical score predictor remains the existing ridge/SVR blend. No deployment artifact or final threshold was saved. All results remain exploratory after repeated tuning on 97 real students; synthetic labels are assumptions and weighted classifier scores are uncalibrated.

## Selected classification model, 13 November 2026

The user selected Small B Random Forest with training-selected augmentation as the classification candidate, prioritizing High detection: 87.1% recall, 34.7% precision, F2 .668 and 28.0 false warnings per 80 Below-high students. These are five-repetition averages from the retained synthetic augmentation run below. The selected ridge/SVR blend remains the numerical score predictor. No deployment model or final warning threshold has been saved.

## Synthetic binary augmentation completed, reviewed 13 November 2026

Completed separate run: [full results](../classification/augmentation-outputs/20261112T125001425382Z/results.md), generated on 12 November. Runner: `classification/train-augmentation.py`; settings: `classification/augmentation-config.json`. The run finished before the interrupted session resumed. Original datasets, SPSS work and earlier experiments were preserved.

### What we compared

The outcome remains primary measured score >=4 (17 High students) versus <4 (80 Below-high). This is a study-defined boundary, not a clinical diagnosis. Logistic regression, Random Forest, XGBoost and histogram gradient boosting each use Small B (8 answers) and Broad D (23), without BAT predictors or new questionnaire inputs. Their real-only references, exact hyperparameter grids, weights, F2 threshold tuning and five repetitions of five stratified outer/four inner folds match the pinned binary run. Reference helpers, packages and fold assignments were verified unchanged.

Within each real training fit, nearby High parents generate new ordinal answer combinations by stochastic rounding of interpolation. The full nominal/binary answer block is copied from one real parent. Constraints restrict parent distance, ordinal gaps and distance from the anchor; exact matches to any real training or accepted synthetic profile are rejected. Synthetic labels are inherited High assumptions, not measured BAT outcomes. Generation never sees validation or outer test profiles. Preprocessing, model settings, weights and warning thresholds are fitted/selected inside training groups. Only real excluded students enter evaluation.

The half batch adds ceil(.5 times the real High training count); the full batch adds one per real High student. Both are independently tuned. An additional procedure chooses no/half/full augmentation by inner F2, precision, recall, threshold and finally lower batch ratio. This batch selection never uses outer results. Fixed-batch results also appear in the full report; choosing the best fixed batch after reading that report would be a further exploratory choice.

### Main results

Metrics/counts average five dependent repetitions of the same 97 students; fractional counts are averages. F2 favors detection of High students while penalizing false warnings.

| Inputs and procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Small B XGBoost, training-selected augmentation | 85.9% | 35.8% | .670 | 14.6 | 26.4 |
| Small B forest, training-selected augmentation | 87.1% | 34.7% | .668 | 14.8 | 28.0 |
| Broad D logistic, training-selected augmentation | 82.4% | 37.1% | .661 | 14.0 | 24.0 |
| Existing ridge/SVR blend, training-selected warning trigger | 80.0% | 37.8% | .653 | 13.6 | 22.4 |
| Small B XGBoost, real-only | 83.5% | 33.4% | .642 | 14.2 | 28.4 |

Augmentation modestly improved some procedures, but not all. Small B XGBoost's selected augmentation improved its own real-only mean F2 by about .028, detected .4 additional High students and made two fewer false warnings on average. Its F2 was higher than real-only XGBoost in four repetitions and lower in one. Relative to the existing blend, it caught one additional High student but made four additional false warnings; F2 was higher in three repetitions and lower in two. Its repetition F2 ranged .619 to .721. The leading mean F2 therefore does not establish a reliable overall winner.

Other training-selected augmentation results were: Small B logistic .632 F2 (75.3% recall/39.0% precision), Small B histogram .604 (71.8%/37.3%), Broad D forest .624 (74.1%/38.4%), Broad D XGBoost .613 (72.9%/37.4%) and Broad D histogram .586 (76.5%/30.3%). This illustrates why synthetic generation should be evaluated rather than assumed helpful. For the leading Small B XGBoost procedure, the 25 training groups selected no augmentation five times, half seven times and full thirteen times. These frequencies are descriptive, not a basis for setting one final batch size from outer results.

### Saved data and verification

All 2,720 requested synthetic profile instances were generated across 250 inner/outer training pools in 3,087 attempts, with no shortfalls. These pools overlap across repeated fits; they are not 2,720 independent extra students. The full nominal/binary parent block and each ordinal value, interpolation fraction, distances, High parent labels, parent membership in training, and novelty within each training pool were independently checked. One generated profile coincidentally matched an excluded real profile; it was not copied from it or filtered against it. Enforcing novelty against excluded profiles would consult evaluation inputs. The guarantee concerns each fit's own training records and generated pool, not every real participant globally.

The completed folder contains configurations, manifest, 17,460 held-out predictions, 180 repetition metrics, 36 summary rows, confusion matrices, paired comparisons, outer/inner assignments, all 600 tuning records, generation counts and synthetic profiles with parent/fold provenance. [Independent verification](../classification/augmentation-outputs/20261112T125001425382Z/verification.json) reproduced metric arithmetic including tied-score AUC/average precision; checked candidate threshold metrics and all parameter/threshold/batch winners; checked selected-procedure predictions against their chosen source; and confirmed original folds, code/package compatibility with the reference and unchanged source hashes. This verification did not rerun model fitting or a separate software test suite.

### Decision and next step

Keep the user's selected ridge/SVR blend for numerical score prediction. Retain augmented Small B XGBoost as a promising warning candidate, alongside the blend with its training-selected trigger. The next decision is whether detecting about one extra High student justifies roughly four extra false warnings per 97 students. These classification results do not reduce regression MAE. Most warnings remain false relative to >=4; weighted classifier outputs are not calibrated personal risk probabilities.

Novel legal profiles do not establish realistic human responses or correct labels. Augmentation also changes training emphasis; there is no matched-extra-weight control to isolate its mechanism. All comparisons reuse the same 97 real students after many experiments, so they remain exploratory. No deployment model or final warning threshold was saved, and no synthetic records were appended to the SAV, source CSV or SPSS analyses.

## Binary warning classification completed, 12 November 2026

Completed separate run: `classification/binary-outputs/20261112T115553112588Z/`. Runner: `classification/train-binary.py`; settings: `classification/binary-config.json`. The user selected the previous fixed 50/50 High-priority Small B ridge / Broad D SVR blend for score prediction. This experiment evaluates a warning function alongside it; it does not replace or improve the saved regression MAE results.

### Outcome and evaluation

The primary measured score defines High >=4 (17 students) versus Below-high <4 (80 students). Below-high does not mean no risk. These are study-defined symptom groups, not validated clinical diagnoses. Logistic regression, Random Forest, XGBoost and scikit-learn histogram gradient boosting each use Small B and Broad D, without BAT predictors, new questions or synthetic records.

All methods share five stratified outer folds repeated with the original five seeds, with four stratified inner folds. These are new assignments, different from the regression and three-class runs. Preprocessing is fitted within training groups. The selected 50/50 regression blend is retuned/refitted on the same new folds using its existing endpoint selection rules. Historical predictions from different folds are not substituted. The old regression MAEs should not be read as metrics of these newly refitted models.

Each classifier jointly tunes settings, normalized High weights 1/2/4 and warning thresholds 0..1 in .05 steps. The objective is pooled inner F2 = 5TP/(5TP+4FN+FP), favoring recall while penalizing false warnings; ties favor precision, recall, a higher threshold and stable grid order. The blend retains 50/50 mixing and its previous High-MAE endpoint tuning; its warning threshold alone is tuned on inner out-of-fold scores using the configured score grid. A separate cutoff-4 result is reported. The same selected classifiers at .5 are diagnostics, not independently tuned .5 models. Full grids and fixed settings are documented in `classification/README.md` and the saved config. No solver warning stopped the run.

### Results with training-selected thresholds

Counts below average the five repetitions of these same 97 students. TP/FP counts may be fractional; each single repetition has integer counts.

| Inputs | Method | High recall | High precision | F2 | True warnings /17 | False warnings /80 |
|---|---|---:|---:|---:|---:|---:|
| Small B + Broad D | Refitted 50/50 ridge/SVR blend | 80.0% | 37.8% | .653 | 13.6 | 22.4 |
| Small B | Logistic regression | 78.8% | 39.0% | .651 | 13.4 | 21.4 |
| Small B | Random Forest | 84.7% | 32.7% | .643 | 14.4 | 29.6 |
| Small B | XGBoost | 83.5% | 33.4% | .642 | 14.2 | 28.4 |
| Small B | Histogram boosting | 74.1% | 33.3% | .593 | 12.6 | 25.6 |
| Broad D | Logistic regression | 77.6% | 34.5% | .618 | 13.2 | 25.8 |
| Broad D | Random Forest | 77.6% | 36.9% | .633 | 13.2 | 23.0 |
| Broad D | XGBoost | 74.1% | 35.4% | .608 | 12.6 | 23.0 |
| Broad D | Histogram boosting | 75.3% | 29.1% | .570 | 12.8 | 31.2 |
| Baseline | Flag everyone | 100.0% | 17.5% | .515 | 17.0 | 80.0 |
| Baseline | Flag no one | 0.0% | 0.0% | .000 | 0.0 | 0.0 |

Undefined precision is reported as zero. The full report includes all .5 diagnostics, fixed-cutoff blend, ROC AUC, average precision, false-positive rates and other metrics. Average precision was .577 for the blend and .554 for Small B logistic, versus .175 for constant-score baselines; these describe discrimination, not calibrated personal risk probabilities.

### What changed and what did not

The threshold-tuned blend had the largest mean F2, but .653 versus logistic's .651 is essentially a tie in this small exploratory comparison. Logistic was higher in two repetitions and lower in three. Its F2 ranged .550 to .694; the blend ranged .600 to .701. These repeated scores are dependent, not independent confirmation of a winner. Histogram boosting did not improve this warning objective over the other leading options.

The most important change was the warning trigger. On the same newly refitted blend scores, cutoff 4 produced 25.9% recall and 62.1% precision (4.4 true warnings/2.6 false warnings on average). Training-selected thresholds produced 80.0% recall and 37.8% precision (13.6 true/22.4 false). In simple terms, the tuned procedure catches roughly 14 of the 17 High students, while also flagging roughly 22 of the 80 Below-high students. Most warnings are therefore false relative to this study's measured-score boundary. This is a detection/false-warning trade-off, not better numerical score predictions.

Measured High remains >=4 throughout. The blend's prediction trigger was chosen between 3.1 and 3.8 in different outer training groups; that does not redefine High. Do not select a single final threshold from these outer results or use the modal value as an independently validated setting. A final threshold would require the specified training-only procedure on the full training data and later evaluation outside this development history.

Recommendation: retain the user's selected regression blend and treat its training-tuned warning function as a promising research option. Small B logistic is a simpler alternative with very similar results. The new classifiers did not establish a clear improvement over a threshold-tuned blend. Whether approximately 38% precision and this false-warning burden are acceptable has not been established; no clinical readiness claim is supported. Weighted classifier outputs are uncalibrated and must not be presented as validated individual burnout-risk percentages.

### Saved files and checks

The manifest is complete. The separate folder saves 9,700 held-out predictions, scores/labels/thresholds, outer and inner fold assignments, repetition/summary metrics, confusion matrices, repetition spread, paired changes against both blend procedures, all 225 tuning records, configurations and source hashes. Original source data and earlier outputs remain unchanged.

Runtime assertions checked probability bounds, class/score alignment, threshold decisions, train/test exclusion and complete unique predictions. A separate standard-library calculation reproduced all 100 repetition metrics and 20 summary rows, including ROC AUC and average precision from ranks. It verified every classifier's recorded candidate threshold counts and selection ties, all 225 tuning selections, inner/outer exclusion, output counts and recorded source hashes. No separate software test suite or deployment model was run. This follows many experiments on the same 97 students and remains exploratory; repetitions do not create extra real students or independent validation.

## Overall-MAE loss tuning completed, 11 November 2026

**Historical record: experiment code/configuration/outputs were deleted on 16 November 2026. The following methods, results and checks are retained for reporting; named paths are former locations.**

Completed separate run: `analysis/outputs/loss-tuning-experiments/20261111T163814733223Z/`. Runner: `analysis/scripts/train-loss-tuning.py`; configuration: `analysis/loss-tuning-config.json`. Previous outputs and source data were preserved. This experiment focuses on overall MAE; High errors are secondary diagnostics, not a separate tuning objective.

### Methods and tuning

Six methods were tuned separately on the existing Small B/Broad D inputs and primary continuous burnout score: gradient boosting with squared-error, absolute-error or Huber loss; linear median regression; linear Huber regression; and refined PCA + ridge. There are no BAT predictors, new questionnaire inputs, synthetic records or High sample weights.

Boosting compares 50/150 trees, learning rates .03/.1 and depths 1/2, with minimum leaf size 10, full sampling and no early stopping. Huber boosting alpha is fixed at .9. Linear median regression uses quantile .5, HiGHS and L1 alpha 0/.01/.1/1; it predicts from each student's inputs and is not the constant median baseline. Linear Huber tunes alpha .01/1/10 and epsilon 1.1/1.35/1.75, fitting a robust residual scale, with 10,000 maximum iterations and tolerance 1e-6. PCA ridge tunes counts 1/2/3/4/5/6/8 within centered training-rank limits and ridge alpha .01/.1/1/10/100/1000. All grids were fixed before this run. Huber's treatment of large residuals does not imply better performance on genuinely high scores.

The original five outer folds repeated five times and four inner folds are retained. Standard encoding/scaling and PCA are fitted inside each training group only. PCA uses full SVD without whitening, with cached leading prefixes. All candidate settings minimize mean inner-fold overall MAE with stable grid-order ties. A separate `inner_family_selector` chooses the family/settings by those same inner scores within each input set. Outer outcomes never choose its settings or family. Predictions are bounded to 1..5, retaining raw values. The same 97 real students are evaluated in each repetition, including 17 with actual scores >=4.

### Results in score points (smaller is better)

| Method | Small B overall MAE | Small B High MAE | Broad D overall MAE | Broad D High MAE |
|---|---:|---:|---:|---:|
| Boosting: squared error | .6133 | .9979 | .6140 | 1.0603 |
| Boosting: absolute error | .6231 | 1.1074 | .6157 | 1.1077 |
| Boosting: Huber | .6111 | 1.0216 | .6102 | 1.0514 |
| Linear median | .6027 | .9605 | .6024 | 1.0948 |
| Linear Huber | .6050 | .7618 | .7555 | .7914 |
| Refined PCA + ridge | .5998 | .9156 | .5755 | .8969 |
| Inner family selector | .6025 | .9282 | .5850 | .9443 |

Saved references: ordinary Small B ridge .5883 overall/.9329 High; ordinary Broad D ridge .5933/.9281; previous ordinary Broad D PCA + ridge .5748/.8991; fixed ridge/SVR blend .6160/.6422. The complete report also includes lower-score MAE, High-within-.5 accuracy and other diagnostics. High >=4 and lower <2.5 are descriptive groups, not clinical categories.

### Interpretation

None of the new procedures improved overall MAE over the previous ordinary Broad D PCA + ridge. Refined Broad D PCA + ridge was effectively tied: .0007 higher overall MAE and .0022 lower High MAE. Versus that reference it had one repetition with lower overall error, two with higher error and two ties. This is not evidence of a useful improvement.

The lowest overall boosting MAE was Broad D Huber (.6102), with High MAE 1.0514. Training directly with absolute-error loss did not improve held-out MAE here. Broad D linear median had no High predictions within .5 points, despite optimizing a loss aligned with MAE. Changing the training loss cannot guarantee better predictions for a different score group or on unseen students.

Inner family selection chose PCA + ridge in 22/25 Broad D fits and 19/25 Small B fits. Its Broad D MAE was .5850, worse than the saved PCA-only procedure (.5748); trying more families did not improve the complete selection procedure. These counts describe dependent fits, not independent evidence about model superiority.

Fold-level training/held-out MAE for Broad D linear Huber averaged .3879/.7553, while refined Broad D PCA + ridge averaged .5179/.5753. The more flexible fit's lower training error did not carry over to excluded students. These diagnostics describe a generalization gap, not proof of its cause or an irreducible error limit. Fold averages differ slightly from pooled repetition MAE because fold sizes differ.

Recommendation: keep the previous ordinary Broad D PCA + ridge as the overall-error reference. Retain the earlier fixed blend and high-priority PCA options when discussing the high-score trade-off. No method in this run improves both errors over the blend, and no new overall-error winner has been established.

### Checks and saved outputs

The manifest is complete; no convergence warning stopped the run. Runtime assertions checked training/test separation, component limits, finite complete predictions, score/error alignment, prediction bounds, original folds and unchanged recorded source hashes. A separate standard-library calculation verified all 18 summary rows from 8,730 saved predictions, all 300 chosen settings against their candidate scores, all 50 family selections and their prediction copies, plus source hashes. Counts of tuning, diagnostics and paired-comparison records were checked. No separate software test suite was run.

The separate folder saves `results.md`, held-out predictions, repetition and summary metrics, paired comparisons with input-matched ridge/previous Broad D PCA/blend, training/inner/outer diagnostics, every candidate and selected setting, configs and the hash manifest. No deployment model or weights were saved. Repeated exploration of the same students limits confidence in small differences; these remain exploratory results, not independent validation of a final model.

## Feature extraction completed, 11 November 2026

**Historical record: experiment code/configuration/outputs were deleted on 16 November 2026. The following methods, results and checks are retained for reporting; named paths are former locations.**

Completed separate run: `analysis/outputs/extraction-experiments/20261111T113950457894Z/`. Runner: `analysis/scripts/train-extraction.py`; configuration: `analysis/extraction-config.json`. Earlier outputs and source data were preserved.

### What we tried

We compressed the existing Small B and Broad D answers into mathematical components, then predicted the primary continuous burnout score. PLS learns components using training answers and training scores; PCA learns components using training answers alone. PCA components feed ridge or SVR. These are combinations of existing answers, not additional survey questions or validated psychological scales. No BAT predictors or synthetic records were used.

The comparison retained the original five outer folds repeated five times, with four inner folds for choosing settings. Encoding, scaling and extraction are fitted separately inside training groups. Counts 2/3/5/8 are eligible only within the minimum centered training-matrix rank. PCA uses full SVD without whitening; PLS disables internal scaling after the existing StandardScaler. PCA prefixes are cached without changing their leading directions.

Each family has ordinary and High-priority tuning. Ordinary minimizes mean inner-fold overall MAE. High-priority minimizes pooled inner High MAE among candidates within .05 pooled overall MAE of ordinary, using existing tie rules and ordinary fallback without High cases. PCA regressors also tune normalized High weights 1/2/4; extraction and scaling stay unweighted. PLS does not use sample weights: its High-priority version only changes the component count selected. The inner tolerance does not guarantee an outer error bound.

### Results in score points (smaller is better)

| Inputs | Method | Tuning | Overall MAE | High MAE (>=4) | Lower MAE (<2.5) | High within .5 |
|---|---|---|---:|---:|---:|---:|
| Small B | PLS | Ordinary | .6049 | .7439 | .9649 | 40.0% |
| Small B | PLS | High-priority | .6037 | .7495 | .9611 | 38.8% |
| Small B | PCA + ridge | Ordinary | .5955 | .9093 | .9858 | 18.8% |
| Small B | PCA + ridge | High-priority | .6339 | .6274 | 1.0856 | 40.0% |
| Small B | PCA + SVR | Ordinary | .6097 | .9098 | .9880 | 16.5% |
| Small B | PCA + SVR | High-priority | .6465 | .6881 | 1.1465 | 34.1% |
| Broad D | PLS | Ordinary | .6206 | .7285 | .8937 | 37.6% |
| Broad D | PLS | High-priority | .6517 | .7543 | .9424 | 38.8% |
| Broad D | PCA + ridge | Ordinary | .5748 | .8991 | .8956 | 21.2% |
| Broad D | PCA + ridge | High-priority | .6026 | .6638 | .9930 | 42.4% |
| Broad D | PCA + SVR | Ordinary | .6003 | .9510 | .9321 | 16.5% |
| Broad D | PCA + SVR | High-priority | .6414 | .6955 | 1.0430 | 34.1% |
| Existing input union | Previous fixed blend | 50/50 | .6160 | .6422 | 1.1440 | 44.7% |

### What changed

Broad D ordinary PCA + ridge improves overall MAE from the input-matched original ridge's .5933 to .5748 and High MAE from .9281 to .8991. High-score errors remain substantial. This ordinary procedure has the lowest overall MAE among the twelve new procedures and their saved references.

Broad D high-priority PCA + ridge gives a useful alternative balance: .6026 overall/.6638 High versus the blend's .6160/.6422. Its overall error is .0134 lower, High error .0216 higher, and lower-score error .1510 lower. Small B high-priority PCA + ridge has the lowest High MAE among these twelve new procedures (.6274), but its overall error is .0179 worse than the blend and its High-within-.5 proportion is lower (40.0% versus 44.7%). Lower average High error does not mean every High-detection measure improves.

Recommendation: keep Broad D high-priority PCA + ridge alongside the fixed blend as a promising balance; retain ordinary Broad D PCA + ridge as the overall-error reference. No new procedure beats the blend on both overall and High MAE. These results do not establish a large improvement in High prediction or a final validated model.

### Checks and saved files

The manifest is complete. Runtime assertions checked training/test separation, component-rank limits, finite complete predictions, source-score alignment, original fold equality across four earlier runs and unchanged recorded source hashes. A separate calculation from saved predictions reproduced all 17 summary rows (12 new procedures and 5 references), covering 8,245 predictions; source hashes were checked again after completion. No separate software test suite was run.

The folder contains `results.md`, real held-out predictions, repetition and summary metrics, paired comparisons with ridge/blend, training/inner/outer diagnostics, extraction directions, PCA variance and selected settings in `tuning.json`, configurations and the hash manifest. Directions alone are not deployable models. Repetitions reuse the same 97 students, including only 17 High students; they are not independent replications. This experiment follows earlier inspection of these students, so small best-looking differences remain exploratory. No deployment model or prospective warning validation was created.

## Model experiments completed, 2 November 2026

### Elastic Net, question-selected SVR and fit diagnostics

Completed run: `analysis/outputs/feature-selection-experiments/20261102T163807090063Z/`. Runner: `analysis/scripts/train-feature-selection.py`; configuration: `analysis/feature-selection-config.json`. Eight procedures compare Elastic Net and question-selected SVR on Small B/Broad D with ordinary/high-priority tuning. Existing inputs and the primary continuous score are retained. There are no new questionnaire variables, engineered interactions, BAT predictors, synthetic records or additional participants.

The original five outer folds repeated five times and four inner folds were used. Standard encoding/scaling is fitted in each training fit. Direct Elastic Net tunes alpha .001/.01/.1/1 and l1 ratio .2/.8/1. Selected SVR uses the previous C/gamma/epsilon grid and selects 4/8/all original questions, deduplicating counts for Small B. Within each inner training group, an Elastic Net selector with fixed alpha .03/l1 ratio .8 ranks questions by the L2 norm of their standardized encoded coefficients divided by sqrt(number of encoded columns). Category columns for each original question stay together. Equal ranks retain original question order. Both selector and predictor use normalized training-only High sample-weight factors 1/2/4; all-input SVR remains eligible.

Ordinary tuning minimizes mean inner-fold overall MAE with factor 1. High-priority tuning minimizes pooled inner High MAE among candidates within .05 pooled overall MAE of ordinary; ties use overall error, lower weight and stable grid order. Without High cases, use ordinary. Neither outer scores nor full-data correlations choose questions or settings. Convergence warnings are treated as errors, and none stopped this completed run.

| Inputs | Family | Procedure | Overall MAE | High MAE (>=4) | Lower MAE (<2.5) | High within .5 |
|---|---|---|---:|---:|---:|---:|
| Small B | Elastic Net | Ordinary | .5945 | .9098 | 1.0207 | 20.0% |
| Small B | Elastic Net | High-priority | .6232 | .6442 | 1.1498 | 40.0% |
| Small B | Question-selected SVR | Ordinary | .6178 | .9106 | 1.0465 | 20.0% |
| Small B | Question-selected SVR | High-priority | .6222 | .6706 | 1.1550 | 38.8% |
| Broad D | Elastic Net | Ordinary | .5999 | 1.0234 | .9779 | 4.7% |
| Broad D | Elastic Net | High-priority | .6408 | .6826 | 1.0865 | 41.2% |
| Broad D | Question-selected SVR | Ordinary | .6260 | .9975 | 1.0242 | 15.3% |
| Broad D | Question-selected SVR | High-priority | .6438 | .6312 | 1.1455 | 47.1% |
| Existing input union | Previous fixed blend | 50/50 | .6160 | .6422 | 1.1440 | 44.7% |

Errors average repetition metrics on the same 97 students (17 measured >=4). Broad D high-priority selected SVR lowers High MAE .0110 relative to the previous blend, at .0277 higher overall MAE. Small B high-priority Elastic Net is close to the blend but has slightly higher overall and High errors. Against earlier weighted ridge (.6282 overall/.6649 High), Small B high-priority Elastic Net improves both averages modestly, but does not improve both over the blend. None of the eight procedures has lower overall MAE than input-matched original ordinary ridge (.5883 Small B/.5933 Broad D). Results do not demonstrate a large accuracy improvement.

Training-versus-evaluation diagnostics use mean fold MAE (distinct from pooled repetition MAE). Broad D high-priority selected SVR averages .4398 in-sample and .6441 excluded-student error, a .2044 gap. Broad D ordinary selected SVR has a .1943 gap. Small B high-priority Elastic Net averages .5448 training/.6235 excluded, a .0786 gap. These gaps suggest that additional flexibility deserves caution, while appreciable training errors remain for simpler models. A gap alone cannot establish memorization, data noise, or an irreducible information limit.

In Broad D high-priority SVR, AI dependence was selected in 25/25 outer fits, avoidance 24/25 and workload 21/25. These are descriptive selection frequencies across dependent repetitions, not causal effects, stable clinical predictors or a full-data rule for later evaluation. The complete selection-frequency CSV and fold-level chosen question lists are saved.

The manifest is complete. Runtime assertions verified original folds, complete finite predictions, grouped encoding, selected-question membership, score alignment and unchanged source hashes. Previous runs and source data remain unchanged. Predictions, repeat/summary metrics, paired differences, training/inner/outer diagnostics, all candidates and selected questions are saved. No separate software test suite or deployment model was run. This is another exploratory same-sample follow-up, not independent validation of a final winner.

### Ridge/SVR prediction blending

Completed run: `analysis/outputs/ensemble-experiments/20261102T163006135317Z/`. Runner: `analysis/scripts/train-ensemble.py`; configuration: `analysis/ensemble-config.json`. This combines the previous high-priority Small B ridge and Broad D SVR using only existing survey variables and real students. The primary continuous score is the outcome; no new questionnaire features, BAT inputs or synthetic records were introduced.

The original five outer folds repeated five times and four inner folds were retained. Inside each outer training group, both base models retain their earlier inner parameter/weight selection. Their selected configurations produce clipped inner out-of-fold predictions, used to choose SVR share 0/.25/.5/.75/1 (ridge share is the remainder). The selection objective is lowest pooled inner High MAE within .05 pooled overall MAE of ordinary Small B ridge, breaking ties by overall MAE then smaller SVR share. Without High students it minimizes overall MAE. Endpoint shares are eligible. Inner validation is reused for base hyperparameters and blend share; the excluded outer groups evaluate the complete procedure. A fixed 50/50 blend, specified before this run, is reported separately and has no blend-share tuning.

| Procedure | Overall MAE | High MAE (>=4) | High underestimation | Lower MAE (<2.5) | High within .5 |
|---|---:|---:|---:|---:|---:|
| Weighted ridge | .6282 | .6649 | .6160 | 1.1699 | 41.2% |
| High-priority SVR | .6282 | .6705 | .6650 | 1.1180 | 37.6% |
| Fixed 50/50 blend | .6160 | .6422 | .6277 | 1.1440 | 44.7% |
| Inner-selected blend | .6343 | .6664 | .6428 | 1.1370 | 41.2% |

Errors average five repetition metrics on the same 97 students, including 17 measured >=4. The fixed half blend lowered overall MAE by .0122 and High MAE by .0228 relative to weighted ridge. It lowered both errors relative to SVR as well. This is a modest numerical improvement, not proof of a clinically useful or independently superior model. Average high underestimation was slightly higher than ridge despite lower High absolute error. Original ordinary Small B ridge still has lower overall MAE (.5883), with higher High error (.9329).

The adaptive selected blend did not lower both overall and High MAE relative to either endpoint. It selected SVR share 0 in seven outer fits, .25 in two, .5 in five, .75 in four and 1 in seven. Its poorer result should remain visible rather than claiming that automatically tuned ensembling improved prediction.

Endpoint error correlation averaged .900 across all students and .775 within High students. Opposite error signs occurred in 13.8% overall and 17.6% of High cases. Both models missed by more than .5 in 52.9% of High cases, explaining why averaging offers limited correction. These diagnostics use excluded-student predictions descriptively and did not choose settings.

Runtime assertions reproduced both previous endpoints and original fold assignments, checked finite/complete predictions and unchanged source hashes. The manifest is complete. Predictions, per-repetition metrics, paired comparisons, candidate/selected settings, endpoint error diagnostics and source configs are saved. No separate software test suite or deployment fit was run. This follow-up was selected after prior evaluations on the same students; selecting the fixed blend after observing its outer results does not independently validate a final winner.

### Removed CatBoost follow-up

The latest CatBoost experiment files and outputs were deleted at the user's request. Its strongest high-score result (.6647 MAE) was essentially tied with earlier weighted ridge (.6649), with worse overall MAE (.6388 versus .6282). Earlier regression experiments remain available. This note preserves the outcome without linking to deleted files.

### SVR and kernel ridge on existing survey inputs

Completed run: `analysis/outputs/kernel-experiments/20261102T160828159897Z/`. Settings: `analysis/kernel-config.json`; runner: `analysis/scripts/train-kernels.py`. Following the constraint that no new questionnaire features or real students could be added, this experiment used only the existing Small B and Broad D inputs and primary continuous target. No synthetic examples, engineered variables or BAT predictors were added. Standard category encoding and scaling match ridge and are fitted inside training folds. RBF kernels represent nonlinear relationships internally without changing collected variables.

Eight procedures were evaluated: two families (SVR/kernel ridge), two existing input sets, and two selection objectives (ordinary/high-priority). Original five outer folds repeated five times, with four inner folds, were preserved. SVR tuned C .1/1/10/100, gamma .01/.1/1 and epsilon .05/.2. Kernel ridge tuned alpha .01/.1/1/10/100 and gamma .01/.1/1. High sample-weight factors 1/2/4 were normalized within each training fit. Ordinary selection minimized mean inner-fold overall MAE with weight 1. High-priority selection minimized pooled inner high-score MAE among candidates within .05 pooled overall MAE of ordinary; ties used overall MAE, lower weight and grid order. The .05 inner tolerance is not an outer-error guarantee.

| Inputs | Family | Procedure | Overall MAE | High MAE (>=4) | Lower MAE (<2.5) |
|---|---|---|---:|---:|---:|
| Small B | Reference ridge | Ordinary | .5883 | .9329 | 1.0140 |
| Small B | SVR | Ordinary | .6077 | .9032 | 1.0259 |
| Small B | SVR | High-priority | .6272 | .6893 | 1.1701 |
| Small B | Kernel ridge | Ordinary | .6001 | .9872 | .9506 |
| Small B | Kernel ridge | High-priority | .6408 | .7364 | 1.0872 |
| Broad D | Reference ridge | Ordinary | .5933 | .9281 | .9740 |
| Broad D | SVR | Ordinary | .6304 | 1.0574 | .9988 |
| Broad D | SVR | High-priority | .6282 | .6705 | 1.1180 |
| Broad D | Kernel ridge | Ordinary | .7027 | 1.3036 | .8474 |
| Broad D | Kernel ridge | High-priority | .7110 | 1.0832 | .8824 |

All errors average five repetition metrics on the same 97 students (17 measured >=4). None of the eight procedures improved overall MAE over its input-matched ordinary ridge. Broad D high-priority SVR lowered high MAE by .2576 relative to Broad D ordinary ridge but increased overall MAE by .0349. Compared with the earlier Small B weighted ridge (.6282 overall/.6649 High), it has nearly identical overall error and slightly higher High error; this does not establish a better option. Raw kernel ridge has no fitted intercept or centered target in this experiment, an explicit modeling limitation to consider in any later kernel follow-up.

The manifest is complete, original outer assignments are verified, and source hashes are unchanged. All candidate metrics, selected settings, predictions, paired differences and configuration are saved. No new software test suite was run; runtime assertions enforced prediction completeness, finite values, fold alignment and source preservation. No deployment model was saved. These same-sample exploratory comparisons cannot establish a definitive selected model's independent performance.

### Synthetic examples for continuous-score regression

Completed separate run: `analysis/outputs/augmentation-experiments/20261102T153249814079Z/`. Configuration: `analysis/augmentation-config.json`; runner: `analysis/scripts/train-augmentation.py`. This follow-up used Small B's eight non-BAT inputs and the primary continuous `burnout_score`, with linear and ridge regression. It did not change the classification experiment.

For each training fit, eligible neighboring students had identical sleep/study-hour categories, the same Low (<2) or High (>=4) sampling band, score difference <=.75, each numeric-answer difference <=2, and mean numeric distance divided by four <=.25. A shared fraction between .2 and .8 interpolated inputs and score; numeric answers were rounded to valid 1–5 values. At most twice the original band count was added, without exceeding the largest band's count. No eligible pair meant no examples were generated. Labels are continuous interpolations, not actual answers to the twelve BAT items.

The same five original outer folds were repeated five times. Ridge retained the original four inner folds and alpha grid, selected by overall MAE. Generation, encoding and scaling happened inside each training fit, including inner tuning; evaluation used only excluded real students. All original unaugmented predictions and outer assignments were reproduced, and source hashes remained unchanged. Duplication used the same eligible anchors and counts as interpolation to separate reweighting from interpolation effects.

| Small B model | Training data | Overall MAE | High-score MAE (>=4) | Lower-score MAE (<2.5) |
|---|---|---:|---:|---:|
| Linear | Real only | .6155 | .7622 | .9840 |
| Linear | Real + duplicates | .6260 | .7374 | 1.0488 |
| Linear | Real + interpolations | .6365 | .7037 | 1.0594 |
| Ridge | Real only | .5883 | .9329 | 1.0140 |
| Ridge | Real + duplicates | .5943 | .8081 | 1.0992 |
| Ridge | Real + interpolations | .5972 | .7783 | 1.1083 |

These are averages of five repetition metrics on the same 97 real students, including 17 with measured scores >=4. Interpolation reduced high-score MAE by .0585 for linear and .1546 for ridge, while worsening overall and lower-score error. Overall MAE was worse in all five repetitions for both interpolated models. Duplication alone produced much of ridge's high-score improvement; interpolation further reduced high-score MAE by .0298 versus duplication, with overall MAE .0029 worse. This is a trade-off, not a general accuracy improvement.

Each outer fit contained 77 or 78 real training students and 0–32 generated records, averaging 25.28. Across the 25 outer fits, there were 632 generated row instances per model family, all High: no Low pair met the fixed criteria. This is not 632 independent new students. Rounded vectors can repeat. The saved combined training CSV contains model/method/fold identifiers, original and generated rows, parent row indices and fractions. Participant count remains 97; generated rows must not enter SPSS reliability/correlation analyses.

Local similarity and valid ranges provide constraints, not proof that synthetic students are psychologically valid. The same-sample follow-up remains exploratory. For context, the previous weighted-ridge experiment had high-score MAE .665, lower than .778 here, but overall MAE .628, higher than .597 here. Keep both experiments as evidence of different trade-offs; do not select a clinically reliable warning system from these results. No final model or weights were saved.

### Separate three-class classification

Completed run: `classification/outputs/20261102T151940669629Z/`. The original regression experiments remain unchanged. Study-defined labels on the primary `burnout_score` are Low [1,2): 6 students; Middle [2,4): 74; High [4,5]: 17. They are not validated clinical categories. Three stratified outer folds repeated five times and two-fold inner tuning were selected because the Low class has only six students. These splits differ from the regression splits.

Four software checks passed. Regularized logistic regression and constrained Random Forest were evaluated on Small B and Broad D, with a shared majority-class baseline. Inner tuning used macro F1 and compared balanced versus no class weights; all preprocessing and class-weight calculation used training data only. No synthetic data, oversampling or threshold search was used. Source hashes remained unchanged.

| Inputs / method | Accuracy | Macro F1 | Low recall | High recall | High precision |
|---|---:|---:|---:|---:|---:|
| Majority baseline | 76.3% | .288 | 0.0% | 0.0% | 0.0% |
| Small B logistic | 68.5% | .441 | 6.7% | 50.6% | 48.5% |
| Small B forest | 55.1% | .430 | 26.7% | 72.9% | 38.9% |
| Broad D logistic | 70.1% | .449 | 10.0% | 45.9% | 44.8% |
| Broad D forest | 57.9% | .445 | 23.3% | 76.5% | 38.7% |

All values average five repetition metrics on the same 97 students. Broad D forest's higher High recall came with a 25.8% false-positive rate among non-High students and low precision. Low-class performance remained weak and uncertain. Broad D logistic's slightly higher mean macro F1 does not establish a definitive winning model. These results are exploratory after previous data inspection and do not establish clinical detection or deployment readiness. The run saves each repetition's confusion matrix, probabilities, tuning, metrics and source configurations; no deployment model was saved.

### Fixed interactions in linear and ridge regression

**Historical record: experiment code/configuration/outputs were deleted on 16 November 2026. The following methods, results and checks are retained for reporting; named paths are former locations.**

Completed in `analysis/outputs/interaction-experiments/20261102T145944836445Z/`. The experiment added workload-by-sleep-category terms and centered AI-dependence-by-offloading to Small B, retaining the original main effects. Both outcomes and identical original outer/inner folds were used. Ridge selection retained overall inner MAE as the objective. Three new software tests passed; run status is complete and source hashes were unchanged.

| Primary-outcome model | Overall MAE | MAE for measured scores >=4 |
|---|---:|---:|
| Original linear | .6155 | .7622 |
| Linear with interactions | .6131 | .8356 |
| Original ridge | .5883 | .9329 |
| Ridge with interactions | .5872 | .9011 |

The overall changes are very small. Linear interactions worsened high-score MAE by .0734 despite slightly lower overall MAE. Ridge interactions reduced high-score MAE by .0319, with overall MAE only .0011 lower. Secondary-score overall MAE changed from .5816 to .5741 for linear and .5528 to .5508 for ridge; linear high-score MAE also worsened there. These selected interaction hypotheses do not provide evidence of a substantial practical improvement. This does not establish that every possible interaction is useless.

SPSS correlations were used as descriptive context, not copied as model weights or used for full-data p-value screening. They cannot establish whether the interaction terms help. Any future learned correlation screening must occur inside training groups. This follow-up was selected after previous evaluations and is exploratory; do not claim independent validation or a definitive winning model from the tiny differences. No model weights were saved.

### High-score-priority ridge follow-up

Completed separately in `analysis/outputs/high-score-experiments/20261102T144716191460Z/`, using Small B, both outcomes, and identical original outer/inner splits. The ordinary-ridge predictions were reproduced against the saved original run. Four new software tests passed. Dataset and prior-run source hashes were unchanged.

Relative training weights 1/2/4 for measured scores >=4 and six ridge alphas were selected inside training groups only. We normalized weights to mean one. Inner selection minimized pooled high-score MAE among candidates whose pooled overall MAE was at most .05 worse than the ordinary-ridge reference. The .05 guardrail is an exploratory analytical choice, not a clinical standard. The >=4 boundary is descriptive, not a validated diagnosis.

| Primary-outcome measure | Ordinary Small B ridge | High-score-priority ridge |
|---|---:|---:|
| Overall MAE | .5883 | .6282 |
| MAE for measured scores >=4 | .9329 | .6649 |
| Mean underestimation in that group | .9329 | .6160 |
| Recall at predicted >=4 among measured >=4 | 3.5% | 25.9% |
| False-positive rate among measured <4 | 0.0% | 4.0% |
| MAE among measured scores <2.5 | 1.0140 | 1.1699 |

These average the five repetition metrics; percentages do not represent additional independent students. High-score MAE fell by .268 points (about 29%), while overall MAE rose by .040 and lower-score errors increased. The primary numerical goal held in three of five repetitions, not consistently across all splits. The secondary outcome showed high-score MAE .9665 to .6752, but overall MAE .5528 to .6031; the numerical goal held in two of five repetitions.

This demonstrates a trade-off, not an overall model improvement or readiness for deployment. Even the priority model missed most students in the descriptive >=4 group. Keep both procedures and report the trade-off; do not choose a final warning model solely from these reused evaluation results. Read the run's `results.md`, per-repetition metrics, and false-positive counts before deciding on further research. No deployment model was saved.

### Saved-prediction diagnostics

A descriptive investigation is saved in `analysis/outputs/diagnostics/20261102T143712960388Z/findings.md`. No models were fitted. The script `analysis/scripts/diagnose-predictions.py` checks prediction/student alignment, aggregates errors across repetitions, compares input similarity, and counts selected tuning settings. Source-file hashes were unchanged after analysis. This is exploratory diagnosis, not a new validation experiment.

For the primary outcome, measured-score standard deviation was .795, versus .299 for Small B ridge predictions (about 38% of the measured spread). Small B linear predictions had more spread (.503), but worse MAE (.615 versus ridge's .588). Thus increasing spread alone is not evidence of better prediction. Small B ridge selected alpha 100 in 20 of the 25 outer fits, alpha 10 in four, and alpha 1000 in one; those penalties were selected by inner validation.

Broad D ridge improved average errors for 13 of the 17 students whose Small B mean absolute error exceeded one point, while its overall MAE remained slightly worse. Students 41 and 93 had a similarity distance of .125 with measured scores 1.583 and 3.750; students 69 and 2 had distance .094 with scores 1.917 and 3.333. Distance averages fixed-range differences on six 1–5 items and category mismatches on sleep/study hours, giving each question equal weight. These are similar rather than identical answers. Only one exact repeated input pattern existed, with two students and a score gap of .25. The matches suggest ambiguity but do not prove an unavoidable error limit or identify causal missing factors.

Recommendation: preserve these evaluations, report the modest predictive gains and poor extremes, and examine the broader-input trade-off before choosing a research demonstration model. Do not simply expand predictions, remove hard students, or weaken regularization based on these held-out outcomes. If extreme-score performance becomes the explicit priority, specify a separate training-objective/weighting experiment and acknowledge the trade-off in overall error and the need for new validation data. More representative real data and potentially more informative questions are sensible future work; their benefit is not established by this inspection.

The original comparison completed in `analysis/outputs/model-runs/20261102T083420352990Z/`. The exploratory XGBoost follow-up completed in **`analysis/outputs/xgboost-experiments/20261102T093101705609Z/`**. Both manifests report `complete`. Run folders are local and excluded from Git because they contain individual predictions. Historical pending-run statements below refer to the earlier handoff.

The follow-up used the same 97 students, outcomes, outer groups and inner splits. It tested Small A/B with four shallow-tree XGBoost settings chosen by inner validation. No augmentation or oversampling was used. This was chosen after reviewing original results, not independent confirmation. Source datasets and original run files were unchanged.

| Outcome | Inputs | Original ridge MAE | XGBoost MAE |
|---|---|---:|---:|
| Primary 12-item score | Small A | .6183 | .6259 |
| Primary 12-item score | Small B | .5883 | .6155 |
| Secondary 23-item score | Small A | .6001 | .5875 |
| Secondary 23-item score | Small B | .5528 | .5749 |

Lower MAE is better. XGBoost did not improve on Small B ridge for either outcome. Its Small A secondary-outcome improvement does not justify switching the primary target. Repetitions share students, so consistency across splits is not statistical significance.

For the primary outcome, 19 students had measured scores below 2.5 and 17 had scores of 4 or above. These are descriptive ranges, not clinical categories. Small B ridge had average errors of 1.014 and .933 points in those ranges, versus 1.047 and .995 for XGBoost. Both overestimated the lower scores and underestimated the higher scores. Changing to XGBoost did not solve this problem.

Open the follow-up's `comparison-with-original.md` for range-specific errors and `results.md` for overall metrics. No deployment model or weights were saved. Five existing and three new software tests passed; dependencies were consistent. Next: assess the prediction limitations before selecting a final research model or planning another separately justified experiment.

Analysis record: 28 October 2026. Language and navigation updated: 29 October 2026. Numerical results below are unchanged.

## Model preparation check, 29 October 2026

The experiment configuration, training workflow, and run instructions are prepared. The full real-data model comparison has not been run.

The new data reader found three missing `ai_use_summaries` indicators, which differs from the older saved-file check described below. The original multi-choice answers exactly match the raw CSV. The workflow reconstructs these three indicators in memory from those answers, without changing the SAV. Both burnout targets passed formula checks. Read [the analysis guide](../analysis/README.md#implementation-choices) and [readiness report](../analysis/checks/model-readiness.json) for this preparation step.

## Quick reading guide

Data preparation and the first analyses are complete. Both burnout scores are ready; no prediction model has been trained or evaluated.

| Need | Go to |
|---|---|
| Score formulas | [Section 2](#2-burnout-scores-created) |
| Reliability, averages, and correlations | [Section 3](#3-statistical-analyses-completed) |
| Question codes and labels | [Section 4](#4-preparing-the-non-bat-questions) |
| Corrections and saved data checks | [Section 7](#7-corrections-and-final-verification) |
| Proposed next experiment | [Model plan](prediction-experiment.md) |

Read one section at a time. You do not need every table to understand the next task.

## 1. Current status and files

We collected responses from **97 Lebanese university students** about GenAI use, study conditions, and burnout. The questionnaire contains 20 non-BAT questions and 23 Burnout Assessment Tool for Students (BAT-S) items.

**Data preparation and initial analyses are complete. The predictive model has not been fitted or evaluated yet.** The current data can support prediction of current burnout symptoms. Early warning of future burnout would require follow-up measurements, because all current answers were collected at the same time.

| File | Purpose |
|---|---|
| `data/prepared/burnout-data.sav` | **Current working dataset:** original responses, burnout scores, and numeric recodes |
| `analysis/outputs/descriptive-statistics.spv` | Shared output containing results and tables; continue saving results here |
| `archive/data/burnout-before-corrections.sav` | Earlier dataset retained as a backup |
| `archive/data/burnout-older-checkpoint.sav` | Older analysis checkpoint |
| `data/raw/survey-export-spss.csv` | Original response export used to verify answers |
| `analysis/scripts/prepare-predictors.sps` | Syntax that created the remaining numeric predictors and saved the prepared dataset |

The preparation syntax opens `archive/data/burnout-before-corrections.sav` and writes a separate `data/prepared/burnout-data-rebuilt.sav`. That rebuild still needs the two corrections documented in Section 7. Use the corrected `data/prepared/burnout-data.sav` for analysis.

All **97 respondents remain included**: 87 answered Yes to enrollment at a university in Lebanon and 10 answered No. The researcher identified the latter as Lebanese students studying abroad. Q1 records enrollment location, is not an exclusion rule, and does not identify public/private universities. Reviewed SPSS procedure notes showed no active filter, weighting, or split-file setting.

## 2. Burnout scores created

BAT responses run from **1 = Never** to **5 = Always**. Higher scores mean more frequent symptoms. We calculated two versions of burnout and kept them separate.

### Primary outcome: 12-item short form

Each dimension uses three selected items. The overall score averages the four dimension means.

| Variable | Dimension | Calculation |
|---|---|---|
| `exhaustion` | Exhaustion | `MEAN.3(BAT21, BAT23, BAT24)` |
| `mental_distance` | Disengagement from studies | `MEAN.3(BAT29, BAT31, BAT33)` |
| `cognitive_impairment` | Difficulties with attention and thinking | `MEAN.3(BAT34, BAT37, BAT38)` |
| `emotional_impairment` | Difficulties regulating emotional reactions | `MEAN.3(BAT39, BAT40, BAT43)` |
| `burnout_score` | Overall primary score | `MEAN.4(exhaustion, mental_distance, cognitive_impairment, emotional_impairment)` |

The saved scores were checked against these formulas. Because every dimension has three items, the overall score also equals the mean of the 12 selected items.

### Secondary outcome: full 23-item core

| Variable in the actual file | Items | Calculation |
|---|---|---|
| `exhaustion_23` | BAT21–BAT28: 8 items | `MEAN.8(BAT21 TO BAT28)` |
| `mental_distance_23` | BAT29–BAT33: 5 items | `MEAN.5(BAT29 TO BAT33)` |
| `congnitive_impairement_23` | BAT34–BAT38: 5 items | `MEAN.5(BAT34 TO BAT38)` |
| `emotional_impairment_23` | BAT39–BAT43: 5 items | `MEAN.5(BAT39 TO BAT43)` |
| `burnout_score_23` | Four full-core dimension means | `MEAN.4(exhaustion_23, mental_distance_23, congnitive_impairement_23, emotional_impairment_23)` |

**Naming detail:** `congnitive_impairement_23` is misspelled in the dataset. Its values are correct; use that exact name in syntax unless it is deliberately renamed.

In these formulas, `MEAN.3`, `MEAN.5`, and `MEAN.8` require all listed dimension items to be valid; `MEAN.4` requires all four dimension means. All ten calculated scores remain on the **1–5 scale**.

The secondary score gives each dimension equal weight. It is **not the simple mean of all 23 items**, which would give exhaustion more weight because it has eight items. The study plan names the 12-item score as primary and the 23-item score as secondary. Record any change before comparing models. Project-defined low/moderate/high bands are exploratory, not validated diagnostic thresholds for Lebanese students.

## 3. Statistical analyses completed

### Reliability: do the BAT items work consistently together?

We ran Cronbach's alpha for each dimension and both complete item sets, using the individual BAT items. The full-core analyses included Item Statistics, Item-Total Statistics, and Scale Statistics.

| Dimension or item set | Short-form items | Short-form alpha | Full-core items | Full-core alpha |
|---|---:|---:|---:|---:|
| Exhaustion | 3 | .781 | 8 | .909 |
| Mental distance | 3 | .733 | 5 | .820 |
| Cognitive impairment | 3 | .876 | 5 | .919 |
| Emotional impairment | 3 | .775 | 5 | .839 |
| All items together | 12 | .900 | 23 | .944 |

These results support internal consistency in this sample. **All items were retained.** Small increases in alpha after deleting an item were not used to alter the designated scales.

A corrected item–total correlation compares an item with the sum of the other items in the analyzed set, excluding itself. For the full-core dimensions, these correlations ranged from .562–.783 for exhaustion, .533–.677 for mental distance, .678–.861 for cognitive impairment, and .538–.725 for emotional impairment. Across all 23 items, the range was .382–.789.

Deleting BAT38 would change full-core cognitive alpha from .919 to .923; deleting BAT43 would change total 23-item alpha from .944 to .945. Neither small increase justified deletion. In the short form, deleting BAT43 would change emotional alpha from .775 to .797 and total alpha from .900 to .904; it was retained there too.

Alpha measures how consistently items vary together. It does not show prediction accuracy, prove validity, or prove that the four dimensions measure a single dimension. The 23-item alpha uses the individual items; it does not give the exact reliability of our score, which gives equal weight to each dimension.

### Descriptive statistics and Explore: how are scores distributed?

We produced frequencies and bar charts for BAT21–BAT43, descriptives for the short-form dimensions and overall score, and Explore output for both overall scores. Explore included descriptive statistics, histograms, stem-and-leaf plots, and boxplots.

| Short-form dimension | Mean | Standard deviation |
|---|---:|---:|
| Exhaustion | 3.430 | .934 |
| Mental distance | 2.986 | .908 |
| Cognitive impairment | 3.110 | 1.104 |
| Emotional impairment | 2.973 | .937 |

| Overall-score statistic | `burnout_score` | `burnout_score_23` |
|---|---:|---:|
| Valid N | 97 | 97 |
| Mean | 3.125 | 3.150 |
| Standard deviation | .795 | .765 |
| Median | 3.083 | 3.075 |
| Minimum | 1.417 | 1.444 |
| Maximum | 5.000 | 5.000 |
| Skewness | .176 | .288 |
| Excess kurtosis | −.164 | −.026 |

Both score distributions look roughly balanced, with a slightly longer tail toward higher scores. These summaries do not show an obvious need to transform the score. They do not replace formal distribution checks or later checks of regression errors. A score of 5 is valid; an extremes label in a plot is not a reason to exclude a student.

Scale Statistics in reliability output describe **item sums**, whereas our calculated score variables are **means on the 1–5 scale**. A mean near 3 is not a clinical diagnosis.

### Correlations: which individual questions are associated with burnout?

We ran exploratory Spearman correlations between the **primary `burnout_score`** and 11 non-BAT questions. Positive values mean that higher responses on that question tended to accompany higher burnout. These are separate associations, without adjustment for other predictors.

| Variable | Spearman rho | Two-tailed p |
|---|---:|---:|
| AI dependence | .377 | <.001 |
| AI offloading | .331 | <.001 |
| AI frequency | .220 | .030 |
| Perceived workload | .388 | <.001 |
| Academic stress | .367 | <.001 |
| Financial strain | .196 | .054 |
| University support | −.148 | .149 |
| Internet quality | −.059 | .564 |
| Avoidance/procrastination | .445 | <.001 |
| AI output verification | −.010 | .923 |
| Anxiety about AI accusations | .278 | .006 |

A Pearson correlation was also run for AI dependence and burnout: **r = .361, p < .001**. It agrees in direction with Spearman, but uses the same responses and is not independent confirmation.

The three-variable matrices also included:

| Predictor pair | Spearman rho | Two-tailed p |
|---|---:|---:|
| Workload and academic stress | .672 | <.001 |
| Financial strain and university support | .064 | .533 |
| Internet quality and avoidance | .112 | .277 |
| AI verification and AI anxiety | .416 | <.001 |

All saved correlations used 97 students and two-tailed tests, which check associations in either direction. SPSS used available pairs if values were missing. The output did not adjust for testing many associations or report confidence intervals. Avoidance had the strongest burnout correlation among the tested questions. Workload and stress were also closely related; check their overlap in a later model.

These results do not show causes or prediction accuracy. A p-value below .05 does not guarantee a useful model input, and a larger p-value does not prove an input is useless. The GenAI questions are separate items; we have not validated a combined AI scale.

## 4. Preparing the non-BAT questions

The first 20 questions describe different things, so we did not calculate one alpha across them. Their roles as model inputs or separate outcomes still need to be chosen.

For answers already stored as numbers, we added labels and corrected measurement settings. For text answers, we created numeric copies with labels. We kept every original text column. A label explains a number; a recode converts an answer into a number. Neither step tests a research question.

### Existing numeric questions

All the following are **Numeric, 0 decimals, Ordinal**. Their saved labels currently name the endpoints; values 2–4 are valid but have no display labels.

| Question | Variable | Label for 1 | Label for 5 |
|---|---|---|---|
| Q6 | `internet` | Very poor | Excellent |
| Q7 | `financial_strain` | No strain | Severe strain |
| Q8 | `ai_frequency` | Never | Daily |
| Q10 | `ai_dependence` | Strongly disagree | Strongly agree |
| Q11 | `ai_offloading` | Strongly disagree | Strongly agree |
| Q12 | `ai_verification` | Strongly disagree | Strongly agree |
| Q13 | `ai_anxiety` | Strongly disagree | Strongly agree |
| Q15 | `workload` | Strongly disagree | Strongly agree |
| Q17 | `academic_stress` | Strongly disagree | Strongly agree |
| Q18 | `avoidance` | Strongly disagree | Strongly agree |
| Q19 | `university_support` | Strongly disagree | Strongly agree |
| Q20 | `leave_intention` | Strongly disagree | Strongly agree |

The endpoints match the saved questionnaire. If the live form explicitly named options 2–4, add those exact labels later rather than inventing them. Their absence does not change calculations. Higher numbers represent more of each stated characteristic, including better internet and greater support where applicable.

### Text questions converted into numeric copies

Every new variable below is **Numeric, 0 decimals**, with labels matching these mappings.

| Original | New variable | Codes and labels | Measure |
|---|---|---|---|
| `eligible` | `enrolled_lebanon` | 0 = No; 1 = Yes | Nominal |
| `academic_level` | `academic_level_code` | 1 = Freshman / First Year; 2 = Sophomore / Second Year; 3 = Junior / Third Year; 4 = Senior / Fourth Year +; 5 = Master's / Postgraduate | Ordinal |
| `major` | `major_code` | 1 = STEM; 2 = Health Sciences / Medicine / Nursing / Pharmacy; 3 = Business / Economics / Finance; 4 = Humanities, Social Sciences, or Law; 5 = Arts & Design | Nominal |
| `GPA` | `gpa_code` | 1 = Academic Warning / Passing; 2 = Satisfactory; 3 = Good; 4 = Excellent | Ordinal |
| `electricity` | `electricity_code` | 1 = Less than 2 hours / Minimal impact; 2 = 2–5 hours; 3 = 5–8 hours; 4 = More than 8 hours / Severe disruption | Ordinal |
| `study_hours` | `study_hours_code` | 1 = Less than 5 hours; 2 = 5–10 hours; 3 = 11–20 hours; 4 = More than 20 hours per week | Ordinal |
| `sleep_duration` | `sleep_duration_code` | 1 = Less than 5 hours; 2 = 5–6 hours; 3 = 7–8 hours; 4 = More than 8 hours per night | Ordinal |

Nominal means categories have no numerical order: major 5 is not greater than major 1. Ordinal means categories have an order, but the gaps may differ. Study-hours code 3 means the 11 to 20 hour category, not three hours. The SPSS Ordinal setting does not choose how a regression model will use that variable.

### Q9: AI use cases

The export contains up to two selections per student in `ai_use_cases`. We created five separate indicators, each **Numeric, 0 decimals, Nominal**, with **0 = Not selected** and **1 = Selected**.

| New variable | Represents | Students selecting it |
|---|---|---:|
| `ai_use_concepts` | Concept explanation and brainstorming | 72 |
| `ai_use_writing` | Essay writing, grammar polishing, or drafting | 21 |
| `ai_use_coding` | Coding, debugging, or technical problem solving | 27 |
| `ai_use_summaries` | Summarizing articles or lecture slides | 37 |
| `ai_use_solutions` | Direct assignment/homework solutions | 16 |

21 students selected one use and 76 selected two. Counts overlap because two selections were allowed.

### BAT and score settings in Variable View

- **BAT21–BAT43:** Numeric, 0 decimals, Ordinal; 1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often, 5 = Always.
- **All ten calculated dimension and overall scores:** Numeric, 3 decimals, Scale, Values = None because decimal means are meaningful.
- **Original text columns and Timestamp:** retained unchanged. Use appropriate numeric copies for model preparation.

## 5. Sample description from frequency tables

Frequency analyses covered academic level, major, GPA, study hours, sleep, and electricity. The preparation syntax also requested frequencies and cross-tabulations to check recode mappings.

| Variable | Counts, out of 97 |
|---|---|
| Academic level | Freshman 8; Sophomore 21; Junior 12; Senior 13; Master's/Postgraduate 43 |
| Major | STEM 48; Health Sciences 19; Business 12; Humanities/Social Sciences/Law 16; Arts & Design 2 |
| GPA | Academic Warning/Passing 3; Satisfactory 25; Good 38; Excellent 31 |
| Study hours/week | Less than 5: 34; 5–10: 33; 11–20: 22; More than 20: 8 |
| Sleep hours/night | Less than 5: 12; 5–6: 50; 7–8: 35; More than 8: 0 |
| Electricity disruption hours/day | Less than 2: 65; 2–5: 25; 5–8: 3; More than 8: 4 |

These counts describe the 97 students in this sample. They do not describe all students. Some categories have very few students. If we combine categories for modeling, we need a clear reason based on their meaning.

## 6. What the checks establish

We checked reliability, score distributions, initial associations, and variable preparation. We have not completed regression, checks of regression errors, VIF/tolerance checks for input overlap, factor analysis, omega reliability estimates, or cross-validated predictions. Extra t-tests, ANOVA, or chi-square tests are not required before starting the planned prediction work.

## 7. Corrections and final verification

Two blanks were found in the earlier `burnout-before-corrections.sav` and carried into the first prepared file. The corrected working file was saved and checked again:

| Record | Variable | Correction and basis |
|---|---|---|
| Timestamp `2026/10/05 1:21:45 am EEST` (row 18 in the checked order) | `emotional_impairment` | Recalculated from BAT39, BAT40, BAT43: all three are 5, so the mean is 5 |
| Timestamp `2026/10/06 11:35:51 pm EEST` (row 65 in the checked order) | `internet` | Restored 3, matching the original CSV response |

Their cause is unknown. They were not missing survey answers. Use timestamps to identify these records if the row order changes.

The final saved-file check confirmed:

- **97 rows, 66 variables**, and no numeric system-missing values.
- All original numeric survey answers match the CSV.
- Every new category code matches its original text answer.
- Every AI-use indicator matches the student's selections.
- All ten dimension and overall scores match the intended calculations.
- Value labels, Nominal/Ordinal/Scale settings, and decimal formats match the plan above.
- Existing values differ from the earlier `burnout-before-corrections.sav` only in the two corrected cells; new variables were added separately.

The script `analysis/scripts/check-data.py` reads the SAV files and writes verification reports. It does not modify the dataset or the SPSS output.

## 8. Next step: define the first experiment

Follow [the model plan](prediction-experiment.md) for the proposed targets, inputs, encoding, and evaluation. Record its open decisions before training.

Keep the first model small because we have 97 students. Exclude BAT answers and BAT-derived scores from inputs. Use training data alone to fit preprocessing and choose tuning settings. Compare prediction errors with the training-mean baseline.

SPSS can support regression checks, while Python can support repeated cross-validation. Fit on the training students does not establish prediction accuracy.

## Terms used in this review

| Term | Plain meaning |
|---|---|
| Mean | Average |
| Standard deviation | How spread out scores are around the average |
| Correlation | How two answers tend to vary together; it does not establish cause |
| Cronbach's alpha | A measure of how consistently a group of items varies together |
| Predictor / outcome | Information used by a model / the value the model tries to estimate |

Next: open [the proposed input sets](prediction-experiment.md#2-compare-two-sets-of-inputs).
