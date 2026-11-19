TYPE Original Research PUBLISHED 10 April 2026 DOI 10.3389/fams.2026.1742828 



###### OPEN ACCESS 

EDITED BY Mitali Sarkar, Sejong University, Republic of Korea 

REVIEWED BY 

Rekha Guchhait, Joongbu University, Republic of Korea Sanaz Khalaj Rahimi, Alzahra University, Iran Gul Freen, International Islamic University, Islamabad, Pakistan 

*CORRESPONDENCE Samir Haddad samir.haddad@balamand.edu.lb 

RECEIVED 09 November 2025 REVISED 05 March 2026 ACCEPTED 18 March 2026 PUBLISHED 10 April 2026 

# Fuzzy hyperheuristic optimization of a facilitated hub-and-spoke drone-enabled logistics network: a case study of Australia Post 

Kassem Danach<sup>1</sup> , Samir Haddad<sup>2</sup> *, Wissam Khalil<sup>3</sup> , Ziad El Balaa<sup>4</sup> and Jinane Sayah<sup>5</sup> 

1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon, 2Department of Computer Science and Mathematics, Faculty of Arts and Sciences, University of Balamand, Balamand, Lebanon,<sup>3</sup> Faculty of Economics and Business Administration, Lebanese University, Beirut, Lebanon, 4Laboratoire de Recherche en Réseaux, Informatique et Sécurité (LaRRIS) Laboratory, Computer Science Department, Lebanese University, Fanar, Lebanon,<sup>5</sup> Department of Telecom and Networks, Issam Fares Faculty of Technology, University of Balamand, Balamand, Lebanon 

###### CITATION 

Danach K, Haddad S, Khalil W, El Balaa Z and Sayah J (2026) Fuzzy hyperheuristic optimization of a facilitated hub-and-spoke drone-enabled logistics network: a case study of Australia Post. _Front. Appl. Math. Stat._ 12:1742828. doi: 10.3389/fams.2026.1742828 

###### COPYRIGHT 

© 2026 Danach, Haddad, Khalil, El Balaa and Sayah. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. 

Introduction: The rapid growth of e-commerce has increased pressure on postal logistics networks, especially in remote regions. Methods: This study proposes a fuzzy hyperheuristic genetic algorithm for optimizing a facilitated hub-and-spoke network with drone integration under uncertainty. 

Results: The proposed approach improves service robustness by 25–35% and expands drone coverage to 93.4% of remote demand, with only a modest cost increase (8–12%). 

Discussion: Results highlight the effectiveness of fuzzy optimization and adaptive hyperheuristics in designing resilient and cost-efficient postal logistics systems. 

###### KEYWORDS 

fuzzy logic, hub location problem, hyperheuristic, optimization, supply chain resilience 

## 1 Introduction 

### 1.1 Motivation 

The exponential growth of e-commerce in Australia has transformed the operational landscape of national postal and freight services. Australia Post, the country’s dominant parcel carrier, now processes millions of parcels per day, with year-on-year increases exceeding 20% in some regional corridors [1, 2]. This rapid demand escalation, combined with stringent expectations for next-day and same-day delivery, has created unprecedented pressure on the existing hub-and-spoke postal infrastructure. While metropolitan areas benefit from dense networks and short lead times, service coverage in remote and sparsely populated regions remains costly and unreliable [3]. 

Frontiers in Applied Mathematics and Statistics 

01 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

Recent advances in unmanned aerial vehicle (UAV) technology have opened new opportunities for postal networks to extend service reach and responsiveness. Drones are particularly suited for time-sensitive, low-volume deliveries to remote communities, islands, and areas with limited surface access. Integrating drones into the existing postal air and ground network, however, requires a rethinking of hub location and flow assignment strategies. Traditional network design methods—optimized for deterministic demand, single transport modes, and static routes—are inadequate for systems characterized by variable parcel volumes, uncertain service times, and dynamic regulatory conditions [4]. 

Moreover, operational uncertainty in postal logistics has grown due to weather-induced disruptions, fluctuating aircraft slot availability, and workforce variability [5]. These uncertainties can severely impact service reliability and cost performance. Hence, there is a growing need for resilient, adaptive, and datadriven network design methodologies capable of addressing uncertainty while maintaining cost efficiency and service continuity [6, 7]. 

### 1.2 Research gap 

Existing hub location and postal network optimization studies have predominantly focused on deterministic or stochastic models limited to ground or air transport [8, 9]. Most of these frameworks treat network parameters such as demand, capacity, and transit time as fixed or scenario-based, which limits their applicability under real-world uncertainty [7]. Furthermore, although drones have been extensively studied in routing and vehicle scheduling problems, they have rarely been incorporated into national-scale hub location and multi-modal postal network design. 

In the context of Australia, prior research on postal logistics has emphasized cost minimization, carbon footprint reduction, or facility allocation, often neglecting the resilience and robustness aspects required for a geographically diverse country [10]. Studies that consider uncertainty typically rely on probabilistic or scenariobased methods, which can be computationally expensive and difficult to interpret by decision-makers [6]. 

From an algorithmic standpoint, most existing works apply classical metaheuristics such as genetic algorithms (GA), simulated annealing (SA), or tabu search (TS) with fixed search operators. However, these approaches are often sensitive to parameter tuning and problem-specific landscape variations. The emerging paradigm of hyperheuristics, which autonomously selects and adapts low-level heuristics based on online performance feedback, has not yet been exploited in hub location or drone-enabled postal logistics—especially not under fuzzy, uncertainty-aware formulations [11, 12]. 

### 1.3 Contributions 

To address these gaps, this study proposes a novel fuzzy hyperheuristic optimization framework for the design of a resilient, 

drone-enabled national postal network. The main contributions are as follows: 

1. We define a facilitated three-tier network structure consisting of (i) the Cargo Air Backbone (CAB) representing major air freight corridors, (ii) Access Points (AP) representing regional postal depots or small airports, and (iii) drone spokes serving local demand clusters. This structure allows integration of conventional air logistics and drone delivery within a unified optimization model. 

2. We represent uncertainty in demand, handling capacity, and drone service reliability using fuzzy triangular numbers and evaluate service robustness through fuzzy membership functions, thereby incorporating uncertainty directly in the optimization objective rather than as an external scenario penalty. 

3. We develop a fuzzy-aware adaptive hyperheuristic genetic algorithm (FHH-GA) that dynamically selects low-level heuristics such as hub activation, reassignment, drone reallocation, and facilitation arc toggling based on their recent contribution to fitness improvement. This enables self-tuning search behavior and enhances convergence stability under uncertainty. 

4. We validate the proposed framework using realistic Australia Post data, quantifying trade-offs between total cost, service robustness, and facilitation subsidies. The results demonstrate the potential of drone-enabled postal networks to improve regional service reliability without imposing high operational or policy costs. 

### 1.4 Article structure 

The remainder of this study is organized as follows. Section 2 reviews relevant literature on hub location, drone logistics, fuzzy optimization, and hyperheuristic algorithms. Section 3 describes the operational context of Australia Post and outlines the network structure and decision variables. Section 4 presents the mathematical formulation of the facilitated hub-and-spoke model with fuzzy uncertainty. Section 5 details the proposed fuzzy hyperheuristic genetic algorithm. Section 6 reports the case study design and data sources, while Section 7 discusses experimental results and managerial insights. Finally, Section 8 summarizes conclusions and future research directions. 

## 2 Related work 

### 2.1 Hub location and hub-and-spoke networks 

Hub location problems have been extensively researched in logistics and transportation domains, focusing on optimizing network design to minimize costs while satisfying demand and capacity constraints. Classical formulations include the p p-hub median problem and capacitated hub location models [13, 14]. 

Frontiers in Applied Mathematics and Statistics 

02 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

Advances in multi-modal hub location particularly address air cargo freight networks integrating road, rail, and air segments, expanding strategic freight transport capabilities [15, 16]. Robust hub location models incorporate demand uncertainty via stochastic or fuzzy frameworks to enhance resilience under variable operating conditions common in national postal and freight services [15, 17, 18]. 

Recent studies have further explored robust optimization techniques specifically targeted at fresh agricultural products with uncertain demand, underscoring the applicability of hub location theory beyond traditional freight to perishable goods requiring expedited transport and refrigeration [18]. These developments leverage stochastic optimization to ensure reliability and service levels under fluctuating demand scenarios, enhancing the operational robustness of hub-and-spoke networks. 

### 2.2 Drone-enabled distribution networks 

Emerging research investigates the role of UAVs or drones as a disruptive last-mile delivery mode, with a primary focus on tactical vehicle routing problems such as vehicle routing with drones (VRPD) and integrated truck-drone fleet routing [19, 20]. These approaches mainly optimize trip scheduling and combined vehicle usage to reduce delivery time and operational costs. However, much of the current literature has concentrated on city-scale or regional delivery routing problems rather than on strategic network-level planning for national postal systems [21]. 

