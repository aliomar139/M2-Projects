

Received 3 February 2025, accepted 9 March 2025, date of publication 26 March 2025, date of current version 4 April 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3550560_ 

# Advanced Optimization in E-Commerce Logistics: Combining Matheuristics With Random Forests for Hub Location Efficiency 

## KASSEM DANACH 1, (Member, IEEE), ABBAS RAMMAL2, IMAD MOUKADEM3, HASSAN HARB<sup>4</sup> , (Member, IEEE), AND ABBASS NASSER<sup>5</sup> , (Senior Member, IEEE) 

1Basic and Applied Sciences Research Center, Al Maaref University, Beirut 1600, Lebanon 

2Department of Computer and Telecom Engineer, Islamic University of Lebanon, Beirut 30014, Lebanon 

3Electrical and Computer Engineering Maroun Semaan Faculty of Engineering and Architecture, American University of Beirut, Beirut 1107 2020, Lebanon 

4College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait 

5Business Computing Department, Business School, Holy-Spirit University of Kaslik, Jounieh, Lebanon 

Corresponding author: Abbass Nasser (abbass.nasser@usek.edu.lb) 

- **ABSTRACT** The rapid growth of e-commerce has introduced significant challenges in optimizing logistics and distribution networks, particularly in determining hub locations to balance cost efficiency and service quality. This study presents a novel framework integrating matheuristics with Random Forest machine learning to address the Hub Location Problem (HLP) in e-commerce logistics. Leveraging real-world data from a global logistics company, the methodology combines predictive analytics with robust optimization techniques to dynamically adjust hub configurations based on fluctuating demand and operational constraints. Experimental results demonstrate substantial improvements over traditional methods, including an improvement of 7 _._ 8% in delivery time compliance, a 9 _._ 4% increase in fulfillment rate and enhanced network robustness by 16%. The findings highlight the strategic advantages of integrating advanced analytics into logistics planning, offering actionable insights for industry practitioners. 

**INDEX TERMS** Hub location problem, e-commerce, logistics, optimization, matheuristics, random forest. 

### **I. INTRODUCTION** 

### _A. CONTEXT_ 

The rapid expansion of e-commerce has significantly reshaped global supply chains, prompting an increased emphasis on optimizing logistics and distribution networks [1]. Central to these networks is the strategic placement of hubs, which act as critical nodes for the sorting and distribution of goods. The efficiency of these hubs directly influences operational costs and service quality, making the Hub Location Problem (HLP) a crucial focus of research in logistics management and operations research [2]. 

The concept of hub-and-spoke networks was initially explored by [3] and has since been a cornerstone in the study of transportation and logistics optimization. These networks leverage economies of scale to reduce transportation costs, 

The associate editor coordinating the review of this manuscript and approving it for publication was Wei Ni. 

a principle that has been validated across various industries, including telecommunications and freight [4], [5]. The primary objective in HLP research is often to minimize total costs, which encompass fixed hub establishment costs, variable transportation costs, and potential penalties for unmet demand or delays [4], [6]. 

### _B. CHALLENGES_ 

In the context of e-commerce, the HLP is particularly complex due to the dynamic nature of consumer demand, the broad range of product categories, and the critical requirement for timely deliveries. Previous studies, such as those by [7], have emphasized the significance of accommodating fluctuating demand patterns and varying service levels in hub network design. Additionally, the integration of robust optimization techniques has been explored to address uncertainties and potential disruptions within these networks [5], [6]. 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

55915 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



### _C. CONTRIBUTIONS_ 

This paper aims to contribute to the body of knowledge on the HLP by developing a comprehensive mathematical model tailored to the specific challenges of e-commerce logistics. The model incorporates factors such as demand variability, hub capacity constraints, and risk management for potential disruptions. We propose advanced computational methods, including metaheuristic algorithms and machine learning techniques, to solve the problem efficiently. Through case studies, we demonstrate the practical application and benefits of our approach, highlighting significant improvements in cost efficiency and service quality. 

### _D. PAPER STRUCTURE_ 

The remainder of this paper is organized as follows. Section II provides a comprehensive literature review, summarizing relevant studies and highlighting gaps that this research aims to address. Section III presents the problem statement, detailing the key challenges and considerations specific to the Hub Location Problem in e-commerce logistics. Section IV outlines the study’s objectives and the methodology employed, including the development of the mathematical model and the design of advanced algorithms. In Section V, we discuss the research questions and hypotheses that guide this study. The mathematical formulation for the HLP is detailed in Section VI, followed by the solution approach in Section VII, which integrates meta-heuristics and Random Forest techniques. Section VIII describes the dataset used in our experiment along with the environmental setup. Section IX discusses the results obtained by applying our solution, and, Finally, Section X concludes the paper with a summary of findings, implications, and suggestions for future research. 

### **II. LITERATURE REVIEW** 

The Hub Location Problem (HLP) has been extensively studied in the fields of operations research and logistics, particularly in the context of transportation and supply chain management. The foundational work established the significance of hub-and-spoke networks in minimizing transportation costs and improving service efficiency [3]. This model has since been adapted and extended to various applications, including telecommunications [4], [5] and airline operations [8]. 

Recent advancements in HLP research have focused on integrating sophisticated optimization techniques to address complex logistical challenges. For instance, research explored the capacitated single-allocation p-hub location routing problem using a Lagrangian relaxation combined with a hyper-heuristic approach. This method addresses both the routing and allocation aspects of the problem, highlighting the importance of efficient algorithm design in solving large-scale HLPs [9]. 

In the realm of e-commerce, the HLP presents unique challenges due to dynamic demand patterns and the necessity 

for rapid deliveries. Research highlighted the importance of integrating demand variability into hub location models, noting that fluctuations in consumer behavior and seasonal trends significantly impact logistics networks [5], [6]. This view is supported by studies that emphasized the need for models that can adapt to changing market conditions [4]. 

Capacity constraints are another critical factor in the HLP, particularly in e-commerce settings where hubs must manage varying volumes of goods. Studies discussed models that incorporate capacity limitations, focusing on optimizing the allocation of demand to prevent bottlenecks [4], [7]. This aspect is crucial for maintaining service levels, as unmet demand or delays can lead to significant penalties and customer dissatisfaction [10], [11]. 

Service level agreements (SLAs) are increasingly vital in e-commerce logistics, with companies striving to meet strict delivery deadlines. Research underscores the role of hub location in achieving these service levels, highlighting the need for precise and efficient network design [3], [12]. The integration of robust optimization techniques has been suggested to address uncertainties and disruptions, ensuring that networks remain resilient and reliable under varying conditions [6], [8]. 

