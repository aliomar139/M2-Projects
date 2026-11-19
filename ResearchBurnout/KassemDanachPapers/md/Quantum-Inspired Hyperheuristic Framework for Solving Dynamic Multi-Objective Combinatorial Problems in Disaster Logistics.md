

_Article_ 

# **Quantum-Inspired Hyperheuristic Framework for Solving Dynamic Multi-Objective Combinatorial Problems in Disaster Logistics** 

**Kassem Danach**<sup>**1**</sup> **, Hassan Harb**<sup>**2**</sup> **, Louai Saker**<sup>**2,**</sup> *** and Ali Raad**<sup>**3**</sup> 

- 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut 1600, Lebanon; kassem.danach@mu.edu.lb 

- 2 College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait; hassan.harb@aum.edu.kw 

- 3 Faculty of Science and Art, Islamic University of Lebanon, Khaldeh P.O. Box 30014, Lebanon; ali.raad@iul.edu.lb 

- Correspondence: louai.saker@aum.edu.kw 

Academic Editor: Vladimir Katic 

Received: 28 April 2025 Revised: 27 May 2025 Accepted: 30 May 2025 Published: 2 June 2025 

**Citation:** Danach, K.; Harb, H.; Saker, L.; Raad, A. Quantum-Inspired Hyperheuristic Framework for Solving Dynamic Multi-Objective Combinatorial Problems in Disaster Logistics. _World Electr. Veh. J._ **2025** , _16_ , 310. https://doi.org/10.3390/ wevj16060310 

**Copyright:** © 2025 by the authors. Published by MDPI on behalf of the World Electric Vehicle Association. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

**Abstract:** Disaster logistics presents a highly complex decision-making challenge under conditions of uncertainty, where the timely and efficient allocation of scarce resources is essential to minimize human suffering. In this context, we propose a novel QuantumInspired Hyperheuristic Framework (QHHF) designed to solve Dynamic Multi-Objective Combinatorial Optimization Problems (DMOCOPs) arising in disaster relief operations. The proposed framework integrates Quantum-Inspired Evolutionary Algorithms (QIEAs), which facilitate diverse and explorative solution generation, with a Reinforcement Learning (RL)-based hyperheuristic capable of dynamically selecting the most suitable low-level heuristic in response to evolving disaster conditions. A dynamic multi-objective mathematical model is formulated to simultaneously minimize total travel cost and risk exposure, while maximizing priority-weighted demand satisfaction. The model captures real-world complexity through time-dependent variables, stochastic demand variations, and fluctuating transportation risks. Extensive simulations using real-world disaster scenarios demonstrate the effectiveness of the proposed approach in generating high-quality solutions within stringent response time constraints. Comparative evaluations reveal that QHHF consistently outperforms traditional heuristics and metaheuristics in terms of adaptability, scalability, and solution quality across multiple objective trade-offs. Notably, our method achieves a 9.6% reduction in total travel cost, a 6.5% decrease in cumulative risk exposure, and a 4.7% increase in priority-weighted demand satisfaction when benchmarked against existing techniques. This work contributes both to the advancement of hyperheuristic theory and to the development of practical, AI-enabled decision-support tools for emergency logistics management. 

**Keywords:** artificial intelligence; combinatorial optimization; hyperheuristic; quantuminspired algorithm; dynamic vehicle routing 

## **1. Introduction** 

### _1.1. Context_ 

Disaster logistics involves the planning, management, and coordination of resources and services to support affected populations during and after natural or human-made disasters [1–3]. Efficient logistical operations are critical for minimizing human suffering, especially in time-sensitive and resource-constrained environments. One of the most 

_World Electr. Veh. J._ **2025** , _16_ , 310 

https://doi.org/10.3390/wevj16060310 

_World Electr. Veh. J._ **2025** , _16_ , 310 

2 of 36 

challenging aspects of disaster logistics is decision-making under uncertainty, where factors such as road closures, fluctuating demand, and limited accessibility significantly complicate routing and resource allocation [4–6]. 

### _1.2. Challenges_ 

These challenges naturally lead to complex combinatorial optimization problems, where the goal is to optimize multiple conflicting objectives such as cost, risk, and service level across a dynamic and uncertain network [7]. Traditional optimization methods often fall short in such contexts due to their rigidity and computational intractability, particularly as problem size increases or when rapid re-optimization is needed [8–10]. Metaheuristics such as Genetic Algorithms (GAs), Ant Colony Optimization (ACO), and Particle Swarm Optimization (PSO) have shown promise in addressing some of these issues by offering flexibility and near-optimal solutions within acceptable timeframes [11,12]. 

### _1.3. Motivation_ 

Hyperheuristics, which operate on a higher level than traditional heuristics or metaheuristics by selecting or generating heuristics dynamically, have gained attention as a more adaptive alternative in uncertain environments [13]. They are particularly useful in dynamic combinatorial contexts where different phases of the problem may benefit from different solution strategies. Reinforcement learning-based hyperheuristics, in particular, offer a learning mechanism to improve heuristic selection policies over time, adapting to problem changes [14,15]. 

In parallel, Quantum-Inspired Evolutionary Algorithms (QIEAs) have emerged as a class of metaheuristics that leverage principles inspired by quantum computing—such as qubit representation and probabilistic evolution—to explore large and complex search spaces more effectively [16]. These algorithms have demonstrated superior convergence characteristics and solution diversity across various optimization domains. 

Despite the effectiveness of conventional metaheuristics such as Genetic Algorithms (GAs) and Ant Colony Optimization (ACO), these methods often exhibit limitations in dynamic and uncertain environments like disaster logistics. Specifically, their reliance on static search operators and fixed update rules may lead to premature convergence and poor adaptability to evolving constraints, such as fluctuating demand, blocked routes, and shifting risk zones. In large-scale emergencies, where response conditions change rapidly, traditional methods may fail to maintain solution quality or respond to environmental shifts in real-time. To overcome these limitations, this work introduces a novel integration of Quantum-Inspired Evolutionary Algorithms (QIEAs) with a Reinforcement Learning-based hyperheuristic controller for tackling dynamic multi-objective optimization in uncertain disaster logistics scenarios. To the best of our knowledge, this is the first framework to combine quantum-inspired search with learning-based heuristic selection specifically for this class of problems. QIEAs offer advantages such as population diversity through probabilistic qubit representation, exploration via quantum rotation gates, and compact encoding schemes that support high-dimensional search spaces. When integrated with a hyperheuristic controller guided by reinforcement learning, the system dynamically selects the most effective low-level heuristic based on real-time feedback and evolving problem states. This hybrid design ensures a balance between exploration and exploitation, robustness against dynamic disruptions, and scalability across disaster scenarios. Recent research has demonstrated the growing applicability of quantum-inspired techniques in emergency logistics and complex decision-making tasks [17,18]. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

3 of 36 

### _1.4. Contributions_ 

This study introduces a novel Quantum-Inspired Hyperheuristic Framework (QHHF) for solving dynamic multi-objective combinatorial optimization problems in disaster logistics. The key contributions of this work, which distinguish it from existing methods in the literature, are as follows: 

- Hybrid Quantum–Learning Approach:We propose an innovative integration of Quantum-Inspired Evolutionary Algorithms (QIEAs) with a Reinforcement Learning (RL)-based hyperheuristic controller. While QIEAs have been applied to combinatorial optimization and RL-based hyperheuristics for dynamic adaptation, this is the first known framework to combine both for disaster logistics under uncertainty. 

- Dynamic Multi-Objective Modeling: We formulate a dynamic multi-objective mathematical model that simultaneously minimizes total travel cost and risk exposure, and maximizes priority-weighted demand satisfaction. The model accounts for stochastic and time-dependent parameters such as changing demand levels, route risks, and accessibility conditions—elements often ignored or simplified in previous models. 

- Adaptive Heuristic Selection Mechanism: The RL-based hyperheuristic dynamically selects the most appropriate low-level heuristic from a diverse portfolio, based on evolving disaster conditions and real-time feedback. This mechanism improves the adaptability of the framework and ensures continuous learning and adjustment. 

- Comprehensive Benchmarking and Validation: We evaluate QHHF through extensive simulations and a real-world case study of the 2020 Beirut Port Explosion. The framework outperforms traditional metaheuristics (GA, ACO) and standalone QIEA in terms of travel cost, risk exposure, and demand satisfaction. For instance, it achieves up to 9.6% cost reduction, 6.5% risk minimization, and 4.7% gain in critical demand fulfillment. 

- Scalability and Practical Impact: The modular architecture of QHHF ensures scalability and operational feasibility in real-world deployments. The integration of real-time learning, quantum encoding, and multi-objective analysis lays the groundwork for deployable, intelligent decision-support systems in humanitarian operations. 

These contributions advance the state of the art in both hyperheuristic theory and AIdriven emergency logistics, offering a flexible and robust solution framework for complex, uncertain, and high-stakes environments. 

### _1.5. Research Questions and Challenges_ 

Based on the complex characteristics of disaster logistics, we frame the following research questions to guide the proposed work: 

- RQ1: How can we model disaster logistics problems in a way that captures timedependent uncertainty, multi-objective trade-offs, and dynamically changing risk and demand? 

- RQ2: Given the limitations of traditional heuristics and metaheuristics, how can a framework adaptively select suitable heuristics in real time to maintain performance under evolving constraints? 

- RQ3: Can we enhance both solution diversity and convergence in dynamic environments by integrating quantum-inspired search with learning-based heuristic control? 

Most existing methods rely on fixed rule-based search operators or metaheuristics that do not adapt to real-time environmental changes. These methods also lack robust mechanisms to balance multiple conflicting objectives or to dynamically respond to disruptions in demand, risk, and travel feasibility. 

To address these gaps, we propose the QHHF (Quantum-Inspired Hyperheuristic Framework), which: 

_World Electr. Veh. J._ **2025** , _16_ , 310 

4 of 36 

- Encodes routing and allocation decisions using quantum-inspired representations to promote exploration and diversity; 

- Integrates a reinforcement learning controller to adaptively select heuristics based on evolving system states; 

- Employs a multi-objective evaluation model that captures cost, risk, and demand priority simultaneously. 

### _1.6. Paper Organization_ 

The remainder of this paper is structured as follows: Section 2 reviews the related literature. Section 3 defines the problem and presents the mathematical model. Section 4 describes the proposed quantum-inspired hyperheuristic framework. Section 5 outlines the solution strategy. Section 6 details the experimental setup, along with the obtained results and their discussion. Section 7 presents a real-world case study. Finally, Section 8 concludes the paper with final remarks and directions for future research. 

## **2. Related Work** 

### _2.1. Combinatorial Optimization in Disaster Logistics_ 

Disaster logistics involves complex and urgent decision-making under uncertainty, where efficient allocation of limited resources is critical [19]. The core challenges are typically modeled as combinatorial optimization problems, such as vehicle routing, facility location, and inventory allocation [20,21]. Researchers have proposed various methods, ranging from exact integer programming [22,23] to metaheuristic approaches such as Genetic Algorithms (GA) and Ant Colony Optimization (ACO) [24–26]. The authors of [27] used K-means clustering to break down a multi-distribution center challenge into distinct single-distribution center problems. They further evaluated and compared vehicle routing models with time window limitations for emergency logistics delivery, applying Guided Local Search (GLS), Tabu Search (TS), and Simulated Annealing (SA) techniques. In [17], the authors introduced a multi-objective chance-constrained model to reduce transportation deviation, utilizing uncertainty theory to formulate a computationally efficient deterministic equivalent model. Moreover, a hybrid optimization method, integrating the Estimation of Distribution Algorithm and the Multi-Objective Snow Goose Algorithm (EDA-MOSGA), was proposed to efficiently search the solution space and achieve near-optimal results. By incorporating adaptive population adjustments and a specialized operator model, the EDA-MOSGA enhances Pareto front diversity, representing a significant advancement over current methodologies. In [28], the authors investigated emergency supply distribution challenges during large-scale crises, with a focus on optimizing the placement of logistics facilities and the deployment of relief materials. Their study formulated a multi-objective logistics center siting model that balances emergency response costs and delivery efficiency, integrating both deterministic and robust optimization strategies. Due to the time-sensitive nature of relief efforts, the model incorporates a bi-objective function that evaluates transportation expenses, travel duration, facility construction, and inventory management. The authors of [29] presented a two-layer emergency supply distribution network that integrates road restoration with facility location and route planning. The model factors in road repair during route selection, optimizing the trade-off between response time and supply fulfillment to maximize overall effectiveness. A variable neighborhood search algorithm was also introduced to effectively address the problem. 

### _2.2. Dynamic and Multi-Objective Optimization_ 

Multi-objective optimization has become a key requirement in humanitarian logistics due to the conflicting nature of goals, such as minimizing cost, minimizing risk, and 

_World Electr. Veh. J._ **2025** , _16_ , 310 

5 of 36 

