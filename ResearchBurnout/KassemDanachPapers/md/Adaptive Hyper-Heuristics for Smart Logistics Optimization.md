# **Adaptive Hyper-Heuristics for Smart Logistics Optimization** 



### **Kassem Danach, Hasan Fayyad-Kazan, Wissam Khalil, Samir Haddad, and Jinane Sayah** 

**Abstract** The complexity of logistics combinatorial optimization problems including vehicle routing, warehouse scheduling, and dynamic delivery has increased because of rising demand and evolving constraints. Metaheuristics show effectiveness but need problem-specific tuning and demonstrate limited general applicability. This research presents a learning-based hyper-heuristic framework which operates at high abstraction levels to select or generate low-level heuristics through dynamic decision-making based on problem features and real-time performance feedback. The proposed system uses reinforcement learning to select heuristics while pursuing adaptability, scalability and domain independence. Additionally, the framework demonstrates its effectiveness through benchmark dataset experiments, which show better solution quality and improved computational efficiency and robustness compared to traditional metaheuristics. Moreover, the framework shows its capability to perform automated decision-making while minimizing human involvement and demonstrating effective adaptation to changing logistics environments. Finally, 

K. Danach (B) 

Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon e-mail: kassem.danach@mu.edu.lb 

H. Fayyad-Kazan 

Computer Science and Engineering Department, Kuwait College of Science and Technology, Kuwait City, Kuwait e-mail: h.kazan@kcst.edu.kw 

#### W. Khalil 

Faculty of Economics and Business Administration, Islamic University of Lebanon, Beirut, Lebanon e-mail: wissam.khalil@iul.edu.lb 

#### S. Haddad 

Department of Computer Science and Mathematics, Faculty of Arts and Sciences, University of Balamand, Koura, Lebanon e-mail: samir.haddad@balamand.edu.lb 

#### J. Sayah 

Department of Telecom and Networks, Issam Fares Faculty of Technology, University of Balamand, Koura, Lebanon e-mail: jinane.sayah@balamand.edu.lb 

© The Author(s) 2026 

M. Trabelsi et al. (eds.), _Proceedings of the 2nd Symposium on Smart, Sustainable, and Secure Internet of Things_ , Lecture Notes in Electrical Engineering 1513, https://doi.org/10.1007/978-981-95-5136-1_7 

65 

66 

K. Danach et al. 

this research presents an adaptable intelligent optimization system which enhances operational efficiency and resilience in smart supply chain systems. 

**Keywords** Hyper-heuristics · Combinatorial optimization · Smart logistics · Heuristic selection · Supply chain optimization 

## **1 Introduction** 

The core of many real-world decision-making scenarios in logistics depends on combinatorial optimization problems because they require efficient routing, scheduling and resource allocation [1]. The implementation of smart logistics systems using Industry 4.0 technology and the Internet of Things (IoT) has led to substantial growth in problem complexity, which exceeds traditional optimization methods’ capabilities [2]. The optimization challenges are addressed through the use of metaheuristics, which include Genetic Algorithms (GA), Ant Colony Optimization (ACO) and Simulated Annealing (SA) [3]. Unfortunately, these methods need problem-specific tuning and lack broad applicability to different problem instances. Hyper-heuristics function at a higher level of abstraction because they select or generate low-level heuristics dynamically while avoiding domain-specific customization [4]. This research presents a learning-based hyper-heuristic system which addresses multiple logisticsrelated combinatorial problems through vehicle routing, warehouse scheduling, and dynamic delivery planning. Real-time feedback integration with reinforcement learning strategies enables the framework to select heuristics dynamically, which results in improved adaptability and scalability and enhanced decision quality in dynamic logistics environments. 

## **2 Related Work** 

The complexity of combinatorial optimization challenges in smart logistics systems continues to rise while metaheuristics and hyper-heuristic methods emerge as successful solution approaches. Metaheuristics such as Genetic Algorithms (GA), Simulated Annealing (SA), Particle Swarm Optimization (PSO) and Ant Colony Optimization (ACO) demonstrate effectiveness in solving the Vehicle Routing Problem (VRP), Job Shop Scheduling Problem (JSSP), and warehouse operations [3]. 

