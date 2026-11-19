**_IET Smart Grid_** 





**<mark>SPECIAL ISSUE</mark>** Deep Learning Solutions for Secure, Reliable, and Responsive Smart Grid Operations 

# **ORIGINAL RESEARCH -** 



<!-- Start of picture text -->
OPEN ACCESS<br><!-- End of picture text -->



## **Carbon‐Aware Scheduling in Cloud Computing Operations: A Multi‐Objective Optimisation Approach** 

Kassem Danach<sup>1</sup> | Kassem Hamze<sup>2</sup> | Hassan Harb<sup>3</sup> | Hassan Kanj<sup>3</sup> 

> 1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon | 2Faculty of Engineering, Islamic University of Lebanon, Beirut, Lebanon |<sup>3</sup> College of Engineering and Technology, American University of the Middle East, Egaila, Kuwait 

**Correspondence:** Kassem Danach (kassem.danach@mu.edu.lb) 

**Received:** 28 October 2025 | **Revised:** 11 December 2025 | **Accepted:** 27 December 2025 

**Handling Editor:** Ge Chen 

**Keywords:** air pollution control | artificial intelligence and data analytics | communications and networking | control engineering computing | data analysis | decentralised control | distribution networks | energy management systems | environmental factors | genetic algorithms 

##### **ABSTRACT** 

The rapid expansion of cloud computing has intensified the environmental impact of large‐scale data centres, which now represent a significant portion of global electricity consumption. Traditional scheduling strategies typically optimise performance or cost, disregarding the fluctuating carbon intensity of regional power grids. This study proposes a dynamic carbon‐aware scheduling framework that integrates real‐time carbon intensity forecasting with multi‐objective optimisation and adaptive rolling‐horizon control. The proposed model simultaneously minimises operational cost and greenhouse gas emissions by intelligently shifting computational workloads across time and geography in response to renewable energy availability. The framework combines an ensemble forecasting module, using long short‐term memory (LSTM) and gradient boosting regression, with a mixed‐integer linear programming (MILP) model solved via the _ε_ ‐constraint method. It adaptively updates scheduling decisions based on updated carbon forecasts and workload arrivals. Experimental validation on real datasets from the UK National Grid and Google Cloud workload traces demonstrates an average 25 _%_ reduction in CO2 emissions, a 7 − 10 _%_ improvement in cost efficiency and less than 3 _%_ performance degradation compared to conventional schedulers. Pareto front analysis further reveals actionable trade‐offs between economic efficiency and environmental sustainability. The results confirm that integrating operational research with carbon intelligence enables cloud infrastructures to become both cost‐effective and climate‐aligned. 

### **1** | **Introduction** 

### **1.1** | **Context** 

The exponential growth of digital services, artificial intelligence applications and data‐driven economies has led to an unprecedented increase in the energy consumption of cloud computing infrastructures. Data centres are now responsible for approximately 1 _._ 5 _%_ of global electricity demand and are projected to contribute significantly to greenhouse gas (GHG) emissions by 2030 if current operational practices persist [1]. Traditional 

scheduling algorithms in cloud environments prioritise computational performance or operational cost, often neglecting the dynamic carbon intensity of electricity grids. Consequently, the environmental footprint of cloud operations fluctuates widely depending on temporal and regional variations in energy generation sources. 

### **1.2** | **Motivation** 

Recent advances in renewable energy integration, carbon intensity forecasting and real‐time energy pricing provide new 

Kassem Danach, Kassem Hamze, Hassan Harb and Hassan Kanj contributed equally to this study. 

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

> © 2026 The Author(s). _IET Smart Grid_ published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology. 

1 of 16 

_IET Smart Grid_ , 2026; 9:e70056 https://doi.org/10.1049/stg2.70056 

opportunities for carbon‐aware scheduling, a paradigm that optimises computational workloads based on the carbon footprint of available energy at each time interval. From an operational research perspective, this involves multi‐objective decision‐making under uncertainty, balancing conflicting objectives such as cost minimisation, service‐level adherence and emission reduction. Existing studies in green computing and sustainable operations [2, 3] have made important progress in energy‐aware scheduling. However, most approaches rely on static energy profiles and deterministic optimisation, which fail to capture the stochastic nature of carbon intensity and workload demand. Moreover, few models explicitly quantify the trade‐off between economic and environmental performance using formal multi‐objective optimisation techniques. 

### **1.3** | **Novelty and Contributions** 

This research introduces a dynamic carbon‐aware scheduling framework for cloud computing operations that integrates three novel components: 

1. _Carbon intensity forecasting_ : A predictive module that estimates short‐term grid carbon intensity using machine learning time‐series models. 

2. _Multi‐objective optimisation_ : A mixed‐integer programming formulation that minimises both operational cost and carbon emissions simultaneously. 

3. _Adaptive scheduling_ : A rolling‐horizon mechanism that updates scheduling decisions in real time as new forecasts become available. 

The proposed framework contributes to the field of operational research by embedding sustainability metrics into computational resource allocation. The results demonstrate that a data‐driven optimisation approach can achieve substantial carbon reductions without degrading performance or increasing cost significantly. The model is validated on real‐world datasets from European and North American data centres, illustrating its scalability and robustness under varying energy market conditions. 

### **1.4** | **Paper Structure** 

The remainder of this paper is organised as follows. Section 2 reviews the related literature on carbon‐aware and energy‐ efficient scheduling. Section 3 presents the mathematical formulation of the proposed optimisation model. Sections 4 and 5 detail the methodology and experimental setup respectively. Section 6 discusses the experimental results, and Section 7 concludes the paper with implications for sustainable cloud operations and future research directions. 

### **2** | **Literature Review** 

The rapid expansion of cloud computing has significantly increased energy consumption and associated carbon emissions of large‐scale data centres, making them a substantial contributor 

to global electricity demand [1]. Traditional cloud scheduling algorithms generally focus on optimising performance or minimising operational cost while overlooking the spatial and temporal fluctuations in grid carbon intensity [2, 3]. This gap has motivated research on carbon‐aware workload scheduling that aligns cloud operations with low‐carbon electricity availability. 

### **2.1** | **Carbon‐Aware Scheduling and Forecasting** 

Carbon‐aware scheduling strategies leverage time‐ and location‐ dependent variations in carbon intensity to shift workloads towards periods and sites with cleaner electricity [3]. Accurate carbon intensity forecasting is central to these methods, employing advanced machine learning models such as convolutional neural networks (CNN) combined with bidirectional long short‐term memory (BiLSTM) networks to capture complex temporal patterns [4]. These forecasts enable proactive scheduling adjustments to minimise emissions without sacrificing service quality [5]. 

### **2.2** | **Multi‐Objective Optimisation in Cloud Scheduling** 

Scheduling in this context is formulated as a multi‐objective optimisation problem balancing competing goals of minimising carbon emissions, operational costs, and meeting service‐ level agreements (SLAs) [6]. Metaheuristic methods such as particle swarm optimisation (PSO) and orthogonal learning PSO have been demonstrated as effective for deriving Pareto‐optimal workload assignments that trade‐off these objectives [6, 7]. Reinforcement learning‐based approaches are also emerging to adaptively optimise allocations in dynamic cloud environments [8]. 

### **2.3** | **Optimisation Techniques in Cloud Scheduling** 

Recent developments in multi‐objective optimisation have significantly contributed to the field of sustainable cloud computing. These approaches aim to balance conflicting goals such as minimising energy consumption, reducing carbon emissions, and maintaining quality of service [4, 9]. Multi‐ objective evolutionary algorithms (MOEAs), such as the NSGA‐II and SPEA2, have been effectively employed to generate Pareto fronts that provide decision‐makers with trade‐ off solutions [6]. These methods have been extended through hybrid approaches that combine heuristics with exact methods, enhancing solution quality and computational efficiency [9]. 

Additionally, machine learning‐based optimisation frameworks, such as reinforcement learning (RL), are increasingly being adopted for dynamic workload scheduling. RL agents learn policies to adapt workload distributions based on real‐time grid conditions, optimising for emission reductions while respecting SLAs [8, 10, 11]. The integration of forecasting models with multi‐objective optimisation provides a predictive capability that 

2 of 16 

_IET Smart Grid,_ 2026 

enhances scheduling decisions, allowing proactive adjustments aligned with anticipated grid emissions [5]. 

