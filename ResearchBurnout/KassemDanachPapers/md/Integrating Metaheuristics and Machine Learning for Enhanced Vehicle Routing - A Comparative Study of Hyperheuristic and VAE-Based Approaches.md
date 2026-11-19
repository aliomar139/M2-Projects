

_Article_ 

# **Integrating Metaheuristics and Machine Learning for Enhanced Vehicle Routing: A Comparative Study of Hyperheuristic and VAE-Based Approaches** 

**Kassem Danach**<sup>**1,†**</sup> **, Louai Saker**<sup>**2,**</sup> *****<sup>**,†**</sup> **and Hassan Harb**<sup>**2,†**</sup> 

- 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut 1600, Lebanon; kassem.danach@mu.edu.lb 

- 2 College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait; hassan.harb@aum.edu.kw 

- Correspondence: louai.saker@aum.edu.kw 

- These authors contributed equally to this work. 

Academic Editor: Grzegorz Sierpi´nski 

Received: 1 April 2025 Revised: 26 April 2025 Accepted: 29 April 2025 Published: 2 May 2025 

**Citation:** Danach, K.; Saker, L.; Harb, H. Integrating Metaheuristics and Machine Learning for Enhanced 

Vehicle Routing: A Comparative Study of Hyperheuristic and VAE-Based Approaches. _World Electr. Veh. J._ **2025** , _16_ , 258. https://doi.org/10.3390/ wevj16050258 

**Copyright:** © 2025 by the authors. Published by MDPI on behalf of the World Electric Vehicle Association. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

**Abstract:** This study addresses the optimization of the Vehicle Routing Problem (VRP) with prioritized customers by introducing and comparing two advanced solution approaches: a metaheuristic-based hyperheuristic framework and a Variational Autoencoder (VAE)-based hyperheuristic. The VRP with prioritized customers introduces additional complexity by requiring efficient routing while ensuring high-priority customers receive service within strict constraints. To tackle this challenge, the proposed metaheuristic-based hyperheuristic dynamically selects and adapts low-level heuristics using Simulated Annealing (SA) and Ant Colony Optimization (ACO), enhancing search efficiency and solution quality. In contrast, the VAE-based approach leverages deep learning to model historical routing patterns and autonomously generate new heuristics tailored to problem-specific characteristics. Through extensive computational experiments on benchmark VRP instances, our results reveal that both approaches significantly enhance routing efficiency, with the VAE-based method demonstrating superior generalization across varying problem structures. Specifically, the VAE-based approach reduces total travel costs by an average of 8% and improves customer priority satisfaction by 95% compared to traditional hyperheuristic methods. Moreover, a comparative analysis with recent state-of-the-art algorithms highlights the competitive performance of our approaches in balancing computational efficiency and solution quality. These findings underscore the potential of integrating metaheuristics with machine learning in complex routing problems and provide valuable insights for real-world logistics and transportation planning. Future research will explore the generalization of these methodologies to dynamic and large-scale routing scenarios. 

**Keywords:** intelligent transportation systems; artificial intelligence; metaheuristics; simulated annealing; ant colony optimization; variational autoencoder 

## **1. Introduction** 

The Vehicle Routing Problem (VRP) is a fundamental and widely studied problem in the field of logistics and operations research, originating from the need to optimize the delivery of goods and services to a set of geographically dispersed customers. The primary objective of the VRP is to determine the most efficient routes for a fleet of vehicles to service a given set of customers from a central depot while minimizing total costs, which typically include travel distance, time, or fuel consumption [1]. This problem has significant practical implications for industries such as transportation, distribution, and 

_World Electr. Veh. J._ **2025** , _16_ , 258 

https://doi.org/10.3390/wevj16050258 

_World Electr. Veh. J._ **2025** , _16_ , 258 

2 of 21 

supply chain management, where efficient routing can lead to substantial cost savings and improved service levels [2,3]. Furthermore, VRP is considered an extension of the wellknown Traveling Salesman Problem (TSP), where the goal is to find the shortest possible route that visits each customer exactly once and returns to the starting point [4]. 

### _1.1. Motivation_ 

Unfortunately, the VRP introduces additional complexities by incorporating multiple vehicles and constraints such as vehicle capacities, delivery time windows, and the necessity to serve customers with varying levels of priority [5,6]. These constraints make the VRP a more realistic and challenging problem, reflecting the operational considerations faced by logistics providers in real-world scenarios. 

Indeed, various formulations and variants of the VRP exist, each addressing specific logistical challenges. Some common variants include the Capacitated VRP (CVRP), where vehicles have a maximum load capacity that must not be exceeded, and the VRP with Time Windows (VRPTW), which adds constraints on the time periods during which customers can be served [7]. Another significant variant is the VRP with prioritized customers, where certain customers have higher service priorities, requiring routes to be planned in a way that prioritizes these customers’ needs over others [8]. 

Solving the VRP is computationally challenging due to its NP-hard nature, meaning that the time required to find an optimal solution increases exponentially with the size of the problem [9]. As a result, exact methods such as branch and bound or dynamic programming are often impractical for large instances, and heuristic and metaheuristic approaches are commonly employed to obtain near-optimal solutions within a reasonable computational time [10]. 

Heuristic methods, such as the Clarke–Wright savings algorithm and sweep algorithm, provide practical solutions by iteratively improving the initial routes through local search techniques [11]. Metaheuristic approaches, including genetic algorithms, Simulated Annealing, and Ant Colony Optimization, offer more advanced strategies by combining multiple heuristics and exploring the solution space more comprehensively [12]. These methods have been extensively used and refined in both academic research and industry applications to tackle the complexities of the VRP effectively [13]. 

The Vehicle Routing Problem (VRP) with prioritized customers is a critical optimization challenge in logistics and transportation, where the objective is to determine the most efficient routes for a fleet of vehicles to service a set of customers. This problem becomes even more complex when customer priorities are involved, requiring a nuanced approach to balancing delivery constraints with customer preferences [14]. The VRP with prioritized customers necessitates the optimization of routes that not only minimize costs but also meet specific delivery requirements for high-priority customers, thus adding layers of complexity to the traditional VRP framework [15]. 

Traditional metaheuristics, such as Simulated Annealing (SA) and Ant Colony Optimization (ACO), have been widely used for VRP due to their effectiveness in exploring large solution spaces and their flexibility in accommodating various constraints and objectives [16]. SA, inspired by the annealing process in metallurgy, allows for the probabilistic acceptance of worse solutions to escape the local optima and explore more diverse solutions [17]. ACO, modeled after the foraging behavior of ants, utilizes pheromone trails to guide the search process, iteratively improving the solution quality through collective learning [18]. 

Hyperheuristics represent a higher level of optimization, where the focus is on selecting and generating heuristics to solve complex problems dynamically [19]. In this context, metaheuristics like SA and ACO can be employed as heuristic selectors within 

_World Electr. Veh. J._ **2025** , _16_ , 258 

3 of 21 

a hyperheuristic framework, enhancing the ability to adapt to various problem instances and customer requirements [20]. This approach leverages the strengths of metaheuristics in navigating solution spaces while maintaining the flexibility to adjust heuristic selection based on the problem context [21,22]. 

### _1.2. Contributions_ 

Recent studies focused on applying hyperheuristics or machine learning-based algorithms to solve the Vehicle Routing Problem. In this paper, our main goal is to compare the traditional metaheuristic-driven hyperheuristic framework with Variational Autoencoders (VAEs)-based machine learning in solving the VRP with prioritized customers. By evaluating the performance of these approaches on benchmark VRP instances, we aim to provide insights into their relative strengths and weaknesses, highlighting the potential for integrating metaheuristics with machine learning to enhance logistics optimization. 

### _1.3. Paper Structure_ 

The rest of the paper is structured as follows. Section 2 discusses the state of the art on hyperheuristics and machine learning in VRP. Section 3 describes the problem statement along with the challenges and methodological approaches. The mathematical formulation of VRP with prioritized customers is shown in Section 4. Section 5 explains both types of hyperheuristics used in VRP, e.g., traditional and VAE based. Section 6 presents the performed experimentation and the result discussion. Finally, we provide a conclusion and suggest future works at Section 7. 

## **2. Related Works** 