Hyper-heuristics emerged as a solution to overcome these limitations through higher-level abstraction techniques, which enable automatic low-level heuristic selection or generation during the search process [4]. These approaches focus on developing problem-independent solutions which need minimal human intervention, provide enhanced flexibility and improved generalizability. Research has 

67 

Adaptive Hyper-Heuristics for Smart Logistics Optimization 

recently investigated the application of reinforcement learning (RL) and deep learning as components of intelligent hyper-heuristics specifically designed for logistics optimization. 

Hyper-heuristics consist of two main categories, which include heuristic selection and heuristic generation, according to [5, 6]. The first approach chooses heuristics from an available set according to their performance, while the second approach generates heuristics dynamically through machine learning methods. The field of logistics has experienced explosive growth in hyper-heuristics applications [7] through several prominent frameworks. The applications include Deep Reinforcement Learning Hyper-Heuristics (DRLH), Q-learning with Clustering, Nested Markov Chain Hyper-Heuristics (NMHH) and Large Language Models (LLMs). 

The current generation of hyper-heuristics demonstrates strong potential, but they primarily work with benchmark problems while neglecting real-world logistics operations under time constraints. Our research closes this knowledge gap through a practical reinforcement learning-based hyper-heuristic system that ensures scalability and adaptability. 

## **3 Proposed Hyper-Heuristic Framework** 

The proposed hyper-heuristic framework is a general-purpose solution for combinatorial logistics problems that is robust, adaptive and designed to solve problems such as vehicle routing, warehouse scheduling and order fulfillment. It has two hierarchical levels: the high-level strategy (heuristic selection and acceptance mechanism) and the low-level heuristics (solution perturbation operators). This framework aims to separate problem-specific details from search control, and thus enable greater scalability and reusability across domains such as vehicle routing, warehouse scheduling and order fulfillment. 

## **_3.1 Low-Level Heuristics_** 

The proposed framework implements a range of low-level heuristics (LLHs), which function independently of specific problem domains to provide broad applicability across multiple logistics optimization challenges. The organized heuristics consist of two functional categories that include constructive operators, which create initial solutions through greedy insertion methods and perturbative operators, which enhance existing solutions. The perturbative operators consist of five essential techniques which include (1) Insertion for repositioning tasks or nodes to enhance solution feasibility (2) Swap for exchanging pairs of elements to discover new configurations (3) 2-opt as a specialized routing heuristic that reverses subsequences to minimize travel distance (4) Mutation for controlled randomization to escape local optima and (5) Greedy Repair for systematic solution component re-optimization. The heuristics 

68 

K. Danach et al. 

need only basic cost evaluation and feasibility checking functions to operate since they maintain minimal interaction with the problem domain, thus ensuring both computational efficiency and easy integration into different problem contexts. The framework design enables flexibility while delivering strong solution improvement abilities throughout various combinatorial optimization problems in logistics. 

## **_3.2 Heuristic Selection Method_** 

The high-level controller employs a reinforcement learning-based selection strategy. Specifically, a multi-armed bandit (MAB) approach is used where each low-level heuristic is treated as an “arm,” and selection is based on its historical performance (e.g., improvement rate, time efficiency). The selection probability . _Pi_ of heuristic . _hi_ is updated using the Upper Confidence Bound (UCB) algorithm shown in Eq. 1: 



<!-- Start of picture text -->
ln  N<br>. Pi = Ri +  C (1)<br>ni<br><!-- End of picture text -->

where . _Ri_ is the average reward, . _ni_ is the number of times . _hi_ has been applied, . _N_ is the total number of heuristic applications, and . _C_ is the exploration parameter. 

## **_3.3 Acceptance Criteria_** 

To balance exploration and exploitation, the framework utilizes an adaptive acceptance criterion: 

- **Improvement-based Acceptance** : Always accept a new solution if it improves the objective function. 

- **Simulated Annealing-based Acceptance** : If the new solution is worse, it is accepted with a probability . _p_ = _e_<sup>−</sup> _T_ , where . is the deterioration in solution quality and . _T_ is the current temperature, gradually reduced over time. 

- **Stagnation-based Diversification** : If no improvement is observed over a predefined number of iterations, a large mutation is introduced to diversify the search. 

## **_3.4 Upper Confidence Bound Heuristic Selection Strategy_** 

