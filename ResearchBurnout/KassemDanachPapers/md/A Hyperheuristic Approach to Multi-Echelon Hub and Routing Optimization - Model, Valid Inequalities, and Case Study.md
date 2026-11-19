Received 5 January 2025; revised 19 March 2025; accepted 16 April 2025. Date of publication 29 April 2025; date of current version 24 June 2025. _Digital Object Identifier 10.1109/OJITS.2025.3565209_ 

# **A Hyperheuristic Approach to Multi-Echelon Hub and Routing Optimization: Model, Valid Inequalities, and Case Study** 

**KASSEM DANACH 1 (Member, IEEE), HASSAN HARB2 (Member, IEEE), BADIH BAZ 3, AND ABBASS NASSER 3 (Senior Member, IEEE)** 

1Basic and Applied Sciences Research Center, Al Maaref University, Beirut 5078 0025, Lebanon 

2College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait 

3Business Computing Department, Business School, Holy-Spirit University of Kaslik, Jounieh, Lebanon 

CORRESPONDING AUTHOR: A. NASSER (e-mail: abbass.nasser@usek.edu.lb) 

**ABSTRACT** Efficient logistics management is critical in the modern global supply chain, and this study introduces an advanced hyperheuristic approach to the Multi-Echelon Hub and Routing Optimization (MEHRO) problem. The MEHRO problem encompasses optimizing hub locations and vehicle routes while balancing cost efficiency, service quality, and environmental sustainability. A novel mathematical model integrates transportation, hub setup, and inventory costs, strengthened by valid inequalities to enhance computational efficiency. The hyperheuristic framework dynamically selects from a pool of lowlevel heuristics, adapting strategies to varying problem instances. A real-world case study validates the model’s effectiveness, demonstrating significant cost reductions, improved service levels, and minimized environmental impact compared to traditional methods. This work sets a foundation for scalable and adaptive solutions in logistics and combinatorial optimization, catering to the evolving demands of global supply chain management. 

**INDEX TERMS** Multi-echelon hub and routing optimization, hyperheuristics, logistics optimization, hub location problem, vehicle routing problem, valid inequalities, supply chain management. 

### **I. INTRODUCTION** 

T HE OPTIMIZATIONaspect of modern supplyof logisticschain management,networks isdrivena criticalby the increasing complexity and globalization of trade [1]. Multi-echelon logistics systems, which include multiple levels of hubs, warehouses, and distribution centers, present significant challenges due to their complex structure and the need for efficient coordination across different levels [2]. The Multi-Echelon Hub and Routing Optimization (MEHRO) problem specifically addresses these challenges by optimizing both the location of hubs and the routing of vehicles [3]. Recent advancements highlight the integration of AIdriven methodologies to enhance supply chain management, focusing on cost reduction, sustainability, and improved 

The review of this article was arranged by Associate Editor Vesna Šešum- Cavi´c.<sup>ˇ</sup> 

decision-making processes [4]. These approaches underscore the importance of leveraging advanced optimization frameworks to meet the evolving demands of logistics and supply chain management [4]. Recent research has also explored sustainable supply chain optimization within hub location models, incorporating customer segmentation to enhance efficiency. The authors in [5] proposed a hub location model that integrates sustainability considerations with customer segmentation, demonstrating how demand clustering and environmental impact assessments can improve decision-making in logistics networks. This approach aligns with our study’s emphasis on sustainability in multi-echelon hub routing optimization, further highlighting the importance of incorporating green logistics principles in modern supply chains. Additionally, the integration of hub location optimization with sustainable logistics strategies has been explored in recent studies. A study by [6] 

⃝c 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

VOLUME 6, 2025 

781 

DANACH et al.: HYPERHEURISTIC APPROACH TO MEHRO: MODEL, VALID INEQUALITIES, AND CASE STUDY 

highlights the role of advanced optimization techniques in improving multi-echelon transportation networks, emphasizing the impact of route optimization, energy-efficient transportation modes, and environmental cost considerations. These findings reinforce the significance of hyperheuristic frameworks in addressing sustainability challenges in supply chain management, aligning closely with the objectives of our study. 

Hub location problems (HLP) and vehicle routing problems (VRP) are well-established areas of research within logistics optimization [7]. The HLP focuses on selecting optimal hub locations to minimize transportation costs and improve service levels [8], [9]. Meanwhile, the VRP involves designing vehicle routes that minimize costs while satisfying constraints such as delivery time windows, vehicle capacities, and service requirements [10]. The integration of these two problems into the MEHRO problem provides a comprehensive framework for optimizing logistics networks [11]. 

Recent advancements in logistics optimization have emphasized the use of multi-echelon systems, where goods pass through multiple stages of distribution before reaching the final customer [12], [13]. This structure offers several benefits, including increased flexibility and the potential for economies of scale [14]. However, it also introduces additional complexity, particularly in coordinating the flow of goods and managing inventory across different levels [15]. Effective optimization of multi-echelon systems requires sophisticated mathematical models that can capture these complexities and provide actionable insights [16]. 

In addressing the MEHRO problem, one must consider a range of factors, including transportation costs, hub setup and operational costs, and inventory holding costs [17]. The inclusion of valid inequalities in the mathematical model can significantly enhance computational efficiency by reducing the feasible solution space and improving the convergence of optimization algorithms [18]. These valid inequalities, often derived from problem-specific constraints, help tighten the model and lead to faster and more accurate solutions [19]. 

To tackle the computational challenges posed by the MEHRO problem, this study proposes a hyperheuristic approach. Hyperheuristics are higher-level procedures that aim to select or generate heuristics to solve complex optimization problems [20]. Unlike traditional heuristics that are problem-specific, hyperheuristics operate on a broader range of problems by adapting their strategies based on the problem’s characteristics [21], [22]. This flexibility makes them particularly suitable for solving multi-objective and multi-constraint problems like the MEHRO [23]. 

The contribution of this paper is threefold. First, it presents a comprehensive mathematical model for the MEHRO problem, incorporating valid inequalities to improve solution quality and computational efficiency. Second, it introduces a hyperheuristic framework that dynamically selects from a pool of low-level heuristics, offering a versatile solution approach that adapts to different problem instances. Third, it applies the proposed methodology to a case study, 

demonstrating its practical relevance and effectiveness in real-world scenarios. 

In the following sections, we will review relevant literature on VRP, HLP, and hyperheuristics (Section II), detail the problem formulation and mathematical model (Section III), and describe the hyperheuristic framework and its implementation (Section IV). We will then present the case study and analyze the results (Sections V and VI), before concluding with a discussion on the implications of our findings and directions for future research (Sections VII and VIII). 

### **II. LITERATURE REVIEW** 

Sustainability has become a crucial aspect of logistics and supply chain management. Recent research by [24] highlights the integration of sustainable practices in logistics optimization, emphasizing the importance of eco-friendly transportation, carbon footprint reduction, and circular supply chain strategies. Their study explores how optimization techniques, including hyperheuristics, can be leveraged to balance economic efficiency and environmental responsibility. These insights align with our study’s focus on environmentally sustainable logistics operations, reinforcing the relevance of multi-echelon hub optimization in green supply chain management. 

In [25], the authors developed a multi-objective mixed integer linear programming model that considers both open and closed routes while optimizing costs, employment rate and gas emissions factors. Furthermore, the proposed model takes into account various routing types in each echelon; Augmented Epsilon Constraint (AEC) method combined with CPLEX Optimizer Solver is used to solve smallsized problem, while two metaheuristic algorithms, e.g., Non-dominated Sorting Genetic Algorithm (NSGA-II) and Multi-Objective Stochastic Fractal Search (MOSFS), are introduced to solve medium and large size problems respectively. 