The application of drones to strategic hub location and comprehensive network design remains nascent, particularly when considering multi-modal integration and facilitation policy constraints. Recent advancements have addressed some gaps by considering location planning for unmanned aerial vehicles in challenging scenarios such as crisis management for Internet service providers [4]. These works propose sophisticated location planning techniques that support UAV deployment and network resilience during crises, extending beyond tactical routing to strategic infrastructure planning. 

In this context, multi-purpose drones enable dual-use coverage and transport applications, enhancing network flexibility and operational efficiency [22]. Studies have also examined the intricate balance between battery life, flight endurance, and operational performance in UAV delivery services through stochastic modeling, providing vital insights into efficient drone flight strategies [23]. Moreover, the integration of blockchain technologies to ensure secure interoperability in UAV networks opens new research avenues in secure drone-enabled logistics networks [24]. 

This growing body of research points to a shift from purely tactical routing models toward strategic-level frameworks necessary for national-scale postal and logistics network modernization using drone-enabled technologies. 

### 2.3 Uncertainty modeling with fuzzy logic in logistics 

Fuzzy logic offers a flexible method to model uncertainty and imprecision inherent in logistics system parameters such as demand variability, handling capacity, and service reliability [25, 26]. Triangular or trapezoidal fuzzy numbers are favored for representing uncertain demands and capacities, enabling smooth membership functions to measure service satisfaction levels rather than rigid constraints [27, 28]. This fuzzy satisfaction measure is utilized to capture robustness in service performance and to support decision-making under incomplete or subjective information [27, 29]. Applications include demand forecasting, supplier selection, and risk management within supply chains, where crisp models often fail to accommodate qualitative factors [30]. 

### 2.4 Hyperheuristics and adaptive metaheuristics 

Hyperheuristics, which operate by selecting or generating heuristics to solve computationally hard problems, have proved effective in complex combinatorial logistics and scheduling challenges [11]. Adaptive hyperheuristic frameworks dynamically adjust heuristic use based on performance metrics, improving convergence and generalization across problem instances [12]. Prior applications include vehicle routing, workforce scheduling, and multi-objective delivery optimization [31]. 

Recently, hybrid hyperheuristic approaches have been developed for specialized logistics tasks, including mobile hospital routing with heterogeneous patient priorities, demonstrating the ability of hyperheuristics to manage diverse and complex constraint sets in healthcare logistics [32]. Moreover, advances in e-commerce logistics have seen the integration of matheuristics combined with machine learning models such as random forests to enhance hub location efficiency, showcasing the potential for data-driven adaptive metaheuristics to improve strategic logistics decision-making [33]. 

To the best of our knowledge, no previous research has simultaneously addressed facilitated hub location, fuzzy robustness evaluation, and drone allocation in the context of a national postal distribution network such as Australia Post. 

## 3 Problem description 

### 3.1 Operational context: Australia Post network 

Australia Post operates one of the most extensive and geographically dispersed postal systems in the world, covering more than ten million addresses across a landmass exceeding 

Frontiers in Applied Mathematics and Statistics 

03 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

7.6 million square kilometers [34]. The network relies on a multi-modal transport structure combining road, rail, and air corridors that connect major capital cities with regional and remote communities. The core of its national distribution system is the Cargo Air Backbone (CAB), composed of major freight gateways such as Sydney (SYD), Melbourne (MEL), Brisbane (BNE), and Perth (PER), which handle inter-capital and international air parcel movements [3, 35]. 

Supporting this backbone are numerous Access Points (AP), including regional postal depots, small airports, and logistics centers located in secondary cities such as Hobart, Adelaide, Townsville, and Darwin [34]. These AP nodes act as feeders to the main hubs, consolidating regional flows and distributing inbound freight to local markets. At the periphery of the network, local communities and postcode-level delivery zones represent the drone service layer, where small UAVs or hybrid drones can provide finalleg deliveries within a radius of 20–60 km from an AP or CAB node. The geographical and demographic diversity of Australia introduces significant logistical challenges. Large distances between population centers, low freight density in remote regions, and frequent weather disruptions complicate conventional hub-and-spoke design [36]. Australia Post also carries a public service obligation to maintain delivery access for all communities, including those in remote and low-volume areas where traditional modes are uneconomical [10]. To meet these obligations, the network may require facilitation arcs—temporary or subsidized connections activated under government or corporate social responsibility programs to ensure continuity of service [37]. These arcs may 

represent short-term air links, contracted regional carriers, or drone corridors temporarily justified through policy incentives. 

The proposed model captures this operational environment by integrating the CAB, AP, and drone tiers into a unified optimization framework that accounts for uncertain demand, fuzzy service reliability, and potential facilitation mechanisms. 

### 3.2 Network tiers 

The facilitated postal network is structured into three interacting tiers, as illustrated conceptually in Figure 1. 

The first tier corresponds to the Cargo Air Backbone (CAB). This tier consists of the main air freight hubs and their connecting corridors, which together form the national backbone for long-haul parcel movement. Each CAB node can be opened as a hub with an associated fixed cost and handling capacity. The CAB arcs represent scheduled or potential air routes between these hubs, and each route is characterized by transport cost, capacity, and operational reliability. 

The second tier is formed by the Access Points (AP). These are regional nodes, such as secondary airports or postal depots, that collect, sort, and dispatch parcels to and from nearby communities. Each AP must be assigned to exactly one CAB hub, or it may itself be upgraded to hub status if economically justified. This assignment defines how regional parcel flows are aggregated and injected into the national air backbone. AP-to-CAB connections typically use short-haul domestic air movements or surface transport links. 

FIGURE 1 Three-tier facilitated postal air network with drone extensions. 

Frontiers in Applied Mathematics and Statistics 

04 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

The third tier represents the drone service regions. Within a defined endurance radius, unmanned aerial vehicles or hybrid drones provide last-mile delivery to remote or low-density postcode clusters. Each sortie originates from a designated base—either an AP or an active CAB node—and can serve one or multiple demand points. The feasibility of each drone link depends on several factors, including range, payload capacity, weather exposure, and local airspace rules. For each demand point, service satisfaction is expressed as a fuzzy membership value that reflects the likelihood that delivery will meet both time and reliability targets. 

Together, these three tiers enable hierarchical optimization of hub openings, regional assignments, and drone coverage, while allowing the model to introduce subsidized facilitation links where normal commercial operation would otherwise be uneconomical. 

robustness, the optimization favors network configurations that maintain acceptable performance even when subject to operational disturbances such as weather delays or aircraft slot restrictions. 

The third objective is to minimize the facilitation burden, defined as the total subsidy or policy support required to activate non-commercial facilitation arcs. Reducing this burden encourages economically self-sustaining network designs while quantifying the trade-off between public subsidy and network accessibility for remote regions. 

The overall model can be addressed either through a scalarized formulation—using a weighted sum of normalized objectives—or by generating a Pareto frontier of nondominated solutions. Both approaches enable decision-makers to explore trade-offs between operating cost, service reliability, and the level of policy intervention required to ensure equitable national coverage for the Australia Post logistics network. 

### 3.3 Decision variables 

The model employs the following decision variables: 

## 4 Mathematical formulation 

- yi ∈{0, 1}: 1 if node i (CAB or AP) is opened as a hub or active facility, 0 otherwise. 

- xij ∈{0, 1}: 1 if Access Point i is assigned to hub j, 0 otherwise. 

- fij ≥ 0: flow of parcel volume (tons per period) on CAB arc (i, j). 

- zik ∈{0, 1}: 1 if demand node k (drone service area) is served by base i, 0 otherwise. 

- aij ∈{0, 1}: 1 if facilitation arc (i, j) is activated under subsidy, 0 otherwise. 

- µk ∈ [0, 1]: fuzzy service satisfaction level for demand node k, representing the degree of compliance with time and reliability targets. 

These variables collectively determine the structure and performance of the entire network, from strategic hub openings to operational drone allocations. 

### 3.4 Objectives 

The design problem is formulated as a multi-objective optimization model that balances cost efficiency, service robustness, and policy feasibility. The first objective is to minimize the total logistics cost, which encompasses the fixed cost of opening hubs, transport costs along CAB and AP arcs, drone operating expenses, and handling costs at each facility. Facilitation subsidies are treated as additional cost penalties whenever policy-supported links are activated. 

The second objective seeks to maximize service robustness. Robustness is evaluated through the aggregate fuzzy satisfaction of all demand nodes, representing the probability-weighted ability of the network to meet service-level targets under uncertain demand, capacity, and reliability conditions. By emphasizing 