The framework uses the **Upper Confidence Bound (UCB)** algorithm to dynamically select low-level heuristics (LLHs). The framework treats each heuristic as an 

69 

Adaptive Hyper-Heuristics for Smart Logistics Optimization 

“arm” in a multi-armed bandit problem, which balances exploration (trying less-used heuristics) and exploitation (reusing high-performing ones). 

Each heuristic . _hi_ ∈ _H_ , where . _H_ is the pool of low-level heuristics, is treated as an arm in the bandit model. The UCB score for each heuristic is calculated using Eq. 2: 



<!-- Start of picture text -->
ln  N<br>. UC Bi = Ri +  C (2)<br>ni<br><!-- End of picture text -->

where: 

- . _Ri_ is the average reward obtained from applying heuristic . _hi_ , 

- . _ni_ is the number of times . _hi_ has been selected, 

- . _N_ is the total number of heuristic applications across all . _h_ ∈ _H_ , 

- . _C_ is the exploration parameter that controls the trade-off between exploration and exploitation. 

The reward . _Ri_ can be defined based on: 

- The relative improvement in objective function value. 

- The quality of the solution compared to the global or local best. 

- The computational efficiency (e.g., improvement per time unit). 

At each iteration, the heuristic with the highest UCB score is selected bas on Formula 3: 



<!-- Start of picture text -->
. h ∗ = arg max hi ∈ H (UC Bi ) (3)<br><!-- End of picture text -->

## **_3.5 Overall Workflow_** 

The overall workflow is outlined as follows: 

1. Generate an initial solution using a greedy or random constructive heuristic. 

2. While termination criteria are not met: 

   - (a) Select a low-level heuristic based on the UCB heuristic selection strategy. 

   - (b) Apply the selected heuristic to the current solution to generate a candidate solution. 

   - (c) Evaluate the candidate solution. 

   - (d) Accept or reject the candidate solution based on the acceptance criterion. 

   - (e) Update heuristic performance metrics. 

3. Return the best solution found. 

This flexible, intelligent framework allows for generalization across various logistics scenarios, offering a balance between solution quality and computational efficiency. 

K. Danach et al. 

70 

## **4 Experimental Setup** 

To evaluate the effectiveness and generalizability of the proposed hyper-heuristic framework, a series of computational experiments were conducted on wellestablished combinatorial optimization problems in logistics, including variants of the Vehicle Routing Problem (VRP) and Job Shop Scheduling Problem (JSSP). 

## **_4.1 Benchmark Datasets_** 

The experiments utilized publicly available and widely used benchmark datasets: 

- **Solomon’s VRPTW Instances** [8]: These datasets include customer locations with time windows, service durations, and vehicle capacities. 

- **Gehring & Homberger Extended VRPTW Instances** [9]: Large-scale versions of Solomon’s problems, featuring up to 1000 customers. 

- **OR-Library JSSP Instances** [10]: Standard scheduling datasets, including LA, FT, and ABZ problems, often used to test scheduling heuristics. 

Each dataset represents a different class of real-world logistics problems, ensuring diversity in problem complexity and scale. 

## **_4.2 Implementation Details_** 

The hyper-heuristic framework was implemented in Python 3.11 using NumPy and SciPy for numerical operations. A modular architecture was adopted to enable plugand-play of low-level heuristics and heuristic selection strategies. Each experiment was repeated 30 times with different random seeds to ensure statistical significance. The performance of the proposed framework was compared to classical metaheuristics such as Genetic Algorithm (GA), Ant Colony Optimization (ACO), and Simulated Annealing (SA). 

## **_4.3 Parameter Settings_** 

- **Max Iterations** : 10,000 

- **Population Size (for GA and ACO)** : 50 

- **Exploration Parameter (UCB)** : . _C_ = 2 

- **Initial Temperature (SA)** : 100, with exponential decay 

- **Stagnation Limit** : 500 iterations 

Adaptive Hyper-Heuristics for Smart Logistics Optimization 

71 

Parameter values were selected based on preliminary experiments and commonly accepted settings in the literature [4]. 

## **_4.4 Evaluation Metrics_** 

The following metrics were used to evaluate solution quality and computational efficiency: 

- **Total Cost / Objective Value** : Total travel distance (VRP), makespan (JSSP), or combined cost. 

