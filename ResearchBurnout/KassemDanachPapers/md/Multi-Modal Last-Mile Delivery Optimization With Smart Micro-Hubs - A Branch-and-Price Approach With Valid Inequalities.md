Received 24 March 2025; revised 7 July 2025; accepted 24 November 2025. Date of publication 5 December 2025; date of current version 8 December 2025. _Digital Object Identifier 10.1109/OJITS.2025.3638659_ 

**Multi-Modal Last-Mile Delivery Optimization With Smart Micro-Hubs: A Branch-and-Price Approach With Valid Inequalities** 

**KASSEM DANACH 1 (Member, IEEE), ALI RAAD2, AND ABBASS NASSER 3 (Senior Member, IEEE)** 

1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon 

2Faculty of Art and Science, Islamic University of Lebanon, Choueifat, Lebanon 

3CIRAME Research Centre, Business School, Holy-Spirit University of Kaslik, Jounieh, Lebanon 

CORRESPONDING AUTHOR: A. NASSER (e-mail: abbass.nasser@usek.edu.lb) 

**ABSTRACT** The rapid growth of e-commerce and urban logistics has intensified the challenges associated with last-mile delivery, necessitating the integration of autonomous delivery vehicles (ADVs), drones, and smart micro-hubs for cost-effective and sustainable operations. This study introduces a novel Multi-Depot Capacitated Vehicle Routing Problem with Time Windows and Multi-Modal Transportation (MD-CVRPTW-MM), where deliveries are dynamically assigned to either ADVs or drones while optimizing hub locations and vehicle routing. The objective is to minimize total operational costs, including transportation, hub activation, and delivery mode selection, while ensuring service-level constraints such as time windows and capacity limits. To efficiently solve this complex combinatorial problem, we propose a mathematical formulation enhanced with valid inequalities for computational efficiency. Furthermore, a Branch-andPrice algorithm is developed, where column generation is employed to iteratively refine delivery routes while enforcing depot assignments and mode selection constraints. The solution approach integrates dual stabilization techniques and path-based heuristics to accelerate convergence. Experimental evaluations on benchmark datasets and real-world logistics scenarios demonstrate the effectiveness of the proposed method in reducing last-mile delivery costs, optimizing fleet utilization, and enhancing service reliability. The results highlight the significance of multi-modal last-mile delivery optimization in improving urban logistics and sustainability. This research contributes a new mathematical model, efficient optimization techniques, and practical insights for intelligent last-mile delivery planning in smart cities. 

**INDEX TERMS** Last-mile delivery, multi-depot vehicle routing problem, autonomous delivery vehicles, drones, smart micro-hubs, mathematical optimization, branch-and-price, valid inequalities. 

## **I. INTRODUCTION** **_A. BACKGROUND_** 

T HE EXPONENTIALicantly impacted globalgrowthlogistics,oflogistics,of e-commerceparticularlyhaslast-milesignif- 

icantly impacted globalgrowthlogistics,oflogistics,of particularlyhaslast-milesignif-last-milesignifdelivery, which accounts for over 50% of total logistics costs [1]. Urban congestion, high demand for same-day deliveries, and sustainability concerns have pushed companies toward integrating multi-modal delivery solutions [2]. Traditional routing models focus on single-mode transportation, often neglecting hybrid solutions that involve 

The review of this article was arranged by Associate Editor Jun Liu. 

autonomous delivery vehicles (ADVs), drones, and microhubs [3]. 

Recent studies emphasize the potential of drone-based last-mile delivery in reducing delivery time and cost, particularly in urban areas with high traffic congestion [4]. However, standalone drone systems face constraints such as limited battery life and payload capacity, necessitating their integration with ground vehicles [5]. Several optimization models have been proposed for routing hybrid fleets, but they lack efficient mathematical formulations and scalable computational methods [6]. 

Moreover, Branch-and-Price methods have been successfully applied to various combinatorial problems, 

⃝c 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

VOLUME 6, 2025 

1596 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1597 

including vehicle routing problems with time windows (VRPTW) [7]. However, their adaptation to multi-modal last-mile logistics is still underexplored. Addressing these gaps requires a robust mathematical framework that integrates fleet coordination, time window constraints, and routing optimization [8]. This paper proposes a comprehensive optimization framework that integrates multi-modal routing with smart micro-hub activation, enhancing both operational efficiency and delivery responsiveness. The framework is tailored for complex urban logistics scenarios involving coordinated use of autonomous delivery vehicles (ADVs) and drones, strategic depot activation decisions, and time-sensitive delivery constraints. 

The key contributions of this work include: 

- _A novel mathematical formulation_ for the _MultiDepot Capacitated Vehicle Routing Problem with Time Windows and Multi-Modal Transportation (MD-CVRPTW-MM)_ , which incorporates depot activation and dual-mode routing decisions. 

- _Introduction of valid inequalities_ to strengthen the formulation and improve computational efficiency. 

- _Development of a Branch-and-Price solution framework_ adapted to this complex problem structure, utilizing column generation and advanced branching strategies to solve large-scale instances. 

- _A rigorous comparative performance benchmark_ against strong baseline methods, including Adaptive Large Neighborhood Search (ALNS), Large Neighborhood Search (LNS), and Google OR-Tools, highlighting the advantages of the proposed method in minimizing cost and delivery time. 

- _Evaluation on benchmark datasets and real-world scenarios,_ demonstrating significant improvements in cost-efficiency, delivery responsiveness, and scalability for intelligent urban logistics. 

## **_B. PROBLEM MOTIVATION & IMPORTANCE_** 

The rapid expansion of e-commerce has placed unprecedented demands on last-mile delivery systems. As urban logistics become increasingly complex, traditional delivery models face challenges related to: 

- _The rapid growth of e-commerce and last-mile logistics challenges._ Increased demand for fast and cost-effective deliveries has led to congestion, high operational costs, and inefficiencies in existing logistics systems. 

- _The need for multi-modal delivery systems._ Autonomous delivery vehicles (ADVs), drones, and smart microhubs offer potential solutions for enhancing last-mile logistics. 

- _The importance of optimizing delivery costs, time efficiency, and sustainability._ Reducing emissions, lowering fuel consumption, and improving service reliability are critical for the future of smart logistics. 

To address these challenges, this section formalizes the multi-modal last-mile delivery problem incorporating depot 

activation, time windows, and dual-mode routing. We extend classical MDVRPTW formulations by introducing dronespecific constraints, hub activation decisions, and binary delivery mode selection variables. This extension allows the model to realistically capture the operational dynamics of urban delivery fleets that combine ground vehicles and drones, supporting both flexibility and sustainability in modern logistics systems. 

## **_C. UNADDRESSED INDUSTRIAL CHALLENGES IN LAST-MILE DELIVERY_** 

While existing models such as the MDVRP, VRPTW, and vehicle-drone hybrids (e.g., TSP-D, VRPD) offer valuable insights, they often fall short of addressing the following realworld challenges faced in industrial-scale last-mile logistics: 

- _Regulatory Constraints on Drone Operations:_ Most existing models assume unconstrained drone use, yet in practice, drone deployment is restricted by no-fly zones, airspace regulations, and line-of-sight mandates, especially in urban areas. 

- _Dynamic Demand Surges:_ E-commerce platforms often experience sudden spikes in delivery demand (e.g., during flash sales or seasonal peaks), which require realtime adaptive routing and scalable micro-hub activation strategies. Traditional static models fail to capture these fluctuations. 

- _Energy and Battery Replenishment Logistics:_ Drones and ADVs have limited battery capacities. Coordinating their recharging/replacement schedules adds a layer of operational complexity rarely modeled in MDVRP variants. 

- _Micro-Hub Congestion and Throughput Limits:_ Unlike classical depot models, smart micro-hubs must account for finite throughput, physical loading capacity, and activation costs that vary based on location and urban density. 

- _Fleet Coordination Across Modes:_ In practice, hybrid fleets require intelligent load balancing between air (drones) and ground (ADVs) vehicles based on time, weight, cost, and delivery urgency – a feature underrepresented in classical literature. 

- _Multi-Criteria Service-Level Constraints:_ Industries are concerned not only with cost but also with strict delivery windows, carbon emissions, and customer satisfaction metrics. This necessitates multi-objective optimization, often lacking in single-cost classical models. 

These practical constraints motivate the need for an integrated, multi-modal delivery optimization model with realistic industrial assumptions, such as the one proposed in this study. 

## **_D. RESEARCH GAP & CHALLENGES_** 

Despite the advances in last-mile logistics, several challenges remain: 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1598 

- _Existing last-mile delivery solutions lack integrated multi-modal approaches._ Most models focus on singlemode delivery, neglecting the potential synergies of ADVs, drones, and micro-hubs. 

- _Need for a rigorous mathematical formulation._ Effective routing under constraints such as time windows, vehicle capacities, and mode selection remains an open research problem. 

- _Scalability issues in existing methods._ Traditional approaches struggle to handle large-scale problem instances due to the combinatorial nature of routing optimization. 

## **II. LITERATURE REVIEW** 

## **_A. LAST-MILE DELIVERY CHALLENGES AND OPTIMIZATION_** 

The rise of e-commerce-driven logistics has intensified challenges related to last-mile delivery, particularly concerning cost efficiency, congestion, and sustainability [1]. Last-mile logistics account for a significant portion of transportation costs, often exceeding 50% of total supply chain expenditures [9]. Additionally, rapid urbanization has led to increased traffic congestion and environmental concerns, necessitating more sustainable and efficient routing strategies [10]. 

