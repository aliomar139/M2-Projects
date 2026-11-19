

## **Hyperheuristics in Logistics** 

Kassem Danach 



### **To cite this version:** 

Kassem Danach. Hyperheuristics in Logistics. Combinatorics [math.CO]. Ecole Centrale de Lille, 2016. English. ⟨NNT : 2016ECLI0025⟩. ⟨tel-01485160⟩ 

### **HAL Id: tel-01485160** 

**https://theses.hal.science/tel-01485160v1** 

Submitted on 8 Mar 2017 

**HAL** is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers. 

L’archive ouverte pluridisciplinaire **HAL** , est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés. 



HAL Authorization 

N<sup>_o_</sup> d’ordre: 315 

## Centrale Lille 

## **THÈSE** 

présentée en vue d’obtenir le grade de 

#### **DOCTEUR** 

en 

_Automatique, Génie Informatique, Traitement du Signal et des Images_ 

par 

**Kassem Danach** 

DOCTORAT DELIVRE PAR CENTRALE LILLE 

## **Hyperheuristiques pour des problèmes** 

## **d’optimisation en logistique** 

## **Hyperheuristics in Logistics** 

Soutenue le 21 decembre 2016 devant le jury d’examen: 

|**President:**|Pr. Laetitia Jourdan|Université de Lille 1, France|
|---|---|---|
|**Rapporteurs:**|Pr. Adnan Yassine|Université du Havre, France|
||Dr. Reza Abdi|University of Bradford, United Kingdom|
|**Examinateurs:**|Pr. Saïd Hanafi|Université de Valenciennes, France|
||Dr. Abbas Tarhini|Lebanese American University, Lebanon|
||Dr. Rahimeh Neamatian Monemin|University Road, United Kingdom|
|**Directeur de thèse:**|Pr. Frédéric Semet|Ecole Centrale de Lille, France|
|**Co-encadrant:**|Dr. Shahin Gelareh|Université de l’ Artois, France|
|**Invited Professor:**|Dr. Wissam Khalil|Université Libanais, Lebanon|



Thèse préparée dans le Laboratoire CRYStAL 

École Doctorale SPI 072 (EC Lille) 

**2** 

### **Acknowledgements** 

Firstly, I would like to express my sincere gratitude to my advisor Prof. Frédéric Semet, Dr. Shahin Gelareh and Dr. Wissam Khalil for their continuous support of my Ph.D study and related research, for their patience, motivation, and immense knowledge. Their guidance helped me in all the time of research and writing of this thesis. 

I would also like to thank my parents for their wise counsel and sympathetic ear. I would like express appreciation to my beloved wife Jomana Al-haj Hasan who spent sleepless nights with and was always my support in the moments when there was no one to answer my queries. 

Finally, there are my children, who have given me much happiness and keep me hopping. My son, Mahdi, has grown up watching me study and juggle with family and work. Abbass, the little one, who always try to do everything to make his presence felt. I hope I have been a good father and that I have not lost too much during the tenure of my study. 

**3** 

#### **Resumé** 

Le succès dans l’utilisation de méthodes exactes dans l’optimisation combinatoire à grande échelle est encore limité à certains problèmes, et peut-être des classes spécifiques d’instances de problèmes. Le moyen alternatif consiste soit à utiliser des métaheuristiques ou des mathématiques qui utilisent des méthodes exactes à certains égards. Le concept d’hyperheuristique (HH) est une généralisation de celle des métaheuristiques. Dans le contexte de l’optimisation combinatoire, nous nous intéressons à l’heuristique pour choisir l’heuristique. Les deux catégories hyperheuristiques principales de la classification précédente sont: 1) la sélection heuristique, qui considère une méthode pour sélectionner des heuristiques à partir d’un ensemble d’heuristiques existantes, et 2) la génération heuristique qui consiste à générer de nouvelles heuristiques à partir des composantes des heuristiques existantes. 

Dans cette thèse, nous nous concentrons sur l’optimisation hyperheuristique des problèmes logistiques. Nous présentons une revue de littérature détaillée sur les termes origine, concept, domaine d’application, etc. Ensuite, deux problèmes logistiques ont été choisis pour lesquels nous avons proposé HH. Sur la base de la structure générale d’une solution réalisable et en exploitant les informations cachées dans les données d’entrée, nous définissons un ensemble d’heuristiques possibles pour chaque problème. Nous nous concentrons ensuite sur la proposition d’un cadre hyperheuristique qui effectue une recherche dans l’espace des algorithmes heuristiques et apprend comment changer l’heuristique en place d’une manière systématique le long du processus de telle sorte qu’une bonne séquence 

**4** 

d’heuristiques produit des solutions de haute qualité. Notre cadre hyperheuristique est équipé d’un mécanisme d’apprentissage qui apprend l’environnement et guide la transition d’une heuristique historique à une autre jusqu’à ce que l’algorithme global se termine. 

Le premier problème abordé est le problème d’ordonnancement de la plateforme de workover (WRSP), qui consiste à trouver le meilleur horaire pour un certain nombre de plates-formes de workover pour minimiser la perte de production, associée à un grand nombre de puits en attente de maintenance. Un algorithme d’hyperheuristique de sélection est proposé, qui est guidé par un mécanisme d’apprentissage conduisant à un choix approprié de mouvements dans l’espace des heuristiques qui sont appliquées pour résoudre le problème. Nos expériences numériques sont menées sur des exemples d’une étude de cas de Petrobras, la Société nationale brésilienne du pétrole, et ont été comparées avec une méthode exacte prouvant son efficacité. 

Le deuxième problème est une variante du problème de routage d’emplacement de concentrateur, qui cherche à diviser les nœuds en moyeux et rayons. Deux HH différentes ont été appliquées à deux variantes de ce problème, qui sont dérivées d’un problème d’acheminement de localisation de concentrateur de capacité d’allocation unique et diffèrent principalement dans la définition de la capacité. Dans le premier, le nombre de rayons pouvant être attribué à chaque hub est limité; Tandis que dans la seconde, c’est le volume de l’écoulement circulant sur la voie du rayon-niveau. De plus, cinq relaxations lagrangiennes (LR) ont été proposées pour le premier problème afin d’utiliser certains résultats pendant le processus de 

**5** 

HH. Les résultats de calcul prouvent l’efficacité de HH et la pertinence d’inclure l’information LR. Enfin, nous comparons les performances de plusieurs HH proposées dans la littérature pour le problème précédemment abordé, avec différentes méthodes de sélection heuristique telles que la sélection aléatoire, la fonction de choix, Q-Learning et la colonie de fourmis. 

**6** 

# **Contents** 

|**Acknow**|**ledgements**<br>**2**|
|---|---|
|**Conten**|**ts**<br>**6**|
|**List of**|**Tables**<br>**11**|
|**List of**|**Figures**<br>**13**|
|**1**<br>**Hyp**|**erheuristic: A General Overview**<br>**15**|
|1.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>15|
|1.2|Heuristics, Metaheuristics and Matheuristics . . . . . . . . . . . .<br>18|
|1.3|Hyperheuristics . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>22|
||1.3.1<br>Hyperheuristic Classification . . . . . . . . . . . . . . . .<br>25|
||1.3.2<br>Move Acceptance Criteria . . . . . . . . . . . . . . . . .<br>29|
||1.3.3<br>Termination Criteria<br>. . . . . . . . . . . . . . . . . . . .<br>34|
|1.4|State of the art . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>35|
|1.5|Existing and the Proposed Framework . . . . . . . . . . . . . . .<br>39|
|1.6|Contributions and Overview<br>. . . . . . . . . . . . . . . . . . . .<br>42|



|**8**||**CONTENTS**|
|---|---|---|
|**2**<br>**Wor**|**kover**|**Rig Problem**<br>**45**|
|2.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>45|
|2.2|Litera|ture review<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>47|
||2.2.1|Objective and contribution . . . . . . . . . . . . . . . . .<br>49|
|2.3|Proble|m Description<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>51|
|2.4|Mathe|matical Model<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>51|
||2.4.1|Workover Rig Scheduling (WRS) Problem<br>. . . . . . . .<br>52|
||2.4.2|Valid inequalities . . . . . . . . . . . . . . . . . . . . . .<br>55|
||2.4.3|Preprocessing . . . . . . . . . . . . . . . . . . . . . . . .<br>57|
||2.4.4|Illustrative example . . . . . . . . . . . . . . . . . . . . .<br>58|
|2.5|Hyper|heuristic for WRS Problem. . . . . . . . . . . . . . . . . .<br>58|
||2.5.1|Reinforcement learning. . . . . . . . . . . . . . . . . . .<br>63|
|2.6|Nume|rical experiments . . . . . . . . . . . . . . . . . . . . . . .<br>66|
|2.7|Summ|ary, conclusion and outlook to future work<br>. . . . . . . . .<br>74|
|**3**<br>**Cap**|**acitate**|**d Single Allocation p-Hub Location Routing Problem**<br>**77**|
|3.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>77|
|3.2|Mathe|matical Formulation . . . . . . . . . . . . . . . . . . . . .<br>87|
||3.2.1|(CSA_p_HLRP-1-F1) . . . . . . . . . . . . . . . . . . . . .<br>88|
||3.2.2|(CSA_p_HLRP-1-F2) . . . . . . . . . . . . . . . . . . . . .<br>91|
||3.2.3|(CSA_p_HLRP-2). . . . . . . . . . . . . . . . . . . . . . .<br>94|
|3.3|Soluti|on algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . .<br>97|
||3.3.1|Lagrangian relaxation<br>. . . . . . . . . . . . . . . . . . .<br>98|



**CONTENTS** 

**9** 

||3.3.2|Hyperheuristic for CSA_p_HLRP-1 and CSA_p_HLRP-2 . . . 104|
|---|---|---|
|3.4|Comp|utational experiments . . . . . . . . . . . . . . . . . . . . . 117|
||3.4.1|CSA_p_HLRP-1 Computational experiments<br>. . . . . . . . 118|
||3.4.2|CSA_p_HLRP-2 Computational experiments<br>. . . . . . . . 129|
|3.5|Concl|usion and future work. . . . . . . . . . . . . . . . . . . . . 129|
|**4**<br>**Sele**|**ction M**|**ethods**<br>**137**|
|4.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
|4.2|The Pr|oposed Selection Methods . . . . . . . . . . . . . . . . . . 139|
||4.2.1|Random Selection Based Hyperheuristic. . . . . . . . . . 140|
||4.2.2|Greedy Based Hyperheuristic<br>. . . . . . . . . . . . . . . 142|
||4.2.3|Peckish Based Hyperheuristic . . . . . . . . . . . . . . . 142|
||4.2.4|Choice Function Based Hyperheuristic<br>. . . . . . . . . . 143|
||4.2.5|Reinforcement Learning . . . . . . . . . . . . . . . . . . 145|
||4.2.6|Metaheuristics Based Hyperheuristic<br>. . . . . . . . . . . 148|
|4.3|Nume|rical Results. . . . . . . . . . . . . . . . . . . . . . . . . . 156|
|4.4|Concl|usion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157|
|**5**<br>**Gen**|**eral Co**|**nclusion**<br>**161**|
|**Bibliogr**|**aphy**|**167**|



**10** 

# **List of Tables** 

|2.1|Model Parameters and variables. . . . . . . . . . . . . . . . . . .|52|
|---|---|---|
|2.2|Best solution and execution time results of the two methods.<br>. . .|68|
|2.3|Computational results of our branch, price and cut.<br>. . . . . . . .|73|
|3.1|A summary of main elements of the relevant contributions in liter-||
||ature.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|84|
|3.2|CSA_p_HLRP-1-F1 and CSA_p_HLRP-1-F2 Models Parameters. . . .|87|
|3.3|The decision variables for CSA_p_HLRP-1-F1 and CSA_p_HLRP-1-F2.|88|
|3.4|CSA_p_HLRP-2 Model Parameters.<br>. . . . . . . . . . . . . . . . .|95|
|3.5|CSA_p_HLRP-2 Decision Variables. . . . . . . . . . . . . . . . . .|95|
|3.6|Comparison of the quality between benders decompositions and||
||the proposed hyperheuristic with and without LR . . . . . . . . .|121|
|3.7|Number of each heuristic in each instance was applied. . . . . . .|123|
|3.8|Comparison of the quality between the initial objective function||
||taken by the proposed hyperheuristic with and without LR<br>. . . .|124|
|3.9|HH results for large instances of pHub location problem. . . . . .|125|



**12 LIST OF TABLES** 

- 3.10 A comparison between results of Matheuristic with that of LR HH. 126 3.11 Lagrangian relaxation results. . . . . . . . . . . . . . . . . . . . . 128 3.12 Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), cab instance with 25 nodes 133 

- 3.13 Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 25 nodes . . 134 

- 3.14 Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 40 nodes . . 135 

- 3.15 Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 50 nodes . . 136 

# **List of Figures** 

|1.1|The general scheme of hyperheuristic framework. . . . . . . . . .|25|
|---|---|---|
|1.2|A classification of hyperheuristic approaches (Burke et al.,2010) .|29|
|1.3|The Proposed Hyperheuristic Framework. . . . . . . . . . . . . .|42|
|2.1|Illustrative example with_|R|_= 3,_|J_ <sup>+</sup>_|_= 7and_|T |_= 16. Every||
||machine starts by processing job0at_t_= 0and terminates at the||
||same job as the job processed on it.. . . . . . . . . . . . . . . . .|58|
|2.2|The wells are uniformly distributed within a given geographical||
||zone.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|66|
|2.3|Execution time of each method.<br>. . . . . . . . . . . . . . . . . .|70|
|2.4|The constructive and improvement heuristics calls distribution by||
||each method.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|71|
|2.5|the mutation and crossover heuristics calls distribution by each||
||proposition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
|2.6|insert/drop and reconstructive heuristics calls distribution by each||
||method. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|



**LIST OF FIGURES** 

**14** 

|3.1|A solution of network with 3 hubs and 10 nodes.<br>. . . . . . . . .|80|
|---|---|---|
|3.2|A solution of network with 3 hubs and 10 nodes.<br>. . . . . . . . .|85|
|3.3|Civil Aeronautics Board data with 25 nodes. . . . . . . . . . . . .|118|
|3.4|Australia post data with 200 nodes. . . . . . . . . . . . . . . . . .|119|
|3.5|Optimal solution for CAB25 with_p_=5,_q_=13,_α_=0.8,_β_=0.01. . . .|130|
|3.6|Optimal solution for CAB25 with_p_=5,_q_=13,_α_=0.8,_β_=0.05. . . .|130|
|3.7|Optimal solution for CAB25 with_p_=5,_q_=13,_α_=0.8,_β_=0.2.<br>. . .|130|
|3.8|HH execution time in CSA_p_HLRP-2.. . . . . . . . . . . . . . . .|131|
|4.1|Algorithm selection model taken byRice(1976).<br>. . . . . . . . .|139|
|4.2|A general schema of the VNS algorithm. . . . . . . . . . . . . . .|155|
|4.3|The process of the proposed VNS Hyperheuristic. . . . . . . . . .|155|
|4.4|HH results within different heuristic selection methods . . . . . .|157|
|4.5|HH results within different peckish selection methods . . . . . . .|158|
|4.6|HH results within different RL selection methods . . . . . . . . .|158|
|4.7|HH results within simple random, random descent, random per-||
||mutation descent, greedy and choice function selection methods<br>.|159|



# **Chapter 1** 

# **Hyperheuristic: A General Overview** 

## **1.1 Introduction** 

The term _Optimization_ , according to Merriam Webster<sup>1</sup> , is a process or methodology of making something as fully perfect, or effective as possible. We seek a state from among the set of possible states with the most cost effective or highest achievable performance under given constraints. In mathematical optimization with one single objective, we search a maximum or a minimum value of an objective function of several variables over a set of feasible solutions defined by a set of constraints. When both the objective function and the search space could be described by means of linear terms and linear system, respectively, linear programming based 

> 1www.merriam-webster.com/dictionary/mW 

**Hyperheuristic: A General Overview** 

**16** 

techniques are used to solve such models and find the optimum (optima). A combinatorial problem (COP) is defined as a problem of finding an optimal solution from a finite set or possibly countable infinite set of searching area (Schrijver, 2005). Usually, COPs involve grouping, ordering, or assignment of a discrete finite set of objects with some predefined conditions. Many problems in the real-life from telecommunications, transportation, logistics and energy sectors to modeling of social networks, bio-informatics and even archeology and beyond are modeled as COPs. Some classical and well-studied problems of COPs that often appear as subproblem in other more complex problems includes: knapsack problems (Martello and Toth, 1990), traveling salesman problems (Applegate et al., 2011), vehicle routing problems (Toth and Vigo, 2014) and variants of facility location problems (Drezner and Hamacher, 2001) among many others. 

In this thesis, we focus on a couple of problems arising in logistics and network design for management of the flow of resources between the point of origin and the point of consumption in order to meet some requirements. Such problems, like many other problems in logistics, are categorized as COPs and they also include continuous decision variables. These problems are often modeled as mixed integer 

**1.1 Introduction** 

**17** 

programming (MIP) models which can be expressed as follows: 

Objective : min _c_<sup>_T_</sup> _x_ + _d_<sup>_T_</sup> _y_ 

Constraints : _Ax_ + _By_ = _b_ linear constraints _x ∈_ R<sup>_m_1</sup> _l ≤ x ≤ u_ bound constraints _y ∈_ Z<sup>_m_2</sup> integrality constraints 

The optimization techniques proposed in the literature, are classified in two main categories: exact method and non-exact method(variants of heuristic approaches). Exact optimization methods provide provably optimal solutions, when exists, while the non-exact methods (which might also be based on MIP models and mathematical programming). Yet, there is a serious bottleneck when dealing with exact methods including general-purpose solvers: Small instances of real-life problems can be often solved to optimality in reasonable times when a good description of polytope (in terms of tightness of LP relaxation, additional valid inequalities are available etc) is available while moderate size instances may be solved using efficient and specialized methods in reasonable times. However, the larger ones are very less likely to be solved to optimality and often even finding a feasible solution for such problems may become very difficult task for exact approaches. At this point, non-exact methods such as those combining heuristic techniques with mathematical programming techniques such as Lagrangian heuristics, LP-based heuristic and primal-dual heuristic. or the different approaches such as specialize ad-hoc heuristics, evolutionary or metaheuristic approaches that are developed to 

**Hyperheuristic: A General Overview** 

**18** 

find very good feasible solutions become inevitable. Sometimes in exact methods, an indication of optimality can be provided, the non-exact often do not provide any indication. 

In the remainder of this chapter, we elaborate further on heuristic optimization and explain some differences among different techniques and paradigms. We then focus on the context of hyperheuristic, the paradigm, general framework, steps, and different components. 

## **1.2 Heuristics, Metaheuristics and Matheuristics** 

_Heuristics_ are often problem-dependent techniques that are usually adapted to the problem at hand and they try to take full advantage of the particularities (structure or other kind of information) of the problem. However, since they are often too biased, they usually get trapped in a local optimum and thus fail, in general, to obtain the global optimum solution, and no guarantee if it get the optimal solution or not. 

_Metaheuristic_ is a class of approximate methods developed in the early 1980s. Metaheuristics are designed to solve complex optimization problems; in fact, the classical heuristics were not always effective and efficient, as they were time consuming or there were some limitation to help them escape from a local optima. 

**1.2 Heuristics, Metaheuristics and Matheuristics** 

**19** 

Metaheuristics are problem-independent techniques, pattern or paradigms. For example Simulated Annealing (SA) (Kirkpatrick, 1984) imitates the cooling of material in a heat bath and maps the objective function optimal of the optimization problem on the optimal energy level function of the hot material such that annealing is the process in which the temperature of a molten substance is slowly reduced until the material crystallises to give a large single crystal. 

Metaheuristic, can be defined as an iterative generation of a process, which guides a subordinate heuristic by combining intelligently different concepts for exploring and exploiting the search space (Osman and Laporte, 1996). 

As such, the metaheuristics are independent of any specificity of the problem and, therefore, can be used as general paradigm. In general, they are less greedy approaches in characteristic. In fact, they may even accept a temporary deterioration of the solution (e.g. SA), which allows them to explore more thoroughly the solution space and thus to get a hopefully better solution (that sometimes will coincide with the global optimum). Although a metaheuristic is a problem-independent technique, it is nonetheless necessary to do some fine-tuning of its associated parameters in order to adapt the technique to the problem at hand. 

To illustrate the concept of metaheuristic, we should first distinguish between heuristic algorithms and metaheuristic algorithm. The main objective of heuristics is to obtaining a solution at an acceptable cost for a wide range of problems. Heuristics do not have an approximation guarantee on the quality of the obtained 

**Hyperheuristic: A General Overview** 

**20** 

solutions. On the other hand, Metaheuristics are general-purpose algorithms that can be regarded as upper level general methodologies employed as guiding strategy for the heuristics. 

In metaheuristics approach, two strategies must be taken in account (Talbi, 2009): 

1. _Diversification_ : that explores the search space to avoid getting stuck in the same or similar areas of feasible space. 

2. _Intensification_ : that emphasizes on concentrating search in the promising regions previously found, in order to exploiting the potentials. 

Several families of metaheuristic algorithms are proposed in the literature such as simulated annealing (SA) (Aarts and Korst, 1988), tabu search (TS) (Glover, 1989), genetic algorithm (GA) (Davis, 1991), GRASP (Dyall et al., 1989), variable neighborhood search (VNS) (Mladenovi´c and Hansen, 1997a), adaptive large neighborhood search (ALNS) (Ahuja et al., 2000), path relinking (Glover, 1998), particle swarm optimization (PSO) (Eberhart et al., 1995), scatter search (SS) (Glover, 1998), ant colony (Dorigo et al., 2000), among others. 

Metaheuristic algorithms can be categorized with respect to different characteristics as follows. The _deterministic_ ones offer the same results for several runs while the _non-deterministic_ ones may report different results per different invocations. 

**1.2 Heuristics, Metaheuristics and Matheuristics** 

**21** 

One can distinguishes among metaheuristic algorithms by the algorithm that use single solution ( _trajectory methods_ ) at each iteration of the search such as local search, SA, TS, VNS, ALNS, GRASP, path relinking, etc, and those which use multiple solutions ( _population-based methods_ ) and contain more than one (partial) solution such as GA, Ant colony, PSO, scatter search, etc. 

One can also distinguishes between the metaheuristics that make use of some kind of long-term or short term memories and the memory-less ones. Memory based methods are the methods where the search moves are recorded and the future moves should use those information to avoid cycling, previous solution, worse solution etc. such as Tabu Search, PSO, Scatter, Path relinking, Genetic Algorithm, Ant Colony, etc., while others such as GRASP, VNS, etc. are originally memory-less. 

Matheuristic optimization (Bartolini and Mingozzi, 2009) algorithms are a combination between (meta)heuristic approaches and different techniques of mathematical programming. Whether mathematical programming is in charge of solving the problem at hand and (meta)heuristics exploit the primal/dual information to generate better primal bounds or mathematical programming techniques are employed within (meta)heuristics to solve a sub-problem after some variable being fixed (for example a capacitated flow problem, or a linear part of an initially non-linear model where part of variables are fixed by the (meta)heuristic) we are 

**Hyperheuristic: A General Overview** 

**22** 

talking about the matheuristics. Such techniques become very popular as MIP solvers or customized MIP codes have become more effective as primary solvers or as sub-procedures which is due to the advancements that were achieved in the research on mathematical programming, and in particular on discrete optimization. 

## **1.3 Hyperheuristics** 

Hyperheuristics (HH) aims to solve hard computational search problems by automating the design of heuristic methods. The term itself appeared for the first time in 1997, in a study about automated theorem proving (Denzinger et al., 1996). It was given to a protocol that combines several artificial intelligence methods. It was then more adequately used in the year 2000 in connection with combinatorial optimization (Cowling et al., 2001): _heuristics to choose heuristics_ . In this context, a hyperheuristic is a high-level approach that solves hard computational search problems, given a particular problem instance and a number of low-level heuristics, by selecting and applying an appropriate low-level heuristic at each decision point. Even though the term is relatively new, the idea itself dates back to the 1960s (Crowston et al., 1963). A number of researchers developed the automation of the design process of heuristic methods during the 1990s (Fang et al., 1993). Hyperheuristics however go a step beyond metaheuristics. The particularity of hyperheuristics is that their search space is not the usual space of the solutions but is rather the space of heuristics or metaheuristics. 

**1.3 Hyperheuristics** 

**23** 

The concept of _Hyperheuristic_ may be seen a generalization of that of (Meta)heuristics and facilitates classifying a large body of literature of heuristics and metaheuristics that was rather difficult to classify before this. Many definition of the term was found in the literature. Özcan et al. (2010) defines hyperheuristics as methodologies for searching the feasible space, which is generated by a set of low level heuristics while Topcuoglu et al. (2014) defines it as methods for automation of the process of selecting and generating multiple low-level heuristics. 

When we are dealing with certain variants of optimization problems, hyperheuristics are most useful since they only require general knowledge of the problem domain. Cowling et al. (2001) defined the term hyperheuristic as _heuristics to choose heuristics_ . Ochoa et al. (2009) stated that in hyperheuristics research, the importance of increasing the efficiency of the solution method is more important than bettering the solution itself. They also stated that what distinguishes metaheuristics from hyperheuristics is that the latter has a search space of heuristics not of problem solutions, which was previously mentioned by (Ross, 2005). 

Recently, the definition of hyperheuristics has been recently extended to refer to the _search method or learning mechanism to select or generate heuristic to solve combinatorial problem_ . The main objective is to design a generic method which can apply in several problem domains. This method should produce a solution of high quality but the emphasis, in this method, is on the use of low level heuristics that are easy to implement. 

The hyperheuristic framework requires a set of predefined materials. The hyper- 

**Hyperheuristic: A General Overview** 

**24** 

heuristic framework is provided with a set of preexisting simple heuristics, and the challenge is to select or generate the heuristic or the operator that is somehow the most suitable for the current problem state. This process continues until the termination criteria is met.Figure 1.1 depicts a generic hyperheuristic process, which represents the strategy plan in the high level and the major components such as the termination criteria, Low-level heuristics (LLH)/operator selection methods, the acceptance criteria etc. Until the termination criteria is met, HH selects the corresponding LLH (or operator) from an _a priori_ known set according a predefined selection rule and apply it subsequently. The resulted solution at each iteration may or may not be accepted which depends on the predefined acceptance criteria. 

**1.3 Hyperheuristics** 

**25** 



<!-- Start of picture text -->
Operator  1 • Acceptance Criteria<br>1 2 • Termination Criteria<br>Operator 2 heuristics”“generate  Case of  3 • Selection Rules<br>…<br>HYPERHEURISTIC<br>Apply the candidate heuristic<br>(selected or generated)<br>Heuristic1 Heuristic 2 …<br>Solution<br>Unless termination  Evaluation<br>criteria<br>Case of  “select heuristics” Will be accepted or not?<br><!-- End of picture text -->

**Figure 1.1:** The general scheme of hyperheuristic framework. 

### **1.3.1 Hyperheuristic Classification** 

A variety of hyperheuristic approaches was defined in the literature. In this subsection, we present an overview of the different categorizations of hyperheuristic with respect to I) the nature of heuristic search space, II) if it is constructing a solution from scratch or starting from a feasible solution in order to improve it, and III) and the use of learning mechanisms during the search process. Interested readers are 

**Hyperheuristic: A General Overview** 

**26** 

referred to see (Burke et al., 2010, 2009a; Bader-El-Den and Poli, 2008) for further details. 

**Nature of heuristic search space:** While in the beginning the hyperheuristics were to uses (select from among) the pool of existing low-level heuristics, in the late of 2000’s genetic programming started being used for hyperheuristics. This has introduced a new way in which the low-level heuristics were not only _selected_ but also being _generated from existing heuristic components_ . Such an emerging perspective has led to a revised definition: _as an automated methodology to select or generate heuristic in order to solve hard problems_ (Burke et al., 2010). Hence, the HH are now belong to either heuristic selection category or the heuristic generation ones. We are not aware of any work that try to propose any hybrid method. 

Akin to the heuristic selection HH class of hyperheuristics, the other category requires a set of heuristics that are suitable to the problem at hand. The difference is that these heuristics will not be supplied directly to the framework, they will be fragmented into their basic building-blocks so that new heuristics can be generated from them, all in the hopes of achieving a good feasible solution. This class of hyperheuristics led researchers to distinguish between _reusable_ and _disposable_ heuristics. The latter refers to heuristics that were built to be used on a specific problem and cannot be used on others. 

**1.3 Hyperheuristics** 

**27** 

**Solution Target: construction vs. perturbation:** If no initial feasible solution is at hand we talk about the Selection based _construction_ hyperheuristics which aim at select and use construction heuristics in a smart and efficient way that it builds a good solution from the scratch progressively. It starts with an empty solution and uses the _hopefully_ most suitable heuristic, from a pool of pre-existing problem specific construction heuristics, to solve the current problem instance. This process terminates when it reaches the complete feasible solution. This highlights the importance of choosing the best heuristic at each problem instance, because the sequence is not infinite. 

On the other hand, when a feasible solution is indeed at hand, one talks about the selection based _perturbation_ hyperheuristics that require a complete solution to start with. This solution could be generated randomly or using a construction heuristic (not directly related to the HH). Afterwards, the higher-level selection hyperheuristic is supplied with a pool of neighborhood structures and/or simple local search routines. It selects and applies those heuristics to the starting solution in an iterative manner until a stopping condition has been met, unlike the constructive class where the process is ended after a certain number of choices. 

**Selection Methods: with learning or without:** Researchers also classified hyperheuristics based on whether they include learning mechanisms or not (Soubeiga, 2003). Hyperheuristics with learning are methods that record the historical performance of the heuristics available in the search pool, and use learning mechanisms to 

**Hyperheuristic: A General Overview** 

**28** 

study those records and manage the selection process of the heuristics based on it. The Hyperheuristics without learning, select the heuristics from the search pool in a predetermined manner. In Chapter 4, we will elaborate further on different selection methods with and without learning. 

The 2-dimension hyperheuristic classification by (Burke et al., 2010), shown in Figure 1.2, presents a classification of hyperheuristics according the nature of heuristic search space and the source of feedback during the process. The first dimension distinguishes between heuristic selection and heuristic generation, which could both be constructive or local search hyperheuristics using construction and perturbation low-level heuristics, respectively. The second dimension however, points out towards another classification, which is orthogonal to the first one. It distinguishes between new categories according to the source of feedback during learning. 

The first class is referred to as _online learning_ hyperheuristics, where the learning mechanism is active during the solution process of an instance of the problem. The higher-level strategy selects or generates the appropriate low-level heuristic according to their real-time performances. 

The second class are the _off-line learning_ hyperheuristics, which use a set of training instances in order to extract hidden knowledge in the form of programs or rules, all in the hopes of generalizing the process to the stage where it becomes 

**1.3 Hyperheuristics** 

**29** 

fully capable of solving unseen instances. 

Apart from the aforementioned classes, there are _non-learning_ hyperheuristics that are the one that do not employ any learning mechanisms of any sort. 





**Figure 1.2:** A classification of hyperheuristic approaches (Burke et al., 2010) 

There are also other classification schemes such as the one in (Chakhlevitch and Cowling, 2008a) that will be more elaborated in chapter 4. 

### **1.3.2 Move Acceptance Criteria** 

The decision of whether or not accepting a new solution during the search, which known as _move acceptance strategy_ , is regarded as a crucially important decision in 

**Hyperheuristic: A General Overview** 

**30** 

the recent studies such the selection methods. The acceptance strategies themselves are divided into two categories: Deterministic and non-deterministic. 

Deterministic methods make the same acceptance decision for the same candidate situations and no random elements exists in this category. Few deterministic methods, which are used in (Cowling et al., 2001, 2002a), are summarized in the following: 

- i) _All Moves(AM)_ : deals with accepting the candidate solution regardless of its quality. 

- ii) _Only Improvements (OI)_ : accepts only the improving solutions. 

- iii) _Improving and Equal (IE)_ : the same of _Only Improvements_ except that accepting candidates with the same quality as of the current but significantly different from the incumbent, as a kind of diversification. 

Cowling et al. (2002a) present a variety of hyperheuristic in order to compare the performance of different combinations of heuristics selection methods and acceptance strategies. Two acceptance methods were tested: AM and OI. The choice function hyperheuristic with AM acceptance criteria is shown to be the better one in their experimental results. To the best of our knowledge the AM is only considered in (Nareyek, 2004) as the acceptance criteria with reinforcement learning technique. 

On the other hand, non-deterministic methods might make different decision for 

**1.3 Hyperheuristics** 

**31** 

the same input at different decision point. Therefore, non-deterministic methods require additional parameter such as the time stamp. Several non-deterministic acceptance strategies are proposed in the literature, some of which are listed in the sequel: 

1. _Exponential Monte Carlo (MC)_ (Ayob and Kendall, 2003a), allows the nonimproving solution to be accepted with a probability _e_<sup>_−δ_</sup> , where _δ_ is the difference between the objective function value of the current solution and that of the candidate. The probability of a non-improving solution to be accepted decreases as the _δ_ increases. 

2. _Simulated Annealing (SA)_ (Bai and Kendall, 2005), accepts any worsening solution with a probability of _e_<sup>_−δ/t_</sup> . The probability of a non-improving solution being accepted decreases as _δ/t_ increases, where _t_ is the time stamp. 

3. _Exponential Monte Carlo With Counter (EMCQ)_ (Ayob and Kendall, 2003a), is a variant of simulated annealing, but the probability of accepting a candidate solution follows the equation exp(<sup>_−_</sup> _τ_<sup>_<u>θ</u>_), where</sup><sup>_θ_=</sup><sup>_δt_,</sup><sup>_τ_=</sup><sup>_p_(</sup><sup>_Q_),</sup><sup>_t_is</sup> the time. _θ_ and _τ_ were defined in a manner to ensure that the probability of accepting worsening solution decrease as _t_ increase and _δ_ decrease. _Q_ is a parameter which it is represented as a counter of consecutive non-improved iterations. With the smaller values of _Q_ the probability of accepting nonimproving solution increases which ensures some kind of diversification. 

4. _Record to Record Travel (RRT)_ , (Dueck, 1993), which allows worsening 

**Hyperheuristic: A General Overview** 

**32** 

solutions to be accepted with respect to a threshold value, which depends on the objective function deviation from the current best solution. 

5. _Great Deluge_ , (Dueck, 1993), which is similar to the RRT while the threshold _τ_ , presented in the following, decreases in time linearly. _maxIter_ represents the maximum number of iterations or the time limit, _t_ is the elapsed time or iterations, and ∆ _R_ is an expected range between the initial objective function value and the best one. 