The study of logistics optimization has evolved significantly, with particular attention given to Vehicle Routing Problems (VRP) and Hub Location Problems (HLP), which form the foundation of the Multi-Echelon Hub and Routing Optimization (MEHRO) problem. The VRP is a cornerstone in the field of combinatorial optimization, aiming to design optimal routes for a fleet of vehicles to service a set of customers under various constraints [10], [26]. Early formulations of the VRP, such as the classic model by Dantzig and Ramser, have been expanded to address diverse realworld complexities, including time windows [27], multiple depots [28], and heterogeneous fleets [29]. 

In parallel, the HLP focuses on determining optimal locations for hubs in a network to minimize transportation costs and improve efficiency [9], [30]. The p-hub median problem, a variant of the HLP, has been extensively studied for its applications in transportation and telecommunications [8], [31]. Hub-and-spoke systems, which leverage central hubs to streamline distribution and reduce overall costs, are a common strategy in logistics networks [9], [32]. 

VOLUME 6, 2025 

782 

Recent advances in hub location-allocation problems have also considered resilience against disruptions. The authors of [33] introduced an NSGA-II-based multi-objective optimization model that incorporates backup hub allocation to mitigate risks associated with hub failures. Their approach highlights the importance of robust decisionmaking strategies in logistics optimization, particularly in uncertain environments. This work complements our study by emphasizing the need for flexible and adaptive hub allocation methods, which align with the hyperheuristic framework employed in our model. 

The authors of [34] tackle a new trend in vehicle routing protocols by considering electric vehicles (EV) deliver items and articles to clients. To preserve EV battery capacity, they exploited the preemptive fuzzy goal programming method (PFGP) to solve small-sized vehicle network, and two metaheuristic algorithms inspired by nature, e.g., MOSA and NSGAII_TLBO, are introduced for large-sized problems. In [35], a hybrid model that combines trucks and UAVs is proposed to enable realistic and adaptive logistics planning. Such combination is demonstrated as a powerful method that enhances the performance of system while considering various weather conditions. Particularly, the model allows to minimize delivery time and cost, and uses three metaheuristic algorithms (CPLEX, NSGA-II and MOPSO) to solve small and large problems. 

Recent advancements in logistics optimization have increasingly emphasized the integration of VRP and HLP into multi-echelon systems [12], [15]. These systems, which involve multiple levels of distribution, offer enhanced flexibility and efficiency but also introduce additional layers of complexity in terms of inventory management and coordination [13], [14]. The joint optimization of hub location and vehicle routing in such systems is critical for achieving cost-effective and timely distribution [36], [37]. 

The inclusion of valid inequalities in mathematical models for these problems is a well-established technique to strengthen formulations and enhance computational efficiency [6], [18]. These inequalities help to reduce the feasible solution space, thereby speeding up the solution process and improving the accuracy of the results [19]. For example, magnanti et al. demonstrated the effectiveness of valid inequalities in capacitated facility location problems, showing substantial reductions in computation times [6]. 

The application of hyperheuristics, which are higher-level strategies that manage a set of heuristics, has gained traction as an effective approach for solving complex combinatorial problems like the MEHRO [20]. Hyperheuristics offer the advantage of generality, as they are designed to work across different problem domains without requiring significant customization [23], [38]. This adaptability is particularly valuable in logistics, where problem characteristics can vary widely based on factors such as demand patterns, network structure, and service level requirements [29], [39]. In summary, the literature underscores the critical importance of integrating VRP and HLP frameworks in 

multi-echelon logistics systems to achieve optimized hub locations and vehicle routes. The use of valid inequalities and hyperheuristics provides robust tools for tackling the inherent complexities of these problems, leading to more efficient and scalable solutions. This study builds on these foundations by proposing a comprehensive mathematical model for the MEHRO problem, enhanced with valid inequalities, and a hyperheuristic framework to dynamically select low-level heuristics, tailored to the specific characteristics of the problem instance. 

### **III. PROBLEM DEFINITION AND MATHEMATICAL MODEL** **_A. PROBLEM DESCRIPTION_** 

The Multi-Echelon Hub and Routing Optimization (MEHRO) problem is a complex logistics optimization challenge that involves determining the optimal locations for hubs and the routing of vehicles in a multi-tiered supply chain network. This network typically consists of several levels or echelons, denoted as _E_ , including suppliers, primary hubs, secondary hubs, and end customers. The MEHRO problem aims to enhance the efficiency and effectiveness of logistics operations by addressing three key components. 

Hub location involves selecting strategic locations for hubs, represented as _H_ , that serve as consolidation points where goods from various suppliers are collected, sorted, and distributed to subsequent echelons or directly to customers. The decision requires balancing the costs _Fh_ associated with establishing and operating these hubs against the benefits of reduced transportation distances _dij_ and times _tij_ . Vehicle routing focuses on designing optimal routes for a fleet of vehicles _V_ , each with a capacity _Qv_ , tasked with transporting goods between hubs and from hubs to customers. This aspect considers factors such as vehicle capacity _Qv_ , delivery time windows _Ti_ , fuel consumption _fv_ , and route length _rv_ , all of which directly impact operational costs and service quality. Inventory management, although not the primary focus of this study, influences the overall system performance by determining appropriate inventory levels _Ih_ at hubs to meet customer demand _Di_ while minimizing holding costs _hh_ and avoiding stockouts. 

The MEHRO problem is guided by three primary objectives. Cost minimization includes reducing transportation costs _cij_ , hub establishment and operational costs _Fh_ , and potentially inventory holding costs _hhIh_ . Transportation costs typically depend on factors such as distance traveled _dij_ , fuel consumption _fv_ , and vehicle utilization _uv_ , while hub costs include fixed and variable components. Service level maximization ensures customer demands _Di_ are met within specified delivery time windows _Ti_ , achieving high service levels through efficient routing to minimize delays and ensure timely deliveries. This objective may also account for the reliability of the network in meeting demand under varying conditions. Environmental impact reduction, driven by increasing emphasis on sustainability, aims to minimize the environmental footprint of logistics operations. This is achieved through optimized routing to reduce distances 

VOLUME 6, 2025 

783 

DANACH et al.: HYPERHEURISTIC APPROACH TO MEHRO: MODEL, VALID INEQUALITIES, AND CASE STUDY 

_dij_ , improve vehicle utilization _uv_ , and adopt eco-friendly vehicles or alternative fuels. 

The MEHRO problem integrates these components and objectives into a comprehensive framework, requiring a holistic approach to optimize logistics operations effectively. The following sections provide a detailed mathematical formulation of the problem, incorporating these objectives and constraints that reflect real-world logistics challenges. 

### **_B. MATHEMATICAL MODEL_** 

The MEHRO problem integrates hub location and vehicle routing decisions in a multi-echelon supply chain network. The objective is to minimize costs, maximize service levels, and reduce environmental impacts. Below is the detailed mathematical model. 

### 1) NOTATION AND DEFINITIONS 

Let the following notation be used: 

- _N_ : Set of customer locations. 

- _H_ : Set of potential hub locations. 

- _E_ : Set of echelons in the supply chain. 

- _V_ : Set of vehicles. 