Traditional routing models, such as the Vehicle Routing Problem (VRP), the Multi-Depot VRP (MDVRP), and the VRP with Time Windows (VRPTW), have been widely studied in operational research [11], [12]. These models provide structured solutions for optimizing vehicle routes but often struggle with real-world constraints such as dynamic demand fluctuations, multi-modal transportation, and time-sensitive deliveries [13]. Moreover, solving these combinatorial problems at scale requires advanced optimization techniques due to the computational complexity of large instances [14]. 

Recent studies have explored multi-modal last-mile delivery systems, integrating autonomous delivery vehicles (ADVs), electric bikes, and drones to improve logistics efficiency [6], [15]. ADV-based solutions can reduce dependency on human drivers and lower operational costs by minimizing idle time and empty vehicle returns [16]. Meanwhile, drone delivery has emerged as a complementary solution, particularly in high-traffic urban areas and remote locations, where conventional vehicles face infrastructure limitations [4], [17]. 

However, standalone drone delivery remains impractical due to payload constraints, battery limitations, and strict regulatory restrictions [5], [18]. To overcome these challenges, hybrid vehicle-drone coordination models have been proposed, where drones are deployed from mobile depots (ADVs) or strategically located micro-hubs to serve customers more efficiently [3], [19]. Recent studies indicate that hybrid last-mile delivery systems can reduce total delivery time by 20-30% and cut operational costs by up to 40%, making them a promising alternative for urban logistics [20], [21]. 

Furthermore, advancements in dynamic routing algorithms and real-time traffic monitoring are enhancing adaptive last-mile delivery systems [22], [23]. Leveraging machine learning and artificial intelligence (AI)-driven optimization, modern last-mile solutions are capable of predicting demand patterns and adjusting fleet allocation dynamically, reducing service disruptions and improving delivery reliability [24]. 

Overall, last-mile delivery optimization remains a critical challenge in logistics and transportation research, requiring innovative solutions that balance cost efficiency, scalability, and sustainability [1], [10]. 

## **_B. MATHEMATICAL MODELS FOR LAST-MILE OPTIMIZATION_** 

Mathematical formulations of last-mile delivery problems must accommodate multi-depot constraints, heterogeneous fleets, and customer time windows [2]. Traditional models such as the Capacitated Vehicle Routing Problem (CVRP) and its extensions, including the Multi-Depot VRP (MDVRP) and VRP with Time Windows (VRPTW), have been extensively studied in operations research [11], [12]. However, these classical models often fail to capture the full complexity of last-mile logistics, necessitating advanced modifications to handle dynamic routing, stochastic demand, and multiple transportation modes [25]. 

A widely recognized enhancement to last-mile delivery modeling is the micro-hub-based delivery system, which leverages localized depots to streamline urban logistics [8]. Studies suggest that micro-hubs can reduce total delivery costs by up to 30%, significantly improving service reliability in high-density areas [1], [26]. These systems also support hybrid fleet operations, allowing for the flexible allocation of deliveries between trucks, bikes, and drones based on real-time traffic conditions and energy constraints [27]. 

Another emerging optimization challenge involves the integration of drone-truck delivery models, which require sophisticated mathematical formulations to balance energy constraints, minimize route overlap, and comply with airspace regulations [5], [28]. Several models have been proposed to address these challenges, such as the Traveling Salesman Problem with Drones (TSP-D) and Vehicle Routing Problem with Drones (VRPD), which optimize joint vehicle-drone coordination [3], [19]. Recent research suggests that hybrid drone-truck systems can reduce delivery time by 25-40% compared to conventional vehicle-only models while maintaining cost efficiency [20], [21]. 

To further enhance routing efficiency, stochastic and dynamic optimization models have been explored to incorporate uncertainty in demand, delivery time windows, and traffic congestion [22], [23]. AI-driven approaches, such as reinforcement learning-based optimization and predictive analytics, are also gaining traction in real-time last-mile routing adjustments [24], [29]. These approaches allow lastmile logistics systems to dynamically adjust routes based on real-time conditions, reducing service disruptions and improving delivery efficiency. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1599 

Overall, modern last-mile delivery optimization models are evolving beyond traditional VRP formulations, incorporating multi-modal transportation, stochastic demand, and AI-driven decision-making to achieve higher efficiency and sustainability [1], [10]. 

## **_C. COMPARISON WITH RECENT EXACT AND HEURISTIC METHODS IN MULTI-MODAL VRP_** 

Recent studies in multi-modal last-mile delivery have explored a range of solution methods, from classical exact approaches to hybrid metaheuristics [30], [31], [32], [33]. 

## 1) EXACT METHODS 

Branch-and-cut and Benders decomposition have been widely applied to multi-depot and capacitated VRPs [30], [31]. For instance, Li et al. [30] proposed a Benders decomposition for electric vehicle routing with time windows, achieving exact solutions for medium-scale instances. Similarly, Montoya-Torres et al. [31] employed a branch-and-cut algorithm integrated with preprocessing rules for the capacitated VRPD. Compared to these, our approach: 

- Leverages **column generation** within a branch-andprice framework to scale more effectively to large datasets [30]. 

- Introduces **dual stabilization** techniques to improve convergence stability–a common bottleneck in exact decomposition methods [30]. 

- Includes **valid inequalities** tailored for mode selection, micro-hub activation, and drone feasibility, which are not present in prior formulations [31]. 

## 2) HEURISTIC AND METAHEURISTIC METHODS 

Metaheuristics such as adaptive large neighborhood search (ALNS) and hybrid genetic algorithms (GA+LS) have been prominent in recent VRPD literature [32], [33]. Reyes et al. [32] applied a machine learning-guided ALNS to multi-modal routing, demonstrating improved generalization over standard heuristics. Similarly, Yurek and Ozmutlu [33] proposed an iterative large neighborhood search with drone coordination. 

In comparison: 

- Our method provides **provable optimality or optimality bounds** , which heuristic-based models cannot guarantee [32], [33]. 

- Experimental benchmarks (see Section V) show that our approach outperforms heuristic methods (e.g., ACO, GA) in terms of both cost minimization and delivery time across multiple dataset scales. 

- The **mode-switching and hub activation cost structures** embedded in our model are not easily represented in ALNS or GA-based approaches [32]. 

These comparisons reinforce the need for hybrid methodologies like ours that maintain solution quality while remaining scalable and structurally flexible for multi-modal, real-world routing problems. 

## **_D. SOLUTION APPROACHES IN THE LITERATURE_** 

The high computational complexity of multi-modal last-mile optimization has led researchers to explore various solution methodologies, including heuristic, exact, and hybrid approaches. 

Metaheuristic techniques such as Genetic Algorithms (GA), Ant Colony Optimization (ACO), Tabu Search, and Simulated Annealing have been extensively applied to vehicle routing and scheduling problems [34], [35]. These algorithms provide near-optimal solutions by searching large solution spaces efficiently, making them suitable for complex combinatorial problems such as last-mile delivery optimization [36], [37]. However, these methods often require problem-specific adaptations and extensive parameter tuning, which can impact their generalizability across different logistical environments [38]. 

In contrast, exact methods, including Branch-and-Cut, Column Generation, and Lagrangian Relaxation, have been employed to solve combinatorial optimization problems in transportation and logistics [7], [13], [39], [40]. These methods provide mathematically rigorous and provably optimal solutions, making them ideal for small- to medium-sized problem instances. However, their applicability becomes computationally intractable for large-scale routing problems due to the exponential growth of the solution space [12], [41]. 

A promising research direction involves the integration of machine learning with mathematical programming, leading to hybrid optimization approaches [42]. Machine learning models can be used to predict demand fluctuations, classify delivery zones, and assist in real-time decision-making [8], [43]. For instance, reinforcement learning (RL) algorithms have been successfully applied to dynamically adjust delivery routes based on real-time traffic data, allowing for adaptive fleet allocation and congestion mitigation [44], [45]. Additionally, neural combinatorial optimization techniques have been explored to accelerate last-mile delivery scheduling by leveraging deep learningbased policy models [46]. 

Overall, while heuristic and exact methods remain the foundation of last-mile optimization, the integration of machine learning, reinforcement learning, and hybrid techniques is expected to drive future innovations in the field. By combining data-driven insights with optimization heuristics, these approaches enable scalable, adaptive, and more efficient last-mile logistics solutions. 

## **III. PROBLEM DESCRIPTION** 

This study addresses the Multi-Depot, Multi-Modal LastMile Delivery Problem, where a fleet of autonomous delivery vehicles (ADVs) and drones is used to distribute packages from multiple depot locations to customers within specific time windows. The key challenges include: 

- _Time Window Constraints:_ Each customer must be served within a predefined time window. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1600 

- _Capacity Constraints:_ Vehicles and drones have limited carrying capacities for deliveries. 

- _Depot Assignments:_ Deliveries are dispatched from multiple depots, with routing decisions based on operational costs. 

- _Fleet Balancing:_ The allocation of deliveries between ADVs and drones must be optimized to minimize cost and travel distance. 

1) CAPACITY AND TIME WINDOW CONSTRAINTS Each vehicle/drone must respect its capacity limit: 



<!-- Start of picture text -->
� diyik ≤ Qk, ∀ k  ∈ K (2)<br>i ∈ C<br><!-- End of picture text -->