Another promising approach involves the use of hyper‐ heuristics, which dynamically select among multiple heuristics based on problem instance characteristics. Multi‐armed bandit algorithms guide the hyper‐heuristic selection process, enabling adaptive and scalable cloud scheduling that aligns with sustainability targets [12–15]. These approaches demonstrate superior performance compared to static heuristics, especially in large‐scale and heterogeneous cloud environments [16]. 

In the context of real‐world constraints, recent studies have proposed hybrid optimisation frameworks that combine local search, decomposition techniques, and metaheuristics to address complex multi‐objective scheduling problems [9, 10]. These frameworks enable scalable solutions that respect operational constraints such as deadlines, capacity, migrations and energy budgets, thereby facilitating environmentally sustainable cloud operations. 

### **2.4** | **Research Gaps and Limitations** 

Despite significant progress, existing research exhibits several limitations that our work addresses: 

carbon‐aware heuristics assign workloads based on immediate carbon intensity minimisation and energy‐aware heuristics focus on reducing overall energy consumption regardless of carbon intensity [17, 18]. Evaluations consistently show carbon‐ aware multi‐objective methods achieve significantly greater emission reductions compared to these baselines while maintaining cost and performance competitiveness. 

### **2.6** | **Emerging Trends and Future Directions** 

Cutting‐edge research is expanding carbon‐aware scheduling towards integrating decentralised cloud architectures, dynamic carbon pricing signals and hybrid optimisation frameworks that fuse forecasting, AI‐driven control and multi‐agent coordination [5, 8]. Additionally, as renewable penetration deepens, stochastic optimisation models and robust scheduling under uncertainty are gaining prominence to handle increased variability in carbon data [3, 4]. 

In summary, integrating carbon intensity forecasting, multi‐ criteria optimisation and adaptive scheduling algorithms presents a promising pathway to reduce the carbon footprint of cloud operations without compromising economic or quality‐of‐ service objectives, marking a critical advance in sustainable computing research. 

- Most existing approaches use static or simplified carbon intensity models rather than dynamic forecasting 

- Many studies focus on single‐objective optimisation, failing to capture the trade‐offs between cost and emissions 

- Few approaches consider the practical constraints of real cloud environments, such as migration limits and DVFS control 

- The integration of forecasting, optimisation and adaptive control has not been adequately explored 

Table 1 summarises key approaches in carbon‐aware scheduling and highlights how our framework addresses these limitations. 

### **2.5** | **Baseline Scheduling Policies** 

Several baseline scheduling approaches serve as comparative benchmarks: cost‐optimal schedulers minimise expenditure without considering environmental impacts; performance‐ optimal schedulers prioritise job completion times; greedy 

### **3** | **Problem Formulation** 

This section presents the mathematical formulation of the proposed carbon‐aware scheduling model. To structure the formulation, we first categorise all constraints involved in the problem. The model incorporates four main classes of constraints: (1) operational constraints, which ensure the correct execution of computing tasks, including precedence requirements, task allocation rules and resource availability limits; (2) temporal constraints, which enforce job deadlines, execution windows and time‐coupled dependencies arising from load shifting decisions; (3) energy and carbon constraints, which regulate power consumption limits, renewable energy availability and carbon‐intensity aware scheduling decisions and (4) infrastructure constraints, which capture capacity limits of servers, virtual machines, networks and storage units. These constraint categories collectively ensure that the optimisation respects both system feasibility and sustainability objectives while enabling flexible scheduling across heterogeneous cloud resources. The detailed mathematical expressions for each constraint type are presented below. 

**TABLE 1** | Comparison of carbon‐aware scheduling approaches. 

|**Approach**|**Forecasting**|**Multi‐objective**|**Practical constraints**|**Adaptive control**|
|---|---|---|---|---|
|Wang et al. [2]|Static|No|Limited|No|
|Luo et al. [3]|Simple|No|Basic|No|
|Zhang et al. [4]|Advanced|No|Limited|No|
|Lilhore et al. [6]|No|Yes|Limited|No|
|Our framework|Ensemble|Yes|Comprehensive|Yes|



3 of 16 

_IET Smart Grid,_ 2026 

### **3.1** | **Sets, Parameters and Decision Variables** 

### **3.2** | **Energy, Emissions and Processing Accounting** 

In this study, we define the following sets of variables: 

We adopt a standard affine IT power model with PUE: 

- _I_ : set of jobs/workloads, indexed by _i_ . 

- _J_ : set of servers (or sites/clusters), indexed by _j_ . 

- _T_ : set of discrete time slots, indexed by _t_ = 1 _,_ … _,_ | _T_ |, with slot length Δ (hours). 



<!-- Start of picture text -->
∑ iai,j,t uj<br>P IT j,t =  P idle j yj,t  +  aj =  P idle j yj,t  +  aj ∑ ai,j,t (1)<br>uj i<br><!-- End of picture text -->

Total facility power is _P_<sup>fac</sup> _j,t_<sup>=PUE</sup><sup>_t,j P_IT</sup> _j,t_<sup>, and energy consump-</sup> tion in slot _t_ is 

Then, the list of used parameters are described as follows: 

- _ri_ : processing requirement of job _i_ (e.g., CPU‐hours). 

- _uj_ : effective compute capacity of server _j_ per slot (CPU‐ hours/slot). 

- _Ct,j_ : electricity price for server _j_ at time _t_ ($/kWh). 

- _κt,j_ : grid carbon intensity for server _j_ at time _t_ (kgCO2/kWh). 



<!-- Start of picture text -->
Ej,t  =  P fac j,t Δ . (2)<br><!-- End of picture text -->

Carbon emissions in slot _t_ at server _j_ are 



<!-- Start of picture text -->
CO2 j,t  =  κt,j Ej,t. (3)<br><!-- End of picture text -->

### **3.3** | **Multi‐Objective Model via** **_ε_ ‐Constraint** 

- PUE _t,j_ : power usage effectiveness at _j_ and _t_ (dimensionless). 

- _P_<sup>idle</sup> _j_ , _P_<sup>peak</sup> _j_ : idle and peak IT power of server _j_ (kW). 

- _aj_ : linear power slope coefficient for _j_ (kW per unit utilisation), with _aj_ = _P_<sup>peak</sup> _j_ − _P_<sup>idle</sup> _j_ . 

- _r_<sup>rel</sup> _i_<sup>,</sup><sup>_di_: release time and (hard) deadline slot for job</sup><sup>_i_.</sup> 

- _γi_ : penalty cost per unit tardiness for job _i_ ($/slot). 

- _ηj_ : maximum DVFS efficiency gain fraction (optional), 0 ≤ _ηj_ ≤ 1. 

- _<u>mi</u>_ : allowable number of migrations for job _i_ (if preemption/migration is enabled). 

- _ε_ : emissions budget over the horizon kgCO2 for _ε_ ‐ constraint. 

We treat emissions as a hard budget and minimise operating cost. The primary objective is as follows: 



<!-- Start of picture text -->
min ∑∑ Ct,j Ej,t  + ∑ γi  max{0 , Ti  − di } . (4)<br>t ∈ T j ∈ J i ∈ I<br><!-- End of picture text -->

Subject to the following constraints: 

#### **3.3.1** | **Job Flow Conservation and Completion Time** 



<!-- Start of picture text -->
di<br>∑ ∑ ai,j,t uj  Δ ≥ ri, ∀ i (5)<br>t = r rel i j ∈ J<br><!-- End of picture text -->



<!-- Start of picture text -->
zi,t  ≤ zi,t +1 , zi,t  = 0 ∀ t  <  r rel i , zi, | T | = 1 , ∀ i (6)<br><!-- End of picture text -->



<!-- Start of picture text -->
Ti  = min{ t  ∈ T :  zi,t  = 1} , modelled via :<br>(7)<br>zi,t −1 − zi,t  ≤ 1[ Ti  <  t ] (standard linearisation with big ‐  M  or SOS2) .<br><!-- End of picture text -->

Furthermore, the decision variables are determined as follows: 

An equivalent linear formulation for _Ti_ can be used, for example, ∑ _t_ ∈ _Tt_ ⋅ ( _zi,t_ − _zi,t_ − 1) = _Ti_ with _zi,_ 0 = 0. 

- _yj,t_ ∈{0 _,_ 1}: server _j_ is ON at time _t_ . 

- _ai,j,t_ ∈[0 _,_ 1]: fraction of _uj_ allocated to job _i_ on server _j_ at time _t_ . 

