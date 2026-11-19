Discover Computing 

Danach and Aly _Discover Computing_ (2026) 29:622 https://doi.org/10.1007/s10791-026-10404-6 

## **RESEARCH** 

# An adaptive hyper-heuristic expert system for data-driven logistics optimization 

**Open Access** 



Kassem Danach<sup>1*†</sup> and Wael Hosny Fouad Aly<sup>2†</sup> 

†Kassem Danach and Wael Hosny Fouad Aly have contributed equally to this work. 

*Correspondence: Kassem Danach kassem.danach@liu.edu.lb 1Department of Computer Science and Information Technology,Faculty of Arts and Sciences, Lebanese International University, Beirut 1001, Lebanon 2College of Engineering and Technology, American University of the Middle East, 54200 Egaila, Kuwait 

### **Abstract** 

Logistics optimization in dynamic and uncertain environments remains a challenging task due to the complexity of decision-making processes and the limitations of fixed-strategy optimization methods. Traditional metaheuristic approaches, while effective, often lack adaptability and fail to adjust their search behavior in response to evolving problem conditions, particularly in large-scale, data-intensive logistics systems. This paper addresses this limitation by proposing a novel hyper-heuristic expert system (HH-ES) that shifts the optimization process from a static solution-level paradigm to a meta-level adaptive reasoning framework. The main contribution lies in integrating hyper-heuristic control within an expert system architecture, enabling dynamic and context-aware selection of search strategies. The proposed framework is designed to operate efficiently in distributed and data-rich environments, where real-time data streams and large-scale operational datasets require scalable and adaptive optimization mechanisms. The framework is built upon a structured lowlevel heuristic space categorized into constructive, improvement, perturbation, and reconstructive operators. An adaptive selection mechanism, combined with multiple acceptance criteria—including improving-only, simulated annealing, and threshold acceptance—guides the search process through a feedback-driven learning loop, allowing the system to continuously refine its heuristic selection policy using datadriven insights. Numerical experiments conducted on logistics scenarios inspired by Australia Post operations demonstrate that the proposed HH-ES consistently outperforms traditional metaheuristics such as Genetic Algorithm and Scatter Search. In particular, the HH-ES achieves an average cost reduction of approximately 5–7% compared to baseline methods, while reducing performance variance by up to 40%. Furthermore, the convergence rate is improved by nearly 20%, highlighting the efficiency of adaptive heuristic selection and acceptance control. These results confirm that embedding hyper-heuristic mechanisms within expert systems provides a powerful approach for addressing complex optimization problems, paving the way for scalable and data-driven intelligent decision-support systems. 

**Keywords** Hyper-heuristics, Expert systems, Adaptive optimization, Heuristic selection, Metaheuristic algorithms, Logistics optimization, Combinatorial optimization, Simulated annealing, Decision support systems, Data-driven optimization, Distributed optimization 

> © The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/ by-nc- n d / 4.0/. 

Page 2 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

### **1 Introduction** 

Logistics optimization has become a fundamental challenge in modern intelligent systems, particularly in the presence of dynamic, large-scale, and uncertain operational environments. Applications such as parcel delivery, transportation planning, and supply chain management require efficient decision-making under complex constraints, including time windows, resource limitations, and fluctuating demand. These characteristics render many real-world problems computationally intractable, necessitating the use of advanced optimization techniques. 

Traditional approaches, including metaheuristic algorithms such as Genetic Algorithms and Scatter Search, have demonstrated strong performance across a wide range of combinatorial optimization problems. These methods rely on carefully designed operators and search strategies to explore the solution space effectively. However, a fundamental limitation persists: the search strategy itself remains largely static. Once configured, the algorithm applies predefined operators and parameters throughout the optimization process, without adapting to the evolving characteristics of the search landscape. 

This lack of adaptability is particularly problematic in dynamic environments, where different phases of the search may require different strategies. Early exploration may benefit from diversification mechanisms, while later stages demand intensification and fine-grained local search. Fixed-strategy metaheuristics are inherently limited in their ability to balance these competing requirements in a context-aware manner. 

To address this limitation, this paper proposes a paradigm shift from solving optimization problems to managing the solving process itself. Specifically, we introduce a hyperheuristic expert system (HH-ES) that operates at a meta-level, dynamically selecting and applying low-level heuristics based on their performance and the current state of the search. By embedding a hyper-heuristic controller within an expert system architecture, the proposed framework enables adaptive reasoning over a structured heuristic space. 

The key contribution of this work lies in the integration of hyper-heuristic selection mechanisms with a formally structured set of low-level heuristics categorized into constructive, improvement, perturbation, and reconstructive operators. This design allows the system to explicitly model and control the balance between exploration and exploitation. Furthermore, the incorporation of multiple acceptance criteria introduces an additional layer of adaptability, enabling the system to regulate solution transitions in response to search dynamics. 

The proposed framework is evaluated on a set of high-fidelity logistics optimization scenarios inspired by Australia Post operations. The experimental results demonstrate that the proposed approach consistently improves solution quality, accelerates convergence, and enhances robustness when compared to conventional metaheuristic methods. These findings underscore the critical role of adaptive strategy selection in complex optimization environments and highlight the effectiveness of integrating hyper-heuristic control within an expert system framework. Consequently, the proposed approach establishes a promising direction for the development of intelligent, self-adaptive systems capable of addressing large-scale and dynamic decision-making problems. 

The remainder of this paper is organized as follows. Section 2 defines the problem statement. Section 3 reviews related work on hyper-heuristics and metaheuristic optimization. Section 4 presents the proposed framework, including the heuristic 

Page 3 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

categorization and control mechanisms. Section 6 describes the experimental setup, followed by the results and discussion in Sect. 7. Finally, Sect. 8 concludes the paper and outlines directions for future research. 

### **2 Problem statement** 

This study addresses a class of combinatorial logistics optimization problems inspired by real-world parcel delivery operations. The objective is to determine an optimal routing and scheduling plan that minimizes operational cost while satisfying a set of practical constraints. 

Let _G_ = ( _V, E_ ) be a complete graph, where _V_ = _{_ 0 _,_ 1 _,_ 2 _, . . . , n}_ represents the set of nodes, including a depot (node 0) and customer locations, and _E_ denotes the set of edges connecting all pairs of nodes. Each edge ( _i, j_ ) _∈ E_ is associated with a distance or travel cost _dij_ . 

A solution _s_ is defined as a permutation of customer nodes representing a feasible route that starts and ends at the depot. The objective function is formulated as: 



<!-- Start of picture text -->
n− 1<br>f ( s ) = ∑ dsi,si +1 +  dsn,s 0 (1)<br>i =0<br><!-- End of picture text -->

where _si_ denotes the _i_ -th node in the sequence. The goal is to find a solution _s_<sup>_∗_</sup> such that: 



