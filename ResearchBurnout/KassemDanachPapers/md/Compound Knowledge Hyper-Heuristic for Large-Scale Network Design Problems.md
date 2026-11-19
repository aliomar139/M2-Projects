

# **Compound Knowledge Hyper-Heuristic for Large-Scale Network Design Problems** Kassem Danach, Jomana Al Haj Hassan, Mariem Belhor 



## **To cite this version:** 

Kassem Danach, Jomana Al Haj Hassan, Mariem Belhor. Compound Knowledge Hyper-Heuristic for LargeScale Network Design Problems. ROADEF 2026, Université de Tours [UT], Feb 2026, Tours, France. ⟨hal05534814⟩ 

## **HAL Id: hal-05534814** 

**https://hal.science/hal-05534814v1** 

Submitted on 3 Mar 2026 

**HAL** is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers. 

L’archive ouverte pluridisciplinaire **HAL** , est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés. 



HAL Authorization 

# Compound Knowledge Hyper-Heuristic for Large-Scale Network Design Problems 

Kassem Danach<sup>1</sup> , Jomana Al Haj Hassan<sup>2</sup> , Mariem Belhor<sup>3</sup> 

> 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon 

```
kassem.danach@mu.edu.lb
```

> 2 Department of Management Information Systems, Faculty of Business Administration, Lebanese International University, Beirut P.O. Box 1464/04, Lebanon 

```
jomana.hajhassan@liu.edu.lb
```

Laboratoire des Technologies Innovantes (LTI, UR 3899), University of Picardie Jules Verne, Avenue des Facultés, Le Bailly, 80000 Amiens, France 

```
mariem.belhor@u-picardie.fr
```

**Keywords** : _Hyper-heuristics, Knowledge-guided optimization, Reinforcement learning._ 

## **1 Introduction** 

Large-scale network design (facility opening, capacity allocation, flow routing) is naturally modeled as mixed-integer optimization but quickly becomes intractable under heterogeneous costs, asymmetric distances, tight capacities, and realistic side constraints. Classical metaheuristics (GA, SA, VNS) improve locally yet often stagnate or overfit instance structure, while purely learning-based controllers risk overfitting and lack interpretability. We propose **CK-HH** , a two-layer <u>Compound</u> Knowledge Hyper-Heuristic that fuses encoded analytical/empirical/contextual knowledge with an adaptive bandit/RL controller selecting among low-level heuristics (e.g., swaps, greedy insertion, SA/VNS, fix-and-optimize). A hyper-heuristic is a reinforcement-learning–driven, high-level strategy that selects or composes low-level heuristics during search [1].The state combines solution and runtime features; rewards balance improvement, time, and diversity [2]. This hybrid yields interpretable guidance early and data-driven intensification near convergence, improving scalability and stability on large instances. 

## **2 Problem Definition** 

We model capacitated network design (covering capacitated hub location and hub–spoke routing) on a directed graph _G_ = ( _V, E_ ) with candidate hubs _H ⊆ V_ and demand nodes _D ⊆ V_ . Each _i ∈ D_ has demand _di ≥_ 0; opening hub _k ∈ H_ costs _Fk_ and yields capacity _Uk_ ; assignment and routing costs are _cij ≥_ 0 and _γpq ≥_ 0. Decisions: 

_yk ∈{_ 0 _,_ 1 _}_ ( _k ∈ H_ ) _, xij ∈{_ 0 _,_ 1 _}_ ( _i ∈ D, j ∈ H_ ) _, zpq ≥_ 0 (( _p, q_ ) _∈ E_ ) _._ 



<!-- Start of picture text -->
min � � cijxij + � Fkyk  + � γpqzpq (1)<br>i∈D j∈H k∈H ( p,q ) ∈E<br>s.t. � xij = 1 ∀i ∈ D (2)<br>j∈H<br>� dixij ≤ Ujyj ∀j ∈ H (3)<br>i∈D<br>� zpq − � zqp =  bp ∀p ∈ V (4)<br>q :( p,q ) ∈E q :( q,p ) ∈E<br>xij ∈{ 0 ,  1 }, yj ∈{ 0 ,  1 }, zpq ≥ 0 .<br><!-- End of picture text -->

Here _bp_ is the net supply/demand induced by assignments. Extensions (optional): budget on openings, arc capacities, hop/service limits, multi-allocation, or multi-commodity flows. 

## **3 Compound Knowledge Hyper-Heuristic (CK-HH)** 

CK-HH has two layers linked by a compound gate. The knowledge layer fuses analytical rules (e.g., flow conservation, dominance, triangle inequality, capacity tightness), empirical signals from elite solutions and runtime traces, and contextual descriptors (node density, demand skewness, hub proximity, congestion) to guide the search. The adaptive layer uses a contextual bandit/RL controller mapping state _st_ (solution + runtime features) to an LLH _ht ∈H_ (swaps, greedy insertion, SA/VNS, local B&B fix-and-optimize), with reward balancing improvement, time, and diversity. A gate _α_ ( _t_ ) _∈_ [0 _,_ 1] blends knowledge and learning—analytic guidance early, learned policy later—yielding interpretable, adaptive control across scales. 

## **4 Experimental Setup and Results** 

We evaluate on public CAB and Australian Post instances up to _n_ = 200 nodes with heterogeneous capacities and costs, comparing CK-HH against SA, GA, VNS, and an RL-based hyper-heuristic (RL-HH). Each instance is run ten times under a fixed time budget; we report best/average objective, runtime, variability, and improvement over the best baseline. Implementations use Python 3.11. CK-HH consistently yields higher-quality solutions with competitive runtimes; on large instances ( _n ≥_ 150) it improves the strongest baseline by 3–6% with lower variance. Knowledge-guided phases accelerate early descent and prevent stagnation, while learned policies refine near convergence. The approach is especially effective under tight capacities and asymmetric costs, and policies trained on medium sizes generalize to larger instances without retraining, confirming robustness and scalability. 

## **5 Conclusion and Perspectives** 

We introduced CK-HH, a dual-layer, knowledge-and-learning hyper-heuristic for large-scale network design. By fusing analytical structure with adaptive control, CK-HH improves solution quality, stability, and interpretability. Future work includes multi-objective extensions (cost, reliability, sustainability), integration with branch-and-cut/decomposition, and application to industrial-scale instances with uncertainty. 

## **References** 

- [1] Kassem Danach, Hassan Harb, Semaan Amine, and Mariem Belhor. Neuhh: A neuromorphic-inspired hyper-heuristic framework for solving the capacitated singleallocation p-hub location routing problem. <u>Vehicles,</u> 7(2):61, 2025. 

- [2] Kassem Danach, Hassan Harb, Hussin Jose Hejase, and Louai Saker. A hybrid metaheuristic framework with reinforcement learning–based heuristic selection for large-scale combinatorial optimization. European <u>Journal</u> of Pure and Applied Mathematics, 18(3):6602–6602, 2025. 