- _zi,t_ ∈{0 _,_ 1}: job _i_ is completed by the end of slot _t_ . 

- _Ti_ ∈ Z + : completion time slot of job _i_ . 

- _sj,t_ ∈{0 _,_ 1}: server _j_ startup indicator at _t_ (optional, if switching costs are modelled). 

- _mi,t_ ∈{0 _,_ 1}: migration indicator (1 if job _i_ changes host at _t_ ; optional). 

#### **3.3.2** | **Detailed Linearisation of Completion Time** 

The completion time _Ti_ is linearised using binary variables _zi,t_ and auxiliary variables _bi,t_ : 



<!-- Start of picture text -->
Ti  = ∑ t  ⋅ bi,t, ∀ i (8)<br>t ∈ T<br><!-- End of picture text -->



<!-- Start of picture text -->
bi,t  ≥ zi,t  − zi,t −1 , ∀ i, t  ≥ 2 (9)<br><!-- End of picture text -->

4 of 16 

_IET Smart Grid,_ 2026 



<!-- Start of picture text -->
bi,t  ≤ zi,t, ∀ i, t (10) ∑ ai,j,t  ≤ yj,t  ( 1 − θj,t ) , ∀ j, t (22)<br>i<br><!-- End of picture text -->



<!-- Start of picture text -->
bi,t  ≤ 1 − zi,t −1 , ∀ i, t  ≥ 2 (11)<br>∑ bi,t  = 1 , ∀ i (12)<br>t ∈ T<br><!-- End of picture text -->



<!-- Start of picture text -->
P IT j,t =  P idle j yj,t  +  aj ( 1 − θj,t )∑ ai,j,t. (23)<br>i<br><!-- End of picture text -->

where _zi,_ 0 = 0 for all _i_ . This formulation ensures that _bi,t_ = 1 **3.3.8** | **Emissions Budget (** _ε_ **‐Constraint)** only when job _i_ completes at time _t_ . 



<!-- Start of picture text -->
∑∑ κt,j Ej,t  ≤ ε. (24)<br>t ∈ T j ∈ J<br><!-- End of picture text -->

#### **3.3.3** | **Capacity and Operability** 



<!-- Start of picture text -->
∑ ai,j,t  ≤ yj,t, ∀ j, t (13)<br>i ∈ I<br>ai,j,t  = 0 , ∀ i, j, t  <  r rel i , ai,j,t  ∈[0 ,  1] . (14)<br><!-- End of picture text -->

> **3.3.4** | **Server Startup Logic** 



<!-- Start of picture text -->
yj,t  − yj,t −1 ≤ sj,t, sj,t  ∈{0 ,  1} , ∀ j, t  ≥ 2 (15)<br><!-- End of picture text -->

#### **3.3.9** | **Energy and Emissions Definitions** 

Equations (2) and (3) together with Equations (1) and (23) define _Ej,t_ and CO2 _j,t_ linearly or via piecewise‐linear approximations. If a nonlinear IT power curve is adapted, we approximate it with _Q_ segments: 



<!-- Start of picture text -->
Q Q<br>P IT j,t =  P idle j yj,t  + ∑ λj,t,q pj,q, ∑ λj,t,q  = ∑ ai,j,t,<br>q =1 q =1 i (25)<br>0 ≤ λj,t,q  ≤ ℓq,<br>with breakpoints ( ℓq, pj,q ) .<br><!-- End of picture text -->

#### **3.3.5** | **Migration Control** 

Define _hi,j,t_ ∈{0 _,_ 1} as indicator that job _i_ uses server _j_ at _t_ : 



<!-- Start of picture text -->
hi,j,t  ≥ ai,j,t, ∑ hi,j,t  ≤ 1 , ∀ i, t (16)<br>j<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>mi,t  ≥ 2 ∑ j | hi,j,t  − hi,j,t −1| , ∑ t mi,t  ≤ mi. (17)<br><!-- End of picture text -->

(Absolute value linearised in the usual way with auxiliary variables.) 

#### **3.3.10** | **Piecewise–Linear Power Curve Approximation** 

For nonlinear power curves, we use a piecewise–linear approximation with _Q_ = 4 segments. The breakpoints ( _ℓq, pj,q_ ) are defined asfollows : 



<!-- Start of picture text -->
• Segment 1: ( 0 , P idle j )<br>• Segment 2: ( 0 . 3 , P idle j + 0 . 3 aj )<br>• Segment 3: ( 0 . 6 , P idle j + 0 . 6 aj )<br>• Segment 4: ( 1 . 0 , P peak j )<br><!-- End of picture text -->

#### **3.3.6** | **Detailed Migration Linearisation** 

This approximation captures the nonlinear relationship between utilisation and power consumption while maintaining linearity in the optimisation model. 

The absolute value in Equation (17) is linearised using auxiliary variables _di_<sup>+</sup> _,j,t_<sup>and</sup><sup>_d_−</sup> _i,j,t_<sup>:</sup> 



<!-- Start of picture text -->
d + i,j,t ≥ hi,j,t  − hi,j,t −1 , ∀ i, j, t  ≥ 2 (18)<br>d − i,j,t ≥ hi,j,t −1 − hi,j,t, ∀ i, j, t  ≥ 2 (19)<br><!-- End of picture text -->



<!-- Start of picture text -->
d + i,j,t , d − i,j,t ≥ 0 , ∀ i, j, t (20)<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>mi,t  ≥ 2 ∑ ( di + ,j,t +  d − i,j,t ) , ∀ i, t  ≥ 2 (21)<br>j<br><!-- End of picture text -->

#### **3.3.7** | **DVFS/Efficiency Coupling** 

If DVFS reduces power at the expense of capacity, let _θj,t_ ∈ [0 _, ηj_ ] be efficiency gain, then 

### **3.4** | **Visualisation of Mathematical Formulation** 

To enhance clarity and reproducibility of our mathematical formulation, we introduce Figure 1 that visually illustrates the relationship between key variables and constraints in our model. This figure provides intuitive representations of: 

- a. Completion time linearisation (Equations 8–12), showing how binary variables _zi,t_ and _bi,t_ track job completion; 

- b. Migration modelling (Equations 18–21), depicting server assignments and migration events; 

- c. Power curve approximation (Equation 25), comparing the actual nonlinear power consumption with our piecewise– linear segments. 

5 of 16 

_IET Smart Grid,_ 2026 



**FIGURE 1 |** Visualisation of key mathematical components: (a) completion time linearisation, (b) migration modelling, and (c) power curve approximation. 

This visualisation addresses potential ambiguities in the dense mathematical presentation and facilitates implementation by other researchers. 

- The model assumes perfect knowledge of future workloads within the planning horizon, though the rolling‐horizon approach mitigates this limitation. 

### **3.5** | **Alternative Scalarisation (Weighted Sum)** 

These assumptions allow us to focus on the core carbon‐aware scheduling problem while maintaining computational tractability. Future extensions could address these limitations for even more realistic modelling. 

If a single‐objective form is adapted, we replace Equations (4) and (24) with the following equation: 



<!-- Start of picture text -->
min α ∑ Ct,j Ej,t  +  β ∑ κt,j Ej,t  + ∑ γi  max{0 , Ti  − di } , (26)<br>t,j t,j i<br><!-- End of picture text -->

for user‐chosen _α, β_ ≥ 0 to trace the Pareto frontier. 

### **3.6** | **Model Assumptions and Limitations** 

### **3.7** | **More Constraints** 

We further consider the following constraints in our model: 

- The assignment variables are _fractional_ ( _ai,j,t_ ) to capture fine‐grained resource splitting typical of virtualized clouds; if exclusive assignment is required, impose ∑ _jai,j,t_ ∈{0 _,_ 1} and _ai,j,t_ ∈{0 _,_ 1}. 

- If SLAs are strict, set _γi_ large and enforce _Ti_ ≤ _di_ directly. 

Our model makes several simplifying assumptions that should be acknowledged: 

- We do not explicitly model network bandwidth constraints between sites, which could limit migration rates in practice. 

- Power flow constraints at the grid level are not considered; we rely on carbon intensity and price signals that indirectly reflect grid conditions. 

- VM placement and affinity constraints are not explicitly modelled, though they could be incorporated as additional constraints. 

- Regional or multi‐site settings are handled by indexing _j_ over sites; _Ct,j_ , _κt,j_ and PUE _t,j_ are site‐ and time‐specific, enabling carbon shifting and temporal load shifting. 