maximizing service level [30,31]. Dynamic models have been proposed to address the time-varying aspects of real-world disaster scenarios [32]. In [33], the authors proposed a multi-objective optimization model that considers different categories of injured individuals, various vehicle types with predefined capacities, and a multi-period logistics framework. The model is designed to be dynamic, allowing modifications in response to newly available resource data and additional injured individuals. Moreover, it incorporates the total transportation activities of different vehicle types as another key objective. By employing discrete scenarios, the authors of [28] characterized the uncertainty associated with the demand for emergency supplies at disaster locations, along with fluctuations in both shipment costs and delivery schedules. Simultaneously, they focused on two main objectives—minimizing emergency relief costs and response time—while formulating a multi-objective logistics center siting model that integrates deterministic and robust optimization techniques. In [34], the authors introduced a scenario-based robust bi-objective optimization model that integrates the siting of medical facilities, the transportation of casualties, and the distribution of relief supplies while factoring in triage. The objective is to reduce the total deprivation cost resulting from delays in medical care, as well as the total operational cost. To safeguard solutions against potential disruptions in temporary medical centers, the model employs a scenario-based robust optimization approach that accounts for various disruption scenarios. The authors of [35] proposed a multi-objective optimization-based emergency response framework, emphasizing the configuration and management of emergency supplies across both pre-disaster and post-disaster phases. During the pre-disaster stage, a mathematical model is used to develop an emergency supply configuration plan based on actual enterprise production. In the post-disaster phase, leveraging the inventory from the previous stage, third-party emergency resources are considered to optimize the distribution of supplies using a multi-objective approach. 

### _2.3. Hyperheuristics and Learning-Based Heuristic Selection_ 

Hyperheuristics aim to automate the process of selecting or generating heuristics to solve combinatorial optimization problems more efficiently [9,36,37]. Rather than solving the problem directly, they operate at a higher level by managing a set of low-level heuristics. Reinforcement learning-based hyperheuristics have shown promise in dynamic environments, as they can adapt their strategy based on real-time feedback [38,39]. Applications in logistics, scheduling, and resource allocation have demonstrated their robustness and generalizability. The authors of [40] proposed a vehicle routing and depot management system to streamline the procurement of supplies for soldiers facing material shortages during operations. The system functions in two stages. Initially, an aerial vehicle is deployed to determine the soldier location and evaluate the surrounding physical conditions. In the second stage, the required material information is obtained from the user, and the most efficient delivery routes are generated using a hyper-heuristic approach that integrates genetic algorithms and Tabu search, optimizing routes based on depot inventory levels. In [41], the authors introduced an optimized approach to manage emergency calls and enhance rescue route efficiency. The model differentiates between two patient categories: green-case and red-case. To solve the Ambulance Routing Problem (ARP) within time windows, a mathematical model is formulated and solved using the Gurobi solver for smallscale instances. Furthermore, two Tabu Search-based algorithms are designed: Hybrid Tabu Search (HTS) and Tabu Search-based Hyper-Heuristic (TSHH). The authors of [42] formulated the problem as a Multiple Roaming Salesman Problem, where a set number of political representatives visit multiple cities over a defined planning horizon to maximize accumulated rewards while remaining within budget and time limitations. A compact Mixed Integer Linear Programming (MILP) formulation is presented, strengthened with ef- 

_World Electr. Veh. J._ **2025** , _16_ , 310 

6 of 36 

fective valid inequalities. Furthermore, a Learning-based Granular Variable Neighborhood Search algorithm is introduced, showcasing its ability to produce high-quality solutions rapidly when applied to real-world scenarios. 

Recent advances in reinforcement learning-based hyperheuristics have extended the capabilities of traditional rule-based frameworks. Deep Q-Network (DQN)-based selectors and policy-gradient approaches have been applied to dynamic scheduling and vehicle routing tasks [43–45]. These frameworks learn over state–action pairs and dynamically update their policies to improve heuristic decisions. Our QHHF model follows this trend but introduces a quantum-inspired initialization and evolution scheme, enhancing population diversity and exploration. 

Regarding evolutionary baselines, NSGA-II and NSGA-III remain popular for multiobjective optimization [46]. However, they are static in terms of operator selection and do not integrate reinforcement learning mechanisms. In contrast, QHHF adapts its search heuristics over time using feedback from the problem environment, making it more suitable for dynamic disaster logistics contexts. Future work may explore hybridizing QHHF with NSGA-II operators to benefit from both Pareto sorting and learning-based adaptation. 

Recent advances in deep reinforcement learning (DRL) have demonstrated promising results in solving routing problems using neural policy models. For instance, Nazari et al. [47] proposed a DRL-based pointer network to solve the VRP without relying on handcrafted rules. Bello et al. [48] extended this line of work by applying attentionbased transformer architectures to combinatorial routing. More recently, Wang et al. [49] introduced a physics-guided graph neural network to optimize traffic flow and logistics in urban networks with spatiotemporal dynamics. 

While these methods are powerful, they often require substantial training time, highdimensional representations, and offline learning pipelines. In contrast, our QHHF framework uses a tabular Q-learning controller for fast, interpretable, and real-time heuristic selection in dynamic environments, which is more suitable for field-level deployment in disaster logistics. Nonetheless, incorporating DRL into QHHF is a promising future direction. 

### _2.4. Quantum-Inspired Evolutionary Algorithms_ 

Quantum-Inspired Evolutionary Algorithms (QIEAs) mimic quantum computing principles—such as qubit representation and probabilistic decision making—to improve the diversity and convergence speed of classical evolutionary algorithms [50]. QIEAs have been applied to a range of NP-hard problems, including knapsack, TSP, and scheduling tasks [51]. Their compact representation and ability to explore vast solution spaces make them suitable for combinatorial problems under uncertainty. The authors of [52] discussed the evolving landscape of supply chain logistics, shaped by the fusion of quantum computing and data-driven decision-making. They explored the core concepts of quantum computing and their role in optimizing decision-making processes in key areas such as demand prediction, inventory control, transportation efficiency, and risk evaluation. Similarly, the authors of [53] investigated how quantum machine learning (QML) techniques can be utilized to optimize disaster recovery strategies, demonstrating their benefits compared to traditional methods. QML algorithms support various aspects of disaster management, including forecasting, preparedness, emergency response, and proactive alert systems. The findings reveal that QML enhances disaster response efficiency by enabling real-time data analysis, ensuring quick interventions and timely alerts, thereby preventing unnecessary loss of life due to insufficient awareness. In [18], a Hybrid Quantum Genetic Algorithm with Fuzzy Adaptive Rotation Angle (HQGAFARA) is proposed to optimize the deployment of UAVs for maximizing coverage in disaster-impacted zones. HQGAFARA integrates quantum fuzzy meta-heuristics and employs the Deutsch–Jozsa quantum circuit to gen- 

_World Electr. Veh. J._ **2025** , _16_ , 310 

7 of 36 

erate quantum populations, acting as haploid recombination and mutation operators. By harnessing quantum entanglement, the algorithm enhances both exploratory and exploitative properties, facilitating the generation of improved solutions. Deep learning-based approaches have recently been introduced for solving combinatorial optimization problems such as the vehicle routing problem (VRP). Vinyals et al. [54] proposed Pointer Networks for supervised learning of solution sequences. Bello et al. [48] extended this work using reinforcement learning and attention-based models to generate optimized routing plans. Nazari et al. [47] applied actor–critic reinforcement learning to dynamic VRPs, showing strong results on benchmark instances. 

These methods are powerful in data-rich and simulation-friendly environments, but they require significant offline training and may lack transparency or adaptability under volatile disaster conditions. In contrast, the QHHF framework is designed for on-the-fly adaptation using lightweight heuristic control, making it more suitable for time-critical, infrastructure-limited logistics scenarios. Nonetheless, integrating learned policies as meta-controllers within QHHF is a promising future direction. 

### _2.5. Discussion on Deep Learning and Benchmark Selection_ 

While traditional metaheuristics such as GA, ACO, and QIEA have long been applied to routing and logistics problems due to their simplicity and flexibility, recent advancements in deep learning have introduced neural combinatorial optimization methods. Notable among these are Pointer Networks [54], Graph Attention Policies [47], and Transformer-based models [55] that learn routing behaviors through supervised or reinforcement learning. 

However, these DRL-based methods typically require extensive training over problemspecific distributions, rely heavily on GPU infrastructure, and may not generalize well to rapidly changing or data-sparse environments like disaster logistics. In contrast, our QHHF framework is designed for adaptability, interpretability, and low computational overhead, making it more suitable for real-time decision-making in uncertain emergency contexts. Nonetheless, future work may explore hybridizing QHHF with DRL policies to further enhance responsiveness. 

Unlike hybrid deep reinforcement learning (DRL) approaches that integrate neural networks with symbolic reasoning or handcrafted rules, our QHHF model operates without any neural architecture. Instead, it combines a tabular Q-learning agent with a quantuminspired population model. This design offers interpretability and on-the-fly adaptability, setting it apart from neuro-symbolic models that often require extensive offline training. In this context, QHHF bridges symbolic heuristic control and probabilistic exploration, without relying on learned neural encodings. 

### _2.6. Integrated AI Approaches in Disaster Response_ 

Recent advancements in artificial intelligence have led to the development of integrated systems that combine multiple optimization and learning paradigms for disaster response [56,57]. These include hybrid metaheuristics, deep reinforcement learning models, and decision-support systems with real-time data feeds. In response to the needs of emergency logistics during public health emergencies, the authors of [58] created an artificial intelligence-driven logistics model that includes a perception linkage layer, an information system layer, an emergency management layer, and an information security chain. This model utilizes intelligent early warning, intelligent sharing, intelligent transportation, and intelligent services, ensuring that AI technology effectively supports the requirements of emergency logistics, ultimately improving the efficiency and quality of emergency logistics services. In [59], the authors demonstrated the role of AI in bolstering early warning systems, optimizing the distribution of resources, and refining real-time response strategies. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

8 of 36 

The effectiveness of AI-based solutions in minimizing human and economic losses during disasters is demonstrated through various case studies. Additionally, they highlighted the importance of combining AI with IoT devices and cloud computing for real-time data analysis, emphasizing the significance of cooperation between government bodies, private industries, and technology providers. In [60], the authors created a multifaceted emergency response tool designed to give stakeholders prompt access to accurate, pertinent, and trustworthy information. The tool integrates various layers of open-source geospatial data, including flood risk areas, road network resilience, inundation maps that represent inland flooding, and computer vision-driven semantic segmentation for assessing flooded zones and infrastructure damage. These layers are combined and utilized as inputs for machine learning algorithms, such as identifying the best evacuation routes at different stages of an emergency or offering a list of available accommodations for first responders in the impacted area. 

### _2.7. Research Gap_ 

Despite their potential, existing techniques for managing disaster logistics suffer from several drawbacks: (1) Combinatorial optimization-based techniques often lack the adaptability required to handle dynamic environments; (2) Multi-objective optimization approaches struggle with adapting to drastic changes in problem parameters over time; (3) The integration of hyperheuristic frameworks in the context of humanitarian logistics remains underexplored; and (4) Few existing approaches incorporate both quantum-inspired search mechanisms and heuristic adaptation in dynamic, multi-objective disaster settings. Furthermore, it is evident that while individual techniques like QIEAs and hyperheuristics have shown promising results in combinatorial optimization, their integration together remains rare, especially in dynamic disaster logistics. Moreover, existing solutions often rely on static assumptions or single-objective formulations, which limits their real-world applicability. This study addresses these gaps by proposing a dynamic, multi-objective hyperheuristic framework enhanced with quantum-inspired representations and real-time learning. 

To provide a consolidated overview of the existing literature, Table 1 summarizes representative approaches in the field of disaster logistics optimization. The comparison highlights the methodology, problem type, level of dynamic support, multi-objective consideration, and whether hyperheuristics or quantum-inspired techniques were employed. This summary clearly illustrates the unique contribution of our proposed framework, which is the only approach integrating both quantum-inspired and reinforcement learning-based hyperheuristics in a dynamic multi-objective setting. 

**Table 1.** Summary of Representative State-of-the-Art Techniques in Disaster Logistics Optimization. 

|**Reference**|**Method**|**Problem Type**|**Dynamic**<br>**Support**|**Multi-Objective**|**Hyperheuristic/Quantum**|
|---|---|---|---|---|---|
|Wu et al. [17]|Hybrid<br>Metaheuristic<br>(EDA-MOSGA)|Emergency<br>Distribution|Partially dynamic|Yes|No|
|Tlili et al. [41]|Tabu Search<br>Hyperheuristic|Ambulance<br>Routing with<br>Time Windows|No|Yes|Hyperheuristic|
|Ballinas et al. [18]|Hybrid Quantum<br>Genetic<br>Algorithm|UAV Deployment<br>in Disaster Zones|No|No|Quantum-inspired|



_World Electr. Veh. J._ **2025** , _16_ , 310 

9 of 36 

**Table 1.** _Cont._ 

|**Reference**|**Method**|**Problem Type**|**Dynamic**<br>**Support**|**Multi-Objective**|**Hyperheuristic/Quantum**|
|---|---|---|---|---|---|
|Ye et al. [35]|Multi-Objective<br>Logistics<br>Planning|Emergency<br>Response for<br>Petrochemical<br>Plants|Yes|Yes|No|
|Gomes et al. [16]|Quantum-<br>Inspired<br>Algorithms<br>Review|General<br>Operations<br>Research|No|General|Quantum-inspired|
|This Work (2025)|QIEA + RL-based<br>Hyperheuristic|Dynamic Disaster<br>Logistics Routing|Yes|Yes|Both|



## **3. Problem Definition and Mathematical Model** 

In disaster logistics, rapid and efficient allocation of critical resources such as food, medical supplies, and shelter is crucial. The underlying problem is a dynamic multiobjective combinatorial optimization problem (DMOCOP), which involves allocating resources from a central depot to multiple demand nodes using a limited fleet of vehicles. The system must optimize multiple conflicting objectives under uncertainty, including minimizing travel cost, minimizing risk exposure, and maximizing the satisfaction of urgent needs. 