To formalize the multi-tiered network architecture and decision variables delineated in the preceding section, we now articulate a comprehensive mixed-integer fuzzy programming model. This mathematical framework rigorously quantifies the trade-offs between economic efficiency, service resilience, and policy intervention. The core of the formulation is the multi-objective function, presented in Equation 1, which seeks to simultaneously minimize total logistics cost, maximize aggregate service robustness, and minimize the reliance on policy-driven facilitation subsidies. A series of structural constraints (Equations 5, 6) govern the logical integrity of the hub-and-spoke topology, ensuring that each Access Point is assigned to a single, active hub. Subsequently, flow conservation and capacity feasibility are enforced through Equations 7 and 8, which model parcel movements through the Cargo Air Backbone and, critically, introduce the concept of fuzzy capacity handling at each hub. The operational specifics of the drone delivery layer are captured by Equations 9 and 10, which mandate that all demand clusters are served by a single, in-range drone base. The policy mechanism of subsidized facilitation arcs is modeled via logical constraints (11–13), linking their activation to the status of their endpoint nodes. Crucially, the model transcends deterministic formulations by embedding uncertainty directly into its core. Equations 14 and 15 define the triangular fuzzy numbers for demand, capacity, and reliability, and their corresponding membership functions, respectively, which are integral to computing the service robustness objective. This complete system of equations, spanning from (1) to (15), constitutes a computationally intractable yet precise representation of the real-world problem, providing the rigorous, uncertainty-aware search space that the proposed fuzzy hyperheuristic algorithm is designed to navigate effectively. 

Frontiers in Applied Mathematics and Statistics 

05 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

### 4.1 Sets and indices 

- I Set of candidate facility nodes (CAB + AP). H ⊂ I Subset of major air freight gateways (Cargo Air Backbone hubs). 

- A ⊂ I Subset of regional Access Points (AP) or depots. 

- K Set of demand nodes representing postcode or community-level delivery zones. 

- E Set of candidate CAB arcs (i, j) representing possible air connections. 

- R Set of feasible drone service pairs (i, k), where node i can serve demand k within drone range. 

measured in different units (AUD for costs and a unitless score for robustness), each objective is normalized prior to scalarization to ensure meaningful weight interpretation. 

For any objective Q, normalization is performed as 



<!-- Start of picture text -->
Q − Q min<br>Q norm = (1)<br>Q max − Q min  ,<br><!-- End of picture text -->

where Q<sup>min</sup> and Q<sup>max</sup> denote lower and upper bounds estimated from baseline and extreme feasible configurations. 

We use a scalarized formulation combining the three goals: 



<!-- Start of picture text -->
min Z = w1 Ctotal norm − w2 R service norm + w3 P facilitation norm (2)<br><!-- End of picture text -->

### 4.2 Parameters 

|cij|Unit transport cost (AUD/ton) on<br>CAB arc (i,j)∈E.|
|---|---|
|dij|Cost (AUD/ton) from Access Point<br>i∈Ato hubj∈H.|
|˜Di =(D<sup>L</sup><br>i <sup>, DM</sup><br>i <sup>, DU</sup><br>i <sup>)</sup>|Fuzzy triangular demand|
||(tons/period) at Access Pointi.|
|˜Cj =(C<sup>L</sup><br>j <sup>, CM</sup><br>j <sup>, CU</sup><br>j <sup>)</sup>|Fuzzy triangular handling capacity<br>(tons/period) at hubj.|
|gik|Cost (AUD/kg) of serving demand<br>nodekfrom drone basei.|
|tik|Expected drone service time<br>(minutes) for link (i,k).|
|˜pik =(p<sup>L</sup><br>ik<sup>, pM</sup><br>ik <sup>, pU</sup><br>ik<sup>)</sup>|Fuzzy reliability of meeting the<br>delivery time window on (i,k).|
|Fi|Fixed cost (AUD) to open or activate<br>nodei.|
|Sij|Required subsidy (AUD) to activate<br>facilitation arc (i,j).|
|Rmax|Maximum allowable drone range<br>(km).|
|w1,w2,w3|Weights for cost, robustness, and<br>facilitation objectives respectively<br>(for scalarization).|
|M|Large positive constant for capacity<br>or logical constraints.|



### 4.3 Decision variables 

|yi ∈{0, 1}|1 if nodeiis opened as a hub or active facility,<br>0 otherwise.|
|---|---|
|xij ∈{0, 1}|1 if APiis assigned to hubj, 0 otherwise.|
|fij ≥0|Flow quantity (tons/period) on CAB arc (i,j).|
|zik ∈{0, 1}|1 if demand nodekis served by drone basei, 0<br>otherwise.|
|aij ∈{0, 1}|1 if facilitation arc (i,j) is activated, 0<br>otherwise.|
|µk ∈[0, 1]|Fuzzy satisfaction level of demand nodek.|



### 4.4 Objective functions 

The model seeks to minimize total cost and facilitation burden while maximizing service robustness. Since these objectives are 

This normalization ensures that no objective dominates the optimization due to scale differences and allows the weights (w1, w2, w3) to reflect relative preference among the three goals. where each component is defined as follows. 

#### 4.4.1 Total logistics cost 



<!-- Start of picture text -->
Ctotal = � Fiyi + � cijfij + � � dijxijE[D ˜ i] + � gikzik.<br>i∈I (i,j)∈E i∈A j∈H (i,k)∈R<br>(3)<br><!-- End of picture text -->

#### 4.4.2 Service robustness (fuzzy satisfaction) 



<!-- Start of picture text -->
Rservice = � µk, (4)<br>k∈K<br><!-- End of picture text -->

where µk quantifies the fuzzy satisfaction degree of each demand node k being served within its reliability and time threshold. 

#### 4.4.3 Facilitation burden 



<!-- Start of picture text -->
Pfacilitation = � Sijaij. (5)<br>(i,j)∈E<br><!-- End of picture text -->

Although the optimization model uses a scalarized objective during individual evolutionary runs, Pareto-optimal trade-offs are generated by systematically varying the weight vector (w1, w2, w3) across multiple runs and maintaining an external archive of nondominated solutions. 

In addition, dominance filtering is applied to the union of solutions obtained from different weight configurations. This procedure enables the recovery of non-dominated solutions that approximate the full Pareto frontier, including regions that may not be reachable through a single fixed weight combination. 

Frontiers in Applied Mathematics and Statistics 

06 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

### 4.5 Constraints 

#### 4.5.1 Hub opening and assignment constraints 

Each Access Point (AP) must be assigned to exactly one open hub: 



<!-- Start of picture text -->
� xij = 1, ∀i ∈ A, (6)<br>j∈H<br><!-- End of picture text -->

Flow on facilitation arcs is bounded by their activation: 



<!-- Start of picture text -->
fij ≤ Maij, ∀(i, j) ∈ E. (13)<br><!-- End of picture text -->

### 4.6 Fuzzy evaluation and satisfaction membership 

Uncertainty in demand, capacity, and reliability is represented using triangular fuzzy numbers. 

and assignments are valid only if the chosen hub is open: 



<!-- Start of picture text -->
xij ≤ yj, ∀i ∈ A, j ∈ H. (7)<br><!-- End of picture text -->

#### 4.6.1 Fuzzy demand 

For each Access Point i: 

#### 4.5.2 Flow conservation and hub capacity 

Each hub operates as a transshipment node. Therefore, the total flow entering a hub together with the demand aggregated from its assigned Access Points must equal the flow leaving that hub toward other hubs. 



<!-- Start of picture text -->
� fij + � E[D ˜ i]xij = � fjk, ∀j ∈ H, (8)<br>(i,j)∈E i∈A (j,k)∈E<br><!-- End of picture text -->

This formulation allows parcels to pass through intermediate hubs before reaching their final destination. For example, a shipment from Brisbane to Melbourne, routed via Sydney, would generate flows fBNE,SYD and fSYD,MEL. 

The capacity constraint applies to the total throughput handled at each hub, defined as the total incoming flow plus the aggregated demand from assigned Access Points: 



<!-- Start of picture text -->
� fij + � E[D ˜ i]xij ≤ C ˜ j, ∀j ∈ H. (9)<br>(i,j)∈E i∈A<br><!-- End of picture text -->

Since C<sup>˜</sup> j is fuzzy, violation of Equation 9 does not render a solution infeasible; instead, the degree of satisfaction of each hub’s capacity constraint contributes to the robustness score. 

#### 4.5.3 Drone service feasibility 



<!-- Start of picture text -->
D˜ i = (D L i , DM i , DU i ), (14)<br><!-- End of picture text -->

with membership function 



