**_<mark>IET Intelligent Transport Systems</mark>_** 





**ORIGINAL RESEARCH** 

# **An Adaptive Hyper-Heuristic Framework for the Hub Location Problem in Intelligent Supply Chain Networks** 

Kassem Danach<sup>1</sup> Hassan Harb<sup>2</sup> Malak Ghandour<sup>1</sup> Hassan Kanj<sup>2</sup> 

> 1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon 2College of Engineering and Technology, American University of the Middle East, Kuwait 

**Correspondence:** Kassem Danach (kassem.danach@mu.edu.lb) 

**Received:** 20 November 2025 **Revised:** 6 May 2026 **Accepted:** 8 June 2026 

## **ABSTRACT** 

The hub location problem (HLP) is a central challenge in strategic supply chain design, requiring the optimal placement of hub facilities and the routing of goods to minimise overall transportation costs. Due to its combinatorial complexity and dynamic constraints, such as fluctuating demand, transportation costs and capacity limits, traditional solution techniques often fall short in providing scalable and adaptive performance. This paper proposes a novel reinforcement learning–based hyper-heuristic framework designed to address both capacitated and uncapacitated HLP variants under dynamic supply chain scenarios. The framework operates by intelligently selecting among a pool of low-level heuristics, guided by a high-level learning strategy that adapts based on feedback from the search space. Extensive experiments using benchmark datasets and simulated real-world data demonstrate that the proposed method outperforms traditional heuristics and metaheuristics in terms of solution quality, computational efficiency and adaptability. The results underscore the potential of hyper-heuristics as a generalisable and scalable approach for solving complex logistics optimisation problems in evolving operational environments. 

## **1 Introduction** 

The design and optimisation of supply chain networks has become increasingly critical in modern logistics, where global connectivity, digital transformation and just-in-time delivery paradigms demand both cost-efficiency and adaptability. Strategic decisions, such as the placement of hub facilities, can significantly impact transportation efficiency, service responsiveness and network robustness. These decisions are typically modelled through the hub location problem (HLP), a class of NP-hard combinatorial optimisation problems aimed at minimising total transportation and transshipment costs by optimally selecting hub nodes and routing flows. 

Variants of the HLP, including capacitated, uncapacitated, singleand multiple-allocation models, have been studied extensively. However, their complexity increases exponentially in the presence of real-world constraints such as fluctuating demands, 

stochastic travel times, facility disruptions and capacity limitations. These challenges render exact mathematical programming approaches impractical for large-scale and dynamic environments. Consequently, metaheuristic approaches, such as genetic algorithms (GA), simulated annealing (SA), ant colony optimisation (ACO) and particle swarm Optimisation (PSO), have gained popularity for solving HLPs in practice. These methods balance exploration and exploitation but often require significant parameter tuning and are typically problem-specific, limiting their generalisability across different scenarios [1]. 

To overcome these limitations, hyper-heuristics have emerged as a promising alternative. These high-level methodologies operate by adaptively selecting or generating low-level heuristics during the optimisation process, thereby enabling broader applicability with minimal manual tuning. Hyper-heuristics have been successfully applied to various combinatorial problems, including vehicle routing, medical logistics and job/machine scheduling 

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

> © 2026 The Author(s). _IET Intelligent Transport Systems_ published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology. 

1 of 14 

_IET Intelligent Transport Systems_ , 2026; 20:e70264 https://doi.org/10.1049/itr2.70264 

[2, 3]. In particular, reference [4] introduced a neuromorphicinspired hyper-heuristic framework based on spiking neural networks to solve the capacitated single-allocation p-hub location routing problem. The proposed NeuHH approach enables adaptive heuristic selection through spike-timing-based learning and demonstrated superior performance in cost reduction, load balancing, and scalability compared to classical metaheuristics and reinforcement learning (RL)-based hyper-heuristics. Further study in [5] proposed a selection-based hyper-heuristic (HH) decision-support framework for sustainable agricultural decision-making using real-world data from Lebanese farms. The framework dynamically selects heuristics through a reinforcement learning–inspired policy to optimise crop planning, irrigation scheduling and logistics operations, achieving significant performance improvements over traditional metaheuristics. 

Despite these promising results, the integration of HHs into hub location optimisation under dynamic conditions remains underexplored. Recent advances in machine learning, particularly RL, have opened new opportunities for learning-based optimisation strategies that adapt over time [6]. RL has shown significant success in various resource allocation and logistics domains by enabling systems to learn heuristic selection policies based on experience and environment feedback. Unlike deep RL approaches that attempt to directly construct solutions, the proposed method focuses on learning an adaptive heuristic selection policy within a HH framework. The novelty of the proposed approach lies in the integration of RL with a problemspecific HH designed for the capacitated HLP, including a tailored state representation that incorporates capacity utilisation and search progress indicators, a feasibility-aware reward mechanism and a dedicated set of low-level heuristics for hub opening, closing, allocation and load balancing decisions. 

This study addresses this gap by proposing a novel RL-based HH (RL-HH) framework for solving both capacitated and uncapacitated variants of the HLP in dynamic supply chain networks. The main contributions of this paper are as follows: 

- We develop an adaptive HH framework driven by reinforcement learning to dynamically select among a portfolio of low-level heuristics for the HLP. 

- We evaluate the framework on benchmark and synthetically generated datasets with dynamic constraints, comparing its performance against traditional metaheuristics and standalone heuristics. 

- We demonstrate the model’s scalability, generalisation and robustness under varying demand profiles and network sizes. 

Unlike existing RL-HHs proposed for general combinatorial optimisation problems, the proposed RL-HH framework is specifically designed for the capacitated HLP and incorporates several problem-aware components. First, the state representation is not limited to generic solution quality indicators but includes capacity utilisation levels, hub load distribution and allocation structure, allowing the learning agent to better capture the feasibility and structural properties of hub networks. Second, the heuristic portfolio is tailored to hub location decisions and includes operators dedicated to hub opening, hub closing, reallocation and load balancing under capacity constraints. Third, the 

reward mechanism is feasibility-aware and integrates both solution cost improvement and capacity violation penalties, guiding the learning process toward feasible and high-quality solutions. These elements differentiate the proposed RL-HH from existing RL-HHs that typically rely on generic state descriptors and operator selection strategies, and they enable the method to effectively handle capacity-constrained hub location optimisation problems. 

The remainder of this paper is organised as follows: Section 2 reviews related work. Section 3 presents the mathematical model of the HLP. Section 4 describes the proposed HH framework. Sections 5 and 6 reports experimental setup and results, followed by a discussion in Section 7. Section 8 presents the implications and future work of our framework. Finally, Section 9 concludes the paper and outlines future research directions. 

## **2 Literature Review** 

The HLP is a fundamental optimisation problem in the design of transportation, telecommunications and logistics networks. It involves identifying a set of hub nodes and allocating non-hub nodes (spokes), such that the total routing cost is minimised while satisfying capacity and flow constraints. HLP has since evolved into a rich area of research with numerous variants, including the p-hub median, p-hub centre, capacitated and uncapacitated and multiple versus single allocation models [7]. These models have found extensive applications in parcel delivery (e.g., FedEx), airline networks (e.g., hub-and-spoke configurations) and digital communication infrastructures [8]. 

Given the NP-hard nature of HLP, solving it optimally becomes intractable as problem dimensions increase. Exact methods based on mixed-integer linear programming or branch-and-bound remain suitable for small instances but fail to scale efficiently [9]. To address large-scale HLPs, researchers have turned to approximate methods such as heuristics and metaheuristics. Algorithms like GA, SA, ACO, Tabu Search (TS) and PSO have demonstrated success in various HLP configurations [10]. However, their effectiveness often depends on manual parameter tuning and problem-specific adaptations, limiting their transferability across dynamic or uncertain problem instances [11]. 

In light of these limitations, HHs have gained traction as a higherlevel search methodology that selects or generates low-level heuristics during the search process [12]. The primary motivation is to decouple problem-specific knowledge from the heuristic design process, thereby enabling generalisation across multiple problem domains. HHs have been successfully applied to job shop scheduling, bin packing, vehicle routing and timetabling problems, where adaptability and scalability are crucial [13]. 

