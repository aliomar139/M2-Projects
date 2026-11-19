# Routing Heterogeneous Mobile Hospital With Different Patients Priorities: Hyper-Heuristic Approach 

Kassem Danach 

and Jomana Al-Haj Hassan and Wissam Khalil 

## Shahin Gelareh 

Laboratoire Genie Informatique et Automatique Universite D’Artois, France 

Faculty of Economics and Business Administration Islamic University of Lebanon, Lebanon 

Email: kassem.danach@iul.edu.lb 

Abstract—Telemedicine, which is the use of technologies in order to provide clinical health care at a distance, can be insufficient in some cases where there is a need for medical instruments. This implies the need for supplementary services that would provide to overcome some of the deficiencies. Thus, many techniques were proposed, one of them is to dispatch the so-called Mobile Hospital (MH). This study centers around dispatching and scheduling of dispatched MHs. We aim at allocation and scheduling of MHs to serve patients at their locations given that every patient has its priority in receiving services and the provided service for each patient needs an a priori known time slot. In this study, we propose a hyper-heuristic solution method, which includes several low-level heuristics categorized as constructive, improvement, perturbation etc. coordinated via an artificial intelligent method. Our computational results confirm the efficiency of our solution in terms of solution quality and time. 

### I. INTRODUCTION 

A Mobile Hospital (MH) (see Figure1) is a mobile medical care service unit in the size of a 40-ft container size truck. It offers medical services outside of the traditional hospital. In regions where huge investment in constructing permanent hospitals is rather impossible due to some reasons (including dynamic/dispersion of population in region, economic instability etc.), MHs are one of the best practices for the governments to assure a minimum required service level to major part of the territory. 

Routing Heterogeneous Mobile Hospital With Different Patients Priorities Problem (RHMHDPPP) is a critical problem, which deals with the allocation and scheduling a set of MHs to a set of patients in given discrete locations within a given geographical region. The fleet of MHs is a heterogeneous fleet of MHs and to every MH only a subset of patients can be assigned. Every such a patient has needs one (one package) set of services that can take up to a certain time depending on his/her state. 

The objective is to find the optimal or near optimal solutions that represent a schedule of tasks for each MH. Each task represents a medical service for a specific patient. The aims is to complete tasks in a manner of minimizing the termination time of service to every patient. As the priority of each patient is represented by a proportional cost and the start time of service in the objective function, therefore, minimizing such 



Fig. 1. A Mobile Hospital. 

function basically translate to service the patients with higher priority earlier in our schedule. The literature of this problem is limited. For this reason we list some similar problems such as: 

- 1) Open Vehicle Routing Problem 

- 2) Team Orienteering Problem 

- 3) Job Shop Scheduling Problem 

Open Vehicle Routing Problem (OVRP) consists of serving customers but there is no need to return to the depot. A tabu search meta-heuristic method is proposed for the problem by[1][2][3]. Variable Neighborhood Search was also proposed to solve the problem where neighborhoods consist of reversing segments of routes (sub-routes) and exchanging segments between routes[4]. Ant Colony with post-optimization procedure was also proposed in order to improve the best-found solutions [5]. 

The problem is also similar to Team Orienteering Problem (TOP). In a given time horizon, TOP consists of finding a path for an agent from an origin to a destination where each node is associated with a reward value and the objective is to maximize the collecting of reward values. Some exact and meta-heuristic methods applied to the problem such [6][7][8][8]. 

The problem also resembles Job Shop Scheduling Problem. Job Shop Scheduling Problem (JSSP) purpose is to find a schedule, that is, an allocation of the operations to time intervals to machines. To apply this theory to our study, jobs are replaced by patient medical series and machines are 

�������������������������������������������� 

��� 

replaced by mobile hospitals. Also, in RHMHDPPP, the mobile hospitals are not identical, they offer different medical services. While, in JSSP, there doesn’t exist a variable that considers the delays between jobs which is represented in our problem as travel time between patients. 

