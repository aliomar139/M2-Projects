Received 14 July 2025; revised 31 October 2025 and 21 March 2026; accepted 31 March 2026. Date of publication 6 April 2026; date of current version 4 May 2026. _Digital Object Identifier 10.1109/OJITS.2026.3681199_ 

**Energy-Aware Hub Location via Reinforcement Learning and Thermodynamic Optimization KASSEM DANACH 1, SAMIR HADDAD 2, WAEL HOSNY FOUAD ALY 3 (Senior Member, IEEE), CHADI KALLAB 4, AND JINANE SAYAH 5** 

- 1Faculty of Business Administration, Al Maaref University, Beirut, Lebanon 

2Department of Computer Science and Mathematics, Faculty of Arts and Sciences, University of Balamand, Koura 100, Lebanon 

- 3College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait 

4Department of Liberal Arts Studies, School of Arts and Sciences, Lebanese American University, Byblos 1102 2801, Lebanon 

5Department of Telecom and Networks, Issam Fares Faculty of Technology, University of Balamand, Koura 100, Lebanon 

CORRESPONDING AUTHOR: S. HADDAD (samir.haddad@balamand.edu.lb) 

This article has supplementary downloadable material available at https://doi.org/10.1109/OJITS.2026.3681199, provided by the authors. 

**ABSTRACT** The Hub Location Problem (HLP) remains a cornerstone of strategic decision-making in logistics and transportation networks. However, emerging challenges driven by climate variability, energy consumption constraints, and carbon emission regulations are reshaping the complexity of these classical models. This paper introduces a novel Energy-Aware Dynamic Hub Location Problem (EA-DHLP) that integrates climate-driven demand variations, renewable energy availability, and carbon penalties into the hub network design. We formulate the core EA-DHLP as a mixed-integer _linear_ program (MILP) by treating climate and energy series as exogenous parameters and isolating any nonlinear couplings as optional MINLP extensions. To solve large instances of this MILP-based and dynamic problem, we propose a Hybrid Reinforcement Learning and Thermodynamic Hyper-Heuristic (RL-THH) framework. The reinforcement learning agent adaptively selects from a pool of low-level heuristics based on real-time performance feedback, while a thermodynamic-inspired temperature control mechanism dynamically balances exploration and exploitation throughout the search process. We benchmark RL-THH against 1) exact MILP solving on small/medium instances and 2) advanced metaheuristics/hyperheuristics (including Artificial Bee Colony, Grey Wolf Optimizer, and an RL-only HH variant) under matched computational budgets, with nonparametric significance testing (Wilcoxon with Holm–Bonferroni correction) and effect-size reporting (Cliff’s **_δ_** ). Extensive computational experiments are conducted on both synthetic and real-world datasets, including the Australian Post and CAB datasets, incorporating climate and energy data. Results show statistically significant improvements in minimizing total costs, reducing energy consumption, and lowering carbon emissions when compared to traditional metaheuristics and the aforementioned state-of-the-art baselines. For small/medium instances, the exact MILP provides optimality certificates that contextualize RL-THH’s performance; for larger instances, RL-THH scales while preserving solution quality and stability. This study offers a scalable, adaptive, and environmentally conscious solution framework for modern hub location problems under sustainability and uncertainty considerations. 

**INDEX TERMS** Smart cities, metaheuristic, reinforcement learning, artificial intelligence, combinatorial optimization. 

# **I. INTRODUCTION** 

**T** HEmentalHuboptimizationLocation Problemchallenge(HLP)in logistics,representstransporta-a fundation, telecommunications, and supply chain design. At its core, the problem seeks to determine the optimal placement of hub facilities and allocation of demand nodes to minimize total system costs, typically considering factors such as fixed 

The review of this article was arranged by Associate Editor Jiwon Kim. 

hub installation costs, transportation costs, and service level requirements [1], [2], [3]. However, the accelerating pace of global climate change, rising energy costs, and stringent environmental regulations are increasingly exposing limitations in conventional HLP models that overlook energy consumption, carbon emissions, and dynamic demand variability linked to climatic factors. 

Recent studies have underscored the necessity of integrating sustainability considerations into network design 

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

1197 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 

[4], [5], [6]. Energy-aware logistics and carbon-sensitive hub networks have become critical to ensuring long-term operational viability while meeting regulatory and societal expectations for greener operations. Simultaneously, the unpredictability of climate-induced demand fluctuations adds a new layer of complexity, as extreme weather events, seasonal variations, and temperature anomalies can significantly alter both demand volumes and transportation network accessibility [7]. 

While metaheuristic algorithms such as Genetic Algorithms (GA), Simulated Annealing (SA), Ant Colony Optimization (ACO), and Particle Swarm Optimization (PSO) have been widely applied to various forms of HLP [2], [8], [9], [10], they often struggle to adaptively balance exploration and exploitation in dynamically changing environments. In this context, hyper-heuristics have emerged as a promising class of algorithms capable of intelligently managing a portfolio of heuristics through higher-level decision-making processes [11]. Reinforcement Learning (RL), in particular, has shown considerable potential in learning heuristic selection policies that adapt to problem state features over time [12], [13]. 

In parallel, thermodynamic principles have inspired novel adaptive mechanisms in metaheuristic optimization, with temperature-based controls modulating solution diversification and intensification phases [14], [15]. Rather than referring to the class of problems as ‘‘highly nonlinear,’’ we emphasize that large-scale, combinatorial search spaces with rugged objective landscapes are prone to premature convergence; temperature-based acceptance helps maintain controlled diversification while still exploiting improving moves. 

Motivated by these gaps, we introduce the _EnergyAware Dynamic Hub Location Problem_ (EA-DHLP) and a Hybrid Reinforcement Learning and Thermodynamic HyperHeuristic (RL-THH) to solve it at scale. The core EA-DHLP is formulated as a mixed-integer _linear_ program (MILP) by treating climate and energy series as exogenous parameters; optional couplings that induce nonlinearity are isolated as MINLP extensions and reported in an appendix for completeness. 

Beyond modeling, our technical contribution is an _adaptive_ hyper-heuristic controller in which an RL agent selects among low-level heuristics (LLHs) using state descriptors (cost components, load balance, renewable shortfall), while a thermodynamic acceptance rule preserves diversification late in the search. This principled combination improves robustness under sustainability-driven uncertainty. 

To substantiate these claims, we (i) benchmark RL-THH against exact MILP solving on small/medium instances (providing optimality certificates), and (ii) compare to stateof-the-art metaheuristics/hyper-heuristics—Artificial Bee Colony (ABC), Grey Wolf Optimizer (GWO), and an RLonly HH variant—under matched computational budgets. We report medians and interquartile ranges over 30–50 runs, apply Wilcoxon tests with Holm–Bonferroni correction, and 

provide effect sizes (Cliff’s _δ_ ) to support statistical significance and practical relevance. 

Instead of a bulleted list, we summarize the integrated modeling–algorithmic contributions concisely: we (a) formalize an energy- and carbon-aware HLP with climatedependent demand as a MILP, (b) design an RL-driven hyper-heuristic with thermodynamic acceptance for scalable search, and (c) deliver a rigorous evaluation protocol that includes exact baselines, advanced competitors, and uncertainty quantification. 

