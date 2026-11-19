Submitted Manuscript 

# **Auditing Construct Overlap in Explainable Machine Learning: Evidence from Burnout-Depression Prediction Across Student Cohorts** 

**Alireza Dehghan**<sup>1</sup> **Negin Ashrafi**<sup>2,*</sup> 

> 1Sharif University of Technology, Tehran, Iran 

> 2University of Southern California, California, USA 

> *Corresponding author: ashrafin@usc.edu 

**Abstract.** Explainable machine learning (XML) pipelines applied to composite mental health outcomes can produce apparently-robust, cross-population-stable risk hierarchies that are largely artefacts of how the outcome was constructed. We demonstrate this using an ElasticNet pipeline applied to 886 medical students at the University of Lausanne (primary cohort, 2022), validated across 2,580 longitudinal observations at three time points and 701 non-medical students from eight faculties; all three datasets share identical instruments. 

The pipeline produces a hierarchy in which trait anxiety and health satisfaction dominate wherever the outcome is measured, with Kendall _τ_ = 1 _._ 0 for the top-two positions across all five evaluation sets and consistent transfer performance (R<sup>2</sup> : 0.41–0.49). Two residualization experiments, which isolate shared variance between correlated variables via regression, reveal the mechanism: when trait anxiety (STAI-T) is residualized against the co-included depression subscale (CES-D, _r_ = 0 _._ 72), model R<sup>2</sup> drops from 0.41 to 0.16 and STAI-T falls from rank 1 to rank 6; when burnout subscales are residualized against CES-D, R<sup>2</sup> collapses to 0.016. Prediction intervals average 35.4 units on a 0–100 scale (2.4 outcome standard deviations), independently ruling out individual-level deployment. The residualization protocol is the paper’s transferable contribution: any XAI study combining correlated predictor and outcome constructs should apply this check before interpreting apparent stability as a finding. 

**Keywords:** construct overlap; explainability artefact; burnout; depression; residualization; XAI; SHAP; conformal prediction; medical students; multi-cohort validation 

## **1 Introduction** 

Burnout and depression among medical students are prevalent and consequential: reported burnout rates consistently exceed those of the general population, and untreated distress impairs clinical empathy and patient care quality [1–3]. The application of machine learning to self-report survey data offers a route to automated risk stratification; paired with SHAP explanations, such pipelines appear to identify stable, crosspopulation risk hierarchies, a consistent rank-ordering of predictors by importance, in which trait anxiety and health satisfaction dominate [4, 5]. 

The objective of this study is not to identify definitive risk factors, but to test whether the stability produced by such a pipeline is real. Specifically: trait anxiety (STAI-T) and the CES-D depression scale are highly correlated ( _r_ = 0 _._ 72 in this sample). The CES-D is embedded inside the composite burnoutdepression outcome. When a predictor and an outcome component share a latent construct, the predictor’s explanatory dominance may reflect psychometric overlap rather than a genuine risk relationship. We call this construct overlap, and we introduce a residualization protocol to quantify how much of the apparent hierarchy survives once the overlap is removed. 

The principal contributions are threefold. First, we validate a _residualization protocol for detecting construct overlap artefacts_ : removing the anxiety– depression psychometric channel collapses R<sup>2</sup> from 0.41 to 0.016 (burnout-specific outcome) and STAI-T 

from rank 1 to rank 6. Second, we demonstrate that _apparent cross-cohort stability is not evidence of a portable risk structure_ when the signal is anchored to a fixed psychometric correlation: the model transfers with R<sup>2</sup> = 0.41–0.49 across five evaluation sets because the STAI-T/CES-D bivariate relationship is constant, not because the pipeline learned a generalisable risk structure. Third, we provide _deployment-relevant uncertainty quantification_ : conformal prediction intervals average 35.4 BDCI units (2.4 outcome standard deviations), establishing that individual-level clinical prediction is not actionable with current feature sets. 

The remainder of this paper is organised as follows. Section 2 briefly reviews related work. Section 3 describes the methodology. Section 4 presents results in four subsections structured around the central audit. Section 5 discusses implications. Section 6 concludes. 

## **2 Related Work** 

A growing body of work applies machine learning and XAI to mental health outcomes in student populations. Martínez-Ramón et al. [6] achieved high classification accuracy for teacher burnout using ANN. Bozorgmehr and Weltermann [4] applied XGBoost with SHAP to a large German adult sample and identified health satisfaction as a dominant protective factor, consistent with our findings on a different instrument. Rashid et al. [5] applied ensemble and deep learning to the same 886student Lausanne cohort as this paper, achieving moderate classification accuracy. Benito et al. [7] and Nnadi et al. [8] combined SHAP with clustering and hierarchi- 