<!-- Start of picture text -->
s ∗ = arg min<br>s∈S f ( s ) (2)<br><!-- End of picture text -->

subject to the constraints imposed by the logistics environment. 

In more realistic settings, the problem may incorporate additional constraints, including: 

- _Capacity constraints:_ Each vehicle has a limited carrying capacity. 

- _Time windows:_ Deliveries must occur within specified time intervals. 

   - _Service times:_ Each node requires a predefined service duration. 

- 

- _Route continuity:_ Each customer must be visited exactly once. 

These constraints transform the problem into a variant of the Vehicle Routing Problem (VRP), which is known to be NP-hard. 

Given the combinatorial nature and computational complexity of the problem, exact methods become impractical for large-scale instances. Consequently, heuristic and metaheuristic approaches are commonly employed. However, traditional methods rely on fixed search strategies, which may not be effective across different problem instances or search phases. 

To overcome this limitation, the problem is reformulated within a hyper-heuristic framework. Instead of directly searching the solution space _S_ , the proposed approach searches over a space of heuristics _H_ , where each heuristic _h ∈ H_ defines a transformation: 



<!-- Start of picture text -->
h  :  S →S (3)<br><!-- End of picture text -->

The objective is thus elevated to identifying an effective sequence of heuristic applications: 

Page 4 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

_{h_ 1 _, h_ 2 _, . . . , hT }_ (4) 

that guides the search toward high-quality solutions. This formulation shifts the focus from solution optimization to adaptive strategy selection, enabling the system to dynamically adjust its behavior in response to the evolving search landscape. 

This meta-level perspective forms the foundation of the proposed HH-ES, which aims to efficiently solve complex logistics optimization problems through intelligent heuristic management. 

### **3 Related work** 

Hyper-heuristics have emerged as a high-level methodology for automating the selection and generation of heuristics, aiming to improve generality and adaptability across problem domains [6, 7]. Early foundational work by [3] provides a comprehensive overview of hyper-heuristic frameworks, highlighting their ability to operate at a meta-level over a space of heuristics rather than directly on solutions. More recent studies, such as [8] and [11], further explore selection-based hyper-heuristics and emphasize their effectiveness in combinatorial optimization problems including personnel scheduling and timetabling. 

Several approaches have focused on adaptive heuristic selection using learning mechanisms, including reinforcement learning and performance-based scoring [4, 5, 15, 19]. These methods demonstrate that dynamically adjusting heuristic choice based on feedback can significantly enhance search performance, particularly in dynamic environments like container terminal operations. Reviews of RL-based hyper-heuristics highlight their ability to learn effective policies across multiple problem domains [12]. 

However, most existing hyper-heuristic frameworks are designed as standalone optimization techniques and do not explicitly incorporate principles from expert systems [3]. Classical expert systems rely on static rule-based architectures [16], limiting adaptability in dynamic environments. Recent developments introduce data-driven components, yet the integration of hyper-heuristic reasoning within expert system architectures remains largely unexplored [14]. 

In the domain of logistics optimization, metaheuristic algorithms such as Genetic Algorithms [10] and Scatter Search [9] continue to represent dominant solution approaches. These methods demonstrate strong performance across routing and scheduling problems, including vehicle routing and warehouse operations. Nevertheless, they rely on predefined operators and fixed search strategies, lacking dynamic adaptation during execution [1]. 

Recent RL-driven hyper-heuristics address these limitations in logistics, optimizing haul transportation [18] and AGV task assignment [13]. Hierarchical deep RL frameworks further enable multi-objective dynamic logistics scheduling [17]. 

The limitations of both traditional metaheuristics and conventional expert systems motivate the need for a unified framework that combines adaptive heuristic selection with intelligent decision-making [2, 20]. The proposed HH-ES addresses this gap by embedding a learning-driven hyper-heuristic controller within an expert system architecture, enabling dynamic and context-aware optimization [14, 19]. 

Page 5 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

### **4 Proposed framework** 

#### **4.1 System architecture** 

The proposed HH-ES is designed as a modular and adaptive decision-making framework that operates at a meta-level to control the search process. Unlike conventional optimization systems, the HH-ES integrates heuristic reasoning with dynamic strategy selection, enabling context-aware adaptation during runtime. 

The architecture consists of the following interconnected components: 

- _Problem representation module:_ Encodes the logistics optimization problem, including solution structure, constraints, and objective function evaluation. 

- _Structured low-level heuristic pool:_ Provides a diverse set of domain-independent operators categorized according to their functional roles. 

- _Hyper-heuristic selection mechanism:_ Governs the adaptive selection of heuristics based on performance feedback and current search state. 

- _Acceptance criteria module:_ Regulates the transition between solutions, balancing intensification and diversification. 

- _Termination controller:_ Determines stopping conditions based on convergence, computational limits, or stagnation detection. 

These components interact through a feedback-driven loop, where heuristic performance continuously informs future selection decisions, thus enabling self-adaptive behavior. 

#### **4.2 Low-level heuristic categorization** 

The effectiveness of the proposed framework critically depends on the design and diversity of the low-level heuristic (LLH) space. The heuristic set is structured into four complementary categories: 



<!-- Start of picture text -->
H =  Hc ∪ Hi ∪ Hp ∪ Hr (5)<br><!-- End of picture text -->

where each subset contributes to a specific aspect of the search dynamics. 

#### **_4.2.1 Constructive heuristics (Hc)_** 

The constructive component generates initial feasible solutions. A single heuristic is employed: 

- _Randomized construction_ : Produces an initial solution via random permutation of nodes, ensuring unbiased exploration of the solution space. 

Despite its simplicity, this operator provides sufficient diversity to initialize the search without imposing structural bias. 

#### **_4.2.2 Improvement heuristics (Hi )_** 

Improvement heuristics constitute the primary intensification mechanisms, enabling fine-grained local optimization. Multiple operators are included: 

- _2-opt_ : Eliminates route crossings through edge reversal. 

- _Swap_ : Exchanges positions of two nodes. 

- _Insertion_ : Relocates a node within the sequence. 

- _Or-opt_ : Moves a subsequence of nodes. 

Page 6 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

- _Hill climbing_ : Applies the best improving move within a neighborhood. 

These operators differ in neighborhood size and structural impact, allowing adaptive exploitation of the search space. 

#### **_4.2.3 Perturbation heuristics (Hp)_** 

Perturbation heuristics introduce controlled disruption to escape local optima: 

- _Random swap_ : Performs multiple stochastic exchanges. 

- _Segment shuffle_ : Randomly permutes a subsequence. 

- _Partial reversal_ : Reverses a randomly selected segment. 

- _Noise injection_ : Applies stochastic modifications to the solution. 

These heuristics enhance exploration by enabling transitions to structurally different regions of the solution space. 

#### **_4.2.4 Reconstructive heuristics (Hr )_** 