Indeed, VRP is a fundamental challenge in logistics and transportation, with significant implications for cost reduction, efficiency improvement, and sustainability. Recently, researchers have focused their attention to VRP due to its complexity and real-world impact, leading to the development of various metaheuristic and machine learning approaches [23,24]. In the literature, VRP has been extensively studied, resulting in numerous extensions such as capacitated VRP, time-window constraints, and multi-depot variants to address industry-specific challenges. Furthermore, the advancements in artificial intelligence, machine learning, and optimization techniques have further enhanced VRP solutions, enabling more adaptive and scalable approaches. 

### _2.1. Hyperheuristics-Based Approaches_ 

Recent studies have explored the use of swarm intelligence for hyperheuristics in VRP. For example, [25] demonstrates the effectiveness of using swarm intelligence to guide heuristic selection for VRP, highlighting its potential for adaptive optimization in complex scenarios [26]. The study utilizes swarm intelligence to develop a hyperheuristic framework that dynamically adjusts the selection of low-level heuristics, effectively improving solution quality and computational efficiency. This approach underscores the value of combining heuristic selection strategies with adaptive learning mechanisms to tackle VRP challenges. The authors of [27] investigate a VRP that incorporates multiple objectives, ensuring vehicles reach destinations within a defined time window while considering crashed traveling time. The problem is addressed using a fuzzy multi-objective linear programming (FMOLP) approach, which reformulates it into a single-objective model. To tackle large-scale instances, an enhanced genetic algorithm (IGA) is introduced for efficient optimization. In [28], the authors address the Vehicle Routing Problem for Security Dispatch (VRPSD) by developing three optimization algorithms that integrate metaheuristic techniques. The methods utilize Adaptive Large Neighborhood Search (ALNS) alongside Threshold Accepting (TA) and Tabu Search (TS) to enhance search efficiency. By leverag- 

_World Electr. Veh. J._ **2025** , _16_ , 258 

4 of 21 

ing a multiphase strategy, these approaches improve exploration and avoid local optima effectively. The authors of [29] present the 2T-MDVRP-RS-TW, a Two-Tier Multi-Depot Vehicle Routing Problem with Robot Stations and Time Windows. It is a complex Vehicle Routing Problem incorporating multi-depot logistics, robot stations, and time windows. To solve it, a Mixed-Integer Linear Programming (MILP) model is formulated alongside a Multi-Start Iterated Local Search (MS-ILS-CR) approach. The MS-ILS-CR method enhances optimization by combining Multi-Start, Crossover, and Repair strategies drawn from advanced metaheuristics. In [30], the authors explore a delivery routing problem that integrates heavy depot vehicles, local vehicles, swap bodies, and switch points. A previously applied metaheuristic provides fast solutions but without quality assurance. To evaluate the solution quality, the authors develop two column generation-based formulations, optimizing complexity through switch point enumeration. The authors of [31] aim at heuristic and metaheuristic algorithms to optimize faculty transportation between two university campuses. Their study focuses on selecting efficient routing strategies and vehicle types, while the primary goal is to minimize travel distance through optimized route planning. In [32], a Time Window-based Green Vehicle Routing Problem (GVRP-TW) solution is introduced to optimize alternative fuel vehicle routes with time constraints. The approach ensures minimal refueling stops while serving customer demands efficiently. The objective is to decrease the travel distance, lower energy usage, and reduce CO2 emissions. The authors of [33] investigate optimizing UAV operations for search and pesticide spraying while managing battery and tank capacity constraints. To achieve this, a hybrid metaheuristic approach integrates genetic algorithm (GA) with a Guided Genetic Algorithm (GGA). The proposed method seeks to reduce energy and resource consumption for efficient mission execution. In [34], a smart two-echelon waste management system (WMS) leveraging Industry 4.0 and IoT devices is proposed to enhance waste collection efficiency. The system helps optimize bin collection and waste transfer routes. The model aims to cut costs and CO2 emissions using an advanced vehicle routing framework. In [35], the authors introduce a real-time feeder Vehicle Routing Problem (RTFVRP) where both trucks and motorcycles can participate in the freight delivery process. The problem is formulated using Mixed-Integer Linear Programming, and a dynamic inertia weight particle swarm optimization (DIWPSO) algorithm is proposed to provide an efficient solution. Finally, the authors of [36] propose a new hybrid approach, called GA-RR, designed to address the capacitated Vehicle Routing Problem. The method combines two well-established techniques: the ruin and recreate algorithm and the genetic algorithm. By leveraging the strengths of both, GA-RR balances exploration and exploitation to enhance solution quality. The goal is to generate optimal solutions across various Vehicle Routing Problem test instances. 

_2.2. Machine Learning-Based Approaches_ 

Recently, there has been growing interest in applying machine learning techniques into VRP [37,38]. The authors of [39] present an attention-based end-to-end deep reinforcement learning model for solving VRP, incorporating edge information between nodes for enhanced graph representation learning. The approach utilizes a Transformer-based encoder–decoder framework, integrating an edge information embedded multi-head attention (EEMHA) layer in the encoder. The EEMHA-based encoder captures the graph underlying structure by combining node and edge data, producing a rich topology representation. In [40], the authors explore the Capacitated Electric Vehicle Routing Problem (CEVRP) using an innovative Q-learning approach. Q-learning, a model-free reinforcement learning algorithm, optimizes decision-making by maximizing an agent cumulative reward. Furthermore, a mathematical model is employed to determine optimal solutions for each EVRP instance. The authors of [41] model VRP using a Markov decision process 

_World Electr. Veh. J._ **2025** , _16_ , 258 

5 of 21 

and propose a reinforcement learning (RL)-based solution. The RL model employs an attention-based encoder and a recurrent neural network decoder. This approach optimizes coordination by assigning vehicles to customers and determining rendezvous points, effectively integrating drones to minimize overall completion time. In [42], the authors address the limitation of assuming a fixed charging rate in traditional Electric Vehicle Routing Problems (EVRPs). Accordingly, a new EVRP model incorporating a flexible charging strategy (EVRP-FCS) is introduced, treating charged energy as a decision variable. Additionally, an improved evolutionary algorithm is developed to efficiently solve the model and explore the solution space more effectively. The authors of [43] present an efficient encoder–decoder framework, called the Residual Graph Convolutional Encoder with Multiple AttentionBased Decoders (RGCMA), trained using a reinforcement learning approach with an elite baseline. The encoder generates robust node representations by effectively aggregating neighborhood features through a dense residual edge and node feature updating block. Meanwhile, the multiple-decoder mechanism incrementally constructs diverse solutions for any CVRP instance, expanding the solution space and enhancing the overall solution quality. The authors of [44] introduce the Collaborative Attention Model with Profiles (CAMP), a novel approach utilizing multi-agent reinforcement learning to develop efficient solvers for the Profiled VRP (PVRP). CAMP features an attention-based encoder that embeds client profiles in parallel for each vehicle type. Furthermore, a communication layer enables collaborative decision-making among agents, while a batched pointer mechanism evaluates the likelihood of next actions by attending to the profiled embeddings during decoding. In [45], the authors present a flexible Hierarchical Learning-based Graph Partition (HLGP) framework designed to enhance the partitioning of CVRP instances by effectively combining global and local partition strategies. The global partition policy generates a coarse multi-way partition, breaking it down into sequential two-way partition subtasks. These subtasks serve as the foundation for the subsequent K local partition levels. At each level, the local partition policy handles specific subtasks, leveraging local topological features to incrementally reduce accumulated errors. In [46], a neural heuristic approach using deep reinforcement learning (DRL) to solve both traditional and enhanced variants of the VRB with Backhauls (VRPB) is proposed. The method employs an encoder–decoder structured policy network trained to sequentially generate vehicle routes. The VRPB is first modeled as a graph, with solution construction formulated as a Markov decision process. To better capture node relationships, a two-stage attention-based encoder is designed, incorporating self-attention and heterogeneous attention mechanisms to enhance node representations and improve solution quality. The authors of [47] introduce an end-to-end reinforcement learning framework for solving the VRP with Time Windows (VRPTW). The approach starts with an agent model that encodes constraints into input features and applies strict policies to ensure deterministic outputs. To handle time-window constraints effectively, a time penalty-augmented reward mechanism is incorporated during gradient propagation. The authors of [48] propose a deep reinforcement learning framework to address the dynamic and uncertain VRP (DU-VRP). A partial observation Markov decision process is designed to continuously monitor real-time fluctuations in customer demand within a decision support system powered by a deep neural network with a dynamic attention mechanism. Moreover, an advanced reinforcement learning algorithm is proposed to optimize the value function, enhancing the training process to better manage the complexities of routing dynamics and uncertainty. In [49], the study presents an ensemble-based deep reinforcement learning approach for solving VRP, where multiple diverse sub-policies are trained to handle various instance distributions. Diversity among sub-policies is encouraged using Bootstrap with random initialization. In addition, regularization terms are incorporated during training to further promote variation between sub-policies, enhancing overall solution adaptability. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

