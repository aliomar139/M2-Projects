**_algorithms_** 



_Article_ 

# **Infection Aware Hyper-Heuristic Framework for Hospital Room–Patient Matching** 

**Kassem Danach**<sup>**1,**</sup> *****<sup>**,†**</sup> **, Wael Hosny Fouad Aly**<sup>**2,**</sup> *****<sup>**,†**</sup> **and Chadi Fouad Riman**<sup>**2,†**</sup> 

- 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut P.O. Box 5078/25, Lebanon 

- 2 College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait; chadi.riman@aum.edu.kw 

- Correspondence: kassem.danach@mu.edu.lb (K.D.); wael.aly@aum.edu.kw (W.H.F.A.) 

- These authors contributed equally to this work. 

### **Abstract** 

The assignment of hospital rooms to patients is a critical operational decision that has a direct impact on patient safety, infection control, and staff workload. This study introduces HRPM–IRC, an epidemiology-aware hyper-heuristic framework developed to optimize room–patient matching by minimizing the risk of nosocomial infections, reducing travel and specialty mismatch costs, and promoting equitable nurse workload distribution. A mixed-integer linear programming model is formulated to capture infection transmission probabilities, isolation and cohorting requirements, and multi-ward capacity constraints. On top of this model, a bio-inspired hyper-heuristic adaptively selects and refines low-level heuristics, including cohort-first greedy allocation, risk-gradient swaps, and pathogenaware local MILP refinement, on the basis of contextual epidemiological indicators and reinforcement learning. The framework was validated using a real-world dataset obtained from a tertiary hospital in Lebanon, comprising 142 anonymized patient admissions, 35 rooms, and six nursing teams. Results demonstrate that HRPM–IRC consistently reduces modeled infection risk and workload imbalance by up to forty percent compared to conventional assignment heuristics while maintaining near-real-time decision-making capabilities suitable for dynamic hospital operations. These findings underscore the effectiveness of epidemiology-aware hyper-heuristics in enhancing hospital resilience, improving infection prevention, and supporting fair resource utilization in data-limited healthcare environments typical of Lebanon and other middle-income countries. 



Academic Editors: Frank Werner, Mohammad Shokouhifar and Mehdi Hosseinzadeh 

Received: 26 January 2026 Revised: 20 February 2026 Accepted: 3 March 2026 Published: 9 March 2026 

**Copyright:** © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license. 

**Keywords:** hospital room assignment; infection control; epidemiology-aware optimization; hyper-heuristics; bio-inspired algorithms; mixed-integer programming; workload fairness; healthcare operations management; real-time decision support 

## **1. Introduction** 

Efficient hospital room–patient matching is a central challenge in healthcare operations, directly influencing patient safety, infection control, and workforce well-being [1,2]. In complex hospital environments, especially those facing constrained resources, each admission decision carries epidemiological and operational consequences [3]. The COVID-19 pandemic and subsequent infection outbreaks have underscored the vulnerability of traditional static room assignment policies that neglect dynamic infection risk and staff workload heterogeneity [4]. Hospitals should act now to adopt intelligent decision-support systems capable of balancing infection prevention with fairness and resource efficiency in real time [4]. 

_Algorithms_ **2026** , _19_ , 205 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

2 of 25 

In middle-income healthcare systems such as that of Lebanon, hospitals operate under acute constraints—limited bed capacity, intermittent power and resource shortages, and varying nurse-to-patient ratios. Shared rooms remain common, and infrastructure limitations amplify the risk of nosocomial infections. Under these conditions, allocating patients without considering epidemiological interactions or staff distribution can lead to infection clusters, unequal workloads, and reduced quality of care. These challenges emphasize the urgent need for adaptive, data-driven optimization models that integrate epidemiological risk modeling with operational objectives regarding scheduling and fairness. 

Existing research on hospital room assignment primarily focuses on deterministic or single-objective formulations that minimize travel distance, cost, or occupancy imbalance [5,6]. While effective under stable conditions, such models fail to capture the stochastic nature of infection transmission and the ethical dimension of workload fairness. Heuristic and metaheuristic approaches have improved computational tractability, yet they remain static and problem-specific, unable to learn or adapt when infection rates or hospital occupancies fluctuate [7,8]. This gap calls for a unified, learning-based framework that integrates epidemiological knowledge with combinatorial optimization under uncertainty [5]. 

To address these limitations, this study proposes HRPM–IRC (Hospital Room–Patient Matching with Infection Risk Constraints), an epidemiology-aware hyper-heuristic framework that dynamically balances infection control, spatial allocation, and fairness in healthcare operations. The framework embeds a mixed-integer linear programming (MILP) model within a bio-inspired hyper-heuristic controller that adaptively selects and refines lowlevel heuristics on the basis of contextual epidemiological indicators. The controller draws inspiration from immune and ant-colony behaviors to explore feasible allocations and exploit patterns of effective decision-making. By incorporating reinforcement learning and adaptive feedback, HRPM–IRC continuously improves allocation quality as hospital conditions evolve. 

The framework is validated using real-world data collected from a tertiary Lebanese hospital encompassing 142 anonymized patient admissions, 35 rooms, and six nursing teams across multiple wards. The empirical results demonstrate that HRPM–IRC consistently reduces infection risk and workload imbalance while maintaining computational efficiency suitable for real-time deployment. Beyond its methodological contribution, the study offers a scalable and transparent decision-support system for hospitals operating in resource-limited or crisis contexts, providing a foundation for next-generation infectionaware operational management. 

The remainder of this paper is organized as follows. Section 2 reviews prior work on hospital bed/room assignment, infection-aware optimization, fairness, and hyper-heuristics. Section 3 presents the mathematical formulation of HRPM–IRC. Section 4 develops stochastic and robust extensions. Section 5 details the bio-inspired hyper-heuristic framework. Section 6 describes the datasets, baselines, metrics, scenarios, and ablations and reports empirical results alongside the descriptions of the relevant components (without a separate results subsection). Section 6.8 discusses managerial implications and ethical considerations. Section 8 concludes the paper with limitations and directions for future research. 

## **2. Related Work** 

### _2.1. Hospital Bed and Room Assignment Problems_ 

Hospital bed and room assignment is a critical operational problem affecting patient safety, workflow efficiency, and staff workload. Early formalizations modeled it as a combinatorial optimization problem, often tackled by mixed-integer linear programming (MILP) and heuristic methods [9–12]. Studies to date have focused on minimizing travel distance, specialty mismatch, and room capacity constraints, mainly at the ward level [13,14]. Re- 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

3 of 25 

searchers have also applied local search methods such as tabu search and simulated annealing to improve assignment quality while coping with NP-hard complexity [9]. Some works have integrated distinct scheduling problems, e.g., patient admission and nurse rostering, to address holistic hospital operations [9]. Simulation-based approaches are widely used for performance evaluation and capacity planning [12,15]. 

However, traditional models often overlook infection control and fairness considerations, limiting their effectiveness in high-risk or resource-limited settings. Additionally, the practical impacts of bed-sharing policies, emergency patient handling, and multi-specialty requirements are active areas of research [16,17]. These factors motivate the development of adaptive, integrated frameworks that balance operational efficiency with infection risk and workload fairness. 

### _2.2. Infection-Aware and Epidemiological Models_ 

Recent advances in infection-aware modeling focus on incorporating transmission dynamics into hospital operations. Existing models estimate infection probabilities between co-located patients and adjust for room ventilation and isolation status [6,18]. Robust and chance-constrained optimization methods address uncertainties in infection parameters and patient arrivals, enhancing model resilience during outbreaks. Some studies integrate epidemiological forecasting with hospital capacity planning, leveraging Susceptible–Infected– Recovered (SIR) or Bayesian inference models [18]. Despite advances, the integration of epidemiological data into operational scheduling remains underdeveloped in many healthcare resource planning systems. 

### _2.3. Hyper-Heuristics and Bio-Inspired Methods in Healthcare Logistics_ 

Static heuristics struggle to adapt under the fluctuating infection rates, occupancy, and nurse availability typical of hospital operations [19,20]. Hyper-heuristics address this by learning to select among a portfolio of low-level heuristics (LLHs) based on state features, thereby improving robustness under nonstationarity [4,21]. In HRPM–IRC, a hyper-heuristic controller (contextual bandit or RL policy) chooses LLHs such as cohort-first construction, risk-gradient swaps, fairness moves, and pathogen-aware local MILP refinement, while an acceptance mechanism regulates diversification and stability [8,22]. 

Beyond healthcare, there is growing evidence that adaptive and bio-inspired hyperheuristics scale to dynamic, safety-critical logistics. A hyper-heuristic for heterogeneous medical routing under patient-priority constraints demonstrates that state-aware heuristic selection can respect clinical priorities and service heterogeneity under real-time constraints. Reinforcement-learning controllers trained on dynamic vehicle routing further show that policies can react to streaming events and nonstationary costs, a paradigm directly transferable to dynamic bed/room reallocation during surges or outbreaks [23,24]. 

Recent work has proposed a Q-learning hyper-heuristic with a simulated-annealing acceptance rule, yielding a principled exploration–exploitation balance and temperaturecontrolled move acceptance [25,26]. We adopt this design pattern in HRPM–IRC: an RL/bandit selector scores LLHs by short-horizon reward (joint improvements in infection risk, travel mismatch, and fairness), while a temperature or threshold governs acceptance to preserve solution stability and reduce unnecessary patient moves. Complementarily, matheuristic ML hybrids, e.g., those combining predictive models (random forests) with exact or local optimization for hub location, illustrate how data-informed priors can steer the search toward promising neighborhoods and accelerate convergence [27,28]. We mirror this idea by using epidemiological and operational features (e.g., ward infection index, isolation demand forecasts) to bias LLH selection and seed local MILP neighborhoods around hotspots. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

4 of 25 