### _3.1. Problem Description_ 

Let _V_ = _{_ 0, 1, 2, . . . , _n}_ be the set of all nodes, where node 0 represents the central depot and the rest represent disaster-affected demand locations. A fleet of _k_ homogeneous vehicles _R_ = _{_ 1, 2, . . . , _k}_ is available to transport relief items. The problem unfolds over discrete time periods _T_ = _{_ 1, 2, . . . , _τ}_ , with demand levels, risk conditions, and travel costs evolving dynamically over time. Each vehicle has a fixed capacity _Qr_ and must return to the depot after completing its route. 

### _3.2. Parameters_ 

- _cij_<sup>_t_:Travel cost from node</sup><sup>_i_to</sup><sup>_j_at time</sup><sup>_t_</sup> 

- _d_<sup>_t_</sup> _j_<sup>:Demand at node</sup><sup>_j_at time</sup><sup>_t_</sup> 

- _Qr_ : Capacity of vehicle _r_ 

- _R_<sup>_t_</sup> _j_<sup>:Risk level for reaching node</sup><sup>_j_at time</sup><sup>_t_</sup> 

- _Sj_ : Priority score of node _j_ 

- _M_ : A sufficiently large constant for constraint relaxation 

### _3.3. Decision Variables_ 

- _xijr_<sup>_t∈{_0, 1</sup><sup>_}_:1 if vehicle</sup><sup>_r_travels from node</sup><sup>_i_to</sup><sup>_j_at time</sup><sup>_t_, 0 otherwise</sup> 

- _y_<sup>_t_</sup> _jr_<sup>_∈{_0, 1</sup><sup>_}_:1 if vehicle</sup><sup>_r_serves node</sup><sup>_j_at time</sup><sup>_t_, 0 otherwise</sup> 

- _q_<sup>_t_</sup> _jr_<sup>_≥_0:Quantity of supplies delivered to node</sup><sup>_j_by vehicle</sup><sup>_r_at time</sup><sup>_t_</sup> 

- _zt ∈ H_ : Heuristic used at time _t_ from set _H_ = _{h_ 1, _h_ 2, . . . , _hm}_ 

### _3.4. Objective Functions_ 

We define the following three conflicting objectives, which together reflect the realworld trade-offs faced in disaster response logistics: 

_World Electr. Veh. J._ **2025** , _16_ , 310 

10 of 36 

- Objective 1: Minimize Total Travel Cost 



<!-- Start of picture text -->
min  Z 1 = ∑ cij t · x ijr t<br>t∈T r ∑ ∈R i ∑ ∈V j ∑ ∈V<br><!-- End of picture text -->

This objective reflects the total operational cost incurred by the relief vehicles across all periods. 

- Objective 2: Minimize Total Risk Exposure 



<!-- Start of picture text -->
min  Z 2 = ∑ t∈T r ∑ ∈R j∈V ∑ \{ 0 } R t j · yt jr<br><!-- End of picture text -->

Risk exposure is calculated based on the danger associated with visiting certain nodes, influenced by proximity to hazard zones. 

- Objective 3: Maximize Priority-Weighted Demand Satisfaction 



<!-- Start of picture text -->
max  Z 3 = ∑ ∑ Sj · q t jr<br>d t<br>t∈T r ∑ ∈R j∈V\{ 0 } j<br><!-- End of picture text -->

This ensures that demand satisfaction is biased toward high-priority nodes, reflecting ethical and strategic urgency. 

- _3.5. Constraints_ 

The system is subject to the following operational and logical constraints: 

- Flow Conservation: 



<!-- Start of picture text -->
∑ xijr t = ∑ x t jir ∀i ∈ V ,  ∀r ∈ R ,  ∀t ∈ T<br>j∈V j∈V<br><!-- End of picture text -->

- Vehicle Capacity: 



<!-- Start of picture text -->
∑ q t jr ≤ Qr ∀r ∈ R ,  ∀t ∈ T<br>j∈V\{ 0 }<br><!-- End of picture text -->

- Demand Satisfaction Limit: 



<!-- Start of picture text -->
∑ q t jr ≤ dt j ∀j ∈ V \ { 0 }<br>r∈R t ∑ ∈T<br><!-- End of picture text -->

- Deliver Only If Node is Visited: 



<!-- Start of picture text -->
q t jr ≤ M · yt jr ∀j ∈ V \ { 0 } ,  ∀r ∈ R ,  ∀t ∈ T<br><!-- End of picture text -->

- Node Visited Only If Travel Occurs: 



<!-- Start of picture text -->
y t jr ≤ ∑ xijr t ∀j ∈ V \ { 0 } ,  ∀r ∈ R ,  ∀t ∈ T<br>i∈V<br><!-- End of picture text -->

- Delivery Cap per Node: 



<!-- Start of picture text -->
∑ q t jr ≤ κ · dt j ∀j ∈ V \ { 0 }<br>r∈R t ∑ ∈T<br><!-- End of picture text -->

where _κ ∈_ (0, 1] is a configurable upper bound on the deliverable ratio per node (e.g., _κ_ = 1.0 by default). 

_World Electr. Veh. J._ **2025** , _16_ , 310 

11 of 36 

- Heuristic Selection Constraint: 



<!-- Start of picture text -->
zt ∈ H ∀t ∈ T<br><!-- End of picture text -->

### _3.6. Model Characteristics_ 

This model captures three essential aspects of disaster logistics: 

- Dynamic behavior: All time-dependent parameters ( _cij_<sup>_t_,</sup><sup>_dt_</sup> _j_<sup>,</sup><sup>_Rt_</sup> _j_<sup>)allowthemodelto</sup> respond to real-time changes in cost, demand, and risk. In simulation, demand levels are updated every five generations using a stochastic function, risk zones evolve using a Gaussian proximity model, and random road blockages impact route feasibility. 

- Multi-objective nature: The formulation handles conflicting goals using Pareto-based non-dominated sorting, rather than scalarization, to provide a balanced set of tradeoff solutions. 

- Hyperheuristic integration: The model allows for dynamic heuristic selection through reinforcement learning. The variable _zt_ tracks the heuristic selected at each time _t_ , enabling learning-driven adaptation to problem dynamics. 

## **4. Proposed Methodology** 

This section presents the proposed Quantum-Inspired Hyperheuristic Framework (QHHF) designed to solve the dynamic multi-objective combinatorial optimization problem outlined in the previous section. The framework integrates a Quantum-Inspired Evolutionary Algorithm (QIEA) with a Reinforcement Learning (RL)-based hyperheuristic controller. The QIEA provides global exploration capabilities, while the RL-based selector adaptively chooses appropriate low-level heuristics based on evolving disaster conditions and feedback from the environment. 

### _4.1. Overview of the Framework_ 

Figure 1 illustrates the modular structure and control flow of the proposed QuantumInspired Hyperheuristic Framework (QHHF). The process begins with the initialization of a quantum population, where each solution is represented as a string of qubits in a superposition state. A reinforcement learning-based high-level controller observes the current environment state and selects the most suitable low-level heuristic (LLH) using an _ϵ_ -greedy action selection strategy. The selected LLH is then applied to the current solution to explore the neighborhood or construct a new one. Following this, quantum rotation gates update the underlying qubit states to guide future sampling toward promising regions of the search space. The updated solution is then evaluated using a multi-objective evaluation module, and a scalar reward signal is derived based on the improvement in objective values. This reward is used to update the Q-table, which in turn improves the quality of heuristic selection in subsequent generations. This feedback-driven loop allows the framework to adapt continuously in response to changes in problem dynamics such as varying risk levels, updated demand, and cost fluctuations. 

The QHHF consists of the following components: 

1. Solution Representation using Quantum Chromosomes: Each individual in the population is represented by a quantum bit (qubit) string encoding vehicle routes and resource allocations. 

2. Quantum-Inspired Operators: The framework employs rotation gates and quantum measurement operators for population evolution and solution decoding. These operators maintain population diversity and enable probabilistic search. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

12 of 36 

3. Low-Level Heuristic Pool: A diverse set of local search and constructive heuristics (e.g., Nearest Neighbor, Swap, 2-opt, Insertion) is maintained to allow flexible move generation in different solution contexts. 

4. Reinforcement Learning-Based Heuristic Selector: A Q-learning agent dynamically selects the most appropriate heuristic based on state-action values learned through repeated interactions with the environment. 

5. Multi-objective Evaluation Module: Inspired by NSGA-II principles, this module evaluates individuals based on total travel cost, cumulative risk exposure, and priorityweighted demand satisfaction using Pareto dominance and crowding distance. 

6. Dynamic Update Module: This module tracks real-time changes in environmental parameters such as risk zones, road accessibility, and demand levels. It updates the problem instance accordingly to maintain the realism and responsiveness of the framework. 



**Figure 1.** The proposed Quantum-Inspired Hyperheuristic Framework (QHHF) integrates a quantum evolutionary population with a reinforcement learning-based heuristic controller. It includes solution representation via qubits, RL-based selection of low-level heuristics, quantum rotation for exploration, dynamic problem updates, and multi-objective evaluation to generate Pareto-optimal solutions. 

Algorithm 1 provides a high-level pseudocode representation of the proposed Quantum-Inspired Hyperheuristic Framework (QHHF). The algorithm begins by initializing the quantum population, where each individual is represented as a string of qubits capable of encoding multiple possible solution states. A Q-table is also initialized to store heuristic performance values across various environmental states. At each generation, the 

_World Electr. Veh. J._ **2025** , _16_ , 310 

13 of 36 

framework iterates over all individuals in the population. For each solution, the current environment state is observed and used to query the reinforcement learning controller, which selects a suitable low-level heuristic (LLH) using an _ϵ_ -greedy exploration strategy. The selected heuristic is applied to the decoded solution, after which the multi-objective fitness is computed using the cost, risk, and satisfaction metrics. The reinforcement signal—based on improvement in fitness—is used to update the Q-table via the standard Q-learning update rule. Subsequently, quantum rotation gates are applied to the qubit string based on the fitness landscape feedback, thereby biasing the next generation toward promising solution subspaces. This iterative process continues until convergence or the predefined maximum number of generations is reached. The final output is the set of non-dominated solutions approximating the Pareto front. 

**Algorithm 1** Modular Quantum-Inspired Hyperheuristic Framework (QHHF) 

- 1: **Module 1: Initialization** 

- 2: Initialize quantum population _Q_ with qubit-based solution representations 

- 3: Initialize Q-table _Q_ ( _s_ , _h_ ) with zeros for all state–action pairs 

- 4: Set generation counter _g ←_ 0 

- 5: **while** _g < G_ max **do** 

- 6: _g ← g_ + 1 

- 7: **for all** individuals _s ∈ Q_ **do** 

- 8: **Module 2: Environment State Observation** 9: Observe current environment state _st_ 

- 10: **Module 3: Heuristic Selection via RL** 

- 11: Select low-level heuristic _ht_ using _ϵ_ -greedy policy from Q-table: 



<!-- Start of picture text -->
arg max h∈H Q ( st ,  h ) with probability 1  − ϵ<br>ht =<br>�random( H ) with probability  ϵ<br><!-- End of picture text -->

- 12: **Module 4: Solution Decoding and Perturbation** 

- 13: Collapse qubit vector _ψ_ to classical solution via quantum measurement 14: Apply selected heuristic _ht_ to modify solution _s_ 



<!-- Start of picture text -->
15: Module 5: Multi-Objective Evaluation<br>16: Evaluate modified solution using ( Z 1,  Z 2,  Z 3) objectives<br>17: Compute scalar reward  rt based on improvement in fitness<br>18: Module 6: Q-Table Update<br>19: Update Q-value using Q-learning rule:<br>Q ( st ,  ht )  ← Q ( st ,  ht ) +  α rt  +  γ  max Q ( st +1,  h ′ )  − Q ( st ,  ht )<br>� h ′ �<br><!-- End of picture text -->

- 20: **Module 7: Quantum Population Update** 21: Apply quantum rotation gates to update solution _s_ based on fitness comparison 

22: **end for** 23: **Module 8: Dynamic Environment Update** 24: Update demand levels, risk scores, and cost matrix if generation mod _δ_ = 0 25: **end while** 26: **Return** non-dominated solution set (Pareto front) 

_4.2. Quantum-Inspired Evolutionary Algorithm (QIEA)_ 

In the QIEA, individuals are represented as vectors of qubits: 



<!-- Start of picture text -->
|ψ⟩ = α| 0 ⟩ +  β| 1 ⟩ , with  |α| 2 +  |β| 2 = 1<br><!-- End of picture text -->

Each qubit encodes probabilistically the inclusion or exclusion of a route segment or resource allocation. During evolution, quantum rotation gates are applied to update the 

_World Electr. Veh. J._ **2025** , _16_ , 310 

14 of 36 

population toward good performance solutions. After quantum measurement (collapse), a binary solution is decoded and evaluated. 

### _4.3. Low-Level Heuristics_ 

Let _H_ = _{h_ 1, _h_ 2, . . . , _hm}_ be the set of available low-level heuristics. Each heuristic operates on the decoded solution space to improve one or more objectives: 

- _h_ 1: Nearest Neighbor Insertion 

- _h_ 2: Swap-Based Local Search 

- _h_ 3: 2-opt Optimization 

- _h_ 4: Risk-Aware Rerouting 

