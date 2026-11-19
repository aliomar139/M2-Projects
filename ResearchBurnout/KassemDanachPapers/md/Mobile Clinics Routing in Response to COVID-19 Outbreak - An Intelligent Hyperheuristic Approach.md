**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** Published Online January 2022 in IJEAST (http://www.ijeast.com) 



# MOBILE CLINICS ROUTING IN RESPONSE TO COVID-19 OUTBREAK: AN INTELLIGENT HYPERHEURISTIC APPROACH 

Jomana Al-Haj Hassan 

Abbas Tarhini 

Department of Management Information System,                            Department of Operations Management Islamic University of Lebanon, Lebanon                              Lebanese American University, Beirut, Lebanon 

**_Abstract_ — In March 2020, the World Health Organization (WHO) announced the COIVD-19 as a global pandemic that caused thousands of deaths and brought the world to a standstill with a huge economic burden [1]. Health is an essential factor for sustaining a better life in a better world. Today, for different reasons, several districts in our countries would be deprived from the needed health support and thus, in such cases, we need to deliver health care to those regions. Despite its considerable cost, the mobile clinic remains one of the good solutions to deliver health care to critical areas in our countries. A recognized problem in this domain is minimizing the cost of mobile clinics route in a way that the number of served patients is maximized. This problem is known as the mobile clinics routing problem (MCRP). The purpose of this paper is to present a novel approach that, within the given limited resources, it minimizes the cost and the traveling distance of mobile clinics while maximizing the number of served patients as per priorities assigned according to the patients’ medical status. This paper implements and tests an intelligent variable neighbourhood search algorithm for MCRP.** 

## _Keywords—_ **Pandemic Management, Hyperheuristic, Machine Learning** 

## I. BACKGROUND OF THE STUDY 

Today, several reasons prevent governments in different countries from providing suitable health care to their citizens. Some of these reasons are related to pandemics, natural disasters, or even to terrorist acts that hit health care centers, which might take a long time for governments to recover. Other reasons could be the distributions of the population in different geographic areas that lead to establishing health care centers in these areas becoming expensive and unfeasible 

projects. All these reasons forces governments to think about delivering health care to citizens instead of having them cross the long distance to acquire it. Mobile clinics were one of the feasible solutions to be considered. 

Mobile clinic is defined as “a typical clinic with all needed machines and equipment which can move from one place to another to provide better service. It is a way of having all the equipment built into a moving vehicle to be ready for usage at any time and to reach long distances where there are no fixed clinics” [2]. Today, the need for mobile clinics is demanding to resolve the dilemma of an enormous number of people deprived from health care services. This fact is revealed in World Health Organization’ report [1], the report clearly stated that 400 million people do not have access to essential health services due to the increase in natural disasters, epidemics, food shortage, refugee aid and military conflicts. The basic problem reported is the lack of or destroyed infrastructure, which hinders the performance or the reconstruction of clinics. The report further “recommend that countries pursuing universal health coverage should aim to achieve a minimum of 80% population coverage of essential health services”, and that everyone everywhere should be protected from catastrophic and impoverishing health services. 

The demand for universal health coverage is further asserted by the WHO [1], which requires the “health policies and programs focus on providing quality health services for the poorest people, women and children, people living in rural areas and those from minority groups". Further, in its report on health care services, the Rural Health Services Review Committee of Alberta [3]  found that “some fixed clinics are closing in the rural area because of the declining population, economic recession, shortages of physicians and other health care professionals, a disproportionate number of elderly, poor, and underinsured residents, and high rates of chronic illness”. Participants in the report claimed that it is difficult for them to find out a professional doctor or a trusted health care center in 

1 

**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

## Published Online January 2022 in IJEAST (http://www.ijeast.com) 



rural areas. Most of the citizens in the rural areas believed that the government should provide clinics in the rural areas other than sending people to other places and clinics. 

At present, mobile clinics offer a feasible solution to the above dilemma. In addition to being equipped to respond to the COVID 19 outbreak, mobile clinics provide many programs and centers including the da Vinci® Surgical system, cancer services, diabetes, digestive health, emergency services, and many other health care services. In fact, such a variety of services offered by mobile clinics provides efficient health care, flexibility, accessibility to patients; still a major problem faces mobile clinics operators. The problem is to optimize the mobile clinics trip in a way that minimizes the cost and the traveling distance of the mobile clinics routes while maximizing the number of patients served as per priorities assigned according to the patients’ medical status. Such a problem is very critical and hard since it incorporates vehicle routing and scheduling problems. This makes the mobile clinic routing problem (MCRP) a nondeterministic polynomial time (NP)-complete problem. Such problems may be too computationally-intensive to find their exact solution. In such cases, heuristic techniques can be effective. In fact, due to their random nature, heuristic techniques are not guaranteed to find an optimal solution for any problem, but they will find a good solution if one exists. 

In this work, we propose a novel Variable Neighbourhood Search (VNS) metaheuristic for solving MCRP. The selection of the VNS metaheuristic was motivated by [4] perception which states that “it aims at solving very rapidly, very large instances, and increasing precision and reducing solution time for combinatorial optimization problems; further VNS uses strategies for search diversification and intensification that have proved effective in a variety of optimization problems”. This paper presents and tests the VNS algorithm with randomly generated input that simulates actual data in MCRP with instances of 200 patients and 12 mobile clinics. The test case results clearly show a significant improvement in the cost of the objective function and the execution time. 

The rest of this paper is organized as follows. The next section is devoted to the literature review. Section 3 presents the mathematical formulation. The Variable Neighbourhood Search metaheuristic is discussed in Section 4. Section 5 presents the empirical results. Finally, the conclusion is presented in Section 6. 

## II. LITERATURE REVIEW 

Several researchers addressed the mobile clinics routing problem (MCRP). A number of researchers considered reducing the mobile clinics routes as the most important factor to optimize since the distance may sometimes hinder the usage of a medical service [5-11]. Literature also shows that many governments equip clinics with mobile healthcare facilities instead of building fixed healthcare centers [2, 12, 13]. 

Furthermore, other researchers studied the idea of building fixed healthcare centers that could be reached within a given walking distance instead, and thus aimed at finding the best location a healthcare center is suited, and how they should be staffed [14-17]. Most of the previous works dealt with the problem as either a tour planning distance reduction problem or as a fixed healthcare allocation problem. In addition to that, only a few articles addressed this problem in the past five years, at a time international healthcare organizations urged the need for further research in this area. All this motivated us to present our novel algorithm to solve this problem. To the best of our knowledge, none of the previously proposed solutions used VNS algorithm to solve the MCRP. Unlike other evolutionary methods, VNS uses strategies for diversification and intensification that have proved effective in a variety of optimization problems [4]. Interestingly our proposed solution was able to find very good results tested on large-sized problems with 200 patients and 12 mobile clinics within an acceptable running time. 

## III. PROBLEM STETEMENT 

Disasters, such as pandemics, natural disasters, wars, etc., are intractable problems for humanity that lead to human losses that are not easy to recover. Routing of mobile clinics to cure victims in such environments is an important problem. The objective is to minimize the mobile clinic route time while taking into consideration other important parameters such as patients’ priorities, road conditions, and clinics’ capacities. To solve this problem, we propose a mathematical model and a hyper-heuristic solution method that comprises several lowlevel heuristics guided by a reinforcement learning heuristic. 

## IV. MOBILE CLINIC ROUTING PROBLEM 

In the mobile clinic routing problem, mobile clinics are required to serve many patients living in a given spatial area. These patients are assigned priorities according to their medical status. Given a limited number of resources, a mobile clinic is required to serve the maximum possible number of patients, taking into consideration the patients’ priorities. In this problem, it is assumed that there exists an overall time limiting the whole process, and that each mobile clinic can handle one operation at a time, where each operation is processed within an uninterrupted period. It is worth noting that failing to find a feasible assignment of a mobile clinic to patients would be very expensive in terms of wasting exceptional healthcare resources processed in unexpected time frames that would further lead to threatening patients’ lives in some cases. The effect of such an assignment is illustrated in the following example. This example shows two different permutations to assign one mobile clinic to eight patients taking into consideration the operation time, traveling time and patient priorities. The first permutation is illustrated in Figure 1.  In this permutation, the 

2 

**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 



mobile clinic is assigned to the corresponding eight patients consecutively 1, 2, 3, 4, 5, 6, 7, 8. 



<!-- Start of picture text -->
5<br>P2  P3<br>P8<br>3<br>5<br>9<br>P1<br>P7<br>7<br>P4<br>5<br>4<br>P5<br>4  P6<br><!-- End of picture text -->

Fig. 1. Mobile clinic assignment – First permutation 

Figure 1 clearly shows the path traversed by the mobile clinic to serve the eight patients. The numbers on the arrows represent the time taken to travel from one patient to another. For example, the time needed to reach patient 1 is 7, and to reach patient 2 from patient 1 we need 9 units of time. The cost of such a permutation would be calculated as follows (this formula will be verified in the following section): ∑(ti + tij ) * PRi, = (5+7)*1+ (5+9)*2+ (7+6)*1+ (5+5)*1+ (8+5)*1+ (5+4)*1+ (5+4)*1+ (7+3)*1 = 104, where ti is the operation time at patient i, and tij is the time from patient i to patient j, and  PRi is the priority of patient i. 



<!-- Start of picture text -->
5<br>P3<br>P2<br>2  P8<br>2<br>P1  1<br>P7<br>P4  1<br>1<br>2<br>P5<br>4  P6<br><!-- End of picture text -->

Fig. 2. Mobile clinic assignment – Second permutation 

Obviously, the combination of the time and priority between patients has a tremendous effect on the total cost. Therefore, it is rational to assume that if we assigned the mobile clinic to patients with lower traveling time, we would get an optimized solution. To explain this concept further, 

consider Figure 2, which represents a different permutation from that given in Figure 1 where the mobile clinic is assigned to patients in a different sequence. The cost of such a permutation would be calculated as follows (this formula will be verified again in the following section): ∑(ti + tij ) * PRi, = (8+1)*1+ (5+4)*1+ (5+2)*1+ (5+1)*1+ (5+1)*1+ (7+2)*2+ (5+2)*1+ (7+5)*1 = 72, where ti is the operation time at patient i, and tij is the time from patient i to patient j, and  PRi is the priority of patient i. This clearly proves that reaching patients in different sequences may affect the total cost. 

## V. MATHMATICAL FORMILATION 

Assignment problems can be represented by graphs [18]. Let G (VG, EG) be a graph in which vertex vi  VG represents a patient, and |VG| = A is the total number of patients to be assigned to mobile clinics. Vertex weight PRi represents the priority that patient vi holds; further it also holds the time ti taken by each operation at patient vi. Edge e  EG joining two vertices vi and vj represents the existence of a flow between patient vi and patient vj; the weight of edge e, tij, represents the travel time between the two patients vi and vj. 

The objective function of this problem presented in the following equation, it minimizes the total routes taking into consideration each patient’s priority 



Given a fixed number of patients and mobile clinics distributed in the whole country. Distances between all mobile clinics and patients, in addition to distances between patients themselves are given as well. Each patient must be served exactly by one mobile clinic. Each mobile clinic can serve exactly one patient at a given time. Each mobile clinic takes an operation time for each patient. 

## VI. VARIABLE NEIGHBORHOOD SEARCH (VNS) 

Variable neighborhood search (VNS), proposed by Mladenović and Hansen [19], is another kind of metaheuristics to solve combinatorial optimization problems.  It explores neighborhoods found in one solution space, and moves from there to a new one randomly or intelligently if and only if an improvement was made. VNS includes two main phases: 1) the shaking phase and 2) the local search phase. The first one aims to diversify the search space in order to escape from local optima, while the objective of the second phase is to intensify the search around the current solution in order to improve it. Figure 3 illustrates how the implementation of the VNS phases avoids local optimum and helps to explore and exploit the search space in order to achieve a near optimal solution.  Each phase of the VNS applies more than one heuristic; further 