<!-- Start of picture text -->
t<br>T =  fopt  + ∆ R (1  − maxIter ) (1.1)<br><!-- End of picture text -->

6. _Naive Acceptance_ , (Cowling et al., 2001), where non-improving solutions are accepted with a probability of 0.5. 

7. _Adaptive Acceptance_ , which authorizes worsening moves being accepted with a probability of 1 _− C_<sup><u>1</u></sup><sup>_,C>_0.</sup><sup>_C_is considered as a counter, which</sup> increases to _N_ consecutive operation without improving the solution. _C_ is reset to 1 each time an improvement in the solution is observed. 

8. _Late Acceptance (LA)_ , is a generic optimisation method (Burke and Bykov, 2008) which is an extension of simple hill-climbing and requires a unique parameter with a memory based approach. Such in hill-climbing, accepted new solution should be better than the incumbent one, LA accepts a solution if it is of better quality than the solution n iterations previously, where n is the size of a memory of previously seen solutions. 

**1.3 Hyperheuristics** 

**33** 

The non-deterministic acceptance criteria have received a lot of attentions so far. Ayob and Kendall (2003b) proposed three move acceptance strategies based on Monte Carlo move acceptance method, which are based on the change of the fitness value, time and the number of consecutive non-improving moves. The heuristic selection method was a simple random method, forms with one of the three move acceptance methods a hyperheuristic approach, which aims to solve the component placement problem. Authors demonstrate that the best move acceptance strategies for this problem within the used heuristic selection method, is exponential Monte Carlo with counter method. 

Other SA-based acceptance method were also applied in the literature. Bai and Kendall (2005) demonstrates good performance of a simple random hyperheuristic with SA acceptance criteria in the problem of shelf space allocation. Reheating schema was embedded into the SA move acceptance, and applied to the problem of travelling tournament problem in (Anagnostopoulos et al., 2006). Moreover, a hyperheuristic, consists of SA with reheating and a reinforcement learning method, was applied in (Bai et al., 2007) for nurse roistering, course timetabling and 1D bin packing problem. It must be noted that SA differs from EMCQ by using a cooling schedule. 

In (Dueck, 1993), simple random heuristic selection was combined with four acceptance strategies including monte carlo, AM, OI and RRT, in order to compare their performances. RRT move acceptance provides the better solution among the three others. 

**Hyperheuristic: A General Overview** 

**34** 

Another performance study for several heuristic selection methods and acceptance strategies was employed by (Bilgin et al., 2007) for the problem of exam timetabling. The hyperheuristic comprised of a choice function heuristic selection method and SA acceptance mechanism, is demonstrated as the best method. While, simple random with great deluge hyperheuristic has the second place with respect to the performance. 

The great deluge, which is a threshold based acceptance method, is proposed by (Dueck, 1993). It was applied by (Kendall and Mohamad, 2004) with simple random selection method to a mobile telecommunication network problem. The great deluge with greedy heuristic selection was also applied in order to solve a problem of job shop scheduling in (Mcmullan, 2007). 

Three variants of great deluge move acceptance strategies with a reinforcement learning was presented in (Sin and Kham, 2012) in order to solve a problem of exam timetabling problem. 

Özcan et al. (2009) applied late acceptance strategy with several heuristic selection method for solving exam timetabling problem. Simple random selection method, which select one of four perturbation low-level heuristics, with late acceptance method is shown as the best proposed approach compared to the performance of using tabu search or choice function selection methods. 

### **1.3.3 Termination Criteria** 

Termination criteria deal with defining a special condition(s) as search stopping criteria. The termination condition tries to avoid useless computations and also 

**1.4 State of the art** 

**35** 

avoid early termination. The most known proposed termination criteria include time limit, number of iterations, number of non-improvement steps, performance changes of each existing heuristic etc. 

The different (combination of) termination criteria in different contexts were proposed in literature, e.g. (Özcan et al., 2010), (Burke et al., 2008a), (Raghavjee and Pillay, 2015), (Shmygelska and Hoos, 2005) and (GiriRajkumar et al., 2010) among others. 

## **1.4 State of the art** 

The hyperheuristic approach has been successfully applied to solve many combinatorial problems in Scheduling (see e.g. (Ahmed et al., 2015; Zheng et al., 2015; Aron et al., 2015), Routing (Danach et al., 2015a,b; Monemi et al., 2015; Marshall et al., 2014; Garrido and Riff, 2010; Garrido and Castro, 2012)), Bin Packing (see (Sim et al., 2015; Beyaz et al., 2015; Ross et al., 2002)), Telecommunications (see (Kendall and Mohamad, 2004; Keles et al., 2010; Segura et al., 2011)) and Constraint Satisfaction Terashima-Marín et al. (2008); Ortiz-Bayliss et al. (2010) from among others. The interested readers are referred to (Chakhlevitch and Cowling, 2008b) for a classification and review of the recent developments in hyperheuristics including real-world applications. The authors identified three distinct attributes that define a hyperheuristic method. According to the authors, a hyperheuristic is 1) a high level heuristic that manages lower level ones, 2) its goal is to find a 

**Hyperheuristic: A General Overview** 

**36** 

good solution method instead of finding a good solution, and 3) it makes use of problem-specific information uniquely. The authors emphasize on the importance of the last attribute. 

Burke et al. (2009a) elaborates on some of the possible methodologies that use sets of promising heuristic components to generate new heuristics. These methodologies are highly influenced by Genetic Programming techniques. Many points were highlighted in this chapter, the authors described the steps to properly apply this approach along with some case studies. Furthermore, some of the issues faced by this type of HH are discussed and a brief literature review is presented. Kendall et al. (2002a) presents an approach to solve three personnel scheduling problems by ranking heuristics using a performance-rating function. Burke et al. (2003) combined Tabu-search and HH has been proposed as a hybrid method that was then applied on eleven university course timetabling problems and on variants of a nurse scheduling problem. Burke et al. (2002, 2006); Petrovic and Qu (2002) reported the effectiveness of case based reasoning when employed in timetabling problems as a heuristic selection methodology. 

The following approaches are based on the work by Ross et al. (2002) on uni-dimensional bin packing and are categorized as evolutionary approaches in generating HH for solving the 2D-Regular Cutting Stock Problems: in (TerashimaMarín et al., 2005a), HH was generated by using the XCS Classifier System; in (Terashima-Marín et al., 2005b), the authors made use of a GA with integer and fixed-length representation in order to produce HH. The results achieved by both of 

**1.4 State of the art** 

**37** 

these HH were significantly superior to the ones delivered by ordinary heuristics, proving efficiency of HH for many different problem instances. 

In (Ross et al., 2002), the authors focused on learning methods that could be applied to many problem instances rather than learning and improving individual solutions. This method selects a heuristic at each problem state, in order to solve the problem. The selected heuristic is the most appropriate one and has the biggest chance of solving that specific state. The method proceeds progressively in this manner; selecting different heuristics for different states of problems, until eventually, the problem reaches a solved state. This is consistent with the attributes that make every HH (Chakhlevitch and Cowling, 2008b). 

In (Wilson et al., 1998), an accuracy-based Learning Classifier System (XCS) was employed to learn a set of rules that allows the method to associate characteristics of the current problem state with eight different heuristics. This application on the one-dimensional bin packing problem was the first attempt at using such HH model. 

In (Schulenburg et al., 2002), improvements were made over the initial method. A new heuristic that randomly selects heuristics was introduced to the method in order to compare results. The HH method gave results that greatly supersede those achieved by the proposed heuristics. During the learning process of HH, two different reward systems were applied to the process, creating and evolving individual processes. This work gave much importance to those individual processes 

**Hyperheuristic: A General Overview** 

**38** 

and focused mainly on them. The authors continued to analyze and compare the performance of the HH method to that of single heuristics. 

The promising results led to further examine the idea on the other problem domains. A HH method was proposed by (Cowling et al., 2001, 2002a,b,c) with an even higher level of abstraction than that of metaheuristic local search methods. It selects different neighborhoods according to a choice function of which the goal is to determine the most appropriate neighborhood for the current problem. Previously, several time consuming trial and error experimentations were carried out to select the correct neighborhoods. This in turn, highlights the importance of this HH method in reducing the computational time, and perform results quality. Cowling et al. (2001, 2002a,b,c) also stressed the importance of choice functions, and their integral role in the success of HH. 

Burke and Newall (2002) proposed a HH approach aiming at improving an initial heuristic ordering in examination timetabling problems. The adaptive heuristic functions works as follows: First, it schedules the exams in an order specified by the original heuristic in order to create an initial solution. An exam is prompted up the order in a later construction in the case where the use of this ordering hinders the process of acceptably scheduling an exam. The termination criteria of this process are either achieving the goal, which is effectively ordering the exams in a manner that they all can be acceptably scheduled, or reaching a pre-determined time limit. The process will continue until at least one of them is met. The results obtained from the experiments prove that the quality of the solution method 

**1.5 Existing and the Proposed Framework** 

**39** 

achieved by this process is greatly better than the quality achieved by the original heuristic. According to the authors, the method can still find acceptable results relatively quickly even if the initial heuristic was poor. 

Cowling et al. (2002c) studied a _trainer scheduling_ using a genetic algorithm based hyperheuristic (hyper-GA) in order to schedule several geographically distributed training staff and courses. The aim of the hyper-GA is to evolve a good-quality heuristic for each given instance of the problem and use this to find a solution by applying a suitable ordering from a set of low-level heuristics. 

Since the user only supplies a number of low-level heuristics and an objective function, the proposed hyperheuristic can be re-implemented for a different type of problem. The method’s results appear much better than those of conventional genetic and memetic algorithm methods, and it is expected to be robust across a wide range of problem instances. 

## **1.5 Existing and the Proposed Framework** 

The hyperheuristic system is consist of two levels separated by the domain barrier: Hyper Level and Base Level. A set of predefined heuristics, a specific fitness function and search space was encapsulated in the base level (Swan et al., 2013). 

The main decision of the hyper level is to decide which base level heuristics must solve the defined problem (Ryser-Welch and Miller, 2014). The hyperheuristic architecture represented by the two level concept, answers not only the question 

**Hyperheuristic: A General Overview** 

**40** 

about the degree of generality, but also paves the way of plug and play concept in heuristic domain. Many hyperheuristic frameworks were proposed in the literature such as in the following: 

1. _SATzilla_ : is proposed by (Nudelman et al., 2004) for SAT solvers, is focused on the concept of algorithm portfolio, which aims at predicting the executing time of algorithms in order to solve the problem with a reduced time. It uses an off-line learning in order to develops heuristics portfolios. A Matlab code of this framework has been developed. 

2. _Single Neighborhood-based Algorithm Portfolio in Python_ (Snappy): adopts the algorithm portfolio. The main different issue with SATzilla is using online learning methods in order to improve its own performances (Samulowitz et al., 2013). 

3. _Hyflex_ : is a library proposed by (Burke et al., 2009b), implemented in java, which includes a set of methods, the communication protocols between the solver and the problem domain. It is an efficient tools to build new cross-domain hyperheuristic. 

4. _parHyFlex_ : is a parallel implementation of Hyflex framework allowing to run a hyperheuristic in a parallel setting (Van Onsem and Demoen, 2013). 

5. _Generic Intelligent Hyperheuristic (GIHH)_ : is an improved version of Hyflex, proposed as a generic framework for online selective hyperheuristic, which equipped with several online learning methods (Misir, 2012). 

**1.5 Existing and the Proposed Framework** 

**41** 

Our proposed heuristic selection hyperheuristic framework, shown in Figure 1.3, ic comprised of two main classes: HyperLevel and BaseLevel. The first one represents the hyperheuristic process methods and attributes, while the second one represents the problem properties. 

Heuristics, which are predefined for the given problem, are categorized by type using HeuristicTypes abstract class. Hyperheuristic can use any acceptance criteria in the set of All Moves, Only Improvements, Improving and Equal, Exponential Monte Carlo (MC), Simulated Annealing (SA), Exponential Monte Carlo With Counter (EMCQ), Record to Record Travel, Naive Acceptance, Late Acceptance etc. In addition, concerning the termination criteria, three possible methods are defined which are the time limit, a defined number of non improvement consecutive iterations and termination based on the heuristics performance. Finally, the hyperheuristic system can opt for any selection method among the aforementioned ones (with/without learning). We elaborate further on the selection methods in 4. 

**Hyperheuristic: A General Overview** 

**42** 



**Figure 1.3:** The Proposed Hyperheuristic Framework. 

## **1.6 Contributions and Overview** 

This thesis is organized as follows: in chapter 2 we deal with the Workover Rig Problem. We review the state of the arts and propose a new mathematical model and several valid inequalities. We then propose a selective hyperheuristic application with two learning methods applied in real instances of the problem. 

The following contributions summarize the results of this chapter. 

1. Monemi, R. N., Danach, K., Khalil, W., Gelareh, S., Lima, F. C., & Aloise, 

**1.6 Contributions and Overview** 

**43** 

D. J. (2015). Solution methods for scheduling of heterogeneous parallel machines applied to the workover rig problem. Expert Systems with Applications, 42(9), 4493-4505 

2. Danach, K. M., Khalil, W., Junior, F., & Gelareh, S. (2014). Routing parallel heterogeneous machines in maintenance planning:A hyperheuristic approach. ICCSA, (p. 441). Le Havre, France. 

chapter 3 is composed of two parts. The first part introduces a new variant of hub location routing problem which is referred to as _p_ -Hub Location Routing Problem. After a through literature review, we propose a 3-index design variable model for this problem. We then propose a Lagrangian relaxation for a 2-index version of the problem. We then propose a HH that exploits information from the Lagrangian Multipliers to solve the problem. Two learning mechanisms were employed within our HH. The second part, examines the effectiveness of the aforementioned HH (together with its learning mechanisms) on instances of another variant of Hub Location Routing Problem proposed in Rodríguez-Martín et al. (2014). 

The following contribution is the outcome of this chapter: 

1. Danach, K., Khalil, W., Gelareh, S., Semet, F., & Junior, F. (2015). Capacitated Single location P-Hub Location Routing : Hyperheuristic Approach. ROADEF. Marseille, France. 

In chapter 4 we study the impact and effectiveness of several heuristic selection methods on the overall performance of HHs proposed for our problems in the previous chapter. This includes the approaches including learning mechanisms and 

**Hyperheuristic: A General Overview** 

**44** 

without it. 

The following contribution is the outcome of this chapter: 

1. Danach, K., Gelareh, S., Khalil, W., & Semet, F. (2016). Capacitated Single Allocation p-Hub Location Problem:Hyperheuristic Approaches with different Selection Methods. ROADEF. Compiegne, France. 

During this thesis, we have also produced other contributions that make use of the knowledge of HH we have obtained during this thesis. 

1. Danach, K., Khalil, W., & Gelareh, S. (2015). Multiple Strings Planing Problem in Maritime Service Network: Hyperheuristic Approach. TAEECE. Beirut, Lebanon. 

2. Danach, K., Haj Hassan, J., Khalil, W., Gelareh, S., & Kalakish, A. (2015). Routing Heterogeneous Mobile Hospital With Different Patients Priorities: Hyperheuristic Approach. DICTAP. Beirut, Lebanon. 

# **Chapter 2** 

# **Workover Rig Problem** 

## **2.1 Introduction** 

One of the most important natural resources of the world since late XIX century is oil, which shapes our lives in many ways, not only by being the main energy source of our era, but also its uses on plastics, road construction, pharmaceutical drugs, etc. The process of finding, drilling, producing, transporting and refining oil provides a wide range of research fields, from geology to biochemistry and so on. 

Many land (onshore) oil fields are composed of many wells, which are distributed geographically. Occasionally, failures happen on these wells, requiring an intervention inside them to return to their original condition. Such operation normally includes substituting the production equipments (cleaning) or stimulating the reservoir itself (stimulation), to name a few. Those interventions require the use of _workover rigs_ , big structures that can be dismounted, transported and 

**Workover Rig Problem** 

**46** 

mounted from one well to another, providing safety and accuracy conditions to the intervention. Renting of workover rigs come at great cost, thus having them at standby availability is expensive. This chapter boards the problem of prioritizing onshore interventions using workover rigs to minimize production loss associated with the wells awaiting service. The problem in study here can be classified like a particular case of machine scheduling problem. 

A classical problem of machine scheduling represents a set of tasks (or jobs) to be processed, where each task consists of a sequence of operations to be performed using a given number of machines. The processing of an operation requires the use of a specific machine for a particular processing time, and each operation must be executed in the order given by the sequence. Each machine must process only one operation at a time. The objective is to arrange the wells so that the global performance measures can be optimized. 

A vast body of literature is dedicated to the classical problems of scheduling (job-shop and flow-shop), but in specific applications, the quantity of publications is rather limited. Two well-known samples of historical papers for the classical problems are related to the problems with 10 wells and 10 workover rigs proposed by Muth J.F. (1963), which was only solved 26 years later by Carlier and Pinson (1989). In this problem, each task has to be processed on each of the given workover rigs exactly once —classical job-shop scheduling problem. 

Here we are concerned by a particular case of machine scheduling, an application to the problem of _Workover Rigs Scheduling (WRS)_ for maintenance services in oil wells of onshore fields. The problem consists in finding the best schedule for 

**2.2 Literature review** 

**47** 

a small number of workover rigs to minimize the production loss, associated with a large number of wells waiting for service. 

## **2.2 Literature review** 

Smith (1956) showed that if the problem has only one rig and no time windows, the optimal sequencing is obtained, independent of the quantity of wells, by sorting the wells in an increasing order of value _Et_<sup>_<u>Pi</u>_</sup> _i_<sup>, where</sup><sup>_Pi_is the rate of daily production</sup> loss of well _i_ and _Eti_ is the estimated maintenance service time of well _i_ . 

Barnes et al. (1977) provided lower bounds for workover rigs problem. The authors consider _m_ rigs and _n_ wells, and show that a lower bound can be obtained as _Max{B_ (1) _, B_ ( _n_ ) _}_ where _B_ ( _n_ ) is the total production loss with _n_ rigs and _B_ (1) = 21 _m_<sup>[(</sup><sup>_m−_1)</sup><sup>_B_(</sup><sup>_n_)+2</sup><sup>_B_(1)] is the total production loss with only one single</sup> rig. 

Noronha et al. (2001) presented a greedy heuristic algorithm for the workover rigs problem. The authors consider priorities for the wells as _Gij_ = _T_<sup>_<u>P</u>_</sup> _ij_<sup>_<u>i</u>_, where,</sup><sup>_Pi_</sup> is the daily rate of production loss of well _i_ , and _Tij_ is the estimated maintenance service time of the well _i_ by the rig _j_ . In their greedy approach, the authors consider also the environmental risks corresponding to the service. The proposed algorithm was later used a constructive phase of a GRASP metaheuristic. 

Aloise et al. (2006) proposed a variable neighborhood search (VNS) metaheuristic. In the VNS algorithm the authors, have used the constructive heuristic _H_ 1, proposed by Noronha et al. (2001), which adds one well at-a-time to the 

**Workover Rig Problem** 

**48** 

routes computed for the workover rigs. The local search procedure proposed for the VNS is based on a swap neighborhood defined by all solutions, which can be obtained by the exchange of a pair of wells from the current solution. The numerical experiments were performed with real-life instances showing a loss reduction of 16.4% on average. This VNS metaheuristic approach is currently being used as an operational scheduling tool at Petrobras S. A (Brazilian National Petroleum Corporation). 

Mattos Ribeiro et al. (2011) proposed a simulated annealing (SA) for a variant of the WRS where the travel time is not considered. The authors have used CPLEX 12.1 (IBM, 2009) to solve instances with up to 50 wells. They have also reported that the proposed SA presents a low deviation (the worst case, 0.037%) from optimality and takes, approximately, 10 seconds for solving real-life instances composed of 25, 50, 75, 100 and 125 wells, with 2, 4, 6, 8 and 10 rigs. 

In Duhamel et al. (2012), three mixed integer linear models are proposed. The first model improves an existing scheduling-based formulation. The second one, uses an open vehicle routing approach and the third one is an extended model for which a column generation strategy is developed. The models were tested using CPLEX 12.0 under default parameters and the instances were composed with up to 60 wells, the number of rigs varies from 2 to 5 and the time horizon is set to 15 days. The authors report optimal values for medium-size instances of WRS. 

Ribeiro et al. (2012a) presented the WRS as a workover rig routing problem, a particular case of vehicle routing problem with time windows, in context of the operations of onshore oil fields. The authors have proposed three metaheuristics 

**2.2 Literature review** 

**49** 

for the problem: an iterated local search, a clustering search, and an Adaptive Large Neighborhood Search (ALNS). They have carried out experiments with 50, 100 and 500 wells, and 5 and 10 rigs, testing a total of 60 instances. The authors reported a superior performance of ALNS on larger instances. 

Mattos Ribeiro et al. (2012), in this work the authors propose a branch, price and cut algorithm as the first exact algorithm for the WRS, which is modeled as a workover rig routing problem. The computational experiments relies on a set of 40 instances (with 100 and 200 wells, 5 and 10 rigs, and 200 to 300 units of time for the horizon). For the larger instances (200 wells), 12 of the 40 instances could not be solved, in particular, all instances with 200 wells,10 rigs, and horizon time of 300 hours were unsolvable. 

Ribeiro et al. (2012b) look at the problem as a routing problem and proposes a branch, price and cut algorithm for solving instances of this problem up to 200 wells and 10 rigs. Recently, Ribeiro et al. (2014) proposed three different heuristics such as branch-price-and-cut (BPC) heuristic version of Ribeiro et al. (2012b), an adaptive large neighborhood search (ALNS), and a hybrid genetic algorithm (HGA). They managed to solve up to 10 rigs and 300 wells. 

### **2.2.1 Objective and contribution** 

We propose a new model, which is based on an arc-time-indexed formulation inspired by the work in Pessoa et al. (2010). We also propose several classes of valid inequalities in order for tightening the MIP polytope. 

The work was motivated by the industrial application and the need for an 

**Workover Rig Problem** 

**50** 

efficient and scalable solution framework that can exploit the knowledge hidden in all the heuristics proposed for the problem at hand. 

Here, a heuristic selection type of hyperheuristics is proposed, which is a selfadaptive mechanism in the sense that the selection of heuristic algorithm (chosen from a pool of constructive, improvement and destructive ones) iteratively applied to the problem is based on a proposed learning method. Our main goal is to show that the self-adaptive nature of the learning mechanism controlling the heuristic selection type hyperheuristic allows a very efficient exploration of neighborhoods using several heuristics. This helps us to identify the classes of heuristic, among those applied here, which fit best for solving instances of WRS. 

While we only focus on the HH heuristic in this thesis, however, in order to evaluate the performance and measure the quality of solutions reported by our solution framework, the outcome of the HH has been injected into an exact solution method which is a branch-and-price algorithm. The best solution reported by the HH constitutes the initial columns of a branch-and-price algorithm and helps accelerating convergence. With a fast convergence or within a given time limit when the branch-and-price decide to terminate we are able to show whether the solution reported by the HH is optimal or will have an indication of distance from optimality. We must emphasize that this branch-and-price have been developed by a different group of researchers and is independent of the work in this thesis. Details of this approach can be found in (Monemi et al., 2015). 

**2.3 Problem Description** 

**51** 

## **2.3 Problem Description** 

The problem is described as following: _A set of wells requiring maintenance, J_ = _{_ 1 _, . . . , n}, scattered within a geographical area._ [ _dij_ ] _|J |×|J | represents the distance in term of travel time between every ordered pair of wells_ ( _i, j_ ) _∈J × J . A set of workover rigs (i.e. mobile maintenance heterogeneous workover rigs) are available to serve the wells upon need and there is a service capacity qr associated to each workover rig r ∈R such that q_ 1 _≤· · · ≤ q|R|. Every workover rig r can offer all the services offered by rig r_<sup>_′_</sup> _, qr′ ≤ qr. To every well j ∈J a required service level lj is associated and there is a smallest r_ ˆ _for which every rig r_ : _r ≥ r_ ˆ _can serve the well j. At time_ 0 _, all the rigs are at their initial locations and the production is already interrupted (or significantly deteriorated) at all the wells requiring maintenance. Duration of maintenance on well i ∈J is pi and production revenue per time unit has a monetary value of gi, i ∈J . The objective is to minimize the total lost production revenue that is to minimize the total completion time of maintenance activities._ 

## **2.4 Mathematical Model** 

Our modeling framework relies on a set of assumptions as in the following: i) A _field of work_ is comprised of a set of wells and a set of workover rigs within this field dedicated to serve wells inside it. Normally, the area of this field as well as the travel time between every pair of wells is limited. This suggests that a workover rigs does not need to travel a very long distance between pairs of well. 

**Workover Rig Problem** 

**52** 

ii) The process takes place on a discrete-time planning horizon. Moreover, we assume that dismounting (equivalently mounting) of all workover rigs are equal and equivalent to one unit of time, _δt_ , iii) the dismounting (equivalently mounting) time is already included in the processing time of every workover rig, and, iv) without loss of generality, we assume that the rigs are heterogeneous meaning that no two machines have the same compatibility list (otherwise, the subproblems per those similar machines will collapse to one as explained in Pessoa et al. (2010)). 

The necessary parameters and variables are listed in Table 3.4: 

**Table 2.1:** Model Parameters and variables. 

Parameters: _J_ : the set of well to be serviced, _R_ : the set of workover rigs to service the wells, _T_ : the time horizon periods, 1 _, . . . , T_ , _pi_ : the process time of task _i_ , _dij_ : the travel distance between the location of task _i_ and the location of task _j_ , 0: the dummy task, which is the _first_ and _last_ task on every machine. Variables: 

_xijrt_ : 1, if task _i_ is finished and task _j_ is started at period _t_ on machine _r_ , 0, otherwise. 

We define _J_<sup>+</sup> = _J ∪{_ 0 _}_ . To this end, we use _workover rig (WOR)_ and _machine_ , alternatively. The _well_ and _tasks/job_ are also used alternatively. 

### **2.4.1 Workover Rig Scheduling (WRS) Problem** 

In our modeling approach at _t_ = 0, every machine is processing dummy task 0. 

**2.4 Mathematical Model** 

**53** 

|(_WRS_)|
|---|
|_min_<br>�<br>_r∈R_<br>�<br>_t∈T_<br>�<br>_i∈J_<br>�<br>_j∈J_ <sup>+</sup><br>_gi_(_t_+_pj_)_xijrt_<br>(2.1)|
|_s. t._|
|�<br>_j∈J_<br>_x_0_jr p_0+_d_0_j_ +_x_00_r p_0 = 1_,_<br>_∀r ∈R,_|
|(2.2)|
|�<br>_i∈J_<br>_|T |_<br>�<br>_t_=_pi_+1<br>_xi_0_rt_+_x_00_r p_0 = 1_,_<br>_∀r ∈R,_|
|(2.3)|
|�<br>_r∈R_<br>�<br>_i∈J_ <sup>+</sup>:_j̸_=_i_<br>_|T |_<br>�<br>_t_=_pi_<br>_xijrt_ = 1_,_<br>_j ∈J ,_|
|(2.4)|
|�<br>_r∈R_<br>�<br>_i∈J_ <sup>+</sup>:_j̸_=_i_<br>_|T |_<br>�<br>_t_=_pj_<br>_xjirt_ = 1_,_<br>_j ∈J ,_|
|(2.5)|
|_xijrt ≤_<br>�<br>_l∈J_<br>_t_+_djl_+_pj≤|T |_<br>_xjlr t_+_djl_+_pj,_|
|+_xj_ 0 _r t_+_pj_<br>_∀t ∈T , r ∈R, i ∈J_ <sup>+</sup>_, j ∈J_ :_j̸_ =_i,_|
|(2.6)|
|_xijrt ∈{_0_,_1_}_<sup>_|J_ +</sup><sup>_|×|J_ +</sup><sup>_|×|T |×|R|_</sup>_._<br>(2.7)|



**Workover Rig Problem** 

**54** 

The objective function (2.1) accounts for the minimizing the lost production revenue. 

Constraints (2.2) ensure that for every machine, either it start working on a task _j_ at _p_ 0 + _d_ 0 _j_ (assuming that _|R| ≤|J |_ ) or _x_ 00 _r_ 0 = 1 meaning that the task 0 is being treated after the task 0 and terminated at time _p_ 0. If a real job _i̸_ = 0 started, then such a first task on every machine _r_ does not start before _p_ 0 + _d_ 0 _i_ , which accounts for the process time of dummy job 0 plus travel time from the initial location (where the dummy job takes place) to _i_ . 

The last job on every machine is actually the dummy task 0, which is executed after the last real task _i_ . Such a task does not occur during [0 _, p_ 0 + _doi_ ], evidently. This is ensured in constraints (2.3). 

Constraints (2.4) ensure that the real task _j_ will start at some point in time after another task _i ∈J_<sup>+</sup> on one of the available workover rigs. However, this cannot start earlier than _p_ 0 + _d_ 0 _i_ . Analogously, constraints (2.5) ensure that a real task _j_ is followed by a task _i ∈J_<sup>+</sup> on the same machine and this cannot occur within [0 _, p_ 0 + _doi_ ]. 

For task _j_ executed after a real task _i_ on machine _k_ and time _t_ there must be a consecutive task _l ∈J_<sup>+</sup> , which starts at _t_ + _pj_ + _djl ≤|T |_ (starts at _t_ + _pj_ + _djl_ : _l_ = 0). This has been ensured by constraints (2.6). 

**2.4 Mathematical Model** 

**55** 

### **2.4.2 Valid inequalities** 

Constraints (2.2)-(2.6) describe the polytope of the problem including all the feasible solutions given the fact that all the variables have positive cost in the objective function. However, there are some other constraints which, can be added to the model as following: 

a) Every task _i_ is excused at some point in time on one machine: 



<!-- Start of picture text -->
� � � xijrt = 1 , ∀i ∈J + (2.8)<br>t∈T j∈J + r∈R<br><!-- End of picture text -->

- b) For two distinct well _i, j_ on the same machine _k_ , either of them is executed before the other one: 



<!-- Start of picture text -->
� �( xijrt  +  xjirt ) = 1 , i, j ∈J (2.9)<br>t∈T r∈R<br><!-- End of picture text -->

- c) The total number of variables _xijrt, i, j̸_ = _i ∈J_<sup>+</sup> _, r ∈R, t ∈T_ taking 1 in any feasible solution is constrained as following: 



<!-- Start of picture text -->
� � � xijrt =  |J |, (2.10)<br>i,j̸ = i∈J r∈R t∈T<br><!-- End of picture text -->



<!-- Start of picture text -->
� � � xijrt =  |J |  + 2 |R|. (2.11)<br>i,j̸ = i∈J + r∈R t∈T<br><!-- End of picture text -->

**Workover Rig Problem** 

**56** 

d) a real task _i ∈J_ must be followed (precede) by a another task _j ∈J_<sup>+</sup> : _j̸_ = _i_ : 



<!-- Start of picture text -->
|T | |T |<br>� � xijrt ≤ � � xjirt, ∀r ∈R, i ∈J , (2.12)<br>t = p 0 j∈|J + | t = p 0 j∈|J + |<br><!-- End of picture text -->

e) There is no 3-cycle in the order of jobs on a give machine: 



<!-- Start of picture text -->
|T |<br>�( xijrt  +  xjlrt  +  xlirt )  ≤ 2 , ∀r ∈R, {i, j, l} ∈J , (2.13)<br>j̸ = i,l̸ = i,l̸ = j<br>t = p 0<br><!-- End of picture text -->

f) On the same machine no two wells can be executed at the same time: 



<!-- Start of picture text -->
� � xijrt ≤ 1 , ∀r ∈R, t ∈{p 0 , . . . , , |T |} (2.14)<br>i∈J + j∈J + : j̸ = i<br>� � xjirt ≤ 1 , ∀r ∈R, t ∈{p 0 , . . . , , |T |} (2.15)<br>i∈J + j∈J + : j̸ = i<br><!-- End of picture text -->

g) On every rig _r_ either at some point _t ∈T_ a task _j ∈J_ is started (finished) as the first (last) task or _x_ 00 _r_ 0 = 1: 



<!-- Start of picture text -->
� � x 0 jrt  +  x 00 r 0 = 1 , ∀r ∈R, (2.16)<br>j∈J t∈T<br><!-- End of picture text -->



<!-- Start of picture text -->
� � xj 0 rt  +  x 00 r 0 = 1 , ∀r ∈R, (2.17)<br>j∈J t∈T<br><!-- End of picture text -->

The aforementioned constraints are particularly useful when due to some relaxations or reduced cost updates, the pricing problem or Lagrangian subproblem objective has variables with negative cost. There, these constraints serve to avoid 

**2.4 Mathematical Model** 

**57** 

too many variables take 1 and will tighten the pricing problem/Lagrangian relaxation polytop. 

### **2.4.3 Preprocessing** 

Some of the variables can be set to zero in advance. The total number of variables eliminated in this way depends on the instance of problem being solved. 

**Lemma 1.** _None of the wells i ∈J can receive service during_ [0 _,_ min _j∈J_<sup>_{p_0 +</sup><sup>_d_0</sup><sup>_j}−_</sup> 

1] _on any machine._ 

Analogously, we have: 

**Lemma 2.** _None of the wells i ∈J can receive service during_ [ _T −_ min _j∈J_<sup>_{pj_+</sup> _dj_ 0 _}_ + 1 _, T_ ] _on any machine._ 

#### **variable fixing by task-machine feasibility** 

As stated in the problem description, the workover rigs of larger size can serve those wells of equal size or smaller while the inverse does not hold. 

Let _R_ ( _j_ ) represents the set of all workover rigs that can serve task _j_ . The following constraint ensures the feasibility of task assignment. 



<!-- Start of picture text -->
xijrt = 0 ∀i, j ∈J :  j̸ =  i, r ∈R/ ( i )  ∨ r ∈R/ ( j ) (2.18)<br><!-- End of picture text -->

**Workover Rig Problem** 

**58** 

### **2.4.4 Illustrative example** 

We have considered _|R|_ = 3, _|J_<sup>+</sup> _|_ = 7 and a time horizon _|T |_ = 16. We have run the model in CPLEX 12.60 for a TiLim = 1000 seconds. _gi_ = 1 _, ∀i ∈J_<sup>+</sup> , 



<!-- Start of picture text -->
dij =  ⌊ ( i×j +( n 10 −i )( n−j )) ⌋, ∀i, j ∈J + and  pi =  i, ∀∈J + .<br><!-- End of picture text -->



**Figure 2.1:** Illustrative example with _|R|_ = 3, _|J_<sup>+</sup> _|_ = 7 and _|T |_ = 16. Every machine starts by processing job 0 at _t_ = 0 and terminates at the same job as the job processed on it. 