6 of 21 

### _2.3. State-of-the-Art Techniques: A Summary_ 

Table 1 summarizes the state-of-the-art techniques in VRP in terms of publication year, used methods, and category, e.g., hyperheuristic based or machine learning based. 

**Table 1.** State-of-the-art methods summary. 

|**Mthd [Rf]**|**Y**|**Ap**|**proach**|
|---|---|---|---|
|**eos e.**|**ear**|**Hyperheuristics**|**Machine Learning**|
|DRL [48]|2023||X|
|Ensemble-based DRL [49]|2023||X|
|Two-Echelon WMS, IoT [34]|2023|X||
|RTFVRP, DIWPSO [35]|2023|X||
|GA-RR [36]|2023|X||
|Variational Autoencoder [37]|2023||X|
|Variational Autoencoder [38]|2023||X|
|EEMHA [39]|2023||X|
|Swarm Intelligence, Adaptive<br>Learning [25]|2024|X||
|<br>Path Cheapest Arc, Path Most||||
|<br>Constrained Arc, Savings, Christofides,||||
|i<br>Greedy Descent, Guided Local Search,|2024|X||
|<br>Simulated Annealing, Tabu Search [31]||||
|GVRP-TW [32]|2024|X||
|UAV, GGA [33]|2024|X||
|DRL [46]|2024||X|
|VRPTW [47]|2024||X|
|FMOLP, IGA [27]|2025|X||
|ALNS, TA, TS [28]|2025|X||
|2T-MDVRP-RS-TW, MILP,<br>MS-ILS-CR [29]|2025|X||
|Two Column Generation-based|2025|X||
|Formulations [30]||||
|Q-learning [40]|2025||X|
|Markov Decision Process,||||
|<br>Reinforcement Learning [41]|2025||X|
|<br>EVRP-FCS [42]|2025||X|
|RGCMA [43]|2025||X|
|CAMP [44]|2025||X|
|HLGP [45]|2025||X|



## **3. Problem Statement** 

Figure 1 shows the scenario considered in this study and illustrates an instance of the Vehicle Routing Problem (VRP) along with its optimized solution. On the left side, we see a network of points representing customers that require service, with a central point labeled “Depot”, which serves as the starting and ending location for the delivery vehicles. The lines connecting the customers and the depot illustrate the various possible routes that vehicles could take to deliver goods or services. This network is unorganized, depicting all potential routes without any optimization. The primary goal in this scenario is to determine the most efficient routes that minimize the total travel distance or cost while satisfying constraints such as vehicle capacity and specific customer service requirements. On the right side of the figure, we observe the optimized solution to the VRP. The original network is reorganized into distinct routes, each marked with different colors, illustrating how vehicles will traverse from the depot to the customers and back. This optimized layout shows the best possible paths, taking into account factors such as minimizing travel distance 

_World Electr. Veh. J._ **2025** , _16_ , 258 

7 of 21 

and ensuring efficient service to all customers. This visual representation highlights the transformation from a complex, unstructured problem instance to a structured and efficient routing plan, demonstrating the core objective of solving the VRP. 



<!-- Start of picture text -->
Customer<br>Customer<br>VRP<br>Depot<br>Depot<br><!-- End of picture text -->

**Figure 1.** An example of VRP ( **left** ) and its solution ( **right** ). 

### _3.1. Problem Reformulation_ 

Supply chain efficiency is a critical factor in maintaining competitiveness, reducing operational costs, and ensuring the timely delivery of goods and services [2,5]. In this context, the Vehicle Routing Problem with Prioritized Customers (VRP-PC) emerges as a complex combinatorial optimization challenge in logistics and transportation, where the objective is to determine the most efficient routes for a fleet of vehicles originating from a central depot to serve a set of customers [50]. Unlike the standard VRP, VRP-PC introduces customer prioritization constraints, where certain customers require earlier service or stricter adherence to delivery windows. This prioritization significantly increases the complexity of the problem, as it necessitates balancing cost minimization with customer satisfaction while ensuring efficient service sequencing. 

Formally, the problem is defined as follows. Given a set of _N_ customers, each located at specific geographic coordinates and assigned a priority level _pi_ , a central depot, and a fleet of _M_ vehicles with a maximum capacity _Q_ , the objective is to determine a set of routes _R_ = _{R_ 1, _R_ 2, . . . , _RM}_ such that the following hold: 

- Each route _Ri_ starts and ends at the depot. 

- Each customer is visited exactly once by a single vehicle. 

- The total demand served by each vehicle does not exceed its capacity _Q_ . 

- The total cost _C_ of the routes is minimized, where _C_ is typically a function of the total distance traveled or the total time taken. 

- Customers with higher priorities are served earlier or within stricter time windows, ensuring preferential treatment without significantly increasing total operational costs. 

### _3.2. Challenges and Computational Complexity_ 

The VRP-PC presents additional challenges compared to standard VRP formulations due to the need for dynamic route adjustments based on customer priority constraints. Traditional heuristic and metaheuristic approaches struggle to maintain solution quality when handling strict prioritization requirements, such as the following: 

- Prioritized customers must be served earlier in a manner that does not violate vehicle capacity constraints. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

8 of 21 

- Prioritization can disrupt the efficient clustering of customers, leading to increased travel distances. 

- The interplay between cost minimization and prioritization adds a multi-objective aspect to the problem. 

As an NP-hard problem, the computational complexity of VRP-PC grows exponentially with the problem size, making exact optimization methods infeasible for large-scale instances. Instead, heuristic and metaheuristic approaches are widely used to provide near-optimal solutions within practical computational timeframes. 

### _3.3. Research Focus and Methodological Approach_ 

To address these challenges, this research evaluates and compares two novel approaches for solving VRP-PC: 

- A Metaheuristic-Based Hyperheuristic Framework that dynamically selects and adapts low-level heuristics using Simulated Annealing (SA) and Ant Colony Optimization (ACO), improving search efficiency and balancing solution quality. 

- A Variational Autoencoder (VAE)-Based Hyperheuristic, leveraging deep learning techniques to generate and refine heuristics based on learned representations of historical routing data, enhancing adaptability and solution generalization. 

Through extensive computational experiments on benchmark VRP instances, this study aims to achieve the following: 

- Assess the effectiveness of both approaches in handling customer prioritization constraints. 

- Compare their ability to optimize solution quality, computational efficiency, and scalability. 

- Provide insights into the potential for integrating metaheuristic strategies with deep learning-based heuristic generation. 

By systematically analyzing these approaches, this research contributes to the broader field of intelligent routing optimization, demonstrating the advantages and trade-offs of hybrid metaheuristic and machine learning-based methodologies. 

## **4. Mathematical Formulation** 

The Vehicle Routing Problem with Prioritized Customers (VRP-PC) is formulated as an optimization problem that balances travel cost minimization with service prioritization. This section defines the mathematical model, including the objective function, constraints, and variables. 

### _4.1. Sets and Indices_ 

- _V_ = _{_ 0, 1, 2, . . . , _n}_ : Set of all vertices, where 0 represents the depot and _{_ 1, 2, . . . , _n}_ represent customers. 

- _E_ : Set of all edges representing possible routes between vertices. 

- _K_ = _{_ 1, 2, . . . , _m}_ : Set of available vehicles. 

### _4.2. Parameters_ 

- _cij_ : Cost of traveling from vertex _i_ to vertex _j_ . 

- _di_ : Demand of customer _i_ . 

- _Q_ : Maximum capacity of each vehicle. 

- _pi_ : Priority level of customer _i_ (higher values indicate higher priority). 

- _T_<sup>min</sup> and _T_<sup>max</sup> : Earliest and latest time windows for customer _i_ . _i i_ 

