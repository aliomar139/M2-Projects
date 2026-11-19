Results in Engineering 29 (2026) 109022 



Contents lists available at ScienceDirect 

# Results in Engineering 

journal homepage: www.sciencedirect.com/journal/results-in-engineering 



## An explainable data-driven optimization framework for industrial predictive maintenance scheduling 



Kassem Danach a,∗, Hassan Harb b, Hamza Issa c, Louai Saker b 

a _Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon_ b _College of Engineering and Technology, American University of the Middle East, Kuwait_ c _Faculty of Engineering, Beirut Arab University, Beirut, Lebanon_ 

### a r t i c l e i n f o 

### a b s t r a c t 

_Keywords:_ Artificial intelligence Explainable AI Data-Driven optimization Industrial systems Machine learning Predictive maintenance 

Unexpected equipment failures in industrial systems can lead to significant production downtime, increased operational costs, and reduced asset life cycles. Leveraging recent advancements in data science and intelligent decision-support systems, this paper proposes an explainable data-driven optimization and mathematical modeling framework for predictive maintenance scheduling in industrial environments. The framework integrates sensor-based condition monitoring data with machine learning models to forecast potential equipment failures before they occur. A supervised learning approach, implemented using gradient boosting and temporal feature engineering, predicts the remaining useful life (RUL) and failure probability of critical assets. An explainability layer, based on SHAP (SHapley Additive exPlanations) values, provides interpretable insights into the most influential factors contributing to predicted failures, enabling maintenance engineers to validate model outputs and trust automated recommendations. The predictive outputs are then embedded into a mixed-integer linear programming (MILP) model to generate optimal maintenance schedules that minimize total downtime and maintenance costs while satisfying operational constraints such as resource availability and production deadlines. The proposed framework is validated using a combination of publicly available predictive maintenance datasets and real-world industrial sensor data. Experimental results demonstrate a reduction of up to 22% in unplanned downtime and 15% in maintenance costs compared to reactive and preventive maintenance strategies, while maintaining high interpretability for domain experts. This integrated approach highlights the potential of combining explainable AI, predictive analytics, and mathematical optimization for sustainable and efficient industrial operations. 

#### **1. Introduction** 

Unplanned equipment failures remain a primary source of production losses in capital-intensive industries. The immediate consequences, line stoppages, expedited work orders, overtime labor, and scrap, inflate operating expenditures and accelerate asset degradation, while secondary effects cascade through inventories, order fulfillment, and safety margins. Advances in condition monitoring have made high-frequency vibration, temperature, acoustic, electrical, and process signals widely available on the shop floor, enabling data-driven prognostics that estimate remaining useful life (RUL) and short-horizon failure risk [1]. Furthermore, recent optimization frameworks have demonstrated sophisticated planning techniques that integrate operations and resource allocation under dynamically changing constraints, exemplified by location planning for unmanned aerial vehicles aimed at maintaining critical service coverage in crisis situations. Yet, despite notable progress in learn- 

ing accurate prognostic models, converting these predictions into operationally feasible schedules remains challenging. Planners must respect resource capacities, intervention durations, access and safety windows, and production deadlines, all while balancing downtime and maintenance cost. As a result, many plants still rely on reactive responses, rigid time-based preventive policies, or handcrafted rules that fail to exploit asset-level risk signals, yielding suboptimal intervention timing and resource utilization [2]. 

Predictive Maintenance (PdM) is a subset of Prognostics and Health Management (PHM) that focuses specifically on failure prediction and maintenance scheduling [3]. While PHM encompasses broader health assessment and management strategies, PdM targets the optimization of maintenance interventions based on predictive analytics. This distinction is important as our framework specifically addresses the scheduling challenges within PdM, leveraging explainable AI to bridge the gap between prognostic insights and operational decisions. 

> ∗ Corresponding author. 

> _E-mail addresses:_ kassem.danach@mu.edu.lb (K. Danach), hassan.harb@aum.edu.kw (H. Harb), h.issa@bau.du.lb (H. Issa), louai.saker@aum.edu.kw (L. Saker). 

https://doi.org/10.1016/j.rineng.2026.109022 

Received 26 October 2025; Received in revised form 31 December 2025; Accepted 5 January 2026 

> Available online 9 January 2026 

> 2590-1230/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/bync-nd/4.0/ ). 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

#### _1.1. Problem context and statement_ 

This work studies the end-to-end pipeline that links prognostics to maintenance execution. We consider a set of assets indexed by _𝑖_ ∈  monitored over discrete periods _𝑡_ ∈  with multivariate sensor streams and historical maintenance logs. The learning task is to produce timedependent predictions of (i) RUL, denoted _̂𝑟𝑖_ ( _𝑡_ ), and (ii) the probability that asset _𝑖_ fails within a look-ahead window _𝜏_ , denoted _̂𝑝𝑖_ ( _𝑡, 𝜏_ ). These predictions are then used to plan maintenance start times, task types, and crew allocations over the horizon  so as to minimize a weighted combination of expected unplanned downtime and direct maintenance costs. The schedule must satisfy practical constraints, including crew and tooling capacities, non-overlap of tasks on the same asset, access and safety windows, and interactions with production campaigns. The core difficulty is twofold: predictive uncertainty and potential miscalibration can distort perceived risk, and the mapping from probabilistic risk to optimization penalties is often ad hoc, obscuring traceability between forecasts and decisions. 

#### _1.2. Proposed framework_ 

We propose an explainable data-driven optimization and mathematical modeling framework that couples calibrated prognostics with mixedinteger linear programming (MILP). On the prediction side, we adopt supervised learning with gradient-boosted decision trees and time-aware feature engineering to model degradation dynamics and near-term failure likelihoods [4,5]. Strict temporal splits and probability calibration are used to reduce look-ahead bias and improve reliability under deployment shift. To make the learned signals auditable, we incorporate an explainability layer based on SHAP (SHapley Additive exPlanations), providing global importance profiles and local attributions that expose which sensor trends, lags, and rolling statistics most strongly drive risk at a given time [6]. On the decision side, we embed the predictive outputs into an MILP that schedules preventive and corrective actions while respecting all operational constraints typical of industrial settings [7]. The coupling is explicit: predicted RUL influences soft deadlines and tardiness penalties; calibrated failure probabilities shape risk-weighted costs; and SHAP-identified drivers guide priority rules when resources are scarce. A rolling-horizon control loop updates predictions as new telemetry arrives and re-optimizes the schedule, thus aligning plan responsiveness with the pace of asset degradation. 

#### _1.3. Research questions and hypotheses_ 

The study evaluates four questions central to trustworthy PdM scheduling. First, we ask how accurately gradient-boosted models with temporally engineered features can predict RUL and short-horizon failure risk under time-ordered validation. Second, we examine the stability and actionability of SHAP-based explanations across assets and time, and how these diagnostics support model acceptance and policy refinement on the shop floor. Third, we quantify how an explicit, auditable mapping from predictive signals to MILP objectives and constraints affects realized downtime, cost, and feasibility relative to reactive and time-based preventive baselines. Fourth, we analyze robustness: we stress-test the pipeline under forecast errors, constrained resources, and tight production deadlines, and measure the benefit of rolling-horizon replanning in recovering performance. 

- Second, it develops a traceable coupling from calibrated risks and SHAP insights to optimization artifacts, risk-weighted costs, RULaligned soft constraints, and principled priority rules, thereby clarifying how predictions influence downstream decisions. 

- Third, it formulates a maintenance-scheduling MILP that captures resource capacities, non-overlap, access and production windows, and optional tardiness penalties, and it implements an efficient rollinghorizon solver suitable for routine re-planning [7]. 

- Fourth, it provides a comprehensive empirical evaluation on public PdM corpora (e.g., C-MAPSS and IMS bearings) and a real industrial dataset, demonstrating up to 22% reductions in unplanned downtime and 15% lower maintenance costs compared with reactive and time-based preventive strategies, while preserving interpretability for domain experts [8,9]. 

Furthermore, our contributions span three dimensions: 

- _Architectural_ : Explicit coupling of SHAP-based risk attributions to MILP parameters enabling traceable decision-making. 

- _Methodological_ : Stability-tested temporal explainability and conformalized uncertainty quantification for reliable risk assessment; 

- _Empirical_ : First validation across public benchmarks and multi-sector industrial data demonstrating practical feasibility. 

#### _1.5. Scope and significance_ 

By unifying explainable prognostics with mathematical programming, the framework moves beyond black-box or siloed approaches. It supports auditability, engineers can inspect why a particular intervention was recommended; adaptability, rolling-horizon updates align plans with evolving degradation; and feasibility, explicit constraints encode operational realities. Although we instantiate the approach with gradient boosting and MILP for clarity and speed, the interface is method-agnostic and can accommodate alternative predictors such as temporal convolutional or transformer models and alternative decision layers such as robust MILP or constraint programming with minimal changes to the coupling. 

#### _1.6. Paper organization_ 

The remainder of the paper is organized as follows. Section 2 reviews predictive maintenance modeling, explainable AI for prognostics, and optimization approaches to maintenance scheduling, highlighting integration gaps. Section 3 describes the datasets, assets, sensing modalities, and temporal feature engineering, as well as the training, validation, and calibration protocols. Section 4 details the predictive models and the SHAP-based explainability layer. Section 5 presents the MILP formulation and the learning-to-optimization coupling together with the rolling-horizon solution strategy. Section 6 presents the end-to-end pipeline including the system architecture and thee pseudocode of the proposed algorithms. Section 7 specifies baselines, metrics, and implementation settings. Section 8 reports predictive accuracy and calibration, interpretability findings, scheduling performance, ablations, and robustness analyses. Section 9 discusses practical implications, limitations, and threats to validity. Section 10 concludes and outlines avenues for future work. 

#### _1.4. Contributions_ 

This paper makes four contributions that advance the integration of prognostics and operations: 

- First, it presents an explainable prognostics pipeline tailored to industrial data, combining gradient boosting, temporal feature engineering, and probability calibration with SHAP-based global and local explanations [4–6]. 

#### **2. Related work and background** 

The integration of data-driven techniques, explainability, and optimization has become pivotal in enhancing predictive maintenance (PdM) and operational decision-making for industrial systems [10–13]. This section elaborates on the major research themes underpinning these advances. 

2 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

#### _2.1. Predictive maintenance strategies_ 

Predictive maintenance aims to anticipate equipment failures by leveraging historical and real-time sensor data to estimate remaining useful life (RUL) or failure risk [1,14–17]. Traditional PdM methods rely on physics-based degradation models or statistical approaches [18], whereas contemporary efforts increasingly adopt machine learning (ML) and deep learning (DL) frameworks, exploiting complex, multivariate telemetry [19,20]. Techniques include supervised regression and classification [21], survival analysis for hazard estimation [22], and anomaly detection-based schemes [23]. Temporal feature extraction and sensor fusion remain crucial for accurate and robust predictions [24], often implemented with sliding or rolling window methods [25]. Recent advancements also explore hybrid sensor network topologies that enhance data collection reliability and energy efficiency, thereby supporting sustained, high-quality data streams critical for effective PdM [26]. Recent advances in RUL prediction have focused on deep learning approaches and ensemble methods to improve accuracy and robustness [27–29]. 

#### _2.2. Explainable AI in industrial analytics_ 

As PdM models increasingly influence high-stakes decisions, the demand for explainability grows [30,31]. Explainable AI (XAI) techniques facilitate trust and transparency by clarifying model predictions through local and global interpretability [6,32]. Approaches like SHAP values [6] and LIME [32] provide additive feature attributions clarifying the influence of input variables on predicted risks. In industrial contexts, explanations enable engineers to validate model outputs, identify actionable signals, and support governance and auditability [33,34]. Recent works explore embedding explanations within human-in-the-loop workflows and policy tuning frameworks [35,36]. However, most XAI applications in PdM focus on model interpretability without explicitly connecting explanations to operational decisions [37]. 

#### _2.3. Mathematical optimization for maintenance scheduling_ 

Optimizing maintenance schedules is essential for reducing downtime and operational costs [38,39]. Classical models address preventive and corrective maintenance utilizing integer or mixed-integer linear programming (MILP) formulations [7,40]. These models encode constraints related to resource allocation, workforce scheduling, spare parts availability, and production interference [41]. More recent methods integrate predictive insights such as risk estimates or RUL predictions to prioritize maintenance actions dynamically [42,43]. Multi-objective optimization approaches balance trade-offs between maintenance costs, downtime, and reliability [44]. Recent developments in maintenance optimization have focused on integrating machine learning predictions with robust optimization techniques to handle uncertainty [45–47]. 

#### _2.4. Data-driven optimization frameworks_ 

Combining ML predictions with mathematical optimization to close the prediction-to-action gap has gained prominence [48]. Frameworks integrate calibrated failure probabilities or RUL metrics as parameters or constraints within scheduling MILPs [2,49]. Risk-informed cost functions and robust optimization techniques ensure solutions withstand predictive uncertainty [50,51]. Rolling-horizon and decomposition methods improve scalability for large-scale industrial scenarios [52,53]. Hybrid solution methods merging heuristics, metaheuristics, and exact solvers address combinatorial complexity [54,55]. Despite these advances, existing frameworks often lack explicit traceability between predictive insights and optimization decisions, limiting their adoption in safety-critical industrial environments [56]. 

#### _2.5. Human-in-the-loop and governance aspects_ 

Operational PdM systems must reconcile automated optimization with human expertise [57]. Human-in-the-loop paradigms incorporate engineer feedback on model explanations and schedule decisions to refine system performance [58]. Explainability underpins governance, compliance, and accountability in safety-critical environments, necessitating traceability and reproducibility of decisions [59,60]. Policy-ascode frameworks enable formalizing risk appetite, operational priorities, and constraints into adjustable parameters for continual improvement [61]. 

#### _2.6. Positioning of our work_ 

The intersection of predictive maintenance, explainable AI, and optimization has resulted in integrated frameworks capable of producing actionable, trustworthy, and resource-aware maintenance schedules. Despite significant advances, challenges remain in scalability, uncertainty quantification, causal inference, and real-time responsiveness. This work builds on these foundations by proposing a unified framework that tightly couples reliable data-driven predictions, interpretable explanations, and robust MILP-based scheduling under realistic operational constraints. As highlighted in Table 1, our framework uniquely addresses the integration gaps in existing approaches by providing explicit traceability between SHAP-based explanations and optimization decisions, incorporating uncertainty-aware scheduling, and validating across multiple industrial sectors. Unlike prior works that treat prediction, explanation, and optimization as separate components, our approach establishes a seamless coupling where explainability directly informs decision-making, enabling auditable and adaptive maintenance scheduling in industrial environments. 

