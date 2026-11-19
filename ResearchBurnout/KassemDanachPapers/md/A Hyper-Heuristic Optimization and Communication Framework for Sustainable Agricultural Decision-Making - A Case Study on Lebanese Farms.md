Journal of Agriculture and Food Research 24 (2025) 102522 



Contents lists available at ScienceDirect 

Journal of Agriculture and Food Research 

journal homepage: www.sciencedirect.com/journal/journal-of-agriculture-and-food-research 



# A hyper-heuristic optimization and communication framework for sustainable agricultural decision-making: A case study on Lebanese farms 



## Kassem Danach<sup>a,∗</sup> , Hassan Harb<sup>b</sup> , Hamza Issa<sup>c</sup> 

a _Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon_ b _College of Engineering and Technology, American University of the Middle East, Kuwait_ c _Faculty of Engineering, Beirut Arab University, Beirut, Lebanon_ 

### A R T I C L E I N F O 

### A B S T R A C T 

_Keywords:_ Hyper-heuristic Agricultural optimization Irrigation scheduling Supply chain logistics Artificial intelligence Combinatorial optimization 

Agricultural systems in Lebanon face intertwined constraints, water scarcity, fragmented landholdings, firstmile logistics frictions, and climatic variability, that limit the effectiveness of single-technique optimizers. We propose a selection-based hyper-heuristic decision-support framework that learns to choose among diverse low-level heuristics via a multi-armed bandit policy (softmax exploration–exploitation) with a simulatedannealing-inspired move acceptance. Using a real-world dataset from 15 smallholder farms in the Beqaa Valley across three seasons (120 decision variables; 50 constraints), we jointly address crop planning, irrigation scheduling, and first-mile routing formulated as capacitated vehicle routing with time windows (CVRPTW). Empirically, the framework outperforms Genetic Algorithm, Simulated Annealing, and Tabu Search with 9.7–15.8% higher normalized objective values across problems, trading a modest 18.5% average runtime increase versus the fastest baseline (SA). The gains materialize through concrete mechanisms that directly affect decisions: (i) higher water-use efficiency by prioritizing parcels with the largest marginal yield response under scarcity; (ii) resilient crop mixes that balance water-intensive and drought-tolerant varieties across fragmented parcels; and (iii) clustered farm pickups that reduce first-mile distance and distribution cost. These outputs translate into actionable seasonal crop-mix plans, weekly irrigation calendars, and daily pickup routes. The learned policies exhibit interpretable patterns aligned with agronomic intuition, improving trust and adoption potential. While developed in Lebanon, the framework is directly transferable to smallholder, water-stressed contexts with heterogeneous parcels and volatile logistics, offering an adaptive, interpretable, and scalable pathway toward more sustainable resource allocation and yield-oriented decisions. 

#### **1. Introduction** 

Agriculture plays a pivotal role in Lebanon’s economy and food security, accounting for approximately 5% of the national GDP and employing around 20% of the labor force, particularly in rural areas [1]. Despite its socio-economic significance, the sector faces persistent and systemic challenges, including severe water scarcity, land fragmentation, inefficient resource allocation, and pronounced vulnerability to both climatic variability and geopolitical instability [2,3]. These structural inefficiencies are further compounded by Lebanon’s ongoing financial crisis and its repercussions on input affordability and rural supply chains [4]. 

Lebanese farmers are routinely required to make intricate and interdependent decisions across multiple domains-crop selection, irrigation planning, fertilizer application, labor deployment, and logistics coordination-often with limited access to data, predictive tools, 

or advisory services. These decision processes are subject to multidimensional constraints, including resource scarcity, market volatility, and agro-ecological heterogeneity. As such, the agricultural sector increasingly demands decision-support tools that can adapt to uncertain and dynamic environments. 

In this context, the integration of computational intelligence techniques has emerged as a transformative strategy to foster low-carbon, data-driven agricultural systems. Intelligent optimization frameworks are capable of processing heterogeneous agricultural data and generating adaptive decisions that improve productivity while preserving critical resources [5,6]. Recent studies have demonstrated that hybrid approaches combining artificial intelligence, optimization algorithms, and domain knowledge can effectively enhance precision agriculture practices. For instance, the AgriFusion framework integrates multisource environmental data to optimize crop and irrigation planning, 

- ∗ Corresponding author. 

_E-mail addresses:_ kassem.danach@mu.edu.lb (K. Danach), hassan.harb@aum.edu.kw (H. Harb), h.issa@bau.edu.lb (H. Issa). 

https://doi.org/10.1016/j.jafr.2025.102522 

Received 14 June 2025; Received in revised form 26 October 2025; Accepted 12 November 2025 

> Available online 13 November 2025 

2666-1543/© 2025 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/bync-nd/4.0/ ). 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

thereby promoting sustainable farming practices under resource constraints [7]. Other research has proposed bio-inspired optimization models and hyper-heuristic frameworks tailored to decentralized agricultural settings, with promising results in yield optimization, resource allocation, and logistics coordination [8,9]. 

These developments highlight a growing consensus in the literature: computational intelligence, when embedded in domain-specific optimization frameworks, offers a scalable, interpretable, and resourceefficient approach to addressing the complex operational challenges facing modern agriculture, particularly in the Global South and postcrisis economies like Lebanon. Unfortunately, within Lebanon, prior decision-support efforts have largely relied on Linear/ Mixed-Integer Programming for crop mix or water allocation and on single metaheuristics (e.g., GA/SA/TS) or rule-based advisories for isolated tasks. These approaches tend to assume deterministic parameters, require frequent manual retuning across farms and seasons, and do not coordinate decisions across crop-water-logistics layers; their performance deteriorates under fragmented parcels, uncertain water availability, and first-mile access frictions [10,11]. Our study addresses these shortcomings by evaluating a single, selection-based hyper-heuristic that generalizes across the three decision layers using real smallholder data, without problem-specific retuning. 

In recent decades, optimization techniques have been widely applied to agricultural decision-making to enhance resource efficiency, productivity, and sustainability. Methods such as Linear Programming, Mixed-Integer Programming, and classical metaheuristics (e.g., Genetic Algorithms, Simulated Annealing) have demonstrated potential in solving problems related to crop planning, irrigation scheduling, and supply chain logistics [12–14]. However, these techniques often require domain-specific customization, parameter tuning, and lack the flexibility to adapt to diverse and dynamic problem instances, limiting their applicability in real-world agricultural settings. 

Hyper-heuristics, introduced by Cowling et al. [15], represent an emerging class of optimization methodologies aimed at automating the heuristic design process. Unlike traditional metaheuristics that operate at the solution-space level, hyper-heuristics operate at a higher abstraction level by selecting or generating low-level heuristics to solve the problem [16]. This paradigm offers advantages in terms of generalizability, scalability, and reduced reliance on expert-driven customization, making it particularly attractive for domains characterized by heterogeneous, evolving, and uncertain problem spaces, such as agriculture. 

Recent studies have demonstrated the effectiveness of hyper-heuristics in solving combinatorial optimization problems in various fields, including scheduling [17], vehicle routing [18], and supply chain network design [19]. Nevertheless, their application in agricultural optimization remains limited, especially in the context of developing regions such as Lebanon. There is a research gap in leveraging hyper-heuristic approaches to address agricultural challenges under constraints of fragmented land, variable water availability, and unpredictable supply chain conditions prevalent in Lebanon [10,11]. To the best of our knowledge, no prior work applies selection-based hyper-heuristics to Lebanese agricultural systems; existing local studies employ LP/MIP or single metaheuristics for isolated sub-problems, with limited cross-layer coordination and portability. This study focuses explicitly on smallholder crop farming in Lebanon and targets three decision layers that dominate farm-level performance: (i) crop planning across fragmented parcels; (ii) irrigation scheduling under water scarcity; and (iii) first-mile farm-to-market logistics (pickup consolidation and routing on rural roads), which we later model as a capacitated VRP with optional time windows (CVRPTW). Livestock operations and downstream processing/distribution are outside the present scope. 