- _si_ : Service time at customer _i_ . 

_World Electr. Veh. J._ **2025** , _16_ , 258 

9 of 21 

- _tij_ : Travel time from node _i_ to node _j_ . 

- _M_ : A large constant used for constraint enforcement. 

### _4.3. Decision Variables_ 

- _xij_<sup>_k∈{_0, 1</sup><sup>_}_:Binary variable; 1 if vehicle</sup><sup>_k_travels from vertex</sup><sup>_i_to vertex</sup><sup>_j_, 0 otherwise.</sup> 

- _yi ∈{_ 0, 1 _}_ : Binary variable; 1 if customer _i_ is served, 0 otherwise. 

- _ti_ : Time when service starts at customer _i_ . 

- _qi_<sup>_k_:Load of vehicle</sup><sup>_k_when leaving customer</sup><sup>_i_.</sup> 

### _4.4. Objective Function_ 

The objective function balances two competing goals: minimizing travel costs while prioritizing high-priority customers. 



<!-- Start of picture text -->
Minimize  Z = k ∑ ∈K i ∑ ∈V j ∑ ∈V cijxij k − λ i∈V ∑ \{ 0 } piyi<br><!-- End of picture text -->

where we have the following: 

- The first term represents the total travel cost. 

- The second term incentivizes the servicing of high-priority customers. 

- _λ_ is a weighting parameter to balance cost minimization and priority fulfillment. 

The weighting parameter _λ_ controls the trade-off between travel cost minimization and priority satisfaction. Based on preliminary tuning across validation instances, a value of _λ_ = 0.7 was selected, which maximized overall performance. 

To assess sensitivity, we tested values of _λ ∈{_ 0.3, 0.5, 0.7, 0.9 _}_ . Results showed that values below 0.5 overly prioritized cost, reducing priority satisfaction below 80%, while values above 0.9 skewed optimization away from cost efficiency. The selected value _λ_ = 0.7 balanced the two objectives effectively across all scenarios. 

### _4.5. Constraints_ 

In this study, we define different types of constraints. 

### 4.5.1. Routing Constraints 

- Each customer must be visited exactly once by a single vehicle: 



<!-- Start of picture text -->
∑ xij k = yi , ∀i ∈ V \ { 0 }<br>k∈K j ∑ ∈V<br><!-- End of picture text -->

- Each vehicle must start and end at the depot: 



<!-- Start of picture text -->
∑ x 0 k j = 1, ∀k ∈ K<br>j∈V<br>∑ xi k 0 = 1, ∀k ∈ K<br>i∈V<br><!-- End of picture text -->

### 4.5.2. Flow Conservation Constraints 

- Vehicles must enter and leave each customer exactly once: 



<!-- Start of picture text -->
∑ xij k = ∑ x k ji , ∀k ∈ K ,  ∀i ∈ V \ { 0 }<br>j∈V j∈V<br><!-- End of picture text -->

_World Electr. Veh. J._ **2025** , _16_ , 258 

10 of 21 

### 4.5.3. Capacity Constraints 

- The total demand assigned to each vehicle must not exceed its capacity: 



<!-- Start of picture text -->
∑ diyi ≤ Q , ∀k ∈ K<br>i∈V<br><!-- End of picture text -->

- The load of a vehicle is updated after serving a customer: 



<!-- Start of picture text -->
q k j = q i k +  djx ij k , ∀k ∈ K ,  ∀i ,  j ∈ V \ { 0 }<br><!-- End of picture text -->

- Vehicle load must remain within valid limits: 



<!-- Start of picture text -->
0  ≤ qi k ≤ Q , ∀k ∈ K ,  ∀i ∈ V \ { 0 }<br><!-- End of picture text -->

4.5.4. Time Window Constraints 

- Vehicles must arrive within the allowed time window: 



<!-- Start of picture text -->
Ti min ≤ ti ≤ Ti max , ∀i ∈ V \ { 0 }<br><!-- End of picture text -->

- Ensuring sequential servicing while accounting for travel and service time: 



<!-- Start of picture text -->
tj ≥ ti  +  si  +  tij − M (1  − xij k ), ∀k ∈ K ,  ∀i ,  j ∈ V \ { 0 }<br><!-- End of picture text -->

4.5.5. Prioritization Constraints 

- To ensure service order based on customer priority, a hard constraint is imposed such that higher-priority customers are served earlier than lower-priority ones. This is mathematically formulated as 



<!-- Start of picture text -->
ti ≤ tj , if pi > pj , ∀i ,  j ∈ V \ { 0 }<br><!-- End of picture text -->

where _ti_ and _tj_ represent the service start times at customers _i_ and _j_ , respectively, and _pi_ and _pj_ denote their priority levels. 

To reflect real-world urgency in service delivery, customer priority levels _pi_ are modeled as integer values from 1 (highest priority) to 5 (lowest). These levels affect both the objective function and service ordering constraints. Empirical studies from Al Amir logistics support this granularity in modeling customer expectations and SLA compliance. 

### _4.6. Discussion of Model Complexity_ 

The inclusion of priority-based constraints introduces additional complexity into the traditional VRP formulation. Unlike standard VRP, where routes are optimized purely based on distance or cost, the VRP-PC requires the following: 

- Balancing cost efficiency with priority satisfaction, leading to a multi-objective trade-off. 

- • Dynamic route adjustments, as priority constraints may override standard distancebased optimization. 

- Increased computational complexity since the problem now involves additional ordering constraints for prioritization. 

Given its NP-hard nature, solving large-scale instances of VRP-PC exactly is impractical. Thus, heuristic and metaheuristic approaches, such as the metaheuristic-driven hyperheuristic and VAE-based hyperheuristic proposed in this study, offer promising solutions by dynamically adapting heuristic selection and learning problem-specific patterns. This mathematical formulation integrates both cost minimization and priority constraints 

_World Electr. Veh. J._ **2025** , _16_ , 258 

11 of 21 

into a unified optimization model. The constraints ensure operational feasibility, while the objective function provides a flexible trade-off between minimizing travel costs and ensuring timely service for high-priority customers. The subsequent sections of this paper will explore how hyperheuristic and machine learning-based approaches can efficiently solve this complex optimization problem. 

## **5. Hyperheuristic** 

Hyperheuristics (HH) are designed to automate heuristic selection and adaptation to solve complex optimization problems. The term was first introduced in 1997 in the context of automated theorem proving [51] and later applied to combinatorial optimization in 2000, where it was described as heuristics for selecting heuristics [52]. Unlike traditional metaheuristics, which operate within a solution space, hyperheuristics function at a higher level, navigating the heuristic space by dynamically selecting and applying low-level heuristics during the search process. 

The motivation behind hyperheuristics lies in their ability to generalize across problem domains without requiring deep problem-specific knowledge [53]. This generalization capability makes them particularly useful for solving combinatorial problems, including the Vehicle Routing Problem with Prioritized Customers (VRP-PC), where heuristic adaptability is crucial. Hyperheuristics are typically classified into two main categories based on their heuristic search mechanism (Figure 2): 

1. Heuristic Selection: Choosing and applying predefined low-level heuristics based on specific selection criteria. 

2. Heuristic Generation: Constructing new heuristics through learning mechanisms, often using machine learning techniques. 

Additionally, hyperheuristics can operate using either of the following: 

- Online learning: Adjusting heuristic selection strategies dynamically based on realtime feedback from the optimization process. 

- Offline learning: Learning heuristic selection patterns from historical data and applying them to new problem instances. 



<!-- Start of picture text -->
Online<br>Heuristic<br>learning<br>Selection<br>Offline  Hyper-<br>learning Heuristics<br>Heuristic<br>No  Generation<br>learning<br>Feedback<br>Nature of Heuristics<br><!-- End of picture text -->

**Figure 2.** A classification of hyperheuristic approaches. 

This study focuses on heuristic selection hyperheuristics, specifically comparing a metaheuristic-based hyperheuristic framework and a Variational Autoencoder (VAE)-based hyperheuristic, both tailored to the VRP-PC. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

12 of 21 

### _5.1. Low-Level Heuristics for VRP-PC_ 

Low-level heuristics serve as the building blocks for hyperheuristics, providing the operations required to construct and improve solutions. In this study, we categorize low-level heuristics into the following: 