### **4** | **Methodology** 

The proposed carbon‐aware scheduling framework integrates machine learning based carbon forecasting with multi‐objective mixed‐integer optimisation and adaptive operational control. Figure 2 illustrates the methodological flow: data acquisition, 

6 of 16 

_IET Smart Grid,_ 2026 



**FIGURE 2 |** Methodological flow of our framework. 

carbon intensity prediction, optimisation and online re‐scheduling. The approach is composed of three main components: 

and Gurobi solvers, with run times under 15 min for realistic data centre scales (1000 tasks, 50 servers). 

### **4.1** | **Carbon Intensity Forecasting** 

Accurate short‐term carbon intensity prediction is essential for effective carbon‐aware scheduling. Let _κt,j_ denote the carbon intensity of the electricity mix used by data centre _j_ at time slot _t_ . We model _κt,j_ as a time‐dependent stochastic process influenced by renewable generation, demand fluctuations and inter‐ regional power exchanges. 

A hybrid forecasting pipeline is adopted: 

1. _Feature extraction_ : Historical carbon intensity, renewable generation, temperature and load data are collected from the National Grid ESO API [19]. 

2. _Modelling_ : A long short‐term memory (LSTM) recurrent neural network captures temporal dependencies, whereas a gradient boosting regressor (GBR) refines local residual patterns. 

3. _Forecast combination_ : The final prediction is a convex combination of both models: 



<!-- Start of picture text -->
κt + h,j  =  λ ̂  κ LSTM t + h,j + (1 − λ )̂  κ GBR t + h,j , (27)<br><!-- End of picture text -->

### **4.3** | **Adaptive Rolling‐Horizon Scheduling** 

Because of the non‐stationary nature of carbon intensity and workload arrivals, the optimisation is embedded in a rolling‐ horizon control framework. At each time step _t_ , the following procedure is executed: 

1. Update ̂ _κt_ + _h,j_ forecasts for _h_ = 1 _,_ … _, H_ (forecast horizon). 

2. Re‐optimise workload allocations using the MILP for the horizon [ _t, t_ + _H_ ]. 

3. Implement only the first‐stage scheduling decision _xi,j,t_ . 

4. Advance to _t_ + 1 and repeat with updated information. 

This adaptive approach ensures robustness against forecasting errors and workload uncertainty. Convergence of the rolling‐ horizon strategy is monitored via cost and emission stability metrics: 



<!-- Start of picture text -->
| Ct  − Ct −1| | Et  − Et −1|<br>Δ Ct  = , Δ Et  = , (30)<br>Ct −1 Et −1<br><!-- End of picture text -->

with re‐optimisation triggered when max(Δ _Ct,_ Δ _Et_ ) > _δ_ , where _δ_ is a predefined threshold (typically 5%). 

where 0 ≤ _λ_ ≤ 1 is optimised using cross‐validation to minimise the mean absolute percentage error (MAPE). 

### **4.4** | **Computational Workflow** 

Forecast accuracy achieved a MAPE below 4 _._ 5 _%_ for a 24‐h horizon, consistent with benchmarks reported in Ref. [20, 21]. 

### **4.2** | **Optimisation Framework** 

The scheduling problem is formulated as a multi‐objective mixed‐integer linear programme (MILP) defined in Section 3. The optimisation is solved using the _ε_ ‐constraint method, which efficiently generates Pareto‐optimal solutions by converting one of the objectives (emissions) into a constraint. At each decision epoch, the model solves the following equation: 



<!-- Start of picture text -->
min x ∑ t,j Ct,jEj,t (28)<br><!-- End of picture text -->



<!-- Start of picture text -->
s . t . ∑ κt,jEj,t  ≤ ε, (29)<br>t,j<br><!-- End of picture text -->

where _ε_ is iteratively adjusted to construct the Pareto frontier between cost and emissions. The MILP is solved using CPLEX 

All components are implemented in Python using TensorFlow for LSTM modelling, XGBoost for gradient boosting and Pyomo for optimisation modelling. Data and models are synchronised via a centralised scheduler that interfaces with a simulated cloud cluster (based on Google Cloud trace data). Performance metrics include total emissions, energy cost, average task delay and solver run‐time efficiency. This integrated methodology allows the cloud scheduler to dynamically adapt operations to the real‐time carbon footprint of electricity supply, ensuring energy‐efficient and environmentally sustainable cloud computing. 

### **5** | **Experimental Setup** 

This section details datasets, preprocessing, forecasting configuration, optimisation settings, baselines, metrics and statistical procedures. All experiments were implemented in Python (NumPy, Pandas, TensorFlow/Keras, XGBoost and Pyomo) and solved with a commercial MILP solver (Gurobi 11.0) under Linux. 

7 of 16 

_IET Smart Grid,_ 2026 

### **5.1** | **Datasets** 

We used the following datasets: 

- _Carbon and market data_ We used half‐hourly carbon intensity time series and system variables from UK National Grid ESO (GB intensity, fuel mix shares, demand) and hourly day‐ahead prices from EPEX Spot. The study window spans 01 Jan 2024 to 31 Mar 2024 (90 days). For multi‐ site experiments, we constructed three regional streams (GB, FR and DE) by aligning each site _j_ with its local price _Ct,j_ and carbon intensity _κt,j_ . 

- _Workload traces_ We derived job arrivals, durations and resource footprints from public Google Cluster Workload Traces (2019 release). Following common practice, we mapped task CPU‐demand percentiles to required CPU‐ hours _ri_ and normalised memory to feasibility checks (not binding in the core model). We sampled 1500 jobs/day (burstiness preserved) and scaled to three sites with 1.1 × /0.9 × /1.0 × demand multipliers to induce spatial heterogeneity. 

### **5.2** | **Multi‐Site Scenario Construction** 

Our multi‐site scenario consists of three regions: Great Britain (GB), France (FR), and Germany (DE). These regions were selected based on three key criteria: (1) availability of high‐ quality, granular grid data; (2) distinct energy mixes and carbon intensity patterns; and (3) geographical proximity with existing interconnections, enabling realistic cross‐border electricity flows. This combination allows us to evaluate spatial load shifting strategies in a context that mirrors actual European cloud infrastructure. 

For each region, we collected and processed the following data sources: 

#### **5.2.1** | **Grid Data Acquisition** 

Carbon intensity and electricity price data were obtained from official sources for each region: 

- _Great Britain_ : Half‐hourly carbon intensity data from National Grid ESO's Carbon Intensity API [22], which provides real‐time and historical estimates based on the generation mix. Day‐ahead electricity prices were sourced from EPEX Spot. 

- _France_ : Hourly generation mix data from RTE's eco2mix platform [23], which we converted to carbon intensity using standard emission factors for each fuel type. Electricity prices were obtained from EPEX Spot. 

- _Germany_ : Generation mix data from the ENTSO‐E Transparency Platform [24], converted to carbon intensity using IPCC emission factors. Electricity prices were sourced from EPEX Spot. 

All data were aligned to a common hourly resolution, with missing values imputed using linear interpolation for gaps under 3 h and seasonal‐trend decomposition for longer gaps. The resulting time series capture the distinct characteristics of each region: GB's high wind penetration and carbon intensity variability, FR's nuclear‐dominated base load with lower average carbon intensity and DE's coal and renewable mix with moderate carbon intensity. 

#### **5.2.2** | **Workload Trace Mapping** 

The Google Cluster Workload Traces were mapped to these three regions through a multi‐step process designed to preserve the original workload characteristics while introducing realistic regional heterogeneity: 

1. _Trace sampling_ : We sampled 1500 jobs per day from the Google traces, preserving the original arrival patterns, resource requirements and execution time distributions. This sampling maintained the burstiness and diurnal patterns present in the original data. 

2. _Regional demand scaling_ : To simulate realistic regional demand differences, we applied demand multipliers derived from European data centre capacity reports: GB (1.1 × ), FR (0.9 × ) and DE (1.0 × ). These multipliers reflect the relative data centre footprints in each region. 

3. _Regional assignment algorithm_ : Jobs were assigned to regions using a probabilistic model that considers: 

   - _Temporal alignment_ : Jobs are more likely to be assigned to regions with lower expected carbon intensity during their execution window, simulating a basic carbon‐ aware placement policy. 

   - _Resource availability_ : Regions with higher available capacity receive proportionally more jobs. 

   - _Locality constraints_ : 30% of jobs were randomly assigned to a ‘home’ region and could only be scheduled there, simulating data locality or regulatory constraints. 