The authors of [13], [14], and [15] used metaheuristic LSTMs for demand prediction in e-commerce logistics. In [13], the authors proposed a Density Based Spatial Clustering of Applications with Noise (DBSCAN) Algorithm to detect and remove outlier packages in the noisy geospatial dataset. The clustering algorithm is first used to distribute packages equally to each courier on the time, then a Long Short-term Memory (LSTM) is constructed to predict how many packages will be delivered to each courier in the coming days. Similarly, the authors of [14] designed two neural networks to forecast B2B sales in e-commerce, e.g. recurrent neuronal network (RNN) and LSTM. Subsequently, the hyper-parameter tuning and feature selection process are done through a modified metaheuristic optimizer to reach more accurate predictions. In [15], the authors proposed a transformer model based on LSTM that uses a self-attention mechanism to forecast the passenger flow between transportation hubs in urban zones. The model is also used to predict more multimodal traffic network data in urban agglomerations, such as the prediction of transport volume in important passenger hubs, and to predict passenger flow in inter-hub transfer corridors in different states. 

The authors of [16] focused on metaheuristic graph neural networks (GNNs) optimization to solve the multi-objective facility location problem in transportation systems. Accordingly, they proposed a federated graph neural networks with bipartite graph to acquire implicit embeddings for nodes and edges. On one hand, the federated learning is used to enable collaboration on training tasks without sharing raw data, thus protecting sensitive information related to facility construction and transportation costs. On the other hand, the GNN is applied on the central server to ensure transportation 

55916 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



equity between clients through a probability distribution of the Pareto set. 

Cost minimization remains a primary objective in the HLP. Studies have explored various strategies for reducing both fixed and variable costs, including the strategic placement of hubs to minimize transportation expenses [4], [5]. The trade-offs between cost and service quality are a recurring theme in the literature, with recent advancements focusing on balancing these factors to optimize overall network performance [17], [18]. 

In summary, the literature on the Hub Location Problem in e-commerce logistics highlights the complexity of balancing multiple factors such as demand variability, capacity constraints, service levels, cost efficiency, and risk management. This study builds on these foundations, proposing advanced mathematical models and algorithms to further enhance the efficiency and robustness of e-commerce distribution networks. 

### **III. PROBLEM STATEMENT** 

The e-commerce sector has experienced unprecedented growth, significantly increasing the complexity of logistics and distribution networks. A critical challenge within these networks is the Hub Location Problem (HLP), which involves determining the optimal placement and configuration of distribution hubs to minimize total costs and maximize service efficiency. This problem is particularly pronounced in e-commerce due to several key factors: 

- **Types of Hubs Considered:** Distribution networks can employ various types of hubs, such as: 

   - -- **Centralized Hubs:** Large-scale facilities designed to handle significant volumes of goods, prioritizing economies of scale. These hubs are the primary focus of this study due to their strategic role in consolidating operations and reducing costs in e- commerce logistics. 

   - -- **Distributed Hubs:** Smaller hubs dispersed across regions to enhance responsiveness and reduce delivery times. Although distributed hubs are not the primary focus of this study, their characteristics are acknowledged as part of the broader landscape of hub configurations. 

   - -- **Hybrid Hubs:** A combination of centralized and distributed hubs that balance cost efficiency and responsiveness. This study provides insights into centralized hubs as a foundational aspect of hybrid configurations. 

By focusing on centralized hubs, this research aims to provide a detailed understanding of their optimization while acknowledging the potential extension of the model to distributed or hybrid hub systems in future studies. 

- **Dynamic Demand and Variability:** E-commerce platforms frequently encounter fluctuating demand levels ( _dj_ ) influenced by seasonal trends, marketing promotions, and shifts in consumer behavior. This variability 

complicates the accurate prediction of demand patterns ( _d_<sup>ˆ</sup> _j_ ), necessitating a robust and adaptive model for hub placement [5], [6]. 

- **Capacity Constraints:** Centralized hubs have limited capacity ( _u_<sup>_k_</sup> _i_<sup>), including physical storage space, process-</sup> ing capabilities, and workforce availability. Efficient management of these capacities is essential to prevent bottlenecks while meeting demand allocation ( _yij_ ) requirements [4], [7]. 

- **Service Level Requirements:** To maintain competitiveness, e-commerce companies must ensure fast and reliable deliveries. Centralized hubs play a crucial role in meeting service level agreements (SLAs) by minimizing the distance ( _dij_ ) or time ( _tij_ ) to delivery points [3]. 

- **Cost Minimization:** The objective is to minimize total operational costs, including fixed costs for establishing centralized hubs ( _fi_ ), variable transportation costs ( _cij_ ), and penalties ( _p_ ) for delays or unmet demand. The study explores how centralized hub placement impacts overall network design and cost efficiency [4], [5]. 

- **Risk and Uncertainty Management:** E-commerce logistics networks are vulnerable to disruptions such as natural disasters, supply chain interruptions, and transportation delays. This study incorporates robust optimization techniques to enhance the resilience of centralized hub networks [5], [6]. 

This research aims to address these challenges by developing a comprehensive mathematical model and advanced solution algorithms tailored to the HLP for centralized hubs in e-commerce. While the primary focus is on centralized hubs, the study acknowledges the relevance of distributed and hybrid hubs, paving the way for potential future extensions. The model incorporates elements such as demand variability, capacity constraints, service level agreements, cost efficiency, and risk management, providing actionable insights for optimizing e-commerce distribution networks. 

### **IV. STUDY OBJECTIVE AND SCOPE** 

The primary objective of this research is to develop and validate a comprehensive framework for optimizing hub locations in e-commerce distribution networks. This framework addresses the unique challenges posed by the dynamic and complex nature of e-commerce logistics. To clearly define the scope, the study focuses on the following specific objectives: 

- **Mathematical Model Development:** Formulate a robust mathematical model tailored to e-commerce logistics that incorporates: 

   - -- Demand variability and forecasting tailored to real-world seasonal and regional e-commerce demand patterns. 

   - -- Hub capacity constraints reflecting industryspecific storage and processing limitations. 

   - -- Service level requirements and time-sensitive delivery constraints, such as next-day or same-day delivery. 

55917 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



   - -- Cost minimization objectives, covering fixed and variable costs relevant to e-commerce operations. 

   - -- Risk management strategies to mitigate disruptions like supplier delays or unexpected demand surges. 

- **Algorithm Design and Implementation:** Design and implement advanced algorithms for solving the Hub Location Problem (HLP), emphasizing: 

   - -- Metaheuristic algorithms, including Genetic Algorithms (GA) and Variable Neighborhood Search (VNS), adapted for large-scale e-commerce datasets. 

   - -- Machine learning models for demand forecasting and supporting dynamic decision-making in volatile market conditions. 

   - -- Robust optimization techniques to ensure resilience against demand uncertainties and logistical disruptions. 

- **Case Study Application:** Validate the proposed framework using real-world industry data from a prominent e-commerce platform, emphasizing: 

   - -- Comprehensive data collection and analysis, including customer demand trends, operational constraints, and cost structures. 

   - -- Simulation of various hub configurations and their impact on key performance metrics like delivery speed and cost-efficiency. 

   - -- Comparative analysis with existing industrystandard solutions to quantify improvements and innovations. 

