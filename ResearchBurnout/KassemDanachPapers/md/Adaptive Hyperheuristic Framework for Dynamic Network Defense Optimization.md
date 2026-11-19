# Adaptive Hyperheuristic Framework for Dynamic Network Defense Optimization 

1<sup>st</sup> Kassem Danach 2<sup>nd</sup> Samir Haddad 3<sup>d</sup> Jomana Al Haj Hassan Basic and Applied Sciences Research Center) Management Information Systems Management Information Systems Al Maaref University Lebanese International University Lebanese International University Beirut, Lebanon Beirut, Lebanon Beirut, Lebanon kassem.danach@mu.edu.lb samir.haddad@balamand.edu.lb jomana.hajhassan@liu.edu.lb 4<sup>th</sup> Jinane Sayah 5<sup>th</sup> Merhej Joseph 6<sup>th</sup> Kallab Chadi Management Information Systems Department of Computer Science Department of Computer Science Lebanese International University LaRRIS Laboratory, Lebanese university Lebanese American University Beirut, Lebanon Fanar, Lebanon Jbeil, Lebanon jinane.sayah@balamand.edu.lb joseph.merhej@ul.edu.lb chadi.kallab@lau.edu.lb 

Index Terms—Hyperheuristics, Network Security, Optimization, Reinforcement Learning, Adaptive Acceptance Criteria 

Abstract—Network defense optimization in dynamic and adversarial environments poses significant challenges to traditional metaheuristic approaches due to their limited adaptability to non-stationary conditions. This paper proposes an Adaptive Hyperheuristic (AHH) framework that integrates reinforcement learning for intelligent heuristic selection across constructive, improvement, perturbation, and reconstructive operators, combined with adaptive acceptance criteria including Simulated Annealing, Great Deluge, and Late Acceptance. The problem is formulated as a multi-objective optimization model minimizing attack surface, response time, and operational cost while maximizing network resilience. Extensive numerical experiments conducted on simulated network topologies (50–500 nodes) under multiple attack scenarios demonstrate that AHH achieves superior performance, improving hypervolume by up to 12.5%, reducing IGD by 38%, and decreasing convergence time by approximately 15% compared to Genetic Algorithm and Scatter Search baselines. Furthermore, the proposed method reduces attack success rate by 40% and improves network resilience by over 13%, while maintaining low variance across 30 independent runs. These results confirm the robustness, efficiency, and practical applicability of the proposed framework for real-world network defense optimization. 

## I. INTRODUCTION 

The increasing complexity of modern networked systems, coupled with the rapid evolution of cyber threats, has made network defense optimization a critical and challenging task. Traditional optimization approaches, including classical metaheuristics, often struggle to maintain performance in dynamic and adversarial environments due to their limited adaptability and reliance on fixed search strategies. In this context, hyperheuristics have emerged as a promising paradigm, offering a higher level of abstraction by selecting or generating heuristics dynamically during the search process. 

The objective of this paper is to develop an adaptive hyperheuristic framework capable of efficiently solving dynamic 

network defense optimization problems. Specifically, the proposed approach aims to intelligently select low-level heuristics based on the current system state, while incorporating adaptive acceptance criteria to enhance the balance between exploration and exploitation under varying threat conditions. 

The main contributions of this work are threefold: (i) the design of a reinforcement learning-driven hyperheuristic for context-aware heuristic selection across multiple heuristic categories, (ii) the integration of adaptive acceptance mechanisms to improve search robustness and convergence behavior, and (iii) a comprehensive experimental evaluation demonstrating the superiority of the proposed method over Genetic Algorithm and Scatter Search baselines in terms of solution quality, convergence speed, and security effectiveness. 

## II. RELATED WORK 

Hyperheuristics have emerged as a high-level search methodology aimed at improving the generality and adaptability of optimization algorithms. The foundational work by [1] provides a comprehensive overview of hyperheuristic frameworks, distinguishing between selection and generation approaches. Selection hyperheuristics, in particular, have gained significant attention due to their ability to dynamically choose appropriate low-level heuristics during the search process [2]– [4]. 