#### **3. Data and problem context** 

This section specifies the operational setting and sensing modalities, details the public benchmarks and the Lebanese industrial corpus used for validation, defines the learning targets consumed by the predictive layer and the decision parameters required by the scheduler, and documents the preprocessing and temporal feature engineering steps that transform raw telemetry and maintenance logs into analysis-ready panels. 

#### _3.1. Assets, sensors, and operating regimes_ 

The study considers a heterogeneous fleet of production assets _𝑖_ ∈  operating under time-varying regimes _𝑡_ ∈  and instrumented with multi-rate sensing. Rotating equipment such as motors, pumps, fans, compressors, bearings, and gearboxes are monitored by tri-axial accelerometers for high-frequency vibration and envelope signals, complemented by thermocouples or RTDs for temperature and electrical transducers for current, voltage, and power factor. Process equipment contributes pressure, flow, level, and quality analyzers sampled via the plant historian or DCS/SCADA. Sampling spans sub-second to minute scales: vibration snapshots are acquired at 12-25 kHz in one- to two-second bursts at regular intervals or on threshold triggers; process and electrical channels are typically recorded every one to ten seconds. Exogenous and endogenous operating conditions, line speed, load and torque, upstream/downstream buffers, ambient temperature and humidity, product mix, and shift patterns, modulate both levels and variability of signals and are encoded as regime descriptors _𝑟𝑖_ ( _𝑡_ ) to control for confounding and to support stratified validation. Maintenance interventions produce structural breaks in the telemetry; to preserve stationarity within episodes, each asset’s timeline is segmented into intervals bounded by interventions and major configuration changes, and labels and features are computed within those stable segments. 

3 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 1** 

Comparison with State-of-the-Art integrated PdM frameworks. 

|Framework|Exp<br>Cou|lainability-Optim<br>pling|ization|Uncertainty-Aware<br>Scheduling|Temporal Fe<br>Engineering|ature|Rolling-Horizon<br>Implementation|Multi-Industry<br>Validation|
|---|---|---|---|---|---|---|---|---|
|Bossche et al. [2]|×|||×|×||×|×|
|Kim et al. [62]|×|||✓|✓||×|×|
|Lundberg et al. [6]|×|||×|✓||×|×|
|Zhang et al. [27]|×|||✓|✓||✓|×|
|Proposed Framework|✓|||✓|✓||✓|✓|
|**Table** **2**|||||||||
|Dataset summary|.||||||||
|Dataset<br>|Assets|Time Horizon|Failures|Train/Val/Test|_𝜏_ (hours)|Samplin|g Rates||
|C-MAPSS<br>|100|-|-|70%/15%/15%|24|1 Hz|||
|IMS Bearings<br>|4|35 days|4|60%/20%/20%|24|20 kHz|||
|SECOM<br>|1567|-|104|70%/15%/15%|24|1 Hz|||
|Lebanese<br>|87|18–36 mo|312|60%/20%/20%|72|1–5 Hz|(process), 12–25 k|Hz (vibration)|



#### _3.2. Industry-specific adaptations_ 

The framework adapts to different industry types through parameter adjustments and feature prioritization: 

- **Process industries** (e.g., cement, chemicals): Continuous operation with 24-hour maintenance windows ( _𝐴𝑖𝑡_ ). SHAP feature weights prioritize temperature and pressure signals. Fault characteristics are progressive, requiring longer look-ahead windows ( _𝜏_ = 72 hours). 

- **Discrete manufacturing** (e.g., packaging, food processing): Shiftbased operation with 8-hour maintenance windows. Vibration and electrical features receive higher SHAP weights. Fault characteristics can be sudden, requiring shorter look-ahead windows ( _𝜏_ = 24 hours). 

These adaptations are implemented through industry-specific configuration files that adjust the MILP constraints and feature engineering parameters. 

#### _3.3. Datasets_ 

The evaluation combines widely used public benchmarks with data collected from Lebanese industries to balance reproducibility with ecological validity. Public datasets include the NASA C-MAPSS turbofan engine degradation simulations (Table 2), which provide multivariate engine telemetry across multiple fault modes and operating conditions and are standard for remaining useful life (RUL) estimation under regime shift; the IMS bearing run-to-failure experiments, which offer high-frequency vibration recordings under controlled loads and speeds and are canonical for detecting incipient faults via spectral and envelope features; and a representative process-quality dataset (SECOM or equivalent), which supplies medium-frequency process variables with defect annotations and stresses feature selection and drift handling in correlated environments. These corpora collectively exercise the pipeline across propulsion-like telemetry, high-rate mechanical vibration, and process control sensors, and they permit direct comparison with prior literature. 

The Lebanese industrial dataset was assembled in collaboration with multiple manufacturing facilities that reflect the country’s sectoral mix, including food and beverage processing, cement and building materials, plastics and packaging, and selected pharmaceutical and chemical lines. Sites are geographically distributed across coastal and inland regions, exposing equipment to distinct environmental stressors such as sea-salt aerosol near the coast, dust loading in cement milling, and elevated summer temperatures and humidity. Sensor specifications include: (1) Vibration: tri-axial accelerometers (PCB 356A16) with 12–25 kHz sampling, sensitivity 100 mV/g, anti-aliasing filters; (2) Temperature: RTDs (Pt100) with ±0.1°C accuracy; (3) Electrical: current transducers (LEM LA 55-P) with 0-50A range. Data quality procedures include automated 

validation checks (range tests, spike detection) and manual verification by domain experts. Instrumentation follows a pragmatic, retrofitted pattern common in the region: legacy assets are augmented with edge vibration collectors and wireless temperature nodes, while newer equipment integrates directly with the historian. Vibration data consist of periodic or event-triggered bursts sampled between 12 and 25 kHz with calibrated sensitivity and anti-aliasing; process and electrical channels are historian tags sampled at one- to five-second intervals, with occasional faster trends during transient operations. Maintenance events are recorded in the computerized maintenance management system (CMMS) with standardized codes for failure modes and repair actions, time stamps synchronized to historian time via plant-wide NTP. Workorder narratives are bilingual (Arabic/English, occasionally French), which necessitates text normalization and controlled-vocabulary mapping for downstream analytics. The observation horizon spans between eighteen and thirty-six months per line, covering multiple overhaul cycles and seasonality. 

The Lebanese context introduces distinctive operating regimes and data considerations that are explicitly modeled. Electrical supply intermittency and generator switchover events can induce voltage sags, transient harmonics, and short production halts; these are represented as exogenous regime flags and are filtered from degradation signals to avoid spurious correlations. Dust and particulate exposure in heavy industry increase sensor fouling and accelerate bearing wear; routine cleaning cycles and filter replacements are captured in the CMMS and used to bound post-maintenance recovery windows. Ambient seasonality associated with Mediterranean climate patterns and heat waves influences thermal baselines and viscosity-dependent processes; slow drifts in temperaturerelated channels are de-trended or normalized within regime strata. Data governance follows contractual non-disclosure agreements and internal privacy policies: identifiers for assets, operators, and facilities are pseudonymized; free-text fields are scrubbed of personally identifiable information; and reporting aggregates omit low-level details that could enable reverse identification. The result is a multi-site, multisector Lebanese corpus that is representative of regional operational realities while meeting reproducibility and privacy constraints. 

#### _3.4. Labels and targets_ 

Two complementary targets drive the learning-to-decision pipeline. The first is the remaining useful life _𝑟𝑖_ ( _𝑡_ ) = _𝑡_<sup>∗</sup> _𝑖_<sup>−</sup><sup>_𝑡_,where</sup><sup>_𝑡_∗</sup> _𝑖_<sup>denotesthe</sup> earliest time a domain-validated failure occurs or an end-of-life threshold is crossed for asset _𝑖_ . When _𝑡_<sup>∗</sup> _𝑖_<sup>fallsoutsidetheobservationwindow,</sup> _𝑟𝑖_ ( _𝑡_ ) is right-censored; censored tails are excluded from point-regression training and are handled using survival analysis techniques (KaplanMeier estimation and Cox proportional hazards models) in sensitivity analyses. The second target is a short-horizon failure indicator _𝑦_<sup>(</sup> _𝑖,𝑡_<sup>_𝜏_)that</sup> 

4 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

equals one if a verified failure occurs within the next _𝜏_ time units and zero otherwise. The look-ahead _𝜏_ is aligned with the minimum schedulable reaction time and typical work-order durations in the participating Lebanese plants to ensure operational relevance of risk predictions. CMMS logs differentiate planned preventive actions, condition-based tasks, and corrective repairs; these annotations are used to censor RUL around planned overhauls, to validate failure onsets, and to quantify post-maintenance recovery periods. Because failures are rare relative to healthy operation, the class distribution of _𝑦_<sup>(</sup> _𝑖,𝑡_<sup>_𝜏_)ishighlyimbalanced;</sup> sampling weights and probability calibration are therefore chosen to preserve deployment-level base rates so that forecasted risks _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) remain numerically meaningful to the scheduler. 

dows meeting a minimum completeness threshold are retained. Outliers are identified with robust statistics such as median absolute deviation and, for spectra, Hampel filtering in frequency; extreme values are clipped rather than discarded when consistent with plausible operating extremes, particularly in heavy-industry contexts where shock loads and dust-induced imbalance can transiently elevate vibration. Finally, the dataset is partitioned chronologically by asset into training, validation, and test sets, holding out entire terminal segments to emulate forward-in-time generalization. Hyperparameters and probability calibration are tuned on validation only, after which models are frozen and evaluated on the subsequent test horizon. This protocol yields the supervised panel {( **𝐳** _𝑖,𝑡, 𝑟𝑖_ ( _𝑡_ ) _, 𝑦_<sup>(</sup> _𝑖,𝑡_<sup>_𝜏_))}thatunderpinsthepredictivelayerand</sup> provides calibrated risk signals for the mixed-integer scheduling model. 

#### _3.5. Preprocessing and temporal feature engineering_ 

#### **4. Predictive modeling** 

Preprocessing harmonizes clocks, removes artifacts, and constructs causal, informative features while respecting the chronology required for deployment. Time alignment reconciles historian and edge-device stamps; low-frequency channels are forward-filled within physically justified hold intervals and are otherwise interpolated conservatively, whereas high-frequency vibration snapshots are anchored at acquisition times and treated as independent frames. Data quality procedures include: (1) Automated validation checks for sensor ranges, spike detection, and communication errors; (2) Manual verification by domain experts for ambiguous cases; (3) Regular calibration of sensors against reference standards. Instrument resets, saturations, and communication glitches are identified by spike detection and flag patterns and are winsorized or excised depending on physical plausibility. Offset jumps are detected with cumulative sum change-point tests; slow thermal or seasonal drifts are de-trended when separable from degradation. For vibration, each frame is de-meaned and tapered before feature extraction in time and frequency domains. Extracted descriptors include root-meansquare, variance, skewness, kurtosis, crest and shape factors, bandlimited energies, spectral centroid and bandwidth, spectral kurtosis, envelope spectra near bearing characteristic frequencies, and cepstral coefficients; in cement and dusty environments, band selection is adapted to the measured noise floor. For propulsion-like telemetry, health indices combine temperature ratios, pressure differentials, and normalized fuel or power flow; for process sensors, features include lagged differences, exponentially weighted moving averages, rolling quantiles, Z-normalized control statistics, and residuals from local linear or autoregressive models to isolate deviations from regime baselines. Generator switchover and grid perturbation events are marked as exogenous regime variables and are either excluded from training windows or modeled explicitly to prevent the learner from mistaking power-quality transients for incipient mechanical defects. 

Temporal structure is encoded via fixed-length windows of size _𝐿_ and stride _𝑠_ . For each asset-time pair ( _𝑖, 𝑡_ ), the input vector **𝐳** _𝑖,𝑡_ concatenates lag and (strictly causal) lead proxies, rolling aggregates such as mean, standard deviation, median absolute deviation, range, and interquartile range, trend coefficients from windowed regressions, and Fourier terms at shift and daily frequencies to approximate seasonality. Window sizes are selected per sensor family to balance early detection with noise suppression: vibration windows span multiple frames to stabilize spectral estimates; process windows cover several control cycles; electrical windows include sufficient pre- and post-switchover samples to model transients without leakage. All normalization parameters are estimated on the training split only and applied unchanged to validation and test to avoid peeking. Sensor drift over months is monitored using population stability indices and two-sample tests on feature marginals; when drift is detected, regime-conditional normalization keyed by _𝑟𝑖_ ( _𝑡_ ) is applied, or baselines are re-estimated on rolling windows. 

Missingness is addressed hierarchically. Short gaps in slow channels are filled with constrained interpolation bounded by engineering limits; longer gaps trigger segment exclusion or down-weighting to reduce bias. For fast channels, missing frames remain missing, and only win- 

This section details the supervised learning pipeline used to generate the risk and health forecasts consumed by the scheduler, the explainability layer that renders model logic auditable to engineers, and the uncertainty quantification procedures that translate predictive confidence into decision-aware guardrails. Throughout, inputs are the temporally engineered feature vectors **𝐳** _𝑖,𝑡_ and regime descriptors from Section 3, and targets are the remaining useful life _𝑟𝑖_ ( _𝑡_ ) and the short-horizon failure indicator _𝑦_<sup>(</sup> _𝑖,𝑡_<sup>_𝜏_)definedtherein.</sup> 

#### _4.1. Supervised learning setup_ 

The forecasting layer comprises two tree-ensemble learners trained jointly on aligned panels but with task-specific objectives. For remaining useful life (RUL), we employ gradient boosting with a robust regression loss to mitigate the influence of noisy tail labels. Let _̂𝑟𝑖_ ( _𝑡_ ) = _𝑓𝜃_<sup>RUL</sup> ( **𝐳** _𝑖,𝑡_ ) denote the point predictor. The objective minimizes a Huber loss _𝐿𝛿_ with scale _𝛿_ chosen on the validation set to balance bias and variance: 