- **Performance Evaluation:** Evaluate the effectiveness of the proposed solutions using clearly defined metrics, such as: 

   - -- Total operational costs, including logistics, infrastructure, and operational costs. 

   - -- Service levels, customer satisfaction rates, and fulfillment times. 

   - -- Scalability of the hub network to accommodate growth in demand or geographical expansion. 

   - -- Resilience against disruptions, including unforeseen demand shifts or logistical challenges. 

This study not only seeks to advance theoretical insights into the Hub Location Problem (HLP) in e-commerce but also aims to provide actionable recommendations and decision-support tools for practitioners in the logistics and e- commerce industries. 

### **V. RESEARCH QUESTIONS AND HYPOTHESIS** 

The research aims to address the following key questions regarding the optimization of hub locations in e-commerce distribution networks: 

- 1) How can the variability in customer demand be accurately forecasted and incorporated into hub location decisions to enhance service efficiency? 

- 2) What is the impact of varying hub capacities on overall operational costs and service levels, and how can these be optimized? 

- 3) How can robust optimization techniques be utilized to mitigate the risks associated with uncertainties and disruptions in the logistics network? 

- 4) What are the comparative advantages of metaheuristic algorithms versus machine learning approaches in solving the Hub Location Problem (HLP) for e- commerce? 

- The study posits the following hypotheses based on the 

- outlined research questions: 

- **H1:** Incorporating advanced demand forecasting techniques into the hub location model will significantly improve the accuracy of demand predictions, leading to better allocation of resources and improved service efficiency. 

- **H2:** Optimizing hub capacities, considering both physical and operational constraints, will reduce total operational costs and enhance service levels by minimizing the occurrence of bottlenecks and overcapacity situations. 

- **H3:** The application of robust optimization methods will enhance the resilience of the e-commerce distribution network, ensuring consistent service levels and reduced costs even under uncertain conditions and potential disruptions. 

- **H4:** Metaheuristic algorithms, due to their ability to efficiently explore large solution spaces, will outperform traditional optimization methods and potentially machine learning techniques in finding optimal hub configurations for large-scale e-commerce networks. 

- **H5:** The integration of real-time data analytics and dynamic decision-making models will provide significant improvements in the flexibility and scalability of the hub network, allowing for adaptive responses to changing market conditions. 

These hypotheses will be tested through the development and application of the proposed mathematical models and algorithms, with their effectiveness evaluated using real-world data and simulation scenarios. 

### **VI. MATHEMATICAL FORMULATION FOR THE HUB LOCATION PROBLEM IN E-COMMERCE DISTRIBUTION NETWORKS** 

In this section, we present a comprehensive mathematical model for optimizing hub locations in e-commerce distribution networks. The model aims to minimize total costs, considering various constraints and operational parameters typical in e-commerce logistics. 

### _A. NOTATION_ 

- _I_ : Set of potential hub locations, indexed by _i_ . 

- _J_ : Set of demand points (e.g., customer locations), indexed by _j_ . 

- _K_ : Set of different hub capacity levels, indexed by _k_ . 

- _C_ : Set of vehicle types, if applicable, indexed by _c_ . 

- _fi_ : Fixed cost for opening a hub at location _i_ . 

55918 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



- _cij_ : Variable cost for transporting goods between hub _i_ and demand point _j_ . This cost typically includes fuel, labor, and maintenance costs. 

- _dj_ : Demand at point _j_ , representing the total quantity of goods required at this location. 

- • _u_<sup>_k_</sup> _i_<sup>:Capacityofhub</sup><sup>_i_whenoperatingatcapacitylevel</sup> _k_ . This capacity could be defined in terms of volume, weight, or number of orders processed. 

- _p_ : Penalty cost for unmet demand or delays, representing the cost associated with failing to meet customer demand or k8 delivering late. 

- _xi_ : Binary decision variable indicating whether a hub is established at location _i_ ( _xi_ = 1) or not ( _xi_ = 0). 

- _yij_ : Continuous decision variable representing the amount of demand from point _j_ that is served by hub _i_ . 

- • _z_<sup>_k_</sup> _i_<sup>:Binarydecisionvariableindicatingwhetherhub</sup><sup>_i_</sup> operates at capacity level _k_ ( _z_<sup>_k_</sup> _i_<sup>= 1) or not (</sup><sup>_z_</sup> _i_<sup>_k_= 0).</sup> 

### _B. OBJECTIVE FUNCTION_ 

The objective is to minimize the total costs, which include the fixed costs of establishing hubs, the variable transportation costs, and the penalties for unmet demand. The objective function is defined as follows: 



<!-- Start of picture text -->
min  fixi  + � � cijyij  +  p � dj  − � yij<br> � i ∈ I i ∈ I j ∈ J j ∈ J � i ∈ I �   (1)<br><!-- End of picture text -->

Here, the first term represents the fixed costs of establishing hubs, the second term covers the variable transportation costs, and the third term accounts for penalties due to unmet demand. 

### _C. CONSTRAINTS_ 

_Capacity Constraints:_ The total amount of goods handled by a hub cannot exceed its capacity at the chosen level. This is represented by the following constraint: 



<!-- Start of picture text -->
� yij ≤ � u k i zk i ∀ i  ∈ I (2)<br>j ∈ J k ∈ K<br><!-- End of picture text -->

### 1) DEMAND FULFILLMENT 

The model ensures that the demand at each point _j_ is met by the hubs, either partially or fully: 



<!-- Start of picture text -->
� yij =  dj ∀ j  ∈ J (3)<br>i ∈ I<br><!-- End of picture text -->

### 2) HUB ESTABLISHMENT AND CAPACITY LEVELS 

A hub can only operate at one capacity level if it is established. This is modeled by the following constraint: 



<!-- Start of picture text -->
� z k i =  xi ∀ i  ∈ Ik 8 (4)<br>k ∈ K<br><!-- End of picture text -->

### 3) BINARY AND NON-NEGATIVITY CONSTRAINTS 

The decision variables _xi_ and _z_<sup>_k_</sup> _i_ are binary, indicating the presence or absence of a hub and its capacity level, 

respectively. The flow variables _yij_ must be non-negative: 



<!-- Start of picture text -->
xi, z k i ∈{0 ,  1} , yij ≥ 0 ∀ i  ∈ I , j  ∈ J , k ∈ K (5)<br><!-- End of picture text -->

These constraints collectively ensure that the model accurately reflects the real-world limitations and requirements of e-commerce distribution networks, providing a comprehensive tool for optimizing hub locations and operations. 

### _D. VALID INEQUALITIES_ 

In the optimization of the Hub Location Problem (HLP), valid inequalities play a crucial role in tightening the mathematical model. These constraints help eliminate non-optimal and fractional solutions, thus improving the efficiency of solving the problem. Below are some of the key types of valid inequalities commonly used in HLP formulations: 