Bio-inspired metaphors also guide long-run adaptation. Pheromone-like memory traces of successful ( _i_ , _r_ ) allocations (ant-colony style) and clonal selection of effective LLHs (immune-system analogy) provide lightweight, explainable persistence that helps the controller remember what worked under specific epidemiological regimes yet forget outdated patterns as conditions change. While crisis UAV siting is outside the scope of healthcare, it underscores the value of resilient, adaptive metaheuristics under disrupted infrastructure and sparse data [29]; our robust and stochastic extensions play an analogous role in hospital settings by reserving capacity and hedging transmission-parameter uncertainty. 

In summary, hyper-heuristics—augmented by RL selection, annealing-based acceptance, and bio-inspired long-term memory—offer a principled way to synchronize infection-aware assignment, fairness, and logistical objectives under uncertainty. This synthesis complements data-driven optimization frameworks emerging in healthcare operations [10,30] and provides the adaptive control backbone required for near-real-time hospital room–patient matching. 

### _2.4. Methodological Advances in Hospital Optimization_ 

In parallel with advances in optimization and risk-aware modeling, recent literature has highlighted the importance of transparency and interpretability in automated decisionmaking frameworks. Refs. [5,31,32] present systematic reviews of explainable artificial intelligence (XAI) techniques within operational and strategic decision systems, emphasizing that interpretability is essential for fostering trust, regulatory compliance, and human-in-theloop validation. Their findings underscore the growing need for explainable optimization methodologies, particularly in safety-critical domains such as healthcare, where clinical staff must understand the rationale behind room assignments, isolation decisions, and infectionprevention strategies. This perspective aligns with the design philosophy of HRPM–IRC, which couples hyper-heuristic learning with epidemiological indicators in a manner that remains transparent to practitioners while preserving optimization performance. 

### _2.5. Research Gap_ 

Despite extensive work on bed/room assignment, three strands of the literature— (i) operational assignment under capacity and specialty constraints, (ii) infection-aware planning, and (iii) fairness in workforce utilization—remain largely siloed. Most formulations optimize one or two dimensions while relaxing the third or approach the problem in a static, offline manner [9–11,13,33]. This separation is problematic in hospitals where infection control, logistical efficiency, and equitable staffing interact tightly in day-to-day decisions. 

First, infection risk is rarely modeled at room-level granularity with explicit co-location exposure and environmental multipliers (e.g., ventilation) embedded directly in the assignment objective. Recent studies incorporate compatibility rules or high-level infection penalties [6,18,34], but few integrate pairwise transmission propensities with cohorting and isolation policies while simultaneously coordinating travel/mismatch costs and nurse workload fairness within a single optimization layer. 

Second, uncertainty is typically handled either through stochastic/robust optimization of capacity planning or through simulation studies, with limited online adaptability in the assignment engine itself. Works that do accommodate uncertain arrivals often stop at wardlevel or ICU-level allocation and do not provide mechanisms for rapid, local reoptimization of room assignments during surges or outbreaks. 

Third, fairness is well studied in nurse rostering and integrated bed–staff models [13], yet fairness as a co-primary objective in room–patient matching—linked to team coverage regions and acuity-weighted workloads—remains underexplored. Many approaches assess fairness ex post or as a soft penalty, rather than enforcing explicit upper bounds and stability-aware reallocation that preserve continuity of care. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

5 of 25 

Fourth, there is a methodological gap in adaptive search. Hyper-heuristics and bioinspired methods are powerful for nonstationary combinatorial problems [35,36], but they have seen limited application to hospital room assignment with epidemiology-aware state features and learning-based heuristic selection. Existing hospital optimization pipelines are predominantly static or hand-tuned, lacking reinforcement learning and contextual bandit controllers that can shift search behavior as infection patterns and staffing fluctuate in real time [16,30]. 

Fifth, deployment feasibility in resource-constrained, data-scarce settings is insufficiently addressed. Most evaluations report aggregate improvements on well-curated datasets or simulation test beds [11,12], with little attention to explainability, run-time guarantees under strict time budgets, and stability criteria that limit disruptive patient moves—factors that are pivotal for middle-income hospitals. 

These gaps motivate an epidemiology-aware, fairness-sensitive, adaptive framework that (a) encodes pairwise infection exposure with room-specific risk multipliers, (b) cooptimizes infection, distance/mismatch, and acuity-weighted fairness objectives under uncertainty, (c) supports near-real-time reallocation via learning-driven hyper-heuristics, and (d) demonstrates practical feasibility on a Lebanese hospital dataset. HRPM–IRC is proposed to address this intersection precisely, advancing beyond static heuristics and single-objective formulations [13]. 

## **3. Problem Definition and Mathematical Formulation** 

This section presents the formal definition of the Hospital Room–Patient Matching with Infection Risk Constraints (HRPM–IRC) problem. The objective is to assign a set of patients to available hospital rooms while minimizing infection risk, travel cost, and workload imbalance among nursing teams. The problem is formulated as a mixed-integer linear programming (MILP) problem designed to capture both epidemiological and operational realities observed in Lebanese hospitals, where resource limitations, isolation requirements, and uneven staff distribution coexist. 

### _3.1. Problem Description_ 

Each patient admitted to the hospital must be allocated to exactly one room that satisfies both medical and epidemiological constraints. Patients vary by isolation requirements, diagnosis category, and risk of infection transmission. Rooms differ in capacity, ventilation quality, and proximity to specific wards. Nursing teams are responsible for subsets of rooms, and their workload must remain balanced to ensure fairness and quality of care. 

The HRPM–IRC formulation jointly optimizes three main objectives: 

1. Minimizing nosocomial infection risk by reducing high-risk co-location pairs; 

2. Minimizing travel or mismatch costs between patients and wards; 

3. Minimizing workload imbalance among nursing teams to promote fairness. 

### _3.2. Sets and Indices_ 

The sets and their indices are as follows: 

- _P_ : set of patients, indexed by _i_ ; 

- _R_ : set of rooms, indexed by _r_ ; 

- _N_ : set of nurse teams, indexed by _n_ ; 

- _W_ : set of wards, with _Rw ⊆ R_ denoting rooms in ward _w_ ; 

- _C_ : set of incompatible patient pairs (clinical or epidemiological); 

- ( _i_ , _j_ ): unordered patient pair such that _i < j_ . 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

6 of 25 

### _3.3. Parameters_ 

The parameters are as follows: 

- _cr_ : capacity (number of beds) of room _r_ ; 

- _di_ , _r_ : travel or mismatch cost for assigning patient _i_ to room _r_ ; 

- _πij_ : infection transmission propensity between patients _i_ and _j_ ; 

- _αr_ : room risk multiplier based on ventilation or ward type; 

- _κi ∈{_ 0, 1 _}_ : isolation indicator (1 if patient _i_ requires isolation); 

- _br_ : baseline workload contribution for an occupied bed in room _r_ ; 

- _ω_ 1, _ω_ 2, _ω_ 3: weighting coefficients for infection, travel, and fairness objectives; 

- Γ: maximum number of allowed patient relocations between consecutive optimization runs. 

In the Lebanese hospital dataset, _πij_ values are estimated from historical co-location and infection logs, and _αr_ values reflect room-specific air quality (good, moderate, or poor ventilation). 

For dynamic re-optimization settings, let _xi_<sup>_prev_</sup> , _r_ denote the assignment of patient _i_ to room _r_ in the previous solution. 

### _3.4. Decision Variables_ 

The decision variables are as follows: 

- _xi_ , _r ∈{_ 0, 1 _}_ : 1 if patient _i_ is assigned to room _r_ , 0 otherwise; 

- _yijr ∈{_ 0, 1 _}_ : 1 if patients _i_ and _j_ share the same room _r_ ; 

- _un ≥_ 0: workload of nurse team _n_ ; 

- _z ≥_ 0: upper bound on team workloads (fairness measure); 

- _vi ∈{_ 0, 1 _}_ : relocation indicator (1 if patient _i_ is reassigned from a previous room). 

### _3.5. Objective Function_ 

The HRPM–IRC formulation addresses three complementary goals: reducing infection transmission risk, minimizing travel or mismatch cost, and promoting fairness in nurse workload distribution. These objectives are combined into a single weighted function to balance epidemiological safety, logistical efficiency, and equity in resource utilization. 

Formally, the proposed model constitutes a multi-objective optimization problem in which three conflicting performance criteria must be simultaneously considered. Rather than optimizing each objective independently, the model aggregates them within a normalized weighted-sum framework to preserve joint optimization behavior. 

Since these three objectives are measured in different units (expected infection risk, spatial distance cost, and workload imbalance), direct aggregation may introduce scale bias. To ensure dimensional consistency and meaningful weight interpretation, each objective component is normalized using min–max scaling based on extreme single-objective solutions. Let _F_<sup>min</sup> and _F_<sup>max</sup> denote the minimum and maximum achievable values obtained _k k_ when optimizing each objective independently. The normalized objective components are defined as 



<!-- Start of picture text -->
Fk − Fk min<br>F ˆ k = , k ∈{R ,  C ,  W} .<br>F max − F min<br>k k<br><!-- End of picture text -->

This transformation ensures that all objectives become dimensionless and lie within the interval [0, 1], thereby eliminating unit inconsistencies, preventing dominance of numerically larger terms, and enabling a fair and interpretable trade-off representation. 

The resulting optimization problem is expressed as 



<!-- Start of picture text -->
min ω 1 R ˆ  +  ω 2 C ˆ  +  ω 3 W ˆ (1)<br><!-- End of picture text -->

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

7 of 25 

where _R_<sup>ˆ</sup> , _C_<sup>ˆ</sup> , and _W_<sup>ˆ</sup> denote the normalized infection risk, travel cost, and workload imbalance components, respectively. The optimization is always performed on this aggregated objective, ensuring simultaneous consideration of all three criteria. 

The coefficients _ω_ 1, _ω_ 2, and _ω_ 3 are non-negative weighting parameters that determine the relative priority of infection prevention, spatial efficiency, and fairness. 