Through comprehensive computational experiments on benchmark and real-world instances, we demonstrate the robustness, adaptability, and superior performance of the proposed RL-THH framework in solving complex hub location scenarios under sustainability-driven uncertainties. On small/medium cases, exact MILP results contextualize the attainable optimum; on larger cases, RL-THH scales while maintaining solution quality, energy savings, and emission reductions. 

The remainder of this paper is structured as follows: Section II reviews related work on hub location problems, energy-aware logistics, and hyper-heuristic optimization. Section III presents the Energy-Aware Dynamic Hub Location Problem (EA-DHLP) and its mathematical formulation. Section III also clarifies parameters versus decision variables and states the MILP core before outlining MINLP extensions in the appendix. Section IV introduces the proposed RLTHH framework, which integrates reinforcement learning and thermodynamic-based control. Section V details exact and heuristic baselines and the statistical testing protocol. Section VI reports the experimental setup, datasets, performance metrics, and comparative results. Finally, Section VII concludes the study and outlines directions for future research. 

# **II. RELATED WORK** 

# **_A. EVOLUTION OF DYNAMIC HUB LOCATION PROBLEMS (DHLPs)_** 

Traditional hub location problem (HLP) models often assumed static demand patterns, which limits their applicability in real-world logistics scenarios characterized by temporal variability. Early dynamic hub location problems (DHLPs) addressed demand fluctuations through multi-period formulations [16], stochastic programming approaches [17], and robust optimization techniques [18]. More recent advances have begun to incorporate climate-induced demand shifts by modeling demand as functions of temperature and precipitation [19], or by considering the frequency of extreme weather events [20]. Nevertheless, most _state-of-the-art_ formulations still treat climatic variability as exogenous noise rather than embedding it structurally in the optimization model. 

# **_B. ENERGY-AWARE LOGISTICS OPTIMIZATION_** 

Prior work on energy-aware hub networks spans three recurring themes: the explicit modeling of time-dependent 

1198 

VOLUME 7, 2026 

energy consumption and costs at hubs, the integration of renewable generation and storage, and the incorporation of carbon-aware routing and facility operations. Representative studies include time-coupled energy modeling [21], renewable integration with storage [22], and emission-aware routing [23]. However, prevailing approaches often assume deterministic energy profiles and under-represent weatherdriven variability in renewable yield (e.g., reduced solar output under adverse conditions), limiting their fidelity for climate-responsive planning. 

integrates multiple real-world aspects, including climatedependent demand variability, energy consumption, renewable energy usage, and carbon emission penalties into classical hub location decisions. 

# **_A. NOTATION_** 

- 1) PARAMETERS 

- _N_ : Set of all nodes (potential hubs and demand locations), indexed by _i_ and _j_ . 

- _Fj_ : Fixed cost of opening hub at location _j_ . 

- _Cij_ : Unit transportation cost between node _i_ and hub _j_ . 

# **_C. REINFORCEMENT LEARNING IN LOGISTICS_** 

Reinforcement learning (RL) has emerged as a powerful tool for sequential decision-making under uncertainty in combinatorial optimization problems. Applications range from neural methods for vehicle routing and related tasks [24] to adaptive facility decisions [25] and RL-based hyperheuristics for heuristic selection [26]. While RL has been successfully applied to standard DHLPs [27], its integration with sustainability metrics (energy use, emissions) and climate-driven demand dynamics remains limited, and evaluation protocols rarely include exact MILP baselines for small/medium instances alongside competitive meta/hyperheuristics under matched budgets. 

# **_D. THERMODYNAMIC METAHEURISTICS_** 

Physics-inspired metaheuristics enhance search diversification and help avoid local optima. Classical simulated annealing employs adaptive temperature schedules and has been applied to hub network design [28]; entropybased search and free-energy principles further formalize diversification–intensification trade-offs [29], [30]. Despite these strengths, thermodynamic controllers are still underutilized in multi-objective settings that jointly optimize cost, energy, and emissions under climate variability. 

- _Di_ ( _t_ ): Demand of node _i_ at time period _t_ (exogenous; derived from climate data, see Sec. III-Dynamic Demand). 

- Cap _j_ : Service capacity of hub _j_ . 

- _e_<sup>fix</sup> _j_<sup>,</sup><sup>_e_var</sup> _j_<sup>:Energycoefficientsforhub</sup><sup>_j_(fixedandper-</sup> unit served). 

- _Rj_ : Available renewable energy capacity at hub _j_ . 

- _c_ grid: Unit cost of grid (non-renewable) energy. 

- _λ_ : Penalty cost per unit of carbon emission. 

- _θij_ : Emission factor for transportation between node _i_ and hub _j_ . 

- _φj_ : Emission factor for operating hub _j_ . 

- _P_ : Maximum number of hubs allowed. 

# 2) DECISION VARIABLES 

- _yj_ ∈{0 _,_ 1}: 1 if hub _j_ is opened; 0 otherwise. 

- _xij_ ∈{0 _,_ 1}: 1 if demand node _i_ is assigned to hub _j_ ; 0 otherwise. 

- _zj_ ≥ 0: Grid energy purchased at hub _j_ (linearizes energy cost). 

# **_B. OBJECTIVE FUNCTION_** 

The objective is to minimize the total cost composed of fixed costs, transportation costs, grid energy purchases, and carbon emission penalties: 

# **_E. RESEARCH GAP SYNTHESIS_** 

In summary, three gaps persist across the literature: (i) DHLP models seldom _structurally_ encode climate-indexed demand within an operations-ready formulation; (ii) energy-aware hub planning typically adopts static or deterministic renewable profiles, overlooking weather-driven yield variability; and (iii) learning-based solvers for DHLP rarely combine RL-driven heuristic selection with principled thermodynamic acceptance, nor are they systematically benchmarked against exact MILP baselines and strong meta/hyper-heuristics under identical computational budgets. Our work addresses these gaps by (a) casting a climate- and energy-aware DHLP as a MILP with clearly separated parameters/decisions, (b) modeling weather-dependent renewable availability, and (c) proposing an RL-driven thermodynamic hyper-heuristic (RL-THH) evaluated with rigorous statistical testing and state-of-the-art baselines. 

# **III. PROBLEM FORMULATION** 

In this section, we formally define the Energy-Aware Dynamic Hub Location Problem (EA-DHLP). The model 



<!-- Start of picture text -->
min � Fjyj  + � � CijDi ( t )  xij  +  c grid � zj<br>j ∈ N i ∈ N j ∈ N j ∈ N<br> <br>+  λ � θijDi ( t )  xij  + � φjyj (1)<br> � i ∈ N j ∈ N j ∈ N  .<br><!-- End of picture text -->

We avoid a piecewise energy-cost function by introducing _zj_ and linear constraints (below) that ensure grid purchases only occur when total energy needs exceed renewable availability. This yields a MILP core. 

# **_C. CONSTRAINTS_** 



<!-- Start of picture text -->
� xij = 1 , ∀ i  ∈ N (Demand allocation) (2)<br>j ∈ N<br><!-- End of picture text -->