- **Average Gap to Optimal / Best Known Solution** : Expressed as a percentage. 

- **Computational Time** : Execution time in seconds. 

- **Stability** : Standard deviation of solution quality over multiple runs. 

Statistical tests (e.g., paired t-test and Wilcoxon signed-rank test) were used to compare results and validate improvements. 

## **_4.5 Algorithmic Complexity and Scalability_** 

The proposed hyper-heuristic framework exhibits a modular and efficient architecture designed to support scalability across large-scale logistics optimization problems. The overall time complexity per iteration can be decomposed into three principal components: 

- **Low-level heuristic application** : Each heuristic (e.g., 2-opt, swap) has a complexity that depends on the problem structure. For instance, 2-opt has a complexity of . _O(n_<sup>2</sup> _)_ in routing problems, where . _n_ is the number of nodes or tasks. 

- **Heuristic selection via UCB** : The selection of the best-performing heuristic using the Upper Confidence Bound (UCB) strategy involves computing a score for each of the. _k_ heuristics. This results in a selection time complexity of. _O(k)_ per iteration. 

- **Solution evaluation** : Evaluating the candidate solution (e.g., computing the cost, feasibility) typically requires . _O(n)_ to . _O(n_<sup>2</sup> _)_ operations, depending on whether the problem is routing, scheduling, or packing. 

Combining these components, the time complexity per iteration becomes as shown in Eq. 4: 



<!-- Start of picture text -->
. O( f (n)  +  k  +  e(n)) (4)<br><!-- End of picture text -->

where . _f (n)_ is the time to apply a heuristic, . _k_ is the number of available low-level heuristics, and . _e(n)_ is the cost of evaluating a solution. 

Assuming the algorithm runs for. _I_ iterations, the total worst-case runtime is shown in Eq. 5: 



<!-- Start of picture text -->
. O(I ·  ( f (n)  +  k  +  e(n))) (5)<br><!-- End of picture text -->

K. Danach et al. 

72 

**Table 1** Solution <u>quality: hyper-heuristic versus genetic algorithm</u> 

|Instance|GA (Avg)|HH (Avg)|Improvement (%)|
|---|---|---|---|
|C101 (VRPTW)|845.7|**798.2**|5.61|
|R201 (VRPTW)|1215.3|**1105.6**|9.02|
|LA16 (JSSP)|998.3|**942.8**|5.56|
|ABZ8 (JSSP)|820.5|**773.9**|5.67|



Bold represents results of our method 

## **5 Results and Discussion** 

The experimental findings of the proposed hyper-heuristic framework appear in this section against a classical Genetic Algorithm (GA), which functions as the performance evaluation baseline. The evaluation takes place across standard benchmark instances for vehicle routing and job shop scheduling. The same computational environment and termination criteria were applied to both methods. 

## **_5.1 Genetic Algorithm Implementation_** 

The hyper-heuristic framework demonstrated superior performance than the baseline Genetic Algorithm (GA) in all benchmark instances (VRPTW and JSSP). The main findings included: 

- 5–9% better solutions (e.g., 798.2 vs. 845.7 for C101 VRPTW) 

- Higher stability (lower standard deviation in repeated runs) 

- Generalized performance across problem types (routing/scheduling) 

The framework’s adaptive heuristic selection needed 10–15% longer runtime to outperform GA’s fixed operators but demonstrated better robustness especially in dynamic scenarios. (Data from Table 1, Sect. 5.2) 

## **_5.2 Solution Quality Comparison_** 

Table 1 shows the average objective values over 30 independent runs. The hyperheuristic outperformed GA in all test cases, achieving lower total cost or makespan with higher consistency. 

Adaptive Hyper-Heuristics for Smart Logistics Optimization 

73 

## **_5.3 Runtime and Stability_** 

While the hyper-heuristic required slightly longer average runtime per instance (by 10–15%), it exhibited more stable performance with lower standard deviation across repeated runs. The adaptive learning and dynamic acceptance strategy contributed to fewer premature convergences compared to GA. 

## **_5.4 Discussion_** 

The results demonstrate that the hyper-heuristic framework delivers substantial improvements above a well-configured GA system. The framework demonstrates better generalization capabilities through its autonomous heuristic selection and adaptation mechanism, which uses real-time feedback. The hyper-heuristic provides a scalable automated solution for real-world logistics environments because it adapts to dynamic problem characteristics better than GA with its domain-specific tuning. 