In practical implementation, these weights reflect managerial preference and hospital policy priorities. They may be calibrated through structured expert consultation, Analytic Hierarchy Process (AHP)-based pairwise comparisons, or policy-driven prioritization (e.g., assigning higher _ω_ 1 during infectious disease outbreaks or higher _ω_ 3 during staffing shortages). Unless otherwise specified, equal weights are used to represent balanced prioritization. 

To further ensure robustness, a systematic sensitivity analysis on the weight vector is conducted in Section 6, demonstrating that solution patterns remain stable under moderate weight perturbations and that meaningful trade-offs are consistently preserved. 

The first objective component represents the epidemiological dimension of the model. The parameter _πij_ denotes the infection transmission probability between patients _i_ and _j_ if co-located in the same room, while _yijr_ is a binary variable indicating whether the two patients share room _r_ . The multiplier _αr_ adjusts this risk according to room-specific ventilation quality or infection-control level, such as isolation units or negative-pressure wards. Minimizing this component reduces expected nosocomial transmission events by discouraging high-risk co-locations and favoring well-ventilated or single-bed rooms. This is especially important in Lebanese hospitals where multi-bed rooms are common and infection control resources are limited. 

The second objective component captures the spatial and logistical dimension of patient placement. The parameter _di_ , _r_ measures the travel or mismatch cost associated with assigning patient _i_ to room _r_ , which may reflect distance from specialized wards, transport inefficiency, or mismatch with clinical service areas. By minimizing this component, the optimization model promotes operational proximity between patients and their required medical units, improving workflow coordination and reducing internal patient movement. Such efficiency gains are particularly relevant in hospitals with fragmented layouts or constrained infrastructure. 

The third objective component enforces fairness in workload distribution among nursing teams. The continuous variable _z_ represents the upper bound on total workload across all teams, while the team workload _un_ aggregates weighted assignments within each team’s coverage area. Minimizing _z_ ensures that no team experiences an excessive care burden relative to others. This contributes to sustained service quality and reduces staff fatigue or burnout. 

Although full Pareto-front generation techniques (e.g., NSGA-II or other evolutionary multi-objective algorithms) could be employed to enumerate a diverse set of non-dominated solutions, such approaches typically require population-based search and substantially higher computational effort. Given that hospital room assignment decisions must often be computed within tight operational time windows, computational efficiency and deterministic reproducibility are critical requirements. 

The normalized weighted-sum formulation therefore provides an effective compromise: it preserves multi-objective trade-off modeling while enabling rapid solution times suitable for near-real-time clinical decision support. Furthermore, the weighted structure offers direct managerial interpretability, allowing hospital administrators to transparently adjust priorities without reconfiguring the optimization framework. 

Together, the three components in Equation (1) create a balanced multi-criterion framework that aligns epidemiological risk management with operational logistics and workforce equity. The weighted structure provides flexibility: higher _ω_ 1 values emphasize 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

8 of 25 

infection control during epidemic surges, while higher _ω_ 3 values promote workforce equity during prolonged strain periods. 

Overall, the objective function defines a holistic optimization strategy that jointly minimizes infection exposure, spatial inefficiency, and staff inequity—three interdependent dimensions crucial for resilient and equitable hospital management. 

### _3.6. Constraints_ 

The HRPM–IRC formulation is governed by the following constraints, which ensure feasibility with respect to patient assignment, room capacity, epidemiological safety, and workload fairness. Each constraint group is described below with its operational interpretation. 

Patient Assignment and Room Capacity. 



<!-- Start of picture text -->
∑ xi , r = 1, ∀i ∈ P (2)<br>r∈R<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ xi , r ≤ cr , ∀r ∈ R (3)<br>i∈P<br><!-- End of picture text -->

Constraint (2) ensures that each patient _i_ is assigned to exactly one room, reflecting the practical requirement that no patient can occupy multiple rooms simultaneously. Constraint (3) enforces the physical capacity limit _cr_ of each room _r_ , ensuring that the number of assigned patients never exceeds the number of available beds. In the Lebanese dataset, _cr ∈{_ 1, 2 _}_ distinguishes single and double occupancy rooms, often linked to infection isolation policies. 

Co-Location Linearization. 



<!-- Start of picture text -->
yijr ≤ xi , r , ∀i < j ,  r ∈ R (4)<br><!-- End of picture text -->



<!-- Start of picture text -->
yijr ≤ xj , r , ∀i < j ,  r ∈ R (5)<br><!-- End of picture text -->



<!-- Start of picture text -->
yijr ≥ xi , r  +  xj , r − 1, ∀i < j ,  r ∈ R (6)<br><!-- End of picture text -->

These constraints linearize the product between binary variables _xi_ , _r_ and _xj_ , _r_ by introducing auxiliary binary variables _yijr_ that take value 1 if and only if patients _i_ and _j_ share the same room _r_ . This formulation allows infection risk terms _πijyijr_ to be modeled linearly in the objective function. In operational terms, _yijr_ = 1 identifies patient pairs co-located within the same room, which is critical for computing nosocomial infection exposure. 

Isolation and Incompatibility. 



<!-- Start of picture text -->
∑ yijr ≤ (1  − κi ), ∀i ∈ P , ∀r ∈ R (7)<br>j̸ = i<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ yijr = 0, ∀ ( i ,  j )  ∈C (8)<br>r∈R<br><!-- End of picture text -->

Constraint (7) enforces isolation requirements in linear form. If a patient requires isolation ( _κi_ = 1), the inequality forces ∑ _j̸_ = _i yijr_ = 0, meaning the patient cannot share a room with others. This models infection-control regulations in Lebanese hospitals, particularly in wards handling tuberculosis, COVID-19, or MRSA cases. 

Constraint (8) prevents co-location of clinically or epidemiologically incompatible pairs ( _i_ , _j_ ) _∈C_ , such as patients with conflicting gender, pathogen, or treatment protocols. These incompatibility sets are derived from infection control logs and hospital assignment guidelines. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

9 of 25 

Nurse Workload and Fairness. 



<!-- Start of picture text -->
un = ∑ br  ∑ xi , r , ∀n ∈ N (9)<br>r∈R ( n ) i∈P<br><!-- End of picture text -->



<!-- Start of picture text -->
un ≤ z , ∀n ∈ N (10)<br><!-- End of picture text -->

Constraint (9) computes the total workload _un_ for each nurse team _n_ , aggregating all assigned patients in the rooms covered by that team. The workload weight _br_ captures room-specific care intensity, derived from hospital acuity scoring. Constraint (10) imposes an upper bound _z_ on all team workloads, ensuring balanced distribution of responsibilities and preventing nurse burnout. In practice, minimizing _z_ corresponds to promoting equity in staff utilization across wards—a key fairness requirement in Lebanese hospitals where teams operate under tight resource limitations. 

Stability Constraints. 



<!-- Start of picture text -->
vi ≥ xi prev , r − xi , r , ∀i ∈ P , ∀r ∈ R (11)<br><!-- End of picture text -->



<!-- Start of picture text -->
vi ≥ xi , r − xi prev , r , ∀i ∈ P , ∀r ∈ R (12)<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ vi ≤ Γ (13)<br>i∈P<br><!-- End of picture text -->

Constraints (11) and (12) activate relocation indicator _vi_ when patient _i_ is assigned to a different room than in the previous solution. Constraint (13) limits the total number of disruptive reallocations to a managerial threshold Γ, ensuring operational stability. 

Variable Domains. 



<!-- Start of picture text -->
xi , r ,  yijr ,  vi ∈{ 0, 1 } , un ,  z ≥ 0. (14)<br><!-- End of picture text -->

This final set of constraints specifies variable domains. Binary variables _xi_ , _r_ and _yijr_ capture discrete assignment and co-location decisions, while _un_ and _z_ are continuous non-negative variables representing workload magnitudes and their upper bound, respectively. These domain restrictions ensure mathematical consistency and computational tractability within the MILP framework. 

Together, these constraints maintain epidemiological safety, resource feasibility, and staff equity in the optimization model. They represent a mathematically precise translation of real hospital operational rules into an optimization structure suitable for integration with the bio-inspired hyper-heuristic framework described in Section 5. 

### _3.7. Model Discussion_ 

The HRPM–IRC formulation is a binary MILP problem with quadratic infection risk terms linearized via _yijr_ variables. The model simultaneously captures epidemiological safety, operational cost, and fairness. Its structure enables hybrid optimization, allowing the proposed bio-inspired hyper-heuristic to exploit the MILP formulation locally for refinement. For the Lebanese hospital dataset, instance sizes up to 150 patients and 40 rooms can be solved within seconds using adaptive heuristic control, while full MILP solutions serve as optimality references for small-scale scenarios. 

## **4. Stochastic and Robust Extensions** 

Hospital operations are inherently uncertain. Patient arrivals, isolation requirements, and infection dynamics can fluctuate rapidly, particularly during epidemic or surge conditions. To enhance the practical resilience of the HRPM–IRC model, this section extends 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

10 of 25 

the deterministic formulation to handle stochastic arrivals and uncertain infection parameters through chance-constrained and robust optimization techniques. In addition, a stability-aware rolling-horizon mechanism is introduced to explicitly control patient reallocations across successive decision epochs, ensuring practical feasibility in real hospital environments. 

### _4.1. Stochastic Patient Arrivals_ 

In practice, new patients may arrive during each scheduling period, often with unpredictable isolation needs. Let _A_<sup>˜</sup> _w_ denote the random variable representing the number of isolation-required arrivals targeting ward _w_ during a decision horizon _H_ . To guarantee feasible capacity under most scenarios, a safety buffer _sw_ is reserved in each ward according to a probabilistic threshold: 



<!-- Start of picture text -->
P( A ˜ w ≤ sw )  ≥ 1  − β , ∀w ∈ W (15)<br><!-- End of picture text -->

where _β_ represents the risk tolerance level (e.g., _β_ = 0.05 for 95% confidence). This leads to the following revised ward-level capacity constraint: 



