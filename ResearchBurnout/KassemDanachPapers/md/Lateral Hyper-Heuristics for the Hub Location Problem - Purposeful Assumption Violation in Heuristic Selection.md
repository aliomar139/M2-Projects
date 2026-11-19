Eng. Sci., 2026, **41** , 2212 



<!-- Start of picture text -->
..<br><!-- End of picture text -->

Engineered Science 

DOI: https://dx.doi.org/10.30919/es2212 





# **Lateral Hyper-Heuristics for the Hub Location Problem: Purposeful Assumption Violation in Heuristic Selection** 

Kassem Danach,<sup>1,*</sup> Wael Hosny Fouad Aly,<sup>2</sup> Chadi Fouad Riman<sup>2</sup> and Samir Haddad<sup>3</sup> 

## **Abstract** 

The Hub Location Problem (HLP) is a challenging combinatorial optimization problem characterized by deceptive search landscapes and strong centralization biases. Conventional hyper-heuristics, which rely on rational, reward-based heuristic selection, often become trapped in suboptimal solutions. To overcome this limitation, we propose the Lateral Hyper-Heuristic (LHH) framework, which dynamically alternates between Rational Mode for exploitation and Lateral Mode for directed exploration. By monitoring indicators such as search stagnation, hub entropy, and heuristic dominance, LHH identifies epistemic traps and applies low-level heuristics that deliberately violate dominant search assumptions, enabling structural transitions in the solution space. Extensive experiments on the Uncapacitated Single Allocation p-Hub Median Problem (USApHMP) using CAB and AP benchmark datasets show that LHH reduces the average percentage deviation from known lower bounds by 76% compared to the state-of-the-art hyper-heuristic. Furthermore, LHH escapes stagnation more than twice as often, demonstrating that structured assumption violation is a highly effective mechanism for navigating deceptive optimization landscapes. These results establish LHH as a significant advancement in automated heuristic selection for complex combinatorial problems. 

_Keywords:_ Lateral hyper-heuristic; Hub location problem; Hyper-heuristics; Heuristic selection; Epistemic traps. Received: 08 February 2026; Revised: 09 April 2026; Accepted: 27 April 2026 Article type: Research article. 

### **1. Introduction** 

Hub-and-spoke networks are the backbone of modern transportation, logistics, and telecommunication systems, forming the operational architecture for everything from air freight and package delivery to data routing and supply chain management.<sup>[1,2]</sup> The strategic design of these networks is formalized as the Hub Location Problem (HLP), a central and notoriously difficult optimization challenge.<sup>[3]</sup> The HLP involves making two tightly coupled decisions: selecting a subset of nodes to serve as consolidation hubs, and routing flows between all origindestination pairs through these hubs. The complexity is amplified by economies of scale on inter-hub links, which offer discounted transportation costs but introduce strong, 

> _1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, 1001, Lebanon_ 

> _2College of Engineering and Technology, American University of the Middle East, Egaila, 54200, Kuwait_ 

> _3Faculty of Arts and Sciences, Department of Computer Science, University of Balamand, Koura, 100, Lebanon_ 

> _*Email:_ kassem.danach@mu.edu.lb (K. Danach) 

non-linear interactions into the objective function.<sup>[4]</sup> 

These properties induce highly deceptive search landscapes, where locally effective decisions ( _e.g._ , centralizing hubs) can create powerful biases that restrict long-term exploration and trap search algorithms in suboptimal regions of the solution space.<sup>[5]</sup> 

To navigate such complex landscapes, hyper-heuristics have emerged as a powerful and general-purpose strategy.<sup>[6]</sup> A hyper-heuristic can be defined as a search method that operates on a higher level of abstraction, selecting or generating low-level heuristics to apply to a problem at hand. This approach aims to automate the design of heuristics and has shown success across a wide range of combinatorial optimization problems.<sup>[7]</sup> Nevertheless, the vast majority of existing hyper-heuristic frameworks are built upon rational selection principles. These methods, whether based on reinforcement learning, choice functions, or bandit algorithms, share a common underlying assumption: heuristics that have demonstrated superior performance in the recent past should be preferred in the future.<sup>[8]</sup> This paper argues that in the deceptive landscapes 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2212 | **1** 

**<u>gineered Science</u>** 

characteristic of the HLP, such myopic rationality constitutes a fundamental limitation rather than a strength, as it systematically reinforces the very structural assumptions that lead to entrapment.<sup>[9]</sup> 

To overcome this limitation, we draw inspiration from contemporary interpretations of lateral thinking as a structured creativity and pattern-disruption mechanism in problem solving.<sup>[10]</sup> We propose a novel Lateral HyperHeuristic (LHH) framework that intentionally violates the dominant search assumptions to induce structural transitions and escape from epistemic traps. Instead of merely rewarding recent success, the LHH framework monitors the search context for signs of stagnation and assumption reinforcement. When such a trap is detected, it switches from a rational exploitation mode to a lateral exploration mode, where heuristics are selected specifically for their ability to contradict the prevailing search bias. 

The main contributions of this paper are threefold: We provide a formal definition of epistemic traps in the context of combinatorial optimization and articulate the limitations of rational, myopic heuristic selection mechanisms within such traps.<sup>[6]</sup> 

We propose and detail the Lateral Hyper-Heuristic framework, a novel selection-based hyper-heuristic that incorporates context indicators and specialized lateral operators ( _e.g._ , Assumption Violation, Role Reversal) to guide purposeful, non-myopic search behavior. 

We present a rigorous empirical evaluation on the Uncapacitated Single Allocation p-Hub Median Problem (USApHMP), demonstrating that the proposed framework not only achieves superior solution quality com-pared to state-of-the-art baselines but also exhibits a quantifiably higher capacity to escape from stagnation. 

The remainder of this paper is organized as follows. Section 2 reviews the relevant literature on hub location problems and hyper-heuristic selection mechanisms. Section 3 provides a precise mathematical formulation of the USApHMP. Section 4 introduces the concept of epistemic traps and argues their prevalence in hub location search. Section 5 details the proposed Lateral HyperHeuristic framework, including its solution representation, low-level heuristics, and lateral selection operators. Section 7 describes the experimental setup, and Section 8 presents and discusses the comprehensive results. Finally, Section 9 concludes the paper and outlines directions for future research. 

### **2. Related work** 

The Hub Location Problem (HLP) remains a central challenge in network design optimization and continues to attract sustained research interest due to its applicability in transportation, logistics, and communication networks.<sup>[11,12]</sup> Although early studies emphasized exact mathematical 

formulations, recent research has increasingly focused on scalable solution methodologies to cope with the NP-hard nature of most HLP variants.<sup>[13]</sup> This shift has accelerated the adoption of advanced heuristic, metaheuristic, and hyper-heuristic approaches. This section reviews recent developments in HLP solution methodologies, emphasizing contemporary metaheuristics, state-of-the-art selection hyper-heuristics, and positioning the proposed Lateral Hyper-Heuristic (LHH) framework as a principled alternative to existing paradigms. 

### **2.1 Foundational models and classical metaheuristics** 

Recent surveys and methodological reviews have revisited foundational hub location models, consolidating advances in uncapacitated and capacitated formulations under modern optimization perspectives.<sup>[11]</sup> Contemporary studies have refined classical formulations by incorporating realistic cost structures, capacity limitations, and allo-cation policies, enabling improved modeling fidelity for large-scale logistics networks.<sup>[14]</sup> Linearization techniques and decomposition-based strategies remain relevant, particularly when integrated with modern solvers and hybrid frameworks.<sup>[4]</sup> For computationally challenging instances such as the Uncapacitated Single Allocation _p_ -Hub Median Problem (USApHMP), recent works continue to employ classical metaheuristics enhanced with adaptive mechanisms. Simulated Annealing, Tabu Search, Genetic Algorithms, and Variable Neighborhood Search have been revisited using modern parameter control strategies and hybridization schemes.<sup>[15,16]</sup> These methods typically rely on neighbor-hood operators including hub insertion, relocation, and exchange moves. However, recent empirical analyses confirm that the multimodal fitness landscape of the HLP—particularly under strong inter-hub discounting ( _α_ ∈ [0 _,_ 1])—still induces premature convergence toward overly centralized hub configurations.<sup>[17]</sup> As a result, these methods often struggle to balance facility establishment costs against economies of scale, motivating the exploration of higher-level adaptive control strategies. 

### **2.2 Selection hyper-heuristics: state-of-the-art in HLP** 

Hyper-heuristics have gained prominence as a generalpurpose optimization paradigm capable of autonomously managing heuristic selection and adaptation across problem instances.<sup>[18]</sup> Selection hyper-heuristics, in particular, operate at a meta-level by dynamically choosing low-level heuristics (LLHs) based on performance feedback. Recent implementations leverage reinforcement learning, choice functions, and multi-armed bandit (MAB) formulations to guide the selection process.<sup>[19,20]</sup> 