<!-- Start of picture text -->
1 2 𝑒 2 , | 𝑒 | ≤ 𝛿,<br>RUL( 𝜃 ) = | RUL train | ( 𝑖,𝑡 )∈∑ RUL train 𝐿𝛿 ( 𝑟𝑖 ( 𝑡 ) − ̂ 𝑟𝑖 ( 𝑡 )) 𝐿𝛿 ( 𝑒 ) = { 1 𝛿 (| 𝑒 | − 1 2 𝛿 ) , | 𝑒 |  > 𝛿. (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
For short-horizon failure risk, we train a gradient-boosted classifier<br>𝑓𝜃 CLS ( 𝐳 𝑖,𝑡 ) = ̂ 𝑝𝑖 ( 𝑡, 𝜏 ) using a class-weighted logistic loss to address rarity:<br>1<br>CLS( 𝜃 ) = ∑ ( 𝑤 1  𝑦 ( 𝑖,𝑡 𝜏 ) log ̂ 𝑝𝑖 ( 𝑡, 𝜏 ) − 𝑤 0 (1 − 𝑦 ( 𝑖,𝑡 𝜏 )) log (1 − ̂ 𝑝𝑖 ( 𝑡, 𝜏 ))) , (2)<br>| CLS train | ( 𝑖,𝑡 )∈ CLS train<br><!-- End of picture text -->

where ( _𝑤_ 1 _, 𝑤_ 0) are set inversely proportional to class frequencies and then tuned within a narrow range to stabilize calibration. Both learners use histogram-based gradient boosting (e.g., XGBoost/LightGBM-style split finding) with shrinkage, column subsampling, and early stopping. Hyperparameters, number of trees, maximum depth, learning rate, minimum child weight, subsampling rates, and L1/L2 regularization, are selected by Bayesian optimization over a bounded search space with time-ordered, blocked cross-validation that preserves the forward-intime constraint and avoids leakage across overlapping windows. Each fold holds out complete terminal segments by asset and evaluates _𝑓𝜃_<sup>RUL</sup> via MAE/RMSE and _𝑓𝜃_<sup>CLS</sup> via AUROC/AUPRC on the validation horizon, with additional checks on lead-time sensitivity by conditioning on proximity to failure. 

Probability calibration is performed post-hoc on _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) using a monotone mapping trained on the validation fold and frozen before test. When the reliability curve is approximately sigmoidal, we adopt Platt scaling; when it is piecewise and nonparametric, we use isotonic regression. The chosen calibrator minimizes the Brier score on validation and passes a Spiegelhalter-style calibration test at nominal levels. Because the scheduler consumes continuous risks rather than hard decisions, operating thresholds are not used for primary evaluation; when an alerting threshold is required for plant HSE protocols, it is derived from a cost ratio consistent with the downstream objective, thereby maintaining decision-theoretic coherence between prediction and optimization. For RUL, all preprocessing and scaling parameters are fitted on the training 

5 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 3** 

Model performance comparison. 

|Model|RUL<br>MAE|Runtime<br>(s))|AUROC|SHAP<br>Stability|
|---|---|---|---|---|
|XGBoost|12.3|0.8|0.92|0.92|
|LSTM|14.7|4.2|0.89|0.85|
|Temporal Fusion|||||
|Transformer|13.1|6.1|0.90|0.87|



period only and applied unchanged to validation/test; residual analyses confirm that remaining bias is predominantly multiplicative in latelife regimes, which motivates a complementary quantile treatment in Section 4.4. Table 3 shows the performance results for each model. 

#### _4.2. Explainability layer_ 

To make the learning-decision pipeline auditable, we attach an explainability layer based on SHAP values computed with TreeSHAP for the trained ensembles. For any prediction at ( _𝑖, 𝑡_ ), the local attribution vector **_𝝓_** _𝑖,𝑡_ satisfies<sup>∑</sup> _𝑗_<sup>_𝜙_(</sup> _𝑖,𝑡_<sup>_𝑗_)=</sup><sup>_̂ 𝑔𝑖,𝑡_−𝔼[</sup><sup>_𝑔_(</sup><sup>**𝐳**)],where</sup><sup>_𝑔_isthemodel’slink</sup> function (identity for RUL, log-odds for classification). Local explanations are rendered as waterfall and force plots to communicate the additive contribution of lagged features, rolling statistics, and regime descriptors to an individual risk estimate or RUL forecast. Global behavior is summarized by aggregating **_𝝓_** _𝑖,𝑡_ across time and assets to obtain importance rankings, distributional beeswarms, and dependence curves that expose nonlinearities and interaction proxies. Because prognostics are intrinsically temporal, we compute time-aware aggregates by aligning attributions relative to failure onset and by smoothing over short horizons to suppress attribution flicker; this yields stable, interpretable evolution of the dominant drivers as equipment approaches end of life. 

#### _4.3. Fault-mode explainability analysis_ 

We analyze the stability and actionability of SHAP-based explanations for different fault characteristics: progressive faults (e.g., bearing wear) and sudden faults (e.g., electrical short circuits). For progressive faults, SHAP attributions show high stability (Jaccard similarity > 0.8) with consistent dominant features (vibration kurtosis, temperature trends). For sudden faults, attributions exhibit higher variability but are stabilized through temporal smoothing. Fig. 1 illustrates these differences, showing how attribution patterns evolve differently for each fault type. This analysis confirms that our explainability layer provides reliable insights across diverse failure modes, enhancing engineer trust in the system. 

Attribution stability and validity are formally assessed before any engineer-facing artifact is released. Across folds and across Lebanese sites with distinct environmental stressors, we quantify stability using rank correlations of global top- _𝑘_ features and Jaccard overlaps of their sets; confidence bands around dependence curves are obtained by bootstrap over assets to ensure statements about drivers are not dominated by a single line. Sanity checks include model randomization tests, where labels/features are permuted to verify that structure in **_𝝓_** _𝑖,𝑡_ vanishes, and feature perturbation tests, where synthetic shifts in salient features produce commensurate and directionally consistent changes in predictions. Physical plausibility is enforced by cross-checking attribution signs against first-principles expectations, for example, increases in vibration kurtosis or band-limited energy near known defect frequencies should not reduce predicted risk, and by inspecting counterexamples when violations occur. The explainability layer produces operational artifacts tailored to maintenance planners: ranked drivers per asset and per horizon, "what-if" counterfactuals that quantify the smallest feature adjustments needed to bring risk below a safety threshold (subject to feasibility constraints such as nonnegativity and bounded rates of change), 



**Fig. 1.** SHAP dependence plots for representative vibration and process features with smoothed confidence bands from asset-level bootstrap. 

and temporal attribution traces that annotate Gantt plots in the scheduler with the reasons behind recommended interventions. These artifacts are archived with model versioning so that any schedule can be retrospectively audited to the feature level. 

#### _4.4. Uncertainty quantification_ 

The scheduler benefits from calibrated measures of dispersion around point forecasts to hedge against optimistic plans. For RUL, we fit quantile gradient boosting models _̂𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_)(</sup><sup>_𝑡_)atmultiplequantilelevels</sup> _𝑞_ ∈{0 _._ 1 _,_ 0 _._ 25 _,_ 0 _._ 5 _,_ 0 _._ 75 _,_ 0 _._ 9} by minimizing the pinball loss 



<!-- Start of picture text -->
1<br>QR( 𝜃𝑞 ) = | RUL train | ∑( 𝑖,𝑡 ) 𝜌𝑞 ( 𝑟𝑖 ( 𝑡 ) − ̂ 𝑟 ( 𝑖 𝑞 )( 𝑡 ) ) 𝜌𝑞 ( 𝑒 ) =  𝑒 ( 𝑞 − 𝟙{ 𝑒<  0}) (3)<br><!-- End of picture text -->

which yields asymmetric intervals<sup>[</sup> _𝑟_<sup>_̂_(0</sup> _𝑖_<sup>_._1)</sup> ( _𝑡_ ) _,̂ 𝑟_<sup>(0</sup> _𝑖_<sup>_._9)</sup> ( _𝑡_ )<sup>]</sup> that expand naturally under regime variability. To guarantee finite-sample coverage under temporal shift, we conformalize these quantiles on the validation tail via residual envelopes computed chronologically; the resulting conformalized quantile regression (CQR) intervals respect time order and are then applied unchanged on test. For classification risk, we monitor calibration with the Brier score and expected calibration error (ECE) computed in sliding time bins and by distance-to-failure strata; reliability diagrams are produced per site to detect drift. When mild miscalibration persists, temperature or isotonic scaling is refit using only the validation period immediately preceding deployment, which empirically stabilizes ECE without degrading discrimination. 

Uncertainty enters decision-making in two complementary ways. First, the MILP cost shaping uses a convex risk transform of _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) parameterized by the observed ECE so that noisier probabilities incur a slight penalty unless corroborated by multiple consecutive high-risk readings; this implements a principled form of temporal smoothing tied to measurement confidence. Second, robust schedule candidates are built against the RUL lower quantile _̂𝑟_<sup>(0</sup> _𝑖_<sup>_._1)</sup> ( _𝑡_ ) when the interval width exceeds a data-driven threshold, effectively narrowing maintenance windows for assets with volatile health estimates. Sensitivity analyses confirm that these simple, transparent hedges recover a significant portion of the value of more intricate stochastic models while preserving solver tractability and auditability. All predictive models, calibrators, and uncertainty post-processors are frozen after validation and versioned together with their SHAP explainers, ensuring that downstream schedules can be traced to the exact forecast distributions that informed them. 

#### **5. Optimization model for maintenance scheduling** 

This section formulates the time-indexed mixed-integer linear program that transforms predictive signals into executable maintenance plans. The model captures resource capacities, admissible operating 

6 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 4** 

MILP parameter guidance for practical Implementation. 

|Parameter|Description|Practical Guidance|
|---|---|---|
|_𝛼𝑖_|Risk scaling factor|Set to downtime cost per period for asset _𝑖_|
|_𝜅𝑖,𝑡_|Risk-shaping factor|Increase (1.2-1.5) for physical degradation; decrease (1.0–1.2) for transients|
|_𝜓_(⋅)|Convex risk transform|Linear: _𝜓_(_𝑝_) =_𝑝_; Quadratic: _𝜓_(_𝑝_) =_𝑝_<sup>2</sup>; Piecewise-linear for nonlinearity|
|_𝑞_|RUL quantile|_𝑞_= 0_._25 for safety-critical assets; _𝑞_= 0_._4 for cost-sensitive operations|
|_𝜋𝑖_|Tardiness penalty|Set to 1.5-2.0 times normal downtime cost|
|_𝜆_|CVaR weight|0.1-0.3 for moderate risk aversion; 0.4-0.6 for high risk aversion|
|_𝛽_|CVaR level|0.9-0.95 for most applications|



windows, non-overlap on each asset, and risk-aware due dates derived from remaining useful life (RUL) forecasts. The formulation is intentionally transparent so that each term in the objective and constraints can be traced back to a measurable quantity in the predictive layer or to an operational policy. 

#### _5.1. Notation and assumptions_ 

The planning horizon is discretized into periods _𝑡_ ∈  = {1 _,_ … _, 𝑇_ } of equal length Δ (e.g., 15 minutes). Assets are indexed by _𝑖_ ∈ , maintenance modes by _𝑚_ ∈  _𝑖_ (e.g., inspection, lubrication, bearing replacement), and teams by _𝑘_ ∈  with unit capacity per period. For each ( _𝑖, 𝑚_ ), _𝑑𝑖,𝑚_ ∈ ℤ+ denotes the processing time in periods, _̄𝑐𝑖,𝑚_ the fixed execution cost (labor, parts), and _𝑟𝑖,𝑚_ ∈{1 _,_ 2 _,_ …} the number of teams required concurrently (typically 1). Availability of asset _𝑖_ for maintenance in period _𝑡_ is given by _𝐴𝑖,𝑡_ ∈{0 _,_ 1}, which encodes production blackouts, safety lockout/tagout constraints, and site-specific restrictions (e.g., generator change- over intervals in Lebanese plants). The time-indexed downtime cost for taking _𝑖_ out of service in _𝑡_ is _𝑐𝑖,𝑡_<sup>down</sup> ≥ 0 (lost throughput, quality risk), while the calibrated short-horizon failure probability supplied by the predictive layer is _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) ∈[0 _,_ 1] for a look-ahead _𝜏_ matched to typical reaction times. An asset-level due date _𝐷𝑖_ ∈{1 _,_ … _, 𝑇_ } is derived from the RUL forecast by setting 



<!-- Start of picture text -->
𝐷𝑖 ∶= min { 𝑇, 𝑡 0 + ⌊ 𝑟 ̂ ( 𝑖 𝑞 )( 𝑡 0)⌋} (4)<br><!-- End of picture text -->

where _𝑡_ 0 is the plan start and _̂𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_)isacalibratedlowerquantile(e.g.,</sup> _𝑞_ = 0 _._ 25) to hedge against optimistic RUL. Tardiness beyond _𝐷𝑖_ is penalized at rate _𝜋𝑖_ ≥ 0. To reflect that not all risk is equal, the explainability layer supplies a multiplicative risk-shaping factor _𝜅𝑖,𝑡_ ∈[1 _,_ 1 + _𝜂_ ] computed from SHAP summaries, which is higher when the dominant drivers correspond to physically causal degradation (e.g., growing bandlimited vibration energy at defect frequencies) and lower when risk is dominated by exogenous transients (e.g., grid perturbations). The convex transform _𝜓_ ∶[0 _,_ 1] → ℝ+ maps probabilities to marginal risk weights; in practice _𝜓_ is implemented as a piecewise-linear function fitted on validation (Section 4). All parameters are known at planning time and are updated in a rolling horizon as new telemetry arrives. 

Decision variables are time-indexed. The binary variable _𝑥𝑖,𝑚,𝑡_ equals 1 if maintenance mode _𝑚_ on asset _𝑖 starts_ at the beginning of period _𝑡_ ; _𝑧𝑖,𝑡_ equals 1 if asset _𝑖_ is under maintenance during period _𝑡_ ; and _𝑎𝑖,𝑚,𝑘,𝑡_ equals 1 if team _𝑘_ works on job ( _𝑖, 𝑚_ ) in period _𝑡_ . A binary _𝑣𝑖_ flags whether any maintenance is scheduled on asset _𝑖_ in the horizon. The nonnegative variable _𝑇𝑖_ captures tardiness beyond _𝐷𝑖_ . If required, a continuous completion-time variable _𝐶𝑖_ records the end of the scheduled job to linearize lateness. Unless stated otherwise, at most one maintenance mode is executed per asset within the horizon; multiple interventions can be accommodated with minor extensions by indexing jobs. 

#### _5.2. MILP formulation_ 

The objective minimizes expected unplanned downtime from deferral, planned downtime during execution, fixed maintenance costs, and 

#### tardiness penalties: 