### II. PROBLEM STATEMENT 

The problem is described as such: A set of patients, P = {1, . . . , n} are scattered within a geographic area. Every patient i, needs certain medical services and he has a certain priority PRi according to his medical state. Each operation of a patient i takes ti unit of time. [Tij]|P|×|P| represents the matrix of travel times between every pair of (i, j) ∈P × P. A set of mobile hospital, where every v ∈V has a specific type indicating the medical services that can be offered. Each mobile hospital M = {1, . . . , m} can handle exactly one patient per time. Every operation needs to be processed during an uninterrupted period. 

The problem is to find a schedule of tasks of each mobile hospital in order to serve patients that have higher priority(urgent cases) as soon as possible while minimizing the cost in terms of time. 1 represents the objective function. 



<!-- Start of picture text -->
min � (tj + ti o) ∗ PRi i = 1, . . . , n (1)<br><!-- End of picture text -->

tj represents the cumulative time before arriving to the patient i, and t<sup>o</sup> i<sup>representsthetimetakenbyservingpatienti.</sup> 

III. HYPER-HEURISTIC APPROACH 

Finding solutions to this type of problems using exact methods is quite difficult even for very small size instances. For this reason, we resort to a hyper-heuristic approach. Hyper-heuristics are distinguished from the meta-heuristic and heuristic as in the following: 

- 1) Heuristic: the objective is just to find a feasible solution with no guaranty to be optimal but is good enough for a given set of goals. 

- 2) Meta-heuristic: it tries to find very good quality solution using two strategies: intensify and diversify the search space. 

- 3) Hyper-heuristic: it is a higher level procedure the previous types. It consists in trying to find the optimal solution but by using a set of low level heuristics guided by an intelligent method. 

We note that hyper-heuristic methods are categorized as: 

- 1) Heuristic Selection: The goal is to select the best series of heuristics in order to obtain good solution. 

- 2) Heuristic Generation: Generate new heuristic methods using basic components of construction and perturbation heuristics. 

The goal of hyper-heuristic techniques is to automate the design and tune the heuristics in order to solve a hard computational problems [9]. Also, according to [9], hyper-heuristics can be divided into two types: 

- 1) Constructive: select and use constructive heuristics in order to construct the solution from scratch. 

- 2) Perturbation: iteratively select and uses perturbation procedures until a set of termination criteria is met. 

We are interested, in this paper, to develop a selective perturbation hyper-heuristic. For that, we implemented several low level heuristics oriented by a meta-heuristic method which is further explained in section IV. 

### A. Constructive Heuristics 

Constructive algorithms consist of building a feasible solution from scratch given predefined rules. Our constructive method, CS1, tries to schedule for each mobile hospital the corresponding patients considering the task lengths for each mobile hospital. The constructive algorithm is applied once at the beginning in order to build the initial solution. 

### B. Improvement Heuristics 

In order to improve the objective function value, we apply improvement heuristics, which are defined as methods that perform some successive changes. Our improvement heuristic, LS1, consists of re-ordering each mobile hospital sequence separately. Re-ordering in each sequence consists of searching the best order of tasks (patients) assigned to each mobile hospital. The pseudo-code for LS1 is shown in Algorithm 1. We note that Q(Hs) represents patients assigned to mobile hospital s. 

### Al <mark>g</mark> orithm 1 LS1 

procedure LS1(S) ▷ INPUT: Hospitals Queues 2: for s = 1, . . . , m do ∀s = 1, . . . , m, (m = |H|) Queue temp; 4: for i = 1, . . . , n do ∀i = 1, . . . , n, (n = |Q(Hs)| MinimumOF; 6: CurrentPatient; if thenMinimumOF > OF (Pi, Hs) 8: MinimumOF = ← OF (Pi, Hs); CurrentPatient ← Pi; 10: end if tabu ← Pi; 12: Hs ← Pi; end for 14: end for return H; 16: end procedure 

### C. Perturbation Heuristics 

Perturbation Heuristics consist of explore the search space in order to escape from a local optima. In this study, we implement two perturbation heuristics as following: 

- 1) SW1: consists of swapping two patients between two hospitals if they can offer these patients their needed medical services. 