1 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 

**Table 1.** Summary of reviewed studies on machine learning for mental health estimation in student and clinical populations. 

|**No.**|**Authors (Year)**|**Model / Approach**|**Explainability**|**N**|
|---|---|---|---|---|
|1|Al-Alawi et al. (2019)|Logistic Regression|None|662|
|2|Wang et al. (2019)|Statistical Analysis|None|1,271|
|3|Cheng et al. (2020)|Linear Regression|None|1,722|
|4|Pokhrel et al. (2020)|Logistic Regression|None|651|
|5|Ilic et al. (2021)|Logistic Regression|None|760|
|6|Martínez-Ramón et al. (2021)|ANN|None|419|
|7|Lou et al. (2022)|Penalised LR, SVM, RF|None|88|
|8|Carrard et al. (2022)|Logistic Regression|None|886|
|9|Ghosh et al. (2023)|SVM|None|1,182|
|10|Alam & Alam (2023)|Neural Network|Pre-hoc|28|
|11|Bozorgmehr & Weltermann (2023)|XGBoost|SHAP|5,801|
|12|Benito et al. (2024)|RF, SVM, MLP|SHAP, UMAP|9,291|
|13|Khan et al. (2024)|NLP + Ensemble|Feature Importance|19,000|
|14|Rashid et al. (2024)|RF, NB, DNN|None|886|
|15|Li et al. (2025)|Regression + Classification|SHAP|2,024|
|16|Nnadi et al. (2026)|RF, SVM|SHAP, H-LIME, DiCE|27,901|
|*|This study|ElasticNet<br>(primary);<br>OLS,<br>Ridge, Lasso, SVR|SHAP; residualization audit|886 / 2,580 / 701|



**Table 2.** Cohort overview. All datasets use identical instruments (CES-D, STAI-T, MBI-SS). 2022 thresholds are used for <u>BDCI construction in all cohorts.</u> 

|**Cohort**|**Description**|_n_|**Design**|**Source**|
|---|---|---|---|---|
|Primary (2022)|Medical students, Univ. Lausanne|886|Cross-sectional|[9]|
|Temporal (2021–22)|Medical, 3 waves (Mar. 2021, Nov. 2021, Nov. 2022)|2,580|Longitudinal|[10]|
|Non-medical (NMS)|8 non-medical faculties, same institution|701|Cross-sectional|[11]|



cal explanation frameworks. In all cases, the feature hierarchy is treated as a finding; no prior work has tested whether the hierarchy survives a residualization check for construct overlap. 

Table 1 summarises reviewed studies. The methodological gap is clear: regression-based continuous framing and construct-overlap auditing are both absent from the existing literature. 

## **3 Methodology** 

### **3.1 Data and Cohorts** 

Table 2 describes the three datasets. The primary cohort ( _n_ = 886 medical students, University of Lausanne, 2022) was collected by the Faculty of Biology and Medicine [9]. It contains no missing values. Predictors include ten demographic and psychological survey items (age, academic year, health satisfaction, psychotherapy history, partnership status, employment status, weekly study hours, mother tongue, sex, and trait anxiety from the State-Trait Anxiety Inventory; STAI-T). Outcome components are the three Maslach Burnout Inventory–Student Survey (MBI-SS) subscales and the Center for Epidemiological Studies Depression Scale (CES-D). 