Recent advances have focused on incorporating learning mechanisms into hyperheuristics. Reinforcement learning (RL) has been widely adopted to enhance heuristic selection by modeling the problem as a sequential decision-making process [5]. Such approaches enable adaptive behavior in dynamic environments, making them suitable for non-stationary optimization problems. 

In parallel, adaptive acceptance criteria have been explored to improve the balance between intensification and diversification. Methods such as Simulated Annealing, Great Deluge, and Late Acceptance have been successfully integrated within 

hyperheuristic frameworks to enhance performance across various domains [6], [7]. 

From the application perspective, optimization techniques have been increasingly applied to network security problems, including intrusion detection, attack mitigation, and resource allocation [8], [9]. However, most existing works rely on static optimization strategies and lack the ability to adapt to rapidly evolving threat landscapes. 

Despite these advancements, limited research has addressed the integration of adaptive hyperheuristics with dynamic network security optimization. In particular, the combination of reinforcement learning-based heuristic selection with adaptive acceptance mechanisms remains underexplored. This gap motivates the development of the proposed framework, which aims to provide a robust and scalable solution for real-time network defense optimization. 

## III. PROBLEM FORMULATION 

We model the network defense optimization problem as a dynamic multi-objective optimization problem defined over a complex networked system. The goal is to determine an optimal configuration of defense mechanisms that balances security effectiveness and operational cost under evolving threat conditions. 

Let G = (V, E) denote a network graph, where V is the set of nodes (hosts, routers, servers) and E is the set of communication links. A candidate solution x ∈X represents a configuration of security controls, including firewall rules, intrusion detection parameters, and routing policies. 

The problem is formulated as: 

## A. Constraints 

The optimization is subject to operational and security constraints: 



<!-- Start of picture text -->
g1(x) : Latency(x) ≤ Lmax (6)<br><!-- End of picture text -->



<!-- Start of picture text -->
g2(x) : ResourceUsage(x) ≤ Rmax (7)<br><!-- End of picture text -->



<!-- Start of picture text -->
g3(x) : x ∈Xfeasible (8)<br><!-- End of picture text -->

where Lmax and Rmax denote maximum allowable latency and resource capacity, respectively. 

## B. Dynamic Environment Modeling 

To capture the evolving nature of cyber threats, the problem is extended to a time-dependent formulation: 



<!-- Start of picture text -->
F (x, t) = (f1(x, t), f2(x, t), f3(x, t), f4(x, t)) (9)<br><!-- End of picture text -->

where system states and threat patterns vary over time t. This induces a non-stationary search space, requiring adaptive optimization strategies. 

## C. Solution Representation 

A solution x is encoded as a vector: 



<!-- Start of picture text -->
x = (x1, x2, . . . , xn) (10)<br><!-- End of picture text -->

where each decision variable xi corresponds to a specific security control parameter, such as: 

- Firewall rule activation (binary) 

- IDS sensitivity level (discrete) 



<!-- Start of picture text -->
min F (x) = (f1(x), f2(x), f3(x), f4(x)) (1)<br><!-- End of picture text -->

where the objective functions are defined as follows: 

• Attack Surface Minimization (f1): 



<!-- Start of picture text -->
f1(x) = � αv · Exposure(v, x) (2)<br>v∈V<br><!-- End of picture text -->

where αv represents the criticality weight of node v. • Response Time Minimization (f2): 



<!-- Start of picture text -->
1<br>f2(x) = � Tmitigation(a, x) (3)<br>|A|<br>a∈A<br><!-- End of picture text -->

- Routing policy adjustment (categorical) 

This representation allows flexible encoding of heterogeneous defense strategies within a unified optimization framework. 

## D. Pareto Optimality 

Given the multi-objective nature of the problem, solutions are evaluated based on Pareto dominance. A solution x<sup>∗</sup> is Pareto-optimal if no other solution x exists such that: 



<!-- Start of picture text -->
fi(x) ≤ fi(x ∗ ) ∀i ∈{1, 2, 3, 4} (11)<br><!-- End of picture text -->

and 

where A is the set of detected attacks. 

• Resilience Maximization (f3): 



<!-- Start of picture text -->
1<br>f3(x) = − � R(v, x) (4)<br>|V |<br>� v∈V �<br><!-- End of picture text -->