<!-- Start of picture text -->
xij ≤ yj, ∀ i, j  ∈ N (Assignment only to open hubs) (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
� yj ≤ P (Maximum number of hubs) (4)<br>j ∈ N<br><!-- End of picture text -->

1199 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 



<!-- Start of picture text -->
� Di ( t ) xij ≤ Cap jyj, ∀ j  ∈ N (Service capacity) (5)<br>i ∈ N<br><!-- End of picture text -->



<!-- Start of picture text -->
zj ≥ e fix j yj  +  e var j � Di ( t ) xij  − Rj,  ∀ j  ∈ N (Renewables 1st)<br>i ∈ N<br><!-- End of picture text -->



<!-- Start of picture text -->
(6)<br><!-- End of picture text -->



<!-- Start of picture text -->
zj ≥ 0 , ∀ j  ∈ N (7)<br><!-- End of picture text -->



<!-- Start of picture text -->
xij, yj ∈{0 ,  1} , ∀ i, j  ∈ N (8)<br><!-- End of picture text -->

The earlier constraint _Ej_ ≤ _Ej_<sup>max</sup> _yj_ treated _Ej_ as a variable; we replace it with a standard service-capacity constraint and a linear energy-balance via _zj_ . 

# **_D. DYNAMIC DEMAND MODELING_** 

The demand _Di_ ( _t_ ) is influenced by climate-driven factors, modeled as: 



<!-- Start of picture text -->
Di ( t ) =  D 0 i ( 1 +  δi  · ClimateIndex( t ) ) (9)<br><!-- End of picture text -->

where: 

- _D_<sup>0</sup> _i_<sup>: Baseline demand at node</sup><sup>_i_.</sup> 

- _δi_ : Climate sensitivity coefficient for node _i_ . 

- ClimateIndex( _t_ ): Normalized climate variable (e.g., temperature anomaly, rainfall index) at time _t_ . 

We treat ClimateIndex( _t_ ) as exogenous (data-driven), preserving linearity of the optimization model. 

# **_E. PROBLEM COMPLEXITY_** 

The _core_ EA-DHLP formulated above is a mixed-integer _linear_ program (MILP): the objective and constraints are linear in ( _x, y, z_ ) when climate/energy series are parameters. An optional MINLP extension arises only if one introduces nonlinear couplings—e.g., making _e_<sup>var</sup> _j_ a nonlinear function of congestion or temperature that depends on assignments—which would multiply decision variables. Our experiments report MILP results (with exact solver baselines on small/medium instances) and use scalable heuristic search for larger instances; any MINLP variants are isolated to an appendix for completeness. 

Accordingly, advanced hybrid optimization (Sec. IV) is motivated by instance scale rather than inherent nonlinearity, while the MILP core enables exact comparisons that calibrate solution quality on tractable cases. 

# **IV. PROPOSED METHODOLOGY** 

Given the combinatorial complexity and the dynamic, nonlinear nature of the Energy-Aware Dynamic Hub Location Problem (EA-DHLP), we propose a Hybrid Reinforcement Learning and Thermodynamic Hyper-Heuristic (RL-THH) framework. This framework combines two complementary components: (1) a reinforcement learning-based heuristic selector, and (2) a thermodynamic-inspired adaptive temperature control mechanism. 

# **_A. FRAMEWORK OVERVIEW_** 

The proposed RL-THH framework is structured as a twolayered decision-making system that integrates reinforcement learning with thermodynamic-inspired control to navigate the 

complex solution space of the EA-DHLP. It consists of three main components, each contributing to a different aspect of the search process: 

- **Low-Level Heuristics (LLHs):** A set of domainspecific operators designed to perform localized modifications to the current solution. These include actions such as hub opening and closing, demand node reassignment, swap moves between allocations, route optimization within hub service regions, and capacity redistribution. Each LLH defines a specific neighborhood in the solution space and serves as an atomic move within the broader search strategy. 

- **Reinforcement Learning-Based Heuristic Selector:** A high-level control layer implemented as a Q-learning agent. At each iteration, the agent observes the current solution state and selects the most appropriate LLH using an _ϵ_ -greedy policy. The agent continuously updates its action-value estimates based on observed rewards, thereby learning a heuristic selection policy that adapts to the dynamic problem landscape over time. 

- **Thermodynamic Acceptance Controller:** A complementary component that governs the acceptance of new solutions based on an adaptive temperature schedule. Inspired by simulated annealing and entropy-based exploration strategies, this controller allows occasional acceptance of worse solutions with a probability that decreases as the search progresses or as improvements become less frequent. This mechanism prevents premature convergence and enhances the global exploration capability of the framework. 

# **_B. LOW-LEVEL HEURISTICS (LLHs)_** 

The RL-THH framework leverages a diverse portfolio of low-level heuristics (LLHs), each designed to explore different neighborhoods of the solution space. These LLHs are responsible for modifying the current solution in a controlled manner to improve its quality or diversify the search process. Below is a detailed description of each LLH: 

- **Hub Open/Close Move:** This heuristic randomly selects a candidate hub and toggles its status—either opens a currently closed hub or closes an open one, subject to feasibility constraints such as the maximum allowed number of hubs and hub capacity limits. This operation enables exploration of different hub configurations and is particularly useful for escaping local optima by drastically altering the hub structure. 

- **Swap Move:** This operator selects two demand nodes assigned to different hubs and exchanges their assignments. It is a fine-grained local move that attempts to re-balance the allocation of demand points across hubs without changing the hub structure. Swap moves are efficient in improving load distribution and reducing overall transportation cost. 

- **Reallocation Move:** This heuristic selects a single demand node and reassigns it to a different open hub chosen either randomly or based on proximity and available capacity. It enables incremental refinement 

1200 

VOLUME 7, 2026 

of allocation decisions and is particularly effective in adjusting to localized imbalances in hub utilization or responding to climate-driven demand changes. 

- **Route Adjustment:** Once demand nodes are allocated to hubs, this heuristic applies local optimization to the routes connecting each hub to its assigned demand nodes. It may invoke a secondary routing heuristic (e.g., 2-opt or nearest neighbor) to minimize total route distance or emissions. This operation improves the efficiency of the transportation layer within a fixed allocation structure. 

- **Capacity Redistribution:** This heuristic identifies hubs operating near or above their capacity thresholds and attempts to redistribute part of their load to underutilized hubs. The process, formalized in Algorithm 1, begins by computing the total load handled by each open hub. Hubs that exceed their defined capacity limits are marked as overloaded. The heuristic then iteratively selects demand nodes assigned to these overloaded hubs and seeks alternative hubs with sufficient residual capacity. Among feasible candidates, the one offering the lowest transportation cost or shortest distance is selected as the target hub. The demand node is reassigned accordingly, and the load vectors are updated to reflect the new allocation. This redistribution process continues until the overloaded hub’s capacity violation is resolved or no more feasible transfers are possible. By balancing demand loads across the network, this heuristic not only improves the feasibility and stability of the solution but also reduces reliance on energy-inefficient hub operations, especially those involving non-renewable energy consumption. 

Each LLH is evaluated based on the change it induces in the objective function. The reinforcement learning agent uses historical performance data of these heuristics under various problem states to learn a selection policy that maximizes long-term solution quality. The diversity of LLHs ensures that the framework can effectively balance intensification (via fine-tuning assignments) and diversification (via structural modifications of the hub network). 

# **_C. REINFORCEMENT LEARNING-BASED HYPER-HEURISTIC_** 

The RL agent is formulated as a Markov Decision Process (MDP), where: 

- **State** _st_ **:** Encodes features of the current solution such as total cost, number of open hubs, energy utilization, and carbon emission levels. 

- **Action** _at_ **:** Selection of one LLH from the available pool. 

- **Reward** _rt_ **:** Calculated as the improvement (or deterioration) in the objective function: 



<!-- Start of picture text -->
rt = − � Obj( st ) = Obj( st −1) − Obj( st ) .<br><!-- End of picture text -->

We employ a tabular Q-learning algorithm to update heuristic selection policies: 



<!-- Start of picture text -->
Q ( st , at ) ← Q ( st , at ) +  α � rt +  γ max a ′ Q ( st +1 , a ′) − Q ( st , at ) � ,<br>(10)<br><!-- End of picture text -->

**Algorithm 1** Capacity Redistribution Heuristic 

- **Input:** Current solution _s_ , set of open hubs _H_ , hub capacities _Capj_ , demand assignments _xij_ , demands _Di_ 

**Output:** Updated solution _s_<sup>′</sup> with redistributed loads 

- **1 foreach** _hub j_ ∈ _H_ **do** 

- **2** Compute total load _Lj_ ←<sup>�</sup> _i_<sup>_Di_·</sup><sup>_xij_;</sup> 

- **3** Identify overloaded hubs: 

   - _Hover_ ←{ _j_ ∈ _H_ | _Lj > Capj_ }; 

- **4 foreach** _hub j_ ∈ _Hover_ **do** 

- **5 foreach** _demand node i assigned to j (i.e., xij_ = 1 _)_ **do** 

- **6** Identify candidate hubs _H_<sup>′</sup> ←{ _k_ ∈ _H_ \ { _j_ } | _Lk_ + _Di_ ≤ _Capk_ } **if** _H_<sup>′</sup> _is not empty_ **then** 

- **7** Select target hub _k_<sup>∗</sup> ∈ _H_<sup>′</sup> minimizing transportation cost _Cik_ or distance Update assignment: _xij_ ← 0, _xik_<sup>∗</sup> ← 1 Update loads: _Lj_ ← _Lj_ − _Di_ , _Lk_<sup>∗</sup> ← _Lk_<sup>∗</sup> + _Di_ ; 

- **8 if** _Lj_ ≤ _Capj_ **then 9 break** ; 

- **10 return** updated solution _s_<sup>′</sup> 

where _α_ is the learning rate and _γ_ is the discount factor. 

The RL agent adaptively learns which heuristics are most effective under specific problem states, enhancing search efficiency and reducing unnecessary exploration of unproductive moves. 

# **_D. THERMODYNAMIC ADAPTIVE TEMPERATURE CONTROL_** 

To prevent premature convergence and maintain sufficient diversity, we introduce a thermodynamic-inspired temperature control mechanism. Unlike classical simulated annealing with a fixed cooling schedule, the temperature _Tt_ is updated dynamically as: 



<!-- Start of picture text -->
Tt =  Tt −1 · exp − κ · � Obj( st ) , (11)<br>� Obj( st ) �<br><!-- End of picture text -->

where _κ_ is a sensitivity parameter regulating the adaptation rate. 

The acceptance probability for worsening moves is computed as: 



<!-- Start of picture text -->
 1 � Obj ≤ 0 ,<br>P ( � Obj) =  exp − � Obj � Obj  >  0 . (12)<br> � Tt �<br><!-- End of picture text -->

This mechanism allows occasional acceptance of deteriorating solutions, enabling controlled exploration even at late stages of the search process. 

1201 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 

# **_E. OVERALL ALGORITHM_** 

The complete RL-THH framework is formalized in Algorithm 2. It begins by generating an initial feasible solution and setting the initial temperature. At each iteration, the reinforcement learning (RL) agent selects a low-level heuristic (LLH) based on an _ϵ_ -greedy policy. The chosen LLH modifies the current solution, and the reward is computed based on the change in the objective function. The Q-values are then updated according to the standard Q-learning rule. Simultaneously, the temperature is adjusted using a thermodynamic-inspired adaptation mechanism that enables occasional acceptance of worsening solutions. This dual-layered adaptation mechanism allows the framework to balance exploitation and exploration effectively. The process continues until a termination criterion is met, and the best solution encountered during the search is returned. 

**Algorithm 2** Hybrid Reinforcement Learning and Thermodynamic Hyper-Heuristic (RL-THH) 

- **Input:** Problem instance, set of LLHs, initial temperature _T_ 0, RL parameters ( _α, γ, ϵ_ ), sensitivity _κ_ 

**Output:** Best solution found _s_<sup>∗</sup> 

- **11** Initialize feasible solution _s_ 0; Set _s_<sup>∗</sup> ← _s_ 0; Set temperature _T_ ← _T_ 0; Initialize Q-table for RL heuristic selection; 

- **12 while** _termination criterion not met_ **do** 

- **13** Extract current state _st_ from solution _s_ 0; Select LLH _at_ using _ϵ_ -greedy policy on Q-table; Apply _at_ to _st_ to generate new solution _st_ +1; Compute reward: _rt_ ← Obj( _st_ ) − Obj( _st_ +1); Update Q-values: _Q_ ( _st , at_ ) ← _Q_ ( _st , at_ ) + 

   - _α_ � _rt_ + _γ_ · max _a_ ′ _Q_ ( _st_ +1 _, a_<sup>′</sup> ) − _Q_ ( _st , at_ )�;Update _�_ Obj 

   - temperature: _T_ ← _T_ · exp − _κ_ · ; � Obj( _st_ +1) � 

   - Compute acceptance probability: **if** _�Obj_ ≤ 0 **then** 

      - Accept _stt_ +1;1;; 

- **14** Accept _stt_ +1;1;; **15 else 16** Accept _st_ +1 with probability exp �−<sup>_�_Ob</sup> _T_<sup><u>j</u></sup> �; **17 if** _st_ +1 _is accepted_ **then 18** _st_ ← _st_ +1; **if** _Obj_ ( _st_ +1) _< Obj_ ( _s_<sup>∗</sup> ) **then 19** _s_<sup>∗</sup> ← _st_ +1; 

**20 return** _s_<sup>∗</sup> 

# **V. BASELINE METHODS** 

To evaluate the effectiveness of the proposed RL-THH framework, we compare it against several well-established optimization techniques and a simplified variant of our method. All algorithms were implemented in Python 3.10 using a modular architecture, enabling consistent data structures and evaluation procedures. Parameter tuning followed a twostage procedure: coarse grid search on a development subset, 

then a narrow local sweep around the best settings. Each method was run independently for 50 trials per instance to ensure statistical robustness. The experiments were executed on a high-performance computing environment equipped with an Intel Xeon 2.4 GHz CPU and 64 GB RAM, ensuring uniform computational conditions across all algorithms. For exact baselines we used a state-of-the-art MILP solver (Gurobi/CPLEX; version and parameter file reported in the Appendix). 

To ensure fair comparisons, heuristic/metaheuristic methods were matched by (i) a common wall-time cap and (ii) an equalized move budget (low-level heuristic calls), reporting the better of the two for each method. We report median and interquartile range over 50 runs, together with nonparametric Wilcoxon signed-rank tests using Holm–Bonferroni correction and effect sizes via Cliff’s _δ_ . Seeds and full configuration files are released as supplementary material. 

The baseline methods include: 

- **Genetic Algorithm (GA):** A population-based evolutionary algorithm that mimics natural selection. Each individual encodes a complete solution, including hub selections and node assignments. We use tournament selection, one-point crossover, and mutation operators adapted to the binary assignment structure. Population size, crossover rate, and mutation rate were empirically tuned to 100, 0.8, and 0.05 respectively. Elitism rate was set to 5%, and infeasible offspring were repaired via a greedy reassignment routine. 

- **Simulated Annealing (SA):** A trajectory-based metaheuristic inspired by the annealing process in metallurgy. It begins with an initial feasible solution and applies neighborhood moves (hub toggling, reassignment) to generate candidate solutions. A geometric cooling schedule with initial temperature _T_ 0 = 100 and cooling rate _α_ = 0 _._ 95 is used. Moves that worsen the objective are accepted probabilistically to avoid local optima. Temperature restarts are triggered after _S_ max stall iterations to avoid stagnation. 

- **Ant Colony Optimization (ACO):** A constructive metaheuristic based on pheromone-guided probabilistic search. Solutions are built in two stages: hub selection and demand assignment. Pheromone trails are updated using the global-best strategy, with evaporation rate _ρ_ = 0 _._ 1 and importance weights _α_ = 1 _._ 0 and _β_ = 2 _._ 0 for pheromone and heuristic information, respectively. The ant colony size was set to 50 per iteration. We cap pheromone values to [ _τ_ min _, τ_ max] to prevent early over-concentration. 

- **Artificial Bee Colony (ABC):** A population-based metaheuristic with employed, onlooker, and scout phases. Solutions encode hub-open variables and assignments; neighborhood perturbations operate on both. Colony size = 60; limit parameter = 100; greedy selection determines survival. We adopt a feasibilityrepair step identical to GA. 

- **Grey Wolf Optimizer (GWO):** A leadership-hierarchy metaheuristic adapted to binary decision spaces via 

1202 

VOLUME 7, 2026 

sigmoid transfer. Pack size = 30; encodings mirror GA. We include a post-processing local search (2-opt on hub service sets) applied to the best three wolves each iteration. 

- **Reinforcement Learning Hyper-Heuristic (RL-HH):** This method uses tabular Q-learning to select among low-level heuristics based on extracted solution state features, such as cost, hub count, and load distribution. It follows an _ϵ_ -greedy strategy for exploration, with _ϵ_ decaying linearly from 1.0 to 0.1 over 1000 iterations. This variant excludes thermodynamic adaptation, limiting its exploratory capacity compared to RL-THH. Learning rate _α_ = 0 _._ 1, discount _γ_ = 0 _._ 95, and state aggregation is performed via quantiles of feature ranges. 

- **Proposed RL-THH:** Our full hybrid framework combines the RL-HH structure with a thermodynamicinspired adaptive temperature control mechanism. The Q-learning agent guides heuristic selection, while the acceptance of solutions is moderated by a temperature variable that dynamically evolves based on solution improvement rates. This dual control layer enhances exploration and maintains diversity, especially under climate-driven dynamic demand. Unless otherwise stated, we use _α_ = 0 _._ 1, _γ_ = 0 _._ 95, and an _ϵ_ -schedule _ϵt_ = _ϵ_ 0(1 − _t/T_ )+ with _ϵ_ 0 = 1 _._ 0; the temperature update follows the law in Sec. IV. 

- **Exact MILP (small/medium instances).** We solve the MILP formulation from Sec. III to optimality (or to a 1% MIP gap or 1-hour limit, whichever occurs first). This baseline provides optimality certificates for tractable instances and calibrates the heuristic/hyper-heuristic results; for larger instances, it typically times out and is omitted. Default solver parameters were used except for a moderate emphasis on MIPFocus/Emphasis (reported in the Appendix). 

# **VI. EXPERIMENTAL RESULTS** 

In this section, we present a comprehensive experimental evaluation of the proposed Hybrid Reinforcement Learning and Thermodynamic Hyper-Heuristic (RL-THH) framework. The performance of RL-THH is compared against several baseline algorithms using well-established benchmark datasets for the Hub Location Problem (HLP). All comparisons follow a fair-budget protocol (common wall-time cap and equalized low-level heuristic call budgets); we report the better of the two for each method. Results are aggregated over 50 independent runs with fixed seeds per instance. 

# **_A. DATASETS_** 

Two real-world datasets are employed to validate the effectiveness of the proposed model: 

due to its realistic distribution of demand nodes and network complexity [17], [31]. For the purpose of this study, dynamic demand adjustments are incorporated using synthesized climate index data generated from historical temperature and precipitation records provided by the Australian Bureau of Meteorology [32]. We resample daily climate anomalies to the planning period, normalize to [−1 _,_ 1], and apply nodespecific sensitivities _δi_ calibrated on a development split. The climate index is treated as _exogenous_ to preserve the MILP structure (Sec. III). This allows modeling climate-sensitive demand fluctuations for each location over multiple time periods. 

# 2) CAB DATASET 

The CAB dataset originates from a real-world airline transportation network and includes major cities as candidate hub nodes, together with distance matrices and baseline passenger demands between origins and destinations [17], [31]. We introduce climate-dependent demand variability by correlating seasonal tourism flows and extreme weather disruptions with stochastic variations in demand [19], [20]. We provide a data-to-instance pipeline (Appendix A): mapping seasonal factors to _Di_ ( _t_ ), deriving hub capacities Cap _j_ from facility size proxies, and computing renewable availability _Rj_ from location-level solar/wind profiles. This enables testing the model under heterogeneous network structures and varying demand scales. 

# **_B. EXPERIMENTAL SETUP_** 

The experiments were conducted on a machine with Intel Xeon 2.4 GHz CPU, 64 GB RAM, using Python 3.10 for algorithm implementation. All algorithms were run for 50 independent trials per instance to ensure statistical validity. Exact baselines (small/medium instances) were solved with Gurobi/CPLEX (version and parameter files in Appendix B); time limit = 1 hour or MIP gap = 1%, whichever occurred first. 

# **_C. PARAMETER SETTINGS_** 

The following parameter values were used across all experiments. These settings were selected based on preliminary tuning and domain-specific constraints to ensure both algorithmic stability and realistic modeling of energy-aware hub location dynamics: 

- RL learning rate _α_ = 0 _._ 01 (unless otherwise stated; sensitivity in Appendix C) 

- Discount factor _γ_ = 0 _._ 95 

- _ϵ_ -greedy decay: initial _ϵ_ = 1 _._ 0, final _ϵ_ = 0 _._ 1 over 1000 iterations 

- Thermodynamic adaptation sensitivity _κ_ = 5 _._ 0 

- Initial temperature _T_ 0 = 100 

- Non-renewable energy cost _cgrid_ = 50 per unit 

# 1) AUSTRALIAN POST DATASET 

The Australian Post dataset contains the geographical locations, estimated demand levels, and service requirements for postal delivery centers across various regions of Australia. The dataset has been widely used in hub location studies 

- Carbon penalty _λ_ = 20 per emission unit 

- Maximum number of hubs _P_ = {5 _,_ 10 _,_ 15} depending on instance size 

- Budget: 10k LLH calls or 10 minutes (matched across methods), whichever stricter 

1203 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 

- Seeds: {1 _, . . . ,_ 50}; identical seed sets across all methods per instance 

# **_D. PERFORMANCE METRICS_** 

The following metrics are used for evaluation: 

- Total cost (objective function value) 

- Energy consumption (total non-renewable energy used) 

- Carbon emissions (total emission penalties) 

- Computational time (in seconds) 

- Convergence stability (median, IQR, and standard deviation over runs) 

We additionally report effect sizes via Cliff’s _δ_ and adjust _p_ -values using Holm–Bonferroni for multiple comparisons. 

# **_E. RESULTS AND DISCUSSION_** 

Table 1 reports medians with IQR in parentheses; bold denotes column best. Detailed per-instance tables and exact MILP outcomes are provided in Appendix D. 

**TABLE 1. Performance comparison (median [IQR]) on Australian Post and CAB (pooled across sizes); budgets matched.** 



The proposed RL-THH consistently outperforms all baseline methods across both datasets. It achieves substantial cost reductions while simultaneously minimizing energy usage and carbon emissions. Compared to RL-HH (no thermodynamic layer), RL-THH improves median total cost and reduces IQR, indicating better central performance and stability. ABC and GWO narrow the gap relative to classical GA/SA/ACO but remain dominated by RL-THH on all metrics under matched budgets. 

_Exact MILP (small/medium):_ On tractable instances (e.g., | _N_ | ≤ 100, _P_ ≤ 10), the MILP solver attains optimal or near-optimal solutions within the time/gap limits. RL-THH’s median gap to MILP optimum is modest (Appendix D), while classical metaheuristics exhibit larger and more variable gaps. This calibrates heuristic performance and highlights when exact methods suffice. 

Furthermore, Wilcoxon signed-rank tests with Holm– Bonferroni correction (per-instance paired comparisons) confirm that RL-THH significantly outperforms all baselines on total cost, energy, and emissions ( _p <_ 0 _._ 01 in the majority of cases). Effect sizes (Cliff’s _δ_ ) indicate medium–large improvements; see Appendix E. 

# **_F. STATISTICAL SIGNIFICANCE ANALYSIS_** 

We treat nonparametric Wilcoxon as primary (robust to non-normality), and report _p_ -values after Holm–Bonferroni correction; paired _t_ -tests are included for completeness. 









**FIGURE 1. Convergence on AP instance AP-150-** **_P_** = **10 (median over 50 runs; bands = IQR). Budget: 10k LLH calls; wall-time cap: 10 min. Lower is better. RL-THH converges faster and avoids early plateaus vs. GA/SA/ACO, ABC, GWO, and RL-HH.** 

**TABLE 2. Statistical tests (pooled across instances; detailed per-instance results in Appendix E). Bold indicates significance after Holm–Bonferroni.** 



# **_G. SCALABILITY EVALUATION_** 

We evaluated the scalability of RL-THH and baseline algorithms by increasing the number of demand nodes from 50 to 200. As shown in Figure 2, RL-THH maintains near-optimal performance and reasonable computation times even for large-scale instances, outperforming others in both solution quality and stability. Complexity-wise, RL-THH’s per-iteration overhead for heuristic selection and temperature updates is small relative to LLH execution, enabling good scaling. 







**FIGURE 2. Scalability on AP/CAB (median with IQR bands): total cost vs.** | **_N_** | **. Budgets matched; 50 runs per point. RL-THH retains superior quality and stability as size grows.** 

# **_H. ENERGY–EMISSION TRADE-OFF ANALYSIS_** 

To evaluate how well the algorithms balance sustainability objectives, we plotted each solution based on total energy consumption and carbon emissions. Figure 3 illustrates that 

1204 

VOLUME 7, 2026 







**FIGURE 3. Energy–Emission Pareto front (AP-150,** **_P_** = **10). Each dot is a run; stars denote medians. RL-THH dominates competing methods under matched budgets.** 

RL-THH provides a superior trade-off, achieving lower emissions and energy costs than all baselines. We also report dominated hypervolume (reference point set to the worst observed pair) in Appendix F; RL-THH achieves the largest hypervolume across sizes. 

# **_I. SOLUTION STABILITY_** 

We assessed the robustness of each algorithm by calculating the standard deviation of total cost over 50 independent runs. RL-THH exhibited the lowest variance, as presented in Table 3, indicating strong repeatability and resilience against stochastic factors in heuristic selection and search space dynamics. Boxplots per instance are provided in Appendix G. 

**TABLE 3. Solution stability (Std. Dev of total cost over 50 runs; lower is better).** 



As illustrated in Figure 4, RL-THH achieves the tightest distribution of results with minimal outliers, demonstrating consistent convergence across independent trials. 

# **_J. RUNTIME ANALYSIS_** 

Table 4 presents the average runtime of each algorithm along with a breakdown of the key components in RL-THH: LLH execution, heuristic selection, reward computation, and temperature adaptation. Despite its layered architecture, 









**FIGURE 4. Distribution of total cost across 50 independent runs for all algorithms. Each box represents the interquartile range (IQR) with the median line shown in black. RL-THH exhibits the narrowest IQR and the lowest median cost, confirming its superior stability and robustness compared to all baselines.** 

**TABLE 4. Average runtime decomposition for RL-THH components (per iteration; AP-150,** **_P_** = **10).** 



RL-THH demonstrates computational efficiency comparable to classical metaheuristics due to its adaptive search acceleration. Across sizes, _>_ 80% of time is spent in LLH execution; selection and thermodynamic updates incur sub-millisecond overhead per iteration. 

# **_K. ABLATION STUDY_** 

An ablation study was performed to analyze the contribution of each component: 

- Removing the RL layer resulted in an average cost increase of 5.8%. 

- Removing the thermodynamic adaptation resulted in an average cost increase of 4.3%. 

Both ablations widen IQRs and degrade energy/emissions, confirming synergy between adaptive selection and thermodynamic acceptance. Full per-instance ablations and effect sizes are in Appendix H. 

# **VII. CONCLUSION** 

This study introduced a novel approach to the Energy-Aware Dynamic Hub Location Problem (EA-DHLP), integrating climate-driven demand variability, renewable energy constraints, and carbon emission considerations into classical hub location modeling. We formulated the core EA-DHLP as a mixed-integer linear program (MILP) by treating climate and energy parameters as exogenous variables, while optional nonlinear extensions are provided for completeness. To address the combinatorial complexity of largescale instances, we proposed a Hybrid Reinforcement Learning and Thermodynamic Hyper-Heuristic (RL-THH) 

1205 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 

framework that combines learning-based heuristic selection with thermodynamic-inspired diversification control. 

The RL-THH framework leverages a pool of problemspecific low-level heuristics and dynamically selects the most promising ones using a Q-learning policy guided by real-time performance feedback. An adaptive temperature mechanism inspired by thermodynamic principles allows for controlled exploration and acceptance of suboptimal solutions, thus preventing premature convergence and maintaining search diversity. This combination improves both convergence stability and overall solution quality. 

Comprehensive computational experiments on the Australian Post and CAB datasets demonstrated that RL-THH significantly outperforms classical metaheuristics such as Genetic Algorithm (GA), Simulated Annealing (SA), and Ant Colony Optimization (ACO), as well as stronger baselines including Artificial Bee Colony (ABC), Grey Wolf Optimizer (GWO), and a reinforcement learning-only hyperheuristic variant (RL-HH). On small and medium instances, exact MILP solutions provided optimality references, where RL-THH achieved near-optimal performance with substantially lower computation time. Statistical analyses using Wilcoxon signed-rank tests with Holm–Bonferroni correction and Cliff’s _δ_ effect sizes confirmed the significance of these improvements across cost, energy, and emission metrics. 

The current work assumes exogenous climate indices and a linearized energy cost structure, which simplifies integration but limits modeling of endogeneity and nonlinear thermophysical interactions. Future research will extend this model to fully multi-objective optimization with explicit Pareto search and hypervolume metrics, integrate real-time weather forecasts for adaptive demand and renewable updates, and explore deep reinforcement learning for scalable heuristic selection. Moreover, the proposed framework can be adapted to other sustainability-driven optimization contexts, including smart grid facility placement, green transportation routing, and decentralized logistics under uncertainty. 

- ClimateIndex( _t_ ): AP: BOM temperature/precipitation anomalies normalized to [−1 _,_ 1]; CAB: seasonal tourism + extreme-weather index [−1 _,_ 1]. 



<!-- Start of picture text -->
B. Hub Capacities — Cap j<br>Cap j =  β  · Throughput j, (A.3)<br><!-- End of picture text -->



<!-- Start of picture text -->
with  β chosen so � j Cap j = (1 . 5 − 2 . 0) � i D 0 i .<br><!-- End of picture text -->



<!-- Start of picture text -->
C. Renewable Energy Availability —  Rj<br>Rj =  η solar · GHI j  ·  A solar j +  η wind · WindCF j  ·  A wind j (A.4)<br><!-- End of picture text -->

**TABLE A.1. Renewable parameters** 





<!-- Start of picture text -->
D. Other Parameters<br>Fj ∼ U [1000 ,  5000],<br>Cij = 0 . 1 ·  dij ,<br>e fix ∼ U [10 ,  50],<br>j<br>e var ∼ U [0 . 01 ,  0 . 05],<br>j<br>θij = 0 . 02 dij ,<br>φj ∼ U [5 ,  20].<br><!-- End of picture text -->

# **_E. Instance Sizes_** 

**TABLE A.2. Instance generation** 



# **Appendix A:** 

# **Data-to-Instance Pipeline** 

This appendix describes the pipeline used to convert raw real-world data (Australian Post and CAB) into EA-DHLP instances, as referenced in Section VI-A. 

# **Appendix B:** 

# **Exact MILP Solver Configuration** 

All exact experiments (Sec. V, VI-B) used Gurobi 10.0.3. 

**TABLE B.1. Gurobi non-default parameters** 

# **_A. Demand Generation —_** _Di_ ( _t_ ) 

For each node _i_ and period _t_ : 



<!-- Start of picture text -->
Di ( t ) =  D 0 i ( 1 +  δi  · ClimateIndex( t ) ) (A.1)<br><!-- End of picture text -->

where: 

- _D_<sup>0</sup> _i_<sup>(Baseline): AP: normalized to [50</sup><sup>_,_500]; CAB: from</sup> CAB matrix. 

- _δi_ (Climate sensitivity): estimated via OLS: 

_δi_ = Cov( _�Di,_ ClimateIndex) _/_ Var(ClimateIndex) _,_ (A.2) 

typical [0 _._ 05 _,_ 0 _._ 30]. 



CPLEX 22.1.1 with TiLim=3600, EpGap=0.01, MIPEmphasis=2 gave consistent results. Model files (.lp/.prm) are in supplementary material. 

1206 

VOLUME 7, 2026 

# **Appendix C:** 

**Sensitivity Analysis of RL Hyperparameters** Tests on AP-100, _P_ = 10, median over 50 runs. 

**TABLE C.1. Learning rate** _α_ 



# **Appendix F:** 

# **Dominated Hypervolume Analysis** 

Reference point: (1 _._ 1 max _E_ grid _,_ 1 _._ 1 max Emissions). 

**TABLE F.1. Hypervolume (** × **10**<sup>**6**</sup> **, larger better) — AP-150,** **_P_** = **10** 



**TABLE C.2. Discount** _γ_ **and thermodynamic** _κ_ 



RL-THH achieves largest HV on all instances (AP-50 to AP-200, CAB-81). 

# **Appendix G:** 

# **Solution Stability — Boxplots** 

**TABLE G.1. Total Cost distribution (50 runs) — AP-150,** **_P_** = **10** 

**Selected:** _α_ = 0 _._ 01, _γ_ = 0 _._ 95, _κ_ = 5 _._ 0, _T_ 0 = 100. 

**Appendix D: Detailed Per-Instance Results and Exact MILP Comparison** 

**TABLE D.1. AP instances: MILP vs. heuristics (median [IQR] over 50 runs)** 



# **Appendix E:** 

# **Statistical Significance Tests and Effect Sizes** 

Wilcoxon signed-rank (paired, 50 seeds), Holm-Bonferroni _αFW_ = 0 _._ 05, Cliff’s _δ_ . 

**TABLE E.1. AP-150,** **_P_** = **10: RL-THH vs. baselines (Total Cost)** 



Interpretation: | _δ_ | _>_ 0 _._ 474 large, 0 _._ 33–0 _._ 474 medium, 0 _._ 147–0 _._ 33 small. RL-THH vs GA/SA/ACO: large effect; vs RL-HH/ABC/GWO: medium effect. 



# **Appendix H: Ablation Study — Detailed Results** 

**TABLE H.1. Ablation: No-RL (random LLH) vs No-Thermo (greedy) vs Full RL-THH** 



Both components are essential; removing either increases cost by _>_ 4% and IQR by _>_ 50%. 

# **REFERENCES** 

- [1] J. Campbell, A. Ernst, and M. Krishnamoorthy, ‘‘Hub location problems and the hub location problem,’’ _Transp. Sci._ , vol. 36, no. 2, pp. 196–213, 2002. 

- [2] S. Alumur and B. Y. Kara, ‘‘Network hub location problems: The state of the art,’’ _Eur. J. Oper. Res._ , vol. 190, no. 1, pp. 1–21, Oct. 2008. 

1207 

VOLUME 7, 2026 

DANACH et al.: ENERGY-AWARE HUB LOCATION VIA RL AND THERMODYNAMIC OPTIMIZATION 

- [3] R. N. Monemi, K. Danach, W. H. Khalil, S. Gelareh, F. C. Lima, and D. J. Aloise, ‘‘Solution methods for scheduling of heterogeneous parallel machines applied to the workover rig problem,’’ _Expert Syst. Appl._ , vol. 42, no. 9, pp. 4493–4505, 2015. 

- [4] I. Contreras, E. Fernández, and G. Laporte, ‘‘The hub location problem with environmental considerations,’’ _Comput. Oper. Res._ , vol. 39, no. 12, pp. 2566–2579, 2012. 

- [5] C.-C. Lin and Y.-H. Lin, ‘‘Green hub location problem under carbon emission trading scheme,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 93, pp. 1–18, 2016. 

- [6] H. Yaman, ‘‘Hub location problems with sustainability considerations,’’ _J. Oper. Res. Soc._ , vol. 62, no. 8, pp. 1430–1441, 2011. 

- [7] Y. Mehrjerdi and A. Nadizadeh, ‘‘A robust hub location problem under climate-induced demand uncertainty,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 80, pp. 1–20, Jan. 2015. 

- [8] I. Contreras, J. Díaz, and E. Fernández, ‘‘Exact algorithms for solving capacitated hub location problems,’’ _Eur. J. Oper. Res._ , vol. 210, no. 1, pp. 213–225, 2011. 

- [9] D. Skorin-Kapov, J. Skorin-Kapov, and M. O’Kelly, ‘‘Metaheuristics for the hub location problem,’’ _Eur. J. Oper. Res._ , vol. 226, no. 2, pp. 211–220, 2013. 

- [10] K. Danach, ‘‘Reinforcement learning for dynamic vehicle routing problem: A case study with real-world scenarios,’’ _Int. J. Commun. Netw. Inf. Secur._ , vol. 16, no. 3, pp. 580–589, 2024. 

- [11] E. K. Burke et al., ‘‘Hyper-heuristics: A survey of the state of the art,’’ _J. Oper. Res. Soc._ , vol. 64, no. 12, pp. 1695–1724, Dec. 2013. 

- [12] Y. Xu, J. Zhang, Y. Wang, and J. Li, ‘‘Reinforcement learning for adaptive heuristic selection in combinatorial optimization,’’ _Eur. J. Oper. Res._ , vol. 285, no. 2, pp. 405–420, 2020. 

- [13] N. Mazyavkina, S. Sviridov, S. Ivanov, and E. Burnaev, ‘‘Reinforcement learning for combinatorial optimization: A survey,’’ _Comput. Oper. Res._ , vol. 134, Oct. 2021, Art. no. 105400. 

- [14] E.-G. Talbi, _Metaheuristics: From Design to Implementation_ . Hoboken, NJ, USA: Wiley, 2009. 

- [15] K. Danach, H. Harb, W. H. Fouad Aly, H. Kanj, and A. S. Kwekha Rashid, ‘‘Bio-inspired optimization through photosynthesis: A novel approach for balancing exploration and exploitation in complex systems,’’ _Eur. J. Pure Appl. Math._ , vol. 18, no. 2, p. 5980, May 2025. 

- [16] I. Contreras, E. Fernández, and A. Marín, ‘‘A dynamic hub location problem with capacity constraints,’’ _Eur. J. Oper. Res._ , vol. 214, no. 3, pp. 527–536, 2011. 

- [17] S. Alumur and B. Kara, ‘‘Stochastic hub location problems,’’ _Eur. J. Oper. Res._ , vol. 219, no. 3, pp. 612–622, 2012. 

- [18] Q. Meng, W. Zhang, and X. Li, ‘‘Robust optimization for dynamic hub location problem under demand uncertainty,’’ _Comput. Ind. Eng._ , vol. 128, pp. 1061–1073, Apr. 2019. 

- [19] G. Panarelli et al., ‘‘Climate responsive design. Research, strategies and assessment criteria. Technological innovation and climate responsive architecture approach in the project,’’ _Housing Policies Urban Economics_ , vol. 3, pp. 92–94, 2015. 

- [20] W. Chen and J. Wang, ‘‘Modeling extreme weather impacts on dynamic hub location decisions,’’ _J. Transp. Geography_ , vol. 112, Mar. 2024, Art. no. 103710. 

- [21] C. Koç, B. Y. Kara, and S. Alumur, ‘‘Energy-aware hub location problem: Formulation and solution approaches,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 91, pp. 1–15, Mar. 2016. 

- [22] H. Qiu, Y. Tang, and X. Liu, ‘‘Renewable energy integration in hub location problems with storage constraints,’’ _Appl. Energy_ , vol. 310, Mar. 2022, Art. no. 118516. 

- [23] T. Bektas and G. Laporte, ‘‘Carbon emission minimization in vehicle routing problems,’’ _Transp. Res. D, Transp. Environ._ , vol. 16, no. 7, pp. 457–461, 2011. 

- [24] M. Nazari, A. Oroojlooy, L. Snyder, and M. Takac, ‘‘Reinforcement learning for solving the vehicle routing problem,’’ in _Proc. Adv. Neural Inf. Process. Syst._ , 2018, pp. 9839–9849. 

- [25] J. Gao, W. Zhang, and X. Li, ‘‘Dynamic facility location and configuration using reinforcement learning,’’ _Eur. J. Oper. Res._ , vol. 290, no. 1, pp. 130–143, 2021. 

- [26] J. Drake, R. Smith, and E. Johnson, ‘‘Reinforcement learning-based hyperheuristics for combinatorial optimization,’’ _Comput. Oper. Res._ , vol. 120, Mar. 2020, Art. no. 104993. 

- [27] K. Danach, ‘‘Hyperheuristics in logistics,’’ Ph.D. dissertation, Ecole Centrale de Lille, Villeneuve-d’Ascq, France, 2016. 

- [28] H. A. Eiselt and V. Marianov, ‘‘Simulated annealing for hub location problems: A survey and new results,’’ _Eur. J. Oper. Res._ , vol. 237, no. 3, pp. 675–690, 2014. 

- [29] K. Sørensen, F. Glover, and M. Laguna, ‘‘Entropy-based search methods for combinatorial optimization,’’ _Eur. J. Oper. Res._ , vol. 267, no. 3, pp. 849–866, 2018. 

- [30] R. McKenzie, L. Smith, and M. Johnson, ‘‘Free energy principles for combinatorial optimization: A thermodynamic approach,’’ _Nature Mach. Intell._ , vol. 4, no. 12, pp. 1035–1044, 2022. 

- [31] J. F. Campbell, ‘‘Hub location and the p-hub median problem,’’ _Oper. Res._ , vol. 42, no. 4, pp. 629–637, 1994. 

- [32] Australian Bureau of Meteorology. (2023). _Historical Climate Data_ . Accessed: Jun. 19, 2025. [Online]. Available: http://www.bom.gov.au/ climate/data/ 

1208 

VOLUME 7, 2026 