<!-- Start of picture text -->
0, x ≤ D L i ,<br>µDi (x) = Dx M i − − D DL i L i , D L i < x ≤ DM i ,<br>  DD U i U i −−DxM i , D M i < x < D U i ,<br> 0, x ≥ D U i .<br><!-- End of picture text -->

#### 4.6.2 Fuzzy hub capacity 

For each hub j, capacity is modeled as a triangular fuzzy number 



<!-- Start of picture text -->
C˜ j = (Cj L, C j M, C j U ),<br><!-- End of picture text -->

where Cj<sup>L,C</sup> j<sup>M,andC</sup> j<sup>U</sup> denote the lower, most likely, and upper capacity bounds, respectively. 

The associated membership function is defined as: 



<!-- Start of picture text -->
0, x ≤ Cj L,<br>x − C L<br>j , C L<br>µCj (x) =   CCj MU− C j L j < x ≤ C j M, (15)<br>j − x<br>Cj U − C j M , Cj M < x < Cj U ,<br> 0, x ≥ Cj U .<br><!-- End of picture text -->

Each demand node must be served by exactly one eligible base: 

Let Fj denote the total throughput handled by hub j: 



<!-- Start of picture text -->
� zik = 1, ∀k ∈ K. (10)<br>i∈I<br><!-- End of picture text -->

Service is allowed only for feasible drone ranges: 



<!-- Start of picture text -->
zik = 0, if distance(i, k) > Rmax. (11)<br><!-- End of picture text -->

#### 4.5.4 Facilitation arc activation 

Facilitation arcs can only be activated if both endpoints are open: 



<!-- Start of picture text -->
aij ≤ yi, aij ≤ yj, ∀(i, j) ∈ E. (12)<br><!-- End of picture text -->



<!-- Start of picture text -->
Fj = � fij + � E[D ˜ i]xij. (16)<br>(i,j)∈E i∈A<br><!-- End of picture text -->

The degree of capacity satisfaction for hub j is computed as 



<!-- Start of picture text -->
ηj = µCj (Fj). (17)<br><!-- End of picture text -->

Thus, if the flow exceeds the modal capacity Cj<sup>M,satisfaction</sup> decreases linearly toward zero at Cj<sup>U. For example, if a hub has fuzzy</sup> capacity C<sup>˜</sup> j = (80, 100, 120) tons and the routed flow is Fj = 110, the resulting satisfaction level is 



<!-- Start of picture text -->
ηj = 120 − 110<br>120 − 100 = 0.5.<br><!-- End of picture text -->

Frontiers in Applied Mathematics and Statistics 

07 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

This formulation allows moderate capacity violations to reduce the robustness score gradually rather than making the solution infeasible. 

#### 4.6.3 Fuzzy drone reliability 

= Each drone service link (i, k) has fuzzy reliability p˜ik (p<sup>L</sup> ik<sup>, pM</sup> ik<sup>, pU</sup> ik<sup>). Let pik denote the expected reliability of the drone link</sup> and tik the expected service time from drone base i to demand node k. To capture both service reliability and delivery timeliness, two satisfaction components are defined. 

The reliability satisfaction is given by the membership function 

of the framework is the FHH-GA, which iteratively generates and refines candidate network designs. Unlike a standard GA, the FHH-GA incorporates a hyperheuristic controller that dynamically manages a set of low-level heuristics (search operators). This controller learns which operators are most effective at different stages of the search, allowing the algorithm to autonomously balance exploration (e.g., opening new hubs) and exploitation (e.g., fine-tuning drone assignments). Each candidate solution generated by the GA is then evaluated using a fuzzy fitness function, which quantifies not just the deterministic cost but also the robustness of the solution under uncertainty. The resulting fitness score guides the selection process for the next generation, completing the evolutionary cycle. 



<!-- Start of picture text -->
µ rel ik = µp ik (pik), (18)<br><!-- End of picture text -->

where µpik (·) is the triangular membership function associated with the fuzzy reliability parameter. 

Let Tk denote the target delivery time for node k. The time satisfaction is modeled as 



<!-- Start of picture text -->
1, tik ≤ Tk,<br>T k max − tik<br>µ time ik =   Tk max − Tk , Tk < tik < Tk max , (19)<br>0, tik ≥ Tk max .<br><!-- End of picture text -->

The overall service satisfaction that demand node k receives from drone base i is then computed using a product t-norm: 



<!-- Start of picture text -->
µk = zik µ rel ik µtime ik , (20)<br><!-- End of picture text -->

which ensures that both reliability and delivery time jointly determine the satisfaction level of each serviced demand node. 

#### 4.6.4 Aggregate robustness 

The system-wide robustness used in Objective Equation 2 is then: 



<!-- Start of picture text -->
Rservice = � µk + � ηj. (21)<br>k∈K j∈H<br><!-- End of picture text -->

This formulation integrates fuzzy feasibility directly into the optimization evaluation, allowing the hyperheuristic genetic algorithm to evolve network configurations that are not only costefficient but also resilient under uncertain operating conditions. 

## 5 Proposed fuzzy hyperheuristic framework 

### 5.1 Solution framework 

The framework operates as a closed-loop system, as shown in Figure 2. It begins with the fuzzy problem definition, where key parameters like demand (D<sup>˜</sup> i), hub capacity (C<sup>˜</sup> j), and drone reliability (p˜ik) are modeled as triangular fuzzy numbers. The core 

### 5.2 Chromosome representation 

The proposed solution approach employs an evolutionary search procedure in which each candidate network design is encoded as a chromosome. This chromosome jointly represents strategic facility location decisions, regional assignments, drone coverage, and facilitation activation. The representation is organized into four interrelated layers. 

The first layer, the hub activation layer (y-layer), is a binary vector **y** of length |I| indicating which nodes i ∈ I (either Cargo Air Backbone hubs or Access Points) are opened as active facilities or drone bases. These decisions determine which Australia Post terminals operate as national consolidation or regional dispatch points. 

The second layer, the Access Point assignment layer (x-layer), maps each Access Point i ∈ A to an open hub j ∈ H. This defines the regional aggregation structure of the network and drives linehaul flows entering the Cargo Air Backbone. Each assignment satisfies xij ≤ yj, ensuring that APs connect only to active hubs. 

The third layer, the drone service layer (z-layer), maps each demand node k ∈ K to its serving base i ∈ I. This layer determines last-mile coverage for remote or low-density communities. Feasibility is restricted to pairs (i, k) ∈ R within drone range Rmax, and each demand node must be served by exactly one base, i.e.,<sup>�</sup> i∈I<sup>zik= 1.</sup> 

The final layer, the facilitation layer (a-layer), is a binary structure over arcs (i, j) ∈ E with aij = 1 if a facilitation arc is activated. These arcs represent subsidized or policy-supported links extending coverage to uneconomic regions, influencing both network connectivity and the facilitation cost component. 

In implementation, the chromosome is stored as a mixed data structure consisting of: 

- binary vectors for **y** and **a** , 

- integer arrays where each AP index points to its assigned hub, 

- integer arrays where each demand node points to its drone base. 

Because the chromosome contains several interdependent decision layers, crossover or mutation operations may temporarily generate structurally inconsistent solutions (e.g., assigning an Access Point to a hub that is not activated). To address this issue, 

Frontiers in Applied Mathematics and Statistics 

08 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 2 

Conceptual framework of the proposed fuzzy hyperheuristic optimization methodology, illustrating the flow from fuzzy problem definition to the final network solution. 

a repair procedure is applied after each genetic operation to restore feasibility before fitness evaluation. 

phenotype is scored according to the fitness function described in Section 4.4. 

### 5.3 Baseline genetic algorithm 

#### 5.2.1 Repair mechanism 

The repair process enforces consistency between chromosome layers using the following rules: 

1. AP–hub consistency: if an Access Point i is assigned to a hub j with yj = 0, the AP is reassigned to the nearest open hub. 

2. Hub activation safeguard: if crossover produces a chromosome with no active hub, the geographically nearest candidate hub to the largest demand cluster is activated. 

3. Drone assignment feasibility: if a demand node k is assigned to a base outside the feasible range (i, k) ∈/ R, it is reassigned to the nearest feasible base within Rmax. 

4. Facilitation arc consistency: facilitation links must satisfy aij ≤ yi and aij ≤ yj; otherwise the corresponding arc is removed. 

During decoding, induced flows fij are reconstructed, total handling load and fuzzy capacity satisfaction are evaluated for each open hub, drone coverage is verified, and the resulting network 

A baseline genetic algorithm (GA) is used to evolve a population of network configurations through iterative selection, recombination, and mutation. The initial population is generated through a combination of constructive heuristics and randomized variants. Constructive initialization preferentially activates highcapacity CAB nodes, assigns each AP to the nearest open hub, and allocates drones to feasible nearby communities within endurance limits. Random perturbations maintain genetic diversity. 