<!-- Start of picture text -->
� dizid ≤ Qd, ∀ d ∈ L (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
i ∈ C<br><!-- End of picture text -->

# where: 

- _di_ is the demand at customer _i_ . 

## **IV. MATHEMATICAL FORMULATION** 

To formalize the problem, we define a graph-based model where: 

- Let _G_ = _(V, E)_ be a directed graph, where: 

   - _V_ = { _D, C_ } is the set of nodes, with depots _D_ and customers _C_ . 

   - _E_ is the set of feasible travel arcs between nodes. 

- A set of vehicles _K_ and drones _L_ is available for deliveries. 

- Each vehicle/drone has a capacity constraint and follows a time window restriction. 

- The objective is to minimize the total operational cost, including transportation, hub activation, and modeswitching costs. 

## **_A. DECISION VARIABLES_** 

We define the following decision variables: 

- _xijk_ : Binary variable, equals 1 if vehicle _k_ travels from node _i_ to node _j_ . 

- _yik_ : Binary variable, equals 1 if customer _i_ is assigned to vehicle _k_ . 

- _zid_ : Binary variable, equals 1 if customer _i_ is assigned to drone _d_ . 

- _wm_ : Binary variable, equals 1 if micro-hub _m_ is activated. 

- _ti_ : Continuous variable representing the arrival time at customer _i_ . 

## **_B. OBJECTIVE FUNCTION_** 

The objective is to minimize the total transportation cost, hub activation cost, and mode-switching cost, formulated as: 



<!-- Start of picture text -->
min � � Cijxijk  + � � Ci ′ zid  + � Fmwm (1)<br>k (i,j) ∈ E d i ∈ C m<br><!-- End of picture text -->

# where: 

- _Cij_ is the travel cost between locations _i_ and _j_ . 

- _Ci_<sup>′is the cost of using a drone for delivery at location</sup><sup>_i_.</sup> 

- _Fm_ is the fixed cost of opening micro-hub _m_ . 

## **_C. CONSTRAINTS_** 

The optimization model is subject to the following constraints: 

- _Qk_ and _Qd_ are the capacity limits of vehicle _k_ and drone _d_ . 

Time windows must be satisfied: 



<!-- Start of picture text -->
ti  +  si  +  Tij ≤ tj, ∀ (i, j)  ∈ E, k  ∈ K (4)<br><!-- End of picture text -->

where: 

- _si_ is the service time at node _i_ . 

- _Tij_ is the travel time from node _i_ to node _j_ . 

- 2) VEHICLE AND DRONE MODE SELECTION CONSTRAINTS 

Each customer must be assigned to exactly one delivery mode: 



<!-- Start of picture text -->
� yik  + � zid = 1 , ∀ i  ∈ C (5)<br>k ∈ K d ∈ L<br><!-- End of picture text -->

- 3) DEPOT ASSIGNMENT AND HUB ACTIVATION CONDITIONS 

Each vehicle must start and end at the assigned depot: 



<!-- Start of picture text -->
� x 0 jk = 1 , ∀ k  ∈ K (6)<br>j ∈ C<br>� xi(n +1 )k = 1 , ∀ k  ∈ K (7)<br>i ∈ C<br><!-- End of picture text -->

where: 

- Node 0 represents the starting depot. 

- Node _n_ + 1 represents the return to the depot. 

- Micro-hubs are activated if at least one vehicle is assigned: 



<!-- Start of picture text -->
wm ≥ 1 � xmjk, ∀ m  ∈ M (8)<br>| K |<br>k ∈ K<br><!-- End of picture text -->

## **_D. SOLUTION APPROACH_** 

The formulated problem is a mixed-integer linear program (MILP). Due to its high complexity, we employ: 

- Valid Inequalities to strengthen the formulation and reduce computation time. 

- Branch-and-Price to solve large-scale instances efficiently using column generation. 

- Heuristic Initial Solutions for faster convergence in practical scenarios. 

To solve the formulated problem effectively, we adopt a Branch-and-Price (B&P) strategy. The section begins with an overview of the framework, followed by the column generation mechanism, pricing subproblem formulation, and advanced branching strategies. Acceleration techniques are then presented to ensure scalability. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1601 

## **V. MODEL DIFFERENTIATION FROM CLASSICAL FORMULATIONS** 

While our model builds on classical VRP extensions, it incorporates several novel features that go beyond what is captured in the traditional TSP-D, VRPD, or MDVRPTW frameworks [6], [47], [48]: 

- _Simultaneous Multi-Modal Optimization:_ Unlike TSPD or VRPD, which typically model vehicle-drone pairings or sequential dispatching [6], [47], our model jointly optimizes assignments and routing for both _autonomous delivery vehicles (ADVs)_ and _drones_ across a heterogeneous fleet. 

- _Smart Micro-Hub Activation:_ Classical formulations do not consider activation decisions or associated costs for intermediate micro-hubs [48]. Our model includes a binary variable for each micro-hub’s activation, linked to both routing feasibility and cost efficiency. 

- _Mode-Switching Cost Structure:_ We incorporate explicit costs for using drones versus ground vehicles, modeling trade-offs in time, energy, and operational risk. This cost differentiation is absent in standard MDVRPTW and most VRPD variants [47], [48]. 

- _Depot-to-Hub-to-Customer Routing Chains:_ Our model allows for flexible routing paths involving depot-to-hub-to-customer sequences, a structure not permitted in classical direct routing approaches like MDVRPTW [48]. 

- _Realistic Drone Payload Restrictions:_ We enforce delivery feasibility constraints using indicator-based logic: drones are only assigned to customers whose demand does not exceed drone capacity. This fine-grained feasibility modeling is often overlooked in simplified drone-enabled models [6], [47]. 

- _Fleet Mode Assignment Coupling:_ In contrast to standard formulations where vehicle types are fixed, our model dynamically assigns delivery modes (ground vs. air) based on cost and feasibility, while ensuring each customer is served exactly once [48]. 

- _Micro-Hub Utilization Constraints:_ Depot and hub usage is not only subject to capacity but also constrained by binary activation decisions and their routing implications, which classical formulations either ignore or treat statically [48]. 

These structural extensions allow the model to better reflect the operational realities of modern urban logistics involving mixed fleets and decentralized infrastructure. 

## **VI. MODEL EXTENSIONS BEYOND MDVRPTW** 

The proposed MD-CVRP-TW-MM model introduces several enhancements to the classical Multi-Depot Vehicle Routing Problem with Time Windows (MDVRPTW). These extensions reflect the evolving nature of last-mile delivery systems in smart cities and multi-modal logistics. Below, we describe and justify the key modeling innovations: 

- _Drone Assignment Variable (zid):_ A binary variable that assigns customer _i_ to drone _d_ , enabling airborne 

delivery modes. This extension is critical in modeling modern logistics systems where lightweight parcels can be delivered via UAVs, which is not captured in MDVRPTW. 

- _Micro-Hub Activation Variable (wm):_ This binary variable activates micro-hub _m_ , incorporating strategic decisions about infrastructure use and operating costs. MDVRPTW assumes fixed depots; our model allows dynamic hub selection. 

- _Mode Selection Constraint:_ 



<!-- Start of picture text -->
� yik  + � zid = 1 , ∀ i  ∈ C<br>k ∈ K d ∈ L<br><!-- End of picture text -->

ensures that each customer is served by exactly one delivery mode – either by a ground vehicle or a drone – a distinction absent from traditional MDVRPTW. 

- _Drone Payload Feasibility Constraint:_ 



<!-- Start of picture text -->
zid ≤ I (di ≤ Qd), ∀ i  ∈ C, d ∈ L<br><!-- End of picture text -->

guarantees that drones are only used for deliveries that comply with payload limitations, adding realistic physical constraints to the model. 

- _Hub-Based Routing Logic:_ Unlike MDVRPTW, which uses only depot-to-customer routing, our model supports depot → hub → customer paths, allowing efficient, decentralized dispatching. 

- _Objective Function Additions:_ 



<!-- Start of picture text -->
min � Cijxijk  + � Ci ′ zid  + � Fmwm<br><!-- End of picture text -->

includes drone-specific delivery costs and micro-hub activation costs, enriching the cost structure beyond the standard travel cost minimization in MDVRPTW. 

Together, these innovations enable our model to capture emerging trends in urban logistics, balancing cost, flexibility, and operational realism. 

**VII. VALID INEQUALITIES FOR MODEL ENHANCEMENT** **_A. MOTIVATION FOR VALID INEQUALITIES_** 

The inclusion of valid inequalities in the optimization model is crucial for improving computational efficiency and solution accuracy. These inequalities serve to: 

- _Reduce computational complexity:_ By tightening the feasible region, we eliminate redundant solutions and speed up convergence. 

- _Strengthen the LP relaxation:_ Ensuring that fractional solutions in the Linear Programming (LP) relaxation are closer to integer solutions. 

- _Improve convergence in Branch-and-Price:_ Reducing the search space in the column generation phase. 

## **_B. PROPOSED INEQUALITIES_** 

Several valid inequalities are introduced to enhance model performance: 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1602 

## 1) CAPACITY STRENGTHENING CUTS 

Capacity constraints ensure that no vehicle or drone exceeds its maximum load, but additional inequalities can be introduced to strengthen these conditions: 



<!-- Start of picture text -->
i ∈ S di<br>� yik ≤ , ∀ S  ⊆ C, k  ∈ K (9)<br>� � Qk �<br>i ∈ S<br><!-- End of picture text -->

where: 

- _di_ is the demand at customer _i_ . 

## **_C. IMPACT OF VALID INEQUALITIES_** 

By integrating these valid inequalities, we achieve: 

   - _Reduced solution time:_ The computational burden is lowered due to a more restricted search space. 

   - _Higher quality solutions:_ Fractional LP solutions are closer to integer solutions, reducing Branch-and-Price iterations. 

   - _More stable convergence:_ Particularly in large-scale instances, where column generation benefits from tighter LP relaxations. 

- _Qk_ is the vehicle capacity. 

- This inequality ensures that if a vehicle visits a subset _S_ of customers, its total demand does not exceed capacity. 

## 2) SUBTOUR ELIMINATION CONSTRAINTS (SEC) 

To prevent vehicles from forming disconnected loops, we introduce: 



<!-- Start of picture text -->
� xijk ≤| S | − 1 , ∀ S  ⊆ C, k  ∈ K (10)<br>(i,j) ∈ S<br><!-- End of picture text -->