3 

## **_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** Published Online January 2022 in IJEAST (http://www.ijeast.com) 



description of the heuristics selection method is found in the below subsections. 

In fact, VNS is used by several researchers to solve scheduling problems. In their work, Remde, Cowling [20] proposed a VNS in order to solve workforce scheduling problem where it proved to be a powerful tool compared with the solution quality resulting from by a genetic algorithm. Further, Hsiao, Chiang [21] propose a VSN based hyperheuristic method to solve more than one problem such as job shop scheduling, and bin packing problems. 



Fig. 3. A general schema of the VNS algorithm 

In this work, the proposed VNS constructs a feasible solution as an initial step before moving to the shaking and the local search phases. In the shaking phase, the Tabu search method is used. It selects a low level heuristic from the set of perturbation heuristic. In the local search phase, a random cycle of the existing predefined improvement heuristics is formed. It applies an improvement heuristic while it is still improving the solution and switches to the next one in the cycle in case it stops improving the solution. As illustrated in Figure 4, this process keeps repeating until n consecutive non-improving solutions are reached. The proposed low level-heuristic is classified as constructive, improvement, and perturbation. 

In our study, the constructive algorithm is applied only once at the beginning of the assignment problem to build the initial solution. Constructive heuristics build a solution from scratch based on several predefined rules. Thus, taking into consideration the overall (task length) time allocated to each mobile clinic, the proposed constructive method of this study, CS1, schedules for each mobile clinic the corresponding adequate patients. 



