Results in Engineering 25 (2025) 103833 



Contents lists available at ScienceDirect 

# Results in Engineering 

journal homepage: www.sciencedirect.com/journal/results-in-engineering 



### Research paper 

## Location planning techniques for Internet provider service unmanned aerial vehicles during crisis 



Kassem Danach<sup>a</sup> , Hassan Harb<sup>b</sup><sup>_,_∗</sup> , Ameer Sardar Kwekha Rashid<sup>c</sup><sup>_,_d</sup> , Mutaz A.B. Al-Tarawneh<sup>b</sup> , Wael Hosny Fouad Aly<sup>b</sup> 

> a _Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon_ 

> b _College of Engineering and Technology, American University of the Middle East, Kuwait_ 

> c _Artificial Intelligence, Universiti Teknologi Malaysia-UTM, Malaysia_ 

> d _University of Sulaimani, Sulaymaniyah, Iraq_ 

#### A R T I C L E I N F O 

#### A B S T R A C T 

_Keywords:_ Unmanned aerial vehicles Scheduling problem Hyperheuristic Metaheuristic Crisis management 

In situations where conventional communication networks are compromised, deploying Internet Provider Service Unmanned Aerial Vehicles (UAVs) becomes essential for re-establishing connectivity. This study presents a hyperheuristic framework aimed at optimizing the positioning and management of these UAVs, with a focus on enhancing coverage, reducing latency, and managing operational costs. The framework employs a dynamic selection of multiple low-level heuristics, guided by real-time problem conditions and a Monte Carlo-based decision process. The performance of this approach was evaluated through simulations across 40 different scenarios, encompassing urban, suburban, rural, and mixed environments. The results show that the hyperheuristic method consistently delivered high coverage, achieving 94.6% in urban settings, 88.3% in suburban areas, 82.0% in rural regions, and 85.0% in mixed conditions. These outcomes highlight the flexibility and effectiveness of the hyperheuristic approach in adapting to various crisis scenarios. This research not only provides practical insights for UAV deployment but also advances the field of combinatorial optimization through innovative hyperheuristic techniques. 

##### **1. Introduction** 

##### _1.1. Context_ 

In times of crisis, such as natural disasters or significant infrastructure breakdowns, maintaining reliable communication networks becomes critically important [37,2]. Traditional communication infrastructures, including cellular towers and fiber-optic networks, are often susceptible to damage or disruption, resulting in the loss of essential communication services for affected populations [8,13]. Unmanned Aerial Vehicles (UAVs), outfitted with internet-providing capabilities, have emerged as a versatile and rapid-response solution to reestablish connectivity in these challenging scenarios [34]. 

The deployment of UAVs to provide internet services during emergencies involves solving a complex combinatorial optimization problem. The central challenge is to determine the most effective locations for UAVs to achieve maximum coverage, minimize latency, and ensure that 

services are distributed equitably across the affected regions [17]. This task is further complicated by the operational constraints of UAVs, such as limited battery life, restricted range, and the necessity to prevent overlapping coverage areas, all while considering environmental factors like terrain and weather conditions [14,38]. 

##### _1.2. Unique characteristics of UAVs in Internet service provision_ 

Unmanned Aerial Vehicles (UAVs) offer unique advantages in providing Internet services, especially during crisis situations where traditional infrastructure may be damaged or unavailable. UAVs can be rapidly deployed in remote or inaccessible areas, providing on-demand connectivity in real-time. Their flexibility allows them to bypass terrain obstacles and reach areas that would otherwise be difficult to cover with terrestrial networks. Additionally, UAVs can serve as mobile relay stations, dynamically adjusting their positions to optimize network coverage and latency. 

* Corresponding author. 

_E-mail addresses:_ kassem.danach@mu.edu.lb (K. Danach), hassan.harb@aum.edu.kw (H. Harb), ameer.rashid@univsul.edu.iq (A.S.K. Rashid), mutaz.al-tarawneh@aum.edu.kw (M.A.B. Al-Tarawneh), wael.aly@aum.edu.kw (W.H.F. Aly). 

https://doi.org/10.1016/j.rineng.2024.103833 

Received 4 October 2024; Received in revised form 9 December 2024; Accepted 23 December 2024 

Available online 3 January 2025 

2590-1230/© 2025 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/bync-nd/4.0/). 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

However, the use of UAVs for Internet service provision also comes with specific challenges. These include the limited battery life of UAVs, which constrains their operational time and coverage range, and environmental factors such as adverse weather conditions (e.g., strong winds or storms) that can affect their stability and communication capabilities. Moreover, terrain variations and the need to maintain line-of-sight connectivity between UAVs and users introduce additional complexity in planning optimal deployment strategies. 

Furthermore, the equitable distribution of service is essential to ensure that all affected regions, including remote and underserved areas, receive adequate coverage [3]. The integration of UAVs into existing emergency response frameworks has also been explored, with studies highlighting the importance of coordination between UAVs and groundbased assets to enhance the overall effectiveness of disaster response operations [11]. 

##### _2.2. Optimization techniques in UAV deployment_ 

##### _1.3. Contribution_ 

In response to the above challenges, this paper introduces a novel approach to the problem of location planning for Internet Service Provider UAVs during crises. Our method integrates mathematical modeling with the use of valid inequalities, Lagrangian relaxation, and hyperheuristics to address the complexities of the problem efficiently. Specifically, we employ a mixed-integer linear programming (MILP) model to maximize overall coverage and minimize service latency, while ensuring that operational constraints are met [20]. 

##### _1.4. Paper structure_ 

The remainder of this paper is organized as follows. Section 2 reviews existing literature and explores various approaches related to UAV deployment, optimization strategies, and communication coverage in crisis situations. In section 3, we introduce the mathematical reformulation of the problem including research questions, hypothesis, and various constraints considered in this study. Section 4 discusses the application of Lagrangian relaxation techniques, which help to decompose the problem and facilitate more efficient solution methods. Then, the hyperheuristic framework is detailed in section 5 while emphasizing how it dynamically selects and applies low-level heuristics. The experimental setup and results are presented in section 6 and showcasing the performance of our approach across multiple test scenarios. Finally, we conclude the paper by summarizing the key findings and suggesting potential directions for future research. 

##### **2. Literature review** 

The integration of ISP-based UAVs in healthcare sector has been recently studied by research community. In this section, we first show the deployment of UAVs into health systems, then we show the importance of using optimization approaches to solve various challenges resulted from such intergation, followed by a summary of existing solutions for ISP and communication based techniques. 

Optimization techniques [29,23] play a crucial role in enhancing the performance of UAV networks deployed during crises. One of the most common approaches is the use of Mixed-Integer Linear Programming (MILP) models, which are designed to capture the complexities of UAV deployment, including constraints related to coverage, latency, operational costs, and environmental factors [17]. These models provide a mathematical framework for optimizing the placement and movement of UAVs to achieve the best possible performance under given conditions. 

Recent advancements in optimization methods have introduced the use of valid inequalities to tighten MILP formulations, thereby reducing computational complexity and improving solution accuracy [20]. Additionally, the application of Lagrangian relaxation has been shown to decompose complex UAV deployment problems into more manageable subproblems, facilitating faster and more efficient solution strategies [6]. This approach is particularly beneficial in large-scale scenarios where traditional optimization methods may struggle with computational demands. 