<!-- Start of picture text -->
min ∑ ∑ 𝛼𝑖 𝜅𝑖,𝑡 𝜓 ( 𝑝 ̂ 𝑖 ( 𝑡, 𝜏 ) ) (1 − 𝑧𝑖,𝑡 ) + ∑ ∑ 𝑐𝑖,𝑡 down 𝑧𝑖,𝑡 + ∑ ∑ ∑ 𝑐𝑖,𝑚 𝑥𝑖,𝑚,𝑡 + ∑ 𝜋𝑖 𝑇𝑖 .<br>𝑖 ∈ 𝑡 ∈ 𝑖 ∈ 𝑡 ∈ 𝑖 ∈ 𝑚 ∈ 𝑖 𝑡 ∈ 𝑖 ∈<br>⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ ⏟⏞⏟⏞⏟<br>risk-weighted deferral penalty planned downtime execution cost tardiness<br>(5)<br><!-- End of picture text -->

To prevent over-accumulation of risk across time, we introduce temporal discounting in the risk term. The deferral penalty is modified as _𝛼𝑖 𝜅𝑖,𝑡 𝜓_ ( _̂𝑝𝑖_ ( _𝑡, 𝜏_ )) (1 − _𝑧𝑖,𝑡_ ) ⋅ _𝛾_<sup>_𝑡_−</sup><sup>_𝑡_0</sup> , where _𝛾_ ∈[0 _._ 95 _,_ 0 _._ 99] is a discount factor that reduces the weight of distant risk predictions. This design choice ensures that recent risk signals have greater influence on scheduling decisions while still accounting for future risks. Table 4 shows the MILP parameter guidance for the practical implementation purposes. 

Here _𝛼𝑖_ scales risk terms to the unit of downtime cost for asset _𝑖_ ; (1 − _𝑧𝑖,𝑡_ ) ensures that high risk is penalized only while the asset is _not_ in maintenance. The constraints enforce feasibility. Linking between starts and occupancy is achieved by standard time-indexed convolution: 

_𝑧𝑖,𝑡_ ≥ _𝑥𝑖,𝑚,𝑢_ ∀ _𝑖_ ∈  _,_ ∀ _𝑚_ ∈  _𝑖,_ ∀ _𝑢_ ∈  _,_ ∀ _𝑡_ ∈{ _𝑢,_ … _,_ min( _𝑢_ + _𝑑𝑖,𝑚_ −1 _, 𝑇_ )} 



<!-- Start of picture text -->
(6)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑧𝑖,𝑡 ≤ ∑ ∑ 𝑡 𝑥𝑖,𝑚,𝑢 ∀ 𝑖 ∈  , ∀ 𝑡 ∈  (7)<br>𝑚 ∈ 𝑖 𝑢 =max(1 , 𝑡 − 𝑑𝑖,𝑚 +1)<br><!-- End of picture text -->

so that _𝑧𝑖,𝑡_ equals 1 if and only if some maintenance that started earlier is still in process. Non-overlap on the same asset is naturally enforced by (5). Starts are allowed only within admissible windows and when the full job fits within the horizon: 



<!-- Start of picture text -->
𝑥𝑖,𝑚,𝑡 ≤ 𝐴𝑖,𝑡 ′ ∀ 𝑖, 𝑚, ∀ 𝑡, ∀ 𝑡 ′ ∈{ 𝑡,  …  ,  min( 𝑡 +  𝑑𝑖,𝑚 −1 , 𝑇 )} (8)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖,𝑚,𝑡 = 0 ∀ 𝑖, 𝑚, ∀ 𝑡> 𝑇 − 𝑑𝑖,𝑚 + 1 (9)<br><!-- End of picture text -->

Team capacity and assignment coherence are modeled as: 



<!-- Start of picture text -->
∑ ∑ 𝑎𝑖,𝑚,𝑘,𝑡 ≤ 1∀ 𝑘 ∈  , ∀ 𝑡 ∈  (10)<br>𝑖 ∈ 𝑚 ∈ 𝑖<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ 𝑎𝑖,𝑚,𝑘,𝑡 =  𝑟𝑖,𝑚 ∑ 𝑡 𝑥𝑖,𝑚,𝑢 ∀ 𝑖, 𝑚, ∀ 𝑡 ∈  (11)<br>𝑘 ∈ 𝑢 =max(1 , 𝑡 − 𝑑𝑖,𝑚 +1)<br><!-- End of picture text -->



<!-- Start of picture text -->
ensuring each active job is fully staffed and no team is double-booked.<br>If at most one intervention per asset is allowed, we set:<br>∑ ∑ 𝑥𝑖,𝑚,𝑡 ≤ 1 𝑣𝑖 = ∑ ∑ 𝑥𝑖,𝑚,𝑡 ∀ 𝑖 ∈  . (12)<br>𝑚 ∈ 𝑖 𝑡 ∈ 𝑚 ∈ 𝑖 𝑡 ∈<br><!-- End of picture text -->

Completion time and tardiness are linearized as 



<!-- Start of picture text -->
𝐶𝑖 ≥ ∑ ∑( 𝑡 +  𝑑𝑖,𝑚 −1)  𝑥𝑖,𝑚,𝑡 (13)<br>𝑚 ∈ 𝑖 𝑡 ∈<br>𝐶𝑖 ≤ ∑ ∑( 𝑡 +  𝑑𝑖,𝑚 −1)  𝑥𝑖,𝑚,𝑡 +  𝑀𝑖 (1 − 𝑣𝑖 ) (14)<br>𝑚 ∈ 𝑖 𝑡 ∈<br>𝑇𝑖 ≥ 𝐶𝑖 − 𝐷𝑖, 𝑇𝑖 ≥ 0 ∀ 𝑖 ∈  (15)<br><!-- End of picture text -->

with _𝑀𝑖_ a tight upper bound such as _𝑀𝑖_ = _𝑇_ . When setup or cleaning buffers are required around an intervention, they are absorbed by inflating _𝑑𝑖,𝑚_ or, if asymmetry matters, by adding binary cooldown variables with standard linearizations; these do not alter the basic structure above. 

7 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 5** 

MILP scalability analysis. 

|Assets|Teams|Horizon|Variables|Solve Time (s)|
|---|---|---|---|---|
|50|5|1 week|12,450|12|
|50|5|2 weeks|24,900|28|
|100|10|1 week|49,800|45|
|100|10|2 weeks|99,600|112|
|150|15|1 week|112,050|89|
|150|15|2 weeks|224,100|252|



#### _5.3. Coupling predictions to optimization_ 

The coupling is explicit and auditable at three interfaces. First, RUL forecasts determine service deadlines. The due date _𝐷𝑖_ reflects a conservative RUL quantile consistent with the plant’s risk appetite; sensitivity studies may substitute data-driven, asset-specific guard bands [ _𝐷𝑖_<sup>−</sup><sup>_, 𝐷_</sup> _𝑖_<sup>+]</sup> derived from conformalized intervals, with lateness measured relative to _𝐷𝑖_<sup>−forsafety-criticalassets.Second,failureprobabilitiesshapethe</sup> marginal penalty for deferral. The weight _𝛼𝑖 𝜅𝑖,𝑡 𝜓_ ( _̂𝑝𝑖_ ( _𝑡, 𝜏_ )) in (5) is computed upstream and passed as a parameter to the MILP, making the risk term linear in (1 − _𝑧𝑖,𝑡_ ) and thus solver-friendly. The convex map _𝜓_ amplifies high probabilities and discounts low ones to reflect the nonlinear economics of unexpected breakdowns; its piecewise-linear approximation preserves optimality in MILP. The SHAP-based multiplier _𝜅𝑖,𝑡_ increases the penalty when leading drivers correspond to physical degradation modes, such as rising spectral kurtosis or energy around characteristic bearing frequencies, and decreases it when risk is dominated by exogenous or reversible factors, ensuring that the optimizer prioritizes mechanical wear over nuisance transients. Third, probability calibration enters through the scale of _𝜓_ : when expected calibration error rises, the slope of _𝜓_ near the operating region is modestly reduced, effectively tempering overly aggressive scheduling responses to noisy signals; this link maintains coherence between predictive confidence and operational aggressiveness. 

The same interfaces support explainability of the schedule ex post. Each scheduled intervention is annotated with ( _̂𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_)</sup><sup>_,̂ 𝑝𝑖, 𝜅𝑖,𝑡_)atthede-</sup> cision point and with the top-ranked SHAP drivers that lifted the risk penalty above the triggering level, enabling engineers to audit why a particular slot was selected or why a deferral was deemed acceptable. 

#### _5.4. Solution strategy and complexity_ 

The time-indexed MILP is NP-hard by reduction from parallel machine scheduling with release dates, yet it scales effectively in practice under three measures. First, presolve removes dominated starts: any ( _𝑖, 𝑚, 𝑡_ ) that violates (8)-(9) or yields _𝐷𝑖_ −( _𝑡_ + _𝑑𝑖,𝑚_ −1) _<_ − _̄𝐻_ for a userdefined slack _̄𝐻_ is fixed to zero. Second, we warm-start with a greedy constructive heuristic consistent with the objective: assets are sorted by a hazard index _𝐻𝑖_ =<sup>∑</sup> _𝑡_<sup>_𝜅_</sup> _𝑖,𝑡_<sup>_𝜓_(</sup><sup>_̂𝑝_</sup> _𝑖_<sup>(</sup><sup>_𝑡, 𝜏_))normalizedbyanearliest-feasible</sup> duration, and jobs are placed by earliest-risky-deadline with resourcefeasible insertion; the resulting { _𝑥, 𝑧, 𝑎_ } initialize the solver within milliseconds. Third, we add valid inequalities that tighten the LP relaxation without obscuring interpretability. Cover cuts derived from (10) bound simultaneous high-demand jobs on scarce teams; clique cuts on { _𝑥𝑖,𝑚,𝑡_ } _𝑡_ enforce mutual exclusivity of overlapping starts; and knapsack inequalities bound<sup>∑</sup> _𝑡_<sup>_𝑧_</sup> _𝑖,𝑡_<sup>forlongjobsonassetswithsparsewindows.Branch-</sup> ing priorities favor high-risk _𝑥_ -variables to accelerate convergence. The model is solved with a commercial MILP solver (e.g., Gurobi/CPLEX) using default cuts and concurrent root algorithms; time limits are set per rolling-horizon slice, after which the best incumbent is executed. 

In the Lebanese deployments, horizons of one to two weeks at Δ ∈ {10 _,_ 15} minutes, || between 40 and 150, and || between 5 and 25 solve to near-optimality in seconds to a few minutes on commodity hardware, which is compatible with hourly replanning (Table 5). 

Rolling-horizon control closes the loop. At each epoch _𝑡_ 0, predictions and { _𝜅𝑖,𝑡_ } are refreshed, _𝐷𝑖_ is re-evaluated from the updated RUL, and the MILP is re-solved on [ _𝑡_ 0 _, 𝑡_ 0 + _𝑇_ look] with continuity constraints that respect tasks already started. This policy adapts naturally to evolving risk while preserving stability; optional move limits cap the number of rescheduled jobs per epoch to respect shop-floor constraints. 

#### _5.5. Robust and scenario-Based extensions_ 

Uncertainty can be represented explicitly without sacrificing tractability. A scenario-based extension augments the model with a finite set  of joint scenarios for ( _̂𝑝𝑖,̂ 𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_))sampledfromconformalized</sup> intervals or Bayesian posteriors. The schedule ( _𝑥, 𝑧, 𝑎_ ) is here-and-now, while losses are evaluated per scenario. Let _𝐿_<sup>(</sup><sup>_𝑠_)</sup> ( _𝑥, 𝑧_ ) denote the objective value of (5) under scenario _𝑠_ with parameters { _̂𝑝_<sup>(</sup> _𝑖_<sup>_𝑠_)</sup><sup>_, 𝐷_</sup> _𝑖_<sup>(</sup><sup>_𝑠_)}.</sup> 

We define auxiliary variables: _𝜁_ represents the Value-at-Risk (VaR) at level _𝛽_ , and _𝜉𝑠_ represents the shortfall for scenario _𝑠_ (the amount by which the scenario loss exceeds VaR). A CVaR-regularized objective 



<!-- Start of picture text -->
1 1<br>𝑥,𝑧,𝑎,𝜁,𝜉 min || 𝑠 ∑∈ 𝐿 ( 𝑠 ) ( 𝑥, 𝑧 ) +  𝜆 ( 𝜁 + (1 − 𝛽 )|| 𝑠 ∑∈ 𝜉𝑠 ) , (16)<br>s.t. 𝜉𝑠 ≥ 𝐿 ( 𝑠 ) ( 𝑥, 𝑧 ) − 𝜁, 𝜉𝑠 ≥ 0 , ∀ 𝑠 ∈  ,<br><!-- End of picture text -->

controls tail risk at level _𝛽_ with weight _𝜆_ . Alternatively, a robust deadline may require _𝐶𝑖_ ≤ _𝐷𝑖_<sup>(</sup><sup>_𝑠_)forall</sup><sup>_𝑠_inaconservativesetorforatleastafrac-</sup> tion _𝛾_ of scenarios via big- _𝑀_ activation, approximating a chance constraint. Multi-criteria trade-offs between expected cost, expected downtime, and risk are efficiently explored by _𝜖_ -constraint or lexicographic optimization: for example, minimize expected cost subject to expected downtime ≤ _𝜖_ , then tighten _𝜖_ iteratively to trace the Pareto frontier. These variants preserve linearity, remain explainable, since all risk parameters are externally visible, and integrate seamlessly with the rollinghorizon policy. 

The resulting optimization layer accepts calibrated predictive signals with documented provenance, encodes operational constraints faithfully, and returns schedules whose economic and safety implications are explicit in the model coefficients. This transparency allows maintenance planners to justify automated decisions, to tune risk appetite via ( _𝑞, 𝜓, 𝜆, 𝛽_ ), and to incorporate domain feedback without redesigning the pipeline. 

#### **6. End-to-end pipeline** 

The end-to-end system implements a tightly coupled yet modular pipeline that converts raw telemetry and maintenance records into executable, auditable schedules. Data flow begins with ingestion from the plant historian and CMMS, passes through causal preprocessing and temporal feature engineering, and enters the predictive layer where remaining useful life and short-horizon failure risks are inferred and calibrated. An explainability layer computes SHAP-based attributions and derives a risk-shaping coefficient that distinguishes physically causal degradation from exogenous transients. These signals are compiled into linear parameters for a time-indexed MILP, which returns a resourcefeasible schedule aligned with production and safety windows. Execution metadata and realized outcomes are fed back to the data lake and model registry, closing a rolling-horizon loop that maintains coherence between inference, optimization, and plant operations. 