Fig. 4. The process of the proposed VNS Hyperheuristic 

On the other hand, Improvement heuristics start from a complete solution and apply some moves to improve the objective function value. In our study, different improvement heuristics are proposed: 

1. Better-sequence-on-the-same-mobile-clinic: for a given mobile clinic, we reorder (one task per time) the sequence of allocated patients to be served by this mobile clinic and among the improving solution found, we move to the best found feasible solution in a greedy manner. The pseudocode for local search (LS1) is described in Algorithm 1 in Figure 5. We note that Q(Hs) represents patients assigned to mobile clinic s. 

2. Inset/drop-between-two-different-mobile-clinic: aiming at making a balanced utilization and fair distribution of tasks among mobile clinics, for two randomly chosen mobile clinics ri,rj(i ≠ j), we consider the following moves: 1) move one tasks from mobile clinic ri to mobile clinic rj (i≠j) such that the difference between the objective functions of mobile clinic ri and mobile clinic rj, ∆ = (OF(ri)−OF(rj)), is minimized. 2) removing a patient from the list of patients being served by a given mobile clinic and insert it in a proper place within the sequence of patients being served by the mobile clinic with the least objective function. 

4 

**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 





3. Crossover: consists of swapping of ’genetic material’ is made with the mobile clinic (part of the chromosome), while in the mutation operator is made with two mobile clinics, one in each chromosome. 