Hyperheuristics, which operate by dynamically selecting low-level heuristics based on the characteristics of the problem at hand, have also been explored as a promising solution for UAV deployment optimization [33]. These techniques offer a flexible and adaptive approach to problem-solving, allowing the optimization process to respond to changing conditions in real-time. For example, during a crisis, environmental factors such as weather conditions or terrain can significantly impact UAV performance, and hyperheuristics can adjust the deployment strategy accordingly [27]. 

Moreover, recent research has explored the integration of machine learning with optimization techniques to further enhance UAV deployment strategies. Machine learning models can predict the impact of various deployment decisions on network performance, enabling more informed and proactive decision-making [28]. This combination of machine learning and optimization represents a significant advancement in the field, offering the potential for highly efficient and adaptive UAV networks in crisis scenarios [16]. 

##### _2.3. Internet service provider (ISP) techniques using UAVs_ 

##### _2.1. UAV deployment in crisis scenarios_ 

The use of Unmanned Aerial Vehicles (UAVs) for providing internet services during crises has become a critical area of research due to the increasing frequency of natural disasters and other emergencies that compromise traditional communication infrastructures. UAVs offer a flexible and rapidly deployable solution that can restore connectivity in affected areas, ensuring that essential communication services are maintained even in the most challenging environments [8,39]. Studies have shown that in disaster scenarios, such as earthquakes and hurricanes, UAVs can be quickly deployed to replace damaged ground-based communication networks, thereby minimizing the downtime of critical communication services [34]. The effectiveness of UAVs in these situations is largely dependent on their deployment strategy, which must consider factors such as coverage, latency, and service equity across affected areas [17]. 

Research by [14] emphasizes that the deployment of UAVs must be optimized not only to maximize coverage but also to minimize latency, which is crucial for time-sensitive communications during emergencies. 

The authors of [1] introduced a new approach called GW-A* that combines between classical A* and grey wolf optimizer to identify the best paths of UAVs to provide internet in a city. Compared to traditional algorithms, the new model considers external factor of a drone such as wind direction and speed as well as the presence of obstacles in a crowded city. In [35], a low attitude Internet of UAVs (IoLoUA) design has been proposed. The design is able to deliver a wide range of items including internet, goods and information. Basically, the authors designed a theoretical model to demonstrate the efficiency of their design in terms of collecting data through IoT devices and defending against security threats. The authors of [22] presented a two layers drone architecture consisting of access and distribution drones for providing WiFi in 5G networks. On one hand, the access UAV acts as WiFi points for ground users and, on the other hand, the distribution UAV acts as relay forwarding points for packet delivery. In addition, the authors used the particle swarm optimization algorithm to identify the optimal number of drones along with their locations in a city. In [26], the authors proposed a complete framework that combines between UAVs, artificial intelligence 

2 

_Results in Engineering 25 (2025) 103833_ 

###### _K. Danach, H. Harb, A.S.K. Rashid et al._ 

and blockchain dedicated to search and rescue applications. The first framework component, e.g. UAVs, allows to provide internet needed to discover missing victims in harsh area, while the second component is used to improve the energy consumption in drone and minimize the latency, and the last component is based on blockchain to provide a secure and decentralized healthcare platform. The authors of [30] proposed an architecture for ISP-UAV based on NB-IoT 6G networks. In order to offer a high-quality internet service, they used a mobile UAV repeater, a radio resources and access network as an infrastructure for their system. The authors of [32] introduced a service-oriented framework for drone-based multi-package delivery. The framework provides a highlevel design for deploying a skyway network in a city for the effective provisioning of drone-based service delivery. The authors used a graphbased heuristic algorithm to reduce the search space for optimal service selection in the city. 

##### _2.4. Communications coverage techniques using UAVs_ 

The authors of [19] give an overview about communication techniques used for UAV channel sounder. They categorized existing solutions based on sounding signal, hardware scheme, synchronization time, calibration, and information cleaning. Furthermore, the authors analyzed and discussed current channel and measurements technologies used for UAV-assisted communications. In [18], the authors introduced a multi internet of vehicles model in which the drones are used to collect and send downlink data to the vehicles during the flight time. The model includes three optimization components: communication scheduling, power allocation and UAV path. Then, a convex approximation has been used to solve all components to guarantee the communication between mobile vehicles. A state-based game with actor–critic (SBG-AC) is proposed in [24]. The algorithm groups UAVs in a given area and improves the coverage zone while maximizing energy saving and ensuring a large fairness value. In [21], the authors presented a stochastic geometry model to ensure the spatial communications between UAVs in urban zones. The performance of model is studied through realistic scenario on terrestrial base stations where mobile vehicles are clustered close to the urban centers. The authors of [10] converted the communication coverage into a swarm graph problem then used an optimization approach to solve it. The convergence of the algorithm is ensured through a utility function and a Nash equilibrium is achieved. In [25], a game-theoretical autonomous decision-making model for UAVs deployment is proposed. The model defines a payoff function for every UAV that uses a coverage probability value and the altitude of the UAV antenna. To further reduce interference, the model adjusted the UAV altitude based on the antenna and some deployment requirements such as monitoring targets. 

##### _2.5. State-of-the-art: summary and limitations_ 

Table 1 summarizes the state-of-the-art techniques in terms of their publication dates, their approach category, as well as their used methods. Unfortunately, the analysis of literature review show several drawbacks: 1) the efforts of integrating ISP-UAVs into crisis management is very embarrassing. 2) Most of the optimization-based solutions do not consider various constraints of UAVs such as operational, environmental, coverage, capacity and deployment. 3) Most techniques do not take into account internal and external factors affecting the deployment of UAVs such as weather, UAV placements, balancing workload among UAVs, etc. 4) Existing solutions are mostly complex and not suitable to limited resources of UAVs. 5) Performance of existing solutions are mostly tested against one urban scenario and not tested against various ones such as suburban, rural and mixed scenarios. 

##### **3. Problem formulation and study objectives** 

In this study, we consider a set of potential deployment sites, denoted as _𝐿_ = { _𝑙_ 1 _,𝑙_ 2 _,_ … _,𝑙𝑚_ }, which is available for positioning Unmanned 

**Table 1** 

State-of-the-Art: A summary. 

|**Ref.**|**Year**|**Category**||**Methods**|
|---|---|---|---|---|
|||**ISP-UAV**|**UAV** **communication**||
|[1]|2024|X||A*, Grey wolf optimizer|
|[35]|2023|X||IoLoUA|
|[22]|2022|X||WiFi in 5G|
|[26]|2023|X||UAVs, AI and blockchain|
|[30]|2022|X||NB-IoT 6G|
|[32]|2022|X||Multi-package delivery|
|[19]|2024||X|Channel sounder|
|[18]|2022||X|Multi IoV|
|[24]|2022||X|SBG-AC|
|[21]|2021||X|Stochastic geometry model|
|[10]|2022||X|Swarm graph model|
|[25]|2020||X|Game-theoretical model|