#### _6.1. System architecture_ 

The architecture is organized as cooperating services with clear contracts to ensure traceability and operational resilience (Fig. 2). A data ingestion service subscribes to historian tags and CMMS events, performs time alignment under a unified clock, and stages raw streams in a write-once store with cryptographic checksums. A feature service 

8 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

materializes strictly causal windows and temporal descriptors described in Section 3, versioning transformations alongside their training-time statistics to preclude leakage. The inference service hosts the gradientboosted RUL regressor and the calibrated failure-risk classifier; it exposes batch and streaming endpoints that return _̂𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_)(</sup><sup>_𝑡_)forselectedquan-</sup> tiles and _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) over operational look-ahead windows. A calibration component applies the frozen monotone mapping determined on validation and reports reliability diagnostics. The explainability service computes TreeSHAP values for both tasks, aggregates them in a timeaware manner, and emits an interpretable risk-shaping factor _𝜅𝑖,𝑡_ together with ranked drivers and compact artifacts suitable for human audit. The optimization service constructs the linear objective weights _𝛼𝑖 𝜅𝑖,𝑡 𝜓_ ( _̂𝑝𝑖_ ( _𝑡, 𝜏_ )), evaluates conservative due dates from RUL quantiles, assembles the MILP described in Section 5, and solves it under a time budget with warm starts and valid inequalities. An orchestration layer governs rolling-horizon operation, enforces continuity constraints with respect to tasks already started, and publishes the committed portion of the schedule to the CMMS via transactional APIs while annotating work orders with the top explanatory factors. A monitoring service tracks data drift, calibration error, solver performance, and schedule adherence; when thresholds are exceeded, it triggers an offline retraining or recalibration workflow, ensuring that the online loop remains stable. All models, calibrators, explainers, and MILP configurations are registered as immutable artifacts with provenance, enabling any schedule to be traced back to the exact forecast distributions and attribution summaries that informed it. 

#### _6.2. Algorithmic pseudocode_ 

The pseudocode makes explicit the separation of concerns between learning, explainability, and optimization while preserving a single source of truth for the parameters that bind them (Algorithm 1). All transformations are causal with respect to the decision time _𝑡_ 0, calibration is applied exactly as validated, and the conversion from probabilistic risk to linear MILP weights is performed upstream to maintain solver transparency. The rolling-horizon workflow accepts new information without destabilizing the shop floor by committing only a protected slice of the plan and by enforcing continuity constraints and move limits. Together these design choices yield schedules that are responsive to emerging degradation, economically consistent with plant costs, and defensible under engineering and managerial scrutiny. 

#### **7. Experimental setup** 

This section establishes the evaluation protocol for the integrated learning-optimization pipeline, specifies the competing baselines, defines the performance metrics at both the predictive and scheduling layers, and documents implementation particulars needed for faithful reproduction. All experiments adhere to the chronology and causal constraints stated in Sections 3-6. Models are trained only on information available up to the decision time, probabilities are calibrated on a heldout temporal validation tail and then frozen, and the optimization layer is exercised in a rolling-horizon replay in which each epoch commits a short protected slice of the plan before the next re-optimization. 

#### _7.1. Baselines_ 

Three reference policies are used to contextualize the value of the proposed framework. The reactive baseline represents run-to-failure operation: no preventive work is scheduled, and a corrective task is triggered only after a verified failure, incurring full unplanned downtime equal to the repair duration plus access and restart overheads. This baseline uses the same resource model, windows, and task durations as all other policies to ensure that differences arise solely from decision timing. The time-based preventive baseline implements fixed-interval maintenance derived from manufacturer recommendations and local CMMS 

practices. For each asset-mode pair, a periodicity is selected on the validation horizon to minimize the same economic composite used in our objective while respecting windows and capacities; the resulting schedule is applied rollingly without consuming predictive risk signals. 

**Algorithm 1** Rolling-horizon Maintenance Scheduling Workflow. 

- **Require:** Historical data hist, current time _𝑡_ 0, horizon _𝑇_ look, move limit _𝑀_ max 

- **Ensure:** Committed schedule for [ _𝑡_ 0 _, 𝑡_ 0 + _𝑇_ commit] 1: Initialize model registry  with trained predictors, calibrators, explainers 

- 2: Load current schedule state _𝑆_ current from CMMS 3: _𝑡_ start ← _𝑡_ 0 4: **while** _𝑡_ start ≤ _𝑡_ 0 + _𝑇_ look **do** 5: Ingest new telemetry new from historian 6: Preprocess and engineer features **𝐳** _𝑖,𝑡_ for _𝑡_ ∈[ _𝑡_ start _, 𝑡_ start + _𝑇_ look] 7: Predict RUL quantiles _̂𝑟_<sup>(</sup> _𝑖_<sup>_𝑞_)(</sup><sup>_𝑡_)andfailureprobabilities</sup><sup>_̂𝑝𝑖_(</sup><sup>_𝑡, 𝜏_)</sup> 8: Compute SHAP attributions **_𝝓_** _𝑖,𝑡_ and risk-shaping factors _𝜅𝑖,𝑡_ 9: Derive MILP parameters: _𝐷𝑖_ , _𝛼𝑖 𝜅𝑖,𝑡 𝜓_ ( _̂𝑝𝑖_ ( _𝑡, 𝜏_ )), _𝑐𝑖,𝑡_<sup>down</sup> 

- 10: Set continuity constraints for tasks in progress 11: Solve MILP with warm-start and time limit _𝑇_ solve 12: Extract new schedule _𝑆_ new 13: Compute changes Δ _𝑆_ = _𝑆_ new ⧵ _𝑆_ current 14: **if** |Δ _𝑆_ | _> 𝑀_ max **then** 15: Prune Δ _𝑆_ to _𝑀_ max highest-priority changes 16: **end if** 17: Commit schedule for [ _𝑡_ start _, 𝑡_ start + _𝑇_ commit] to CMMS 18: Annotate work orders with top SHAP drivers 19: _𝑆_ current ← _𝑆_ new 20: _𝑡_ start ← _𝑡_ start + _𝑇_ commit 21: Monitor execution outcomes and update hist 22: **end while** 

The heuristic scheduler constitutes a planning-aware but optimization-light alternative. At each epoch it computes a priority index for every asset combining a conservative RUL quantile and the current calibrated short-horizon risk over the admissible window, then assigns jobs by earliest due date with first-fit insertion subject to team capacities and non-overlap. The heuristic incorporates the same availability calendars and crews as the MILP, re-plans at the same epochs, and honors continuity of started tasks; it is therefore a strong, transparent comparator that exploits the same predictions while eschewing full mathematical programming. The priority index is computed as _𝐻𝑖_ = _𝜅𝑖,𝑡_ ⋅ _𝜓_ ( _̂𝑝𝑖_ ( _𝑡, 𝜏_ ))∕ _̂𝑟_<sup>(0</sup> _𝑖_<sup>_._25)</sup> ( _𝑡_ ), balancing immediate risk against remaining life. 

Additionally, we include two data-driven baselines: (1) A thresholdbased scheduler that triggers maintenance when _̂𝑝𝑖_ ( _𝑡, 𝜏_ ) exceeds a threshold optimized on validation data, with tasks scheduled by earliest deadline; (2) A deep learning prognostic baseline using LSTM networks for RUL prediction, with the same MILP optimization layer to isolate the value of gradient boosting. 

#### _7.2. Evaluation metrics_ 

Predictive accuracy is reported separately for remaining useful life and for short-horizon failure risk. Let _̂𝑟𝑖_ ( _𝑡_ ) denote the point forecast of RUL and _𝑟𝑖_ ( _𝑡_ ) the realized value for uncensored segments. Mean absolute error and root-mean-squared error are computed in a strictly timeordered fashion as: 



<!-- Start of picture text -->
MAE = 𝑁 1 ∑ ||| ̂ 𝑟𝑖 ( 𝑡 ) − 𝑟𝑖 ( 𝑡 ) |||RMSE = 𝑁 1 ∑ ( ̂𝑟𝑖 ( 𝑡 ) − 𝑟𝑖 ( 𝑡 ))2 (17)<br>( 𝑖,𝑡 )∈ √ ( 𝑖,𝑡 )∈<br><!-- End of picture text -->

with  the evaluation panel of uncensored points. To reflect operational value, lead-time sensitivity is reported by conditioning these errors on distance to failure. For classification of failure within a look-ahead _𝜏_ , 

9 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 



**Fig. 2.** End-to-end pipeline architecture showing data flow from telemetry ingestion to schedule execution and feedback. 

10 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

discrimination is measured by AUROC and AUPRC on the test tail, while calibration is quantified by the Brier score 



<!-- Start of picture text -->
Brier = 𝑀 1 ∑ ( ̂𝑝𝑖 ( 𝑡, 𝜏 ) − 𝑦 ( 𝑖,𝑡𝜏 ))2 (18)<br>( 𝑖,𝑡 )∈<br><!-- End of picture text -->

and by the expected calibration error computed on reliability bins that preserve time order. Reliability diagrams and Spiegelhalter tests are used diagnostically but not as selection criteria after calibration has been frozen. 

Scheduling performance metrics align with the optimization objective and plant operations KPIs: 

- **Total unplanned downtime** : Sum over assets and periods in which a failure occurs before the scheduled completion of the next intervention, using ground-truth repair durations from CMMS for the Lebanese corpus and truth-table failure times from benchmarks. 

- **Total maintenance cost** : Aggregates fixed execution costs (labor, parts) and planned downtime costs (lost throughput, quality risk) incurred while assets are under maintenance. 

- **Tardiness** : Deadline violations relative to service due dates derived from conservative RUL quantiles, reported alongside a deadlinecompliance rate (share of jobs completed at or before due). 

- **Resource utilization** : Per team fraction of schedulable time devoted to active tasks, averaged over the horizon, with variance to reveal load balancing. 

- **Makespan** : Last completion time of accepted jobs on each rolling slice, providing a proxy for work-in-process. 

Computational efficiency is reported as wall-clock solve time per epoch and as the final optimality gap returned by the MILP solver at the time limit. Because the system operates in a rolling fashion, plan stability is also tracked by the fraction of jobs that change start times between successive epochs; small move-limit parameters can be used to equalize stability across methods when required by site policy. 

#### _7.3. Implementation details_ 

All data processing, model training, and replay experiments are executed under a common software and hardware envelope to avoid confounds (Table 6). Feature engineering and data handling follow the causal procedures in Section 3 and are implemented in a vectorized stack with reproducible random seeds and deterministic histogrambased learners. Gradient boosting for RUL regression and failure classification uses a modern implementation with shrinkage, depth constraints, column and row subsampling, and early stopping monitored on a temporally blocked validation set. Hyperparameters are selected by Bayesian optimization over bounded ranges covering the number of trees, learning rate, maximum depth, minimum child weight, subsampling rates, and 𝓁1∕𝓁2 regularization. Search runs enforce time-ordered _𝐾_ -folds where each fold holds out terminal segments by asset to preserve forward-in-time generalization; the final models are refit on the union of training and validation periods with the chosen settings, after which probability calibration is applied using Platt scaling or isotonic regression according to validation reliability curves. Explainability artifacts are computed with TreeSHAP on the frozen models; local attributions are smoothed over short windows to reduce flicker, and global summaries are stored with model version identifiers. The optimization layer is instantiated exactly as in Section 5, with risk weights and due dates pre-computed upstream to keep the MILP linear. A commercial solver with default cut generation and concurrent root algorithms is used; a warm start derived from earliest-risky-deadline insertion is provided at each epoch, and a modest time limit per rolling slice is enforced. All policies, including baselines, re-plan at identical epochs and commit the same near-term slice to ensure comparability. 

**Table 6** 

Implementation environment and parameters. 

|Component|Specification|
|---|---|
|Hardware|Intel Xeon Gold 6248R @ 3.0GHz, 128GB RAM|
|Operating System|Ubuntu 20.04 LTS|
|Python Version|3.8.10|
|ML Libraries|XGBoost 1.5.0, LightGBM 3.3.2, scikit-learn 1.0.2|
|Optimization Solver|Gurobi 9.5.2|
|Solver Parameters|Time limit = 300s, MIPGap = 0.01%, Threads = 8|
|Random Seeds|Fixed for all experiments (seed=42)|



|**Table** **7**<br>Calibration metrics on|the test horizon.|
|---|---|
|Dataset|Brier score<br> ECE|
|C–MAPSS|0.076<br> 0.018|
|IMS Bearings|0.071<br> 0.016|
|SECOM/Process|0.112<br> 0.031|
|Lebanese Industrial|0.095<br> 0.027|



#### **8. Results** 

This section reports predictive accuracy and calibration of the forecasting layer, interpretability outcomes from the explainability layer, and end-to-end scheduling performance in rolling-horizon replay on public benchmarks and the Lebanese industrial corpus. Unless otherwise stated, all metrics are computed on the chronologically held-out test horizon with models, calibrators, and MILP parameters frozen after validation. Confidence intervals are obtained by paired, time-aligned bootstrap on per-asset trajectories, and statistical significance for paired comparisons is assessed by Wilcoxon signed-rank tests on per-asset deltas. All results are shown in Table 8. 

#### _8.1. Predictive performance_ 

Across public corpora and Lebanese sites, the forecasting layer achieves high discrimination for short-horizon failure risk and competitive error for remaining useful life (RUL) estimation under strict time ordering. The calibrated classifier maintains reliable probabilities over the operating range relevant to scheduling, which is critical because the optimization layer consumes continuous risks rather than thresholded alerts. Table 9 summarizes RUL errors (MAE/RMSE) and failurerisk discrimination (AUROC/AUPRC) per dataset, stratified by distanceto-failure to illuminate lead-time sensitivity. Calibration behavior is reported in Table 7 via Brier score and expected calibration error (ECE) by time bins and by distance-to-failure strata. Reliability diagrams in Fig. 3 confirm near-identity mapping post-calibration, while precisionrecall curves in Fig. 4 show consistent gains over baselines in the lowprevalence regime typical of industrial failures. 

#### _8.2. Explainability findings_ 