- _Cij_ : Transportation cost between locations _i_ and _j_ . 

- _Di_ : Demand at customer location _i_ . 

- _Qv_ : Capacity of vehicle _v_ . 

- _Fh_ : Fixed cost of establishing hub _h_ . 

- _Ti_ : Maximum allowable delivery time window for customer _i_ . 

- _Sh_ : Service level target at hub _h_ . 

- _Eij_ : Emission factor per unit distance between locations _i_ and _j_ . 

### 2) DECISION VARIABLES 

- _xij_<sup>_v_:Binaryvariableequalto1ifvehicle</sup><sup>_v_travelsfrom</sup> location _i_ to _j_ , 0 otherwise. 

- _yh_ : Binary variable equal to 1 if hub _h_ is established, 0 otherwise. 

- _zih_ : Binary variable equal to 1 if customer _i_ is assigned to hub _h_ , 0 otherwise. 

- _qiv_ : Quantity delivered to customer _i_ by vehicle _v_ . 

- _tij_<sup>_v_:Traveltimeofvehicle</sup><sup>_v_fromlocation</sup><sup>_i_to</sup><sup>_j_.</sup> 

The second objective (Equation (2)) seeks to maximize the service level, represented by the reliability and timeliness of deliveries. The term _Shyh_ ensures that service levels at hubs are considered, while _(Ti_ − _tij_<sup>_v)x_</sup> _ij_<sup>_v_penalizesdeliveriesthat</sup> approach the maximum allowable time window _Ti_ . 

_c: Environmental Impact Reduction_ 



<!-- Start of picture text -->
min � Eijxij v (3)<br>i ∈ N,j ∈ N,v ∈ V<br><!-- End of picture text -->

The third objective (Equation (3)) focuses on minimizing environmental impacts, specifically carbon emissions, which are proportional to the distance traveled and the emission factor _Eij_ between locations _i_ and _j_ . 

### 4) CONSTRAINTS 

The model is subject to the following constraints: 

_a: Flow Conservation_ 



<!-- Start of picture text -->
� xij v = 1 ∀ i  ∈ N, v  ∈ V (4)<br>j ∈ N<br><!-- End of picture text -->



<!-- Start of picture text -->
� xij v = 1 ∀ j  ∈ N, v  ∈ V (5)<br>i ∈ N<br><!-- End of picture text -->

Equations (4) and (5) ensure that each customer is served exactly once by a vehicle and that vehicles maintain consistent routing. 

_b: Hub Assignment_ 



<!-- Start of picture text -->
zih ≤ yh ∀ i  ∈ N, h  ∈ H (6)<br>� zih = 1 ∀ i  ∈ N (7)<br>h ∈ H<br><!-- End of picture text -->

Equation (6) ensures that customers are only assigned to established hubs, and Equation (7) guarantees that each customer is assigned to exactly one hub. 

_c: Vehicle Capacity_ 



<!-- Start of picture text -->
� qiv ≤ Qv ∀ v  ∈ V (8)<br>i ∈ N<br><!-- End of picture text -->

Equation (8) restricts the total quantity delivered by each vehicle to its capacity _Qv_ . 

_d: Delivery Time Windows_ 

### 3) OBJECTIVE FUNCTIONS 

The MEHRO problem has three primary objectives: 

_a: Cost Minimization_ 



<!-- Start of picture text -->
min � Fhyh  + � Cijxij v + � � Dizih (1)<br>h ∈ H i ∈ N,j ∈ N,v ∈ V h ∈ H i ∈ N<br><!-- End of picture text -->

This objective (Equation (1)) aims to minimize the total cost, including the fixed costs of establishing hubs _(Fh)_ , transportation costs _(Cij)_ , and any additional costs associated with customer assignments to hubs _(Di)_ . 

_b: Service Level Maximization_ 



<!-- Start of picture text -->
max � Shyh  − � � Ti  − tij v � xij v (2)<br>h ∈ H i ∈ N,v ∈ V<br><!-- End of picture text -->



<!-- Start of picture text -->
tij v ≤ Ti ∀ i, j  ∈ N, v  ∈ V (9)<br><!-- End of picture text -->

Equation (9) ensures that deliveries are made within the specified time windows _Ti_ . 

_e: Binary and Non-negativity Constraints_ 



<!-- Start of picture text -->
xij v , yh, zih ∈{0 ,  1} (10)<br><!-- End of picture text -->



<!-- Start of picture text -->
qiv, tij v ≥ 0 (11)<br><!-- End of picture text -->

Equations (10) and (11) enforce the binary nature of decision variables related to routing, hub establishment, and customer assignment, and the non-negativity of quantities and travel times. 

VOLUME 6, 2025 

784 

### **_C. VALID INEQUALITIES_** 

Valid inequalities are additional constraints added to the mathematical model to strengthen the formulation and improve the computational efficiency of solving the MEHRO problem. These inequalities help to tighten the feasible region, reducing the solution space and potentially accelerating the convergence of optimization algorithms. 

### 1) DEVELOPMENT OF VALID INEQUALITIES 

To enhance the model, we introduce the following valid inequalities: 

_a: Hub Capacity Constraint_ For practical scenarios, hubs have a limited capacity in terms of the volume of goods they can handle. This capacity can be related to physical storage space, processing capabilities, or transportation limits. The inequality can be expressed as: 



<!-- Start of picture text -->
� Dizih ≤ Chyh ∀ h  ∈ H (12)<br>i ∈ N<br><!-- End of picture text -->

where _Ch_ is the capacity of hub _h_ . This inequality ensures that the total demand assigned to a hub does not exceed its capacity. 

_b: Minimum Load Constraint on Vehicles_ To prevent inefficient vehicle utilization, we can impose a minimum load constraint. This constraint ensures that vehicles are not dispatched with loads significantly below their capacity, which helps to reduce the number of trips and associated costs. It can be expressed as: 



<!-- Start of picture text -->
� qiv ≥ αQv ∀ v  ∈ V (13)<br>i ∈ N<br><!-- End of picture text -->

where _α_ is a fraction representing the minimum load factor (e.g., 0.5 for 50). 

_c: Connectivity and Path Validity Constraints_ To ensure that each hub is connected to at least one customer and that the network is fully operational, the following inequality is introduced: 



<!-- Start of picture text -->
� xij v =  zih ∀ i  ∈ N, v  ∈ V, h  ∈ H (14)<br>j ∈ N<br><!-- End of picture text -->

This inequality ensures that if a customer _i_ is assigned to a hub _h_ , then at least one vehicle must serve that customer, maintaining k2 the network’s operational integrity. 

### 2) THEORETICAL JUSTIFICATION OF VALID INEQUALITIES 

The introduction of valid inequalities is justified on both practical and theoretical grounds. They enhance the model by: 

- Reducing Feasible Solutions: By tightening the bounds on variables, these inequalities reduce the number of feasible solutions that need to be considered, thereby speeding up the optimization process. 

- Improving Solution Quality: Valid inequalities help to avoid suboptimal solutions that may satisfy the basic 

- constraints but are impractical or inefficient in realworld applications. 

- Facilitating Convergence: These inequalities often lead to faster convergence in optimization algorithms, especially in branch-and-bound or branch-and-cut frameworks, by pruning non-promising branches early in the solution process. 

In summary, valid inequalities are crucial for enhancing the computational efficiency and practical relevance of the MEHRO model. They not only streamline the solution process but also ensure that the solutions are more aligned with real-world operational constraints. 