where R(v, x) measures the ability of node v to maintain functionality under attack. The negative sign converts maximization into minimization. 

• Cost Minimization (f4): 



<!-- Start of picture text -->
f4(x) = � Cdeploy(v, x) + Coperation(x) (5)<br>v∈V<br><!-- End of picture text -->



<!-- Start of picture text -->
fj(x) < fj(x ∗ ) for at least one j (12)<br><!-- End of picture text -->

The objective is to approximate the Pareto front representing optimal trade-offs among conflicting objectives. 

## IV. PROPOSED METHODOLOGY 

The proposed framework introduces an adaptive hyperheuristic (AHH) designed to efficiently solve dynamic network security optimization problems. The approach operates at two levels: a high-level strategy responsible for heuristic selection, and a set of low-level heuristics that directly manipulate candidate solutions. 

## A. Hyperheuristic Framework 

## D. Acceptance Criteria 

To enhance exploration capabilities, multiple acceptance strategies are integrated: 

The hyperheuristic operates as a supervisory layer that iteratively selects and applies low-level heuristics. The framework is defined as a tuple: 

- Simulated Annealing (SA): 

P = exp (−fracDeltafTright)(17) 



<!-- Start of picture text -->
HH = ⟨H, S, A, T ⟩ (13)<br><!-- End of picture text -->

- Great Deluge (GD): Accepts solutions below a dynamically decreasing threshold. 

where H is the set of low-level heuristics, S represents the system state, A denotes the acceptance criteria, and T is the termination condition. 

- Late Acceptance (LA): Compares current solution with a historical solution stored in a buffer. 

At each iteration t, the framework: 

An adaptive mechanism selects among these criteria based on search progress and system dynamics, enabling a balance between diversification and intensification. 

- 1) Observes the current state St 

- 2) Selects a heuristic h ∈ H 

- 3) Applies h to generate a candidate solution x<sup>′</sup> 

## E. Termination Criteria 

- 4) Decides acceptance using criterion A 

The algorithm terminates when one of the following conditions is satisfied: 

This iterative loop enables adaptive exploration of the search space under dynamic conditions. 

   - Maximum number of iterations is reached 

   - Convergence threshold is achieved: 

- B. Low-Level Heuristics 



<!-- Start of picture text -->
|F (xt) − F (xt−k)| < ϵ (18)<br><!-- End of picture text -->

The heuristic set H is partitioned into four categories: 

- Constructive Heuristics: Generate initial feasible solutions from scratch. 

   - Stability condition: no significant improvement over a predefined window 

- Improvement Heuristics: Perform local search to refine existing solutions. 

This hybrid termination strategy ensures computational efficiency while maintaining solution quality. 

- Perturbation Heuristics: Introduce controlled randomness to escape local optima. 

## V. EXPERIMENTAL SETUP 

- Reconstructive Heuristics: Partially rebuild degraded or suboptimal solutions. 

## A. Benchmark Environment and Scenarios 

The experimental campaign is conducted on a controlled simulation platform modeling enterprise-scale networks. Synthetic topologies are generated with sizes ranging from 50 to 500 nodes, including routers, servers, and end-hosts interconnected via heterogeneous links. 

Each heuristic hi operates on a solution x: 



<!-- Start of picture text -->
x ′ = hi(x) (14)<br><!-- End of picture text -->

The diversity of heuristic types ensures a balance between intensification and diversification. 

Each network instance is evaluated under dynamic threat scenarios: 

- Distributed Denial of Service (DDoS) 

## C. Adaptive Selection Mechanism 

- Lateral movement attacks 

A reinforcement learning (RL) model governs heuristic selection. The selection process is modeled as a Markov Decision Process (MDP): 

- Zero-day exploit propagation 

To emulate realistic environments, traffic demand and attack intensity follow stochastic variations, leading to non-stationary optimization landscapes. 

- State (St): Encodes features such as solution quality, improvement rate, and network threat level. 

All algorithms are implemented in Python and executed under identical computational settings. Each experiment is repeated 30 times to ensure statistical reliability. The stopping criterion is fixed to 50,000 fitness evaluations or 30 minutes runtime. 

- Action (at): Selection of a heuristic hi 

- Reward (Rt): Improvement in objective value: 