## **2.5 Hyperheuristic for WRS Problem** 

The mathematical model of WRS becomes intractable even with small _|T |_ , few wells and rigs. Therefore, in order to solve more realistic size instances, we have to resort to other techniques, which are efficient and provide good approximation of optimal solutions. From among such techniques, we have chosen to use the concept of Hyperheuristic (Burke et al., 2009a, 2008b, 2013) 

**2.5 Hyperheuristic for WRS Problem** 

**59** 

The low-level heuristics are categorized as follows: 

1. _constructive_ ones, which produce complete feasible solutions from the scratch, 

2. _improvement_ methods that accept a feasible solution and try to improve it within a predefined neighborhood, 

3. _perturbation_ procedures that try to inject some noises to the process in order to produce solutions, which might help in finding better solutions and possibly escaping from local optima, and finally 

4. _reconstructive_ mechanisms to (randomly or deterministically) destroy and reconstruct part of solutions again, hoping to jump to some unexplored part of the search space that might involve better solutions. 

#### **Low Level Heuristic** 

In the following, we briefly explain how each of these low-level heuristics performs. 

- 1) _constructive heuristic_ : we construct an initial feasible solution, step-by-step, according to a set of predefined rules without any effort to improve this solution. i) _C1_ construct a solution by exploiting the instance information. Here, we sort wells based on the decreasing production parameter. Subsequently, we 

**Workover Rig Problem** 

**60** 

start from the wells with highest production and allocated each well _i_ to the compatible rig _r_ that is less utilized among others (see Algorithm 4). 

- 2) _improvement heuristics_ : 

The improvement algorithm starts from a feasible solution and improve it by applying successive changes within a given neighborhood. Our neighborhoods are characterized by the following moves: 

- i) _better-sequence-on-the-same-rig_ : For a given rig, we reorder (one task per time) the sequence of allocated wells to be served by this rig (see Algorithm 2) and among the improving solution found, we move to the best found feasible solution in a greedy manner. 

- ii) _inset/drop-between-two-different-rigs_ : aiming at making a balanced utilization and fair distribution of tasks among rigs, for two _randomly_ chosen rigs _ri, rj̸_ = _i_ , we consider three moves: 1) move one tasks from rig _ri_ to rig _rj̸_ = _ri_ such that the difference between the objective functions of rig _ri_ and rig _rj_ , i.e. ∆= ( _OF_ ( _ri_ ) _− OF_ ( _rj_ )), being minimized. 2) removing a well from the list of wells being served by a given rig and insert it in a proper place within the sequence of wells being served by the rig with the least objective function. 

**Algorithm 1:** Constructive Heuristic 1 (C1) 

- 1: **procedure** CONSTRUCTIVE1( _J , R_ ) _▷_ INPUT: sets of wells and rigs 2: _Ss ←∅, ∀s_ = 1 _, . . . , m,_ ( _m_ = _|R|_ ) 

- 3: _i ←_ 0 

**2.5 Hyperheuristic for WRS Problem** 

**61** 

- 4: _M ←_ 0 

- 5: _piM ←∞_ 6: **for** _i_ = 1 _, . . . , n_ ( _n_ = _|J |_ ) **do** 7: **for** _r_ = 1 _, . . . , m_ **do** 8: **if** ( _pir < piM_ ) **then** _▷pir_ is the processing time of well _i_ by rig _r_ 

- 9: _M ← r_ 

- 10: **end if** 11: _SM ←_ [ _SM , Ji_ ] 

- 12: **end for** 

- 13: **end for** 

- 14: **return** _S ▷_ OUTPUT: sequence of wells associated to each rig _r_ 

- 15: **end procedure** 

**Algorithm 2:** Order Improvement Operator 

- 1: **procedure** ORDERIMPROVE( _S_ ) _▷_ INPUT: sequences associating wells to rigs 

- 2: _L ←∅_ 3: _G ←∅_ 

- 4: _Mid ←∅_ 

- 5: _p ← SelectPivot_ ( _S_ ) 

- 6: **for** _s_ = 1 _, . . . , m_ ( _m_ = _|S|_ ) **do** 

- 7: **if** ( _Lvs ≤ Lvp_ ) **then** _▷Lvs_ is the production loss value of sequence 

_s_ 

**Workover Rig Problem** 

**62** 

- 8: _Append_ ( _L, s_ ) 9: **else** 

- 10: _Append_ ( _G, s_ ) 11: **end if** 12: **end for** 13: _S ← Concatenate_ (ORDERIMPROVE( _L_ ), _Mid_ ( _p_ ),ORDERIMPROVE( _G_ )) 

- 14: **return** _S ▷_ OUTPUT: Ordered sequences by best objective function value 

#### 15: **end procedure** 

- 3) _Perturbation heuristics_ : 

The perturbation phase assures a _diversification_ strategy during the search; it tries to explore the search space via randomized efforts to escape search from local optimum. In this study, we implement different perturbation heuristics as the following: 

1. _Mutation-like_ : it resembles the genetic operator used to maintain diversified population from one generation to another. This operator corresponds to a perturbation in the configuration of a chromosome (a sequence of wells on every rig), that prevents the risk of premature convergence and allows the exploration of other areas in the search space. The operator is applied with two chromosomes that are selected randomly in the current population. 

2. _Crossover_ : In this case, the swapping of ’genetic material’ is made with the 

**2.5 Hyperheuristic for WRS Problem** 

**63** 

rigs (part of the chromosome), while in the mutation operator is made with two wells, one in each chromosome. 

   3. _SequenceRandomSwap_ : This operator is a kind of mutation-like operator. But here, the perturbation is made in the same chromosome, which is carried out randomly. 

- 4) _Destroy-and-reconstruct heuristic_ : 

In order to better exploit the search space (diversify the search process), we define an operator that destroys and reconstructs part of a solution, which is randomly chosen. Thus the operator _Reconstructive1_ destroys a part of the current solution and then reconstruct it by using constructive algorithms presented previously. 

### **2.5.1 Reinforcement learning** 

A reinforcement learning method in an _selection-type_ hyperheuristic, selects a heuristic that has the maximal utility value (Burke et al., 2008b). Thus, it is a mechanism that chooses corresponding actions given some information about its performance, and update this performance at each time it is applied. The process takes into consideration when to diversify and when to intensify in the search process. In chapter 4, we will elaborate more the concept, techniques, and methods of reinforcement learning. 

Here, we employ two different methods of learning: 1) the built-in method of generic intelligent hyperheuristic - GIHH (Misir, 2012)<sup>1</sup> and 2) our improved 

> 1The code is publicly available at https://code.google.com/p/generic-intelligent-hyperheuristic/ 

**Workover Rig Problem** 

**64** 

method called _Alternative Learning Method (A.L.M.)_ . 

Both methods rely on using Hyperheuristics Flexible framework (Hyflex), which is an well-defined library incorporating a set of methods that assure the communication between the problem domain and the solver components. 

In GIHH, The number of new best solutions and time spent by each heuristic are determinant to update the probability vector in the selection operation. In addition, an acceptance criterion is defined to balance intensification and diversification processes. In general, diversification is occurred at the beginning of the search, followed by intensification towards the end. 

Our proposed hyperheuristic, is based on constructing a feasible solution and consequently applying of heuristics that are chosen following a specific criteria. Then we design a tabu list that prevents some heuristics, in particular conditions, to be applied, in order to guide the search to apply heuristic series to reach the optimal solution. 

We define a so-called _heuristic weight_ variable as the following: 



<!-- Start of picture text -->
Ψ i = � ∆ f = �( f in − f out ) /f in<br><!-- End of picture text -->

A Heuristic _Hi_ weight is equal to the negative sum (for minimization case) of the objective function values taken by the application of _Hi_ divided by the total number of times that _Hi_ has been applied during the search. 

Our tabu list _Tl_ is designed as the following: Given our time limit, we initially set _Tl_ = _∅_ and at each iteration, _Tl_ is updated as follows: if the CPU time spend 

**2.5 Hyperheuristic for WRS Problem** 

**65** 

is less than the half of the time limit, we put all heuristics that, in mean more frequently used than the other my suggestion. Also, all heuristics with too small weights in _Tl_ . In case of the consumed time is greater than the half of the time limit, _Tl_ will contain all heuristics expect those having the best improvement and those having their weight greater than the mean of heuristics weights. The Tabu list is updating with change of quality of each heuristic - calculation of Ψ _i_ . To simplify our tabu strategy, we represent it as a learning method in Algorithm 3. 

#### **Algorithm 3** Alternative Learning Method 

- 1: **procedure** LEARNINGMETHOD( _t_ ) _▷_ INPUT: time limit 2: _α ←_ 0 _._ 7 3: _P ← Proba(Random)_ 4: **while** ( _consumed_  time < t_ ) **do** 5: **if** ( _consumed_  time < t/_ 2) **then** 6: **if** ( _h_ == _SearchHightImproveBestHeuris_ ()) **then** 7: **return** _h_ 8: **end if** 9: **if** ( _HeurisWeight_ [ _h_ ] _> CalcWeightMean_ ()) **then** 

- 10: **return** _h_ 11: **end if** 12: **else** 13: **if** (( _HeurisNbOfCall_ [ _h_ ] _< CalcCallMean_ ())) **then** 14: **return** _h_ 15: **end if** 16: **if** ( _HeurisWeight_ [ _h_ ] _> CalcWeightMean_ ()) **then** 17: **return** _h_ 18: **end if** 19: **if** ( _h_ == _SearchHightImproveBestHeuris_ ()) **then** 20: **return** _h_ 21: **end if** 22: **end if** 23: **end while** _▷_ OUTPUT: heuristic selected 24: **end procedure** 

**Workover Rig Problem** 

**66** 



**Figure 2.2:** The wells are uniformly distributed within a given geographical zone. 

## **2.6 Numerical experiments** 

Our computational experiments are based on a set of perturbed data from Petrobras and within the Brazilian territory. The data relates to a particular field of operation within which the total number of wells is around 200 wells and are densely distributed in such a moderate size field. A geographical presentation of spatial distribution of wells within this field for an aggregated instance of size _|J |_ = 100 is presented in Figure 2.2. 

Our order of business is as follows: we run our hyperheuristic on the instances of the problem. We compare our method against that of GIHH and present an analysis of the results. In addition, HH results are compared with result of an exact method called branch, price and cut algorithm which uses the best-known solution of our hyperheuristic as an initial column in the branch, price and cut algorithm in 

**2.6 Numerical experiments** 

**67** 

Monemi et al. (2015). 

All experiments were performed on an Intel 2.54 GHz core i5 CPU and 4 Gb of memory running on Windows 7. All instances are named in a format instance_i_j where _i_ indicates the number of wells, and _j_ indicates the number of workovers in the instance. 

There are, in total, 37 instances ranging from 10 tasks and 3 workover rigs to 200 tasks and 12 workover rigs. Table 2.2 reports the numerical experiments. The first column reports the instance name, the second one indicates the objective value of the initial solution. The third (resp. fifth) column reports the objective function value of the best solution found when using the learning mechanism of GIHH framework (resp. A.L.M.). The computational times of GIHH and that of A.L.M. are reported in the fourth and sixth columns, respectively. 

We further assume _p_ 0 = 0 _, d_ 0 _j_ = 0 _, ∀j_ in our experiments. 

**68** 

#### **Workover Rig Problem** 

**Table 2.2:** Best solution and execution time results of the two methods. 

|Instance Name|Init. Obj.|Best Obj. (GIHH)|CPU Time (GIHH)|<br>Best Obj. A.L.M.|CPU Time A.L.M.|
|---|---|---|---|---|---|
|Instance_10_3|38223|21578|0.534|19683|0.117|
|Instance_15_3|96179|50020|0.431|40054|1.143|
|Instance_15_5|51415|26055|5.019|28965|1.093|
|Instance_20_3|165681|90499|0.841|86809|0.241|
|Instance_20_5|97214|52314|5.206|45985|1.164|
|Instance_25_3|245356|136401|0.949|124236|1.045|
|Instance_25_5|214666|102923|5.636|97772|0.638|
|Instance_25_7|123666|64582|5.11|63494|0.150|
|Instance_30_3|559221|165326|4.697|162479|0.566|
|Instance_30_5|231082|126291|0.593|117757|0.220|
|Instance_30_7|186164|124002|0.367|94619|0.155|
|Instance_35_3|521748|181936|5.672|180341|1.074|
|Instance_35_5|396655|172343|0.603|159223|0.304|
|Instance_35_7|245830|119389|0.549|104206|0.208|
|Instance_50_5|768691|286110|5.013|276221|0.705|
|Instance_50_7|549441|221749|5.296|201456|0.556|
|Instance_50_9|413259|204595|5.561|200710|0.362|
|Instance_50_10|241935|170762|0.589|154070|0.295|
|Instance_75_7|1357179|503698|10.079|493423|0.658|
|Instance_75_9|790796|440775|9.921|445433|0.826|
|Instance_75_10|849473|386271|10.008|367835|4.203|
|Instance_100_7|6284802|1748851|10.145|1719752|4.273|
|Instance_100_9|6302564|2151156|1.471|2020055|4.118|
|Instance_100_10|5062012|1792773|10.052|1728323|4.276|
|Instance_100_12|4287143|1519804|9.711|1448339|1.116|
|Instance_125_7|27388184|5136775|6.914|5010572|4.228|
|Instance_125_10|21967460|5351825|9.785|5185172|2.503|
|Instance_125_12|13899045|4166687|1.864|4109715|1.064|
|Instance_150_7|39577184|7413717|11.093|6959831|3.179|
|Instance_150_10|29616360|6922348|6.695|6778345|4.183|
|Instance_150_12|25065540|6590526|9.561|6234537|3.162|
|Instance_175_7|96465248|17056898|10.187|16443304|5.112|
|Instance_175_10|75896016|16379125|5.017|15493673|4.186|
|Instance_175_12|59023100|14735414|10.104|14380174|4.139|
|Instance_200_7|109649824|18386244|10.017|17943176|4.143|
|Instance_200_10|87850240|19201584|10.033|18810648|6.427|
|Instance_200_12|83277888|17716744|4.71|17785952|4.295|



We introduce _νa, a ∈{GIHH, A.L.M.}_ defined as in (2.19) to be the accumulated relative improvement of each of the two methods over all the 37 instances. 

**2.6 Numerical experiments** 

**69** 



<!-- Start of picture text -->
37<br>InitObja − BestObja<br>νt = (2.19)<br>�<br>InitObja<br>i =1<br><!-- End of picture text -->

For GIHH , _νGIHH_ is equal to 61.205 while for A.L.M., _νA.L.M._ is equal to 63.497. This confirms that in average our method is superior to that of GIHH. 

The solution method is ended in accordance with the termination criteria. The termination condition takes in consideration avoiding useless computation and tries to avoid early termination. 

The proposed termination criteria, sets a global time limit: 



<!-- Start of picture text -->
Numberof Wells<br>Tl = max { 10000 ,  1000 NumberofWorkovers }<br><!-- End of picture text -->

seconds for the overall computation time while for every low-level heuristic the termination criteria relies on the number non-improving solutions, 



<!-- Start of picture text -->
Numberof Wells<br>Li = 100<br>NumberofWorkovers<br><!-- End of picture text -->

. In addition, we set a third termination criteria to terminate the whole algorithm once _W_ = 10 _NumberofWorkoversNumberof Wells_<sup>non-improving iterations is observed.</sup> 

Figure 2.3 presents the execution time behavior as a function of number of wells. Clearly, almost always, when the number of wells is less than 50, the CPU 

**Workover Rig Problem** 

**70** 

time is almost less than 5 seconds and when the number of wells is greater than 50, the consumed time is around 10 seconds using GIHH. However, the result shows that, except for _four_ instances, still our computational times are always inferior to those of GIHH. For instances that have more than 50 wells in it, our computational times remains around 7 seconds. 



<!-- Start of picture text -->
GIHH<br>A.L.M.<br>12<br>10<br>8<br>6<br>4<br>2<br>0<br>Instances<br>Computational Time (sec.)<br>Instance_10_3 Instance_15_3 Instance_15_5 Instance_20_3 Instance_20_5 Instance_25_3 Instance_25_5 Instance_25_7 Instance_30_3 Instance_30_5 Instance_30_7 Instance_35_3 Instance_35_5 Instance_35_7 Instance_50_5 Instance_50_7 Instance_50_9 Instance_50_10 Instance_75_7 Instance_75_9 Instance_75_10 Instance_100_7 Instance_100_9 Instance_100_10 Instance_100_12 Instance_125_7 Instance_125_10 Instance_125_12 Instance_150_7 Instance_150_10 Instance_150_12 Instance_175_7 Instance_175_10 Instance_175_12 Instance_200_7 Instance_200_10 Instance_200_12<br><!-- End of picture text -->

**Figure 2.3:** Execution time of each method. 

Figure 2.4, Figure 2.5 and Figure 2.6 report the statistics of heuristic calls by each proposition for each instance. In Figure 2.4, the largest percentage is 

**2.6 Numerical experiments** 

**71** 

dedicated to the order improvement heuristic in both cases (GIHH and A.L.M.). An absolute majority of the calls is associated with the order improvement heuristic in A.L.M. and a minor part belongs to the reconstructive heuristic. 



**Figure 2.4:** The constructive and improvement heuristics calls distribution by each method. 

**Workover Rig Problem** 

**72** 



**Figure 2.5:** the mutation and crossover heuristics calls distribution by each proposition. 



**Figure 2.6:** insert/drop and reconstructive heuristics calls distribution by each method. 

**2.6 Numerical experiments** 

**73** 

**Table 2.3:** Computational results of our branch, price and cut. 

||min(A.L|.M., GIHH)|||branch, price and cut(Monemi et al.,2|015)||
|---|---|---|---|---|---|---|---|
|Instance Name|Best Obj.|CPU (sec. )|#bb.nodes|#cols|( <sup>_fA.L.M −fB_&</sup><sup>_p_&</sup><sup>_C_</sup><br>_f_<sup>_B_&</sup><sup>_p_&</sup><sup>_C_</sup><br>)_×_100|CPU (sec.)|Term. Cond.|
|Instance_10_3|19683|0.117|0|26|0.00|1133.20|opt.|
|Instance_15_3|40054|1.143|0|31|0.00|1298.46|opt.|
|Instance_15_5|26055|5.019|0|37|0.00|1413.76|opt.|
|Instance_20_3|86809|0.241|2|40|0.00|3044.17|opt.|
|Instance_20_5|45985|1.164|2|53|0.00|3734.80|opt.|
|Instance_25_3|124236|1.045|2|74|0.00|4331.15|opt.|
|Instance_25_5|97772|0.638|2|88|0.00|4783.87|opt.|
|Instance_25_7|63494|0.150|0|105|0.01|5163.40|tlim.|
|Instance_30_3|162479|0.566|5|110|0.03|6415.23|tlim.|
|Instance_30_5|117757|0.220|6|156|0.10|6335.19|tlim.|
|Instance_30_7|94619|0.155|5|201|0.24|7561.65|tlim.|
|Instance_35_3|180341|1.074|10|226|3.55|7820.65|tlim.|
|Instance_35_5|159223|0.304|8|269|4.04|8214.07|tlim.|
|Instance_35_7|104206|0.208|5|318|5.23|9384.43|tlim.|
|Instance_50_5|276221|0.705|12|470|3.75|9633.20|tlim.|
|Instance_50_7|201456|0.556|11|512|11.55|10041.21|tlim.|
|Instance_50_9|200710|0.362|8|556|6.93|9792.10|tlim.|
|Instance_50_10|154070|0.295|10|601|9.36|9645.43|tlim.|



In the Table 2.3 we report our numerical experiments. The first column reports the instance name, followed by the column reporting best objective function of the solutions found by our hyperheuristic and the CPU times in the column immediately next to it. 

In column 4 and 5 , reports the number of branching performed and number of columns added before termination Monemi et al. (2015). The relative gap between the solution of our hyperheuristic and that found by the branch, price and cut upon termination was shown in the sixth column. In general, the solutions found by hyperheuristic are practically very good solutions. The CPU time is reported in the next column, which shows that while we can obtain a high quality solution with 

**Workover Rig Problem** 

**74** 

our heuristic very quickly, a similar quality solution with branch, price and cut take much longer. This may confirm that the proposed hyperheuristic is a good and reliable alternative for a mathematical programming-based method. 

## **2.7 Summary, conclusion and outlook to future work** 

Workover rig scheduling problem is an important problem in the highly sensitive petroleum production industry as it seeks to maintain the optimal production level of a company. There is a huge investment involved in acquiring, training, staffing and operations of workover rigs while the oil production itself plays direct role in the economy growth, welfare and the GDP of a country. 

We have proposed a new mixed integer linear model for the workover rig scheduling problem that is based on a time-arc indexed formulation. We proposed several valid inequalities. The results of hyperheuristic were used for setting the initial columns of an exact method. We have shown that as long as the optimal solution (or the optimal interval) is known, the solutions reported by the hyperheuristic are very near to optimal solutions. This confirms the particular efficiency of our learning mechanism in controlling the selection of heuristics and allowing the right heuristic to search the right part of the solution space at appropriate iterations. 

However, a major limitation of this work is that we have to keep a very small size set of heuristic as the search in the space of heuristics and neighborhoods 

**2.7 Summary, conclusion and outlook to future work** 

**75** 

becomes very time consuming and deteriorates the efficiency. Moreover, the discretization of planning horizon also needs to be done cleverly in order to avoid unnecessarily enlargement of search space for every heuristic. 

The research on this problem is very often limited to modeling it as a routing problem while perhaps scheduling is the dominating part of the problem. The literature is unaware of any multi-agent or distributed optimization techniques applied to this problem given an inherent distributed nature (in larger scale the wells are scattered within dispersed zones with long distances among the zones). 

Further research on minimizing workover _CO_ 2 emission, incorporating more real aspects such as workforce scheduling, task time window and ensuring robustness in the solution. 

**76 Workover Rig Problem** 

# **Chapter 3** 

# **Capacitated Single Allocation p-Hub Location Routing Problem** 

## **3.1 Introduction** 

The term _hub_ is commonly used in different domains such as transportation, logistics and telecommunication systems, among others. In almost all such areas, the hubs serve as consolidation, switching and sorting centers. In transportation and logistics, the hub-and-spoke structures are present in almost all modes of transport (cross-docks in national level, major airports and container ports in continental and inter-continental level). Hubs are facilities at which arriving flows of commodities in smaller volumes originated from the spokes are consolidated, sorted and re-distributed (repartitioned) in a larger volumes on fewer highly utilised links and sent to either the final destinations that are hubs or the hubs where the spoke 

**78 Capacitated Single Allocation p-Hub Location Routing Problem** 

destinations are allocated to them. The main motivation for deploying such a flow network structures is in exploiting economies of scale (in terms of time and/or cost) in transporting higher volumes on much more efficient corridors (connecting hubs). 

Given a graph _G_ ( _V, A_ ) where _V_ is the set origins and destinations and _A_ is the set of all possible arcs, Hub Location Problem (HLP) seeks a partition of nodes in _V_ into hub and spokes. Consequently, each spoke is associated to one or more hubs. In classical models, two main classes are distinguished Alumur and Kara (2008): 1) _Single Allocation_ : wherein each spoke node is assigned to only one hub, and 2) _Multiple Allocation_ : offering the possibility that a spoke be allocate to more than one hub node. Moreover, one also distinguishes between _capacitated_ and _uncapacitated_ variants depending on where the capacity is being imposed. Some authors also distinguish between the cases where cardinality of the set of selected hub nodes is defined exogenously and when it is an endogenous part of the problem. This topic has been one of the very active areas of research in the past two decades. 

We consider the previously defined graph _G_ , a fixed number, _p_ , of hubs node to be installed, Γ, the minimum number of spokes associated to each hub, _C_ , the capacity that can be installed on each feeder route, _wij_ , the demand to be transferred from _i_ to _j_ , and _tij_ , the cost between any two node _i_ and _j_ , which is taken in this study as the time needed to travel between node _i_ and _j_ . We also define _di_ as 

**3.1 Introduction** 

**79** 

the load of transporter after leaving node _i_ on a spoke-level route (the load at arrival minus the total demand of _i_ from every other node plus the total supply of _i_ to every other node). We seek to construct from the scratch a hub-and-spoke network, which is consist of a complete hub-level subgraph with _p_ hub nodes and _p_ spoke-level directed cyclic routes each of which composed of a hub node and all the spoke nodes allocated to it. The hub-level network is a complete subgraph where each two connected hub have a bidirectional link. The objective function of our problem seeks minimizing the total transit time composed of transportation plus transhipment time in the whole network provided that the total volume of flow on the spoke-level arcs does not violate the capacity of transporter on it, given a homogenous fleet of transporters. 

This problem is a special case of the _Bounded Cardinality Capacitated Hub Routing Problem (BCCHRP)_ proposed in Gelareh et al. (2015) in which the lower and upper bounds on the number of hub nodes coincide. We refer to this problem as _Capacitated Single Allocation p-Hub Location Routing Problem (CSApHLRP-1)_ . 

Figure 3.1 represents a solution for an instance with _|V |_ = _n_ = 10 nodes and _p_ = 3 fully interconnected hub nodes. The nodes 4, 5 and 7 represent hubs while all the remaining nodes considered as spokes. One observes that each hub together with spoke nodes allocated to it forms a directed cycle. In this solution, three cycles are define: i) 4 _→_ 0 _→_ 2, ii) 7 _→_ 9 _→_ 8 _→_ 6, and iii) 5 _→_ 3 _→_ 1. 

In this work we are dealing with a problem that fits within the category of 

**80 Capacitated Single Allocation p-Hub Location Routing Problem** 



**Figure 3.1:** A solution of network with 3 hubs and 10 nodes. 

capacitated single allocation hub location problems (CSAHLP). In the following, we review some of the related work in the literature with particular emphasis on the single allocation scheme and exogenous number of hubs in modeling part and (Meta)heuristic approaches in solution methods. Ebery et al. (2000) proposed a hybrid method that combines evolutionary algorithm (EA) with a branch-andbound method (B&B) in order to solve a capacitated single allocation hub location problem. In this work, the proposed EA selects the set of hubs while B&B continues with the allocation part of the problem by allocating the non-hubs to the located hubs. 

Correia et al. (2009) proposed a Mixed Integer Programming (MIP) formulation for the problem of single allocation where hub capacity is not an exogenous value but it is a variable with discrete choices of value. Several variants of this problem have been proposed including: capacitated and uncapacitated for single allocation problem, and capacitated flow splitting (Campbell et al., 2007) for 

**3.1 Introduction** 

**81** 

multiple allocation. 

A MIP formulation and branch-and-cut algorithm were proposed by RodríguezMartín et al. (2014), which consider a single allocation model, the capacity constraint in terms of number of spokes per route, and a fixed number of hubs. 

Ebery et al. (2000) proposed a MIP formulation and a heuristic for capacitated multiple allocation hub location problem. Uncapacitated _p_ -Hub problem wherein each spoke should be connected to _r_ hubs, is studied by Peiró et al. (2014). The authors proposed a GRASP method as a solution method. 

An Uncapacitated _p_ -Hub Single Allocation Location problem, has been proposed in Ge et al. (2007) that seeks _p_ hubs in the network and single allocation of non-hubs to the hubs in a manner to minimize the total cost of transporting between all origin-destination pairs in the network. In this work, the spokes are simply connected to the hub and there is no particular topology imposed on the spokes allocated to the same hub. 

A MIP formulation has been proposed by Gelareh et al. (2013a) for a hub and spoke network design and fleet deployment of liner shipping, in order to minimize weighted sum of transit times and the fixed deployment costs. The proposed MIP is based on 4-index formulation of HLPs and allocated spokes form directed cycles (the so called _string_ ). On every string, the vessel class or capacity to be installed to accommodated the volume of flow on the string must be determined from a given heterogeneous fleet. 

The current work has some similarity with the one studied in Rodríguez-Martín 

**82 Capacitated Single Allocation p-Hub Location Routing Problem** 

et al. (2014) but it s distinguished from it, as follows: In Rodríguez-Martín et al. (2014) the objective function is only to minimize the total transportation cost while in this work transshipment cost(time) has also been taken into account. In the former, the spoke-level routes are undirected while we consider that flow on the spoke-level route circulates in only one direction. Finally, in Rodríguez-Martín et al. (2014), the capacity is defined as the maximum number of spokes along a spoke-level route while we define it as the volume of flow circulating on the spoke-level route that needs to respect the capacity of transporter on it. 

This work is also distinguished from Gelareh et al. (2015), by the fact that we do not take into account any upper/lower bound on the number of hubs, rather we assume a fixed cardinally, _p_ , as an exogenous parameter. 

To the best of our knowledge, so far, the non-exact methods applied to variants of hub location problems were either metaheuristics (population-based or trajectorybased) or classical heuristics. 

Kratica et al. (2012) proposed a genetic algorithm (GA) for solving an uncapacitated multiple allocation problem. Binary encoding and genetic operators are used and the run-time is optimized by a caching technique. 

Rabbani and Kazemi (2015) proposed a genetic algorithm and a simulated annealing for solving an uncapacitated multiple allocation _p_ -hub center problem wherein the objective function is calculated based on Dijkstra’s algorithm. 

A heuristic based on (GA) is proposed by Stanimirovic (2008) in order to solve uncapacitated multiple allocation _p_ -hub median problem. Described GA uses 

**3.1 Introduction** 

**83** 

binary representation of the solutions. A mutation operator with frozen bits and a caching technique, all of that contribute to improve the solution quality. 

Randall (2008) proposed an ant colony metaheuristic optimization method. Four variations exploring different construction modelling choices are developed to solve the capacitated single allocation hub location problem. 

Multiple Ant Colony Optimization (MACO) algorithm is proposed by Ting and Chen (2013) to solve a capacitated location routing problem, which is decomposed into two subproblems: 1) facility location problem and 2) multiple depot vehicle routing problem. The two subproblems are treated together within MACO where collaboration of colonies is operated by interchanging information through pheromone renewing the chosen location and costumer assignment. 

In order to avoid local optima in _p_ -hub location problem, Klincewicz (1992) proposed two metaheuristic: tabu search and GRASP algorithm. The considered objective was to minimize the total costs of sending traffic over links. In these two methods, local search procedure is based on the 2-exchange neighborhood. 

A _p_ -median Problem was treated by Rolland et al. (1997) that proposed a tabu search algorithm which uses short term and long term memory, and a strategic oscillation for random tabu list sizes. 

Abdinnour-Helm (1998) developed a hybrid method based on a combination of genetic algorithm and tabu search in order to solve an uncapacitated hub location problem with single allocation. Genetic Algorithm is used to choose hubs, while Tabu Search is used to assign spokes to hubs. 

A two phases of tabu search algorithm (location and routing phases with short 

**84 Capacitated Single Allocation p-Hub Location Routing Problem** 

term memory) has been considered by Tuzun and Burke (1999), in order to solve capacitated hub location problem with single allocation. 

Simulated annealing (SA) and iterated local search (ILS) were proposed by Zarandi et al. (2015) in order to solve single-allocation hub median problem. Another simulated annealing for single-allocation capacitated hub location problem was proposed by Vincent et al. (2010), given that routes and hubs are constrained by capacity. 

Uncapacitated single allocation _p_ -hub median problem was studied by Ili´c et al. (2010). They proposed a Variable Neighborhood Search (VNS) where variable neighborhood descent (VND) based local search uses three different neighborhood structures. Another VNS was proposed by Jarboui et al. (2013) but for uncapacitated single allocation hub location problem. VND is used as local search and it consists of five neighborhood structures, including insertion and swap operators. Table 3.1 summarizes some key features in closely related contributions. 

**Table 3.1:** A summary of main elements of the relevant contributions in literat- 

ure. 

|Work|Allocation Scheme|No. Hubs|Objective|Capacity|Cycle Length|No. Vehicles|Solution method|
|---|---|---|---|---|---|---|---|
|Nagy and Salhi(1998)|pickup/delivery routes|endogenous|cost|yes|yes|endogenous|MIP + heuristic|
|Cetiner et al.(2006)|multiple allocation|endogenous|cost+fleet|no|yes|endogenous|heuristic|
|de Camargo et al.(2013)|single allocation|endogenous|cost|no|yes|endogenous|MIP + Benders decomposition|
|Wasner and Zäpfel(2004)|multiple allocation|endogenous|cost|yes|yes|endogenous|MIP + heuristic|
|Rodríguez-Martín et al.(2014|)<br>single allocation|exogenous|cost|#. spoke per route|no|one per route|MIP + branch-and-cut|
|Gelareh et al.(2013b)|single allocation|exogenous|cost+fleet|yes|multiple of weeks|variable|MIP+Lagrangian decomposition|
|Gelareh et al.(2015)|single allocation|_q_ = 3 _≤.. ≤p_|time|yes|_≥_2spokes|one per route|MIP+branch-and-cut+Benders|
||||(transit+transshipment)|||||
|current work|single allocation|exogenous|time<br>(transit+transshipment)|yes|_≥_2spokes|one per route|MIP+Lagrangian Relaxation<br>+ Hyperheuristic|



This work contributes to the state-of-the-arts as follows: First, we present a 

**3.1 Introduction** 

**85** 



**Figure 3.2:** A solution of network with 3 hubs and 10 nodes. 

mixed integer linear formulation with 2-index design variables that is basically similar to the model in Gelareh et al. (2015) and we proposed a 3-indexed design formulation where the number of hubs is fixed. We then propose a particular Lagrangian relaxation of the problem allowing to exploit the reduced cost of spoke level variables. The outputs of this relaxation scheme are then used in our proposed hyperheuristic framework. To the best of our knowledge, this is the first work tackling a variant of hub location problems using a hypereutectic approach (in particular exploiting Lagrangian relaxation information in hyperheuristic). The proposed hyperheuristic is comprised of a portfolio of low level heuristics (some of which use the Lagrangian relaxation information) and a _heuristic selection_ method that learns in the course of process how to choose among the existing heuristics the one leading to a higher likelihood of success and improvement. The later is in fact a reinforcement learning method that has been inspired from the concept of 

**86 Capacitated Single Allocation p-Hub Location Routing Problem** 

_association rules_ in the _business data mining_ world. To further expand our research, we have also tackled the problem presented by Rodríguez-Martín et al. (2014). For this problem, we propose a hyperheuristic method with another method of reinforcement learning methods called Q-learning, in order to guide in selection heuristic to be applied during the search. 