### **IV. SOLUTION APPROACH: HYPERHEURISTIC FRAMEWORK** 

### **_A. HYPERHEURISTIC OVERVIEW_** 

Hyperheuristics are a high-level search methodology that operates over a set of heuristics to solve complex optimization problems. Unlike traditional heuristics, which are often designed for specific problems, hyperheuristics are problem-independent and focus on selecting or generating heuristics based on the characteristics of the problem instance at hand. This approach offers several advantages, including greater flexibility, adaptability, and the ability to generalize across various problem domains [20], [38]. 

The primary advantage of using hyperheuristics in the MEHRO problem lies in their capacity to dynamically adapt to different problem scenarios and efficiently explore the solution space. By leveraging a diverse set of low-level heuristics, hyperheuristics can switch strategies based on the problem’s needs, potentially leading to more robust and highquality solutions. 

### **_B. FRAMEWORK DESIGN_** 

The design of a hyperheuristic framework involves two main components: the selection of low-level heuristics and the mechanism for choosing among them. 

### 1) LOW-LEVEL HEURISTICS 

Low-level heuristics are the fundamental building blocks of optimization processes, directly manipulating the solution space to improve solution quality. In the context of the Multi-Echelon Hub and Routing Optimization (MEHRO) problem, these heuristics are categorized into constructive, improvement, and perturbation heuristics. 

Constructive heuristics are used to build initial solutions by incrementally adding elements based on specific criteria. For example, the nearest-neighbor heuristic constructs routes for vehicles _v_ ∈ _V_ by iteratively selecting the nearest unvisited location _j_ from the current position _i_ , minimizing the distance _dij_ . The savings heuristic constructs routes by merging customer pairs _i, j_ ∈ _N_ that minimize the combined travel cost _cij_ , ensuring that vehicle capacities _Qv_ and delivery time windows _Ti_ are respected. These heuristics prioritize feasibility and provide a solid foundation for further refinement. 

VOLUME 6, 2025 

785 

DANACH et al.: HYPERHEURISTIC APPROACH TO MEHRO: MODEL, VALID INEQUALITIES, AND CASE STUDY 

## **Algorithm 1** Relocate Heuristic 

**Require:** Current solution _S_ , set of customers _N_ , set of hubs _H_ , cost function _C(S)_ , service metrics _M(S)_ **Ensure:** Updated solution _S_ with optimized costs and service metrics 1: Initialize _S_<sup>←</sup> _S_ 

- 2: **for all** customer _i_ ∈ _N_ **do** 

- 3: Identify current hub or route _h_ 1 assigned to customer _i_ 4: **for all** hub _h_ 2 ∈ _H_ \ { _h_ 1} **do** 5: Temporarily reassign customer _i_ from _h_ 1 to _h_ 2 6: Update the temporary solution _S_ temp 7: **if** _C(S_ temp _) < C(S)_ **or** _M(S_ temp _) > M(S)_ **then** 8: Update _S_<sup>←</sup> _S_ temp 9: **end if** 

- 10: **end for** 11: **end forreturn** _S_ 

Improvement heuristics refine existing solutions by systematically exploring their neighborhoods. Several techniques are commonly used: 

- 2-Opt Heuristic: This method improves routing solutions by iteratively removing two edges in a route and reconnecting them to eliminate overlaps and reduce total travel distance _dij_ . For example, given a route _(i, j, k, l)_ , the edges _(i, j)_ and _(k, l)_ are replaced with _(i, k)_ and _(j, l)_ if the change reduces total costs. 

- 3-Opt Heuristic: Extending the 2-opt, this heuristic removes three edges and reconnects them in the most cost-effective configuration. It explores a broader neighborhood, enhancing the ability to escape local optima at the cost of increased computational time. 

- Swap Heuristic: This heuristic swaps two customer assignments between routes or hubs to reduce overall transportation costs _cij_ or balance vehicle loads _Qv_ . For example, customers _i_ and _j_ assigned to hubs _h_ 1 and _h_ 2 respectively, are exchanged if it results in lower costs or better service levels. 

- Relocate Heuristic: A customer _i_ is removed from its current hub _h_ 1 or route and reassigned to a different hub _h_ 2 or route if the reassignment reduces costs or improves service metrics, as detailed in Algorithm 1. 

Perturbation heuristics are employed to escape local optima by introducing controlled disruptions to the current solution. These methods allow the exploration of new regions in the solution space: 

- Random Reassignment: Customers _i_ ∈ _N_ are randomly reassigned to different hubs _h_ ∈ _H_ or routes, regardless of immediate cost implications. This method increases diversity in the solution space, enabling the discovery of alternative configurations. 

- Cluster-Based Reassignment: Customers are grouped into clusters based on proximity or demand similarity, and entire clusters are reassigned to different hubs. This perturbation heuristic focuses on large-scale modifications, making significant changes to the solution structure. 

**Algorithm 2** Route Splitting and Merging Heuristic **Require:** Current set of routes _R_ = { _r_ 1 _, r_ 2 _, . . . , rk_ }, cost function _C(S)_ , vehicle capacity _Qv_ , and service levels. **Ensure:** Updated set of routes _R_ with balanced load capacities and optimized costs. 

1: Initialize _R_<sup>←</sup> _R_ 2: **for all** route _ri_ ∈ _R_ **do** 3: Compute load _L(ri)_ and cost _C(ri)_ for route _ri_ 4: **if** _L(ri) > Qv_ **then** 5: Split _ri_ into sub-routes { _ri_<sup>1</sup><sup>_, r_</sup> _i_<sup>2</sup><sup>_, . . ._}ensuringeachsub-</sup> route satisfies _L(ri_<sup>_j)_≤</sup><sup>_Qv_</sup> 6: Update _R_ temp ← _R_<sup>\</sup> { _ri_ } ∪{ _ri_<sup>1</sup><sup>_, r_</sup> _i_<sup>2</sup><sup>_, . . ._}</sup> 7: **if** _C(R_ temp _) < C(R)_ **then** 8: Update _R_<sup>←</sup> _R_ temp 9: **end if** 10: **end if** 11: **end for** 12: **for all** pairs of routes _ri, rj_ ∈ _R_ **do** 13: **if** _L(ri)_ + _L(rj)_ ≤ _Qv_ **then** 14: Merge _ri_ and _rj_ into a single route _r_ merged 15: Update _R_ temp ← _R_<sup>\</sup> { _ri, rj_ } ∪{ _r_ merged} 16: **if** _C(R_ temp _) < C(R)_ **then** 17: Update _R_<sup>←</sup> _R_ temp 18: **end if** 19: **end if** 20: **end for return** _R_ 

- Route Splitting and Merging: Existing vehicle routes are split into smaller sub-routes or merged into larger ones to explore the impact on total costs _cij_ , vehicle utilization _uv_ , and service levels. This technique is particularly effective in balancing load capacities across vehicles, as detailed in Algorithm 2. 

- Shuffle Heuristic: Randomly rearranges the order of customers within a route, effectively altering delivery sequences and exploring different route configurations. This can uncover better arrangements for time window compliance _Ti_ . 

By combining constructive, multiple improvement, and diverse perturbation heuristics, the MEHRO problem can be addressed effectively. The interplay between these heuristics ensures flexibility in handling varying problem complexities and enhances the robustness of the solution process. 

### 2) HEURISTIC SELECTION MECHANISM 