Selection of parent chromosomes is performed using tournament selection with bias toward individuals achieving a lower total objective value Z from Equation 2, representing lower cost, higher robustness, and smaller facilitation burden. 

Crossover operates on network substructures rather than individual bits. Hub-level crossover exchanges subsets of open hubs between parents; AP-assignment crossover swaps regional assignment segments; drone coverage crossover exchanges groups of served demand nodes; and facilitation crossover swaps activated 

Frontiers in Applied Mathematics and Statistics 

09 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

subsidized arcs. This approach preserves logical network structures across generations. 

Mutation introduces controlled variation by toggling hub states, reassigning APs, reallocating drone coverage, toggling facilitation arcs, or rebalancing flows across CAB routes. To maintain feasibility, a deterministic repair procedure is applied after mutation. This repair process ensures that all assignments correspond to open hubs, drone range, and capacity constraints are respected, and facilitation arcs are consistent with active endpoints. Capacity violations are not rejected outright but penalized through reduced fuzzy satisfaction scores, reflecting operational strain rather than infeasibility. 

Each repaired chromosome is then decoded and evaluated using three components: total cost Ctotal, service robustness Rservice, and facilitation burden Pfacilitation, combined into the overall objective Z from Equation 2. Fuzzy quantities such as D<sup>˜</sup> i, C<sup>˜</sup> j, and p˜ ik are defuzzified by expected value for cost evaluation, while membership functions are used directly for robustness measures. 

An elitist survivor selection scheme retains a fraction of the best individuals across generations. Non-dominated solutions can be archived in a Pareto front when running in multi-objective mode. 

### 5.4 Adaptive hyperheuristic layer 

To enhance learning capability, the baseline GA is extended with an adaptive hyperheuristic layer that dynamically selects among low-level search operators according to their historical contribution to performance improvement. 

A set of heuristics H is defined, each corresponding to a specialized perturbation: hub activation/deactivation, AP reassignment, local drone re-optimization, facilitation toggling, and CAB flow rebalancing. The hyperheuristic maintains a score vector �, where each entry �h represents the recent effectiveness of heuristic h in improving the objective value. 

Let s denote the current solution and s<sup>′</sup> the offspring obtained after applying heuristic h. The improvement produced by h is measured as 



<!-- Start of picture text -->
�h = Z(s) − Z(s ′ ), (22)<br><!-- End of picture text -->

where Z(·) is the scalarized objective defined in Equation 2. A positive value �h > 0 indicates that the heuristic improved the solution. 

Operator scores are updated using an exponential moving average 



<!-- Start of picture text -->
� new h = (1 − α)� old h + α�h, (23)<br><!-- End of picture text -->

where α ∈ (0, 1) is a learning-rate parameter controlling the influence of recent performance. 

At each iteration, heuristic selection follows an ǫ-greedy strategy: with probability ǫ, a heuristic is chosen uniformly at random (exploration), while with probability 1 − ǫ, a heuristic is selected with probability proportional to �h (exploitation). This mechanism prevents the algorithm from prematurely converging 

to a small subset of operators that may have performed well early in the search. 

This adaptive mechanism enables the algorithm to learn search patterns suited to the evolving landscape. Early in the run, structural operators such as hub flips dominate, exploring network topology. Later, as the structure stabilizes, local operators like drone re-optimization and CAB flow rebalancing become more active, refining robustness with minimal cost increase. The adaptive policy, therefore, automates the balance between exploration and exploitation. 

The overall procedure is summarized in **Algorithm 1** . 

- 1: Initialize population _P_ 

- 2: Initialize heuristic score vector � over H 3: **while** stopping criterion not met **do** 4: Select parent solutions from _P_ 5: Apply crossover to generate offspring 6: Select heuristic _h_ ∈ H using the ǫ-greedy rule based on scores � _h_ 

- 7: Apply _h_ to offspring (hub flip, reassignment, drone optimization, facilitation toggle, or flow rebalance) 

- 8: Repair feasibility (hub status, AP assignment, drone reachability, facilitation logic) 

- 9: Decode chromosome and evaluate fuzzy fitness components _C_ total, _R_ service, _P_ facilitation 

- 10: Compute objective _Z_ in Equation (2) 11: Compute improvement � _h_ = _Z_ ( _s_ ) − _Z_ ( _s_<sup>′</sup> ) and update � _h_ 

- 12: Form next generation _P_ using elitist survivor selection 

13: **end while** 

14: **return** best non-dominated solutions 

Algorithm 1. Fuzzy hyperheuristic GA. 

### 5.5 Computational complexity discussion 

The integrated decision problem simultaneously determines hub openings, AP-to-hub assignments, inter-hub flows, drone allocations, and activation of subsidized facilitation arcs. Even simplified versions of this formulation correspond to well-known NP-hard problems such as the capacitated hub location and location-routing problems. The inclusion of fuzzy uncertainty, drone reachability, and facilitation subsidies adds non-linearity and high-dimensional coupling between decision layers. 

Exact mixed-integer formulations quickly become intractable for a national-scale instance like Australia Post, particularly when evaluating multiple fuzzy demand and reliability scenarios. The proposed fuzzy hyperheuristic GA therefore provides a practical alternative that maintains solution quality and interpretability within a reasonable runtime. By integrating fuzzy robustness evaluation and adaptive operator selection, the method yields 

Frontiers in Applied Mathematics and Statistics 

10 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 3 

Representative layout of the Australia Post air and drone network showing CAB hubs, regional access points, and drone service clusters. 

high-quality, policy-relevant solutions suitable for real-world postal air–drones logistics planning. 

## 6 Case study: Australia Post 

### 6.1 Data description 

The proposed fuzzy hyperheuristic optimization framework was evaluated using data representative of the Australia Post domestic air and parcel network. The network was modeled as a three-tier system following the structure described in Section 3 and visualized in Figure 1. 

The Cargo Air Backbone (CAB) layer includes the main air freight gateways that handle inter-capital and interstate parcel movements. The selected hubs are Sydney (SYD), Melbourne (MEL), Brisbane (BNE), Perth (PER), and Adelaide (ADL). Together, these airports represent over 85% of Australia Post’s total air parcel throughput according to the National Freight Data Hub [38]. Each CAB node is characterized by its average daily throughput (tons/day), handling cost, and reliability index based on historical weather and slot access data. 

The second tier comprises regional Access Points (APs), representing depots and small airports that aggregate or distribute parcels between local markets and CAB hubs. The case study includes twelve representative AP nodes, such as Townsville (TSV), Darwin (DRW), Hobart (HBA), Alice Springs (ASP), Launceston (LST), and Broome (BME). Distances between APs and CABs were computed using great-circle airport coordinates and converted into 

transport costs using domestic air freight rates of $1.8–$2.3 per ton-km [39]. 

The third tier corresponds to drone-served demand clusters. Each AP or active CAB node is associated with several remote delivery zones derived from postcode-level parcel data. For example, Hobart (HBA) covers the Tasman Peninsula and Bruny Island, while Alice Springs (ASP) serves Northern Territory communities. Each demand node is defined by its expected daily parcel volume and geographic coordinates, allowing feasibility checks for drone sorties within endurance limits. 

Two main cost matrices were developed: 

1. CAB–CAB matrix (cij), based on inter-capital air routes and cost coefficients (AUD/ton-km); 

2. AP–CAB matrix (dij), estimated using multi-modal truck–air cost data for regional feeders. 

Drone operational costs (gik) were approximated at AUD 2.5–3.5 per kg per 40 km flight, consistent with UAV logistics trials in regional Australia. 

Uncertainties were modeled using triangular fuzzy numbers. Fuzzy demand D<sup>˜</sup> i was defined with bounds (0.8, 1.0, 1.3)D<sup>M</sup> i<sup>,</sup> fuzzy capacity C<sup>˜</sup> j with ±10–15% deviation around nominal hub throughput, and fuzzy service reliability p˜ ik with (0.6, 0.8, 0.95) for tropical regions (e.g., BME, TSV) and (0.75, 0.9, 0.98) for temperate areas (e.g., HBA, LST). The final testbed consisted of five CAB hubs, twelve AP nodes, and sixty drone demand clusters. The structure of this network is illustrated in Figure 3, which presents a representative layout including CAB hubs, regional access points, and drone service clusters. 

Frontiers in Applied Mathematics and Statistics 

frontiersin.org 

11 

10.3389/fams.2026.1742828 

Danach et al. 

### 6.2 Parameter calibration 