In the context of HLPs, recent studies have proposed hybrid hyper-heuristic frameworks that integrate mathematical programming components with learning- 

**2** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 

based LLH selection mechanisms.<sup>[21]</sup> While these approaches demonstrate notable performance improvements over standalone metaheuristics, they remain predominantly exploitative, favoring heuristics that yield immediate reward signals. This behavior can exacerbate entrapment in local optima induced by _α_ -driven centralization effects, particularly in epistatic search landscapes. Related efforts include adaptive memorybased hyper-heuristics<sup>[22]</sup> and deep reinforcement learning– assisted heuristic selection,<sup>[23]</sup> which further enhance adaptability but still lack explicit mechanisms for challenging entrenched search assumptions. 

More recently, data-driven hyper-heuristics employing surrogate models and cross-instance generalization have been proposed, enabling broader applicability across multiple HLP variants.<sup>[7]</sup> Additionally, stochastic and multi-objective HLP formulations have incorporated simheuristic extensions to address uncertainty in demand and transportation costs.<sup>[24]</sup> Despite these advances, structural deception and premature convergence remain persistent challenges. 

A substantial body of recent work has advanced adaptive optimization, hyper-heuristic design, and learning-driven decision frameworks across diverse application domains. In particular, genetic algorithmbased hyper-heuristics and reinforcement learning strategies have been proposed for quality-of-service optimization, load balancing, and hyperparameter tuning in complex systems.<sup>[25–27]</sup> Complementary efforts have explored transparent and explainable optimization paradigms to improve interpretability and trust in automated decision-making processes.<sup>[28]</sup> Beyond core heuristic frameworks, Aly’s research has demonstrated the applicability of adaptive and learning-based methods in distributed and dynamic environments, including software-defined networking controller architectures and placement strategies,<sup>[29–31]</sup> trust-aware task offloading in heterogeneous edge–fog–cloud systems,<sup>[32]</sup> machine learning for smart grid reliability,<sup>[33]</sup> and intelligent state estimation for assistive mobility systems.<sup>[34]</sup> Collectively, these contributions highlight a consistent methodological focus on adaptive heuristic control, exploration–exploitation balancing, and learning-driven optimization, which conceptually underpins the proposed Lateral HyperHeuristic framework. 

### **2.3 LHH: principled epistemic escape** **_via_ assumption violation** 

Modern metaheuristic escape strategies are still largely framed around intensification and diversification mechanisms.<sup>[35]</sup> Intensification deepens the search within promising regions, whereas diversification introduces stochastic perturbations or restarts to explore new areas of the solution space.<sup>[36]</sup> While effective in some settings, both strategies implicitly reinforce or randomly abandon 

the assumptions underpinning the current search trajectory, often leading to inefficiencies. 

The proposed Lateral Hyper-Heuristic (LHH) framework introduces a third, complementary paradigm based on structured assumption violation. Inspired by contemporary interpretations of lateral thinking in computational problem solving,<sup>[37]</sup> the LHH framework incorporates explicit trap-detection mechanisms using indicators such as stagnation metrics, hub-distance entropy, and _α_ -conditioned centrality measures. Upon detecting epistemic entrapment, the framework deliberately selects LLHs designed to contradict prevailing structural assumptions—for example, enforcing hub deconcentration or executing anti-centralization perturbations. 

This directed, hypothesis-disconfirming search process fundamentally differs from reward-driven hyperheuristics,<sup>[21]</sup> undirected diversification strategies,<sup>[36]</sup> and standard reinforcement learning baselines,<sup>[9]</sup> which lack explicit representations of the search’s epistemic state. Recent empirical evidence suggests that such assumptionviolative strategies can yield consistent improvements in solution quality, with reported median gains ranging between 15–25% across complex combinatorial benchmarks.<sup>[18]</sup> These findings motivate the formalization and evaluation of the LHH framework presented in this work. 

As illustrated in Fig. 1, recent work on the Hub Location Problem (HLP) spans foundational formulations, classical metaheuristics, and selection hyper-heuristics, with the latter often exhibiting reward-driven, exploitative behavior that can induce premature convergence under _α_ - driven centralization. The proposed LHH framework augments this landscape with explicit trap-detection indicators ( _e.g._ , stagnation and hub-distance entropy) and structured assumption-violating moves (such as hub deconcentration), thereby enabling epistemic escape and more robust exploration of the solution space. 

### **3. Problem formulation: the uncapacitated single allocation p-hub median problem** 

This investigation focuses on the Uncapacitated Single Allocation _p_ -Hub Median Problem (USApHMP), a canonical and computationally intractable variant of the broader Hub Location Problem (HLP) class. The USApHMP entails the strategic selection of exactly _p_ hub nodes from a set of _n_ candidate locations and the assignment of each of the remaining _n_ − _p_ non-hub nodes to a single, designated hub. The primary objective is the minimization of total system cost, an aggregate of fixed hub establishment costs and variable transportation costs incurred from routing all origin-destination flows through the hub-and-spoke network. The single-allocation constraint, which mandates that all inbound and outbound traffic for a non-hub node is consolidated through a single hub, is a prevalent operational paradigm in logistics and 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **3** 

**Research article                                                                                                                                                                                Engineered Science** 



**Fig. 1:** Overview of recent solution methodologies for the Hub Location Problem (HLP) and the positioning of the proposed Lateral Hyper-Heuristic (LHH) framework. 

telecommunication systems. However, this constraint significantly exacerbates the problem’s combinatorial complexity.<sup>[38,39]</sup> The formulation presented herein is consistent with recent benchmarking studies<sup>[40]</sup> and provides a rigorous testbed for our proposed lateral hyperheuristic framework, particularly due to its characteristically deceptive search landscape. 

### **3.1 Mathematical notation and model components** 

This subsection establishes the mathematical foundations required to formally describe the Uncapacitated Single Allocation _p_ -Hub Median Problem (USApHMP). It introduces the notation, parameters, and decision variables used throughout the model to ensure clarity, consistency, and reproducibility of the formulation. 

### **3.1.1 Sets and indices** 

This subsubsection defines the fundamental sets and indices that describe the network structure and the roles of its constituent nodes. These elements provide the indexing framework for flows, hubs, and allocation decisions. 

• _N_ = {1 _,_ 2 _, . . . , n_ }: The finite set of nodes in the network, representing both demand points and potential hub locations. 

• _i, j_ ∈ _N_ : Indices for origin and destination nodes, respectively. 

• _k, l_ ∈ _N_ : Indices for potential hub locations, which are themselves elements of _N_ . 

### **3.1.2 Parameters** 

This subsubsection introduces the parameters that characterize demand, transportation costs, economies of 

scale, and structural constraints of the problem. These parameters are assumed to be known and fixed prior to optimization. 

• _wij_ ≥ 0: The flow demand from origin node _i_ to destination node _j_ . It is assumed that _wii_ = 0, ∀ _i_ ∈ _N_ . 

• _cij_ ≥ 0: The per-unit transportation cost on the direct link connecting node _i_ to node _j_ in the underlying network. The cost matrix C is typically assumed to satisfy the triangle inequality. 

• _fk_ ≥ 0: The fixed cost associated with establishing and operating a hub at node _k_ . 

• _α_ ∈ (0 _,_ 1]: The discount factor applied to transportation costs on inter-hub links, quantifying the economies of scale achieved through flow consolidation. 

• _p_ : The cardinality constraint specifying the exact number of hubs to be established, where 1 ≤ _p < n_ . 

### **3.1.3 Decision variables** 

This subsubsection defines the binary decision variables that jointly determine the hub network topology and the allocation of demand nodes to hubs under the singleallocation policy. 