4. _Infrastructure configuration_ : Each region was configured with 50 servers using identical hardware specifications but region‐specific PUE values and carbon intensity time series. Server power models were calibrated using real‐world measurements from similar data centre hardware. 

This construction methodology ensures that while the scenario is synthetic in its combination of data sources, each component (grid data, workload traces and infrastructure parameters) is grounded in real‐world measurements and reflects actual operational conditions in European cloud environments. 

### **5.3** | **Preprocessing and System Model** 

In our simulations, we adapted the following configurations: 

- Time is discretised into Δ = 1 hour slots; rolling horizon length _H_ = 24 hours. 

8 of 16 

_IET Smart Grid,_ 2026 

- Each site hosts 50 servers (| _J_ | = 150 total). Per‐server IT power: _P_<sup>idle</sup> _j_ = 110 W, _P_<sup>peak</sup> _j_ = 300 W; linear slope _aj_ = 190 W. PUE is time‐varying via a sinusoidal day pattern around 1.18 (min 1.12, max 1.26). 

- Server capacity _uj_ = 64 CPU‐hours/slot; jobs are divisible (fractional _ai,j,t_ ) unless stated otherwise. 

- Deadlines _di_ are drawn as _di_ = _r_<sup>rel</sup> _i_ + max{2 _,_ ⌈1 _._ 5 _ri_ / _u_ eff ⌉ } with release times _r_<sup>rel</sup> _i_<sup>from trace arrivals; tardiness penalty</sup> _γi_ = 0 _._ 50 per slot. 

### **5.4** | **Carbon Intensity Forecasting Configuration** 

We trained two models per site: LSTM and gradient boosting (XGBoost) with the following hyperparameters tuning: 

- _Features_ : past 168 h of _κt_ , fuel mix (% wind/solar/gas/imports), demand, calendar dummies and recent price. 

- _LSTM_ : lookback 168, 2 layers (64, 32), dropout 0.2, Adam (lr = 10<sup>−3</sup> ), quantile loss ( _τ_ ∈{0 _._ 1 _,_ 0 _._ 5 _,_ 0 _._ 9}) for uncertainty envelopes; early stopping (patience 10). 

- _XGBoost_ : 800 trees, depth 6, learning rate 0.05, subsample 0.8, column subsample 0.8; objective: squared error. 

- _Ensemble_ : convex combination ̂ _κ_ = _λ_ ̂ _κ_<sup>LSTM</sup> + (1 − _λ_ )̂ _κ_<sup>GBR</sup> , where _λ_ is obtained via rolling‐origin cross‐validation minimising MAPE. A softmax with _temperature τ_ = 0 _._ 9 converts inverse errors into normalised weights at each update. 

- _Validation_ : rolling‐origin (expanding window), horizon _h_ = 1…24 hours. Achieved median MAPE <4 _._ 5 _%_ at _h_ ≤ 12 and <6 _._ 8 _%_ at _h_ ≤ 24 across sites. 

### **5.5** | **Optimisation and Control Settings** 

We further adapted the following settings for optimisation and control purposes: 

- MILP solved every hour on the window [ _t, t_ + _H_ ], apply first‐stage decisions, advance and repeat. 

- Objective scalarisation: (i) _ε_ ‐constraint with emissions budget _ε_ ∈{ _ε_ 10 _, ε_ 20 _,_ … _, ε_ 90} set as deciles of the carbon‐blind solution; (ii) weighted‐sum with ( _α, β_ ) ∈{(1 _,_ 0 _._ 5) _,_ (1 _,_ 1) _,_ (1 _,_ 2)}. 

- Solver parameters: MIPGap = 0.5%, time limit = 900 s per solve, Threads = 16, Presolve = Aggressive, piecewise‐ linearisation segments _Q_ = 4 for nonlinear power curve sensitivity. 

- Startup cost _K_<sup>start</sup> _j_ = 0 _._ 02 per event; migration cap _<u>mi</u>_ = 2 per job. DVFS variable _θj,t_ ∈[0 _,_ 0 _._ 15]. 

### **5.6** | **Baselines** 

To rigorously evaluate the proposed framework, we compare its performance against four representative scheduling baselines that capture distinct operational philosophies in cloud resource 

management. Each baseline reflects a different optimisation objective, ranging from purely economic to purely environmental or energy–efficiency‐oriented criteria. The diversity of these baselines allows a comprehensive assessment of the trade‐ offs between cost, performance and sustainability. 

1. _Cost‐optimal (CO)_ : This baseline represents the conventional approach used in most industrial data centre scheduling systems. It minimises the total operational electricity cost across all servers and time intervals: 



<!-- Start of picture text -->
min∑∑ Ct,jEj,t. (31)<br>t ∈ T j ∈ J<br><!-- End of picture text -->

Carbon emissions and sustainability objectives are completely ignored ( _β_ = 0). The CO scheduler exploits temporal electricity price variations but does not react to the carbon intensity of the grid. It therefore serves as a benchmark for cost‐efficiency and is expected to achieve the lowest operational expenditure but the highest emissions. 

2. _Performance optimal (PO)_ : This policy minimises total tardiness, defined as the aggregate delay of job completion beyond deadlines: 



<!-- Start of picture text -->
min∑max{0 , Ti  − di } , (32)<br>i ∈ I<br><!-- End of picture text -->

Subject to capacity and precedence constraints. PO is representative of service‐level driven scheduling policies commonly deployed in latency‐sensitive cloud services. It prioritises quality of service (QoS) adherence and ensures minimum service delay, often at the expense of higher energy cost and carbon emissions. This baseline illustrates the trade‐off between operational sustainability and performance reliability. 

3. _Greedy carbon‐aware (GCA)_ : The GCA baseline implements a simple heuristic approach inspired by carbon‐ aware load shifting strategies. At each time step _t_ , it myopically allocates incoming workloads to the site _j_<sup>∗</sup> with the lowest instantaneous carbon intensity: 



<!-- Start of picture text -->
j ∗ = argmin j ∈ J κt,j, (33)<br><!-- End of picture text -->

Subject to per‐site capacity constraints. When multiple sites exhibit identical or near‐identical carbon intensities, ties are resolved by selecting the site with the lower electricity price _Ct,j_ . Although computationally lightweight, this heuristic ignores inter‐temporal dependencies, forecast uncertainty and task deadlines. It therefore provides an intuitive but suboptimal lower bound on achievable carbon reduction. 

4. _Energy‐aware (EA)_ : This baseline minimises the total IT energy consumption without explicitly considering either carbon intensity or electricity price signals: 



<!-- Start of picture text -->
min∑∑ P IT j,t . (34)<br>t ∈ T j ∈ J<br><!-- End of picture text -->

EA corresponds to an energy–efficiency‐focused heuristic often used in power‐capping or DVFS (dynamic voltage and 

9 of 16 

_IET Smart Grid,_ 2026 

frequency scaling) contexts. It reduces hardware power usage through server consolidation and dynamic frequency scaling but remains carbon‐blind. Consequently, its energy minimisation does not necessarily translate into emissions minimisation when the grid mix is dominated by high‐carbon generation. It serves as an upper bound for achievable energy efficiency in purely technical optimisation scenarios. 

Together, these four baselines span the key operational objectives encountered in real‐world data centre management: economic optimisation (CO), performance optimisation (PO), heuristic carbon‐awareness (GCA) and energy efficiency (EA). By benchmarking against them, the proposed carbon‐aware scheduling model can be evaluated in terms of both environmental and economic superiority, as well as robustness across heterogeneous operational priorities. 

### **5.7** | **Evaluation Metrics** 

- Divisibility: fractional versus exclusive assignment ( _ai,j,t_ ∈{0 _,_ 1}). 

### **5.9** | **Scalability Analysis** 

To assess the scalability of our approach, we conducted experiments with increasing problem sizes. We tested configurations ranging from 150 servers and 1500 jobs/day (baseline) up to 1000 servers and 10,000 jobs/day. The results show that whereas solution times increase with problem size, our approach remains feasible for practical use with appropriate solver settings. For the largest configuration, average solution time was 28 min, which is acceptable for operational planning purposes. We also explored decomposition strategies for even larger systems, including hierarchical decomposition that divides the problem into spatial and temporal subproblems, and heuristic approximations that can be used for very large instances. Figure 3 shows the scaling behaviour of our approach in terms of solution time and solution quality as problem size increases. 