- **Capacity Constraints:** Ensure that the total demand assigned to a hub does not exceed its capacity: 



<!-- Start of picture text -->
� yij ≤ � u k i zk i ∀ i  ∈ I (6)<br>j ∈ J k ∈ K<br><!-- End of picture text -->

This constraint ensures that the sum of demands _yij_ served by hub _i_ does not surpass the total capacity _u_<sup>_k_</sup> _i_ available at the hub’s operational level _k_ . 

- **Flow Conservation Inequalities:** These inequalities guarantee that the amount of flow into and out of the hubs and demand points matches the supply and demand: 



<!-- Start of picture text -->
� yij =  dj ∀ j  ∈ J (7)<br>i ∈ I<br><!-- End of picture text -->

This constraint ensures that the total flow _yij_ from all hubs to a demand point _j_ meets the demand _dj_ at that point. 

- **Hub Activation Constraints:** These constraints link the use of a hub to its activation, ensuring that demand is routed only through active hubs: 



<!-- Start of picture text -->
yij ≤ djxi ∀ i  ∈ I , j  ∈ J (8)<br><!-- End of picture text -->

Here, _xi_ is a binary variable indicating whether hub _i_ is active ( _xi_ = 1) or not ( _xi_ = 0). This inequality ensures that demand _dj_ can only be served if the corresponding hub _i_ is active. 

- **Allocation Constraints:** These can ensure that each demand point is served by only one hub, particularly in single-allocation problems: 



<!-- Start of picture text -->
� xi = 1 ∀ j  ∈ J (9)<br>i ∈ I<br><!-- End of picture text -->

This constraint guarantees that each demand point _j_ is assigned to exactly one hub _i_ . 

- **Demand Splitting Inequalities:** In cases where demand splitting across multiple hubs is allowed, valid inequalities can limit excessive splitting: 



<!-- Start of picture text -->
yij ≥ ϵxi ∀ i  ∈ I , j  ∈ J (10)<br><!-- End of picture text -->

55919 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



where _ϵ_ is a small positive constant, ensuring that if a hub serves a demand point, a minimum amount of demand is allocated to it. 

These valid inequalities not only help in reducing the solution space but also improve the solver’s efficiency by providing a more structured and constrained optimization problem. They are essential in ensuring that the model aligns closely with practical considerations such as capacity limits and demand satisfaction. 

### **VII. SOLUTION APPROACH** 

The solution approach integrates matheuristic techniques with Random Forest, a machine learning method known for its robustness in prediction and classification tasks. This hybrid method combines the strengths of both approaches, enhancing decision-making in the Hub Location Problem (HLP) for e-commerce logistics. Random Forest is particularly well-suited for this problem due to its ability to handle high-dimensional and non-linear relationships in demand forecasting, ensuring more accurate hub placement decisions. Compared to alternative machine learning models such as Support Vector Machines (SVM) and Neural Networks (NN), Random Forest offers high interpretability, lower sensitivity to hyperparameter tuning, and resilience against overfitting due to its ensemble nature. Additionally, its efficiency in handling large datasets without extensive feature engineering makes it an ideal choice for real-world logistics applications. Empirical results demonstrate that the incorporation of Random Forest improves the predictive accuracy by X % compared to traditional statistical methods, leading to better demand forecasting and cost-effective allocation of the hub. Future work could explore hybrid models that combine tree-based methods with deep learning for enhanced predictive power in dynamic logistics environments. 

### _A. MATHEURISTIC COMPONENT_ 

Matheuristics are a blend of mathematical programming and heuristic methods, designed to achieve high-quality solutions within reasonable computational times [19], [20]. For the HLP, we employ a matheuristic that leverages Mixed-Integer Linear Programming (MILP) to solve smaller, tractable subproblems to optimality, while heuristics like Variable Neighborhood Search (VNS) are used to explore larger, more complex solution spaces [21], [22]. 

MILP provides a strong framework for obtaining exact solutions to the HLP, particularly when dealing with capacity constraints and complex cost structures [23]. However, due to the problem’s NP-hard nature, solving large instances requires heuristic methods to navigate the solution space effectively and efficiently. 

### _B. RANDOM FOREST INTEGRATION_ 

Random Forest, a powerful ensemble learning method, is integrated into the matheuristic framework to enhance decision-making. This integration occurs in several key areas: 

- **Demand Prediction:** The Random Forest model is trained on historical sales and demand data to predict future demand at various locations [24], [25]. Accurate demand forecasting is crucial for determining the appropriate hub capacities and allocations, ensuring that hubs are neither underutilized nor overwhelmed. 

- **Parameter Tuning:** The model assists in tuning the parameters of the matheuristic, such as determining the thresholds for opening new hubs or expanding existing ones. This is achieved by analyzing historical data and simulated scenarios [26], [27]. 

- **Scenario Analysis:** By simulating various demand scenarios, the Random Forest helps assess the impact of uncertainty and variability in demand, thereby enhancing the robustness of the solution [28], [29]. 

### _C. ALGORITHMIC FRAMEWORK_ 

The combined matheuristic and Random Forest approach involves a structured sequence of steps designed to optimize hub locations in e-commerce logistics. The following steps detail the process (Figure 1): 



**FIGURE 1.** Flowchart of the proposed framework. 

55920 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



- 1) **Data Collection and Preprocessing:** The first step involves collecting comprehensive data on various aspects critical to the Hub Location Problem (HLP). This includes: 

   - **Demand Patterns:** Historical sales data, seasonality trends, and daily transaction records. 

   - **Transportation Costs:** Detailed records of costs associated with transporting goods between hubs and customer locations, including fuel, labor, and maintenance expenses. 

   - **Potential Hub Locations:** Geographic data on potential hub sites, including their physical capacity, accessibility, and proximity to major demand centers. 

   - The collected data is then preprocessed to remove any anomalies, inconsistencies, and missing values to ensure the dataset is clean and reliable for further analysis [24]. Techniques such as normalization and standardization are applied to bring all data to a common scale, facilitating accurate and efficient processing. 

- 2) **Initial Solution Generation:** Using Mixed-Integer Linear Programming (MILP), a relaxed version of the HLP is solved to generate an initial solution. This step provides a baseline by identifying a feasible set of hub locations and their respective allocations that minimize the overall costs. The MILP model incorporates constraints related to hub capacities, transportation costs, and service levels [23]. This initial solution serves as a starting point for further refinement through heuristic methods. 

- 3) **Heuristic Improvement:** To enhance the initial solution, heuristic methods such as Variable Neighborhood Search (VNS) are applied. VNS systematically explores the neighborhood of the current solution by making small, iterative changes, searching for better alternatives. This step helps in overcoming local optima and finding more cost-effective and efficient hub configurations [21]. The iterative nature of VNS allows it to adaptively focus on promising regions of the solution space, improving the overall quality of the solution. 