Within the logistics and supply chain domain, several efforts have applied HHs to improve decision-making flexibility. For instance, reference [14] proposed a quantum-inspired HH framework to address dynamic multi-objective combinatorial optimisation problems in disaster logistics. The approach leverages quantum-inspired operators to enhance exploration and exploitation, enabling efficient adaptation to dynamic conditions while improving solution quality across multiple conflicting objectives. Another work in [15] investigated the integration of 

2 of 14 

_IET Intelligent Transport Systems_ , 2026 

metaheuristics and machine learning techniques for improving vehicle routing optimisation. The study compared an HH strategy with a variational autoencoder (VAE)-based approach, demonstrating the potential of learning-based methods to enhance solution quality and adaptability in complex routing scenarios. 

Recent advances in intelligent scheduling and optimisation have highlighted the growing importance of adaptive, learning-based and hybrid metaheuristic frameworks for solving large-scale combinatorial problems in industrial and supply chain environments. In [2], a knowledge-based two-population optimisation algorithm was proposed for distributed energy-efficient parallel machine scheduling, where heuristic initialisation, cooperative evolutionary operators and local search strategies were integrated to simultaneously optimise energy consumption and tardiness. The study demonstrates the effectiveness of combining domain knowledge with adaptive search mechanisms, which aligns with the objectives of adaptive HHs for hub location optimisation in intelligent supply chain networks. Similarly, the dual Q-learning scheduling approach introduced in [3] emphasised self-learning and adaptability under uncertain production environments by dynamically balancing local and global scheduling objectives. Such RL-driven adaptability is highly relevant to intelligent hub location systems where dynamic decision-making and responsiveness to changing logistics conditions are essential. Furthermore, the work in [16] leveraged heterogeneous graph neural networks and deep reinforcement learning to solve dynamic jobshop scheduling problems, demonstrating strong generalisation and scalability in complex industrial settings. The integration of graph-based learning and adaptive scheduling principles provides valuable insights for intelligent supply chain network design, particularly for modelling interconnected hub structures and dynamic transportation flows. In [17], logic-based Benders decomposition methods were developed for distributed flexible job shop scheduling, combining exact optimisation, constraint programming and heuristic search to efficiently solve decomposable large-scale scheduling problems. This hybrid decomposition philosophy is closely related to hub location optimisation, where decomposable network structures can benefit from adaptive hybrid optimisation frameworks. Moreover, the ensemble genetic programming approach proposed in [18] enhanced population diversity and search space exploration for dynamic flexible job shop scheduling through adaptive ensemble evolution strategies. Such diversity-driven adaptive search mechanisms further motivate the use of HH frameworks capable of selecting and evolving suitable heuristics for different supply chain scenarios. Finally, the deep learning-based Lagrangian dual approximation framework introduced in [19] demonstrated how neural architectures can efficiently approximate solutions for NP-hard scheduling problems while preserving feasibility constraints. This reflects the increasing trend toward integrating machine learning with combinatorial optimisation, which can significantly enhance the scalability and intelligence of adaptive hub location frameworks in modern supply chain networks. 

Some research has also demonstrated the growing synergy between HHs and machine learning. In [20], a deep-learningbased patch-wise strategy was introduced to guide HH decisions for medical image enhancement, emphasising the potential of learning-enabled selection mechanisms. Moreover, [21] and [22] highlight the feasibility of integrating RL into com- 

binatorial optimisation, allowing systems to learn policies over time for improved performance on dynamic problem distributions. 

Recently, HH approaches based on RL and deep learning have been increasingly applied to complex supply chain and logistics network design problems, including hub location, vehicle routing and green logistics optimisation. For instance, the authors of [23] proposed a RL HH with a cumulative reward mechanism for time-varying heterogeneous vehicle routing problems, where the learning agent selects heuristics based on long-term performance, resulting in improved solution stability and quality. Similarly, the authors of [24] developed a Q-learning-based HH for container storage optimisation in port terminals, demonstrating that adaptive heuristic selection can significantly improve space utilisation and operational efficiency. More recently, deep reinforcement learning has been integrated into HH frameworks for large-scale logistics and supply chain optimisation. In [25], the authors proposed an improved deep reinforcement learning algorithm for multi-cycle multi-objective green supply chain network design, showing that deep learning can effectively optimise complex network configuration and flow decisions under multiple conflicting objectives. In [26], the authors introduced a deep reinforcement learning-based HH for time-dependent green logistics with crowdsourcing, where the model learns heuristic selection strategies based on dynamic network conditions and environmental cost factors, achieving significant improvements compared to traditional metaheuristics. These studies confirm that learning-based HHs represent a promising direction for solving complex supply chain network design problems. However, most existing works focus on vehicle routing, green logistics or supply chain flow optimisation, while the application of RL-HHs specifically to the capacitated HLP remains relatively limited, which motivates the proposed research. 

In addition to HH approaches, several recent studies have proposed advanced metaheuristic, matheuristic and learningbased optimisation methods for complex logistics and facility location problems. The authors of [27] introduced a pheno-geno unified surrogate genetic programming approach for real-life container terminal truck scheduling, where surrogate models are used to approximate solution quality and guide the genetic programming process, significantly reducing computational time while maintaining high solution quality. In [28], the authors proposed a hybrid optimisation framework combining a genetic algorithm with large neighbourhood search for cargo aircraft capacity optimisation, demonstrating that hybrid metaheuristic approaches can effectively handle large-scale capacity planning problems with complex constraints. In [29], the authors developed a matheuristic fixed set search method for the two-stage capacitated facility location problem, integrating mathematical programming with metaheuristic search to improve solution quality and computational efficiency for large-scale facility location problems. The authors of [30] proposed a collaborative truck scheduling optimisation method based on graph theory and deep reinforcement learning (DDQN), showing that learningbased optimisation can improve decision-making in dynamic and complex logistics environments. These studies highlight the growing interest in hybrid, matheuristic and learning-based optimisation methods for logistics, scheduling and facility location problems. However, the application of RL-HHs specifically to the 

3 of 14 

_IET Intelligent Transport Systems_ , 2026 

**TABLE 1** Qualitative comparison between RL-HH and state-of-the-art techniques. 

|**Method**|**Learning** **type**|**Problem** **type**|**Complexity**|**Hub** **location**|
|---|---|---|---|---|
|[ 23 ]|RL hyper-heuristic|Vehicle routing|Medium|No|
|[ 24 ]|Q-learning HH|Container storage|Low|No|
|[ 26 ]|Deep RL HH|Green logistics|High|No|
|[ 25 ]|Deep RL|Supply chain network|Very High|No|
|[ 27 ]|Genetic programming HH|Scheduling|High|No|
|[ 29 ]|Matheuristic|Facility location|Medium|Partial|
|**Proposed** **RL-HH**|RL hyper-heuristic|Hub location|Low|Yes|



capacitated HLP remains limited, which further motivates the proposed research. 

Despite these advancements, the application of HHs to HLPs, particularly under real-world dynamic conditions such as demand variability, facility failures and cost uncertainty, remains sparse. Very few studies have tackled the integration of learning-based or adaptive HH systems within the HLP context, where decisions must be continuously re-optimised in response to evolving supply chain topologies. Notable exceptions such as [31] and [32] point to the untapped potential of adaptive strategies in operational logistics. 

This research aims to fill that gap by developing a RL-HH framework for solving both capacitated and uncapacitated HLPs. The proposed system dynamically selects from a portfolio of low-level heuristics based on real-time state feedback, enabling scalability, flexibility and responsiveness in complex supply chain design. More specifically, Table 1 presents a qualitative comparison between recent learning-based optimisation approaches and the proposed RL-HH method. It can be observed that most recent learning-based approaches focus on vehicle routing, scheduling and green logistics problems, while limited work has been conducted on RL-HHs for the capacitated HLP. In addition, deep RL and genetic programming approaches generally require higher computational resources and longer training time compared to tabular RL. The proposed RL-HH method provides a good balance between solution quality and computational efficiency while being specifically designed for the capacitated HLP. 