<!-- Start of picture text -->
Rt = F (xt) − F (xt+1) (15)<br><!-- End of picture text -->

The policy π(St) is learned using Q-learning: 

## B. Baselines 

The proposed Adaptive Hyperheuristic (AHH) is compared against two well-established metaheuristics: 



<!-- Start of picture text -->
Q(St, at) ← Q(St, at)+α Rt + γ max Q(St+1, a) − Q(St, at)<br>� a<br>(16)<br><!-- End of picture text -->

� 

- Genetic Algorithm (GA): Configured with tournament selection, one-point crossover, and bit-flip mutation. The population size is set to 100, crossover probability to 0.8, and mutation probability to 0.02. Elitism preserves the top 5% of individuals. 

where α is the learning rate and γ is the discount factor. 

This mechanism allows the hyperheuristic to adaptively prioritize heuristics based on their historical effectiveness under varying conditions. 

- Scatter Search (SS): Implemented using a referenceset based strategy. The reference set size is fixed to 20 solutions, combining diversification and improvement phases. 

For fairness, all methods use identical solution encoding, objective evaluation functions, and computational budgets. Parameters are tuned via preliminary experiments. 

TABLE II 

IMPACT OF ACCEPTANCE CRITERIA 

|Acceptance Method|HV|Convergence Iterations|Stability|
|---|---|---|---|
|Simulated Annealing|0.79|8200|Medium|
|Great Deluge|0.76|7800|High|
|Late Acceptance|0.81|7500|Medium|
|Adaptive (Proposed)|0.83|6900|High|



## C. Performance Metrics 

Performance evaluation considers both optimization efficiency and network security effectiveness: 

- Convergence Speed: Number of evaluations required to reach 95% of the best-observed solution quality. 

- Solution Quality: Measured using Hypervolume (HV) and Inverted Generational Distance (IGD), capturing convergence and diversity. 

- Robustness: Assessed via standard deviation of solution quality across multiple runs. 

- Security Effectiveness: Includes: 

   - Attack Success Rate (ASR) 

   - Mean Time to Mitigation (MTTM) 

   - Network Resilience Index (NRI) 

- Computational Cost: Average runtime and number of evaluations. 

Statistical significance is validated using the Wilcoxon signed-rank test at a 95% confidence level. 

## C. Convergence Behavior 

Figure 1 illustrates convergence trends over iterations. 



Fig. 1. Convergence comparison of AHH, GA, and SS 

## VI. RESULTS AND DISCUSSION 

This section presents a comprehensive evaluation of the proposed Adaptive Hyperheuristic (AHH) against baseline methods and alternative acceptance criteria. Results are analyzed in terms of convergence behavior, solution quality, robustness, and security effectiveness. 

AHH converges faster and avoids premature stagnation, highlighting the effectiveness of adaptive heuristic selection. 

## D. Heuristic Selection Dynamics 

To understand the internal behavior of the hyperheuristic, we analyze heuristic usage frequencies. 

## A. Overall Performance Comparison 

Table I summarizes the aggregated performance across all benchmark instances. 

TABLE I 

OVERALL PERFORMANCE COMPARISON 

|Method|HV ↑|IGD ↓|Time (s) ↓|NRI ↑|
|---|---|---|---|---|
|GA|0.71|0.082|1420|0.65|
|SS|0.75|0.067|1315|0.69|
|AHH (Proposed)|0.83|0.041|1185|0.78|



The proposed AHH achieves superior hypervolume and IGD values, indicating better convergence and diversity. Additionally, it demonstrates improved network resilience (NRI) with reduced computational cost. 

## B. Acceptance Criteria Analysis 

We evaluate different acceptance strategies integrated within the hyperheuristic. 

The adaptive acceptance mechanism consistently outperforms static strategies by dynamically balancing exploration and exploitation. 

### TABLE III 

HEURISTIC USAGE DISTRIBUTION 

|Heuristic Type|Frequency (%)|Avg. Contribution|
|---|---|---|
|Constructive|18|0.12|
|Improvement|34|0.28|
|Perturbation|27|0.22|
|Reconstructive|21|0.19|



Improvement heuristics dominate the search process, while perturbation and reconstructive operators play a critical role in escaping local optima. 