The two aforementioned problems are distinct in the sense that as the first one is a transportation problem, the capacity concerns the volume of flow on the arcs (spoke-level arc) while the second treats the capacity as the maximum number of spokes along a cycle presenting the limited number of ports on switches, routers etc. in a telecommunications network. We denote the first problem as CSA _p_ HLRP-1, and the second CSA _p_ HLRP-2. 

The remainder of this paper is organized as in the following: In section 3.2, we propose a mathematical model is a 3-index design MIP and present the 2-index design formulation for CSA _p_ HLRP-1 in Gelareh et al. (2015). Than we present the mathematical formulation of the problem in Rodríguez-Martín et al. (2014), CSA _p_ HLRP-2. The section 3.3 is divided into two parts. In the first part we propose five Lagrangian relaxations for the CSA _p_ HLRP-1 2-index design model, which is capable of offering approximation of reduced costs of the spoke-level network variables. In the second part a hyperheuristic solution approach and its components exploiting information of Lagrangian dual to guide are presented for the CSA _p_ HLRP-1 problem, and another one for the CSA _p_ HLRP-2 problem. Computational experiments and discussions are reported in section 3.4. Finally, in section 3.5, we conclude our work and present the possible future work. 

**3.2 Mathematical Formulation** 

**87** 

## **3.2 Mathematical Formulation** 

We present two mathematical models for the first variant of HLRP problem. For the first problem, CSA _p_ HLRP-1, we propose a 3-index design variable mathematical formulation CSA _p_ HLRP-1-F1, and we present another model proposed by Gelareh et al. (2015) with 2-index design variable, CSA _p_ HLRP-1-F2. 

Considering CSA _p_ HLRP-2, we present the model proposed by RodríguezMartín et al. (2014). 

The following parameters and variables are used in models, CSA _p_ HLRP-1-F1 and CSA _p_ HLRP-1-F2. The only difference in variables in these two models, refers to variable _r_ , which will be declared as 2-index or 3. 

**Table 3.2:** CSA _p_ HLRP-1-F1 and CSA _p_ HLRP-1-F2 Models Parameters. 

|_wij_:|the flow from_i_to_j_,|
|---|---|
|_tij_:|the distance/time on a direct link on the edge (arc)_i −j_,|
|_α_:|the factor of economies of scale (the factor<br>of travel time efficiency over hub edges),|
|_p_:|the upper bound on the number of hubs (depots),|
|Γ:|the minimum number of spokes allocated<br>to each hub/depot node,|
|_C_<sup>_v_</sup>:<br>_ϕ_<sup>_k_</sup>:|the capacity of each vehicle for each feeder network,<br>the (fixed) average transshipment time at hub_k_.|



**88 Capacitated Single Allocation p-Hub Location Routing Problem** 

**Table 3.3:** The decision variables for CSA _p_ HLRP-1-F1 and CSA _p_ HLRP-1-F2. 

|_xijkl_:|the fraction of flow from_i_to_j_<br>traversing inter-hub edge_{k, l}_,|
|---|---|
|_sijkl_:|the fraction of flow from_i_to_j_<br>traversing non-hub edge_{k, l}_,|
|_rij_(_rijk_):|1, if the arc (i, j) belongs to a spoke-level|
||route (i and j are allocated to hub k in CSA_p_HLRP-1-F1),<br>0 otherwise.|
|_zik_:|1, if the node_i_is allocated to node_k_where_k_is a hub,<br>0 otherwise.|



### **3.2.1 (CSA** _p_ **HLRP-1-F1)** 

_(CSApHLRP-1-F1)_ 

|min<br>�<br>_i,j,k,l_<br>(_tkl_(_sijkl_+_αxijkl_)) +<br>�<br>_i,j,k,l_:(_k̸_=_i∨l̸_=_j_)<br>(_ϕ_<sup>_k_ </sup>+_ϕ_<sup>_l_</sup>)_xijkl_|(3.1)|
|---|---|
|_s. t._||
|�<br>_k_<br>_zkk ≤p_<br>�<br>_l_<br>_zkl_ = 1|(3.2)<br>_∀k ∈V_|
||(3.3)|
|_rijk ≥_Γ_zkk_|_∀k_|
||(3.4)|
|�<br>_j_<br>_rijk_ =_zik_|_∀i, k_<br>(3.5)|



**3.2 Mathematical Formulation** 

**89** 

|�<br>_j_<br>_rjik_ =_zik_||_∀i, k_|
|---|---|---|
||(3.6)||
|�<br>_j_:_l̸_=_j_<br>_rjlk_ =<br>�<br>_j_:_l̸_=_j_<br>_rljk_|(3.7)|_∀l, k_|
|_rijk_+_rjik ≤zik_|_∀i, j, k_ :|_j̸_ =_i_|
||(3.8)||
|_rijk_+_rjik ≤zjk_|_∀i, j, k_ :<br>(3.9)|_j̸_ =_i_|
|_zik ≤zkk_|_∀i, k ∈V_ : <br>(3.10)|_k̸_ =_i_|
|�<br>_k̸_=_i_<br>(_xijik_+_sijik_) = 1_,_|_∀i, j ∈V_ :<br>(3.11)|_j̸_ =_i_|
|�<br>_l̸_=_j_<br>(_xijlj_ +_sijlj_) = 1_,_|_∀i, j ∈V_ :|_j̸_ =_i_|
||(3.12)||
|�<br>_l̸_=_i,k_<br>(_xijkl_+_sijkl_) =<br>�<br>_l̸_=_j,k_<br>(_xijlk_+_sijlk_)_,_|_∀i, j, k ∈V, k̸ ∈{_|_i, j, }_|
||(3.13)||
|�<br>_l̸_=_k_<br>_xijkl ≤zkk_|_∀i, j, k ∈V_ :_j̸_ =_i,_|_k < l_|
||(3.14)||



**Capacitated Single Allocation p-Hub Location Routing Problem** 

**90** 



<!-- Start of picture text -->
� xijlk ≤ zkk ∀i, j, k ∈ V :  j̸ =  i, k < l<br>l̸ = k<br>(3.15)<br>sijkl ≤ � rklm ∀i, j, k, l ∈ V :  l̸  =  k<br>m<br>(3.16)<br>� wijsijkl ≤ C, ∀k ∈ V<br>ijl : j̸ = i<br><!-- End of picture text -->



<!-- Start of picture text -->
(3.17)<br><!-- End of picture text -->



<!-- Start of picture text -->
r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.18)<br><!-- End of picture text -->

The objective function (3.1) is comprised of two parts; the first accounts for the total transportation times and the second part is the transshipment times. The transportation part is composed of travel times on the hub-level edges as well as spoke-level arcs. The travel time on the hub-level edges is discounted by _α_ because the transporters offer faster services. The transhipment time is measured twice for every O-D flow; once at the first hub visited along O-D path and once at the last hub along the same path. Constraints (3.2) sets a limit on the number of hub nodes (depots) that can be installed while constraints (3.3) guarantee that every node is allocated to exactly one hub depot. A self-allocation of _i_ (i.e. _zii_ = 1) represents a hub depot _i_ . If a node is designated as a hub node, there must be at least Γ nodes (including itself) allocated to it (making the route) as stated in (3.4). Here, we assume that Γ = 3. Constraints (3.5) (3.6) ensure that every spoke node that is assigned to a hub node will not be part of more than one route (i.e. will be 

**91** 

#### **3.2 Mathematical Formulation** 

part of exactly one route). Constraints (3.7) ensure that, the number of arcs arriving to a spoke node is equal to the number of outgoing ones. Constraints (3.8)-(3.9) ensure that a leg on a given route can be established only if both end-nodes are allocated to the same hub depot. A spoke node can only be allocated to a hub node as in constraints (3.10). Constraints (3.11)-(3.13) stand for the flow conservation for every O-D pair. Constraints (3.11)-(3.15) state that traversing a hub edge is equivalent to traversing an edge where both end-points are hub nodes. Constraints (3.16) ensure that the flows on the route (spoke) edges will traverse in the correct direction and on an existing feeder edge. Constraints (3.17) ensure that the volume of flow on every leg of the routes associated to the hub nodes is constrained to the capacity of vehicles. Given that the flow leaving a spoke node will traverse a unique link encompassed from that spoke node, the term on the left side determines the whole flow leaving the spoke node _k_ no matter originated from _k_ itself or passing through it. 

### **3.2.2 (CSA** _p_ **HLRP-1-F2)** 

A 2-index (design variables) was proposed in Gelareh et al. (2015) for the Bounded Cardinality Capacitated Hub Routing Problem (BCCHRP). In this model, definition of variable _r_ does not indicate the allocation for end-nodes to any hub. More precisely, _rij_ does not determine to which hub it belongs. This somehow helps to get rid of some of the constraints in the preceding model, however, in order to make sure that both end-points belong to the same hub node one needs to add some additional constraints. 

**92 Capacitated Single Allocation p-Hub Location Routing Problem** 

#### _(CSApHLRP-1-F2)_ 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl (3.19)<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>s. t.<br>zkk ≤ p (3.20)<br>�<br>k<br>zkl = 1 ∀k ∈ V<br>�<br>l<br>(3.21)<br>zik ≤ zkk ∀i, k ∈ V :  k̸ =  i<br>(3.22)<br>zik ≥ Γ zkk ∀k ∈ V<br>�<br>i<br>(3.23)<br>� rij = 1 ∀i ∈ V<br>j̸ = i<br>(3.24)<br>� rji = 1 ∀i ∈ V<br>j̸ = i<br>(3.25)<br>rij +  rji ≤ 2  − zik − zjl ∀i, j, k, l ∈ V :  j̸ =  i, k̸ =  l<br>(3.26)<br>rij +  rji ≤ 1 ∀i, j ∈ V :  j̸ =  i,<br>(3.27)<br><!-- End of picture text -->

**93** 

#### **3.2 Mathematical Formulation** 



<!-- Start of picture text -->
�( xijik  +  sijik ) = 1 , ∀i, j ∈ V :  j̸ =  i,<br>k̸ = i<br>(3.28)<br>�( xijlj +  sijlj ) = 1 , ∀i, j ∈ V :  j̸ =  i,<br>l̸ = j<br>(3.29)<br>�( xijkl  +  sijkl ) = �( xijlk  +  sijlk ) , ∀i, j, k ∈ V, k̸ ∈{i, j, } ,<br>l̸ = i,k l̸ = j,k<br>(3.30)<br>� xijkl ≤ zkk ∀i, j, k ∈ V :  j̸ =  i, k < l<br>l̸ = k<br>(3.31)<br>� xijlk ≤ zkk ∀i, j, k ∈ V :  j̸ =  i, k < l<br>l̸ = k<br>(3.32)<br>sijkl ≤ rkl ∀i, j, k, l ∈ V :  l̸  =  k<br>(3.33)<br>� wijsijkl ≤ C, ∀k ∈ V<br>ijl : j̸ = i<br>(3.34)<br>r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.35)<br><!-- End of picture text -->

The objective function (3.19) and all constraints (3.20)- (3.22) remain the same as in the previous model. Constraints (3.23), are in fact equivalent to the constraints (3.4) in terms of z variables. Constraints (3.24) and (3.25) ensure that one arc 

**94 Capacitated Single Allocation p-Hub Location Routing Problem** 

departs and one arc arrives at every node, respectively. Constraints (3.26), ensure that a spoke arc cannot exist if its end-points are allocated to different hubs and constraints (3.27) guarantee that an arc can appear only in either directions. The flow conservation constraints (3.28))-(3.32) are the same as in the previous model. Constraints (3.33) make sure that a spoke flow will traverse an existing spoke arc. The capacity constraints ((3.34)) are the same as in the previous model. It must be noted that in the 2-indexed formulation, the constraints (3.8)-(3.9) are no longer applicable. Instead, we needed to introduce constraints (3.26). Briefly speaking, approximately 2 _n_<sup>3</sup> constraints and ( _n −_ 1)( _n_<sup>2</sup> _− n_ ) variables are removed in favor of 2 _n_ ( _n −_ 1) + 2 _n_<sup>2</sup> ( _n −_ 1)<sup>2</sup> constraints and _n_ ( _n −_ 1). Moreover, less number of integer variables in the primal is expected to facilitate resolution and convergence of a branch-and-bound-based method. 

### **3.2.3 (CSA** _p_ **HLRP-2)** 

Let _E_ = _{_ [ _i, j_ ] : _i, j ∈_ V _, i̸_ = _j}_ , the following parameters and variables are used in this model. 

**3.2 Mathematical Formulation** 

**95** 

**Table 3.4:** CSA _p_ HLRP-2 Model Parameters. 

|_V_|set of nodes,|
|---|---|
|_wij_|the traffic demand from_i_to_j_,|
|_cjl_|cost of routing from node_j_ to_l_,|
|_oi_|total amount of demand originate at node_i_,|
|_di_|total amount of demand with destination at node_i_,|
|_q_|the maximum number of nodes assigned spokes to a hub,|
|_fe_|cost of using the edge_e ∈E_ in a cycle,|
|_β_|factor of changing the relative weight of the cycle<br>edge costs in the objective function.|



**Table 3.5:** CSA _p_ HLRP-2 Decision Variables. 

|_xe_|edge variable in a cycle with at least three edges,|
|---|---|
|_δ_(_S_)|set of edges with exactly one end point in_S_ and_E_(_S_)|
|_z_<sup>1</sup><br>_jj_|1, if node j_∈V_ is a hub and no other node is assigned to_j_,|
|_z_<sup>1</sup><br>_ij_|1, if node_j ∈V_ is a hub and_i_is assigned to_j_ with_i̸_=_j_,|
|_z_<sup>2</sup><br>_ij_|1, if node_j ∈V_ is a hub and_i_is assigned to_j_,|
|_g_<sup>_i_</sup><br>_jl_|Amount of traffic that originates at node_i ∈V_|
||and travels from hub_j ∈V_ to hub_l ∈V −{j}_|



_(CSApHLRP-2)_ 



<!-- Start of picture text -->
min � � ( cijoi  +  cjidi ) � zij 1 +  z ij 2 � +<br>i∈V j∈V −{j}<br>α � � cjl � gjl i +  β  � 2 fijzij 1 + � fexe  (3.36)<br>j∈V l∈V −{j} i∈V  � i∈V j∈V −{j} e∈E <br>s. t.<br>� zij 1 z ii 1 + � zji 1 + � zij 2 = 1 ∀i ∈ V (3.37)<br>j∈V −{i} j∈V −{i} j∈V<br><!-- End of picture text -->

#### **96 Capacitated Single Allocation p-Hub Location Routing Problem** 



<!-- Start of picture text -->
� zij 2 ≤ qz jj 2 ∀j ∈ V (3.38)<br>i∈V<br>� zij 1 +  z jj 2 =  p (3.39)<br>j∈V �� i∈V �<br>� gjl i − � glj i =<br>l∈V −{j} l∈V −{j}<br>� � zij 1 +  z ij 2 − z mj 1 − z mj 2 � +  wij zij 1 +  z ij 2 − � zkj 1 − z jj 2 ∀i, j ∈ V, i̸  =  j<br>m∈V −{i,j} � k∈V �<br><!-- End of picture text -->



<!-- Start of picture text -->
(3.40)<br>� gjl j − � glj j = � zkj 1 +  z jj 2 − z mj 1 − z mj 2 ∀j ∈ V<br>l∈V −{j} l∈V −{j} m∈V −{j} �� k∈V �<br>(3.41)<br><!-- End of picture text -->



<!-- Start of picture text -->
x ( δ ( i )) = 2 � zij 2 ∀i ∈ V (3.42)<br>j∈V<br>x ( δ ( S ))  ≥ 2 � zij 2 ∀S ⊂ V, i ∈ S (3.43)<br>j∈V −{S}<br>xii′ +  zij 2 +  z i 2 ′ j ′ ≤ 2 ∀ [ i, i ′ ]  ∈ E, j, j ′ ∈ V, j̸ =  j ′ (3.44)<br>xe ∈{ 0 ,  1 } ∀e ∈ E (3.45)<br>zij 1 ∈{ 0 ,  1 } ∀i, j ∈ V (3.46)<br>zij 2 ∈{ 0 ,  1 } ∀i, j ∈ V (3.47)<br>gjl i ≥ 0 ∀i, j ∈ V, l ∈ V −{j} (3.48)<br><!-- End of picture text -->

In order to have a feasible solution, we need _pq ≥|V |_ . _cijoi_ + _cjidi_ represents the cost of assigning node _i_ to hub _j_ . Where _i_ and _j_ are hubs then the routing cost is discounted by a factor of _α_ , the same as the previous problem. Two nodes form 

**3.3 Solution algorithm** 

**97** 

a cycle with a cost of 2 _fij_ . The objective function (3.36) accounts for the total installation cost of the edges and the routing of flows. Constraints (3.37) ensure that a node _i_ can be in one of the four different situations: 1) the unique node allocated to another hub (case<sup>�</sup> _j∈V −{i}_<sup>_z_</sup> _ij_<sup>1=1),2)ahubwithoutothernode</sup> allocated to it (case _zii_<sup>1= 1), 3) it is a hub with one other node specified to it (case</sup> � _j∈V −{i}_<sup>_z_</sup> _ji_<sup>1=1), 4) a hub is specified to another hub at least two other nodes</sup> (case<sup>�</sup> _j∈V_<sup>_z_</sup> _ij_<sup>2= 1). Constraints (3.38) are capacity constrains to guarantee that</sup> a cycle does not contain more than _q_ nodes. _p_ is the number of hubs to open in constraint (3.39). The flow balance constraints for the traffic on the hub network is due to constraints (3.40) and (3.41). Constraints (3.42) states that two edges must be incident to a node that is on a ring containing at least two other nodes. Constraints (3.43) maintain the connectivity of the cycles. In case, node _i ∈ S_ is allocated to a hub in set _V/S_ , then the cycle which holds node _i_ has to cross the cut declared by subset _S_ and _x_ ( _δ_ ( _S_ )) _≥_ 2. Constraints (3.44) prohibit nodes allocated to different hubs to be on the same cycle. 

It must be note that, the constraints (3.36)-(3.48) is a model for the SA _p_ HMP (Single Allocation _p_ Hub Median Problem) as _β_ = 0. 

## **3.3 Solution algorithm** 

The proposed solution algorithm, for CSA _p_ HLRP-1, is a lower/upper bound solution method. We examine several Lagrangian relaxation schemes of this problem 

#### **98 Capacitated Single Allocation p-Hub Location Routing Problem** 

with respect to the quality of their bounds. Each relaxation behaves independently regarding the convergence of dual multipliers as well as development of Lagrangian relaxation objective function variable coefficients. Therefore, the information stored in objective function variable coefficients can be used to guide different heuristic algorithms that are part of a hyperheuristic framework. 

### **3.3.1 Lagrangian relaxation** 

Lagrangian relaxation for solving (mixed) integer programming problems was first proposed in Geoffrion (1974); Geoffrion and Bride (1978) and later in Fisher (1981, 2004). The idea behind this method is to relax _complicating constraints_ by penalizing the objective function upon violation of these constraints. The relaxed problem is expected to be easier to solve than the original problem and provides a dual bound on the optimal value (as well as valuable information about the dual) of the problem (see Guignard (2003) for a comprehensive survey of the method.). Three well-known methods are commonly practiced in the literature for solving the Lagrangian relaxation problems. The oldest and most well-known one is the _subgradient_ method as an iterative method for solving convex minimization problems. The subgradient method was originally proposed in the 60’s in the former Soviet Union. Almost at the same time, a very similar method has been also proposed in Held and Karp (1971) for solving traveling salesman problem. Later, Lemarechal (1975) proposed the well-known bundle methods as an extension to the simple subgradient. The volume algorithm was later proposed in Barahona 

**3.3 Solution algorithm** 

**99** 

and Anbil (2000) as a methods which simultaneously produces a primal feasible solution and a dual bound for the problem. A further analysis of volume algorithm and its relation with bundle methods has been studies in Bahiense et al. (2002). 

Several variants of the subgradient-based methods have been proposed in the literature. Here, based on some observation from our preliminary computational experiments, we opted to use the well-known bundle method of Frangioni (1995) and the corresponding code (publicly available). 

Dualizing some constraints of a MIP model, in Lagrangian fashion, may result in a Lagrangian problem that is easier to solve and its optimal value is a lower bound on the original problem (case of minimization problems) Fisher (2004). In brief, Lagrangian relaxation decomposes constraints of the problem into two separate group:1) The first group, usually named as hard constraints, which are dualized (are transferred and penalized in the objective function), and 2) The remaining subset of constraints that remain in the subproblem. 

Let _u_<sup>_∗_</sup> _∗_<sup>_, u∗_</sup> _∗∗_<sup>and</sup><sup>_u∗_</sup> _∗∗∗_<sup>are the Lagrangian multipliers with the proper dimensions</sup> and sign (unsigned for the equality constraints and nonnegative for the inequalities, i.e. _≤_ ). In the following, we present five different lagrangian relaxations for the mathematical model of in CSA _p_ HLRP-1. 

#### **LRX1: design relaxation** 

The aim of this relaxation is 1) to accommodate the hub location variables ( _zkk_ ) in the objective function problem with a cost as a function of Lagrangian multipliers, 

**100** 

#### **Capacitated Single Allocation p-Hub Location Routing Problem** 

2) to obtain a subproblem that can be efficiently solved using a general-purpose MIP solver, and 3) determining the values of flow variables by inspection. 

The new costs for design variables are calculated by _−_<sup>�</sup> _ij_ : _j̸_ = _i_<sup>(</sup><sup>_u_</sup> _ijk_<sup>4+</sup><sup>_u_5</sup> _ijk_<sup>) for</sup> every _zkk_ . These costs are going to be used as _guiding information_ in the heuristic algorithm to bias the search space exploration. 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl +<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>� u 1 ij ( xijik  +  sijik )  − 1 + � u 2 ij ( xijlj +  sijlj )  − 1 +<br>i,j̸ = i �� k̸ = i � i,j̸ = i �� l̸ = j �<br>� u 3 ijk ( xijkl  +  sijkl )  − �( xijlk  +  sijlk ) +<br>i,j,k̸ =( i,j ) �� l̸ = i,k l̸ = j,k �<br>� u 4 ijk xijkl − zkk + � u 5 ijk xijlk − zkk<br>ijk : j̸ = i,k<l �� l̸ = k � ijk : j̸ = i,k<l �� l̸ = k �<br>� u 6 ijkl ( sijkl − rkl ) + � u 7 k ( � wijsijkl − C )<br>i,j,k,l̸ = k k ijl : j̸ = i<br>(3.49)<br>s. t.<br>(3.20) ,  (3.21) ,  (3.22) ,<br>(3.23) ,  (3.24) ,  (3.25) ,  (3.26) ,<br>(3.27)<br>r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.50)<br><!-- End of picture text -->

**3.3 Solution algorithm** 

**101** 

#### **LRX2:** _z_ **-relaxed** 

This relaxation aims at accommodating all the _zij_ (but no _rij_ ) variables in the objective function in addition to the already existing flow variables. In this way, the dual information will be contained in the coefficients of _zij_ variables and such modified costs can be exploited in guiding the heuristic algorithm by allowing better identifying location of hub nodes and allocation of spoke nodes to the hub nodes. 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl +<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>u 1 ij zkk − p + � u 2 k zkl − 1 + � u 3 ik ( zik − zkk )<br>�� k � k �� l � ik : k̸ = i<br>� u 4 k Γ zkk − � zik + � u 5 ijk xijkl − zkk +<br>k � i � ijk,j̸ = i,k<l �� l̸ = k �<br>u 6<br>� ijk xijlk − zkk<br>ijk,j̸ = i,k<l �� l̸ = k �<br>(3.51)<br><!-- End of picture text -->



<!-- Start of picture text -->
s. t.<br>(3.24) ,  (3.25) ,  (3.26) ,  (3.27) ,<br>(3.28) ,  (3.29) ,  (3.30) ,<br>(3.33) ,  (3.34) ,<br>r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.52)<br><!-- End of picture text -->

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**102** 

#### **LRX3:** _r_ **-relaxed** 

This relaxation aims at accommodating all the _rij_ (but no _zij_ ) variables in the objective function in addition to the already existing flow variables. By doing so, the dual information will be contained in the coefficients of _rij_ variables. Such information can partially describe the network and route structures and can be used to either constructing a partial initial solution or, in general, to guide the heuristic by a given frequency. 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl +<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>� u 1 ij rij − 1 + � u 2 ij rji − 1 +<br>i,j̸ = i �� j̸ = i � i,j̸ = i �� j̸ = i �<br>� u 3 ijkl ( rij +  rji − 2 +  zik +  zjl ) + � u 4 ij ( rij +  rji − 1)+<br>ijkl : k̸ = l,j̸ = i i,j̸ = i<br>� u 5 ijkl ( sijkl − rkl )+<br>ijkl,l̸ = k<br>(3.53)<br><!-- End of picture text -->

_s. t._ 



<!-- Start of picture text -->
(3.20) ,  (3.21) ,  (3.22) ,  (3.23)<br>(3.28) ,  (3.29) ,  (3.30)<br>(3.31) ,  (3.32) ,  (3.34)<br>r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.54)<br><!-- End of picture text -->

**3.3 Solution algorithm** 

**103** 

#### **LRX4:** _z, r_ **-relaxed** 

The idea is almost the same as that of LRX2 except that in addition to the _zij_ variables, all _rij_ will also appear in the objective function and their modified costs can be used to guide the heuristic algorithms. Moreover, the resulting subproblem is a computationally inexpensive problem to solve using any of the general-purpose solvers (even often by inspection). Some partial information such as location of hub nodes, allocation of spokes to the routes and some edges along routes can be exploited by using this relaxation. 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl +<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>u 1 zkk − p + � u 2 k zkl − 1 + � u 3 ik ( zik − zkk )<br>�� k � k �� l � i,k̸ = i<br>� u 4 k Γ zkk − � zik + � u 5 i rij − 1 + � u 6 i rji − 1 +<br>k � i � i �� j̸ = i � i �� j̸ = i �<br>� u 7 ijkl ( rij +  rji − 2  − zik − zjl ) + � u 8 ij ( rij +  rji − 1)<br>ijkl,l̸ = k,j̸ = i i,j̸ = i<br>(3.55)<br><!-- End of picture text -->

_s. t._ 



<!-- Start of picture text -->
(3.28) ,  (3.29) ,  (3.30)<br>(3.31) ,  (3.32) ,  (3.33) ,  (3.34)<br>r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.56)<br><!-- End of picture text -->

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**104** 

#### **LRX5: Lagrangian decomposition** 

The aim is to decompose the LR into two separate problems, one in the space of design variables _z, r_ and another one in the space of flow variables _x, s_ . 



<!-- Start of picture text -->
min � ( tkl ( sijkl  +  αxijkl )) + � ( ϕ k +  ϕ l ) xijkl +<br>i,j,k,l i,j,k,l :( k̸ = i∨l̸ = j )<br>� u 1 ijkl ( rij +  rji − 2 +  zik +  zjl ) + � u 2 ijk xijkl − zkk +<br>i,j̸ = i,k,l̸ = k i,j̸ = i,k<l �� l̸ = k �<br>� u 3 ijk xijlk − zkk + � u 4 ijkl ( sijkl − rkl )<br>i,j̸ = i,k<l �� l̸ = k � ijkl : k̸ = l<br><!-- End of picture text -->



<!-- Start of picture text -->
(3.57)<br><!-- End of picture text -->

_s. t._ 



<!-- Start of picture text -->
(3.20) ,  (3.21) ,  (3.22) (3.58)<br><!-- End of picture text -->



<!-- Start of picture text -->
(3.23) ,  (3.24) ,  (3.25) ,  (3.27) (3.59)<br><!-- End of picture text -->



<!-- Start of picture text -->
(3.28) ,  (3.29) ,  (3.30) ,  (3.34) (3.60)<br><!-- End of picture text -->



<!-- Start of picture text -->
r ∈ B |V | 2 , z ∈ B |V |×|V | , xijkl, sijkl ∈∈ R[0 |V ,  | 1] 4 (3.61)<br><!-- End of picture text -->

### **3.3.2 Hyperheuristic for CSA** _p_ **HLRP-1 and CSA** _p_ **HLRP-2** 

Our proposed hyperheuristic-selection method is in fact a _reinforcement learning_ method and has been inspired from the concept of _association rules_ in the _business data mining_ world (Aguinis et al., 2012). 

In the following, we propose a hyperheuristic framework (based on the defin- 

**3.3 Solution algorithm** 

**105** 

ition of Burke et al. (2010)) that: 1) is a heuristic-selection type (as opposed to heuristic-generation type), 2) applies an online learning, and 3) is a hybrid construction-perturbation heuristic. 

The overall flow of algorithm is described in the following: First an initial solution is constructed using a constructive heuristic. Then through a learning process, the hyperheuristic proposes a series of perturbation, constructive and/or improvement heuristics in order to optimize the solution. 

In the CSA _p_ HLRP-1, The first heuristic, which is a constructive one, optionally exploits the Lagrangian dual (for the first problem) information to construct the initial (probably partial) solution. In the next step, such a solution can be partially destructed and reconstructed, perturbed and improved, directly improved or any other combination. A potential improvement made by a transition from the first constructive heuristic to another heuristic is measured. An acceptance criteria then decides on the transition from the current state to another state. 

Here, we use a simulated annealing move acceptance method, where the decision regarding the transition (move) to be accepted depends on the quality of solution obtained from applying heuristics (amount of improvement) and the elapsed CPU time. All improved moves are always accepted, and worsening moves might be accepted in accordance with the Metropolis criterion Kirkpatrick (1984): 



<!-- Start of picture text -->
exp( − ∆ f/T )  > R (0 ,  1) (3.62)<br><!-- End of picture text -->

**106 Capacitated Single Allocation p-Hub Location Routing Problem** 

where ∆ _f_ is the difference between the post-transition and pre-transition objective functions, _T_ is a _synthetic temperature_ and _R_ (0 _,_ 1) is a uniform random number between 0 and 1. _T_ represents the global temperature. When _T_ is larger, many non-improving or even deteriorating transitions (moves) are accepted while when it tends to zero exp( _−_ ∆ _f/T_ ) tends to zero, too. Therefore, for sufficiently small values of _T_ , only improvement moves are accepted. 

The algorithm starts with solving one or more (in parallel) Lagrangian relaxation(s) of the mathematical model (CSA _p_ HLRP-1-F2) using bundle algorithm (Frangioni, 1995). The outputs are in form of one (probably partially) feasible solution as well as _one_ set of the coefficients of variables in the objective function, per relaxation. 

In the CSA _p_ HLRP-2, the general scheme of the hyperheuristic has some similarity with the proposed hyperheuristic for CSA _p_ HLRP-1, expect it does not have any kind of information like results of Lagrangian Relaxation. In addition, the applied acceptance criteria is the so called Great Deluge. Great Deluge accepts solutions according to a dynamic threshold. We elaborate on further details in Chapter 1. 

#### **Low level heuristics** 

A rather large set of heuristics categorized in three classes, _constructive_ , _improvement_ , and _perturbation_ are used within our hyperheuristic framework. In the following we describe every heuristic, proposed for CSA _p_ HLRP-1, with sufficient details. 

**3.3 Solution algorithm** 

**107** 

_Constructive_ heuristics build a solution from the scratch, based on several predefined rules. In this study, two constructive algorithms are implemented _CS1_ and _CS2_ . 

_CS1_ that is detailed in Algorithm4, perform as in the following : it chooses _p_ hubs that have the highest flow transshipment. Then it allocates at least Γ nearest spokes to every hub (by partially respecting the capacity constraint as the volume of demand/supply arriving/departing at the hub for the spoke on route must not violate the capacity). Finally, it incrementally constructs each feeder route by sequencing the spokes allocated to a given hub taking into consideration the capacity constraint. 

The second constructive heuristic, _CS2_ , is distinguished from the first one, i.e. _CS1_ , in the way it chooses the set of _p_ hubs candidates. _CS2_ uses the information accumulated in the course of solving the third Lagrangian relaxation (LR3) (i.e. the coefficient of _zik_ in LR3 objective function) as well as some statistics collected about the frequency that a given node appeared as a hub during the iterations of bundle method and the history of hyperheuristic process, if any. It then allocates at least Γ spokes to each hub then allocate remainder spokes. To construct the spoke-level route and sequencing the hub and its allocated spokes along it, we start from the hub and add the arcs incrementally. Let _l_ be the last node already added to the partial spoke-level route and _SL_ be the set of remaining spokes to put on the route, unless _SL_ is a singleton, the next candidate spoke node, which we call it _R_  Nearest_ , to be added to the existing partial route is _i_<sup>_∗_</sup> = 

#### **108 Capacitated Single Allocation p-Hub Location Routing Problem** 

argmin _i∈SL{a_ 1 _tsl sc_ + _a_ 2 _rsl sc},_ 0 _≤ a_ 1 + _a_ 2 _≤_ 1 _, a_ 1 _, a_ 2 _≥_ 0. Where _tsl sc_ represents the travel time between the last spoke _sl_ in the cycle of the feeder network allocated to h and the candidate spoke _sc_ . _r_ ( _sl, sc_ ) corresponds to the _r_ coefficient between _sl_ and _sc_ resulted from LR3. As long as _a_ 2 increases, the influence of LR3 increases. 

**Algorithm 4** CS1 

1: **procedure** CONSTRUCTIVE1( _N_ ,p,Sigma) 2: Hubs = ChooseHubAccordingDemand() 3: getFeeders(Hubs) 4: **for** _i_ = 1 _, . . . , p_ ( _p_ = _|H |_ ) **do** 5: j=0 6: **while** j _<_ Sigma **do** 7: f= _R_Nearest_ (Hub[i],feeders,tabu) 8: temp TempTabu _←_ f 9: **if** CapacityConstraint(AssignFeederToHub(Hub[i],f)) **then** 10: AssignFeederToHub(Hub[i],f) 11: Tabu _← f_ 12: _j_ = _j_ + 1 13: **end if** 14: **end while** 15: TempTabu = Tabu 16: **end for** 17: TempTabu = Tabu 18: **for** _i_ = 1 _, . . . , p_ ( _p_ = _|H |_ ) **do** 19: j=0 20: **while** true **do** 21: f= _R_Nearest_ (Hub[i],feeders,tabu) 22: **if** f==Null **then** Break; 23: **end if** 24: TempTabu _←_ f 25: **if** CapacityConstraint(AssignFeederToHub(Hub[i],f)) **then** 26: AssignFeederToHub(Hub[i],f) 27: Tabu _←_ f 28: _j_ = _j_ + 1 29: **end if** 30: **end while** 31: TempTabu = Tabu 32: **end forreturn** Hubs 33: **end procedure** 

**3.3 Solution algorithm** 

**109** 

_Improvement_ heuristics start from a complete solution and apply some moves in order to improve the objective function value. In our study, different _improvement_ heuristics are proposed: 