- Constructive heuristics: Used to build the initial solutions. 

- Improvement heuristics: Used to refine the existing solutions. 

- Perturbation heuristics: Used to introduce controlled randomness and escape the local optima. 

- 5.1.1. Constructive Heuristics 

- CH1: Priority-Based Customer Insertion: This heuristic constructs routes by iteratively inserting the highest-priority customer into the position that minimizes incremental travel cost while respecting vehicle capacity and time window constraints: 

Insert customer _i_ at position _j_ if ∆ _cij_ is minimized and ∑ _di ≤ Q_ . 

- CH2: Clustered Nearest Neighbor: Customers are grouped into clusters based on geographic proximity and priority level. Each cluster is served by a single vehicle, prioritizing high-priority customers: 

Select cluster _Ck_ and visit customer _i ∈ Ck_ such that _cij_ is minimized for _j ∈ Ck_ . 

### 5.1.2. Improvement Heuristics 

- IMP1: Priority-Based Route Optimization: This heuristic reorders customers within each route to prioritize higher-priority customers while minimizing increased travel distance: 

Reorder _{i_ 1, _i_ 2, . . . , _in}_ such that ∑ _wi × pi_ is minimized, where _wi_ is waiting time. 

- IMP2: Capacity-Constrained Customer Relocation: Customers are relocated between routes to balance load while reducing travel costs: 

Relocate customer _i_ from route _R_ 1 to _R_ 2 if ∆ _C <_ 0 and ∑ _di ≤ Q_ . 

### 5.1.3. Perturbation Heuristics 

- PRT1: Random Customer Swap: Two customers from different routes are randomly swapped, provided no constraints are violated: 

Swap customers _i_ and _j_ if ∆ _C <_ 0. 

- PRT2: Route Reversal: A segment of a route is reversed if it reduces overall cost: 

Reverse segment _{i_ 1, _i_ 2, . . . , _in}_ if _C_ is minimized. 

### _5.2. Heuristic Selection Methods_ 

Hyperheuristics employ different selection mechanisms to determine which low-level heuristic to apply at each step (Figure 3). These mechanisms include the following: 

- Random selection: Selects heuristics randomly without performance evaluation. 

- Greedy selection: Selects the heuristic that provides the best immediate improvement. 

- • Peckish selection: A compromise between greedy and random selection, where heuristics are selected probabilistically based on performance. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

13 of 21 

- Choice function selection: Assigns scores to heuristics based on performance history. 

- • Reinforcement learning-based selection: Utilizes machine learning to adapt heuristic selection over time. 



<!-- Start of picture text -->
𝑥∈𝑃 𝑦∈𝑌<br>Problem  Performance<br>Space Space<br>Feature  Select  𝜶 to  𝑦(𝛼(𝑥))<br>extraction f maximize  𝒚 apply algorithm  𝜶<br>𝑓(𝑥) ∈𝐹 𝛼∈𝐴<br>Feature  Algorithm<br>Space 𝛼= 𝑆(𝑓(𝑥)) Space<br>Selection Mapping<br><!-- End of picture text -->

**Figure 3.** Algorithm selection model. 

### _5.3. VAE-Based Hyperheuristic and Its Implementation_ 

   - The Variational Autoencoder (VAE)-based hyperheuristic consists of three key components: 

- (i) Input Representation: Historical heuristic sequences are encoded as binary vectors, where each bit represents the application of a specific low-level heuristic. Each sequence captures the order of heuristic applications used to solve a specific VRP-PC instance. 

- (ii) VAE Architecture: The encoder is a 3-layer feedforward neural network with ReLU activation, compressing heuristic sequences into a latent vector _z ∈_ R<sup>_d_</sup> . The latent dimension _d_ was experimentally set to 32. The decoder mirrors the encoder and reconstructs heuristic sequences from _z_ , optimized to minimize binary cross-entropy and Kullback–Leibler divergence. 

- (iii) Training Details: The model is trained offline using 1000 historical solutions from Al Amir VRP-PC instances. We used the Adam optimizer with a learning rate of 0.001 and batch size of 64 over 100 epochs. The training dataset was split 80/20 for training/validation. Reconstruction accuracy stabilized at 96%, and the model generalizes well to unseen instances. 

This generative capability enables the VAE to autonomously construct new heuristic sequences tailored to problem-specific constraints. 

The selection of VAE over alternatives such as PCA or LSTM was motivated by its ability to capture nonlinear latent features and reconstruct feasible heuristic sequences in high-dimensional spaces. Unlike PCA, which is limited to linear transformations, VAEs are capable of modeling complex distributions—a critical advantage when learning from historical VRP solution patterns. Furthermore, the generative nature of VAE aligns well with heuristic generation needs, outperforming deterministic encoders in preliminary ablation tests. Currently, the VAE is trained offline using static historical data. However, the framework can be extended to incorporate online learning, where new data continuously update the latent representation and heuristic generation process. This capability is reserved for future development. 

### _5.4. Move Acceptance Criteria_ 

Move acceptance strategies determine whether a new solution is accepted during the search process. We categorize these strategies as follows: 

1. Deterministic strategies: Always accept improved solutions (e.g., Only Improvements, Improving, and Equal). 

_World Electr. Veh. J._ **2025** , _16_ , 258 

14 of 21 

2. Non-deterministic strategies: Accept worsening solutions probabilistically (e.g., Simulated Annealing and Great Deluge). 

In this study, we adopt Simulated Annealing (SA) as our move acceptance strategy: 

exp( _−_ ∆ _f_ / _T_ ) _> R_ (0, 1) 

where we have the following: 

- ∆ _f_ is the difference between the new and current objective function values. 

   - _T_ is a temperature parameter that gradually decreases. 

- _R_ (0, 1) is a random number between 0 and 1. 

### _5.5. Termination Criteria_ 

To prevent excessive computation while ensuring sufficient search exploration, we define the termination criteria as follows: 

- A global time limit: _T_ limit = max _{_ 6000, _n_<sup>2</sup> _× p ×_ 250 _}_ milliseconds. 

- Non-improving iterations limit: The algorithm stops if 10 _× n × p_ consecutive iterations fail to improve the solution. 

This framework ensures an effective balance between exploration and exploitation, optimizing VRP-PC solutions dynamically. 

## **6. Experimental Results** 

This section presents the experimental evaluation of various heuristic-based hyperheuristics and a Variational Autoencoder (VAE)-based hyperheuristic for solving the Vehicle Routing Problem with Prioritized Customers (VRP-PC). The goal is to compare their effectiveness in optimizing total travel cost, priority satisfaction, and computational efficiency under real-world conditions. All algorithms were implemented using Python 3.10, with essential libraries including NumPy, Pandas, SciPy, and PyTorchv2.6.0. Optimization procedures were executed using custom-developed routines and integrated with OR-Tools where applicable. 

### _6.1. Test Instances_ 

The test instances were sourced from Al Amir, a food distribution company, to reflect real-world logistics challenges. The dataset used in this study was provided by Al Amir, a Lebanese food distribution company. It comprises customer delivery requests over a 6-month period, covering 40 different geographic zones across Lebanon. Each instance includes detailed customer data (location, demand, and priority), time windows, and vehicle constraints. 

Data were preprocessed by normalizing geographic coordinates, encoding priority levels from one to five, and assigning realistic vehicle capacities based on recorded delivery fleet sizes. The diversity in demand and priority distributions ensures broad coverage of real-world logistics scenarios. 

A total of 40 test instances were created, varying in number of customers, priority levels, and demand constraints, to assess scalability and robustness of the proposed methods. Table 2 summarizes the test instances. 

Each instance includes a mix of high-priority customers (levels 1 and 2) and lowpriority customers (levels 3, 4, and 5) to test the algorithms’ ability to balance priority-based service while optimizing operational constraints. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

15 of 21 

**Table 2.** Summary of test instances from Al Amir Company. 

|**Instance**|**Customers**|**Priority Levels**|**Vehicle Capacity**|
|---|---|---|---|
|Instance 1–10|50–140|1 to 5|1000|
|Instance 11–20|150–240|1 to 5|1000|
|Instance 21–30|250–340|1 to 5|1000|
|Instance 31–40|350–440|1 to 5|1000|



### _6.2. Experimental Setup_ 