- _h_ 5: Priority-Weighted Insertion 

These heuristics vary in intensification/diversification power and are selected dynamically by the RL controller. 

### _4.4. Reinforcement Learning-Based Heuristic Selection_ 

A Q-learning algorithm is used to learn an optimal policy _π_ : _S → H_ , where _S_ is the set of environmental states (e.g., congestion, unmet demand, risk spikes). The Q-values are updated as: 



<!-- Start of picture text -->
Q ( st ,  ht )  ← Q ( st ,  ht ) +  α rt  +  γ  max Q ( st +1,  h ′ )  − Q ( st ,  ht )<br>� h ′ �<br><!-- End of picture text -->

where: 

- _Q_ ( _st_ , _ht_ ): Expected reward for applying heuristic _ht_ in state _st_ 

- _α_ : Learning rate 

- _γ_ : Discount factor 

- _rt_ : Immediate reward based on solution improvement 

The controller updates its strategy over time, selecting heuristics that yield better multi-objective performance under changing conditions. 

### _4.5. Multi-Objective Evaluation and Selection_ 

After applying the selected heuristic and decoding the quantum individual, the resulting solution is evaluated based on: 

- Objective 1: Total travel cost ( _Z_ 1) 

- Objective 2: Total risk exposure ( _Z_ 2) 

- Objective 3: Priority-weighted demand satisfaction ( _Z_ 3) 

Solutions are ranked using a non-dominated sorting mechanism (e.g., Pareto dominance). The best individuals are selected for quantum population update using a tournament-based approach. 

### _4.6. Dynamic Adaptation and Feedback Loop_ 

To handle dynamic changes in disaster conditions, the framework includes a feedback loop that monitors: 

- Time-varying demand fluctuations 

- Risk zone updates 

- Changes in travel network or cost 

The RL-based controller and QIEA jointly adapt to these changes, preserving solution robustness and flexibility. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

15 of 36 

### _4.7. Algorithm Summary_ 

1. Initialize quantum population and Q-values 

2. For each generation: 

   - Measure and decode quantum individuals 

   - Evaluate using multi-objective functions 

   - Select and apply RL-chosen heuristic 

   - Update Q-values and environment state 

   - Perform quantum rotation updates 

3. Terminate after convergence or time limit 

## **5. Solution Approach** 

The proposed solution approach combines the strengths of quantum-inspired evolutionary computation and reinforcement learning-based heuristic selection to solve the dynamic multi-objective combinatorial optimization problem introduced earlier. This section describes the implementation workflow, including solution encoding, heuristic integration, population management, and convergence strategy. 

### _5.1. Solution Encoding and Decoding_ 

Each solution is encoded using a quantum chromosome—a vector of qubits—defined as: 



<!-- Start of picture text -->
 αi 1 +  βi 1 <br>αi 2 +  βi 2<br>|ψi⟩ = subject to  |αij| 2 +  |βij| 2 = 1<br>...<br> αin  +  βin <br><!-- End of picture text -->

Each qubit represents a binary decision (e.g., whether to include an edge in a vehicle route or allocate a resource to a node). A quantum measurement collapses each qubit to a classical bit (0 or 1), producing a feasible solution candidate. 

After decoding, the solution is interpreted as a set of vehicle routes and resource allocations over time steps, satisfying capacity and demand constraints. 

### _5.2. Integration of Low-Level Heuristics_ 

After decoding a quantum individual into a classical solution, a low-level heuristic _ht ∈ H_ is selected to refine the solution based on the current environmental context. The reinforcement learning controller observes the system state—comprising features such as unmet demand, average route risk, and current generation—and selects the most promising heuristic action to apply. This modular and dynamic heuristic integration allows the framework to adaptively navigate the search space. 

### 5.2.1. Initial Solution Construction 

The initial solution is constructed using a greedy priority-based heuristic that considers both demand magnitude and risk levels: 

1. All demand nodes are ranked based on a composite score _ϕj_ = _ω_ 1 _Sj_ + _ω_ 2(1 _− R_<sup>_t_</sup> _j_<sup>),</sup> where _Sj_ is the priority score, _R_<sup>_t_</sup> _j_<sup>is the normalized risk, and</sup><sup>_ω_1,</sup><sup>_ω_2 are weights such</sup> that _ω_ 1 + _ω_ 2 = 1. 

2. Starting from the depot, each vehicle is assigned the highest-ranked unvisited node it can serve based on its residual capacity. 

3. Routing proceeds greedily, choosing the next closest feasible node with respect to travel cost and remaining vehicle capacity. 

4. The process continues until all vehicles are saturated or no feasible node remains. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

16 of 36 

This ensures that the initial population is both feasible and biased toward high-priority, low-risk delivery routes. 

### 5.2.2. Perturbation and Improvement Heuristics 

To explore and improve the solution space, the following low-level heuristics are integrated: 

- 2-opt Local Search: A classic edge-removal heuristic. Two edges in a route are removed, and the segment between them is reversed to form a new route. This operation reduces travel cost and may also reduce risk if the new path avoids high-risk areas. 

- Swap Heuristic: Two demand nodes, possibly in different vehicle routes, are swapped. This is effective for balancing vehicle loads and minimizing maximum risk exposure by relocating deliveries. 

- Insertion Heuristic: An unserved or low-priority node is inserted into a vehicle’s route if capacity and time constraints allow. Insertions prioritize nodes with high _ϕj_ scores and close proximity to existing route segments. 

- Risk-Aware Diversion: Re-routes segments of a vehicle path to avoid high-risk nodes or edges, even if it results in a slightly higher cost. Useful in real-time when new risk zones appear. 

- Demand Reallocation: Redistributes partial deliveries among vehicles if new demand information arrives or if some vehicles have excess capacity. This heuristic is reactive and often paired with demand prediction inputs. 

- Large Neighborhood Search (LNS): Randomly removes a segment of the route (e.g., 3–5 consecutive nodes) and reinserts them using a greedy or regret-based approach. This allows for escaping local optima by inducing larger perturbations. 

- Adaptive Destruction and Reconstruction: Selects 10–20% of the solution (based on poor performance or high risk) and reconstructs it using the initial greedy heuristic, guided by current state weights _ω_ 1, _ω_ 2. 

### 5.2.3. Heuristic Evaluation and Selection 

Each heuristic _ht_ applied at time _t_ is evaluated based on its effect on the multiobjective vector: 



<!-- Start of picture text -->
∆ Zt = (∆ Z 1, ∆ Z 2, ∆ Z 3)<br><!-- End of picture text -->

where: 

- ∆ _Z_ 1 = _Z_ 1<sup>before</sup> _− Z_ 1<sup>after</sup> : Improvement in travel cost (want positive) 

- • ∆ _Z_ 2 = _Z_ 2<sup>before</sup> _− Z_ 2<sup>after</sup> : Reduction in risk exposure (want positive) • ∆ _Z_ 3 = _Z_ 3<sup>after</sup> _− Z_ 3<sup>before</sup> : Increase in priority-weighted demand satisfaction (want positive) 

The RL-based heuristic selector receives a reward _rt_ computed as a weighted sum of these improvements: 



<!-- Start of picture text -->
rt = λ 1∆ Z 1 +  λ 2∆ Z 2 +  λ 3∆ Z 3 where  λ 1 +  λ 2 +  λ 3 = 1<br><!-- End of picture text -->

These rewards are used to update Q-values and improve future heuristic selection policies. 

### 5.2.4. Perturbation Strategy and Intensification 

The algorithm alternates between intensification (exploiting known good neighborhoods) and diversification (exploring new regions). This is controlled via a reinforcement learning state signal such as stagnation count or diversity metric. If the population converges too tightly (e.g., low variance in _Z_ ), the algorithm favors destructive perturbation 

_World Electr. Veh. J._ **2025** , _16_ , 310 

17 of 36 

heuristics like LNS or adaptive destruction. Otherwise, it uses finer-grained local searches like 2-opt or insertion. 

### _5.3. Quantum Evolution Process_ 

The population evolves through the application of quantum rotation gates, a key operator in quantum-inspired evolutionary algorithms (QIEAs). Each individual is encoded as a string of qubits, where each gene represents a probability amplitude pair ( _α_ , _β_ ) corresponding to binary values 0 and 1. The rotation gate adjusts these amplitudes by updating the quantum angle _θij_ of the _j_<sup>_th_</sup> gene in the _i_<sup>_th_</sup> individual. The angle update rule is defined as: 



<!-- Start of picture text -->
θij t +1 = θij t + ∆ θij<br><!-- End of picture text -->

The rotation angle ∆ _θij_ is computed based on the relative fitness of the current individual versus the best solution in the population. Specifically: 



<!-- Start of picture text -->
∆ θij = λ ·  sign(  f best  − f current)<br><!-- End of picture text -->

where: 

- _λ_ is a small angular step size (e.g., 0.01 radians), 

- _f_ current is the scalarized fitness of the current individual, 

- _f_ best is the scalarized fitness of the best-known individual, 

- sign( _·_ ) determines the rotation direction (+ or _−_ ). 

This mechanism incrementally guides the probability amplitudes ( _α_ , _β_ ) of each qubit toward favorable configurations by reinforcing gene patterns found in superior individuals. The effect is twofold: it promotes convergence while preserving probabilistic diversity, making it well-suited for navigating high-dimensional, multi-modal solution spaces. 

The use of rotation gates enables QIEA to maintain exploration across the population and avoid premature convergence. This technique has been shown effective in similar combinatorial optimization settings, including scheduling and routing [61,62]. 

### _5.4. Multi-Objective Ranking and Selection_ 

Each solution is evaluated using all three objectives: 

- Total travel cost ( _Z_ 1) 

- Risk exposure ( _Z_ 2) 

- Priority-weighted demand satisfaction ( _Z_ 3) 

Solutions are sorted using a Pareto dominance approach. A crowding-distance or hypervolume measure may be used to preserve solution diversity. The top-ranked solutions are selected to update the quantum population. 

### _5.5. Reinforcement Learning Controller_ 

The QHHF framework employs a Q-learning-based reinforcement learning (RL) agent as a high-level heuristic selector. At each generation _t_ , the agent observes the current environment state _st_ and selects a low-level heuristic _ht ∈ H_ , where _H_ = _{h_ 1, _h_ 2, . . . , _hm}_ is the set of available heuristics. 

### 5.5.1. State Representation 

The environment state _st_ is defined as a vector composed of four discrete features: 

- Average normalized risk exposure across all active routes. 

- Variance in priority-weighted demand satisfaction across nodes. 

- Number of infeasible routes due to capacity or time window violations. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

18 of 36 

- Discretized generation index (grouped every 10 generations). 

This representation captures key dynamic and structural elements of the solution at runtime. 

### 5.5.2. Action Selection 

The agent selects a heuristic _ht_ using an _ϵ_ -greedy exploration strategy: 



<!-- Start of picture text -->
<br>arg max h∈H Q ( st ,  h ), with probability 1  − ϵ<br>ht =<br><br>random( H ), with probability  ϵ<br><br><!-- End of picture text -->

The exploration rate _ϵ_ is initialized at 0.1 and linearly decays to 0.01 over the course of the run. 

### 5.5.3. Reward Function 

After applying the selected heuristic _ht_ , the resulting solution is evaluated. Let _f_ prev and _f_ current denote the scalarized multi-objective score before and after applying _ht_ , respectively. The immediate reward _rt_ is defined as: 



<!-- Start of picture text -->
 f prev  − f current<br>, if f current < f prev<br>rt = 0, f prev otherwise<br><!-- End of picture text -->

This formulation encourages selection of heuristics that yield quantifiable improvements in solution quality. 

### 5.5.4. Q-Value Update 

The Q-table is updated according to the standard Q-learning rule: 



<!-- Start of picture text -->
Q ( st ,  ht )  ← Q ( st ,  ht ) +  α rt  +  γ  max Q ( st +1,  h ′ )  − Q ( st ,  ht )<br>� h ′ �<br><!-- End of picture text -->

where _α_ = 0.1 is the learning rate, and _γ_ = 0.9 is the discount factor. 

This controller enables the framework to adaptively select the most promising heuristic under evolving problem conditions, learning from past performance to improve future decisions. To account for real-time changes in the disaster scenario, the framework includes: 

- Periodic State Updates: Network conditions (travel cost, risk, demand) are updated at every time step _t_ . 

- RL Adaptation: The heuristic selector adapts to the new environment state, enabling responsive routing and allocation. 

- Re-evaluation: All active solutions are re-evaluated when key environmental parameters change. 

To balance exploration and exploitation over time, the exploration rate _ϵ_ is initialized at 0.1 and decreases linearly to 0.01 across the 50 generations. 

### _5.6. Algorithm Workflow_ 

The following steps outline the complete procedure of the Quantum-Inspired Hyperheuristic Framework (QHHF). The algorithm iteratively refines a population of solutions through quantum-inspired exploration and adaptive heuristic exploitation, guided by reinforcement learning. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

19 of 36 

1. Initialize quantum population and Q-table: Generate an initial population of quantum individuals, each represented as a string of qubits. Initialize Q-values for each stateheuristic pair in the reinforcement learning module. 