# where: 

- _S_ is any subset of customer nodes. 

- The inequality ensures that no vehicle forms a separate cycle that does not include the depot. 

## 3) DEPOT ACTIVATION BOUNDING CONSTRAINTS 

To ensure a balanced workload among depots, we introduce: 



<!-- Start of picture text -->
� x 0 jk ≤ M  ·  wm, ∀ j  ∈ C, m  ∈ M (11)<br>k ∈ K<br><!-- End of picture text -->

# where: 

- _M_ is a large constant representing the maximum number of activated hubs. 

- _wm_ is a binary variable indicating whether micro-hub _m_ is activated. 

- This ensures that hubs are only activated when necessary, reducing operational costs. 

## 4) MODE SELECTION VALID INEQUALITIES 

Each customer must be assigned exclusively to one delivery mode (vehicle or drone): 



<!-- Start of picture text -->
� yik  + � zid = 1 , ∀ i  ∈ C (12)<br>k ∈ K d ∈ L<br><!-- End of picture text -->

Additionally, to ensure that drone deliveries are only feasible for lightweight packages, we enforce: 



<!-- Start of picture text -->
zid ≤ I (di ≤ Qd), ∀ i  ∈ C, d ∈ L (13)<br><!-- End of picture text -->

# where: 

- I _(_ · _)_ is an indicator function that ensures drones are not assigned to packages exceeding their maximum payload _Qd_ . 

## **_D. THEORETICAL COMPLEXITY AND VALIDITY OF INEQUALITIES_** 

## NP-HARDNESS OF THE PROBLEM 

The proposed MD-CVRP-TW-MM problem generalizes the classical Multi-Depot Vehicle Routing Problem with Time Windows (MDVRPTW), which is known to be NP-hard [49]. Our formulation introduces additional decision layers–such as drone feasibility, mode-switching costs, and microhub activation—which increase the problem’s combinatorial complexity. As a result, MD-CVRP-TW-MM is also NP-hard by extension and intractable to solve optimally in polynomial time for large instances. 

## 1) VALIDITY OF THE INTRODUCED INEQUALITIES 

We briefly sketch the reasoning behind the validity of each inequality class: 

- _Capacity Strengthening Cuts (Eq. (_ 1 _)):_ These are derived from the classical CVRP constraints, ensuring that for any subset _S_ ⊆ _C_ , the total number of customers served does not exceed what a single vehicle of capacity _Qk_ can handle. The floor function bounds the maximum allowable number of visits. 

- _Subtour Elimination Constraints (Eq. (_ 2 _)):_ These follow the well-established Miller–Tucker–Zemlin (MTZ) logic and prevent the formation of disconnected loops in vehicle routing. Each vehicle’s route must form a single connected path that starts and ends at a depot. 

- _Depot Activation Constraints (Eq. (_ 3 _)):_ These enforce a logical dependency: a depot _m_ can only be used if it is activated (i.e., _wm_ = 1 _)_ . This binary coupling is standard in facility location and capacitated routing problems. 

- _Mode Selection and Feasibility (Eq. (_ 4 _) and Eq. (_ 5 _)):_ These constraints ensure that each customer is assigned to one–and only one–delivery mode (either vehicle or drone). Additionally, Eq. (5) ensures drones are assigned only to customers whose demand does not exceed their payload limit, using a logical indicator condition. 

These inequalities are mathematically valid and serve to tighten the linear programming relaxation, reduce fractional solutions, and accelerate convergence within the Branch-andPrice framework. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1603 

## **VIII. SOLUTION APPROACH: BRANCH-AND-PRICE METHOD** 

## **_A. OVERVIEW OF BRANCH-AND-PRICE FRAMEWORK_** 

Given the combinatorial nature of the Multi-Depot, MultiModal Last-Mile Delivery Problem, solving it using traditional Mixed-Integer Programming (MIP) techniques can be computationally expensive. Instead, we employ a Branch-and-Price (B&P) approach, which is an exact method combining: 

- Branch-and-Bound: Systematically exploring the solution space using a branching tree. 

- Column Generation: Iteratively refining the Restricted Master Problem (RMP) by introducing new delivery routes as columns. 

The problem is decomposed into: 

- A Master Problem (MP), which determines optimal vehicle and drone assignments while minimizing cost. 

- A Pricing Subproblem, which finds optimal delivery routes based on dual values from the master problem. 

## 1) COLUMN GENERATION STRATEGY FOR DELIVERY ROUTE SELECTION 

The Restricted Master Problem (RMP) is initially solved with a limited set of feasible routes. New delivery routes (columns) are iteratively added to improve the solution. Formally, the RMP is defined as: 



<!-- Start of picture text -->
min � crλr (14)<br>r ∈ R<br><!-- End of picture text -->

subject to: 



<!-- Start of picture text -->
� airλr = 1 , ∀ i  ∈ C (15)<br>r ∈ R<br>� drλr ≤ Qk, ∀ k  ∈ K (16)<br>r ∈ R<br><!-- End of picture text -->

# where: 

- _R_ is the set of feasible delivery routes. 

- _cr_ is the cost associated with route _r_ . 

- _λr_ is a binary variable indicating whether route _r_ is selected. 

- _air_ is 1 if customer _i_ is served in route _r_ , otherwise 0. 

- _dr_ is the total demand in route _r_ . 

## 2) PRICING SUBPROBLEM FORMULATION AND RESOLUTION 

The pricing subproblem generates the most cost-effective delivery route to be added to the master problem. It is formulated as a Shortest Path Problem with Resource Constraints (SPPRC): 



<!-- Start of picture text -->
min � Cijxijk  − � πiyik (17)<br>(i,j) ∈ E i ∈ C<br><!-- End of picture text -->



<!-- Start of picture text -->
subject to:<br>� xijk  − � xjik = 0 , ∀ i  ∈ C, k  ∈ K (18)<br>j ∈ C j ∈ C<br><!-- End of picture text -->

- **Algorithm 1:** Branch-and-Price for Multi-Modal LastMile Delivery (MD-CVRP-TW-MM) 

- **Input** : Customer set _C_ , depot set _D_ , hub set _M_ , fleets _K_ and _L_ 

- **Output** : Optimized assignment of vehicles/drones and routes minimizing total delivery cost 

- 1 Initialize Restricted Master Problem (RMP) with feasible seed routes **repeat** 

- 2 Solve RMP (LP relaxation) and obtain dual prices _πi_ 

   - **foreach** _delivery mode (vehicle or drone)_ **do** 

- 3 Solve pricing subproblem via SPPRC using duals _πi_ 

- **if** _route has negative reduced cost_ **then** 

- 4 Add new route as a column to RMP 

- 5 **until** _no new route with negative reduced cost is found_ ; 

- 6 **if** _RMP solution is fractional_ **then** 

- 7 Apply branching strategies: 

   - Enforce mode exclusivity (vehicle vs. drone) 

   - Fix depot or hub assignment per customer 

   - Resolve subtour violations 

   - Recurse into each branch node 

- 8 **return** _Best integer solution across branch-and-bound_ _<u>tree</u>_ 



<!-- Start of picture text -->
� diyik ≤ Qk, ∀ k  ∈ K (19)<br>i ∈ C<br><!-- End of picture text -->

where: 

- _πi_ is the dual price from the master problem, influencing route selection. 

- _xijk_ is a binary variable indicating whether vehicle _k_ travels from node _i_ to node _j_ . 

- _yik_ is a binary variable indicating whether customer _i_ is assigned to vehicle _k_ . 

New routes are iteratively generated and added to the RMP until no negative reduced-cost columns remain. 

3) PSEUDOCODE SUMMARY OF THE BRANCH-AND-PRICE PROCEDURE 

See Algorithm 1. 

## **_B. BRANCHING STRATEGIES_** 

Once an optimal fractional solution is found, branching is required to obtain integer solutions. We employ three key branching strategies: 

## 1) BRANCH ON MODE SELECTION: DRONE VS. ADV ASSIGNMENTS 

If a customer is fractionally assigned to both an ADV and a drone, we branch by enforcing: 



<!-- Start of picture text -->
� zid = 0 or � yik = 0 , ∀ i  ∈ C (20)<br>d ∈ L k ∈ K<br><!-- End of picture text -->

ensuring that the customer is served only by one mode. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1604 

- 2) BRANCH ON DEPOT ASSIGNMENTS: BALANCING HUB WORKLOADS 

If a fractional depot assignment is found, we enforce: 



<!-- Start of picture text -->
� x 0 jk ≤ 1 , ∀ j  ∈ C (21)<br>k ∈ K<br><!-- End of picture text -->

ensuring that the customer is served from one depot only. 

## 3) BRANCH ON ROUTING DECISIONS: ENSURING FEASIBILITY 

## **_A. EXPERIMENTAL SETUP_** 

To evaluate the efficiency of our Branch-and-Price (B&P) approach, we conducted experiments on various benchmark datasets representing small-scale, medium-scale, and largescale last-mile delivery problems. 

**Benchmark Datasets:** To evaluate the performance and scalability of the proposed optimization approach, we constructed synthetic datasets across three problem scales, each reflecting practical multi-modal last-mile delivery environments with increasing complexity: 

To avoid cycles and enforce direct connections: 



<!-- Start of picture text -->
xijk = 0 , or xjik = 0 , ∀ (i, j) ∈ C, k  ∈ K (22)<br><!-- End of picture text -->

ensuring vehicles follow a direct path without unnecessary loops. 

## **_C. ACCELERATION TECHNIQUES_** 

To improve computational performance, we introduce: 

## 1) DUAL STABILIZATION TO IMPROVE COLUMN GENERATION 

Traditional column generation can exhibit instability, leading to slow convergence. To mitigate this, we implement: 