The process of selecting the most appropriate low-level heuristic at any stage of the optimization process is critical for achieving high-quality solutions. In the context of the Multi-Echelon Hub and Routing Optimization (MEHRO) problem, a reinforcement learning-based heuristic selection mechanism is employed to dynamically adapt to the problem’s complexity and characteristics. 

Reinforcement learning (RL) provides a robust framework for dynamic decision-making, consisting of an agent, a set of actions, a state space, and a reward function. In this context, the RL agent acts as the heuristic selection 

VOLUME 6, 2025 

786 

mechanism, tasked with choosing the most suitable lowlevel heuristic based on the current state of the solution. The available actions correspond to applying one of the low-level heuristics, and the state space captures the key properties of the solution, such as cost, vehicle utilization, and service level. The Q-learning algorithm is employed to guide the heuristic selection process. Q-learning is a model-free RL method that learns an optimal policy by iteratively updating a Q-value table, where each entry _Q(S, a)_ represents the expected cumulative reward of taking action _a_ in state _S_ . 

At each time step _t_ , the state _St_ is represented by features of the current solution, including total transportation cost, the number of active hubs, average route length, and the level of unmet demand. These features encapsulate the solution’s quality and guide heuristic selection. The action space _At_ comprises a set of low-level heuristics, including constructive heuristics such as nearest neighbor methods, improvement heuristics like 2-opt, 3-opt, or swap operations, and perturbation heuristics such as random reassignment or route splitting. 

After applying an action _at_ ∈ _At_ , the system transitions to a new state _St_ +1, and a reward _Rt_ is calculated. The reward reflects the improvement in solution quality. Positive rewards are assigned for reductions in total transportation cost, improved service levels, or reduced unmet demand. Conversely, negative rewards are given if the solution quality deteriorates. The Q-learning update rule adjusts the Q-values as follows: 



<!-- Start of picture text -->
Q(St, at)  ← Q(St, at)<br>+ α Rt  +  γ max Q(St +1 , a) − Q(St, at) ,<br>� a �<br><!-- End of picture text -->

where _α_ is the learning rate, _γ_ is the discount factor, and _Rt_ is the reward at time _t_ . The term max _a Q(St_ +1 _, a)_ represents the highest Q-value for the subsequent state _St_ +1, accounting for future rewards. 

The heuristic selection mechanism balances exploration and exploitation using an _ϵ_ -greedy strategy. At each step, the agent selects a random action with probability _ϵ_ to explore new heuristics; otherwise, it chooses the action with the highest Q-value for the current state. Over time, the exploration rate _ϵ_ decays to favor exploitation, ensuring that the agent increasingly relies on learned knowledge to optimize decisions. 

The workflow begins by initializing the Q-value table _Q(S, a)_ , the learning rate _α_ , discount factor _γ_ , and exploration rate _ϵ_ . The initial solution is represented as state _S_ 0. At each iteration, the current state _St_ is extracted based on the solution features, an action _at_ is selected using the _ϵ_ -greedy policy, and the selected heuristic is applied to generate a new solution. The system transitions to a new state _St_ +1, the reward _Rt_ is computed, and the Q-value is updated using the Q-learning rule. This process repeats until a termination criterion is met, such as a maximum number of iterations or convergence to an optimal solution. The best solution _S_ observed during the process is returned as the final result. 

By leveraging Q-learning, the heuristic selection mechanism dynamically adapts to the problem’s complexity, applying the most effective heuristic at each stage of the optimization process. This approach enhances the ability to navigate the solution space, balancing exploration and exploitation to achieve high-quality solutions for the MultiEchelon Hub and Routing Optimization problem. 

The reinforcement learning-based heuristic selection mechanism ensures adaptability and efficiency by learning from past decisions and continuously improving its performance. By dynamically selecting the most suitable heuristic, the mechanism can navigate the solution space more effectively, overcoming local optima and addressing the complex trade-offs inherent in the MEHRO problem. 

The hyperheuristic framework dynamically selects from a diverse pool of constructive, improvement, and perturbation heuristics, ensuring adaptability to varying problem instances. The selection process is governed by a reinforcement learning-based approach or a rule-based adaptive mechanism that evaluates the effectiveness of different heuristics based on key solution state indicators, such as cost reduction, service level enhancement, and convergence rate. For instance, if a route restructuring heuristic results in a marginal improvement in cost but leads to violations of the time window constraints, the framework intelligently adapts by shifting towards an alternative heuristic, such as a swap-based or 2-opt heuristic. This transition ensures that the optimization process refines the routing solution without compromising feasibility, thus maintaining an effective balance between cost efficiency and service quality. The adaptive nature of this selection mechanism significantly enhances the robustness of the proposed hyperheuristic approach in solving complex logistics optimization problems. 

### **V. GENERATED INSTANCE AND CASE STUDY** **_A. INSTANCE GENERATION_** 

To evaluate the effectiveness of the proposed hyperheuristic framework, a set of problem instances was generated based on realistic logistics scenarios. The methodology for generating these instances involves several key steps: 

- _Network Design:_ Define a network of potential hub locations, customer locations, and echelons. The network is structured hierarchically, with primary hubs receiving goods from suppliers and secondary hubs or customers receiving goods from primary hubs. 

- _Parameter Initialization:_ Set parameters such as transportation costs _(Cij)_ , hub setup costs _(Fh)_ , demand at each customer location _(Di)_ , vehicle capacities _(Qv)_ , and time windows _(Ti)_ . These parameters are based on typical logistics costs, vehicle specifications, and service level requirements in the industry. 

- _Demand and Capacity Allocation:_ Generate random but realistic demand data for each customer and assign capacity limits to each hub and vehicle. The distribution of demand can follow a normal distribution to simulate 

VOLUME 6, 2025 

787 

DANACH et al.: HYPERHEURISTIC APPROACH TO MEHRO: MODEL, VALID INEQUALITIES, AND CASE STUDY 

variability, while capacity limits are set to reflect constraints in real-world logistics operations. 

- _Environmental Data:_ Include environmental factors such as emission factors _(Eij)_ to account for the carbon footprint of transportation activities. These factors are calculated based on the type of vehicles used and the distance traveled. 

The generated instances are designed to test the hyperheuristic framework under various conditions, such as varying network sizes, demand patterns, and service level requirements. This diversity ensures a comprehensive evaluation of the framework’s robustness and adaptability. 

### **_B. CASE STUDY APPLICATION_** 

The hyperheuristic framework was applied to one of the generated instances to demonstrate its practical application and effectiveness. The case study focuses on a medium-sized logistics network with the following characteristics: 

- _Network Composition:_ 10 potential hub locations, 50 customer locations, and 5 vehicle types with different capacities and emission profiles. 

- _Objective Prioritization:_ The primary objective was cost minimization, followed by service level maximization and environmental impact reduction. 

- _Scenario Variations:_ Several scenarios were tested, including different levels of demand variability, varying service level requirements, and different vehicle capacities. 

### 1) APPLICATION OF THE HYPERHEURISTIC FRAMEWORK 

The hyperheuristic framework utilized a combination of greedy heuristics, local search methods, and metaheuristicbased approaches to navigate the solution space. The high-level selection mechanism employed a learning-based approach, where heuristic performance data were used to inform future selections. 

### 2) EVALUATION METRICS AND COMPARATIVE ANALYSIS 

The performance of the hyperheuristic framework was evaluated using several metrics: 

- _Total Cost:_ Including transportation, hub setup, and operational costs. 