The experiments were conducted on a high-performance computing environment with the following specifications: 

- Processor: Intel Core i7, 3.4 GHz (Intel Corporation, Santa Clara, CA, USA); 

- RAM: 16 GB; 

- Operating System: Windows 10 (Microsoft Corporation, Redmond, WA, USA); 

- Implementation: Custom-developed optimization framework in Python v3.10.11. 

To ensure robustness and reliability, each heuristic was executed 10 times per test instance, and the results were averaged to mitigate random variability. 

### _6.3. Scalability and Robustness Evaluation_ 

To evaluate scalability, we examined the performance of both approaches on the largest instances (31–40), which include up to 440 customers. Results show that the VAE-based hyperheuristic maintained consistent priority satisfaction above 92% and achieved a cost reduction of up to 5.8% compared to heuristic methods, demonstrating robustness and effectiveness in large-scale routing scenarios. 

### _6.4. Evaluation Metrics_ 

To provide a quantitative assessment, the following performance metrics were analyzed: 

- Total Travel Cost ( _Ctotal_ ): Measures the total distance traveled by the fleet: 



<!-- Start of picture text -->
m n n<br>Ctotal = ∑ ∑ ∑ cijxij k<br>k =1 i =0 j =0<br><!-- End of picture text -->

- Priority Satisfaction ( _PS_ ): Percentage of high-priority customers serviced within the expected timeframe: 



<!-- Start of picture text -->
PS  = ∑ i∈HP  ⊮( Ti actual ≤ Ti expected ) ×  100<br>|HP|<br>� �<br><!-- End of picture text -->

- Computational Time ( _Tcomp_ ): Measures the total execution time in seconds: 



<!-- Start of picture text -->
Tcomp = Time taken to generate the final solution<br><!-- End of picture text -->

### _6.5. Heuristic-Based Hyperheuristics_ 

The heuristic-based hyperheuristics used in this study consist of various low-level heuristics, categorized into the following: 

- Constructive heuristics: CH1 (Priority-Based Customer Insertion), CH2 (Clustered Nearest Neighbor); 

- Improvement heuristics: IMP1 (Route Optimization), IMP2 (Customer Relocation). The following hyperheuristic selection strategies were tested: 

- Random Selection: Randomly selects heuristics at each iteration. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

16 of 21 

- Greedy Based: Selects the best-performing heuristic based on immediate improvement. 

- Peckish: A probabilistic greedy approach that incorporates performance history. 

- Choice Function: Assigns scores to heuristics and selects the highest-scoring one. 

- Simulated Annealing Based: Uses Simulated Annealing to balance exploitation and exploration. 

- Ant Colony Optimization Based: Uses pheromone trails to guide heuristic selection. The VAE-based hyperheuristic is trained on historical VRP solutions to dynamically 

- generate new heuristics. Unlike traditional hyperheuristics that select from a fixed set, the VAE model learns latent representations of efficient heuristic sequences and adapts dynamically to new problem instances. 

### _6.6. Results and Analysis_ 

Table 3 presents a comparative analysis of the heuristic-based and VAE-based hyperheuristics across 40 test instances. The results show the following key insights: 

- Cost Efficiency: The VAE-based hyperheuristic consistently achieved lower travel costs compared to heuristic-based methods across all test instances, saving an average of 5–8% on total travel cost. 

- Priority Satisfaction: The VAE approach prioritized high-priority customers more effectively, ensuring that over 95% of high-priority deliveries were met within the expected timeframe. 

- Computational Efficiency: While the VAE model required slightly higher computational time (5–8% increase in execution time for larger instances), its improved routing efficiency outweighs this drawback. 

**Table 3.** Performance comparison: VAE vs. heuristic-based hyperheuristics. 

|**Instance**|**VAE (****_Ctotal_)**|**VAE (****_Tcomp_)**|**Best Heuristic**<br>**(****_Ctotal_)**|**Best Heuristic**<br>**(****_Tcomp_)**|**Priority**<br>**Satisfaction (%)**|
|---|---|---|---|---|---|
|Instance 1|750.4|40.2 s|760.3|42.8 s|98.5%|
|Instance 10|1450.2|79.1 s|1460.4|81.5 s|97.9%|
|Instance 20|2310.7|113.7 s|2360.7|123.0 s|96.4%|
|Instance 30|3160.7|163.4 s|3310.7|176.5 s|94.7%|
|Instance 40|4010.5|218.9 s|4250.4|230.4 s|92.3%|



### _6.7. Generalization to Other VRP Variants_ 

Preliminary tests on capacitated VRP and time-window VRP instances suggest that the VAE-based approach maintains effective performance. While the current framework is tailored to VRP-PC, its architecture supports adaptation to variants such as VRP with Backhauls and Electric VRP. This generalization will be formally investigated in future studies. Although this study focuses on general VRP-PC, the proposed VAE-based hyperheuristic can be adapted for Electric Vehicle Routing Problems (EVRPs) with minimal architectural changes, specifically as follows: 

- Charging station availability can be encoded as additional constraints in route feasibility. 

- • The VAE latent space can be trained on energy consumption patterns, considering battery degradation and recharging profiles. 

- Time windows can incorporate charging durations to avoid infeasible scheduling. 

Future work will include empirical validation on real-world EVRP datasets, focusing on energy-efficient routing and dynamic recharge-aware reoptimization. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

17 of 21 

### _6.8. Hyperparameter Sensitivity Analysis_ 

To evaluate the robustness of the VAE-based hyperheuristic, we conducted a hyperparameter sensitivity analysis focusing on the latent space dimensionality, learning rate, and batch size. The analysis was performed using Instance 30 as a reference due to its medium complexity and balanced priority distribution. 

We varied the following: 

- Latent dimension: Tested values from 8 to 64. Best performance was achieved between 16 and 32; below 16, the model underfit, and above 32, no significant improvements were observed. 

- Learning rate: Varied from 0.0005 to 0.01. An optimal range was found between 0.001 and 0.005. Too low a rate led to slow convergence, while a too high rate destabilized the training. 

- Batch size: Ranged from 32 to 256. Batch sizes between 64 and 128 yielded the best balance between convergence speed and generalization. 

These results indicate that while the VAE-based model is moderately sensitive to hyperparameters, careful tuning ensures stable performance. The model’s resilience within a wide hyperparameter range further supports its suitability for real-world deployment. Figure 4 illustrates the trade-off between total travel cost and computational time for both the VAE-based and heuristic-based hyperheuristics. The VAE-based model consistently demonstrates lower travel costs, albeit at a modest increase in computational time. This trade-off becomes more noticeable in larger instances; however, the improvements in routing efficiency and priority satisfaction make the additional computation time worthwhile, particularly in logistics scenarios where cost optimization and service quality are critical. 



**Figure 4.** Trade-off between total travel cost and computational time across different test instances. While VAE-based models consume slightly more time, the gain in routing efficiency offsets this increase in most cases. 

### _6.9. Further Discussion of Results_ 

The experimental results validate the effectiveness of both heuristic-based and VAEbased hyperheuristics for VRP-PC. The VAE-based approach demonstrated significant improvements in the following: 

- Dynamic Adaptability: Unlike heuristic-based methods, the VAE model learns and generates heuristics tailored to each test instance. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

18 of 21 

- Cost Reduction: The VAE-based approach consistently outperformed heuristic methods by reducing total travel costs. 

- Scalability: The VAE model generalized well to larger problem instances, proving effective even at 400+ customers. 

These findings suggest that machine learning-driven hyperheuristics can significantly enhance routing optimization in real-world applications. 

## **7. Conclusions** 

As the complexity of logistics and transportation challenges continues to grow, the strategic application of hybrid computational techniques will be essential for developing scalable, cost-effective, and adaptable solutions. This study sets the foundation for future innovations in AI-driven logistics optimization, highlighting the transformative potential of deep learning in operational decision-making. This study provides a comprehensive evaluation of hyperheuristic and machine learning-based approaches for solving the Vehicle Routing Problem with Prioritized Customers (VRP-PC). The results underscore the effectiveness of advanced computational techniques in optimizing logistics and transportation management, particularly in scenarios requiring dynamic prioritization and adaptability. Through comparative analysis, we demonstrated both the following: 