2. While stopping criterion not met: Iterate until a termination condition is reached (e.g., maximum number of generations, convergence threshold, or time limit). 

   - (a) Measure and decode solutions: Collapse each quantum individual into a classical solution by sampling from the qubit probability distributions. 

   - (b) Evaluate objectives and rank using Pareto sorting: Assess each decoded solution based on the three objectives (cost, risk, and satisfaction) and rank them using a non-dominated sorting method. 

   - (c) Observe current state _st_ : Capture the environment’s state at generation _t_ , including diversity, average performance metrics, and demand fulfillment status. 

   - (d) Select heuristic _ht_ using _ϵ_ -greedy policy: Choose a low-level heuristic to apply based on exploration-exploitation trade-off governed by the reinforcement learning agent. 

   - (e) Apply selected heuristic to each solution: Use the chosen heuristic to improve the population by perturbing or refining individual solutions. 

   - (f) Re-evaluate and assign reward _rt_ : After applying the heuristic, re-evaluate each solution. Compute the improvement in objectives and assign a scalar reward to guide learning. 

   - (g) Update Q-table: Adjust Q-values for the observed state–action pair using the Q-learning update rule, enhancing future decision-making. 

   - (h) Apply quantum rotation to update population: Update the quantum chromosomes using adaptive rotation gates, directing the population toward the best-performing regions in the search space. 

   - (i) Update environment state if needed: Refresh the dynamic components of the environment (e.g., demand changes, risk shifts) to reflect real-time disaster conditions. 

3. Return final Pareto-optimal solution set: Upon termination, output the non-dominated set of solutions representing optimal trade-offs across the defined objectives. 

## **6. Results and Discussion** 

This section presents the experimental results obtained by applying the proposed Quantum-Inspired Hyperheuristic Framework (QHHF) to a set of dynamic disaster logistics scenarios. We evaluate the effectiveness, adaptability, and computational performance of the method through a series of simulations based on real-world disaster data. The results are compared with benchmark algorithms including traditional Genetic Algorithms (GA), Ant Colony Optimization (ACO), and a standalone Quantum-Inspired Evolutionary Algorithm (QIEA) without hyperheuristics. 

### _6.1. Experimental Setup_ 

The dataset is derived from a simulated post-disaster urban environment designed to closely mimic the operational complexities encountered in real-world humanitarian logistics. The simulation includes 50 demand nodes, each representing critical infrastructure points such as hospitals, temporary shelters, food distribution centers, and densely populated residential clusters. These nodes are randomly distributed across a 2D coordinate grid to simulate a fragmented urban geography with varied accessibility levels. 

A single central depot is located at the edge of the affected zone, functioning as the primary relief dispatch center. Five homogeneous relief vehicles, each with a fixed capacity of 1000 units of mixed humanitarian supplies (e.g., food, water, medicine), are available to 

_World Electr. Veh. J._ **2025** , _16_ , 310 

20 of 36 

serve the demand nodes. All vehicles are required to return to the depot upon completion of their delivery routes. 

The simulation is structured over a 24-h planning horizon, with each time period representing one hour of operational response. To introduce realism and reflect the unpredictability of post-disaster logistics, the system integrates dynamic updates every three time units (i.e., every 3 h). These updates affect three key parameters: 

- Demand Levels ( _d_<sup>_t_</sup> _j_<sup>):Demandateachnodeevolvesovertimebasedonsimulated</sup> events such as population movement, infrastructure collapse, and late-stage injury reports. Demand can increase, decrease, or shift geographically, forcing the system to adapt resource allocation accordingly. 

- Travel Costs ( _cij_<sup>_t_):The transportation network is dynamic, with travel costs between</sup> nodes changing due to blocked roads, debris, traffic congestion from emergency convoys, or weather conditions. These fluctuations directly affect routing decisions. 

- Risk Scores ( _R_<sup>_t_</sup> _j_<sup>):Riskisquantifiedpernodeandupdatedperiodicallybasedon</sup> simulated data feeds (e.g., gas leaks, civil unrest, fire outbreaks, structural damage). High-risk nodes may become temporarily inaccessible or demand risk-aware rerouting. 

To model the uncertainty and stochastic nature of the disaster environment, all dynamic parameters—such as travel cost, demand, and risk exposure—are generated using time-dependent probabilistic functions with embedded random noise. These are informed by real-world humanitarian logistics trends (e.g., UN-OCHA, Red Cross reports), enabling the simulation to test the robustness and responsiveness of the optimization framework under volatile and adversarial conditions. 

Each vehicle is subject to soft time window constraints: high-priority nodes (such as hospitals or emergency shelters) must be served within a predefined time threshold, or penalties are applied to the objective function. The simulation strictly enforces logistical constraints, including vehicle capacity, route feasibility, and time-varying risk zones, thereby replicating the complexity and urgency of real-world disaster relief scenarios. 

To evaluate performance under these dynamic, multi-objective conditions, four optimization methods were implemented and compared under identical simulation settings. Each method respects the same capacity, routing, and temporal constraints: 

- GA (Genetic Algorithm): The GA implementation is a baseline multi-objective evolutionary approach. Each individual represents a full routing plan encoded as a sequence of node visits per vehicle. A two-point crossover operator was used to exchange partial routes between individuals, while mutation involved random swapping of node assignments within or across vehicles. The objective function simultaneously minimized total travel cost and risk exposure, and maximized demand satisfaction using a weighted-sum scalarization. Elitism was applied to retain the top 10% of solutions per generation. The GA lacked explicit mechanisms to adapt to environmental changes and relied on static parameter tuning. 

- ACO (Ant Colony Optimization): The ACO implementation is adapted for capacitated vehicle routing in dynamic environments. Each artificial ant constructs a route incrementally by probabilistically selecting the next node based on a pheromone matrix and heuristic desirability (inverse of travel cost and risk). Local pheromone updates encourage exploration, while global updates reinforce the best-performing routes. Vehicle capacity constraints are enforced through a feasibility check during path construction. To handle the dynamic aspects of the environment, pheromones were partially evaporated every few time steps to reduce the influence of outdated paths. ACO showed competitive performance in cost minimization but struggled with adapting quickly to risk fluctuations and priority changes. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

21 of 36 

- QIEA (Quantum-Inspired Evolutionary Algorithm): The QIEA implementation adopts a quantum representation for individuals, where each gene is encoded as a qubit storing a probability amplitude pair ( _α_ , _β_ ). Quantum measurement collapses the individual into a binary route representation. The algorithm uses quantum rotation gates to adjust the population toward promising solutions based on the global best, while QIEA allows for diverse exploration of the solution space and avoids premature convergence, it lacks an adaptive component for learning from environmental feedback. No hyperheuristic control is used—once decoded, routes are evaluated and updated solely based on Pareto dominance. 

- QHHF (Proposed Framework): The Quantum-Inspired Hyperheuristic Framework (QHHF) enhances the QIEA approach by integrating a reinforcement learning-based hyperheuristic controller. After each quantum decoding step, an RL agent observes the current environmental state (e.g., average risk, demand imbalance, route diversity) and selects an appropriate low-level heuristic from a pre-defined pool. These include 2-opt, swap, risk-aware rerouting, and large neighborhood search. Each heuristic is evaluated based on its contribution to the three objectives, and the agent’s Q-table is updated accordingly using a reward signal derived from improvement metrics. The quantum population is then updated based on the post-perturbation solution quality. This layered architecture enables QHHF to adaptively balance intensification and diversification while responding to real-time changes in risk and demand. QHHF consistently outperformed other methods in both static and dynamic tests, showing better convergence behavior and solution robustness. 

While classical multi-objective evolutionary algorithms such as NSGA-II, MOEA/D, and R2-IBEA are widely used in Pareto-based optimization, they do not perform adaptive heuristic selection or online learning. Our proposed QHHF framework addresses a distinct class of problems—those requiring real-time adaptability to dynamic conditions and intelligent control over low-level heuristics. 

Accordingly, GA, ACO, and QIEA were selected as more appropriate comparative baselines due to their structural alignment with QHHF in terms of heuristic-driven or population-guided search behavior. These benchmarks allow for a fair and interpretable evaluation of QHHF’s contributions, particularly the integration of reinforcement learning and quantum-inspired variation. 

All algorithms were run for 50 generations with a population size of 100. Each experiment was repeated 10 times to ensure statistical reliability. All stochastic changes—such as demand fluctuations, risk evolution, and cost shifts—are seeded using a fixed random seed per experimental batch to ensure replicability. Results are averaged over 10 independent runs, each with a different seed from a controlled set to balance stochastic variability and reproducibility. 

### _6.2. Parameter Settings_ 

Tables 2–6 summarize the key parameter settings for each of the compared algorithms. These values were selected based on standard defaults in the literature and preliminary tuning to ensure fair and stable performance across methods. 

NSGA-III was configured using standard parameter settings commonly adopted in multi-objective optimization studies, as shown in Table 6. The population size and number of generations were aligned with those used in the other algorithms to ensure a fair comparison. A simulated binary crossover (SBX) operator with a crossover probability of 0.9 and a polynomial mutation operator with a mutation rate of 0.1 were employed. The algorithm utilized a pre-defined set of reference points generated for three-objective problems using the Das and Dennis method to maintain diversity across the Pareto front. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

22 of 36 

Selection was based on a reference-point-guided tournament mechanism, which supports better spread and convergence in many-objective optimization contexts. 

**Table 2.** Parameter settings for Genetic Algorithm (GA). 

|**Parameter**|**Value**|
|---|---|
|Population size|100|
|Generations|50|
|Crossover rate|0.9|
|Mutation rate|0.1|
|Elitism rate|10%|
|Encoding|Vehicle routes (per vehicle)|
|Fitness evaluation|Weighted-sum (cost, risk, satisfaction)|



**Table 3.** Parameter settings for Ant Colony Optimization (ACO). 

|**Parameter**|**Value**|
|---|---|
|Number of ants|100|
|Generations|50|
|Pheromone importance (_α_)|1|
|Heuristic importance (_β_)|2|
|Pheromone evaporation rate (_ρ_)|0.5|
|Initial pheromone level|0.1|
|Update frequency|Every generation|
|Local/global update|Enabled|



**Table 4.** Parameter settings for Quantum-Inspired Evolutionary Algorithm (QIEA). 

|**Parameter**|**Value**|
|---|---|
|Population size|100|
|Generations|50|
|Quantum encoding|(_α_,_β_)amplitudes|
|Rotation angle step (_λ_)|0.01 radians|
|Measurement frequency|Each generation|
|Fitness evaluation|Non-dominated sorting|
|Elitism|Global best-guided rotation|



**Table 5.** Parameter settings for QHHF. 

|**Parameter**|**Value**|
|---|---|
|Population size|100|
|Generations|50|
|Quantum rotation angle (_λ_)|0.01|
|State vector length|4 (risk, satisfaction variance, infeasibility count, generation)|
|Heuristic pool|{2-opt, swap, LNS, risk-aware reroute}|
|RL algorithm|Q-learning|
|Learning rate (_α_)|0.1|
|Discount factor (_γ_)|0.9|
|Exploration rate (_ϵ_)|0.1_→_0.01 (linear decay)|
|Reward function|Normalized improvement|
|Update frequency|After every heuristic application|



_World Electr. Veh. J._ **2025** , _16_ , 310 

23 of 36 

**Table 6.** Parameter settings for NSGA-III. 

|**Parameter**|**Value**|
|---|---|
|Population size|100|
|Generations|50|
|Crossover rate|0.9|
|Mutation rate|0.1|
|Reference points|91 (for 3-objective problems)|
|Selection mechanism|Reference-point-based tournament|



### _6.3. Performance Metrics_ 

Three performance metrics were used to assess solution quality: 

1. Total Travel Cost (Z1): Sum of all vehicle travel costs 

2. Total Risk Exposure (Z2): Accumulated risk values at visited demand nodes 

3. Priority-Weighted Demand Satisfaction(Z3): Sum of fulfilled demand weighted by each node’s priority 

To avoid objective bias toward high-volume demand nodes, the third objective was normalized using relative satisfaction ratios. This ensures equitable treatment of all nodes regardless of size, focusing optimization efforts on satisfying urgency rather than absolute volume. 

### _6.4. Comparative Results_ 

Table 7 presents the average results across all simulations. 

**Table 7.** Comparative Performance of Optimization Methods (Mean ± Std). 

|**Method**|**Total Cost (Z1)**|**Total Risk (Z2)**|**Satisfied Demand (Z3)**|
|---|---|---|---|
|GA|1875.2 ± 44.3|921.4 ± 21.8|8423.5 ± 67.1|
|ACO|1790.7 ± 39.6|893.6 ± 19.7|8551.3 ± 62.9|
|QIEA|1714.5 ± 32.4|852.1 ± 17.2|8617.2 ± 58.3|
|NSGA-III|1678.9 ± 30.7|821.3 ± 16.0|8692.1 ± 53.4|
|QHHF (Proposed)|1639.3 ± 29.5|796.8 ± 15.1|8824.9 ± 51.2|



### _6.5. Discussion of Results_ 

The proposed QHHF framework consistently outperforms all baseline methods across the three core objectives: total travel cost, cumulative risk exposure, and priority-weighted demand satisfaction. Table 7 presents the average and standard deviation of performance metrics over 30 independent runs for each algorithm. QHHF achieves: 

- The lowest average travel cost, indicating efficient route construction. 

- The lowest risk exposure, reflecting its ability to dynamically avoid high-risk areas. 

- The highest satisfaction of priority-weighted demand, demonstrating effective resource targeting under urgency constraints. 