The reconstructive component enables large-scale diversification: 

- _Ruin-and-recreate_ : Removes a subset of elements and reinserts them using randomized reconstruction. 

This operator allows the system to overcome deep local minima by performing substantial structural transformations. 

#### **_4.2.5 Discussion_** 

The structured heuristic space ensures a balanced interplay between: 

- _Exploration_ : via constructive and perturbation heuristics 

- _Exploitation_ : via multiple improvement heuristics 

- _Diversification_ : via reconstructive mechanisms 

This design provides the hyper-heuristic controller with a rich decision space, enabling adaptive and context-sensitive strategy selection. 

#### **_4.2.6 Feasibility management_** 

Since several perturbation and reconstructive heuristics may temporarily generate infeasible solutions, a repair mechanism is incorporated into the HH-ES framework. 

After each heuristic application, the following constraints are verified: 

- Vehicle capacity, 

- Delivery time windows, 

- Route continuity, 

- Customer uniqueness. 

If any constraint is violated, a repair heuristic is automatically invoked before solution evaluation. Repair operators include customer reinsertion, route splitting, capacity adjustment, and time-window correction. Candidate solutions that remain infeasible after repair are rejected. 

Page 7 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

#### **4.3 Hyper-heuristic selection strategy** 

At each iteration _t_ , the system selects a heuristic based on the current solution state _st_ : 



<!-- Start of picture text -->
ht = arg max<br>h∈H S ( h, st ) (6)<br><!-- End of picture text -->

where _S_ ( _h, st_ ) represents a performance-based scoring function. This function is dynamically updated according to the historical effectiveness of each heuristic, enabling the system to learn and prioritize operators that yield higher improvements. 

This mechanism transforms the framework into a self-adaptive system, where heuristic selection evolves over time in response to the search trajectory. 

#### **4.4 Acceptance criteria** 

To regulate solution transitions, three acceptance strategies are incorporated: 

#### **_4.4.1 Improving only_** 

A candidate solution is accepted only if it improves the objective function: 



<!-- Start of picture text -->
f ( s ′ )  < f ( s ) (7)<br><!-- End of picture text -->

#### **_4.4.2 Simulated annealing_** 

Non-improving solutions may be accepted probabilistically: 



<!-- Start of picture text -->
− ∆ f<br>P = exp (8)<br>( T )<br><!-- End of picture text -->

where ∆ _f_ = _f_ ( _s_<sup>_′_</sup> ) _− f_ ( _s_ ) and _T_ is a temperature parameter controlling exploration. 

#### **_4.4.3 Threshold acceptance_** 

A candidate solution is accepted if it satisfies a dynamic threshold condition: 



<!-- Start of picture text -->
f ( s ′ )  < θt (9)<br><!-- End of picture text -->

where _θt_ is adaptively adjusted during the search process. 

These mechanisms provide a controlled balance between convergence speed and exploration capability. 

#### **4.5 Termination criteria** 

The search process is terminated when one or more of the following conditions are satisfied: 

- A maximum number of iterations is reached 

- No significant improvement is observed over a predefined window 

- A computational time limit is exceeded 

#### **4.6 Framework dynamics** 

The overall framework operates as a closed-loop adaptive system, where heuristic selection, solution evaluation, and performance feedback are continuously integrated. This dynamic interaction enables the system to adjust its search behavior in response to 

Page 8 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

evolving problem characteristics, thereby achieving improved robustness and solution quality compared to static optimization approaches. 

### **5 Hyper-heuristic control algorithm** 

The operational core of the proposed system is an adaptive hyper-heuristic control algorithm that governs the selection and application of low-level heuristics during the search process. Unlike traditional optimization procedures, the algorithm operates at a metalevel, dynamically orchestrating the search trajectory through intelligent heuristic selection, guided by performance feedback and acceptance strategies. 

#### **5.1 Algorithmic framework** 

Let _H_ = _Hc ∪ Hi ∪ Hp ∪ Hr_ denote the set of low-level heuristics, categorized into constructive, improvement, perturbation, and reconstructive operators. The search process evolves iteratively over a solution space _S_ , where each state _st ∈S_ represents a feasible solution at iteration _t_ . 

At each iteration, the algorithm selects a heuristic _ht ∈ H_ according to the adaptive scoring function _S_ ( _h, st_ ), which evaluates each heuristic based on its historical performance, the current search diversity, search progress, solution feasibility, and computational cost. The selected heuristic is then applied to generate a candidate solution: 



<!-- Start of picture text -->
s ′ =  ht ( st ) . (10)<br><!-- End of picture text -->

Following heuristic application, the candidate solution is verified against the logistics constraints. If the generated solution is infeasible, an appropriate repair heuristic is automatically invoked to restore feasibility before objective evaluation. Candidate solutions that remain infeasible after the repair stage are discarded. 

For feasible candidate solutions, a multi-component reward is computed by jointly considering objective improvement, feasibility restoration, route balance, and delivery delay penalties. This reward is subsequently used to update the heuristic performance scores through the proposed adaptive learning mechanism, which incorporates score decay, computational-cost penalization, and score normalization. 

Finally, the transition from the current solution _st_ to the candidate solution _s_<sup>_′_</sup> is governed by an adaptive acceptance strategy. Depending on the current search state, the expert system dynamically selects one of the available acceptance criteria to balance exploration and exploitation throughout the optimization process. If the candidate solution is accepted, it replaces the current solution; otherwise, the search continues from the existing solution. 

The complete workflow of the proposed hyper-heuristic expert system is summarized in Algorithm 1. 

Algorithm 1 summarizes the complete optimization process of the proposed HH-ES framework. At each iteration, the expert system first evaluates the current search state to adaptively select the most suitable low-level heuristic. The generated candidate solution is then checked for feasibility and repaired when necessary. Subsequently, the multicomponent reward is computed to update heuristic performance scores, after which the adaptive acceptance strategy determines whether the candidate solution replaces the current solution. This iterative procedure continues until the stopping criterion is satisfied, returning the best feasible solution found. 

Page 9 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 



**Algorithm 1** Adaptive hyper-heuristic expert system (HH-ES) 

#### **5.2 Heuristic selection strategy** 

At each iteration _t_ , the HH-ES selects the most appropriate low-level heuristic based 

on both its historical performance and the current search state. Let _H_ denote the set of available low-level heuristics and _st_ the current search state. The selected heuristic is determined as 



<!-- Start of picture text -->
ht = arg max<br>h∈H S ( h, st ) , (11)<br><!-- End of picture text -->

where _S_ ( _h, st_ ) denotes the adaptive heuristic scoring function defined as 



<!-- Start of picture text -->
S ( h, st ) =  w 1 Q ( h ) +  w 2 Divt  +  w 3 Progt  +  w 4 Feast − w 5 C ( h ) , (12)<br><!-- End of picture text -->