## **6 Sensitivity and Robustness Analysis** 

This section investigates how the exploration parameter . _C_ affects the hyperheuristic framework together with its performance across various problem instances. The exploration parameter . _C_ determines the equilibrium between exploration and exploitation in the UCB strategy. The graph in Fig. 1 how different . _C_ values affect the average objective value during 30 runs for the C101 instance. 



**Fig. 1** Sensitivity analysis: effect of UCB exploration parameter . _C_ 

K. Danach et al. 

74 

The results indicate that the best performance is achieved when . _C_ = 1 _._ 5, with an average objective value of 798.2 and the lowest standard deviation of 4.3. Smaller values of . _C_ result in insufficient exploration, while larger values lead to excessive exploration, degrading performance. 

## **_6.1 Robustness Across Instances_** 

Figure 2 shows the standard deviation of the objective value obtained by the hyperheuristic across four benchmark instances. Low variance across repeated runs indicates that the algorithm produces consistent results regardless of problem scale or type. 

The results confirm that the proposed framework maintains stable performance across both routing and scheduling problems. The average standard deviation ranged from 4.3 (C101) to 6.1 (LA16), highlighting its robustness in dynamic and stochastic environments. 

## **7 Conclusion and Future Work** 

The research introduced an innovative hyper-heuristic framework which solves complex combinatorial optimization problems in smart logistics systems. The proposed method gained high generality and adaptability toward different problem types including Vehicle Routing and Job Shop Scheduling through its abstraction of domain-specific heuristics. The framework used a learning-based heuristic selection 



**Fig. 2** Robustness analysis: standard deviation across benchmark instances 

75 

Adaptive Hyper-Heuristics for Smart Logistics Optimization 

strategy based on Upper Confidence Bound (UCB) to achieve effective exploration and exploitation balance. 

The experimental findings showed that the hyper-heuristic produced better solutions than a well-tuned Genetic Algorithm while demonstrating stable and robust performance. The exploration parameter sensitivity analysis confirmed its effect on search performance while robustness evaluation showed the framework maintained consistent results across various benchmark instances. 

The upcoming research will concentrate on developing the framework to manage real-time and stochastic logistics problems. Our future work includes developing multi-objective optimization functions and implementing deep reinforcement learning to generate adaptive heuristics in dynamic systems with uncertainty. 

## **References** 

1. Laporte G (2009) Fifty years of vehicle routing. Transp Sci 43(4):408–416 

2. Lu Y (2019) Industry 4.0: a survey on technologies, applications and open research issues. J Ind Inf Integr 6:1–10 

3. Blum C, Roli A (2003) Metaheuristics in combinatorial optimization: overview and conceptual comparison. ACM Comput Surv 35(3):268–308 

4. Burke EK, Gendreau M, Hyde M, Kendall G, Ochoa G, Ozcan E, Qu R (2013) Hyper-heuristics: a survey of the state of the art. J Oper Res Soc 64(12):1695–1724 

5. Danach K (2016) Hyperheuristics in logistics. Ph.D. Thesis, École Centrale de Lille 

6. Chakhlevitch K, Cowling P (2008) Hyperheuristics: recent developments. In: Cotta C, Sevaux M, Sörensen K (eds) Adaptive and multilevel metaheuristics, vol 136. Studies in computational intelligence. Springer, Berlin, Heidelberg, pp 3–29 

7. Danach K, El Dirani A, Rkein H (2024) Revolutionizing supply chain management with AI: a path to efficiency and sustainability. IEEE Access 

8. Solomon MM (1987) Algorithms for the vehicle routing and scheduling problems with time window constraints. Oper Res 35(2):254–265 

9. Homberger J, Gehring H (1999) A genetic algorithm for the capacitated vehicle routing problem with time windows. In: Proceedings of the 2nd metaheuristics international conference, vol 2, pp 1–8 

10. Beasley JE (1990) OR-library: distributing test problems by electronic mail. J Oper Res Soc 41(11):1069–1072 

76 

K. Danach et al. 

**Open Access** This chapter is licensed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license and indicate if changes were made. 

The images or other third party material in this chapter are included in the chapter’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the chapter’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. 