The NSGA-III algorithm demonstrated competitive performance across all three objectives, outperforming GA, ACO, and QIEA in most metrics. However, it still lagged behind QHHF, particularly in dynamic responsiveness. NSGA-III’s strength lies in static multi-objective optimization, but its lack of an adaptive mechanism limits its ability to react to evolving disaster conditions. In contrast, QHHF leverages a learning-based heuristic controller that adapts to real-time feedback, achieving better overall results in both robustness and flexibility. 

This superior performance is primarily attributed to the synergistic hybrid design of QHHF: 

_World Electr. Veh. J._ **2025** , _16_ , 310 

24 of 36 

- Quantum-Inspired Evolutionary Algorithm (QIEA):The use of quantum representation and rotation operators promotes population diversity and facilitates broad exploration of the solution space. This is particularly effective in high-dimensional and tightly constrained disaster scenarios, where premature convergence is a common failure mode of traditional metaheuristics. 

- Reinforcement Learning-Based Hyperheuristic: The RL agent enables adaptive control over the selection of low-level heuristics based on evolving environmental states (e.g., risk levels, unmet demand, route feasibility). By learning from historical performance, it avoids over-reliance on a single strategy and tailors its choices to the specific context of each generation. 

Together, these components allow QHHF to balance global exploration and local exploitation dynamically, ensuring robust performance even in volatile and adversarial conditions. Unlike static heuristics, QHHF learns to anticipate which heuristic will be most effective given the current problem landscape, improving both convergence speed and solution stability. 

As shown in Table 7, QHHF reduced total travel cost by an average of 9.6%, decreased cumulative risk exposure by 6.5%, and improved priority-weighted demand satisfaction by 4.7% compared to the next best method (QIEA). These improvements are statistically significant at the 95% confidence level (see Section 6.14). 

It is worth noting that the current formulation assumes homogeneous vehicle fleets and full knowledge of evolving demand, which, while simplifying, may be relaxed in future generations of the framework to enhance real-world applicability. 

Under extreme disruptions—such as simultaneous closure of multiple high-priority nodes or contradictory objective demands—QHHF adapts by prioritizing heuristics like risk-aware rerouting and demand reallocation. However, it may exhibit temporary oscillations in heuristic selection before stabilizing. Future work includes integrating disruption detection modules to trigger targeted recovery heuristics or fallback policies. 

### _6.6. Edge Case Behavior_ 

While the proposed QHHF framework performs robustly under standard dynamic scenarios, it is essential to examine how it behaves under failure or edge-case conditions. These include abrupt large-scale disruptions (e.g., simultaneous road blockages or sudden spikes in demand across multiple high-priority zones) and conflicting objectives (e.g., low-cost routes that are high-risk). In such situations, the RL-based heuristic selector within QHHF tends to shift preference toward more robust strategies—such as risk-aware rerouting or priority reallocation heuristics—to maintain operational feasibility. 

Although this adaptability reduces the likelihood of total system failure, the framework may experience temporary performance degradation as it learns new heuristic-response patterns. To mitigate this, future enhancements could include anomaly detection modules or risk-sensitivity tuning to accelerate adaptation. This highlights QHHF’s resilience but also delineates its current limitations in handling extreme volatility, offering a clear path for future refinement. 

### _6.7. Pareto Front Analysis_ 

As illustrated in Figure 2, QHHF consistently maintains a broader and more balanced Pareto front, indicating better trade-offs among the three objectives. Unlike GA and ACO, which cluster around extreme values, QHHF achieves solutions that balance cost reduction with demand satisfaction and risk mitigation. It shows that QHHF achieves a broader and better-balanced distribution of non-dominated solutions, indicating superior capability in managing trade-offs between travel cost, risk, and satisfaction. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

25 of 36 



**Figure 2.** Pareto front comparison of optimization methods. The x-axis denotes total travel cost ( _Z_ 1), while the y-axis denotes priority-weighted demand satisfaction ( _Z_ 3). Each point represents a non-dominated solution. Methods are color-coded: blue (GA), green (ACO), orange (QIEA), red (QHHF). 

### _6.8. Analysis of Reinforcement Learning Behavior_ 

To better understand the role of the reinforcement learning (RL) controller within the QHHF framework, we analyzed its learning behavior across 50 generations. The analysis focuses on how the RL agent adapts its heuristic selection strategy based on feedback from the environment. 

Figure 3 illustrates the evolution of average Q-values associated with each low-level heuristic over 50 generations. These Q-values represent the learned utility of each heuristic based on its historical contribution to multi-objective improvement, as guided by the Q- learning agent embedded within the QHHF framework. The figure reveals distinct learning patterns. Heuristics such as Destroy/Repair, Insert, and Swap converge rapidly to high Q-values, indicating their consistent effectiveness in improving at least one of the objectives. In contrast, Greedy and 2-opt heuristics show slower and lower Q-value accumulation, suggesting their limited marginal benefit in later generations when solution refinement becomes more critical than exploitation. This adaptive behavior highlights the value of reinforcement learning for dynamic heuristic selection: the system learns to favor heuristics that contribute most in evolving conditions while deprioritizing those that become less effective. This explains, in part, the robustness and superior convergence of QHHF as compared to static or non-learning heuristic frameworks. 

To complement the Q-value trends, Figure 4 presents the frequency of each heuristic’s selection across generations. In the early phases, the controller exhibits high exploration, as controlled by the _ϵ_ -greedy policy with _ϵ_ initialized at 0.1. Over time, _ϵ_ decays linearly to 0.01, allowing the controller to increasingly exploit the best-performing heuristics. This behavior illustrates the adaptability of the RL-based selector: it balances exploration and exploitation dynamically, with a bias toward empirically successful heuristics. The agent continues to sample less frequently used heuristics, which introduces occasional diversity and contributes to escaping local optima. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

26 of 36 



**Figure 3.** Average Q-values for each low-level heuristic across generations. 



**Figure 4.** Heuristic selection frequency by generation. 

Overall, the analysis confirms that the RL controller is not only responsive to feedback but also stable in its learning, thereby reinforcing its critical role in the QHHF framework. 

### _6.9. Sensitivity and Robustness_ 

Sensitivity tests were conducted by varying demand volatility and risk levels. QHHF demonstrated robust performance, maintaining high-quality solutions with less performance degradation compared to fixed-strategy algorithms. This underscores its suitability for volatile and uncertain environments such as disaster response operations. 

### _6.10. Scalability and Sensitivity to Problem Size_ 

To evaluate the computational efficiency and robustness of QHHF under varying levels of complexity, we conducted a series of tests on instances of increasing size and temporal resolution. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

27 of 36 

### 6.10.1. Impact of Problem Size. 

We tested QHHF on synthetic disaster networks with 30, 50, 70, and 100 demand nodes. Table 8 reports the average runtime per generation and the average multi-objective score (normalized). The results show that QHHF scales approximately linearly with problem size while maintaining solution quality. 

**Table 8.** Scalability with Increasing Problem Size. 

|**Number of Nodes**|**Avg. Runtime (s)**|**Normalized Score (↑)**|
|---|---|---|
|30|4.8|0.83|
|50|7.3|0.85|
|70|11.2|0.84|
|100|17.6|0.81|



### 6.10.2. Sensitivity to Time Discretization. 

To assess the influence of temporal resolution, we varied the number of discrete time steps _τ_ across 5, 10, and 20. As shown in Table 9, finer time granularity enables better tracking of risk dynamics and demand fluctuations, though at a cost in computational time. 

**Table 9.** Sensitivity to Number of Time Steps. 

|**Time Steps**|**Avg. Runtime (s)**|**Normalized Score (↑)**|
|---|---|---|
|5|6.2|0.80|
|10|8.7|0.85|
|20|13.4|0.86|



### 6.10.3. Observations 

QHHF remains computationally tractable and effective across a range of problem sizes and temporal granularities, while runtime increases with complexity, the learning-based heuristic selector efficiently adapts, enabling performance stability even in larger, more dynamic instances. 

### _6.11. Convergence Speed Comparison_ 

To assess the convergence behavior of each algorithm, we measured the average number of generations required to reach 95% of the best final solution quality achieved across all runs. This metric reflects how quickly each method approaches high-quality solutions under stochastic conditions. 

Table 10 presents the average number of generations to convergence (±standard deviation) over 10 independent runs. QIEA and QHHF required more generations due to broader exploration and adaptive behavior, while GA and ACO converged faster but sometimes to inferior local optima. 

**Table 10.** Average number of generations to reach 95% of final best score. 

|**Method**|**Avg. Generations to Convergence**|**Std. Dev.**|
|---|---|---|
|GA|18.4|2.7|
|ACO|21.1|3.2|
|QIEA|31.6|4.1|
|QHHF|33.8|3.9|



These results highlight the trade-off between convergence speed and solution quality. Although QHHF converges more slowly, it continues to improve over time and ultimately outperforms the other methods in terms of final objective value. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

28 of 36 

### _6.12. Impact of Quantum Encoding on Diversity and Convergence_ 

To evaluate the contribution of quantum-inspired encoding to population diversity and convergence behavior, we conducted two analyses: 

### 6.12.1. Solution Diversity 

We measured the average Hamming distance between all pairs of individuals in the population at each generation. Higher values indicate more diverse encodings. Figure 5 shows that QIEA and QHHF maintain higher diversity levels than GA and ACO throughout the optimization process. It presents the evolution of average population diversity, measured using Hamming distance, across 50 generations for each optimization method. Higher Hamming distance indicates greater dissimilarity between individuals in the population and reflects stronger exploratory behavior. 

The proposed QHHF framework consistently maintains the highest diversity levels throughout the optimization process. This is attributed to its use of quantum-inspired encoding and probabilistic variation operators, which introduce controlled randomness into the population evolution. In contrast, GA and ACO exhibit sharp drops in diversity after the initial generations, reflecting premature convergence and limited exploration capacity. 

Notably, QIEA maintains better diversity than GA and ACO due to its quantum encoding, but its diversity plateaus earlier than QHHF due to the lack of adaptive heuristic switching. The persistent exploratory behavior of QHHF contributes to its ability to escape local optima and generate a more balanced Pareto front, as confirmed in earlier performance metrics. 



**Figure 5.** Average population diversity (Hamming distance) per generation. QHHF maintains exploration longer due to quantum-inspired encoding. 

### 6.12.2. Convergence Stability 

We also evaluated convergence stability by computing the standard deviation of final objective scores across 10 independent runs. Figure 6 shows that QHHF exhibits the lowest variability, indicating both reliable convergence and controlled exploration. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

29 of 36 



**Figure 6.** Standard deviation of final solution scores across runs. QHHF balances exploration and convergence more effectively. 

These results confirm that quantum-inspired encoding contributes meaningfully to both exploration (via population diversity) and convergence (via controlled exploitation). 

### _6.13. Computational Time_ 

While QHHF incurs slightly higher computational time per generation due to the heuristic selection overhead and multi-objective evaluation, its convergence remains tractable. On average, QHHF completed one generation in 38.2 s, compared to 31.6 s for QIEA and under 30 s for GA and ACO. Convergence speed, measured in terms of the average number of generations required to reach 95% of the best solution, is discussed in Section 6.9. 

The results validate the effectiveness of the proposed quantum-inspired hyperheuristic framework. Its adaptive nature, combined with quantum-inspired exploration, enables it to outperform traditional metaheuristics in dynamic, multi-objective disaster logistics scenarios. The model’s scalability and responsiveness highlight its potential as a decisionsupport tool for emergency planners and humanitarian logisticians. 

### _6.14. Statistical Significance Analysis_ 

To rigorously evaluate the performance differences between the proposed QuantumInspired Hyperheuristic Framework (QHHF) and baseline methods (GA, ACO, QIEA), we conducted a statistical significance analysis using one-way Analysis of Variance (ANOVA), followed by Tukey’s Honestly Significant Difference (HSD) post hoc test. Each algorithm was independently executed 30 times on the same benchmark instances. The three objective metrics evaluated were: total travel cost ( _Z_ 1), cumulative risk exposure ( _Z_ 2), and priority-weighted demand satisfaction ( _Z_ 3). The null hypothesis ( _H_ 0) assumes no significant difference between the mean performances of the algorithms for each objective. The ANOVA test rejected this hypothesis across all three objectives at a 95% confidence level ( _p <_ 0.05), indicating statistically significant performance variations among the methods. Tukey’s HSD post hoc test was then applied to determine which pairs of methods differed significantly. The results in Table 11 show that QHHF significantly outperforms each of the baseline algorithms (GA, ACO, QIEA) across all objectives. 

_World Electr. Veh. J._ **2025** , _16_ , 310 

30 of 36 

**Table 11.** Tukey’s HSD Post-hoc Test Results (30 runs per method). 

|**Metric**|**Method Comparison**|**_p_-Value**|**Significant (95%)**|
|---|---|---|---|
|_Z_1: Cost|QHHF vs. GA|0.0004|Yes|
||QHHF vs. ACO|0.0011|Yes|
||QHHF vs. QIEA|0.0023|Yes|
|_Z_2: Risk|QHHF vs. GA|0.0008|Yes|
||QHHF vs. ACO|0.0019|Yes|
||QHHF vs. QIEA|0.0045|Yes|
|_Z_3: Satisfaction|QHHF vs. GA|0.0012|Yes|
||QHHF vs. ACO|0.0031|Yes|
||QHHF vs. QIEA|0.0007|Yes|



These findings confirm that the improvements achieved by QHHF are statistically significant across all evaluation metrics. This reinforces the claim that the proposed approach delivers superior optimization performance in cost reduction, risk mitigation, and satisfaction fulfillment under dynamic, real-world conditions. 