This research proposes the development of a hyper-heuristic optimization framework tailored to Lebanese agricultural systems, utilizing a real-world dataset encompassing crop yields, irrigation schedules, land use records, and distribution logistics collected from local farms. 

The framework dynamically selects among diverse low-level heuristics via a reinforcement-learning-driven policy (softmax multi-armed bandit with simulated-annealing–style acceptance) to optimize these three decision layers without problem-specific retuning, thereby increasing robustness to data heterogeneity and environmental variability. 

The novelty of this research lies in its contextualized application of hyper-heuristic optimization to an underexplored domain characterized by smallholder, resource-constrained, and highly variable agricultural systems. By integrating adaptive heuristic selection with real agricultural data, this study aspires to deliver interpretable, scalable, and practical solutions for improving resource efficiency, productivity, and resilience in Lebanese farming. Our contributions are threefold: (i) a unified, selection-based hyper-heuristic that coordinates crop planning, irrigation scheduling, and first-mile routing; (ii) an empirical evaluation on data from 15 Beqaa Valley farms across three seasons, demonstrating 9.7–15.8% gains over GA/SA/TS with interpretable operator usage; and (iii) actionable decision products (seasonal crop mixes, weekly irrigation-calendars, daily pickup routes) and policyoriented recommendations for stakeholders. The findings are expected to contribute both theoretically to the hyper-heuristics literature and practically to agricultural policy and farm-level decision-making. To guide the empirical analysis, we state the following hypotheses: **(H1)** a selection-based hyper-heuristic (HH) achieves higher objective values than single metaheuristics (GA, SA, TS) across crop planning, irrigation scheduling, and first-mile logistics; **(H2)** the learned selection policy converges toward a subset of consistently effective low-level heuristics; **(H3)** the HH yields interpretable patterns aligned with agronomic intuition (e.g., diversified crop mixes, prioritization of highmarginal-yield parcels, clustered pickups); and **(H4)** the HH generalizes across problem classes without manual retuning of problem-specific parameters. 

#### **2. Related work** 

Optimization techniques have long been employed in agricultural systems to improve decision-making regarding crop planning, irrigation scheduling, fertilization, pest management, and supply chain logistics. Early approaches relied predominantly on mathematical programming models, such as Linear Programming (LP) and Mixed-Integer Programming (MIP), which required strict problem formulation and were often limited by computational tractability in large-scale, real-world applications [20,21]. 

With the advancement of computational power, metaheuristic algorithms such as Genetic Algorithms (GA), Particle Swarm Optimization (PSO), and Simulated Annealing (SA) have gained popularity for solving complex agricultural optimization problems under uncertainty and non-linearity [22,23]. These methods have been successfully applied to irrigation scheduling [13], crop rotation optimization [12], and agricultural supply chain design [14]. However, metaheuristics are often problem-specific, requiring tailored configurations and significant tuning to perform effectively across different problem instances, leading to concerns about generalizability and scalability. 

To address these limitations, the field of hyper-heuristics emerged as an innovative paradigm that operates at a higher level of abstraction by selecting or generating heuristics rather than directly solving the problem instance [15]. The seminal work by Burke et al. [16] provided a comprehensive classification of hyper-heuristics into selection-based and generation-based approaches, with the former being more widely adopted due to their simplicity and adaptability. 

Hyper-heuristics have demonstrated promising results in diverse combinatorial optimization problems such as timetabling [24], vehicle routing [9,18], production scheduling [17], and logistics [8,25– 27]. Their ability to dynamically select heuristics based on performance feedback makes them suitable for solving complex, dynamic, and heterogeneous problems without extensive problem-specific customization. Recent developments have also extended hyper-heuristic 

2 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

frameworks with bio-inspired strategies, such as photosynthesis-based exploration–exploitation balancing mechanisms, further enhancing their adaptability in uncertain and high- dimensional environments [5]. 

Despite their growing application in industrial and operational contexts, hyper-heuristic methods remain underexplored in the agricultural optimization domain. Few studies have applied hyper-heuristics to crop planning or irrigation scheduling. For instance, Santos et al. [28] applied a hyper-heuristic approach to optimize agricultural irrigation networks under water resource constraints, achieving improvements in water use efficiency compared to standalone heuristics. Similarly, Chaves et al. [29] explored hyper-heuristic methods for optimizing multi-crop production schedules in greenhouse environments, highlighting their adaptability under uncertain environmental conditions. Although their effectiveness, these studies address single sub-problems in relatively controlled settings and do not couple irrigation or production decisions with parcel-level yield responses, fragmented land constraints, or first-mile logistics. They also do not learn a reinforcementlearning-based heuristic selection policy, nor do they evaluate crossproblem generalization on real smallholder datasets. 

In Lebanon specifically, published decision-support efforts have predominantly employed deterministic LP/MIP for crop-mix planning and seasonal water allocation, as well as single metaheuristics (e.g., GA/PSO /SA) or rule-based tools for isolated tasks such as irrigation scheduling or greenhouse planning. Reported gains are typically case-specific and hinge on careful parameter retuning; portability across farms, seasons, and data regimes is limited. Moreover, these approaches treat sub-problems in isolation, rarely account for parcel fragmentation and first-mile routing frictions, and often assume deterministic water availability—factors that degrade performance in heterogeneous smallholder settings [10,11]. 

However, no studies to date have investigated the use of hyperheuristics in agricultural systems within Lebanon or similar contexts characterized by fragmented land ownership, limited water availability, and highly variable climatic and economic conditions. The absence of localized hyper-heuristic applications represents a critical research gap, particularly given the need for flexible and scalable optimization methods tailored to smallholder, resource-constrained farming systems in developing regions [10,11]. This motivates an integrated approach that unifies multiple decision layers, learns a selection policy over diverse low-level heuristics, and explicitly targets smallholder contexts where water scarcity and logistics frictions are first-order constraints. 

Building upon these foundations, this research aims to bridge this gap by developing a hyper-heuristic optimization framework tailored to the specific challenges and data characteristics of Lebanese farms. The proposed framework leverages a real-world dataset comprising crop yields, irrigation schedules, resource allocations, and supply chain records, and explicitly targets three decision layers-crop planning, irrigation scheduling, and first-mile farm-to-market routing, while employing a reinforcement-learning-driven selection mechanism to promote generalization across problem classes and instances. 

#### **3. Problem formulation** 

Agricultural decision-making in Lebanese farms presents a multifaceted optimization landscape characterized by highly interdependent challenges, including crop selection, irrigation scheduling, resource allocation, and supply chain logistics. These tasks must be addressed under diverse constraints such as limited water availability, fragmented land parcels, labor shortages, fluctuating input costs, and transportation inefficiencies exacerbated by Lebanon’s socio-economic instability and climatic variability [2,4]. Traditional decision-making models often lack the flexibility and adaptability required to manage this complexity, particularly in smallholder and resource-constrained environments. 

To address these challenges, this research introduces a hyperheuristic optimization framework that systematically selects or generates low-level heuristics to solve a set of combinatorial optimization 

problems inherent to Lebanese agriculture. Hyper-heuristics offer a promising solution paradigm due to their abstraction from specific problem instances, their ability to generalize across problem types, and their capacity to autonomously balance exploration and exploitation based on dynamic feedback [5,16,27]. We explicitly target three key farm decision layers that the framework is designed to support-crop planning, irrigation scheduling, and first-mile farm-to-market routing. These layers correspond to the decision products used throughout the paper: seasonal crop-mix plans, weekly irrigation calendars, and daily pickup routes. 

In this study, we investigate three representative subproblems that collectively encapsulate the core decision-making bottlenecks in sustainable agricultural management: 