<!-- Start of picture text -->
πi (t) =  απi (t −1 ) +  ( 1 − α)πi (23)<br><!-- End of picture text -->

where: 

- _πi_<sup>_(t)_</sup> is the dual price at iteration _t_ . 

- • _πi_ is the optimal dual value from the last iteration. • _α_ is a stabilization parameter (0.5–0.9). 

This ensures smooth updates and avoids drastic fluctuations. 

## 2) PATH-BASED HEURISTICS FOR FASTER CONVERGENCE 

To quickly generate high-quality delivery routes, we implement: 

- Labeling algorithms for solving the SPPRC pricing problem. 

- Path-based heuristics to pre-generate feasible columns before optimization. 

## **_D. COMPUTATIONAL BENEFITS OF BRANCH-AND-PRICE_** 

- _Reduces memory requirements:_ Only active routes are stored. 

- _Improves convergence:_ Column generation avoids unnecessary route exploration. 

- _Scalable to large problem instances:_ Enables solving real-world last-mile delivery problems efficiently. 

## **IX. COMPUTATIONAL EXPERIMENTS AND RESULTS** 

This section evaluates the performance of our approach on synthetic benchmarks across varying instance scales. We compare it with heuristic baselines (ALNS, LNS), a commercial solver, and Google OR-Tools to ensure realistic benchmarking. 

- _Small-Scale:_ 10 instances with 50 customers, 2 depots, and 10 vehicles. 

- _Medium-Scale:_ 10 instances with 200 customers, 5 depots, and 20 vehicles. 

- _Large-Scale:_ 10 instances with 500 customers, 10 depots, and 50 vehicles. 

These sizes were selected to represent (i) small urban areas with constrained resources, (ii) mid-sized city-wide operations, and (iii) large metropolitan or regional logistics scenarios. These scales align with standard benchmarks in the literature for VRP/MDVRPTW and are sufficient to test both algorithmic scalability and routing efficiency under realistic conditions. Fleet sizes were proportionally scaled with problem size to maintain consistent service feasibility while introducing increasing routing complexity. 

Each instance was generated on a 2D Euclidean grid of 100 × 100 units. Depot locations were positioned near the grid boundaries, while candidate micro-hubs were clustered near the center to reflect realistic hub-and-spoke patterns in urban logistics. This spatial setup mimics central business districts with peripheral warehouses, a common configuration in smart city planning and last-mile distribution. 

Customer demands were drawn from a uniform distribution _di_ ∼ _U_ [5 _,_ 20]. Drone deliveries were constrained to serve only customers with demand _di_ ≤ 8 units, reflecting standard drone payload capacities (e.g., ≤ 5 kg) used in commercial delivery services. The lower demand threshold reflects FAA guidelines and Amazon/Zipline operational payloads. 

Time windows were randomly generated over a daily planning horizon of 480 minutes (8 hours), with early and late bounds and service durations between 5 to 10 minutes, consistent with courier and retail delivery benchmarks. These ranges reflect hourly delivery blocks typical of e-commerce and express logistics services. 

**Cost Structure:** The ground vehicle cost per unit distance was set higher than drone cost, reflecting higher operational and labor expenses. However, drones incur additional fixed dispatch penalties and range limitations to simulate energy and maintenance constraints. Depot activation costs were incorporated to reflect utility, setup, and personnel overhead, encouraging minimal hub usage where possible. 

To ensure reproducibility of results, we used a fixed random seed (seed = 42) across all instance generation 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1605 

steps including demand values, location coordinates, and time window assignments. 

# **Computational Environment:** 

- Intel Core i9 Processor, 32GB RAM. 

- Solver: CPLEX 12.10 with Gurobi for comparison. 

- Programming Language: Python with PuLP for MILP formulation. 

## **_B. PERFORMANCE METRICS_** 

The primary performance indicators include: 

- Cost Minimization: Lower total transportation and hub activation costs. 

- Delivery Time Reduction: Time taken to complete deliveries. 

- Computational Efficiency: Solution time and optimality gap. 

## **_C. COMPARISON WITH BASELINE METHODS_** 

To evaluate the effectiveness of our Branch-and-Price (B&P) approach, we compare it with various baseline methods, including heuristic approaches, commercial solvers, and traditional Vehicle Routing Problem with Time Windows (VRPTW) models. 

## 1) HEURISTIC APPROACHES 

Heuristic methods are widely used for solving complex combinatorial optimization problems where exact methods are computationally expensive. We compare B&P with: 

a) Implementation of Ant Colony Optimization (ACO): The Ant Colony Optimization (ACO) algorithm is implemented through an iterative process that mimics the foraging behavior of ants. The algorithm begins with the initialization of key parameters, including the number of ants _(m_ ), the pheromone evaporation rate ( _ρ_ ), the pheromone influence factor ( _α_ ), and the heuristic desirability factor ( _β)_ . These parameters guide the algorithm’s exploration and exploitation strategies. 

During the solution construction phase, each ant starts at a depot and selects the next delivery node _j_ based on a probabilistic rule. The probability of an ant moving from node _i_ to node _j_ is given by: 



<!-- Start of picture text -->
τ α<br>ij ·  η i β j<br>Pij = (24)<br>� k ∈ Ni τ ik  α ·  η ik β<br><!-- End of picture text -->

where _τij_ represents the pheromone level on the route between nodes _i_ and _j_ , and _ηij_ is the heuristic desirability, defined as the inverse of the distance _(ηij_ = 1 _/dij_ ). The set _Ni_ contains all feasible next nodes. This probabilistic selection mechanism ensures that the ants balance between exploiting the best-known paths and exploring alternative routes. 

To refine the solution, the pheromone trails are updated dynamically. Pheromone evaporation occurs as: 



<!-- Start of picture text -->
τij ← ( 1 − ρ)  ·  τij (25)<br><!-- End of picture text -->

which prevents unlimited accumulation and encourages exploration. Additionally, reinforcement is applied based on the best-performing ants: 



<!-- Start of picture text -->
m Q<br>τij ← τij  + � (26)<br>Lk<br>k =1<br><!-- End of picture text -->

where _Q_ is a constant and _Lk_ is the total route length of ant _k_ . This mechanism favors shorter and more efficient routes, gradually reinforcing the best solutions over iterations. 

The algorithm repeats until a predefined termination condition is met, such as reaching a maximum number of iterations or when no further improvement is observed in the solutions. 

ACO dynamically adapts to changing constraints, making it particularly suitable for multi-modal last-mile delivery optimization. However, the convergence speed depends heavily on parameter tuning, and the algorithm may stall in local optima if pheromone updates are not properly controlled. 

b) Implementation of Genetic Algorithm (GA): The Genetic Algorithm (GA) approach follows a structured evolutionary process to optimize delivery routing. The process, shown in Algorithm 2, begins with the initialization of a population, where a set of candidate solutions, represented as chromosomes, is generated. Each chromosome encodes a sequence of delivery stops, forming a potential route. 

The next step involves evaluating the fitness function, which assesses the quality of each chromosome based on factors such as total travel cost, fleet utilization, and route length. Solutions that minimize delays and optimize travel efficiency are favored. 

For selection, GA employs mechanisms such as Roulette Wheel Selection, which assigns higher selection probabilities to better solutions, and Tournament Selection, which enhances diversity and prevents premature convergence. 

In the crossover phase, parent chromosomes are recombined using Partially Mapped Crossover (PMX). This process involves selecting crossover points, swapping route segments, and resolving duplicate assignments to maintain feasibility. 

To introduce variation, the mutation phase applies Swap Mutation, where two random delivery points are exchanged. This prevents genetic stagnation and ensures diverse route exploration. 

The process iterates until a stopping criterion is met, such as a predefined number of generations or the absence of significant improvements over iterations. 

GA is well-suited for solving high-dimensional routing problems due to its ability to explore diverse feasible solutions. However, it can be computationally intensive for large-scale datasets, and its convergence rate may be slow without well-designed mutation strategies. 

c) Implementation of Large Neighborhood Search (LNS): The LNS algorithm operates by repeatedly destroying and repairing parts of a current solution. In each iteration, a 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1606 

**TABLE 1. Cost minimization across different methods.** 

subset of customers is removed using a Shaw removal strategy based on relatedness (e.g., spatial proximity and time window overlap). The removed customers are then reinserted using a regret-2 insertion heuristic that favors minimizing future insertion regret. This process helps escape local optima by allowing large changes in the solution space. 

d) Implementation of Adaptive Large Neighborhood Search (ALNS): ALNS extends LNS by adaptively selecting removal and insertion heuristics based on historical performance. At each iteration, ALNS assigns scores to operators and updates their selection probabilities using a roulette-wheel strategy. We implemented multiple destroy operators (random, worst, Shaw removal) and repair operators (greedy, regret-k). This allows the algorithm to self-tune and adapt to the search landscape dynamically. 

e) Commercial Solvers: To further validate the performance of B&P, we compare it with industry-standard Mixed-Integer Linear Programming (MILP) solvers, specifically CPLEX and Gurobi. 

CPLEX is a powerful branch-and-bound solver that provides exact solutions by employing cutting-plane methods to strengthen LP relaxations, branch-and-cut algorithms for better integer feasibility, and dual simplex methods for faster convergence. While robust, CPLEX can be computationally expensive, particularly for large-scale routing problems. 

Gurobi, another leading MILP solver, incorporates presolve reductions to simplify constraints, parallel branchand-bound techniques for enhanced computational speed, and heuristic-based warm starts to improve initial solutions. Despite its efficiency, Gurobi faces challenges in handling multi-modal routing problems, as it is primarily designed for standard VRP formulations. 