- 4) **Demand Prediction with Random Forest:** A Random Forest model is trained on the historical demand data to forecast future demand across different customer locations. This machine learning technique uses an ensemble of decision trees to improve prediction accuracy and robustness [24]. The predicted demand values are then used to adjust the hub locations and capacities dynamically, ensuring that the hub network remains responsive to varying demand patterns. Hyperparameter tuning and cross-validation are employed to optimize the Random Forest model, enhancing its predictive performance. 

- 5) **Integration and Adjustment:** The demand forecasts generated by the Random Forest model are integrated 

   - into the matheuristic framework. This step involves iteratively refining the solution by re-optimizing the hub locations and allocations based on updated demand predictions [29]. The matheuristic approach leverages both exact optimization methods and heuristics to balance computational efficiency with solution quality. This integration ensures that the hub network can adapt to changes in demand and other uncertainties, maintaining high levels of service and cost efficiency. 

- 6) **Final Solution Validation:** The final solution is validated against a series of test scenarios designed to assess its robustness and efficiency. These scenarios simulate various real-world conditions, such as peak demand periods, sudden demand spikes, and disruptions in transportation routes [26]. Performance metrics such as total operational costs, service levels, and computational time are evaluated to ensure the solution meets the desired objectives. Sensitivity analysis is also conducted to understand the impact of different parameters on the solution’s performance, providing insights for further improvements. 

### **VIII. DATASET AND EXPERIMENTAL FRAMEWORK** 

The experimental results presented in this section are based on extensive simulations using a dataset from a major e-commerce platform. The dataset utilized in this study was obtained from a real-life logistics and supply chain industry setting. Specifically, it includes operational data from a leading global transportation company, capturing real-world complexities such as varying customer demands, geographical constraints, and dynamic routing requirements. This industry-sourced dataset ensures the applicability of the proposed methodology to practical scenarios, enhancing its relevance for addressing real-world challenges. The dataset includes information on customer locations, historical demand patterns, and transportation costs. The experiments were designed to evaluate the effectiveness of the proposed matheuristic combined with Random Forest in optimizing hub locations and managing logistical complexities. 

### _A. DATASET DESCRIPTION_ 

The dataset encompasses a large geographical area with thousands of customer locations and multiple potential hub sites. It includes: 

- **Customer Demand Data:** Historical data covering a period of two years, capturing seasonal variations and peak demand periods [30], [31]. 

- **Transportation Costs:** Variable costs associated with transporting goods between hubs and customer locations, including factors such as distance, fuel costs, and labor [32], [33]. 

- **Hub Capacity Information:** Data on the capacity constraints of potential hubs, considering both physical storage and processing capabilities [34], [35]. 

55921 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



### _B. METHODOLOGY_ 

The experiments were conducted using the combined matheuristic and Random Forest approach. The methodology involved: 

- 1) **Initial Setup:** Preprocessing the dataset to ensure data quality and consistency. 

- 2) **Model Training and Validation:** Training the Random Forest model on a subset of the data to predict future demand patterns [24], [36]. 

- 3) **Optimization Process:** Applying the matheuristic to determine optimal hub locations, considering predicted demand and cost factors [19], [20]. 

- 4) **Scenario Analysis:** Conducting scenario analyses to test the robustness of the hub network under different demand conditions [28], [29]. 

### **IX. PERFORMANCE EVALUATION** 

In this section, we evaluate the performance of our solution compared to traditional methods while mentioning the limitations of our study. 

model’s robustness and suitability for addressing the dynamic challenges of e-commerce logistics. 



**FIGURE 2.** Delivery time compliance across different demand scenarios. 

### _B. SCALABILITY STUDY_ 

### _A. SERVICE LEVEL ANALYSIS_ 

Service level analysis is a critical component in evaluating the effectiveness of the proposed hub network model. The analysis focuses on key metrics such as Delivery Time Compliance ( _Tc_ ), Fulfillment Rate ( _Fr_ ), and Network Robustness ( _Rn_ ). These metrics ensure the network meets delivery time constraints, satisfies customer demand, and maintains resilience under uncertainties. 

- **Delivery Time Compliance:** it evaluates the network’s ability to deliver orders within predefined time limits. The proposed model aims to minimize _Tc_ deviations by optimizing hub locations and routing. Experiments showed an average _Tc_ of 92.3%, with variations depending on demand levels. 

- **Fulfillment Rate:** it represents the percentage of customer orders satisfied within the network’s constraints. The proposed model achieved an average _Fr_ of 97.6%, significantly higher than traditional models, particularly under peak demand scenarios. This performance underscores the model’s ability to allocate demand effectively across hubs. 

- **Network Robustness:** it quantifies the system’s resilience to disruptions, such as fluctuating hub capacities or transportation delays. Using robust optimization techniques, the proposed model maintained a high _Rn_ of 0.87, outperforming traditional approaches and demonstrating effective risk mitigation strategies. 

Table 1 summarizes the comparative performance of the proposed model versus traditional hub location approaches. Furthermore, Figure 2 shows the delivery time compliance across varying demand scenarios. In summary, the proposed hub network model demonstrates its capability to meet service level requirements efficiently, outperforming traditional models in key metrics. The results highlight the 

The current study evaluates the proposed hub location model using a network configuration of _N_ nodes, representing both potential hub locations and customer demands, with _M_ decision variables corresponding to the binary selection of hubs, demand allocations, and associated routing constraints. The dimensionality of the decision variables grows as ( _N_<sup>2</sup> + _N_ ), where _N_ scales with the number of nodes in the logistics network. This formulation ensures a robust representation of real-world distribution challenges, capturing demand variability, capacity constraints, and service level requirements. 

To assess scalability, the model was tested on networks ranging from 50 to 500 nodes. Computational experiments demonstrate that the proposed algorithm efficiently handles networks with up to 300 nodes within reasonable time limits, achieving near-optimal solutions for larger systems with up to 500 nodes. The computational performance was achieved through a combination of advanced optimization techniques, including variable neighborhood search (VNS) and metaheuristics, which adapt dynamically to the problem’s size and complexity. 

### _C. COMPARATIVE ADVANTAGES OVER TRADITIONAL METHODS_ 

The superiority of the proposed model lies in its ability to incorporate real-world complexities such as demand variability, hybrid hub configurations (centralized and distributed hubs), and robust optimization techniques for managing disruptions. Compared to traditional linear optimization models, the proposed approach excels in the following areas: 

- **Dynamic Adaptability:** Traditional methods often struggle with fluctuating demand and the need for rapid response. The integration of machine learning for demand forecasting and real-time optimization enables 

55922 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



**TABLE 1.** Summary of service level metrics. 



the proposed model to dynamically adjust to changes in the system. 