Quantitative parameters were calibrated using publicly available data and operational guidelines. Domestic air freight cost coefficients were set in the range $1.8–$2.3 per ton-km, consistent with reported Australian interstate air freight tariffs (BITRE, 2023). These coefficients were multiplied by great-circle distances between major air hubs to derive CAB–CAB transport costs. AP–CAB connections incurred an additional handling surcharge of $90–$120 per ton to reflect regional transfer, linehaul consolidation, and manual sorting at intermediate depots. 

Drone operating costs and service time were derived from Wing and Swoop Aero field trials (2023). The nominal cost was $2.8 per kilogram per 40 km flight, with an endurance of 60 km. Drone mission duration tik was modeled as 

##### tik = 25 + 0.6 dik minutes, 

where dik is the one-way flight distance in kilometers. The intercept represents fixed turnaround and preparation time, while the linear term models travel duration. 

Fuzzy demand D<sup>˜</sup> i for each Access Point was constructed from regional parcel counts reported by Australia Post [40]. The most likely value D<sup>M</sup> i represents average daily parcel throughput, and the bounds (D<sup>L</sup> i<sup>, DU</sup> i<sup>)weresetat±30%tocaptureoff-peakand</sup> surge conditions. Fuzzy capacity C<sup>˜</sup> j for each CAB hub was based on BITRE throughput data, with (Cj<sup>L, C</sup> j<sup>U)setat±15%around</sup> nominal. 

Facilitation subsidies Sij were estimated for low-density corridors that are not commercially sustainable at current volumes. Routes such as PER–ASP (Perth–Alice Springs) and BNE–BME (Brisbane–Broome) required subsidy levels of $40,000–$80,000 per period, corresponding to the activation cost of low-utilization charter services and regional policy support. 

Weights for the scalarized objective in Equation 2 were set to (w1, w2, w3) = (0.5, 0.4, 0.1), emphasizing cost and robustness while modestly penalizing facilitation expenditure to discourage overreliance on subsidies. 

### 6.3 Experimental setup 

To evaluate algorithmic performance, three model configurations were tested under identical conditions: 1. Model A: Deterministic Hub GA. Conventional GA solving a deterministic capacitated hub location problem without drones or fuzzy evaluation. 

2. Model B: Deterministic Hub + Drone Post-Processing. Twostage heuristic that first selects hubs deterministically, then assigns drones greedily to remote nodes. 

3. Model C: Fuzzy Hyperheuristic GA (FHH-GA). Full integration of fuzzy uncertainty and adaptive operator selection. 

Each model was executed for 50 independent runs using identical population seeds and stopping criteria. The population = size was Np 100 with a maximum of 300 generations. Tournament selection (size 4), substructure crossover, and adaptive 

mutation rates were used. The hyperheuristic layer in Model C updated operator performance scores every ten generations based on relative improvement. 

Multi-objective trade-offs among cost, robustness, and facilitation were examined by varying the weight vector (w1, w2, w3) and compiling the resulting Pareto-optimal frontiers. All experiments were implemented in Python 3.12 (Python Software Foundation, Wilmington, Delaware, United States) and executed on a workstation with an AMD Ryzen 9 processor and 64 GB of RAM. The average runtime per optimization instance was under 10 min. 

The case study results confirm that the proposed fuzzy hyperheuristic framework efficiently scales to a realistic national postal network, producing interpretable trade-offs between operational cost, service robustness, and policy support. Figure 4 illustrates the influence of facilitation budget on network coverage and subsidy efficiency. 

## 7 Results and discussion 

### 7.1 Network design outcomes 

The fuzzy hyperheuristic GA produced a resilient and costefficient three-tier network configuration for Australia Post. The resulting design activates five Cargo Air Backbone hubs, ten regional Access Points, and provides drone coverage to fifty-seven remote or low-density communities. Table 1 reports the selected hubs, their assigned Access Points (APs), and the subsidized facilitation arcs required to sustain service in low-demand regions under the weight setting (w1, w2, w3) = (0.5, 0.4, 0.1). 

The optimized configuration preserves five major hubs (SYD, MEL, BNE, PER, and ADL), which act as national consolidation points. Perth (PER) and Brisbane (BNE) exhibit the highest reliance on subsidized facilitation arcs because they support low-density western and northern corridors. Approximately 30% of total network arcs are facilitation-enabled, indicating that a significant portion of national service equity is maintained through policysupported rather than purely commercial links. These subsidized connections primarily involve Access Points such as Broome (BME) and Alice Springs (ASP), which serve sparsely populated regions in Western Australia and the Northern Territory. 

Figure 5 visualizes the resulting spatial structure of the optimized network. The east-coast corridor linking Sydney, Melbourne, and Brisbane operates without facilitation, reflecting high and self-sustaining parcel volumes. In contrast, Western and Northern Australia depend on subsidized arcs to guarantee acceptable access levels. The figure also shows drone service regions as coverage zones around Access Points or CAB hubs, generally spanning 40–60 km. These drone coverage zones extend last-mile reach into communities that are prohibitively expensive to serve with traditional road or manned air transport. 

In addition to the structural design, the economic profile of each model configuration can be decomposed into hub fixed costs, backbone air corridor cost, AP feeder cost, drone operations, and facilitation cost. Figure 6 shows that the fuzzy hyperheuristic 

Frontiers in Applied Mathematics and Statistics 

12 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 4 

Effect of facilitation budget on service coverage and robustness improvement across the Australia Post network. 

TABLE 1 Optimized hub configuration and regional assignments (FHH-GA solution). 

|Hub (CAB/AP)|Assigned Access|Activated|
|---|---|---|
||Points (APs)|facilitation arcs|
|SYD (open)|CBR, WGA, NTL|SYD–HBA (subsidized)|
|MEL (open)|LST, HBA, ALB|MEL–LST (subsidized)|
|BNE (open)|TSV, CNS, ROK|BNE–BME (subsidized)|
|PER (open)|KGI, BME, ASP|PER–ASP (subsidized)|
|ADL (open)|MKY, DRW|–|



solution slightly increases drone and facilitation expenditure relative to the deterministic baseline, but total cost remains within a 10–12% increase while delivering substantially greater service reach. 

### 7.3 Drone coverage of remote demand 

Table 2 compares the ability of each algorithmic configuration to serve remote communities under acceptable service levels. The fuzzy hyperheuristic GA achieves 93.4% coverage with satisfaction µk ≥ 0.8, compared to 72.1% for the deterministic baseline. 

Coverage gains are most pronounced in Tasmania, northern Queensland, Western Australia, and the Northern Territory. The algorithm selectively activates AP nodes such as Hobart (HBA), Townsville (TSV), and Broome (BME) as drone bases in order to buffer against weather risk and long overland transport times. This behavior is consistent with the hyperheuristic’s shift toward localized drone re-optimization later in the search. 

These improvements are also reflected geographically in terms of service robustness. Figure 8 reports the fuzzy robustness index for a set of regional bases, comparing the deterministic GA and the fuzzy hyperheuristic GA. For remote nodes such as Alice Springs (ASP), Darwin (DRW), and Broome (BME), robustness improves from roughly 0.6–0.7 to above 0.8. 

### 7.2 Cost vs. robustness trade-offs 

Figure 7 presents the Pareto frontier obtained by varying the objective weights in Equation 2. Each point is a non-dominated network configuration that balances total logistics cost against the fuzzy robustness index µ¯ . The frontier exhibits a concave structure: increasing robustness from 0.72 to 0.90 requires roughly an 11% increase in total logistics cost. The benefit of this additional cost is concentrated in regions subject to weather-induced and slotinduced unreliability. 

Compared to the deterministic GA (Model A), the proposed fuzzy hyperheuristic GA (Model C) improves robustness by 25– 35% at a marginal cost increase of only 8–12%. This supports the use of fuzzy satisfaction as an explicit objective rather than treating service reliability as a post-hoc stress test. 

### 7.4 Effect of facilitation budget 

Figure 9 quantifies how increasing the facilitation budget affects equitable access. Without facilitation funding, only 68% of remote locations achieve the target service satisfaction threshold (µk ≥ 0.8), because several low-density corridors are not commercially viable. Allocating a moderate budget of 100,000 AUD activates key subsidized links such as PER–ASP and BNE–BME, raising highquality coverage to nearly 85%. Beyond 200,000 AUD, additional subsidy produces diminishing returns: the marginal increase in covered demand falls below 3%, and most remaining subsidies reinforce redundant connectivity rather than opening new regions. 

Frontiers in Applied Mathematics and Statistics 

frontiersin.org 

13 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 5 

Optimized three-tier Australia Post network under the fuzzy hyperheuristic GA. CAB hubs (blue), regional Access Points (green), facilitation arcs (dashed orange), and drone service regions (shaded) are shown. 

This saturation behavior defines a policy efficiency frontier. It provides regulators and Australia Post with an estimate of the minimum effective subsidy required to guarantee service for lowdensity regions, while avoiding systematic overspend on redundant capacity. 