1. **Crop Planning Optimization:** Determining the optimal crop selection and spatial allocation across farm parcels to maximize expected yield or economic return while satisfying agronomic and resource constraints (e.g., water availability, land suitability, labor availability). This problem has been widely studied using linear programming and metaheuristic approaches [12,20], yet remains underexplored through adaptive hyper-heuristic frameworks that can handle heterogeneous and evolving farm conditions. 

2. **Irrigation Scheduling Optimization:** Optimally distributing limited water supplies across multiple plots and time periods to ensure crop water needs are met while minimizing total water consumption. Previous studies have addressed this using particle swarm optimization and mixed-integer programming [21,30], but these methods often require problem-specific tuning. Hyperheuristics can enhance generalization and robustness in such water-constrained scenarios [28]. 

3. **Supply Chain Logistics Optimization:** Developing efficient routing strategies for transporting agricultural outputs from farms to market centers, aiming to minimize total delivery costs, fuel consumption, and transit delays. The vehicle routing problem with time windows (VRPTW) and capacitated vehicle routing models have been studied in this context [9,18], yet scalable, context-aware solutions for fragmented rural infrastructure remain scarce. In this work, we model this layer explicitly as a first-mile, capacitated VRP with optional time windows (CVRPTW). 

Each of these subproblems can be formulated as a discrete, combinatorial optimization problem defined over a finite but exponentially large solution space. The combinatorial nature of these problems necessitates search-based solution techniques capable of navigating rugged and multidimensional landscapes. By leveraging hyper-heuristics with reinforcement learning-based heuristic selection, this research proposes a unified, adaptive approach to optimizing diverse and interdependent decisions in Lebanese agriculture [8]. For clarity, these three formulations are the ‘‘key operations’’ and the basis for our empirical evaluation. 

#### _3.1. General mathematical formulation_ 

Let: 

- _𝑋_ denote the space of feasible solutions. 

- _𝑓_ ∶ _𝑋_ → R be the objective function to minimize (e.g., total cost) or maximize (e.g., total yield). 

- • _𝐶_ = { _𝑐_ 1 _, 𝑐_ 2 _,_ … _, 𝑐𝑚_ } denote a set of constraints (e.g., water availability, land capacity, labor limits). 

The general optimization problem is: 

optimize _𝑓_ ( _𝑥_ ) (1) _𝑥_ ∈ _𝑋_ 

|s.t. _𝑐𝑗_(_𝑥_)≤_𝑏𝑗,_ ∀_𝑗_∈{1_,_…_, 𝑚_}_,_|(2)|
|---|---|



where _𝑏𝑗_ denotes the capacity/threshold for constraint _𝑗_ . 

3 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

#### _3.2. Crop planning model_ 

#### For crop planning, let: 

- _𝑖_ ∈ _𝐼_ : index of available crops. 

- _𝑘_ ∈ _𝐾_ : index of farm parcels. 

- _𝑦𝑖𝑘_ : binary decision variable (1 if crop _𝑖_ is planted in parcel _𝑘_ , 0 otherwise). 

- _𝑟𝑖_ : expected revenue (or yield value) per hectare for crop _𝑖_ . 

- _𝑎𝑖𝑘_ : area (hectares) allocated to crop _𝑖_ in parcel _𝑘_ . 

- _𝑤𝑖_ : water requirement per hectare for crop _𝑖_ . 

- _𝑊_ total: total available water across all parcels. 



<!-- Start of picture text -->
∑ 𝑥𝑖𝑗𝑣 = ∑ 𝑥𝑗𝑖𝑣 ∀ 𝑣 ∈  , ∀ 𝑖 ∈  (13)<br>𝑗 ∈ 𝑗 ∈<br>∑ 𝑥 0 𝑗𝑣 = ∑ 𝑥𝑖 0 𝑣 ≤ 1 ∀ 𝑣 ∈  (14)<br>𝑗 ∈ 𝑖 ∈<br>𝑁<br>∑ 𝑑𝑖 ∑ 𝑥𝑖𝑗𝑣 ≤ 𝑄𝑣 ∀ 𝑣 ∈  (15)<br>𝑖 =1 𝑗 ∈<br>𝑇𝑗 ≥ 𝑇𝑖 +  𝑠𝑖 +  𝑡𝑖𝑗 − 𝑀 (1 − ∑ 𝑥𝑖𝑗𝑣 ) ∀ 𝑖 ≠ 𝑗 (16)<br>𝑣 ∈<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑎𝑖 ≤ 𝑇𝑖 ≤ 𝑏𝑖 ∀ 𝑖 ∈  (if time windows apply) (17)<br><!-- End of picture text -->

- _𝐴𝑘_ : available arable area (hectares) of parcel _𝑘_ . 

#### Objective: 



<!-- Start of picture text -->
max ∑ ∑ 𝑟𝑖 𝑎𝑖𝑘 𝑦𝑖𝑘 (3)<br>𝑖 ∈ 𝐼 𝑘 ∈ 𝐾<br><!-- End of picture text -->

Subject to: 



<!-- Start of picture text -->
∑ ∑ 𝑤𝑖 𝑎𝑖𝑘 𝑦𝑖𝑘 ≤ 𝑊 total (global water budget) (4)<br>𝑖 ∈ 𝐼 𝑘 ∈ 𝐾<br>∑ 𝑎𝑖𝑘 𝑦𝑖𝑘 ≤ 𝐴𝑘 ∀ 𝑘 ∈ 𝐾 (parcel area capacity) (5)<br>𝑖 ∈ 𝐼<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ 𝑦𝑖𝑘 ≤ 1 ∀ 𝑘 ∈ 𝐾 (6)<br>𝑖 ∈ 𝐼<br>𝑦𝑖𝑘 ∈{0 ,  1} ∀ 𝑖 ∈ 𝐼, ∀ 𝑘 ∈ 𝐾 (7)<br><!-- End of picture text -->

#### _3.3. Irrigation scheduling model_ 

Let: 

- _𝑡_ ∈ _𝑇_ : index of time periods. 

- _𝑤𝑘𝑡_ : amount of water allocated to parcel _𝑘_ at time _𝑡_ . 

- _𝑊𝑡_ : available water at time _𝑡_ . 

- _𝑦𝑙𝑑𝑘𝑡_ ( _𝑤𝑘𝑡_ ): yield (or yield-contribution) function for parcel _𝑘_ at time _𝑡_ . 

Objective: 



<!-- Start of picture text -->
max ∑ ∑ 𝑦𝑙𝑑𝑘𝑡 ( 𝑤𝑘𝑡 ) (8)<br>𝑘 ∈ 𝐾 𝑡 ∈ 𝑇<br><!-- End of picture text -->

Subject to: 



<!-- Start of picture text -->
∑ 𝑤𝑘𝑡 ≤ 𝑊𝑡 ∀ 𝑡 ∈ 𝑇 (9)<br>𝑘 ∈ 𝐾<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑤𝑘𝑡 ≥ 0 ∀ 𝑘 ∈ 𝐾, ∀ 𝑡 ∈ 𝑇 (10)<br><!-- End of picture text -->

#### _3.4. Supply chain logistics model_ 

We specify first-mile farm-to-market routing as a capacitated VRP with optional time windows (CVRPTW). Let  = {0 _,_ 1 _,_ … _, 𝑁_ } be nodes, with 0 the depot (collection center) and 1 _..𝑁_ farm pickup locations; let  be vehicles. Parameters: _𝑑𝑖_ demand at farm _𝑖_ ; _𝑄𝑣_ capacity of vehicle _𝑣_ ; _𝑐𝑖𝑗_ travel cost; _𝑡𝑖𝑗_ travel time; [ _𝑎𝑖, 𝑏𝑖_ ] time window at node _𝑖_ (optional); _𝑠𝑖_ service time at node _𝑖_ . Decision variables: _𝑥𝑖𝑗𝑣_ ∈{0 _,_ 1} equals 1 if vehicle _𝑣_ traverses arc ( _𝑖, 𝑗_ ); _𝑇𝑖_ ≥ 0 arrival time at _𝑖_ . Objective: 