- IMP 1) In _Rotate_ , given a route (a hub and a sequence of spokes along the route), it rotates (clock-wise or counter clock-wise) the string. Such rotation of size _k_ will designate the _k_ -th spoke node after the current hub as a hub and renders the current hub as a spoke. This heuristic is useful when the order of nodes on the route is rather correct but the choice of hub is the cause of infeasibility or sub-optimality. 

- IMP 2) _Re-order_ tries to re-sequence the nodes (hub and spokes) in order to find a better order of nodes along the route. While re-ordering, a sequence of _{H, S_ 1 _, S_ 2 _, . . . , Sm}_ may turn to _{S_ 3 _, S_ 1 _, H, Sm, . . . , S_ 2 _}_ wherein _S_ 3 becomes a hub and _H_ turns to a spoke node. This heuristic takes into the capacity on the route and the total volume of demand and supply of nodes such that by some intelligent re-sequencings, either a feasible solution is obtained or an already feasible solution is improved. 

- IMP 3) _Re-allocate_ tries to remove an allocated port from a feeder network that has the maximum number of feeder nodes, and inserts it to another feeder network. This node can be a hub or spoke in its original route and can be equivalently hub or spoke in the devotional route. If it becomes hub at the destination then the hub at the destination turns to spoke on the route. Normally, such nodes can be the one in an _irreducible subset_ of 

#### **110 Capacitated Single Allocation p-Hub Location Routing Problem** 

the nodes on the route that are the cause of infeasibility or the nodes that are far from each other but lie on the same spoke-level arc (imposing high transportation time). 

- IMP 4) _SW1ffImp_ randomly swaps two allocated ports from two different feeder networks, if and only if the solution improves the incumbent. This heuristic can be seen as a kind of search that tries to diversify and sample from different parts of the search space. 

- IMP 5) _SW2ffImp_ randomly swaps tree ports belonging to three different feeder networks, if and only if the solution improves over the incumbent. 

_Perturbation_ heuristics start with a complete solution and do some changes in order to inject some diversification. In our study, we implement different perturbation heuristics in a manner of all changes will be in the solution must respect that to connect a pair of spokes _i_ and _j_ , they should have _r_ ( _j, j_ ) less than a defined threshold _TH_ : 

- PRT 1) _SW1ff_ , The search tries to randomly swap two spokes allocated to the two different hubs In the end, it either returns the feasible solution with the maximum Hamming distance (with respect to the binary design variables) from the input solution or one of the solutions among the _p_ farthest ones. 

- PRT 2) _SW2ff_ , tries to randomly swap three spokes belonging to three different routes. It follows the same principle as in _SW1ff_ , except that a very limited number ( _n_<sup>2</sup> _< |.| ≪ n_<sup>3</sup> ) of samples are examined as a complete 3-opt is very expensive, 

**3.3 Solution algorithm** 

**111** 

- PRT 3) _SW1hf_ , swaps a random feeder and its corresponding hub. The hub becomes a spoke and the spokes turns to a hub. 

- PRT 4) _SW2hf_ a fast local search that swaps a random feeder and a random hub which should not be its corresponding hub. 

- PRT 5) _SWhh_ , a fast local search swapping two hubs. This can be done by taking into account the supply/demand of the entering hub that can violate the capacity (if we seek generating feasible solutions from perturbation). 

- PRT 6) _Insert/Delete_ , removes an allocated spoke from a route, and inserts it to another one either with respect to the residual capacity available on another route or even randomly . 

It must be emphasized that the _perturbation_ heuristics aim at introducing some diversifications. Therefore, we do not expect a perturbed solution be a feasible one. Rather, we hope that it can help exploring unvisited regions in the solution space. 

For the CSA _p_ HLRP-2, most of the components proposed (such as low-levelheuristics etc.) for CSA _p_ HLRP-1, are adapted for this problem. The main modification are: 

1. The concept of edges is converted to arc in the feeder networks. 

2. The problem has constraint capacity on the vertices rather than on the flow. 

3. Add a check on the number of spokes allocated to each hub specially in _CS1_ , _Insert/Delete_ and _Re-allocate_ . 

**112 Capacitated Single Allocation p-Hub Location Routing Problem** 

4. LR3 results does not intervene in the process of _CS2_ . 

#### **Heuristic Selection Methods** 

As mentioned in chapter 1, several heuristic-selection methods are introduced in the literature. In this study, we work with reinforcement learning mechanism in order to select the corresponding heuristic to be applied during the hyperheuristic process. 

Proposed Learning for the CSA _p_ HLRP-1 

Here, learning mechanism, which is presented in Algorithm 5, is inspired from a data mining technique called Association Rules (AR) guided by a Tabu Search (TS). When looking at the principles of AR, one can observe that AR is actually a kind of reinforcement learning that helps in respecting the dependency order of heuristic applications. The AR was first introduced by Agrawal et al. (1993) and is a technique in data mining that has attracted a lot of attention from the researchers and practitioners. Extracting interesting correlation, frequent patterns, associations or casual structures from group of items in the transaction databases or data repositories are the purpose of association rules technique. The technique of association rules finds interesting relationships among large set of data items. It shows attribute value conditions that occur frequently together in a given dataset. Traditionally, AR has been widely-used in Market Basket Analysis (Aguinis et al., 2012) in order to find how items purchased by customers are related . In association analysis, there are two sets of items (called _itemsets_ ): 1) the _antecedent_ (the if part), and 2) the _consequent_ (the then part). Moreover, an association rule has 

**3.3 Solution algorithm** 

**113** 

two more values that express the degree of uncertainty about the rule. The first value is called the _support_ for the rule. The support is defined as the proportion of task-relevant data transactions for which the pattern is true. The second one is known as the _confidence_ of the rule. The so called confidence is a measure of _certainty_ or _trustworthiness_ associated with each discovered pattern. Here, our goal is to find some relationships between the different implemented heuristics, in order to find the best series of heuristics to be applied. The numerical reward is not going to be assigned to a single heuristic but to a series of them. Association Rules heuristic selection method deals with two main variables: _support_ and _confidence_ . These variables are used to measure the performance of a series of heuristics. If a heuristic does not have the required support at a certain time, or if it does not have enough confidence, the Tabu Search metaheuristic method prevents it from being selected. The relevant variables and parameters are explained in the following: 

1. A heuristic series ( _Hm, . . . , Hn_ ) weight (reward) is equal to the negative summation (for minimization case) of the objective function value divided by the number of the application of this heuristic. 

2. A support of a suggested _Hs_ is equal to the summation of the heuristic series ( _H_ 1 _, . . . , Hs_ ) reward in the precedent transactions divided by the summation of all heuristic series rewards. 

3. The confidence of a suggested _Hs_ in such series ( _Hm, . . . , Hn_ ) is equal to the support of _Hs_ divided by the support item set ( _Hm, . . . , Hn_ ). 

_Tabu list Tl_ : Given our time limit, we initially set _Tl_ = _∅_ and at each iteration, _Tl_ is 

**114 Capacitated Single Allocation p-Hub Location Routing Problem** 

updated as follows: if the elapsed CPU time is less than a certain milestone (e.g. the the time limit divided by a given number _v_ 1), heuristics are chosen randomly in order to establish a historical heuristic series performance. Otherwise, if the elapsed CPU time is greater than the milestone _/v_ 1, _Tl_ will contain all heuristics for each series expect those for which the support value is greater than a threshold _thS_ . In the case that the elapsed time is greater than the milestone _/v_ 2, _Tl_ will contain all heuristics for each series expect those for which the confidence value is greater than a threshold _thC_ . It must be noted that the tabu list is updated with changes of quality of each heuristic series, i.e. calculation of _WHS_ . 

**Algorithm 5** Association Rules Heuristic Selection Method **procedure** CHOOSEHEURISTIC( _Elapsed_  Time_ ) **if** ( _ElapsedT ime_ < V1) **then** Return Random(NbOfHeuristic) **end if if** ( _Elapsed_  Time_ > V1) **then while** TRUE **do** Suggested_Heuristic_ID = Random(Nb_Of_Heuristic) S = Support(Suggested_Heuristic_ID) **if** (S > S_Threshold) **then** Return Suggested_Heuristic_ID **end if end while end if if** ( _Elapsed_  Time_ > V2) **then while** TRUE **do** Suggested_Heuristic_ID = Random(Nb_Of_Heuristic) C = Confidence(Suggested_Heuristic_ID) **if** (C > C_Threshold) **then** Return Suggested_Heuristic_ID **end if end while end if end procedure** 

**3.3 Solution algorithm** 

**115** 

Proposed Learning for the CSA _p_ HLRP-2 

From among several methods for solving the reinforcement learning problem, _temporal-difference_ methods serve our purpose the best as they do not require a complete description of the environment and are fully incremental. 

The well-known Q-learning algorithm Watkins (1989) which falls within this category uses the following update formula: 



<!-- Start of picture text -->
Qt +1( st, at ) =  Qt ( st, at ) + αt ( st, at )<br>� �� � � �� �<br>old value learning rate<br><!-- End of picture text -->



<!-- Start of picture text -->
learned value<br>� �� � <br>· reward R ��� t +1� + discount���� γ factor max� a Qt �(� st +1 , a �) − Q � old t ( s �value t � , at �)<br> estimate of optimal future value <br><!-- End of picture text -->

where _Rt_ +1 is the reward collected after taking action _at_ in state _st_ , _αt_ ( _s, a_ )(0 _< α ≤_ 1) is the learning factor (may be the same for all pairs) and _γ ≥_ 1. wherein _s_ is the current state, _a_ is the action taken in the state _s_ , _r_ is the immediate reward received for executing action _a_ in state _s_ , _s_<sup>_′_</sup> is the new state, _γ ≥_ 1, and 0 _< αq <_ 1 is the learning factor. 

In a choice scheme as _ϵ − greedy_ (see Watkins and Dayan (1992) for explanations and the proof of convergence), an agent will select the action resulting in the highest reward _Q_ with probability 1 _− ϵ_ and a random action with probability _ϵ_ . The _learning rate_ determines how the newly information will replace the old information. Two extreme cases are ’0’ in which the agent will not learn anything 

**116 Capacitated Single Allocation p-Hub Location Routing Problem** 

and ’1’ in which the agent takes into account only the most recent information. Here we use _αt_ ( _s, a_ ) = 0 _._ 1 _∀t_ . 

A discount factor _γ_ close to 0 will make the agent short-sighted by only considering current rewards, while a factor approaching 1 will make it strive for a long-term high reward. 

A higher initial condition will encourage further exploration in any case of action update rule will cause it to have lower values than the other alternative and increases the probability of being chosen. 

The process of Q-learning algorithm is shown in Algorithm 6. 

**Algorithm 6** <u>Q-Learning Controller Algorithm</u> 

Inputs(set of state S, set of actions A, _γ_ the discount factor, _α_ the step size) Inputs(real array Q[S,A], previous state s, previous action a) 

#### **repeat** 

Select and Carry out an action a Calculate reward r get state s’ _Q_ [ _s, a_ ] _← Q_ [ _s, a_ ] + _α_ ( _r_ + _γmaxa′Q_ [ _s_<sup>_′_</sup> _, a_<sup>_′_</sup> ] _− Q_ [ _s, a_ ]) s _←_ s’ 

**until** Termination 

Q-learning based hyperheuristic was applied by Falcao et al. (2015), in a problem of scheduling. Results proof that using Q-learning improve siginificantly the solution quality compared by solutions got from no-learning hyperheuristic. Q-LA is used in secondary control to calculate microgrid regulation error (MRE), which is the regulated power, for real time operation. Economy and environmental benefits are so necessary in real time modification process of the generation sched- 

**3.4 Computational experiments** 

**117** 

ule of distributed generators (DGs) like batteries with the MRE by the fuzzy theory and particle swarm optimization method Xi et al. (2015). Q-learning is applied in Boyan and Littman (1994) to packet routing, where it is able to discovering efficiently different routing policies in a dynamic change of network with no information needed about the network topology, traffic patterns and etc. A modified version of Q-learning was proposed to plan pathes for mobile robots because it must be able to autonomous complete various intelligent tasks Gao et al. (2008). For interested researchers, Dorigo and Gambardella (2014), Ho et al. (2006), Choi and Yeung (1996) and Gaskett et al. (1999) are among good examples of work considering this reinforcement learning method. 

## **3.4 Computational experiments** 

We have generated our instances based on the the well-known Australian Post (AP) dataset, for CSA _p_ HLRP-1. The transhipment times are generated randomly for some real values within [2, 5] for the given time unit. The existing capacities of the original data (see Ernst and Krishnamoorthy (1999)) are not used because they do not always results in feasible solutions as the problem structures are different. In CSA _p_ HLRP-2, the data sets was Civil Aeronautics Board (CAB), which is proposed by O’kelly (1987), and based on airline passenger flow among 25 important cities in the US (in addition to AP data set). CAB and AP nodes distributions shown respectively in Figure 3.3 and Figure 3.4. 

All experiments were performed on an Intel 2.54 GHz core i5 CPU and 4 Gb of 

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**118** 



**Figure 3.3:** Civil Aeronautics Board data with 25 nodes. 

memory running on Windows 7. 

The termination criteria are chosen in such a way to avoid useless computation as well as premature convergence. The proposed termination criterion, sets a global time limit _Tlimit_ = max _{_ 6000 _, n_<sup>2</sup> _× p ×_ 250 _}_ m.s. for the overall computation. In addition, we set a second termination criterion for terminating the whole algorithm once 10 _× n × p_ non-improving iterations have been observed. 

### **3.4.1 CSA** _p_ **HLRP-1 Computational experiments** 

We assume that our fleet of vehicles is homogenous and therefore with a unique capacity size. Let O _i_ =<sup>�</sup> _j_<sup>_Wij_and D</sup><sup>_j_= �</sup> _j_<sup>_Wij_and let</sup><sup>_p_is the number of hubs.</sup> <u>�</u> _<u>i</u>_<sup>_Oi_+�</sup> _<u>i</u>_<sup>_Di_</sup> The capacity is generated as _C_ = . _p_ 

All instances are named in a format _ni_  pj_  k_ where _i_ indicates the number of nodes, _j_ indicates the number of hubs and _k_ indicates the factor of economies of scale. 

**3.4 Computational experiments** 

**119** 



**Figure 3.4:** Australia post data with 200 nodes. 

While a fair comparison between a heuristic algorithm and an exact decomposition is rather non-trivial, in Table 3.6, we report the results of our computational experiments with hyperheuristic (HH), with and without using results of LR, next to the results of Bender decomposition from Gelareh et al. (2015). There are, in total, 24 instances ranging from 10 nodes with 3 hubs to 20 nodes with 6 hubs. The first column reports the instance name, the second(resp. seventh) one indicates the computational times of Bender Decomposition method (resp. HH.). 

The best solution found by HH without LR (resp. Bender Decomposition) are reported in the fifth (resp. third). The fourth column reports the Cplex status when apply Bender decomposition method. The gap between HH without LR results (resp. LR HH) and Benders Decompositions are reported in the seventh (resp. ten). The last column indicates the gap between the best objective function value taken by HH with and without using LR results. 

**120 Capacitated Single Allocation p-Hub Location Routing Problem** 

One observes that the relative gaps between the solution reported by Benders decomposition and those of HH never exceeded 0 _._ 08% if HH use LR results, otherwise it does not exceed 0 _._ 32%. In this table, the negative gaps indicate that such HH solutions are better than the feasible solution obtained by applying the Benders decomposition method in Gelareh et al. (2015). When compared with the computational time elapsed to obtain such high quality solutions, it is confirmed that the proposed HH framework is capable of obtaining high quality solutions in very reasonable computational times, specially within LR results. 

The gap between HH with and without LR results reaches 3 _._ 92%, proves the additional value of using the LR variable coefficient into the process of HH. LR variable coefficient shown in the objective function of LR3, appears very well during the process of HH. In construction phases (resp. in perturbation phase), all routes between any pairs have the coefficient greater than a number _ι_ (resp. _ν_ ) are excluded. Furthermore, during the improvement phases pairs with small coefficients are favored to be connected. 

**3.4 Computational experiments** 

**121** 

||Gap(% between HHs)<br>0.00<br>0.00<br>0.00<br>0.00|2.37<br>0.00<br>3.92<br>0.00<br>0.00<br>0.24<br>0.00|0.00|0.00<br>0.00|0.00|0.00<br>0.00<br>0.00<br>0.00<br>0.67|0.00<br>0.00<br>0.38|1.56|
|---|---|---|---|---|---|---|---|---|
|e|Gap(%)with BD<br>0.00<br>0.00<br>0.00<br>-1.18|-2.99<br>-7.90<br>-30.31<br>-27.66<br>-1.32<br>0.08<br>-3.20|0.00|-6.13<br>-|-6.94|-<br>-21.49<br>0.00<br>0.00<br>-8.42|0.00<br>-9.31<br>-17.19|-17.81|
|rs decompositions and th<br>thout LR|HH with LR<br>Obj. Val.<br>HH Ex.Time(sec.)<br>3235.99<br>3.11<br>3315.81<br>5.01<br>3395.63<br>5.01<br>10990.48<br>4.10|10929.41<br>6.10<br>10421.16<br>5.11<br>8198.31<br>6.08<br>7966.52<br>4.10<br>8949.29<br>6.11<br>6905.00<br>5.10<br>6921.75<br>4.19|7387.35<br>5.00|23380.95<br>5.09<br>22411.66225<br>5.10|23316.54777<br>5.11|19382.47479<br>7.99<br>17519.51325<br>7.00<br>21585.40<br>7.01<br>16933.63<br>8.21<br>16256.34<br>8.07|17441.26<br>8.24<br>14397.56<br>11.13<br>14440.86<br>9.06|14662.78<br>11.19|
|etween bende<br>ic with and wi|LR<br>Gap(%)with BD<br>0.00<br>0.00<br>0.00<br>-1.18|-0.54<br>-7.90<br>-25.21<br>-27.66<br>-1.32<br>0.32<br>-3.20|0.00|-6.13<br>-|-6.94|-<br>-21.49<br>0.00<br>0.00<br>-7.69|0.00<br>-9.31<br>-16.74|-15.98|
|omparison of the quality b<br>proposed hyperheurist|Hypeheuristic without<br>Obj. Val.<br>HH Ex. Time(sec.)<br>3235.99<br>4.075<br>3315.81<br>6.127<br>3395.63<br>6.064<br>10990.48296<br>5.003|11194.96<br>6.109<br>10421.16<br>6.058<br>8532.44<br>6.06<br>7966.52<br>5.076<br>8949.29<br>6.089<br>6921.75<br>6.068<br>6921.75<br>5.064|7387.35<br>5.028|23380.95<br>6.06<br>22411.66225<br>6.044|23316.54777<br>6.045|19382.47479<br>8.11<br>17519.51325<br>7.077<br>21585.4<br>8.129<br>16933.63<br>9.26<br>16365.60<br>10.076|17441.26<br>10.146<br>14397.56<br>12.145<br>14495.69<br>11.233|14894.40<br>12.252|
|**ble 3.6:** C|io<br>CplexStatus<br>OptimalTol<br>Optimal<br>Optimal<br>OptimalTol|OptimalTol<br>OptimalTol<br>OptimalTol<br>OptimalTol<br>OptimalTol<br>Optimal<br>Optimal|Optimal|OptimalTol<br>failed|OptimalTol|failed<br>OptimalTol<br>Optimal<br>Optimal<br>OptimalTol|Optimal<br>OptimalTol<br>AbortUser|AbortUser|
|**Ta**|der Decomposit<br>Obj. Val.<br>3235.99<br>3315.81<br>3395.63<br>11120.2|11255.74<br>11244.2<br>10683.44<br>10170.06<br>9067.25<br>6899.27<br>7143.31|7387.35|24814.09<br>-|24935.81|â˘AˇT<br>21284.45<br>21585.4<br>16933.63<br>17624.7|17441.26<br>15738.56<br>16922.59|17274.12|
||Ben<br>Ex. Time(sec.)<br>17<br>14<br>14<br>929|1395<br>398<br>1073<br>883<br>899<br>626<br>591|1615|15307<br>-|28673|â˘AˇT<br>14432<br>15767<br>6470<br>19572|19051<br>27531<br>46695|98991|
||instance<br>n10_q3_0.7<br>n10_q3_0.8<br>n10_q3_0.9<br>n15_q3_0.7|n15_q3_0.8<br>n15_q3_0.9<br>n15_q4_0.7<br>n15_q4_0.8<br>n15_q4_0.9<br>n15_q5_0.7<br>n15_q5_0.8|n15_q5_0.9|n20_q3_0.7<br>n20_q3_0.8|n20_q3_0.9|n20_q4_0.7<br>n20_q4_0.8<br>n20_q4_0.9<br>n20_q5_0.7<br>n20_q5_0.8|n20_q5_0.9<br>n20_q6_0.7<br>n20_q6_0.8|n20_q6_0.9|



**122 Capacitated Single Allocation p-Hub Location Routing Problem** 

Table 3.7 reports the total number of iterations every heuristic has worked on each instance. Rotate improvement heuristic has worked the most in all instances. Next, it comes to the constructive heuristics CS1 and CS2 which have more or less similar number of iterations for many instances. This may indicate that the information collected in the course of Lagrangian optimization in LR3, the statistics collected during HH process, and the construction by taking into account demand (i.e. CS1) when choosing the hubs, have some similarities. Among the perturbation heuristics SW2hf contributes in the most number of iterations. 

**3.4 Computational experiments** 

**123** 

**Table 3.7:** Number of each heuristic in each instance was applied. 

|instance|Insert/Delete|Re-Allocate|Re-order|Rotate|SW1ffImp|SW2ffImp|SW2hf|SW1ff|SW2ff|CS1|CS2|SWhh|SW1hf|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|n10_q3_0.7|3605|3568|3613|14331|3550|3641|3621|3570|3491|3542|3542|3553|3572|
|n10_q3_0.8|3864|3899|3900|15481|3861|3794|3898|3815|3846|3731|3769|3884|3843|
|n10_q3_0.9|3770|3895|3853|15165|3856|3786|3897|3796|3706|3821|3751|3868|3838|
|n15_q3_0.7|2513|2520|2458|9969|2470|2533|2533|2461|2427|2490|2464|2481|2500|
|n15_q3_0.8|2471|2534|2437|9938|2505|2551|2497|2458|2421|2443|2460|2501|2439|
|n15_q3_0.9|2466|2515|2482|9876|2394|2561|2483|2467|2436|2428|2437|2427|2461|
|n15_q4_0.7|2571|2519|2532|10129|2549|2621|2518|2469|2490|2494|2522|2550|2528|
|n15_q4_0.8|2381|2388|2348|9263|2348|2423|2412|2287|2252|2328|2334|2341|2296|
|n15_q4_0.9|2451|2509|2427|9824|2474|2529|2502|2391|2426|2483|2422|2454|2472|
|n15_q5_0.7|2561|2577|2562|10079|2511|2518|2554|2463|2474|2511|2561|2591|2491|
|n15_q5_0.8|2468|2418|2495|9898|2485|2576|2495|2401|2459|2467|2460|2494|2427|
|n15_q5_0.9|2483|2479|2469|9917|2514|2579|2478|2407|2449|2405|2442|2505|2443|
|n20_q3_0.7|1055|1072|1021|4148|1056|1058|1108|1013|1021|1046|1058|1036|1011|
|n20_q3_0.8|1195|1127|1105|4582|1160|1235|1181|1087|1115|1177|1179|1198|1093|
|n20_q3_0.9|1164|1124|1112|4602|1181|1194|1161|1126|1133|1118|1152|1158|1122|
|n20_q4_0.7|1642|1603|1601|6323|1612|1690|1682|1532|1569|1642|1625|1610|1605|
|n20_q4_0.8|1584|1601|1515|6242|1516|1578|1612|1530|1553|1602|1542|1531|1547|
|n20_q4_0.9|1672|1614|1581|6444|1500|1624|1693|1552|1578|1608|1587|1637|1554|
|n20_q5_0.7|1973|1956|1931|7716|1923|2041|1933|1884|1854|1939|1936|1978|1956|
|n20_q5_0.8|1974|1951|1926|7638|1902|2034|1962|1861|1831|1926|1934|1944|1968|
|n20_q5_0.9|1928|1973|1995|7687|1889|1951|1914|1928|1882|1892|1942|1942|1881|
|n20_q6_0.7|2211|2226|2233|8769|2193|2253|2214|2161|2115|2139|2181|2241|2123|
|n20_q6_0.8|2187|2156|2152|8650|2155|2241|2225|2154|2104|2162|2164|2189|2136|
|n20_q6_0.9|2156|2159|2172|8707|2148|2196|2172|2137|2147|2184|2123|2157|2067|



We have applied the proposed HH framework on a wider ranger of problem instance sizes. Table 3.9 reports the statistics of applying the proposed HH on a tested composed of instances of up to 100 nodes. 

In Table Table 3.8, initials objective functions of the HH with and without LR results are reported. In general initial objective function using LR results is better than without LR results. The average relative gap between the initial and the best found objective function value for instances of table without using LR results is 21 _._ 45% (resp. 19 _._ 36% using LR results) while this becomes 26 _._ 66% for the instances between greater than 20 nodes Table 3.9. This on one hand is due to a much larger solution space in larger instances which in turn increases the probability of finding better solutions during the search and on the other hand, may show that the HH is capable of benefiting from such a much larger search space to better improve the initial solutions. Another pessimistic view might question the performance of 

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**124** 

**Table 3.8:** Comparison of the quality between the initial objective function taken by the proposed hyperheuristic with and without LR 

|instance|HH Initial Obj. Val.|LR Initial Obj. Val|Gap|
|---|---|---|---|
|n10_q3_0.7|4113.93|4113.93|0.00|
|n10_q3_0.8|3732.68|3732.68|0.00|
|n10_q3_0.9|4281.89|4281.89|0.00|
|n15_q3_0.7|11967.42|11967.42|0.00|
|n15_q3_0.8|14148.48|12075.56|14.66|
|n15_q3_0.9|14267.24|14267.24|0.00|
|n15_q4_0.7|12287.22|11194.78|8.89|
|n15_q4_0.8|12460.91|11373.32|8.73|
|n15_q4_0.9|11551.86|11551.86|0.00|
|n15_q5_0.7|7942.10|7942.10|0.00|
|n15_q5_0.8|9341.05|8160.33|12.64|
|n15_q5_0.9|7583.26|7583.26|0.00|
|n20_q3_0.7|30247.17|30093.41|0.51|
|n20_q3_0.8|28804.76|28804.76|0.00|
|n20_q3_0.9|29559.33|29559.33|0.00|
|n20_q4_0.7|28564.87|26512.51|7.18|
|n20_q4_0.8|29230.58|23481.05|19.67|
|n20_q4_0.9|24569.19|24569.19|0.00|
|n20_q5_0.7|22584.80|22584.80|0.00|
|n20_q5_0.8|24364.62|24364.62|0.00|
|n20_q5_0.9|21354.40|21354.40|0.00|
|n20_q6_0.7|15949.97|15949.97|0.00|
|n20_q6_0.8|17950.91|17950.91|0.00|
|n20_q6_0.9|18522.41|18522.41|0.00|



construction heuristics and quality of initial solution constructed by them. In order to ensure the quality of the solution, we reserve only information about the allocation resulted from LR HH and ignore all spokes routes information. The problem has some similarities with the picked-up delivery vehicle routing problem with multiple depots. Each hub is considered as depot, and the objective is to construct a feeder network for each hub from its allocated spokes. We inject all allocation information into solver, which find feeders network. All constraints related to the number of hubs and allocations was ignored. This process, which use some data resulted from a heuristic approach and complete the solution using a solver is referred to as _Matheuristic_ chapter 1. 

Results of matheuristic are reported in Table 3.10, within the gap with the LR HH objective function, and the execution time. All instances for which we 

**3.4 Computational experiments** 

**125** 

**Table 3.9:** HH results for large instances of pHub location problem. 

|instance|HH Initial Obj. Val.|HH Obj. Val.|HH Execution Time(sec.)|
|---|---|---|---|
|n30_p3_0.7|105144.53|75757.20|21.08|
|n30_p3_0.8|114888.19|76278.81|21.05|
|n30_p3_0.9|104911.22|72447.12|21.02|
|n30_p5_0.7|69112.47|53366.71|35.09|
|n30_p5_0.8|78602.46|54171.46|35.03|
|n30_p5_0.9|73163.24|54901.29|35.03|
|n40_p3_0.7|202842.00|164427.72|31.63|
|n40_p3_0.8|212202.17|170884.40|31.54|
|n40_p3_0.9|206603.16|178590.38|31.53|
|n40_p5_0.8|184960.11|132972.45|52.58|
|n40_p5_0.9|189692.00|117903.04|52.54|
|n40_p6_0.7|140120.51|106682.03|63.13|
|n50_p3_0.7|370022.47|283335.66|36.09|
|n50_p3_0.8|357808.84|290623.44|36.12|
|n50_p3_0.9|374514.09|225264.35|36.19|
|n50_p5_0.7|291375.19|208124.35|60.10|
|n50_p5_0.8|287717.05|208912.96|60.50|
|n50_p5_0.9|288860.51|232705.22|60.09|
|n70_p3_0.7|808406.46|638821.53|51.28|
|n70_p3_0.8|805167.64|617315.20|51.07|
|n70_p3_0.9|880752.26|617315.20|51.14|
|n70_p5_0.7|789712.18|484787.83|85.14|
|n70_p5_0.8|693946.36|542097.71|85.14|
|n70_p5_0.9|717687.40|551465.33|85.16|
|n80_p3_0.7|1129687.50|905846.24|61.64|
|n80_p3_0.8|1128080.39|919430.31|61.74|
|n80_p3_0.9|1172538.60|853701.87|61.73|
|n80_p5_0.7|902766.77|676355.62|102.69|
|n80_p5_0.8|908105.30|713127.24|102.84|
|n80_p5_0.9|949987.94|723792.60|102.77|
|n90_p3_0.7|1430318.33|1265909.60|66.10|
|n90_p3_0.8|1594559.93|1186128.92|66.29|
|n90_p3_0.9|1407958.75|1166788.83|66.38|
|n90_p5_0.7|1085625.40|959702.73|110.30|
|n90_p5_0.8|1288459.47|971146.25|110.34|
|n90_p5_0.9|1126831.55|988784.52|110.15|
|n100_p3_0.7|1679715.79|1484907.58|76.69|
|n100_p3_0.8|1692753.82|1491646.31|76.96|
|n100_p3_0.9|2061323.94|1512299.50|76.88|
|n100_p5_0.7|1839058.26|1251859.24|127.96|
|n100_p5_0.8|1499370.20|1291282.92|127.77|
|n100_p5_0.9|1450410.23|1275010.77|127.75|
|n100_p10_0.7|1095903.40|980333.22|255.55|
|n100_p10_0.8|1185961.32|967479.92|255.37|
|n100_p10_0.9|1143466.25|952694.14|255.30|



do not have BD optimal solution or that have negative gap between HH and BD objective function were tested, in addition to some medium size instances. The gap reaches 2 _._ 66% in instance n20_p5_0.8, in addition it finds optimal solution for given allocations to some instances such as n15_p3_0.7, n15_q3_0.8, n15_q3_0.9, etc. The added value of _matheuristic_ , which appears in instances less than 20 nodes, does not appear much pertinent in the medium instances within time limit of 1 hour. Table 3.10 report these results and showing the quality gained, while the 

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**126** 

negative gaps proves the deteriorated quality by _matheuristic_ . 

**Table 3.10:** A comparison between results of Matheuristic with that of LR HH. 

|instance|Status|Matheuristi<br>Time|c<br>OF|LR HH Obj. val.|GAP(%)LR HH and Math.|
|---|---|---|---|---|---|
|n10_q3_0.7|Optimal|0.30|3235.991|3235.99|0.00|
|n15_q3_0.7|Optimal|13.82|10990.48|10990.48|0.00|
|n15_q3_0.8|Optimal|40.30|10902.53|10929.41|0.25|
|n15_q3_0.9|Optimal|16.97|10276.65|10421.16|1.39|
|n15_q4_0.7|Optimal|1.76|8198.31|8198.31|0.00|
|n15_q4_0.8|Optimal|11.56|7966.52|7966.52|0.00|
|n15_q4_0.9|Optimal|2.00|8945.09|8949.29|0.05|
|n20_q3_0.7|Feasible|3605.57|23213.17|23380.95|0.72|
|n20_q3_0.8|Feasible|3605.70|22411.66|22411.66|0.00|
|n20_q3_0.9|Feasible|3605.73|23316.55|23316.55|0.00|
|n20_q4_0.7|Optimal|3675.79|19382.47|19382.47|0.00|
|n20_q4_0.8|Optimal|484.40|17519.51|17519.51|0.00|
|n20_q5_0.8|Optimal|7304.80|15824.26|16256.34|2.66|
|n20_q6_0.7|Optimal|12.45|14397.56|14397.56|0.00|
|n20_q6_0.8|Optimal|26.89|14321.04|14440.86|0.83|
|n20_q6_0.9|Optimal|33.88|14662.78|14662.78|0.00|
|n30_p3_0.7|Feasible|3672.64|80871.04|75757.20|-6.75|
|n30_p3_0.8|Feasible|4118.88|81845.67|76278.82|-7.30|
|n30_p3_0.9|Feasible|7756.06|78998.28|73284.34|-7.80|
|n40_p3_0.7|Feasible|3770.47|292132.10|164427.72|-77.67|
|n40_p3_0.8|Feasible|3787.60|352933.80|170884.40|-106.53|
|n40_p3_0.9|Feasible|3796.32|316753.50|178590.38|-77.36|



In Table 3.11, we report results of applying iterative method for solving the five variants of Lagrangian relaxation methods proposed in subsection 3.3.1. The different relaxations were solved by using bundle. The bundle method is known for its higher precision and faster convergence compared to the simpler versions of subgradient method. We have initialized the Lagrangean multipliers with the corresponding dual values of the LP relaxation, wherever possible. 

In Table 3.11, for every relaxation we have reported the CPU time as well as the best bound obtained for the given amount of CPU time. For some relaxations (for example LR2) the computational time for the very small instances was several order of magnitude higher than other relaxations and the bound quality was not really dominating. Therefore, we have not gone further with the larger instances as the run times were increasing exponentially. From among all five relaxations, only 

**3.4 Computational experiments** 

**127** 