<!-- Start of picture text -->
∑ xi , r ≤ ∑ cr − sw , ∀w ∈ W (16)<br>r∈Rw i ∑ ∈P r∈Rw<br><!-- End of picture text -->

If _A_<sup>˜</sup> _w_ follows a known discrete or Poisson distribution with mean _µw_ and variance _σw_<sup>2,</sup> the quantile _sw_ = _Q_<sup>_−_</sup> _A_ ˜ _w_<sup>1(1</sup><sup>_−β_) can be precomputed.When only the first two moments are</sup> known, the Chebyshev inequality yields a conservative deterministic bound: 



<!-- Start of picture text -->
1  − β<br>sw = µw  + σw (17)<br>� β<br><!-- End of picture text -->

where _µw_ is the mean arrival rate and _σw_ is the standard deviation of arrivals to ward _w_ . 

### _4.2. Uncertain Infection Transmission Parameters_ 

Infection propagation parameters _πij_ are estimated from limited and noisy epidemiological data (e.g., co-location logs and microbiological results). To hedge against this uncertainty, we define an interval uncertainty set: 



<!-- Start of picture text -->
πij ∈ [ π ¯ ij − δij , π ¯ ij  +  δij  ], ∀i ,  j ∈ P (18)<br><!-- End of picture text -->

where _π_ ¯ _ij_ is the nominal estimate and _δij_ is the maximum deviation determined from historical variance or expert judgment. 

The corresponding robust counterpart of the infection-risk term becomes 



<!-- Start of picture text -->
max αr  ∑ πijyijr = ∑ αr  ∑( ¯ πij  +  δij ) yijr (19)<br>πij∈ [ ¯ πij−δij , ¯ πij + δij ] r ∑ ∈R i<j r∈R i<j<br><!-- End of picture text -->

which inflates the infection-risk component in proportion to the uncertainty margin, ensuring conservatism under worst-case propagation conditions. 

### _4.3. Distributionally Robust Formulation (Optional Extension)_ 

When the exact distribution of infection risk or arrivals is unknown, a distributionally robust variant can be formulated. Let _P_ denote the ambiguity set of all probability distribu- 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

11 of 25 

tions consistent with known moments ( _µ_ , _σ_<sup>2</sup> ). The worst-case expected infection risk can be bounded as 



<!-- Start of picture text -->
max P∈P E P ∑ αr  ∑ πijyijr ≤ ∑ αr  ∑ � π ¯ ij  + Γ  σij � yijr (20)<br>� r∈R i<j � r∈R i<j<br><!-- End of picture text -->

where Γ controls the conservatism level of the ambiguity set. This formulation offers a tunable trade-off between risk aversion and performance, particularly relevant during infectious outbreaks with limited data. 

### _4.4. Receding-Horizon Implementation with Stability Control_ 

To accommodate time-varying hospital dynamics, HRPM–IRC is embedded within a rolling-horizon control mechanism. At each decision epoch _t_ , the model is re-solved over horizon _H_ , incorporating new arrivals, discharges, and updated epidemiological parameters. 

However, unrestricted re-optimization may lead to reassignment of patients who are already hospitalized, which can generate operational disruption, patient dissatisfaction, and additional nursing workload. To explicitly control such reallocations, we define _xir_<sup>(</sup><sup>_t−_1)</sup> as the room assignment of patient _i_ at the previous decision epoch. 

A binary relocation variable is introduced: 



<!-- Start of picture text -->
<br>1 if patient  i  is reassigned at epoch  t ,<br>zi ( t ) = 0 otherwise. (21)<br><br><!-- End of picture text -->

Relocation is activated when the new assignment differs from the previous one. The following linear constraints ensure consistency: 



<!-- Start of picture text -->
zi ( t ) ≥ xir ( t ) − x ir ( t− 1) , ∀i ∈ P ,  ∀r ∈ R (22)<br><!-- End of picture text -->



<!-- Start of picture text -->
zi ( t ) ≥ xir ( t− 1) − xir ( t ), ∀i ∈ P ,  ∀r ∈ R (23)<br><!-- End of picture text -->

To prevent excessive patient movement, a relocation budget is imposed: 



<!-- Start of picture text -->
∑ zi ( t ) ≤ Γ (24)<br>i∈P<br><!-- End of picture text -->

where Γ represents the maximum allowable number of relocations per decision epoch, determined by hospital management policy. In practice, Γ is set to a small fraction (e.g., 3–5%) of currently admitted patients, ensuring that most patients remain in their initially assigned rooms unless substantial infection-risk reduction or workload balancing benefits justify reassignment. 

The learning controller leverages prior solutions as warm starts, improving convergence speed and solution stability. The explicit relocation control mechanism ensures that dynamic re-optimization remains aligned with real-world operational constraints and patient-centered care considerations. 

### _4.5. Summary of Benefits_ 

The stochastic and robust extensions significantly enhance HRPM–IRC in the following ways: 

- Preserving feasibility under fluctuating admission and isolation demands; 

- Accounting for uncertainty in infection transmission estimates; 

- Explicitly limiting unnecessary patient reallocations across decision epochs; 

- Enabling dynamic, near-real-time decision-making through receding-horizon adaptation. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

12 of 25 

These extensions make the framework more reliable for deployment in real-world hospital environments where uncertainty, operational disruption, and patient comfort considerations are pervasive. 

## **5. Bio-Inspired Hyper-Heuristic Framework** 

The deterministic and robust HRPM–IRC formulations provide strong optimization capabilities for hospital room–patient matching. However, their performance can degrade when hospital conditions evolve rapidly, such as during infection surges or sudden staff shortages. To ensure adaptability and near-real-time responsiveness, we design a bioinspired hyper-heuristic (BHH) that dynamically selects, refines, and coordinates low-level heuristics (LLHs) according to contextual epidemiological and operational indicators. 

### _5.1. Motivation_ 

Fixed or static heuristics often fail to maintain performance under changing infection and workload dynamics. During outbreaks, room configurations, patient isolation statuses, and nursing availability can shift within hours, rendering static assignment strategies suboptimal. The BHH component of HRPM–IRC overcomes this limitation by incorporating a hyper-heuristic controller that observes the current system state and adaptively chooses the most promising heuristic for the next decision step. This enables the algorithm to continuously improve as new epidemiological data become available, achieving a balance between exploitation of effective heuristics and exploration of alternative strategies. 

### _5.2. Architecture of the HRPM–IRC Framework_ 

The proposed framework is composed of four main layers: 

1. State Representation Layer: a layer that encodes the current hospital configuration, including infection intensity, occupancy level, and fairness deviation. 

2. Low-Level Heuristic (LLH) Portfolio: a layer that provides a set of specialized operators designed to improve distinct objectives. 

3. Hyper-Heuristic Controller: a reinforcement learning or contextual bandit agent that adaptively selects the LLH based on state feedback and reward signals. 

4. Acceptance Mechanism: a layer that determines whether a candidate move is accepted, balancing solution quality and diversification. 

Each iteration of the BHH combines these components into a self-adaptive decision loop capable of learning optimal heuristic-selection policies over time. 

### _5.3. Low-Level Heuristic Portfolio_ 

The LLH portfolio contains diverse operators, each tailored to exploit different structural properties of the HRPM–IRC search space: 

- Cohort-First Greedy (CFG): assigns patients with similar infection profiles or isolation statuses to shared rooms to minimize cross-contamination. 

- Risk-Gradient Swap (RGS): evaluates pairwise patient exchanges between rooms and performs a swap if the marginal improvement in infection risk plus travel cost is negative. 

- Isolation Packing (IP): groups non-infectious patients to preserve single rooms for isolation-required cases in future stochastic arrivals. 

- Nurse-Balance Move (NBM): reassigns low-acuity patients from overloaded to underloaded nurse teams while preserving room feasibility. 

- Pathogen-Aware Local MILP (PA-MILP): solves a localized MILP on a subset of highrisk wards to perform fine-grained optimization around epidemiological hotspots. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

13 of 25 

- Ant-Inspired Search (AIS): utilizes pheromone trails representing the historical success rate of specific ( _i_ , _r_ ) assignments, favoring moves that consistently reduce infection risk. 

The combination of constructive, neighborhood, and metaheuristic LLHs ensures search diversity and robustness across operational states. 

### _5.4. Learning Controller_ 

The hyper-heuristic controller governs the selection of LLHs at each iteration. Let _st_ denote the system state at iteration _t_ , characterized by a feature vector: 



<!-- Start of picture text -->
st = [  ρt , ηt , ξt , ∆ ft  ] (25)<br><!-- End of picture text -->

where _ρt_ is the ward-level infection index, _ηt_ represents capacity utilization, _ξt_ is the fairness deviation, and ∆ _ft_ captures recent improvement trends. 

All state variables are normalized to [0, 1] prior to learning to ensure scale consistency and numerical stability. 

The controller’s action _at_ corresponds to selecting a heuristic: 



<!-- Start of picture text -->
hk ∈H  =  { CFG, RGS, IP, NBM, PA-MILP, AIS } . (26)<br><!-- End of picture text -->

A reward signal is computed after the execution of _hk_ : 



<!-- Start of picture text -->
rt =  − ( ω 1∆Risk +  ω 2∆Travel +  ω 3∆ z ) (27)<br><!-- End of picture text -->

In the experimental evaluation, the controller is implemented as a contextual bandit using the LinUCB algorithm. Although the framework is extensible to other reinforcement learning strategies, all reported results correspond to this specific implementation for reproducibility. 

### Learning Mechanism 

At each iteration _t_ , LinUCB selects heuristic _hk_ by maximizing 



<!-- Start of picture text -->
at = arg max k � θ ˆ k ⊤st  +  α � s ⊤ t A− k 1 st �<br><!-- End of picture text -->

where _θ_<sup>ˆ</sup> _k_ is the estimated parameter vector for heuristic _k_ , _Ak_ is the design matrix updated online, and _α_ controls the exploration level. 