- _Service Level:_ Measured by the percentage of deliveries made within the specified time windows. 

- _Environmental Impact:_ Assessed based on total emissions resulting from transportation activities. 

- _Computational Efficiency:_ Evaluated in terms of computation time and resources used. 

The results were compared against a baseline solution derived using traditional heuristics and an exact optimization approach. The hyperheuristic framework demonstrated superior performance in balancing cost, service level, and environmental impact, particularly in scenarios with high demand variability and strict service requirements. 

**TABLE 1. Performance metrics comparison.** 





**TABLE 2. Sensitivity analysis results.** 



In summary, the case study illustrates the practical application of the hyperheuristic framework and its ability to provide high-quality solutions in complex logistics networks. The framework’s adaptability to different scenarios and its effectiveness in optimizing multiple objectives make it a valuable tool for decision-makers in the logistics industry. 

### **VI. RESULTS AND ANALYSIS** 

### **_A. PRESENTATION OF COMPUTATIONAL RESULTS_** 

The computational results demonstrate the effectiveness of the hyperheuristic framework compared to traditional heuristics, specifically the Nearest Neighbor Heuristic and the Savings Algorithm. These traditional heuristics were chosen for their common use in logistics optimization due to their simplicity and speed. Key performance metrics are summarized in Table 1. 

As shown in Table 1, the hyperheuristic framework reduced the total cost by 15%, improved the service level by 9.4%, and lowered total emissions by 12% compared to the traditional heuristics. Additionally, the computation time decreased by 16.7%, indicating increased efficiency in solving complex logistics problems. 

### **_B. SENSITIVITY ANALYSIS AND DISCUSSION OF FINDINGS_** 

A sensitivity analysis was conducted to understand the impact of varying key parameters on the performance of the hyperheuristic framework. The results are presented in Table 2. 

Table 2 shows the following impacts: 

- _Demand Variability:_ The hyperheuristic framework maintained stable performance, with only a 2% increase in costs and a 1% decrease in service levels under demand variability. 

- _Vehicle Capacity Constraints:_ A reduction in vehicle capacity to 80% resulted in a 3% increase in costs and a 2% decrease in service levels, reflecting the sensitivity to logistical capacity constraints. 

VOLUME 6, 2025 

788 

- _Environmental Weighting:_ Increasing the weight of environmental considerations in the optimization objective led to a 4% increase in costs, but provided a better balance between cost and emissions reduction. 

These results highlight the framework’s robustness and its ability to balance different operational goals under varying conditions. 

### **_C. BENCHMARKING AND COMPARATIVE ANALYSIS_** 

To further validate the effectiveness of the proposed hyperheuristic framework, a comparative analysis was conducted against a Genetic Algorithm (GA), a widely used metaheuristic for combinatorial optimization problems. The GA was selected due to its strong performance in logistics optimization and its ability to handle large-scale problems through evolutionary search. 

The GA implementation followed a traditional structure comprising selection, crossover, and mutation operators. The initial population was generated randomly, ensuring diversity in the solution space. A tournament selection strategy was employed to maintain a balance between exploration and exploitation. The crossover mechanism used a two-point crossover operator to recombine parent solutions, while mutation introduced small perturbations to avoid premature convergence. The stopping criterion was defined as either reaching a maximum number of generations _(_ 500 _)_ or the absence of significant improvement over 50 consecutive iterations. 

For a fair comparison, both hyperheuristic framework and GA were tested on identical problem instances, consisting of multi-echelon hub networks with varying transportation costs, service level constraints, and environmental impact factors. The algorithms were implemented in Python, utilizing the DEAP library for GA and a custom-built hyperheuristic selection mechanism. All experiments were conducted on a system with an Intel Core _i_ 9 − 12900K processor, 32GB RAM, and a computational limit of 3000 seconds per run. 

Table 3 presents the comparative performance metrics, including total cost, service level, computational time, and convergence behavior. The results indicate that the hyperheuristic framework outperforms the GA in both total cost and service level while also reducing computational time by nearly 46.4%. The faster convergence of the hyperheuristic is attributed to its adaptive heuristic selection mechanism, which dynamically adjusts to problem characteristics rather than relying on a fixed set of evolutionary operators. In contrast, GA exhibited slow convergence with frequent oscillations, particularly in larger problem instances, due to the reliance on probabilistic mutation and crossover for solution refinement. One key advantage observed in the hyperheuristic approach is its ability to maintain solution feasibility throughout iterations, whereas GA frequently generated infeasible solutions requiring constraint-handling techniques. This was particularly evident in scenarios with tight service-level constraints, where GA 

**TABLE 3. Comparison of hyperheuristic framework and genetic algorithm.** 



struggled to balance cost minimization with time-window compliance. The hyperheuristic’s structured heuristic selection process allowed for efficient adjustments, ensuring that routes remained optimized while meeting operational constraints. 

The computational complexity of both methods was also analyzed. While GA’s iterative nature and population-based search required significantly more function evaluations, the hyperheuristic framework leveraged problem-specific heuristic combinations, reducing redundant computations. This difference is especially important for large-scale logistics applications, where scalability and real-time decision-making are crucial. 

Overall, the findings reinforce the effectiveness of hyperheuristics in adaptive logistics optimization, particularly in environments with dynamic constraints and multiobjective trade-offs. The superior computational efficiency and enhanced service level compliance suggest that hyperheuristics provide a more practical solution for large-scale logistics networks compared to traditional evolutionary approaches. 

### **VII. DISCUSSION** 

### **_A. INSIGHTS AND PRACTICAL IMPLICATIONS_** 

The study reveals several key insights into the application of hyperheuristics in logistics optimization: 

- _Adaptability and Flexibility:_ The hyperheuristic framework effectively adapts to changing conditions, such as varying demand and vehicle capacities, making it suitable for dynamic logistics environments. 

- _Holistic Decision-Making:_ By integrating multiple objectives, including cost, service level, and environmental impact, the framework facilitates comprehensive decision-making that aligns with both operational and sustainability goals. 

- _Scalability:_ The framework’s efficient handling of different problem scales, from small to large, suggests its broad applicability across various logistics sectors and company sizes. 

### **_B. CONNECTION TO REAL-WORLD APPLICATIONS_** 

While the experiments have demonstrated its effectiveness in the taken case study, our proposed hyperheuristic framework is inherently flexible and can be adapted to various geographical regions and industries with different operational requirements. For instance, in e-commerce logistics, where rapid order fulfillment and last-mile delivery efficiency are critical, the model can be tailored by incorporating dynamic demand patterns and real-time traffic constraints. 

VOLUME 6, 2025 

789 

DANACH et al.: HYPERHEURISTIC APPROACH TO MEHRO: MODEL, VALID INEQUALITIES, AND CASE STUDY 

Similarly, in healthcare logistics, where timely and reliable distribution of medical supplies is essential, the approach can accommodate strict service-level requirements and regulatory constraints. Additionally, the model ability to handle multiechelon hub and routing optimization makes it suitable for geographically diverse networks, where transportation infrastructure and cost structures vary significantly. These adaptations demonstrate the broader applicability of our framework, making it a valuable tool for decision-makers across multiple domains. 

### **_C. LIMITATIONS AND FUTURE RESEARCH DIRECTIONS_** 

Despite its strengths, the hyperheuristic framework has certain limitations: 

- _Computational Demands:_ While the framework is efficient, solving larger instances can still be computationally intensive, potentially limiting its use in real-time applications. 