_a: State-of-the-Art Solver (Google OR-Tools):_ To benchmark our approach against publicly available advanced solvers, we implemented the same datasets using Google OR-Tools, a widely adopted open-source library for vehicle routing problems, including Multi-Depot VRPTW. The ORTools solver is configured with: 

- Global Cheapest Insertion strategy for initial solution construction. 

- Tabu Search and Simulated Annealing metaheuristics for local improvement. 

- Capacity, time window, and depot constraints enforced via built-in filters. 

Although OR-Tools does not natively support drone-based deliveries or dynamic hub activation, it provides a strong baseline for standard MDVRPTW problems. Our results show that while OR-Tools achieves competitive runtimes and feasible routes, it lacks multi-modal coordination and typically incurs higher delivery costs due to its reliance on ground vehicles alone. 

By comparison, our Branch-and-Price framework achieves lower delivery costs and shorter delivery times by optimally coordinating between ground fleets and drones. This advantage becomes more evident as problem size increases. 

_b: Traditional VRPTW Models:_ The Vehicle Routing Problem with Time Windows (VRPTW) is considered as a baseline model without multi-modal integration. Traditional VRPTW models focus on vehicle allocation using MILP formulations, optimizing routes within fixed time windows and employing single-mode delivery strategies. However, they do not account for the integration of drones or autonomous delivery vehicles (ADVs), which are crucial in modern last-mile logistics. Consequently, these models struggle to optimize hybrid fleet coordination, leading to higher delivery costs and longer service times. 

_c: Key Observations From Baseline Comparisons:_ The comparison of B&P with heuristic approaches, commercial solvers, and traditional VRPTW models highlights several advantages. Branch-and-Price consistently outperforms heuristic methods by generating near-optimal solutions with significantly lower costs. While commercial solvers such as CPLEX and Gurobi deliver high-quality solutions, their computational time is substantially longer, making them less practical for large-scale last-mile delivery applications. Furthermore, traditional VRPTW models are ineffective in multi-modal logistics, as they fail to integrate drones and dynamic depot selection, limiting their applicability in realworld scenarios. 

f) Cost Minimization Comparison Table 1 presents the cost minimization results for the four tested methods: Branch-and-Price (B&P), Heuristic approaches, Google ORTools, and a Commercial Solver. The comparison was conducted across small-scale, medium-scale, and large-scale last-mile delivery datasets. 

_a: Analysis and Interpretation:_ The Branch-and-Price method outperforms heuristic approaches in all dataset sizes by achieving the lowest total delivery cost. The cost savings are most noticeable in large-scale problems, where the heuristic solution incurs an additional $7,000 in expenses. This improvement is attributed to: 

- _More efficient route selection:_ B&P generates optimized delivery routes while heuristics may rely on approximations. 

- _Better load balancing:_ The model minimizes unnecessary hub activations and optimizes vehicle utilization. 

- _Precise integer solutions:_ Unlike heuristics, which rely on local optima, B&P provides globally optimal or nearoptimal solutions. 

_b: Comparison With Commercial Solver:_ The commercial solver performs well but remains slightly more expensive than B&P. This difference is due to: 

- Computational time limitations: The solver may apply early stopping criteria, leading to sub-optimal solutions. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1607 

**TABLE 2. Average delivery time (in minutes).** 

**TABLE 3. Solution time (s) and optimality gap (%).** 



- Model flexibility: B&P tailors column generation strategies to multi-modal fleet dynamics, whereas general solvers optimize standard VRPTW formulations. 

The Branch-and-Price (B&P) approach consistently achieves the lowest cost, reducing last-mile delivery expenses by 6–12% compared to heuristic methods. Its advantage becomes more evident as the problem size increases, demonstrating superior scalability for large-scale logistics networks. While commercial solvers such as CPLEX and Gurobi provide effective solutions, a tailored B&P approach further enhances cost efficiency, particularly in the context of multi-modal delivery systems. By optimizing fleet allocation and minimizing travel distances, B&P offers a practical and computationally efficient alternative for modern last-mile logistics. 

g) Delivery Time Reduction: Table 2 presents the average delivery time (in minutes) for different optimization methods, including Branch-and-Price (B&P), Heuristic approaches, Google OR-Tools, and a Commercial Solver. The results are shown for small-scale, medium-scale, and large-scale lastmile delivery datasets. 

_a: Analysis and Interpretation:_ The Branch-and-Price method achieves the lowest delivery time across all dataset sizes, demonstrating its ability to optimize last-mile delivery operations efficiently. The key advantages include: 

- _Improved route selection:_ The model dynamically selects routes that minimize total travel distance and avoid unnecessary detours. 

- _Optimized fleet allocation:_ Ensures balanced workload distribution among autonomous delivery vehicles (ADVs) and drones. 

- _Better scheduling within time windows:_ Reduces idle time at depots and optimally assigns deliveries to minimize waiting periods. 

_b: Comparison with Heuristic Approaches:_ The heuristicbased methods result in 5-8% longer delivery times due to: 

- Sub-optimal routing decisions: Greedy heuristics prioritize local optima instead of global optimization. 

- Lack of adaptive fleet coordination: Heuristics often do not effectively balance the use of ADVs and drones. 

- Higher vehicle idle times: Inefficient scheduling increases waiting times at micro-hubs. 

The commercial solver performs better than heuristic methods but is still 2–4% slower than the Branch-and-Price (B&P) approach. This difference arises primarily from the solver’s reliance on a generic solution framework, which is optimized for standard Vehicle Routing Problem with Time Windows (VRPTW) formulations and may not fully 

exploit the advantages of multi-modal logistics. Additionally, commercial solvers tend to make sub-optimal trade-offs between vehicle and drone assignments, as they focus primarily on traditional vehicle routing rather than ensuring seamless coordination between autonomous delivery vehicles (ADVs) and drones. 

The Branch-and-Price approach consistently outperforms heuristic methods and commercial solvers, reducing average delivery time by 5–8%. The advantage of B&P becomes more pronounced as the problem size increases, reinforcing its scalability for complex last-mile delivery networks. Efficient multi-modal fleet coordination is a crucial factor in achieving these improvements, as the model dynamically assigns deliveries between vehicles and drones based on cost, time, and capacity constraints. 

h) Computational Efficiency: Table 3 presents the solution time (in seconds) and optimality gap (in percentage) for the four methods: Branch-and-Price (B&P), Heuristic approaches, Google OR-Tools, and a Commercial Solver. The results are reported for small-scale, medium-scale, and large-scale last-mile delivery datasets. 

_a: Analysis and Interpretation:_ The Branch-and-Price method achieves a better trade-off between solution quality and computational efficiency compared to both heuristic methods and commercial solvers. The key observations are: 

- _Solution Time:_ The heuristic method is faster but at the cost of suboptimal solutions. Commercial solvers take significantly longer for medium and large-scale problems. 

- _Optimality Gap:_ B&P maintains a low optimality gap (1.2-4.1%), outperforming heuristics (3.5-7.9%) and slightly better than commercial solvers (2.0-5.5%). 

- _b: Comparison with Heuristic Approaches:_ Heuristic 

- methods are faster but less precise: 

- Computational Time Advantage: Heuristic methods provide quick solutions for real-time applications. 

- Higher Optimality Gap: The trade-off is a higher suboptimality margin, especially for large-scale datasets. 

- Greedy Nature: Local optimization prevents heuristics from finding globally optimal routes. 

- _c: Comparison With Commercial Solver:_ Commercial 

- solvers deliver high-quality solutions but at the cost of longer runtime: 

- Scalability Issues: Solver time grows exponentially with dataset size. 

- Fixed Constraint Handling: General solvers may not leverage problem-specific heuristics, making B&P more efficient for multi-modal last-mile delivery. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1608 

**TABLE 4. Wilcoxon signed-rank test for total cost comparison.** 



# _d: Key Observations_ 

- _Branch-and-Price provides a near-optimal solution with significantly lower computational cost compared to commercial solvers._ 

- _Heuristic approaches are useful for real-time applications but yield higher suboptimality._ 



**FIGURE 1. Total cost comparison across Branch-and-Price, Heuristic, OR-Tools, ALNS, LNS, and Commercial Solver methods for small-, medium-, and large-scale datasets.** 

- _For large-scale datasets, Branch-and-Price offers the best balance between accuracy and efficiency._ 

## **_D. STATISTICAL VALIDATION AND ROBUSTNESS_** 

To ensure the reliability and significance of the observed performance improvements, we conducted additional statistical analysis across the ten synthetic instances per dataset scale. 

**Mean** ± **Standard Deviation Reporting:** All performance metrics in Tables 1, 2, and 3 have been enhanced with standard deviation values, enabling a more robust comparison across algorithms and problem scales. This quantifies variability and emphasizes consistency across independent runs. 

**Wilcoxon Signed-Rank Test:** We employed the Wilcoxon signed-rank test to compare the Branch-and-Price method with both heuristic and commercial solver baselines. The test results for total cost (Table 4) confirm statistically significant improvements _(p <_ 0 _._ 01 _)_ in favor of B&P across all dataset sizes. 

## **_E. SENSITIVITY ANALYSIS_** 

To assess the robustness and adaptability of our optimization model, we conducted a comprehensive sensitivity analysis on four critical parameters: fleet size, demand variability, traffic conditions, and newly added dimensions such as depot activation cost and drone payload limits. 

**Fleet Size:** As the fleet size increases, computational time decreases due to the greater availability of delivery resources, but cost efficiency begins to plateau. This suggests that while expanding the fleet improves delivery performance, the marginal benefit diminishes beyond a certain threshold. 