### Training Protocol 

Learning is performed fully online during each optimization run. No offline pre-training or historical replay buffer is used. Parameter updates occur immediately after observing reward _rt_ . 

### Hyperparameter Settings 

The exploration parameter was set to _α_ = 0.2 on the basis of preliminary tuning on the development split. 

### Sensitivity Analysis 

To assess robustness, additional experiments were conducted for _α ∈{_ 0.1, 0.3, 0.5 _}_ . Performance variation remained below 3% across tested instances, indicating stable convergence behavior. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

14 of 25 

### _5.5. Bio-Inspired Component_ 

The adaptive mechanism of HRPM–IRC draws inspiration from biological intelligence paradigms: 

- Immune System Analogy: heuristics act as antibodies competing to neutralize “infection risk” within the system. Effective heuristics are clonally selected and mutated for diversity, following the clonal selection principle. 

- Ant Colony Analogy: each heuristic deposits pheromones proportional to its recent reward, reinforcing successful search patterns. Pheromone evaporation ensures responsiveness to changing epidemiological contexts. 

This bio-inspired learning process enables continual adaptation and resilience, mirroring how biological systems evolve defense mechanisms under dynamic environments. 

### _5.6. Algorithmic Flow_ 

The integrated algorithmic flow of the HRPM–IRC framework is summarized in Algorithm 1. The process begins with a feasible assignment from the MILP or CFG heuristic and iteratively refines it through adaptive LLH selection until the time budget or convergence threshold is reached. 

**Algorithm 1** Bio-Inspired Hyper-Heuristic (BHH) for HRPM–IRC. The algorithm iteratively selects low-level heuristics using a learning controller, applies them to the current solution, and accepts improvements on the basis of a simulated annealing acceptance criterion. 

**Require:** initial feasible assignment _x_ , LLH portfolio _H_ , time limit _T_ 

1: _x_<sup>_∗_</sup> _← x_ 

2: Evaluate _F_ ( _x_ ); observe state _s_ 0; initialize controller and pheromone trails 

- 3: **while** elapsed_time() _< T_ **do** 

- 4: Observe state _st_ from hospital configuration 

- 5: Select heuristic _hk ∈H_ using policy _π_ ( _· | st_ ) 6: _x_<sup>_′_</sup> _←_ apply( _hk_ , _x_ ) 7: _rt ←−_ ( _ω_ 1∆Risk + _ω_ 2∆Travel + _ω_ 3∆ _z_ ) 8: **if** accept( _rt_ , _τt_ ) **then** 

- 9: _x ← x_<sup>_′_</sup> 

10: Update pheromones and controller parameters 11: **if** _F_ ( _x_ ) _< F_ ( _x_<sup>_∗_</sup> ) **then** 12: _x_<sup>_∗_</sup> _← x_ 13: **end if** 14: **end if** 

- 15: Update temperature _τt_ +1 or exploration parameter 16: **if** new_patients_arrive() **then** 

17: Insert arrivals into _x_ and trigger local reallocation 

- 18: **end if** 

19: **end while** 

20: **return** _x_<sup>_∗_</sup> 

The adaptive selection, reward-driven reinforcement, and pheromone-guided learning together form the bio-inspired intelligence core of HRPM–IRC. This enables the system to maintain high-quality room assignments in the face of changing infection patterns and operational constraints, as demonstrated in the experimental results presented in Section 6. 

## **6. Experimental Design and Evaluation** 

We evaluate HRPM–IRC on real and synthetic datasets against strong baselines, using multi-criterion metrics and rigorous statistical testing. Figures are provided as `.png` files for portability and are referenced directly in the text below. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

15 of 25 

### _6.1. Datasets_ 

The empirical evaluation is based on an anonymized snapshot of tertiary hospitals in Beirut, Lebanon, complemented by a family of synthetic test beds calibrated to the real data. All records were de-identified prior to analysis and approved under institutional datause and IRB guidelines (ref. MU-2025-HH01). The variables span patient attributes (age band, diagnosis group, comorbidity index, isolation flag _κi_ , expected length of stay), room attributes (capacity _cr ∈{_ 1, 2 _}_ , ward label, ventilation class) and staff structure (nursing teams covering disjoint room sets with workload weights _br_ ). 

Although the empirical evaluation is based on a single tertiary hospital network, the modeling framework itself is institution-agnostic. All input components (room capacities, isolation flags, ventilation classes, workload weights, and infection propensities) correspond to standard hospital information system variables that are routinely available across healthcare facilities. The optimization structure does not rely on Lebanon-specific regulatory assumptions and can be recalibrated using local data from other institutions. 

For infection modeling, pairwise propensities _πij_ were estimated using a logistic regression model trained on historical co-location and pathogen transmission logs. The dependent variable indicates whether a secondary infection was observed following co-location of patients _i_ and _j_ within the same ward block. 

The feature set includes (i) temporal overlap duration (hours of shared stay), (ii) pathogen class compatibility indicators, (iii) immunosuppression or high-risk clinical flags, (iv) wardlevel contact intensity metrics, and (v) shared staff coverage indicators. Continuous variables were standardized prior to fitting. 

Model coefficients were estimated using maximum likelihood, with empirical Bayes shrinkage toward ward-level priors to mitigate small-sample bias in low-incidence wards. Calibration quality was evaluated using fivefold cross-validation, reporting mean AUC, Brier score, and calibration slope. The resulting predicted probabilities were clipped to [0, 1] and used as pairwise infection propensity parameters _πij_ . 

Room multipliers _αr_ encode environmental risk modifiers that capture room-level infection transmission conditions. In practical hospital settings, these values can be determined from measurable infrastructure and infection-control attributes, including ventilation performance (air changes per hour), presence of negative-pressure systems, HEPA filtration availability, single versus double occupancy configuration, and isolation capability. 

In the Lebanese dataset, _αr_ values were derived from facilities audit reports and ventilation classifications. Rooms were grouped into three environmental risk classes (low, medium, high) based on infection-control infrastructure. These classes were then mapped to normalized multipliers within [0, 1], preserving relative risk differences while ensuring numerical stability in optimization. Spatial or specialty mismatch costs _di_ , _r_ combine geometric proximity to the required specialty unit and penalties for off-service placement; distances are computed from floor plans (Manhattan metric across ward blocks) and rescaled to [0, 1]. Nurse workload weights _br_ were derived from acuity scoring (nurse-to-patient ratios per ward), z-scored within wards and clipped to ensure numerical stability. 

Data cleaning removed impossible timestamps and resolved overlapping admissions using earliest-start precedence; missing covariates ( _<_ 3%) were imputed using wardconditional medians for continuous fields and non-frequent categories. To assess generalization, we split instances into development (60%), validation (20%), and holdout evaluation sets (20%) at the admission-episode level, maintaining ward and isolation stratification. All algorithms receive only the evaluation slice during final reporting. 

Synthetic test beds expand the operating envelope while preserving key epidemiological and operational regularities. We vary scale with _|P|∈{_ 50, 100, 150, 200 _}_ and _|R|∈{_ 20, 40, 60 _}_ , and modulate infection density from 5% to 30%. Pairwise risks _πij_ are sampled from a ward- 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

16 of 25 

blocked Beta mixture calibrated to the Lebanese posterior means and variances, yielding community-like clusters (higher within-wards risk, lower between-wards risk). We induce correlation between isolation flags and high-risk edges by increasing the Beta concentration for _κi_ = 1 cases. Ventilation multipliers _αr_ follow the empirical room-class histogram; capacities mirror the real ratio of single to double rooms. Distances _di_ , _r_ are generated on a synthetic grid consistent with the ward map, then scaled to [0,1]; workload weights _br_ follow truncated normal distributions centered at ward means. 

Arrival uncertainty for scenario analysis is simulated via an inhomogeneous Poisson process with time-of-day intensity fitted from the real timestamps; lengths of stay draw from a ward-specific log-normal. To stress robustness, we add zero-mean Gaussian noise to _πij_ (bounded to [0, 1]) and occasionally perturb _αr_ within class bounds to emulate ventilation outages. All random generators are seeded for reproducibility and released with the code. 

Owing to patient privacy regulations and IRB restrictions, the real hospital dataset cannot be publicly shared. To ensure reproducibility despite these constraints, we provide a complete data dictionary (variable definitions, units, and ranges), documented preprocessing procedures, synthetic instance generators statistically calibrated to the empirical dataset, fixed random seeds, and parameter configuration files. 

The synthetic test beds are constructed to preserve key structural characteristics observed in the real hospital (infection density, ward clustering patterns, capacity ratios, and ventilation class distributions), while systematically varying scale and epidemiological intensity. This design enables independent replication of experiments and supports external validity assessment beyond the single empirical site. Dataset summary (real and synthetic) is shown in Table 1. 

**Table 1.** Dataset summary (real and synthetic). 

|**Dataset**|**_|P|_**|**_|R|_**|**Wards**|**Teams**|**Iso.%**|**Notes**|
|---|---|---|---|---|---|---|
|Lebanon (real)|142|35|5|6|12%|Vent. classes,_πij_ from logs|
|Syn-S (small)|50|20|3|3|10%|Beta-calibrated_πij_|
|Syn-M (med.)|100|40|4|4|15%|As above|
|Syn-L (large)|150|60|5|6|20%|As above|
|Syn-XL (surge)|200|60|5|6|25%|High occupancy|



### _6.2. Baseline Methods_ 

We benchmark HRPM–IRC against five standard baselines under matched time budgets and identical feasibility rules (capacity, isolation, incompatibilities). All methods operate on the same solution encoding (patient-to-room vector) and minimize the aggregated normalized multi-objective function in Equation (1) under identical feasibility constraints, ensuring consistent multi-objective evaluation across methods. Baselines and main settings (pilot-tuned) is shown in Table 2 

**Table 2.** Baselines and main settings (pilot-tuned). 