LR3 was able to converge for the problem until size of 20 nodes in reasonable times. Furthermore, LR3 offers bests bounds among other relaxations. LR1 was able to solve problem up to 15 nodes and 4 hubs but for 15 nodes and 5 hubs, it could just terminated in reasonable time for _α_ = 0 _._ 9 from among other values. As mentioned earlier, LR2 is the most expensive relaxation in terms of computational time as it was able to solve instances of 10 nodes with 3 hubs in reasonable time. LR4 and LR5 appear effective in terms of computational time only until instances with 15 nodes and 5 hubs. When doing iterations of bundle algorithm, the subproblem was solved using CPLEX 12.6.2, the time limit was set to 3600 seconds and the number of iterations was set to 100. 

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**128** 



<!-- Start of picture text -->
Table 3.11: Lagrangian relaxation results.<br><!-- End of picture text -->



<!-- Start of picture text -->
100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100<br>nbIterations<br>BestLB 2049.61 2066.57 2032.45 5312.45 5380.57 5293.16 5038.77 5071.04 4957.92 4787.32 4738.18 4648.12 — — — — — — — — — — — —<br>LR5<br>Time ()sec. 25.419 24.662 23.965 113.771 114.311 113.224 114.761 114.53 116.671 115.739 112.559 113.274 — — — — — — — — — — — —<br>BestLB 2123.11 2088.45 2031.92 5352.14 5275.19 5152.99 4983.24 5026.48 4916.29 4881.33 4854.58 4687.78 — — — — — — — — — — — —<br>LR4<br>Time ()sec. 23.317 22.153 21.091 118.179 107.336 105.078 103.942 112.094 108.545 104.984 104.874 105.495 — — — — — — — — — — — —<br>BestLB 2384.16 2319.98 2239.29 5785.28 5732.76 5580.06 5593.87 5418.13 5253.88 5332.59 5134.72 4992.37 10239.6 10066.4 10014.9 9933.42 9636.57 9426.4 9586.66 9389.53 9188.13 9366.45 8991.41 8652.79<br>LR3<br>Time ()sec. 228.177 231.55 219.116 1665.9 1704.89 1744.7 1901.39 2020.9 1937.78 2164.69 2246.72 2185.9 10818 10693 10240 12879 13407 12408 22194 19660 15495 33290 23062 17112<br>BestLB 2325.97 2228.71 2133.36 — — — — — — — — — — — — — — — — — — — — —<br>LR2<br>Time ()sec. 1987.52 1806.25 1537.42 — — — — — — — — — — — — — — — — — — — — —<br>BestLB 2068.61 2020.86 1956.84 5253.67 5089.8 4969.5 4975.18 4842.1 4688.62 4770.47 — — — — — — — — — — — — — —<br>LR1<br>Time ()sec. 231.69 195.81 182.26 993.1 947.26 1009.9 2467.3 2027.5 2431.2 51424 — — — — — — — — — — — — — —<br>instance n10 p3 0.9 n10 p3 0.8 n10 p3 0.7 n15 p3 0.9 n15 p3 0.8 n15 p3 0.7 n15 p4 0.9 n15 p4 0.8 n15 p4 0.7 n15 p5 0.9 n15 p5 0.8 n15 p5 0.7 n20 p3 0.9 n20 p3 0.8 n20 p3 0.7 n20 p4 0.9 n20 p4 0.8 n20 p4 0.7 n20 p5 0.9 n20 p5 0.8 n20 p5 0.7 n20 p6 0.9 n20 p6 0.8 6 0.7n20 p<br><!-- End of picture text -->

**3.5 Conclusion and future work** 

**129** 

### **3.4.2 CSA** _p_ **HLRP-2 Computational experiments** 

Instances was named in a format _Cabi_  j_  αβ_ where _i_ indicates the number of nodes, _j_ indicates the number of hubs, _α_ indicates the factor of economies of scale and _β_ the factor of changing the relative weight of the cycle. 

In Table 3.12, Table 3.13, Table 3.14 and Table 3.15, we report the results of branch and cut in (Rodríguez-Martín et al., 2014), next the HH results. The gap between CPLEX and HH never exceeds 1%. Furthermore, the average of the gap between initial objective and the best found is 21 _._ 01%, which inherits some similarity to CSA _p_ HLRP-1. Execution time for AP instances with 40 and 50 nodes, was show in Figure 3.8. It is clear that HH process for for these instances doesn’t exceed 4.5 sec. 

Figure 3.5 - Figure 3.7 sketch the optimal solution for a CAB instance, as proven in Rodríguez-Martín et al. (2014) and offered by the proposed HH, having 25 nodes, _q_ = 13, _α_ =0.8, _β_ =0.01 or 0.05 or 0.2. Due to the influence of the objective function, while _β_ increase while cycles try be more large. 

## **3.5 Conclusion and future work** 

We proposed a hyperheuristic approach for solving two variants of Hub Location Routing Problems, CSA _p_ HLRP-1 and CSA _p_ HLRP-2. Given a set of nodes and a set of O-D demands, the problem seeks designating _p_ hubs, allocating each non-hub (spoke) node to one hub while each hub lies on a Hamiltonian path comprised of 

**Capacitated Single Allocation p-Hub Location Routing Problem** 

**130** 



**Figure 3.5:** Optimal solution for CAB25 with _p_ =5, _q_ =13, _α_ =0.8, _β_ =0.01. 



**Figure 3.6:** Optimal solution for CAB25 with _p_ =5, _q_ =13, _α_ =0.8, _β_ =0.05. 



**Figure 3.7:** Optimal solution for CAB25 with _p_ =5, _q_ =13, _α_ =0.8, _β_ =0.2. 

**3.5 Conclusion and future work** 

**131** 



<!-- Start of picture text -->
5<br>4<br>3<br>2<br>1<br>0<br>Instances<br>Computational Time (sec.)<br>AP40_3_0.75_1 AP40_3_0.75_100 AP40_3_0.75_1000 AP40_3_0.75_500 AP40_4_0.75_1 AP40_4_0.75_100 AP40_4_0.75_1000 AP40_4_0.75_500 AP40_5_0.75_1 AP40_5_0.75_100 AP40_5_0.75_1000 AP40_5_0.75_500 AP50_3_0.75_1 AP50_3_0.75_100 AP50_3_0.75_1000 AP50_3_0.75_500 AP50_4_0.75_1 AP50_4_0.75_100 AP50_4_0.75_1000 AP50_4_0.75_500 AP50_5_0.75_1 AP50_5_0.75_100 AP50_5_0.75_1000 AP50_5_0.75_500<br><!-- End of picture text -->

**Figure 3.8:** HH execution time in CSA _p_ HLRP-2. 

the hub and its spokes. The allocation of nodes and the construction of Hamiltonian paths is done in such a way that the transported volume on the route respects a given capacity in CSA _p_ HLRP-1, and not exceed a certain number of spokes in CSA _p_ HLRP-2 and the hub-level network is a connected one. While exact methods have shown a very limited success, for CSA _p_ HLRP-1, when dealing with instances of problem and the instances of moderate size remain still very intractable, one has to resort to non-exact (heuristic-based) methods for obtaining solutions to the moderate-to-large size instances. We applied five Lagrangian Relaxation on the model of CSA _p_ HLRP-1, and we use the results of the best one in the process of HH. LR HH has proven in the numerical results as better than HH without LR results, even its initial fitness. We proposed hyperheuristic method for the two problem, in order to solve large instances. The proposed hyperheuristic consists 

**132 Capacitated Single Allocation p-Hub Location Routing Problem** 

of several low level heuristics guided by means of a learning method, which is inspired from a topic in business data mining world known as _Association Rules_ for CSA _p_ HLRP-1, and _Q-Learning_ method for CSA _p_ HLRP-2. 

Our numerical results, for the two problems, show that in the case of instances for which an optimal solution or a solution with known quality is known, the proposed method is capable of providing high quality solutions. In all cases, such solutions are obtained in a very reasonable CPU times. Therefore, it is expected that for larger size instances for which finding an optimal solution needs an effort beyond the capacity of current hardware resources, the proposed framework that is equipped with advances learning mechanisms performs sufficiently well. 

In our future work we will add further aspects of real-life application to the model and consider solving problem taking into account heterogeneous fleet of vessels with different route capacities, inter-route transshipment etc. 

**3.5 Conclusion and future work** 

**133** 

**Table 3.12:** Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), cab instance with 25 nodes 

|Instance|q<br>B&C Obj. ValueRodríguez-Martín et al.|(2014)<br>HH. Obj. Value|Gap (%)|
|---|---|---|---|
|Cab25_3_0.2_0.01||V|<br>858.76|858.76|0.00|
|Cab25_3_0.2_0.05<br>Cab25_3_0.2_0.2<br>||V|<br>1193.41<br>|V|<br>2448.35<br><br>|1193.41<br>2448.35<br>|0.00<br>0.00<br>|
|Cab25_3_0.4_0.01<br>Cab25_3_0.4_0.05||V|<br>998.04<br>|V|<br>1332.69|998.04<br>1332.69|0.00<br>0.00|
|Cab25_3_0.4_0.2||V|<br>2587.63|2587.63|0.00|
|Cab25_3_0.8_0.01<br>Cab25_3_0.8_0.05<br>||V|<br>1254.02<br>|V|<br>1605.91<br><br>|1254.02<br>1605.91<br>|0.00<br>0.00<br>|
|Cab25_3_0.8_0.2<br>Cab25_4_0.2_0.01||V|<br>2827.03<br>|V|<br>720.84|2827.03<br>720.84|0.00<br>0.00|
|Cab2540.20.05||V|<br>1041.09|1041.09|0.00|
|___<br>Cab25_4_0.2_0.2<br>Cab25_4_0.4_0.01||V|<br>2227.04<br>|V|<br>876.30|2227.04<br>876.30|0.00<br>0.00|
|Cab25_4_0.4_0.05<br>Cab25_4_0.4_0.2||V|<br>1206.25<br>|V|<br>2392.19|1206.25<br>2392.19|0.00<br>0.00|
|Cab25_4_0.8_0.01<br>Cb25408005||V|<br>1176.44<br>|V|<br>152842|1176.44<br>152842|0.00<br>000|
|a__._.<br>Cab25_4_0.8_0.2|.<br>|V|<br>2615.26|.<br>2615.26|.<br>0.00|
|Cab25_5_0.2_0.01<br>Cab2550.20.05||V|<br>626.71<br>|V|<br>947.54|626.71<br>947.54|0.00<br>0.00|
|___<br>Cab25_5_0.2_0.2<br>||V|<br>2027.18<br><br>|2027.18<br>|0.00<br>|
|Cab25_5_0.4_0.01<br>Cab25_5_0.4_0.05||V|<br>795.61<br>|V|<br>1120.99|795.61<br>1130.89|0.00<br>0.88|
|Cab25_5_0.4_0.2<br>Cab2550.80.01||V|<br>2179.65<br>|V|<br>1126.18|2179.65<br>1126.18|0.00<br>0.00|
|___<br>Cab25_5_0.8_0.05<br>||V|<br>1446.56<br><br>|1446.56<br>|0.00<br>|
|Cab25_5_0.8_0.2<br>||V|<br>2457.77<br><br>|2457.77<br>|0.00<br>|
|Cab25_3_0.2_0.01<br>Cab25_3_0.2_0.05||V|/2<br>865.42<br>|V|/2<br>1213.10|865.42<br>1223.16|0.00<br>0.82|
|Cab25_3_0.2_0.2<br>Cb25304001||V|/2<br>2495.76<br>|V|/2<br>99962|2495.76<br>99962|0.00<br>000|
|a__._.<br>|.<br><br>|.<br>|.<br>|
|Cab25_3_0.4_0.05<br>Cab25_3_0.4_0.2||V|/2<br>1359.94<br>|V|/2<br>2648.59|1359.94<br>2648.59|0.00<br>0.00|
|Cab25_3_0.8_0.01||V|/2<br>1254.02|1254.02|0.00|
|Cab25308005||V|/2<br>162326|162326|000|
|__._.<br>Cb2530802|.<br>|V|/2<br>291772|.<br>291772|.<br>000|
|a__._.<br>Cab25_4_0.2_0.01|.<br>|V|/2<br>720.84|.<br>727.50|.<br>0.92|
|Cab25_4_0.2_0.05||V|/2<br>1041.09|1041.09|0.00|
|Cab2540.20.2||V|/2<br>2227.04|2227.04|0.00|
|___<br>Cab25_4_0.4_0.01<br>||V|/2<br>876.30<br><br>|876.30<br>|0.00<br>|
|Cab25_4_0.4_0.05<br>Cab25_4_0.4_0.2||V|/2<br>1206.25<br>|V|/2<br>2392.19|1206.25<br>2392.19|0.00<br>0.00|
|Cab25_4_0.8_0.01<br>Cab2540.80.05||V|/2<br>1176.44<br>|V|/2<br>1528.42|1176.44<br>1528.42|0.00<br>0.00|
|___<br>Cab25_4_0.8_0.2<br>||V|/2<br>2716.52<br><br>|2716.52<br>|0.00<br>|
|Cab25_5_0.2_0.01<br>Cab25_5_0.2_0.05||V|/2<br>626.71<br>|V|/2<br>947.54|626.71<br>947.54|0.00<br>0.00|
|Cab25_5_0.2_0.2||V|/2<br>2040.02|2040.02|0.00|
|Cab25_5_0.4_0.01<br>Cab25_5_0.4_0.05<br>||V|/2<br>795.61<br>|V|/2<br>1120.99<br><br>|795.61<br>1120.99<br>|0.00<br>0.00<br>|
|Cab25_5_0.4_0.2<br>Cab25_5_0.8_0.01||V|/2<br>2208.83<br>|V|/2<br>1126.18|2208.83<br>1126.18|0.00<br>0.00|
|Cab2550.80.05||V|/2<br>1446.56|1446.56|0.00|
|___<br>Cab2550802||V|/2<br>251493|251493|000|
|__._.<br>Cab25_3_0.2_0.01<br>|.<br>|V|/p<br>943.25<br><br>|.<br>943.25<br>|.<br>0.00<br>|
|Cab25_3_0.2_0.05<br>Cab25_3_0.2_0.2||V|/p<br>1348.93<br>|V|/p<br>2789.59|1348.93<br>2789.59|0.00<br>0.00|
|Cab25_3_0.4_0.01<br>Cb25304005||V|/p<br>1089.05<br>|V|/<br>149495|1089.05<br>149675|0.00<br>012|
|a__._.<br>Cab25_3_0.4_0.2<br>|p<br>.<br>|V|/p<br>2926.27<br><br>|.<br>2926.27<br>|.<br>0.00<br>|
|Cab25_3_0.8_0.01<br>Cab25_3_0.8_0.05||V|/p<br>1302.98<br>|V|/p<br>1708.64|1302.98<br>1708.64|0.00<br>0.00|
|Cab25_3_0.8_0.2<br>Cb25402001||V|/p<br>3099.42<br>|V|/<br>72198|3099.42<br>72198|0.00<br>000|
|a__._.<br>Cab25_4_0.2_0.05|p<br>.<br>|V|/p<br>1063.03|.<br>1063.03|.<br>0.00|
|Cab25_4_0.2_0.2<br>Cab2540.40.01||V|/p<br>2341.94<br>|V|/p<br>881.26|2341.94<br>881.26|0.00<br>0.00|
|___<br>Cab25404005||V|/<br>122230|122230|000|
|__._.<br>Cb2540402|p<br>.<br>||/<br>250122|.<br>250122|.<br>000|
|a__._.<br>|Vp<br>.<br><br>|.<br>|.<br>|
|Cab25_4_0.8_0.01<br>Cab25_4_0.8_0.05||V|/p<br>1178.69<br>|V|/p<br>1531.41|1178.69<br>1531.41|0.00<br>0.00|
|Cab2540.80.2||V|/p<br>2810.33|2822.19|0.42|
|___<br>Cab25_5_0.2_0.01<br>Cab25_5_0.2_0.05<br>||V|/p<br>686.85<br>|V|/p<br>1050.38<br><br>|686.85<br>1050.38<br>|0.00<br>0.00<br>|
|Cab25_5_0.2_0.2<br>Cab25_5_0.4_0.01||V|/p<br>2393.88<br>|V|/p<br>857.24|2393.88<br>857.24|0.00<br>0.00|
|Cab2550.40.05||V|/p<br>1221.48|1221.48|0.00|
|___<br>Cab25_5_0.4_0.2<br>||V|/p<br>2564.98<br><br>|2564.98<br>|0.00<br>|
|Cab25_5_0.8_0.01<br>Cab25_5_0.8_0.05||V|/p<br>1165.79<br>|V|/p<br>1532.11|1165.79<br>1532.11|0.00<br>0.00|
|Cab25_5_0.8_0.2||V|/p<br>2875.61|2885.14|0.33|



**Capacitated Single Allocation p-Hub Location Routing Problem** 

**134** 

**Table 3.13:** Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 25 nodes 

|Instance|q|B&C Obj. ValueRodríguez-Martín et al. (2014)|HH. Obj. Value|Gap (%)|
|---|---|---|---|---|
|AP25_3_0.75_1||V||155482.14|155539.68|0.04|
|AP25_3_0.75_100||V||177838.26|177838.26|0.00|
|AP25_3_0.75_500||V||262544.57|262544.57|0.00|
|AP25_3_0.75_1000<br>||V|<br>|366638.05<br>|366638.05<br>|0.00<br>|
|AP25_4_0.75_1||V||139430.10|139773.20|0.25|
|AP25_4_0.75_100||V||161485.26|161485.26|0.00|
|AP25_4_0.75_500||V||243004.56|243004.56|0.00|
|AP25_4_0.75_1000||V||344903.68|344903.68|0.00|
|AP25_5_0.75_1||V||123802.90|123802.90|0.00|
|AP25_5_0.75_100||V||145099.06|145099.06|0.00|
|AP25_5_0.75_500||V||227204.68|227204.68|0.00|
|AP25_5_0.75_1000||V||327043.26|327043.26|0.00|
|AP25_3_0.75_1||V|/2|155482.14|155482.14|0.00|
|AP25_3_0.75_100||V|/2|177838.26|177838.26|0.00|
|AP25_3_0.75_500||V|/2|262544.57|262591.10|0.02|
|AP25_3_0.75_1000||V|/2|366638.05|366638.05|0.00|
|AP25_4_0.75_1||V|/2|139430.10|139430.10|0.00|
|AP25_4_0.75_100||V|/2|161485.26|161485.26|0.00|
|AP25_4_0.75_500||V|/2|243004.56|243004.56|0.00|
|AP25_4_0.75_1000||V|/2|344903.68|344903.68|0.00|
|AP25_5_0.75_1||V|/2|123802.90|123802.90|0.00|
|AP25_5_0.75_100||V|/2|145099.06|145099.06|0.00|
|AP25_5_0.75_500||V|/2|227204.68|227204.68|0.00|
|AP25_5_0.75_1000||V|/2|327043.26|327567.38|0.16|
|AP25_3_0.75_1||V|/p|156287.34|156287.34|0.00|
|AP25_3_0.75_100||V|/p|178328.06|178328.06|0.00|
|AP25_3_0.75_500||V|/p|267381.48|267381.48|0.00|
|AP25_3_0.75_1000||V|/p|376932.18|376998.36|0.02|
|AP25_4_0.75_1||V|/p|139876.23|139876.23|0.00|
|AP25_4_0.75_100||V|/p|161720.99|161720.99|0.00|
|AP25_4_0.75_500||V|/p|249982.62|249995.77|0.01|
|AP25_4_0.75_1000||V|/p|359669.90|359899.70|0.06|
|AP25_5_0.75_1||V|/p|130727.14|130986.57|0.20|
|AP25_5_0.75_100||V|/p|154151.28|154222.44|0.05|
|AP25_5_0.75_500||V|/p|245105.99|247225.09|0.86|
|AP25_5_0.75_1000||V|/p|357731.82|359951.33|0.62|



**3.5 Conclusion and future work** 

**135** 

**Table 3.14:** Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 40 nodes 

|Instance|q|B&C Obj. ValueRodríguez-Martín et al. (2014)|HH. Obj. Value|Gap (%)|
|---|---|---|---|---|
|AP40_3_0.75_1||V||159131.34|159307.66|0.11|
|AP40_3_0.75_100||V||188910.27|190118.62|0.64|
|AP40_3_0.75_500||V||306243.01|309118.03|0.93|
|AP40_3_0.75_1000<br>||V|<br>|445218.18<br>|449552.36<br>|0.96<br>|
|AP40_4_0.75_1||V||144269.55|145531.86|0.87|
|AP40_4_0.75_100||V||174036.22|174210.98|0.10|
|AP40_4_0.75_500||V||291653.08|294126.26|0.84|
|AP40_4_0.75_1000||V||430540.90|432062.32|0.35|
|AP40_5_0.75_1||V||134569.34|135248.65|0.50|
|AP40_5_0.75_100||V||164038.24|165552.92|0.91|
|AP40_5_0.75_500||V||277247.49|277838.75|0.21|
|AP40_5_0.75_1000||V||411710.46|413003.15|0.31|
|AP40_3_0.75_1||V|/2|159131.34|160361.65|0.77|
|AP40_3_0.75_100||V|/2|188910.27|190482.33|0.83|
|AP40_3_0.75_500||V|/2|306243.01|307611.19|0.44|
|AP40_3_0.75_1000||V|/2|445218.18|448957.91|0.83|
|AP40_4_0.75_1||V|/2|144269.55|144898.52|0.43|
|AP40_4_0.75_100||V|/2|174036.22|175315.75|0.73|
|AP40_4_0.75_500||V|/2|291653.08|294172.56|0.86|
|AP40_4_0.75_1000||V|/2|430540.90|434211.48|0.85|
|AP40_5_0.75_1||V|/2|134569.34|134937.21|0.27|
|AP40_5_0.75_100||V|/2|164038.24|165195.15|0.70|
|AP40_5_0.75_500||V|/2|277247.49|278422.13|0.42|
|AP40_5_0.75_1000||V|/2|411710.46|413651.82|0.47|
|AP40_3_0.75_1||V|/p|161989.74|163463.58|0.90|
|AP40_3_0.75_100||V|/p|191404.41|191537.87|0.07|
|AP40_3_0.75_500||V|/p|309484.80|312184.78|0.86|
|AP40_3_0.75_1000||V|/p|454614.67|455895.18|0.28|
|AP40_4_0.75_1||V|/p|145732.10|145926.45|0.13|
|AP40_4_0.75_100||V|/p|176241.71|177536.93|0.73|
|AP40_4_0.75_500||V|/p|295787.67|296627.18|0.28|
|AP40_4_0.75_1000||V|/p|443393.74|444343.50|0.21|
|AP40_5_0.75_1||V|/p|139032.42|140286.01|0.89|
|AP40_5_0.75_100||V|/p|168736.29|169422.29|0.40|
|AP40_5_0.75_500||V|/p|286728.55|289342.59|0.90|
|AP40_5_0.75_1000||V|/p|453254.27|455785.30|0.56|



**Capacitated Single Allocation p-Hub Location Routing Problem** 

**136** 

**Table 3.15:** Comparison of the quality between results of HH and B&C Obj. Value Rodríguez-Martín et al. (2014), AP instance for 50 nodes 

|Instance|q|B&C Obj. ValueRodríguez-Martín et al. (2014)|HH. Obj. Value|Gap (%)|
|---|---|---|---|---|
|AP50_3_0.75_1||V||158880.67|159311.06|0.27|
|AP50_3_0.75_100||V||189643.25|190608.90|0.51|
|AP50_3_0.75_500||V||313509.45|314390.99|0.28|
|AP50_3_0.75_1000<br>||V|<br>|461294.25<br>|464755.89<br>|0.74<br>|
|AP50_4_0.75_1||V||143692.01|143819.90|0.09|
|AP50_4_0.75_100||V||174356.01|174676.08|0.18|
|AP50_4_0.75_500||V||297364.38|297604.55|0.08|
|AP50_4_0.75_1000||V||444031.52|445899.83|0.42|
|AP50_5_0.75_1||V||132689.72|133359.01|0.50|
|AP50_5_0.75_100||V||163460.64|163743.78|0.17|
|AP50_5_0.75_500||V||281644.93|283820.89|0.77|
|AP50_5_0.75_1000||V||426543.08|430379.06|0.89|
|AP50_3_0.75_1||V|/2|158880.67|160187.65|0.82|
|AP50_3_0.75_100||V|/2|189643.25|190272.34|0.33|
|AP50_3_0.75_500||V|/2|313509.45|315496.93|0.63|
|AP50_3_0.75_1000||V|/2|468204.82|471234.36|0.64|
|AP50_4_0.75_1||V|/2|143692.01|145047.48|0.93|
|AP50_4_0.75_100||V|/2|174356.01|175116.27|0.43|
|AP50_4_0.75_500||V|/2|297364.38|300110.39|0.92|
|AP50_4_0.75_1000||V|/2|444031.52|446973.31|0.66|
|AP50_5_0.75_1||V|/2|132688.63|133157.79|0.35|
|AP50_5_0.75_100||V|/2|163460.64|164354.90|0.54|
|AP50_5_0.75_500||V|/2|281644.93|282177.99|0.19|
|AP50_5_0.75_1000||V|/2|426543.08|430587.17|0.94|
|AP50_3_0.75_1||V|/p|162358.48|163567.25|0.74|
|AP50_3_0.75_100||V|/p|193611.51|194612.66|0.51|
|AP50_3_0.75_500||V|/p|318506.03|321222.49|0.85|
|AP50_3_0.75_1000||V|/p|487540.97|490968.03|0.70|
|AP50_4_0.75_1||V|/p|144210.66|145604.69|0.96|
|AP50_4_0.75_100||V|/p|175349.65|177053.61|0.96|
|AP50_4_0.75_500||V|/p|300103.26|302645.79|0.84|
|AP50_4_0.75_1000||V|/p|462471.69|463936.61|0.32|
|AP50_5_0.75_1||V|/p|140093.97|140132.69|0.03|
|AP50_5_0.75_100||V|/p|173088.85|173680.76|0.34|
|AP50_5_0.75_500||V|/p|311508.49|311727.23|0.07|
|AP50_5_0.75_1000||V|/p|524502.41|528222.94|0.70|



# **Chapter 4** 

# **Selection Methods** 

## **4.1 Introduction** 

In the context of combinatorial problem, hyperheuristic is defined as _heuristics to select heuristics_ Cowling et al. (2001). While the objective of a heuristic is to offer a feasible (near-optimal) solution, selective heuristic aims at identifying a series of heuristics to be applied. The selection process can be totally random or based on some historical performances. Statistical performances should be related to the solution quality offered by each heuristic and the computational time taken by each low-level-heuristic. When these accumulated statistical performance intervene in the selection process, we talk about learning mechanism. Learning is defined as the act of acquiring new, or modifying and reinforcing existing knowledge and information. According to the Oxford dictionaries, it is the acquisition of knowledge or skills through study, experience, or being taught. Hence, The science of enabling 

**Selection Methods** 

**138** 

computer to learn is known as machine learning (ML), that is considered as the capacity of a computer to learn from historical experiences. 

In the context of hyperheuristic, machine learning contributes in selecting an incumbent heuristic to be applied based on historical performances. ML appears in different aspects such as _reinforcement learning_ , _choice function_ , _metaheuristic_ etc, which will be elaborated in the second section. The problem of selection heuristics during hyperheuristic process is closely related to other problems such as _Algorithm Selection Problem_ Rice (1976), _MetaLearning_ Smith-Miles (2008) and etc. Algorithm Selection Problem deals with the selecting the best algorithm among a pool to solve a given problem. According to Rice (1976), The broad methodology which binds problems and solution methods with performance and problem characteristics is the algorithm selection framework. Three important dimensions should be taken into consideration when addressing algorithm selection problems: (i) the problem space; (ii) the algorithm space, and (iii) the performance measure. It is an abstract model as shown in Figure 4.1, which limits its wide application and it did not provide a specific implementation methods. However, metalearning has been successfully applied in different problem domains SmithMiles (2008). Metalearning is a subfield of Machine learning Hilario et al. (2009), which exploits metadata (metafeatures) resulted from previous experiments by constructing models that can be used for prediction. In that situation in which no additional knowledge of available algorithms or problem structure exist, the automation of the whole process will then be called the _hyperheuristic_ . 

**4.2 The Proposed Selection Methods** 

**139** 



**Figure 4.1:** Algorithm selection model taken by Rice (1976). 

## **4.2 The Proposed Selection Methods** 

Several selection methods have been proposed in the literature. Chakhlevitch and Cowling (2008a) categorizes such methods as in the sequel: i) random selection, ii) greedy selection, iii) peckish selection iv) metaheuristic-based hyperheuristic, and v) hyperheuristic with learning. 

In this chapter, we will present and propose several heuristic selection methods, which are categorized in two main class: i) random selection (i.e. pure random selection, random descent, and etc.) (see in (Özcan and Kheiri, 2012), (Kendall and Mohamad, 2004)), and ii) intelligent method, which it is based on some accumulated historical performances (i.e. choice function (see in (Kendall et al., 2002a), (Drake et al., 2015)), metaheuristic (see in (Kendall and Mohamad, 2004), (Burke and Soubeiga, 2003)), etc.). In the other way, selection methods can be categorized as sequential selection(i.e. Random Permutation Descent (Cowling et al., 2001), Bayes (our proposition), Association Rules (our proposition), etc.) and parallel selection (i.e. peckish (see in (Cowling and Chakhlevitch, 2003), Cowling 

**Selection Methods** 

**140** 

and Chakhlevitch (2007)), greedy (see in (Cowling et al., 2001), (Cowling et al., 2002b)), (Özcan and Kheiri, 2012)) , etc.). Some of them perform by applying a selected heuristic until a worsening move is hit. 

### **4.2.1 Random Selection Based Hyperheuristic** 

The term _Random_ can be defined as "made, or occurring without definite aim, reason, or pattern". Selecting a random item from a predefined set, expects that all items have the same probability to be selected. 

Randomness is the loss of pattern or predictability in activities. Therefore, _random heuristic selection method_ is based on selecting one of existing heuristic with no data based input. For that, expected running time depends on the random choices only, not on any input distribution. Random selection algorithms are often simpler and faster than other algorithms. Another important feature of this method, is the inherit diversification in the process. 

The disadvantages can be summarized as: i) lack of intensification strategy in the algorithm, ii) The solution quality can vary among more than one execution, and iii) heuristic selection probability is totaly independent of its performance. 

In the following, we present three approaches of random selection regularly used in the literature: i) Pure random, ii) Random descent, and iii) Random permutation descent. 

**4.2 The Proposed Selection Methods** 

**141** 

#### **Pure Random** 

Pure random hyperheuristic is the most straightforward way to implement a of hyperheuristic. It is based on randomly selecting one of the existing low-levelheuristic from a set of predefined low-level-heuristics at each decision point Chakhlevitch and Cowling (2008a). 

Pure random hyperheuristics have been applied in many problem domains such as scheduling problems (see Cowling et al. (2001), Cowling et al. (2002b), Cowling et al. (2002a)), space allocation problems (see Bai and Kendall (2005), Burke and Kendall (2005)), channel assignment in mobile communication problems(see Kendall and Mohamad (2004)) and time tabling problems(see Burke and Kendall (2005)). 

#### **Random Descent (Gradient)** 

Random descent or random gradient declare the heuristic selection strategy as choosing a low-level-heuristic randomly and employ it as long as the candidate solution in hand is improved Özcan et al. (2012). Hence, the improving low-levelheuristic is applied repeatedly until a worsening move is hit. 

Random Descent method was applied in many domains (see Cowling et al. (2001), Soubeiga (2003) for examples of such a selection strategy). 

**Selection Methods** 

**142** 

#### **Random Permutation Descent (Gradient)** 

Random Permutation Descent selection chooses randomly a set of low-levelheuristics, which form a cyclic list. It then applies the first heuristic and employ it until a worsening move is observed. It then applies the next ones in the order dictated by the cycle. Examples of such selection strategy can be found in Özcan and Kheiri (2012), Cowling et al. (2001) and Burke and Soubeiga (2003). 

### **4.2.2 Greedy Based Hyperheuristic** 

Greedy selection applies all low-level-heuristics independently at each iteration, to the same solution candidate and chooses the one that generates the best solution quality. No diversification type is considered, while only improvement moves are accepted (see Cowling et al. (2002b), Cowling et al. (2001) and Özcan and Kheiri (2012) for examples of such strategies). 

The limitation of this approach is mainly the limited capacity to explore the search space in order to avoid local optima (Chakhlevitch and Cowling, 2008a). 

### **4.2.3 Peckish Based Hyperheuristic** 

The term _Peckish_ follows the same concepts as a greedy selection, but a subset of low-level-heuristics is considered instead of all low-level-heuristics. (Cowling and Chakhlevitch, 2003) and (Cowling and Chakhlevitch, 2007) are among the examples of work considering this selection method. 

In this chapter, we will present more than one method of _Peckish_ selection based 

**4.2 The Proposed Selection Methods** 

**143** 

on the way of choosing subset of low-level-heuristic to be applied in a parallel manner. There are as the following: 

1. Peckish selection based on Tabu Search (TS), where TS, selects a predefined number of heuristics to be applied in parallel at each iteration. 

2. Peckish selection based on Simulated Annealing (SA), where SA, selects predefined number of heuristics. 

3. Peckish selection based on Association Rules (AR), where AR, selecst the subset of heuristics to be applied in parallel at each iteration. 

4. Peckish selection based on Bayes Theorem (BT) 

5. Peckish selection based on Q-Learning (QL) 

### **4.2.4 Choice Function Based Hyperheuristic** 

Choice function heuristic selection methods, defined by Cowling et al. (2001), addresses learning as a model selection problem. The choice function selects a low-level-heuristic to be applied according to a weight resulted from a combination of three different measures. Therefore, selection of such low-level-heuristic at each iteration depends on its corresponding choice function. For that reason, score computations for the low-level-heuristics are repeated at each iteration. 

The low-level heuristics are ranked according to several measures. The heuristic ranking technique is based on: I) the heuristic’s individual performance (Equation (4.1)), II) improvement observed as a results of invoking a heuristic subsequent 

**Selection Methods** 

**144** 

to another one (Equation (4.2)), and III) the time elapsed since it was last called (Equation (4.3)). _In_ ( _y_ ) and _Tn_ ( _y_ )( _In_ ( _x, y_ ) and _Tn_ ( _x, y_ )) indicate the change of evaluation function and the amount of execution time, when the _n_<sup>_th_</sup> last time the heuristic _y_ was chosen and applied immediately after heuristic _x_ . 

Intensification strategies were provided by the first two components, while the diversification was assured by the third on. _α_ , _β_ , and _δ_ , represents the weights of the three components and their relative influence on the choice function. Both _α_ and _β ∈_ [0 _,_ 1] reflect the greater influence attached to recent performance. 