- **Scalability:** While conventional methods face significant computational overhead as network size increases, the proposed metaheuristic-driven algorithm maintains efficiency, leveraging parallel computing and intelligent neighborhood search techniques to explore the solution space effectively. Empirical results demonstrate that the algorithm achieves near-optimal solutions for networks up to 500 nodes while maintaining competitive computational time. Moreover, the integration of machine learning allows dynamic adaptation to changing demand, reducing unnecessary recomputations. Future enhancements could explore GPU-accelerated computing, distributed optimization techniques, and adaptive heuristics to further improve scalability for networks exceeding 1000 nodes. 

- **Solution Quality:** The hybrid nature of the algorithm combines global search capabilities with local refinement, yielding solutions that consistently outperform traditional methods in terms of cost minimization and service level adherence. Comparative analysis with benchmarks shows an average improvement of 15–20% in operational cost reduction. The synergy between metaheuristic optimization and machine learning enables more adaptive and context-aware decisionmaking, reducing inefficiencies in hub allocation and transportation planning. Sensitivity analysis further confirms the robustness of the proposed approach, demonstrating its ability to maintain high-quality solutions under varying demand scenarios. Future research could explore reinforcement learning or multi-objective optimization techniques to further enhance solution quality and balance trade-offs between cost, efficiency, and environmental impact. 

- **Resilience:** By incorporating robust optimization techniques, the proposed model accounts for uncertainties such as demand surges and supply chain disruptions, which traditional methods often neglect. 

The findings underline the model’s capability to provide scalable and high-quality solutions for large-scale e-commerce logistics networks. Future work will further explore its application to networks exceeding 1000 nodes and investigate additional heuristic enhancements to optimize computational efficiency. 

### _D. TEMPORAL EFFECTS STUDY_ 

One of the critical challenges in hub location optimization is accounting for temporal fluctuations, such as varying 

hub capacities and changing demand levels over time. In the proposed model, temporal effects are addressed by incorporating dynamic constraints and parameters that reflect real-world variability. 

### 1) DYNAMIC HUB CAPACITIES 

The model includes time-dependent capacity constraints ( _u_<sup>_k_</sup> _i_<sup>(</sup><sup>_t_)) to account for fluctuations in hub performance. These</sup> constraints are formulated as: 



<!-- Start of picture text -->
� yij ( t ) ≤ ui k ( t ) , ∀ i, t<br>j<br><!-- End of picture text -->

where _yij_ ( _t_ ) represents the allocation of demand from node _j_ to hub _i_ at time _t_ , and _u_<sup>_k_</sup> _i_<sup>(</sup><sup>_t_) denotes the available capacity of</sup> hub _i_ at time _t_ . This approach ensures that the optimization respects temporal capacity variations, such as increased storage needs during peak seasons. 

### 2) COST VARIABILITY 

To capture temporal variations in operational costs, the model introduces a time-dependent cost parameter ( _cij_ ( _t_ )). These costs are adjusted based on factors such as seasonal fuel price changes or demand shifts, enhancing the realism of the optimization framework. 

### 3) SCENARIO-BASED ROBUST OPTIMIZATION 

To further address temporal effects, the model employs a scenario-based robust optimization approach. Multiple scenarios ( _s_ ) are generated, each representing different temporal conditions (e.g., peak demand, low demand, or disrupted supply chains). The optimization objective minimizes the worst-case performance across all scenarios: 



<!-- Start of picture text -->
min max Total Cost( s ) + Penalty for Unmet Demand( s )<br>s � �<br><!-- End of picture text -->

This ensures that the solution remains effective under a range of temporal conditions, providing robustness against uncertainties. 

### 4) SIMULATION OF TEMPORAL DYNAMICS 

The model’s performance is evaluated using a simulation framework that captures temporal dynamics over multiple time periods. This allows for the assessment of key performance metrics, such as average delivery time, total costs, and service level compliance, under varying conditions. 

By incorporating these temporal considerations, the proposed model extends beyond static optimization, offering a more practical and adaptable solution for real-world hub location challenges in e-commerce logistics. 

55923 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



### _E. LIMITATIONS OF THE STUDY_ 

The study, while utilizing real-life industry data, has several limitations that warrant acknowledgment. The dataset reflects characteristics specific to a particular sector, which may limit the generalizability of the findings to other industries with differing operational dynamics. Moreover, the scalability of the proposed model to larger datasets or more complex scenarios has not been extensively tested, potentially impacting its applicability in diverse industrial contexts. The data also represents a snapshot of operational conditions during the collection period, without accounting for temporal changes or evolving industry practices that might influence the model’s long-term relevance. Additionally, the computational constraints during model development and training could affect the feasibility of its deployment in resource-limited environments. While the study focuses on Random Forest integration, alternative machine learning algorithms and ensemble approaches were not deeply explored, which might limit the discovery of potential performance gains. Furthermore, the study evaluates the algorithm’s performance in an offline setting, leaving real-time deployment in dynamic industrial environments unexplored. Lastly, certain assumptions regarding data quality and feature independence might introduce biases or dependencies that could impact the model’s robustness. Addressing these limitations in future research could enhance the model’s applicability, scalability, and relevance across diverse industrial contexts. 

### **X. CONCLUSION** 

This study presents a comprehensive approach to optimizing hub locations in e-commerce distribution networks by integrating matheuristics with Random Forest machine learning techniques. The proposed method demonstrates substantial improvements over traditional heuristic methods in several key areas. Firstly, the enhanced cost efficiency is achieved through the integration of advanced demand forecasting, which significantly improves the accuracy of demand predictions. This leads to more precise resource allocation and a reduction in operational costs, particularly in transportation and hub operations. 

Secondly, the method improves service levels, including higher on-time delivery rates and increased order accuracy. These improvements are crucial for maintaining customer satisfaction in the competitive e-commerce landscape, where quick and accurate deliveries are vital. Thirdly, the approach increases computational efficiency, combining the strengths of matheuristics and machine learning to achieve faster convergence and reduced computation time. This efficiency is particularly beneficial for large-scale logistics networks, allowing for quicker and more reliable decision-making. 

Additionally, the study highlights strategic business benefits, as the dual focus on reducing costs and improving service quality offers significant strategic advantages. This approach aligns well with the goals of businesses aiming to enhance 

operational efficiency and customer satisfaction. Furthermore, the research points to potential future directions, including the exploration of other machine learning models and real-time data integration, which could further refine demand forecasting accuracy and system responsiveness. 

Overall, this research demonstrates that the synergy between optimization algorithms and predictive analytics can lead to significant improvements in the management of complex logistics systems. The proposed framework not only addresses current logistical challenges but also provides a foundation for ongoing innovation and adaptation in the field. 

Building on the findings of this study, future research could explore the integration of real-time data from IoT devices and advanced sensor networks to further enhance the responsiveness and accuracy of demand forecasting models. By leveraging IoT-enabled tracking and edge computing, logistics networks can achieve dynamic, real-time decisionmaking, reducing delays and inefficiencies. Additionally, investigating the application of other machine learning algorithms, such as deep learning (e.g., Long Short-Term Memory (LSTM) and Transformer-based models) and reinforcement learning, could provide deeper insights and potentially yield even more robust optimization strategies for adaptive hub location planning. 