Global and local SHAP analyses render the forecasting layer auditable and actionable for planners and reliability engineers. Aggregated attributions consistently highlight physically meaningful drivers across datasets: for rotating machinery, band-limited vibration energies near defect characteristic frequencies, spectral kurtosis, and envelope peaks rise in prominence as assets approach end-of-life; for process sensors, combinations of temperature ratios, pressure differentials, and flow residuals dominate risk under stressed regimes. The global beeswarm plots in Fig. 5 rank feature influence and expose nonlinearities and interactions that are otherwise opaque to raw feature importance. Dependence plots in Fig. 1 show monotonic relationships with plausible saturation effects for key vibration and thermal features. Local case studies in Fig. 7 explain concrete recommendations by decomposing a single forecast into additive contributions, while temporal attribution 

11 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 8** 

Scheduling KPIs on the held-out test horizon (rolling replay) with absolute baseline values. 

|Dataset|Baseline|Unplanned downtime (hrs)|Maintenance cost ($)|Our Method (hrs)|Our Method ($)|Deadline compliance|Makespan|Solve time/epoch|
|---|---|---|---|---|---|---|---|---|
||Reactive|536.2|1,318,000|418.0|1,120,000|93.8%|51.2 h|26.4 s|
|Lebanese|Preventive|489.7|1,285,000|418.0|1,120,000|93.8%|51.2 h|26.4 s|
||Heuristic|452.3|1,221,000|418.0|1,120,000|93.8%|51.2 h|26.4 s|
||Reactive|407.8|791,000|310.0|680,000|95.2%|46.3 h|14.8 s|
|C-MAPSS|Preventive|382.4|765,000|310.0|680,000|95.2%|46.3 h|14.8 s|
||Heuristic|336.5|724,000|310.0|680,000|95.2%|46.3 h|14.8 s|
||Reactive|164.8|331,000|122.0|275,000|96.4%|38.7 h|9.6 s|
|IMS Bearings|Preventive|152.3|318,000|122.0|275,000|96.4%|38.7 h|9.6 s|
||Heuristic|131.7|298,000|122.0|275,000|96.4%|38.7 h|9.6 s|
||Reactive|239.2|593,000|208.0|540,000|90.7%|44.1 h|17.3 s|
|SECOM|Preventive|226.5|578,000|208.0|540,000|90.7%|44.1 h|17.3 s|
||Heuristic|215.8|562,000|208.0|540,000|90.7%|44.1 h|17.3 s|



|**Table** **9**|||||||
|---|---|---|---|---|---|---|
|Predictive performan|ce on the he|ld-out test ho|rizon.||||
|Dataset|RUL MAE|RUL RMSE|AUROC|AUPRC|AUROC (DtF ≤ window)|AUPRC (DtF ≤ window)|
|C–MAPSS|12.4|20.1|0.94|0.57|0.97|0.75|
|IMS Bearings|8.1|12.6|0.96|0.63|0.98|0.80|
|SECOM/Process|—|—|0.89|0.38|0.92|0.52|
|Lebanese Industrial|9.8|15.2|0.92|0.41|0.95|0.60|





**Fig. 3.** Reliability diagrams on the held-out test horizon for the short-horizon failure classifier. 



**Fig. 5.** Global SHAP beeswarm plots per dataset. 



**Fig. 4.** Precision-recall curves on the test horizon. 

traces in Fig. 6 reveal the progression of dominant drivers in the days preceding an intervention. Stability analysis in Table 10 quantifies crosssite robustness by reporting rank correlations and Jaccard overlaps of the top- _𝑘_ features across Lebanese plants and public corpora, together with bootstrap confidence bands; high stability on mechanically causal features supports safe operationalization. 



**Fig. 6.** Time-aligned SHAP attribution traces relative to failure onset for the top drivers on rotating equipment. 

#### _8.3. Scheduling performance_ 

The end-to-end pipeline translates calibrated risks and RUL deadlines into resource-feasible schedules that materially reduce unplanned losses. In rolling replay, the proposed framework achieves a median 

12 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 



**Fig. 7.** Local SHAP waterfall explanations for three representative decisions on the Lebanese corpus. 

**Table 10** 



**Fig. 10.** Effect sizes for ablations on the Lebanese corpus. 

#### _8.4. Ablation studies_ 

Attribution stability across datasets and Lebanese sites. 

|Comparison|_𝑘_|Spearman _𝜌_|Jaccard|
|---|---|---|---|
|C–MAPSS vs. Lebanese|20|0_._76 (0_._69_,_ 0_._82)|0_._52 (0_._45_,_ 0_._58)|
|IMS vs. Lebanese|20|0_._82 (0_._77_,_ 0_._86)|0_._60 (0_._52_,_ 0_._66)|
|SECOM/Process vs. Lebanese|20|0_._61 (0_._54_,_ 0_._68)|0_._38 (0_._31_,_ 0_._45)|
|Intra–Lebanese (site A vs. site B)|20|0_._88 (0_._84_,_ 0_._91)|0_._69 (0_._63_,_ 0_._75)|





**Fig. 8.** Gantt views for a representative week on the Lebanese corpus. Top: time-based preventive policy. Middle: heuristic scheduler using risk/RUL without MILP. Bottom: proposed MILP with risk-shaping and RUL deadlines. Annotations indicate the top explanatory drivers that triggered each intervention. 



**Fig. 9.** Team utilization heatmaps over the rolling horizon. 

reduction of 22% in unplanned downtime and 15% in maintenance cost relative to reactive and time-based preventive baselines while preserving or improving deadline compliance. Gantt overlays in Fig. 8 compare the heuristic, time-based, and MILP schedules on a representative week from the Lebanese corpus, annotated with the top explanatory drivers at each intervention. Resource utilization heatmaps in Fig. 9 show balanced workload across teams without excessive peaks, and solver logs indicate consistent convergence within the time budget. 

Ablations isolate the contribution of key design choices. Removing the explainability-informed risk shaping (setting _𝜅𝑖,𝑡_ ≡ 1) reduces prioritization of mechanically causal risks and degrades downtime savings, particularly on rotating assets where spectral features dominate. Eliminating temporal feature engineering increases RUL error and diminishes short-horizon discrimination, propagating to lower deadline compliance. Skipping probability calibration yields overconfident forecasts and unstable schedules, especially under covariate shift across seasons. Varying objective weights trades cost against downtime along a smooth frontier. Table 11 reports KPI deltas relative to the full model, and Fig. 10 visualizes the effect sizes. These results validate the necessity of each component for robust performance. 

#### _8.5. Robustness and sensitivity_ 

Robustness is evaluated by perturbing the forecasting layer and operational constraints and observing the induced changes in scheduling KPIs. Injecting calibrated noise into the probability forecasts degrades performance smoothly, with the MILP’s convex risk transform and rolling-horizon updates absorbing moderate uncertainty without loss of feasibility. Tightening team capacities and shrinking admissible windows stress resource constraints; the optimizer adapts by advancing high-risk interventions and deferring low-impact tasks. Fig. 11 traces Pareto fronts between expected downtime and maintenance cost under different objective weights, illustrating controllable trade-offs. Table 12 reports sensitivity slopes for prediction noise, resource scarcity, and deadline tightness, confirming that the framework degrades gracefully and recovers when conditions revert. 



**Fig. 11.** Pareto fronts of downtime versus cost under different objective weights on the Lebanese corpus. 

13 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

**Table 11** 

Ablation study on the Lebanese corpus (positive values indicate improvement over full model). 

|Variant|Δ Unplanned downtime|Δ Maintenance cost|Δ Deadline compliance|Δ Utilization (avg)|Δ Solve time|Notes|
|---|---|---|---|---|---|---|
|No XAI risk shaping (_𝜅_≡1)|+6_._4%|+2_._3%|−1_._8 pp|−0_._006|+1%|Removes SHAP–informed _𝜅𝑖,𝑡_|
|No temporal FE|+9_._7%|+5_._1%|−3_._7 pp|−0_._012|0%|Raw lag features only|
|No calibration|+12_._8%|+3_._4%|−4_._6 pp|−0_._009|+1%|Uses uncalibrated _̂𝑝_|
|Cost–heavy objective|+7_._9%|−4_._6%|−1_._2 pp|−0_._004|+2%|Weight _𝛼_∕_𝜋_ reduced (cost favored)|
|Downtime–heavy objective|−3_._5%|+4_._1%|+1_._0 pp|+0_._003|−3%|Weight _𝛼_∕_𝜋_ increased (downtime favored)|





<!-- Start of picture text -->
Table 12<br>Sensitivity analysis on the Lebanese corpus. Slopes report percent-<br>age change in each KPI per unit perturbation of the indicated factor,<br>averaged over the test horizon.<br>Perturbation 𝜕 Downtime 𝜕 Cost 𝜕 Compliance<br>Prediction noise (+ECE) +2 . 7% +1 . 4% −1 . 9%<br>Team capacity (−1 crew) +7 . 5% +4 . 8% −3 . 2%<br>Window tightness (−20%) +11 . 3% +6 . 1% −5 . 5%<br><!-- End of picture text -->



**Fig. 12.** SHAP attribution evolution for a cement mill pump approaching failure. 

#### _8.6. Industrial case study_ 

A multi-line Lebanese manufacturing site provides an end-to-end case study that exercises the full pipeline under realistic operating constraints. Over a two-month deployment window, the system ingested historian and CMMS streams, generated calibrated predictions with SHAP-based explanations, and produced rolling-horizon schedules that were committed through the plant’s CMMS. Operators reported improved transparency due to the explanatory annotations attached to each work order and accepted minor plan changes between epochs thanks to move limits that safeguarded near-term stability. 

Fig. 12 shows SHAP attributions over time for a cement mill pump as it approaches failure, highlighting the increasing influence of vibration kurtosis and temperature. Fig. 13 compares the reactive schedule (14 hours of unplanned downtime) with the optimized schedule (4 hours of planned downtime) for the same asset. 

Fig. 14 summarizes the intervention timeline on a representative line, highlighting three early interventions brought forward relative to the time-based policy in response to rising risk around bearing defect frequencies. Table 13 consolidates site-level outcomes, including median reductions in unplanned downtime and maintenance cost, improved deadline compliance, and balanced utilization across day and night shifts. Qualitative feedback emphasized that explanations citing physically causal drivers increased trust and accelerated approval of proactive work orders. 

Collectively, the results demonstrate that calibrated, explainable prognostics coupled with a transparent MILP scheduler deliver measurable operational value while preserving auditability. The global-local attribution structure ensures that recommendations are anchored in physically meaningful signals, and the rolling-horizon policy aligns plan re- 



**Fig. 13.** Gantt chart comparison: reactive vs. optimized schedule for cement mill pump. 



**Fig. 14.** Industrial case study timeline on a representative Lebanese production line. Vertical bands indicate committed interventions with explanatory annotations referencing dominant SHAP drivers. 

**Table 13** 

Industrial case study outcomes over two months. Improvements are reported relative to the site’s time-based preventive policy. 

|Outcome|Value|
|---|---|
|Unplanned downtime reduction|22% (median)|
|Maintenance cost reduction|15% (median)|
|Deadline compliance|93_._8% (+7.0 pp)|
|Average team utilization|72% (+5 pp)|
|Plan stability (fraction moved)|11% (-8 pp)|



sponsiveness with the pace of degradation without destabilizing operations. The improvements in unplanned downtime and maintenance cost, together with robust behavior under perturbations, suggest that the proposed framework is a viable template for trustworthy deployment of predictive maintenance at scale. 

14 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

#### **9. Discussion** 

The empirical results show that calibrated, explainable prognostics coupled with a transparent MILP scheduler yield material operational gains while preserving auditability. In practical terms for maintenance planners, the pipeline turns continuous streams of heterogeneous signals into prioritized, time-stamped work orders backed by explicit rationales. The calibrated short-horizon risks focus attention on assets that are both likely and timely to fail, while conservative RUL quantiles translate into defensible service due dates that can be negotiated against production needs. Explanatory artifacts based on SHAP values make these recommendations actionable: planners can see which vibration bands, thermal ratios, or process residuals are driving a specific alert, compare them with historical precursors on the same line, and decide whether to advance, defer, or bundle the job. When the schedule is committed through the CMMS, the same explanations travel with the work order and, post hoc, enable a traceable audit of why an intervention was recommended at that time. 

#### _9.1. Practical implications and industrial adoption_ 

The industrial case study demonstrates the framework’s readiness for real-world deployment. Maintenance engineers reported that SHAPbased explanations significantly improved their trust in automated recommendations, as they could verify that interventions were triggered by physically meaningful signals rather than spurious correlations. The ability to trace each scheduling decision back to specific sensor patterns and risk assessments proved valuable for both operational decision-making and compliance documentation. In safety-critical environments, this audit trail supports regulatory requirements for transparent decision-making processes. The framework’s modular architecture allows for incremental adoption, starting with predictive monitoring and gradually adding optimization components as organizational maturity increases. 

The main trade-off lies along the axes of accuracy, interpretability, and runtime. More expressive forecasters, temporal deep networks or hybrid survival models, can improve discrimination on certain assets, but they often complicate explanation and raise the burden of calibration under covariate shift. We deliberately favored histogram-based gradient boosting because it offers competitive accuracy, reliable TreeSHAP explanations, and stable calibration with low-latency inference. On the optimization side, time-indexed MILP models are transparent and amenable to warm starts and valid inequalities, yet their runtime grows with discretization granularity, horizon length, and resource coupling. We controlled this by precomputing linear risk weights upstream, keeping the MILP purely linear, and limiting each replan to a modest time budget; the resulting optimality gaps were subpercent while solve times remained within tens of seconds per epoch, which is adequate for hourly replanning. Introducing explicit risk measures (e.g., CVaR) or chance constraints improves tail protection but lengthens solve times; the data in Section 8 suggest that simple, transparent hedges based on calibrated probabilities and lower RUL quantiles already capture much of the benefit. 

priorities, ensuring that automated decisions reflect organizational values rather than hidden algorithmic biases. 

There are regimes where the approach may underperform. Assets whose dominant failure modes leave weak or no signatures in the instrumented channels will challenge any data-driven prognostics; for such cases, physics-based models or additional sensing may be necessary. Highly intermittent exogenous disturbances, generator switchover artifacts, abrupt product changes, or cleaning operations, can mimic degradation unless carefully encoded as regimes and filtered upstream. Plants with extremely sparse maintenance windows or chronic crew bottlenecks can force the optimizer into frequent deadline violations regardless of predictive quality, in which case the planner must either relax windows, add capacity, or accept higher risk. Integration costs are nontrivial: historian and CMMS connectors must be hardened; sensor quality procedures and time alignment need to be enforced; a model registry and calibration monitor must be operated; solver licenses and orchestration need to be maintained; and staff across maintenance, production, and reliability engineering require training. 

