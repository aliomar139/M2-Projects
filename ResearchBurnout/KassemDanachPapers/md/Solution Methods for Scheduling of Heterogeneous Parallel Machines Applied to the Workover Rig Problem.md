
# Solution Methods for Scheduling of Heterogeneous Parallel Machines Applied to the Workover Rig Problem

Rahimeh Neamatian Monemi<sup>_∗_</sup> , Kassem Danach, Shahin Gelareh and Wissam Khalil _∗_ IFSTTAR, Univ. Lille Nord de France, rue Élisée Reclus 20, 59666 Villeneuve d’Ascq, Lille, France 

rahimeh.neamatian-monemi@ifsttar.fr 

We consider a parallel heterogenous machine scheduling problem arising in maintenance planning of heterogeneous wells. This problem particularly arises in the context of workover rig scheduling. The oil wells need regular maintenance to ensure an optimal level of production. After oil production being decreased at some wells, appropriate workover rigs with compatible service capacity are deployed to serve the wells at discrete locations. Every well needs a certain level of maintenance and rehabilitation services that can only be offered by compatible workover rigs. A new mixed integer linear programming model based on the arc-time-indexed formulation is proposed. Then, a heuristic selection type hyperheuristic algorithm is proposed, which is guided by a learning mechanism resulting in a clever choice of moves in the space of heuristics that are applied to solve the problem. The output is then used to warm start a branch, price and cut algorithm. Our numerical experiments are conducted on instances of a case study of Petrobras, the Brazilian National Petroleum Corporation. The computational experiments prove the efficiency of our hyper-heuristic in searching the right part of the search space using the right alternation among different heuristics and confirm the high quality of solutions obtained by our hyper-heuristic. 

**Keywords** workover rig scheduling; arc-time-index formulation; branch, price and cut; hyper-heuristics. 

## **1 Introduction** 

One of the most important natural resources of the world since late XIX century is oil. Many land (onshore) oil fields are composed of many wells, which are distributed geographically. Occasionally, failures happen on these wells, requiring an intervention inside them to return to their original condition. Such operation normally includes substituting the production equipments (cleaning) or stimulating the reservoir itself (stimulation), to name a few. Those interventions require the use of _workover rigs_ , big structures that can be dismounted, transported and mounted from one well to another, providing safety and accuracy conditions to the intervention. Renting of workover rigs come at great cost, thus having them at standby availability is expensive. This paper boards the problem of prioritizing onshore interventions using workover rigs to minimize production loss associated with the wells awaiting service. The problem in study here can be classified like a particular case of machine scheduling problem. 

In this paper, we propose a new model, which is based on an arc-time-indexed formulation inspired by the work in [ **?** ]. We also propose several classes of valid inequalities in order for tightening the MIP polytope. The model is well-designed in such a way that a particular relaxation of this model allows a decomposition of the relaxed model per rigs thus reducing the computational difficulties in resolution. A branch, price and cut is proposed that is capable of solving instances of moderate size to optimality. 

113 

**_www.SID.ir_** 


## **2 Problem Description** 

The problem is described as following: _A set of wells requiring maintenance, J_ = _{_ 1 _, . . . , n} , scattered within a geographical area._ [ _dij_ ] _|J|×|J| represents the distance in term of travel time between every ordered pair of wells_ ( _i, j_ ) _∈ J × J . A set of workover rigs (i.e. mobile maintenance heterogeneous workover rigs) are available to serve the wells upon need and there is a service capacity qr associated to each workover rig r ∈R such that q_ 1 _≤· · · ≤ q|R| . Every workover rig r can offer all the services offered by rig r_<sup>_′_</sup> _, qr_<sup>_′_</sup> _≤ qr . To every well j ∈J a required service level lj is associated and there is a smallest r_ ˆ _for which every rig r_ : _r ≥ r_ ˆ _can serve the well j . At time_ 0 _, all the rigs are at their initial locations and the production is already interrupted (or significantly deteriorated) at all the wells requiring maintenance. Duration of maintenance on well i ∈J is pi and production revenue per time unit has a monetary value of gi, i ∈J . The objective is to minimize the total lost production revenue that is to minimize the total completion time of maintenance activities._ 

## **3 Mathematical Model** 

The necessary parameters and variables are listed in tab:Params: We define _J_<sup>+</sup> = _J ∪{_ 0 _}_ . To this end, 

Table 1: Model Parameters and variables. 

Parameters: 

_J_ : the set of well to be serviced, _R_ : the set of workover rigs to service the wells, _T_ : the time horizon periods, 1 _, . . . , T_ , _pi_ : the process time of task _i_ , _dij_ : the travel distance between the location of task _i_ and the location of task _j_ , 0 : the dummy task, which is the _first_ and _last_ task on every machine. Variables: _xijrt_ : 1, if task _i_ is finished and task _j_ is started at period _t_ on machine _r_ , 0, otherwise. 

we use _workover rig (WOR)_ and _machine_ , alternatively. The _well_ and _tasks/job_ are also used alternatively. 

In our modeling approach at _t_ = 0 , every machine is processing dummy task 0 . 

114 

**_www.SID.ir_** 


#### **3.0.1 Mathematical model (WOR)** 