The approach mentioned above is prevented from reaching its full potential by several obstacles. The first obstacle being that it requires a warm-up period during which the values of the choice functions will be initialized by randomly selected heuristics. The second one, is that achieving the best results requires the weights _α_ , _β_ , and _δ_ of individual components in the choice function to be manually tuned. 



<!-- Start of picture text -->
f 1( hj ) = � n α n− 1 ( T In n ( ( h h j j ) ) ) (4.1)<br><!-- End of picture text -->



<!-- Start of picture text -->
f 2( hk, hj ) = � n β n− 1 ( T In n ( ( h h k k , , h  hj j ) ) ) (4.2)<br><!-- End of picture text -->



<!-- Start of picture text -->
f 3( hj ) =  elapsedTime ( hj ) (4.3)<br><!-- End of picture text -->

**4.2 The Proposed Selection Methods 145** 



<!-- Start of picture text -->
f ( hj ) =  αf 1( hj ) +  βf 2( hk, hj ) +  δf 3( hj ) (4.4)<br><!-- End of picture text -->

Cowling et al. (2001), Cowling et al. (2002b), Kendall et al. (2002b) and Soubeiga (2003) are examples of work considering this heuristic selection method. 

### **4.2.5 Reinforcement Learning** 

In reinforcement learning we are dealing with an _agent_ that learns its behavior through some interaction with a so called _dynamic environment_ . Such interaction is usually realized in trial-and-error efforts fashion. At each point in time, _t_ , an agent is in a given state _st ∈ S_ and can choose an action _at_ , eventually from among several, to make a transition to another state _st_ +1 _∈ S_ . In this work, we deal with the sets _S_ and _A_ of bounded cardinality, i.e. _card_ ( _|A|_ )+ _card_ ( _|S|_ ) _< card_ (R) = _ℵ_ . More precisely, where we work with a finite number of transition that can be made. 

When an action is taken, a numerical reward, _rt_ +1 is attributed. Such reward is a feedback from the environment that depends on the quality of action taken by the agent. An agent that wants to maximize the total reward attributed to it, has to be able to exploit the experiences it has obtained so far and also be able to explore other parts of the environment and identify better actions Sutton and Barto (1998). In general, there are two types of reinforcement learning: 

1. _Online Learning_ : heuristic rewards are updated online (i.e. dynamically) throughout the search according to the performance of every heuristic. 

**Selection Methods** 

**146** 

2. _Off-line Learning_ : heuristics rewards are retrieved from a database, which stores the historical performance of every heuristic in the past. 

#### **Naive Bayes Classifier based Hyperheuristic** 

In the context of probability science, inverse probability is an obsolete term for the probability distribution of an unobserved variable. Hence, Thomas Bayes (1701 1761) proposed a solution to a problem of inverse probability. The proposed solution was presented in "An Essay towards solving a Problem in the Doctrine of Chances" which was read to the Royal Society in 1763 after Bayes’ death. 

Today, the problem of determining an unobserved variable (by whatever method) is called inferential statistics, the method of inverse probability (assigning a probability distribution to an unobserved variable) is called Bayesian probability, the "distribution" of an unobserved variable given data is rather the likelihood function (which is not a probability distribution), and the distribution of an unobserved variable, given both data and a prior distribution, is the posterior distribution. The development of the field and terminology from "inverse probability" to "Bayesian probability" is described by Fienberg (2006). 

Bayesian probability is one interpretation of the concept of probability. In contrast to interpreting probability as frequency or propensity of some phenomenon, Bayesian probability is a quantity that we assign to represent a state of knowledge, Jaynes (1986) or a state of belief.De Finetti (1974) In the Bayesian view, a probability is assigned to a hypothesis, whereas under frequentist inference, a hypothesis is typically tested without being assigned a probability. 

**4.2 The Proposed Selection Methods** 

**147** 

Naive Bayes classifier assumes that all the features are conditionally independent of each other. This therefore permits us to use the Bayesian rule for probability. Usually this independence assumption works well for most cases, if even in actuality they are not really independent. Bayesian rules is stated mathematically as the following equation De Finetti (1974): 



<!-- Start of picture text -->
P ( A|B ) = P ( A )  P ( B|A ) , (4.5)<br>P ( B )<br><!-- End of picture text -->

_A_ and _B_ are events, products, actions or etc. _P_ ( _A_ ) and _P_ ( _B_ ) are the probabilities of _A_ and _B_ without regard to each other. _P_ ( _A|B_ ), a conditional probability, is the probability of observing event _A_ given that _B_ is true. _P_ ( _B|A_ ), is the probability of observing event _B_ given that _A_ is true. 

In our proposed method, after each heuristic being applied, the frequency of worsening moves and the frequency of improvement move was accumulated. Therefore, in our hand we have at each iteration, the number of times each heuristic has improved/worsened the solution. Hence, we can calculate the probability of a heuristic _hi_ given that the solution is improved. 

The method is based on dividing the time horizon into three portion ( _V_ 1, _V_ 2 and _V_ 3). In _V_ 1, which represents the time when the process starts till the time limit ( _Tl_ ) divided by 5, heuristics are selected totaly random. In _V_ 2, which is bounded between _V_ 1 and 3 _Tl_ divided by 5, a heuristic _hi_ will be selected in the case of having the probability of being applied given that the solution was improved ( _P_ ( _hi|class_ = _Improvement_ )) is grater than 0.4. In addition, a 

**Selection Methods** 

**148** 

chance of 0.2 is acceptable by the search space in the case where the heuristic is selected randomly. In the last period, _V_ 3, the selected heuristic _hi_ must have _P_ ( _hi|class_ = _Improvement_ ) greater than 0.6, or it may be selected in a probability of 0.1. 

Bayesian approach is usually used in the domain of data mining, such as in Heckerman (1997), Kirkos et al. (2007), and Kantarcıoglu et al. (2003). Also, many researches applied bayesian approach in the context of optimization such as Inza et al. (2000), Mockus (2012), and Pelikan (2005). 

### **4.2.6 Metaheuristics Based Hyperheuristic** 

Metaheuristic, as mentioned in the chapter 1, can be defined as an iterative generation of a process, which guides a subordinate heuristic by combining intelligently different concepts for exploring and exploiting the search space Osman and Laporte (1996). Here, the role of metaheuristic is not to search in a solution space, but to search in the space of heuristics in order to guide HH to choose heuristics during HH process. We implement different metaheuristic methods: Simulated Annealing, Ant Colony, Variable Neighborhood Search and Genetic Algorithm. 

#### **Simulated Annealing Based Hyperheuristic** 

Simulated Annealing (SA) as an idea is inspired from a paper published by Metropolis et al. (1953), is motivated by an analogy to annealing in solids. It describes an algorithm that simulates the process called ’annealing’ which is the cooling 

**4.2 The Proposed Selection Methods** 

**149** 

of materials in a heat bath. Cooling a solid after heating it past its melting point makes its structural properties dependent on the cooling rate. It is also possible to notice the formation of crystals in the case where the cooling process was slow enough. If cooling the materials was achieved rapidly then there is a high chance that the crystals will contain imperfections. The materials used in Metropolis’s algorithm were simulated as a system of particles. The simulation lowered the system’s temperature gradually until it converged to a steady, frozen state. In 1982, optimization problems were subjected to SA for the first time in Kirkpatrick (1984). Simulated annealing was used to search for feasible solutions that could converge into an optimal solution. 

The law of thermodynamics express that at temperature, _t_ , the likelihood of an expansion in vitality of greatness, _δE_ , is given by 



<!-- Start of picture text -->
P ( δE ) = exp( −δE/kT ) (4.6)<br><!-- End of picture text -->

Where _k_ is a consistent known as Boltzmann’s steady. The reenactment in the Metropolis calculation computes the new vitality of the framework. On the off chance that the vitality has diminished then the framework moves to this state. In the event that the vitality has expanded then the new state is acknowledged utilizing the likelihood returned by the above recipe. A specific number of emphases are done at every temperature and afterward the temperature is diminished. This is rehashed until the framework solidifies into an unfaltering state. This mathematical 

**Selection Methods** 

**150** 

statement is specifically utilized as a part of reenacted toughening, in spite of the fact that it is common to drop the Boltzmann consistent as this was just acquainted into the comparison with adapt to various materials. Along these lines, the likelihood of tolerating a more terrible state is given by the mathematical statement 



<!-- Start of picture text -->
P = exp( −c/t )  ≥ r (4.7)<br><!-- End of picture text -->

Where: 

_c_ = the adjustment in the assessment capacity. 

_t_ = the present temperature. 

_r_ = an irregular number somewhere around 0 and 1. 

The likelihood of tolerating a more terrible move is a component of both the temperature of the framework and of the adjustment in the cost capacity. It can be valued that as the temperature of the framework diminishes the likelihood of tolerating a more terrible move is diminished. This is the same as slowly moving to a solidified state in physical annealing. Additionally take note of, that if the temperature is zero then just better moves will be acknowledged which successfully makes recreated strengthening act like slope climbing. 

SA was widely applied in many different combinatorial problem, such as scheduling problem (see Ma et al. (2016), Bouleimen and Lecocq (2003) and Schlünz and Van Vuuren (2013)), hub location problem (see Sedehzadeh et al. (2014), Parvaresh et al. (2013) and Rabbani and Kazemi (2015)), routing problem (see Grosse et al. 

**4.2 The Proposed Selection Methods** 

**151** 

(2014),BañOs et al. (2013) and Vincent and Lin (2014)), workover rig problem (see Ribeiro et al. (2011) and Paiva et al. (2000)) and etc. 

SA was used in hyperheuristic approaches in a two manners: I) in selection heuristics and II) in accepting a candidate solution. SA as an accepting criteria was explained in Chapter 1. 

SA heuristic selective hyperheuristic was applied as a tool to select a heuristic of a reward r ,0 _< r <_ 1, having exp(<sup>_−_</sup> _t_<sup>_<u>r</u>_)</sup><sup>_>random_(0</sup><sup>_,_1).Annealing schedule is</sup> considered as linear, where: 



<!-- Start of picture text -->
T ( t ) =  T 0  − ηt (4.8)<br><!-- End of picture text -->

Dowsland et al. (2007), Bai et al. (2012), Anagnostopoulos and Koulinas (2010) are examples of SA selective hyperheuristic. 

#### **Ant Colony Based Hyperheuristic** 

Ant colony optimization (ACO) is among the well-known population-based metaheuristics that has been extensively proposed to solve difficult optimization problems. In the natural world, ants move randomly, and then they lay down pheromone trails by the way of finding food and returning to their colony. Other ants stop wandering randomly upon discovering such a path by following the trail. With time, evaporation of pheromone trail will take place and its attractive strength will be minimized. The pheromone evaporates more as the time taken by the ants to stroll the path back and forth increases. For clarification, the pheromone density 

**Selection Methods** 

**152** 

becomes higher on shorter paths, which is the more frequent marched path, than longer ones. Pheromone evaporation is the key process of searching for optimal solution. However, if evaporation process does not exist, all ants will follow the first path chosen by first ants. Therefore, the exploration of the solution space would be constrained. In such cases, when one ant finds the shortest path from colony to a food source, all ants are aiming to follow this single path with their positive leading feedback. The goal of the ant colony algorithm is to avoid such a behaviour with a kind of ’simulated ants’ walking around the graph representing the problem to solve. Successful applications of ACO has been reported in hub location routing problem (Randall (2008), Ting and Chen (2013)), vehicle routing problem (Chávez et al. (2016), Gajpal and Abad (2009)), timetable problem (Dowsland and Thompson (2005), Ayob and Jaradat (2009)) etc. 

This technique has been used as a heuristic selection method in hyperheuristic approaches. The ant based hyperheuristic, proposed by Kiraz et al. (2013), is proven to be better than the choice function hyperheuristic on some problem domains. Another ant-based hyperheuristic proposed by Ferreira et al. (2015). A hybrid flow shop scheduling problem is solved by an ant colony optimization-based hyperheuristic combined with a genetic algorithm, which forms a hyperheuristic that generate and select heuristics. 

Our proposed method is the following: 

1. An arc is formed between every two heuristic, which allows the transition between any heuristic to another. 

**4.2 The Proposed Selection Methods** 

**153** 

2. A pheromone _τij_ and a visibility function _ηij_ were defined for each vertex <i,j>, and they are updated after each heuristic application using (4.10) and (4.9). The visibility function in our proposition is inspired from the choice function hyperheuristic. 



<!-- Start of picture text -->
ηij =  β I ( hi, hj ) (4.9)<br>T ( hi, hj<br><!-- End of picture text -->



<!-- Start of picture text -->
<br><br> ρ × ηij + C C bestk if ant  k  chooses heuristic  j after heuristic  i<br>τij =<br><br><br> ρ × ηij Otherwise<br><br>(4.10)<br><!-- End of picture text -->

It should be to note that, the _ρ_ coefficient indicates the evaporation rate. 

3. Since the hyperheuristic starts with no knowledge about the existing lowlevel-heuristics, it must be initially unbiased and impartial while continuously adaptive. 

4. The probability of selecting a heuristic _j_ after a applying heuristic _i_ is defined in (4.11). 



<!-- Start of picture text -->
ηij × τij<br>Pij = (4.11)<br>� i � j ηij × τij<br><!-- End of picture text -->

#### **Variable Neighborhood Search based Hyperheuristic** 

Variable neighborhood search (VNS), proposed by Mladenovi´c and Hansen (1997b), is another kind of metaheuristics for COPs. It explores neighborhoods, which ap- 

**Selection Methods** 

**154** 

plied on solution space, and moves from there randomly or intelligently. VNS includes two main phases: I) shaking phase and II) local search phase. The first one aims to diversify the search space in order to escape from local optima, while the objective of the second phase is to intensify the search around the current solution in order to improve it. Figure 4.2 shows how each combination of these two phases contributes in avoiding a local optimum and tries to explore and exploit the search space in order to achieve a near optimal solution. Each phase contains more than one heuristic, which necessitates a definition of the heuristic selection method. VNS appears an affective tool when it is combined with hyperheuristic methods. Hsiao et al. (2012) propose a VSN based hyperheuristic method for solving more than one problem such as job shop scheduling, bin packing, and etc Hansen and Mladenovi´c (2014). Remde et al. (2007) proposed a VNS hyperheuristic in order to solve workforce scheduling problem. In this work, hyperheuristic appears a powerful tools compared with the solution quality resulted by a genetic algorithm. The proposed VNS hyperheuristic, shown in Figure 4.3, aims to constructs a feasible solution at the beginning, then construct the shaking and finally the local search phases. In the shaking phase, the tabu search method, which is proposed in chapter 2, selects a low level heuristic from the set of perturbation heuristic. In the second phase, a random cycle of the existing predefined improvement heuristics is formed. It applies improvement heuristic while it is still improving the solution and switches to the next one in the cycle in case it stops improving the solution. It keeps on repeating this process until reaching n consecutive non-improving solution. 

**4.2 The Proposed Selection Methods** 

**155** 



**Figure 4.2:** A general schema of the VNS algorithm. 



**Figure 4.3:** The process of the proposed VNS Hyperheuristic. 

**Selection Methods** 

**156** 

## **4.3 Numerical Results** 

In order to examine performance of different selection methods, every method is in turn examined on the same problem in chapter 3, CSA _p_ HLRP-1, and the same testbed. 

Results of HH within different heuristic selection methods are reported in this section (including Tabu Search method proposed in chapter 2, Association Rules and Q-learning proposed in chapter 3) in 4.4 (and further elaborated in Figure 4.5, Figure 4.6 and Figure 4.7) while the acceptance criteria employe here is SA and all methods have the same input. Low gaps between the different methods, even the pure random selection method, prove the effectiveness of the hyperheuristic. Overall, pure random and greedy selection methods were the worst one, while the Association Rules selection method was the better. Note that, for small instances, the solution quality differences between most selection methods is minimal. Random Descent and Random Permutation Descent are better than pure random method. Peckish based on Bayes theorem was proven to be exceptionally effective compared with the most other methods. Reinforcement learning and metaheuristic method have a good solutions compared with the other, specially Association Rules, Q-learning and Tabu Search. 

In general, SA acceptance criteria with the different selection methods is the better, while minimal differences exists when using the other acceptance criteria. It should be note that: 

1. Association Rules with SA is indeed better than with Great Deluge by an 

**4.4 Conclusion** 

**157** 



**Figure 4.4:** HH results within different heuristic selection methods 

average of 0.7%. 

2. In all selection methods, almost any other acceptance criteria is better than random acceptance in 0.62% except the choice function in 0.38%. 

3. Choice function with SA is better than OI in 0.84%. 

4. Choice function with SA is better than IE in 0.24%. 

5. Q-learning with Great Deluge is better than with SA in 0.102%. 

Furthermore, if we expand the execution time no additional gain was observed. 

## **4.4 Conclusion** 

In this chapter, we presented and proposed different heuristic selection methods in order to integrate them in HH framework. We propose different learning and 

**Selection Methods** 

**158** 



**Figure 4.5:** HH results within different peckish selection methods 



<!-- Start of picture text -->
800000.00<br>700000.00<br>600000.00<br>500000.00<br>400000.00<br>300000.00<br>200000.00<br>100000.00<br>0.00 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45<br>TS SA AssociationRule Q-Learning Bayes VNS<br><!-- End of picture text -->

**Figure 4.6:** HH results within different RL selection methods 

**4.4 Conclusion** 

**159** 



**Figure 4.7:** HH results within simple random, random descent, random permutation descent, greedy and choice function selection methods 

metaheuristic methods as heuristic selection methods and we compared their performances when applyed on HLRP proposed in chapter 3. Here, SA acceptance criteria appears in average the best acceptance method among others such as all moves method, naive method, great deluge, etc. The performance of the overall performance of methods; even the random and greedy selection which is the last effective one; appears very promising, which proves the effectiveness of the other strategies of HH as well as robustness of LLHs. AR methods, which is well stablished in business data mining application, has proven to be the most effective learning method to select subsequent heuristics during the process of HH. 

**160 Selection Methods** 

# **Chapter 5** 

# **General Conclusion** 

In this thesis, we have studies the Hyperheuristic (Burke et al., 2008b, 2013), which is a search method or learning mechanism to select or generate heuristic in order to solve a specific combinatorial problem. Hyperheuristic is considered as a high-level approach that, given a problem and a number of low-level heuristics, can select/generate and apply a suitable low-level heuristic at each iteration. Topcuoglu et al. (2014) defines it as methods for automation of the process of selecting and generating multiple low-level heuristics. Clearly, the difference between metaheuristics and hyperheuristics lies in the fact that metaheuristics search directly on the solution space while hype-heuristics work on the heuristic space. This work proposes a selective hyperheuristic framework, which is comprised of a set of low-level heuristics and a heuristic selection mechanisms. 

In our study, we are dealing with problems in logistics. For general business concept, logistics is the administration of the flow of any matters between the point 

**General Conclusion** 

**162** 

of origin and that of consumption orderly to convene the customers or corporations needs. The managed resources in logistics may involve some physical matters like food, materials, animals, equipments and liquids, and some abstract matters like time and information. The logistics of physical matters can include the gathering of information flow, material handling, production, packaging, inventing, transportation, warehousing, and mainly security. Logistics management, which represented as an important part of supply chain management, focuses on planing, implementing, and controlling the efficient, effective forward, and reverse flow and storage of goods, services, and related information between the origin point to reach the destination. 

In the first thesis phase, we are invited to be a member with _Brazilian_ collaboration group, that is interested in a real logistic problem: Workover Rig Problem. The Workover Rig Routing Problem (WRRP) arises on onshore oil fields that can have a large number of wells spread over a wide region and relatively few number of the mobiles maintenance machines called workover rigs. To serve wells that demand every type of maintenance, WRRP aims to determine over the next finite horizon of time H, a feasible routes of workover rigs that minimize the sum of oil production lossRibeiro et al. (2013). WRRP states on finding the best routes of rigs in order to serve all wells, in an accepted time and the oil production loss is minimized Ribeiro et al. (2012c). For this problem, we propose a mathematical formulation model, several valid inequalities, and finally a hyperheuristic method based on a proposed tabu search metaheuristic method as a learning method. Our proposed learning has been proven its effectiveness when compared with an exact method 

**163** 

(Monemi et al., 2015), as long as the optimal solution (or the optimal interval) is known, the solutions reported by the hyper-heuristic produce very near optimal solutions. Our learning method outperforms a generic intelligent hyper-heuristic (GIHH) proposed earlier in the literature both in terms of time and quality. In addition, the proposed hyper-heuristic output has served as the initial columns for the proposed branch-and-price in Monemi et al. (2015). 

On the other hand, another logistic problem has been studied in this thesis: Hub Location Routing Problem. Hub Location Routing Problem dealing with selecting from several nodes (e.g. ports), which will be considered as hub and which will not be (spoke), then design the full network according a given rules. Many transportation operators and logistics service providers operate on hub-and-spoke structures. In this way, the long haul (in national or international scale) transport of their cargo is done by using larger transporters (with higher volume concentration) circulating between major hubs. In a short-distance level, transportation service is realized by means of smaller transporters. In this thesis, we was interested on _p_ Hub location routing problem, which fix the number of hubs as _p_ . A hyperheuristic approach has been proposed as an effective solution for a recently introduced two variant of Hub Location Routing Problems proposed by Gelareh et al. (2015) and Rodríguez-Martín et al. (2014), with two different learning methods: Association Rules and Q-learning. Furthermore, two solution acceptance criteria, for the two problems, was in the HH high level strategies: Simulated Annealing and Great Deluge. Five Lagrangian Relaxation have been proposed for the first problem, and we use the results of the best one in the process of HH. HH with Lagrangian Relax- 

**General Conclusion** 

**164** 

ation results has been proven in the numerical results as better than HH without LR results, even in the initial fitness. A part of HH results has been injected to the solver, in order to find an optimal solution for some given allocation information, as a _Matheuristic_ method. As well as the HH has been proven its effectiveness by the too minimal gap with the proposed Matheuristic. 

Finally, in order to examine how different heuristic selection mechanism can impact the performance of a hyperheuristic framework and quality of solution for a given problem, several exiting methods were studied and some new ones are proposed. Through an extensive computational experiment, we could identify some of the methods that outperform the others for the problem at hand. 

Özcan et al. (2010) categorizes such methods as the following: i) Purely Random selection, ii) Random Descent selection, iii) Random Permutation Descent selection, iv) Greedy selection, v) Peckish selection, vi) Metaheuristic-based and vii) Reinforcement Learning. Here, all these categories were implemented. Hence, we propose different reinforcement learning and metaheuristic methods such as Naive Bayes, ACO, SA, VNS, etc. that guide in selection of heuristics. these methods was examined with several solution acceptance criteria such as SA, Great Deluge, IO, etc. Association Rules method, an intelligent tools used in business data mining application, was the most effective method in selection of heuristics during HH process when combined with SA solution acceptance criteria. 

Our future directions consider solving these two problems with taking into consideration more real-world aspects such as task time window, constraints related to the environment such that related to green logistics, etc. In addition, we are very 

**165** 

interested to faced problems of Emergency Logistics (or Humanitarian Logistics), which deals with denote specific time-critical modes of transport used to move service or goods or objects rapidly in the event of an emergency. This motivation has been introduced in a our contribution Danach et al. (2015a). Furthermore, we will be more interested to develop more intelligent methods, that are proposed in artificial intelligence science such as Neural Network (NN), Decision Tree (DT), etc. in order to perform heuristic selection phase in the HH framework. Finally, developing a hybrid method that combine metaheuristic and hyperheuristic, in order to relate the heuristic to be applied to the solution state in addition to its performance, can be intervenes in our future work. 

**166 General Conclusion** 

# **Bibliography** 

- Inmaculada Rodríguez-Martín, Juan-José Salazar-González, and Hande Yaman. A branch-and-cut algorithm for the hub location and routing problem. _Computers & Operations Research_ , 50:161–174, 2014. 

- Edmund K Burke, Matthew Hyde, Graham Kendall, Gabriela Ochoa, Ender Özcan, and John R Woodward. A classification of hyperheuristic approaches. In _Handbook of metaheuristics_ , pages 449–468. Springer, 2010. 

- John R. Rice. The algorithm selection problem. _Advances in Computers_ , 15: 65–118, 1976. 

- Alexander Schrijver. Combinatorial optimization: Polyhedra and efficiency. _Discrete Applied Mathematics_ , 146:120–122, 2005. 

- Silvano Martello and Paolo Toth. _Knapsack problems: algorithms and computer implementations_ . John Wiley & Sons, Inc., 1990. 

David L Applegate, Robert E Bixby, Vasek Chvatal, and William J Cook. _The_ 

**BIBLIOGRAPHY** 

**168** 

_traveling salesman problem: a computational study_ . Princeton university press, 2011. 

- Paolo Toth and Daniele Vigo. _Vehicle routing: problems, methods, and applications_ , volume 18. Siam, 2014. 

- Zvi Drezner and Horst W Hamacher. _Facility location: applications and theory_ . Springer Science & Business Media, 2001. 

- Scott Kirkpatrick. Optimization by simulated annealing: Quantitative studies. _Journal of statistical physics_ , 34(5-6):975–986, 1984. 

- Ibrahim H Osman and Gilbert Laporte. Metaheuristics: A bibliography. _Annals of Operations research_ , 63(5):511–623, 1996. 

- El-Ghazali Talbi. _Metaheuristics: from design to implementation_ , volume 74. John Wiley & Sons, 2009. 

Emile Aarts and Jan Korst. Simulated annealing and boltzmann machines. 1988. 

- Fred Glover. Tabu search-part i. _ORSA Journal on computing_ , 1(3):190–206, 1989. 

Lawrence Davis. Handbook of genetic algorithms. 1991. 

- KG Dyall, IP Grant, CT Johnson, FA Parpia, and EP Plummer. Grasp: A generalpurpose relativistic atomic structure program. _computer physics communications_ , 55(3):425–456, 1989. 

**BIBLIOGRAPHY** 

**169** 

- Nenad Mladenovi´c and Pierre Hansen. Variable neighborhood search. _Computers & Operations Research_ , 24(11):1097–1100, 1997a. 

- Ravindra K Ahuja, James B Orlin, and Dushyant Sharma. Very large-scale neighborhood search. _International Transactions in Operational Research_ , 7(4-5): 301–317, 2000. 

- Fred Glover. A template for scatter search and path relinking. _Lecture notes in computer science_ , 1363:13–54, 1998. 

- Russ C Eberhart, James Kennedy, et al. A new optimizer using particle swarm theory. In _Proceedings of the sixth international symposium on micro machine and human science_ , volume 1, pages 39–43. New York, NY, 1995. 

- Marco Dorigo, Eric Bonabeau, and Guy Theraulaz. Ant algorithms and stigmergy. _Future Generation Computer Systems_ , 16(8):851–871, 2000. 

- Enrico Bartolini and Aristide Mingozzi. Algorithms for the non-bifurcated network design problem. _Journal of Heuristics_ , 15(3):259–281, 2009. 

- Jörg Denzinger, Marc Fuchs, and Matthias Fuchs. _High performance ATP systems by combining several AI methods_ . Citeseer, 1996. 

- Peter Cowling, Graham Kendall, and Eric Soubeiga. A hyperheuristic approach to scheduling a sales summit. In _Practice and Theory of Automated Timetabling III_ , pages 176–190. Springer, 2001. 

**BIBLIOGRAPHY** 

**170** 

- Wallace B Crowston, Fred Glover, Jack D Trawick, et al. Probabilistic and parametric learning combinations of local job shop scheduling rules. Technical report, DTIC Document, 1963. 

- Hsiao-Lan Fang, Peter Ross, and David Corne. _A promising genetic algorithm approach to job-shop scheduling, rescheduling, and open-shop scheduling problems_ . University of Edinburgh, Department of Artificial Intelligence, 1993. 

- E. Özcan, M. Misir, G. Ochoa, and E. K. Burke. A reinforcement learning-greatdeluge hyper-heuristic for examination timetabling. _International Journal of Applied Metaheuristic Computing (IJAMC)_ , 1(1):39–59, 2010. 

- Haluk Rahmi Topcuoglu, Abdulvahid Ucar, and Lokman Altin. A hyper-heuristic based framework for dynamic optimization problems. _Applied Soft Computing_ , 19:236–251, 2014. 

- Gabriela Ochoa, Rong Qu, and Edmund K Burke. Analyzing the landscape of a graph based hyper-heuristic for timetabling problems. In _Proceedings of the 11th Annual conference on Genetic and evolutionary computation_ , pages 341–348. ACM, 2009. 

- Peter Ross. _Search Methodolgies_ , chapter Hyper-heuristics, pages 529–556. 2005. 

- Edmund K Burke, Matthew Hyde, Graham Kendall, Gabriela Ochoa, Ender Ozcan, and Rong Qu. A survey of hyper-heuristics. _Computer Science Technical Report No. NOTTCS-TR-SUB-0906241418-2747, School of Computer Science and Information Technology, University of Nottingham_ , 2009a. 

**BIBLIOGRAPHY** 

**171** 

- Mohamed Bader-El-Den and Riccardo Poli. Generating sat local-search heuristics using a gp hyper-heuristic framework. In _Artificial evolution_ , pages 37–49. Springer, 2008. 

- Eric Soubeiga. _Development and application of hyperheuristics to personnel scheduling_ . PhD thesis, University of Nottingham, 2003. 

- Konstantin Chakhlevitch and Peter Cowling. Hyperheuristics: recent developments. In _Adaptive and multilevel metaheuristics_ , pages 3–29. Springer, 2008a. 

- Peter Cowling, Graham Kendall, and Eric Soubeiga. Hyperheuristics: A tool for rapid prototyping in scheduling and optimisation. In _Applications of Evolutionary Computing_ , pages 1–10. Springer, 2002a. 

- Alexander Nareyek. Choosing search heuristics by non-stationary reinforcement learning. In _Metaheuristics: Computer decision-making_ , pages 523–544. Springer, 2004. 

- Masri Ayob and Graham Kendall. A monte carlo hyper-heuristic to optimise component placement sequencing for multi head placement machine. In _Proceedings of the international conference on intelligent technologies, InTech_ , volume 3, pages 132–141. Citeseer, 2003a. 

- Ruibin Bai and Graham Kendall. An investigation of automated planograms using a simulated annealing based hyper-heuristic. In _Metaheuristics: Progress as Real Problem Solvers_ , pages 87–108. Springer, 2005. 

**BIBLIOGRAPHY** 

**172** 

- Gunter Dueck. New optimization heuristics: the great deluge algorithm and the record-to-record travel. _Journal of Computational physics_ , 104(1):86–92, 1993. 

- Edmund K Burke and Yuri Bykov. A late acceptance strategy in hill-climbing for exam timetabling problems. In _PATAT 2008 Conference, Montreal, Canada_ , 2008. 

- Masri Ayob and Graham Kendall. A monte carlo hyper-heuristic to optimise component placement sequencing for multi head placement machine. In _Proceedings of the international conference on intelligent technologies, InTech_ , volume 3, pages 132–141, 2003b. 

- Aris Anagnostopoulos, Laurent Michel, Pascal Van Hentenryck, and Yannis Vergados. A simulated annealing approach to the traveling tournament problem. _Journal of Scheduling_ , 9(2):177–193, 2006. 

- Ruibin Bai, Jacek Blazewicz, Edmund K Burke, Graham Kendall, and Barry McCollum. A simulated annealing hyper-heuristic methodology for flexible decision support. _School of CSiT, University of Nottingham, UK, Tech. Rep_ , 2007. 

- Burak Bilgin, Ender Özcan, and Emin Erkan Korkmaz. An experimental study on hyper-heuristics and exam timetabling. In _Practice and Theory of Automated Timetabling VI_ , pages 394–412. Springer, 2007. 

- Graham Kendall and Mazlan Mohamad. Channel assignment in cellular communication using a great deluge hyperheuristic. In _Networks, 2004.(ICON 2004)._ 

**BIBLIOGRAPHY** 

**173** 

_Proceedings. 12th IEEE International Conference on_ , volume 2, pages 769–773. IEEE, 2004. 

- Paul Mcmullan. An extended implementation of the great deluge algorithm for course timetabling. In _Computational Science–ICCS 2007_ , pages 538–545. Springer, 2007. 

- Ei Shwe Sin and Nang Saing Moon Kham. Hyper heuristic based on great deluge and its variants for exam timetabling problem. _arXiv preprint arXiv:1202.1891_ , 2012. 

- Ender Özcan, Yuri Bykov, Murat Birben, and Edmund K Burke. Examination timetabling using late acceptance hyper-heuristics. In _Evolutionary Computation, 2009. CEC’09. IEEE Congress on_ , pages 997–1004. IEEE, 2009. 

- Edmund K Burke, Graham Kendall, Mustafa Mısır, and Ender Özcan. A study of simulated annealing hyper-heuristics. In _Proceedings of the international conference on the practice and theory of automated timetabling (PATAT 2008)_ , 2008a. 

- R Raghavjee and N Pillay. A genetic algorithm selection perturbative hyperheuristic for solving the school timetabling problem. _ORiON_ , 31(1):39–60, 2015. 

- Alena Shmygelska and Holger H Hoos. An ant colony optimisation algorithm for the 2d and 3d hydrophobic polar protein folding problem. _BMC bioinformatics_ , 6(1):1, 2005. 

**BIBLIOGRAPHY** 

**174** 

- SM GiriRajkumar, K Ramkumar, and Sanjay Sarma O V. Real time application of ants colony optimization. _International Journal of Computer Applications_ , 3(8), 2010. 

- Leena N Ahmed, Ender Özcan, and Ahmed Kheiri. Solving high school timetabling problems worldwide using selection hyperheuristics. _Expert Systems with Applications_ , 42(13):5463–5471, 2015. 

- Yu-Jun Zheng, Min-Xia Zhang, Hai-Feng Ling, and Sheng-Yong Chen. Emergency railway transportation planning using a hyperheuristic approach. _Intelligent Transportation Systems, IEEE Transactions on_ , 16(1):321–329, 2015. 

- Rajni Aron, Inderveer Chana, and Ajith Abraham. A hyperheuristic approach for resource provisioning-based scheduling in grid environment. _The Journal of Supercomputing_ , 71(4):1427–1450, 2015. 

- Kassem Danach, Jomana Al-Haj Hassan, Wissam Khalil, and Shahin Gelareh. Routing heterogeneous mobile hospital with different patients priorities: Hyperheuristic approach. In _Digital Information and Communication Technology and its Applications (DICTAP), 2015 Fifth International Conference on_ , pages 155–158. IEEE, 2015a. 

