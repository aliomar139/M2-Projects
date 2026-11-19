Discover Sustainability 

### RESEARCH | Article in Press 

# **Multi-objective optimization for energy-aware job scheduling in industry 4.0** 

## **Kassem Danach · Hani Haidoura · Ali Mansour · Abbass Nasser** 

Received: 12 April 2026 / Accepted: 15 September 2026 © The Author(s) 2026 

#### **Abstract** 

Energy-aware flexible job-shop scheduling is a key optimization problem in Industry 4.0 manufacturing, where machine assignment and operation sequencing jointly influence production efficiency, energy consumption, and resource utilization. This paper addresses a multi-objective flexible job-shop scheduling problem with heterogeneous machines, machine-operation compatibility, precedence constraints, non-preemptive processing, and machine-capacity limitations. A mixed-integer linear programming (MILP) model is developed to simultaneously minimize makespan, processing-related energy consumption, and machine workload imbalance. Workload imbalance is conceptually characterized by the standard deviation of machine utilization, while a linear absolute-deviation surrogate is used in the MILP to preserve model tractability. To efficiently solve large-scale instances, a two-phase hybrid optimization framework is proposed. In the first phase, an adaptive hyper-heuristic dynamically selects constructive, improvement, and perturbation heuristics while maintaining a non-dominated solution archive. In the second phase, selected archive solutions are refined using a normalized weighted-sum MILP formulation with warm-start initialization to improve solution quality and provide optimality-gap information. The warm-start solutions are provided as incumbent solutions rather than fixed decision variables, allowing the MILP to modify machine assignments, operation sequencing, and start times during refinement. The proposed framework is evaluated using industrial and synthetic flexible job-shop scheduling instances and compared with NSGA-II, MOEA/D, dispatching-rule heuristics, a standalone adaptive hyper-heuristic, and a single-objective MILP baseline. All methods are evaluated using the same objective definitions and final non-dominated filtering procedure. For the multi-objective methods, the final external archives are additionally evaluated using hypervolume (HV), inverted generational distance (IGD), and spacing. Experimental results demonstrate consistent improvements in both objective values and Pareto-front quality. Compared with NSGA-II, the proposed method reduces makespan by 4.3%, energy consumption by 8.1%, and workload imbalance by 8.0%, while improving hypervolume by 18.1% and reducing inverted generational distance by 63.4%. Relative to the best single-phase baseline, improvements reach 6.5%, 21.6%, and 13.4% for makespan, energy consumption, and workload imbalance, respectively. The Pareto-quality results further indicate improved convergence, coverage, and distribution of the obtained non-dominated solutions. Statistical analysis confirms that these improvements are significant. The proposed hybrid framework provides an 

This Article in Press is shared early to give you faster access to new research. It is citable and carries a permanent DOI. The final edited version will replace it automatically. 

Hani Haidoura, Ali Mansour and  Abbass Nasser are equally contributed to this work. 





Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

effective and reproducible approach for balancing productivity, energy efficiency, and resource utilization in sustainable Industry 4.0 manufacturing systems. 

**Keywords** Flexible job-shop scheduling · Industry 4.0 · Energy-aware scheduling · Multi-objective optimization · Hyper-heuristics · MILP 

## **1 Introduction** 

### **1.1 Background and motivation** 

Industry 4.0 has revolutionized manufacturing by integrating automation, cyber–physical systems (CPS), and the Industrial Internet of Things (IIoT) [1, 2]. This transformation enables high connectivity, real-time data acquisition, and intelligent decision-making across the entire production lifecycle, creating the foundation for datadriven optimization and adaptive control [3]. The convergence of Artificial Intelligence (AI), robotics, cloud computing, and big data has further reshaped traditional production environments into smart factories capable of dynamic reconfiguration, predictive control, and mass customization [4, 5]. 

However, these technological advancements also introduce complex challenges in production planning and control. Heterogeneous machine configurations, variable processing times, and fluctuating demand patterns necessitate advanced scheduling strategies capable of managing both operational complexity and uncertainty. Among these challenges, job scheduling plays a pivotal role in determining overall throughput, energy consumption, and cost efficiency, thereby directly affecting productivity and sustainability [2, 6]. 

Modern scheduling problems must therefore balance multiple and often conflicting objectives–such as minimizing makespan, reducing energy consumption, and ensuring fair resource utilization–particularly under dynamic, data-rich industrial conditions [3, 7, 8]. In addition, the growing global emphasis on sustainability and regulatory compliance has made energy-aware decision-making an integral component of production optimization [9]. 

To meet these challenges, recent research increasingly combines metaheuristics, hyper-heuristics, and mathematical programming into hybrid optimization frameworks that are scalable, adaptive, and sustainability-oriented. These frameworks enable flexible, real-time decision-making while preserving theoretical optimality guarantees under Industry 4.0 paradigms [3, 5, 6, 10, 11]. 

### **1.2 Problem statement** 

Traditional job scheduling approaches–whether based on exact methods (e.g., branch-and-bound or Mixed Integer Linear Programming (MILP)) or on heuristics–often optimize a single performance criterion, typically the makespan (overlook other essential factors, notably energy efficiency and machine workload balance, which are central to 𝐶𝐶max). Although effective for small-scale or isolated cases, such mono-objective formulations tend to sustainable manufacturing within Industry 4.0.Let 𝒥𝒥𝒥 {𝐽𝐽1, 𝐽𝐽2, … , 𝐽𝐽𝑛𝑛} represent the set of _n_ independent jobs to be processed on a set of _m_ heterogeneous machines ℳ= {𝑀𝑀1, 𝑀𝑀2, … , 𝑀𝑀𝑚𝑚}. Each job 𝐽𝐽𝑗𝑗 comprises a sequence of operations 𝑂𝑂𝑗 **𝑗** , 𝑂𝑂𝑗 **𝑗** , … , 𝑂𝑂𝑗 𝑗𝑗<sup>, where 𝐾𝐾𝑗𝑗 is the</sup> number of operations within 𝐽𝐽𝑗𝑗. Each operation 𝑂𝑂𝑗 **𝑗** can be executed only on a compatible subset of machines, with processing times 𝑝𝑝𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>and energy consumption rates 𝑒𝑒</sup> 𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>that depend on the selected machine 𝑀𝑀𝑖𝑖.</sup> ● The decision variables are defined as follows:𝑥𝑥𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>∈{0, 1}: a binary variable equal to 1 if operation 𝑂𝑂𝑗</sup><sup>**𝑗**is assigned to machine 𝑀𝑀𝑖𝑖, and 0 otherwise,</sup> **𝑗 𝑗** 

**𝑗**<sup>**𝑗**</sup> ● 𝑠𝑠𝑗 **𝑗** : start time of operation 𝑂𝑂𝑗 **𝑗** , 1 ●● ̄ 𝑈𝑈𝑈𝑈𝑈 𝑖𝑖: total active processing time of machine 𝑚𝑚<sup>∑</sup> 𝑖𝑚𝑚 1<sup>𝑈𝑈𝑖𝑖: average utilization across all machines.</sup> 𝑀𝑀𝑖𝑖, 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

The objective is to construct a feasible schedule that respects precedence and capacity constraints while optimizing the following three conflicting goals: 

#### 1. **Makespan minimization:** 



<!-- Start of picture text -->
(1)<br>min 𝐶𝐶max = max𝑗 𝑗 𝑗 𝑗 𝑗𝑗 (𝑠𝑠𝑗 𝑗 + 𝑝𝑝 𝑗 𝑗𝑗 𝑗 ),<br>𝑗 𝑗<br><!-- End of picture text -->

(1) **𝑗 𝑗 𝑗**<sup>**𝑗**</sup> where (𝑠𝑠𝑗 **𝑗** + 𝑝𝑝𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>) represents the completion time of operation 𝑂𝑂𝑗</sup><sup>**𝑗**on machine 𝑀𝑀𝑖𝑖. This constraint limits the total</sup> production horizon and ensures time-efficient scheduling. 

#### 2. **processing-related energy consumption:** 



<!-- Start of picture text -->
𝑛𝑛 𝐾𝐾𝑗𝑗 𝑚𝑚<br>∑ ∑ ∑ (2)<br>min 𝐸𝐸𝑡 𝑡 𝑡 𝑡 𝑡𝑡 = 𝑗 𝑗 𝑥𝑥𝑗𝑗𝑘𝑘 𝑖𝑖 𝑝𝑝 𝑗𝑗𝑘𝑘 𝑖𝑖 𝑒𝑒 𝑗𝑗𝑘𝑘 𝑖𝑖 ,<br>𝑘𝑘𝑗𝑗 𝑖𝑖𝑗𝑗<br><!-- End of picture text -->

which quantifies the processing-related energy consumed by scheduled operations. To maintain model tractability and preserve linearity, the MILP objective explicitly models machine-dependent processing energy. Idle and ramp-up energy components are considered during post-schedule evaluation using machine-specific energy profiles, but they are not directly included as decision-dependent terms in the linear MILP objective. 

#### 3. **Machine utilization balance:** 