**Demand Variability:** High-demand scenarios necessitate a greater reliance on drones, which in turn affects cost efficiency by increasing operational expenses associated with drone deployment. The model dynamically adjusts to such fluctuations, ensuring that resources are optimally allocated between autonomous delivery vehicles and drones. Simulated demand distributions _(U_ [3 _,_ 10], _U_ [5 _,_ 20], and _U_ [10 _,_ 25] _)_ revealed a 15–18% shift in mode selection patterns, with heavier demands reducing drone utility by up to 22%. 

**Depot Activation Cost:** By increasing or decreasing the depot activation cost by ±50%, we observed significant behavioral shifts in the model. High activation costs discouraged the use of multiple depots, resulting in longer route distances and increased delivery costs (up to +9.2%). Conversely, reduced activation costs encouraged broader depot utilization, lowering delivery times by 6.7% on average due to improved regional accessibility. 

**Drone Payload Limits:** When drone capacity was varied between 6, 8 (baseline), and 10 units, higher limits led to increased drone usage (by up to 22%), especially in medium-scale scenarios. This reduced average delivery time by approximately 4.1%, confirming the importance of drone capacity in shaping optimal route configurations. 

**Traffic Conditions:** Real-time traffic patterns directly affect routing efficiency and depot selection. The model adapts dynamically by adjusting depot activation and travel times. With congestion simulated by inflating travel time costs by 20–40%, depot proximity and drone deployment became more influential in minimizing overall delay, thereby preserving service-level constraints in high-traffic scenarios. 

These results highlight the model’s flexibility and provide actionable insights for decision-makers when tuning operational parameters in real-world deployments. 

## **_F. VISUALIZATION OF RESULTS_** 

Figures 1, 2, 3, and 4 illustrate the performance of our Branch-and-Price (B&P) approach compared to a variety of optimization methods, including Heuristics, Commercial Solvers (CPLEX/Gurobi), Google OR-Tools, Adaptive Large Neighborhood Search (ALNS), and Large Neighborhood Search (LNS). These methods were tested across small-, medium-, and large-scale last-mile delivery datasets. 

Figure 1 shows the total cost comparison. B&P consistently achieves the lowest delivery cost across all scales. In large-scale datasets, the advantage becomes more pronounced due to the framework’s effective coordination between vehicles and drones. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1609 



**FIGURE 2. Average delivery time across optimization methods for different dataset scales. Branch-and-Price consistently yields the shortest delivery times.** 



**FIGURE 3. Solution time (in seconds) for each method across all dataset sizes. B&P is more scalable than commercial solvers while achieving better precision than heuristics.** 

Figure 2 presents the average delivery time (in minutes). B&P outperforms all baselines, especially in complex scenarios, where multimodal coordination is critical. OR-Tools, while competitive, lacks drone integration, and ALNS/LNS achieve better results than basic heuristics but fall short of B&P. 

Figure 3 evaluates solution time across all methods. Heuristics and LNS are fastest but least accurate. B&P offers a strong balance between computational effort and solution quality, outperforming commercial solvers in larger instances. 

Figure 4 shows the optimality gap percentages. B&P delivers the lowest gap across all problem sizes, with its advantage increasing in large-scale scenarios. ALNS and OR-Tools reduce gaps relative to basic heuristics but cannot match the exactness of B&P. 

## **X. DISCUSSION AND PRACTICAL IMPLICATIONS** 

We now synthesize insights drawn from the experimental results, focusing on trade-offs, operational patterns, and practical deployment implications. 

Our computational experiments demonstrate that the Branch-and-Price (B&P) approach significantly enhances last-mile delivery optimization. The results indicate that B&P reduces total costs by 12–18% compared to heuristic 



**FIGURE 4. Optimality gap percentage comparison. Branch-and-Price consistently achieves lower gaps, particularly in medium and large-scale problems.** 

approaches and commercial solvers. Additionally, the integration of autonomous delivery vehicles (ADVs) and drones results in an average delivery time reduction of 8–12%, improving the efficiency of last-mile logistics. The proposed model also proves to be computationally advantageous, solving medium-scale problems approximately 1.5 times faster than conventional exact methods. 

A key insight from our results is the trade-off between cost minimization and delivery-time performance. While B&P delivers the lowest operational costs across all dataset scales, heuristic methods such as ALNS occasionally achieve faster delivery times in small-scale scenarios. This is particularly evident where route compactness takes precedence over global cost optimization. However, the advantage of heuristics diminishes with increasing problem size, as they struggle with complex multi-modal coordination. B&P, by contrast, leverages both ground and drone modes effectively to balance cost and time, making it a more robust option for large-scale and time-sensitive applications. 

To further analyze the behavior of our optimization framework, we examined key aspects of the solution structures across various problem scales: 

- _Drone vs. ADV Utilization:_ On average, drones were used for approximately 32% of deliveries in smallscale problems and around 26% in large-scale problems. Drones were primarily dispatched for short-range, lightweight deliveries within a 5 km radius of microhubs. 

- _Hub Usage Patterns:_ The number of activated microhubs varied based on demand distribution. Typically, 50–70% of candidate hubs were utilized in large-scale problems. The model favored centrally located hubs to minimize total travel distances and balance depot activation costs. 

- _Route Complexity:_ ADV routes served between 8–14 customers per tour, whereas drone tours were limited to 1–3 customers due to payload and range constraints. This structure enables efficient division of labor between modes while respecting operational limits. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1610 

These findings confirm that the model not only optimizes performance metrics but also generates interpretable and realistic logistics structures, contributing to practical implementability. 

The findings have significant implications for modern urban logistics. The model enhances on-demand delivery services in high-density cities by optimizing fleet operations and reducing congestion through micro-hub-based logistics networks. E-commerce and retail supply chains stand to benefit from improved delivery reliability, particularly for companies such as Amazon, UPS, and DHL. By optimizing last-mile logistics, businesses can lower operational costs and improve service levels. Additionally, the environmental impact is notable as optimized fleet routes and the incorporation of electric drones contribute to reduced carbon emissions. The model encourages the adoption of lowemission delivery solutions, aligning with sustainability goals in modern logistics. 

Despite its advantages, the current approach has some limitations. Scalability remains a challenge, particularly for large-scale instances involving over 1,000 customers and 50+ depots, which require substantial computational resources. Future research could explore parallelized B&P methods to improve scalability and efficiency. Another area for enhancement is the integration of machine learning-based demand forecasting, which could improve routing decisions under dynamic and uncertain demand conditions. Moreover, real-time traffic congestion and weather conditions are not currently incorporated into the model, limiting its adaptability in dynamic urban environments. Future extensions should address these aspects to further improve last-mile delivery optimization. 

## **XI. CONCLUSION** 

This study introduced a novel Multi-Depot, Multi-Modal Last-Mile Delivery Optimization Model and developed a Branch-and-Price (B&P) approach to enhance efficiency in last-mile logistics. The proposed methodology is built upon a Mixed-Integer Linear Programming (MILP) formulation, incorporating both autonomous vehicles and drones to optimize delivery operations. To improve computational performance, the model integrates valid inequalities, which strengthen the formulation and accelerate convergence. Furthermore, the Branch-and-Price framework enhances solution efficiency, particularly for medium to large-scale problems, ensuring that routing and fleet allocation are optimized dynamically. 

The effectiveness of the proposed approach was validated through extensive computational experiments, demonstrating its superiority over heuristic methods and commercial solvers in minimizing total costs and improving delivery efficiency. By successfully integrating multi-modal fleet optimization, the framework provides a scalable and practical solution for applications in e-commerce logistics, urban transportation, and sustainability-driven supply chains. In addition to cost reductions, the model enhances delivery time efficiency and 

computational performance, making it a valuable tool for modern last-mile logistics. 

We presented a novel optimization framework for multimodal last-mile delivery, demonstrating improvements in cost, delivery time, and hub utilization. Future work will focus on real-time adaptability and ML integration for predictive logistics. 

## **DECLARATIONS** 

## **_GENERATIVE-AI_** 

The authors did not use any generative AI and AI-assisted technologies in the writing process. 

## **_DATA AVAILABILITY_** 

The data are available upon request from authors. 

## **REFERENCES** 

- [1] N. Boysen, S. Schwerdfeger, and F. Weidinger, “Last-mile delivery concepts: A survey from an operational research perspective,” _OR Spect._ , vol. 43, no. 1, pp. 1–58, 2021. 

- [2] M. Savelsbergh and T. Van Woensel, “Optimization of transportation systems,” _Eur. J. Oper. Res._ , vol. 248, no. 3, pp. 701–702, 2016. 

- [3] N. Agatz, P. Bouman, and M. Schmidt, “Optimization approaches for the traveling salesman problem with drone,” _Transp. Sci._ , vol. 52, no. 4, pp. 965–981, 2018. 

- [4] J. K. Stolaroff, C. Samaras, and E. R. O’Neill, “Energy use and life cycle greenhouse gas emissions of drones for commercial package delivery,” _Nat. Commun._ , vol. 9, p. 409, Feb. 2018. 

- [5] S. Poikonen, B. Golden, and A. Assad, “The vehicle routing problem with drones: Extended models and connections,” _Networks_ , vol. 72, no. 4, pp. 464–476, 2019. 

- [6] C. C. Murray and A. G. Chu, “The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery,” _Transp. Res. C, Emerg. Technol._ , vol. 54, pp. 86–109, May 2015. 

- [7] G. Desaulniers, J. Desrosiers, and M. M. Solomon, “Accelerating strategies in column generation algorithms for vehicle routing and crew scheduling problems,” _Transp. Sci._ , vol. 36, no. 3, pp. 325–353, 2002. 

- [8] M. W. Ulmer, V. Thomas, and D. C. Mattfeld, “Anticipatory planning for courier dispatching in attended home delivery,” _Transp. Sci._ , vol. 54, no. 1, pp. 76–93, 2020. 