<!-- Start of picture text -->
min ∑ ∑ ∑ ∑ gi ( t  +  pj ) xijrt (3.1)<br>r∈R t∈T i∈J j∈J +<br>s.t.<br>∑ x 0 jr p 0+ d 0 j +  x 00 r p 0 = 1 , ∀r ∈ R, (3.2)<br>j∈J<br>|T |<br>∑ ∑ xi 0 rt  +  x 00 r p 0 = 1 , ∀r ∈ R, (3.3)<br>i∈J t = pi +1<br>|T |<br>∑ ∑ ∑ xijrt = 1 , j ∈ J, (3.4)<br>r∈R i∈J + : j̸ = i t = pi<br>|T |<br>∑ ∑ ∑ xjirt = 1 , j ∈ J, (3.5)<br>r∈R i∈J + : j̸ = i t = pj<br>xijrt ≤ ∑ xjlr t + djl + pj +  xj 0 r t + pj ,<br>l∈J<br>t + djl + pj ≤|T |<br>∀t ∈ T, r ∈ R, i ∈ J + , j ∈ J :  j̸ =  i, (3.6)<br>xijrt ∈{ 0 ,  1 } |J + |×|J + |×|T |×|R| . (3.7)<br><!-- End of picture text -->

115 

**_www.SID.ir_** 


### **3.1 Valid Inequalities** 

|∑<br>_t∈T_<br>∑<br>_j∈J_<sup>+</sup><br>∑<br>_r∈R_<br>_xijrt_ = 1_,_<br>_∀i ∈J_<sup>+</sup>|(3.8)|
|---|---|
|∑<br>_t∈T_<br>∑<br>_r∈R_<br>(_xijrt_+_xjirt_) = 1_,_<br>_i, j ∈J_|(3.9)|
|∑<br>_i,j̸_=_i∈J_<br>∑<br>_r∈R_<br>∑<br>_t∈T_<br>_xijrt_ =_|J|,_|(3.10)|
|∑<br>_i,j̸_=_i∈J_<sup>+</sup><br>∑<br>_r∈R_<br>∑<br>_t∈T_<br>_xijrt_ =_|J|_+ 2_|R|._|(3.11)|
|_|T |_<br>_|T |_||
|∑<br>_t_=_p_0<br>∑<br>_j∈|J_ <sup>+</sup>_|_<br>_xijrt ≤_<br>∑<br>_t_=_p_0<br>∑<br>_j∈|J_ <sup>+</sup>_|_<br>_xjirt,_<br>_∀r ∈R, i ∈J ,_|(3.12)|
|_|T |_||
|∑<br>_t_=_p_0<br>(_xijrt_+_xjlrt_+_xlirt_)_≤_2_,_<br>_∀r ∈R, {i, j, l}_<br>_j̸_=_i,l̸_=_i,l̸_=_j_<br>_∈J,_|(3.13)|
|∑<br>_i∈J_<sup>+</sup><br>∑<br>_j∈J_<sup>+</sup>:_j̸_=_i_<br>_xijrt ≤_1_,_<br>_∀r ∈R, t ∈{p_0_, . . . , , |T|}_|(3.14)|
|∑<br>_i∈J_<sup>+</sup><br>∑<br>_j∈J_<sup>+</sup>:_j̸_=_i_<br>_xjirt ≤_1_,_<br>_∀r ∈R, t ∈{p_0_, . . . , , |T|}_|(3.15)|
|∑<br>_j∈J_<br>∑<br>_t∈T_<br>_x_0_jrt_+_x_00_r_0 = 1_,_<br>_∀r ∈R,_|(3.16)|
|∑<br>_j∈J_<br>∑<br>_t∈T_<br>_xj_0_rt_+_x_00_r_0 = 1_,_<br>_∀r ∈R,_|(3.17)|



The aforementioned constraints are particularly useful when due to some relaxations or reduced cost updates, the pricing problem or Lagrangian subproblem objective has variables with negative cost. There, these constraints serve to avoid too many variables take 1 and will tighten the pricing problem/Lagrangian relaxation polytop. 

#### **3.1.1 variable fixing by model properties** 

#### **Lemma 3.1.** _None of the wells i ∈ J can receive service during_ [0 _,_ min _j∈J_<sup>_{p_0 +</sup><sup>_d_0</sup><sup>_j} −_1]</sup><sup>_on any machine._</sup> **Lemma 3.2.** _None of the wells i ∈ J can receive service during_ [ _T −_ min _j∈J_<sup>_{pj_+</sup><sup>_dj_0</sup><sup>_}_+1</sup><sup>_, T_]</sup><sup>_on any machine._</sup> 

Let _R_ ( _j_ ) the represent the set of all workover rigs that can serve task _j_ . The following constraint ensure the feasibility of task assignment. 



<!-- Start of picture text -->
xijrt = 0 ∀i, j ∈ J :  j̸ =  i, r ∈ / R ( i )  ∨ r ∈ / R ( j ) (3.18)<br><!-- End of picture text -->

## **4 Solution Methods and Numerical Results** 

A vast body of literature is devoted to the Dantzig-Wolfe decomposition, column generation and branch and price (an cut) algorithms [ **?** , **?** , **?** ]. The applications range from variants of routing problems to scheduling and network design and several other classes of problems. 

In our Dantzig-Wolf decomposition, we choose to keep a reformulated equivalent of (3.4) and (3.5) in the restricted master problem and move all the remaining constraints to the pricing sub-problem. This 

116 

**_www.SID.ir_** 


decomposition produces a set partitioning-like master problem and a subproblem that is separable for every single machine (rig). 

There are _|R|_ workover rigs each of which has its own list of compatible wells that can service. Thus, the subproblems _are not identical_ . 

Interested researchers are kindly invited to read [ **?** ]. 

117 

**_www.SID.ir_** 