- _Parameter Sensitivity:_ The performance is sensitive to the parameters set for the various heuristics and objective weights, which requires careful tuning to ensure optimal results. 

- _Potential for Model Enhancement:_ Future research could explore more complex constraints, such as incorporating multi-modal transportation, real-time data analytics, and adaptive demand forecasting to further improve model accuracy and applicability. 

Additionally, integrating machine learning techniques for better heuristic selection and enhancing the framework’s adaptability could lead to further improvements in both efficiency and solution quality. 

### **VIII. CONCLUSION** 

This study presents an advanced hyperheuristic framework for optimizing multi-echelon hub and routing systems, addressing the critical challenges faced in modern logistics networks. By integrating a comprehensive mathematical model, strengthened with valid inequalities, and a dynamic heuristic selection mechanism, the proposed approach demonstrates its ability to achieve significant improvements in cost reduction, service level enhancement, and environmental sustainability. 

The hyperheuristic framework’s ability to adapt dynamically to varying problem instances highlights its flexibility and robustness in addressing complex multi-objective optimization problems. Comparative analyses validate its effectiveness, particularly in benchmarking against a Genetic Algorithm (GA). The results indicate that the hyperheuristic outperforms GA in terms of total cost, service level, and computational efficiency, with a 46.4% reduction in runtime and faster, more stable convergence. The hyperheuristic’s adaptive heuristic selection mechanism enables solution feasibility retention and constraint satisfaction, unlike GA, which often generates infeasible solutions requiring extensive adjustments. 

The study also highlights the computational efficiency and scalability of the proposed approach, making it suitable for large-scale logistics networks. Unlike population-based metaheuristics, which rely on extensive function evaluations, the hyperheuristic framework leverages problem-specific heuristic combinations, significantly reducing redundant computations. This efficiency makes it a more practical choice for real-time logistics optimization, where adaptability and responsiveness are critical. 

Future work can explore integrating real-time data analytics and dynamic demand adjustments, enhancing the framework’s ability to handle evolving logistical constraints. Additionally, the incorporation of multi-modal transportation networks and hybrid hyperheuristic-metaheuristic models could further improve solution quality and robustness. Extending the model to accommodate uncertain and timesensitive environments will enable its application across a broader range of industries, including e-commerce, healthcare logistics, and disaster relief operations. This study lays a strong foundation for continued innovation in logistics optimization, reinforcing the role of hyperheuristics as a powerful tool for operational efficiency, adaptability, and sustainability. 

### **REFERENCES** 

- [1] M. Christopher, _Logistics and Supply Chain Management_ . London, U.K.: Financial Times Management, 1992. 

- [2] D. Carlsson, “Optimization in multi-echelon supply chain networks,” _Eur. J. Oper. Res._ , vol. 224, no. 3, pp. 419–428, 2013. 

- [3] M. S. Daskin, _Network and Discrete Location: Models, Algorithms, and Applications_ . Hoboken, NJ, USA: Wiley, 2002. 

- [4] K. Danach, A. E. Dirani, and H. Rkein, “Revolutionizing supply chain management with AI: A path to efficiency and sustainability,” _IEEE Access_ , vol. 12, pp. 1–15, 2024. [Online]. Available: https://ieeexplore. ieee.org/abstract/document/10705303 

- [5] A. Heidari, D. M. Imani, and M. Khalilzadeh, “A hub location model in the sustainable supply chain considering customer segmentation,” _J. Eng., Design Technol._ , vol. 19, no. 6, pp. 1387–1420, 2021. 

- [6] T. L. Magnanti, P. B. Mirchandani, and R. T. Wong, “Accelerating benders decomposition: Algorithmic enhancements and model selection criteria,” _Oper. Res._ , vol. 34, no. 3, pp. 281–296, 1986. 

- [7] K. Danach, S. Gelareh, and R. Neamatian Monemi, “The capacitated single-allocation p-hub location routing problem: A lagrangian relaxation and a hyper-heuristic approach,” _EURO J. Transp. Logist._ , vol. 8, no. 5, pp. 597–631, 2019. [Online]. Available: https://www. sciencedirect.com/science/article/pii/S2192437620300388 

- [8] J. F. Campbell, “Hub location and the p-hub median problem,” _Oper. Res._ , vol. 42, no. 4, pp. 923–935, 2002. 

- [9] R. O’Kelly and J. F. Campbell, “Hub location problems in transportation,” in _Transportation_ . Amsterdam, The Netherlands: Elsevier, 2007, pp. 537–552. 

- [10] P. Toth and D. Vigo, _The Vehicle Routing Problem_ (Monographs on Discrete Mathematics and Applications). Philadelphia, PA, USA: SIAM, 2002. 

- [11] J. F. Bard and J. A. Feinberg, “A decomposition algorithm for the inventory routing problem,” _Transp. Res. B, Methodol._ , vol. 36, no. 5, pp. 443–458, 2002. 

- [12] Z. J. M. Shen, C. R. Coullard, and M. S. Daskin, “A joint locationinventory model,” _Transp. Sci._ , vol. 37, no. 1, pp. 40–55, 2003. 

- [13] X. Guo and W. M. P. van der Aalst, “Multi-echelon supply chain inventory optimization with service level constraints,” _Comput. Oper. Res._ , vol. 36, no. 11, pp. 3122–3132, 2009. 

- [14] T. G. Crainic and K. H. Kim, “Service network design,” in _Transportation_ . Amsterdam, The Netherlands: Elsevier, 2004, pp. 375–406. 

VOLUME 6, 2025 

790 

- [15] B. Liu, Y. Chen, and Y. Wan, “Supply chain coordination with quantity discount policy under stochastic demand,” _Comput. Ind. Eng._ , vol. 66, no. 3, pp. 634–642, 2013. 

- [16] A. Amiri, “Designing a distribution network in a supply chain system: Formulation and efficient solution procedure,” _Eur. J. Oper. Res._ , vol. 171, no. 2, pp. 567–576, 2006. 

- [17] J. F. Campbell and M. E. O’Kelly, “Twenty-five years of hub location research,” _Transp. Sci._ , vol. 39, no. 2, pp. 195–222, 2005. 

- [18] A. M. Costa, J. F. Oliveira, and E. Mendes, “Applications of integer programming in production planning and scheduling,” _Eur. J. Oper. Res._ , vol. 201, no. 3, pp. 909–914, 2010. 

- [19] I. Contreras and E. Fernandez, “Branch and price for large-scale capacitated hub location problems with single assignment,” _INFORMS J. Comput._ , vol. 24, no. 1, pp. 147–162, 2012. 

- [20] E. K. Burke et al., “Hyper-heuristics: A survey of the state of the art,” _J. Oper. Res. Soc._ , vol. 64, no. 12, pp. 1695–1724, 2013. 

- [21] J. H. Drake, E. K. Burke, and G. Kendall, “An examination of layering in hyper-heuristics applied to bin packing,” in _Evolutionary Computation in Combinatorial Optimization_ . Cham, Switzerland: Springer, 2010, pp. 276–287. 

- [22] K. Danach, “Hyperheuristics in logistics,” Ph.D. dissertation, Université de Lille, Lille, France, 2016. [Online]. Available: https:// theses.hal.science/tel-01485160 

- [23] L. López-Ibáñez and T. Stützle, “The ant colony optimization metaheuristic for the permutation flowshop scheduling problem,” _Comput. Oper. Res._ , vol. 39, no. 3, pp. 823–835, 2012. 