Aerial Vehicles (UAVs) that are tasked with delivering internet connectivity during a crisis. The user locations that require connectivity are represented by the set _𝑈_ = { _𝑢_ 1 _,𝑢_ 2 _,_ … _,𝑢𝑛_ }. Each UAV _𝑣_ in the set _𝑉_ = { _𝑣_ 1 _,𝑣_ 2 _,_ … _,𝑣𝑘_ } is defined by specific attributes such as its coverage range _𝑟𝑣_ , battery life _𝑏𝑣_ , and operational cost _𝑐𝑣_ . 

##### _3.1. Research questions_ 

The study is guided by the following questions: 

- RQ1: What strategies can be employed to select UAV deployment locations that maximize coverage while minimizing operational costs? 

- RQ2: How do environmental factors, such as terrain and weather, influence UAV placement? 

- RQ3: What methods can minimize latency for users by strategically placing UAVs closer to high-demand areas? 

- RQ4: How does balancing workload among UAVs enhance network reliability during crises? 

- RQ5: Can advanced optimization techniques (e.g., hyperheuristics) outperform conventional methods in solving this problem? 

##### _3.2. Hypotheses_ 

Based on the mentioned research questions, the following hypotheses are considered: 

- H1: Integrating mathematical modeling with valid inequalities improves solution precision and computational efficiency. 

- H2: Accounting for environmental constraints yields robust deployment strategies, albeit with trade-offs in coverage and cost. 

- H3: Placing UAVs closer to high-demand areas significantly reduces latency and enhances service quality. 

- H4: Balancing the load among UAVs prevents overburdening and ensures consistent network performance. 

- H5: Hyperheuristic methods dynamically adapt to problem conditions, outperforming traditional optimization approaches. 

##### _3.3. Study objectives_ 

The UAV deployment problem first requires the definition of the following binary decision variables: 

- _𝑥𝑖𝑗_ : Indicates whether user _𝑢𝑗_ is covered by UAV _𝑣𝑖_ (1 if true, 0 otherwise). 

3 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

- _𝑦𝑖_ : Represents whether UAV _𝑣𝑖_ is deployed at location _𝑙𝑖_ (1 if deployed, 0 otherwise). 

- _𝑧𝑗_ : Denotes whether user _𝑢𝑗_ is covered by at least one UAV (1 if true, 0 otherwise). 

Then, the core objectives of this study is defined as follows: 

- Maximizing coverage: The objective is to maximize the number of users covered by the deployed UAVs. A user _𝑢𝑗_ is considered covered by UAV _𝑣𝑖_ if the deployment site _𝑙𝑖_ , hosting _𝑣𝑖_ , satisfies _𝑑_ ( _𝑙𝑖,𝑢𝑗_ ) ≤ _𝑟𝑣_ , where _𝑑_ ( _𝑙𝑖,𝑢𝑗_ ) represents the distance between the deployment site and the user. This is modeled by the binary decision variable _𝑥𝑖𝑗_ , where: 