|**Method**|**Main Settings**|
|---|---|
|GRD|Greedy assignment minimizing_di_,_r_, capacity/isolation enforced.|
|SA|Initial GRD; swap neighborhood; geometric cooling_T ←_0.95_T_; stop at 0.01_T_0.|
|GA|Pop. 60; one-point crossover _pc_ = 0.8; mutation _pm_ = 0.1; elitism 2.|
|TS|Swap/insertion; tabu tenure 10; aspiration by best; 300 iterations.|
|MILP (exact)|Gurobi, 300 s cap, optimality gap reported; small/medium only.|



The greedy construction (GRD) orders patients (e.g., isolation first, then by descending ∑ _j πij_ ) and assigns each to the feasible room with the minimum marginal objective increase, breaking ties by lower risk and then shorter travel, as illustrated in Algorithm 2. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

17 of 25 

**Algorithm 2** GRD: Greedy Feasible Assignment 

**Require:** patients _P_ (ordered), rooms _R_ , feasibility set _F_ 

- 1: _x ←_ empty assignment 

- 2: **for** _i ∈ P_ **do** 

- 3: _Ri ←{r ∈ R_ : ( _i_ , _r_ ) feasible under _F}_ 4: choose _r_<sup>_⋆_</sup> _∈_ arg min _r∈Ri_ ∆ _F_ ( _x_ ; _i → r_ ) 5: assign _i → r_<sup>_⋆_</sup> in _x_ 

- 6: **end for** 

- 7: **return** _x_ 

Simulated annealing (SA), as illustrated in Algorithm 3, starts from GRD and explores a swap/move neighborhood with geometric cooling; a candidate _x_<sup>_′_</sup> is accepted with probability min _{_ 1, exp( _−_ ∆/ _T_ ) _}_ , where ∆ = _F_ ( _x_<sup>_′_</sup> ) _−F_ ( _x_ ). 

The genetic algorithm (GA) maintains a population of 60 solutions, uses one-point crossover ( _pc_ = 0.8), feasible mutation ( _pm_ = 0.1), and elitism (top 2). Infeasible offspring are repaired by projecting to _F_ via capacity-aware reassignments that prioritize isolation, as presented in Algorithm 4. 

**Algorithm 3** SA: Swap/Move with Geometric Cooling 

- **Require:** initial _x ←_ GRD; _T ← T_ 0; time limit _T_ max 1: **while** elapsed_time() _< T_ max **and** _T >_ 0.01 _T_ 0 **do** 2: _x_<sup>_′_</sup> _←_ sample_neighbor( _x_ ) _▷_ random move or pairwise swap respecting _F_ 3: ∆ _←F_ ( _x_<sup>_′_</sup> ) _−F_ ( _x_ ) 4: **if** ∆ _≤_ 0 **or** rand() _<_ exp( _−_ ∆/ _T_ ) **then** 

- 5: _x ← x_<sup>_′_</sup> 

- 6: **end if** 7: _T ←_ 0.95 _T_ 8: **end while** 9: **return** best solution seen 

**Algorithm 4** GA: One-Point Crossover + Feasible Mutation 

**Require:** pop size _N_ = 60, _pc_ = 0.8, _pm_ = 0.1, time limit _T_ max 

- 1: _P ←_ initialize with GRD and random feasible variants 

- 2: **while** elapsed_time() _< T_ max **do** 

- 3: select parents by tournament; with prob _pc_ apply one-point crossover 

- 4: mutate with prob _pm_ by reassigning a random _i_ to a random feasible _r_ 

- 5: repair any infeasibility by Proj _F_ ( _·_ ) 

- 6: evaluate _F_ ( _·_ ); form next generation with elitism = 2 

- 7: **end while** 

- 8: **return** best in _P_ 

Tabu search (TS), illustrated in Algorithm 5, explores swap/insertion moves with tabu tenure 10 and aspiration by best; the neighborhood is filtered to maintain feasibility and to prioritize high-risk or overloaded wards. 

**Algorithm 5** TS: Swap/Insertion with Short-Term Memory 

- **Require:** initial _x ←_ GRD; tabu list _T_ ; tenure = 10; maxIter = 300 1: **for** _t_ = 1 **to** maxIter **do** 2: _N_ ( _x_ ) _←_ feasible swap/insertion moves not in _T_ 

- 3: choose _x_<sup>_′_</sup> _∈_ arg min _y∈N_ ( _x_ ) _F_ ( _y_ ) _▷_ aspiration allows tabu if globally best 4: update _T_ with reverse move; drop expired entries 

- 5: _x ← x_<sup>_′_</sup> ; update best if improved 

- 6: **end for** 

- 7: **return** best solution seen 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

18 of 25 

The exact MILP solves the full model in Section 3 using Gurobi Optimizer version 10.0.3 under a 300 s time cap; we report the final objective value and MIPGap. All experiments were conducted on a workstation equipped with an Intel Core i7-12700 CPU @ 2.10 GHz, 32 GB RAM, running Ubuntu 22.04 LTS. Medium instances use GRD warm starts to tighten root bounds, as illustrated in Algorithm 6. 

**Algorithm 6** MILP: Exact Solving with Time/Gap Limit 

**Require:** model min _F_ ( _x_ ) s.t. constraints (2)–(14) 

1: set MIPGap _≤_ 0.01; TimeLimit = 300 s; warm start _←_ GRD 

2: solve with branch-and-bound + cuts; keep incumbent and bound 

3: **return** incumbent solution, best bound, and reported gap 

All local methods (SA, TS, GA-mutation/repair) share a feasibility-preserving neighborhood: (i) swap ( _i ↔ j_ ) across rooms; (ii) move _i_ : _r → r_<sup>_′_</sup> with capacity/isolation checks; (iii) two-swap ( _i_ , _j_ ) across ( _r_ , _r_<sup>_′_</sup> ) targeting risk-gradient improvement or nurse-balance relief. Repairs always prioritize isolation feasibility, then capacity, then incompatibilities. 

### _6.3. Performance Metrics_ 

To evaluate the performance of HRPM–IRC and the comparative baselines, five complementary metrics are used to capture the infection control efficiency, operational cost, workload fairness, computational efficiency, and temporal stability of allocations. All metrics are reported as averages across experimental instances, and lower values generally indicate better performance. 

It is important to clarify that all optimization procedures (HRPM–IRC and baselines) minimize the aggregated normalized multi-objective function defined in Equation (1). The individual objective values _R_ , _T_ , and _W_ reported below are presented solely for analytical interpretation of trade-offs and performance decomposition. They do not correspond to independent single-objective optimizations. 

The first metric, infection risk _R_ , quantifies expected cross-infection exposure: 



<!-- Start of picture text -->
R  = ∑ αr  ∑ πijyijr . (28)<br>r∈R i<j<br><!-- End of picture text -->

Figure 1 shows the distribution of _R_ for all methods on the Lebanese dataset; HRPM–IRC reduces the median risk notably versus GRD and GA. 



**Figure 1.** Infection risk ( _R_ ) distribution by method on the Lebanese dataset. The box plot shows the median, quartiles, and outliers for each method. HRPM–IRC reduces the median _R_ vs. GRD by _∼_ 29% and vs. GA by _∼_ 18%, demonstrating superior infection control performance. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

19 of 25 

Spatial/logistical efficiency is measured by the travel cost _T_ : 



<!-- Start of picture text -->
T = ∑ di , rxi , r . (29)<br>i∈P r ∑ ∈R<br><!-- End of picture text -->

Workload fairness is tracked through imbalance _W_ : 



<!-- Start of picture text -->
un = ∑ br  ∑ xi , r , W = max (30)<br>n∈N un − min n∈N un .<br>r∈R ( n ) i∈P<br><!-- End of picture text -->

Runtime _t_ CPU (seconds) indicates practical deployability; Figure 2 compares runtimes on the medium synthetic set, showing HRPM–IRC remains within operational windows while the exact MILP is capped. 



**Figure 2.** Runtime comparison on Syn-M under equal time budgets. The bar chart shows mean runtime with error bars representing standard deviation. MILP is capped at 300s, while HRPM–IRC operates within practical time windows while maintaining solution quality. 

Temporal stability _S_ measures reallocation volatility via normalized Hamming distance: 



<!-- Start of picture text -->
1<br>St = |P| i ∑ ∈P 1� xi ( , t · ) ̸ = x i ( , t · − 1) �. (31)<br><!-- End of picture text -->

Figure 3 (outbreak scenario) indicates faster stabilization for HRPM–IRC than for GA. 



**Figure 3.** Solution stability across reallocation rounds in the Outbreak scenario. The line plot shows the normalized Hamming distance ( _S_ ) between consecutive allocations. Lower values indicate fewer patient moves; HRPM–IRC stabilizes faster than GA, reducing operational disruption. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

20 of 25 

For each metric, significance is evaluated using non-parametric tests (Wilcoxon, Friedman with Nemenyi), with effect sizes expressed as Cliff’s _δ_ . For ablation-only ranking, we form a normalized composite 



<!-- Start of picture text -->
J = λRR ˆ  +  λT T ˆ  +  λWW ˆ , (32)<br><!-- End of picture text -->

where _λR_ + _λT_ + _λW_ = 1. 

### _6.4. Sensitivity Analysis on Objective Weights_ 

To evaluate the robustness of the proposed multi-objective framework with respect to managerial preference variations, multiple weight configurations were systematically tested. Importantly, in all experiments, the optimization was performed using the aggregated normalized objective defined in Equation (1), ensuring simultaneous optimization of infection risk, cost, and workload fairness. All weights satisfy _w_ 1 + _w_ 2 + _w_ 3 = 1, preserving interpretability as relative policy priorities. 

- Infection-priority regime: ( _w_ 1, _w_ 2, _w_ 3) = (0.6, 0.2, 0.2) 

- Cost-priority regime: (0.2, 0.6, 0.2) 

- Workload-priority regime: (0.2, 0.2, 0.6) 