- Kassem Danach, Wissam Khalil, and Shahin Gelareh. Multiple strings planing problem in maritime service network: Hyperheuristic approach. In _Technological Advances in Electrical, Electronics and Computer Engineering (TAEECE), 2015 Third International Conference on_ , pages 85–88. IEEE, 2015b. 

**BIBLIOGRAPHY** 

**175** 

- Rahimeh Neamatian Monemi, Kassem Danach, Wissam Khalil, Shahin Gelareh, Francisco C Lima, and Dario José Aloise. Solution methods for scheduling of heterogeneous parallel machines applied to the workover rig problem. _Expert Systems with Applications_ , 42(9):4493–4505, 2015. 

- Richard J Marshall, Mark Johnston, and Mengjie Zhang. Developing a hyperheuristic using grammatical evolution and the capacitated vehicle routing problem. In _Simulated Evolution and Learning_ , pages 668–679. Springer, 2014. 

- Pablo Garrido and María Cristina Riff. Dvrp: a hard dynamic combinatorial optimisation problem tackled by an evolutionary hyperheuristic. _Journal of Heuristics_ , 16(6):795–834, 2010. 

- Pablo Garrido and Carlos Castro. A flexible and adaptive hyperheuristic approach for (dynamic) capacitated vehicle routing problems. _Fundamenta Informaticae_ , 119(1):29–60, 2012. 

- Kevin Sim, Emma Hart, and Ben Paechter. A lifelong learning hyperheuristic method for bin packing. _Evolutionary computation_ , 23(1):37–67, 2015. 

- Muhammed Beyaz, Tansel Dokeroglu, and Ahmet Cosar. Robust hyperheuristic algorithms for the offline oriented/non-oriented 2d bin packing problems. _Applied Soft Computing_ , 36:236–245, 2015. 

- Peter Ross, Sonia Schulenburg, Javier G Marín-Blázquez, and Emma Hart. Hyperheuristics: learning to combine simple heuristics in bin-packing problems. In _GECCO_ , pages 942–948, 2002. 

**BIBLIOGRAPHY** 

**176** 

- Ali Keles, Yayimli, et al. Ant based hyper heuristic for physical impairment aware routing and wavelength assignment. In _Sarnoff Symposium, 2010 IEEE_ , pages 1–5. IEEE, 2010. 

- Carlos Segura, Gara Miranda, and Coromoto León. Parallel hyperheuristics for the frequency assignment problem. _Memetic Computing_ , 3(1):33–49, 2011. 

- Hugo Terashima-Marín, José Carlos Ortiz-Bayliss, Peter Ross, and Manuel Valenzuela-Rendón. Hyper-heuristics for the dynamic variable ordering in constraint satisfaction problems. In _Proceedings of the 10th annual conference on Genetic and evolutionary computation_ , pages 571–578. ACM, 2008. 

- José Carlos Ortiz-Bayliss, Ender Özcan, Andrew J Parkes, and Hugo TerashimaMarín. Mapping the performance of heuristics for constraint satisfaction. In _Evolutionary Computation (CEC), 2010 IEEE Congress on_ , pages 1–8. IEEE, 2010. 

- Konstantin Chakhlevitch and Peter Cowling. Hyperheuristics: recent developments. In _Adaptive and multilevel metaheuristics_ , pages 3–29. Springer, 2008b. 

- Graham Kendall, Peter Cowling, and Eric Soubeiga. Choice function and random hyperheuristics. In _Proceedings of the fourth Asia-Pacific conference on simulated evolution and learning, SEAL_ , pages 667–671, 2002a. 

- Edmund K Burke, Graham Kendall, and Eric Soubeiga. A tabu-search hyperheuristic for timetabling and rostering. _Journal of Heuristics_ , 9(6):451–470, 2003. 

**BIBLIOGRAPHY** 

**177** 

- Edmund K Burke, Bart L MacCarthy, Sanja Petrovic, and Rong Qu. Knowledge discovery in a hyper-heuristic for course timetabling using case-based reasoning. In _Practice and Theory of Automated Timetabling IV_ , pages 276–287. Springer, 2002. 

- Edmund K Burke, Sanja Petrovic, and Rong Qu. Case-based heuristic selection for timetabling problems. _Journal of Scheduling_ , 9(2):115–132, 2006. 

- Sanja Petrovic and Rong Qu. Case-based reasoning as a heuristic selector in a hyper-heuristic for course timetabling problems. 2002. 

- Hugo Terashima-Marín, EJ Flores-Alvarez, and Peter Ross. Hyper-heuristics and classifier systems for solving 2d-regular cutting stock problems. In _Proceedings of the 7th annual conference on Genetic and evolutionary computation_ , pages 637–643. ACM, 2005a. 

- Hugo Terashima-Marín, Armando Morán-Saavedra, and Peter Ross. Forming hyper-heuristics with gas when solving 2d-regular cutting stock problems. In _Evolutionary Computation, 2005. The 2005 IEEE Congress on_ , volume 2, pages 1104–1110. IEEE, 2005b. 

- Stewart W Wilson, SW Wilson, Generalization Xcs, et al. Generalization in the xcs classifier system. 1998. 

- Sonia Schulenburg, Peter Ross, Javier G Marín-Blázquez, and Emma Hart. A hyperheuristic approach to single and multiple step environments in bin-packing prob- 

**BIBLIOGRAPHY** 

**178** 

lems. In _5th International Workshop on Learning Classifier Systems (IWLCS)_ , pages 7–8, 2002. 

- Peter Cowling, Graham Kendall, and Eric Soubeiga. Hyperheuristics: A robust optimisation method applied to nurse scheduling. In _Parallel Problem Solving from Nature-PPSN VII_ , pages 851–860. Springer, 2002b. 

- Peter Cowling, Graham Kendall, and Limin Han. An investigation of a hyperheuristic genetic algorithm applied to a trainer scheduling problem. In _Evolutionary Computation, 2002. CEC’02. Proceedings of the 2002 Congress on_ , volume 2, pages 1185–1190. IEEE, 2002c. 

- EK Burke and JP Newall. A new adaptive heuristic framework for examination timetabling problems. _University of Nottingham, Working Group on Automated Timetabling, TR-2002-1 http://www. cs. nott. ac. uk/TR-cgi/TR. cgi_ , pages 2002– 1, 2002. 

- Jerry Swan, John Drake, Ender Özcan, James Goulding, and John Woodward. A comparison of acceptance criteria for the daily car-pooling problem. In _Computer and Information Sciences III_ , pages 477–483. Springer, 2013. 

- Patricia Ryser-Welch and Julian F Miller. A review of hyper-heuristic frameworks. In _Proceedings of the 50th anniversary convention of the AISB, 1–4 April 2014, London_ , 2014. 

- Eugene Nudelman, Kevin Leyton-Brown, Alex Devkar, Yoav Shoham, and Hol- 

**BIBLIOGRAPHY** 

**179** 

ger Hoos. Satzilla: An algorithm portfolio for sat. _Solver description, SAT competition_ , 2004, 2004. 

- Horst Samulowitz, Chandra Reddy, Ashish Sabharwal, and Meinolf Sellmann. Snappy: A simple algorithm portfolio. In _Theory and Applications of Satisfiability Testing–SAT 2013_ , pages 422–428. Springer, 2013. 

- Edmund K Burke, Tim Curtois, Matthew Hyde, Graham Kendall, Gabriela Ochoa, Sanja Petrovic, and José Antonio Vázquez-Rodríguez. Hyflex: A flexible framework for the design and analysis of hyper-heuristics. In _Multidisciplinary International Scheduling Conference (MISTA 2009), Dublin, Ireland_ , pages 790–797, 2009b. 

- Willem Van Onsem and Bart Demoen. Parhyflex: A framework for parallel hyperheuristics. In _BNAIC 2013: Proceedings of the 25th Benelux Conference on Artificial Intelligence, Delft, The Netherlands, November 7-8, 2013_ . Delft University of Technology (TU Delft); under the auspices of the Benelux Association for Artificial Intelligence (BNVKI) and the Dutch Research School for Information and Knowledge Systems (SIKS), 2013. 

- Mustafa Misir. Intelligent hyper-heuristics: a tool for solving generic optimisation problems. _status: published_ , 2012. 

- Thompson G.L. Muth J.F. Industrial scheduling. _Prentice Hall_ , pages 225–251, 1963. 

**BIBLIOGRAPHY** 

**180** 

- Jacques Carlier and Eric Pinson. An algorithm for solving the job-shop problem. _Management science_ , 35(2):164–176, 1989. 

- Wayne E Smith. Various optimizers for single-stage production. _Naval Research Logistics Quarterly_ , 3(1-2):59–66, 1956. 

- J. W. Barnes, J. J. Brennan, and R. M. Knap. Scheduling a backlog of oil well workovers. _Journal of Petroleum Technology_ , 29(12):1651â A¸S1653, 1977.<sup>˘</sup> 

- TF Noronha, FCJ Lima, and DJ Aloise. Um algoritmo heurístico guloso aplicado ao problema do gerenciamento das intervenções em poços petrolíferos por sondas de produção terrestre. In _Proceedings of the XXXIII Brazilian Symposium on Operations Research, Campos do Jordão_ , page 135, 2001. 

- Dario J. Aloise, Daniel Aloise, Caroline T.M. Rocha, Celso C. Ribeiro, JosÃl’ C. Ribeiro Filho, and Luiz S.S. Moura. Scheduling workover rigs for onshore oil production. _Discrete Applied Mathematics_ , 154(5):695 – 702, 2006. 

- Glaydston Mattos Ribeiro, Geraldo Regis Mauri, and Luiz Antonio Nogueira Lorena. A simple and robust simulated annealing algorithm for scheduling workover rigs on onshore oil fields. _Computers & Industrial Engineering_ , 60(4):519–526, 2011. 

- Christophe Duhamel, Andréa Cynthia Santos, and Lucas Moreira Guedes. Models and hybrid methods for the onshore wells maintenance problem. _Computers & Operations Research_ , 39(12):2944–2953, 2012. 

**BIBLIOGRAPHY** 

**181** 

- Glaydston Mattos Ribeiro, Gilbert Laporte, and Geraldo Regis Mauri. A comparison of three metaheuristics for the workover rig routing problem. _European Journal of Operational Research_ , 220(1):28–36, 2012a. 

- Glaydston Mattos Ribeiro, Guy Desaulniers, and Jacques Desrosiers. A branchprice-and-cut algorithm for the workover rig routing problem. _Computers & Operations Research_ , 39(12):3305–3315, 2012. 

- Glaydston Mattos Ribeiro, Guy Desaulniers, and Jacques Desrosiers. A branchprice-and-cut algorithm for the workover rig routing problem. _Computers & Operations Research_ , 39(12):3305 – 3315, 2012b. ISSN 0305-0548. doi: http://dx.doi.org/10.1016/j.cor.2012.04.010. 

- Glaydston Mattos Ribeiro, Guy Desaulniers, Jacques Desrosiers, Thibaut Vidal, and Bruno Salezze Vieira. Efficient heuristics for the workover rig routing problem with a heterogeneous fleet and a finite horizon. _Journal of Heuristics_ , 20(6):677–708, dec 2014. doi: 10.1007/s10732-014-9262-1. 

- Artur Pessoa, Eduardo Uchoa, Marcus Poggi de Aragão, and Rosiane Rodrigues. Exact algorithm over an arc-time-indexed formulation for parallel machine scheduling problems. _Mathematical Programming Computation_ , 2(3-4):259– 290, 2010. 

- Edmund K Burke, Mustafa Misir, Gabriela Ochoa, and Ender Ozcan. Learning heuristic selection in hyper-heuristics for examination timetabling. In _Pro-_ 

**BIBLIOGRAPHY** 

**182** 

_ceedings of 7th International Conference of Practice and Theory of Automated Timetabling (PATAT08), Montreal, Canada_ , 2008b. 

- Edmund K Burke, Michel Gendreau, Matthew Hyde, Graham Kendall, Gabriela Ochoa, Ender Özcan, and Rong Qu. Hyper-heuristics: A survey of the state of the art. _Journal of the Operational Research Society_ , 64(12):1695–1724, 2013. 

- Sibel Alumur and Bahar Y. Kara. Network hub location problems: The state of the art. _European Journal of Operational Research_ , 190(1):1–21, 2008. 

- Shahin Gelareh, Rahimeh Neamatian Monemic, and Frédéric Semet. Capacitated bounded cardinality hub routing problem: Model and solution algorithm. Technical report, 2015. 

- J. Ebery, M. Krishnamoorthy, A. Ernst, and N. Boland. The capacitated multiple allocation hub location problem: Formulations and algorithms. _European Journal of Operational Research_ , 120:614–631, 2000. 

- Isabel Correia, Stefan Nickel, and Francisco Saldanha-da Gama. _Single-allocation hub location problems with capacity choices_ . Fraunhofer-Institut für Techno-und Wirtschaftsmathematik, Fraunhofer (ITWM), 2009. 

- A. Campbell, T. Lowe, and L. Zhang. The p-hub center allocation problem. _European Journal of Operational Research_ , 176 (2):819–835, 2007. 

- Juanjo Peiró, Ángel Corberán, and Rafael Martí. Grasp for the uncapacitated _r_ -allocation _p_ -hub median problem. _Computers & Operations Research_ , 43: 50–60, 2014. 

**BIBLIOGRAPHY** 

**183** 

- Dongdong Ge, Yinyu Ye, and Jiawei Zhang. The fixed-hub single allocation problem: a geometric rounding approach. _Preprint available at http://www. stanford. edu/˜ yyye/revisedHub. pdf_ , 2007. 

- Shahin Gelareh, Nelson Maculan, Philippe Mahey, and Rahimeh Neamatian Monemi. Hub-and-spoke network design and fleet deployment for string planning of liner shipping. _Applied Mathematical Modelling_ , 37(5):3307–3321, 2013a. 

- Jozef Kratica, Zorica Stanimirovi´c, Dušan Toši´c, and Vladimir Filipovi´c. Genetic algorithm for solving uncapacitated multiple allocation hub location problem. _Computing and Informatics_ , 24(4):415–426, 2012. 

- Masoud Rabbani and S Kazemi. Solving uncapacitated multiple allocation p-hub center problem by dijkstraŠs algorithm-based genetic algorithm and simulated annealing. _International Journal of Industrial Engineering Computations_ , 6(3): 405–418, 2015. 

- Zorica Stanimirovic. An efficient genetic algorithm for the uncapacitated multiple allocation p-hub median problem. _Control and Cybernetics_ , 37:669–692, 2008. 

- Marcus Randall. Solution approaches for the capacitated single allocation hub location problem using ant colony optimisation. _Computational Optimization and Applications_ , 39(2):239–261, 2008. 

- Ching-Jung Ting and Chia-Ho Chen. A multiple ant colony optimization algorithm 

**BIBLIOGRAPHY** 

**184** 

for the capacitated location routing problem. _International Journal of Production Economics_ , 141(1):34–44, 2013. 

- J.G. Klincewicz. Avoiding local optima in the p-hub location problem using tabu search and grasp. _Annals of Operations Research_ , 40:283–302, 1992. 

- Erik Rolland, David A Schilling, and John R Current. An efficient tabu search procedure for the p-median problem. _European Journal of Operational Research_ , 96(2):329–342, 1997. 

- S. Abdinnour-Helm. A hybrid heuristic for the uncapacitated hub location problem. _European Journal of Operational Research_ , 106(23):489–499, 1998. 

- Dilek Tuzun and Laura I Burke. A two-phase tabu search approach to the location routing problem. _European Journal of Operational Research_ , 116(1):87–99, 1999. 

- MH Fazel Zarandi, S Davari, and SA Haddad Sisakht. An empirical comparison of simulated annealing and iterated local search for the hierarchical single allocation hub median location problem. _Scientia Iranica. Transaction E, Industrial Engineering_ , 22(3):1203, 2015. 

- F Yu Vincent, Shih-Wei Lin, Wenyih Lee, and Ching-Jung Ting. A simulated annealing heuristic for the capacitated location routing problem. _Computers & Industrial Engineering_ , 58(2):288–299, 2010. 

- Aleksandar Ili´c, Dragan Uroševi´c, Jack Brimberg, and Nenad Mladenovi´c. A general variable neighborhood search for solving the uncapacitated single allocation 

**BIBLIOGRAPHY** 

**185** 

p-hub median problem. _European Journal of Operational Research_ , 206(2): 289–300, 2010. 

- Bassem Jarboui, Houda Derbel, Saïd Hanafi, and Nenad Mladenovi´c. Variable neighborhood search for location routing. _Computers & Operations Research_ , 40(1):47–57, 2013. 

- Gábor Nagy and Said Salhi. The many-to-many location-routing problem. _Top_ , 6 (2):261–275, 1998. 

- S. Cetiner, C. Sepil, and H. Sural. Hubbing and routing in postal delivery systems. Technical report, Industrial Engineering Department, Middle East Technical University, 06532 Ankara, Turkey., 2006. 

- Ricardo Saraiva de Camargo, Gilberto de Miranda, and Arne Løkketangen. A new formulation and an exact approach for the many-to-many hub location-routing problem. _Applied Mathematical Modelling_ , 37(12):7465–7480, 2013. 

- Michael Wasner and Günther Zäpfel. An integrated multi-depot hub-location vehicle routing model for network planning of parcel service. _International Journal of Production Economics_ , 90(3):403–419, 2004. 

- Shahin Gelareh, Nelson Maculan, Philippe Mahey, and Rahimeh Neamatian Monemi. Hub-and-spoke network design and fleet deployment for string planning of liner shipping. _Applied Mathematical Modelling_ , 37(5):3307–3321, 2013b. 

**BIBLIOGRAPHY** 

**186** 

- A. M. Geoffrion. Lagrangian relaxation and its uses in integer programming. _Math. Programming Stud_ , 2:82–114, 1974. 

- A Geoffrion and R Me Bride. Lagrangean relaxation applied to capacitated facility location problems. _AIIE transactions_ , 10(1):40–47, 1978. 

- Marshall L. Fisher. The lagrangian relaxation method for solving integer programming problems. _Management Science_ , 27(1):1–18, 1981. ISSN 00251909. 

- Marshall L Fisher. The lagrangian relaxation method for solving integer programming problems. _Management science_ , 50(12_supplement):1861–1871, 2004. 

- M. Guignard. Lagrangian relaxation. _TOP_ , 11(2):151–228, 2003. 

- M. Held and R.M. Karp. The traveling-salesman problem and minimum spanning trees: Part II. _Mathematical Programming_ , 1(1):6–25, 1971. ISSN 0025-5610. 

- C. Lemarechal. An extension of Davidon methods to non differentiable problems. _Nondifferentiable Optimization_ , pages 95–109, 1975. 

- F. Barahona and R. Anbil. The volume algorithm: producing primal solutions with a subgradient method. _Mathematical Programming_ , 87(3):385–399, 2000. ISSN 0025-5610. 

- Laura Bahiense, Nelson Maculan, and Claudia A. Sagastizábal. The volume algorithm revisited: relation with bundle methods. _Math. Program._ , 94(1): 41–69, 2002. 

**BIBLIOGRAPHY** 

**187** 

- Antonio Frangioni. Solving semidefinite quadratic problems within nonsmooth optimization algorithms. Technical report, 1995. 

- Herman Aguinis, Lura E Forcum, and Harry Joo. Using market basket analysis in management research. _Journal of Management_ , page 0149206312466147, 2012. 

- Rakesh Agrawal, Tomasz Imieli´nski, and Arun Swami. Mining association rules between sets of items in large databases. In _ACM SIGMOD Record_ , volume 22, pages 207–216. ACM, 1993. 

- Christopher John Cornish Hellaby Watkins. _Learning from delayed rewards_ . PhD thesis, University of Cambridge England, 1989. 

- Christopher JCH Watkins and Peter Dayan. Q-learning. _Machine learning_ , 8(3-4): 279–292, 1992. 

- Diamantino Falcao, Ana Madureira, and Ivo Pereira. Q-learning based hyperheuristic for scheduling system self-parameterization. In _Information Systems and Technologies (CISTI), 2015 10th Iberian Conference on_ , pages 1–7. IEEE, 2015. 

- Yuanyuan Xi, Liuchen Chang, Meiqin Mao, Peng Jin, Nikos Hatziargyriou, and Haibo Xu. Q-learning algorithm based multi-agent coordinated control method for microgrids. In _Power Electronics and ECCE Asia (ICPE-ECCE Asia), 2015 9th International Conference on_ , pages 1497–1504. IEEE, 2015. 

- Justin A Boyan and Michael L Littman. Packet routing in dynamically changing 

**BIBLIOGRAPHY** 

**188** 

networks: A reinforcement learning approach. _Advances in neural information processing systems_ , pages 671–671, 1994. 

- Meijuan Gao, Jin Xu, and Jingwen Tian. Mobile robot global path planning based on improved augment ant colony algorithm. In _Genetic and Evolutionary Computing, 2008. WGEC’08. Second International Conference on_ , pages 273– 276. IEEE, 2008. 

- Marco Dorigo and LM Gambardella. Ant-q: A reinforcement learning approach to the traveling salesman problem. In _Proceedings of ML-95, Twelfth Intern. Conf. on Machine Learning_ , pages 252–260, 2014. 

- Junius Ho, Daniel W Engels, and Sanjay E Sarma. Hiq: a hierarchical q-learning algorithm to solve the reader collision problem. In _Applications and the Internet Workshops, 2006. SAINT Workshops 2006. International Symposium on_ , pages 4–pp. IEEE, 2006. 

- S Choi and Dit-Yan Yeung. Predictive q-routing: A memory-based reinforcement learning approach to adaptive tra c control. _Advances in Neural Information Processing Systems_ , 8:945–951, 1996. 

- Chris Gaskett, David Wettergreen, and Alexander Zelinsky. Q-learning in continuous state and action spaces. In _Australian Joint Conference on Artificial Intelligence_ , pages 417–428. Springer, 1999. 

- A.T. Ernst and M. Krishnamoorthy. Solution algorithms for the capacitated single 

**BIBLIOGRAPHY** 

**189** 

allocation hub location problem. _Annals of Operations Research_ , 86:141–159, 1999. 

- Morton E O’kelly. A quadratic integer program for the location of interacting hub facilities. _European Journal of Operational Research_ , 32(3):393–404, 1987. 

- Kate A Smith-Miles. Cross-disciplinary perspectives on meta-learning for algorithm selection. _ACM Computing Surveys (CSUR)_ , 41(1):6, 2008. 

- Melanie Hilario, Alexandros Kalousis, Phong Nguyen, and Adam Woznica. A data mining ontology for algorithm selection and meta-mining. In _Proceedings of the ECML/PKDD09 Workshop on 3rd generation Data Mining (SoKD-09)_ , pages 76–87, 2009. 

- Ender Özcan and Ahmed Kheiri. A hyperheuristic based on random gradient, greedy and dominance. In _Computer and Information Sciences II_ , pages 557– 563. Springer, 2012. 

- John H Drake, Ender Ozcan, and Edmund K Burke. A modified choice function hyperheuristic controlling unary and binary operators. In _Proceedings of the IEEE Congress on Evolutionary Computation (CEC 2015)_ , 2015. 

- E Burke and E Soubeiga. Scheduling nurses using a tabu-search hyperheuristic. In _Proceedings of the 1st Multidisciplinary International Conference on Scheduling: Theory and Applications (MISTA 2003), Nottingham, UK_ , pages 180–197, 2003. 

- Peter Cowling and Konstantin Chakhlevitch. Hyperheuristics for managing a large collection of low level heuristics to schedule personnel. In _Evolutionary_ 

**BIBLIOGRAPHY** 

**190** 

   - _Computation, 2003. CEC’03. The 2003 Congress on_ , volume 2, pages 1214– 1221. IEEE, 2003. 

- Peter I Cowling and Konstantin Chakhlevitch. Using a large set of low level heuristics in a hyperheuristic approach to personnel scheduling. In _Evolutionary Scheduling_ , pages 543–576. Springer, 2007. 

Edmund K Burke and Graham Kendall. _Search methodologies_ . Springer, 2005. 

- Ender Özcan, Mustafa Mısır, Gabriela Ochoa, and Edmund K Burke. A reinforcement learning: Great-deluge hyperheuristic. _Modeling, Analysis, and Applications in Metaheuristic Computing: Advancements and Trends: Advancements and Trends_ , page 34, 2012. 

- Graham Kendall, Peter Cowling, and Eric Soubeiga. Choice function and random hyperheuristics. In _Proceedings of the 4th Asia-Pacific Conference on Simulated Evolution and Learning_ , pages 667–671. Citeseer, 2002b. 

- Richard S. Sutton and Andrew G. Barto. _Introduction to Reinforcement Learning_ . MIT Press, Cambridge, MA, USA, 1st edition, 1998. ISBN 0262193981. 

Edwin T Jaynes. Bayesian methods: General background. 1986. 

- Bruno De Finetti. _Theory of Probability: A critical introductory treatment. Vol. 2_ . Wiley, 1974. 

- David Heckerman. Bayesian networks for data mining. _Data mining and knowledge discovery_ , 1(1):79–119, 1997. 

**BIBLIOGRAPHY** 

**191** 

- Efstathios Kirkos, Charalambos Spathis, and Yannis Manolopoulos. Data mining techniques for the detection of fraudulent financial statements. _Expert Systems with Applications_ , 32(4):995–1003, 2007. 

- Murat Kantarcıoglu, Jaideep Vaidya, and C Clifton. Privacy preserving naive bayes classifier for horizontally partitioned data. In _IEEE ICDM workshop on privacy preserving data mining_ , pages 3–9, 2003. 

- Iñaki Inza, Pedro Larrañaga, Ramón Etxeberria, and Basilio Sierra. Feature subset selection by bayesian network-based optimization. _Artificial intelligence_ , 123 (1):157–184, 2000. 

- Jonas Mockus. _Bayesian approach to global optimization: theory and applications_ , volume 37. Springer Science & Business Media, 2012. 

- Martin Pelikan. Bayesian optimization algorithm. In _Hierarchical Bayesian optimization algorithm_ , pages 31–48. Springer, 2005. 

- Nicholas Metropolis, Arianna W Rosenbluth, Marshall N Rosenbluth, Augusta H Teller, and Edward Teller. Equation of state calculations by fast computing machines. _The journal of chemical physics_ , 21(6):1087–1092, 1953. 

- Shu-Mei Ma, Yun Sun, and Ai-Ping Li. A simulated annealing algorithm for multiobjective hybrid flow shop scheduling work partially supported by national major science and technology of high-grade cnc machine tools and basic manufacturing equipment special project of china under grant no. 2013zx04012-071. 2016. 

**BIBLIOGRAPHY** 

**192** 

- KLEIN Bouleimen and HOUSNI Lecocq. A new efficient simulated annealing algorithm for the resource-constrained project scheduling problem and its multiple mode version. _European Journal of Operational Research_ , 149(2):268–281, 2003. 

- EB Schlünz and JH Van Vuuren. An investigation into the effectiveness of simulated annealing as a solution approach for the generator maintenance scheduling problem. _International Journal of Electrical Power & Energy Systems_ , 53: 166–174, 2013. 

- Samaneh Sedehzadeh, Reza Tavakkoli-Moghaddam, Mehrdad Mohammadi, and Fariborz Jolai. Solving a new priority m/m/c queue model for a multi-mode hub covering location problem by multi-objective parallel simulated annealing. _Economic Computation and Economic Cybernetics studies and Research_ , 48(4): 299–318, 2014. 

- F Parvaresh, SA Hashemi Golpayegany, SM Moattar Husseini, and B Karimi. Solving the p-hub median problem under intentional disruptions using simulated annealing. _Networks and Spatial Economics_ , 13(4):445–470, 2013. 

- EH Grosse, CH Glock, and R Ballester-Ripoll. A simulated annealing approach for the joint order batching and order picker routing problem with weight restrictions. Technical report, Darmstadt Technical University, Department of Business Administration, Economics and Law, Institute for Business Studies (BWL), 2014. 

**BIBLIOGRAPHY** 

**193** 

- RaúL BañOs, Julio Ortega, Consolación Gil, Antonio FernáNdez, and Francisco De Toro. A simulated annealing-based parallel multi-objective approach to vehicle routing problems with time windows. _Expert Systems with Applications_ , 40(5):1696–1707, 2013. 

- F Yu Vincent and Shih-Wei Lin. Multi-start simulated annealing heuristic for the location routing problem with simultaneous pickup and delivery. _Applied Soft Computing_ , 24:284–290, 2014. 

- Glaydston Mattos Ribeiro, Geraldo Regis Mauri, and Luiz Antonio Nogueira Lorena. A simple and robust simulated annealing algorithm for scheduling workover rigs on onshore oil fields. _Computers & Industrial Engineering_ , 60(4): 519–526, 2011. 

- RO Paiva et al. Optimizing the itinerary of workover rigs. In _16th World petroleum congress_ . World Petroleum Congress, 2000. 

- Kathryn A Dowsland, Eric Soubeiga, and Edmund Burke. A simulated annealing based hyperheuristic for determining shipper sizes for storage and transportation. _European Journal of Operational Research_ , 179(3):759–774, 2007. 

- Ruibin Bai, Jacek Blazewicz, Edmund K Burke, Graham Kendall, and Barry McCollum. A simulated annealing hyper-heuristic methodology for flexible decision support. _4OR_ , 10(1):43–66, 2012. 

- Konstantinos P Anagnostopoulos and Georgios K Koulinas. A simulated annealing 

**BIBLIOGRAPHY** 

**194** 

hyperheuristic for construction resource levelling. _Construction Management and Economics_ , 28(2):163–175, 2010. 

- J Chávez, J Escobar, and M Echeverri. A multi-objective pareto ant colony algorithm for the multi-depot vehicle routing problem with backhauls. _International Journal of Industrial Engineering Computations_ , 7(1):35–48, 2016. 

- Yuvraj Gajpal and Prakash Abad. An ant colony system (acs) for vehicle routing problem with simultaneous delivery and pickup. _Computers & Operations Research_ , 36(12):3215–3223, 2009. 

- KA Dowsland and JM Thompson. Ant colony optimization for the examination scheduling problem. _Journal of the Operational Research Society_ , 56(4):426– 438, 2005. 

- Masri Ayob and Ghaith Jaradat. Hybrid ant colony systems for course timetabling problems. In _Data Mining and Optimization, 2009. DMO’09. 2nd Conference on_ , pages 120–126. IEEE, 2009. 

- Berna Kiraz, A ¸Sima Etaner-Uyar, and Ender Özcan. _An ant-based selection hyper-heuristic for dynamic environments_ . Springer, 2013. 

- Alexandre Silvestre Ferreira, POZO Aurora, and Richard Aderbal Gonçalves. An ant colony based hyper-heuristic approach for the set covering problem. _ADCAIJ: Advances in Distributed Computing and Artificial Intelligence Journal_ , 4(1): 1–21, 2015. 

**BIBLIOGRAPHY** 

**195** 

- Nenad Mladenovi´c and Pierre Hansen. Variable neighborhood search. _Computers_ 

   - _& Operations Research_ , 24(11):1097–1100, 1997b. 

- Ping-Che Hsiao, Tsung-Che Chiang, and Li-Chen Fu. A vns-based hyper-heuristic with adaptive computational budget of local search. In _Evolutionary Computation (CEC), 2012 IEEE Congress on_ , pages 1–8. IEEE, 2012. 

- Pierre Hansen and Nenad Mladenovi´c. _Variable neighborhood search_ . Springer, 2014. 

- Stephen Remde, Peter Cowling, Keshav Dahal, and Nic Colledge. Exact/heuristic hybrids using rvns and hyperheuristics for workforce scheduling. In _Evolutionary Computation in Combinatorial Optimization_ , pages 188–197. Springer, 2007. 

- GM Ribeiro, G Desaulniers, J Desrosiers, T Vidal, and BS Vieira. Efficient heuristics for the workover rig routing problem with a heterogeneous fleet and a finite horizon. 2013. 

- Glaydston Mattos Ribeiro, Gilbert Laporte, and Geraldo Regis Mauri. A comparison of three metaheuristics for the workover rig routing problem. _European Journal of Operational Research_ , 220(1):28–36, 2012c. 

**196** 

#### **Hyperheuristics in Logistics** 

Success in using exact methods for large scale combinatorial optimization is still limited to certain problems or to specific classes of instances of problems. The alternative way is either using metaheuristics or matheuristics.In the context of combinatorial optimization, we are interested in heuristics to choose heuristics invoked to solve the addressed problem. In this thesis, we focus on hyperheuristic optimization in logistic problems. We focus on proposing a hyperheuristic framework that carries out a search in the space of heuristic algorithms and learns how to change the incumbent heuristic in a systematic way along the process.We propose HHs for two optimization problems in logistics: the workover rig scheduling problem and the hub location routing problem. Then, we compare the performances of several HHs described in the literature for the latter problem, which embed different heuristic selection methods such as a random selection, a choice function, a Q-Learning approach, and an ant colony based algorithm. The computational results prove the efficiency of HHs for the two problems in hand, and the relevance of including Lagrangian relaxation information for the second problem. 

Keywords: Metaheuristic, Heuristic, Hyperheuristic, Matheuristic, Reinforcement learning, Hub location problem, Workover rig scheduling problem, Association rules. 

##### **Hyperheuristiques pour des problèmes d’optimisation en logistique** 

Le succeès dans l’utilisation de méthodes exactes d’optimisation combinatoire pour des problèmes de grande taille est encore limité à certains problèmes ou à des classes spécifiques d’instances de problèmes. Une approche alternative consiste soit à utiliser des métaheuristiques ou des matheuristiques.Dans le contexte de l’optimisation combinatoire, nous nous intéressons des heuristiques permettant de choisir les heuristiques appliquées au problème traité. Dans cette thèse, nous nous concentrons sur l’optimisation à l’aide d’hyperheuristiques pour des problèmes logistiques. Nous proposons un cadre hyperheuristique qui effectue une recherche dans l’espace des algorithmes heuristiques et apprend comment changer l’heuristique courante de manière systématique tout au long du processus. Nous étudions plus particulièrement deux problèmes d’optimisation en logistique pour lesquels nous proposons des HHs: un problème de planification d’interventions sur des puits de forage et un problème conjoint de localisation de hubs et de routage. Ensuite, nous comparons les performances de plusieurs HH décrites dans la littérature pour le second problème abordé reposant sur différentes méthodes de sélection heuristique. Les résultats numériques prouvent l’efficacité de HHs pour les deux problèmes traités, et la pertinence d’inclure l’information venant d’une relaxation de Lagrangienne pour le deuxième problème. 

Mots-clefs: Metaheuristique, Heuristique, Hyperheuristique, Matheuristique, Apprentissage par renforcement, Problème de localisation des concentrateurs, Problème d’ordonnancement de workover, Règles d’association. 