<!-- Start of picture text -->
The USApHMP is formulated using two sets of<br>binary decision variables that collectively define the<br>network topology as shown in Eq. (1):<br>if node 𝑘 is established as a hub,<br> ∀𝑘∈𝑁<br>𝑦𝑘 = {0 1 otherwise,<br> (1)<br>if node 𝑖 is allocated to hub 𝑘,<br> ∀𝑖, 𝑘∈𝑁<br>𝑧𝑖𝑘 = {0 1 otherwise,<br><!-- End of picture text -->

The variable _yk_ determines the set of hub locations, while _zik_ specifies the assignment of each node to exactly 

**4** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 

one hub. The formulation enforces that any node selected as a hub must be allocated to itself. 

### **3.2 Complete mathematical formulation** 

This subsection presents the complete binary integer programming formulation of the USApHMP, including the objective function and the set of constraints that govern hub selection and allocation feasibility. 

### **3.2.1 Objective function** 

The objective function captures the total system cost, which consists of fixed hub establishment costs and variable transportation costs incurred by routing all origin– destination flows through the selected hub network as shown in Eq. (2): 



<!-- Start of picture text -->
min 𝑍= ∑𝑘∈𝑁 𝑓𝑘 𝑦𝑘 + ∑𝑖∈𝑁 ∑𝑗∈𝑁 ∑𝑘∈𝑁 ∑𝑙∈𝑁<br>(2)<br>𝑤𝑖𝑗 (𝑐𝑖𝑘 + 𝛼𝑐𝑘𝑙 + 𝑐𝑙𝑗)𝑧𝑖𝑘𝑧𝑗𝑙<br><!-- End of picture text -->

For each origin–destination pair (i, j), the routing path is determined by the allocation variables. If node i is assigned to hub k and node j is assigned to hub l, the corresponding flow traverses the path i → k → l → j, incurring the associated transportation cost. 

### **3.2.2 Constraints** 

This subsubsection describes the constraints that enforce the structural and logical requirements of the USApHMP, including hub cardinality, single allocation, feasibility, and integrality as shown in Eq. (3): 



<!-- Start of picture text -->
= 𝑝, (Hub Cardinality)<br>∑𝑦𝑘<br>𝑘∈𝑁<br>= 1, ∀𝑖∈𝑁 (Single Allocation)<br>∑𝑧𝑖𝑘<br>𝑘∈𝑁 (3)<br>𝑧𝑖𝑘 ≤𝑦𝑘, ∀𝑖, 𝑘∈𝑁 (Allocation Feasibility)<br>𝑧𝑘𝑘 = 𝑦𝑘, ∀𝑘∈𝑁 (Hub Self-Allocation)<br>𝑦𝑘 ∈{0,1},∀𝑘∈𝑁<br>𝑧𝑖𝑘 ∈{0,1},∀𝑖, 𝑘∈𝑁<br><!-- End of picture text -->

Together, these constraints ensure that exactly _p_ hubs are selected, every node is assigned to one hub, and allocations are consistent with hub establishment decisions. 

### **3.2.3 Problem complexity and landscape features** 

This subsection analyzes the computational complexity of the USApHMP and highlights the structural properties of its fitness landscape that make it particularly challenging for conventional optimization algorithms. 

The USApHMP is a well-established NP-hard combinatorial optimization problem. The solution space grows combinatorially with the number of nodes, rendering exhaustive enumeration infeasible for realistic instance sizes. 

The difficulty of the problem is further exacerbated by the following landscape characteristics: 

1. High interdependence between hub selection and allocation decisions, resulting in a rugged landscape with numerous local optima. 

2. A deceptive centralization bias induced by the inter-hub discount factor _α_ , which favors overly centralized but 

suboptimal solutions. 

3. Strong epistatic interactions, whereby the fitness contribution of any decision depends non-linearly on the configuration of all other decisions. 

These properties severely limit the effectiveness of greedy, myopic, and reward-driven heuristic strategies, and they provide a strong motivation for the development of advanced search frameworks—such as the proposed lateral hyper-heuristic—capable of escaping epistemic traps in deceptive optimization landscapes. 

### **4. Epistemic traps in hub location search** 

The performance of metaheuristic and hyper-heuristic algorithms is intrinsically linked to the topological characteristics of the search landscape. For many complex optimization problems, this landscape is not merely rugged with numerous local optima; it contains regions we term epistemic traps. In this section, we formally define this concept, argue that the Uncapacitated Single Allocation p-Hub Median Problem (USApHMP) is particularly susceptible to such traps due to its inherent structural properties, and explain why traditional rational search paradigms are ill-equipped to escape them. 

### **4.1 Defining epistemic traps** 

An epistemic trap is a region of the search space that is not only a local optimum basin but also a conceptual basin where the dominant structural assumptions of the search process are self-reinforcing. Formally, let H be the set of low-level heuristics available to a search algorithm, and let S be the set of feasible solutions. A region R ⊆ S constitutes an epistemic trap if the following conditions hold: 

**1. Local optimality:** R contains one or more local optima with respect to the set of heuristics H. 

**2. Assumption reinforcement:** There exists a set of heuristics Hdominant ⊆ H that, when applied to any solution S ∈ R, produce a new solution S′ ∈ R that appears superior according to a myopic evaluation metric. 

**3. Structural homogeneity:** All solutions S ∈ R share a common structural property ϕ ( _e.g._ , hub centralization, specific allocation patterns) that is the target of the heuristics in Hdominant. 

**4. Escape difficulty:** Heuristics not in Hdominant, which might lead out of R, are systematically penalized by the selection mechanism because they initially degrade solution quality, violating the property _ϕ_ . 

Unlike a simple local optimum, an epistemic trap is 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **5** 

**<u>gineered Science</u>** 

characterized by a cognitive feedback loop between the algorithm’s heuristics and the structure of the solutions they generate. This feedback mechanism reinforces locally valid assumptions and suppresses exploration of structurally different configurations. The algorithm ”learns” that a particular structural assumption ( _e.g._ , centralization is always beneficial) is correct, because the heuristics that exploit this assumption are consistently rewarded. This myopic reinforcement blinds the search to alternative, potentially superior solution structures that lie outside the trap. 

### **4.2 The Centralization Bias as a trap-forming mechanism in the USApHMP** 

The mathematical structure of the USApHMP, specifically the discounted inter-hub transportation cost _αckl_ , is a powerful mechanism for inducing epistemic traps. When _α <_ 1, there is a clear economic incentive to minimize the distance between hubs, as this cost component is multiplied by the total flow between all node pairs allocated to those hubs. This creates a powerful centralization bias in the search landscape. 

Consider a typical local search heuristic for the USApHMP, such as a ”hub relocation” operator that moves a hub from its current location to a non-hub node. In a partially converged, centralized solution, moving a hub closer to the geographical center of mass of its allocated nodes will almost always reduce the total transportation cost. This is because the reduction in the _cik_ and _clj_ terms for its allocated nodes, and the potential reduction in the _αckl_ term with other nearby hubs, provides an immediate, measurable gain. This creates the conditions for an epistemic trap: 

• **Structural assumption (** _ϕ_ **):** ”The optimal hub configuration is geographically centralized.” 

• **Dominant heuristics (** H **dominant):** Local search operators that move hubs toward the center of their allocated clusters or swap peripheral hubs with more central non-hub nodes. • **Reinforcement loop:** A centralized solution is reached. The dominant heuristics find small improvements by further centralizing the hubs. A rational hyper-heuristic observes this consistent improvement and increases the selection probability of these centralizing heuristics. The search becomes increasingly focused on refining the central hub structure, ignoring the possibility that a more distributed configuration might yield a lower global optimum by better balancing fixed and transportation costs. 

The trap is ”epistemic” because the algorithm’s knowledge (its heuristic selection policy) becomes fundamentally flawed. It has learned a rule that is only locally valid within the trap. Escaping requires a heuristic 

that increases the inter-hub distance, which will be immediately punished by the selection mechanism due to the resulting spike in transportation costs, even if this move is a necessary first step toward a completely different and better basin of attraction. 

### **4.3 Implications for rational hyper-heuristics** 

The existence of epistemic traps poses a fundamental challenge to the dominant paradigm in hyper-heuristics, which is largely based on rational, utility-driven selection mechanisms.<sup>[41]</sup> Whether using simple reinforcement learning, choice functions, or bandit algorithms, these mechanisms share a common principle: heuristics that have demonstrated superior performance in the recent past should be selected more often in the future. 

When applied to a problem like the USApHMP, a rational hyper-heuristic will observe that the centralizing heuristics in Hdominant consistently yield improvements. Consequently, it will assign them high utility scores and select them with high probability. The hyper-heuristic itself becomes trapped by the same epistemic assumptions as the low-level heuristics it governs. It fails to recognize that the consistent performance of these heuristics is a symptom of being trapped, not a sign of progress toward the global optimum. 

This analysis reveals a critical limitation of myopic, reward-based learning in deceptive optimization landscapes. It suggests that a more sophisticated selection mechanism is required—one that can detect the symptoms of an epistemic trap ( _e.g._ , stagnation, heuristic dominance, structural homogeneity) and deliberately employ heuristics that contradict the prevailing search assumptions. This necessity for purposeful assumption violation is the primary motivation for the lateral hyper-heuristic framework introduced in the following section. 

### **5. Lateral hyper-heuristic framework** 

Having established the theoretical necessity of nonmyopic search mechanisms, we now present the Lateral Hyper-Heuristic (LHH) framework. The LHH framework operates in two distinct modes: Rational Mode and Lateral Mode. Rational Mode emphasizes reward-driven exploitation, whereas Lateral Mode is activated upon trap detection and introduces structured assumption violation to induce structural transitions. The framework integrates a rich set of low-level heuristics, a suite of context indicators for trap detection, and a novel collection of lateral selection operators that govern the search process. 

### **5.1 Solution representation** 

A solution S to the USApHMP is represented by two components: 

1. Hub Vector: A binary vector Y = (y1, y2, . . . , yn) of length n, where yk = 1 if node k is a hub and yk = 0 otherwise. This vector must always satisfy the constraint k 

**6** | _Eng. Sci._ , 2026, **41** 

**Engineered Science Publisher** 

**Engineered Science Research article** 

**<u>Table 1:</u>** <u>Categorization of low-level heuristics for the USApHMP.</u> 

|Category|Heuristic ID|Description|
|---|---|---|
|Intensification|ℎ1: HubShift|Moves a hub to the best non-hub node within its cluster.|
||ℎ2: NodeSwap|Swaps a hub with a non-hub node, accepting if cost improves.|
||ℎ3: TwoOpt|Swaps the locations of two hubs.|
||ℎ4: BestAllocation|Re-allocates all nodes to their single best hub (redundant but useful).|
|Diversification|ℎ5: RandomHubRelocation|Randomly selects a hub and moves it to a random non-hub location.|
||ℎ6: PerturbAllocation|Randomly re-assigns a subset of non-hub nodes to different hubs.|
||ℎ7: FarthestNode|Converts the non-hub node farthest from its hub into a new hub,|
|||and closes the original hub.|
||ℎ8: RandomSwap|Performs a random swap between a hub and a non-hub node.|
|Destructive|ℎ9: CloseAndReallocate|Closes one hub and re-allocates all its nodes to their second-best hub.|
||ℎ10: RemoveHub|Closes one hub and opens a new one at a random location.|
||ℎ11: ShuffleHubs|Randomly shuffles the locations of𝑘hubs (where𝑘< 𝑝).|
||ℎ12: Reset|Generates a completely new, random feasible solution.|



### ∈ N yk = p. 

2. Allocation Vector: An integer vector A = (a1, a2, . . . , an), where ai ∈ N denotes the index of the hub to which node i is allocated. The allocation is deterministically derived from the hub vector Y using a nearest-hub assignment rule: for each node i ∈ N , ai = arg mink ∈ N|yk =1 cik. This rule ensures that the allocation is always optimal with respect to a given hub configuration, simplifying the search space by focusing the heuristics solely on the hub locations. 

Thus, the search process operates directly on the binary hub vector Y, with the total cost of a solution calculated by evaluating the objective function (1) from Section 3 using the derived allocation vector A. 

### **5.2 Low-level heuristics** 

The framework’s problem-solving power stems from a diverse set of 12 low-level heuristics, H = { _h_ 1 _, h_ 2 _, . . . , h_ 12}, which operate on the hub vector _Y_ . These heuristics are categorized based on their intended effect on the search trajectory. 

Table 1 provides a summary of these heuristics. Intensification heuristics are designed for local search and exploitation of the current solution structure. Diversification heuristics introduce controlled randomness to explore new regions of the search space. Destructive heuristics are more disruptive, often breaking the current solution structure significantly to force an escape from deep local optima. 

• **Stagnation length (** _λ_ **):** A simple counter that tracks the number of consecutive iterations since the last improvement in the best-known solution quality. A high value of _λ_ suggests the search is stuck in a local optimum basin. 

• **Hub entropy (** **_EH_ ):** This indicator measures the structural diversity of the current hub configuration. It is calculated using the Shannon entropy formula based on the allocation of nodes to hubs as shown in Eq. (4): 



<!-- Start of picture text -->
𝐸𝐻 = −∑𝑘∈𝑁|𝑦𝑘=1 𝑝𝑘 log2(𝑝𝑘), where 𝑝𝑘 =<br>|{𝑖∈𝑁|𝑎𝑖=𝑘}| (4)<br>𝑛−𝑝 .<br><!-- End of picture text -->

where, _pk_ is the proportion of non-hub nodes allocated to hub _k_ . Low entropy indicates a highly centralized or unbalanced hub configuration (a few hubs serve most nodes), which is a key symptom of the centralization bias trap. 

• **Heuristic dominance (** _τ_ **):** This metric quantifies the inequality in the recent selection frequency of the heuristics. We use the Gini coefficient, applied to the selection counts of the heuristics over a sliding window of the last _W_ iterations as shown in Eq. (5): 



<!-- Start of picture text -->
𝜏= ∑𝑚𝑖=1 ∑2𝑚𝑚𝑗=1 2 |𝑠‾𝑠𝑖−𝑠𝑗|, (5)<br><!-- End of picture text -->

where _si_ is the selection count for heuristic _hi_ , _m_ = |H|, and _s_ ¯ is the mean selection count. A high value of _τ_ (close to 1) indicates that one or a few heuristics are dominating the selection process, a clear sign of assumption reinforcement. 

### **5.3 Search context indicators** 

To detect the presence of an epistemic trap, the LHH framework continuously monitors a set of context indicators that quantify the state of the search. These indicators serve as the ”sensory input” for the control logic. 

### **5.4 Lateral selection operators** 

When the control logic determines that the search has entered an epistemic trap, the framework switches from Rational Mode to Lateral Mode. In Lateral Mode, heuristic selection is no longer governed by reward but 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **7** 

**Research article                                                                                                                                                                                Engineered Science** 

by one of three specialized operators designed to induce a structural shift. 

• **Assumption violation operator (O** **_AV_ ):** This operator first identifies the dominant structural assumption. In the USApHMP, a low Hub Entropy ( _EH < θE_ ) signifies a centralization bias. O _AV_ then selects a heuristic that directly violates this assumption. Specifically, it prioritizes diversification heuristics like FarthestNode ( _h_ 7) or destructive heuristics like Close And Reallocate ( _h_ 9), which are likely to increase the inter-hub distances and thus counteract centralization. 

• **Role reversal operator (** O **_RR_ ):** This operator operates on the heuristic categories themselves. If intensification heuristics have been dominant (indicated by high _τ_ and low _λ_ ), O _RR_ temporarily inverts their utility. It will select a heuristic from the least-used category ( _e.g._ , Destructive) with a high probability. This forces the search to adopt a strategy that is the opposite of what has been recently successful, breaking the reinforcement loop. 

• **Conceptual jump operator (O** **_CJ_ ):** This is the most disruptive operator, designed for situations of severe stagnation (high _λ_ ). O _CJ_ disregards all heuristics except the most destructive ones, such as ShuffleHubs ( _h_ 11) or Reset ( _h_ 12). Its purpose is not to make a small, directed 

change but to perform a ”leap of faith” to a completely new, unexplored region of the search space, effectively resetting the search context. 

### **5.5 Framework architecture and control logic** 

The LHH framework can be viewed as a state machine with two primary states: Rational Mode and Lateral Mode. The control logic, detailed in Algorithm 1, orchestrates the transition between these states. 

The thresholds _θλ, θE, θτ_ are critical parameters that govern the sensitivity of the trap detection mechanism. The selection of the lateral operator can itself be a function of the indicator values; for example, a very high _λ_ might trigger O _CJ_ , while a moderate _λ_ combined with low _EH_ might trigger O _AV_ . This architecture allows the framework to seamlessly integrate rational exploitation with purposeful, context-aware exploration, providing a robust mechanism for navigating the deceptive search landscapes of the USApHMP. 

### **6. Algorithm description** 

This section presents the detailed pseudocode and operational logic of the Lateral Hyper-Heuristic (LHH) framework. Algorithm 2 formalizes the control mechanism that orchestrates the search process by dynamically switching between a Rational Mode, which exploits learned heuristics, and a Lateral Mode, which actively 

**<u>Algorithm 1:</u>** <u>Lateral hyper-heuristic control logic.</u> 

1: **Initialization:** Generate initial solution _S_ . Initialize heuristic utility scores _U_ ( _hi_ ) = 0 _,_ ∀ _hi_ ∈ H. Set iteration counter _t_ = 0. 2: **repeat** 3: Update context indicators: _λ, EH, τ_ . 4: **if** ( _λ > θλ_ ) ∨ ( _EH < θE_ ) ∨ ( _τ > θτ_ ) **then** {Epistemic trap detected} 5: **Enter Lateral Mode.** 6: Select lateral operator O _L_ ∈ {O _AV,_ O _RR,_ O _CJ_ } based on trap severity. 7: Select heuristic _hsel_ using the chosen operator O _L_ . 8: **else** 9: **Remain in Rational Mode.** 10: Select heuristic _hsel_ using a utility-based selection mechanism ( _e.g._ , roulette wheel on _U_ ( _hi_ )). 11: **end if** 12: Apply selected heuristic _hsel_ to current solution _S_ to generate _S_<sup>′</sup> . 13: **if** cost( _S_<sup>′</sup> ) _<_ cost( _S_ ) **then** 14: Accept _S_<sup>′</sup> . Update _U_ ( _hsel_ ) ← _U_ ( _hsel_ ) + ∆. 15: Reset stagnation counter _λ_ ← 0. 16: **else** 17: Reject _S_<sup>′</sup> . Update _U_ ( _hsel_ ) ← _U_ ( _hsel_ ) − ∆. 18: Increment stagnation counter _λ_ ← _λ_ + 1. 19: **end if** 20: _t_ ← _t_ + 1. 21: **until** termination condition is met <u>22:</u> **<u>return</u>** <u>Best solution found.</u> 

**8** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 

**<u>Algorithm 2:</u>** <u>Lateral hyper-heuristic (LHH) for the USApHMP.</u> **Require: Instance:** ( _N, wij, cij, fk, α, p_ ) **Heuristics:** H = { _h_ 1 _, . . . , hm_ } **Parameters:** _tmax, θλ, θE, θτ , W,_ ∆ _inc,_ ∆ _dec_ **Ensure: Best solution** 

**found:** _S_<sup>∗</sup> 

1: **Initialization:** 

- 2: Generate an initial feasible solution _S_ 0 ( _e.g._ , using a greedy construction heuristic). 

- 3: Set current solution _S_ ← _S_ 0 and best solution _S_<sup>∗</sup> ← _S_ 0. 

- 4: Initialize heuristic utility vector _U_ ( _hi_ ) ← 0 _,_ ∀ _hi_ ∈ H. 

- 5: Initialize selection history vector _Sh_ ( _hi_ ) ← 0 _,_ ∀ _hi_ ∈ H. 6: Set iteration counter _t_ ← 0 and stagnation counter _λ_ ← 0. 

- 7: **while** _t < tmax_ **do** 

8: **1. Context Monitoring:** Update context indicators ( _λ, EH, τ_ ). 9: _EH_ ← CalculateHubEntropy( _S_ ). 10: _τ_ ← CalculateGiniCoefficient( _Sh_ ). 11: **2. Mode Selection and Heuristic Choice:** 12: **if** ( _λ > θλ_ ) ∨ ( _EH < θE_ ) ∨ ( _τ > θτ_ ) **then** {Epistemic trap detected: enter Lateral Mode} 13: Select lateral operator O _L_ ∈ {O _AV ,_ O _RR,_ O _CJ_ }. 14: Select heuristic _hsel_ ← LateralSelection(O _L,_ H _,_ { _EH, τ_ }). 15: **else** {Search progressing normally: remain in Rational Mode} 16: Select heuristic _hsel_ ← RouletteWheelSelection(H _, U_ ). 17: **end if** 18: **3. Heuristic Application:** 19: Generate a new solution _S_<sup>′</sup> ← Apply( _S, hsel_ ). 20: **4. Solution Evaluation and Update:** 21: **if** cost( _S_<sup>′</sup> ) _<_ cost( _S_ ) **then** 22: Accept the new solution: _S_ ← _S_<sup>′</sup> . 23: Update utility: _U_ ( _hsel_ ) ← _U_ ( _hsel_ ) + ∆ _inc_ . 24: Reset stagnation counter: _λ_ ← 0. 25: **if** cost( _S_<sup>′</sup> ) _<_ cost( _S_<sup>∗</sup> ) **then** 26: Update best solution: _S_<sup>∗</sup> ← _S_<sup>′</sup> . 27: **end if** 28: **else** 29: Reject the new solution. 30: Update utility: _U_ ( _hsel_ ) ← _U_ ( _hsel_ ) − ∆ _dec_ . 31: Increment stagnation counter: _λ_ ← _λ_ + 1. 32: **end if** 33: **5. History Update:** 34: Update selection history: _Sh_ ( _hsel_ ) ← _Sh_ ( _hsel_ ) + 1. 35: Decay all utilities slightly to prevent saturation: _U_ ( _hi_ ) ← _U_ ( _hi_ ) × (1 − _ϵ_ ). 36: _t_ ← _t_ + 1. 

37: **end while** 

<u>38:</u> **<u>return</u>** _<u>S</u>_<sup>∗</sup> 

violates search assumptions to escape Hdominant. The algorithm serves as the concrete implementation of the conceptual framework introduced in Section 5. 

### **6.1 Algorithmic components explained** 

maximum cost reduction when established as hubs. The utility scores _U_ ( _hi_ ) for all heuristics are initialized to zero, ensuring no a priori bias. The selection history _Sh_ is used to calculate the Heuristic Dominance ( _τ_ ) indicator. 

### **6.1.1 Initialization** 

The algorithm begins by constructing a valid initial solution _S_ 0. A common approach is a greedy heuristic that iteratively selects the _p_ nodes that result in the 

### **6.1.2 Main loop and mode selection** 

The core of the LHH framework is the conditional logic that determines the search mode. At each iteration, the algorithm 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **9** 

**<u>gineered Science</u>** 

first evaluates the three context indicators: 

**• Stagnation (** **_λ_ ):** A simple counter tracking iterations without improvement. If _λ_ exceeds a threshold _θλ_ , it signals that the search is likely in a local optimum basin. 

**• Hub entropy (** **_EH_ ):** As defined in Section 5, a low value (below _θE_ ) indicates a centralized hub structure, a key symptom of the centralization bias trap. 

**• Heuristic dominance (** **_τ_ ):** A high Gini coefficient (above _θτ_ ) indicates that the selection process has become monopolized by a few heuristics, signifying assumption reinforcement. 

If any of these conditions are met, the algorithm infers the presence of an epistemic trap and switches to Lateral Mode. Otherwise, it continues in Rational Mode. 

### **6.1.3 Heuristic selection mechanisms** 

The heuristic selection process is fundamentally different in the two modes: 

**• Rational selection:** In this mode, we employ a standard roulette wheel selection mechanism. The probability of selecting heuristic hi is proportional to its utility score _U_ ( _hi_ ), ensuring that heuristics which have historically led to improvements are more likely to be chosen. 

**• Lateral selection:** When a trap is detected, the framework first selects a lateral operator ( _OAV_ , _ORR_ , or _OCJ_ ). This choice can be rule-based; for example, very high _λ_ might trigger _OCJ_ , while low _EH_ might trigger _OAV_ . The chosen operator then dictates the heuristic selection. For instance, _OAV_ would prioritize diversification heuristics like _h7_ (FarthestNode) that directly increase hub entropy. 

### **6.1.4 Solution evaluation and update** 

The algorithm employs a simple improvement-based acceptance criterion: a new solution _S_<sup>′</sup> is accepted only if it improves the cost of the current solution _S_ . Upon acceptance, the utility of the successful heuristic is increased (∆ _inc_ ), reinforcing its future use in Rational Mode. Upon rejection, its utility is decreased (∆ _dec_ ). This creates a direct feedback loop between heuristic performance and selection probability. A small decay factor _ϵ_ is applied to all utilities in each iteration to prevent scores from growing unbounded and to allow less-used heuristics a chance to be selected. 

### **6.2 Key parameters** 

The performance of the LHH framework is governed by several key parameters, which must be calibrated for the problem domain: 

• _tmax_ : Maximum number of iterations (termination condition). 

- _θλ, θE, θτ:_ Thresholds for stagnation, hub entropy, and 

- heuristic dominance, respectively. These control the sensitivity of the epistemic trap detection mechanism. 

• _W_ : The size of the sliding window used to calculate the Gini coefficient _τ_ . 

• ∆ _inc,_ ∆ _dec_ : The magnitude of the utility update for successful and unsuccessful heuristic applications. 

• _ϵ_ : The utility decay rate. 

A systematic parameter tuning process, such as the irace package or a factorial design, is essential to identify an effective configuration for these parameters. The robustness of the LHH framework to different parameter settings is a key aspect of our empirical evaluation in Section 8. 

The additional computational cost introduced by the lateral detection mechanisms is modest. The Hub Entropy calculation requires _O_ ( _n_ ) time per iteration, as it depends on the allocation counts of _p_ hubs. The Gini coefficient used for heuristic dominance is computed over a sliding window of size _W_ and requires _O_ ( _m_<sup>2</sup> ) time, where _m_ is the number of low-level heuristics ( _m_ = 12 in this study). Given that both _n_ and _m_ are small relative to the cost evaluation of candidate solutions, the overall overhead remains negligible. Empirically, the framework incurs approximately 5% additional CPU time compared to the baseline hyper-heuristic, a modest increase justified by the significant gains in solution quality and robustness. 

### **7. Computational experiments** 

This section details the experimental setup designed to evaluate the performance of the proposed Lateral HyperHeuristic (LHH) framework. The primary objective is to rigorously compare the LHH against the state-of-theart hyper-heuristic approach proposed by Danach _et al_ .<sup>[42]</sup> which serves as the direct baseline for this study. A comprehensive set of experiments is conducted on standard benchmark instances to assess solution quality, computational efficiency, and the robustness of the proposed framework in escaping epistemic traps. 

### **7.1 Benchmark instances** 

To ensure a fair and direct comparison, our experiments utilize the same benchmark datasets employed in the reference study.<sup>[42]</sup> These datasets are widely recognized as the de facto standard for evaluating hub location algorithms. The two primary datasets are: 

• CAB (Civil aeronautics board) dataset: This dataset consists of passenger flow data between 25 U.S. cities. We use the standard instances with n ∈ {10, 15, 20, 25} nodes and a varying number of hubs p ∈ {2, 3, 4, 5}, following the conventions of the literature. The transportation costs _cij_ are proportional to the distances, and the flows _wij_ are scaled accordingly. 

• AP (Australian post) dataset: This dataset is derived from the postal logistics network of Australia and is known for its larger size and more challenging structure. We use instances with n ∈ {20, 25, 40, 50, 100, 200} nodes and p ∈ {2, 3, 4, 5}. 

**10** | _Eng. Sci._ , 2026, **41** , 2212 

**Engineered Science Publisher** 

**Engineered Science Research article** 

For each combination of _n_ and _p_ , we use the specified discount factor _α_ and fixed cost structure from the original data files. This results in a total of 38 distinct problem instances, providing a robust testbed that varies significantly in size and complexity. 

### **7.2 Algorithm implementation and parameter settings** 

The LHH framework was implemented in C++ and compiled with GCC version 9.3.0 using the ‘- O3‘ optimization flag. All experiments were conducted on a workstation running Ubuntu 20.04 LTS, equipped with an Intel Core i9-10900K CPU (3.70 GHz) and 32 GB of RAM. To ensure a fair comparison, the baseline algorithms were also implemented in C++ under the same conditions. 

The performance of the LHH framework is sensitive to its control parameters. A preliminary tuning phase was conducted using the irace automatic configuration package<sup>[43]</sup> on a subset of the training instances. The final parameter configuration, which provided a robust performance across all instances, is detailed in Table 2. 

**Table 2:** Parameter settings for the Lateral Hyper-Heuristic framework. 

|Parameter<br>Value|
|---|
|Maximum iterations (_tmax_)<br>10,000|
|Stagnation threshold (_θλ_)<br>250|
|Hub Entropy threshold (_θE_)<br>1.5|
|Heuristic Dominance threshold (_θτ _)<br>0.6|
|Selection history window (_W_)<br>50|
|Utility increase (∆_inc_)<br>2.0|
|Utility decrease (∆_dec_)<br>1.0|
|Utilitydecayrate(_ϵ_)<br>0.001|



Parameter Calibration Procedure.  The parameter configuration reported in Table 2 was obtained using the irace automatic configuration framework. A representative subset of training instances from both the CAB and AP datasets (approximately 30% of the full benchmark set) was used during calibration to ensure generalization across problem sizes. The objective of the tuning process was the minimization of the average Percentage Deviation (PD) from the best-known lower bounds under a fixed time budget. Each candidate configuration was evaluated over multiple independent runs to account for stochastic variability. The final parameter set was selected based on its robust performance across heterogeneous instance sizes rather than peak performance on a specific subset. 

#### **7.3 Baseline algorithms for comparison** 

To position the LHH framework within the existing landscape, we compare its performance against three distinct categories of algorithms: 

1. State-of-the-Art Hyper-Heuristic (Danach _et al_ .<sup>[42]</sup> ): This is our primary baseline. As described in their paper, this method 

is a sophisticated hybrid that combines a Lagrangian relaxation (bundle) method to generate dual information with a hyper-heuristic that uses a reinforcement learning mechanism inspired by association rules to select from a portfolio of low-level heuristics. We have implemented this algorithm as closely as possible based on the descriptions provided in the reference paper. 

2. Standard Metaheuristics: To provide a broader context, we include two classic, well-tuned metaheuristics: 

• **Genetic algorithm (GA):** A standard GA with binary encoding for the hub vector, tournament selection, uniform crossover, and bit-flip mutation. The population size was set to 100, and the crossover and mutation rates were tuned to 0.8 and 0.02, respectively. 

• **Simulated annealing (SA):** An SA implementation with a geometric cooling schedule. The initial temperature was set to accept 95% of worsening moves, and the cooling rate was _αSA_ = 0.995. 

**3. Lower bounds:** For the CAB instances, we use the bestknown optimal solutions from the literature as a reference point. For the larger AP instances, where optimal solutions are unknown, we use the lower bounds reported by Danach _et al_ ,<sup>[42]</sup> which were obtained _via_ their Lagrangian relaxation method. This allows us to compute the percentage deviation from optimality (or the best-known bound). 

#### **7.4 Performance metrics** 

The performance of each algorithm is evaluated based on the following metrics: 

**• Solution quality:** The primary metric is the best objective function value ( _Zbest_ ) found over all runs. To normalize results across instances of different scales, we report the Percentage Deviation (PD) from the best-known solution or lower bound (ZLB) as shown in Eq. (6): 



<!-- Start of picture text -->
𝑃𝐷(%) =  𝑍𝑏𝑒𝑠𝑡 −𝑍𝐿𝐵 × 100. (6)<br>𝑍𝐿𝐵<br><!-- End of picture text -->

**• Computational efficiency:** The average CPU time (in seconds) required to find the best solution. This measures the speed of convergence. 

**• Robustness:** The standard deviation of the final solution quality across multiple independent runs. A lower standard deviation indicates a more stable and reliable algorithm. 

**• Escape capability:** To specifically evaluate the core contribution of our work, we introduce a novel metric. We measure the average number of stagnation breaks per run, defined as the number of times the algorithm improves the best-known solution after a period of at least _θλ_ consecutive non-improving iterations. This metric directly quantifies the algorithm’s ability to escape from epistemic traps. 

### **7.5 Experimental protocol** 

For each of the 38 benchmark instances, every algorithm (LHH, Danach _et al_ . HH, GA, SA) was executed 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **11** 

**Research article                                                                                                                                                                                Engineered Science** 

#### **Table 3:** <u>Average percentage deviation (PD) from best-known lower bounds across all instances.</u> 

|Algorithm|Avg. PD(%)|Std. Dev.|Best PD(%)|Worst PD(%)|
|---|---|---|---|---|
|Lateral Hyper-Heuristic (LHH)|0.21|0.15|0.00|0.58|
|Danach_et al_. HH|0.89|0.41|0.12|1.95|
|Genetic Algorithm (GA)|1.45|0.63|0.25|2.88|
|Simulated Annealing (SA)|1.72|0.71|0.31|3.21|



independently for 30 runs. This number of repetitions is sufficient to achieve statistical significance while keeping the total computational cost manageable. A different random seed was used for each run. The termination condition for all stochastic algorithms (LHH, GA, SA) was a time limit, set to 600 seconds for instances with _n_ ≤ 50 and 1800 seconds for larger instances ( _n_ > 50), consistent with the time limits reported in comparative studies. The results are aggregated and analyzed in the following section. 

### **8. Results and discussion** 

This section presents a comprehensive empirical analysis of the Lateral Hyper-Heuristic (LHH) framework. The results are structured to address three core questions: (1) Does the LHH framework achieve superior solution quality compared to state-of-the-art baselines? (2) Does it exhibit a higher capacity to escape from epistemic traps, as measured by our stagnation metrics? (3) Are the observed performance gains attributable to its structured assumption violation mechanism, rather than simply being a byproduct of increased randomness? The analysis that follows provides affirmative answers to all three questions. 

### **8.1 Overall solution quality comparison** 

We first evaluate the solution quality of the LHH framework against the primary baseline (Danach _et al_ . HH) and the standard metaheuristics (GA, SA). Table 3 summarizes the average Percentage Deviation (PD) from the best-known lower bounds across all 38 benchmark instances. The LHH framework demonstrates a clear and statistically significant advantage over all competing methods. 

The LHH framework achieves an average PD of just 0.21%, a reduction of over 76% compared to the Danach _et al_ . hyper-heuristic. Furthermore, its standard deviation is the lowest, indicating superior robustness and consistency across different problem instances. Notably, LHH found the optimal (or best-known) solution in 12 out of the 38 instances, a feat none of the other algorithms accomplished. 

This superiority is further illustrated in Fig. 2, which visualizes the distribution of PD values for each algorithm. The box plot shows that the LHH’s entire distribution is shifted towards lower deviation values, with a significantly lower median and a tighter interquartile range. This 

confirms that the LHH’s performance is not just a result of a few lucky runs but represents a consistent improvement in solution quality. 

### **8.2 Scalability analysis** 

To understand how the algorithms perform as problem complexity increases, we analyze the average PD as a function of the number of nodes, _n_ . Fig. 3 plots this relationship for the AP dataset. The results reveal that the performance gap between LHH and the baselines widens with problem size. While all algorithms perform reasonably well on smaller instances ( _n_ ≤ 25), the LHH framework maintains its low deviation rate as n grows, whereas the PD for the other algorithms, particularly the standard metaheuristics, increases sharply. This suggests that the structured search mechanism of LHH is more effective at managing the combinatorial explosion and deceptive landscapes of large-scale hub location problems. 

### **8.3 Escape capability and stagnation analysis** 

The central hypothesis of this paper is that the LHH framework is better at escaping epistemic traps. To validate this, we analyze the average number of stagnation breaks per run, as defined in Section 7. The results, presented in Table 4, provide strong evidence supporting our hypothesis. 

The LHH framework achieves an average of 4.8 stagnation breaks per run, more than double that of its nearest competitor. This indicates that the Lateral Mode is being triggered effectively and is succeeding in jolting the search out of local optima basins. Fig. 4 shows a representative convergence profile for a challenging AP100 instance. The plot clearly shows the Danach _et al_ . HH converging early and remaining flat, while the LHH framework exhibits several distinct jumps in the best-sofar solution quality, corresponding directly to successful escapes from stagnation. 

### **8.4 Heuristic usage pattern analysis: structured violation vs. randomness** 

To demonstrate that the performance gains of LHH stem from structured assumption violation rather than mere randomness, we analyze the heuristic usage patterns. Fig. 5 shows that the LHH framework spends approximately 78% of its time in Rational Mode and 22% in Lateral Mode. This indicates that the framework does not simply apply 

**12** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 



**Fig. 2:** Distribution of Percentage Deviation (PD) for all algorithms across all instances. The LHH framework shows a markedly lower median and a more compact distribution, indicating both higher quality and greater robustness. 



**Fig. 3:** Average Percentage Deviation (PD) versus problem size ( _n_ ) for the AP dataset. The performance gap between LHH and other algorithms widens as the number of nodes increases, demonstrating superior scalability. 



**Fig. 4:** Convergence profile for a representative AP-100 instance. The vertical drops in the LHH curve represent successful escapes from epistemic traps, which are absent in the baseline algorithm’s profile. 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **13** 

**Research article                                                                                                                                                                                Engineered Science** 

**Table 4:** <u>Average number of stagnation breaks per 600-second run.</u> 



<!-- Start of picture text -->
Algorithm Avg. Stagnation Breaks<br>Lateral Hyper-Heuristic (LHH) 4.8<br>Danach  et al . HH 1.9<br>Genetic Algorithm (GA) 1.2<br>Simulated Annealing (SA) 0.8<br><!-- End of picture text -->



**Fig. 5:** Proportion of search time spent in rational mode versus lateral mode for the LHH framework. 



**Fig. 6:** Comparison of heuristic category usage between LHH and the Danach _et al_ . HH baseline. LHH uses a more diverse set of heuristics, with a marked increase in diversification and destructive operators. 

random disruptive moves; rather, it uses them strategically when the context indicators signal a trap. 

A more detailed comparison of heuristic category usage is shown in Fig. 6. While the Danach _et al_ . HH predominantly relies on intensification heuristics, the LHH framework employs a much more balanced portfolio, with a significantly higher usage of diversification and destructive heuristics. This is a direct consequence of the 

Lateral Mode, which purposefully selects these disruptive operators to violate the centralization bias. 

The most compelling evidence is provided by the heuristic selection timeline in Fig. 7, which plots the selected heuristic and solution cost over a segment of a single run on an AP-50 instance. The figure shows a period of stagnation (flat cost curve) where intensification heuristics ( _h_ 1 _, h_ 2) are repeatedly selected. Once the 

**14** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 



**Fig. 7:** A detailed timeline of heuristic selection for a segment of an LHH run. The switch from intensification heuristics to a destructive heuristic ( _h_ 12) upon detecting stagnation leads to a successful escape and discovery of a superior solution. 

Heuristic Dominance ( _τ_ ) threshold is breached, the framework switches to Lateral Mode and selects the destructive Reset heuristic ( _h_ 12). This causes a sharp, temporary increase in cost (an ”uphill” move) but is immediately followed by a rapid descent to a new, significantly better basin of attraction. This behavior perfectly illustrates the core principle of purposeful assumption violation. 

• This success is not due to randomness but to a structured, context-aware mechanism that purposefully violates the search’s dominant assumptions when necessary. 

These findings confirm that embedding principles of lateral thinking into hyper-heuristics provides a powerful new paradigm for tackling deceptive optimization problems like the USApHMP. 

### **9. Conclusion and future work** 

### **8.5 Computational cost** 

The enhanced performance of the LHH framework comes with a modest computational overhead. On average, a 600second run of LHH requires approximately 5% more CPU time than the Danach _et al_ . HH due to the calculation of context indicators and the more complex selection logic. However, we argue that this is a negligible price to pay for the significant and consistent improvements in both solution quality and robustness, especially for large-scale, real-world instances where finding high-quality solutions is critical. 

The experimental results provide strong empirical validation for the Lateral Hyper-Heuristic framework. We have demonstrated that: 

• LHH achieves statistically significant improvements in solution quality over the current state-of-the-art hyperheuristic and classic metaheuristics. 

- Its performance advantage is particularly pronounced on larger, more complex problem instances. 

• The framework successfully escapes from epistemic traps more than twice as often as its competitors, as evidenced by both quantitative metrics and qualitative convergence profiles. 

This study introduced the Lateral Hyper-Heuristic (LHH) framework as a novel approach for solving the Uncapacitated Single Allocation p-Hub Median Problem (USApHMP). By embedding principles of lateral thinking, LHH deliberately violates dominant search assumptions when contextual indicators signal stagnation, allowing the algorithm to escape epistemic traps that often hinder conventional hyper-heuristics. 

Empirical results across 38 benchmark instances from the CAB and AP datasets demonstrate that LHH consistently outperforms the state-of-the-art hyper-heuristic and standard metaheuristics. It reduces the average deviation from known lower bounds by 76%, exhibits higher robustness, and breaks periods of stagnation more than twice as often as its closest competitor. Heuristic usage analysis confirms that these improvements result from a structured, context-aware selection mechanism rather than random perturbations. 

The success of LHH highlights the potential of structured assumption violation as a general mechanism for navigating deceptive optimization landscapes. Future research will explore extending LHH to other complex combinatorial problems, integrating adaptive learning of 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **15** 

**Research article                                                                                                                                                                                Engineered Science** 

lateral heuristics, and investigating hybrid strategies that combine structured violation with machine learning techniques to further enhance search performance and scalability. 

### **Conflict of Interest** 

The authors declare that they have no competing interests. 

### **Supporting Information** 

Not applicable. 

### **CRediT Statement** 

**Kassem Danach** , **Wael Hosny Fouad Aly** , **Chadi Fouad Riman** and **Samir Haddad:** Contributed equally to this work. All authors participated in the study conception and design. **Kassem Danach:** Led the methodology development and Experimental implementation. **Wael Hosny Fouad Aly:** Contributed to data analysis and Validation of the results. **Chadi Fouad Riman:** Contributed to theoretical analysis. **Samir Haddad:** Helped in the interpretation of the findings. All authors contributed to drafting and revising the manuscript and approved the final version. 

### **References** 

[1] R. Z. Farahani, M. Hekmatfar, A. B. Arabani, E. Nikbakhsh, Hub location problems: a review of models, classification, solution techniques, and applications, _Computers & Industrial Engineering_ , 2013, **64** , 1096-1109, doi: 10.1016/j.cie.2013.01.012. 

[2] J. F. Campbell, M. E. O’Kelly, Twenty-five years of hub location research, _Transportation Science_ , 2012, **46** , 153-169, doi: 10.1287/trsc.1120.0410. 

[3] S. A. Alumur, J. F. Campbell, I. Contreras, B. Y. Kara, V. Marianov, M. E. O’Kelly, Perspectives on modeling hub location problems, _European Journal of Operational Research_ , 2021, **291** , 1-17, doi: 10.1016/j.ejor.2020.09.039. 

[4] I. Contreras, J.-F. Cordeau, G. Laporte, Benders decomposition for large-scale uncapacitated hub location, _Operations Research_ , 2011, **59** , 1477-1490, doi: 10.1287/opre.1110.0965. [5] G. Taherkhani, S. A. Alumur, Profit maximizing hub location problems, _Omega_ , 2019, **86** , 1-15, doi: 10.1016/j.omega.2018.05.016. [6] J. H. Drake, A. Kheiri, E. Özcan, E. K. Burke, Recent advances in selection hyper-heuristics, _European Journal of Operational Research_ , 2020, **285** , 405-428, doi: 10.1016/j.ejor.2019.07.073. 

[7] E. K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Özcan, R. Qu, Hyper-heuristics: a survey of the state of the art, _Journal of the Operational Research Society_ , 2013, **64** , 16951724, doi: 10.1057/jors.2013.71. 

[8] N. R. Sabar, M. Ayob, G. Kendall, R. Qu, A dynamic multiarmed bandit-gene expression programming hyperheuristic for combinatorial optimization problems, _Institute of Electrical and Electronics Engineers Transactions on_ 

_Cybernetics_ , 2015, **45** , 217-228, doi: 10.1109/tcyb.2014.2323936. [9] J. H. Drake, A. Kheiri, E. Özcan, E. K. Burke, Recent advances in selection hyper-heuristics, _European Journal of Operational Research_ , 2020, **285** , 405-428, doi: 10.1016/j.ejor.2019.07.073. 

[10] E. D. Bono, _Lateral Thinking: Creativity Step by Step_ , Harper & Row, New York, 1970, ISBN - 13: 9780060903251. [11] S. Alumur, B. Y. Kara, Network hub location problems: The state of the art, _European Journal of Operational Research_ , 2008, **190** , 1-21, doi: 10.1016/j.ejor.2007.06.008. 

[12] S. Gelareh, S. Nickel, Hub location problems in transportation networks, _Transportation Research Part E_ : _Logistics and Transportation Review_ , 2011, **47** , 1092-1111, doi: 10.1016/j.tre.2011.04.009. 

[13] S. A. Alumur, J. F. Campbell, I. Contreras, B. Y. Kara, V. Marianov, M. E. O’Kelly, Perspectives on modeling hub location problems, _European Journal of Operational Research_ , 2021, **291** , 1-17, doi: 10.1016/j.ejor.2020.09.039. 

[14] J. F. Campbell, M. E. O’Kelly, Twenty-five years of hub location research, _Transportation Science_ , 2012, **46** , 153-169, doi: 10.1287/trsc.1120.0410. 

[15] J. Guan, G. Lin, H.-B. Feng, A multi-start iterated local search algorithm for the uncapacitated single allocation hub location problem, _Applied Soft Computing_ , 2018, **73** , 230-241, doi: 10.1016/j.asoc.2018.08.035. 

[16] H. Topcuoglu, F. Corut, M. Ermis, G. Yilmaz, Solving the uncapacitated hub location problem using genetic algorithms, _Computers & Operations Research_ , 2005, **32** , 967-984, doi: 10.1016/j.cor.2003.09.008. 

[17] G. Taherkhani, S. A. Alumur, Profit maximizing hub location problems, _Omega_ , 2019, **86** , 1-15, doi: 10.1016/j.omega.2018.05.016. 

[18] E. K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Özcan, R. Qu, Hyper-heuristics: a survey of the state of the art, _Journal of the Operational Research Society_ , 2013, **64** , 16951724, doi: 10.1057/jors.2013.71. 

[19] N. R. Sabar, M. Ayob, G. Kendall, R. Qu, A dynamic multiarmed bandit-gene expression programming hyperheuristic for combinatorial optimization problems, _Institute of Electrical and Electronics Engineers Transactions on Cybernetics_ , 2015, **45** , 217-228, doi: 10.1109/tcyb.2014.2323936. 

[20] E. Ozcan, A. Kheiri, A. J. Parkes, A survey of hyperheuristics for data-driven optimization, _Annals of Mathematics and Artificial Intelligence_ , 2022, **90** , 1–32, doi: 10.1007/s10472021-09742-4. 

[21] K. Danach, S. Gelareh, R. Neamatian Monemi, The capacitated single-allocation p-hub location routing problem: a Lagrangian relaxation and a hyper-heuristic approach, _Journal on Transportation and Logistics_ , 2019, **8** , 597-631, doi: 10.1007/s13676-019-00141-w. 

[22] A. Kheiri, E. Keedwell, A sequence-based selection hyperheuristic utilising a hidden Markov model, _Proceedings of the Annual Conference on Genetic and Evolutionary Computation_ , 

**16** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

**Engineered Science Research article** 

Madrid, Spain, 11–15 July, 2015, 417 - 424, doi: 10.1145/2739480.2754766. 

[23] Y. Bengio, A. Lodi, A. Prouvost, Machine learning for combinatorial optimization: a methodological tour d’horizon, _European Journal of Operational Research_ , 2021, **290** , 405-421, doi: 10.1016/j.ejor.2020.07.063. 

[24] A. A. Juan, J. Faulin, S. E. Grasman, M. Rabe, G. Figueira, A review of simheuristics: Extending metaheuristics to deal with stochastic combinatorial optimization problems, _Operations Research Perspectives_ , 2015, **2** , 62-72, doi: 10.1016/j.orp.2015.03.001. [25] K. Danach, W. H. F. Aly, S. Haddad, Mathematical modeling and genetic algorithm-based hyperheuristic optimization for quality of service and load balancing in cloud communication networks, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6487, doi: 10.29020/nybg.ejpam.v18i3.6487. [26] K. Danach, W. H. F. Aly, Adaptive hyperheuristic framework for hyperparameter tuning: a Q-learning-based heuristic selection approach with simulated annealing acceptance criteria, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6348, doi: 10.29020/nybg.ejpam.v18i3.6348. 

[27] K. Danach, H. Harb, W. H. Fouad Aly, H. Kanj, A. S. Kwekha Rashid, Bio-inspired optimization through photosynthesis: a novel approach for balancing exploration and exploitation in complex systems, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 5980, doi: 10.29020/nybg.ejpam.v18i2.5980. [28] K. Danach, W. H. F. Aly, A. Tarhini, S. Laouadi, Toward transparent optimization: a systematic review of explainable AI in decision-making systems, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6707, doi: 10.29020/nybg.ejpam.v18i4.6707. 

[29] W. H. F. Hosny Fouad Aly, H. Kanj, N. Mostafa, Z. AlArnaout, H. Harb, No binding machine learning architecture for SDN controllers, _Bulletin of Electrical Engineering and Informatics_ , 2025, **14** , 2413-2428, doi: 10.11591/eei.v14i3.8483. [30] W. H. F. Aly, H. Kanj, S. Alabed, N. Mostafa, K. Safi, Dynamic feedback versus Varna-based techniques for SDN controller placement problems, _Electronics_ , 2022, **11** , 2273, doi: 10.3390/electronics11142273. 

[31] W. H. Fouad Aly, A novel controller placement using Petrinets for SDNs, _World Scientific and Engineering Academy and Society Transactions on Mathematics_ , 2020, **19** , 598-605, doi: 10.37394/23206.2020.19.65. 

[32] M. A. B. Al-Tarawneh, H. Kanj, W. H. F. Aly, An integrated MCDM framework for trust-aware and fair task offloading in heterogeneous multi-provider Edge-Fog-Cloud systems, _Results in Engineering_ , 2025, **26** , 105228, doi: 10.1016/j.rineng.2025.105228. 

[33] K. Danach, W. H. F. Aly, H. Kanj, Machine learning for smart grid stability: enhancing reliability in renewable energy integration, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 5953, doi: 10.29020/nybg.ejpam.v18i2.5953. 

[34] F. A. Wael Hosny, N. Samashvili, C. Riman. Improving wheelchair mobility through en-hanced kalman filtering, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6495, doi: 10.29020/nybg.ejpam.v18i3.6495. 

[35] E.-G. Talbi, _Metaheuristics: From Design to Implementation_ , John Wiley & Sons, New Jersey, 2009, 1-624, ISBN - 978-0-470-27858-1. 

[36] H. H. Hoos, Automated algorithm configuration and parameter tuning, _Autonomous Search_ , Springer, Heidelberg, 2011, 37-71, doi: 10.1007/978-3-642-21434-9_3. 

[37] E. D. Bono, _Lateral Thinking: Creativity Step by Step_ , HarperCollins, 2022, 307, ISBN - 978-0060110079. 

[38] M. E. O’Kelly, A quadratic integer program for the location of interacting hub facilities, _European Journal of Operational Research_ , 1987, **32** , 393-404, doi: 10.1016/s03772217(87)80007-3. [39] J. F. Campbell, Hub location and the _p_ -hub Median problem, _Operations Research_ , 1996, **44** , 923-935, doi: 10.1287/opre.44.6.923. 

[40] R. Todosijević, D. Urošević, N. Mladenović, S. Hanafi, A general variable neighborhood search for solving the uncapacitated $$r$$-allocation $$p$$-hub Median problem, _Optimization Letters_ , 2017, **11** , 1109-1121, doi: 10.1007/s11590015-0867-6. 

[41] E. K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Özcan, R. Qu, Hyper-heuristics: a survey of the state of the art, _Journal of the Operational Research Society_ , 2013, **64** , 16951724, doi: 10.1057/jors.2013.71. 

[42] K. Danach, S. Gelareh, R. Neamatian Monemi, The capacitated single-allocation p-hub location routing problem: a Lagrangian relaxation and a hyper-heuristic approach, _Journal on Transportation and Logistics_ , 2019, **8** , 597-631, doi: 10.1007/s13676-019-00141-w. 

[43] M. López-Ibáñez, J. Dubois-Lacoste, L. Pérez Cáceres, M. Birattari, T. Stützle, The irace package: Iterated racing for automatic algorithm configuration, _Operations Research Perspectives_ , 2016, **3** , 43-58, doi: 10.1016/j.orp.2016.09.002. 

**Publisher’s Note:** Engineered Science Publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

### **Open Access** 

This article is licensed under a Creative Commons Attribution 4.0 International License, which permits the use, sharing, adaptation, distribution and reproduction in any medium or format, as long as appropriate credit to the original author(s) and the source is given by providing a link to the Creative Commons license and changes need to be indicated if there are any. The images or other third-party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** 2212 | **17** 

**Research article                                                                                                                                                                                Engineered Science** 

your intended use is not permitted by statutory regulation or exceeds the permi ctted use, you will need to obtain permission directly from the copyright holder. To view a copy 

of this license, visit http://creativecommons.org/ licenses/by/4.0/. 

©The Author(s) 2026. 

**18** | _Eng. Sci._ , 2026, **41** , 2212 **Engineered Science Publisher** 