Another promising avenue is the development of hybrid models that combine the strengths of multiple optimization techniques and predictive analytics, such as integrating metaheuristics with deep reinforcement learning for sequential decision-making in highly dynamic logistics environments. Moreover, explainable AI (XAI) techniques could be explored to improve model interpretability and transparency in automated logistics decision-making. 

Furthermore, incorporating sustainability metrics into the optimization framework would align with the growing emphasis on green logistics and corporate social responsibility. Future studies could assess the environmental impact of optimized hub locations by quantifying carbon footprints, fuel consumption, and energy efficiency improvements. Multi-objective optimization techniques that balance cost efficiency with environmental sustainability could lead to more eco-friendly supply chain solutions, promoting long-term resilience and regulatory compliance in e-commerce logistics. 

### **REFERENCES** 

- [1] M. Kahalimoghadam, R. G. Thompson, and A. Rajabifard, ‘‘Determining the number and location of micro-consolidation centres as a solution to growing e-commerce demand,’’ _J. Transp. Geography_ , vol. 117, May 2024, Art. no. 103875. 

- [2] S. Bhatnagar, A. Gupta, G. C. Prashant, P. S. Pandey, S. G. V. Manerkar, M. K. Vanteru, K. S. Yogi, R. S. M. L. Patibandla, and F. Khan, ‘‘Efficient logistics solutions for e-commerce using wireless sensor networks,’’ _IEEE Trans. Consum. Electron._ , vol. 70, no. 4, pp. 6838–6845, Nov. 2024. 

- [3] M. O’Kelly, ‘‘The location of interacting hub facilities,’’ _Transp. Sci._ , vol. 20, no. 2, pp. 92–106, 1986. 

- [4] J. Campbell, A. Ernst, and M. Krishnamoorthy, ‘‘Hub location problems,’’ in _Facility Location: Applications and Theory_ . Berlin, Germany: Springer, 2002, pp. 373–407. 

55924 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



- [5] Z. Shen, R. Zhan, and J. Zhang, ‘‘The reliable facility location problem: Formulations, heuristics, and approximation algorithms,’’ _INFORMS J. Comput._ , vol. 23, no. 3, pp. 470–482, 2011. 

- [6] T. Sim, T. J. Lowe, and B. W. Thomas, ‘‘The stochastic -hub center problem with service-level constraints,’’ _Comput. Oper. Res._ , vol. 36, no. 12, pp. 3166–3177, Dec. 2009. 

- [7] A. T. Ernst and M. Krishnamoorthy, ‘‘Efficient algorithms for the uncapacitated single allocation p-hub median problem,’’ _Location Sci._ , vol. 4, no. 3, pp. 139–154, Oct. 1996. 

- [8] M. Mohammadi, R. Tavakkoli-Moghaddam, A. Siadat, and J.-Y. Dantan, ‘‘Design of a reliable logistics network with hub disruption under uncertainty,’’ _Appl. Math. Model._ , vol. 40, nos. 9–10, pp. 5621–5642, May 2016. 

- [9] K. Danach, S. Gelareh, and R. Neamatian Monemi, ‘‘The capacitated single-allocation p-hub location routing problem: A Lagrangian relaxation and a hyper-heuristic approach,’’ _EURO J. Transp. Logistics_ , vol. 8, no. 5, pp. 597–631, Dec. 2019. 

- [10] Z. Shorabi, B. Rostami, and M. Ahmadi, ‘‘Uncapacitated single-allocation hub location problem: Formulation and exact solution approaches,’’ _Computers & Industrial Engineering_ , vol. 99, pp. 45–57, Jun. 2016. 

   - [31] E. B. Tirkolaee, I. Mahdavi, M. Esfahani, G.-W. Weber, A. Goli, and J. Zhang, ‘‘Developing an integrated approach based on machine learning and optimization for solving the dynamic green vehicle routing problem with multiple time windows,’’ _Neural Comput. Appl._ , vol. 32, no. 6, pp. 1751–1768, 2020. 

   - [32] V. Agrawal and I. Bellos, ‘‘Location-based pricing and delivery cost: Implications for online retailers,’’ _Prod. Oper. Manage._ , vol. 26, no. 12, pp. 2235–2254, 2017. 

   - [33] J. Holguín-Veras, M. Jaller, and J. Wojtowicz, ‘‘Trade-offs in multicommodity free-flow networks with sustainable, revenue-generating arc capacities,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 48, no. 2, pp. 442–462, 2012. 

   - [34] C.-C. Lin, J.-C. Lee, A. Yadav, and M.-C. Shih, ‘‘Hub network design in freight transportation: A review and synthesis,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 48, no. 4, pp. 842–868, 2012. 

   - [35] M. Wen, J. Wang, and D. Zhang, ‘‘Hub network design under uncertainty: A review,’’ _Transp. Res. E, Logistics Transp. Rev._ , vol. 95, pp. 4–18, 2017. 

   - [36] J. Zhu and J. Wang, ‘‘Machine learning applications in load forecasting,’’ in _Proc. IEEE Power Energy Soc. Gen. Meeting_ , Jul. 2015, pp. 1–5. 

- [11] A. Goldman, ‘‘Optimal locations for centers in a network,’’ _Transp. Sci._ , vol. 3, no. 4, pp. 352–360, 1969. 

- [12] M. K. Lim, A. Bassamboo, S. Chopra, and M. S. Daskin, ‘‘Facility location decisions with random disruptions and imperfect estimation,’’ _Manuf. Service Oper. Manage._ , vol. 15, no. 2, pp. 239–249, May 2013. 

- [13] H. B. Oztemel and A. Taskin, ‘‘A constrained clustering and deep learning integrated solution with density based anomaly detectors for artisancourier model in e-commerce logistics,’’ _SSRN_ , vol. 1, no. 4, pp. 1–21, Apr. 2023. 

- [14] A. Jovanovic, N. Bacanin, L. Jovanovic, R. Dama¯sevi¯cius, M. Antonijevic, M. Zivkovic, J. Kaljevic, and M. Dobrojevic, ‘‘Performance evaluation of metaheuristics-tuned recurrent networks with VMD decomposition for Amazon sales prediction,’’ _Int. J. Data Sci. Anal._ , vol. 1, no. 11, pp. 1–19, Nov. 2024. 

- [15] M. Yue and S. Ma, ‘‘LSTM-based transformer for transfer passenger flow forecasting between transportation integrated hubs in urban agglomeration,’’ _Appl. Sci._ , vol. 13, no. 1, p. 637, Jan. 2023. 