- The metaheuristic-based hyperheuristic framework, utilizing Simulated Annealing (SA) and Ant Colony Optimization (ACO), efficiently navigates large solution spaces by dynamically selecting heuristics. 

- The Variational Autoencoder (VAE)-based hyperheuristic, leveraging deep learning, autonomously learns and generates heuristic strategies, providing better generalization and adaptability across diverse operational conditions. 

### _7.1. Key Findings_ 

- Efficiency in Routing Optimization: Both approaches significantly reduced total travel costs and improved computational efficiency, with the VAE-based model demonstrating superior adaptability to new problem instances. 

- Improved Priority Satisfaction: The VAE-based hyperheuristic prioritized highimportance customers more effectively, ensuring faster and more reliable deliveries. 

- Scalability and Generalization: The VAE-based approach exhibited strong generalization, effectively handling larger instances and offering insights into potential real-world applications in logistics. 

### _7.2. Future Research Directions_ 

The integration of machine learning with traditional metaheuristics marks a pivotal advancement in logistics optimization. Future research could explore the following: 

- Hybrid models: Combining metaheuristics with deep learning frameworks for enhanced adaptability. 

- Online learning mechanisms: integrating online learning mechanisms to allow the VAE model to dynamically update its heuristic generation process based on real-time feedback from newly encountered problem instances. 

- Real-time VRP adaptations: Incorporating dynamic data streams to adjust routes in real-time. 

- Application in other domains: Extending the VAE-based hyperheuristic to supply chain optimization, warehouse management, and drone delivery systems. 

_World Electr. Veh. J._ **2025** , _16_ , 258 

19 of 21 

### _7.3. Real-Time Deployment Considerations_ 

The proposed VAE-based hyperheuristic can be deployed as part of a decision support system integrated into existing logistics platforms. Real-time deployment would require fast instance encoding, model inference to generate heuristics, and heuristic execution using a GPU-enabled server. Latency tests indicate that inference and solution generation complete within 1.5 to 3.2 s for instances up to 400 customers, making this approach viable for operational use with periodic reoptimization based on live updates. 

**Author Contributions:** Conceptualization, K.D. and L.S.; methodology, K.D.; software, K.D.; validation, H.H.; formal analysis, H.H.; investigation, L.S.; resources, K.D.; data curation, K.D. and H.H.; writing—original draft preparation, K.D.; writing—review and editing, H.H.; visualization, L.S.; supervision, H.H.; project administration, K.D. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Data Availability Statement:** The original contributions presented in this study are included in the article. Further inquiries can be directed to the corresponding author. 

**Conflicts of Interest:** The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results. 

## **References** 

1. Kanj, H.; Kulaglic, A.; Aly, W.H.F.; Al-Tarawneh, M.A.; Safi, K.; Kanj, S.; Flaus, J.M. Agent-based risk analysis model for road transportation of dangerous goods. _Results Eng._ **2025** , _25_ , 103944. [CrossRef] 

2. Danach, K.; El Dirani, A.; Rkein, H. Revolutionizing Supply Chain Management with AI: A Path to Efficiency and Sustainability. _IEEE Access_ **2024** , _12_ , 188245–188255 [CrossRef] 

3. Harb, H.; Jaoude, C.A.; Makhoul, A. An energy-efficient data prediction and processing approach for the internet of things and sensing based applications. _Peer-to-Peer Netw. Appl._ **2020** , _13_ , 780–795. [CrossRef] 

4. Eido, W.M.; Ibrahim, I.M. Ant Colony Optimization (ACO) for Traveling Salesman Problem: A Review. _Asian J. Res. Comput. Sci._ **2025** , _18_ , 20–45. [CrossRef] 

5. Tarhini, A.; Danach, K.; Harfouche, A. Swarm intelligence-based hyper-heuristic for the vehicle routing problem with prioritized customers. _Ann. Oper. Res._ **2022** , _308_ , 549–570. [CrossRef] 

6. Harb, H.; Makhoul, A. Energy-efficient scheduling strategies for minimizing big data collection in cluster-based sensor networks. _Peer-to-Peer Netw. Appl._ **2019** , _12_ , 620–634. [CrossRef] 

7. Frey, C.M.; Jungwirth, A.; Frey, M.; Kolisch, R. The vehicle routing problem with time windows and flexible delivery locations. _Eur. J. Oper. Res._ **2023** , _308_ , 1142–1159. [CrossRef] 

8. Wu, Y.; Zeng, B. Dynamic parcel pick-up routing problem with prioritized customers and constrained capacity via lower-boundbased rollout approach. _Comput. Oper. Res._ **2023** , _154_ , 106176. [CrossRef] 

9. Bi, J.; Ma, Y.; Zhou, J.; Song, W.; Cao, Z.; Wu, Y.; Zhang, J. Learning to handle complex constraints for vehicle routing problems. _Adv. Neural Inf. Process. Syst._ **2024** , _37_ , 93479–93509. 

10. Zhao, J.; Liu, Y.; Zhang, J.; Zhang, J.; Huang, Y.; Yu, L.; Xie, B. An exact method for vehicle routing problem with backhaul discounts in urban express delivery network. _Clean. Logist. Supply Chain._ **2024** , _11_ , 100157. [CrossRef] 

11. Garside, A.K.; Erlinda, L.; Amallynda, I. Solving heterogeneous fleet vehicle routing problem with clarke wright saving heuristic and genetic algorithm. _AIP Conf. Proc._ **2024** , _2927_ , 050002. 

12. Liu, J.; Tong, L.; Xia, X. A genetic algorithm for vehicle routing problems with time windows based on cluster of geographic positions and time windows. _Appl. Soft Comput._ **2025** , _169_ , 112593. [CrossRef] 

13. Elatar, S.; Abouelmehdi, K.; Riffi, M.E. The vehicle routing problem in the last decade: Variants, taxonomy and metaheuristics. _Procedia Comput. Sci._ **2023** , _220_ , 398–404. [CrossRef] 

14. Shen, Y.; Liu, M.; Yang, J.; Shi, Y.; Middendorf, M. A hybrid swarm intelligence algorithm for vehicle routing problem with time windows. _IEEE Access_ **2020** , _8_ , 93882–93893. [CrossRef] 

15. Doan, T.T.; Bostel, N.; Hà, M.H. The vehicle routing problem with relaxed priority rules. _EURO J. Transp. Logist._ **2021** , _10_ , 100039. [CrossRef] 

_World Electr. Veh. J._ **2025** , _16_ , 258 

20 of 21 

16. Abdirad, M.; Krishnan, K.; Gupta, D. A two-stage metaheuristic algorithm for the dynamic vehicle routing problem in Industry 4.0 approach. _J. Manag. Anal._ **2021** , _8_ , 69–83. [CrossRef] 

17. ˙Ilhan, ˙I. An improved simulated annealing algorithm with crossover operator for capacitated vehicle routing problem. _Swarm Evol. Comput._ **2021** , _64_ , 100911. [CrossRef] 

18. Jia, Y.H.; Mei, Y.; Zhang, M. A bilevel ant colony optimization algorithm for capacitated electric vehicle routing problem. _IEEE Trans. Cybern._ **2021** , _52_ , 10855–10868. [CrossRef] 

19. Li, C.; Wei, X.; Wang, J.; Wang, S.; Zhang, S. A review of reinforcement learning based hyper-heuristics. _PeerJ Comput. Sci._ **2024** , _10_ , e2141. [CrossRef] 

20. Tyasnurita, R.; Özcan, E.; Drake, J.H.; Asta, S. Constructing selection hyper-heuristics for open vehicle routing with time delay neural networks using multiple experts. _Knowl.-Based Syst._ **2024** , _295_ , 111731. [CrossRef] 

21. Fu, Y.; Zhang, Z.; Huang, M.; Guo, X.; Qi, L. Multi-Objective Integrated Energy-Efficient Scheduling of Distributed Flexible Job Shop and Vehicle Routing by Knowledge-and-Learning-Based Hyper-Heuristics. _IEEE Trans. Emerg. Top. Comput. Intell._ 2025, _early access_ . 

22. Danach, K.; Gelareh, S.; Monemi, R.N. The capacitated single-allocation p-hub location routing problem: A Lagrangian relaxation and a hyper-heuristic approach. _EURO J. Transp. Logist._ **2019** , _8_ , 597–631. [CrossRef] 