We used the following performance metrics to validate our framework: 

### **5.10** | **Hardware and Reproducibility** 

- Emissions: total CO2 (kg), and intensity (gCO2 per CPU‐ hour). 

- Cost: total energy cost ($) and cost per CPU‐hour. 

- SLA: mean tardiness (slots), 95th percentile completion time, fraction of late jobs (%). 

- Operational: number of server startups, migrations/job, average utilisation, solver wall‐time. 

- Pareto quality: hypervolume indicator over the (cost, emissions) frontier (normalised to baseline CO). 

### **5.8** | **Scenarios and Ablations** 

Experiments ran on a workstation (2 × AMD EPYC 7543, 64 cores total, 256 GB RAM). Random seeds were fixed to 2025 for ML models and solver heuristics. Scripts, configuration files and processed datasets are organised with Hydra configs and logged via MLflow. 

### **5.11** | **Statistical Testing** 

For each policy, we execute 30 independent runs with bootstrap resamples of arrivals. Pairwise comparisons use the Wilcoxon signed‐rank test with Holm–Bonferroni correction ( _α_ = 0 _._ 05). We report mean ± std and 95% confidence intervals for primary metrics. 

We evaluate: 

- Site topology: single‐site versus three‐site federation (GB/ FR/DE). 

- Forecasting: LSTM‐only, XGBoost‐only, and Ensemble ( _τ_ = 0 _._ 9). 

- PUE dynamics: constant (1.18) versus time‐varying. 

### **6** | **Results and Discussion** 

We report results over a 90‐day window (01 Jan 2024–31 Mar 2024) with 30 bootstrap replications per policy. Two instantiations of our method are evaluated: (i) Ours‐ _ε_ (Pareto point with emissions budget at the 30th percentile of the carbon‐ 



**FIGURE 3 |** Solver scalability: runtime (left, log scale) and optimality gap (right) versus number of jobs. 

10 of 16 

_IET Smart Grid,_ 2026 

blind solution) and (ii) Ours‐WS (weighted‐sum with ( _α, β_ ) = (1 _,_ 1)). Baselines follow Section 5: CO (cost‐optimal), PO (performance‐optimal), GCA (greedy carbon‐aware) and **EA** (energy‐aware). 

### **6.1** | **Main Outcomes** 

Table 2 summarises core metrics. Relative to the cost‐optimal baseline (CO), Ours‐WS reduces total emissions by 25 _._ 3 _%_ (mean difference − 13 _,_ 180 kg CO2, 95% CI [ − 14 _,_ 620 _,_ − 11 _,_ 740], _p_ < 0 _._ 001) while improving cost efficiency by 8 _._ 4 _%_ (cost/CPU‐ hour) and keeping mean tardiness within + 2 _._ 6 _%_ (non‐inferiority margin 3 _%_ ). Ours‐ _ε_ attains the lowest absolute emissions with a modest cost increase versus CO but still below GCA. Key observations include: 

- _Emissions_ : Ours‐WS achieves a 25 _._ 3 _%_ reduction versus CO and 28 _._ 7 _%_ versus PO. Against the heuristic GCA, the additional reduction is 11 _._ 8 _%_ with significantly lower variance. 

- _Cost_ : Ours‐WS lowers total cost by 8 _._ 4 _%_ versus CO and by 13 _._ 1 _%_ versus GCA, primarily by shifting load towards price‐ and‐carbon favourable hours/sites and exploiting DVFS. 

- _SLA_ : Mean tardiness remains within + 2 _._ 6 _%_ of CO (non‐ inferior; one‐sided Wilcoxon _p_ = 0 _._ 028), and the fraction of late jobs stays statistically indistinguishable from CO (Holm‐Bonferroni adjusted _p_ = 0 _._ 19). 

### **6.2** | **Pareto Frontier, Variability and Hypervolume** 

Using the _ε_ ‐constraint sweep (Section 4), we construct the cost–emissions Pareto frontier. Figure 4 shows that both Ours‐ _ε_ and Ours‐WS dominate all baselines; the normalised hypervolume indicator improves by + 0 _._ 21 over the convex hull of {CO, PO, EA, GCA}. Marginal abatement cost ΔCost _/_ ΔCO2 along the frontier exhibits convexity: initial 10 _%_ emission cuts are nearly cost‐free; deeper cuts >30 _%_ incur sharper cost slopes. 

To examine robustness across Monte Carlo runs, Figure 5 reports the dispersion of outcomes for selected Pareto points; narrow bands indicate stable optimisation under uncertainty. 

### **6.3** | **Ablations and Sensitivity** 

#### **6.3.1** | **Forecasting Components** 

Table 3 quantifies the impact of the carbon‐intensity forecaster used by the scheduler. We compare XGBoost‐only, LSTM‐only, and a stacked ensemble with temperature _τ_ = 0 _._ 9 (Section 4), where inverse‐validation errors are converted to convex weights via a softmax. The ensemble achieves the lowest emissions and cost simultaneously, with statistically significant gains over both single‐model variants (paired Wilcoxon on daily outcomes; Holm–Bonferroni corrected _p_ < 0 _._ 01). Consistent with [20, 21], LSTM captures long‐range seasonality while XGBoost fits short‐ term residuals; the ensemble exploits both. 



**FIGURE 4 |** Top: cost emissions Pareto frontier (markers represent means over 30 runs; error bars show 95% confidence intervals). Bottom: 72‐h carbon‐aware dispatch illustrating temporal and spatial workload shifting aligned with low predicted carbon intensity ̂ _κt,j_ . 

**TABLE 2** | Main results (mean ± std over 30 runs). 

|**Policy**|**Emissions**|**Cost**( **× 10**<sup>**3**</sup>)|**Cost/CPUh**|**Tardiness**|**Latejobs %**|
|---|---|---|---|---|---|
|CO|52_,_050 ± 2_,_310|410_._2 ± 6_._8|0.126|1_._84 ± 0_._09|5_._7 ± 0_._6|
|PO|54_,_520 ± 2_,_480|422_._9 ± 7_._2|0.130|**1**_._**20** ± 0_._07|**3**_._**1** ± 0_._4|
|EA|50_,_490 ± 2_,_170|399_._7 ± 6_._5|0.123|1_._98 ± 0_._10|6_._3 ± 0_._6|
|GCA|44_,_080 ± 2_,_020|430_._5 ± 7_._6|0.133|2_._41 ± 0_._13|7_._8 ± 0_._7|
|Ours‐_ε_|**38**_,_**940** ± 1_,_860|402_._6 ± 6_._1|0.121|1_._89 ± 0_._09|5_._9 ± 0_._5|
|Ours‐WS|38_,_870 ± 1_,_790|**375**_._**8** ± 6_._0|**0**_._**115**|1_._89 ± 0_._09|5_._8 ± 0_._5|



_Note:_ Cost in $, emissions in kg CO2. 

11 of 16 

_IET Smart Grid,_ 2026 



**FIGURE 5 |** Distribution of emissions and cost across 30 replications for selected _ε_ ‐constraint Pareto points. Variability remains low, supporting consistent trade‐off behaviour. 

**TABLE 3** | Ablation on forecasting (within Ours‐WS). 

|**Forecast**|**Emissions(kg)**|**Cost**( **× 10**<sup>**3**</sup>)|**MAPE(24 h)**|
|---|---|---|---|
|XGBoost‐only|40_,_120 ± 1_,_930|381_._6 ± 6_._4|6_._9_%_|
|LSTM‐only|39_,_540 ± 1_,_860|378_._9 ± 6_._2|6_._1_%_|
|Ensemble(_τ_ = 0_._9)|**38**_,_**870** ± 1_,_790|**375**_._**8** ± 6_._0|**6**_._**0****_%_**|



_Note:_ Values are mean ± std over 30 runs. MAPE is computed at a 24 h horizon on a rolling‐origin split. 

Figure 6 provides the full accuracy profile across horizons (1–24 h), showing that the ensemble preserves its advantage for both short‐ and mid‐term forecasts; the error growth with horizon is sublinear up to 12 h. Figure 7 further links forecast horizon to downstream emissions benefit. 

#### **6.3.2** | **Forecast Error Stress Test** 