- [9] M. Savelsbergh and T. Van Woensel, “City logistics: Challenges and opportunities,” _Transp. Sci._ , vol. 50, no. 2, pp. 579–590, 2016. 

- [10] R. Gevaers, E. Van de Voorde, and T. Vanelslander, “Cost modelling and simulation of last-mile characteristics in an innovative B2C supply chain environment with implications on urban policy,” _Procedia-Social Behav. Sci._ , vol. 125, pp. 398–411, Mar. 2014. 

- [11] B. Golden, S. Raghavan, and E. Wasil, _The Vehicle Routing Problem: Latest Advances and New Challenges_ . New York, NY, USA: Springer, 2008. 

- [12] G. Laporte, “Fifty years of vehicle routing,” _Transp. Sci._ , vol. 43, no. 4, pp. 408–416, 2009. 

- [13] P. Toth and D. Vigo, _Vehicle Routing: Problems, Methods, and Applications_ . Philadelphia, PA, USA: SIAM, 2014. 

- [14] J.-F. Cordeau, G. Laporte, M. Savelsbergh, and D. Vigo, “Vehicle routing,” in _Handbooks in Operations Research and Management Science_ , vol. 14. Amsterdam, Netherlands: Elsevier B.V., 2007, pp. 367–428. 

- [15] J. Campbell and M. Savelsbergh, “Decision support for integrated last-mile transportation systems,” _Comput. Oper. Res._ , vol. 101, pp. 99–112, Jan. 2018. 

- [16] M. Battarra, Q. Zhang, and X. Wang, “Autonomous delivery vehicles in last-mile logistics: Challenges and future research directions,” _J. Transp. Geography_ , vol. 94, no. 1, 2021, Art. no. 102857. 

- [17] S. M. Ferrandez, T. Harbison, T. Weber, R. Sturges, and J. Rich, “Optimization of a truck-drone in tandem delivery network using k-means and genetic algorithm,” _J. Ind. Eng. Manage._ , vol. 9, no. 2, pp. 374–388, 2016. 

DANACH et al.: MULTI-MODAL LAST-MILE DELIVERY OPTIMIZATION WITH SMART MICRO-HUBS 

1611 

- [18] _DHL Trend Report: Unmanned Aerial Vehicles in Logistics_ , DHL Research Solutions, Bonn, Germany, 2020. 

- [19] S. Yurek and H. C. Ozmutlu, “A decomposition-based iterative optimization algorithm for traveling salesman problem with drone,” _Transp. Res. C Emerg. Technol._ , vol. 103, pp. 1–14, Jan. 2019. 

- [20] H. Mak, Y. Rong, and W. Tang, “Drone and truck collaborative last-mile delivery: A cost-efficient approach,” _Transp. Res. E Logist. Transp. Rev._ , vol. 147, Jan. 2021, Art. no. 102228. 

- [21] K. Leung, J. Chen, and C. Ma, “Multimodal urban last-mile delivery: Evaluating the impact of drones and electric vehicles,” _Eur. J. Oper. Res._ , vol. 302, no. 3, pp. 1109–1123, 2022. 

- [22] G. Macrina, L. Pugliese, F. Guerriero, and G. Laporte, “The last-mile delivery problem with limited drone range,” _Transp. Res. C Emerg. Technol._ , vol. 108, no. 1, pp. 281–299, 2020. 

- [23] A. Goodchild and J. Toy, “Urban freight and the last mile: Opportunities for collaboration,” _Transp. Res. A Policy Pract._ , vol. 146, pp. 131–144, Jan. 2021. 

- [24] B. Reyes, A. Kumar, and S. Yoon, “AI-driven optimization for urban last-mile logistics: A machine learning approach,” _Transp. Res. B Methodol._ , vol. 156, no. 1, pp. 87–102, 2022. 

- [25] J. R. Montoya-Torres, J. L. Franco, S. N. Isaza, H. F. Jiménez, and N. Herazo-Padilla, “A literature review on the vehicle routing problem with multiple depots,” _Comput. Ind. Eng._ , vol. 112, pp. 279–287, Jan. 2017. 

- [26] H. Li, A. V. Goodchild, X. Wang, and E. McCormack, “Optimizing the deployment of urban micro-hubs for e-commerce delivery,” _Transp. Res. E, Logist. Transp. Rev._ , vol. 149, no. 1, 2021, Art. no. 102291. 

- [27] A. Alebrahim, M. Mahmoudi, and M. Kazemi, “A multi-objective optimization approach for last-mile delivery using micro-hubs and multimodal transportation,” _J. Transp. Geography_ , vol. 98, Jan. 2022, Art. no. 103292. 

- [28] C. C. Murray and R. Raj, “Multiple traveling salesman problem with drones: Mathematical modeling and optimization,” _Comput. Oper. Res._ , vol. 115, Mar. 2020, Art. no. 104850. 

- [29] S. S. Özarik, P. da Costa, and A. M. Florio, “Machine learning for datadriven last-mile delivery optimization,” _Transp. Sci._ , vol. 58, no. 1, pp. 27–44, Oct. 2024. 

- [30] X. Li, Y. Zhang, and J. Wang, “A benders decomposition approach for electric vehicle routing with time windows,” _Eur. J. Oper. Res._ , vol. 302, no. 1, pp. 123–137, 2022. 

- [31] J. Montoya-Torres, J. Franco, and S. Isaza, “A hybrid branch-and-cut algorithm for the capacitated vehicle routing problem with drones,” _Comput. Oper. Res._ , vol. 129, Jan. 2021, Art. no. 105216. 

- [32] D. Reyes, A. Erera, and M. Savelsbergh, “Machine learning-guided adaptive large neighborhood search for multi-modal vehicle routing,” _Transp. Sci._ , vol. 56, no. 3, pp. 789–808, 2022. 

- [33] E. Yurek and H. Ozmutlu, “An iterative large neighborhood search algorithm for the vehicle routing problem with drones,” _Transp. Res. C Emerg. Technol._ , vol. 100, pp. 40–60, May 2019. 

- [34] M. Dorigo and T. Stützle, “Ant colony optimization: Overview and recent advances,” in _Handbook of Metaheuristics_ . Cham, Switzerland: Springer, 2006, pp. 227–263. 

- [35] M. Gendreau and J.-Y. Potvin, “Metaheuristics in combinatorial optimization,” _Ann. Oper. Res._ , vol. 140, pp. 189–213, 2005. 

- [36] J.-F. Cordeau and G. Laporte, “A tabu search heuristic for the static multi-depot vehicle routing problem,” _Transp. Res. B Methodol._ , vol. 35, no. 5, pp. 473–490, 2001. 

- [37] K. Danach, “Hyperheuristics in logistics,” Ph.D. dissertation, Ecole Centrale de Lille, Villeneuve-d’Ascq, France, 2016. 

- [38] R. Baldacci, A. Mingozzi, and R. Roberti, “Recent exact algorithms for solving the vehicle routing problem under capacity and time window constraints,” _Eur. J. Oper. Res._ , vol. 218, no. 1, pp. 1–6, 2010. 

- [39] K. Danach, J. A.-H. Hassan, W. Khalil, and S. Gelareh, “Routing heterogeneous mobile hospital with different patients priorities: Hyperheuristic approach,” in _Proc. 5th Int. Conf. Digit. Inf. Commun. Technol. Appl._ , 2015, pp. 155–158. 

- [40] R. N. Monemi, K. Danach, W. Khalil, S. Gelareh, F. C. Lima Jr., and D. J. Aloise, “Solution methods for scheduling of heterogeneous parallel machines applied to the workover rig problem,” _Expert Syst. Appl._ , vol. 42, no. 9, pp. 4493–4505, 2015. 

- [41] J.-F. Cordeau and G. Laporte, “Tabu search heuristics for the vehicle routing problem,” in _Metaheuristic Optimization via Memory and Evolution_ . Boston, MA, USA: Springer, 2005, pp. 145–163. 

- [42] Y. Bengio, A. Lodi, and A. Prouvost, “Machine learning for combinatorial optimization: A methodological tour d’horizon,” _Eur. J. Oper. Res._ , vol. 290, no. 2, pp. 405–421, 2021. 

- [43] M. Andres, P. Walther, and M. Reinhardt, “Predictive last-mile logistics using machine learning: Challenges and opportunities,” _Comput. Ind. Eng._ , vol. 161, no. 1, 2021, Art. no. 107678. 

- [44] B. Lin, B. Ghaddar, and J. Nathwani, “Deep reinforcement learning for the electric vehicle routing problem with time windows,” _IEEE Trans. Intell. Transp. Syst._ , vol. 23, no. 8, pp. 11528–11538, Aug. 2021. 

- [45] Ö. Aslan Yildiz, I. Sariçiçek, and A. Yazici, “A reinforcement learningbased solution for the capacitated electric vehicle routing problem from the last-mile delivery perspective,” _Appl. Sci._ , vol. 15, no. 3, p. 1068, Jan. 2025. 

- [46] W. Kool, H. Van Hoof, and M. Welling, “Attention, learn to solve routing problems!” in _Proc. Int. Conf. Learn. Represent. (ICLR)_ , 2019, pp. 1–14. 

- [47] X. Wang and J.-B. Sheu, “Vehicle routing problem with drones,” _Transp. Res. B Methodol._ , vol. 122, pp. 350–364, Apr. 2019. 

- [48] H. Bae and I. Moon, “Multi-depot vehicle routing problem with time windows considering delivery and installation vehicles,” _Appl. Math. Model._ , vol. 40, nos. 13–14, pp. 6536–6549, May 2016. 

- [49] P. Toth and D. Vigo, _The Vehicle Routing Problem_ . Philadelphia, PA, USA: Society for Industrial and Applied Mathematics, 2002, doi: 10.1137/1.9780898718515. 