- 2) Remove/Insert: removes a patient from a hospital queue and re-insert it to another one. 

The pseudo-code for SW1 is shown in Algorithm 2. 

�������������������������������������������� 

��� 



Fig. 2. Three Heterogeneous Mobile Hospitals serve eight patients: The first mobile hospital offers medical services for the patient 4 then the patient 8. The second serves patients ordered as patient 1, 3, 5, and finally 7. The third serves the patient 2 then the patient 2 then patient 6. 

### Al <mark>g</mark> orithm 2 SW1 

- 1: procedure SW1(S) ▷ INPUT: Hospitals Queues 2: Random R1 ∈ 1, . . . , s (m = |H|) 3: Random R2 ∈ 1, . . . , s − R1 (m = |H|) 4: RandomPosition1 P1 ∈ 1, . . . , l (l = |Q(HR1)|) 5: RandomPosition1 P2 ∈ 1, . . . , k (k = |Q(HR2)|) 6: Swap(HR1(P 1), HR2(P 2)) 

- 7: return S; 

- 8: end procedure 

### IV. REINFORCEMENT LEARNING 

Reinforcement learning is defined as mapping a situation to action in order to maximize a numerical reward signal [10]. Trial-and-error search and delayed reward are the two most important features of reinforcement learning [11]. In this paper, the reward value for any heuristic i is assigned according Equation 2, given OF(hi) is the objective function calculated after the heuristic i is applied and T(hi) is the time spent in heuristic i. 



<!-- Start of picture text -->
− OF ( hi )<br>Ri = � (2)<br>T (hi)<br><!-- End of picture text -->

A simulated Annealing meta-heuristic is implemented to guide heuristic selection in a manner to exploit and explore the heuristic search space. So, at each iteration a heuristic i is applied if the Equation 3 is true. 



<!-- Start of picture text -->
exp(−R ∗ t) > Random(0, 0.5) (3)<br><!-- End of picture text -->

The overall hyper-heuristic process presents the two phases of the reinforcement learning phase: 

- 1) Choose a heuristic i according to its history performance. 

- 2) Update heuristic performance after each time it is applied. 

### V. NUMERICAL EXPERIMENTS 

Table I shows the instance name (formatted as nbPatient_nbMH), initial objective function, the best 

objective function and the execution time. The results show a gap between the initial and the best-found objective function, which demonstrates the effectiveness of the designed hyper heuristic framework in improving the initial solution. However, the main aspect of these results is that the proposed method converges very fast —in less than 10 seconds for all the instances . 

TABLE I. INITIAL, BEST SOLUTION AND EXECUTION TIME RESULTS 