4. Remove/Insert: removes a patient from a clinic queue and re-insert it to another one. 

The pseudocode for SW1 is described in Algorithm 2 in Figure 6. 



Fig. 6. Algorithm for swapping patients in perturbation heuristic 

## VII. EXPERIMENTAL RESULTS 

Fig. 5. Local Search algorithm 

Perturbation heuristics start with a complete solution and do some changes in order to inject some diversification. It consists of exploring the search space step in order to escape from a local optimum. In this study, we implement two perturbation heuristics as follows: 

1. Re-Construct: consists of destroy a part of the current solution and rebuild it using the proposed constructive heuristic. 

2. SW1: consists of swapping two patients between two clinics if they can offer these patients their needed medical services. 

In this section, the results of VNS algorithm are presented. This algorithm is tested on a set of 33 test cases; each of these test cases has a different number of patients and mobile clinics with different timing to reach neighbor patients. Since real data are not available to evaluate the performance of the proposed algorithms, we generated synthetic data. The test cases are illustrated in TABLE I. This table shows several parameters: the test case number, the number of patients, and the number of used mobile clinics. In these 33 test cases we wanted to test how the performance is affected for different combinations of patients assigned to mobile clinics. Thus, in some test cases, (eg.TC1-TC3), we varied the number of patients and kept the number of mobile clinics fixed; in other test cases, the number of patients is fixed and the number of mobile clinics is varied. Further, different test cases scaled up in size to test our algorithm on small, medium, and large sized-problems. 