<!-- Start of picture text -->
min ∑ ∑ ∑ 𝑐𝑖𝑗 𝑥𝑖𝑗𝑣 (11)<br>𝑣 ∈ 𝑖 ∈ 𝑗 ∈<br><!-- End of picture text -->

Subject to: 



<!-- Start of picture text -->
∑ ∑ 𝑥𝑖𝑗𝑣 = 1 ∀ 𝑖 ∈{1 ,  …  , 𝑁 } (12)<br>𝑣 ∈ 𝑗 ∈<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖𝑗𝑣 ∈{0 ,  1} , 𝑇𝑖 ≥ 0 ∀ 𝑖, 𝑗 ∈  , ∀ 𝑣 ∈  (18)<br><!-- End of picture text -->

Subtour elimination can be addressed via MTZ constraints or lazy constraints in the solver. 

#### _3.5. Hyper-heuristic framework_ 

Instead of solving each problem instance with a single metaheuristic, this study proposes a hyper-heuristic framework _𝐻_ that dynamically selects a heuristic _ℎ_ ∈  (from a pool of low-level heuristics) at each iteration based on a selection strategy _𝜎_ and a move acceptance criterion _𝛼_ : 



<!-- Start of picture text -->
𝐻 ( 𝑥,   , 𝜎, 𝛼 ) → 𝑥 ′ (19)<br><!-- End of picture text -->

where _𝑥_ is the current solution, _𝑥_<sup>′</sup> is the new solution, and _𝜎_ and _𝛼_ guide heuristic selection and acceptance. This formalization allows us to plug the three subproblems into a unified selection-and-acceptance loop while preserving problem-specific feasibility through constraint-aware low-level operators. 

#### **4. Proposed solution approach** 

The proposed solution is a selection-based hyper-heuristic optimization framework designed to solve agricultural decision-making problems in Lebanese farms. The framework operates at a high level by selecting suitable low-level heuristics (LLHs) from a pre-defined set, guided by a heuristic selection mechanism, a move acceptance criterion, and a termination condition. 

#### _4.1. Low-level heuristics_ 

The pool of low-level heuristics  = { _ℎ_ 1 _, ℎ_ 2 _,_ … _, ℎ𝑘_ } consists of diverse constructive and improvement heuristics tailored to the agricultural optimization problems under study. Each heuristic acts as an operator that transforms a solution _𝑥_ into a neighboring solution _𝑥_<sup>′</sup> . 

1. **Nearest Neighbor Heuristic (NNH)** : Constructs a solution by iteratively selecting the nearest feasible option (e.g., nearest farm to deliver to, or nearest water source for irrigation), as shown in Algorithm 1. 

2. **Greedy Insertion Heuristic (GIH)** : Inserts a new element (crop or route) into the current solution at the position that provides the maximum marginal gain in objective value. 

3. **Swap Heuristic (SW)** : Swaps two randomly selected assignments (e.g., swapping crop allocations between two parcels). 

4. **2-Opt Heuristic (2OPT)** : Reverses a subsequence in a route or assignment to reduce total distance or cost. 

5. **Random Removal Heuristic (RR)** : Randomly removes a portion of the solution (e.g., removes 10% of assigned crops) to introduce diversification. 

6. **Random Reallocation Heuristic (RA)** : Randomly reallocates a selected element to a different feasible location. 

4 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

7. **Water-Balanced Redistribution Heuristic (WBR)** : Redistributes water allocation from lower-need parcels to higher-need parcels while preserving total water use, as shown in Algorithm 2. 

8. **Capacity-Constrained Greedy Heuristic (CCGH)** : Greedily adds elements to the solution respecting capacity constraints (e.g., water, labor, transport capacity), as shown in Algorithm 3. 

Each heuristic operates under feasibility checks to ensure that constraints (e.g., water, land, labor) are not violated. 

**Algorithm 1** Nearest Neighbor Heuristic (NNH) 

**Require:** Set of nodes _𝑁_ , distance matrix _𝐷_ , starting node _𝑠_ **Ensure:** Route visiting all nodes 

- 1: Initialize route _𝑅_ ← [ _𝑠_ ] 

- 2: Initialize unvisited set _𝑈_ ← _𝑁_ ⧵ { _𝑠_ } 

equal probabilities. After each application, _𝑞_ ( _ℎ_ ) is updated based on the improvement _𝛥𝑓_ achieved: 

#### _𝑞_ ( _ℎ_ ) ← _𝑞_ ( _ℎ_ ) + _𝛼_ ( _𝛥𝑓_ − _𝑞_ ( _ℎ_ )) 

where _𝛼_ is a learning rate parameter. 

Selection probability _𝑃_ ( _ℎ_ ) is computed using a softmax function: 



<!-- Start of picture text -->
𝑒 𝑞 ( ℎ )∕ 𝜏<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑃 ( ℎ ) =<br>∑ ℎ ′ ∈ 𝑒𝑞 ( ℎ ′)∕ 𝜏<br><!-- End of picture text -->

where _𝜏_ is a temperature parameter controlling exploration vs. exploitation. 

At each iteration, a heuristic is selected probabilistically according to _𝑃_ ( _ℎ_ ). 

#### _4.3. Move acceptance criterion_ 

- 3: Set current node _𝑐_ ← _𝑠_ 

- 4: **while** _𝑈_ ≠ ∅ **do** 

- 5: Find nearest neighbor _𝑛_<sup>∗</sup> ← arg min _𝑛_ ∈ _𝑈 𝐷_ [ _𝑐_ ][ _𝑛_ ] 

- 6: Append _𝑛_<sup>∗</sup> to route: _𝑅_ ← _𝑅_ + [ _𝑛_<sup>∗</sup> ] 

- 7: Remove _𝑛_<sup>∗</sup> from unvisited set: _𝑈_ ← _𝑈_ ⧵ { _𝑛_<sup>∗</sup> } 

- 8: Update current node: _𝑐_ ← _𝑛_<sup>∗</sup> 

- 9: **end while** 

- 10: **return** route _𝑅_ 

**Algorithm 2** Water-Balanced Redistribution Heuristic (WBR) 

**Require:** Set of parcels _𝑃_ , current water allocation _𝑤𝑝_ for each _𝑝_ ∈ _𝑃_ , water need _𝑛𝑝_ for each _𝑝_ ∈ _𝑃_ 

**Ensure:** Updated water allocation _𝑤𝑝_ for each _𝑝_ ∈ _𝑃_ 

- 1: Compute water deficit for each parcel: _𝑑𝑝_ ← _𝑛𝑝_ − _𝑤𝑝_ 

- 2: Define _𝐷_<sup>+</sup> ← { _𝑝_ ∈ _𝑃_ ∣ _𝑑𝑝 >_ 0} (under-allocated parcels) 

- 3: Define _𝐷_<sup>−</sup> ← { _𝑝_ ∈ _𝑃_ ∣ _𝑑𝑝 <_ 0} (over-allocated parcels) 

4: **for all** _𝑝_ ∈ _𝐷_<sup>+</sup> **do** 

- 5: **for all** _𝑞_ ∈ _𝐷_<sup>−</sup> **do** 6: _𝛿_ ← min( _𝑑𝑝,_ − _𝑑𝑞_ ) 

- 7: Update allocation: _𝑤𝑝_ ← _𝑤𝑝_ + _𝛿_ , _𝑤𝑞_ ← _𝑤𝑞_ − _𝛿_ 

- 8: Update deficits: _𝑑𝑝_ ← _𝑑𝑝_ − _𝛿_ , _𝑑𝑞_ ← _𝑑𝑞_ + _𝛿_ 

- 9: **if** _𝑑𝑝_ = 0 **then** 

- 10: **break** 

- 11: **end if** 

- 12: **end for** 

- 13: **end for** 