- ∙𝑁 = {1, 2, . . . , 𝑛} is the set of all nodes (clients or facilities), 

- ∙𝐸 is the set of undirected edges representing the paths between nodes. 

The model uses the following notation: 

- ∙𝑤𝑖𝑗: flow demand between node 𝑖 and node 𝑗, 

- ∙𝑐𝑖𝑗: unit transportation cost between node 𝑖 and node 𝑗, 

- ∙𝑓𝑘: fixed cost of establishing a hub at node 𝑘, 

- ∙𝐶𝑘: capacity of the hub at node 𝑘, 

- ∙𝑝: number of hubs to be established, 

- ∙𝛼: discount factor for inter-hub transportation costs (0 _<_ 𝛼 _<_ 1). 

## **3.2 Decision Variables** 

The following decision variable are defined in this study: 



<!-- Start of picture text -->
1 if node 𝑘 is selected as a hub,<br>∙𝑦𝑘 =<br>0 otherwise<br>{<br>1 if node 𝑖 is allocated to hub 𝑘,<br>∙𝑥𝑖𝑘 =<br>0 otherwise<br>{<br><!-- End of picture text -->

## **3.3 Objective Function** 

## **3 Problem Formulation** 

The HLP seeks to determine the optimal configuration of hub nodes within a network to minimise the total cost of transportation between origin–destination pairs. This study focuses on the capacitated single allocation p-hub median problem (CSApHMP), where each non-hub node is allocated to a single hub, and hubs are subject to capacity constraints. 



<!-- Start of picture text -->
The objective is to minimise the total cost consisting of allocation<br>and inter-hub transportation costs:<br>𝑛 𝑛 𝑛 𝑛 𝑛<br>min ∑ ∑ 𝑤𝑖𝑗 ∑ ∑ 𝑥𝑖𝑘𝑥𝑗𝑙(𝑐𝑖𝑘 + 𝛼⋅𝑐𝑘𝑙 + 𝑐𝑙𝑗) + ∑ 𝑓𝑘𝑦𝑘 (1)<br>𝑖=1 𝑗=1 𝑘=1 𝑙=1 𝑘=1<br><!-- End of picture text -->

## **3.4 Constraints** 

## **3.1 Network and Parameters** 

Let the transportation network be defined as a complete graph 𝐺 = (𝑁, 𝐸), where: 



<!-- Start of picture text -->
𝑛<br>∑ 𝑥𝑖𝑘 = 1 ∀𝑖 ∈𝑁 (each node assigned to one hub) (2)<br>𝑘=1<br>𝑥𝑖𝑘 ≤ 𝑦𝑘 ∀𝑖, 𝑘 ∈𝑁 (only assigned to open hubs) (3)<br><!-- End of picture text -->

4 of 14 

_IET Intelligent Transport Systems_ , 2026 



<!-- Start of picture text -->
𝑛 𝑛<br>∑ ∑ 𝑤𝑖𝑗𝑥𝑖𝑘 ≤ 𝐶𝑘𝑦𝑘 ∀𝑘 ∈𝑁 (capacity constraints) (4)<br>𝑖=1 𝑗=1<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑛<br>∑ 𝑦𝑘 = 𝑝 (exactly 𝑝 hubs) (5)<br>𝑘=1<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖𝑘, 𝑦𝑘 ∈{0, 1} ∀𝑖, 𝑘 ∈𝑁 (6)<br><!-- End of picture text -->

These constraints ensure the feasibility and operational integrity of the CSApHMP. Constraint (2) enforces that each non-hub node (client or facility) must be allocated to exactly one hub, reflecting a single allocation policy commonly adopted in supply chain networks for simplification and cost control. Constraint (3) ensures that a node can only be assigned to a hub if that hub has been selected for operation (i.e., is open), thereby linking allocation decisions to hub activation status. Constraint (4) imposes capacity restrictions on hubs by limiting the total flow demand allocated to each hub to not exceed its maximum capacity. This captures real-world operational limits such as warehouse storage or transportation throughput. Constraint (5) restricts the total number of hubs to be exactly 

## **3.5 Assumptions** 

- Flows are symmetric: 𝑤𝑖𝑗 = 𝑤𝑗𝑖 and 𝑐𝑖𝑗 = 𝑐𝑗𝑖. 

- Hubs act as transshipment points; all flows must pass through two hubs. 

- The inter-hub transport cost is discounted by a factor 𝛼 to reflect economies of scale. 

- All client nodes must be assigned to exactly one hub (single allocation). 

## **3.6 Problem Complexity** 

The CSApHMP is known to be NP-hard [33, 34], and the addition of capacity constraints increases the solution space exponentially. Therefore, exact methods become impractical for medium to large instances, motivating the need for intelligent approximate methods such as metaheuristics and HHs. 

## **4 Proposed Methodology** 

This section presents a novel HH framework designed to solve the CSApHMP in dynamic supply chain networks. The framework operates in two levels: a high-level strategy based on reinforcement learning and a pool of LLHs for solution construction and improvement. The proposed method aims to generalise across heterogeneous HLP instances while maintaining efficiency and solution quality. 

## **4.1 Overview of the Framework** 

The proposed HH framework is architected around a hierarchical structure that integrates reinforcement learning with heuristicdriven search. At the high level, an RL agent governs the selection of heuristics based on a state-reward formulation. This agent 

continuously interacts with the environment by observing the current state of the solution and selecting the most promising heuristic action, guided by a Q-value table that is updated through experience. It should be noted that the goal of the RL component in this work is not to replace the optimisation algorithm but to guide the selection of low-level heuristics. Therefore, the RL model acts as a heuristic selection policy rather than a solution generator, which makes tabular Q-learning an appropriate and efficient choice. 

At the lower level, the framework leverages a diverse pool of LLHs, which include both constructive and perturbative strategies. These LLHs are designed to manipulate the current solution in various ways, such as reallocating nodes, modifying hub assignments or swapping paths, thereby enabling effective exploration of the solution space. Their diversity ensures that the framework can balance intensification and diversification throughout the search process. 

To reinforce learning efficiency and support adaptive decisionmaking, the system also incorporates a solution memory component. This memory tracks the historical performance of each heuristic over multiple episodes, allowing the RL agent to associate heuristics with specific state patterns and to favour those that have yielded consistent improvements. This integration of learning, search diversity and performance memory equips the framework with the capacity to operate autonomously and efficiently across a range of HLP instances. 

## **4.2 LLHs** 

The proposed RL-HH framework utilises a diverse portfolio of LLHs, each designed to perform a specific type of transformation on the current solution (Algorithm 1). These heuristics enable the exploration and exploitation of the solution space by applying targeted constructive, perturbative and local search strategies. Their coordinated use, guided by the high-level RL agent, ensures that the framework remains effective across a wide range of HLP instances. 

**1. Greedy hub selection:** This heuristic initialises a solution by selecting a subset of nodes as hubs based on a greedy evaluation of flow distances and demand weights. The selection criterion minimises the total cost of connecting client nodes to potential hub locations while considering capacity feasibility. 

**2. Greedy allocation:** Once hubs are selected, this heuristic assigns each client to the nearest open hub that has sufficient capacity to accommodate its demand. The allocation process minimises assignment cost and serves as a constructive component for initial solutions or partial repairs. 

**3. Swap hubs:** To introduce structural diversity into the current configuration, this heuristic randomly selects a hub node to close and a non-hub node to open. The goal is to escape local optima by changing the core topology of the hub network, which in turn affects client-to-hub allocations. 

**4. Reassign clients:** This local perturbation heuristic evaluates the current assignment of each client and attempts to reallocate it 

5 of 14 

_IET Intelligent Transport Systems_ , 2026 

**ALGORITHM 1** Apply low level heuristic (Solution 𝑆, Heuristic ℎ). 

**Require:** Heuristic ℎ 

to a different hub that offers a lower cost or better load balancing, while preserving feasibility. It is particularly effective during the exploitation phase of the search. 

**Ensure:** Solution 𝑆 

- 1: **if** ℎ = GreedyHubSelection **then** 

- 2: Select top 𝑝 hubs that minimize weighted distances 

- 3: Initialize empty client-to-hub assignments 

- 4: **else** 

- 5: **if** ℎ = GreedyAllocation **then** 

- 6: **for** all clients 𝑖 **do** 

- 7: Assign 𝑖 to nearest open hub with available capacity 

- 8: **end for** 

- 9: **else** 

**5. Destroy and repair:** Inspired by the LNS paradigm, this heuristic removes a subset of client-to-hub assignments (destroy phase) and rebuilds them using a greedy reallocation process (repair phase). It enables significant structural changes while maintaining a degree of control. 

**6. Local search:** This heuristic applies a first-improvement descent algorithm over the allocation decisions. For each client, the method attempts small changes (e.g., reallocating to a different hub) and accepts the first improvement found. This ensures quick convergence to a local optimum and serves as a refinement step. 

- 10: **if** ℎ = SwapHubs **then** 

- 11: Randomly close one hub and open a non-hub node 

- 12: Reallocate affected clients 

- 13: **else** 

- 14: **if** ℎ = ReassignClients **then** 

- 15: **for** all clients 𝑖 **do** 

- 16: Evaluate cheaper feasible hub for 𝑖 

- 17: **if** cost improves **then** 

18: Reassign 𝑖 19: **end if** 20: **end for** 

The selected low-level heuristics are designed to represent different search behaviours required for solving the capacitated HLP. Some heuristics focus on diversification (exploration), such as random hub swap and reallocation heuristics, which help the algorithm explore new regions of the solution space. Other heuristics focus on intensification (exploitation), such as local reallocation and load balancing heuristics, which aim to improve the current solution by making small adjustments. 

By combining diversification and intensification heuristics within the HH framework, the algorithm can effectively balance exploration and exploitation during the search process, which is essential for solving large-scale combinatorial optimisation problems. 

21: **else** 

- 22: **if** ℎ = DestroyAndRepair **then** 

23: Remove 𝑘 random client assignments 24: Reassign them using GreedyAllocation 

**else** 

- 25: 

26: **if** ℎ = LocalSearch **then** 

27: **for** all clients 𝑖 **do** 

28: **for** all feasible hubs 𝑗 **do** 

29: **if** assignment to 𝑗 improves cost **then** 30: Reassign 𝑖 to 𝑗 and break 

31: **end if** 

32: **end for** 

33: **end for** 34: **end if** 35: **end if** 36: **end if** 37: **end if** 38: **end if** 

39: **end if** 

40: **return** Modified Solution 𝑆 

## **4.3 High-Level Strategy: Reinforcement Learning Agent** 

It is important to note that the reinforcement learning component in the proposed framework is used for heuristic selection rather than for direct solution construction. Therefore, the state and action spaces remain relatively small and discrete. In such cases, tabular Q-learning is particularly suitable due to its simplicity, fast convergence, low computational cost and stable learning behaviour. Unlike deep reinforcement learning methods, which require large training data and high computational resources, Q-learning can efficiently learn heuristic selection policies with limited training time. 

Moreover, several studies in HH optimisation have shown that tabular reinforcement learning is effective for selecting LLHs in combinatorial optimisation problems, where the objective is to learn a heuristic selection strategy rather than approximate a complex continuous function. Therefore, Q-learning provides a good balance between performance, computational efficiency and implementation complexity for the considered problem. 

The RL-based heuristic selector uses a Q-learning algorithm defined by: 

- **State:** Encodes current solution features such as cost, diversity and iteration index. 

6 of 14 

_IET Intelligent Transport Systems_ , 2026 

**TABLE 2** State features used by the reinforcement learning agent. 

|**Feature**|**Description**|
|---|---|
|Current solution cost|Total transportation cost of the current solution|
|Best solution cost|Best cost found so far|
|Cost improvement|Difference between current and previous solution cost|
|Iterations since last improvement|Number of iterations without improvement|
|Average hub utilisation|Average capacity utilisation across all hubs|
|Maximum hub utilisation|Maximum load-to-capacity ratio among hubs|
|Number of open hubs|Number of currently selected hub facilities|
|Feasibility indicator|0 = feasible solution, 1 = capacity violation|
|Search stage|Early, middle, or late stage of the search process|



- **Action:** Selecting an LLH from the pool. 

- **Reward:** Improvement in solution quality or convergence speed. 

The Q-value for each state-action pair is updated according to: 

**ALGORITHM 2** Reinforcement learning-based hyper-heuristic for CSApHMP. 1: Initialize 𝑄(𝑠, 𝑎) table and parameters 𝛼, 𝛾, 𝜖 

- 2: Initialize a random feasible solution 𝑆 

- 3: **while** termination criteria not met **do** 



<!-- Start of picture text -->
𝑄(𝑠𝑡, 𝑎𝑡) ← 𝑄(𝑠𝑡, 𝑎𝑡) + 𝛼 𝑟𝑡 + 𝛾max 𝑄(𝑠𝑡+1, 𝑎 ′ ) − 𝑄(𝑠𝑡, 𝑎𝑡) (7)<br>[ 𝑎 ′ ]<br><!-- End of picture text -->

- 4: Observe current state 𝑠 

- 5: Select heuristic 𝑎 using 𝜖-greedy policy 

where 𝛼 is the learning rate, 𝛾 is the discount factor, 𝑟𝑡 is the reward obtained at time 𝑡 and 𝑎𝑡 is the selected action. 

Moreover, the RL agent in our framework is invoked at each iteration of the optimisation process. At iteration 𝑡, the current solution is first analysed to extract the state features, including solution cost, capacity utilisation and search progress indicators. These features define the current state 𝑆𝑡 of the environment. Based on the current state 𝑆𝑡, the RL agent selects an action 𝐴𝑡, which corresponds to selecting one of the available lowlevel heuristics. The selected heuristic is then applied to the current solution to generate a new solution. After applying the heuristic, the reward 𝑅𝑡 is computed based on the improvement in the objective function and feasibility of the new solution. The Q-values are then updated using the Q-learning update rule, and the algorithm proceeds to the next iteration. Therefore, the role of the reinforcement learning agent is to dynamically select the most appropriate heuristic at each iteration in order to improve the solution quality and maintain feasibility under capacity constraints. 

## **4.4 State Representation** 

The performance of an RL-HH strongly depends on the definition of the state representation, which must capture both solution quality and search progress. In this work, the state is defined using a set of features that describe the current solution quality, hub capacity utilisation, and the improvement behaviour of the search process. These features allow the RL agent to decide which low-level heuristic should be applied depending on whether the search is improving, stagnating or approaching capacity limits. 

- 6: Apply heuristic 𝑎 to current solution 𝑆 →𝑆<sup>′</sup> 

- 7: Evaluate reward 𝑟 based on objective improvement 

- 8: Observe new state 𝑠<sup>′</sup> 



<!-- Start of picture text -->
9: Update Q-table:<br>𝑄(𝑠, 𝑎) ← 𝑄(𝑠, 𝑎) + 𝛼 𝑟 + 𝛾max 𝑄(𝑠 ′ , 𝑎 ′ ) − 𝑄(𝑠, 𝑎)<br>[ 𝑎 ′ ]<br><!-- End of picture text -->

- 10: Set 𝑆 ← 𝑆<sup>′</sup> , 𝑠 ← 𝑠<sup>′</sup> 

- 11: **end while** 

- 12: **return** Best solution found 

Table 2. The selected features capture solution quality, capacity utilisation and search progress indicators, allowing the learning agent to adapt heuristic selection based on the current search status. 

According to the table, the state vector at a given iteration, for instance, can be represented as follows: State = {CurrentCost = 12500, BestCost = 12300, Improvement = −200, IterNoImprovement = 5, AvgUtilization = 0.72, MaxUtilization = 0.91, OpenHubs = 4, Feasible = 1, SearchStage = Middle}. Based on this state, the reinforcement learning agent selects the most appropriate low-level heuristic to improve the solution while maintaining feasibility and reducing the total transportation cost. 

## **4.5 Pseudocode of the Framework** 

To improve transparency and reproducibility, the state representation used by the reinforcement learning agent is summarised in 

Algorithm 2 outlines the key steps of the proposed RL-HH framework designed to solve the CSApHMP. The framework 

7 of 14 

_IET Intelligent Transport Systems_ , 2026 

integrates a Q-learning mechanism to dynamically select the most effective low-level heuristic based on the current state of the search process. It begins with initialising a feasible solution and a Q-table, which stores the estimated utilities of applying certain heuristics in specific states. At each iteration, the current state of the solution is used to select a heuristic through an 𝜖-greedy policy that balances exploration and exploitation. The selected heuristic is applied to generate a new solution, which is evaluated to compute a reward signal based on objective improvement. The Q-table is then updated accordingly to reflect the learned experience. This iterative learning process continues until the termination criteria are met, at which point the best-found solution is returned. 

## **5.1 Datasets and Problem Instances** 

We conduct experiments on two types of datasets: 

1. **Benchmark instances:** The classic hub location benchmark instances from the OR-Library [35] are used. These include symmetric flow data for networks of 25, 50, 100 and 200 nodes, with distance matrices based on Euclidean or geographic coordinates. 

2. **Synthetic supply chain networks:** To simulate realistic variability, we generate synthetic networks with varying hub capacities, transportation cost distributions and demand patterns. These are useful to test the adaptability of the framework under fluctuating supply chain conditions. 

## **4.6 Advantages of the Proposed Framework** 

The proposed RL-HH framework exhibits several distinct advantages that enhance its suitability for solving complex HLPs. One of the foremost strengths is its adaptability; the framework dynamically adjusts its heuristic selection strategy based on realtime feedback from the problem instance. This ensures that the search behaviour remains responsive to changes in the solution landscape, such as variations in demand, capacity utilisation or node connectivity. 

Moreover, the RL-HH framework demonstrates strong generalisation capabilities. It can be effectively applied to both capacitated and uncapacitated variants of the HLP without requiring manual reconfiguration or extensive parameter tuning. This flexibility makes the model highly transferable across different supply chain contexts and operational scenarios. 

In terms of efficiency, reinforcement learning mechanisms embedded within the framework allow for intelligent exploitation of past performance. By leveraging Q-value updates, the system quickly identifies promising heuristic pathways, thereby accelerating convergence and reducing computational waste often associated with trial-and-error approaches. 

Finally, the framework is inherently scalable. Its modular architecture and learning-based decision logic enable it to manage increasingly large and complex network structures. This makes it a viable tool for solving real-world supply chain design problems that involve hundreds of nodes, variable constraints, and dynamic operational conditions. 

## **4.7 Implementation Details** 

The framework is implemented in Python for RL infrastructure. Experiments are conducted on benchmark datasets and synthetically generated supply chain networks, varying in size from 25 to 200 nodes. All results are averaged over 30 runs to ensure statistical significance. 

Each instance is tested for multiple values of 𝑝 (the number of hubs), typically in the range [3, 7], and with varying capacity tightness levels (sparse to highly constrained). 

## **5.2 Compared Methods** 

To validate the performance of our framework, we compare it against the following methods: 

- **Greedy baseline:** A deterministic heuristic that selects the lowest-cost hub and assigns clients based on shortest distances. 

- **GA:** A well-tuned GA implementation based on [36]. 

- **Simulated annealing (SA):** A classical metaheuristic tested under different cooling schedules. 

- **Standalone heuristics:** Each of the low-level heuristics from our framework applied individually (no learning). 

- **Proposed RL-HH:** The full framework introduced in Section 4. 

## **5.3 Performance Metrics** 

We evaluate all methods using the following criteria: 

- **Total cost:** The value of the objective function as defined in Equation (1). 

- **Computational time:** The average runtime required to reach convergence or stop conditions. 

- **Convergence behaviour:** Number of iterations required to reach the best-known solution. 

- **Robustness:** Standard deviation across multiple runs to assess stability. 

## **5.4 Parameter Settings** 

## **5 Experimental Setup** 

This section describes the datasets, experimental design, benchmark algorithms and performance evaluation metrics used to assess the effectiveness of the proposed RL-HH framework. 

In all experiments, the reinforcement learning agent operates under a consistent set of parameter configurations, unless otherwise specified. The learning rate (𝛼) is set to 0.1, allowing the agent to update its Q-values gradually while maintaining 

8 of 14 

_IET Intelligent Transport Systems_ , 2026 

**TABLE 3** Total cost comparison on benchmark instances. 

|**Instance**|**Greedy**|**GA**|**SA**|**Best** **LLH**|**[** **23** **]**|**[** **26** **]**|**RL-HH** **(proposed)**|
|---|---|---|---|---|---|---|---|
|25 Nodes|12,300|11,842|11,765|11,680|11,610|11,590|**11,524**|
|50 Nodes|28,710|27,428|27,142|26,900|26,780|26,710|**26,533**|
|100 Nodes|65,110|61,780|61,293|60,980|60,650|60,420|**60,124**|
|200 Nodes|136,221|131,740|130,865|130,144|129,880|129,420|**128,773**|



sensitivity to recent reward observations. The discount factor (𝛾), which governs the importance of future rewards, is fixed at 0.9 to ensure a balance between immediate and long-term gains during the optimisation process. To manage the exploration– exploitation trade-off, an 𝜖-greedy strategy is adopted, with the exploration factor (𝜖) initialised at 0.9 and linearly decaying to 0.1 over time. This setup encourages extensive exploration in the early stages of learning, followed by increased exploitation of known high-reward actions in later phases. 

**TABLE 4** Average runtime (seconds). 

||||**Best**|||**RL-HH**|
|---|---|---|---|---|---|---|
|**Instance**|**GA**|**SA**|**LLH**|**[** **23** **]**|**[** **26** **]**|**(proposed)**|
|25 Nodes|3.12|2.84|1.91|5.10|9.85|**4.35**|
|50 Nodes|6.87|5.91|4.60|9.42|18.73|**8.12**|
|100 Nodes|14.29|13.42|10.77|19.88|39.64|**16.98**|
|200 Nodes|29.78|27.54|22.64|41.35|81.27|**33.91**|



The maximum number of iterations per run is capped at 1000, and an early termination condition is enforced if no improvement is observed over 100 consecutive iterations. To ensure statistical robustness, each experimental configuration is independently repeated 30 times. The reported performance metrics represent the average results over these runs, accompanied by 95% confidence intervals to assess consistency and significance across trials. 

the search process and scale efficiently with problem size. The performance gap becomes more significant as the problem size increases, highlighting the advantage of adaptive heuristic selection in large and complex HLPs. 

## **6.2 Convergence Behaviour** 

## **5.5 Computational Environment** 

All experiments are conducted on a system with: 

Figure 1 illustrates the convergence curves for GA, SA and RLHH on a representative 100-node instance. The proposed method not only converges faster but also avoids premature convergence, maintaining exploration through adaptive heuristic selection. 

- Intel Core i7 processor (2.8 GHz), 32 GB RAM 

- Python 3.10, NumPy, SciPy, and OpenAI Gym 

- Runtime environment: Ubuntu 22.04 LTS 

## **6 Results and Analysis** 

This section presents the results of the experimental evaluation described in Section 5. The performance of the proposed RLHH is compared against traditional metaheuristics and baseline heuristics in terms of solution quality, computational efficiency, convergence behaviour and robustness. 

## **6.1 Total Cost Comparison** 

Table 3 summarises the average total cost achieved by each method across various benchmark instances. In addition to classical metaheuristics, we also include approximate performance values reported in recent learning-based optimisation studies such as [23] and [26] to provide a broader comparison with modern learning–based approaches. As shown in the table, the proposed RL-HH consistently outperforms all compared methods, particularly for medium and large-scale networks (100 and 200 nodes), demonstrating its ability to effectively guide 

## **6.3 Computational Time** 

Table 4 shows the average computation time (in seconds) for all compared methods, including recent learning-based optimisation approaches. In general, learning-based methods require additional computational time due to model training and policy updates. Deep reinforcement learning approaches, such as [26], typically require longer runtime due to neural network training, while RL-HHs such as [23] and the proposed RLHH require moderate additional time for learning the heuristic selection policy. Although the proposed RL-HH introduces additional overhead compared to classical metaheuristics, the increase in runtime remains reasonable and is justified by the significant improvements in solution quality. Furthermore, the proposed method remains computationally more efficient than deep learning–based approaches while achieving superior optimisation performance. 

## **6.4 Robustness and Stability** 

To assess robustness, each method was run 30 times per instance. The standard deviation of the objective values is shown in Table 5. The RL-HH framework exhibits the lowest variance, indicating stable behaviour and consistent solution quality across runs. 

9 of 14 

_IET Intelligent Transport Systems_ , 2026 



**FIGURE 1** Convergence curves on 100-node instance. 

**TABLE 5** Standard deviation of total cost across 30 runs. 

|**Instance**|**GA**|**SA**|**Best** **LLH**|**RL-HH** **(proposed)**|
|---|---|---|---|---|
|25 Nodes|98.1|104.5|86.3|**52.9**|
|50 Nodes|167.6|180.2|152.7|**93.5**|
|100 Nodes|270.8|292.1|245.5|**130.4**|
|200 Nodes|519.7|534.6|478.1|**242.3**|



## **6.5 Statistical Validation** 

To validate statistical significance, a paired _t_ -test was conducted comparing RL-HH and GA results. The _p_ values ( _<_ 0.01 in all cases) confirm that RL-HH significantly outperforms GA in terms of both total cost and variance reduction. 

## **6.6 Sensitivity Analysis of RL Parameters** 

The performance of the proposed RL-HH framework depends on several reinforcement learning parameters, including the learning rate (𝛼), discount factor (𝛾) and exploration decay rate (𝜖-decay). A sensitivity analysis was conducted to evaluate the impact of these parameters on the solution quality and convergence behaviour. The main RL parameter settings used in the experiments are summarised in Table 6. 

The experimental observations showed that the proposed method is relatively stable across a reasonable range of parameter values. The learning rate mainly affects the speed of convergence, where very small values slow down the learning process, while very large values may lead to unstable learning behaviour. The discount factor controls the importance of long-term rewards and was found to have a moderate impact on performance. The exploration decay parameter plays an important role in balancing exploration and exploitation; however, the results remained stable for decay values within a standard range. 

**TABLE 6** RL parameter settings used in the experiments. 

|**Parameter**|**Description**|**Value**|
|---|---|---|
|Learning rate ( 𝛼)|Learning step size|0.1|
|Discount factor ( 𝛾)|Importance of future rewards|0.9|
|Exploration rate ( 𝜖)|Initial exploration probability|1.0|
|Exploration decay|Exploration reduction rate|0.995|
|Minimum|Minimum 𝜖value|0.05|
|exploration rate|||
|Number of episodes|Training iterations|500|



**TABLE 7** Ablation study of proposed RL-HH components. 

|**Method** **variant**|**Average** **cost**|
|---|---|
|Without RL (random heuristic selection)|132,540|
|RL-HH without reward function|131,220|
|RL-HH without capacity features|130,870|
|RL-HH without load balancing heuristic|130,455|
|**Full** **RL-HH** **(proposed)**|**128,773**|



Overall, the RL-HH framework demonstrated robust performance across different parameter settings, and no significant degradation in solution quality was observed when parameters were varied within commonly used ranges in reinforcement learning. 

## **6.7 Component Analysis and Ablation Study** 

Table 7 presents the ablation study conducted to evaluate the effectiveness of each component of the proposed RL-HH framework. The results show that removing the RL component significantly degrades the solution quality, which confirms the 

10 of 14 

_IET Intelligent Transport Systems_ , 2026 

importance of adaptive heuristic selection. Similarly, removing the reward function or capacity-related state features also reduces performance, indicating that the feasibility-aware learning mechanism plays an important role in guiding the search process. The full RL-HH framework achieves the best performance, demonstrating that the combination of RL, problem-specific state representation and tailored heuristics contributes to the overall effectiveness of the proposed method. 

## **6.8 Discussion of Findings and Effectiveness** 

The results support the hypothesis that a learning-driven HH framework can enhance adaptability and solution quality for complex HLPs. RL-HH maintains a favourable trade-off between computational cost and accuracy while offering superior generalisation. The integration of feedback and memory allows the framework to balance exploration and exploitation more effectively than fixed-structure metaheuristics. This superior performance of RL-HH framework can be explained by several factors. First, the reinforcement learning component allows the algorithm to adaptively select low-level heuristics based on the current search state, rather than relying on a fixed heuristic selection strategy. This adaptive mechanism enables the algorithm to balance exploration and exploitation during the optimisation process. Second, the proposed state representation incorporates problem-specific information such as solution quality, hub capacity utilisation and search progress indicators. This allows the reinforcement learning agent to make more informed decisions when selecting heuristics, which improves the overall search efficiency. Third, the feasibility-aware reward mechanism helps guide the search toward feasible solutions while minimising the total transportation cost. This is particularly important in capacitated HLPs, where many candidate solutions may violate capacity constraints. Finally, the combination of diversification heuristics and intensification heuristics within the HH framework allows the algorithm to explore new regions of the solution space while also refining promising solutions. This combination contributes to the robustness and scalability of the proposed method, especially for large-scale problem instances. 

## **7 Discussion** 

The experimental findings reported in Section 6 substantiate the efficacy and robustness of the proposed RL-HH framework in addressing the complexities of capacitated HLPs under dynamic and uncertain conditions. This section contextualises those results within the broader optimisation literature, elaborates on the framework’s distinctive strengths, compares its behaviour against established techniques and discusses the implications for both academic research and industrial practice. 

## **7.1 Performance Analysis** 

The RL-HH framework consistently outperformed traditional metaheuristics such as GA, SA, and ACO across small, medium and large-scale problem instances. In particular, for network sizes of 100 and 200 nodes, the proposed approach demonstrated significantly better solution quality with respect to both the total cost and allocation efficiency. 

Unlike static metaheuristics, which require manual fine-tuning of control parameters and are typically problem-specific, the RLHH autonomously adapts its heuristic selection policy based on state-dependent feedback. This results in a more intelligent traversal of the search space, enhancing exploration in early stages and exploitation in later stages. The results align with previous observations by [21], confirming the strength of reinforcement learning in discovering adaptive policies for combinatorial optimisation problems. 

Furthermore, the RL-HH’s low variance in outcome quality, reflected by minimal standard deviations, illustrates the framework’s stability and repeatability. Such consistency is of paramount importance in logistics, where operational decisions are subject to real-time execution and frequent reevaluation. 

## **7.2 Adaptability and Generalisation** 

A key strength of the proposed RL-HH framework lies in its generalisation capability. Unlike conventional heuristics or even handcrafted HHs, which often require restructuring when applied to different problem variants, RL-HH demonstrates transferable performance across both capacitated and uncapacitated HLP models. It autonomously learns the relationship between problem states, such as node centrality, capacity utilisation and route load distribution, and effective heuristic decisions, without explicit reprogramming. 

This adaptability was further validated by experiments on synthetically generated datasets with stochastic demand patterns and partial topological disruption. The RL-HH framework adjusted dynamically to these perturbations, consistently converging to high-quality solutions despite the presence of demand shocks or fluctuating capacity constraints. This finding is especially relevant in real-world logistics, where uncertainty in demand and infrastructure availability is pervasive. 

## **7.3 Trade-Off Between Runtime and Accuracy** 

While the RL-HH approach incurs a moderate increase in computational effort due to the overhead introduced by Q-value updates and reward tracking, this trade-off is acceptable in the context of large-scale supply chain design. The runtime remained within acceptable operational thresholds, and more importantly, the algorithm achieved significantly faster convergence to nearoptimal solutions compared to baseline metaheuristics. 

The convergence curves revealed that RL-HH avoids stagnation in local optima, a common issue in SA and GA, by dynamically diversifying its heuristic choice based on cumulative reward trends. This strategic variation in search behaviour improves search intensification without compromising diversification, a core balance in HH theory [1, 12]. 

## **7.4 Scalability and Limitations** 

Although the RL-HH framework exhibits commendable performance, certain limitations warrant discussion. First, the current implementation employs a discrete set of predefined LLHs. The 

11 of 14 

_IET Intelligent Transport Systems_ , 2026 

expressive power of the system is therefore constrained by the diversity and quality of this heuristic pool. Future extensions could explore the incorporation of heuristic generation mechanisms using genetic programming or neural policy transfer, thereby enriching the LLH space. 

Second, the framework is built on classical tabular Q-learning, which limits its scalability to problems with compact state-action representations. For extremely large or continuous search spaces, deep Q-Networks (DQNs) or actor-critic models may be more appropriate, offering better generalisation and scalability [22, 31]. 

Third, while the model accounts for capacity and demand variability, it currently assumes deterministic cost parameters. Real-world logistics environments often entail uncertain or timedependent costs (e.g., traffic, weather, fuel price). Integrating stochastic cost models into the reward structure would enhance the framework’s applicability. 

## **7.5 Relevance to Real-World Applications** 

From a practical perspective, the RL-HH framework holds significant promise as a decision-support tool in modern logistics planning. Its self-adaptive architecture, combined with the ability to handle dynamic capacity and demand profiles, aligns with the operational realities of sectors such as courier services (e.g., DHL and UPS), emergency medical logistics and humanitarian aid distribution. In these domains, agility and resilience in network reconfiguration are essential. 

The framework’s autonomous learning capability is particularly valuable in environments where reoptimisation must occur frequently in response to disruptions or new information. For instance, in post-disaster scenarios or during pandemic response operations, logistics networks must rapidly reallocate resources under uncertain and evolving conditions. The RL-HH system could support such decision-making by continuously learning from previous iterations and environmental feedback. 

Moreover, its modular architecture allows easy integration with digital twin platforms, enabling real-time simulation and optimisation of logistics operations. As Industry 4.0 continues to drive the adoption of intelligent supply chain technologies, the integration of AI-driven optimisation tools like RL-HH into enterprise logistics platforms can yield substantial economic and operational benefits. 

## **8 Implications and Future Work** 

## **8.1 Practical Implications** 

The proposed reinforcement learning-based HH framework has significant implications for supply chain design and logistics operations. Unlike traditional methods that require extensive manual tuning and scenario-specific adaptation, the proposed approach provides a flexible and intelligent decision-support tool that can adapt to different network topologies, demand scenarios and operational constraints. 

For logistics companies and public service planners (e.g., health logistics, postal services and disaster relief organisations), the ability to dynamically reconfigure hub locations in response to fluctuating demand or transportation costs is crucial. The framework’s self-learning ability allows for real-time reoptimisation without the need for algorithmic redesign or retraining, making it a highly practical solution in volatile environments. 

Moreover, the low standard deviation observed across multiple runs supports its robustness and dependability—important attributes for strategic supply chain decisions that typically involve large financial investments and long-term commitments. 

## **8.2 Theoretical Implications** 

From a theoretical standpoint, this study contributes to the growing body of research that integrates machine learning into combinatorial optimisation, particularly through RL-HHs. This paper demonstrates how intelligent learning agents can improve both the efficiency and generalisability of search processes across diverse problem instances. 

The results reinforce the idea that heuristic selection need not rely on fixed rules or handcrafted priority mechanisms. Instead, learning-based approaches offer a scalable path toward generalised optimisation strategies applicable to multiple domains, from logistics and transportation to facility location and resource planning. 

## **8.3 Future Work** 

Several directions can further enhance the capabilities of the proposed framework: 

- **Integration with deep learning:** Replacing tabular Q- learning with deep reinforcement learning models can enable the handling of high-dimensional and continuous state spaces, improving scalability for large supply chain networks. 

- **Multi-objective optimisation:** Real-world HLPs often involve trade-offs between cost, time, environmental impact, and equity. Extending the framework to support multi-objective optimisation would increase its practical relevance. 

- **Hyper-heuristic generation:** In addition to selecting from a fixed set of low-level heuristics, the system can be extended to generate new heuristics on-the-fly using techniques such as genetic programming or meta-learning. 

- **Real-time and stochastic environments:** Incorporating real-time data streams and stochastic demand distributions will enhance the applicability of the model in highly dynamic operational settings. 

- **Hybrid matheuristics:** Future studies can explore combining the proposed HH with exact or decomposition-based mathematical models to develop matheuristic hybrids for better solution bounds. 

12 of 14 

_IET Intelligent Transport Systems_ , 2026 

Overall, this research lays the groundwork for next-generation adaptive optimisation frameworks in supply chain network design, contributing to both the theory and practice of intelligent logistics. 

administration. **Hassan Kanj:** methodology, investigation, writing – review and editing. All authors have read and agreed to the published version of the manuscript. 

### **Conflicts of Interest** 

The authors declare no conflicts of interest. 

## **9 Conclusion** 

### **Funding** 

This paper presented a novel RL-HH framework for solving the CSApHMP, a core challenge in supply chain network design. The proposed approach integrates a learning-driven high-level strategy with a diverse set of low-level heuristics to dynamically guide the search process in both static and dynamic environments. The main contributions of this work can be summarised as follows: 

- A RL-HH framework is proposed for solving the capacitated HLP. 

- A problem-specific state representation is designed by incorporating solution quality indicators, hub capacity utilisation and search progress features. 

- A tailored set of low-level heuristics is integrated into the HH framework to handle hub opening, hub closing, allocation and load balancing decisions. 

- A feasibility-aware reward mechanism is introduced to guide the learning process toward high-quality feasible solutions under capacity constraints. 

Extensive experiments on benchmark datasets and synthetically generated supply chain instances demonstrated that the RL-HH framework consistently outperforms traditional metaheuristics such as GAs and SA in terms of solution quality, convergence speed and robustness. The framework’s ability to adapt heuristic selection based on feedback from the search space enables it to generalise effectively across different problem instances without the need for manual reconfiguration or tuning. 

By building upon earlier HH research in logistics optimisation, this work advances the state of the art by integrating reinforcement learning into heuristic selection for large-scale HLPs. The resulting framework is not only theoretically sound but also practically viable for decision-makers in logistics, transportation and public service planning. 

Future research will explore enhancements such as deep reinforcement learning, multi-objective extensions, real-time decision-making and hybridisation with mathematical programming to further improve performance and applicability. Overall, this study contributes to the growing field of intelligent combinatorial optimisation and highlights the promise of HHs as a flexible, adaptive and scalable optimisation paradigm for complex supply chain problems. 

The authors have nothing to report. 

### **Data Availability Statement** 

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request. 

### **References** 

1. S. Vaezinejad, M. S. Pishvaee, and D. Schniederjans, “A Critical Review of Optimisation Models in Smart Supply Chains: Insights and Future Directions,” _International Journal of Production Research_ 64 (2026): 1–34. 

2. Z. Pan, D. Lei, and L. Wang, “A Knowledge-Based Two-Population Optimization Algorithm for Distributed Energy-Efficient Parallel Machines Scheduling,” _IEEE Transactions on Cybernetics_ 52, no. 6 (2020): 5051–5063. 

3. H. Wang, B. R. Sarker, J. Li, and J. Li, “Adaptive Scheduling for Assembly Job Shop With Uncertain Assembly Times Based on Dual Q- Learning,” _International Journal of Production Research_ 59, no. 19 (2021): 5867–5883. 

4. K. Danach, H. Harb, S. Amine, and M. Belhor, “NeuHH: A Neuromorphic-Inspired Hyper-Heuristic Framework for Solving the Capacitated Single-Allocation p-Hub Location Routing Problem,” _Vehicles_ 7, no. 2 (2025): 61. 

5. K. Danach, H. Harb, and H. Issa, “A Hyper-Heuristic Optimization and Communication Framework for Sustainable Agricultural DecisionMaking: A Case Study on Lebanese Farms,” _Journal of Agriculture and Food Research_ 24 (2025): 102522. 

6. F. Zhao, Z. Fu, L. Wang, and H. Sang, “A Heterogeneous Graph Reinforcement Learning Framework With Question-Aware Neighborhood Aggregation and Interoption Prompt Attention for Dynamic Flexible Job Shop Scheduling Problem,” _IEEE Transactions on Industrial Informatics_ 22, no. 4 (2026): 2863–2874. 

7. A. Sharma, S. K. Jakhar, I. Vlachos, and S. Kumar, “Advances in Hub Location Problems: A Literature Review and Research Agenda,” _International Journal of Productivity and Performance Management_ 74, no. 1 (2025): 24–55. 

8. F. Yang, W. Zhang, and W. Wei, “A Review of Hub Location Problems: Models, Solutions, and Applications,” _Transportation Research Part E: Logistics and Transportation Review_ 153 (2021): 102398. 

9. T. Aykin and B. Y. Kara, “Exact Methods for Hub Location Problems: A Survey,” _Computers & Operations Research_ 113 (2020): 104792. 

10. H. Hosseininasab and M. S. Jabalameli, “Hub Location Problems With Transportation Economies of Scale: A Review and Classification,” _Applied Mathematical Modelling_ 90 (2021): 872–894. 

11. W. Liu, M. Liu, and L. Gao, “A Survey on Hyper-Heuristics for Combinatorial Optimization Problems,” _Applied Soft Computing_ 80 (2019): 321–343. 

12. E.-G. Talbi, “A Taxonomy of Hybrid Metaheuristics,” _Journal of Heuristics_ 26 (2020): 1–30. 

### **Author Contributions** 

**Kassem Danach:** conceptualisation, software, formal analysis, data curation, writing – original draft preparation. **Hassan Harb:** conceptualisation, formal analysis, writing – original draft preparation, supervision. **Malak Ghandour:** validation, writing – review and editing, project 

13. B. Bilgin and E. Özcan, “Multi-Objective Hyper-Heuristics for Flexible Job Shop Scheduling,” _Expert Systems With Applications_ 188 (2022): 115963. 14. K. Danach, H. Harb, L. Saker, and A. Raad, “Quantum-Inspired Hyperheuristic Framework for Solving Dynamic Multi-Objective Combinatorial Problems in Disaster Logistics,” _World Electric Vehicle Journal_ 16, no. 6 (2025): 310. 

13 of 14 

_IET Intelligent Transport Systems_ , 2026 

15. K. Danach, L. Saker, and H. Harb, “Integrating Metaheuristics and Machine Learning for Enhanced Vehicle Routing: A Comparative Study of Hyperheuristic and VAE-Based Approaches,” _World Electric Vehicle Journal_ 16, no. 5 (2025): 258. 

16. C.-L. Liu, P.-H. Weng, and C.-J. Tseng, “Harnessing Heterogeneous Graph Neural Networks for Dynamic Job-Shop Scheduling Problem Solutions,” _Computers & Industrial Engineering_ 203 (2025): 111060. 

17. F. Xiong and H. Liu, “Logic-Based Benders Decomposition Methods for the Distributed Flexible Job Shop Scheduling Problem,” _European Journal of Operational Research_ 329, no. 3 (2026): 778–797. 

18. M. Xu, Y. Mei, F. Zhang, and M. Zhang, “Genetic Programming for Dynamic Flexible Job Shop Scheduling: Evolution With Single Individuals and Ensembles,” _IEEE Transactions on Evolutionary Computation_ 28, no. 6 (2023): 1761–1775. 

19. J. Kotary, F. Fioretto, and P. Van Hentenryck, “Fast Approximations for Job Shop Scheduling: A Lagrangian Dual Deep Learning Method,” in _Proceedings of the AAAI Conference on Artificial Intelligence_ 36, no. 7 (AAAI, 2022), 7239–7246. 

32. T. Vidal and G. Laporte, “Optimization Challenges in Last-Mile Delivery: A Survey,” _European Journal of Operational Research_ 285, no. 2 (2020): 1–25. 

33. J. F. Campbell, “A Survey of Network Hub Location,” _Studies in Locational Analysis_ 6 (1994): 31–49. 

34. J. Skorin-Kapov and D. Skorin-Kapov, “Multihub Transportation Network Design: A Polyhedral Approach,” _Management Science_ 45, no. 11 (1999): 1578–1593. 

35. J. E. Beasley, “OR-Library: A Collection of Test Data Sets for Operations Research Problems,” http://people.brunel.ac.uk/~mastjjb/ jeb/orlib/pmedinfo.html. 

36. A. Pourghader Chobar, M. Sabk Ara, S. Moradi Pirbalouti, M. Khadem, and S. Bahrami, “A Multi-Objective Location-Routing Problem Model for Multi-Device Relief Logistics Under Uncertainty Using Meta-Heuristic Algorithm,” _Journal of Applied Research on Industrial Engineering_ 9, no. 3 (2022): 354–373, https://doi.org/10.22105/jarie.2021. 299798.1365. 

20. Z. AlZamili, K. M. Danach, and M. Frikha, “Deep LearningBased Patch-Wise Illumination Estimation for Enhanced Multi-Exposure Fusion,” _IEEE Access_ 11 (2023): 120642–120653. 

21. Y. Bengio, A. Lodi, and A. Prouvost, “Machine Learning for Combinatorial Optimization: A Methodological Tour d’Horizon,” _European Journal of Operational Research_ 290, no. 2 (2021): 405–421. 

22. E. B. Khalil, H. Dai, Y. Zhang, B. Dilkina, and L. Song, “Learning Combinatorial Optimization Algorithms Over Graphs,” in _Advances in Neural Information Processing Systems_ 30 (Curran Associates, Inc., 2017). 

23. X. Wang, N. Li, and X. Jin, “A Reinforcement Learning HyperHeuristic With Cumulative Rewards for Dual-Peak Time-Varying Network Optimization in Heterogeneous Multi-Trip Vehicle Routing,” _Algorithms_ 18, no. 9 (2025): 536. 

24. L. Chen, J. Lin, and S. Xu, “A Study on Container Storage Optimization in Yards Based on a Hyper-Heuristic Algorithm With a q-Learning Mechanism,” _International Journal of Computational Intelligence Systems_ 18, no. 1 (2025): 163. 

25. Z. Wang, C. Ye, and J. Guo, “Optimization of Multi-Cycle MultiObjective Remanufacturing Green Supply Chain Network Based on Improved Deep Reinforcement Learning Algorithm Considering Differentiated Incentive Compatibility Mechanisms,” _Annals of Operations Research_ 359, no. 3 (2026): 2681–2708. 

26. C. Tang, Q. Wei, J. He, G. Perboli, H. Qin, and K. Li, “A Deep Reinforcement Learning-Based Hyper-Heuristic for Time-Dependent Green Logistics With Crowdsourcing,” _IEEE Transactions on Intelligent Transportation Systems_ 27, no. 4 (2026): 4766–4781. 

27. L. Tan, C. Jin, X. Chen, R. Qu, and R. Bai, “PGU-SGP: A Pheno-Geno Unified Surrogate Genetic Programming for Real-Life Container Terminal Truck Scheduling,” in _Proceedings of the Genetic and Evolutionary Computation Conference_ (ACM, 2025), 322–330. 

28. G. Durak and N. C. Demirel, “Cargo Aircraft Capacity Optimization: A Hybrid Approach Comprising a Genetic Algorithm and Large Neighborhood Search,” _Applied Sciences_ 15, no. 22 (2025): 11988. 

29. D. Alicic, N. Sezer, M. Maric, and R. Jovanovic, “Matheuristic Fixed Set Search Applied to the Two-Stage Capacitated Facility Location Problem,” _IEEE Access_ 13 (2025): 171093–171115. 

30. S. Cheng, Q. Liu, H. Jin, R. Zhang, L. Ma, and C. F. Kwong, “Collaborative Optimization of Truck Scheduling in Container Terminals Using Graph Theory and DDQN,” _Scientific Reports_ 15, no. 1 (2025): 6950. 

31. R. Zhang, F. Yang, Q. Ye, and J. Wu, “Learning to Optimize Combinatorial Problems Over Graphs Using Deep Reinforcement Learning,” _IEEE Transactions on Neural Networks and Learning Systems_ 32, no. 7 (2020): 3056–3067. 

14 of 14 

_IET Intelligent Transport Systems_ , 2026 