5 

**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 



Table -1 Initial, Best solution and execution time results 

Table -2 Initial, Best solution and execution time results 

|**TestCase #**|**Number**<br>**of**<br>**Patients**|**Number**<br>**of MH**|**TestCase #**|**Number**<br>**of**<br>**Patients**|**Number of**<br>**MH**|**Instance #**|**Number**<br>**of**<br>**Patients**|**Number**<br>**of MH**|<br>**Initial**<br>**Objective**<br>**Function**<br>**(OF)**|<br>**Best**<br>**Objective**<br>**Function**|<br>**Execution**<br>**Time**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|TC1|8|1|TC18|50|10|||||||
|TC2|10|3|TC19|75|7|TC1|8|1|104|72|2.001|
|TC3|15|3|TC20|75|9|TC2|10|3|472|440|4.001|
|TC4|15|5|TC21|75|10|TC3|15|3|868|799|4.024|
|TC5|20|5|TC22|100|7|||||||
|TC6|25|3|TC23|100|9|TC4|15|5|547|513|3.119|
|TC7|25|5|TC24|100|10|TC5|20|5|942|705|6.014|
|TC8|25|7|TC25|100|12|TC6|25|3|2375|2198|5.030|
|TC9|30|3|TC26|150|7|TC7|25|5|1475|1409|3.441|
|TC10|30|5|TC27|150|9|||||||
|TC11|30|7|TC28|150|10|TC8|25|7|1093|1083|5.887|
|TC12|35|3|TC29|150|12|TC9|30|3|3413|3204|7.303|
|TC13|35|5|TC30|200|7|TC10|30|5|2089|1955|5.414|
|TC14|35|7|TC31|200|9|||||||
|||||||TC11|30|7|1586|1475|7011|
|TC15|50|5|TC32|200|10||||||.|
|TC16|50|7|TC33|200|12|TC12|35|3|4340|4049|8.007|
|TC17|50|9||||TC13|35|5|2665|2498|6.800|
||VIII.|RESULT|S AND DISC|USSION||TC14|35|7|1980|1780|7.100|
|Table 2<br>pplied on<br>lemente|summari<br>the 33 te<br>d usin|zes the b<br>st cases T<br>ava lan|est results o<br>C1-TC33.<br>ae Furth|f the VN<br>The VNS<br>rmore t|S algorithms<br>algorithm is<br>he tests were|TC15|50|5|5772|5299|6.004|
|p<br>rried out<br>nd 2 GB R|g<br>on a Pent<br>AM with|g<br>ium(R), d<br>Window|g.<br>ual-core C<br>s Vista SP1|,<br>PU T430<br>.|<br>0- 2.10 GHz,|TC16|50|7|4116|3822|5.009|
|||||||TC17|50|9|3312|3112|6.474|



Table 2 summarizes the best results of the VNS algorithms applied on the 33 test cases TC1-TC33. The VNS algorithm is implemented using Java language. Furthermore, the tests were carried out on a Pentium(R), dual-core CPU T4300- 2.10 GHz, and 2 GB RAM with Windows Vista SP1. 

6 

## **_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 



|TC18|50|10|3002|2825|6.506|
|---|---|---|---|---|---|
|TC19|75|7|9556|8680|6.714|
|TC20|75|9|7502|6866|7.303|
|TC21|75|10|6752|6233|6.410|
|TC22|100|7|18557|17541|5.004|
|TC23|100|9|17373|16185|6.074|
|TC24|100|10|14245|13148|6.095|
|TC25|100|12|12216|11170|6.147|
|TC26|150|7|49165|45330|5.542|
|TC27|150|9|49056|46121|4.685|
|TC28|150|10|38394|35708|7.420|
|TC29|150|12|33388|30773|8.146|
|TC30|200|7|83511|76447|7.305|
|TC31|200|9|76780|68330|7.415|
|TC32|200|10|64016|57008|6.001|
|TC33|200|12|57662|52003|6.099|