|Instance|Initial O.F|O.F|Execution Time|
|---|---|---|---|
|8<br>3|104|76|3.45|
|10<br>3|472|443|4.01|
|15<br>3|868|838|5.02|
|15<br>5|547|545|5.19|
|20<br>2|2234|2073|7.05|
|20<br>5|942|899|6.08|
|25<br>3|2375|2236|8.087|
|25<br>5|1475|1440|6.884|
|25<br>7|1093|1090|7.36|
|30<br>3|3413|3204|8.573|
|30<br>5|2089|1955|7.737|
|30<br>7|1586|1475|8.088|
|35<br>3|4340|4059|8.547|
|35<br>5|2665|2517|7.073|
|35<br>7|1980|1849|8.405|
|50<br>5|5772|5303|8.265|
|50<br>7|4116|3906|8.211|
|50<br>9|3312|3139|7.186|
|50<br>10|3002|2825|7.314|
|75<br>7|9556|8693|7.903|
|75<br>9|7502|6880|8.972|
|75<br>10|6752|6241|9.684|
|100<br>7|18557|17582|7.354|
|100<br>9|17373|16185|7.588|
|100<br>10|14245|13218|6.891|
|100<br>12|12216|11260|7.466|
|125<br>7|31965|29721|7.784|
|125<br>9|28580|26578|8.045|
|125<br>10|24190|22275|8.153|
|125<br>12|20183|18755|8.67|
|150<br>7|49165|45524|7.936|
|150<br>9|49056|46121|7.867|
|150<br>10|38394|35882|8.206|
|150<br>12|33388|30773|8.215|
|175<br>7|64759|59886|7.779|
|175<br>9|62647|56986|7.238|
|175<br>10|51177|46564|7.343|
|175<br>12|45213|40969|7.095|
|200<br>7|83511|76533|7.482|
|200<br>9|76780|69436|7.724|
|200<br>10|64016|58262|7.562|
|200<br>12|57662|52416|7.907|



Figure 2 presents an example of an instance of 8 patients and 3 mobile hospitals. The best objective function for this instance, as shown in Table I, is 76. 

### VI. CONCLUSION 

In this paper, we demonstrate the effectiveness of the hyper heuristic application in these types of problems. In our future agenda, we will work with more constraints such as time windows constraints where some medical services should be 

�������������������������������������������� 

��� 

offered in a certain time window, constraints related to doctors assigned to hospitals, add constraints of dynamic problem to assign new patients to mobile hospitals during the process, and others. 

### REFERENCES 

- [1] J. Brand˜ao, “A tabu search algorithm for the open vehicle routing problem,” European Journal of Operational Research, vol. 157, no. 3, pp. 552–564, 2004. 

- [2] Z. Fu, R. Eglese, and L. Y. Li, “A new tabu search heuristic for the open vehicle routing problem,” Journal of the operational Research Society, vol. 56, no. 3, pp. 267–274, 2005. 

- [3] M. Gendreau, A. Hertz, and G. Laporte, “A tabu search heuristic for the vehicle routing problem,” Management science, vol. 40, no. 10, pp. 1276–1290, 1994. 

- [4] K. Fleszar, I. H. Osman, and K. S. Hindi, “A variable neighbourhood search algorithm for the open vehicle routing problem,” European Journal of Operational Research, vol. 195, no. 3, pp. 803–809, 2009. 

- [5] X. Li and P. Tian, “An ant colony system for the open vehicle routing problem,” in Ant Colony Optimization and Swarm Intelligence. Springer, 2006, pp. 356–363. 

- [6] H. Tang and E. Miller-Hooks, “A tabu search heuristic for the team orienteering problem,” Computers & Operations Research, vol. 32, no. 6, pp. 1379–1407, 2005. 

- [7] C. Archetti, A. Hertz, and M. G. Speranza, “Metaheuristics for the team orienteering problem,” Journal of Heuristics, vol. 13, no. 1, pp. 49–76, 2007. 

- [8] P. Vansteenwegen, W. Souffriau, G. V. Berghe, and D. V. Oudheusden, “A guided local search metaheuristic for the team orienteering problem,” European Journal of Operational Research, vol. 196, no. 1, pp. 118– 127, 2009. 

- [9] E. K. Burke, M. Hyde, G. Kendall, G. Ochoa, E. Ozcan, and R. Qu, “A survey of hyper-heuristics,” Computer Science Technical Report No. NOTTCS-TR-SUB-0906241418-2747, School of Computer Science and Information Technology, University of Nottingham, 2009. 

- [10] A. G. Barto, Reinforcement learning: An introduction. MIT press, 1998. 

- [11] R. S. Sutton, “Introduction: The challenge of reinforcement learning,” in Reinforcement Learning. Springer, 1992, pp. 1–3. 

�������������������������������������������� 

��� 