- Balanced regime: (0.33, 0.33, 0.34) 

In addition to these representative regimes, a grid-based sensitivity sweep was conducted over clinically plausible ranges, where each weight varied between 0.2 and 0.7 (in increments of 0.1) while proportionally adjusting the remaining weights to maintain normalization. This continuous exploration allowed assessment of stability beyond discrete policy scenarios. 

The results demonstrate clear and consistent trade-off behavior: increasing _w_ 1 leads to measurable reductions in infection exposure, with moderate increases in spatial cost; increasing _w_ 2 improves logistical compactness with limited epidemiological degradation; and increasing _w_ 3 reduces workload imbalance without destabilizing infection-control performance. The observed response curves were monotonic and smooth, with no abrupt performance shifts across tested ranges. 

These observations confirm that the proposed weighted-sum structure captures meaningful Pareto-efficient trade-offs, even though a full Pareto-front enumeration is not explicitly generated. The stability of solution patterns across regimes and across continuous weight variations indicates that the framework is robust to moderate and even substantial weight perturbations. 

Furthermore, computational times remained nearly unchanged across all weight configurations, confirming that the multi-objective aggregation does not compromise realtime applicability. 

Overall, this sensitivity study validates that the HRPM–IRC model does not treat objectives independently; rather, it enables policy-driven trade-off navigation within a computationally efficient optimization structure suitable for operational deployment. Hospitals can therefore adjust weights according to outbreak severity, capacity stress, or staffing constraints without risking optimization instability. 

### _6.5. Experimental Scenarios_ 

We consider three representative scenarios derived from the Lebanese dataset: Routine (85% occupancy, 10% isolation), Surge (95% occupancy, 25% isolation, one fewer team), and Outbreak (elevated _πij_ for high-contact pairs). These conditions stress different parts of the objective: infection control dominates in Outbreak, fairness and runtime dominate in 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

21 of 25 

Surge, and spatial efficiency matters most in Routine. Scenarios derived from the Lebanese dataset are shown in Table 3. 

**Table 3.** Scenarios derived from the Lebanese dataset. 

|**Scenario**|**Occupancy **|**Isolation%**|**_πij_ Shock**|**Nurse Availability**|
|---|---|---|---|---|
|Routine|85%|10%|baseline|baseline|
|Surge|95%|25%|+10% high-contact pairs|_−_1 team|
|Outbreak|88%|18%|_×_2 high-contact pairs|baseline|



### _6.6. Statistical Validation_ 

We use the Wilcoxon signed-rank test (pairwise vs. HRPM–IRC), the Friedman test with a Nemenyi post hoc across methods, and Cliff’s _δ_ for effect size ( _α_ = 0.05). Tests are applied to _R_ , _T_ , _W_ across all instances/scenarios. 

### _6.7. Ablation Studies_ 

We analyze three variants: BHH–NoEpi (no epidemiology features), BHH–NoFair ( _ω_ 3 = 0), and BHH–NoMILP (no local MILP refinement). The normalized ablation summary in Figure 4 shows that removing epidemiology features or fairness significantly worsens the composite score, while local MILP refinement contributes meaningfully to quality. 



**Figure 4.** Ablation study results showing normalized composite scores (R + T + W). The bar chart compares full HRPM–IRC against variants without epidemiology features (NoEpi), without fairness (NoFair), and without local MILP refinement (NoMILP). Removing key components degrades overall performance. 

### _6.8. Statistical Outcomes and Managerial Insights_ 

Across all instances, Wilcoxon tests show that HRPM–IRC significantly outperforms baselines on _R_ and _W_ ( _p <_ 0.01). Friedman/Nemenyi ranks HRPM–IRC first with large effect sizes (Cliff’s _δ >_ 0.6). Insights: (i) Infection-aware objectives are essential during outbreaks; (ii) fairness reduces extreme nurse loads without harming _R_ ; (iii) local MILP refinement accelerates convergence in hotspots; (iv) near-real-time runtimes make the approach deployable in Lebanese hospital control rooms. 

## **7. Discussion and Managerial Implications** 

The results of the HRPM–IRC framework demonstrate clear benefits for hospital operations where infection control, equity, and resource efficiency must coexist. This section 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

22 of 25 

interprets the outcomes in the context of practical deployment within Lebanese and similar middle-income hospital systems. 

### _7.1. Operational Interpretation_ 

The significant reduction in modeled infection risk (up to 40% compared with traditional heuristics) implies tangible epidemiological protection in multi-bed wards. In practical terms, the framework’s infection-aware allocations would reduce cross-contamination events, particularly among vulnerable patients in internal medicine and intensive care units. The fairness component ensures that no single nursing team experiences disproportionate workload pressure—a persistent problem in Lebanese hospitals with limited staffing. This balance between infection safety and staff equity is essential for maintaining long-term service quality and morale. 

### _7.2. Trade-Offs Among Objectives_ 

Three critical trade-offs emerge from the analysis: 

1. Infection Risk vs. Fairness: Increasing fairness slightly relaxes infection minimization, since transferring patients between wards for balancing may reintroduce minor risk. However, this trade-off remains acceptable ( _<_ 5% degradation) given the operational benefits. 

2. Infection Risk vs. Computational Speed: Exact MILP solutions achieve minimal risk but require hours for large instances. HRPM–IRC achieves near-optimal solutions ( _<_ 2% gap) within seconds, making it suitable for real-time reallocation. 

3. Fairness vs. Stability: Continuous rebalancing to maintain fairness may cause frequent patient moves; thus, HRPM–IRC includes a stability constraint to preserve continuity of care. 

These trade-offs illustrate how intelligent hyper-heuristics can maintain a dynamic equilibrium between epidemiological safety and operational feasibility. 

### _7.3. Deployment Scenarios_ 

In practical deployment, HRPM–IRC can operate as a decision-support module integrated into hospital management systems: 

- Routine Operations: HRPM–IRC can be used for daily bed allocation and shift-level workload balancing. 

- Surge Events (e.g., COVID-like Outbreaks): The stochastic and robust extensions (Section 4) allow real-time adaptation to rising infection rates and uncertain admissions. 

- Partial Automation: The hyper-heuristic controller can operate in advisory mode, presenting recommended reallocations for approval by infection control officers. 

This integration is feasible within Lebanese hospitals equipped with basic digital infrastructure (e.g., HIS or EMR systems). Pilot tests indicate that the computation time for a 150-patient configuration remains below one minute—well within operational windows for daily scheduling. 

### _7.4. Ethical and Operational Considerations_ 

Implementing algorithmic allocation in healthcare introduces ethical and operational responsibilities: 

- Transparency: HRPM–IRC’s explainability layer ensures traceable reasoning behind assignments, fostering clinician trust. 

- Fairness and Bias: By explicitly modeling workload and infection constraints, the framework prevents bias toward specific wards or teams. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

23 of 25 

- Privacy and Data Governance: All patient data used for learning must be anonymized, consistent with Lebanese Ministry of Public Health standards. 

- Human Oversight: Final decisions should remain under medical supervision; the algorithm serves as a cognitive aid, not a replacement. 

### _7.5. Managerial Insights_ 

From a strategic management perspective, HRPM–IRC enables data-driven infection control by integrating real-time infection risk into allocation decisions, fair workforce utilization through maintaining balanced workloads to reduce burnout, adaptive preparedness via rapid and explainable reallocation during epidemic surges, and operational resilience by combining optimization and learning to sustain hospital throughput under crisis conditions. HRPM–IRC represents a practical step toward AI-augmented hospital management, balancing computational intelligence with human-centered ethics and providing a pathway toward safer, fairer, and more resilient hospital operations. 

## **8. Conclusions and Future Work** 

This study introduced HRPM–IRC, an Epidemiology-Aware Hyper-Heuristic Framework for hospital room and patient matching under constraints of infection risk and workload fairness. By integrating mathematical optimization with bio-inspired learning and epidemiological modeling, HRPM–IRC provides a practical and adaptive decision-support tool for hospital operations, combining a mixed-integer linear model with a bio-inspired hyper-heuristic controller capable of dynamically selecting low-level heuristics in response to infection and workload signals. Experimental results using real Lebanese hospital data and synthetic test beds confirmed that HRPM–IRC achieves up to forty percent reduction in infection risk, balanced nurse workloads, and near-real-time computation, outperforming classical heuristics and metaheuristics. While the framework demonstrates strong empirical performance, limitations include calibration of infection transmission parameters and workload coefficients from a single hospital; assumptions of symmetric infection probabilities and static ventilation effects; and the absence of stochastic discharge times, emergency admissions, and patient preferences. These findings validate the feasibility of intelligent, fairness-aware optimization in resource-limited and high-uncertainty healthcare environments and suggest future directions such as integration with digital twins and IoT systems, multi-period and multi-hospital extensions, deep reinforcement learning controllers, and enhanced explainability to support human and AI collaboration. HRPM–IRC illustrates how bio-inspired hyper-heuristics can bridge epidemiological knowledge and operational scheduling to achieve intelligent, equitable, and resilient hospital resource management. 

While the empirical dataset originates from a single hospital network owing to regulatory access limitations, the framework is modular and transferable. Future work will include multi-site validation to further strengthen cross-institutional generalizability. Nonetheless, the combination of calibrated synthetic scenarios and parameterized model design supports broader applicability. 

**Author Contributions:** Conceptualization, K.D. and W.H.F.A.; methodology, W.H.F.A.; software, K.D.; validation, C.F.R. and W.H.F.A.; formal analysis, W.H.F.A.; investigation, K.D.; resources. W.H.F.A.; data curation, W.H.F.A. and C.F.R.; writing—original draft preparation, K.D.; writing—review and editing W.H.F.A.; visualization, K.D.; supervision, C.F.R.; project administration, W.H.F.A. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Institutional Review Board Statement:** Not applicable. 

**Informed Consent Statement:** Not applicable. 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

24 of 25 