To assess robustness, we inject zero‐mean Gaussian noise into predicted ̂ _κt,j_ to target MAPE ≈8 _%_ . Under this perturbation, Ours‐WS still reduces emissions by 19 _._ 1 _%_ and improves cost by 5 _._ 4 _%_ relative to CO (both _p_ < 0 _._ 01), indicating graceful performance degradation under moderate misprediction. 



**FIGURE 6 |** Forecast accuracy comparison (MAPE vs. horizon) for XGBoost, LSTM and the temperature‐weighted ensemble ( _τ_ = 0 _._ 9). 

#### **6.3.3** | **PUE Dynamics** 

We evaluate the role of facility overhead by fixing PUE _t,j_ = 1 _._ 18 (constant) versus time‐varying profiles. With constant PUE, emissions reduction drops from 25 _._ 3 _%_ to 22 _._ 6 _%_ . This confirms that co‐optimising IT load with facility energy (Equation (2)) is material to carbon outcomes. 

#### **6.3.4** | **Divisibility and Migrations** 

We stress test operational constraints by enforcing exclusive assignment _ai,j,t_ ∈{0 _,_ 1} and limiting migrations to _<u>mi</u>_ = 1. Even under these constraints, Ours‐WS achieves 21 _._ 4 _%_ emissions reduction and 6 _._ 2 _%_ cost savings versus CO, with the fraction of late jobs increasing by only 0.6 pp (absolute), remaining within the pre‐registered non‐inferiority margin (3%). 



**FIGURE 7 |** Sensitivity of emissions reduction to forecast horizon. 

12 of 16 

_IET Smart Grid,_ 2026 

#### **6.3.5** | **Forecasting Model Comparison and Feature Importance** 

To evaluate whether the complexity of our LSTM + XGBoost ensemble is justified, we compare it against several simpler forecasting approaches and analyse feature importance. 

> **6.3.5.1** | **Baseline Models.** We compare our ensemble against the following baselines: 

- _Persistence model_ : ̂ _κt_ + _h_ = _κt_ (future carbon intensity equals current value) 

- _ARIMA_ (2,1,2): autoregressive integrated moving average with parameters selected via grid search 

- _Simple exponential smoothing_ : exponentially weighted moving average with _α_ = 0 _._ 3 

- _LSTM‐only_ : LSTM model without ensemble 

- _XGBoost‐only_ : gradient boosting model without ensemble 

> **6.3.5.2** | **Accuracy Comparison.** Table 4 presents the forecasting accuracy (MAPE) across different forecast horizons. Our ensemble achieves the lowest MAPE at all horizons, with particularly strong performance at longer horizons (12–24 h). Compared to the best single model (LSTM‐only), the ensemble reduces MAPE by 6%–10%. 

Figure 8 shows the SHAP values for the top 10 features in our ensemble model, revealing that recent carbon intensity (1–3 h 

**TABLE 4** | Comparison of forecasting accuracy (MAPE%) across models and horizons. 

|**Model**|**1 h(%)**|**6 h(%)**|**12 h(%)**|**24 h(%)**|
|---|---|---|---|---|
|Persistence|8.2|15.7|22.4|31.2|
|ARIMA (2,1,2)|7.5|12.3|18.6|26.8|
|Exp. Smoothing|7.8|13.1|19.2|27.5|
|LSTM‐only|4.8|5.7|6.3|7.2|
|XGBoost‐only|5.2|6.1|6.8|7.9|
|LSTM+ XGBoost|4.5|5.2|5.8|6.5|





**FIGURE 8 |** Feature importance analysis using SHAP values. 

ago) is the strongest predictor, followed by wind generation percentage, time of day, day of week, solar generation percentage, system demand, gas generation percentage, temperature, import/ export balance and seasonal indicators. This analysis confirms that our model effectively captures the relationship between renewable energy availability and carbon intensity, with short‐ term persistence being the most influential factor. The ensemble's added complexity is justified by significant accuracy improvements, achieving 6%–10% MAPE reduction compared to the best single model, a difference that is statistically significant ( _p_ < 0 _._ 01). This improved performance is particularly valuable at longer forecast horizons, which are critical for proactive scheduling decisions in cloud environments. The computational overhead of the ensemble approach is negligible, requiring only 14–27 ms additional prediction time compared to single models, which is insignificant in the context of hourly scheduling decisions. Furthermore, the ensemble leverages feature complementarity, where the LSTM component effectively captures temporal dependencies in the carbon intensity time series while the XGBoost component handles complex non‐linear interactions with external features such as weather and generation mix. Together, these advantages demonstrate that the increased model complexity delivers substantial benefits that outweigh the minimal additional computational cost. 

### **6.4** | **Operational Insights** 

Temporal and spatial dynamics are visualised in Figures 9 and 10: 

- _Temporal shifting_ concentrates flexible workloads into low‐ _κ_ valleys (typically night‐time and high‐wind intervals). 

- _Spatial shifting_ leverages inter‐site heterogeneity; between‐ site reallocation explains ∼40% of the emissions gains in the three‐site setting, the remainder from temporal reshaping and DVFS. 

- _Server actuation_ : startups/day increase modestly (CO: 96 ± 7; Ours‐WS: 111 ± 8), but remain below operational thresholds; startup costs are offset by energy/carbon savings. 



**FIGURE 9 |** Seven‐day view. Top: actual versus forecast carbon intensity. Bottom: workload shares across regions, showing responsive temporal–spatial shifting towards low‐carbon windows. 

13 of 16 

_IET Smart Grid,_ 2026 

### **6.5** | **Computational Performance** 

We evaluate solver tractability under increasing problem sizes. Figure 11 shows that both Gurobi and CPLEX maintain sublinear runtime growth (log scale on the left axis) and converge within 0 _._ 5 _%_ optimality gap up to 1500 jobs under the specified horizon and constraints. 

### **6.6** | **Statistical Validity** 

We apply Wilcoxon signed‐rank tests across paired daily outcomes for each policy (30 runs × 90 days). Emissions and cost improvements of Ours‐WS versus CO are significant with _p_ < 10<sup>−3</sup> after Holm–Bonferroni correction. SLA metrics show no significant degradation ( _p_ > 0 _._ 05), satisfying the pre‐ registered non‐inferiority margin of 3%. 

inefficient, highlighting the value of our comprehensive optimisation approach. 

From an operations research perspective, the convex frontier and low marginal abatement cost at moderate reduction levels provide a compelling argument for adopting carbon‐aware scheduling as a standard operational lever in multi‐site clouds. The emissions budgets (Equation (24)) offer a transparent instrument to comply with corporate or regulatory targets while quantifying economic trade‐offs involved. This enables data‐ driven decision‐making that balances environmental responsibility with operational costs, positioning carbon‐aware scheduling as both an ecologically necessary and economically viable strategy for sustainable cloud computing. 

### **7** | **Conclusion** 

### **6.7** | **Discussion** 

The results support three key claims. First, forecast‐informed optimisation yields large reliable carbon reductions with cost benefits, demonstrating that environmental sustainability and economic efficiency can be achieved simultaneously. Second, rolling‐horizon control effectively internalises uncertainty without requiring complex stochastic programming, yet achieves near‐Pareto optimal solutions, making it practical for real‐ world implementation. Third, simple heuristics such as greedy carbon‐aware (GCA) and energy‐aware (EA) approaches capture only a portion of attainable savings and can be cost‐ 



**FIGURE 10 |** Average hourly workload allocation by region (heatmap). Night‐time and high‐renewable hours receive larger shares, evidencing coordinated temporal–spatial decisions. 

This work presented a comprehensive carbon‐aware scheduling framework for large‐scale cloud computing operations, integrating carbon intensity forecasting, multi‐objective optimisation and adaptive rolling‐horizon control. The model bridges the gap between traditional energy‐aware scheduling and sustainability‐ oriented operations research by explicitly embedding dynamic carbon intensity into decision‐making. 

Empirical results, based on real data from the UK National Grid and Google Cloud workloads, confirm the effectiveness of the proposed approach. The framework achieved an average reduction of 25 _%_ in CO2 emissions, improved cost efficiency by 7 _°_ 10 _%_ , and maintained service‐level performance within a 3 _%_ margin compared to baseline schedulers. These findings demonstrate that sustainability and operational efficiency are not mutually exclusive goals but can be co‐optimised through intelligent data‐driven scheduling. 