<!-- Start of picture text -->
√<br>√√ 1 𝑚𝑚<br>∑ (3)<br>⎷ 𝑖 𝑖<br>min 𝜎𝜎𝑢𝑢 = (𝑈𝑈 𝑖𝑖 𝑚̄ 𝑈 𝑈 2 ,<br>𝑚𝑚𝑚1<br><!-- End of picture text -->

**𝑈** where workload balance. Because the standard-deviation expression introduces a nonlinear term into the optimization 𝜎𝜎𝑢𝑢 measures the dispersion of machine utilization and is used as the standard statistical formulation of model, the MILP formulation subsequently employs a linear absolute-deviation surrogate based on auxiliary variables 𝑑𝑑𝑖𝑖. This formulation, hereafter referred to as the Multi-Objective Energy-Aware Job Scheduling Problem (MO- 

This formulation, hereafter referred to as the Multi-Objective Energy-Aware Job Scheduling Problem (MOEAJSP), captures several industrial realities that are typically neglected in simplified formulations: 

- **Heterogeneous machine capabilities:** Processing times and energy consumption vary significantly among machines. 

- **Non-preemptive and sequential operations:** Operations within each job must follow strict precedence without interruption. 

- **Energy-profile awareness:** Machines may exhibit active, idle, and ramp-up energy states. In the present MILP, processing-related energy is optimized directly, while idle and ramp-up components are evaluated after schedule construction using machine-specific energy profiles. 

- **Objective conflicts:** Minimizing makespan may increase energy usage or create load imbalance; thus, multiobjective optimization is essential. 

Unlike prior models assuming homogeneous machine characteristics or fixed energy prices, this study explicitly models realistic energy-aware scheduling with heterogeneous resources. The proposed framework integrates adaptive exploration via hyper-heuristics with exact MILP-based refinement to ensure both scalability and precision in solution quality. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

### **1.3 Research objectives** 

This research aims to: 

- Formulate a comprehensive MILP model that jointly optimizes makespan, processing-related energy consumption, and workload balance under realistic industrial constraints; 

- Develop a hybrid Hyper-Heuristic–MILP framework that adaptively selects and combines low-level heuristics based on performance feedback while leveraging MILP to refine incumbent schedules and provide optimalitygap information under predefined solver tolerances and runtime limits; 

- Validate the proposed approach using both real industrial datasets and statistically generated synthetic instances to assess scalability, robustness, and generalization. 

### **1.4 Contributions** 

The novelty of this work does not arise from the isolated use of MILP, hyper-heuristics, or energy-aware scheduling, since these techniques have been studied individually in the literature. Rather, the contribution lies in their integrated use for a multi-objective, energy-aware job scheduling problem with heterogeneous machines, operation-level eligibility, workload balancing, and MILP-based warm-start refinement. The main contributions are summarized as follows: 

- A hybrid Hyper-Heuristic–MILP framework is proposed in which an adaptive Pareto-based hyper-heuristic first explores the scheduling space and generates a set of non-dominated schedules, which are then used as warm-start solutions for exact MILP refinement. 

- An enhanced operation-level MILP formulation is developed for the multi-objective energy-aware job scheduling problem. The model incorporates machine eligibility, operation precedence, machine-capacity constraints, machine-dependent processing times, processing-related energy consumption, an energy-budget constraint, and a linear workload-balancing objective. 

- A Pareto-aware adaptive hyper-heuristic mechanism is designed to dynamically select among constructive, improvement, and perturbation heuristics using a reward mechanism based on normalized multi-objective improvement and archive contribution. 

- A normalized weighted-sum MILP refinement strategy is used to improve representative non-dominated schedules obtained from the hyper-heuristic phase, thereby combining global search diversification with exact local improvement. 

- A comprehensive computational evaluation is conducted using industrial-inspired and synthetic instances, including comparisons with heuristic-only scheduling, single-objective MILP, and state-of-the-art multi-objective metaheuristics such as NSGA-II, MOEA/D, and MOPSO. 

## **2 Literature review** 

### **2.1 Job scheduling in smart manufacturing** 

Job scheduling in smart manufacturing has witnessed significant evolution due to the integration of Industry 4.0 technologies such as cyber-physical systems, Industrial Internet of Things (IIoT), and advanced automation [1, 2, 12]. These advancements enable unprecedented connectivity, flexibility, and data-driven decision-making, transforming traditional manufacturing into intelligent, adaptable systems. Early scheduling approaches were primarily deterministic and single-objective, focusing on optimizing makespan or throughput under stable and 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

controlled conditions [13]. However, the inherent variability and uncertainty in modern manufacturing environments have necessitated more sophisticated methods. 

The dynamic nature of smart manufacturing demands stochastic scheduling techniques that address uncertainties such as machine breakdowns, variable processing times, and unpredictable job arrivals [6, 14, 15]. This shift reflects a need to accommodate real-time data streams and system disturbances, which are emblematic of Industry 4.0 factories. 

Moreover, multi-objective scheduling methods have gained traction to reconcile conflicting goals including production efficiency, cost reduction, energy consumption, and resource utilization [7, 8, 16]. These methods often incorporate heterogeneous machine capabilities and real-time operational constraints, leveraging AI-based metaheuristics, hyper-heuristics, and machine learning for adaptive and scalable optimization [3, 10, 11]. Recent studies specifically highlight multi-robot task allocation and flexible job shop scheduling under Industry 4.0 constraints, emphasizing the importance of integrating advanced scheduling within Manufacturing Execution Systems (MES) for real-time responsiveness and precision [2, 17]. 

The increasing complexity of scheduling problems in smart manufacturing is addressed via hybrid optimization frameworks combining exact mathematical programming (e.g., MILP) with heuristic or metaheuristic search to balance solution quality and computational efficiency [17, 18]. These integrated approaches are pivotal for handling the combinatorial nature of scheduling in environments with diverse machines, energy-aware operation, and intricate precedence relationships. 

In summary, the existing literature reveals a clear progression from deterministic, single-objective scheduling models toward dynamic, multi-objective, and energy-aware optimization frameworks for Industry 4.0 manufacturing. While exact optimization methods provide optimality guarantees for small and medium-sized instances, their computational complexity limits their applicability to large-scale industrial problems. Conversely, heuristic and metaheuristic approaches offer superior scalability but generally sacrifice solution optimality and provide limited theoretical guarantees. Consequently, recent research has increasingly focused on hybrid optimization frameworks that combine the strengths of exact mathematical programming and adaptive search methods. Motivated by this trend, the present work proposes a hybrid Hyper-Heuristic–MILP framework that exploits the scalability of adaptive hyper-heuristics together with the solution refinement and optimality-gap assessment provided by MILP, thereby addressing the practical requirements of energy-aware multi-objective scheduling in Industry 4.0 manufacturing environments. “‘ 

### **2.2 Energy-aware scheduling** 

The growing emphasis on sustainability has led to the development of energy-aware scheduling models that integrate energy consumption metrics alongside traditional manufacturing performance objectives [12, 19]. These models address the environmental impact by explicitly considering energy use, costs, and carbon emissions during production planning stages. 

Recent research has further investigated operational strategies that reduce energy consumption through intelligent machine control policies [20]. One notable direction is the application of machine switch-off strategies, where idle machines are temporarily powered down during sufficiently long inactive periods to reduce nonproductive energy consumption. Such policies have demonstrated considerable energy savings while maintaining acceptable production performance, highlighting the importance of incorporating machine operational states into scheduling decisions. 

Recent systematic energy-aware scheduling frameworks jointly optimize production schedules and renewable energy availability, enabling factories to reduce both operational costs and carbon emissions while maintaining production efficiency [21]. These studies demonstrate that energy-aware scheduling is evolving beyond machinelevel optimization toward factory-wide energy management under dynamic energy supply conditions. 

Several trade-off strategies have been proposed to balance minimizing energy consumption and maintaining production efficiency or service levels, often formulating the problem as a multi-objective optimization that 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

generates Pareto optimal fronts representing feasible compromises between conflicting goals [7, 19, 22]. For example, scheduling models commonly seek to reduce processing-related energy consumption and peak power demand while controlling makespan or tardiness, reflecting realistic operational priorities. Energy-aware scheduling approaches typically rely on detailed energy consumption profiles for individual machines, including both active machining energy and idle consumption [8, 19]. Idle energy waste, which can amount to a significant fraction of total energy use, motivates the integration of machine ON/OFF strategies or power state transitions to minimize unnecessary consumption [15, 19]. However, many existing methods do not fully incorporate machine-level constraints such as maximum allowable power limits, workload balance, or the impact of frequent machine state changes on equipment wear and operational stability [8, 19]. Recent advancements explore hybrid scheduling frameworks combining offline optimization with online rescheduling driven by real-time data and renewable energy availability, enhancing robustness and energy efficiency in dynamic manufacturing scenarios [15, 22]. These methods leverage cyber-physical systems and data analytics to adapt schedules based on fluctuating energy prices, intermittent renewable supply, and evolving production states. 

Recent NSGA-II-based approaches have targeted very similar tri-objective sets. For example, authors in [23] propose an improved NSGA-II with adaptive mutation and energy-aware chromosome repair for makespan, energy consumption (including idle periods), and workload balance. While the method demonstrates good performance on moderate-sized instances, it remains purely metaheuristic and exhibits premature convergence and constraint-violation issues under tight instantaneous power limits and high machine heterogeneity–limitations also observed in our own NSGA-II baseline. 

Nevertheless, challenges persist in developing scalable models that can manage the combinatorial complexity of real-world scheduling, accurately model heterogeneous energy consumption behaviors, and balance multidimensional objectives including energy, production, and machine utilization [18, 19]. Addressing these gaps is crucial for realizing environmentally sustainable manufacturing aligned with Industry 4.0 paradigms. 

### **2.3 Energy-aware flexible job-shop scheduling and hybrid optimization** 

The problem addressed in this study belongs to the family of flexible job-shop scheduling problems (FJSPs), in which each operation can be processed by one of several eligible machines with machine-dependent processing times. Compared with conventional job-shop scheduling, FJSPs introduce an additional assignment decision and are therefore significantly more complex. Recent studies have extended FJSP formulations by incorporating energy consumption, carbon emissions, peak-demand management, renewable-energy availability, machine switch-off policies, and workload-balancing objectives. Energy-aware FJSP studies generally differ according to the adopted energy model. Some consider only processing energy, whereas others include idle energy, setup energy, machine-state transitions, or time-of-use electricity tariffs. These modeling choices directly affect the formulation and computational complexity. The present study considers active and idle energy consumption while assuming that machines remain powered on during the planning horizon. Therefore, machine shut-down and ramp-up decisions are outside the current scope. 

Multi-objective energy-aware FJSPs are commonly solved using evolutionary algorithms, such as NSGAII and MOEA/D, as well as decomposition methods, variable-neighborhood search, tabu search, and hybrid metaheuristics. Exact MILP models are valuable for small and medium instances because they provide rigorous bounds, but their computational cost increases rapidly as the number of operations and alternative machines grows. Consequently, matheuristics that combine heuristic exploration with exact optimization have attracted increasing attention. 

Selection-based hyper-heuristics are particularly relevant because they choose among several low-level heuristics according to search feedback instead of relying on one fixed metaheuristic. However, relatively limited work has combined archive-based multi-objective hyper-heuristic search with an explicitly defined Pareto-oriented 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

MILP refinement procedure for energy-aware flexible job-shop scheduling. This motivates the hybrid framework proposed in this study. 

### **2.4 Mathematical modeling** 

MILP formulations are widely used to rigorously model complex scheduling problems involving multiple objectives and operational constraints [24]. MILP enables exact optimization by encoding scheduling decisions, precedence relations, resource capacities, and objective trade-offs into linear inequalities with integer and continuous variables. When computational resources permit, MILP methods provide optimal or near-optimal solutions with strong theoretical guarantees. 

In manufacturing, MILP has been successfully applied across diverse contexts, including job-shop scheduling, batch process scheduling, production and maintenance integration, and blending optimization [18, 25, 26]. For example, refinery production scheduling models employ MILP to determine optimal operation modes, sequencing, and inventory levels under capacity and demand constraints [25]. Similar MILP models have been formulated for preventive maintenance scheduling combined with production plans [27] and for project scheduling with complex resource consumption and production profiles [13, 28]. 

However, MILP models face well-known scalability challenges in large-scale, real-time manufacturing scenarios. The combinatorial growth in decision variables and constraints leads to exponential increases in solution times, limiting MILP’s direct applicability to highly complex or time-critical problems [18]. Additionally, representing intricate nonlinearities, stochastic uncertainties, and multi-objective trade-offs often requires model simplifications or relaxations that may affect solution quality or realism. 

To overcome these limitations, research has increasingly focused on hybrid methods that combine MILP with heuristic, metaheuristic, or decomposition techniques [18]. These approaches use heuristics to generate highquality initial solutions or to restrict the MILP search space, thereby improving computational tractability while preserving solution accuracy. Decomposition strategies split large problems into smaller subproblems solved iteratively or hierarchically, enabling scalable scheduling across multiple machines or time horizons. 

Combining MILP with adaptive search techniques like hyper-heuristics harnesses the advantages of both approaches: heuristics enable flexible and efficient exploration of complex solution spaces, while MILP delivers exact refinement and guarantees on solution optimality [6, 18]. Such hybrid methodologies show great potential for Industry 4.0 manufacturing contexts, which feature heterogeneous machinery, energy-conscious objectives, and rapidly changing operating conditions. 

In summary, while MILP remains a cornerstone for exact production scheduling optimization, addressing its scalability and complexity challenges through hybridization and problem decomposition is essential for practical deployment in modern smart manufacturing environments. 

### **2.5 Metaheuristics and hyper-heuristics** 

Metaheuristics constitute a broad class of flexible and powerful optimization methods designed to effectively explore large and complex solution spaces typical in production scheduling problems. Common metaheuristics include genetic algorithms (GAs), simulated annealing (SA), tabu search (TS), and variable neighborhood search (VNS) [10]. These approaches leverage mechanisms inspired by natural processes–such as evolution, annealing of metals, or memory structures–to escape local optima and enhance global search capabilities. 

Genetic algorithms mimic natural selection by iteratively evolving a population of candidate solutions through crossover, mutation, and selection operators, which helps balance exploration and exploitation. Simulated annealing probabilistically accepts worse solutions early in the search to avoid premature convergence, gradually reducing this acceptance over time. Tabu search uses a memory structure to avoid cycling and encourages exploration of new solution neighborhoods, while variable neighborhood search systematically changes the neighborhood structure to escape local traps. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

Hyper-heuristics operate at a higher level than traditional metaheuristics by dynamically selecting, generating, or combining low-level heuristics or metaheuristic operators based on their observed performance [11, 29]. This adaptive mechanism enables the solution method to self-tune during the search, enhancing robustness and generality across different problem instances without extensive manual adjustment. Hyper-heuristics can be classification-based, selection-based, or generation-based, each implementing different strategies to manage heuristic adaptation [30, 31]. 

In the context of Industry 4.0, characterized by complex, multi-objective scheduling problems involving heterogeneous machines, dynamic job arrivals, and energy-aware constraints, hyper-heuristics offer significant advantages. Their ability to adaptively combine heuristics makes them scalable and flexible for handling varying operational conditions and multiple conflicting objectives such as minimizing makespan, energy consumption, and machine wear. 

However, a major limitation of standalone metaheuristic and hyper-heuristic approaches is the lack of formal guarantees on solution optimality or feasibility, which can be critical in high-stakes manufacturing environments. Moreover, while metaheuristics tend to produce near-optimal solutions efficiently, they may struggle to fully exploit problem-specific constraints or achieve precise refinement when the search space grows exceedingly large [32]. 

This challenge motivates the integration of hyper-heuristics with exact optimization methods, such as MILP solvers. Hybrid frameworks leverage the complementary strengths of these approaches: hyper-heuristics facilitate effective search space exploration and initial solution construction by adaptively selecting and combining low-level heuristics, while exact methods provide rigorous solution verification and refinement to guarantee optimality or improve solution bounds [6, 18, 33]. 

Such synergy is especially relevant for multi-objective, energy-aware scheduling in Industry 4.0 smart manufacturing, where problem complexity, heterogeneous machine capabilities, and stringent accuracy demands coexist [2, 5]. Hybrid hyper-heuristic–MILP frameworks have demonstrated advantages in handling large-scale, dynamic scheduling problems by balancing scalability and solution quality [34]. 

Recent advances have further incorporated machine learning techniques within metaheuristic and hyperheuristic frameworks to enhance adaptive capabilities and automate heuristic selection and generation [22, 35, 36]. Deep reinforcement learning (DRL) approaches, for example, learn effective heuristic policies from problem-specific feedback without manual design, improving exploration-exploitation balance and scalability for dynamic, large-scale scheduling scenarios [15, 35]. These intelligent metaheuristics enable real-time adaptation to system state changes, renewable energy availability, and evolving production conditions, positioning them as key components of future smart manufacturing optimization toolsets [3]. 

Recent surveys on Industry 4.0 and Industry 5.0 scheduling indicate that multi-objective metaheuristics continue to dominate large-scale manufacturing optimization because of their flexibility and scalability [3]. Population-based algorithms such as NSGA-II, MOEA/D, particle swarm optimization, and evolutionary algorithms remain widely adopted for balancing conflicting objectives including makespan, energy consumption, carbon emissions, and machine utilization. At the same time, adaptive hyper-heuristics have emerged as a promising alternative by automatically selecting and coordinating multiple low-level heuristics instead of relying on a single search strategy. 

From a scheduling perspective, recent studies have increasingly focused on flexible job-shop scheduling, energy-aware scheduling, and multi-objective production planning under heterogeneous machine environments. Multi-objective evolutionary algorithms such as NSGA-II, MOEA/D, and MOPSO have been widely used to approximate Pareto fronts involving makespan, energy consumption, tardiness, carbon emissions, and machine workload balance. In parallel, matheuristic and hybrid exact–heuristic approaches have emerged to improve solution quality by combining metaheuristic exploration with MILP-based refinement or decomposition. However, most existing approaches either rely on a fixed metaheuristic structure or use MILP only as a standalone exact solver. Fewer studies explicitly combine adaptive selection hyper-heuristics with Pareto-archive management and MILP warm-start refinement for multi-objective energy-aware job scheduling with heterogeneous machines. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

Overall, the combination of hyper-heuristics, exact MILP optimization, and machine learning creates robust, scalable, and precise frameworks capable of meeting the complex and sustainable manufacturing scheduling needs in Industry 4.0 environments. 

Table 1 summarizes representative studies from the literature according to their scheduling problem, energy representation, machine heterogeneity, solution methodology, and validation scale. The comparison focuses particularly on the combination of adaptive Hyper-Heuristic search, Pareto-archive management, and MILP-based warm-start refinement, which distinguishes the proposed framework from the reviewed approaches. 

### **2.6 Research gap** 

Despite substantial progress in energy-aware scheduling, multi-objective metaheuristics, and MILP-based production optimization, several interconnected research gaps persist that limit the practical deployment of intelligent scheduling in Industry 4.0 smart manufacturing environments. These gaps can be identified across three complementary dimensions: modeling completeness, algorithmic design, and operational deployment. 

From a modeling perspective, many existing energy-aware scheduling formulations focus narrowly on makespan and energy consumption while overlooking workload balance among heterogeneous machines. This omission can lead to unbalanced machine usage, increased equipment wear, and suboptimal resource allocation in real production environments. Moreover, several existing models assume homogeneous machine characteristics or fixed energy profiles, which do not reflect the diverse operational conditions encountered in modern smart factories. 

|**Table 1**Comparative<br>summary of representative<br>energy-aware and multi-|Reference|Problem /<br>Objectives|Energy model|Machine<br>heterogeneity /<br>Eligibility|<br>Solution method|Key char-<br>acteristics /<br>Validation|
|---|---|---|---|---|---|---|
|objective job-shop schedul-<br>ing studies and the present<br>work|[7,8,19]|JSP / FJSP; makes-<br>pan + energy|Processing + idle|Limited /<br>homogeneous|Metaheuristics (GA,<br>NSGA-II); no adap-<br>tive archive-based HH<br>or MILP refinement|<br>Mostly<br>synthetic<br>instances|
||[12,18,<br>23]|Energy-aware<br>FJSP; makespan +<br>energy + tardiness|Processing + idle<br>/ switch-off|Partial<br>eligibility|NSGA-II and hybrid<br>metaheuristics; no<br>archive-based HH–<br>MILP refinement|Medium-<br>scale<br>synthetic<br>instances|
||[20,21]|Energy-aware<br>scheduling; energy<br>+ carbon / cost|Machine<br>ON/OFF +<br>renewables|Limited|Exact and metaheuris-<br>tic approaches<br>fl|Case-study<br>validation|
||[15,22]|Dynamic / cyber-<br>physical schedul-<br>ing; makespan +<br>energy|Real-time energy<br>prices|Heterogeneous<br>machines<br>considered|<br>Hybrid offline–online<br>approaches|Simula-<br>tion-based<br>validation|
||[18,37]|Large-scale<br>scheduling;<br>multi-objective|Varies|Heterogeneous<br>machines|<br>Hybrid metaheuris-<br>tic–MILP approaches;<br>partial decomposition-<br>based refinement|Large<br>synthetic<br>instances|
||[5,6,38,<br>39]|Manufacturing<br>scheduling; mul-|Limited / varies|Varies|Hyper-heuristic<br>approaches; lim-|Mostly<br>synthetic|
|||tiple objectives|||ited archive-based<br>selection|instances|
||**Present**<br>**study**|**MO-EAJSP;**<br>**makespan +**<br>**processing-related**<br>**energy + utiliza-**<br>**tion imbalance**|**Processing**<br>**energy opti-**<br>**mized; idle/**<br>**ramp-up energy**<br>**evaluated**<br>**post-schedule**|**Fully het-**<br>**erogeneous**<br>**machines**<br>**with eligibil-**<br>**ity and**<br>**capacity**<br>**constraints**|**Adaptive selection-**<br>**based HH + Pareto**<br>**archive + normal-**<br>**ized weighted-sum**<br>**MILP warm-start**<br>**refinement**|**Industrial**<br>**Lebanon**<br>**instance +**<br>**synthetic**<br>**instances**<br>**up to 700**<br>**jobs**|



Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

From an algorithmic perspective, standalone metaheuristics and hyper-heuristics offer scalability and flexibility but generally lack exact refinement and certified optimality-gap information, which is important for high-stakes manufacturing decisions. Conversely, MILP models provide rigorous optimization but become computationally prohibitive for large-scale, multi-objective scheduling problems due to the combinatorial growth of decision variables and constraints. Existing hybrid approaches that combine heuristic and exact methods rarely integrate Pareto-based adaptive hyper-heuristic exploration with MILP warm-start refinement within a unified framework that jointly optimizes production efficiency, energy consumption, and workload balance. 

From a practical deployment perspective, factory operators require scheduling tools that are simultaneously responsive to sudden disruptions and capable of rigorous long-term energy planning. Standalone MILP solvers are often too slow for real-time edge deployment on the shop floor, while standalone heuristics lack the precision required to guarantee strict energy-budget compliance and workload fairness. This disconnect between algorithmic capability and operational requirements creates a critical barrier to the adoption of optimization-based scheduling in Industry 4.0 environments. 

To address these interconnected gaps across modeling, algorithmic, and deployment dimensions, this study proposes a hybrid Hyper-Heuristic–MILP framework. The framework employs an adaptive hyper-heuristic that generates diverse non-dominated schedules through Pareto-based exploration, followed by a MILP refinement stage that improves selected schedules using normalized scalarization and warm-start initialization. By decoupling the search process into an adaptive heuristic phase for rapid exploration and an exact refinement phase for precision improvement, the proposed framework simultaneously improves makespan, processing-related energy consumption, and machine utilization balance while maintaining computational tractability. This two-phase architecture also provides a viable blueprint for edge-cloud collaborative scheduling in smart factories, where the lightweight heuristic phase handles real-time responsiveness on edge devices and the MILP phase supports strategic optimization on centralized computing infrastructure. 

## **3 Problem formulation** 

### **3.1 System description** 

The manufacturing environment under consideration consists of a finite set of machines ℳ= {𝑀𝑀1, 𝑀𝑀2, … , 𝑀𝑀𝑚𝑚} and a set of jobs 𝒥𝒥𝒥 {𝐽𝐽1, 𝐽𝐽2, … , 𝐽𝐽𝑛𝑛} to be processed. Notation consistency is maintained with previous sections. Each job 𝐽𝐽𝑗𝑗 ∈ 𝒥𝒥 is composed of an ordered sequence of operations 𝒪𝒪𝑗𝑗 = {𝑂𝑂𝑗 **𝑗** , 𝑂𝑂𝑗 **𝑗** , … , 𝑂𝑂𝑗 𝑗𝑗<sup>}, where 𝐾𝐾𝑗𝑗 denotes the number</sup> of operations in job may only be executed on a subset of eligible machines, reflecting technological compatibility, skill, or tooling 𝐽𝐽𝑗𝑗. Operations are processed according to strict precedence constraints, and each operation requirements. 

The processing of each operation consumes both time and energy, where the MILP explicitly accounts for machine-dependent processing energy. Additional energy components associated with idle and ramp-up states are retained for post-schedule evaluation and industrial interpretation. 

### **3.2 Assumptions** 

The following assumptions are made to ensure model tractability while preserving industrial realism: 

- Processing and setup times are deterministic and derived from historical production logs or sensor data. 

- Machine availability is fixed throughout the planning horizon; preventive maintenance and unscheduled breakdowns are not considered at this stage. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

- Processing-related energy consumption for each machine–operation pair from machine telemetry data. Idle and transition-state energy values are available for post-schedule evaluation (𝑖 **𝑖** 𝑖𝑖𝑗 **𝑗** ) is measurable or estimated but are not directly optimized in the MILP formulation. 

- Preemption of operations is not allowed; once started, an operation must continue until completion. 

● Resource availability (e.g., tools, fixtures, or operators) is assumed constant throughout the scheduling horizon. These assumptions correspond to a static, single-period scheduling horizon commonly used in initial Industry 4.0 modeling before dynamic extensions are introduced. 𝒪𝒪𝒪Before presenting the MILP formulation, the main notation is clarified to ensure consistency. Let {𝑂𝑂𝑗 ∶𝑗𝑗 ∈ 𝒥 **𝒥** 𝒥𝒥𝒪𝒥𝒥𝒥𝒥𝒥𝒥𝑗𝑗} denote the complete set of operations. Each operation 𝑂𝑂𝑗 **𝑗** can be processed only on a subset of eligible machines ℳ𝑗 **𝑗** ⊆ ℳ. The processing time of operation 𝑂𝑂𝑗 **𝑗** on machine 𝑀𝑀𝑖𝑖 is denoted by 𝑝𝑝𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>, and the corresponding processing-energy coefficient is denoted by 𝑒𝑒</sup> 𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>. The total processing-related energy</sup> budget over the scheduling horizon is denoted by 𝐸𝐸max. A sufficiently large positive constant used in the disjunctive sequencing constraints is denoted by 𝑀𝑀<sup>𝐵𝐵</sup> to avoid confusion with the machine set ℳ. The average machine workload is denoted by ̄𝑈𝑈. 

### **3.3 Multi-objective optimization strategy** 

The proposed scheduling problem simultaneously considers three conflicting objectives: minimizing makespan, minimizing processing-related energy consumption, and balancing machine utilization. Since a conventional MILP solver optimizes a single objective at a time, the proposed framework adopts a hybrid two-stage optimization strategy. 

During the first stage, the adaptive Hyper-Heuristic explores the search space by dynamically selecting lowlevel heuristics according to their historical performance. This exploration generates a diverse set of feasible scheduling solutions representing different trade-offs among the three objectives. 

During the second stage, these candidate schedules are provided to the MILP solver as warm-start solutions for exact refinement. The MILP improves each candidate while satisfying all scheduling constraints. After refinement, Pareto dominance is applied to identify the non-dominated schedules. A solution is considered Paretoefficient if no other feasible solution improves one objective without degrading at least one of the remaining objectives. The resulting archive of refined non-dominated schedules forms the approximated Pareto frontier used throughout this study. 

### **3.4 MILP model** 

The proposed scheduling problem is formulated as a mixed-integer linear programming model at the operation level. The model determines the machine assignment, operation start times, completion times, and sequencing decisions while minimizing makespan, processing-related energy consumption, and the linearized workloadbalance objective. 

#### **_Decision variables_** 

- 𝑆𝑆𝑗𝑗 **𝑗** ≥ 0: start time of operation 𝑂𝑂𝑗: start time of operation 𝑂𝑂𝑗𝑂𝑂𝑗𝑗 **𝑗** . 

- ● 𝐶𝐶𝑗𝑗 **𝑗** ≥ 0: completion time of operation : completion time of operation 𝑂𝑂𝑗 **𝑗** 

- 𝑆𝑆𝑗𝑗 **𝑗** ≥ 0: start time of operation 𝑂𝑂𝑗: start time of operation 𝑂𝑂𝑗𝑂𝑂𝑗𝑗 **𝑗** . 

- ● 𝐶𝐶𝑗𝑗 **𝑗** ≥ 0: completion time of operation : completion time of operation 𝑂𝑂𝑗 **𝑗** . ● 𝐶𝐶max ≥ 0: makespan of the complete schedule. ● 𝑋𝑋𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>∈{0, 1}: equals 1 if operation 𝑂𝑂𝑗</sup><sup>**𝑗**is assigned to machine 𝑀𝑀𝑖𝑖, and 0 otherwise.</sup> ● 𝑌𝑌𝑗<sup>𝑖𝑖</sup> **𝑗** 𝑗𝑗𝑗<sup>′</sup> 𝑗𝑗<sup>′∈{0, 1}: equals 1 if operation 𝑂𝑂𝑗</sup><sup>**𝑗**is processed before operation 𝑂𝑂𝑗𝑗′𝑘𝑘′ on machine 𝑀𝑀𝑖𝑖, and 0 otherwise.</sup> ● 𝑈𝑈 𝑖𝑖 ≥ 0: total workload assigned to machine 𝑀𝑀𝑖𝑖. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

● chine workload.𝑑𝑑𝑖𝑖 ≥ 0: auxiliary variable representing the absolute deviation of machine 𝑀𝑀𝑖𝑖’s workload from the average ma- 

The MILP component serves as an exact refinement mechanism rather than an independent multi-objective optimizer. Each candidate schedule generated by the adaptive Hyper-Heuristic is refined while preserving feasibility. The refined schedules are then evaluated according to the three optimization objectives, and only the non-dominated solutions are retained. To maintain the linear structure of the MILP, workload balance is represented using a linear absolute-deviation formulation. The standard-deviation measure defined in Section 3.2 is therefore used as the conceptual measure of workload dispersion, whereas the MILP optimizes its linear surrogate. This surrogate measures the total absolute deviation of machine workloads from the average machine workload. **_Objective components_** The three objective components are defined as follows. 



<!-- Start of picture text -->
(4)<br>𝑍𝑍1 = 𝐶𝐶max<br><!-- End of picture text -->

𝐾𝐾𝑗𝑗 ∑ ∑ 𝑘 𝑘 𝑍𝑍2 = ∑ 𝑋𝑋𝑗𝑗𝑘𝑘<sup>𝑖𝑖𝑝𝑝</sup> 𝑗𝑗𝑘𝑘<sup>𝑖𝑖𝑒𝑒𝑖𝑖</sup> 𝑗𝑗∈𝒥𝒥 𝑖𝑖∈ℳ𝑗 𝑍𝑍3 = ∑ 𝑑𝑑𝑖𝑖 𝑖𝑖∈ℳ 



<!-- Start of picture text -->
(5)<br><!-- End of picture text -->



<!-- Start of picture text -->
(6)<br><!-- End of picture text -->

Here, 𝑍𝑍1 represents the makespan, and 𝑍𝑍2 represents the total processing-related energy consumption. Workload balance is conceptually characterized by the standard deviation of machine utilization, 𝜎𝜎𝑢𝑢, which measures the dispersion of utilization levels across machines. However, directly incorporating 𝜎𝜎𝑢𝑢 into the MILP would introduce nonlinear terms. Therefore, the MILP uses the linear absolute-deviation surrogate 𝑍𝑍3 = ∑𝑖𝑖∈ℳ 𝑑𝑑𝑖𝑖, where the auxiliary variables 𝑑𝑑𝑖𝑖 represent the absolute deviation of each machine’s utilization from the average utilization. Thus, measure of workload dispersion. This distinction ensures consistency between the conceptual definition of work-𝑍𝑍3 is the workload-balance objective directly optimized by the MILP, while 𝜎𝜎𝑢𝑢 is retained as the conceptual load balance and its tractable MILP formulation. 

#### **_Scalarized MILP objective_** 

For MILP refinement, the three objectives are combined using a normalized weighted-sum scalarization: 



<!-- Start of picture text -->
(7)<br>𝑍𝑍11 𝑍𝑍22 𝑍𝑍33<br>min 𝑍𝑍𝑍𝑍𝑍1 + 𝑍𝑍2 + 𝑍𝑍3<br>𝑍𝑍 ref 𝑍𝑍 ref 𝑍𝑍 ref<br>(8)<br>𝑤𝑤1 + 𝑤𝑤2 + 𝑤𝑤3 = 1, 𝑤𝑤1, 𝑤𝑤2, 𝑤𝑤3 ≥ 0.<br><!-- End of picture text -->

3<sup>are used to normalize the objectives and prevent scale dominance. Differ-</sup> The reference values ent weight combinations are used to refine different regions of the Pareto front.𝑍𝑍1<sup>ref, 𝑍𝑍</sup> 2<sup>ref, and 𝑍𝑍ref</sup> The third scalarized component therefore corresponds to the linearized absolute-deviation workload objective 𝑍𝑍3, rather than directly to the standard-deviation measure **_Constraints_** 𝜎𝜎𝑢𝑢. **Operation assignment** 



<!-- Start of picture text -->
∑ 𝑗 = 1,<br>(9)<br>𝑋𝑋 𝑖𝑖 ∀𝑗𝑗 ∈ 𝒥𝒥, 𝒥𝒥= 1, 𝒥, 𝒥𝒥𝑗𝑗.<br>𝑖𝑖∈ℳ𝑗<br><!-- End of picture text -->

Each operation must be assigned to exactly one eligible machine. **Completion time definition** 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 



<!-- Start of picture text -->
(10)<br>𝐶𝐶𝑗 = 𝑆𝑆𝑗 𝑗 + ∑ 𝑋𝑋𝑗 𝑖𝑖 𝑗 𝑝𝑝 𝑗 𝑖𝑖 𝑗 , ∀𝑗𝑗 ∈ 𝒥𝒥, 𝒥𝒥= 𝒥, 𝒥, 𝒥𝒥𝑗𝑗.<br>𝑖𝑖∈ℳ𝑗<br>Job precedence constraints<br>(11)<br>𝑆𝑆𝑗 𝑗 𝑗 𝑗 ≥ 𝐶𝐶 𝑗 𝑗 , ∀𝑗𝑗 ∈ 𝒥𝒥, 𝒥𝒥𝒥𝒥, 𝒥, 𝒥𝒥𝑗𝑗 −𝒥.<br>This constraint ensures that the internal operation sequence of each job is respected.<br>Makespan definition<br>(12)<br>𝐶𝐶max ≥ 𝐶𝐶𝑗 𝑗 , ∀𝑗𝑗 ∈ 𝒥𝒥, 𝒥𝒥𝒥𝒥, 𝒥, 𝒥𝒥𝑗𝑗.<br><!-- End of picture text -->

**Machine non-overlap constraints** For any two distinct operations that may be assigned to the same machine, one operation must precede the other. Therefore, for all 𝑂𝑂𝑗 **𝑗** ≠ 𝑂𝑂𝑗𝑗′𝑗𝑗′ and all 𝑖𝑖 ∈ ℳ𝑗 **𝑗** ∩ ℳ𝑗𝑗′𝑗𝑗′, the following constraints are imposed: (13) 𝑆𝑆𝑗𝑗′𝑘𝑘′ ≥ 𝐶𝐶𝑗𝑗𝑘𝑘 −𝑀𝑀<sup>𝐵𝐵</sup> (1 −𝑌𝑌𝑗𝑗𝑘𝑘𝑗𝑗𝑗<sup>𝑖𝑖′</sup> 𝑘𝑘<sup>′) −𝑀𝑀𝐵𝐵(2 −𝑋𝑋</sup> 𝑗𝑗𝑘𝑘<sup>𝑖𝑖−𝑋𝑋</sup> 𝑗𝑗<sup>𝑖𝑖′</sup> 𝑘𝑘<sup>′)</sup> (14) 𝑆𝑆𝑗 **𝑗** ≥ 𝐶𝐶𝑗𝑗′𝑗𝑗′ −𝑀𝑀<sup>𝐵𝐵</sup> 𝑌𝑌𝑗<sup>𝑖𝑖</sup> **𝑗** 𝑗𝑗𝑗<sup>′</sup> 𝑗𝑗<sup>′−𝑀𝑀𝐵𝐵(2 −𝑋𝑋</sup> 𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>−𝑋𝑋</sup> 𝑗𝑗<sup>𝑖𝑖′</sup> 𝑗𝑗<sup>′)</sup> 

These constraints are activated only when both operations are assigned to the same machine. They prevent overlapping operations on each machine. 

#### **Machine workload calculation** 



<!-- Start of picture text -->
𝐾𝐾𝑗𝑗<br>∑ (15)<br>𝑈𝑈 𝑖𝑖 = ∑ 𝑘 𝑘 𝑋𝑋𝑗𝑗𝑘𝑘 𝑖𝑖 𝑝𝑝 𝑗𝑗𝑘𝑘 𝑖𝑖 , ∀𝑖𝑖 ∈ ℳ.<br>𝑗𝑗∈𝒥𝒥<br>(16)<br>𝑈𝑈𝑈 1 𝑈𝑈 𝑖𝑖.<br>𝑚𝑚 ∑ 𝑖𝑖∈ℳ<br><!-- End of picture text -->

#### **Workload imbalance linearization** 



<!-- Start of picture text -->
(17)<br>𝑑𝑑𝑖𝑖 ≥ 𝑈𝑈 𝑖𝑖 −̄ 𝑈 ∀𝑖𝑖 ∈ ℳ.<br>(18)<br>𝑑𝑑𝑖𝑖 ≥̄ 𝑈𝑈𝑈𝑈𝑈 𝑖𝑖, ∀𝑖𝑖 ∈ ℳ.<br><!-- End of picture text -->

Minimizing ∑𝑖𝑖∈𝑀𝑀 𝑑𝑑𝑖𝑖 provides a linear absolute-deviation surrogate for workload balance. At optimality, 𝑑𝑑𝑖𝑖 represents formulation avoids the nonlinear square and square-root terms associated with the standard-deviation measure |𝑈𝑈 𝑖𝑖 −̄ 𝑈𝑈|, so 𝑍𝑍3 = ∑𝑖𝑖∈𝑀𝑀 𝑑𝑑𝑖𝑖 measures the aggregate deviation of machine workloads from the average. This while preserving the intended objective of balancing machine workloads. 

#### **Energy-budget constraint** 



<!-- Start of picture text -->
𝐾𝐾𝑗𝑗<br>∑ ∑ ∑ (19)<br>𝑘 𝑘<br>𝑋𝑋𝑗𝑗𝑘𝑘 𝑖𝑖 𝑝𝑝 𝑗𝑗𝑘𝑘 𝑖𝑖 𝑒𝑒 𝑗𝑗𝑘𝑘 𝑖𝑖 ≤ 𝐸𝐸max.<br>𝑗𝑗∈𝒥𝒥 𝑖𝑖∈ℳ𝑗<br><!-- End of picture text -->

The parameter horizon. This is an energy-budget constraint measured in energy units. If a peak-power constraint is required, a 𝐸𝐸max denotes the maximum allowable processing-related energy consumption over the planning time-indexed formulation would be necessary to limit simultaneous power demand at each time period. 

#### **Resource feasibility** 



<!-- Start of picture text -->
, (20)<br>𝑟𝑟𝑗 𝑗 𝑗𝑗 ≤ 𝑅𝑅𝑗𝑗 available ∀𝑗𝑗, 𝑗𝑗, 𝑗 𝑗<br><!-- End of picture text -->

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 **𝑗 𝑗** 

denotes the availHere, able amount of that resource. This constraint ensures that each operation is individually feasible with respect to 𝑟𝑟𝑗 **𝑗** 𝑗𝑗 denotes the amount of auxiliary resource _q_ required by operation 𝑂𝑂𝑗 **𝑗** , and 𝑅𝑅𝑞𝑞<sup>available</sup> auxiliary resource requirements. 

#### **Variable domains** 



<!-- Start of picture text -->
(21)<br>𝑋𝑋𝑗 𝑖𝑖 𝑗 ∈{0, 1}, 𝑌𝑌𝑗 𝑖𝑖 𝑗 𝑗𝑗𝑗 ′ 𝑗𝑗 ′ ∈{0, 1}.<br>(22)<br>𝑆𝑆𝑗 𝑗 , 𝐶𝐶𝑗 𝑗 , 𝐶𝐶max, 𝑈𝑈 𝑖𝑖, 𝑑𝑑𝑖𝑖 ≥ 0.<br><!-- End of picture text -->

**𝑗 𝑗 Energy modeling scope.** In the MILP formulation, the objective 𝑍𝑍2 and the energy-budget constraint optimize _processing-related_ energy consumption using machine-dependent processing time 𝑝𝑝𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>and processing-energy</sup> coefficient 𝑒𝑒𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>. Idle and transition (ramp-up) energy components, when considered in the study, are included</sup> through machine-specific post-schedule evaluation rather than as decision-dependent terms in the linear MILP objective. This modeling choice preserves MILP linearity and solver compatibility while keeping the energy evaluation consistent. 

## **4 Solution methodology** 

The proposed solution adopts a two-phase hybrid framework that merges adaptive exploration through a hyperheuristic with exact exploitation using MILP optimization. This design leverages the strengths of both paradigms: the hyper-heuristic provides scalability, flexibility, and learning-based adaptation in large combinatorial search spaces, while the MILP phase provides fine-grained refinement, feasibility verification, and certified optimalitygap information when the solver reaches the specified tolerance within the runtime limit. The dual-phase design addresses two core challenges: (i) the computational intractability of large-scale MILP models, and (ii) the local convergence risks of standalone heuristic approaches. 

### **4.1 Phase I: hyper-heuristic search** 

The first phase employs a high-level hyper-heuristic controller that dynamically selects among a set of _low-level heuristics_ ℋ= {ℎ1, ℎ2, … , ℎ𝐾𝐾}, where each ℎ𝑘𝑘 is designed to exploit specific neighborhood structures or domain properties of the scheduling problem. The controller adaptively updates selection probabilities according to observed improvement trends, forming a self-learning search mechanism. 

The low-level heuristics are grouped into three complementary categories: 

**_1. Constructive heuristics_** These heuristics are responsible for building new solutions or completing partial schedules from scratch. 

- **Shortest processing time (SPT):** Prioritizes jobs with minimal operation time. 

- **Earliest due date (EDD):** Orders operations according to the nearest due dates or earliest release times. 

- ●● **Energy-aware assignment (EAA):** while respecting **Minimum slack time (MST):** 𝐸𝐸max. Schedules operations with the smallest remaining slack before deadlines. Chooses machine–operation pairs that minimize active energy usage 

- **Minimum slack time (MST):** Schedules operations with the smallest remaining slack before deadlines. Chooses machine–operation pairs that minimize active energy usage 

**_2. Improvement heuristics_** These operators refine an existing schedule by exploring its local neighborhood and improving one or more objectives. 

- **Swap operator (SW):** Exchanges two operations between machines to balance workloads or minimize idle time. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

- **Insertion operator (INS):** Relocates an operation within or across machine queues to reduce total completion time. 

- ●● **Load balancing operator (LBO):** reduce **Local search energy optimization (LSEO):** 𝜎𝜎𝑢𝑢. Redistributes operations from overloaded to underutilized machines to  Reassigns energy-intensive operations to more efficient machines. 

- **Local search energy optimization (LSEO):** Reassigns energy-intensive operations to more efficient machines. 

**_3. Perturbation heuristics_** These heuristics introduce controlled randomness to escape local optima and diversify the search. 

- **Random block relocation (RBR):** Moves a contiguous sequence of operations to a new position. 

- **Multi-swap perturbation (MSP):** Performs simultaneous multiple swaps to explore distant neighborhoods. 

- **Shuffling underutilized machines (SUM):** Reorders tasks on underloaded machines to promote diversity. 

The hyper-heuristic functions as a _meta-controller_ , maintaining a dynamic performance score for each heuristic ℎ𝑖𝑖 based on historical improvements in objective values. At each iteration _t_ , it selects a heuristic probabilistically according to its relative score, applies it, and updates the scores through reinforcement. 

The probability-based selection policy is adopted because the usefulness of each low-level heuristic varies during the search process. Constructive heuristics are generally more effective in the early stages when feasible solutions are being generated, whereas improvement heuristics are more useful during intensification around promising regions. Perturbation heuristics become important when the search stagnates and diversification is required. Therefore, using adaptive selection probabilities allows the Hyper-Heuristic to exploit heuristics that have recently performed well while still preserving a nonzero probability of selecting less frequently used heuristics. This helps maintain a balance between intensification and diversification. 

At iteration _t_ : **𝑃** 

- At iteration _t_ : 

- 1. Select a low-level heuristic ℎ𝑖𝑖 with probability 𝑃 **𝑃** 𝑃𝑖𝑖) = ∑𝑠ℎℎ **𝑠** 𝑠𝑠 **𝑠𝑠𝑠** 𝑠𝑠 **𝑠𝑠𝑠** 𝑠𝑠 **𝑠** 𝑖𝑖)𝑠)<sup>.</sup> 

- **𝑃** ∑𝑠ℎℎ **𝑠** 𝑠 **𝑠𝑠𝑠** 𝑠𝑠 **𝑠𝑠𝑠** 𝑠 **𝑠** 𝑠)<sup>.</sup> 

- 2. Apply ℎ𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆ℎ𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆 to produce a new neighbor 𝑆𝑆𝑆𝑆<sup>′</sup> = ℎ𝑖𝑖(𝑆𝑆𝑡𝑡). 3. Evaluate 𝑆𝑆𝑆𝑆𝑆𝑆<sup>′</sup> across all objectives (makespan, energy, and utilization). 

- **𝑃 𝑠𝑠𝑠 𝑠 𝑠** 

- 2. Apply ℎ𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆ℎ𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑖𝑖 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆 to the current solution 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆𝑡𝑡 to produce a new neighbor 𝑆𝑆 to produce a new neighbor 𝑆𝑆𝑆𝑆<sup>′</sup> 3. Evaluate 𝑆𝑆𝑆𝑆𝑆𝑆<sup>′</sup> across all objectives (makespan, energy, and utilization). 4. Accept 𝑆𝑆5. Update the heuristic score according to its multi-objective contribution. For a current solution date solution 𝑆𝑆<sup>′</sup> if it Pareto-dominates 𝑆𝑆𝑡𝑡𝑆𝑆 



<!-- Start of picture text -->
3. Evaluate 𝑆𝑆𝑆𝑆𝑆𝑆 ′  across all objectives (makespan, energy, and utilization).<br>4. Accept 𝑆𝑆5. Update the heuristic score according to its multi-objective contribution. For a current solution date solution 𝑆𝑆 ′  if it Pareto-dominates 𝑆𝑆𝑡𝑡𝑆𝑆 ′ , the normalized improvement is computed as: 𝑆𝑆𝑡𝑡𝑡𝑡 or meets an adaptive improvement threshold 𝜃𝜃𝑡𝑡. S  and a candi-<br>𝑆 (23)<br>𝑍𝑍1(𝑆𝑆) 𝑆𝑍𝑍1(𝑆𝑆 ′ ) 𝑍𝑍2(𝑆𝑆) 𝑆𝑍𝑍2(𝑆𝑆 ′ ) 𝑍𝑍3(𝑆𝑆) 𝑆𝑍𝑍3(𝑆𝑆 ′ )<br>Δ(𝑆 𝑆 𝑆𝑆 ′ ) = 𝛼𝛼1 + 𝛼𝛼2 + 𝛼𝛼3<br>𝑍𝑍1(𝑆𝑆) 𝑍𝑍2(𝑆𝑆) 𝑍𝑍3(𝑆𝑆)<br>(24)<br>𝛼𝛼1 + 𝛼𝛼2 + 𝛼𝛼3 = 1, 𝛼𝛼1, 𝛼𝛼2, 𝛼𝛼3 ≥ 0.<br><!-- End of picture text -->

A candidate solution is considered successful if it Pareto-dominates the current solution, improves at least one objective without being dominated, or contributes a new non-dominated solution to the Pareto archive. The score of the selected heuristic _h_ is then updated as follows: **𝑠 𝑠 𝑠**<sup>**𝑠𝑠𝑠**</sup> 



<!-- Start of picture text -->
otherwise . (25)<br>𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠𝑠𝑠 { 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠𝑠𝑠𝑠𝑠+, if 𝑆𝑆 ′ is accepted or improves the Pareto archive ,<br>max{𝑠 𝑠 𝑠 𝑠 𝑠𝑠min, 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠𝑠𝑠𝑠𝑠 − },<br><!-- End of picture text -->

**𝑠 𝑠 𝑠**<sup>**𝑠𝑠𝑠**</sup> **𝑠 𝑠 𝑠 𝑠 𝑠** The parameter 𝛿𝛿<sup>+</sup> rewards heuristics that generate improving or archive-contributing solutions, whereas 𝛿𝛿<sup>−</sup> penalizes heuristics that fail to improve the search. The lower bound permanently eliminated, thereby preserving search diversity. In the computational experiments, the reward and penalty parameters were set to selected because excessively large reward values caused premature concentration on a small subset of heuris-𝛿𝛿<sup>+</sup> = 0.10 and 𝛿𝛿<sup>−</sup> = 0.03 after preliminary tuning. Moderate values were 𝑠 **𝑠** 𝑠 **𝑠** 𝑠𝑠min prevents any heuristic from being tics, while excessively large penalty values reduced exploration by discouraging perturbation-based operators. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

The selected values provided a stable balance between exploration and exploitation across small, medium, and large instances. 

To prevent premature convergence, the controller alternates between two complementary strategies: 

- **Diversification:** Temporarily increases the selection probability of heuristics with low recent usage to explore unvisited areas of the search space. 

- **Intensification:** Increases the probability of high-performing heuristics to exploit regions with strong Pareto improvements. 

The algorithm includes a stopping criterion based on either the maximum number of iterations tion of the Pareto front (no improvement for 𝜂𝜂 successive iterations). _T_ or the stabilizaRequire: Initial schedule S0,0,, heuristic pool H,, maximum iterations T , archive size 

Require: Initial schedule S0,0,, heuristic pool H,, maximum iterations T , archive size Amax Ensure: Pareto archive A 1: Initialize score(h) � 1 for all h � H 

- 2: Initialize A � {S0} 

- 3: S � S0 

- 4: for t = 1 to T do 

> 5: Select heuristic h � H according to score(h) P (h) = score(g) g�H 

> 6: Generate candidate solution S � h(S) 7: Evaluate Z(S ) = (Z1(S ), Z2(S ), Z3(S )) 8: if S is non-dominated with respect to A then 9: Insert S into A 10: Remove from A all solutions dominated by S 11: score(h) � score(h) + δ<sup>+</sup> 12: S � S 13: else 14: score(h) � max{scoremin, score(h) − δ<sup>−</sup> } 15: end if 16: if |A| > Amax then 17: Prune A using crowding-distance-based pruning 18: end if 19: if normalization interval is reached then 20: Normalize heuristic scores 21: end if 22: end for 23: return A 

**~~A~~ lgorithm 1** Pareto-based adaptive 

hyper-heuristic search phase 

This phase outputs a set of Pareto-efficient schedules representing trade-offs among makespan, processingwarm-start candidate for the exact MILP solver.related energy consumption, and machine utilization. The best non-dominated solution 𝑆𝑆<sup>∗</sup> serves as a high-quality ing a non-dominated archive MILP refinement phase, the solver requires a scalar objective; therefore, for each selected representative schedule from **Two-level multi-objective mechanism.** 𝒜𝒜, the MILP is solved using a normalized weighted-sum scalarization with weight vectors 𝒜𝒜 of schedules evaluated with the objective vector  The Hyper-Heuristic phase approximates the Pareto set by maintain-Z(𝑆 **𝑆** 𝑆(𝑆𝑆1(𝑆 **𝑆** 𝑆𝑆𝑆2(𝑆Ω: **𝑆** 𝑆𝑆𝑆3(𝑆 **𝑆** 𝑆. In the 



<!-- Start of picture text -->
,<br>𝑍𝑍11 𝑍𝑍22 𝑍𝑍33<br>min 𝑍𝑍𝑍𝑍𝑍1 + 𝑍𝑍2 + 𝑍𝑍3 (𝑍𝑍1, 𝑍𝑍2, 𝑍𝑍3) ∈ Ω.<br>𝑍𝑍 ref 𝑍𝑍 ref 𝑍𝑍 ref<br><!-- End of picture text -->

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

The final reported Pareto set is obtained as the non-dominated union of the hyper-heuristic archive and the MILP-refined solutions, i.e., After applying a low-level heuristic move, the candidate schedule is repaired to satisfy (i) job precedence, 𝒫𝒫<sup>final</sup> = ND(𝒜𝒜 ∪ 𝒜𝒜<sup>𝑅𝑅</sup> ). (ii) operation-to-eligible-machine assignment, and (iii) machine non-overlap. If repair cannot restore feasibility within a bounded number of attempts, the candidate is rejected and the corresponding heuristic score is penalized. A candidate solution is accepted if it is Pareto-non-dominated with respect to the current archive and improves the archive according to the specified acceptance criterion (dominance and/or archive diversity contribution). The heuristic score is then updated using the reward/penalty parameters 𝛿𝛿<sup>+</sup> and 𝛿𝛿<sup>−</sup> . 

### **4.2 Phase II: exact MILP refinement** 

The Pareto archive as warm-start candidates for the MILP refinement stage. Rather than refining only a single schedule, Phase II 𝒜𝒜 generated during Phase I provides a set of non-dominated feasible schedules that serve systematically refines the archive solutions under a predefined set of normalized weight vectors. By initializing the MILP solver with a feasible incumbent solution, the branch-and-bound procedure can exploit the warm-start solution to obtain high-quality feasible solutions early and potentially reduce the computational effort required for convergence. The objectives of this refinement phase are: 

- Fine-tuning operation start times, sequencing, and machine assignments while preserving all scheduling constraints;Improving the scalarized objective value and reducing the optimality gap Verifying feasibility with respect to precedence, machine-capacity, non-overlap, and energy-related constraints.𝜖𝜖 below a user-defined threshold; 

●● constraints;Improving the scalarized objective value and reducing the optimality gap Verifying feasibility with respect to precedence, machine-capacity, non-overlap, and energy-related constraints.𝜖𝜖 below a user-defined threshold; As detailed in Algorithm 2, there is no one-to-one assignment between archive members and weight vectors. For each archive solution start incumbent for the corresponding normalized weighted-sum MILP objective. Consequently, multiple archive 𝑆𝑆 ∈ 𝒜𝒜 and each weight vector w = (𝑤𝑤1, 𝑤𝑤2, 𝑤𝑤3) ∈ Ω, the solution _S_ is used as a warmmembers are refined under the same weight vector, allowing the same objective preference to be explored from different regions of the Pareto archive. The resulting MILP-refined solutions are collected in duplicate removal and Pareto filtering. 𝒜𝒜<sup>𝑅𝑅</sup> for subsequent 

1: Input: MILP model, Pareto archive A, weight-vector set Ω, gap tolerance , time limit tmax 2: Initialize refined archive A<sup>R</sup> 3: for each solution S � A do 4: for each weight vector w = (w1, w2, w3) � Ω do 5: Set w in the normalized MILP objective 6: Use S as the warm-start incumbent 7: Solve the MILP until gap ≤ or runtime ≥ tmax 8: Insert the best feasible MILP solution into A<sup>R</sup> 9: end for 10: end for 11: Remove duplicate solutions from A A<sup>R</sup> 12: Remove dominated solutions from A A<sup>R</sup> 13: Return final non-dominated archive 

##### **Algorithm 2** MILP refinement of pareto-archive solutions 

The warm-start solution provides initial values for the MILP decision variables but does not fix them during refinement. In particular, the machine-assignment, sequencing, and operation start-time variables remain free and may be modified by the MILP solver when such changes improve the normalized weighted-sum objective while satisfying all model constraints. Thus, the Hyper-Heuristic solution acts as an initial feasible incumbent rather than a fixed schedule. The best feasible solution obtained for each archive–weight-vector combination is added to 𝒜𝒜<sup>𝑅𝑅</sup> . 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

Duplicate solutions are identified using their complete scheduling decision representation. Two schedules are considered duplicates when their machine assignments and operation sequencing decisions are identical and their operation start times are equal within the numerical tolerance used for continuous variables. Only one copy of a duplicate schedule is retained in the combined archive final Pareto-dominance filtering, ensuring that the reported archive contains unique non-dominated scheduling 𝒜𝒜 ∪ 𝒜𝒜<sup>𝑅𝑅</sup> . Duplicate removal is performed before the solutions. 

After all archive–weight-vector combinations have been processed, duplicate solutions are removed from the union of the original and refined archives. The remaining solutions are then subjected to Pareto-dominance filtering to obtain the final non-dominated archive. A MILP-refined solution is therefore not required to dominate its corresponding warm-start solution to be retained; if it is feasible and belongs to the final non-dominated set, it is preserved as an alternative trade-off solution. 

The MILP stage therefore combines exact optimization with heuristic-derived initialization. When the solver reaches the specified optimality-gap tolerance within the imposed time limit, it provides an optimality-gap certificate for the corresponding weighted-sum subproblem. The resulting refined archive preserves alternative objective trade-offs while benefiting from the improved local refinement and feasibility guarantees provided by the MILP formulation. 

### **4.3 Integration rationale** 

The hybrid framework integrates the adaptive intelligence of the hyper-heuristic phase with the mathematical rigor of the MILP phase. 

- **Exploration (Phase I):** The hyper-heuristic adaptively explores the search space, avoiding local minima and generating multiple Pareto-competitive solutions through guided diversity. 

● **Exploitation (Phase II):** The MILP refinement improves selected non-dominated schedules and provides optimality-gap information when the solver reaches the defined tolerance within the specified runtime limit. This synergistic combination allows the system to perform well in both offline (strategic planning) and online (real-time scheduling) contexts, providing a balance between adaptiveness, optimality, and computational efficiency–key requirements for Industry 4.0 smart manufacturing systems. 

## **5 Experimental setup** 

This section outlines the datasets, evaluation metrics, and computational configuration used to validate the proposed hybrid Hyper-heuristic-MILP framework. The design emphasizes both realism and scalability, ensuring a fair comparison between computational efficiency and solution quality under Industry 4.0 conditions. 

### **5.1 Datasets** 

Two dataset categories were utilized to evaluate performance under realistic and scalable operating contexts: 

#### **5.1.1 Industrial dataset** 

The industrial dataset was collected from a discrete manufacturing facility in Lebanon that adheres to Industry 4.0 standards. The dataset captures real production scenarios and includes the following characteristics: 

- **Number of machines:** 12 heterogeneous machines (5 CNC mills, 4 lathes, 3 robotic arms). 

- **Number of jobs:** 87 jobs per production shift, with each job comprising 3–8 operations. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

- **Operation distributions:** Processing times follow a log-normal distribution (mean = 15 min, standard deviation = 5 min), calibrated from historical production logs. 

- **Energy profiles:** Machine-specific energy coefficients (kWh per minute) were recorded at 1-minute granularity, distinguishing three operational states: 

– Idle: 0.5−1.2 kW, 

– Ramp-up: 2.0−3.5 kW, 

– Active: 3.0−8.0 kW. 

- **Due dates:** Jobs have soft due dates sampled from a uniform distribution spanning 1.2-−1.5× the sum of their processing times. **𝑗** 

- **Resource constraints:** Each operation requires 1–2 auxiliary resources (e.g., tools, fixtures), with availability . 

- constraints modeled as 𝑟𝑟𝑗 **𝑗** 𝑗𝑗 ≤ 𝑅𝑅𝑗𝑗<sup>available</sup> 

- **Data availability:** The dataset is anonymized to protect proprietary information. A synthetic version with equivalent statistical properties is available from the corresponding author upon reasonable request. 

#### **5.1.2 Synthetic dataset generation** 

To evaluate scalability, we generated synthetic instances using the following procedure: 

- **Instance sizes:** 

   - Small: 20–50 jobs, 5–10 machines, 

   - Medium: 100–200 jobs, 10–20 machines, 

   - Large: 500–700 jobs, 20–30 machines. 

- **Operation distributions:** 

   - Number of operations per job: sampled from a discrete uniform distribution _U_ (3, 8), 

   - – the industrial dataset.Processing times: sampled from a log-normal distribution LN(𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇𝜇 (in minutes), scaled to match 

- **Energy profiles:** 

   - Energy coefficients: sampled from a uniform distribution _U_ (0.1, 0.5) kWh per minute of processing, with machine-specific multipliers to reflect heterogeneity. **𝑈** 

- ●● **Due dates:Resource constraints:** Generated as  Each operation requires 1–2 resources, with availability sampled from 𝑑𝑑𝑗𝑗 = 𝑟𝑟𝑗𝑗 + 𝛼𝛼 ∑𝑘𝑘 𝑝𝑝𝑗𝑗𝑘𝑘, where 𝑟𝑟𝑗𝑗 is the release time and 𝛼𝛼 ∼ 𝑈 **𝑈** 𝑈𝑈𝑈𝑈𝑈𝑈𝑈𝑈. 

- **Resource constraints:** Each operation requires 1–2 resources, with availability sampled from 𝑑𝑑𝑗𝑗 **𝑈** _U_ (1, 3). 

- ●● **Machine eligibility:Energy budget:** energy requirements across all operations. Set to  Each operation is eligible for 30–70% of machines, randomly selected.𝐸𝐸max = 1.1 × lower bound, where the lower bound is computed as the sum of minimum 

This generation process ensures that the synthetic instances retain the statistical properties of the industrial dataset while allowing controlled scalability experiments. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

### **5.2 Benchmark algorithms** 

To provide a rigorous evaluation, the proposed Hybrid Hyper-Heuristic–MILP framework was compared with the following state-of-the-art and baseline methods: 

- **Heuristic-only:** The proposed hyper-heuristic without MILP refinement (ablation baseline). 

- **Single-objective MILP:** A MILP model optimizing makespan as the primary objective (exact optimization baseline). 

- **NSGA-II:** Non-dominated Sorting Genetic Algorithm, a widely used multi-objective evolutionary benchmark. 

- **MOEA/D:** Multi-Objective Evolutionary Algorithm Based on Decomposition, which scalarizes the problem using weight vectors. 

- **Tabu search:** A multi-objective Tabu Search with a Pareto archive to track non-dominated solutions. 

- **Variable neighborhood search (VNS):** A local-search-based metaheuristic using multiple neighborhood structures. 

- **Genetic algorithm with local search (GA+LS):** A genetic algorithm enhanced with local improvement operators. 

● **MOPSO:** Multi-Objective Particle Swarm Optimization, representing swarm-based scheduling approaches. To ensure a fair and reproducible comparison, all algorithms were implemented using the _same_ underlying components as the proposed framework: 

- The same solution encoding, consisting of a precedence-feasible operation sequence combined with a machine-assignment vector; 

- The same serial schedule-generation scheme used to decode a candidate solution into a feasible schedule; 

- The same feasibility-repair procedure for precedence, machine-eligibility, machine-capacity, and resourceavailability violations;The same objective definitions and evaluation procedure, namely makespan (𝑍𝑍1), processing-related energy 

- availability violations;The same objective definitions and evaluation procedure, namely makespan (𝑍𝑍1), processing-related energy 

- ● consumption (The same industrial constraints described in Section 3.3;𝑍𝑍2), and linearized workload-balance deviation (𝑍𝑍3), as defined in Section 3.3; 

- The same industrial constraints described in Section 3.3;𝑍𝑍2), and linearized workload-balance deviation (𝑍𝑍3), as defined in Section 3.3; 

**Table 2** Parameter settings for the multi-objective and metaheuristic baselines 

|Algorithm|Parameter|Value|
|---|---|---|
|NSGA-II|Population size|200|
||Crossover probability (SBX-like precedence crossover)|0.9|
||Mutation probability|0.1|
||Selection|Binary tournament|
|MOEA/D|Population size|200|
||Neighborhood size|20<br>f|
||Decomposition method|Tchebycheff|
||Weight vector generation|Uniform simplex-lattice design|
|Tabu search|Tabu list size|50|
||Archive size limit|100|
||Neighborhood operator|Swap / insertion|
|VNS|Number of neighborhood structures|4|
||Shaking intensity|1–3 operations|
||Local search|First-improvement|
|GA+LS|Population size|150|
||Local search frequency|Every 10 generations|
||Local search operator|Insertion + swap|
|MOPSO|Swarm size|200|
||Inertia weight<br>fi|0.4-−0.9 (linearly decreasing)|
||Cognitive/social coefficients|1.5 / 1.5|
||External archive size|100|



Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

- The same stopping budget, defined by a maximum wall-clock runtime and a maximum number of objectivefunction evaluations, identical across all methods. 

For every candidate schedule generated by a competing algorithm, the three objective values are calculated using exactly the same definitions as those used by the proposed framework. Thus, differences in the reported objective values are attributable to the search and optimization strategies rather than to differences in objective evaluation or constraint handling. This design isolates the effect of the search strategy itself (evolutionary, swarm-based, localsearch, or hybrid hyper-heuristic–MILP) from confounding factors related to encoding or constraint handling. 

Table 2 summarizes the parameter settings used for each population- or archive-based baseline. Parameters were tuned via grid search on a held-out validation subset of instances (distinct from the test instances used in Section 6) and then fixed for all experimental runs. 

For all multi-objective algorithms, including the proposed framework and the multi-objective benchmark methods, the final solution set is obtained using the same Pareto-dominance definition. For the proposed framework, the Hyper-Heuristic archive and MILP-refined solutions are first combined, duplicate schedules are removed, and the union is then Pareto-filtered. For the competing multi-objective algorithms, their final candidate solution sets are subjected to the same duplicate-removal and Pareto-dominance filtering procedure. This common post-processing ensures that the multi-objective quality indicators are computed from consistently defined nondominated solution sets. 

The resulting final non-dominated archives are used to compute the multi-objective quality indicators, including hypervolume (HV), inverted generational distance (IGD), and spacing, reported in Section 6. 

All algorithms were executed 20 times with independent random seeds under comparable computational budgets to ensure fair comparison. 

### **5.3 Performance metrics** 

To ensure a multi-dimensional evaluation, four performance criteria were employed, aligned with the objectives of the MILP model: 

- **Makespan** values indicate faster throughput. (𝐶𝐶max): The total completion time of all jobs, representing overall production efficiency. Lower 𝐶𝐶max 

- values indicate faster throughput. (𝐶𝐶max): The total completion time of all jobs, representing overall production efficiency. Lower 𝐶𝐶max **Processing-related energy consumption** by all scheduled operations during the planning horizon. Idle and ramp-up energy components are evaluated  (𝐸𝐸total): The aggregate processing-related electrical energy consumed 

- ● separately in the post-schedule analysis when machine-state profiles are available.Machine Utilization Index (𝑈𝑈index): A normalized reporting metric used to express workload balance. The MILP directly optimizes the linear absolute-deviation objective tion and comparison across scheduling solutions:: 𝑍𝑍3, while 𝑈𝑈index is used to facilitate interpreta- 



<!-- Start of picture text -->
,<br>∑𝑖𝑖∈ℳ | |𝑈𝑈 𝑖𝑖 −̄ 𝑈𝑈||<br>𝑈𝑈index = 1 −<br>𝑚𝑚 ⋅̄ 𝑈𝑈<br><!-- End of picture text -->

where values signify better balance. This normalized measure enables fair comparison across configurations with dif-𝑈𝑈 𝑖𝑖 denotes the utilization of machine 𝑀𝑀𝑖𝑖 and ̄𝑈𝑈 is the average utilization across all machines. Higher 𝑈𝑈index ferent machine counts. 

- **Computation time:** Measured wall-clock time from the start of the hyper-heuristic initialization to the completion of MILP refinement. This metric assesses computational scalability and convergence speed. 

All performance metrics were averaged over 20 independent runs with distinct random seeds, and the standard deviation was reported to indicate stability. Statistical significance of observed improvements was tested using paired _t_ -tests and Wilcoxon signed-rank tests (𝑝 **𝑝** 𝑝𝑝𝑝𝑝). 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

### **5.4 Computational environment** 

All experiments were conducted on a high-performance workstation to ensure consistency and repeatability: 

- Processor: Intel<sup>®</sup> Xeon<sup>®</sup> W-2295, 3.0 GHz, 18 cores. 

- Memory: 128 GB DDR4. 

- Storage: 2 TB NVMe SSD. 

- Operating system: Ubuntu 22.04 LTS. 

The MILP component was solved using IBM ILOG CPLEX Optimization Studio 22.1 with warm-start functionality enabled and a relative optimality gap tolerance of 10<sup>−4</sup> . Parameter tuning included emphasis on deterministic concurrent search and node memory reduction to accelerate branch-and-bound convergence. callable operator classes. Adaptive parameters (nary sweeps over 25 configurations using grid search. Random seeds were fixed to ensure reproducibility, and The hyper-heuristic phase was implemented in Python 3.11, where low-level heuristics were modularized into 𝛿𝛿+, 𝛿𝛿−, and learning decay rates) were fine-tuned through prelimiexecution logs were exported for post-run analysis using the `pandas` and `matplotlib` libraries. 

This computational setup ensures that performance comparisons are unbiased, replicable, and aligned with modern Industry 4.0 data processing and optimization standards. For performance evaluation, the proposed framework and the benchmark algorithms are compared using the obtained non-dominated solution sets. The comparison considers the achieved makespan,processing-related energy consumption, and machine utilization balance. In addition, average objective values obtained from multiple independent runs are reported to provide a fair and statistically reliable assessment of algorithm performance. 

### **5.5 Parameter settings** 

The hyper-heuristic parameters were selected through preliminary tuning experiments. The final parameter values used in the computational study are summarized as follows: 

- Maximum number of iterations: for large instances. **𝑠 𝑠 𝑠** 𝑇𝑇𝑇𝑇𝑇𝑇𝑇 for small instances, 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 for medium instances, and 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 

- for large instances.Initial heuristic score: 𝑠 **𝑠** 𝑠 **𝑠** 𝑠 **𝑠** 𝑠𝑠𝑠𝑠 for all low-level heuristics. 

- ● Reward parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>+</sup> = 0.10.. 

- Initial heuristic score: 𝑠𝑠 **𝑠** 𝑠 **𝑠** 𝑠 **𝑠** 

- ● Reward parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>+</sup> = 0.10.. ● Penalty parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>−</sup> = 0.03... **𝑠 𝑠** 

- **𝑠 𝑠 𝑠** 

- ● Reward parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>+</sup> = 0.10.. ● Penalty parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>−</sup> = 0.03... ● Minimum heuristic score: 𝑠𝑠𝑠 **𝑠 𝑠** 

- Penalty parameter: 𝛿𝛿𝛿𝛿𝛿𝛿<sup>−</sup> = 0.03... 

- ● Minimum heuristic score: 𝑠𝑠𝑠 **𝑠** 𝑠 **𝑠** 𝑠𝑠minmin = 0.05.. ●● Maximum Pareto archive size: 𝐴𝐴maxStagnation limit: 500 iterations without Pareto-archive improvement.𝐴𝐴maxmax = 100. 

- Minimum heuristic score: 𝑠𝑠𝑠 **𝑠** 𝑠 **𝑠** 𝑠𝑠minmin = 0.05.. 

- ●● Maximum Pareto archive size: 𝐴𝐴maxStagnation limit: 500 iterations without Pareto-archive improvement.𝐴𝐴maxmax = 100. 

- Stagnation limit: 500 iterations without Pareto-archive improvement.𝐴𝐴maxmax 

- Number of independent runs: 20. 

The MILP refinement stage was implemented using IBM ILOG CPLEX Optimization Studio 22.1. Warm-start functionality was enabled using the non-dominated schedules generated by the hyper-heuristic phase. The relative optimality gap was set to 10<sup>−4</sup> for small and medium instances and 10<sup>−3</sup> for large-scale instances. The time limits were set to 600 s, 1800 s, and 3600 s for small, medium, and large instances, respectively. CPLEX presolve and automatic cut generation were enabled, and deterministic parallel mode was used to ensure reproducibility. 

### **5.6 Sensitivity analysis** 

A sensitivity analysis was conducted to evaluate the effect of the reward and penalty parameters performance of the adaptive hyper-heuristic. The tested values were: 𝛿𝛿<sup>+</sup> and 𝛿𝛿<sup>−</sup> on the (26) 𝛿𝛿<sup>+</sup> ∈{0.05, 0.10, 0.20}, 𝛿𝛿<sup>−</sup> ∈{0.01, 0.03, 0.05}. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

|**Table 3**Performance<br>|Method|Makespan(min)|Energy (kWh)|Utilization index|Time(s)|
|---|---|---|---|---|---|
|comparison across bench-<br>|Heuristic-only|920 ± 26|1250 ± 34|0.82 ± 0.02|120 ± 9|
|mark methods. Values are<br>|Single-objective MILP|880 ± 11|1100 ± 19|0.88 ± 0.01|600 ± 21|
|reported as mean ± standard<br>|NSGA-II|872 ± 17|1018 ± 23|0.90 ± 0.02|345 ± 18|
|deviation over 20 indepen-<br>d  B l|MOEA/D|869 ± 15|1005 ± 20|0.91 ± 0.02|360 ± 16|
|ent runs. est vaues are<br>hn in bld|Tabu search|895 ± 22|1060 ± 28|0.87 ± 0.02|290 ± 15|
|sow  o|VNS|901 ± 16|1086 ± 24|0.86 ± 0.02|210 ± 11|
||GA+LS|892 ± 18|1070 ± 29|0.87 ± 0.02|252 ± 13|
||MOPSO|884 ± 19|1042 ± 27|0.89 ± 0.02|285 ± 14|
||Proposed hybrid|860 ± 12|980 ± 18|0.93 ± 0.01|300 ± 15|



|**Table 4**Pareto-front quality|Method|HV↑|IGD↓|Spacing ↓|
|---|---|---|---|---|
|comparison across multi-<br>|NSGA-II|0.745 ± 0.021|0.1950 ± 0.018|0.086 ± 0.012|
|objective methods. Values<br>|MOEA/D|0.763 ± 0.019|0.1710 ± 0.016|0.078 ± 0.010|
|are reported as mean ± stan-<br>|Tabu search|0.731 ± 0.024|0.2130 ± 0.021|0.094 ± 0.014|
|dard deviation over 20 inde-<br>d  Hih H|VNS|0.718 ± 0.026|0.2290 ± 0.023|0.101 ± 0.015|
|penent runs. ger V<br>d l IGD d Si|GA+LS|0.742 ± 0.022|0.2010 ± 0.019|0.089 ± 0.013|
|an ower  an pacng<br>idit btt f|MOPSO|0.751 ± 0.020|0.1840 ± 0.017|0.083 ± 0.011|
|ncae eer perormance|Proposed hybrid|0.879845 ± 0.014|0.07137 ± 0.009|0.052 ± 0.008|



The results showed that moderate values of 𝛿𝛿<sup>+</sup> and 𝛿𝛿<sup>−</sup> provide the best balance between intensification and diversification. Large values of 𝛿𝛿<sup>+</sup> caused premature concentration on a small number of heuristics, whereas large values of selected for the final experiments.𝛿𝛿<sup>−</sup> overly penalized exploratory heuristics. Based on these observations, 𝛿𝛿<sup>+</sup> = 0.10 and 𝛿𝛿<sup>−</sup> = 0.03 were 

## **6 Results and analysis** 

This section presents an extensive quantitative and qualitative evaluation of the proposed hybrid Hyper-heuristic–MILP scheduling framework. The analysis compares its performance with two baseline, a Heuristic-only and a Single-objective MILP, using both industrial and synthetic datasets (see Sect. 5). The evaluation encompasses small, medium, and large-scale scheduling cases, focusing on efficiency, energy awareness, and workload balance–three pillars of Industry 4.0 sustainability. 

### **6.1 Performance comparison** 

The reported Pareto frontier corresponds to the archive of refined non-dominated schedules obtained after the Hyper-Heuristic exploration and MILP refinement stages. All benchmark algorithms were evaluated using the same three optimization objectives to ensure a fair comparison. 

For the multi-objective algorithms, the final external archive of each run was retained after applying the same Pareto-dominance criterion. These solution archives were used to evaluate Pareto-front quality using Hypervolume (HV), Inverted Generational Distance (IGD), and Spacing. The same objective definitions, normalization procedure, and reference Pareto set were used for all multi-objective methods to ensure a consistent comparison. Higher HV indicates better convergence and coverage, whereas lower IGD and Spacing indicate closer convergence to the reference front and a more uniform distribution of non-dominated solutions, respectively. 

Table 3 summarizes the performance of the proposed Hybrid Hyper-Heuristic–MILP framework and the benchmark methods over 20 independent runs. Four evaluation criteria are considered: makespan, processing-related 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

energy consumption, machine utilization index, and computation time. For each method, the mean and standard deviation are reported to evaluate both solution quality and robustness across repeated executions. 

The proposed Hybrid Hyper-Heuristic–MILP framework consistently achieves the best overall trade-off among the three optimization objectives. Compared with the heuristic-only approach, it reduces the average makespan from 920 to 860 min (approximately 6.5%), decreases processing-related energy consumption from 1250 to 980 kWh (approximately 21.6%), and improves the machine utilization index from 0.82 to 0.93 (approximately 13.4%). These improvements demonstrate the effectiveness of integrating adaptive Hyper-Heuristic exploration with exact MILP refinement for simultaneously improving production efficiency and energy-aware scheduling performance. 

Compared with the single-objective MILP formulation, the proposed framework achieves a better balance among the three optimization objectives. While the single-objective MILP reduces makespan relative to the heuristic-only approach, it is less effective in reducing energy consumption and balancing machine workloads because it optimizes only a single scheduling criterion. In contrast, the proposed framework explores multiple non-dominated scheduling alternatives before applying MILP refinement, resulting in superior overall scheduling performance. 

To further assess the quality of the obtained non-dominated solution sets, Table 4 reports the Hypervolume (HV), Inverted Generational Distance (IGD), and Spacing values for the multi-objective algorithms. The proposed Hybrid Hyper-Heuristic–MILP framework achieves the highest HV and the lowest IGD among the evaluated methods. Compared with NSGA-II, the proposed framework improves HV by 18.1% and reduces IGD by 63.4%. These results demonstrate that the advantage of the proposed method extends beyond the individual objective values reported in Table 3 and includes improved convergence and coverage of the non-dominated solution space. 

The proposed framework also provides a more uniformly distributed non-dominated solution set, as indicated by its lower Spacing value. The combination of higher HV, lower IGD, and lower Spacing indicates that the proposed framework achieves both improved convergence toward high-quality trade-off solutions and better coverage of the objective space. This improvement is attributed to the interaction between adaptive Hyper-Heuristic exploration, which maintains diverse candidate solutions, and MILP refinement, which improves the quality of selected schedules while preserving feasibility. 

The comparison with state-of-the-art multi-objective metaheuristics, including NSGA-II, MOEA/D, Tabu Search, Variable Neighborhood Search, GA+LS, and MOPSO, further demonstrates the competitiveness of the proposed framework. Although several benchmark algorithms achieve reasonable scheduling quality, none simultaneously matches the proposed method in makespan, energy efficiency, and workload balance. The warmstart MILP refinement effectively improves the candidate schedules generated by the adaptive Hyper-Heuristic, leading to higher-quality solutions while maintaining a computational time comparable to other advanced metaheuristics. 

Importantly, the Pareto-quality results complement the objective-level comparison in Table 3. The superiority of the proposed framework is therefore not inferred solely from the best average makespan, energy, or utilization values; it is also supported by quantitative multi-objective indicators that evaluate the quality of the complete non-dominated solution set. 

To evaluate the robustness of the proposed framework, all experiments were repeated over 20 independent runs. Mean values and standard deviations are reported for every performance metric. In addition, statistical 

**Table 5** Scalability analysis of the proposed framework across different instance sizes. Values are reported as mean ± standard deviation over 20 independent runs 

|Instance size|Jobs|Makespan(min)|Energy (kWh)|Time(s)|
|---|---|---|---|---|
|Small|20–50|248 ± 9|286 ± 11|48 ± 6|
|Medium|100–200|860 ± 12|980 ± 18|300 ± 15|
|Large|500–700|2245 ± 37|2578 ± 46|1490 ± 102|



Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

significance was assessed using paired statistical tests, confirming that the observed improvements over the benchmark methods are statistically significant (not only achieves superior average performance but also exhibits stable optimization behaviour across repeated 𝑝𝑝𝑝𝑝𝑝𝑝𝑝). These results demonstrate that the proposed framework executions. 

### **6.2 Scalability analysis** 

To evaluate robustness under increasing problem size, the proposed framework was tested on small, medium, and large scheduling instances. Table 5 summarizes the average results across these instance groups in terms of makespan, processing-related energy consumption, and total runtime. 

Table 5 indicates that the proposed framework maintains stable solution quality across increasing instance sizes. For small instances, the hybrid approach produces high-quality schedules with short runtimes, showing that the Hyper-Heuristic rapidly identifies effective assignments and sequences before MILP refinement is applied. 

For medium-scale instances, the framework preserves its advantage in both makespan and energy reduction, demonstrating that the adaptive heuristic-selection policy remains effective as the search space becomes more complex. The medium-scale results also confirm the practicality of the warm-start refinement stage under realistic production conditions. 

For large-scale instances, the runtime naturally increases because of the combinatorial growth of the scheduling space. Nevertheless, the proposed method remains computationally practical, as the non-dominated warm-start schedules significantly reduce the branch-and-bound effort of the MILP solver. Overall, the scalability results confirm that the proposed framework is suitable for heterogeneous Industry 4.0 manufacturing environments ranging from small production cells to large multi-machine scheduling systems. 

### **6.3 Energy–makespan trade-off** 

Fig. 1 illustrates the energy–makespan trade-off obtained from the multi-objective evaluation. The figure presents the final non-dominated solution archives generated by MOPSO, NSGA-II, MOEA/D, and the proposed Hybrid Hyper-Heuristic–MILP framework, while the Heuristic-only and Single-objective MILP approaches are 

**Fig. 1** Energy–makespan trade-off represented by the final nondominated solution archives of the evaluated multi-objective methods. Lower makespan and lower processing-related energy consumption are preferred. The Heuristiconly and Single-objective MILP methods are shown as individual solutions, whereas the multi-objective methods are represented by their final non-dominated archives 



Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

**Fig. 2** Machine utilization index comparison across all evaluated methods. Higher values indicate better workload balance and more even utilization of available machines 



represented by their respective solutions. The vertical axis represents processing-related energy consumption, which is the energy component directly optimized by the MILP formulation. 

The updated Pareto analysis reveals three main patterns: 

- The Heuristic-only solution is located in a relatively high-energy region, indicating limited effectiveness in simultaneously reducing makespan and processing-related energy consumption. 

- The Single-objective MILP solution achieves a lower makespan than the Heuristic-only solution, but at a higher processing-related energy level. This illustrates the trade-off resulting from optimizing a single scheduling objective rather than explicitly exploring multiple objective combinations. 

- The multi-objective methods generate sets of non-dominated solutions covering different makespan–energy trade-offs. Among these methods, the proposed Hybrid Hyper-Heuristic–MILP framework produces a nondominated archive extending toward lower processing-related energy and competitive makespan values, providing broader coverage of the favorable objective region. 

A solution is considered non-dominated if no other feasible solution simultaneously improves one objective without worsening at least one of the other objectives. The archives shown in Fig. 1 therefore provide a solutionlevel view of the trade-offs explored by the multi-objective algorithms. In contrast to the previous single-point representation, the revised figure preserves the diversity of the generated non-dominated solutions and provides a more informative visual comparison of the competing approaches. 

These results indicate that the adaptive Hyper-Heuristic search, combined with Pareto-archive management and subsequent MILP refinement, is able to explore multiple energy–makespan trade-offs rather than producing only a single compromise solution. The resulting archive provides decision makers with alternative schedules according to the desired balance between production time and processing-related energy consumption. 

### **6.4 Machine utilization balance** 

Fig. A higher value indicates more evenly distributed machine utilization and therefore better workload balance.2 evaluates workload balance using the machine utilization index (𝑈𝑈index) across all nine evaluated methods. The proposed Hybrid Hyper-Heuristic–MILP framework achieves the highest average utilization index of 0.93, followed by MOEA/D (0.91) and NSGA-II (0.90). The single-objective MILP, MOPSO, GA+LS, Tabu Search, and VNS achieve average indices of 0.88, 0.89, 0.87, 0.87, and 0.86, respectively, while the heuristiconly approach obtains 0.82. These results demonstrate that the proposed framework provides the most balanced machine utilization among the evaluated methods, consistent with the workload-balance objective reported in Table 3. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

### **6.5 Scalability and robustness analysis** 

To assess scalability, experiments were performed across varying instance sizes, ranging from 20 to over 500 jobs. The hybrid approach demonstrated consistent solution quality across scales, with computation time growing sub-linearly relative to problem size. 

- For small instances, the hybrid matched optimal MILP results within a 3% deviation, validating correctness. 

- For medium-scale problems (100–200 jobs), the approach maintained energy savings of over 18% compared to heuristic-only baselines. 

- For large-scale cases (> 500 jobs), the heuristic-only method degraded significantly (+20% energy use, −15% utilization), while the hybrid sustained near-optimal performance. 

- The MILP refinement benefited from warm-start initialization, reducing branch-and-bound iterations by approximately 42% on average, confirming the efficiency of Phase II. 

Table 5 further demonstrates the scalability of the proposed method across increasing instance sizes. The results indicate that computation time increases with instance complexity, while the proposed framework maintains competitive solution quality due to the combination of adaptive search and MILP warm-start refinement. 

### **6.6 Statistical validation** 

To verify the statistical significance of the observed improvements, each stochastic algorithm was executed 20 times using independent random seeds. The proposed method was compared pairwise against each benchmark algorithm using paired _t_ -tests when normality assumptions were satisfied and Wilcoxon signed-rank tests otherwise. Bonferroni correction was applied to control the family-wise error rate across multiple comparisons. 

Effect sizes were computed using Cohen’s _d_ to assess the practical significance of the improvements. The results show statistically significant improvements in energy consumption and workload balance for most benchmark comparisons. Makespan improvements were also significant in most medium and large instances, confirming that the proposed framework improves sustainability-oriented objectives without compromising production efficiency. 

## **7 Discussion** 

### **7.1 Insights from results** 

The experimental findings demonstrate that the proposed hybrid Hyper-heuristic–MILP framework successfully achieves multi-objective optimization across makespan, energy consumption, and machine utilization. By integrating adaptive heuristic learning with exact mathematical refinement, the method achieves an average of up to 21.6% energy reduction compared to heuristic-only scheduling, while maintaining or slightly improving production throughput. This confirms that hyper-heuristic adaptability effectively guides the search toward energyefficient regions of the solution space, while the MILP refinement phase improves feasibility control and provides local refinement with solver-reported optimality-gap information. 

Furthermore, the improved workload balance (up to 13.4% higher utilization index) suggests tangible long-term operational benefits: 

- Reduced mechanical wear and power surges due to balanced machine loading; 

- Extended preventive maintenance intervals through stable operational scheduling; 

- Enhanced overall equipment effectiveness (OEE) and predictive maintenance alignment. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

These observations validate that intelligent, data-driven scheduling frameworks are key enablers of sustainable, high-efficiency manufacturing systems in Industry 4.0 environments. 

From a methodological standpoint, the integration of heuristic diversity with mathematical rigor demonstrates that multi-objective optimization can be achieved without the typical trade-off between speed and accuracy. The framework dynamically explores the solution space while preserving convergence guarantees through MILP refinement, striking an effective balance between global exploration and local exploitation. 

### **7.2 Industrial relevance** 

The proposed approach exhibits strong industrial applicability for both real-time and near-real-time decision support. The hyper-heuristic component rapidly generates feasible schedules that comply with operational constraints (e.g., energy caps, machine availability), while the MILP stage refines selected schedules for precisioncritical production runs. This dual-phase mechanism mirrors the operational logic of cyber–physical production systems (CPPS), where edge devices and IoT sensors continuously stream data on machine status, energy usage, and environmental conditions. 

The modular design of the low-level heuristics facilitates customization for specific domains, allowing practitioners to plug in domain-informed heuristics without modifying the high-level control structure. Consequently, the framework can be adapted for: 

- Automotive assembly and component manufacturing, where multi-line coordination and energy optimization are critical; 

- Electronics manufacturing, where machine heterogeneity and reconfiguration frequency are high; 

- High-mix, low-volume (HMLV) environments, where schedule flexibility is more valuable than static optimality. 

Moreover, the framework’s ability to interact with real-time data streams positions it as a potential core module in digital twin architectures, supporting continuous scheduling updates and decision autonomy. 

### **7.3 Practical implementation architecture** 

To bridge the gap between theoretical optimization and real-world deployment, the proposed Hybrid HyperHeuristic–MILP framework is designed to integrate seamlessly with modern Manufacturing Execution Systems (MES) and Cyber-Physical Production Systems (CPPS). In a practical Industry 4.0 environment, the implementation follows an edge-cloud collaborative architecture: 

1. **Data acquisition (IoT layer):** Machine states, processing times, and energy consumption data are continuously streamed via Industrial Internet of Things (IIoT) sensors. This real-time telemetry provides the dynamic parameters (e.g., 𝑝𝑝𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>and 𝑒𝑒</sup> 𝑗<sup>𝑖𝑖</sup> **𝑗**<sup>) required by the scheduling model.</sup> 

2. **Real-time responsiveness (Edge layer):** The adaptive Hyper-Heuristic phase is computationally lightweight and can be deployed on edge computing devices directly on the shop floor. It generates immediate, feasible schedules in response to unexpected disruptions, such as machine breakdowns or rush orders, within seconds. 

3. **Strategic optimization (Cloud layer):** The exact MILP refinement phase requires higher computational power. It can be executed on a centralized cloud server or an on-premise high-performance workstation during off-peak hours or scheduled planning windows. The MILP solver receives the heuristic’s Pareto archive via an API, refines the schedules to optimize energy and workload balance, and pushes the finalized production plan back to the MES. 

This decoupled architecture ensures that the factory maintains high responsiveness to dynamic events while still achieving long-term operational sustainability and energy efficiency. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

### **7.4 Limitations** 

While the presented results are encouraging, several limitations remain that outline future research directions: 

- **Deterministic processing assumptions:** The current model assumes fixed processing and setup times. However, industrial environments often experience stochastic disruptions, variable speeds, or rework loops, which could reduce scheduling accuracy. Future versions should incorporate stochastic or probabilistic processing models. 

- **Energy measurement precision:** The study assumes exact measurement of machine energy profiles. In real deployments, sensor drift, calibration errors, or communication delays can introduce data noise. Robust or fuzzy modeling approaches could mitigate these uncertainties. 

- **Centralized computation:** The proposed system currently executes on a centralized computing unit. Although efficient for mid-scale operations, scaling to geographically distributed manufacturing systems or multi-factory networks will require decentralized coordination, possibly via edge computing or federated optimization. 

- **Processing-related energy modeling:** The current MILP formulation explicitly optimizes processing-related energy consumption. Although idle and ramp-up energy are considered during post-schedule evaluation, they are not directly modeled as time-dependent decision variables. Incorporating full machine-state transitions would require additional binary variables or a time-indexed formulation, which will be addressed in future work. 

- **Integration overhead and data latency:** While the framework is designed for Industry 4.0 environments, deploying it in legacy factories requires significant upfront investment in IIoT sensors and MES integration. Furthermore, network latency or packet loss in wireless sensor networks could delay the transmission of realtime energy data to the edge scheduler. Future work will explore robust optimization techniques to handle delayed or incomplete telemetry data. 

To address these limitations, future work will focus on extending the framework with stochastic hyper-heuristics, robust MILP formulations, and distributed control architectures. Integration with reinforcement learning agents or digital twin environments could further enhance adaptability and resilience under dynamic production conditions. 

## **8 Conclusion and future work** 

This paper presented a hybrid Hyper-Heuristic–MILP framework for multi-objective, energy-aware job scheduling in Industry 4.0 smart manufacturing. The proposed approach combines the adaptive search capability of hyper-heuristics with MILP-based refinement to simultaneously optimize makespan, energy consumption, and workload balance under realistic manufacturing constraints. 

Experimental results on realistic industrial and synthetic benchmark instances demonstrated that the proposed framework consistently generated high-quality schedules while providing feasibility verification and optimalitygap information. Compared with conventional approaches, it achieved up to a 21.6% reduction in energy consumption and a 13.4% improvement in workload balance without sacrificing production throughput. 

From a practical perspective, the proposed framework provides an effective decision-support tool for sustainable manufacturing by enabling energy-efficient scheduling, balanced resource utilization, and improved production planning. However, the current model assumes deterministic operating conditions and has not yet been validated in large-scale real-time manufacturing environments. 

Future work will focus on extending the framework to stochastic and dynamic scheduling scenarios, incorporating real-time IoT data, predictive maintenance, distributed multi-factory scheduling, and renewable energyaware optimization to further enhance its applicability in Industry 5.0 smart manufacturing systems. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

**Author contributions** Kassem Danach: Conceptualization, Methodology, Software, Formal analysis, Investigation, Writing—Original Draft. Hani Haidoura: Methodology, Validation, Data Curation, Writing—Review & Editing. Ali Mansour: Supervision, Methodology, Resources, Writing—Review & Editing. Abbass Nasser: Conceptualization, Supervision, Formal analysis, Writing—Review & Editing, Project administration. 

**Funding** This research receives no funding. 

**Data availability** The datasets generated during and/or analysed during the current study are available from the corresponding author on reasonable request. 

### **Declarations** 

**Ethics approval and consent to participate** Not applicable. 

**Consent for publication** Not applicable. 

**Clinical trial number** Not applicable. 

**Competing interests** The authors declare that they have no competing interests. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 / . 

## **References** 

1. Mämmelä O, Majanen M, Basmadjian R, De Meer H, Giesler A, Homberg W. Energy-aware job scheduler for highperformance computing. Comput Sci-Res Dev. 2012;27(4):265–75. 

2. Sartal A, Bellas R, Mejías AM, García-Collado A. The sustainable manufacturing concept, evolution and opportunities within industry 4.0: a literature review. Adv Mech Eng. 2020;12(5):1687814020925232. 

3. Zhang W, Bao X, Hao X, Gen M. Metaheuristics for multi-objective scheduling problems in industry 4.0 and 5.0: a stateof-the-arts survey. Frontiers in Indust Eng. 2025;3:1540022. 

4. Huang Z, Shen Y, Li J, Fey M, Brecher C. A survey on ai-driven digital twins in industry 4.0: smart manufacturing and advanced robotics. Sensors 2021;21(19), 6340 

5. Parente M, Figueira G, Amorim P, Marques A. Production scheduling in the context of industry 4.0: review and trends. Int J Prod Res. 2020;58(17):5401–31. 

6. Barbosa R, Neto L, Machado P. Hyper-heuristics applications to manufacturing scheduling. Procedia Comput Sci. 2023;221:153–60. https://doi.org/10.1016/j.procs.2023.01.182. 

7. Gao K, Huang Y, Sadollah A, Wang L. A review of energy-efficient scheduling in intelligent production systems. Complex & Intell Sys. 2020;6(2):237–49. 

8. Carlucci D, Renna P, Materi S. A job-shop scheduling decision-making model for sustainable production planning with power constraint. IEEE Trans Eng Manage. 2021;70(5):1923–32. 

9. Jamwal A, Agrawal R, Sharma M, Giallanza A. Industry 4.0 technologies for manufacturing sustainability: a systematic review and future research directions. Appl Sci. 2021;11(12):5725. 

10. Blum C, Roli A. Metaheuristics in combinatorial optimization: overview and conceptual comparison. ACM computing surveys (CSUR). 2003;35(3):268–308. 

11. Kendall G, Cowling P, Soubeiga E. Choice function and random hyperheuristics. Citeseer; 2002. p. 667–71. 

12. Para J, Del Ser J, Nebro AJ. Energy-aware multi-objective job shop scheduling optimization with metaheuristics in manufacturing industries: a critical survey, results, and perspectives. Appl Sci. 2022;12(3):1491. 

13. Pinedo ML. Scheduling: theory, algorithms, and systems. 5th ed. New York, NY: Springer; 2016. 

Discover Sustainability 

https://doi.org/10.1007/s43621-026-04771-9 

Article in Press 

14. Zhang F, Mei Y, Nguyen S, Zhang M. Survey on genetic programming and machine learning techniques for heuristic design in job shop scheduling. IEEE Trans Evol Comput. 2023;28(1):147–67. 

15. Gu W, Li Y, Tang D, Wang X, Yuan M. Using real-time manufacturing data to schedule a smart factory via reinforcement learning. Comput  Ind Eng. 2022;171:108406. 

16. Yin H, Huang X, Cao E. A cloud-edge-based multi-objective task scheduling approach for smart manufacturing lines. J Grid Comput. 2024;22(1):9. 

17. Shakeri Z, Benfriha K, Varmazyar M, Talhi E, Quenehen A. Production scheduling with multi-robot task allocation in a real industry 4.0 setting. Sci Rep. 2025;15(1):1795. 

18. Castro PM, Aguirre AM, Zeballos LJ, Méndez CA. Hybrid mathematical programming discrete-event simulation approach for large-scale scheduling problems. Ind Eng Chem Res. 2011;50(18):10665–80. 

19. Grosch B. Simplified implementation of energy-aware production scheduling. TU Darmstadt; 2023.(Ph.D. Thesis). 

20. Renna P. Energy saving by switch-off policy in a pull-controlled production line. Sustain Prod Consum. 2018;16:25–32. 21. Shao Z, Li W, Tan Y, Otto K. A systematic energy-aware scheduling framework for manufacturing factories integrated with renewables. Int J Prod Res. 2024;62(21):7644–59. 

22. Huang W, Zhao X, Yan H, Zhang W. Event-triggered hybrid energy-aware scheduling in manufacturing systems. J Manuf Syst. 2023;67:362–75. 

23. Mlaouah M, Fekih A, Hajji MK. Energy-efficient scheduling of phosphoric acid processing: a multi-objective approach using nsga-ii and adaptive population-based search. Results Control Optim. 2026;100725. 

24. Nemhauser GL, Wolsey LA. Integer and combinatorial optimization. New York, NY: John Wiley & Sons; 1988. 

25. Zheng Z, Zhang H. A mixed-integer linear programming scheduling optimization model for refinery production. Chem Eng Trans. 2016;51:907–12. 

26. Lee H, Pinto M, Grossmann E, Park S. Mixed-integer linear programming model for refinery short-term scheduling of crude oil unloading with inventory management. Ind Eng Chem Res. 1996;35:1630–41. 

27. Chansombat S, Pongcharoen P, Hicks C. A mixed-integer linear programming model for integrated production and preventive maintenance scheduling in the capital goods industry. Int J Prod Res. 2019;57(1):61–82. 

28. COSTA B, MOURA A, ÁVILA L. Application of mixed-integer linear programming and backward scheduling to reduce waste of operator movement. Acad J Manuf Eng 2025;23(2) 

29. Danach K. Hyperheuristics in logistics. Ecole Centrale de Lille; 2016.(PhD thesis). 

30. Danach K, Saker L, Harb H. Integrating metaheuristics and machine learning for enhanced vehicle routing: a comparative study of hyperheuristic and vae-based approaches. World Electr Veh J. 2025;16(5):258. 

31. Danach K, Harb H, Hejase HJ, Saker L. A hybrid metaheuristic framework with reinforcement learning-based heuristic selection for large-scale combinatorial optimization. European J Pure App Math. 2025;18(3):6602–6602. 

32. Danach K, Aly WHF. Adaptive hyperheuristic framework for hyperparameter tuning: a q-learning-based heuristic selection approach with simulated annealing acceptance criteria. European J Pure App Math. 2025;18(3):6348–6348. 

33. Pellerin R, Perrier N, Berthaut F. A survey of hybrid metaheuristics for the resource-constrained project scheduling problem. Eur J Oper Res. 2020;280(2):395–416. 

34. Wang S, Zhang H, Chu F. An effective hybrid meta-heuristic method for the simultaneous batch production and transportation problem in additive manufacturing. Int J Prod Res. 2025;63(5):1607–23. 

35. Li C, Wei X, Wang J, Wang S, Zhang S. A review of reinforcement learning based hyper-heuristics. PeerJ Comput Sci. 2024;10:2141. 

36. Li Z, Zhou Y, Luo Q. Hyper-heuristic evolutionary algorithm utilizing q-learning for addressing the distributed flexible job-shop scheduling problem in the context of worker absenteeism. J Bionic Eng. 2026;23(3):1932–69. 

37. Castro PM, Aguirre AM, Zeballos LJ, Méndez CA. Hybrid mathematical programming discrete-event simulation approach for large-scale scheduling problems. Ind Eng Chem Res. 2011;50(18):10665–80. 

38. Danach K, Harb H, Aly WHF, Kanj H, Rashid ASK. Bio-inspired optimization through photosynthesis: a novel approach for balancing exploration and exploitation in complex systems. European J Pure App Math. 2025;18(2):5980–5980. 

39. Danach K, Harb H, Rashid ASK, Al-Tarawneh MA, Aly WHF. Location planning techniques for internet provider service unmanned aerial vehicles during crisis. Results Eng. 2025;25:103833. 

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Discover Sustainability 

Article in Press 

https://doi.org/10.1007/s43621-026-04771-9 

## **Authors and Affiliations** 

## **Kassem Danach**<sup>**1**</sup> **· Hani Haidoura**<sup>**2**</sup> **· Ali Mansour**<sup>**3**</sup> **· Abbass Nasser**<sup>**4**</sup> 

Kassem Danach 

kassem.danach@mu.edu.lb 

Hani Haidoura hani.haidoura@ulf.edu.lb 

Ali Mansour ali.mansour@ieee.org 

Abbass Nasser abbass.nasser@ieee.org 

- 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon 

- 2 Business School, Université Libano-Française (ULF), Deddeh, Koura, Lebanon 

- 3 LABSTICC UMR CNRS 6285, ENSTA IP Paris, 29200 Brest, France 

- 4 CIRAME Research Center, Business School, Holy Spirit University of Kaslik, P.O. Box 446, Jounieh, Lebanon 

Discover Sustainability 