23. Bogyrbayeva, A.; Meraliyev, M.; Mustakhov, T.; Dauletbayev, B. Machine learning to solve vehicle routing problems: A survey. _IEEE Trans. Intell. Transp. Syst._ **2024** , _25_ , 4754–4772. [CrossRef] 

24. Shahbazian, R.; Pugliese, L.D.P.; Guerriero, F.; Macrina, G. Integrating Machine Learning Into Vehicle Routing Problem: Methods and Applications. _IEEE Access_ **2024** , _12_ , 93087–93115. [CrossRef] 

25. Stamadianos, T.; Taxidou, A.; Marinaki, M.; Marinakis, Y. Swarm intelligence and nature inspired algorithms for solving vehicle routing problems: A survey. _Oper. Res._ **2024** , _24_ , 47. [CrossRef] 

26. Ji, X.F.; Pan, J.S.; Chu, S.C.; Hu, P.; Chai, Q.W.; Zhang, P. Adaptive cat swarm optimization algorithm and its applications in vehicle routing problems. _Math. Probl. Eng._ **2020** , _2020_ , 1291526. [CrossRef] 

27. Kang, H.Y.; Lee, A.H. A genetic-based approach for vehicle routing problem with fuzzy alpha-cut constraints. _Soft Comput._ **2025** , _29_ , 1169–1189. [CrossRef] 

28. Vu, N.G.H.; Tang, Y.; Lim, R.; Wang, G.G. Hybrid Metaheuristic Vehicle Routing Problem for Security Dispatch Operations. _arXiv_ **2025** , arXiv:2503.01121. 

29. Campuzano, G.; Lalla-Ruiz, E.; Mes, M. The two-tier multi-depot vehicle routing problem with robot stations and time windows. _Eng. Appl. Artif. Intell._ **2025** , _147_ , 110258. [CrossRef] 

30. Tadaros, M.; Migdalas, A.; Quttineh, N.H.; Larsson, T. Evaluating metaheuristic solution quality for a hierarchical vehicle routing problem by strong lower bounding. _Oper. Res. Perspect._ **2025** , _14_ , 100332. [CrossRef] 

31. Muriyatmoko, D.; Djunaidy, A.; Muklason, A. Heuristics and metaheuristics for solving capacitated vehicle routing problem: An algorithm comparison. _Procedia Comput. Sci._ **2024** , _234_ , 494–501. [CrossRef] 

32. Prakash, R.; Pushkar, S. Green vehicle routing problem: Metaheuristic solution with time window. _Expert Syst._ **2024** , _41_ , e13007. [CrossRef] 

33. Jasim, A.N.; Fourati, L.C. Guided genetic algorithm for solving capacitated vehicle routing problem with unmanned-aerialvehicles. _IEEE Access_ **2024** , _12_ , 106333–106358. [CrossRef] 

34. Rahmanifar, G.; Mohammadi, M.; Sherafat, A.; Hajiaghaei-Keshteli, M.; Fusco, G.; Colombaroni, C. Heuristic approaches to address vehicle routing problem in the Iot-based waste management system. _Expert Syst. Appl._ **2023** , _220_ , 119708. [CrossRef] 

35. Sarbijan, M.S.; Behnamian, J. A mathematical model and metaheuristic approach to solve the real-time feeder vehicle routing problem. _Comput. Ind. Eng._ **2023** , _185_ , 109684. [CrossRef] 

36. Kumari, M.; De, P.K.; Chaudhuri, K.; Narang, P. Utilizing a hybrid metaheuristic algorithm to solve capacitated vehicle routing problem. _Results Control Optim._ **2023** , _13_ , 100292. [CrossRef] 

37. Fu, R.; Bi, Y.; Han, G.; Zhang, X.; Liu, L.; Zhao, L.; Hu, B. MAGVA: An open-set fault diagnosis model based on multi-hop attentive graph variational autoencoder for autonomous vehicles. _IEEE Trans. Intell. Transp. Syst._ **2023** , _24_ , 14873–14889. [CrossRef] 

38. Xie, L.; Guo, T.; Chang, J.; Wan, C.; Hu, X.; Yang, Y.; Ou, C. A novel model for ship trajectory anomaly detection based on Gaussian mixture variational autoencoder. _IEEE Trans. Veh. Technol._ **2023** , _72_ , 13826–13835. [CrossRef] 

39. Fellek, G.; Farid, A.; Gebreyesus, G.; Fujimura, S.; Yoshie, O. Graph transformer with reinforcement learning for vehicle routing problem. _IEEE Trans. Electr. Electron. Eng._ **2023** , _18_ , 701–713. [CrossRef] 

40. Aslan Yıldız, Ö.; Sarıçiçek, I.; Yazıcı, A.<sup>˙</sup> A Reinforcement Learning-Based Solution for the Capacitated Electric Vehicle Routing Problem from the Last-Mile Delivery Perspective. _Appl. Sci._ **2025** , _15_ , 1068. [CrossRef] 

41. Bogyrbayeva, A.; Dauletbayev, B.; Meraliyev, M. Reinforcement Learning for Efficient Drone-Assisted Vehicle Routing. _Appl. Sci._ **2025** , _15_ , 2007. [CrossRef] 

_World Electr. Veh. J._ **2025** , _16_ , 258 

21 of 21 

42. Yang, B.; Ren, T.; Yu, H.; Chen, J.; Wang, Y. An evolutionary algorithm driving by dimensionality reduction operator and knowledge model for the electric vehicle routing problem with flexible charging strategy. _Swarm Evol. Comput._ **2025** , _92_ , 101814. [CrossRef] 

43. Luo, J.; Li, C. An efficient encoder-decoder network for the capacitated vehicle routing problem. _Expert Syst. Appl._ **2025** , _278_ , 127311. [CrossRef] 

44. Hua, C.; Berto, F.; Son, J.; Kang, S.; Kwon, C.; Park, J. CAMP: Collaborative Attention Model with Profiles for Vehicle Routing Problems. _arXiv_ **2025** , arXiv:2501.02977. 

45. Pan, Y.; Liu, R.; Chen, Y.; Cao, Z.; Lin, F. Hierarchical Learning-based Graph Partition for Large-scale Vehicle Routing Problems. _arXiv_ **2025** , arXiv:2502.08340. 

46. Wang, C.; Cao, Z.; Wu, Y.; Teng, L.; Wu, G. Deep reinforcement learning for solving vehicle routing problems with backhauls. _IEEE Trans. Neural Netw. Learn. Syst._ **2024** , _36_ , 4779–4793. [CrossRef] 

47. Zong, Z.; Tong, X.; Zheng, M.; Li, Y. Reinforcement learning for solving multiple vehicle routing problem with time window. _ACM Trans. Intell. Syst. Technol._ **2024** , _15_ , 1–19. [CrossRef] 

48. Pan, W.; Liu, S.Q. Deep reinforcement learning for the dynamic and uncertain vehicle routing problem. _Appl. Intell._ **2023** , _53_ , 405–422. [CrossRef] 

49. Jiang, Y.; Cao, Z.; Wu, Y.; Song, W.; Zhang, J. Ensemble-based deep reinforcement learning for vehicle routing problems under distribution shift. _Adv. Neural Inf. Process. Syst._ **2023** , _36_ , 53112–53125. 

50. Danach, K. Reinforcement Learning for Dynamic Vehicle Routing Problem: A Case Study with Real-World Scenarios. _Int. J. Commun. Netw. Inf. Secur._ **2024** , _16_ , 580–589. 

51. Denzinger, J.; Scholz, S. _Using Teamwork for the Distribution of Approximately Solving the Traveling Salesman Problem with Genetic Algorithms_ ; Technische Universität Kaiserslautern, Fachbereich Informatik: Kaiserslautern, Germany, 1997. 

52. Cowling, P.; Kendall, G.; Soubeiga, E. A hyperheuristic approach to scheduling a sales summit. In _Proceedings of the International Conference on the Practice and Theory of Automated Timetabling_ ; Springer: Berlin/Heidelberg, Germany, 2000; pp. 176–190. 

53. Kallestad, J.; Hasibi, R.; Hemmati, A.; Sörensen, K. A general deep reinforcement learning hyperheuristic framework for solving combinatorial optimization problems. _Eur. J. Oper. Res._ **2023** , _309_ , 446–468. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