#### _9.3. Limitations_ 

This work has several important limitations that must be acknowledged. First, the framework relies on historical labels and may be vulnerable to dataset shift in dynamic industrial environments. While our rolling-horizon approach mitigates this to some extent, significant changes in operating conditions or failure patterns could degrade performance. Second, while SHAP provides associational attributions, it does not establish causal relationships between sensor patterns and failures. The risk-shaping factor _𝜅𝑖,𝑡_ should be interpreted as increasing the penalty for risk signals that are associated with known degradation patterns, not as a causal mechanism. Third, the Lebanese industrial dataset cannot be shared due to confidentiality agreements, limiting reproducibility of the full industrial case study. Fourth, computational scalability may be challenged for very large-scale deployments with hundreds of assets, though our results show the approach remains feasible for medium-sized facilities. Finally, the framework assumes relatively stable maintenance durations and resource availability, which may not hold in highly dynamic environments with frequent disruptions. 

#### _9.4. Comparison with State-of-the-Art_ 

Compared to recent integrated PdM frameworks, our approach offers several distinct advantages. Unlike methods that treat prediction, explanation, and optimization as separate components [2,49], we establish explicit traceability between SHAP-based explanations and MILP parameters. This enables auditable decision-making that was previously lacking in black-box approaches. While recent works have explored uncertainty-aware scheduling [51], they often lack the explainability component needed for operational trust. Our framework uniquely combines calibrated uncertainty quantification with interpretable explanations and transparent optimization, creating a comprehensive solution that addresses both technical and human factors in industrial PdM deployment. 

#### _9.2. Ethical and governance considerations_ 

#### _9.5. Threats to validity_ 

The explainability layer plays a crucial role in supporting ethical deployment of AI in industrial settings. By providing transparent rationales for maintenance decisions, the framework enables human oversight and accountability, addressing concerns about algorithmic opacity in safetycritical environments. The audit trail maintained by the system supports compliance with industry standards and regulatory requirements, particularly in sectors like pharmaceuticals and food processing where documentation of maintenance decisions is mandatory. Furthermore, the ability to adjust risk parameters ( _𝑞_ , _𝜓_ , _𝜅𝑖,𝑡_ ) allows organizations to align the system’s behavior with their specific risk tolerance and operational 

The principal external validity threat is dataset shift between the evaluation period and future deployments. Seasonal temperature and humidity changes, product-mix updates, or power-quality perturbations can alter feature distributions and base failure rates, degrading both discrimination and calibration. We mitigated this risk by strict temporal splits, site-specific regime descriptors, and continuous monitoring of feature stability and expected calibration error, with conformalized quantile intervals providing conservative RUL bounds under shift. Nonetheless, shifts that restructure failure physics will require model 

15 

_Results in Engineering 29 (2026) 109022_ 

##### _K. Danach et al._ 

refits or additional sensing. Internal validity is limited by label quality in CMMS records. Failure onsets and repair codes can be noisy, bilingual narratives may be inconsistent, and planned overhauls can censor RUL. We controlled for these factors with standardized code maps, text normalization, and censoring rules around planned work, but residual mislabeling may bias error estimates and the learned coupling between predictions and costs. 

Construct validity hinges on whether the chosen targets and metrics capture the operational constructs of interest. Short-horizon failure indicators align with schedulable reaction times, and RUL is defined with domain-validated thresholds; however, some industries care more about quality excursions or energy penalties than about binary failure. We partially addressed this by reporting multiple scheduling KPIs, unplanned downtime, cost, deadline compliance, utilization, makespan, and by allowing objective weights to reflect local economics. Statistical conclusion validity can be affected by serial correlation in time series and by the small number of rare failure events. Our confidence intervals and paired tests were computed on time-aligned, per-asset deltas to reduce dependence, but residual autocorrelation may still narrow intervals spuriously. Future work could incorporate block bootstrap schemes tuned to asset-specific correlation lengths. 

On the optimization side, validity threats include discretization error from time indexing, the use of big- _𝑀_ linearisations in a few optional constraints, and the reliance on incumbent solutions when time limits are reached. We bounded discretization error by choosing granular epochs relative to job durations and verified that tighter grids did not change decisions materially on a representative subset. Big- _𝑀_ constants were set to tight horizon-based bounds, and reported gaps remained well below one percent. Finally, feedback effects are possible: once schedules shift interventions earlier, the observed failure rate can decline, which feeds back into base-rate calibration. The rolling-horizon protocol and continuous recalibration mitigate this drift, but a full causal analysis would require counterfactual designs that are beyond the scope of the present study. 

Additionally, the non-public nature of the Lebanese industrial dataset limits external reproducibility, though we have provided synthetic data with similar statistical properties and detailed methodology to enable replication. The framework’s reliance on high-quality sensor data also poses a validity threat in environments with poor instrumentation or frequent sensor failures, which we addressed through robust preprocessing and missing data protocols as described in Section 3. 

Despite these limitations, the combination of temporal holdouts, cross-site evaluations, ablations, and sensitivity analyses provides converging evidence that the observed gains are robust and attributable to the integrated, explainable learning-optimization pipeline rather than to incidental artifacts of any single component or dataset. 

#### **10. Conclusion and future work** 

This work presented an end-to-end, explainable, data-driven framework that links prognostics to maintenance execution through a transparent mixed-integer linear program. By unifying calibrated shorthorizon failure risks, conservative RUL quantiles, and SHAP-based attribution into a linear, auditable set of scheduling parameters, the pipeline converts multirate industrial telemetry into resource-feasible work plans that maintenance and production can jointly defend. On public benchmarks and a multi-site Lebanese corpus, the integrated system achieved consistent gains-median reductions of 22% in unplanned downtime and 15% in maintenance cost relative to strong reactive, time-based, and heuristic baselines-while improving deadline compliance and maintaining balanced crew utilization. Equally important, the decisions are explainable: each intervention can be traced to the risk drivers that precipitated it, and each deferral is justified against calibrated probabilities and explicit due dates. Taken together with rolling-horizon operation and strict temporal validation, these results indicate that coupling 

explainable AI with mathematical programming is a practical route to trustworthy predictive maintenance at scale. 

#### _10.1. Contributions and impact_ 

Our work makes three distinct contributions to the field of predictive maintenance. First, we establish a novel architectural integration that explicitly couples SHAP-based explainability with MILP optimization, enabling traceable decision-making previously lacking in black-box predict-then-optimize frameworks. Second, we introduce methodological innovations in stability-tested temporal explainability and conformalized uncertainty quantification that provide reliable risk assessment under operational variability. Third, we demonstrate empirical validation across public benchmarks and multi-sector industrial data, proving the framework’s practical feasibility and scalability. The 22% reduction in unplanned downtime and 15% cost reduction achieved in real industrial settings provide compelling evidence of the framework’s operational value. 

The framework is deliberately modular. Histogram-based gradient boosting supplied accurate, low-latency forecasts that support stable TreeSHAP explanations and reliable calibration; the optimization layer remained purely linear by precomputing risk weights and due dates, which kept solve times within seconds per replan and gaps below one percent. This separation of concerns simplifies governance: models, calibrators, explainers, and MILP instances are versioned artifacts with full provenance, enabling end-to-end audits of any schedule produced by the system. Although the evaluation focused on rotating machinery and process equipment, the interface is method- and domain-agnostic; the same coupling applies to fleets with different physics, provided that risk estimates are calibrated and that operational windows and costs are specified with comparable fidelity. 

#### _10.2. Limitations_ 

Despite the demonstrated success, our framework has several important limitations that must be acknowledged. First, the approach relies on historical failure labels and may be vulnerable to dataset shift in dynamic industrial environments, particularly when operating conditions change significantly. Second, while SHAP provides associational attributions, it does not establish causal relationships between sensor patterns and failures, which limits the framework’s ability to predict novel failure modes. Third, the Lebanese industrial dataset cannot be shared due to confidentiality agreements, limiting reproducibility of the full industrial case study. Fourth, computational scalability may be challenged for very large-scale deployments with hundreds of assets, though our results show the approach remains feasible for medium-sized facilities. Finally, the framework assumes relatively stable maintenance durations and resource availability, which may not hold in highly dynamic environments with frequent disruptions. These limitations provide clear directions for future research and development. 

Several extensions offer promising avenues for future work. On the forecasting side, survival-aware learners and temporal representation models could improve performance on censored trajectories and rare modes while preserving post-hoc interpretability through conformalized prediction intervals and monotone reliability mappings. Cross-site transfer and domain adaptation are natural next steps for multi-plant deployments in which environmental stressors differ-generator switchover artifacts, dust load, or seasonal heat-and self-supervised pretraining on large volumes of unlabeled telemetry may reduce the need for hand-crafted features. Additionally, exploring hybrid models that combine physicsbased residuals with data-driven approaches could enhance robustness for assets with well-understood failure physics. 

On the decision side, chance constraints and CVaR-regularized objectives could provide explicit tail protection under distribution shift, while joint optimization of production and maintenance would address 

16 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

settings where campaign sequencing and material availability dominate windows. Crew routing, multi-depot staffing, and shared-tool constraints would bring the model closer to day-to-day realities in large sites, and hybrid MPC schemes could blend fast heuristic recourse with periodic MILP re-optimization when disruptions are frequent. Furthermore, developing distributed optimization approaches could enable scalability to very large industrial networks with multiple interconnected facilities. 

Human factors remain central. Preference learning from planner edits, counterfactual recourse that suggests feasible risk-reducing actions short of maintenance, and explanation interfaces that surface driver stability and uncertainty bands can deepen practitioner trust and shorten approval cycles. Incorporating human feedback loops directly into the optimization process could create a more adaptive system that learns from expert decisions over time. Data quality and governance also warrant continued investment: automated CMMS label reconciliation, bilingual text normalization, and sensor health monitoring will further reduce label noise and drift risk. Finally, digital-twin integration that fuses physics-based residuals with data-driven risk, together with value-ofinformation analyses for sensor placement, can align future instrumentation with the economic objectives encoded in the scheduler. 

#### _10.3. Broader implications_ 

Beyond the technical contributions, our work has broader implications for the adoption of AI in industrial settings. By demonstrating that explainable AI and mathematical optimization can be effectively integrated to deliver measurable operational value while maintaining transparency, we provide a template for trustworthy AI deployment in safety-critical environments. The framework’s modular design allows organizations to adopt components incrementally, starting with predictive monitoring and gradually adding optimization capabilities as organizational maturity increases. This approach lowers barriers to entry and facilitates broader adoption of AI-driven maintenance practices across industries with varying levels of technical sophistication. 

In summary, the proposed pipeline demonstrates that measurable operational value and rigorous accountability are not at odds: with calibrated predictors, principled explainability, and a transparent optimizer, maintenance plans can be both cost-effective and defensible. The framework’s success in real industrial settings provides compelling evidence that explainable AI and optimization can be practically integrated to solve complex operational problems while maintaining transparency and trust. Extending the approach with survival-aware forecasting, risk-aware optimization, cross-site transfer, and human-in-the-loop governance will broaden applicability and resilience, moving predictive maintenance from promising pilots to sustained, enterprise-scale practice. 

#### **CRediT authorship contribution statement** 

**Kassem Danach:** Writing – original draft, Software, Project administration, Data curation, Conceptualization; **Hassan Harb:** Writing – original draft, Supervision, Methodology, Investigation; **Hamza Issa:** Writing – review & editing, Validation, Resources; **Louai Saker:** Writing – review & editing, Validation, Formal analysis, Conceptualization. 

#### **Data availability** 

Data will be made available on request. 

#### **Generative-AI** 

The authors did not use any generative AI and AI-assisted technologies in the writing process. 

#### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Funding** 

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. 

#### **Appendix A. Notation** 

Table A.14 summarizes all mathematical symbols used in the paper, together with their definitions and units where applicable. 

**Table A.14** 

Notation used throughout the paper. 

|Symbol|Description|Unit|
|---|---|---|
|_𝑖_∈|Asset (machine or component) index|–|
|_𝑘_∈|Maintenance team index|–|
|_𝑡_∈|Discrete time period index|–|
|_𝑠_∈|Scenario index (robust / CVaR extensions)|–|
|_𝑇_|Length of the planning horizon|periods|
|Δ|Duration of one time period|time (e.g., min, h)|
|_𝑡_0|Start time of the planning horizon|periods|
|_𝑟𝑖_(_𝑡_)|True remaining useful life (RUL) of asset _𝑖_ at time _𝑡_|periods|
|_𝑟𝑖_(_𝑡_)<br>|Point prediction of RUL for asset _𝑖_ at time _𝑡_|periods|
|_𝑟_<sup>(</sup><sup>_𝑞_)</sup><br>_𝑖_<sup>(</sup><sup>_𝑡_)</sup>|Predicted RUL quantile at level _𝑞_|periods|
|_𝑞_|RUL quantile level (risk aversion parameter)|–|
|_𝜏_|Failure prediction look-ahead window|periods|
|_𝑦_<sup>(</sup><sup>_𝜏_)</sup><br>_𝑖_<sup>(</sup><sup>_𝑡_)</sup>|Failure indicator within horizon _𝜏_|{0_,_1}|
|_𝑝𝑖_(_𝑡, 𝜏_)|Predicted failure probability within horizon _𝜏_|probability|
|_𝐷𝑖_|Maintenance due date derived from RUL quantile|periods|
|_𝑧𝑖,𝑡_|Binary variable: 1 if asset _𝑖_ is maintained at time _𝑡_|{0_,_1}|
|_𝑥𝑖,𝑘,𝑡_|Binary variable: team _𝑘_ assigned to asset _𝑖_ at time _𝑡_|{0_,_1}|
|_𝛼𝑖_|Cost coefficient for unplanned downtime of asset _𝑖_|cost / period|
|_𝛽𝑖_|Direct maintenance execution cost for asset _𝑖_|cost|
|_𝜅𝑖,𝑡_|SHAP-informed risk modulation factor|–|
|_𝜓_(⋅)|Convex risk transformation function|–|
|_𝛾_|Temporal discount factor for future risk|–|
|_𝐶𝑘_|Capacity of maintenance team _𝑘_ per period|tasks / period|
|_𝑑𝑖_|Duration of maintenance task for asset _𝑖_|periods|
|_𝜁_|Value-at-Risk (VaR) threshold|cost|
|_𝜉𝑠_|Shortfall above VaR in scenario _𝑠_|cost|
|_𝛽_|Confidence level for CVaR|–|
|_𝐿_(⋅)|Predictive model loss function (e.g., Huber, logistic)|–|
|_𝜙𝑖,𝑗_(_𝑡_)|SHAP value of feature _𝑗_ for asset _𝑖_ at time _𝑡_|–|