In Table 2, for each instance several parameters are shown such as the total time of the initial objective function value, the best value of the objective function found by the VNS, and the execution time taken to run the proposed algorithm. The results in Table 2 are further illustrated in figure 7. Figure 7 shows the percentage of objective functions improvement using the VNS algorithm. It is worth noting the VNS algorithm was able to improve the solution by at least 5% in less than 10 seconds. As for the significant improvement in TC1 and TC5 and the minor improvement in TC8, it is mainly affected by the traversal time 

from one patient to another and the priority assigned to every patient. This is clarified in the example shown in Tables 3-a and Table 3-b. 



Fig. 7. Percentage of objective function improvement by VNS algorithm 

Table 3 shows details related only to TC1. The parameters shown in the Table are the patient number, operation time taken at every patient location ti, the traversal time from patient i to patient j tij, the priority assigned to every patient PRi and the objective function OF. 

Table - 3 Priorities and traversal time between patients in TC1. 

|(a<br>**Patient#**|)<br>**t**|**t**|**PR**|**OF**||(|b)|||
|---|---|---|---|---|---|---|---|---|---|
||**i**|**ij**|**i**||**Patient#**|**ti**|**tij**|**PRi **|**OF**|
|1|5|7|1|12|5|8|1|1|9|
|2|5|9|2|28|6|5|4|1|9|
|3|7|6|1|13|4|5|1|1|6|
|4|5|5|1|10|7|5|1|1|6|
|5|8|5|1|13|1|5|1|1|6|
|6|5|4|1|9|8|7|2|2|18|
|7|5|4|1|9|2|5|1|1|6|
|8|7|3|1|10|3|7|5|1|12|
|Objective|Fun|ctio|n|104|Best Objec|tive|Funct|ion|72|



7 

**_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 



In Table 3-a, the mobile clinic path to serve all patients was sequential from 1 till 8 with almost all patients had low priorities with initial objective function equals to 104. The value of the objective function is improved to 72 as shown in Table 3-b by simply changing the order of reaching patients. It should be clear from this example that as patients don’t have competing priorities and there exist a chance to find neighbor patients living close to each other, there is a chance of a significant improvement in the objective function. 

## IX. CONCLUSION 

In this paper, we presented our vision to solve the mobile clinic routing problem. The problem entails the assignment of a maximum number of patients with priorities to mobile clinics in such a way as to reduce the total mobile clinics traversal time. We presented a variable neighborhood search (VNS) algorithm for the MCRP. VNS is a metaheuristic that we were the first to utilize to solve the assignment problem in the mobile clinic routing problem. The methods of the VNS have been enhanced to solve this problem. One contribution of this work is proposing and testing a unique algorithm (VNS) that has not been used before for solving the MCRP problem. The results indicate that our VNS algorithm was able to improve the solution in at least 5% in less than 10 seconds. This is due to the VNS nature that focuses on the Diversification and then intensification methods. A unique constructive method has been used to boost the quality of the initial population. Clearly, this process affected the final results as it aided in yielding the best known solution at earlier stages of the iterations giving an edge when compared to other related work and research that did not focus on generating such enhanced solutions. Additionally, the improvement and heuristic improvement methods have been also reinforced to give better results. 

## V. REFERENCES 

- [1]. WHO. (2020). _World Health Organization announces COVID-19 outbreak a pandemic_ .  [cited 2022; Available from: <u>https://www.euro.who.int/en/health-topics/healthemergencies/coronavirus-covid-</u> 

   - <u>19/news/news/2020/3/who-announces-covid-19outbreak-a-pandemic.</u> 

- [2]. McGowan, C.R., et al. (2020). Mobile clinics in humanitarian emergencies: a systematic review. Conflict and health, 14(1): p. 1-10. 

- [3]. RHC. (2015). RURAL HEALTH CARE REVIEW COMMITTEE REPORT. 2022]; Available from: http://www.health.alberta.ca/newsroom/pub-annualreports.html. 

- [4]. Hansen, P. and N. Mladenović .(2001). Variable neighborhood search: Principles and applications. European journal of operational research, 130(3): p. 449467. [5]. Hislop, D., R. Bosua, and R. Helms .(2018). 

- [5]. Santa González, R., et al. (2020).Mobile Clinics Deployment for Humanitarian Relief: A Multi-period Location-routing Problem: CIRRELT. 

- [6]. Yücel, E., et al. (2020). A data-driven optimization framework for routing mobile medical facilities. Annals of Operations Research, 291(1): p. 1077-1102. 

- [7]. Munawar, H.S., et al. (2021). Towards smart healthcare: Uav-based optimized path planning for delivering COVID-19 self-testing kits using cutting edge technologies. Sustainability, 13(18): p. 10426. 

- [8]. Salman, F.S., et al. (2021). Modeling mobile health service delivery to Syrian migrant farm workers using call record data. Socio-Economic Planning Sciences: p. 101005. 

- [9]. Chênes, C., et al. (2022). Use of Physical Accessibility Modelling in Diagnostic Network Optimization: A Review. Diagnostics, 12(1): p. 103. 

- [10]. Attipoe-Dorcoo, S., et al. (2021). Geographical Influence of Mobile Clinics in the Southern United States. Applied Spatial Analysis and Policy, 14(1): p. 81-87. 

- [11]. Almeida, T., J.B. de Vasconcelos, and G. Pestana.(2020). Attipoe-Dorcoo, S., et al., Mobile health clinic model in the COVID-19 pandemic: lessons learned and opportunities for policy changes and innovation. International Journal for Equity in Health, 19(1): p. 1-5. 

- [12]. Sunitha, G. (2021). Intelligent System to Find the Health Care Centers for Senior Citizens Based on Disease and Nearest Locations using GPS. Turkish Journal of Computer and Mathematics Education (TURCOMAT), 12(2): p. 2140–2150-2140–2150. 

- [13]. Yan, L.L., et al. (2021). Effectiveness of a primary carebased integrated mobile health intervention for stroke management in rural China (SINEMA): A clusterrandomized controlled trial. PLoS medicine, 18(4): p. e1003582. 

- [14]. Sigwele, T., et al. (2018).Intelligent and energy efficient mobile smartphone gateway for healthcare smart devices based on 5G. in 2018 IEEE Global Communications Conference (GLOBECOM). IEEE. 

- [15]. Galvao, R.D., L.G.A. Espejo, and B. Boffey. (2002). A hierarchical model for the location of perinatal facilities in the municipality of Rio de Janeiro. European Journal of Operational Research, 138(3): p. 495-517. 

- [16]. Goldstein, S.M., et al. (2002). The effect of location, strategy, and operations technology on hospital performance. Journal of Operations Management, 20(1): p. 63-75. 

- [17]. Munavalli, J.R., et al. (2021). Workflow-based Adaptive Layout Design to Improve the Patient Flow in the Outpatient Clinics. Annals of the Romanian Society for Cell Biology: p. 8249-8257. 

- [18]. Wood, D.C. (1968). A system for computing university examination timetables. The Computer Journal, 11(1): p. 41-47. 

8 

## **_International Journal of Engineering Applied Sciences and Technology, 2022_ Vol. 6, Issue 9, ISSN No. 2455-2143, Pages 1-9** 

Published Online January 2022 in IJEAST (http://www.ijeast.com) 



- [19]. Mladenović, N. and P. Hansen. (1997). Variable neighborhood search. Computers & operations research, 24(11): p. 1097-1100. 

- [20]. Remde, S., et al. (2007). Evolution of fitness functions to improve heuristic performance. in International Conference on Learning and Intelligent Optimization. Springer. 

- [21]. Hsiao, P.-C., T.-C. Chiang, and L.-C. Fu. (2012). A vnsbased hyper-heuristic with adaptive computational budget of local search. in 2012 IEEE congress on evolutionary computation. IEEE. 

9 