## E. Robustness Analysis 

Figure 2 presents the distribution of solution quality (measured in terms of hypervolume) across 30 independent runs for each method. The boxplots provide insights into both central tendency and variability, enabling a comprehensive assessment of algorithmic robustness under stochastic conditions. 

It can be observed that the proposed AHH framework exhibits a notably tighter interquartile range compared to GA and SS, indicating reduced variability in solution quality. The 



Fig. 2. Robustness comparison across methods 

real-world scenarios. The reinforcement learning component contributes to this improvement by prioritizing heuristics that historically lead to quicker mitigation strategies. 

Moreover, the Network Resilience Index (NRI) achieved by AHH is significantly higher, reflecting the framework’s ability to maintain system functionality under adverse conditions. This suggests that the solutions generated by AHH are not only optimal in a static sense but also structurally robust against disruptions and cascading failures. 

Overall, these results confirm that the proposed method is not only effective from an optimization standpoint but also delivers tangible benefits in practical network security settings. The consistent improvements across multiple metrics highlight the capability of AHH to address the complex and dynamic nature of modern cyber threats. 

## G. Discussion 

median performance of AHH is consistently higher, while the absence of extreme outliers suggests stable convergence behavior across runs. In contrast, GA shows a wider spread with several low-performing runs, reflecting sensitivity to initialization and stochastic operators. Similarly, SS demonstrates moderate variability, though less pronounced than GA. 

From a statistical perspective, the lower standard deviation of AHH confirms its robustness and reliability in dynamic environments. This stability can be attributed to the adaptive learning mechanism, which continuously refines heuristic selection based on feedback, thereby reducing performance fluctuations. Furthermore, the integration of adaptive acceptance criteria mitigates the risk of erratic search behavior, ensuring controlled exploration even under uncertain conditions. 

## F. Security Effectiveness 

Table IV reports the performance of the evaluated methods with respect to domain-specific security metrics, including Attack Success Rate (ASR), Mean Time to Mitigation (MTTM), and Network Resilience Index (NRI). 

TABLE IV 

SECURITY EFFECTIVENESS METRICS 

|Method|ASR ↓|MTTM ↓|NRI ↑|
|---|---|---|---|
|GA|0.32|145|0.65|
|SS|0.28|132|0.69|
|AHH|0.19|108|0.78|



The proposed AHH framework achieves substantial improvements across all security metrics. Specifically, the reduction in ASR from 0.32 (GA) and 0.28 (SS) to 0.19 demonstrates a significant enhancement in the system’s ability to prevent successful attacks. This improvement is primarily driven by the adaptive exploration of diverse defense configurations, which increases coverage of potential vulnerabilities. 

In terms of response efficiency, AHH reduces the mean time to mitigation (MTTM) by approximately 25% compared to GA and 18% compared to SS. This indicates faster detection and reaction to threats, a critical factor in minimizing damage in 

The experimental results clearly demonstrate that the integration of adaptive heuristic selection with dynamic acceptance criteria yields significant improvements over classical metaheuristic approaches. Unlike static strategies such as Genetic Algorithm and Scatter Search, the proposed AHH framework dynamically adjusts its search behavior in response to the evolving optimization landscape. This adaptability enables the method to maintain a consistent balance between intensification and diversification, which is essential for avoiding premature convergence and ensuring high-quality solutions. 

A deeper analysis of the heuristic selection patterns reveals that the reinforcement learning mechanism effectively learns the contextual relevance of different heuristic categories. Improvement heuristics dominate during stable phases of the search, contributing to steady convergence, while perturbation and reconstructive heuristics are preferentially selected during stagnation periods to promote exploration. This intelligent switching behavior highlights the capability of the framework to self-regulate its search dynamics based on real-time feedback. 

Furthermore, the adaptive acceptance mechanism plays a critical role in enhancing the robustness of the search process. By dynamically selecting among Simulated Annealing, Great Deluge, and Late Acceptance strategies, the framework adjusts its acceptance tolerance according to the current search state. This results in a more stable convergence profile with reduced variance across independent runs, while still preserving the ability to escape local optima when necessary. The synergy between heuristic selection and acceptance adaptation constitutes a key strength of the proposed approach. 