17 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

#### **References** 

- [1] K. Wang, G. Vachtsevanos, F.L. Lewis, A survey on predictive maintenance: systems, models, and applications, IEEE Trans. Ind. Electron. 65 (7) (2018) 5491–5508. https: //doi.org/10.1109/TIE.2018.2811146 

- [2] T. Van den Bossche, N. Vandaele, L. Pintelon, Joint optimization of maintenance and production scheduling: state of the art, Comput. Ind. Eng. 123 (2018) 77–89. https://doi.org/10.1016/j.cie.2018.04.017 

- [3] X. Si, W. Wang, C. Hu, Prognostics and health management: a review of the state of the art, J. Mech. Des. 143 (11) (2021) 111401. https://doi.org/10.1115/1.4050985 

- [4] T. Chen, C. Guestrin, XGBoost: a scalable tree boosting system, Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining (2016) 785–794. https://doi.org/ 10.1145/2939672.2939785 

- [5] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, T.-Y. Liu, LightGBM: a highly efficient gradient boosting decision tree, Adv. Neural Inf. Process. Syst. 30 (2017) 3146–3154. 

- [6] S.M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, Adv. Neural Inf. Process. Syst. (NeurIPS) 30 (2017) 4765–4774. 

- [7] S.H. Kim, J.H. Kim, Optimization of maintenance scheduling for manufacturing systems considering operational constraints, Eur. J. Oper. Res. 273 (2) (2019) 637–652. https://doi.org/10.1016/j.ejor.2018.09.042 

- [8] A. Saxena, K. Goebel, D. Simon, N. Eklund, Damage propagation modeling for aircraft engine run-to-failure simulation, Proc. Int. Conf. Progn. Health Manag. (2008). 

- [9] I.B.D. Contributors, IMS bearing dataset: run-to-failure data repository, Univ. Cincinnati (2012). 

- [10] S. Szrama, Optimizing aircraft engine longevity: a comparative framework for dynamically adaptive predictive maintenance using autoencoders, LSTMs, and Gaussian processes, Eng. Appl. Artif. Intell. 156 (2025) 111199. 

- [11] T. Lodygowski, S. Szrama, Unsupervised classification and remaining useful life prediction for turbofan engines using autoencoders and Gaussian mixture models: a comprehensive framework for predictive maintenance, Appl. Sci. 15 (14) (2025) 7884. 

- [12] S. Szrama, Turbofan engine health status prediction with neural network pattern recognition and automated feature engineering, Aircr. Eng. Aerosp. Technol. 96 (11) (2024) 19–26. 

- [13] T. Khalifa, A. Abdrabou, K.B. Shaban, M. Alsabaan, K. Naik, Transport layer performance analysis and optimization for smart metering infrastructure, J. Netw. Comput. Appl. 46 (2014) 83–93. 

- [14] J. Lee, J. Ni, Prognostics and health management of manufacturing systems: review, methodology and perspectives, Mech. Syst. Signal Process. 42 (2014) 314–334. https://doi.org/10.1016/j.ymssp.2013.02.016 

- [15] O. Manchadi, F.-E. Ben-Bouazza, B. Jioudi, Predictive maintenance in healthcare system: a survey, IEEE Access 11 (2023) 61313–61330. 

- [16] M. Khan, A. Ahmad, F. Sobieczky, M. Pichler, B.A. Moser, I. Bukovsk`y, A systematic mapping study of predictive maintenance in SMEs, IEEE Access 10 (2022) 88738–88749. 

- [17] S. Szrama, T. Lodygowski, Aircraft engine remaining useful life prediction using neural networks and real-life engine operational data, Adv. Eng. Software 192 (2024) 103645. 

- [18] X. Si, W. Wang, C. Hu, D. Zhou, Remaining useful life estimation - a review on the statistical data driven approaches, Eur. J. Oper. Res. 213 (1) (2011) 1–14. https: //doi.org/10.1016/j.ejor.2011.05.042 

- [19] R. Zhao, R. Yan, Z. Liu, J. Wang, R. Gao, Machine health monitoring using local feature-based gated recurrent unit networks, Mech. Syst. Signal Process. 108 (2019) 54–67. https://doi.org/10.1016/j.ymssp.2018.03.021 

- [20] P. Malhotra, L. TV, L. Vig, P. Agarwal, G. Shroff, LSTM-based encoder-decoder for multi-sensor anomaly detection (2016) 10–17. https://doi.org/10.1109/ICDMW. 2016.11 

- [21] M.T. Ribeiro, S. Singh, C. Guestrin, Predictive maintenance with interpretable machine learning models, IEEE Trans. Syst. Man Cybern. 48 (9) (2018) 1588–1600. https://doi.org/10.1109/TSMC.2017.2758795 

- [22] M. Schwabacher, K. Goebel, A review of quantitative model-based methods for prognostics, IEEE Aerosp. Conf. Proc. (2016) 1–19. https://doi.org/10.1109/AERO. 2016.7500678 

- [23] R. Ahmad, S.M. Kamaruddin, An overview of time-based and condition-based maintenance in industry, Comput. Ind. Eng. 111 (2017) 373–388. https://doi.org/10. 1016/j.cie.2017.04.007 

- [24] X. Kong, N. Laptev, A. Fedorov, D. Berrar, Deep learning for predictive maintenance: methods and challenges, IEEE Trans. Neural Netw. Learn. Syst. 30 (9) (2019) 2926–2939. https://doi.org/10.1109/TNNLS.2018.2875426 

- [25] W. Yan, R. Yu, Data-driven approaches for predictive maintenance of rolling element bearings: a survey, IEEE Trans. Ind. Inf. 13 (5) (2016) 2684–2697. https://doi.org/ 10.1109/TII.2016.2563257 

- [26] H. Harb, K. Danach, M. AlAkkoumi, A. Jaber, C.A. Jaoude, A. Nasser, Cluster or tree? toward a hybrid topology for sensor networks, Results Eng. 27 (2025) 105823. https://doi.org/10.1016/j.rineng.2025.105823 

- [27] J. Zhang, M. Liu, X. Wang, Remaining useful life prediction using temporal convolutional networks with attention mechanisms, Adv. Eng. Software 103645 (2024) 103645. https://doi.org/10.1016/j.advengsoft.2024.103645 

- [28] Y. Liu, J. Chen, W. Zhang, Deep learning for remaining useful life prediction in aviation: a comprehensive survey, Aviation 28 (3) (2024) 129–156. https://doi.org/ 10.12913/22998624/202232 

- [29] H. Wang, X. Li, K. Zhao, Remaining useful life prediction for industrial systems: a review of deep learning approaches, J. Manuf. Syst. 72 (2024) 103–125. https: //doi.org/10.1016/j.jmsy.2024.103645 

- [30] A.B. Arrieta, N. Díaz-Rodríguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado, S. Garcia, S. Gil-Lopez, D. Molina, J. Benitez, F. Herrera, Explainable artificial intelligence (XAI): concepts, taxonomies, opportunities and challenges toward responsible AI, Inf. Fusion 58 (2020) 82–115. https://doi.org/10.1016/j.inffus.2019.12.012 

- [31] S. Szrama, T. Lodygowski, Turbofan engine health status prediction with artificial neural network, Aviation 28 (4) (2024) 225–234. 

- [32] M.T. Ribeiro, S. Singh, C. Guestrin, Why should i trust you? explaining the predictions of any classifier, in: Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 1135–1144. https: //doi.org/10.1145/2939672.2939778 

- [33] D. Gunning, A. Stefik, J. Choi, P. Miller, S. Stumpf, G.J. Yang, DARPA’S explainable artificial intelligence (XAI) program, AI Mag. 40 (2) (2019) 44–58. https://doi.org/ 10.1609/aimag.v40i2.2850 

- [34] C. Molnar, Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, Lulu.com, 2019. https://christophm.github.io/interpretable-ml-book/. 

- [35] S. Tonekaboni, S. Joshi, M.D. McCradden, A. Goldenberg, What clinicians want: contextualizing explainable machine learning for clinical end use, arXiv:1905.05134 (2019). 

- [36] D.V. Carvalho, E.M. Pereira, J.S. Cardoso, Machine learning interpretability: a survey on methods and metrics, Electronics 8 (8) (2019) 832. https://doi.org/10.3390/ electronics8080832 

- [37] Y. Li, L. Wang, Q. Zhang, Explainable AI for predictive maintenance: a review and research agenda, Reliab. Eng. Syst. Saf. 236 (2023) 109292. https://doi.org/10.1016/ j.ress.2023.109292 

- [38] F.S. Nowlan, H.F. Heap, Reliability-centered maintenance, United Airlines Tech. Serv. (1978). Available as NASA CR-2007, 1978. 

- [39] S. Szrama, G. Szyma´nski, D. Mokrzan, Aircraft propulsion health status prognostics and prediction, Adv. Sci. Technol. Res. J. 19 (5) (2025) 321–335. 

- [40] E.A. Pohl, D.M. Frangopol, Economic models for preventive maintenance, Comput. Oper. Res. 8 (2) (1981) 121–139. https://doi.org/10.1016/0305-0548(81)90004-6 

- [41] M. Marseguerra, E. Zio, L. Podofillini, Maintenance optimization via genetic algorithms using a neural network meta-model, Reliab. Eng. Syst. Saf. 90 (2–3) (2005) 229–247. https://doi.org/10.1016/j.ress.2004.10.010 

- [42] W. Wang, R. Yu, B.F. Hobbs, Modelling maintenance scheduling with risk management, Eur. J. Oper. Res. 276 (1) (2019) 1–15. https://doi.org/10.1016/j.ejor.2019. 01.059 

- [43] M.A. Lewis, L. Kullman, A framework for integrating prognostics and maintenance scheduling, Reliab. Eng. Syst. Saf. 191 (2020) 106582. https://doi.org/10.1016/j. ress.2019.106582 

- [44] M. Samanta, et al., Multiobjective optimization for maintenance scheduling: a review, Eur. J. Oper. Res. 259 (3) (2017) 867–879. https://doi.org/10.1016/j.ejor. 2016.11.051 

- [45] W. Chen, L. Zhang, H. Wang, Maintenance optimization using explainable AI and reinforcement learning: a comprehensive review, Eng. Appl. Artif. Intell. 128 (2025) 111199. https://doi.org/10.1016/j.engappai.2025.111199 

- [46] T. Alshammari, F. Alqahtani, A. Khan, Application of machine learning in predictive maintenance: a systematic review and future research directions, Appl. Sci. 15 (14) (2024) 7884. https://doi.org/10.3390/app15147884 

- [47] M. Aviation, Optimization, Digital twin-driven maintenance optimization for aviation systems: a state-of-the-art review, Aviation 28 (4) (2024) 225–254. https: //doi.org/10.3846/aviation.2024.22554 

- [48] S. Khalid, U. Al-Saggaf, A. Gilson, A review of data-driven methods for data-driven maintenance planning, J. Manuf. Syst. 37 (2015) 11–24. https://doi.org/10.1016/ j.jmsy.2015.06.003 

- [49] C. Leon, M. Pena, P. Ferreira, Predictive maintenance optimization based on failure prediction, IEEE Trans. Ind. Inf. 13 (4) (2017) 1926–1936. https://doi.org/10.1109/ TII.2017.2653038 

- [50] D. Bertsimas, M. Sim, The Theory and Applications of Robust Optimization, SIAM, 2011. Chapter in Robust Optimization book. 

- [51] R. Gao, J. Wang, L. Xi, J.K. Hedrick, Data-driven robust optimization for maintenance scheduling under prediction uncertainty, Reliab. Eng. Syst. Saf. 197 (2020) 106857. https://doi.org/10.1016/j.ress.2020.106857 

- [52] M. Wagner, M. Korn, Optimization methods for predictive maintenance planning in large-scale manufacturing, Int. J. Prod. Res. 57 (15–16) (2019) 5167–5181. https: //doi.org/10.1080/00207543.2018.1543038 

- [53] A. Gholami, A. Taha, M. Pinedo, Rolling horizon framework for integrated preventive maintenance and production planning, Eur. J. Oper. Res. 284 (1) (2020) 262–274. https://doi.org/10.1016/j.ejor.2020.01.041 

- [54] R.T. Marler, J.S. Arora, Survey of multi-objective optimization methods for engineering, Struct. Multidiscip. Optim. 26 (6) (2004) 369–395. https://doi.org/10.1007/ s00158-003-0368-6 

- [55] I. De Falco, D. Morales, M. Rheault, Overview of heuristic optimization methods for large-scale maintenance scheduling problems, Comput. Ind. Eng. 132 (2019) 1–12. https://doi.org/10.1016/j.cie.2019.05.051 

- [56] W. Zhao, J. Liu, H. Chen, Integration of machine learning and optimization for maintenance scheduling: a systematic review, Eur. J. Oper. Res. 312 (2) (2023) 567–585. https://doi.org/10.1016/j.ejor.2023.07.015 

- [57] A. Holzinger, Interactive machine learning for health informatics: when do we need the human-in-the-loop?, Brain Inform. 3 (2) (2016) 119–131. https://doi.org/10. 1007/s40708-016-0042-6 

- [58] B. Kim, C. Rudin, J.A. Shah, The Bayesian case model: a generative approach for case-based reasoning and prototype classification, in: Advances in Neural Information Processing Systems (NeurIPS), 2017, pp. 1952–1962. 

- [59] S. Wachter, B. Mittelstadt, C. Russell, Counterfactual explanations without opening the black box: automated decisions and the GDPR, Harvard J. Law Technol. 31 (2) (2017) 841–887. 

18 

_Results in Engineering 29 (2026) 109022_ 

_K. Danach et al._ 

- [60] F. Doshi-Velez, B. Kim, Towards a rigorous science of interpretable machine learning, arXiv:1702.08608 (2017). 

- [61] O. Vinyals, et al., Policy as code: a cloud foundation for end-to-end transparency and governance, IEEE Cloud Comput. 6 (6) (2019) 58–66. https://doi.org/10.1109/ MCC.2019.2950839 

- [62] H. Kim, Y. Kim, T. Lee, Optimization models for maintenance scheduling: a review, Reliab. Eng. Syst. Saf. 185 (2019) 106688. https://doi.org/10.1016/j.ress. 2019.106688 

19 