The temporal and non-medical cohorts are openly available under CC-BY 4.0 (Zenodo: 10.5281/zenodo.8405764 and 10.5281/zenodo.15149289 respec- 

### tively). 

### **3.2 BDCI Construction** 

The Burnout–Depression Composite Index (BDCI) integrates the three MBI-SS subscales and CES-D into a single severity score on [0 _,_ 100]. Each subscale is normalised to its theoretical maximum (reversing the Academic Efficacy subscale); any component exceeding its empirical 75th-percentile threshold (derived from the 2022 training split) is doubled. The raw sum is then scaled by 100 _/_ (4 + _k_ ), where _k_ is the count of elevated components. The result is a continuous index where higher values indicate greater joint burnout-depression severity. Formally: 



<!-- Start of picture text -->
2 sj sj > τj<br>BDCI = 100 � s ∗ j , s ∗ j = (1)<br>4 +  k j � sj otherwise .<br><!-- End of picture text -->

The 75th-percentile thresholding and doubling scheme is intended to give greater analytic weight to clinically elevated symptom levels, a severity-weighting logic common in composite mental-health indices. We treat this as one reasonable analytic choice rather than a validated clinical rule: the threshold is sample-derived (2022 training split) rather than tied to an external clinical cutoff (e.g., CES-D _≥_ 16), which is a limitation we return to in Section 5.1. Sensitivity to the weighting choice itself is assessed directly via BDCI-A (Table 5), an equal-weight variant that reproduces the same 

2 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 



<!-- Start of picture text -->
Pearson Correlation Matrix -- Continuous Variables<br>Age 1.00 -- -- -- -- -- -- -- -- -- -- --<br>Study h/wk 1.00<br>JSPE 0.75<br>Cog. Empathy<br>0.50<br>Aff. Empathy<br>0.25<br>Acad. Motivation<br>0.00<br>Response Acc.<br>−0.25<br>Depression<br>−0.50<br>Trait Anxiety<br>Exhaustion −0.75<br>Cynicism −1.00<br>Acad. Efficacy<br>AgeStudy h/wk JSPECog. EmpathyAff. EmpathyAcad. MotivationResponse Acc.DepressionTrait AnxietyExhaustionCynicismAcad. Efficacy<br>Pearson r<br><!-- End of picture text -->

**Figure 1.** Pearson correlation matrix for the twelve continuous variables. The strong anxiety–depression association ( _r_ = 0 _._ 72, STAI-T and CES-D) is the structural source of construct overlap: CES-D is an outcome component while STAI-T is the dominant predictor. 

qualitative pattern, indicating the central finding does not depend on this specific scheme. The BDCI is a study-specific analytical composite; it has not been independently validated as a clinical instrument. 

The critical structural feature of the BDCI is that CES-D is one of its four components, while STAI-T (trait anxiety) is one of the predictors. Figure 1 shows the Pearson correlation matrix: STAI-T and CES-D share _r_ = 0 _._ 72 ( _p <_ 0 _._ 001), the strongest pairwise correlation in the dataset. This overlap motivates the residualization audit in Section 4.3. 

ElasticNet was retrained on the 2022 training split using only the predictors available in all three cohorts (age, academic year, health satisfaction, psychotherapy history, partnership status, STAI-T, sex), then applied without retraining to the temporal and non-medical cohorts. The 2022 BDCI thresholds _τj_ were used throughout to prevent leakage. 

Ninety-five percent bootstrap confidence intervals (1,000 resamples) were computed for all test-set metrics. 

### **3.4 Residualization Protocol** 

### **3.3 Analysis Pipeline** 

The dataset was partitioned 80/20 into training ( _n_ train = 708) and test ( _n_ test = 178) sets using stratified random sampling on BDCI quartile (random seed 42 throughout). All predictors were _z_ -score normalised using training-split statistics only. ElasticNet (L1+L2 regularisation) was selected as the primary model after 5-fold cross-validated comparison of six candidate regressors (OLS, Ridge, Lasso, ElasticNet, SVR, ANN); hyperparameters were selected by grid search ( _α ∈_ [10<sup>_−_4</sup> _,_ 10<sup>1</sup> ], mixing ratio _ρ ∈ {_ 0 _._ 1 _,_ 0 _._ 3 _,_ 0 _._ 5 _,_ 0 _._ 7 _,_ 0 _._ 9 _}_ ; optimal: _α_ = 0 _._ 0316, = _ρ_ 0 _._ 7). SHAP values were computed using `LinearExplainer` [12]. 

For cross-cohort validation, a 7-feature reduced 

Two orthogonality experiments were conducted to isolate the anxiety–depression channel. _Experiment 1 (predictor residualization)_ : STAI-T was replaced by the residuals of regressing STAI-T on CES-D (fit on training set, applied to test set). The residual captures trait anxiety variance orthogonal to concurrent depression. _Experiment 2 (outcome residualization)_ : each MBI-SS subscale was individually residualized against CES-D (OLS, training set), then re-normalised and assembled into a depression-free composite (BDCI-C). In both cases, ElasticNet was refit from scratch on the modified data using the same hyperparameter grid and split. We note that BDCI-C is a statistical construct created solely to isolate depression-independent variance in the burnout subscales; residualizing against CES-D does not by itself produce a validated ’pure burnout’ mea- 

3 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 

sure. A near-zero R2 for BDCI-C indicates that this feature set cannot predict the depression-independent portion of the composite, not that a clinically meaningful burnout-specific construct doesn’t exist. Results are compared with the primary BDCI and a CESD-excluded composite (BDCI-B, MBI-SS only) in Table 5. 

### **3.5 Conformal Prediction** 

Point estimates are complemented by split conformal prediction intervals [13]. The test set is split 50/50: the calibration half ( _n_ cal = 89) is used to compute non-conformity scores _si_ = _|yi − y_ ˆ _i|_ ; the evaluation half ( _n_ eval = 89) receives intervals [ˆ _yj ± q_ ˆ], where _q_ ˆ is the (1 _− α_ )(1 + 1 _/n_ cal) quantile at _α_ = 0 _._ 10. This procedure provides marginal coverage _≥_ 90% without distributional assumptions, with the caveat that small calibration sets may produce slight deviations from the nominal level. 

## **4 Results** 

### **4.1 A Standard Pipeline Produces an Apparent Hierarchy** 

Table 3 presents test-set performance. All four linear and regularised models achieve similar accuracy (R<sup>2</sup> : 0.400–0.414); SVR performs somewhat worse. Penalisation offers no meaningful gain over OLS: the BDCI– predictor relationship is approximately linear and additive. A Lasso fit with L1 penalty automatically zeros five of twelve features, retaining a sparse set of seven predictors. 

**Table 3.** Test-set performance (95% bootstrap CI, 1,000 resamples). All four linear variants are statistically indistinguishable. 

|**Model**<br>**R**<sup>**2 **</sup>|**[95% CI]**|**MAE [95% CI]**|
|---|---|---|
|OLS<br>0.400|[0.257, 0.509]|9.38 [8.36, 10.52]|
|Ridge<br>0.401|[0.262, 0.506]|9.38 [8.36, 10.52]|
|Lasso<br>0.413|[0.281, 0.515]|9.28 [8.27, 10.38]|
|ElasticNet<br>0.414|[0.285, 0.514]|9.26 [8.27, 10.35]|
|SVR<br>0.388|[0.222, 0.506]|9.43 [8.34, 10.52]|
|ANN<br>0.375|[0.242, 0.481]|9.59 [8.49, 10.73]|



Figure 2 shows the ElasticNet SHAP beeswarm. Trait anxiety produces the widest spread of SHAP values by a wide margin: its mean _|_ SHAP _|_ exceeds health satisfaction (ranked second) by approximately 10fold. This apparent hierarchy is consistent across the cross-population transfer cohorts (Section 4.2): STAIT ranks first in every wave and in the non-medical student sample. 

### **4.2 The Hierarchy Appears Stable Across Cohorts** 

Table 4 shows transfer performance. The 7-feature reduced ElasticNet, trained exclusively on 2022 data, achieves R<sup>2</sup> of 0.443, 0.487, and 0.388 on the three longitudinal medical waves, and 0.493 on 701 non-medical students from eight faculties, the highest of any evaluation set. Figure 3 shows SHAP feature importance across all five cohorts. Trait anxiety holds rank 1 and health satisfaction holds rank 2 in every cohort; the full rank ordering is Trait Anxiety _>_ Health Satisfaction _>_ Age _>_ Psychotherapy _>_ Sex:Female _>_ Partnership _>_ Academic Year in all five evaluation sets. Kendall _τ_ = 1 _._ 0 for the top-two positions across all pairwise cohort comparisons. The apparent stability is striking. 

Section 4.3 tests whether this stability reflects a portable risk structure or a psychometric artefact. 

### **4.3 Residualization Audit: What Survives When the Depression Channel Is Removed?** 

Table 5 is the central result. Two baseline comparisons (primary BDCI and BDCI-A, an equal-weight variant) confirm that STAI-T dominates at rank 1 regardless of the weighting scheme. When CES-D is simply excluded from the outcome (BDCI-B), STAI-T remains rank 1 and R<sup>2</sup> falls from 0.414 to 0.303, a partial drop, because the MBI-SS burnout subscales themselves correlate with depression. 

The two residualization experiments go further. When STAI-T is replaced by residuals orthogonal to CES-D (Experiment 1), R<sup>2</sup> drops from 0.414 to 0.156 and STAI-T falls from rank 1 to rank 6 in mean absolute SHAP magnitude; health satisfaction becomes the dominant predictor. When the burnout outcome itself is purged of CES-D variance (Experiment 2, BDCI-C), R<sup>2</sup> collapses to 0.016: the full 12-feature model explains essentially none of the burnout-specific variance. 

Figure 4 summarises the residualization audit by plotting ElasticNet R<sup>2</sup> under each outcome/predictor definition. The collapse from the primary BDCI to STAI-T residualization and BDCI-C shows how much of the apparent signal depends on the anxiety– depression channel. 

These experiments answer the central question precisely. The standard pipeline predicts the depressionsaturated portion of the composite outcome well and the burnout-specific portion essentially not at all. The cross-cohort stability in Section 4.2 transfers because the STAI-T/CES-D psychometric correlation ( _r_ = 0 _._ 72) is structurally constant wherever these instruments are used together, not because the pipeline learned a portable multivariate risk structure. 

Health satisfaction is the most robust predictor of the depression-orthogonal signal (rank 1 in Experiment 1) and is the feature most likely to represent an 

4 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 



<!-- Start of picture text -->
ElasticNet SHAP Feature Importance<br>(Primary BDCI, 7-feature model) High<br>STAI-T<br>Health Sat.<br>Age<br>Sex:Female<br>Psychotherapy<br>Acad. Year<br>Partnership<br>Low<br>−15 −10 −5 0 5 10 15 20<br>SHAP value (impact on BDCI estimate)<br>Figure 2. ElasticNet SHAP beeswarm (primary BDCI, 7-feature model). Each point is one test-set observation; colour<br>encodes the raw feature value (red = high, blue = low). Trait anxiety (STAI-T) dominates by approximately 10-fold over<br>health satisfaction.<br>Table 4. Complete cross-cohort transfer. 7-feature ElasticNet trained on 2022 medical students; applied without retraining.<br>BDCI thresholds fixed at 2022 training-split percentiles.<br>SHAP Feature Hierarchy: Cross-Cohort and Cross-Population Stability<br>Feature Rank: Medical Cohorts + Non-Medical Transfer<br>Feature Importance: Medical (Temporal) vs. Non-Medical Transfer (1 = Most Important)<br>2022 Test W2 NMS Non-Med.<br>0.5 W1 W3 2022 Test 1 2 3 5 4 6 7<br>7<br>0.4 W1 1 2 3 5 6 4 7 6<br>5<br>0.3<br>W2 1 2 3 4 5 6 7 4<br>3<br>0.2<br>W3 1 2 3 5 4 6 7 2<br>0.1 1<br>NMS Non-Med. 1 2 3 4 5 6 7<br>0.0<br>Trait Anxiety Health Sat. AgePsychotherapy Sex: Female Acad. Year Partnership Trait Anxiety Health Sat. AgePsychotherapy Sex: Female Acad. Year Partnership<br>Feature value<br>Rank<br>Mean |SHAP value|<br><!-- End of picture text -->

|**Cohort**|**Description**|_n_|**R**<sup>**2**</sup>|**MAE**|
|---|---|---|---|---|
|2022 Test (7-feat)|Medical, reference split|178|0.423|9.23|
|2022 Test (12-feat)|Full feature model|178|0.414|9.26|
|Wave 1 (Mar. 2021)|Longitudinal medical|898|0.443|8.89|
|Wave 2 (Nov. 2021)|Longitudinal medical|723|0.487|7.98|
|Wave 3 (Nov. 2022)|Longitudinal medical|959|0.388|8.67|
|NMS|Non-medical, 8 faculties|701|0.493|8.89|



**Figure 3.** SHAP feature importance across all five evaluation cohorts. _Left_ : mean _|_ SHAP _|_ by feature and cohort. _Right_ : Feature importance rank heatmap (1 = most important; the white line separates medical from non-medical cohorts). Trait anxiety holds rank 1 and health satisfaction holds rank 2 in all five cohorts. 

independent burnout pathway. Researchers who report cross-cohort XAI stability without a residualization audit may be describing instrument correlation, not 

replicated science. 

5 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 

**Table 5.** Residualization audit. ElasticNet fitted under five conditions using the same 80/20 split and hyperparameter <u>grid.</u> The central finding is the R<sup>2</sup> collapse in the final two rows. 

|**Analysis**|**Outcome / predictor**|**R**<sup>**2**</sup>|**STAI-T rank**|**Interpretation**|
|---|---|---|---|---|
|Primary BDCI|STAI-T + MBI-SS + CES-D com-<br>posite|0.414|1|Apparent strong signal|
|BDCI-A|Equal-weight composite (no amplifi-<br>cation)|_≈_0_._42|1|Same pattern; robust to weight-<br>ing|
|BDCI-B|MBI-SS only (CES-D excluded)|0.303|1|Burnout-related signal persists;<br>MBI–CES-D correlation propa-<br>gates|
|BDCI-C|MBI-SS residualized against CES-D|0.016|_·_|Burnout-specific variance is es-<br>sentially unpredictable from this<br>feature set|
|STAI-T residualized|STAI-T _⊥_CES-D as predictor|0.156|6|Anxiety–depression channel ac-<br>counts for _≈_60% of model signal|





<!-- Start of picture text -->
Construct Overlap Audit — Sensitivity to Outcome and Predictor Definitions<br>(ElasticNet, same 80/20 split for all conditions)<br>Primary BDCI-B STAI-T BDCI-C<br>BDCI (no CES-D) residualised (MBI ⊥ CES-D)<br>0.5 0.5 0.5 0.5<br>R 2  = 0.414<br>0.4 0.4 0.4 0.4<br>R 2  = 0.303<br>0.3 0.3 0.3 0.3<br>0.2 0.2 0.2 R 2  = 0.156 0.2<br>0.1 0.1 0.1 0.1<br>R 2  = 0.016<br>0.0 0.0 0.0 0.0<br>Baseline: strong CES-D removed from Depression channel Burnout-specific<br>construct overlap present outcome: STAI-T still ranks 1 removed from STAI-T variance: near-zero<br>2ElasticNet R<br><!-- End of picture text -->

**Figure 4.** Construct-overlap residualization audit. ElasticNet R<sup>2</sup> under four outcome/predictor definitions using the same 80/20 split. Performance drops from R<sup>2</sup> = 0.414 for the primary BDCI to 0.156 after residualizing STAI-T against CES-D, and to 0.016 when burnout subscales are residualized against CES-D ( _BDCI-C_ ). BDCI-B (CES-D excluded from outcome) yields R<sup>2</sup> = 0.303, confirming that STAI-T’s dominance persists even when the depression component of the outcome is removed. 

### **4.4 Uncertainty Rules Out Individual Deployment** 

The non-conformity quantile from the calibration half was _q_ ˆ = 17 _._ 7 BDCI units. On the evaluation half ( _n_ eval = 89), empirical coverage was 84.3% (nominal target: 90%), and average interval width was 35.4 BDCI units (Figure 5). The _−_ 5 _._ 7 percentage-point coverage gap is within sampling noise: the standard deviation of a coverage estimate at true 90% with _n_ eval = 89 is _≈_ 3 _._ 2 pp, so the gap is approximately 1.8 standard deviations from nominal ( _p ≈_ 0 _._ 07). The headline finding is the interval width, not the coverage deviation. 

An interval of 35.4 units on a 0–100 scale is 2.4 outcome standard deviations ( _SD_ = 14 _._ 7). This width is fully determined by the model’s residual distribution; any uncertainty quantification method would pro- 

duce comparable intervals. It independently establishes that individual-level clinical prediction is not actionable with this feature set, regardless of the construct overlap finding. 

## **5 Discussion** 

This study’s central finding is the R<sup>2</sup> collapse: from 0.414 (primary BDCI) to 0.016 (burnout-specific BDCI-C), with an intermediate collapse to 0.156 when only the predictor is residualized. The implication is not that the primary model is wrong: the anxiety–depression nexus is one of the best-replicated constructs in psychiatric epidemiology, and the STAI= T/CES-D association ( _r_ 0 _._ 72) reflects genuine comorbidity [14]. The implication is that a standard multi-method XAI pipeline cannot distinguish this real clinical signal from a psychometric artefact without an 

6 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 



<!-- Start of picture text -->
Split Conformal Prediction Intervals (90% target)<br>Empirical coverage = 84.3%,  Avg width = 35.4 BDCI units<br>90 90% prediction interval<br>Point estimate (EN)<br>80 Observed (covered)<br>Observed (uncovered)<br>70<br>60<br>50<br>40<br>30<br>20<br>10<br>0 20 40 60 80<br>Student (sorted by point estimate)<br>BDCI Score<br><!-- End of picture text -->

**Figure 5.** Split conformal prediction intervals (90% target) for the ElasticNet model on the evaluation half ( _n_ = 89), sorted by point estimate. Shaded region: prediction band of width 2ˆ _q_ = 35 _._ 4 BDCI units (2.4 outcome SDs). Cross markers: uncovered observations (miss rate: 15.7%). 

explicit orthogonality check. Apparent stability across five cohorts is not evidence of a portable risk structure when the dominant predictor and the dominant outcome component share a latent construct. 

The residualization protocol introduced here is the paper’s transferable contribution. Any XAI study combining correlated predictor and outcome constructs (trait anxiety and depression are a prominent example, but any construct pair with _r >_ 0 _._ 5–0.6 warrants scrutiny) should apply this check before interpreting feature hierarchies as findings. The protocol requires only the fitted model and a linear regression of the predictor on the confounded outcome component; it adds no computational burden and produces a clear, quantitative audit. 

The apparently strong cross-cohort transfer (R<sup>2</sup> : 0.41–0.49 across five evaluation sets) deserves an honest characterisation. Wave 2 (0.487) and the non-medical cohort (0.493) exceed the internal test R<sup>2</sup> (0.423), but this is consistent with a stable two-variable relationship rather than broad generalisation: all three cohorts originate from the same institution and use identical instruments. Cross-institutional validation with heterogeneous instruments (instruments that break the STAI-T/CES-D fixed correlation) remains the essential next step before any deployment. 

The conformal width (35.4 BDCI units, 2.4 SDs) establishes a separate and independent bar for deployment. Even if the construct overlap were resolved by a better instrument design, individual-level prediction would require a substantially expanded feature set (likely ecological momentary assessment, physiological data, or longitudinal trajectories) to achieve actionable precision. The current paper quantifies the upper bound of what cross-sectional survey data can deliver under this instrument set. 

Health satisfaction emerges from the residualization experiments as the most durable predictor: after removing the STAI-T/CES-D channel, it ranks first in mean absolute SHAP magnitude. This aligns with Bozorgmehr and Weltermann [4] and Khan et al. [15], who identified health satisfaction and self-rated health as primary determinants in unrelated datasets and populations, suggesting that perceived health quality may be a more portable burnout signal than trait anxiety. Testing this hypothesis requires a study that separates the measurement constructs from the outset, not a posthoc residualization. 

### **5.1 Limitations** 

All datasets originate from the University of Lausanne; cross-institutional generalisability has not been tested. The primary analysis is cross-sectional; longitudinal within-student prediction would require a prospective design. The BDCI is a study-internal composite that has not been independently psychometrically validated. Potentially important predictors (financial stress, sleep quality, social support, institutional climate) are absent from the dataset and likely account for a substantial share of the unexplained variance. The clinicalyear calibration gap (R<sup>2</sup> = 0.294, _n_ = 66, versus 0.456 for pre-clinical) is directionally informative but statistically fragile at this subgroup size. 

### **5.2 Future Directions** 

The natural Phase II is a multi-site prospective study that: (a) recruits at least three institutions with structurally different curricula to obtain genuine crossinstitutional variation; (b) uses a prospective design in which pre-year surveys predict end-of-year burnout episodes or counselling referrals; (c) pre-registers the residualization audit as a primary endpoint to confirm 

7 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 

that the collapse is not an artefact of this particular cohort; and (d) extends the clinical-year feature set with ecological momentary assessment during clinical rotations to test the environmental hypothesis. 

## **6 Conclusion** 

A standard XAI pipeline applied to a burnoutdepression composite produces an apparently-robust, cross-population-stable risk hierarchy. Two residualization experiments show that this hierarchy is largely an artefact of construct overlap: removing the depression channel from the predictor (STAI-T _⊥_ CES-D) drops R<sup>2</sup> from 0.41 to 0.16; removing it from the outcome (MBI-SS subscales _⊥_ CES-D) drops R<sup>2</sup> to 0.016. The apparent cross-cohort stability (R<sup>2</sup> = 0.41–0.49, Kendall _τ_ = 1 _._ 0 for top-two positions across five cohorts) is explained by the fixed STAI-T/CES-D psychometric correlation ( _r_ = 0 _._ 72), not by a learned portable risk structure. Conformal prediction intervals averaging 35.4 BDCI units (2.4 outcome SDs) independently establish that individual-level prediction is not actionable. 

The residualization protocol is directly transferable: any XAI study that combines correlated predictor and outcome constructs should apply this check before reporting apparent stability as a finding. Researchers who skip this step may be describing instrument correlation, not replicated science. 

## **Data and Code Availability** 

The primary 2022 cross-sectional dataset is available from the authors upon reasonable request, subject to ethical approval. The temporal longitudinal cohort is openly available under CC-BY 4.0 at Zenodo (DOI: 10.5281/zenodo.8405764) [10]. The non-medical student cohort is openly available under CC-BY 4.0 at Zenodo (DOI: 10.5281/zenodo.15149289) [11]. Analysis code (Python) is available at `https://github.com/ alirezadehghan1/xai-burnout-depression` . 

## **Conflict of Interest** 

The authors declare no conflict of interest. 

## **Ethical Approval** 

The study uses anonymised secondary data collected under ethical approval of the University of Lausanne Faculty of Biology and Medicine (Protocol No. 201902134). 

## **References** 

- [1] Mohammed Al-Alawi, Hamed Al-Sinawi, Abdulaziz Al-Qubtan, Jawad Al-Lawati, Ahmad AlHabsi, Mohammed Al-Shuraiqi, Samir Al-Adawi, and Sathish Mundackal Panchatcharam. Prevalence and determinants of burnout syndrome and 

depression among medical students at Sultan Qaboos University: a cross-sectional analytical study from Oman. _Archives of Environmental & Occupational Health_ , 74(3):130–139, 2019. doi: 10.1080/ 19338244.2017.1400941. 

- [2] Narayan B. Pokhrel, Rajendra Khadayat, and Prakriti Tulachan. Depression, anxiety, and burnout among medical students and residents of a medical school in Nepal: a cross-sectional study. _BMC Psychiatry_ , 20(1):298, 2020. doi: 10.1186/s12888-020-02645-6. 

- [3] George Morcos and Omar A. Awan. Burnout in medical school: a medical student’s perspective. _Academic Radiology_ , 30(6):1223, 2022. doi: 10. 1016/j.acra.2022.10.004. 

- [4] Amir Bozorgmehr and Birgitta Weltermann. Prediction of chronic stress and protective factors in adults: development of an interpretable prediction model based on XGBoost and SHAP using national cross-sectional DEGS1 data. _JMIR AI_ , 2: e41868, 2023. doi: 10.2196/41868. 

- [5] Samiha Rashid, Taseen Badrul, Luthfun Rafid, Jarin Hora Setu, Nilufar Halder, and Aminul Islam. Ensemble and deep learning approaches for automated screening of anxiety, depression, and burnout in medical student populations. In _2024 IEEE International Conference on Digital Health (ICDH)_ , pages 1–10. IEEE, 2024. doi: 10.1109/ ICDH62654.2024.00010. 

- [6] Juan Pedro Martínez-Ramón, Francisco Manuel Morales-Rodríguez, and Fuensanta J. PérezLópez. Burnout, resilience, and COVID-19 among teachers: predictive capacity of an artificial neural network. _Applied Sciences_ , 11(17):8206, 2021. doi: 10.3390/app11178206. 

- [7] Germán V. Benito, Ximena Goldberg, Natalia Brachowicz, Gemma Castaño Vinyals, Nuria Blay, Ana Espinosa, Flavia Davidhi, Diana Torres, Manolis Kogevinas, and Rafael de Cid. Machine learning for anxiety and depression profiling and risk assessment in the aftermath of an emergency. _Artificial Intelligence in Medicine_ , 157: 102991, 2024. doi: 10.1016/j.artmed.2024.102991. 

- [8] Lilian Chioma Nnadi, Chukwuma P. Isiwu, Dian Ding, Dorel Mundeke Muepu, and Yutaka Watanobe. Multi-level explainable AI for predicting student depression risk: global, subgroup, and individual insights. _IEEE Access_ , 14:6271–6286, 2026. doi: 10.1109/ACCESS.2026.3456122. 

- [9] Valérie Carrard, Clément Bourquin, Sandra Berney, Kilian Schlegel, Jacques Gaume, PierreAlexandre Bart, Martin Preisig, Marianne Schmid Mast, and Alexandre Berney. The relationship between medical students’ empathy, 

8 

_Dehghan & Ashrafi: Auditing Construct Overlap in Explainable ML_ 

mental health, and burnout: a cross-sectional study. _Medical Teacher_ , 44(12):1392–1399, 2022. doi: 10.1080/0142159X.2022.2098708. 

- [10] Valérie Carrard, Clémence Bourquin, Sandra Berney, Kilian Schlegel, Jacques Gaume, Pierre-Alexandre Bart, Martin Preisig, Marianne Schmid Mast, and Alexandre Berney. Mental health and burnout during medical school: Longitudinal evolution and covariates. _PLOS ONE_ , 19(4):e0295100, 2024. doi: 10.1371/journal.pone. 0295100. 

- [11] Valérie Carrard, Céline Bourquin, Sylvie Berney, Pierre-Alexandre Bart, Patrick Bodenmann, and Alexandre Berney. Comparison of mental health and burnout between medical and nonmedical students. _PLOS ONE_ , 20(10):e0328145, 2025. doi: 10.1371/journal.pone.0328145. 

- [12] Waddah Saeed and Christian Omlin. Explainable AI (XAI): a systematic meta-survey of current challenges and future opportunities. _KnowledgeBased Systems_ , 263:110273, 2023. doi: 10.1016/j. knosys.2023.110273. 

- [13] Vladimir Vovk, Alex Gammerman, and Glenn Shafer. _Algorithmic Learning in a Random World_ . Springer, New York, 2005. 

- [14] David H. Barlow, Kristen K. Ellard, Christopher P. Fairholme, Todd J. Farchione, Christina L. Boisseau, Laura B. Allen, and Jill Ehrenreich-May. _Unified Protocol for Transdiagnostic Treatment of Emotional Disorders: Therapist Guide_ . Oxford University Press, New York, 2nd edition, 2014. 

- [15] Asif Ezaz Khan, Mohammad Jakir Hasan, Hosne Anjum, Noman Mohammed, and Sifat Momen. Predicting life satisfaction using machine learning and explainable AI. _Heliyon_ , 10(10):e31304, 2024. doi: 10.1016/j.heliyon.2024.e31304. 

9 