A Simulated Annealing-inspired acceptance criterion is used to prevent premature convergence to local optima. Given a current solution _𝑥_ and a candidate solution _𝑥_<sup>′</sup> , the acceptance probability _𝐴_ is: 



<!-- Start of picture text -->
1 , if 𝑓 ( 𝑥 ′ ) ≤ 𝑓 ( 𝑥 )<br>𝐴 =<br>{ 𝑒 −( 𝑓 ( 𝑥 ′)− 𝑓 ( 𝑥 ))∕ 𝑇 , if 𝑓 ( 𝑥 ′ )  > 𝑓 ( 𝑥 )<br><!-- End of picture text -->

where _𝑇_ is the current temperature, reduced over time using a geometric cooling schedule: 

_𝑇𝑛𝑒𝑤_ = _𝜆𝑇𝑐𝑢𝑟𝑟𝑒𝑛𝑡_ 

with 0 _< 𝜆<_ 1. 

Better solutions are always accepted; worse solutions are accepted probabilistically depending on _𝑇_ . 

#### _4.4. Termination criteria_ 

The hyper-heuristic process terminates when one of the following 

conditions is met: 

1. **Maximum Iterations:** A pre-defined number of iterations _𝑁𝑚𝑎𝑥_ is reached. 

2. **No Improvement:** No improvement is observed over the last _𝑊_ consecutive iterations (stagnation window). 

3. **Time Limit:** A computational time threshold _𝑡𝑚𝑎𝑥_ is exceeded. 

At termination, the best-found solution _𝑥_<sup>∗</sup> is returned as the output. 

14: **return** updated water allocation { _𝑤𝑝_ ∣ _𝑝_ ∈ _𝑃_ } 

#### _4.5. Overall framework flow_ 

#### **Algorithm 3** Capacity-Constrained Greedy Heuristic (CCGH) 

**Require:** Set of candidate items _𝐼_ , benefit _𝑏𝑖_ for each _𝑖_ ∈ _𝐼_ , resource requirement _𝑟𝑖_ for each _𝑖_ ∈ _𝐼_ , total capacity _𝐶_ 

**Ensure:** Selected subset _𝑆⊆𝐼_ maximizing benefit under capacity constraint 

- 1: Initialize _𝑆_ ← ∅, _𝑟𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦_ ← _𝐶_ 

- 2: Sort _𝐼_ in descending order of benefit-to-resource ratio: _𝑏𝑖_ ∕ _𝑟𝑖_ 

- 3: **for all** _𝑖_ ∈ _𝐼_ (in sorted order) **do** 

- 4: **if** _𝑟𝑖_ ≤ _𝑟𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦_ **then** 

- 5: _𝑆_ ← _𝑆_ ∪{ _𝑖_ } 

- 6: _𝑟𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦_ ← _𝑟𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦_ − _𝑟𝑖_ 

The proposed selection-based hyper-heuristic is stated for a minimization objective and makes each internal mechanism explicit. The hyper-heuristic optimization framework operates as follows: 

   1. Initialize a feasible solution _𝑥_ . 

   2. Initialize heuristic quality scores _𝑞_ ( _ℎ_ ) for all _ℎ_ ∈ . 

   3. Set controller parameters and state: _𝑥_<sup>_⋆_</sup> ← _𝑥_ , temperature _𝑇_ ← _𝑇_ 0, learning rate _𝛼_ , exploration temperature _𝜏_ , cooling factor _𝜆_ , iteration/time budgets ( _𝑁_ max _, 𝑡_ max), and stagnation window _𝑊_ with counter stall ← 0. 

   4. Repeat until termination condition: 

- 7: **end if** 

- 8: **end for** 

- 9: **return** selected set _𝑆_ 

#### _4.2. Heuristic selection method_ 

A reinforcement learning-based selection mechanism is adopted using a **multi-armed bandit (MAB) approach**. Let _𝑞_ ( _ℎ_ ) denote the quality estimate (reward) of heuristic _ℎ_ . Initially, all heuristics have 

- (a) _Early stop check:_ if elapsed time _> 𝑡_ max or stall ≥ _𝑊_ , then terminate. 

- (b) Select heuristic _ℎ_ using selection probability _𝑃_ ( _ℎ_ ) given by a softmax multi-armed bandit: 

exp( _𝑞_ ( _ℎ_ )∕ _𝜏_ ) _𝑃_ ( _ℎ_ ) = ~~∑~~ _ℎ_<sup>′</sup> ∈<sup>exp(</sup><sup>_𝑞_(</sup><sup>_ℎ_′)∕</sup><sup>_𝜏_)</sup><sup>_._</sup> 

- (c) Apply _ℎ_ to _𝑥_ to generate _𝑥_<sup>′</sup> under feasibility checks for land, water, capacity, and routing constraints. 

5 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

- (d) Evaluate _𝑓_ ( _𝑥_<sup>′</sup> ) and compute the improvement _𝛥𝑓_ ← _𝑓_ ( _𝑥_ ) − _𝑓_ ( _𝑥_<sup>′</sup> ). 

- (e) Accept _𝑥_<sup>′</sup> as new _𝑥_ with probability _𝐴_ (simulatedannealing-inspired): 

1 _, 𝛥𝑓>_ 0 _, 𝐴_ = {exp<sup>(</sup> −| _𝛥𝑓_ |∕ _𝑇_<sup>)</sup> _,_ otherwise. 

If accepted and _𝑓_ ( _𝑥_ ) _< 𝑓_ ( _𝑥_<sup>_⋆_</sup> ), set _𝑥_<sup>_⋆_</sup> ← _𝑥_ ; update stall accordingly. 

   - (f) Update _𝑞_ ( _ℎ_ ) based on _𝛥𝑓_ via a bandit reward: _𝑞_ ( _ℎ_ ) ← _𝑞_ ( _ℎ_ ) + _𝛼_ ( _𝛥𝑓_ − _𝑞_ ( _ℎ_ )); then cool _𝑇_ ← _𝜆𝑇_ . 

5. Return best solution found _𝑥_<sup>_⋆_</sup> and the derived decision products (seasonal crop mix, weekly irrigation calendar, and daily first-mile CVRPTW routes). 

This expanded flow exposes the controller (softmax bandit), feasibility-preserving low-level heuristics, SA-style acceptance with geometric cooling, reinforcement-style quality updates, and explicit termination via budget and stagnation, clarifying how exploration and exploitation are balanced across crop planning, irrigation scheduling, and logistics. 

#### **5. Experimental results** 

The proposed hyper-heuristic framework was implemented in Python 3.11 using the DEAP and NumPy libraries. Experiments were conducted on an Intel Core i7 12th Gen CPU with 16 GB RAM. A real-world dataset was collected from 15 Lebanese farms in the Beqaa Valley, covering three agricultural seasons. The dataset included crop yields, irrigation schedules, land characteristics, and logistics routes, totaling 120 unique decision variables across 50 constraints. We focus on the Beqaa Valley because it concentrates a large share of Lebanon’s agricultural activity, features fragmented smallholder parcels, and relies heavily on irrigation, making it representative of the constraints modeled in this study (water scarcity, heterogeneous parcels, and first-mile access). 

In order to rigorously evaluate the performance of the proposed hyper-heuristic framework, we benchmarked it against three wellestablished baseline metaheuristic algorithms: Genetic Algorithm (GA), Simulated Annealing (SA), and Tabu Search (TS). These metaheuristics were selected due to their widespread application and proven effectiveness in agricultural optimization problems, as documented in prior literature [13,14,23]. The comparison was conducted across three representative and practically relevant optimization problem classes: 

1. **Crop Planning Optimization:** Determining the optimal allocation of different crop types to available land parcels to maximize expected yield or revenue under constraints such as water, labor, and land suitability. 

2. **Irrigation Scheduling Optimization:** Allocating limited water resources over time and across multiple farm plots to minimize water consumption while ensuring required crop water needs are met. 

3. **Supply Chain Logistics Optimization:** Designing transportation routes to deliver harvested crops from farms to markets, with the objective of minimizing total distribution costs while satisfying delivery deadlines and capacity constraints. We instantiate this layer as first-mile farm-to-market routing modeled as a capacitated VRP with optional time windows (CVRPTW). 

#### _5.1. Benchmark rationale and fairness_ 

GA, SA, and TS are established, transparent single-method baselines spanning population-based, temperature-driven, and memory-based neighborhood search. Using this trio provides broad coverage of search behaviors and aligns with prior agricultural optimization studies. In 



**Fig. 1.** Average normalized objective value by method across the three 

problems (Crop Planning, Irrigation Scheduling, First-Mile Logistics). 

addition, we include two advanced population-based hyper-heuristic controllers, Artificial Bee Colony-HH (ABC-HH) [31] and Grey Wolf Optimizer-HH (GWO-HH) [32], instantiated over the same low-level heuristic pool  with matched evaluation budgets and stopping criteria. For fairness, all methods used identical stopping criteria and the same seed protocol; results are averaged over 30 independent runs per problem. 

This experimental setup aimed to assess the generalizability, solution quality, and computational efficiency of the proposed hyperheuristic framework relative to both single-method baselines (GA, SA, TS) and advanced HH controllers (ABC-HH, GWO-HH) across diverse yet interrelated agricultural decision-making contexts. 

Each algorithm was run 30 independent times per problem to ensure statistical validity. Runs used fixed pseudo-random seeds (one per run) for reproducibility; we report means and standard deviations of the normalized objective (to [0 _,_ 1]). Significance was assessed with paired _𝑡_ -tests across matched runs (HH vs. comparator); when normality was questionable, Wilcoxon signed-rank tests corroborated results. Multiple comparisons across all comparators (GA, SA, TS, ABC-HH, GWO-HH) were Holm-adjusted ( _𝛼_ = 0 _._ 05). 

#### _5.2. Solution quality comparison_ 

Fig. 1 presents the average objective function values (normalized to [0,1]) achieved by each algorithm across the three problems. The hyper-heuristic framework outperformed the baseline metaheuristics in all problems. Specifically: 

- **Crop Planning:** 12.3% improvement over GA; 15.8% over SA; 10.4% over TS. 

- **Irrigation Scheduling:** 9.7% improvement over GA; 11.2% over SA; 8.1% over TS. 

- **Supply Chain Logistics:** 14.6% improvement over GA; 17.1% over SA; 13.2% over TS. 

All improvements were statistically significant at _𝑝<_ 0 _._ 05 (paired t- test). These results support **H1** (higher objective values than GA/SA/TS) and **H4** (cross-problem generalization without retuning). 

#### _5.3. Per-run performance distributions_ 

Fig. 2 summarizes the per-run normalized objective over 30 independent runs for each method (GA, SA, TS, HH) and each problem class (crop planning, irrigation scheduling, first-mile logistics). The hyperheuristic (HH) exhibits lower medians (better) and tighter interquartile ranges across problems, indicating both improved central performance and reduced variability relative to baselines. 

6 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 



**Fig. 2.** Per-run distributions (30 runs each) of normalized objective by method and problem class. Boxes show IQR with median; whiskers show 5–95th percentiles; dots show outliers. 

**Table 1** 

Performance under individual or fixed-cycle LLHs. 

|Method (LLH mode)|Crop planning|Irrigation scheduling|Logistics|
|---|---|---|---|
|Nearest-Neighbor<br>Heuristic (NNH)|0.812 ± 0.029|0.798 ± 0.032|0.819 ± 0.028|
|Greedy insertion|0.828 ± 0.027|0.809 ± 0.026|0.833 ± 0.025|
|Swap|0.817 ± 0.031|0.802 ± 0.029|0.825 ± 0.027|
|2-Opt|0.823 ± 0.028|0.810 ± 0.027|0.836 ± 0.024|
|Random removal|0.798 ± 0.034|0.787 ± 0.031|0.812 ± 0.030|
|Random reallocation|0.805 ± 0.030|0.792 ± 0.028|0.818 ± 0.026|
|Water-Balanced|0.834 ± 0.025|0.816 ± 0.022|0.841 ± 0.023|
|Redistribution (WBR)||||
|Capacity-Constrained<br>Greedy (CCGH)|0.839 ± 0.022|0.821 ± 0.021|0.846 ± 0.021|
|Fixed cycle (Swap →|0.847 ± 0.021|0.828 ± 0.020|0.853 ± 0.019|
|2-Opt → CCGH)||||
|**Hyper-heuristic**<br>**(Proposed)**|**0.923** ± **0.018**|**0.902** ± **0.019**|**0.914** ± **0.017**|



#### _5.4. Ablation: Performance under individual LLHs_ 

To evaluate the contribution of each low-level heuristic (LLH), we conducted an ablation analysis in which the selection controller was disabled and each LLH was executed individually or within a fixed cyclic schedule. All configurations used identical stopping criteria and computational budgets as the main hyper-heuristic (HH) framework to ensure fair comparison. Table 1 reports the mean ± standard deviation of normalized objective values over 30 independent runs per problem class. 

The results indicate that no single LLH consistently achieves performance comparable to the adaptive HH framework. While constructive operators such as Greedy Insertion and Capacity-Constrained Greedy (CCGH) yield relatively strong results on structured problems (e.g., routing and allocation), destructive or perturbation heuristics (e.g., Random Removal, Swap) are effective mainly in early diversification. The integrated HH controller, which dynamically balances exploration and exploitation through the softmax-based selection policy, consistently outperforms all fixed strategies by combining the strengths of individual heuristics in a self-adaptive manner. 

The ablation confirms that the HH’s learning-driven combination of complementary heuristics achieves superior and more consistent outcomes than any stand-alone or cyclic configuration, validating its capability to adapt heuristic utility dynamically across diverse agricultural decision-making scenarios. 

#### _5.5. Computational time_ 

Fig. 3 compares the average computational time (seconds) required to reach convergence. While the hyper-heuristic required 18.5% more computational time on average than the fastest baseline (SA), the solution quality gains justify the additional runtime, especially in strategic planning contexts. 



**Fig. 3.** Average computational time to convergence by method. 

**Table 2** 

Advanced HH baselines vs. <u>proposed</u> method (30 runs, normalized objective). 

|Method|Crop planning|Irrigation scheduling|Logistics|
|---|---|---|---|
|ABC-HH|0.904 ± 0.021|0.887 ± 0.022|0.895 ± 0.020|
|GWO-HH|0.911 ± 0.019|0.893 ± 0.021|0.900 ± 0.018|
|**Proposed**|**0.923** ± **0.018**|**0.902** ± **0.019**|**0.914** ± **0.017**|





**Fig. 4.** Evolution of heuristic selection probabilities over iterations (softmax policy). 

#### _5.6. Comparison with advanced hyper-heuristic baselines_ 

Table 2 reports the 30-run averages (mean ± std, normalized objective) for ABC-HH, GWO-HH, and the proposed selection-based HH across all problem classes. While ABC-HH and GWO-HH are competitive, our HH attains higher means with lower dispersion, indicating better stability and cross-problem generalization. 

#### _5.7. Heuristic selection dynamics_ 

The evolution of heuristic selection probabilities over time is shown in Fig. 4. Early iterations exhibited high exploration, with uniform selection across heuristics. Over time, the selection mechanism converged toward a subset of consistently effective heuristics (e.g., Swap, 2-Opt, Capacity-Constrained Greedy). 

This adaptive heuristic utilization illustrates the framework’s ability to learn heuristic utility patterns from problem feedback. The convergence of probabilities toward a stable subset of operators is consistent with **H2** . 

7 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 



**Fig. 5.** Convergence curves in irrigation scheduling optimization. 

**Table 3** 

Performance summary of optimization methods. 

|Method|Avg. objective|Avg. time (s)|Std. dev|
|---|---|---|---|
|Hyper-heuristic|0.923|212.5|0.018|
|Genetic algorithm|0.822|187.4|0.031|
|Simulated annealing|0.829|179.2|0.028|
|Tabu search|0.837|193.5|0.025|



#### _5.8. Convergence behavior_ 

Fig. 5 depicts the convergence curves (objective value vs. iteration) for the hyper-heuristic and baseline algorithms in the irrigation scheduling problem. 

The hyper-heuristic achieved faster convergence in early iterations while maintaining improvement potential in later iterations compared to the baselines. This pattern, together with the aggregate gains, further supports **H1** . 

#### _5.9. Interpretability and insights_ 

Analyzing the final solutions revealed that the hyper-heuristic framework favored: 

- Diversified crop plans balancing water use and yield 

- Irrigation schedules prioritizing high-value crops under limited water 

- Supply chain routes minimizing distance while clustering deliveries 

This interpretable pattern aligns with domain knowledge, increasing the solution’s acceptability to agricultural stakeholders. These qualitative insights are aligned with **H3** . 

#### _5.10. Summary of results_ 

Table 3 summarizes the quantitative performance across methods. The hyper-heuristic achieved superior average solution quality with competitive runtime and acceptable variance. Combined with the statistical analysis above, these findings reinforce **H1** – **H4** . 

#### **6. Discussion** 

The experimental results demonstrate that the proposed hyperheuristic framework consistently outperforms baseline metaheuristic methods (Genetic Algorithm, Simulated Annealing, Tabu Search) across all three agricultural optimization problems, crop planning, irrigation scheduling, and supply chain logistics. The improvements in objective 

function values (ranging from 9.7% to 15.8%) align with prior studies indicating that hyper-heuristic approaches can achieve higher solution quality by dynamically adapting heuristic selection to problem instance characteristics [16,17]. These aggregate gains directly support **H1** and, because no problem-specific retuning was required across the three classes, also support **H4** . 

#### _6.1. Effectiveness of heuristic selection mechanism_ 

The reinforcement learning-based selection mechanism, employing a softmax probability distribution, successfully guided the framework toward effective heuristics while maintaining exploration in early iterations. Fig. 4 illustrated how heuristic selection probabilities converged toward a subset of high-performing heuristics (Swap, 2-Opt, CapacityConstrained Greedy), confirming the framework’s ability to learn and exploit heuristic utility patterns. This convergence behavior is consistent with **H2** , wherein the policy places increasing mass on a compact subset of operators as evidence accumulates, and is further supported by the LLH ablation in Section 5.4, where stand-alone or fixed-cycle LLHs underperform the adaptive controller. Moreover, relative to advanced hyper-heuristic comparators (ABC-HH, GWO-HH), the learned selection policy maintains superior central performance and lower dispersion (Section 5.6, Table 2). This dynamic adaptation contrasts with static heuristic selection in metaheuristics, which often rely on manual tuning or fixed operators [15,18]. 

The diversity of low-level heuristics played a critical role in enabling the framework to navigate heterogeneous problem landscapes. Destructive heuristics (Random Removal) facilitated exploration, while constructive heuristics (Greedy Insertion, Capacity-Constrained Greedy) enabled intensification. This balance of diversification and intensification is a hallmark of effective hyper-heuristic design [16]. In practice, the policy’s early broad exploration followed by focused exploitation (Fig. 4) mirrors the behavior observed in the convergence curves (Fig. 5) and in the per-run distributions (Fig. 2), where tighter interquartile ranges for HH indicate stable performance across the 30 independent runs. 

#### _6.2. Trade-off between solution quality and computational time_ 

While the hyper-heuristic required an average of 18.5% more computational time than the fastest baseline (Simulated Annealing), this increase is justified by the superior solution quality and robustness. In real-world agricultural planning contexts, where decisions are made on seasonal or monthly timescales, a modest increase in computation is acceptable if it yields more resource-efficient and resilient plans. Moreover, the time-to-solution remains compatible with offline planning workflows (Fig. 3). 

The computational overhead arises from the need to evaluate multiple low-level heuristics and update selection probabilities per iteration. Future work could explore surrogate modeling or early termination of heuristic evaluations to reduce runtime without compromising solution quality. Additional engineering options include (i) batched/parallel evaluation of candidate moves, (ii) bandit-based early stopping for underperforming operators within an iteration, and (iii) adaptive temperature schedules to curb unnecessary exploration once selection uncertainty declines. 

#### _6.3. Interpretability and practical insights_ 

Beyond numerical performance, the hyper-heuristic produced solutions with interpretable patterns that align with domain expertise. For example, the optimized crop plans favored mixed-crop allocations balancing water-intensive and drought-tolerant varieties, while irrigation schedules prioritized high-value crops under constrained water availability. These emergent behaviors suggest that the heuristic selection process captured underlying agricultural trade-offs. Such patterns 

8 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

are precisely those anticipated in **H3** (e.g., diversified crop mixes and prioritization by marginal yield response), supporting stakeholder understanding of _why_ the model recommends a given plan. 

Such interpretability increases stakeholder trust in optimization outputs and enhances the likelihood of adoption by farmers and policymakers, addressing a known barrier in AI-based agricultural decisionsupport tools [10,11]. In practical terms, these results translate into: (i) parcel-level guidance for allocating scarce irrigation to plots with the highest marginal return, (ii) data-informed crop diversification strategies under water risk, and (iii) clustered first-mile routes (modeled as CVRPTW) that reduce distance and fuel consumption, implications that we operationalize in the policy recommendations. Relative to machine learning predictors (e.g., CNNs), our selection-based hyper-heuristic plays a complementary role: ML models can serve as surrogates to score candidate moves, provide learned warm-starts, or extract state features, whereas the HH performs the combinatorial search over feasible decisions. Thus, ML augments guidance, not replaces the discrete optimization engine. 

#### _6.4. Generalizability and scalability_ 

The framework’s ability to achieve high-quality solutions across three distinct problem types (crop planning, irrigation scheduling, logistics) highlights its potential generalizability. Unlike metaheuristics that require problem-specific parameter tuning, the hyper-heuristic adapted its heuristic selection strategy without manual reconfiguration. This adaptability is especially valuable in developing countries like Lebanon, where diverse farm types, resources, and operational constraints co-exist within small geographic regions. Notably, a single selection mechanism was reused across problem classes, lending further evidence to **H4** . At the same time, the modular design allows new low-level operators (e.g., agronomy-specific neighborhood moves) to be plugged in without altering the high-level policy. Moreover, our pattern of gains, policy-driven operator selection outperforming single metaheuristics and converging to a compact operator subset, is qualitatively consistent with reports in logistics, timetabling, and inventory optimization, suggesting that the mechanisms observed here align with broader hyper-heuristic evidence. 

standard metaheuristics (GA, SA, TS) by 9 _._ 7 −15 _._ 8% while maintaining robust solutions across problem types. Its adaptive heuristic selection and interpretable results demonstrate its potential as a scalable decision-support tool for resource-constrained agricultural systems. 

Despite its strong performance, the study has limitations, including higher computational time, reliance on a predefined heuristic pool, and single-objective focus. Future work will address multi-objective optimization, automated heuristic generation, scalability to larger datasets, and improved logistics modeling under uncertainty. Additionally, efficiency and scalability will be enhanced via parallel evaluations, surrogate-assisted selection, learning-to-rank models, and graph-based warm starts for routing problems. 

#### **CRediT authorship contribution statement** 

**Kassem Danach:** Writing – original draft, Software, Project administration, Investigation, Data curation. **Hassan Harb:** Writing – review & editing, Supervision, Resources, Formal analysis, Conceptualization. **Hamza Issa:** Writing – review & editing, Visualization, Validation, Methodology. 

#### **Funding** 

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. 

#### **Generative-AI** 

The authors did not use any generative AI and AI-assisted technologies in the writing process. 

#### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Data availability** 

#### _6.5. Limitations_ 

Data will be made available on request. 

Despite promising results, several limitations warrant discussion. First, computational experiments were conducted on a moderate-scale dataset (15 farms, 120 variables). Scaling the framework to larger regional datasets may introduce additional computational challenges. Second, the current heuristic pool was designed based on expert input and literature but may not cover all possible operators beneficial in specialized agricultural contexts. Future work should explore automated generation of low-level heuristics or incorporation of domainspecific heuristics. Third, although statistical testing (paired _𝑡_ -tests with Holm correction and Wilcoxon confirmations) indicated significance, external validity beyond the Beqaa Valley remains to be established; broader, multi-region datasets and out-of-distribution evaluations would strengthen conclusions. Fourth, the logistics layer assumes deterministic travel times and service durations; extending to stochastic CVRPTW or robust counterparts would better capture rural road variability. Finally, the present study is single-objective; multi-objective extensions (e.g., yield, water, cost, and risk) and sensitivity analyses over objective weights are important directions for future research. 

#### **7. Conclusion** 

This study presents a selection-based hyper-heuristic framework for optimizing crop planning, irrigation scheduling, and farm-to-market logistics in Lebanese farms. Using reinforcement learning to dynamically select low-level heuristics, the framework solves complex problems without problem-specific tuning. Experiments show it outperforms 

#### **References** 

- [1] FAO, Lebanon: Country programming framework 2016–2022, 2021, URL https: //www.fao.org/lebanon/en/. 

- [2] N. Nasrallah, Agriculture in crisis: The impact of Lebanon’s economic collapse on food security, Middle East Institute, 2018, URL https://www.mei.edu/ publications/agriculture-crisis. 

- [3] M. Naoufal, M. Daher, Impact of climate change on lebanese agriculture: Vulnerability and adaptation measures, Reg. Environ. Chang. 17 (2017) 1289–1300. 

- [4] J.O. Jaber, Food security challenges in Lebanon: The role of agriculture, Food Secur. 11 (2019) 97–108. 

- [5] K. Danach, H. Harb, W.H.F. Aly, H. Kanj, A.S.K. Rashid, Bio-inspired optimization through photosynthesis: A novel approach for balancing exploration and exploitation in complex systems, Eur. J. Pure Appl. Math. 18 (2) (2025) 5980–5980. 

- [6] S. Ayoubi, Y. Chen, C. Assi, T. Khalifa, K.B. Shaban, Multicast tree repair and maintenance in the cloud, in: 2015 IEEE 8th International Conference on Cloud Computing, IEEE, 2015, pp. 829–835. 

- [7] M. Alomari, A. Jaradat, A. Jafar, H. Al-Muhtaseb, H. Shakhatreh, AgriFusion: A low-carbon sustainable computing approach for precision agriculture, Comput. Intell. (2024) http://dx.doi.org/10.1111/coin.70006, URL https://onlinelibrary. wiley.com/doi/abs/10.1111/coin.70006. 

- [8] K. Danach, H. Harb, B. Baz, A. Nasser, A hyperheuristic approach to multiechelon hub and routing optimization: Model, valid inequalities, and case study, IEEE Open J. Intell. Transp. Syst. (2025). 

- [9] K. Danach, L. Saker, H. Harb, Integrating metaheuristics and machine learning for enhanced vehicle routing: A comparative study of hyperheuristic and VAE-based approaches, World Electr. Veh. J. (2025). 

9 

_K. Danach et al._ 

_Journal of Agriculture and Food Research 24 (2025) 102522_ 

- [10] J.O. Jaber, Food security challenges in Lebanon: The role of agriculture, Food Secur. 11 (2019) 97–108. 

- [11] M. Naoufal, M. Daher, Impact of climate change on lebanese agriculture: Vulnerability and adaptation measures, Reg. Environ. Chang. 17 (2017) 1289–1300. 

- [12] R.L. Marques, A.M. Costa, Crop planning optimization: A review, Comput. Electron. Agric. 169 (2020) 105178. 

- [13] K. Kimura, K. Nakamura, Optimization of irrigation schedules under limited water resources, Agricult. Water. Manag. 210 (2018) 26–36. 

- [14] L. Pérez, C. Rodríguez, Supply chain optimization in agri-food systems: A review, Comput. Ind. Eng. 152 (2021) 107014. 

- [15] P.I. Cowling, G. Kendall, E. Soubeiga, A hyperheuristic approach to scheduling a sales summit, in: International Conference on the Practice and Theory of Automated Timetabling, Springer, 2001, pp. 176–190. 

- [16] E.K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Ozcan, R. Qu, Hyper-heuristics: A survey of the state of the art, J. Oper. Res. Soc. 64 (12) (2013) 1695–1724. 

- [17] S. Muhammad, S. Hassan, Hyper-heuristic approaches for scheduling optimization: Recent developments and trends, Artif. Intell. Rev. 54 (2021) 3097–3138. 

- [18] S. Boukra, M. Ouali, A hyper-heuristic framework for solving vehicle routing problems with time windows, Expert Syst. Appl. 140 (2020) 112881. 

- [19] P. Sharma, R. Singh, Hyper-heuristic approaches in supply chain network design: A comprehensive review, Comput. Oper. Res. 140 (2022) 105664. 

- [20] M.F. Diaz, N. Kalaitzandonakes, Planning farm operations using mixed-integer programming, Comput. Electron. Agric. 60 (1) (2008) 21–30. 

- [21] M. Manzanera, D. Badia, Irrigation planning optimization under water scarcity: A case study, Agricult. Water. Manag. 98 (4) (2011) 622–629. 

- [22] J. Zhang, Q. Yu, Multi-objective optimization of irrigation scheduling using particle swarm optimization, Comput. Electron. Agric. 159 (2019) 48–60. 

- [23] J. Soares, M. Alves, Metaheuristics in agricultural planning: A review, Comput. Electron. Agric. 175 (2020) 105537. 

- [24] B. Bilgin, A. Demiriz, E. Ozcan, A survey of hyper-heuristics for educational timetabling, INFORMS J. Comput. 19 (1) (2007) 54–64. 

- [25] K. Danach, W. Khalil, S. Gelareh, Multiple strings planing problem in maritime service network: Hyper-heuristic approach, in: 2015 Third International Conference on Technological Advances in Electrical, Electronics and Computer Engineering, TAEECE, IEEE, 2015, pp. 85–88. 

- [26] K. Danach, J.A.-H. Hassan, W. Khalil, S. Gelareh, Routing heterogeneous mobile hospital with different patients priorities: Hyper-heuristic approach, in: 2015 Fifth International Conference on Digital Information and Communication Technology and Its Applications, DICTAP, IEEE, 2015, pp. 155–158. 

- [27] K. Danach, H. Harb, A.S.K. Rashid, M.A. Al-Tarawneh, W.H.F. Aly, Location planning techniques for Internet provider service unmanned aerial vehicles during crisis (Ph.D. thesis), Elsevier, 2025. 

- [28] J.A. Santos, J.F. Oliveira, Hyper-heuristic optimization of irrigation network design under water constraints, Agricult. Water. Manag. 190 (2017) 1–10. 

- [29] J. Chaves, J. Torres, Hyper-heuristic approaches for optimizing multi-crop greenhouse production schedules, Comput. Electron. Agric. 162 (2019) 13–22. 

- [30] K. Kimura, K. Nakamura, Optimization of irrigation schedules under limited water resources, Agricult. Water. Manag. 210 (2018) 26–36. 

- [31] D. Karaboga, B. Basturk, A powerful and efficient algorithm for numerical function optimization: artificial bee colony (ABC) algorithm, J. Global Optim. 39 (3) (2007) 459–471. 

- [32] S. Mirjalili, S.M. Mirjalili, A. Lewis, Grey wolf optimizer, Adv. Eng. Softw. 69 (2014) 46–61. 

10 