### 7.5 Ablation on hyperheuristic 

An ablation experiment was conducted to isolate the contribution of the adaptive hyperheuristic layer. When this layer was disabled (reducing the method to a static GA with fixed mutation probabilities), average performance deteriorated across all key indicators, as shown in Table 3. 

The adaptive layer systematically shifts emphasis from structural exploration (hub activation and AP reassignment) in early generations to localized refinement (drone reallocation, facilitation tuning, CAB flow balancing) in later generations. This targeted search reduces computational variance and improves convergence stability, delivering lower cost, higher robustness, and broader remote coverage compared to the static GA. 

Overall, the case study demonstrates that explicitly modeling uncertainty through fuzzy satisfaction, combined with adaptive hyperheuristic control, generates a postal air–drone network that is both more equitable in service reach and more robust to operational disruption, while remaining economically defensible at a national scale. 

FIGURE 6 

Cost decomposition by model configuration. Components include hub operation cost, backbone air corridor cost, regional feeder cost, drone operations, and facilitation expenditure. 

## 8 Conclusion 

### 8.1 Summary of findings 

This study developed and validated a fuzzy hyperheuristic optimization framework for designing a facilitated, drone-enabled hub-and-spoke postal logistics network, demonstrated through a national-scale case study of Australia Post. The model jointly optimizes hub location, access point assignment, drone 

Frontiers in Applied Mathematics and Statistics 

frontiersin.org 

14 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 7 

Pareto frontier between total cost and fuzzy robustness index. Each point is a non-dominated network configuration generated by varying ( _w_ 1, _w_ 2, _w_ 3). 

TABLE 2 Coverage of remote demand and service satisfaction under different models. 

|Model|Coverage|Average|Avg. delivery|
|---|---|---|---|
||ratio (%)|¯µ|time (min)|
|Model A:|68.5|0.72|61.4|
|Deterministic hub||||
|GA||||
|Model B: Hub +|80.2|0.78|54.7|
|Drone||||
|post-processing||||
|Model C: Fuzzy|**93.4**|**0.88**|**46.9**|
|hyperheuristic GA||||



Bold values indicate our proposed method. 

deployment, and activation of subsidized facilitation arcs under uncertain demand and reliability conditions. Fuzzy logic was used to quantify uncertainty in demand, handling capacity, and service reliability, while the adaptive hyperheuristic genetic algorithm autonomously selected and tuned search operators during optimization. 

Results show that incorporating fuzzy robustness and adaptive heuristic control yields a more resilient and cost-efficient national postal network. The proposed fuzzy hyperheuristic GA improved the average service robustness index µ¯ by 25–35% compared to deterministic hub models, while extending reliable drone coverage to 93.4% of remote demand clusters. These gains were achieved with only an 8–12% increase in total operating cost. The adaptive heuristic selection reduced computational variance and improved convergence speed by approximately 25%, producing stable Pareto frontiers between cost, robustness, and facilitation burden. 

The cost decomposition analysis revealed that drone and facilitation expenditures collectively accounted for less than 

FIGURE 8 Regional fuzzy service robustness index ( ¯µ) for selected Access Points under the deterministic GA and the fuzzy hyperheuristic GA. 

12% of total logistics cost, yet generated a 21% improvement in service equity across remote regions. Moreover, the facilitation budget analysis identified a clear saturation point: beyond 200,000 AUD per planning period, additional subsidies yield marginal coverage gains below 3%. These findings demonstrate that AI-driven fuzzy optimization can generate operationally interpretable, policy-relevant designs for complex national logistics systems. 

### 8.2 Managerial and policy implications 

The research provides actionable insights for postal network planners, regulators, and regional development authorities seeking to balance equity, cost, and resilience in national logistics systems. 

Frontiers in Applied Mathematics and Statistics 

frontiersin.org 

15 

10.3389/fams.2026.1742828 

Danach et al. 

FIGURE 9 

Effect of facilitation budget on remote service coverage. The horizontal axis shows total facilitation subsidy per period, and the vertical axis shows the share of remote demand nodes achieving µ _k_ ≥ 0.8. 

TABLE 3 Ablation analysis: effect of removing the adaptive hyperheuristic layer. 

|Configuration|Total cost<br>(M AUD)|Robustness<br>index ¯µ|Coverage<br>ratio (%)|
|---|---|---|---|
|Static GA (no|4.82|0.81|86.7|
|hyperheuristic)||||
|Adaptive FHH-GA<br>(proposed)|**4.69**|**0.88**|**93.4**|



Bold values indicate our proposed method. 

infrastructure, or flexible air-slot allocation to gradually reduce subsidy reliance and improve self-sufficiency. 

Overall, the integration of fuzzy modeling and adaptive hyperheuristics provides a transparent and flexible decision-support framework that enables national postal operators to co-optimize cost efficiency, service equity, and resilience. It also allows policymakers to derive data-driven thresholds for regional subsidy planning and infrastructure investment. 

- Resilient service coverage: Integrating drones into the national air freight backbone closes persistent lastmile connectivity gaps, particularly in Western and Northern Australia, where population density and road accessibility are low. Drone-enabled coverage ensures continuity of essential parcel delivery during weather or access disruptions. 

- Efficient subsidy allocation: The facilitation frontier highlights diminishing returns beyond approximately 200,000 AUD per period. This provides a quantifiable policy threshold for regional connectivity funding, allowing Australia Post and the Department of Infrastructure to prioritize high-impact, low-redundancy routes such as PER–ASP and BNE–BME. 

- Operational robustness metric: The fuzzy robustness index µ¯ offers a decision-oriented indicator of service reliability under multiple uncertainty sources. Networks achieving µ¯ ≥ 0.85 can be classified as operationally stable within typical Australian climatic and regulatory conditions. 

- Strategic infrastructure targeting: Hubs with high facilitation dependence—especially Perth and Brisbane—should be prioritized for capacity upgrades, enhanced drone 

### 8.3 Limitations and future work 

While the proposed framework demonstrates strong performance and generalizability, several research extensions are recommended to enhance realism and strategic relevance: 

- Environmental and sustainability objectives: Future models should incorporate carbon emission costs and sustainability targets, enabling postal operators to balance financial, environmental, and social performance metrics. 

- Temporal and operational dynamics: Extending the model to consider time-dependent flight schedules, daily demand variations, and drone charging cycles would support operational planning alongside strategic design. 

- Regulatory and stochastic uncertainty: Incorporating probabilistic or fuzzy regulatory states—such as temporary airspace closures, licensing delays, or weather-related flight restrictions—would improve the robustness of feasibility assessment. 

- Heterogeneous UAV fleets: Introducing multiple drone types with varying payloads, ranges, and costs could capture 

Frontiers in Applied Mathematics and Statistics 

16 

frontiersin.org 

10.3389/fams.2026.1742828 

Danach et al. 

the trade-offs between coverage and operating cost more accurately, supporting fleet composition optimization. 

- Reinforcement learning for adaptive control: Embedding reinforcement learning within the hyperheuristic layer could enhance operator selection policies and dynamic weight adjustment, further improving convergence efficiency and multi-objective performance. 

Future research will extend this fuzzy hyperheuristic framework to other postal and logistics systems, enabling comparative international analyses. By quantifying trade-offs between cost, equity, and resilience, the approach provides a pathway toward designing sustainable, adaptive, and inclusive logistics networks at global scale. 

## Funding 

The author(s) declared that financial support was not received for this work and/or its publication. 

## Conflict of interest 

The author(s) declared that this work was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. 

## Generative AI statement 

## Data availability statement 

The original contributions presented in the study are included in the article/supplementary material, further inquiries can be directed to the corresponding author. 

The author(s) declared that generative AI was not used in the creation of this manuscript. 

Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us. 

## Author contributions 

## Publisher’s note 

KD: Resources, Writing – original draft, Methodology, Conceptualization, Validation. SH: Supervision, Validation, Project administration, Writing – review & editing, Conceptualization. WK: Writing – review & editing, Validation, Conceptualization. ZE: Writing – review & editing, Formal analysis, Conceptualization, Resources. JS: Writing – review & editing, Supervision, Formal analysis, Conceptualization, Validation. 

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher. 

## References 

1. Australia Post. Australia Post eCommerce Report 2025 (2025). Available online at: https://ecommerce-report.auspost.com.au (Accessed October 31, 2025). 

2. Australia Post. Executive Summary: 2025 eCommerce Report (2025). Available online at: https://ecommerce-report.auspost.com.au/executive-summary/ (Accessed October 31, 2025). 