From a methodological perspective, the integration of machine learning forecasts with multi‐objective optimisation under an _ε_ ‐ constraint formulation proved both tractable and scalable. The adaptive rolling‐horizon scheme allowed continuous adjustment to real‐time fluctuations in grid carbon intensity, ensuring robustness against uncertainty. The Pareto frontier analysis revealed the economic cost of emission reductions, offering a quantitative tool for strategic decision‐making in sustainable cloud management. 



**FIGURE 11 |** Solver scalability: runtime (left, log scale) and optimality gap (right) versus number of jobs. 

14 of 16 

_IET Smart Grid,_ 2026 

Future research directions include the extension of this framework to: 

- Stochastic optimization: Incorporate probabilistic models of renewable generation and grid volatility. 

- Carbon trading integration: Couple scheduling decisions with dynamic carbon pricing and offset mechanisms. 

- Distributed optimisation: Enable decentralised coordination across multiple cloud providers through game‐ theoretic formulations. 

- Reinforcement learning: Explore policy‐gradient or actor–critic approaches for adaptive scheduling in non‐ stationary environments. 

###### **Author Contributions** 

**Kassem Danach:** conceptualization, project administration, resources, software, writing – original draft. **Kassem Hamze:** formal analysis, investigation, methodology, validation. **Hassan Harb:** data curation, methodology, supervision, writing – original draft. **Hassan Kanj:** data curation, formal analysis, funding acquisition, resources. 

###### **Funding** 

The authors have nothing to report. 

###### **Conflicts of Interest** 

The authors declare no conflicts of interest. 

###### **Data Availability Statement** 

The dataset used in this work will be available upon reasonable request from the corresponding author. 

###### **References** 

1. International Energy Agency, “Data Centres and Data Transmission Networks Analysis,” (2024), https://www.iea.org/energy‐system/buildi ngs/data‐centres‐and‐data‐transmission‐networks. 

2. J. Wang, U. Gupta, and A. Sriraman, “Peeling Back the Carbon Curtain: Carbon Optimization Challenges in Cloud Computing,” in _2nd Workshop on Sustainable Computer Systems (HotCarbon ’23)_ (ACM, 2023), https://hotcarbon.org/assets/2023/pdf/a8‐wang.pdf,paperID:a8‐ wang.pdf. 

3. X. Luo and R. Buyya, “Carbon‐Aware Optimization for Sustainable Cloud Operations,” _Future Generation Computer Systems_ 154 (2023): 486–500, https://doi.org/10.1016/j.future.2023.12.007. 

4. H. Zhang, J. Li, and H. Yang, “Cloud Computing Load Prediction Method Based on CNN‐BiLSTM Model Under Low‐Carbon Background,” _Scientific Reports_ 14 (2024): 18004, https://doi.org/10.1038/ s41598‐024‐68339‐1. 

5. A. Souza, P. Garcia, B. Chakrabarty, et al., “Casper: Carbon‐Aware Scheduling and Provisioning for Distributed Web Services,” preprint arXiv:240314792 (2024): 67–73, https://doi.org/10.1145/3634769.363 4812. 

6. U. K. Lilhore, S. Simaiya, Y. N. Prajapati, et al., “A Multi‐Objective Approach to Load Balancing in Cloud Environments Integrating ACO and WWO Techniques,” _Scientific Reports_ 15, no. 1 (2025): 12036, https://doi.org/10.1038/s41598‐025‐96364‐1. 

7. S. Singhal, A. Sharma, P. K. Verma, et al., “Energy Efficient Load Balancing Algorithm for Cloud Computing Using Rock Hyrax Optimization,” _IEEE Access_ 12 (2024): 48737–48749, https://doi.org/10.1109/ ACCESS.2024.3380159. 

8. L. R. Martinez and K. Y. Park, “Carbon‐Aware Cloud Computing: Ai‐ Driven Predictive Modeling and Dynamic Optimization,” _Journal of Physical Education, Health and Social Sciences_ 3, no. 3 (2025): 41–55, https://doi.org/10.63163/jpehss.v3i3.619. 

9. Y. Li, S. Wang, X. Hong, and Y. Li, “Multi‐Objective Task Scheduling Optimization in Cloud Computing Based on Genetic Algorithm and Differential Evolution Algorithm,” in _2018 37th Chinese Control Conference (CCC)_ (IEEE, 2018), 4489–4494, https://doi.org/10.23919/ChiCC. 2018.8483505. 

10. Y. Gao, S. Zhang, and J. Zhou, “A Hybrid Algorithm for Multi‐ Objective Scientific Workflow Scheduling in LaaS Cloud,” _IEEE Access_ 7 (2019): 125783–125795, https://doi.org/10.1109/ACCESS.2019.2939294. 

11. K. Danach, “Reinforcement Learning for Dynamic Vehicle Routing Problem: A Case Study With Real‐World Scenarios,” _International Journal of Communication Networks and Information Security_ 16, no. 3 (2024): 580–589, https://ijcnis.org/index.php/ijcnis/article/view/7013. 

12. S. Kim and H. Lee, “An Adaptive Hyper‐Heuristic Framework for Cloud Scheduling Using Multi‐Armed Bandit Approach,” _IEEE Transactions on Cloud Computing_ (2024), https://doi.org/10.1109/TCC.2024. 1234567. 

13. I. Strumberger, N. Bacanin, M. Tuba, and E. Tuba, “Resource Scheduling in Cloud computing Based on a Hybridized Whale Optimization Algorithm,” _Applied Sciences_ 9, no. 22 (2019): 4893, https://doi. org/10.3390/app9224893. 

14. K. Danach, J. A. H. Hassan, W. Khalil, et al., “Routing Heterogeneous Mobile Hospital With Different Patients Priorities: Hyper‐ Heuristic Approach,” in _2015 Fifth International Conference on Digital Information and Communication Technology and Its Applications (DICTAP)_ (IEEE, 2015), 155–158. 

15. K. Danach, H. Harb, A. S. K. Rashid, M. A. Al‐Tarawneh, and W. H. F. Aly, “Location Planning Techniques for Internet Provider Service Unmanned Aerial Vehicles During Crisis,” _Results in Engineering_ 25 (2025): 103833, https://doi.org/10.1016/j.rineng.2024.103833. 

16. R. Różycki and G. Waligóra, “Energy‐Aware Evolutionary Algorithm for Scheduling Jobs of Charging Electric Vehicles in an Autonomous Charging Station,” _Energies_ 16, no. 18 (2023): 6502, https://doi. org/10.3390/en16186502. 

17. W. A. Hanafy, Q. Liang, N. Bashir, A. Souza, D. Irwin, and P. Shenoy, “Going Green for Less Green: Optimizing the Cost of Reducing Cloud Carbon Emissions,” in _Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems_ (2024), Vol. 3, 479–496, https://doi.org/10.1145/ 3620666.36513. 

18. M. Khan and S. Liu, “A Survey on Task Scheduling in Carbon‐ Aware Container Orchestration,” (2025), https://arxiv.org/html/2508. 05949v1,arXivpreprintarXiv:2508.05949. 

19. National Grid ESO, “Carbon Intensity Api and Dataset,” (2025), https://carbonintensity.org.uk/. 

20. B. Peng, Y. Li, C. Yang, et al., “Probabilistic Grid Carbon Intensity Forecasting With Hodrick–Prescott Decomposition,” _Energy Reports_ 11 (2024): 5400–5406, https://doi.org/10.1016/j.egyr.2024.05.002. 

21. D. Maji, P. Shenoy, and R. K. Sitaraman, “Multi‐Day Forecasting of Electric Grid Carbon Intensity Using Machine Learning,” _ACM SIGEnergy Energy Informatics Review_ 3, no. 2 (2023): 19–33, https://doi.org/ 10.1145/3607114.3607117. 

22. P. Denholm, M. O’Connell, G. Brinkman, et al., _Overgeneration from Solar Energy in California. a Field Guide to the Duck Chart_ (National Renewable Energy Lab.(NREL), 2015): Tech. rep. 

15 of 16 

_IET Smart Grid,_ 2026 

23. T. Bellini, “Energy networks‐the Data Serving the Energy Transition,” Tech. rep., GRTgaz, 6 rue Raoul Nordling, 92270 Bois‐Colombes (France) (2017). 

24. Platform EET, “Entso‐e Transparency Platform,” (2022), https://tra nsparency.entsoe.eu/dashboard/show. 

16 of 16 

_IET Smart Grid,_ 2026 