- [16] Z. Zheng, Z. Wang, X. Yan, Y. Jin, S. Liu, and Q. Liu, ‘‘Federated graph neural networks with bipartite embedding for multi-objective facility location,’’ in _Proc. 5th Int. Conf. Data-driven Optim. Complex Syst. (DOCS)_ , Sep. 2023, pp. 1–8. 

- [17] M. Daskin, ‘‘Network and discrete location: Models, algorithms, and applications,’’ in _Wiley Series in Discrete Mathematics and Optimization_ . Oxford, U.K.: Taylor & Francis, 2005. 

- [18] S. Alumur and B. Kara, ‘‘Network hub location problems: The state of the art,’’ _Eur. J. Oper. Res._ , vol. 190, no. 1, pp. 1–21, 2008. 

- [19] C. Blum and A. Roli, _Hybrid Metaheuristics: Powerful Tools for Optimization_ . Heidelberg, Germany: Springer, 2011. 

- [20] G. Fonseca, N. Pierre, S. Pinson, and L.-M. Rousseau, _Matheuristics: Hybridizing Metaheuristics and Mathematical Programming_ . Heidelberg, Germany: Springer, 2016. 

- [21] P. Hansen, N. Mladenović, and D. Perez-Britos, _Variable Neighborhood Search_ , vol. 14. Heidelberg, Germany: Springer, 2010. 

- [22] E. L. Demeulemeester and W. S. Herroelen, _Project Scheduling: A Research Handbook_ . Heidelberg, Germany: Springer, 2000. 

- [23] M. Conforti, G. Cornuejols, and G. Zambelli, _Integer Programming_ . Heidelberg, Germany: Springer, 2014. 

- [24] L. Breiman, _Random Forests_ , vol. 45. Heidelberg, Germany: Springer, 2001. 

- [25] G. Louppe, L. Wehenkel, A. Sutera, and P. Geurts, ‘‘Understanding variable importances in forests of randomized trees,’’ in _Proc. Adv. Neural Inf. Process. Syst._ , vol. 26, 2013, pp. 431–439. 

- [26] J. Friedman, T. Hastie, and R. Tibshirani, _The Elements of Statistical Learning_ (Springer Series in Statistics). Heidelberg, Germany: Springer, 2001. 

- [27] Y. Liu, Q. Wang, C. Yang, and W. Liu, ‘‘Hyperparameter optimization: A review of algorithms and applications,’’ in _Proc. Int. Conf. Adv. Comput. Intell. Eng. (ICACIE)_ , 2019, pp. 320–329. 

- [28] G. Biau and E. Scornet, ‘‘Random forests and some of their applications,’’ _Statist. Surv._ , vol. 10, pp. 198–218, 2016. 

- [29] E. Scornet, G. Biau, and J.-P. Vert, ‘‘Consistency of random forests,’’ _Ann. Statist._ , vol. 43, no. 4, pp. 1716–1741, Aug. 2015. 

- [30] K.-L. Choy, H.-K. Lam, G. Ho, T.-D. Cheng, and C.-S. Lee, ‘‘A machine learning approach to big data analytics in manufacturing supply chains,’’ _Int. J. Adv. Manuf. Technol._ , vol. 81, no. 1, pp. 5–16, 2015. 

KASSEM DANACH (Member, IEEE) was born in Lebanon, in 1985. He received the Doctor of Philosophy (Ph.D.) degree in computer engineering from Ecole Centrale de Lille, France, in 2016. He embarked on his academic journey with a fervent passion for computer engineering. Throughout his career, he has amassed a wealth of experience. He has applied his expertise in data analytics, artificial intelligence, machine learning, deep learning, educational technology, and business analytics to various military and professional roles. His illustrious career includes roles, such as the Chairperson of the Information Technology and Management Systems Department, Faculty of Business Administration, Al Maaref University, Lebanon. He has made substantial contributions to the field of operational research and artificial intelligence, earning him prestigious awards, including the Best Paper Award at LCIS, in 2017, and AISD, in 2019, and active participation as a Team Member in the EU-funded SOCORRO Project, from 2019 to 2021. 

ABBAS RAMMAL received the Ph.D. degree in applied mathematics and data science. He has substantial experience and competence in the fields of statistics and data science, encompassing mathematical modeling, structural equation modeling, path analysis, inferential and descriptive statistics, deep learning, machine learning (supervised/unsupervised), variable selection, non-linear optimization, time series analysis, matrix analysis (source separation), data analysis (signal/image), simulation, and numerical analysis. 



IMAD MOUKADEM received the Doctor of Philosophy (Ph.D.) degree in computer science from the University of Teesside. He is an experienced Associate Professor with a demonstrated history of working in the higher education industry. He is skilled in negotiation, analytical skills, databases, and team building. Throughout his academic career, he has contributed significantly to the field of computer science through his research and teaching. His areas of expertise include software 



55925 

VOLUME 13, 2025 

K. Danach et al.: Advanced Optimization in E-Commerce Logistics 



engineering, database management, and artificial intelligence. He has published numerous articles in reputed journals and has presented his work at various international conferences. He is known for his strong analytical skills and his ability to solve complex problems. His ability to lead and build effective teams has been instrumental in the success of many collaborative projects. In addition to his technical skills, he excels in negotiation and has successfully mediated several academic and industry-related agreements. His leadership and team-building abilities have made him a respected figure among his peers and students alike. 

HASSAN HARB (Member, IEEE) received the Ph.D. degree in computer science from the Lebanese University, Lebanon, and the University of Franche-Comté, France, in 2016. He held postdoctoral positions in Ensta-Bretagne, Artois, and Paris-Saclay universities, from 2018 to 2022. Currently, he is an Assistant Professor with the American University of the Middle East, Kuwait. He has published more than 100 conference and journal papers. His research interests include sensor networks and the IoT, artificial intelligence, healthcare, and modular robotic systems. He served as a reviewer for a wide variety of IEEE, ACM, Elsevier, Wiley, and Springer journals. 

ABBASS NASSER (Senior Member, IEEE) received the M.Sc. degree in electronics from Lebanese University, in 2012, and the Ph.D. degree in digital communication from the Université de Bretagne Occidentale (UBO), France, in 2016. From 2012 to 2016, he was an Instructor with the Department of Computer Science, American University of Culture and Education, Lebanon. From 2017 to 2019, he was a Postdoctoral Researcher with ENSTA-Bretagne, France, where he has become a Research Fellow, since 2019. In October 2020, he was a Visiting Professor with Polytech-Nantes, France. In September 2021, he was a Visiting Researcher with LabSTICC—UBO, France. He is currently an Associate Professor with the Business Computing Department, USEK, Lebanon. He is the Supervisor and the Co-Director of several defended and in-progress Ph.D. projects. He has co-authored more than 60 research papers published in international journals and conferences. He serves as an editor and a reviewer for several international high-ranked journals. His current research interests include cognitive radio, the Internet of Things, wireless sensor networks, and intelligent reflecting surfaces. 

55926 

VOLUME 13, 2025 