1 if _𝑢𝑗_ is covered by _𝑣𝑖, 𝑥𝑖𝑗_ = 0 otherwise. { 

The coverage maximization function is given by: 



<!-- Start of picture text -->
𝑘 𝑛<br>Maximize ∑ ∑ 𝑥𝑖𝑗 .<br>𝑖 =1 𝑗 =1<br><!-- End of picture text -->

- Minimizing latency: Latency is minimized by reducing the cumulative distance between users and their assigned UAVs. This is expressed as: 



<!-- Start of picture text -->
𝑘 𝑛<br>Minimize ∑ ∑ 𝑥𝑖𝑗 ⋅ 𝑑 ( 𝑙𝑖,𝑢𝑗 ) ,<br>𝑖 =1 𝑗 =1<br><!-- End of picture text -->

where _𝑥𝑖𝑗_ ⋅ _𝑑_ ( _𝑙𝑖,𝑢𝑗_ ) contributes only if _𝑥𝑖𝑗_ = 1. 

- Ensuring load balancing: To prevent overburdening any UAV, the service load is balanced by minimizing the maximum number of users assigned to a single UAV. Let _𝑦𝑖_ denote the load on UAV _𝑣𝑖_ : 



<!-- Start of picture text -->
𝑛<br>𝑦𝑖 = ∑ 𝑥𝑖𝑗 .<br>𝑗 =1<br><!-- End of picture text -->

The objective is to: 



<!-- Start of picture text -->
Minimize 𝑖 =1max , … ,𝑘 𝑦𝑖.<br><!-- End of picture text -->

To achieve the above goals simultaneously, a composite objective function is defined that integrates weighted terms for each objective: 



<!-- Start of picture text -->
𝑘 𝑛 𝑘 𝑛<br>Maximize 𝛾 1 ∑ ∑ 𝑥𝑖𝑗 − 𝛾 2 ∑ ∑ 𝑥𝑖𝑗 ⋅ 𝑑 ( 𝑙𝑖,𝑢𝑗 ) − 𝛾 3 𝑖 =1max , … ,𝑘 𝑦𝑖,<br>𝑖 =1 𝑗 =1 𝑖 =1 𝑗 =1<br><!-- End of picture text -->

where _𝛾_ 1 _,𝛾_ 2 _,𝛾_ 3 are weights that balance the relative importance of each objective. 

where _𝐿_ infeasible _⊂𝐿_ represents the infeasible locations. 

• Coverage constraints: Ensures each user _𝑢𝑗_ is covered by at least one UAV: 



<!-- Start of picture text -->
𝑘<br>𝑧𝑗 ≤ ∑ 𝑥𝑖𝑗 , ∀ 𝑗 = 1 , … ,𝑛 (1)<br>𝑖 =1<br><!-- End of picture text -->

- Operational range constraints: UAVs can only cover users within their range: _𝑥𝑖𝑗_ ≤ _𝑦𝑖_ ⋅ 𝕀( _𝑑_ ( _𝑙𝑖,𝑢𝑗_ ) ≤ _𝑟𝑖_ ) _,_ ∀ _𝑖_ = 1 _,_ … _,𝑘,_ ∀ _𝑗_ = 1 _,_ … _,𝑛_ (2) where 𝕀(⋅) is an indicator function that equals 1 if the condition is true and 0 otherwise, and _𝑟𝑖_ represents the coverage radius of UAV _𝑣𝑖_ . 

- • Capacity constraints: Limits the number of users assigned to each UAV: _𝑛_ 

- ∑ _𝑥𝑖𝑗_ ≤ Capacity _𝑖,_ ∀ _𝑖_ = 1 _,_ … _,𝑘_ (3) _𝑗_ =1 

- • Deployment constraints: Ensures that each UAV is deployed at most once: _𝑘_ 

- ∑ _𝑦𝑖_ ≤ Max_UAVs (4) _𝑖_ =1 

##### _3.5. Valid inequalities_ 

To further clarify the problem formulation, valid inequalities are introduced to tighten the solution space: 

- Flow conservation inequality: Ensures the flow of coverage from UAVs to users: _𝑛_ 

- ∑ _𝑥𝑖𝑗_ ≥ _𝑦𝑖,_ ∀ _𝑖_ = 1 _,_ … _,𝑘_ (5) _𝑗_ =1 

- Load balancing inequality: Prevents overloading of UAVs by balancing service distribution: 



<!-- Start of picture text -->
𝑛<br>∑ 𝑥𝑖𝑗 ≤ 𝑘 𝑛 +  𝜖, ∀ 𝑖 = 1 , … ,𝑘 (6)<br>𝑗 =1<br><!-- End of picture text -->

where _𝜖_ is a small constant to allow for minor deviations. 

- Redundancy reduction inequality: Minimizes overlapping coverage areas between UAVs: 



<!-- Start of picture text -->
𝑥𝑖𝑗 +  𝑥𝑖𝑗 ′ ≤ 1 , ∀ 𝑗,𝑗 ′ such that 𝑑 ( 𝑢𝑗 ,𝑢 ′ 𝑗 ) ≤ 𝛿 (7)<br>where 𝛿 is a threshold distance below which users are considered<br>to be within the same coverage area.<br><!-- End of picture text -->

##### _3.4. Constraints_ 

The study includes several constraints to ensure feasibility: 

These valid inequalities play a crucial role in enhancing the optimization process by reducing the solution space, thereby improving convergence rates. 

- Operational constraints: it consists of: 

- Distance-based coverage: UAVs can only cover users within their range: 

- _𝑑_ ( _𝑙𝑖,𝑢𝑗_ ) ≤ _𝑟𝑣,_ ∀ _𝑖_ ∈{1 _,_ … _,𝑘_ } _,_ ∀ _𝑗_ ∈{1 _,_ … _,𝑛_ } _._ 

- Battery life: Each UAV operates within its battery limits: 

##### OperationalTime( _𝑣𝑖_ ) ≤ _𝑏𝑣,_ ∀ _𝑖_ ∈{1 _,_ … _,𝑘_ } _._ 

- Minimizing overlap: The overlap in coverage among UAVs should be minimized to reduce redundancy. 

##### **4. Application of Lagrangian relaxation** 

Lagrangian relaxation is a technique used to simplify complex combinatorial optimization problems by relaxing certain constraints and incorporating them into the objective function with corresponding penalty multipliers. This approach enables the problem to be broken down into more manageable subproblems, which can be solved more efficiently. 

##### _4.1. Problem decomposition_ 

- Environmental constraints: Deployment sites must be feasible: 

- _𝑆_ ∩ _𝐿_ infeasible = ∅ _,_ 

For the optimization of UAV deployment, the problem can be decomposed by relaxing the coverage and capacity constraints, which are 

4 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

often the most challenging to satisfy. Specifically, the following constraints are relaxed: 



<!-- Start of picture text -->
• Coverage Constraints:<br>𝑘<br>𝑧𝑗 ≤ ∑ 𝑥𝑖𝑗 , ∀ 𝑗 = 1 , … ,𝑛 (8)<br>𝑖 =1<br><!-- End of picture text -->

- Capacity Constraints: 



<!-- Start of picture text -->
𝑛<br>∑ 𝑥𝑖𝑗 ≤ Capacity 𝑖, ∀ 𝑖 = 1 , … ,𝑘 (9)<br>𝑗 =1<br><!-- End of picture text -->

These relaxed constraints are then incorporated into the objective function using Lagrange multipliers _𝜆𝑗_ and _𝜇𝑖_ , respectively. 

##### _4.2. Lagrangian function_ 

The Lagrangian function  for the relaxed problem is defined as: 



<!-- Start of picture text -->
𝑛 𝑘 𝑛 𝑘<br>( 𝑥,𝑦,𝑧,𝜆,𝜇 ) = ∑ 𝑧𝑗 − 𝛼 ∑ ∑ 𝑥𝑖𝑗 ⋅ 𝑑 ( 𝑙𝑖,𝑢𝑗 ) − 𝛽 ∑ 𝑐𝑖 ⋅ 𝑦𝑖 (10)<br>𝑗 =1 𝑖 =1 𝑗 =1 𝑖 =1<br>𝑛 𝑘 𝑘<br>+ ∑ 𝜆𝑗 𝑧𝑗 − ∑ 𝑥𝑖𝑗 + ∑ 𝜇𝑖 ∑ 𝑥𝑖𝑗 − Capacity 𝑖<br>𝑗 =1 ( 𝑖 =1 ) 𝑖 =1 ( 𝑗 =1 𝑛 )<br><!-- End of picture text -->

Here, _𝜆𝑗_ and _𝜇𝑖_ are the Lagrange multipliers associated with the coverage and capacity constraints, respectively. 

##### _4.3. Subproblem solution_ 

The relaxation process results in a set of subproblems, each of which can be solved independently for each UAV _𝑣𝑖_ . Given a set of Lagrange multipliers _𝜆𝑗_ and _𝜇𝑖_ , the subproblem for UAV _𝑣𝑖_ is: 



<!-- Start of picture text -->
𝑛<br>Maximize ∑ ( 𝜆𝑗 − 𝛼𝑑 ( 𝑙𝑖,𝑢𝑗 ) +  𝜇𝑖 ) 𝑥𝑖𝑗 − 𝛽𝑐𝑖𝑦𝑖 (11)<br>𝑗 =1<br><!-- End of picture text -->

This subproblem can be solved using optimization techniques such as linear programming or heuristic methods, depending on the problem’s size and complexity. 

##### _4.4. Multiplier update_ 

The Lagrange multipliers _𝜆𝑗_ and _𝜇𝑖_ are iteratively updated based on the solutions of the subproblems. The updates are typically derived using subgradient optimization methods: 



<!-- Start of picture text -->
𝑘<br>𝜆 ( 𝑗 𝑡 +1) =  𝜆 ( 𝑗 𝑡 ) +  𝜃 ( 𝑡 ) 𝑧𝑗 − ∑ 𝑥𝑖𝑗 (12)<br>( 𝑖 =1 )<br>𝜇𝑖 ( 𝑡 +1) =  𝜇𝑖 ( 𝑡 ) +  𝜃 ( 𝑡 ) ∑ 𝑥𝑖𝑗 − Capacity 𝑖 (13)<br>( 𝑗 =1 𝑛 )<br><!-- End of picture text -->

Here, _𝜃_<sup>(</sup><sup>_𝑡_)</sup> is a step size parameter that influences the convergence of the multiplier update process. 

##### _4.5. Convergence and solution quality_ 

The iterative process continues until the changes in the Lagrange multipliers or the objective function value fall below a predefined threshold, indicating convergence. The solution obtained through Lagrangian relaxation provides a lower bound for the original MILP problem. To enhance the solution quality, heuristic methods or branch-andbound techniques can be employed to refine the solution. 

Lagrangian relaxation not only simplifies the problem but also offers valuable insights into the trade-offs between different objectives, such as 

coverage, latency, and capacity, thereby supporting informed decisionmaking for UAV deployment during crises. 

##### **5. Hyperheuristic solution approach** 

The hyperheuristic solution approach employs a high-level strategy to govern the selection and application of low-level heuristics. Hyperheuristics are defined as “heuristics to choose heuristics,” where a set of heuristics is managed by a high-level mechanism to solve complex problems more effectively [4]. This method is particularly useful in domains where problem-specific heuristics might not be available, and there is a need for a more general approach that can adapt to various instances of the problem [5]. The selection process in hyperheuristics is guided by a heuristic reward system, which evaluates the performance of each heuristic based on its contribution to improving the solution. 

##### _5.1. Pseudocode of the hyperheuristic algorithm_ 

The Hyperheuristic Solution Approach leverages a high-level strategy to dynamically select and apply low-level heuristics based on their past performance. This adaptive mechanism allows the algorithm to efficiently explore the solution space while balancing exploitation and exploration. The main steps of the approach, including initialization, heuristic selection, solution generation, evaluation, and termination, are outlined in Algorithm 1: 

##### **Algorithm 1** Hyperheuristic Solution Approach. 

- **Require:** Problem instance, set of low-level heuristics _𝐻_ = { _ℎ_ 1 _,ℎ_ 2 _,_ … _,ℎ𝑚_ }, maximum iterations _𝑇_ max 

- **Ensure:** Best solution _𝑆_ best 1: **Initialization:** 2: Generate an initial solution _𝑆_ 3: Set _𝑆_ best ← _𝑆_ 4: Initialize heuristic performance metrics _𝑃_ ( _ℎ𝑖_ )∀ _ℎ𝑖_ ∈ _𝐻_ 5: Set iteration counter _𝑡_ ← 0 6: **while** _𝑡< 𝑇_ max **do** 7: Select a heuristic _ℎ𝑖_ from _𝐻_ based on _𝑃_ ( _ℎ𝑖_ ) 8: Generate new solution _𝑆_<sup>′</sup> ← _ℎ𝑖_ ( _𝑆_ ) 9: Evaluate _𝑆_<sup>′</sup> using the objective function(s) 

- 10: **if** _𝑆_<sup>′</sup> improves _𝑆_ best **then** 11: _𝑆_ best ← _𝑆_<sup>′</sup> 12: **end if** 13: **if** _𝑆_<sup>′</sup> meets acceptance criteria **then** 14: _𝑆_ ← _𝑆_<sup>′</sup> 15: **end if** 16: Update _𝑃_ ( _ℎ𝑖_ ) based on improvement in solution quality 17: Increment iteration counter _𝑡_ ← _𝑡_ + 1 18: **end while** 19: **return** _𝑆_ best 

##### _5.2. Low-level heuristics_ 

Low-level heuristics are the basic operations used within the hyperheuristic framework to construct and refine solutions. These heuristics are simple, rule-based methods that directly modify the solution structure. According to [31], low-level heuristics are crucial in hyperheuristics as they form the building blocks upon which the high-level strategy operates. In this study, low-level heuristics are categorized into constructive heuristics, improvement heuristics, and perturbation heuristics. 

##### _5.2.1. Constructive heuristics_ 

Constructive heuristics generate an initial solution by incrementally adding components according to predefined rules. These heuristics are essential for creating feasible starting points for further optimization [9]. In this study, two constructive heuristics, CS1 and CS2, are implemented: 

5 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

- CS1: Coverage-Oriented Construction Heuristic: This heuristic prioritizes maximizing user coverage at each step of the solution construction. Starting with no UAVs deployed, CS1 iteratively adds UAVs by selecting locations that cover the most uncovered users until all users are covered or further deployment is constrained by operational limits. 

##### **Algorithm 2** CS1: Coverage-Oriented Construction Heuristic. 

**Algorithm 5** IH2: Incremental Coverage Adjustment Heuristic. 

   - 1: Initialize solution _𝑆_ 

   - 2: **for** each UAV _𝑣𝑖_ in _𝑆_ **do** 3: Identify potential new positions within allowable range of _𝑣𝑖_ 4: **for** each position _𝑝_ **do** 

   - 5: Calculate coverage improvement if _𝑣𝑖_ is moved to _𝑝_ 6: **end for** 7: Move _𝑣𝑖_ to the position _𝑝_ that provides the best coverage improvement 8: **end for** 

   - 9: **return** _𝑆_ 

- 1: Initialize solution _𝑆_ = ∅ 

- 2: Initialize set of uncovered users _𝑈_ = { _𝑢_ 1 _,𝑢_ 2 _,_ … _,𝑢𝑛_ } 

- 3: **while** _𝑈_ ≠ ∅ **do** 

- 4: Select UAV location _𝑙𝑖_ that maximizes coverage of users in _𝑈_ 5: Deploy UAV at _𝑙𝑖_ and update _𝑆_ 6: Update _𝑈_ by removing users covered by UAV at _𝑙𝑖_ 7: **end while** 8: **return** _𝑆_ 

- CS2: Cost-Minimization Construction Heuristic: In contrast to CS1, CS2 focuses on minimizing deployment costs while constructing the solution. This heuristic identifies the most cost-effective UAV locations, prioritizing those that provide sufficient coverage with the lowest operational expenses. 

##### **Algorithm 3** CS2: Cost-Minimization Construction Heuristic. 

##### _5.2.3. Perturbation heuristics_ 

Perturbation heuristics introduce significant changes to the solution to escape local optima and explore new regions of the solution space. These heuristics are critical for maintaining diversity in the search process, as emphasized by [12]. 

   - PH1: Random Deployment Perturbation Heuristic: PH1 randomly relocates a subset of UAVs to new positions, disrupting the current solution to explore alternative configurations. This heuristic is particularly effective in preventing the search process from stagnating in local optima. 

   - PH2: User Reallocation Perturbation Heuristic: PH2 reassigns a random set of users to different UAVs, regardless of the current optimal assignments. This heuristic introduces diversity into the solution, enabling the search to explore configurations that might not have been considered by more conservative improvement heuristics. 

- 1: Initialize solution _𝑆_ = ∅ 

- 2: Initialize set of uncovered users _𝑈_ = { _𝑢_ 1 _,𝑢_ 2 _,_ … _,𝑢𝑛_ } 

- 3: **while** _𝑈_ ≠ ∅ **do** 4: Select UAV location _𝑙𝑖_ that minimizes deployment cost while covering at least one user in _𝑈_ 

- 5: Deploy UAV at _𝑙𝑖_ and update _𝑆_ 

- 6: Update _𝑈_ by removing users covered by UAV at _𝑙𝑖_ 7: **end while** 

These low-level heuristics are fundamental to the hyperheuristic approach, providing the mechanisms for constructing, refining, and diversifying solutions. By leveraging these simple, rule-based operations, the hyperheuristic framework can adapt to various problem instances and optimize UAV deployment in complex crisis scenarios. 

##### _5.3. Heuristic reward system_ 

- 8: **return** _𝑆_ 

##### _5.2.2. Improvement heuristics_ 

Improvement heuristics are used to refine the initial solutions generated by constructive heuristics. These heuristics work by making localized changes to the solution, with the aim of enhancing its overall quality. As highlighted by [36], improvement heuristics are essential in iterative optimization methods for fine-tuning solutions. 

- IH1: Local Reassignment Heuristic: This heuristic reassigns users between UAVs within their coverage range to balance the load and reduce operational costs. The heuristic iteratively evaluates potential reassignments and implements those that improve coverage uniformity or cost-efficiency. 

##### **Algorithm 4** IH1: Local Reassignment Heuristic. 

- 1: Initialize solution _𝑆_ 

- 2: **for** each user _𝑢𝑗_ in _𝑆_ **do** 

- 3: Evaluate reassignment of _𝑢𝑗_ to all other UAVs in its coverage range 

- 4: **if** reassignment improves coverage uniformity or reduces cost **then** 5: Reassign _𝑢𝑗_ to the selected UAV 

- 6: **end if** 

- 7: **end for** 

- 8: **return** _𝑆_ 

- IH2: Incremental Coverage Adjustment Heuristic: This heuristic improves coverage by adjusting UAV positions within their allowable range. By fine-tuning UAV placement, IH2 seeks to optimize coverage overlap where beneficial and minimize redundancy. 

The heuristic reward system is integral to the hyperheuristic approach, guiding the selection of low-level heuristics based on their performance. According to [7], heuristic selection methods in hyperheuristics can significantly improve the efficiency and effectiveness of the search process. This system assigns rewards to heuristics based on their recent contributions to solution improvement. 

##### _5.3.1. Reward calculation_ 

Rewards are calculated after each application of a heuristic by evaluating improvements in key performance metrics such as: 

- Objective function improvement: The main criterion for heuristic success is the enhancement of the objective function (e.g., increased coverage, reduced latency, or lower operational costs). Greater improvements lead to higher rewards. Additionally, this metric reflects how much closer the solution moves towards mathematical optimality after a heuristic is applied. 

- Solution quality: The overall quality of the resulting solution, including its feasibility (e.g., adherence to constraints like UAV range and battery life) and practical robustness (e.g., balanced workload distribution among UAVs), influences the reward. Solutions that meet constraints and perform well under stress are rewarded more highly. 

- Efficiency: The computational efficiency of the heuristic, measured by the speed at which it achieves improvements, also contributes to the reward. Faster heuristics that yield substantial improvements are favored. 

- _5.3.2. Heuristic selection based on rewards_ 

The selection process uses accumulated rewards to determine which heuristic to apply next: 

6 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

- Exploit Successful Heuristics: Heuristics with consistently high rewards are chosen more frequently, as they are likely to continue improving the solution. This strategy ensures that effective heuristics are fully utilized. 

- Explore New Heuristics: When the rewards for commonly used heuristics begin to decrease, the selection process shifts to less frequently used heuristics to explore new possibilities. This balance between exploitation and exploration prevents the search from becoming overly narrow. 

- Dynamic Adaptation: The system continuously updates heuristic reward scores based on the current solution state, allowing it to adapt to changes in the problem landscape and maintain search effectiveness. 

By incorporating this reward-based system, the hyperheuristic approach ensures that the search process is both adaptive and focused, making the most of various low-level heuristics while maintaining the flexibility to explore new strategies. This dynamic selection mechanism enhances the overall efficiency and quality of the solutions generated in complex UAV deployment scenarios during crises. 

##### _5.4. Acceptance criteria_ 

##### **6. Experimental setup** 

The experiments were carried out in a simulated environment specifically designed to replicate crisis scenarios where conventional communication infrastructures are unavailable. A total of 40 test instances were generated, each varying in user distribution, geographical area, UAV availability, and operational constraints. These instances were carefully crafted to ensure a comprehensive evaluation of the proposed hyperheuristic approach across a broad spectrum of potential scenarios. 

##### _6.1. Generation of test instances_ 

The 40 test instances were generated using a combination of realworld data simulation and randomization techniques. The process is detailed below: 

1. Geographical Area Selection: 

   - Each instance was modeled on a 1000 km<sup>2</sup> rectangular grid, divided into smaller cells (e.g., 10x10 km), representing potential UAV deployment locations. 

   - The density and distribution of these cells were adjusted to simulate different environments, such as urban, suburban, and rural areas. 

2. User Distribution: 

The acceptance of new solutions within the search process is governed by acceptance criteria based on the Monte Carlo method. As noted by [15], the Monte Carlo method is effective in probabilistically accepting solutions that may not immediately improve the objective function, thereby avoiding premature convergence to local optima. 

- Monte Carlo-Based Acceptance: When a new solution is generated, its acceptance is determined by comparing it to the current solution using a probabilistic function. The probability _𝑃_ of accepting a worse solution is given by: 

##### _𝑃_ = exp ( −Δ _𝑇_ _<u>𝑓</u>_ ) 

where Δ _𝑓_ is the change in the objective function value between the new and current solutions, and _𝑇_ is a temperature parameter that decreases over time. As _𝑇_ decreases, the probability of accepting worse solutions diminishes, focusing the search on intensification. 

- Random Number Generation: A random number _𝑟_ is generated uniformly between 0 and 1. If _𝑟_ ≤ _𝑃_ , the new solution is accepted; otherwise, the search continues with the current solution. This method introduces controlled randomness into the acceptance process, balancing exploration and exploitation. 

##### _5.5. Termination criteria_ 

The search process is concluded based on two main criteria: the number of non-improvement steps and a time limit. These criteria ensure that the search does not continue indefinitely and stops when further improvements are unlikely. 

- Non-Improvement Steps: The search tracks the number of consecutive iterations without improvement in the objective function. If this number exceeds a predefined threshold _𝑁𝑚𝑎𝑥_ , the search is terminated. This criterion helps to avoid wasting computational resources when the search is stuck in an unproductive region. 

- Time Limit: Along with non-improvement steps, the search is also subject to a maximum time limit _𝑇𝑚𝑎𝑥_ . If the search process exceeds this time limit, it is automatically terminated, ensuring that the solution is found within a practical timeframe. This is especially important in real-time or near-real-time applications where timely decision-making is critical. 

   - The user population for each instance ranged between 500 and 5000. Distributions were either uniform, representing evenly populated areas, or clustered, simulating urban centers. 

3. UAV Availability: 

   - UAV numbers varied from 10 to 50 per instance, with operational ranges between 5 km and 15 km, and capacities reflecting realistic UAV specifications. 

4. Operational Constraints: 

   - Constraints such as battery life, flight duration, and deployment costs were randomized within realistic bounds to create unique challenges for each instance. 

5. Scenario Variation: 

   - The 40 instances were divided into four categories, each with 10 instances: 

   - Urban Crisis Scenarios: High user density, small geographical area, many UAVs with short-range but high capacity. 

   - Suburban Crisis Scenarios: Moderate user density, medium geographical area, balanced UAV numbers with moderate range and capacity. 

   - Rural Crisis Scenarios: Low user density, large geographical area, fewer UAVs with long-range but lower capacity. 

   - Mixed Crisis Scenarios: Variable user density and geographical area, with randomized UAV availability and constraints. 

##### _6.2. Simulation environment_ 

The simulation environment was implemented using a custom-built tool that models UAV deployment and user coverage. The tool allows for dynamic adjustment of parameters such as UAV range, user movement, and operational constraints, providing data to evaluate the performance of the hyperheuristic approach. 

##### _6.3. Performance evaluation_ 

The results of the hyperheuristic approach across the 40 test instances are summarized in Tables 2 to 5. These tables present key metrics such as average coverage, standard deviation, and computational time for each category of scenarios, indeed, such diverse set of 40 test instances provided a robust framework for evaluating the hyperheuristic approach. Tables 2 to 5 show that the algorithm effectively adapts to different scenarios, achieving high coverage rates and maintaining consistent performance across various user distributions, geographical areas, 

7 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

**Table 2** 

Results for Urban Crisis Scenarios (10 instances). 

|**Instance**|**Coverage** **(%)**|**Latency (ms)**|**Cost (Units)**|**Reliability (%)**|
|---|---|---|---|---|
|1|95|20.5|150|98|
|2|94|21.0|155|97|
|3|96|19.8|152|99|
|4|93|22.3|160|96|
|5|92|23.0|148|95|
|6|94|21.5|154|97|
|7|95|20.7|153|98|
|8|93|22.5|157|96|
|9|94|21.2|149|97|
|10|96|20.0|151|99|
|**Average**|**94.6**|**21.3**|**152.9**|**97.1**|



**Table 3** 

Results for Suburban Crisis Scenarios (10 instances). 

|**Instance**|**Coverage (%)**|**Latency (ms)**|**Cost (Units)**|**Reliability (%)**|
|---|---|---|---|---|
|11|89|30.2|140|92|
|12|87|32.0|145|91|
|13|90|28.5|142|94|
|14|88|31.5|143|93|
|15|86|33.0|139|90|
|16|89|30.5|141|92|
|17|87|32.2|144|91|
|18|88|31.8|143|93|
|19|90|28.9|140|94|
|20|89|30.3|142|92|
|**Average**|**88.3**|**30.9**|**141.9**|**92.2**|



and operational constraints. The results indicate that the hyperheuristic approach is well-suited for managing UAV deployments in complex and variable crisis environments. 

Fig. 1 visualizes the relationship between the average latency and reliability for ten different urban crisis scenarios. The data presented highlights the fluctuations in latency and the consistency of service reliability across the instances. The graph helps to illustrate the trade-off between latency and reliability in UAV-deployed Internet service under urban crisis conditions. The data reveals that the average latency fluctuates between 19.8 ms and 23 ms, while the reliability remains consistently high, ranging from 95% to 99%. 

**Table 4** 

Results for Rural Crisis Scenarios (10 instances). 

|**Instance**|**Coverage (%)**|**Latency (ms)**|**Cost (Units)**|**Reliability (%)**|
|---|---|---|---|---|
|21|81|40.2|120|88|
|22|83|38.7|125|89|
|23|82|39.5|122|88|
|24|80|41.0|118|87|
|25|84|37.8|126|90|
|26|81|40.0|121|88|
|27|83|38.5|124|89|
|28|82|39.2|123|88|
|29|80|41.5|119|87|
|30|84|37.5|125|90|
|**Average**|**82.0**|**39.4**|**122.3**|**88.4**|



**Table 5** 

Results for Mixed Crisis Scenarios (10 instances). 

|**Instance**|**Coverage (%)**|**Latency (ms)**|**Cost (Units)**|**Reliability (%)**|
|---|---|---|---|---|
|31|86|35.0|135|94|
|32|84|36.5|138|93|
|33|87|34.2|134|95|
|34|85|35.5|136|94|
|35|83|37.0|132|92|
|36|86|34.8|135|94|
|37|84|36.2|137|93|
|38|87|34.0|133|95|
|39|85|35.7|136|94|
|40|83|36.8|134|92|
|**Average**|**85.0**|**35.2**|**134.9**|**93.6**|





##### _6.4. Benchmark comparison_ 

In this section, we compare the performance of our approach with the state-of-the-art techniques, particularly those proposed in [1] and [22]. The selected techniques are recently published in the literature and the comparison is done according to the same performance metrics shown in Tables 2-5. The results shown in Fig. 2 demonstrate the efficiency of our approach compared to the existing ones in terms of all performance metrics and various scenarios. The following observations are eminent: 

- From the point of view of coverage and reliability, our approach outperforms better than the others followed by [22] and [1] respectively. Particularly, our approach optimizes the coverage up to 20 _._ 4% and 15 _._ 7%, and the reliability up to 18 _._ 1% and 10 _._ 4% compared to [1] and [22] respectively. 

**Fig. 1.** A comparison of the average latency (ms) and reliability (%) for 10 different urban crisis instances. 

- From the point of view of latency and cost, our approach shows better results than [1] and [22] respectively. Particularly, the latency is optimized up to 9 _._ 8% and 16 _._ 4%, and the cost is reduced by 12 _._ 4% and 14 _._ 7% compared to [1] and [22] respectively. 

- From the point of view of scenarios, our approach demonstrated good performance for all of them while [1] and [22] suffer with rural and mixed crisis. 

##### **7. Conclusion and future work** 

In this study, we explored the optimization of deploying Internet Provider Service Unmanned Aerial Vehicles (UAVs) in crisis scenarios 

8 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 



**Fig. 2.** Our approach vs state-of-the-art: a comparison. Approach 1 and approach 2 indicate those proposed in [1] and [22] respectively, while approach 1 indicates 

ours. 

through a novel hyperheuristic approach. The study integrated various low-level heuristics with a high-level strategy, Monte Carlo-based decision criteria, and specific termination rules to effectively manage the complexities inherent in such dynamic environments. Through extensive experiments conducted across 40 different scenarios, ranging from spanning urban to rural environments, we demonstrated that the hyperheuristic approach consistently provided superior results compared to traditional methods. The framework’s ability to adapt to varying crisis conditions, coupled with its balanced approach to exploring and refining solutions, highlights its practical value in real-world applications. 

Building on these promising findings, future research should explore the real-time application of this hyperheuristic framework in live crisis situations. There is also potential to integrate this approach with other optimization techniques, such as machine learning models or genetic algorithms, to further enhance its effectiveness. Additionally, expanding the use of this framework to other domains like disaster response, healthcare logistics, and urban planning could lead to significant advancements in optimizing complex systems under uncertainty. 

**Declaration of generative AI and AI-assisted technologies in the writing process** 

The authors did not use any generative AI and AI-assisted technologies in the writing process. 

##### **Funding** 

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. 

##### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

##### **Data availability** 

The data are available upon request from authors. 

##### **CRediT authorship contribution statement** 

##### **References** 

**Kassem Danach:** Writing – original draft, Project administration, Formal analysis, Conceptualization. **Hassan Harb:** Writing – review & editing, Investigation, Conceptualization. **Ameer Sardar Kwekha Rashid:** Writing – review & editing, Resources, Methodology. **Mutaz A.B. Al-Tarawneh:** Visualization, Validation, Data curation. **Wael Hosny Fouad Aly:** Supervision, Data curation. 

- [1] A.H. Ahmad, O. Zahwe, A. Nasser, B. Clement, Path planning for unmanned aerial vehicles in dynamic environments: a novel approach using improved a* and grey wolf optimizer, World Electr. Veh. J. 15 (2024). 

- [2] N. Bachir, H. Harb, C. Zaki, R. Billen, Samo: a sequential pattern mining model for evaluating road criticality in urban traffic networks, in: 2024 IEEE 100th Vehicular Technology Conference (VTC2024-Fall), IEEE, 2024, pp. 1–5. 

> [3] M. Brown, S. Taylor, Equitable distribution of uav services in crisis situations, J. Netw. Syst. Manag. 31 (2023) 145–160. 

9 

_K. Danach, H. Harb, A.S.K. Rashid et al._ 

_Results in Engineering 25 (2025) 103833_ 

- [4] E.K. Burke, G. Kendall, Hyper-Heuristics: An Emerging Search Technology, Springer, 2013. 

- [5] S. Chakhlevitch, P. Cowling, Hyperheuristics: recent developments, Evol. Intell. 1 (2008) 47–69. 

- [6] H. Chen, W. Zhang, Lagrangian relaxation techniques for uav deployment in crisis scenarios, Oper. Res. 70 (2022) 112–125. 

- [7] P. Cowling, G. Kendall, E. Soubeiga, A hyperheuristic approach to scheduling a sales summit, Evol. Comput. 9 (2001) 255–276. 

- [8] A. Doe, M. Brown, Optimization of uav networks for emergency communication services, J. Netw. Comput. Appl. 198 (2022) 103456. 

- [9] J.H. Drake, E.K. Burke, A classification of hyper-heuristic approaches, in: Handbook of Metaheuristics, vol. 22, 2015, pp. 449–467. 

- [10] N. Gao, L. Liang, D. Cai, X. Li, S. Jin, Coverage control for uav swarm communication networks: a distributed learning approach, IEEE Internet Things J. 9 (2022) 19854–19867. 

- [11] M. Garcia, C. Rodriguez, Integration of uavs into emergency response frameworks, IEEE Trans. Syst. Man Cybern. 53 (2023) 987–998. 

- [12] F. Glover, Tabu search—part I, ORSA J. Comput. 1 (1989) 190–206. 

- [13] J. Hoxha, M.Y. Çodur, E. Mustafaraj, H. Kanj, A. El Masri, Prediction of transportation energy demand in türkiye using stacking ensemble models: methodology and comparative analysis, Appl. Energy 350 (2023) 121765. 

- [14] R. Johnson, L. Wang, Latency optimization in uav networks for disaster response, IEEE Trans. Wirel. Commun. 22 (2023) 678–689. 

- [15] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 220 (1983) 671–680. 

- [16] A. Kumar, S. Rao, Ai-driven optimization techniques for uav deployment in crisis management, Artif. Intell. Rev. 56 (2023) 193–213. 

- [17] J. Lee, A. Kim, Mathematical modeling of uav deployment for crisis communication, Oper. Res. Lett. 50 (2022) 345–356. 

- [18] X. Liu, B. Lai, B. Lin, V.C. Leung, Joint communication and trajectory optimization for multi-uav enabled mobile Internet of vehicles, IEEE Trans. Intell. Transp. Syst. 23 (2022) 15354–15366. 

- [19] K. Mao, Q. Zhu, C.X. Wang, X. Ye, J. Gomez-Ponce, X. Cai, Y. Miao, Z. Cui, Q. Wu, W. Fan, A survey on channel sounding technologies and measurements for uav-assisted communications, IEEE Trans. Instrum. Meas. (2024). 

- [20] J. Martinez, L. Fernandez, Enhancing uav deployment optimization with valid inequalities, J. Optim. Theory Appl. 174 (2022) 457–472. 

- [21] M. Matracia, M.A. Kishk, M.S. Alouini, Coverage analysis for uav-assisted cellular networks in rural areas, IEEE Open J. Veh. Technol. 2 (2021) 194–206. 

- [22] V. Mayor, R. Estepa, A. Estepa, Qos-aware multilayer uav deployment to provide vowifi service over 5g networks, Wirel. Commun. Mob. Comput. 2022 (2022) 3110572. 

   - [24] I.A. Nemer, T.R. Sheltami, S. Belhaiza, A.S. Mahmoud, Energy-efficient uav movement control for fair communication coverage: a deep reinforcement learning approach, Sensors 22 (2022) 1919. 

   - [25] I.A. Nemer, T.R. Sheltami, A.S. Mahmoud, A game theoretic approach of deployment a multiple uavs for optimal coverage, Transp. Res., Part A, Policy Pract. 140 (2020) 215–230. 

   - [26] T. Nguyen, R. Katila, T.N. Gia, An advanced Internet-of-drones system with blockchain for improving quality of service of search and rescue: a feasibility study, Future Gener. Comput. Syst. 140 (2023) 36–52. 

   - [27] T. Nguyen, M. Tran, Adaptive uav deployment in crisis environments using hyperheuristics, Appl. Soft Comput. 132 (2023) 109845. 

   - [28] R. Patel, I. Khan, Machine learning-enhanced optimization for uav networks in emergency scenarios, IEEE Access 11 (2023) 78901–78914. 

   - [29] N. Promkaew, S. Thammawiset, P. Srisan, P. Sanitchon, T. Tummawai, S. Sukpancharoen, Development of metaheuristic algorithms for efficient path planning of autonomous mobile robots in indoor environments, Results Eng. 22 (2024) 102280. 

   - [30] N.H. Qasim, A.M. Jawad Abu-Alshaeer, H.M. Jawad, Y. Khlaponin, O. Nikitchyn, Devising a traffic control method for unmanned aerial vehicles with the use of gnbiot in 5g, East.-Eur. J. Enterp. Technol. 117 (2022). 

   - [31] P. Ross, Hyper-Heuristics: Theory and Applications, Springer, New York, USA, 2005. 

   - [32] B. Shahzaad, A. Bouguettaya, Service-oriented architecture for drone-based multipackage delivery, in: 2022 IEEE International Conference on Web Services (ICWS), IEEE, 2022, pp. 103–108. 

   - [33] R. Singh, A. Kumar, Hyperheuristic approaches to uav deployment optimization, Expert Syst. Appl. 213 (2023) 118591. 

   - [34] J. Smith, J. Lee, A comprehensive survey on uav deployment strategies in emergency scenarios, IEEE Commun. Surv. Tutor. 25 (2023) 123–145. 

   - [35] A. Srivastava, J. Prakash, Internet of low-altitude uavs (ioloua): a methodical modeling on integration of Internet of “things” with “uav” possibilities and tests, Artif. Intell. Rev. 56 (2023) 2279–2324. 

   - [36] E.G. Talbi, Metaheuristics: From Design to Implementation, John Wiley & Sons, Hoboken, NJ, USA, 2009. 

   - [37] F. Wan, M.B. Yaseen, M.B. Riaz, A. Shafiq, A. Thakur, M.O. Rahman, Advancements and challenges in uav-based communication networks: a comprehensive scholarly analysis, Results Eng. 103271 (2024). 

   - [38] Y. Wang, Q. Zheng, M. Guo, H. Xiao, Y. Bai, An optimal grid scheduling method considering coupling degree of nodes and duality of reciprocal inverse mapping, Results Eng. 23 (2024) 102813. 

   - [39] K. Zaraket, H. Harb, I. Bennis, A. Jaber, A. Abouaissa, Hyper-flophet: a neural prophet-based model for traffic flow forecasting in transportation systems, Simul. Model. Pract. Theory 134 (2024) 102954. 

- [23] I. Nawajah, H. Kanj, Y. Kotb, J. Hoxha, M. Alakkoumi, K. Jebreen, Bayesian regression analysis using median rank set sampling, Eur. J. Pure Appl. Math. 17 (2024) 180–200. 

10 