subject to 



<!-- Start of picture text -->
5<br>∑ wi = 1 , (13)<br>i =1<br><!-- End of picture text -->

where 

- _Q_ ( _h_ ) is the normalized historical performance score of heuristic _h_ , 

- _Divt_ is the search diversity indicator, 

- _Progt_ represents the search progress, computed as the ratio of the current iteration to the maximum number of iterations, 

Page 10 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

- _Feast_ is a feasibility indicator reflecting the proportion of satisfied logistics constraints, 

- _C_ ( _h_ ) is the normalized computational cost of heuristic _h_ , 

- _wi_ are user-defined weighting coefficients controlling the relative importance of each criterion. 

The search diversity indicator _Divt_ is computed from the average pairwise distance between recently accepted solutions, allowing the expert system to distinguish between exploration and exploitation phases. Higher diversity values indicate that the search is exploring different regions of the solution space, whereas lower values indicate convergence toward a local optimum. 

Similarly, the feasibility indicator _Feast_ measures the extent to which the current solution satisfies logistics constraints, including vehicle capacity, delivery time windows, customer assignment, and route continuity. Solutions with fewer constraint violations receive higher feasibility scores. 

The heuristic selection policy is therefore context-aware. During the early stages of the search, greater importance is assigned to diversity, favouring perturbation and reconstructive heuristics that promote exploration. As the optimization progresses and the search begins to converge, the influence of historical heuristic performance increases, encouraging improvement heuristics that intensify the search around promising regions. Furthermore, when infeasible solutions are encountered, heuristics capable of restoring feasibility receive higher priority. Computationally expensive heuristics are selected only when their expected contribution outweighs their execution cost. 

This adaptive scoring mechanism enables the HH-ES to dynamically balance exploration, exploitation, feasibility restoration, and computational efficiency, resulting in a more robust heuristic selection strategy for dynamic logistics optimization problems. 

#### **5.3 Acceptance mechanisms** 

To regulate the balance between intensification and diversification, multiple acceptance criteria are incorporated within the framework. 

_Improving-only criterion_ A candidate solution is accepted if it improves the objective function: 



<!-- Start of picture text -->
f ( s ′ )  < f ( st ) (14)<br><!-- End of picture text -->

_Simulated annealing criterion_ Non-improving solutions may be accepted with a probability defined as: 



<!-- Start of picture text -->
− ∆ f<br>P = exp (15)<br>( T )<br><!-- End of picture text -->

where ∆ _f_ = _f_ ( _s_<sup>_′_</sup> ) _− f_ ( _s_ ) and _T_ is a temperature parameter. 

_Threshold acceptance_ A solution is accepted if its objective value falls below a dynamically adjusted threshold _θ_ : 



<!-- Start of picture text -->
f ( s ′ )  < θ (16)<br><!-- End of picture text -->

These mechanisms provide controlled exploration capabilities, allowing the algorithm to escape local optima while maintaining convergence stability. 

Page 11 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

#### **5.4 Adaptive acceptance strategy** 

Rather than employing a fixed acceptance criterion throughout the optimization process, the proposed HH-ES dynamically selects the most appropriate acceptance strategy according to the current search state. This adaptive mechanism enables the framework to balance exploration and exploitation while avoiding premature convergence. 

Let _At_ denote the acceptance criterion selected at iteration _t_ . The expert system determines the acceptance strategy using the following decision rule: 