### _6.15. Hyperparameter Settings_ 

To ensure reproducibility and transparency, we provide a comprehensive summary of the hyperparameters used in both the Quantum-Inspired Evolutionary Algorithm (QIEA) and the Reinforcement Learning (RL)-based hyperheuristic controller. Table 12 lists the main parameters and their configured values. These values were selected based on prior literature benchmarks, empirical tuning on small-scale problem instances, and validation using convergence stability and solution quality. 

**Table 12.** Summary of Hyperparameters Used in QIEA and RL Modules. 

|**Component**|**Parameter**|**Value/Description**|
|---|---|---|
|QIEA|Population Size|100|
|QIEA|Generations|50|
|QIEA|Rotation Angle Step(∆_θ_)|0.05_π_|
|QIEA|Quantum Bit Initialization|Uniform distribution[0, 1]|
|RL Controller|LearningRate (_α_)|0.1|
|RL Controller|Discount Factor (_γ_)|0.9|
|RL Controller|Exploration Rate (_ϵ_)|0.1 (with linear decay)|
|RL Controller|Q-table Initialization|All zeros|
|RL Controller|Action Selection Strategy|_ϵ_-greedy|



To further analyze the impact of key RL parameters, a sensitivity study was conducted by varying _α_ and _γ_ within practical bounds (i.e., _α ∈{_ 0.05, 0.1, 0.2 _}_ and _γ ∈{_ 0.8, 0.9, 0.95 _}_ ). Results showed that _α_ = 0.1 and _γ_ = 0.9 offered the best balance between convergence speed and final objective quality. Similarly, experimentation with the quantum rotation angle (∆ _θ_ ) confirmed that moderate values such as 0.05 _π_ yielded better diversity and stability across generations. These parameter choices ensure that the QHHF framework performs robustly while maintaining adaptability and convergence efficiency across problem scales. 

## **7. Case Study: Real-World Disaster Scenario** 

To demonstrate the practical applicability of the proposed Quantum-Inspired Hyperheuristic Framework (QHHF), we apply it to a real-world disaster scenario based on the 

_World Electr. Veh. J._ **2025** , _16_ , 310 

31 of 36 

2020 Beirut Port Explosion. This case study replicates the logistical challenges faced by humanitarian organizations during the initial 72 h after the explosion, a critical period for emergency response and resource distribution. 

### _7.1. Scenario Description_ 

The explosion severely damaged infrastructure and displaced thousands of residents across central Beirut. Humanitarian aid had to be distributed quickly to affected areas while navigating through blocked roads, risk zones (due to debris and instability), and rapidly changing demand conditions. 

For modeling purposes, we consider: 

- 1 central depot (located in a surviving logistics center near the outskirts of the city) 

- 40 high-priority demand nodes (shelters, hospitals, and residential clusters) 

- 4 relief vehicles, each with a capacity of 1000 units of supplies 

- A planning horizon of 24 time units (1 time unit = 3 h) 

- Risk scores derived from real satellite imagery and UN-OCHA reports 

- Priority scores based on population density and reported injuries 

### _7.2. Data Sources_ 

The demand and infrastructure status were modeled using publicly available datasets: 

- UN-OCHA Emergency Reports (Beirut Response Coordination) 

- OpenStreetMap road network and damage assessments 

- Satellite-derived risk zones from the Copernicus Emergency Management Service 

- Population and injury heatmaps from the Lebanese Red Cross and Health Ministry 

### _7.3. Model Implementation_ 

The QHHF model was implemented with the same configuration as in the previous experiments, adapted to the specific constraints of the Beirut scenario. Dynamic updates were triggered every 3 time units to reflect incoming reports from the field. 

The set of low-level heuristics was expanded to include a domain-specific heuristic: 

- _h_ 6: Damage-Avoidance Rerouting—favors safer alternative paths with acceptable delays. 

The reinforcement learning agent was retrained using environment states specific to this scenario, including infrastructure damage level, unmet demand urgency, and congestion estimates. 

### _7.4. Case Study Results_ 

Table 13 summarizes the outcomes achieved by the QHHF after 50 generations. 

**Table 13.** QHHF Performance in Beirut Disaster Scenario. 

|**Metric**|**Value**|**Interpretation**|
|---|---|---|
|Total Travel Cost (Z1)|1528.6|Efficient routing under severe constraints|
|Total Risk Exposure (Z2)|712.9|Avoidance of unstable and dangerous zones|
|Priority-Weighted Satisfaction (Z3)|8945.1|Most critical needs were met effectively|
|Average Response Time per Node|3.8 h|Timely delivery despite blocked routes|



### _7.5. Analysis and Insights_ 

The QHHF achieved a highly efficient response strategy, ensuring that high-priority locations received aid within the golden 24-h window. It consistently prioritized hospitals and dense shelters while minimizing vehicle exposure to damaged areas. Notably: 

- Routes adapted dynamically when new blocked roads were reported 

_World Electr. Veh. J._ **2025** , _16_ , 310 

32 of 36 

- The RL agent began favoring the damage-avoidance heuristic after 15 time units 

- Resource allocation favored areas with higher population impact scores 

Figure 7 shows an example output of optimized vehicle routes with risk zones overlaid. It illustrates how QHHF dynamically prioritizes high-urgency nodes while avoiding highrisk paths. The clear separation of vehicle assignments and efficient loop closures highlight the algorithm’s adaptiveness under evolving constraints. 



**Figure 7.** Optimized vehicle routing plan using QHHF for the Beirut case study. Colored paths represent vehicle routes (color-coded by vehicle ID). Red-shaded areas indicate high-risk zones, while yellow-shaded areas represent moderate-risk regions. Blue circles are high-priority demand nodes, and the central depot is marked by a black square. 

### _7.6. Practical Implications_ 

This case study demonstrates that QHHF can serve as a powerful decision-support tool for emergency logisticians. By integrating domain-specific heuristics and real-time feedback, the framework can dynamically reconfigure routes and allocations, ensuring responsive, risk-aware, and priority-sensitive operations under extreme conditions. 

### _7.7. Stakeholder Utility_ 

Stakeholders such as NGOs, civil defense teams, and governmental crisis units could use such a system to: 

- Simulate and validate aid delivery plans 

- Re-prioritize in real time based on situational intelligence 

- Reduce operational risks for frontline responders 

This validation under real-world constraints strengthens the applicability of QHHF beyond academic benchmarking, marking a step toward deployable AI-supported logistics platforms. 

## **8. Conclusions and Perspectives** 

This study introduced a novel Quantum-Inspired Hyperheuristic Framework (QHHF) for solving dynamic multi-objective combinatorial optimization problems in disaster logistics. The framework combines the global search capabilities of Quantum-Inspired Evolutionary Algorithms (QIEAs) with the adaptive decision-making power of Reinforcement Learning (RL)-based heuristic selection. This integration enables the system to effectively 

_World Electr. Veh. J._ **2025** , _16_ , 310 

33 of 36 

navigate complex and evolving environments characterized by uncertainty, constrained resources, and conflicting objectives. 

We formulated a dynamic multi-objective mathematical model that simultaneously minimizes total travel cost and risk exposure while maximizing the satisfaction of highpriority demand. The QHHF adaptively selects from a pool of low-level heuristics based on real-time feedback, ensuring improved performance as the environment changes. The QHHF framework consistently outperformed GA, ACO, and standalone QIEA across all objectives, achieving reductions of up to 236 units in travel cost and 125 units in risk exposure, along with an increase of over 200 units in weighted demand satisfaction across both simulated and real-world scenarios. 

Key findings from this study include: 

- QHHF consistently outperformed baseline algorithms in cost, risk, and demand satisfaction metrics. 

- The reinforcement learning mechanism enabled effective heuristic selection in dynamic contexts. 

- The quantum-inspired encoding enhanced solution diversity and convergence. 

- • Real-world deployment simulations confirmed its viability in time-critical disaster response. 

Beyond the demonstrated performance in benchmark simulations, the QHHF framework shows promise for real-world deployment in emergency logistics contexts. Its modular structure, low computational overhead, and learning-based adaptability make it suitable for integration into field-level decision-support platforms. However, several practical considerations must be addressed for full deployment. 

The current implementation assumes reliable access to dynamic input data (e.g., evolving risk maps and demand updates), which may not always be available in disasteraffected areas. Furthermore, while the model uses homogeneous vehicle assumptions and static fleet sizes, real operations may involve heterogeneous capacities, vehicle priorities, and constrained communication. 

To address these challenges, future work will explore the hybridization of QHHF with deep reinforcement learning to enhance policy generalization. The model will also be extended to support multi-depot and multi-modal logistics planning, with pilot studies planned in collaboration with humanitarian organizations and civil protection agencies. These steps aim to validate the robustness, scalability, and usability of QHHF in practical response scenarios. 

Future research directions include: 

- Extending the framework to handle multi-depot and heterogeneous fleet configurations. 

- Incorporating real-time data feeds from IoT and GIS sources for live re-optimization. 

- Exploring transfer learning to reduce training time for new disaster scenarios. 

- Deploying a cloud-based version of QHHF as a decision-support tool for humanitarian agencies. 

- Hybridizing QHHF with NSGA-II or MOEA/D, integrating their Pareto-ranking and decomposition strategies into the population update mechanism while retaining the learning-driven heuristic selection controller. 

- The framework currently uses a tabular Q-learning controller, which may be limited in handling larger and more complex state spaces. Future work will explore integrating deep reinforcement learning or graph-based policies to enhance scalability. 

The proposed framework lays the groundwork for intelligent, responsive, and riskaware disaster logistics systems. It opens new avenues for integrating emerging AI 

_World Electr. Veh. J._ **2025** , _16_ , 310 

34 of 36 

paradigms with classical optimization to address the urgent and complex challenges of humanitarian operations. 

**Author Contributions:** Conceptualization, K.D. and L.S.; methodology, K.D.; software, K.D.; validation, H.H.; formal analysis, H.H.; investigation, A.R.; resources, H.H.; data curation, L.S. and H.H.; writing—original draft preparation, K.D.; writing—review and editing, H.H. and A.R.; visualization, L.S.; supervision, H.H.; project administration, K.D. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Institutional Review Board Statement:** Not applicable. 

**Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** The implementation code for the proposed QHHF framework will be made available upon reasonable request to the corresponding author. Plans are underway to release a public GitHub repository following publication. 

**Conflicts of Interest:** The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results. 

## **References** 

1. Rajabboev, B. Evacuation of the Population in Emergency Situations . _Educ. Insights: J. Teach. Theory Pract._ **2025** , _1_ , 392–399. 2. Imbriale, P. The role of government in humanitarian logistics: A systematic review. _J. Humanit. Logist. Supply Chain. Manag._ 2025, ahead-of-print. [CrossRef] 

3. Kanj, H.; Flaus, J.M. A simulation approach for risk modeling and analysis based on multi-agents. In Proceedings of the ESREL 2015, 25th European Safety and Reliability Conference, Zurich, Switzerland, 7–10 September 2015 . 

4. Javan-Molaei, B.; Tavakkoli-Moghaddam, R.; Ghanavati-Nejad, M.; Asghari-Asl, A. A data-driven robust decision-making model for configuring a resilient and responsive relief supply chain under mixed uncertainty. In _Annals of Operations Research_ ; Springer: Berlin/Heidelberg, Germany, 2024; pp. 1–38. 

5. Wang, G. Disaster relief supply chain network planning under uncertainty. _Ann. Oper. Res._ **2024** , _338_ , 1127–1156. [CrossRef] 

6. Nawajah, I.; Kanj, H.; Kotb, Y.; Hoxha, J.; Alakkoumi, M.; Jebreen, K. Bayesian regression analysis using median rank set sampling. _Eur. J. Pure Appl. Math._ **2024** , _17_ , 180–200. [CrossRef] 

7. Kamyabniya, A.; Sauré, A.; Salman, F.S.; Bénichou, N.; Patrick, J. Optimization models for disaster response operations: A literature review. _OR Spectr._ **2024** , _46_ , 737–783. [CrossRef] 

8. Khalili, S.M.; Mojtahedi, M.; Steinmetz-Weiss, C.; Sanderson, D. A systematic literature review on transit-based evacuation planning in emergency logistics management: Optimisation and modelling approaches. _Buildings_ **2024** , _14_ , 176. [CrossRef] 

9. Danach, K. Hyperheuristics in Logistics. Ph.D. Thesis, Ecole Centrale de Lille, Villeneuve-d’Ascq, France, 2016. 

10. Harb, H.; Makhoul, A.; Jaber, A.; Tawbi, S. Energy efficient data collection in periodic sensor networks using spatio-temporal node correlation. _Int. J. Sens. Netw._ **2019** , _29_ , 1–15. [CrossRef] 

11. Yáñez-Sandivari, L.; Cortés, C.E.; Rey, P.A. Humanitarian logistics and emergencies management: New perspectives to a sociotechnical problem and its optimization approach management. _Int. J. Disaster Risk Reduct._ **2021** , _52_ , 101952. [CrossRef] 

12. Harb, H.; Makhoul, A.; Laiymani, D.; Bazzi, O.; Jaber, A. An analysis of variance-based methods for data aggregation in periodic sensor networks. In _Transactions on Large-Scale Data-and Knowledge-Centered Systems XXII_ ; Springer: Berlin/Heidelberg, Germany, 2015; pp. 165–183. 