**Data Availability Statement:** The raw data supporting the conclusions of this article will be made available by the authors on request. The anonymized Lebanese hospital dataset used in this study cannot be shared publicly because of privacy regulations and patient confidentiality agreements. 

**Conflicts of Interest:** The authors declare no conflicts of interest. The founders had no role in the design of the study; in the collection, analysis, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results. 

## **References** 

1. Kubde, D.; Badge, A.K.; Ugemuge, S.; Shahu, S. Importance of Hospital Infection Control. _Cureus_ **2023** , _15_ , e50931. [CrossRef] 2. Gordts, B. Models for the organisation of hospital infection control and prevention programmes. _Clin. Microbiol. Infect._ **2005** , _11_ , 19–23. [CrossRef] 

3. Daud-Gallotti, R.M.; Costa, S.F.; Guimarães, T.; Padilha, K.G.; Inoue, E.N.; Vasconcelos, T.N.; Rodrigues, F.; Barbose, E.; Figueiredo, W.; Levin, A. Nursing workload as a risk factor for healthcare associated infections in ICU: A prospective study. _PLoS ONE_ **2012** , _7_ , e52342. [CrossRef] 

4. El Arab, R.A.; Almoosa, Z.; Alkhunaizi, M.; Abuadas, F.H.; Somerville, J. Artificial intelligence in hospital infection prevention: an integrative review. _Front. Public Health_ **2025** , _13_ , 1547450. [CrossRef] 

5. Braaksma, A.; Copenhaver, M.S.; Zenteno, A.C.; Ugarph, E.; Levi, R.; Daily, B.J.; Orcutt, B.; Turcotte, K.M.; Dunn, P.F. Evaluation and implementation of a just-in-time bed-assignment strategy to reduce wait times for surgical inpatients. _Health Care Manag. Sci._ **2023** , _26_ , 501–515. [CrossRef] 

6. Saghafian, S.; Kilinc, D.; Traub, S. Dynamic assignment of patients to primary and secondary inpatient units: Is patience a virtue? In _The Cambridge Handbook of Healthcare Productivity, Efficiency, Effectiveness_ ; Cambridge University Press: Cambridge, UK, 2022. 

7. Drake, J.H.; Kheiri, A.; Ozcan, E. Recent Advances in Selection Hyper-Heuristics. _Eur. J. Oper. Res._ **2020** , _285_ , 405–428. [CrossRef] 8. Shams Eddin, M.; El Hajj, H. An Optimization-Based Framework to Dynamically Schedule Hospital Beds in a Pandemic. _Healthcare_ **2025** , _13_ , 2338. [CrossRef] 

9. Moody, M. _Multi-Factor Mathematical Optimization for Healthcare Referral and Facility Placement_ ; The University of Alabama in Huntsville: Huntsville, AL, USA, 2025. 

10. Yuan, X.; Wang, P.; Liu, J. A novel intelligent approach for infection protection using a multidisciplinary collaboration in regional general hospitals. _Sci. Rep._ **2025** , _15_ , 22639. [CrossRef] [PubMed] 

11. Paul, T.; Paul, T.; Kolay, A. Multi-agent Decision Support Framework for Bed Allocation and Patient Flow Optimization in Hospitals. In Proceedings of the International Conference on Distributed Computing and Intelligent Technology, Bhubaneswar, Odisha, India, 16–19 January 2026; pp. 479–494. 

12. Cignarale, C. Analysis and Optimization of Patient Bed Assignments Within a Hospital. Ph.D. Thesis, Rochester Institute of Technology, Rochester, NY, USA, 2013. 

13. Sundaramoorthi, D.; Rosenberger, J.M.; Chen, V.C.; Buckley-Behan, D.; Kim, S.B. Simulation and patient assignment: Unearthing patterns. _Nurs. Manag._ **2010** , _41_ , 14–16. [CrossRef] 

14. Matos, J.; Rodrigues, P.P. Modeling decisions for hospital bed management—A review. In Proceedings of the International Conference on Health Informatics, Rome, Italy, 26–29 January 2011; Volume 2, pp. 504–507. 

15. He, L.; Madathil, S.C.; Oberoi, A.; Servis, G.; Khasawneh, M.T. A systematic review of research design and modeling techniques in inpatient bed management. _Comput. Ind. Eng._ **2019** , _127_ , 451–466. [CrossRef] 

16. Wang, S.T.; Weng, S.J.; Yeh, T.Y.; Chen, C.H.; Tsai, Y.T. Optimizing Emergency Department Patient Flow Through Bed Allocation Strategies: A Discrete-Event Simulation Study. _Inquiry_ **2025** , _62_ , 469580251335799. [CrossRef] 

17. Read, J.M.; Eames, K.T.D.; Edmunds, W.J. Dynamic social networks and the implications for the spread of infectious disease. _J. R. Soc. Interface_ **2008** , _5_ , 1001–1007. [CrossRef] 

18. Bolaji, A.L.; Bamigbola, A.F.; Adewole, L.B.; Shola, P.B.; Afolorunso, A.; Obayomi, A.A.; Aremu, D.R.; Almazroi, A.A.A. A roomoriented artificial bee colony algorithm for optimizing the patient admission scheduling problem. _Comput. Biol. Med._ **2022** , _148_ , 105850. [CrossRef] 

19. Siahaan, M.; Handiyani, H.; Nurdiana, N. Optimization of the Roles and Responsibilities Infection Prevention Control Nurses in a Government Hospital in Jakarta. _Int. J. Nurs. Health Sci._ **2019** , _6_ , 45–53. 

20. Eastman, D.; Kernan, K. A new patient acuity tool to support equitable patient assignments in a progressive care unit. _Crit. Care Nurs. Q._ **2022** , _45_ , 54–61. [CrossRef] 

21. Jiang, H.; Gomes, P.; Vander Meer, D. Promoting continuity of care in nurse-patient assignment: A multiple objective heuristic algorithm. _Decis. Support Syst._ **2023** , _167_ , 113926. [CrossRef] 

22. Bonaconsa, C.; Mbamalu, O.; Surendran, S.; George, A.; Mendelson, M.; Charani, E. Optimizing infection control and antimicrobial stewardship team communication and patient outcomes. _Am. J. Infect. Control_ **2024** , _52_ , 872–879. [CrossRef] 

https://doi.org/10.3390/a19030205 

_Algorithms_ **2026** , _19_ , 205 

25 of 25 

23. Danach, K. Reinforcement Learning for Dynamic Vehicle Routing Problem: A Case Study with Real-World Scenarios. _Int. J. Commun. Netw. Inf. Secur._ **2024** , _16_ , 580–589. 

24. O’Reilly, M.M.; Krasnicki, S.; Montgomery, J.; Heydar, M.; Turner, R.; Van Dam, P.; Maree, P. Markov decision process and approximate dynamic programming for a patient assignment scheduling problem. _Ann. Oper. Res._ **2025** , _347_ , 1493–1531. [CrossRef] 

25. Danach, K.; Aly, W.H.F. Adaptive Hyperheuristic Framework for Hyperparameter Tuning: A Q-Learning-Based Heuristic Selection Approach with Simulated Annealing Acceptance Criteria. _Eur. J. Pure Appl. Math._ **2025** , _18_ , 6348. [CrossRef] 

26. Teymourifar, A.; Trindade, M.A. Balanced patient assignment to healthcare centres through dispatching rules. _Health Syst._ **2025** , _14_ , 104–118. [CrossRef] 

27. Danach, K.; Rammal, A.; Moukadem, I.; Harb, H.; Nasser, A. Advanced Optimization in E-Commerce Logistics: Combining Matheuristics With Random Forests for Hub Location Efficiency. _IEEE Access_ **2025** . [CrossRef] 

28. Brandt, T. Structural Insights and Efficient Algorithms for the Patient-To-Room Assignment Problem with Equal Rooms. Ph.D. Thesis, RWTH Aachen University, Aachen, Germany, 2025. 

29. Danach, K.; Harb, H.; Rashid, A.S.K.; Al-Tarawneh, M.A.; Aly, W.H.F. Location planning techniques for Internet provider service unmanned aerial vehicles during crisis. _Results Eng._ **2025** , _25_ , 103833. [CrossRef] 

30. Yao, X.; Shehadeh, K.S.; Padman, R. Multi-resource allocation and care sequence assignment in patient management: A stochastic programming approach. _Health Care Manag. Sci._ **2024** , _27_ , 352–369. [CrossRef] [PubMed] 

31. Abbas, Q.; Jeong, W.; Lee, S.W. Explainable AI in Clinical Decision Support Systems: A Meta-Analysis of Methods, Applications, and Usability Challenges. _Healthcare_ **2025** , _13_ , 2154. [CrossRef] [PubMed] 

32. Brandt, T.; Büsing, C.; Engelhardt, F. Patient-to-room assignment with single-rooms entitlements: Combinatorial insights and integer programming formulations. _Eur. J. Oper. Res._ **2025** , _325_ , 20–37. [CrossRef] 

33. Zanazzo, E.; Ceschia, S.; Schaerf, A. Multi-neighborhood simulated annealing for the integrated patient-to-room and nurse-topatient assignment problem. _Flex. Serv. Manuf. J._ **2025** . [CrossRef] 

34. Jedidi, H.; Ben-Romdhane, H.; Nouaouri, I.; Krichen, S. Bi-objective Hospital Bed Assignment Problem in Emergencies. In Proceedings of the International Conference on Decision Aid and Artificial Intelligence (ICODAI 2024), Alecso, Tunisia, 31 October 2024; pp. 136–146. 

35. Dorigo, M.; Stützle, T. _Ant Colony Optimization_ ; MIT Press: Cambridge, MA, USA, 2004. 

36. Castro, L.N.D.; Timmis, J. _Artificial Immune Systems: A New Computational Intelligence Approach_ ; Springer: Berlin/Heidelberg, Germany, 2002. 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

https://doi.org/10.3390/a19030205 