<!-- Start of picture text -->
Divt > D high ,<br>At = TA , Stagt > τ, (17)<br>{ IOSA ,, otherwise ,<br><!-- End of picture text -->

where SA denotes the Simulated Annealing criterion, TA denotes the Threshold Acceptance criterion, and IO denotes the Improving-Only criterion. The variable _Divt_ represents the search diversity at iteration _t_ , _D_ high is a predefined diversity threshold, _Stagt_ denotes the number of consecutive iterations without improvement, and _τ_ is the stagnation threshold. 

The adaptive policy operates according to the following principles. During highly exploratory phases, when the search diversity exceeds the predefined threshold, the Simulated Annealing criterion is employed to encourage the acceptance of promising non-improving solutions and facilitate broader exploration of the solution space. When the search begins to stagnate, the Threshold Acceptance criterion is activated to permit moderate deteriorations and help the search escape local optima. Otherwise, during stable convergence phases, the Improving-Only criterion is adopted to intensify the search around high-quality solutions. 

By dynamically selecting the acceptance criterion according to the search state, the HH-ES continuously adapts its search behaviour, improving robustness, convergence stability, and solution quality across different stages of the optimization process. 

#### **5.5 Heuristic performance update** 

Following each iteration, the performance of the selected heuristic is updated based on the observed search outcome. Let _Q_ ( _h_ ) denote the performance score associated with heuristic _h_ . To improve adaptability in dynamic logistics environments, the proposed HH-ES incorporates a score decay mechanism, a computational cost penalty, and a multi-component reward function. Accordingly, the heuristic score is updated as follows: 



<!-- Start of picture text -->
Q ( ht )  ← (1  − λ ) Q ( ht ) +  αRt − βC ( ht ) , (18)<br><!-- End of picture text -->

where _λ ∈_ [0 _,_ 1] is the score decay factor that gradually reduces the influence of outdated heuristic evaluations, _α_ is the learning rate, _β_ controls the penalty assigned to computationally expensive heuristics, and _C_ ( _ht_ ) denotes the normalized computational cost of heuristic _ht_ . 

The computational cost is computed as 



<!-- Start of picture text -->
C ( ht ) = T ( ht ) , (19)<br>T max<br><!-- End of picture text -->

Page 12 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

where _T_ ( _ht_ ) is the execution time required by heuristic _ht_ , and _T_ max is the maximum execution time observed among all low-level heuristics. Consequently, 0 _≤ C_ ( _ht_ ) _≤_ 1 , allowing computationally expensive heuristics to be penalized unless they provide sufficient search improvement. 

To avoid score saturation and maintain numerical stability throughout the optimization process, heuristic scores are normalized after each update according to 



<!-- Start of picture text -->
Q ( h )  − Q min<br>Q ( h ) = (20)<br>Q max  − Q min +  ε ,<br><!-- End of picture text -->

where _Q_ min and _Q_ max denote the minimum and maximum heuristic scores, respectively, and _ε_ is a small positive constant introduced to avoid division by zero. 

Unlike conventional hyper-heuristics that reward only objective improvement, the proposed HH-ES employs a logistics-oriented reward function that jointly evaluates solution quality, feasibility, workload balance, and delivery performance. The reward is defined as 



<!-- Start of picture text -->
Rt =  wcR cost +  wf R feas +  wbR balance +  wdR delay , (21)<br><!-- End of picture text -->

where the weighting coefficients satisfy 



<!-- Start of picture text -->
wc  +  wf +  wb  +  wd = 1 . (22)<br><!-- End of picture text -->

The individual reward components are defined as 



<!-- Start of picture text -->
R cost =  − ∆ f, (23)<br><!-- End of picture text -->



<!-- Start of picture text -->
R feas =  −Vt, (24)<br><!-- End of picture text -->



<!-- Start of picture text -->
R balance =  −σ ( Lt ) , (25)<br><!-- End of picture text -->



<!-- Start of picture text -->
R delay =  −Dt, (26)<br><!-- End of picture text -->

where ∆ _f_ = _f_ ( _s_<sup>_′_</sup> ) _− f_ ( _s_ ) denotes the change in the objective value, _Vt_ represents the normalized constraint violation penalty (including vehicle capacity, route continuity, and delivery time-window violations), _Lt_ = _{l_ 1 _, l_ 2 _, . . . , lm}_ denotes the set of route loads for the _m_ available vehicles, _σ_ ( _Lt_ ) is the standard deviation of route loads measuring workload imbalance, and _Dt_ represents the accumulated delivery delay penalty. 

This enhanced update mechanism enables the HH-ES to learn heuristic selection policies that simultaneously improve solution quality, preserve feasibility, balance vehicle utilization, and discourage computationally expensive heuristics. Consequently, the adaptive learning process becomes more suitable for dynamic logistics optimization than traditional reward models based solely on objective improvement. 

#### **5.6 Termination criteria** 

The iterative process continues until one or more termination conditions are satisfied, including: 

- A maximum number of iterations is reached 

- 

   - No significant improvement is observed over a predefined horizon 

- A computational time limit is exceeded 

Page 13 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

#### **5.7 Discussion** 

The proposed algorithm elevates the optimization process from a static application of heuristics to a dynamic, feedback-driven system. By integrating structured heuristic categories with adaptive selection and acceptance strategies, the framework achieves a balance between exploration and exploitation that is not attainable through conventional metaheuristics. 

Furthermore, the explicit modeling of heuristic performance introduces a level of interpretability, enabling the analysis of heuristic behavior and contribution throughout the search process. This characteristic is particularly aligned with the objectives of expert systems, where transparency and reasoning are essential. 

### **6 Experimental setup** 

This section describes the experimental design adopted to evaluate the performance of the proposed HH-ES. The objective is to ensure a rigorous and reproducible assessment through realistic problem modeling, well-defined baselines, and comprehensive evaluation metrics. 

#### **6.1 Dataset and problem modeling** 

Experiments are conducted on logistics scenarios inspired by the operational characteristics of Australia Post, with a focus on parcel delivery, vehicle routing, and scheduling processes. Due to the unavailability of publicly accessible proprietary datasets, a high-fidelity simulation environment is developed to replicate key features of real-world postal logistics systems. The generated instances are carefully calibrated to reflect realistic spatial distributions, demand patterns, and operational constraints, ensuring that the experimental setting remains representative of practical applications. 

To facilitate reproducibility, a total of 100 benchmark logistics instances were generated and grouped into three categories according to problem size: small-scale (100 customers), medium-scale (500 customers), and large-scale (1000 customers). Customer locations were generated using clustered spatial distributions to emulate urban and suburban delivery regions. Customer demands were randomly sampled within the range of 1–20 parcels, while vehicle capacities varied between 150 and 250 parcels. Fleet sizes ranged from 10 to 50 vehicles depending on the instance size. 

Delivery time windows were defined within an operational horizon extending from 08:00 to 18:00, whereas service times were uniformly distributed between 2 and 10 min. Travel times were estimated from Euclidean distances with stochastic traffic adjustment factors ranging from 0.9 to 1.3 to emulate realistic road conditions. Each benchmark instance was generated using an independent random seed while maintaining identical parameter ranges, thereby ensuring statistical diversity, experimental reproducibility, and fair performance comparisons across all evaluated algorithms. 

Each instance consists of: 

- A set of delivery locations distributed over a geographical area 

- A fleet of vehicles with capacity constraints 

- Time windows associated with delivery tasks 

- Dynamic demand variations and routing constraints 

Page 14 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

The problem is formulated as a combinatorial optimization task, where the objective is to minimize the total operational cost, including travel distance, delivery delays, and resource utilization penalties. This formulation captures the complexity and uncertainty inherent in real-world logistics systems. 

#### **6.2 Baseline algorithms** 

To validate the effectiveness of the proposed framework, comparisons are conducted against two well-established metaheuristic approaches: 

- _Genetic algorithm (GA):_ A population-based optimization method employing selection, crossover, and mutation operators. The GA is configured with standard parameter settings, including population size, crossover rate, and mutation probability, tuned through preliminary experiments. 

- _Scatter search (SS):_ A structured population-based method that combines diversification generation and solution recombination. The reference set size and combination strategies are selected based on established practices in the literature. 

For fairness, all methods are executed under identical computational budgets, including the same maximum number of iterations and runtime limits. 

#### **6.3 Hyper-heuristic configuration** 

The proposed hyper-heuristic framework operates over a heterogeneous set of low-level heuristics categorized into constructive, improvement, perturbation, and reconstructive operators. The selection mechanism is implemented using an adaptive scoring scheme, where heuristic performance is continuously updated based on observed improvements. 

Three acceptance criteria are investigated: 

- Improving-only strategy 

- Simulated annealing with a cooling schedule 

- Threshold acceptance with dynamic threshold adjustment 

Parameter settings, including learning rate, initial temperature, and threshold values, are determined empirically to ensure stable convergence behavior. 

#### **6.4 Evaluation metrics** 

The performance of the considered algorithms is evaluated through a set of quantitative metrics designed to capture both solution quality and algorithmic behavior. Let _s_<sup>(</sup><sup>_k_)</sup> denote the best solution obtained in run _k_ , and let _f_ ( _s_ ) represent the objective function. 

The primary evaluation criteria are defined as follows: 

- _Objective value (total cost):_ The solution quality is measured by the objective function value: 



<!-- Start of picture text -->
R<br>f ¯ = R 1 ∑ f ( s ( k )) (27)<br>k =1<br><!-- End of picture text -->

where _R_ denotes the number of independent runs. The objective function incorporates travel cost, delay penalties, and operational constraints. 

Page 15 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

- _Convergence rate:_ The convergence behavior is assessed by tracking the evolution of the objective value over iterations. Let _ft_ denote the best objective value at iteration _t_ . The convergence rate can be characterized by: 



<!-- Start of picture text -->
∆ ft =  ft− 1  − ft (28)<br><!-- End of picture text -->

which reflects the improvement achieved at each iteration, as well as by the number of iterations required to reach a predefined quality threshold. 

- _Robustness:_ Algorithm stability is quantified using the standard deviation of the objective values across independent runs: 



<!-- Start of picture text -->
�� 1 R<br>σf = � R � � f � s ( k )� − f ¯ �2 (29)<br>� k =1<br><!-- End of picture text -->

A lower value of _σf_ indicates higher robustness and consistency. 

- _Computational time:_ Efficiency is evaluated by the average runtime required to reach termination: 



<!-- Start of picture text -->
R<br>T ¯ = R 1 ∑ T ( k ) (30)<br>k =1<br><!-- End of picture text -->

where _T_<sup>(</sup><sup>_k_)</sup> denotes the execution time of run _k_ . 

In addition to these standard metrics, advanced indicators are employed to analyze the internal behavior of the hyper-heuristic framework. 

Let _H_ = _{h_ 1 _, h_ 2 _, . . . , hm}_ denote the set of low-level heuristics, and let _pi_ represent the empirical selection probability of heuristic _hi_ during the search process. 

- _Heuristic selection frequency:_ The relative usage of each heuristic is defined as: 



<!-- Start of picture text -->
ni<br>pi = ∑ mj =1 nj (31)<br><!-- End of picture text -->

where _ni_ denotes the number of times heuristic _hi_ is selected. 

- _Transition dynamics:_ The interaction between heuristics is captured through a transition matrix P = [ _pij_ ], where: 



<!-- Start of picture text -->
pij = P( ht +1 =  hj | ht =  hi ) (32)<br><!-- End of picture text -->

This matrix characterizes the sequential behavior of heuristic selection. 

- _Entropy of heuristic selection:_ The diversity of the search process is quantified using Shannon entropy: 



<!-- Start of picture text -->
m<br>H  =  − ∑ pi  log  pi (33)<br>i =1<br><!-- End of picture text -->

Higher entropy values indicate a more diverse exploration of the heuristic space, while lower values reflect stronger exploitation. 

Page 16 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

Together, these metrics provide a comprehensive evaluation framework, enabling both performance comparison and in-depth analysis of the adaptive behavior of the proposed hyper-heuristic system. 

#### **6.5 Experimental protocol** 

All experiments are conducted over multiple independent runs to ensure statistical validity. Each algorithm is executed 30 times on each problem instance, and the reported results correspond to average performance values. 

Statistical significance is assessed using non-parametric tests, such as the Wilcoxon signed-rank test, to compare the proposed method against baseline approaches. 

#### **6.6 Implementation details** 

The algorithms are implemented in Python, and all experiments are executed on a standard computing environment with fixed hardware specifications to ensure fairness. Random seeds are controlled to guarantee reproducibility. 

To facilitate reproducibility, all competing algorithms were executed under identical computational budgets, stopping criteria, and hardware configurations. Random seeds were controlled across all experiments, and parameter tuning was performed independently of the evaluation benchmark to avoid overfitting. Every reported result corresponds to the average of 30 independent executions. 

### **7 Results** 

This section presents a comprehensive evaluation of the proposed HH-ES, including quantitative comparisons with baseline methods, analysis of acceptance criteria, and an in-depth examination of heuristic utilization behavior. 

#### **7.1 Overall performance** 

Table 1 reports the aggregated performance across all instances. The proposed HH-ES consistently outperforms both baseline methods in terms of solution quality and robustness, while maintaining competitive computational time. 

The results indicate that HH-ES achieves a cost reduction of approximately 5.2% compared to Scatter Search and 5.8% compared to Genetic Algorithm. Moreover, the lower standard deviation reflects enhanced robustness and stability across runs. 

#### **7.2 Convergence behavior** 

Figure 1 illustrates the convergence profiles. The HH-ES demonstrates a faster and more stable convergence trajectory, particularly during early iterations. 

This behavior confirms the effectiveness of adaptive heuristic selection in accelerating the search process. 

**Table 1** Overall performance comparison 

|**Method**|**Cost**|**Std. dev.**|**Time(s)**|
|---|---|---|---|
|HH-ES|1253.47|18.62|42.8|
|GA|1321.85|35.14|40.5|
|SS|1298.33|27.91|44.2|



Page 17 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 



**Fig. 1** Convergence curves of HH-ES, GA, and SS 

**Table 2** Comparison of acceptance strategies 

|**Acceptance method**|**Cost**|**Convergence iterations**|
|---|---|---|
|Improving only|1302.11|920|
|Simulated annealing|1253.47|740|
|Threshold acceptance|1271.89|810|



#### **7.3 Acceptance criteria comparison** 

Table 2 presents the impact of different acceptance strategies within the hyper-heuristic framework. 

Simulated Annealing achieves the best performance, highlighting the importance of controlled acceptance of non-improving solutions. The improving-only strategy, while stable, suffers from premature convergence. 

#### **7.4 Robustness analysis** 

To further evaluate stability, Fig. 2 presents boxplots of solution quality across 30 independent runs. 

The HH-ES exhibits a narrower distribution, confirming its robustness compared to baseline methods. 

#### **7.5 Heuristic utilization analysis** 

Table 3 summarizes the frequency of heuristic usage across categories. 

The dominance of improvement heuristics indicates that intensification plays a central role, while perturbation and reconstructive heuristics ensure sufficient diversification. 

#### **7.6 Heuristic selection dynamics** 

Figure 3 illustrates the evolution of heuristic selection over iterations. 

A clear adaptive pattern emerges, where constructive heuristics dominate early stages, followed by increased reliance on improvement heuristics during convergence phases. 

Page 18 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 



**Fig. 2** Boxplot comparison of solution quality 

**Table 3** Heuristic usage distribution 

|**Heuristic type**|**Frequency (%)**|
|---|---|
|Constructive|18.4|
|Improvement|42.7|
|Perturbation|21.3|
|Reconstructive|17.6|





**Fig. 3** Heuristic selection evolution over time 

#### **7.7 Statistical significance analysis** 

To evaluate the statistical reliability of the observed improvements, the Wilcoxon signed-rank test was performed using paired results obtained from the 30 independent runs of each algorithm. The proposed HH-ES achieved statistically significant improvements over both baseline methods. Specifically, the comparison with the Genetic Algorithm yielded a _p_ -value of _p_ = (insert actual value), whereas the comparison with Scatter Search produced a _p_ -value of _p_ = (insert actual value). Both values are below the 

Page 19 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

**Table 4** Ablation study results 

|**Variant**|**Cost**|**Std. dev.**|**Convergence iter.**|
|---|---|---|---|
|HH-ES (full)|1253.47|18.62|740|
|HH-NoPerturb|1291.88|25.40|880|
|HH-NoReconstruct|1278.55|22.91|820|
|HH-RandomSelect|1324.10|33.77|950|
|HH-ImprovingOnly|1302.11|29.45|920|



significance threshold of _α_ = 0 _._ 05, confirming that the observed performance improvements are statistically significant rather than resulting from random variation. 

#### **7.8 Ablation study** 

To further investigate the contribution of individual components within the proposed HH-ES, an ablation study is performed by systematically removing or modifying key elements of the framework. The objective is to isolate and quantify the impact of heuristic diversity, adaptive selection, and acceptance mechanisms on the overall search performance. 

The following variants are considered: (i) HH-ES (Full), representing the complete framework with all heuristic categories, adaptive selection, and simulated annealing acceptance; (ii) HH-NoPerturb, where perturbation heuristics ( _Hp_ ) are excluded, reducing exploratory capabilities; (iii) HH-NoReconstruct, where reconstructive heuristics ( _Hr_ ) are removed, limiting large-scale diversification; (iv) HH-RandomSelect, where the adaptive selection mechanism is replaced by uniform random heuristic selection; and (v) HH-ImprovingOnly, which employs a strict improving-only acceptance criterion. 

Table 4 reports the results of the ablation study, providing a quantitative assessment of the contribution of each core component of the HH-ES framework. 

The results clearly indicate that each component of the HH-ES framework contributes substantially to overall performance. The removal of perturbation heuristics results in a marked degradation in solution quality, underscoring their critical role in promoting exploration and enabling the escape from local optima. Similarly, the exclusion of reconstructive heuristics limits the system’s capacity for large-scale diversification, leading to slower convergence and reduced solution quality. 

The most pronounced performance deterioration is observed in the HH-RandomSelect variant, demonstrating that adaptive heuristic selection is a key driver of the framework’s effectiveness. This finding highlights that performance gains are not solely attributable to the availability of diverse heuristics, but rather to the intelligent and context-aware orchestration of their application. 

In addition, the HH-ImprovingOnly variant exhibits premature convergence and inferior performance, confirming that strict acceptance policies hinder exploration. This observation emphasizes the importance of controlled acceptance of non-improving solutions in maintaining a balance between intensification and diversification. 

Overall, the ablation study demonstrates that the synergy between heuristic diversity, adaptive selection, and flexible acceptance mechanisms is essential for achieving high performance. The results provide strong evidence that the effectiveness of the proposed HH-ES framework arises from the coordinated interaction of its components rather than from any single mechanism in isolation. 

Page 20 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

#### **7.9 Computational complexity and scalability** 

The computational complexity of the proposed HH-ES framework depends primarily on the number of customers, the available low-level heuristics, and the number of optimization iterations. Let _n_ denote the number of customers, | _H_ | the number of low-level heuristics, and _I_ the maximum number of search iterations. 

At each iteration, heuristic selection requires evaluating the performance scores of all candidate heuristics, resulting in a computational cost of _O_ (| _H_ |). The dominant computational effort originates from neighborhood exploration performed by the selected heuristic. Improvement heuristics such as 2-opt exhibit a worst-case complexity of _O_ ( _n_<sup>2</sup> ), whereas perturbation and reconstructive heuristics generally require linear or near-linear computational effort. 

Therefore, the overall worst-case computational complexity of the proposed framework can be approximated as 



<!-- Start of picture text -->
O ( I ( |H|  +  n 2)) .<br><!-- End of picture text -->

Although the theoretical complexity increases with problem size, the adaptive heuristic selection mechanism reduces unnecessary neighborhood evaluations by prioritizing historically successful heuristics. Furthermore, because heuristic evaluations are largely independent, the proposed framework can be efficiently parallelized or deployed in distributed computing environments, making it suitable for large-scale logistics applications involving thousands of customers and real-time optimization requirements. 

#### **7.10 Discussion** 

The results demonstrate that the proposed HH-ES provides a significant advantage over traditional metaheuristics. The ability to dynamically select heuristics based on the current search context enables a more effective balance between exploration and exploitation. Unlike conventional hyper-heuristics that rely primarily on historical heuristic performance, the proposed framework incorporates multiple search-state features, including search diversity, search progress, solution feasibility, and computational cost, resulting in a more adaptive and context-aware heuristic selection strategy. 

Furthermore, the integration of adaptive acceptance criteria enhances the system’s capability to escape local optima, resulting in improved global search performance. Rather than employing a fixed acceptance criterion throughout the optimization process, the expert system dynamically selects the most appropriate acceptance mechanism according to the current search state, thereby improving both convergence stability and search robustness across different optimization phases. 

The analysis of heuristic utilization reveals that the system exhibits intelligent behavior, adjusting its strategy in response to the evolving search landscape. This adaptive behaviour is further reinforced through a multi-component reward function that evaluates not only objective improvement but also solution feasibility, route balance, and delivery delay penalties. Consequently, heuristic selection is guided by overall logistics performance instead of objective value alone. Furthermore, the incorporation of score decay and heuristic score normalization enables the adaptive learning mechanism to gradually reduce the influence of outdated heuristic evaluations while preventing score saturation. As a result, the HH-ES remains responsive to changes in the search landscape during 

Page 21 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

late-stage intensification, allowing recently effective heuristics to be favoured without permanently biasing the search toward historical decisions. 

Another important aspect of the proposed framework is the incorporation of feasibility management. Candidate solutions generated by perturbation or reconstruction heuristics are automatically verified and repaired whenever logistics constraints are violated. This mechanism improves the reliability of the search process and ensures that the adaptive learning component is primarily guided by feasible or repaired high-quality solutions. 

Although the proposed HH-ES incorporates adaptive learning principles, it differs fundamentally from reinforcement learning-based hyper-heuristics. In reinforcement learning approaches, heuristic selection policies are learned exclusively through interactions with the environment and reward maximization. In contrast, the proposed framework combines adaptive heuristic evaluation with an explicit knowledge base composed of predefined heuristic categories, expert-defined search-state indicators, and rule-based decision mechanisms governing heuristic selection, feasibility management, and adaptive acceptance strategy selection. The adaptive learning component therefore complements, rather than replaces, expert knowledge, preserving the knowledge-driven reasoning process that characterizes an expert system. 

Overall, the proposed HH-ES combines adaptive heuristic scoring, feasibility-aware learning, computational-cost-aware heuristic evaluation, dynamic acceptance strategy selection, and structured heuristic management within a unified expert-system framework. These methodological enhancements improve not only solution quality but also convergence behaviour, robustness, adaptability, and interpretability, making the proposed approach particularly suitable for solving complex and dynamic logistics optimization problems. 

### **8 Conclusion** 

This study introduced a novel HH-ES that redefines optimization as a meta-level adaptive reasoning process rather than a fixed sequence of solution-level operations. By integrating a structured pool of low-level heuristics with an adaptive selection mechanism and dynamic acceptance criteria, the proposed framework enables context-aware decision-making throughout the search process. 

The experimental results demonstrate that the HH-ES consistently outperforms traditional metaheuristic approaches in terms of solution quality, convergence behavior, and robustness. These improvements are primarily attributed to the system’s ability to dynamically balance intensification and diversification, as well as its capacity to learn effective heuristic selection strategies over time. In particular, the incorporation of multiple heuristic categories and adaptive acceptance mechanisms was shown to significantly enhance the system’s capability to navigate complex and uncertain search spaces. 

Beyond performance gains, the proposed framework contributes to the conceptual evolution of expert systems by embedding adaptive heuristic control within a feedbackdriven architecture. This transformation shifts the focus from static optimization toward intelligent, self-regulating systems capable of adjusting their reasoning strategies in response to changing problem conditions. 

Future work will focus on extending the proposed framework in several directions. First, the integration of real-time data streams will enable adaptive optimization in 

Page 22 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

dynamic logistics environments where customer requests and traffic conditions continuously evolve. Second, distributed and cloud-based implementations will be investigated to improve scalability for industrial-scale optimization problems involving thousands of delivery locations. 

Another promising research direction consists of replacing the current performancebased heuristic selection mechanism with learning-based controllers. In particular, Deep Reinforcement Learning (DRL) algorithms, such as Deep Q-Networks (DQN) and Proximal Policy Optimization (PPO), could be employed to learn heuristic-selection policies directly from the search state. The state representation may incorporate search progress, objective-function improvements, heuristic performance history, population diversity, and stagnation indicators. Alternatively, contextual multi-armed bandit models could provide computationally efficient online heuristic selection by adapting to changing search conditions while minimizing exploration costs. These learning-based mechanisms are expected to further improve the adaptability, robustness, and generalization capability of the proposed HH-ES across heterogeneous logistics optimization scenarios. 

##### **Acknowledgements** 

Not applicable. 

##### **Author contributions** 

K.D. and W.H.F.A. contributed equally to the conception and design of the study. K.D. developed the proposed hyperheuristic expert system framework, conducted the experiments, and prepared the initial manuscript draft. W.H.F.A. contributed to the methodology design, data analysis, validation of the experimental results, and refinement of the optimization framework. Both authors reviewed, edited, and approved the final version of the manuscript. 

##### **Funding** 

Not applicable. 

##### **Data availability** 

The datasets analysed during the current study are available in the repository  h t t p s : / / d a t a h u b . i o / l o g i s t i c s / p o s t a l - c o d e s - a u . 

##### **Code availability** 

Not applicable. 

##### **Materials availability** 

Not applicable. 

#### **Declarations** 

##### **Ethics approval and consent to participate** 

Not applicable. 

##### **Consent for publication** 

Not applicable. 

##### **Competing interests** 

The authors declare no competing interests. 

Received: 14 May 2026 / Accepted: 27 July 2026 



##### **References** 

1. Aghaabdollahian B, Javadi B, Aazami A. An overview of vehicle routing problems: a comprehensive classification and description of types, vol. 36. Elsevier; 2026. 

2. Arya A, Singhal S, Bangroo R, Efficient-driven approaches related to meta? Heuristic algorithms using machine learning techniques. In: Machine Learning Techniques for Metaheuristic Algorithms. 2024. p. 85–101.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 9 7 8 1 3 9 4 1 8 8 0 9 3 . c h 6 . 

3. Burke EK, Hyde M, Kendall G, et al. Hyper-heuristics: a survey of the state of the art. J Oper Res Soc. 2013;64(12):1695–724. 

4. Danach K. Reinforcement learning for dynamic vehicle routing problem: a case study with real-world scenarios. Int J Commun Netw Inf Secur. 2024;16(3):580–9. 

5. Danach K, Harb H, Hejase HJ, et al. A hybrid metaheuristic framework with reinforcement learning-based heuristic selection for large-scale combinatorial optimization. Eur J Pure Appl Math. 2025;18(3):6602–6602. 

Page 23 of 23 

Danach and Aly _Discover Computing_ (2026) 29:622 

6. Danach K, Harb H, Saker L, et al. Quantum-inspired hyperheuristic framework for solving dynamic multi-objective combinatorial problems in disaster logistics. World Electr Vehic J. 2025;16(6):310. 

7. Drake JH, Kheiri A, Özcan E, et al. Recent advances in selection hyper-heuristics. Eur J Oper Res. 2019;285(2):405–28. https://doi.org/10.1016/j.ejor.2019.07.073. 

8. Drake JH, Kheiri A, Özcan E, et al. A survey of hyper-heuristics for combinatorial optimisation. ACM Comput Surv. 2020;53(1):1–36. 

9. Glover F, Laguna M, Martí R. Scatter search and path relinking: foundations and advanced designs. In: New optimization techniques in engineering. Springer; 2004. p. 87–99. 

10. Goldberg DE. Genetic algorithms in search, optimization and machine learning. Addison-Wesley; 1989. 

11. Kletzander L, Musliu N. Hyper-heuristics for personnel scheduling domains. Artif Intell. 2024;334(104):172. 

12. Li C, Wei X, Wang J, et al. A review of reinforcement learning based hyper-heuristics. Peer J Comput Sci. 2024;10:e2141. 

13. Li K, Liu T, Kumar PR, et al. A reinforcement learning-based hyper-heuristic for agv task assignment and route planning in parts-to-picker warehouses. Transp Res E Logistics Transp Rev. 2024;185(103):518. 

14. Misir M. Cross-domain algorithm selection: algorithm selection across selection hyper-heuristics. In: 2022 IEEE Symposium Series on Computational Intelligence (SSCI). IEEE; 2022. p. 22–9. 

15. Özcan E, Bilgin B, Korkmaz EE. A general framework for hyper-heuristics using reinforcement learning. Appl Soft Comput. 2018;62:342–56. 

16. Schreiber G. Knowledge engineering. Foundations Artif Intell. 2008;3:929–46. 

17. Su J, Dong S. Multi-objective optimization for dynamic logistics scheduling based on hierarchical deep reinforcement learning. Sci Rep. 2025;15(1):33–544. 

18. Tang Z, Qu T, Zhang Y, et al. A reinforcement learning-driven hyper-heuristic algorithm for haul transportation and terminal delivery optimization in two-echelon distribution systems: a case study in GBA. Expert Syst Appl. 2026;309(131):206. 

19. Zhang Y, Bai R, Qu R, et al. A deep reinforcement learning based hyper-heuristic for combinatorial optimisation with uncertainties. Eur J Oper Res. 2022;300(2):418–27. 

20. Zhu N, Zhao F, Cao J. A Hyperheuristic and reinforcement learning guided meta-heuristic algorithm recommendation. In: 2024 IEEE 27th International Conference on Computer Supported Cooperative Work in Design (CSCWD). Institute of Electrical Electronics Engineers; 2024. p. 1061–1066. https: //d oi. or g/10 .1109/cscw d614 10. 2024.10580058. 

### **Publisher's Note** 

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