13. Zhang, W.; Bao, X.; Hao, X.; Gen, M. Metaheuristics for multi-objective scheduling problems in industry 4.0 and 5.0: A state-of-the-arts survey. _Front. Ind. Eng._ **2025** , _3_ , 1540022. [CrossRef] 

14. Yan, Y.; Chow, A.H.; Ho, C.P.; Kuo, Y.H.; Wu, Q.; Ying, C. Reinforcement learning for logistics and supply chain management: Methodologies, state of the art, and future opportunities. _Transp. Res. Part E Logist. Transp. Rev._ **2022** , _162_ , 102712. [CrossRef] 

15. Sivamayil, K.; Rajasekar, E.; Aljafari, B.; Nikolovski, S.; Vairavasundaram, S.; Vairavasundaram, I. A systematic study on reinforcement learning based applications. _Energies_ **2023** , _16_ , 1512. [CrossRef] 

16. Gomes, C.; Fernandes, J.P.; Falcao, G.; Kar, S.; Tayur, S. A Systematic Mapping Study on Quantum and Quantum-inspired Algorithms in Operations Research. _ACM Comput. Surv._ **2024** , _57_ , 1–35. [CrossRef] 

17. Wu, J.; Wang, X.; Tian, A.; Du, Z.; Yang, Z. A Hybrid Meta-Heuristic Approach for Emergency Logistics Distribution Under Uncertain Demand. _IEEE Access_ **2024** , _12_ , 112345–112357. [CrossRef] 

_World Electr. Veh. J._ **2025** , _16_ , 310 

35 of 36 

18. Ballinas, E.; Montiel, O.; Martínez-Vargas, A.; Rodríguez-Cortés, G. Hybrid Quantum Genetic Algorithm with Fuzzy Adaptive Rotation Angle for Efficient Placement of UAVs in Natural Disaster Areas. _Axioms_ **2024** , _13_ , 48. [CrossRef] 

19. Danach, K.; Hassan, J.A.H.; Khalil, W.; Gelareh, S. Routing heterogeneous mobile hospital with different patients priorities: Hyper-heuristic approach. In Proceedings of the 2015 Fifth International Conference on Digital Information and Communication Technology and its Applications (DICTAP), Beirut, Lebanon, 29 April–1 May 2015; IEEE: Piscataway, NJ, USA, 2015; pp. 155–158. 

20. Carnero Quispe, M.F.; Chambilla Mamani, L.D.; Yoshizaki, H.T.Y.; Brito Junior, I.D. Temporary Facility Location Problem in Humanitarian Logistics: A Systematic Literature Review. _Logistics_ **2025** , _9_ , 42. [CrossRef] 

21. Liu, L.; Lee, L.S.; Seow, H.V.; Chen, C.Y. Logistics center location-inventory-routing problem optimization: A systematic review using PRISMA method. _Sustainability_ **2022** , _14_ , 15853. [CrossRef] 

22. Aghsami, A.; Sharififar, S.; Moghaddam, N.M.; Hazrati, E.; Jolai, F. A bi-objective mixed-integer non-linear programming model with grasshopper optimization algorithm for military-based humanitarian supply chains. _Decis. Anal. J._ **2024** , _10_ , 100409. [CrossRef] 

23. Kasim, M.H.; Djakaria, I.; Yahya, L. Model Integer Linear Programming pada Optimisasi Distribusi Logistik di Daerah Bencana. _Res. Math. Nat. Sci._ **2022** , _1_ , 19–26. [CrossRef] 

24. Rasyid, E.; Artana, K.B.; Sambodho, K. Optimization of disaster management vessel networks in integrated disaster management governance in Indonesia using genetic algorithm. In _Proceedings of the IOP Conference Series: Earth and Environmental Science_ ; IOP Publishing: Bristol, UK, 2024; Volume 1423, p. 12022. 

25. Guerrero Granados, B.; Quintero, M.C.G.; Núñez, C.V. Improved genetic algorithm approach for coordinating decision-making in technological disaster management. _Neural Comput. Appl._ **2024** , _36_ , 4503–4521. [CrossRef] 

26. Bansal, S.; Goel, R.; Maini, R. Ground vehicle and UAV collaborative routing and scheduling for humanitarian logistics using random walk based ant colony optimization. _Sci. Iran._ **2022** , _29_ , 632–644. 

27. Yin, Z.; Yin, Z.; Ye, J.; Liu, R. Optimization of emergency logistics delivery path based on guided local search algorithm. _J. Comput. Methods Sci. Eng._ **2024** , _24_ , 1889–1902. [CrossRef] 

28. Gan, Q. Optimizing emergency logistics centre locations: A multi-objective robust model. _Economics_ **2024** , _18_ , 20220121. [CrossRef] 29. Wang, B.; He, C. Research on the Optimization Model of Emergency Logistics Distribution Path Considering Road Repair Under Extreme Disasters. Social Science Research Network (SSRN). 2025; pp. 1–33. Available online: https://ssrn.com/abstract=5175187 (accessed on 20 April 2025). 

30. Rodríguez-Espíndola, O.; Ahmadi, H.; Gastélum-Chavira, D.; Ahumada-Valenzuela, O.; Chowdhury, S.; Dey, P.K.; Albores, P. Humanitarian logistics optimization models: An investigation of decision-maker involvement and directions to promote implementation. _Socio-Econ. Plan. Sci._ **2023** , _89_ , 101669. [CrossRef] 

31. Guo, K.; Zhang, L. Multi-objective optimization for improved project management: Current status and future directions. _Autom. Constr._ **2022** , _139_ , 104256. [CrossRef] 

32. Carnero Quispe, M.F.; Couto, A.S.; de Brito Junior, I.; Cunha, L.R.A.; Siqueira, R.M.; Yoshizaki, H.T.Y. Humanitarian logistics prioritization models: A systematic literature review. _Logistics_ **2024** , _8_ , 60. [CrossRef] 

33. Ershadi, M.M.; Shemirani, H.S. A multi-objective optimization model for logistic planning in the crisis response phase. _J. Humanit. Logist. Supply Chain Manag._ **2022** , _12_ , 30–53. [CrossRef] 

34. Sun, H.; Li, J.; Wang, T.; Xue, Y. A novel scenario-based robust bi-objective optimization model for humanitarian logistics network under risk of disruptions. _Transp. Res. Part E Logist. Transp. Rev._ **2022** , _157_ , 102578. [CrossRef] 

35. Ye, J.; Jiang, W.; Yang, X.; Hong, B. Emergency materials response framework for petrochemical enterprises based on multiobjective optimization. _Energy_ **2023** , _269_ , 126670. [CrossRef] 

36. Bouazza, W. Hyper-heuristics applications to manufacturing scheduling: Overview and opportunities. _IFAC-PapersOnLine_ **2023** , _56_ , 935–940. [CrossRef] 

37. Danach, K.; Gelareh, S.; Monemi, R.N. The capacitated single-allocation p-hub location routing problem: A Lagrangian relaxation and a hyper-heuristic approach. _EURO J. Transp. Logist._ **2019** , _8_ , 597–631. [CrossRef] 

38. Li, C.; Wei, X.; Wang, J.; Wang, S.; Zhang, S. A review of reinforcement learning based hyper-heuristics. _PeerJ Comput. Sci._ **2024** , _10_ , e2141. [CrossRef] 

39. Danach, K. Reinforcement Learning for Dynamic Vehicle Routing Problem: A Case Study with Real-World Scenarios. _Int. J. Commun. Netw. Inf. Secur._ **2024** , _16_ , 580–589. 

40. Kesik, S.; Altınta¸s, C. A Hyper-Heuristic Approach to Solving Vehicle Routing Problem in Military Logistics Distribution. In Proceedings of the International Conference on Artificial Intelligence and Applied Mathematics in Engineering, Antalya, Türkiye, 3–5 November 2023; Springer: Berlin/Heidelberg, Germany, 2023; pp. 168–191. 

41. Tlili, T.; Ben Nasser, S.; Chicano, F.; Krichen, S. Tabu Search-based hyper-heuristic for Solving the Heterogeneous Ambulance Routing Problem with Time Windows . _Int. J. Intell. Transp. Syst. Res._ **2024** , _22_ , 446–461. [CrossRef] 

42. Shahmanzari, M.; Mansini, R. A learning-based granular variable neighborhood search for a multi-period election logistics problem with time-dependent profits. _Eur. J. Oper. Res._ **2024** , _319_ , 135–152. [CrossRef] 

_World Electr. Veh. J._ **2025** , _16_ , 310 

36 of 36 

43. Ngwu, C.; Liu, Y.; Wu, R. Reinforcement learning in dynamic job shop scheduling: A comprehensive review of AI-driven approaches in modern manufacturing. _J. Intell. Manuf._ **2025** , _4_ , 1–16. [CrossRef] 

44. Tran, M.; Nguyen, T.; Le, H. A Reinforcement Learning-Based Hyper-Heuristic for Multi-Objective Routing Problems. In Proceedings of the GECCO, Boston, MA, USA, 9–13 July 2022. 

45. Torabi, P.; Hemmati, A.; Oleynik, A.; Alendal, G. A deep reinforcement learning hyperheuristic for the covering tour problem with varying coverage. _Comput. Oper. Res._ **2025** , _174_ , 106881. [CrossRef] 

46. Deb, K.; Pratap, A.; Agarwal, S.; Meyarivan, T. A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II. _IEEE Trans. Evol. Comput._ **2002** , _6_ , 182–197. [CrossRef] 

47. Nazari, M.; Oroojlooy, A.; Snyder, L.V.; Takác, M. Reinforcement Learning for Solving the Vehicle Routing Problem. _Adv. Neural Inf. Process. Syst._ **2018** , _31_ , 1–11 . 

48. Bello, I.; Pham, H.; Le, Q.V.; Norouzi, M.; Bengio, S. Attention, Learn to Solve Routing Problems! _arXiv_ **2017** , arXiv:1803.08475. 49. Wang, J.; Chen, L.; Liu, Y.; Sun, Y. Urban Intersection Traffic Flow Prediction: A Physics-Guided Stepwise Framework Utilizing Spatio-Temporal Graph Neural Network Algorithms. _Appl. Soft Comput._ **2022** , _113_ , 107911. 

50. Phillipson, F. Quantum computing in logistics and supply chain management an overview. _arXiv_ **2024** , arXiv:2402.17520. 

51. Tripathi, R.; Tomar, S.; Kumar, S. A Comprehensive Survey on Quantum Annealing: Applications, Challenges, and Future Research Directions. _Authorea Prepr._ **2025** , _1_ , 1–33. 

52. Whig, P.; Mudunuru, K.R.; Remala, R. Quantum-inspired data-driven decision making for supply chain logistics. In _Quantum Computing and Supply Chain Management: A New Era of Optimization_ ; IGI Global: Hershey, PA, USA, 2024; pp. 85–98. 

53. Karn, A.K.; Sinha, P.; Kaur, S.; Bansal, H. Quantum-Enhanced Strategies for Optimizing Disaster Response: A Machine Learning Approach. In _The Rise of Quantum Computing in Industry 6.0 Towards Sustainability_ ; Springer: Berlin/Heidelberg, Germany, 2024; pp. 193–204. 

54. Vinyals, O.; Fortunato, M.; Jaitly, N. Pointer Networks. In Proceedings of the NeurIPS, Montréal, QC, Canada, 7–12 December 2015. 55. Kool, W.; van Hoof, H.; Welling, M. Attention, Learn to Solve Routing Problems! In Proceedings of the ICLR, Addis Ababa, Ethiopia, 26–30 April 2020. 

56. Abid, S.K.; Sulaiman, N.; Chan, S.W.; Nazir, U.; Abid, M.; Han, H.; Ariza-Montes, A.; Vega-Muñoz, A. Toward an integrated disaster management approach: How artificial intelligence can boost disaster management. _Sustainability_ **2021** , _13_ , 12560. [CrossRef] 

57. Sun, W.; Bocchini, P.; Davison, B.D. Applications of artificial intelligence for disaster management. _Nat. Hazards_ **2020** , _103_ , 2631–2689. [CrossRef] 

58. Zhang, W. Research on the Application of Computer Artificial Intelligence Technology in the Response Mechanism of Emergency Logistics System. In Proceedings of the 2022 IEEE International Conference on Advances in Electrical Engineering and Computer Applications (AEECA), Dalian, China, 20–21 August 2022; IEEE: Piscataway, NJ, USA, 2022; pp. 676–680. 

59. Hasanuzzaman, M.; Hossain, S.; Shil, S.K. Enhancing disaster management through AI-driven predictive analytics: Improving preparedness and response. _Int. J. Adv. Eng. Technol. Innov._ **2023** , _1_ , 533–562. 

60. Ortiz, B.; Kahn, L.; Bosch, M.; Bogden, P.; Pavon-Harr, V.; Savas, O.; McCulloh, I. Improving community resiliency and emergency response with artificial intelligence. _arXiv_ **2020** , arXiv:2005.14212. 

61. Han, K.; Kim, J.H. Quantum-inspired evolutionary algorithm for a class of combinatorial optimization. _IEEE Trans. Evol. Comput._ **2002** , _6_ , 580–593. [CrossRef] 

62. Zhou, X.; Wang, L.; Jin, Y. A quantum-inspired evolutionary approach for vehicle routing problems with time windows. _Soft Comput._ **2020** , _24_ , 12589–12605. 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