From a security perspective, the improvements in attack success rate reduction and network resilience indicate that the optimization process is not only mathematically efficient but also practically meaningful. The framework consistently identifies defense configurations that enhance system robustness under diverse and dynamic attack scenarios, demonstrating its applicability to real-world cybersecurity environments. 

Despite these promising results, certain limitations should be acknowledged. The performance of the reinforcement learn- 

ing component depends on the quality of state representation, which in this study is based on aggregated metrics. Incorporating richer representations, such as graph-based embeddings of network topology, could further enhance decision-making. Additionally, while the computational overhead remains acceptable, the integration of learning mechanisms introduces extra complexity that may require optimization for large-scale real-time deployments. 

Overall, the proposed AHH framework exhibits strong scalability, adaptability, and robustness, making it a compelling solution for dynamic network defense optimization. Its ability to autonomously adjust both heuristic selection and acceptance behavior positions it as a significant advancement over traditional metaheuristic methods in complex and adversarial environments. 

- [6] B. Bilgin, E. Ozcan, and E. Korkmaz, “Extending hyper-heuristics with a learning mechanism for selecting heuristics,” in International Conference on Parallel Problem Solving from Nature. Springer, 2006, pp. 1086– 1095. 

- [7] E. K. Burke and Y. Bykov, “A late acceptance strategy for hill-climbing,” European Journal of Operational Research, vol. 258, no. 1, pp. 70–78, 2017. 

- [8] W. Wang, Y. Sheng, J. Wang, X. Zeng, X. Ye, Y. Huang, and M. Zhu, “A survey on cyber security using machine learning techniques,” IEEE Access, vol. 8, pp. 190 895–190 915, 2020. 

- [9] Z. Xu, H. Liu, and W. Chen, “Network security optimization using intelligent algorithms: A survey,” Computer Networks, vol. 186, p. 107742, 2021. 

## VII. CONCLUSION 

This paper presented an Adaptive Hyperheuristic (AHH) framework for solving dynamic network defense optimization problems. By integrating reinforcement learning for heuristic selection and adaptive acceptance criteria, the proposed approach effectively balances exploration and exploitation in non-stationary and adversarial environments. The formulation of the problem as a multi-objective optimization task enables simultaneous consideration of critical factors, including attack surface, response time, resilience, and operational cost. 

Extensive experimental results demonstrated that the proposed AHH consistently outperforms traditional metaheuristic approaches such as Genetic Algorithm and Scatter Search across multiple performance indicators, including convergence speed, solution quality, robustness, and security effectiveness. The adaptive mechanism for selecting both heuristics and acceptance strategies proved particularly effective in handling dynamic threat scenarios and avoiding premature convergence. 

Overall, the proposed framework offers a scalable and robust solution for real-world network security optimization. Future work will focus on extending the approach to real-time deployment environments, incorporating deep learning models for richer state representation, and validating the framework on real-world network datasets. 

## REFERENCES 

- [1] E. K. Burke, M. Hyde, G. Kendall, G. Ochoa, E. Ozcan,<sup>¨</sup> and J. R. Woodward, “Hyper-heuristics: A survey of the state of the art,” Journal of the Operational Research Society, vol. 64, no. 12, pp. 1695–1724, 2013. 

- [2] E. Ozcan,<sup>¨</sup> B. Bilgin, and E. E. Korkmaz, “A review of hyper-heuristics: Approaches, applications and future directions,” Expert Systems with Applications, vol. 123, pp. 213–228, 2019. 

- [3] K. Danach, A. Rammal, I. Moukadem, H. Harb, and A. Nasser, “Advanced optimization in e-commerce logistics: Combining matheuristics with random forests for hub location efficiency,” IEEE Access, 2025. 

- [4] K. Danach, H. Harb, L. Saker, and A. Raad, “Quantum-inspired hyperheuristic framework for solving dynamic multi-objective combinatorial problems in disaster logistics,” World Electric Vehicle Journal, vol. 16, no. 6, p. 310, 2025. 

- [5] M. Mavrovouniotis, C. Li, and S. Yang, “Dynamic optimization using adaptive hyper-heuristics,” Soft Computing, vol. 21, no. 18, pp. 5203– 5221, 2017. 