3. Qantas. Qantas Freight and Australia Post Announce Dedicated Freighter Network (2016). Available online at: https://www.qantasnewsroom.com.au/media-releases/ qantas-freight-and-australia-post-announce-dedicated-freighter-fleet/ (Accessed October 31, 2025). 

4. Danach K, Harb H, Rashid ASK, Al-Tarawneh MAB, Aly WHF. Location planning techniques for Internet provider service unmanned aerial vehicles during crisis. Results Eng. (2025) 25:103833. doi: 10.1016/j.rineng.2024.103833 

5. Liu Y, Wang J, Zhao J, Li X. Route stability in the uncertain capacitated arc routing problem. Front Energy Res. (2022) 10:933705. doi: 10.3389/fenrg.2022.933705 

6. Eck B, Smith MD, Ryan MJ. Scenario generation for network optimization with uncertain parameters. In: Proceedings of the 2015 Winter Simulation Conference (2015). p. 3012–23. Available online at: https://ascelibrary.org/doi/10.1061/9780784479162.079 (Accessed March 30, 2026). 

7. Li H, Zhang J, Li Y. A mathematical model for optimizing postal supply chain networks and facility location under uncertainty. J Indus Manag Optimiz. (2024) 4:103–20. 

8. Fazlollahtabar M, Basheer MA, Khalid Z, Tahir M, Uppal M. Logistics hub location optimization: a K-means and P-median model hybrid approach using road network distances. arXiv Preprint arXiv:230811038. (2025). doi: 10.48550/arXiv.2308.11038 

9. Jin X, Nan Z, Xie F, Wei W. Logistic network modeling and optimization: an approach based on (max,+) algebra and coloured petri nets. Comput Indus Eng. (2019) 134:1060–71. 

10. ALC. Postal Services Modernisation Discussion Paper (2023). Available online at: https://austlogistics.com.au/wp-content/uploads/2023/04/WhitePaper-230427-Postal-Services-Modernisation-V2.pdf (Accessed October 31, 2025). 

11. Edmund K, Burke GK, Petrovic S. Hyper-heuristics: a survey of the state of the art. J Operat Res Soc. (2013) 64:1695–724. doi: 10.1057/jors.2013.71 

12. Ross P, Burke E, Kendall G. Hyper-heuristics: learning to combine simple heuristics in vehicle routing problems. Comput Operat Res. (2014) 41:45–57. 

13. Alumur SA, Campbell JF, Contreras I, Kara BY, Marianov V, O’Kelly ME. Perspectives on modeling hub location problems. Eur J Oper Res. (2021) 291:1–17. doi: 10.1016/j.ejor.2020.09.039 

14. Campbell JF. Hub location and the p-median problem. Eur J Oper Res. (1994) 72:414–9. doi: 10.1016/0377-2217(94)90318-2 

15. Alkaabneh S, Diabat A. Robust hub location models under demand uncertainty: a review and recent advances. Comput Indus Eng. (2022) 168:108011. 

16. O’Kelly ME. A quadratic integer program for the location of interacting hub facilities. Eur J Oper Res. (1987) 32:393–404. doi: 10.1016/S0377-2217(87)8 0007-3 

17. Contreras I. Stochastic uncapacitated hub location problems. Eur J Oper Res. (2011) 210:554–63. 

Frontiers in Applied Mathematics and Statistics 

frontiersin.org 

17 

10.3389/fams.2026.1742828 

Danach et al. 

18. Li S, Han W, Liu L. Robust optimization of the hub location problem for fresh agricultural products with uncertain demand. IEEE Access. (2022) 10:41902–13. doi: 10.1109/ACCESS.2022.3168006 

19. Agatz N, Bouman P, Schmidt M. Optimization approaches for the traveling salesman problem with drone. Transp Sci. (2018) 52:965–81. doi: 10.1287/trsc.2017.0791 

20. Dorling K, Heinrichs J, Messier G, Magierowski S. Vehicle routing problems for drone delivery. IEEE Trans Syst Man Cybernet: Syst. (2016) 47:70–85. doi: 10.1109/TSMC.2016.2582745 

21. Murray CC, Chu AG. The flying sidekick traveling salesman problem: optimization of drone-assisted parcel delivery. Transp Res Part C: Emerg Technol. (2015) 54:86–109. doi: 10.1016/j.trc.2015.03.005 

22. Khosravi M, Enayati S, Saeedi H, Pishro-Nik H. Multi-purpose drones for coverage and transport applications. IEEE Trans Wireless Commun. (2021) 20:3974–87. doi: 10.1109/TWC.2021.3054748 

23. Silva FA, Barbosa V, Lima LN, Sabino A, Rego P, Bittencourt LF, et al. Efficient strategies for unmanned aerial vehicle flights: analyzing battery life and operational performance in delivery services using stochastic models. IEEE Access. (2024) 12:3449283. doi: 10.1109/ACCESS.2024.34 49283 

24. Alkadi R, Alnuaimi N, Yeun CY, Shoufan A. Blockchain interoperability in unmanned aerial vehicles networks: state-of-the-art and open issues. IEEE Access. (2022) 10:14463–79. doi: 10.1109/ACCESS.2022.3145199 

25. Zadeh LA. Fuzzy Sets. Inform Control. (1965) 8:338–53. doi: 10.1016/S0019-9958(65)90241-X 

26. Bonvicini S, Gentili G, Iocchi RL. A fuzzy logic model for transport risk assessment. Fuzzy Sets Syst. (1998) 94:205–11. doi: 10.1016/S0165-0114(96) 00247-3 

27. Ferreira RJ, Machado JAT. A comprehensive review on the use of fuzzy logic in logistics and supply chain management. Appl Soft Comput. (2024) 135:110132. 

28. Bukowski LA, Feliks J. Fuzzy logic expert system for supply chain resilience modelling and simulation. In: Proceedings of the 48th ESReDA Seminar on Critical Infrastructures Preparedness. Wroclaw: Polskie Towarzystwo Bezpiecze´nstwa i Niezawodno´sci (2015). p. 1–12. 

29. Shelash, S., Vasudevan, A., Alqahtani, M. M., Sun, X., and Ali, I.Leveraging fuzzy logic for resilient agricultural supply chain risk assessment and management. Risk Haz Crisis Public Policy. (2023) 14:300–18. 

30. RTInsights. Using Fuzzy Logic and AI to Improve Supply Chain Efficiency (2024). Available online at: https://www.rtinsights.com/using-fuzzy-logic-and-ai-toimprove-supply-chain-efficiency/ (Accessed October 31, 2025). 

31. Kumar V, Gupta R, Sen A. Adaptive metaheuristics for workforce allocation problems: a review and future directions. Expert Syst Appl. (2020) 140:112845. 

32. Danach K, Hassan JAH, Khalil W, Gelareh S. Routing heterogeneous mobile hospital with different patients priorities: hyper-heuristic approach. In: 2015 Fifth International Conference on Digital Information and Communication Technology and its Applications (DICTAP). New York, NY: IEEE (2015). p. 155–8. doi: 10.1109/DICTAP.2015.7113189 

33. Danach K, Rammal A, Moukadem I, Harb H, Nasser A. Advanced optimization in E-commerce logistics: combining Matheuristics with random forests for hub location efficiency. IEEE Access. (2025) 13:55915–26. doi: 10.1109/ACCESS.2025.3550560 

34. Australia Post Annual Report 2022 (2022). Available online at: https://auspost.com. au/content/dam/auspost_corp/media/documents/2022-australia-post-annual-report. pdf (Accessed October 31, 2025). 

35. Australia Post Adds A330 Freighter to Support e-Commerce Demand (2023). Available online at: https://www.aircargonews.net/australia-post-adds-a330-freighterto-support-e-commerce-demand/1065511.article (Accessed October 31, 2025). 

36. The Future of Australia Post’s Service Delivery (2020). Available online at: https:// www.aph.gov.au/DocumentStore.ashx?id=211cefba-64b9-4b64-9159-a9da14e6e1a2& subId=685766 (Accessed October 31, 2025). 

37. International Freight Assistance Mechanism (IFAM) (2020). Available online at: https://lot.dhl.com/australias-new-air-freight-network-to-boost-agriculture-andfishery-exports/ (Accessed October 31, 2025). 

38. National Freight Data Hub. Freight Data Portal. Canberra, ACT (2024). Available online at: https://datahub.freightaustralia.gov.au/ (Accessed March 30, 2026). 

39. BITRE. Australian Infrastructure and Transport Statistics Yearbook 2023. Canberra, ACT (2023). Available online at: https://www.bitre.gov.au (Accessed March 30, 2026). 

40. Australia Post. Annual Report 2024. Melbourne, VIC (2024). Available online at: https://auspost.com.au (Accessed March 30, 2026). 

Frontiers in Applied Mathematics and Statistics 

18 

frontiersin.org 