- [24] A. Heidari, D. M. Imani, M. Khalilzadeh, and M. Sarbazvatan, “Green two-echelon closed and open location-routing problem: Application of NSGA-II and MOGWO metaheuristic approaches,” _Environ., Develop. Sustain._ , vol. 25, no. 9, pp. 9163–9199, 2023. 

- [25] M. Hajghani, M. A. Forghani, A. Heidari, M. Khalilzadeh, and O. Kebriyaii, “A two-echelon location routing problem considering sustainability and hybrid open and closed routes under uncertainty,” _Heliyon_ , vol. 9, no. 3, 2023, Art. no. e14258. 

- [26] G. Laporte, “Fifty years of vehicle routing,” _Transp. Sci._ , vol. 43, no. 4, pp. 408–416, 2009. 

- [27] M. M. Solomon, “Algorithms for the vehicle routing and scheduling problems with time window constraints,” _Oper. Res._ , vol. 35, no. 2, pp. 254–265, 1987. 

- [28] G. Righini and M. Salani, “New dynamic programming algorithms for the resource constrained shortest path problem,” _Networks_ , vol. 45, no. 3, pp. 94–406, 2004. 

- [29] M. Gendreau, A. Hertz, and G. Laporte, _Tabu Search Heuristics for the Vehicle Routing Problem_ . Cham, Switzerland: Springer, 1999. 

- [30] S. A. Alumur and B. Y. Kara, “Network hub location problems: The state of the art,” _Eur. J. Oper. Res._ , vol. 190, no. 1, pp. 1–21, 2008. 

- [31] B. Y. Kara and B. C. Tansel, _Hub Location Problems: The Location of Interacting Facilities_ . Cham, Switzerland: Springer, 2008. 

- [32] J. F. Campbell, “Hub location in a competitive environment,” _Eur. J. Oper. Res._ , vol. 72, no. 3, pp. 364–377, 1994. 

- [33] M. Soleimani, M. Khalilzadeh, A. Bahari, and A. Heidary, “NSGAII algorithm for hub location-allocation problem considering hub disruption and backup hub allocation,” _World J. Eng._ , vol. 19, no. 6, pp. 794–807, 2022. 

- [34] A. H. S. Azadi, M. Khalilzadeh, J. Antucheviciene, A. Heidari, and A. Soon, “A sustainable multi-objective model for capacitated-electricvehicle-routing-problem considering hard and soft time windows as well as partial recharging,” _Biomimetics_ , vol. 9, no. 4, p. 242, 2024. 

- [35] A. Heidari, S. M. H. Orazani, M. Khalilzadeh, and F. Jolai, “A multiobjective model for cooperative delivery of customer orders using multiple trucks and UAVs considering weather conditions,” _Internet Things_ , vol. 29, Jan. 2025, Art. no. 101468. 

- [36] D. Ambrosino, M. G. Scutellà, and A. Sciomachen, “Commodity management in logistics networks: Modeling and optimization,” _Transp. Res. E, Logist. Transp. Rev._ , vol. 45, no. 5, pp. 844–863, 2009. 

- [37] H. Stadtler and C. Kilger, _Supply Chain Management and Advanced Planning: Concepts, Models, Software, and Case Studies_ . Cham, Switzerland: Springer, 2008. 

- [38] P. Ross, “Hyper-heuristics,” in _Search Methodologies_ . Cham, Switzerland: Springer, 2005, pp. 529–556. 

- [39] D. Pisinger and S. Ropke, “A general heuristic for vehicle routing problems,” _Comput. Oper. Res._ , vol. 34, no. 8, pp. 2403–2435, 2007. 

**KASSEM DANACH** (Member, IEEE) was born Lebanon, in 1985. He received the Doctor of Philosophy degree in computer engineering from the Ecole centrale de Lille, France, in 2016. He embarked on his academic journey with a fervent passion for computer engineering. Throughout his career, he has amassed a wealth of experience. He has applied his expertise in data analytics, artificial intelligence, machine learning, deep learning, educational technology, and business analytics to various military and professional roles. His illustrious career includes roles, such as the Chairperson of the Information Technology and Management Systems Department, Faculty of Business Administration, Al Maaref University, Lebanon. He had active participation as a Team Member in the EU-funded SOCORRO Project from 2019 to 2021. He has made substantial contributions to the field of operational research and artificial intelligence, earning him prestigious awards, including the Best Paper Award at LCIS in 2017, and AISD in 2019. 

**HASSAN HARB** (Member, IEEE) received the Ph.D. degree in computer science from Lebanese University, Lebanon, and the University of Franche-Comté, France, in 2016. He was a Postdoctoral Fellow with the Ensta-Bretagne, Artois University, and Paris-Saclay University from 2018 to 2022. He is currently an Assistant Professor with the American University of the Middle East, Kuwait. He has published more than 90 conference and journal papers. His research interests are in sensor networks and IoT, artificial intelligence, healthcare, and modular robotic systems. He served as a reviewer for a wide variety of IEEE, ACM, Elsevier, Wiley, and Springer journals. 

**BADIH BAZ** is an Associate Professor of Business Computing with the USEK Business School. He joined as an Assistant Professor with USEK in 1994. He currently serves as the Head of the Business Computing Program, USEK Grants and Projects Unit focal representative, and a member of the USEK university senate. He has held several academic and administrative leadership positions throughout his profession in higher education: the Chairperson of Business-Computing department, the Director of the Registrar’s Office, and the Dean of the Faculty of Sciences, USEK. He currently teaches undergraduate and graduate courses related to ERP E-Business Systems, decision support models, operations research, and database programming. He has published several IEEE papers on networking and computer systems. Beyond the academic realm, he has actively engaged with the industry, collaborating on projects that bridge the gap between academia and real-world application. His industry partnerships and consultations have further enriched his understanding of the practical challenges and opportunities in mobile app programming. He worked on several progressive Web apps and mobile android/IOS apps currently published and active on many international platforms. With a robust presence at over 30 national and international events, he has been an active participant and contributor to numerous conferences and symposiums, showcasing expertise in the dynamic field of IT and Management, through a diverse range of roles, including a speaker, a VIP guest, the session chair, and a committee member. In addition, he worked as an IT consultant and as an executive board member for several national and international companies and institutions, such as Al Houkair, Saudi Arabia, Retail Group, Lebanon, and Bull - Zenith data systems, France. His research interests span both computer networking and optimization. 

**ABBASS NASSER** (Senior Member, IEEE) received the M.Sc. degree in electronics from Lebanese University in 2012, and the Ph.D. degree in digital communication from the Université de Bretagne Occidentale (UBO), France, in 2016. He serves as an Associate Professor with the Business Computing Department, USEK, Lebanon. From 2012 to 2016, he was an Instructor with the Department of Computer Science, American University of Culture and Education, Lebanon. From 2017 to 2019, he was a Postdoctoral Researcher with ENSTA-Bretagne, France, where he has become a Research Fellow since 2019. In October 2020, he was a Visiting Professor with PolytechNantes, France. In September 2021, he was a Visiting Researcher with LabSTICC–UBO, France. He is the Supervisor and/or the co-director of several defended and in-progress Ph.D. projects. He co-authored more than 60 research papers published in international journals and conferences. His current research interests include cognitive radio, Internet of Things, and wireless sensor networks and intelligent reflecting surfaces. He serves as an editor and a reviewer for several international high-ranked journals. 

VOLUME 6, 2025 

791 

