

**Multi-period hub location problem with serial demands: A case study of humanitarian aids distribution in Lebanon** Rahimeh Neamatian Monemi, Shahin Gelareh, Anass Nagih, Nelson Maculan, Kassem Danach 



# **To cite this version:** 

Rahimeh Neamatian Monemi, Shahin Gelareh, Anass Nagih, Nelson Maculan, Kassem Danach. Multiperiod hub location problem with serial demands: A case study of humanitarian aids distribution in Lebanon. Transportation Research Part E: Logistics and Transportation Review, 2021, 149, pp.102201. ⟨10.1016/j.tre.2020.102201⟩. ⟨hal-04538478⟩ 

**HAL Id: hal-04538478** 

**https://hal.science/hal-04538478v1** 

Submitted on 22 Jul 2024 

**HAL** is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers. 

L’archive ouverte pluridisciplinaire **HAL** , est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés. 



Distributed under a Creative Commons CC BY-NC 4.0 - Attribution - Non-commercial use - International 

License 

Version of Record: https://www.sciencedirect.com/science/article/pii/S1366554520308437 Manuscript_9e9a4fef951c5895a4163f5dcf6c1f56 

\author[SOTON, METZ, LITA]{Rahimeh Neamatian Monemi} 

\author[LGI2A,LITA]{Shahin Gelareh} 

\author[LITA,METZ]{ Anass Nagih} 

\author[UFRJ]{Nelson Maculan} 

\author[LIBAN]{Kassem Danach} 

\cortext[cor1]{Corresponding author, r.n.monemi@gmail.com} 

\address[SOTON]{IT Innovation, University of Southampton, Southampton,  UK} 

\address[LGI2A]{Département R\&T, IUT de Béthune, Université d'Artois, F-62000 Béthune, France} 

\address[LITA]{Laboratoire de Conception, Optimisation et Modélisation des Systèmes, LCOMS EA 7306 } 

\address[METZ]{Université de Lorraine, Metz 57000, FRANCE} 

\address[UFRJ]{Federal University of Rio de Janeiro, COPPE-PESC, P.O. Box 68511, Rio de Janeiro, RJ 21941-972, Brazil} 

\address[LIBAN]{Department of Informatics, Islamic University of Lebanon, Beirut, Lebanon} 

© 2021 published by Elsevier. This manuscript is made available under the CC BY NC user license https://creativecommons.org/licenses/by-nc/4.0/ 

# Multi-period Hub Location Problem with Serial Demands: A Case Study of Humanitarian Aids Distribution in Lebanon 

## **Abstract** 

In this paper, we address the problem of humanitarian aids distribution across refugee camps in war-ridden areas from a network design perspective. We show that the problem can be modeled as a variant of multiperiod hub location problem with a particular demand pattern resulted by the user’s behavior. The problem has been motivated by a case study of Lebanese experience in Syrian war refugee accommodation. We elaborate on the complexity and real-life constraints and, propose a compact formulation of a mathematical model of the problem. We then show that modeling the problem using a Benders paradigm drives O(n<sup>3</sup> ) variables of the original compact model unnecessary in addition to the constraints that are being projected out in a typical Benders decomposition. Additionally, we identify several classes of valid inequalities together with efficient separation procedures leading to a cut-and-Benders approach. Our extensive computational experiments on the case study with real data as well as randomly generated instances proves the performance of proposed solution methods. 

_Keywords:_ Hub-and-spoke network design, distribution, humanitarian aids, refugees, mateheuristics. 

## **1. Introduction** 

The emergency situations including wars and natural disasters introduce fragility for civilians and occurrence of urgent requirements. Loosely speaking, in cases of natural disasters, today’s technology is to a high extent able to foresee many natural phenomena. However, when it comes to a war situation, an anticipation and prediction of its duration is very difficult as it may last unexpectedly long. Therefore, any predictive/preventive plan becomes less realistic. 

Generally speaking, in cases of natural disasters, in many cases the impacted geographical region is relatively restricted. As a consequence, a reconstruction can be started immediately, or relatively very quickly in the aftermath of the event and people will be able to return to their residential areas afterwards; while, in a war condition, everything is of a different nature. In wars, damages are propagated and distributed very quickly across a relatively very wide area. The longer the war lasts, the less becomes the likelihood of any quick return of the refugees back to their homes (those fled out of the region<sup>1</sup> ). This is mainly due to the deteriorated economic conditions hindering the reconstruction until a stability is re-established in that political and economic ecosystem. Till then, the UNHCR-recognized refugees are entitled to some supports including humanitarian aids to overcome their essential needs. 

A most recent case of this situation is already happening in Syria where a multitude of players have got involved and the situation developed since the unrest in the aftermath of the so called _Arab Spring_ has turned into a full-fledged chaotic and asymmetric war spread over a wide region from the south approaching the capital of Iraq, from the east to the boarder villages in Lebanon and up until the Jordanian boarders. According to the UNHCR<sup>2</sup> , Syrian war has caused 6.6 million internally displaced persons, 13.1 million people in need inside Syria and 2.98 million people in hard-to-reach and besieged areas. Table 1 reports the 

> 1Here, unless said otherwise, by the word ’ _refugee_ ’ we refer to those who had to leave their homes and seek residing elsewhere due to the war condition, independent of being recognized/registered as refugees by the UNHCR or not. 

> 2http://www.unhcr.org/syria-emergency.html 

_Preprint submitted to Elsevier_ 

_October 28, 2020_ 

statistics reported by the UNHCR<sup>3</sup> . It must be noted that this only concerns the registered refugees and not all-inclusive. 

|Location Name|Source|Data date|Pop|ulation|
|---|---|---|---|---|
|Turkey|Government of Turkey, UNHCR|18 Oct 2018|63.7%|3,587,930|
|Lebanon|UNHCR|30 Sep 2018|16.9%|952,562|
|Jordan|UNHCR|24 Oct 2018|11.9%|672,578|
|Iraq|UNHCR|30 Sep 2018|4.4%|250,184|
|Egypt|UNHCR|30 Sep 2018|2.3%|131,504|
|Other (North Africa)|UNHCR|15 Mar 2018|0.6%|33,545|



**Table 1:** Total Persons of Concern by Country of Asylum. 

One observes that Lebanon, together with Turkey account for more than 80% of refugees, although when it comes to the registered refugees only. According to the sources within the Lebanon, in 2017, this number reached 1.5 million, which stands for a government estimation accounting for both UNHCR-registered and non-registered displaced Syrians. 

Lebanese Republic is a country of 6.082 million population neighbor with two countries, with almost half of its borders faced to the Mediterranean Sea Figure 1a. Even though the country neither is located in the most peaceful neighborhood in the world nor its political conditions are the most stable one around the globe, the main mode of transport is road for domestic transportation. Moreover, due to the geographical topology and environmental barriers and conditions, the country does not run any known railway system. Although the country’s dimensions are quite limited to an area of 10,452 km<sup>2</sup> , the hilly nature of territory causes long travel time between pairs of theoretically close locations. Therefore imposing accessibility issue for distribution networks is needed in many cases. Figure 1b depicts elevation plan across this territory. 

Since the start of war in Syria, the population of Lebanon has increased by a factor of 25.6% by Syrians, 0.5% by Palestinian refugees from Syria and 0.6% by Lebanese returning from Syria. In Lebanon, according to the UNHCR, life is a daily struggle for more than a million Syrian refugees, who have little or no financial resources. Around 70% live below the poverty line. There are no formal refugee camps and, as a result, Syrians are scattered throughout more than 2,100 urban and rural communities and locations, often sharing small basic lodging facilities with other refugee families in overcrowded conditions<sup>4</sup> . 

Lebanese authority have divided Lebanon into 26 districts at the centroid of the circles depicted in Figure 2a. The circles’ diameters are proportional to the population of refugees residing in those regions. Historically, for the almost half a million Palestinians living in camps in Lebanon, there has been a number of Distribution Centers (DC) serving those camps across the country. In Figure 2b, every centroid represent location of a camp and its diameter is proportional to the population accommodated in that region. In this image, red circles represent DCs, while the main one is in the region of Beirut (annotated in the figure). 

On the other hand, human factors (also known as user’s behavior) is another complicating factor, too. The delivery of packages of humanitarian aids for a given district usually takes place within a certain interval of the time, say a week (five working days). A few loaded trucks leave the Main Warehouse (MW) to the selected destination districts on a daily basis. While the number of people to be served –during the planning horizon– in each zone is known in advance (due to the known historical data, with a good precision), the number of people showing up to collect their packages depends on the day of distribution (first day, second day, third day, fourth or fifth day, depending the planning). 

> 3https://data2.unhcr.org/en/situations/syria 

> 4http://www.unhcr.org/syria-emergency.html 

2 







<!-- Start of picture text -->
(a) Lebanon and its neighborhood. (b)  Map of elevation.<br><!-- End of picture text -->

**Figure 1:** Geographical condition of Lebanon. 

|#|days|# percentage of show-up|
|---|---|---|
|1||100%|
|2||50% and 50%|
|3||38%, 24% and 38%|
|4||31%, 21%, 14% and 34%|
|5||23%, 18%, 18%, 20% and 21%|



**Table 2:** The user’s behavior for different planning horizon lengths. 

In the other word, it is unclear exactly how many people will show up at a given day to collect their items, even though the total demand of every node is precisely known (The total demand of a node is the demand of a node if we serve it exactly once in every horizon and not over several days). The historical data shows that users behavior in showing up at the distribution points follows Figure 3. E.g. if a 3-day distribution plan is considered, the first and last days are the days with highest percentage (around 38%) of people showing up while the second day attracts the minimum percentage (around 24%) of consumers showing up to collect their packages (see Figure 3). The demand pattern for various planning horizon length is depicted in Table 2. 

In general, there is a Main Warehouse (MW), which acquires the nutrition and other essential requirements, needed for developing packages in the form of baskets of given amount of calories, to be sent to the consumers. The preparation of packages are to be done in MWs. Once the packages are formed, depending on the distribution plan, they are loaded on a fleet of trucks and LGVs and are sent to the selected regional DCs. The regional DCs are represented by hub nodes in the model. The next morning, trucks start from the regional DCs and from there, they are deployed to selected points of delivery (the delivery points, other way of saying the refugees camps, are the nodes which are represented by the "spoke nodes" in the model). The delivery points (spoke nodes) are to be visited in a sequential order. every unloaded truck will be discharged from the rest of the operation/itinerary and will leave the fleet immediately. At the end of the day, there must not be any truck left fully or partially loaded. It must be noted that among the locations to be served 

3 





<!-- Start of picture text -->
(a)  Spatial distribution of Syrian refugees across the Lebanese territory.<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) Spatial distribution of Palestinian refugees camps in Lebanon.<br><!-- End of picture text -->

**Figure 2:** Spatial distribution of Syrian and Palestinian refugees and the Distribution Centers (DCs). 

4 



<!-- Start of picture text -->
0.4 0<br>0.3 8<br>0.3 6<br>0.3 4<br>0.3 2<br>0.3 0<br>0.2 8<br>0.2 6<br>0.2 4<br>First Day Second Day Third Day<br><!-- End of picture text -->

**Figure 3:** User behavior in collecting the packages of humanitarian aids from the allocated DCs. 

(the centroid) there are locations with access issues for the trucks; therefore such points are served directly from the DCs using chartered services through a third-party service provider. These points are represented by "isolated nodes" in the model. Once a node received its services (in one, two or three days, depending on the planning), the node will no more be considered as a potential spoke(or spur) node until the end of the current planning horizon. 

Briefly speaking, what we deal with is mainly a hub-and-spoke network design problem, while the demand is not fixed primarily and may vary depending on the planning we propose to the problem. Moreover, establishing the hub-level network does not required any extra charge and hub nodes may be selected among all the nodes available in the network. Hub nodes are to be connected to the main warehouse through a direct connection and spoke nodes are to be assigned to their corresponding hub node, on a ring structure. There might be nodes that are out of access and need to be served separately, using an extra transporter, thus imposing extra charge. Given the above representation, the problem and the targeted operation fits in with the framework of multiperiod Hub-and-Spoke network structures, mainly because the demand per day depends also on the final distribution plan (following the pattern represented in 3). It is essential to mention that every UN camp can potentially be served as a distribution centre (DC, which also called Hub node) while other camps in its neighbourhood are to be considered as spoke nodes all connected to that. The main reason to select a node and not the other one is basically the location of the selected one as the hub (DC) and the distances between the MW, the selected hub and the other nodes in the network. A node can act as a hub node in a day during the planning horizon and not on the next day. Indeed, we do not obliged to meat all nodes, everyday during the horizon, but we make sure that all what a node needs (its demand) will be respected during every horizon. 

The objective is to identify the location of a subset of hub nodes (DCs) in each period of the horizon and establish a network with a multi-level structure. The demand of every node at each period is a percentage of the whole demand during the entire planning horizon and depends on the number of antecedent visits to the same node during the same planning horizon. Flow is unidirectional, only from the Main Warehouse (MW) to its final destination. The fleet of transporters is assumed to be homogeneous. 

## **2. Literature review** 

The hub-and-spoke structures have their roots in the seminal work of Hakimi (1964) –which has then been generalized by Goldman (1969)– for finding the optimal location of a single switching center proven to be on the vertex median of the graph. 

Earlier models assume that every origin-destination (O-D) path includes no more than two hub nodes (O’Kelly (1986a,b) and O’Kelly (1987)). In addition to the single or multiple allocation schemes and simpler 

0 

capacity settings, over the time, further realistic features were integrated into the initial models aiming at achieving a better approximation of real-life practice. At the same time, introducing more realistic features (including multi-modal services) resulted in many more additional variables and constraints and much more complex models, which motivated wider researches including the algorithmic aspects of problems. 

-Re-visiting the literature, one sees that in the earlier contributions, branch-and-cut and enumerationbase methods were the dominant approaches (see Aykin (1994), Ernst and Krishnamoorthy (1996), Klincewicz (1996), Abdinnour-Helm and Venkataramanan (1998), Ernst and Krishnamoorthy (1999), Ebery et al. (2000), Ernst and Krishnamoorthy Mayer and Wagner (2002), Marín (2005a), Sasaki et al. (1999), Sasaki and Fukushima (2003), Labbé et al. (2005), Klincewicz (2002), Campbell et al. (2003), Campbell et al. (2005b) and Yaman and Carello (2005)), Lagrangianbased methods (see Pirkul and Schilling (1998), Elhedhli and Hu (2005), Aykin (1994) and Marín (2005b)), or dual ascent techniques (see Klincewicz (1996), Mayer and Wagner (2002), Cánovas et al. (2007), Contreras et al. (2011d and Wagner (2007)). Meanwhile, as the complexity of models has augmented, Benders decomposition paradigm became a very popular technique, given their historical success in problems with network design substructures. To what we found, Camargo et al. (2008) was the first Benders method proposed for an Uncapacitated Multiple Allocation Hub Location Problem. The proposed formulation in this work is referred by other very efficient works afterwards (Gelareh and Nickel (2011), Rodriguez-Martin and Salazar-Gonzalez (2008) and Contreras et al. (2011a)). 

## _2.1. Multi-period hub location problem_ 

Very few multi-period hub location models have been proposed in the literature. In this subject, Campbell (1990) proposed a continuous approximation model for a general freight carrier serving a fixed region with an increasing density of demand. Also, Gelareh (2008); Gelareh et al. (2015a) proposed a HLP model within which the transport service provider starts with an initial configuration of the hub-level structure at the first period of the time and then the network evolves in the course of a considered planning horizon. Another study is Contreras et al. (2011b), in which a dynamic uncapacitated hub location problem is studied. Recently, Monemi et al. (2017) proposed a hub location problem in a co-opetitive setting. 

Interested readers are also referred to the HLPs literature review in Alumur and Kara (2008), Campbell and O’Kelly (2012 and Farahani et al. (2013) as well as other contributions by Campbell et al. (2002) and Kara and Taner (2011). 

## _2.2. Demand structures in hub location problems_ 

In what concerns the demand structure, Miranda Junior et al. (2011) studies demand uncertainty and congestion with applications tailored for air transport. Also in this context, general demand uncertainty is studied in Alumur et al. (2012) and Contreras et al. (2011c). Later, Merakli and Yaman (2017) and Merakli and Yaman ( were working on introducing robust solution algorithms in presence of various types of demand uncertainty. O’Kelly et al. (2015) analyzes the quality of service in presences of price sensitive demands and proposes relevant models for this variation of the HLP. The literature is unaware of any contribution dealing with a deterministically structured demand patterns or a demand structure resulted by human factors. 

O’Kelly and Bryan (1998) dealt with the flow-dependent costs while congestion cost was considered by de Camargo and Miranda (2012); De Camargo et al. (2011); de Camargo et al. (2009a). Rodríguez-Martín et al. (2014) proposed a model for the hub location and routing problem; while Correia et al. (2014) dealt with multiproduct and capacity and Sasaki et al. (2014) with a competitive hub location based on Stackelberg games. 

0 

## _2.3. Humanitarian subjects in Hub Location Problems_ 

While literature of humanitarian logistics has a rich body, we can only cite a few somehow more relevant ones to our work. In fact, most of contributions concern technical aspects of urban or civil applications that are less relevant to the problems we described here. Yet in the following, we highlight the most recent development in this topic which, are still to some extent relevant. 

-In humanitarian logistics context, Dufour et al. (2018) analyzes the potential cost benefits of adding a regional distribution center in Kampala, Uganda, to the existing network of the UNHRD in order to better respond to humanitarian crises in East Africa. They carry out a simulation, network optimization and statistical analyses to assess the costs of prepositioning high-demand non-food items in Kampala and to propose a robust stocking solution. 

Tofighi et al. (2016) proposed a two-echelon humanitarian logistics network design problem involving multiple central warehouses and local distribution centers and developed a novel two-stage scenario-based possibilistic-stochastic programming approach. What they proposed is a trade-off between the egalitarian and utilitarian objectives. Vahdani et al. (2018) proposed a two-stage multi-objective location-routing-inventory model for humanitarian logistics network design under uncertainty taking into account time factor and robustness of the final solutions under uncertainty. An et al. (2015) studied the hub and spoke network design problem while focusing on the reliability of the service in the network. To this, the authors considered the concept of backup hubs in the phase of planning the network. Zhalechian et al. (2018) proposed a risk analysis study and worked on the hub-and-spoke network design under operational and disruption risks. Later in 2019, Mohammadi et al. (2019) studied the Reliable single-allocation hub location problem while considering disruptions and proposed a bi-objective model for this problem. 

Özdamar and Ertem (2015) reviewed the literature on response and recovery planning phases of disaster management and focused on the classification and computational perspectives of humanitarian logistics models highlighting potential research direction. Boonmee et al. (2017) examines the four main problems highlighted in the literature review: deterministic facility location problems, dynamic facility location problems, stochastic facility location problems, and robust facility location problems. For each problem, facility location type, data modeling type, disaster type, decisions, objectives, constraints, and solution methods are evaluated and real-world applications and case studies are presented and at the end the research gaps are being identified. 

Elçi and Noyan (2018) proposed a novel risk-averse stochastic pre-disaster relief network design problem. In Elçi et al. (2018) they considered a trade-off between the actual cost and the cost of reliability and proposed a tight MIP formulation. 

Charles et al. (2016) proposed a tooled methodology to support humanitarian decision makers in the design of their supply chains. Based on the concept of aggregate scenarios to reliably forecast demand using past disaster data and future trends, some scenarios are generated and demand for relief items based on these scenarios is then fed to a MIP model in order to improve current supply networks. 

## _2.4. Contribution and scope_ 

The prime focus of this paper is to propose a network structure for distribution of humanitarian aids for Syrian refugees in Lebanon. The objective of this work is mainly improving the quality of services provided by the UNHCR, by assuring the frequency of service and receiving the demands in time. Besides, another motivation and objective of this work is to propose an exhaustive planning of distributing the demand in 

1 

the network while optimising the use of available resources, as well as improving the benefits of service providers, in terms of reducing the cost of service provision and the use of navigation fleet (mainly by optimising the use of the capacity of transporters in every trip) to let service providers eventually serving more camps and refugees by providing them with packages of humanitarian aid. This work has been inspired by a thorough investigation of the matter and a close collaboration with the relevant decision makers of the sector. From the theoretical and modeling point of view, this model generalized the previous models of Hub Location Problem by introducing a Multi-Period Hub Location Problem with Serial Demands (MPHLPSD) wherein the demand volume at the n-th visit is proportional to the n-th term of a sequence of number representing human behavior. We propose the first compact mixed integer programming formulation for this problem and show that if Benders decomposition is seen from the perspective of a modeling tool, O(n<sup>3</sup> ) variables can be dropped from the formulation, in addition to the constraints being projected out in Benders fashion. Several classes of effective valid inequalities and efficient separation routines are proposed in order to turn the solution approach into a very efficient cut-and-Benders method reporting a significantly accelerated convergence. For the case at hand, we report the optimal location of DCs to be used in Lebanon. An extensive computational experiments on randomly generated instances of various sizes, confirms computational efficiency of the proposed solution framework and viability of the proposed technique. 

This paper is organized as follows: The problem is formally described in Section 3 and a mathematical model together with several classes of valid inequalities are proposed in Section 4. Section 5 describes the design of our solution approach and the associated components. Section 6 reports some computational experiments and gives insights into the effectiveness of the proposed approach. In Section 7, we summarize, draw conclusions and provide suggestions for further research directions. 

## **3. Problem Description** 

A Main Warehouse acquires the nutrition and composes packages to be distributed, among refugees at the demand points. Every demand point is served q times (at most 3 times, in practice) during a distribution horizon of length T (normally a week, i.e., 5 days) where q < T . For every demand node that is actually representing a refugee’s camp in the network, the sum of demands collected by the associated refugees over the distribution days is an exogenous part of the problem and equivalent to the total demand of that node. Refugees show up at the collection points following a known pattern as a sequence {lp}p∈i,...,m wherein �m1<sup>lp= 1, i.e., lp ×100 percent of the refugees settled in this point (the current visiting camp) are showing</sup> up at the p−th visit to this point during the planning horizon. Each day, a subset of all demand nodes are chosen to be visited and served by the distributors. These nodes are then partitioned into groups/clusters of ordered nodes, according to the order by which they are going to be served. One node per cluster is designated as a DC. Due to some known reasons including geographical barriers and/or security issues, certain locations in a cluster cannot be served on the route. These nodes are referred to as _isolated_ nodes. A convoy of trucks transporting the packages travel overnight from the MW towards a DC node in every cluster, which has the operational capacity of accommodating and assuring the security of the convoy of trucks. We assume that the fleet is a homogenous one as all transporters have comparable specifications. The journey starts the day after, where the DC node is served first and then all the other nodes according to the order and at the end the tour terminates when the last node on the route is served. At every DC node at which an isolated one is allocated, a shuttle service load the demand of isolated node (sufficient supply according to the p-th visit’s demand of that node) and departs from the DC. Each time a demand point is served (its planned daily demand is delivered), the fully unloaded trucks, if any, are discharged and will leave the convoy. A total length of travel from a DC visiting all nodes sitting on the route, up until the last one must not exceed a pre-defined number of nodes as the convoy wishes to finish the task before the end of day (roughly speaking, the sunset time). A demand node (representing a camp) might have already been visited q times on the days before the current day, while in such a situation, it will no more be visited on the current day or afterwards. If not, it may be visited on the current day of the horizon, or if there is not a visit planned for it on the current day, it will have a visit (or more, if needed) on the forthcoming days before the 

2 

end of the planning horizon, to ensure the exactitude of receiving q visits before the end of the horizon. It is to clarify that on a certain day, a demand node may have a visit or not, while it definitely have q visits on different q days during the distribution horizon to cover the total demand of it. 

We seek at every period, locating an optimal number of DCs and identify the demand nodes to be visited, while avoiding them being visited more than q = 3 times in a period, the clusters to be formed, the sequences of demand point being served by every DC (on the route or directly using a chattel service) and the optimal number of transporters, such that the total cost of operations accounting for the fixed set up cost for DCs and the total transportation and fixed vehicles costs is being minimized. 

In the remainder of this paper, we will use DC and hub node, demand point and spoke node interchangeably. 

## **4. Mathematical Model** 

The problem as described in the previous section resembles a hub-and-spoke structure and gives rise to a new variant of this problem, which to the best of our knowledge, has not been studied previously. In this section, we present a MIP formulation for this problem and will refer to it as _Multiperiod Hub Location Problem with Serial Demand (MPHLPSD)_ . The parameters are listed in Table 3. 

|c<sup>t</sup><br>ij<sup>:</sup>|the unit transportation cost associated with the arc(i,j)at periodt,|
|---|---|
|wj:|the demand at nodej,|
|b:|the penalty cost coefficient applied to the arc connecting an isolated node,|
|F<sup>t</sup><br>i<sup>:</sup><br>|the fixed cost of using locationias a DC in periodt,|
|N <sup>0</sup>:|N ∪{0}={1, . . .,N}∪{0}represents the set of nodes acting as DCs; 0 being the Main Warehouse,|
|V<sup>t</sup><br>0i<sup>:</sup>|the fixed cost of deploying a truck from the MW to the DC located ati,|
|T :|T ={1, . . .,T}represents the planning horizon, where|T|=T is the length,|
|P:|P ={1, . . .,q}represents the set of call numbers to every node, where|P|=qis the visit frequency,|
|DC:<br>|DC ⊆N represents the set of potential DC nodes,|
|N<sup>min</sup>/N<sup>max</sup>:|represent the min/max number of nodes (spoke nodes) allocated to every DC in a given period,|
|V<sup>cap</sup>:|the typical capacity of vehicles in a convoy,|
|lp:|the fraction of demand to be delivered during thep-th visit.|



**Table 3:** Model parameters. 

_4.1. Decision variables:_ Decision variables required to model this problem are listed below: rijt is 1, for all i, j ∈ N<sup>0</sup> , i � j and for all t ∈ T , if arc (i, j) is an arc belonging to one of the service routes at period t, and 0 otherwise. z<sup>t</sup> ij is 1, for all i, j ∈ N if node i is allocated to hub j in period t, self-allocation represents a DC at i. It means that z<sup>t</sup> ii is 1, if i is a DC node (hub) at period t, and 0 otherwise. y<sup>t</sup> ii is 1, for all i ∈ N if i is an isolated node at period t, and 0 otherwise. y<sup>t</sup> ij is 1, for all i, j ∈ N if j is an isolated node in period t allocated to a DC i, and 0 otherwise. ζ<sup>p</sup> it is 1, for all i ∈ N , for all t ∈ T and p ∈ {1, 2, 3} if p-th visit to i takes place at period t, and 0 otherwise. x<sup>t</sup> jkl for all j, k, l ∈ N and for all t ∈ T represents the fraction of flow from the MW to j traversing arc (k, l) in period t. And finally v<sup>t</sup> kl for all k, l ∈ N and for all t ∈ T represents the number of transporters deployed on the arc 

3 

## (k, l) in period t. 

We also introduce G(V, A ∪ A<sup>′</sup> ), S ⊂ V, δ<sup>+</sup> (S) = {a = (i, j)|i ∈ S, j ∈ V/ S}, δ<sup>−</sup> (S) = {a = (j, i)|i ∈ S, j ∈ V/ S} and γ(S) = {a = (i, j)|i, j ∈ S, j � i}. 

- _4.2. A mixed integer linear programming model_ 

We propose the following MIP for the MPHLPSD: 

(MPHLPSD) 



<!-- Start of picture text -->
min � � � wjckl t xt jkl + � � V0 t k vt 0k<br>t j k�j,l t k�MW:MW=0<br>+ � � bc t ij y ij t + � � F t i z ii t (1)<br>t i,j�i t i:i�MW<br>s. t.<br>N min ⩽ � z t ji ⩽ Nmax, ∀i, t, (2)<br>j<br>� r t ij = � z t ij , ∀i, t, (3)<br>j�i j<br>� r t ji = � z t ij , ∀i, t, (4)<br>j�i j<br>r t ji + rt ij ⩽ 2 − z ik t − zt jl , ∀i, j, k, l, t, k : j � i, k � l, (5)<br>�(� z t ij + z ii t + yt ii ) = q, ∀i, t, (6)<br>t j�i<br>r t ij + rt ji ⩽ 1, ∀i, j, t : j � i, (7)<br>� ζ p it = 1, ∀p, i, (8)<br>t<br>ζ 1 i1 = z1 ii + � z 1 ij + y ii 1 , ∀i, j : j � i, (9)<br>j�i<br>ζ p it ⩽ z ii t + � z t ij + y ii t , ∀i, j, p, t : j � i, t ⩾ 2, (10)<br>j�i<br>t<br>� ζit p+′ 1 ⩽ ζ p it , ∀i, t, p : p ⩾ 1, (11)<br>t ′ =1<br>z t ij ⩽ zt jj , ∀i, j : j � i, t, (12)<br>� y t ji = y ii t , ∀i, t, (13)<br>j�i<br>r t 0i = z ii t , ∀i, t, (14)<br>y t ii ⩽ � ζ p it , ∀i, t, (15)<br>p<br>y t ij ⩽ z ii t , ∀i, j, t : j � i, (16)<br>� y t ij ⩽ 1, ∀i, t, (17)<br>j�i<br>� �ζ p it + ζp it+1 + ζp it+2� ⩽ 2, ∀i, t ∈ {1, N − 2}, p, (18)<br>p<br><!-- End of picture text -->

4 

|�<br>wjx<sup>t</sup><br>j0k <sup>= wj</sup><br>�<br>lpζ<sup>p</sup><br>jt<sup>,</sup>|∀t,j:�MW,|(19)|
|---|---|---|
|k�i,0<br>p|||
|�<br>wjx<sup>t</sup><br>jkj <sup>= wj</sup><br>�<br>lpζ<sup>p</sup><br>jt<sup>,</sup>|∀t,j�MW,|(20)|
|k�j<br>p|||
|�<br>wjx<sup>t</sup><br>jkl <sup>=</sup><br>�<br>wjx<sup>t</sup><br>jlk<sup>,</sup>|∀t,j:j�MW,k�{j},|(21)|
|l�0<br>l�k,k�0|||
|x<sup>t</sup><br>j0l <sup>⩽rt</sup><br>0l<sup>,</sup>|∀j,l,t,|(22)|
|x<sup>t</sup><br>jkl <sup>⩽rt</sup><br>kl <sup>+ yt</sup><br>kl<sup>,</sup>|∀t,j,k:k�j,l�k,|(23)|
|x<sup>t</sup><br>jkl <sup>⩽</sup><br>�<br>j<br>z<sup>t</sup><br>kj<sup>,</sup>|∀t,j,k:k�j,l�k,|(24)|
|�<br>wjxj0kt ⩽V<sup>cap</sup>v<sup>t</sup><br>0k<sup>,</sup>|∀k,t,|(25)|
|k|||
|x<sup>t</sup><br>jkl <sup>∈(0, 1)|N 0|3|T|, rt</sup><br>ij<sup>, zt</sup><br>ij <sup>∈{0, 1}|E||T|, ζp</sup><br>it <sup>∈{0, 1}pN|T|, vt</sup><br>kl <sup>∈NN|T|.</sup>||(26)|



The objective function (1) accounts for the total transportation cost as well as the cost of deploying transporter on legs of call, fixed setup cost for the DCs and the penalty cost of having isolated nodes. 

The number of nodes along every route is bounded between a minimum and a maximum number to avoid too many stops as per constraint (2). Exactly one arc arrives to/leaves a node that belongs to a route. This is expressed by the constraints (3)-(4). A route arc can only be established between two spoke nodes allocated to the same hub nodes in the same period as guaranteed in constraints (5). Constraints (6) ensure that q times during the distribution horizon every node is being served —either directly or indirectly. Two arcs (i, j) and (j, i) cannot be established simultaneously between two nodes i and j. This is guaranteed in constraints (7). Every node has a first, second, . . . , p-th time that it has been visited as per constraints (8). A visit to a node at the first period corresponds to the first visit as stated in constraints (9). For every p-th visit to a node in a given period, the node must appear in that period, as stated in constraints (10). Constraints (11) ensure that the p + 1-th visits cannot take place before the p-th one. Constraints (12) ensure that every route node must be allocated to a hub node. Every isolated node must be connected to the rest of the network via an arc that arrives to it from one route node (hub or non-hub) from among all of them. This is ensured by constraints (13). At every period, there is an arc from the MW to every hub node as stated in constraints (14). Constraints (15) ensure that an isolated node of a given period will not be opened unless the number of visits to that node is incremented. Constraints (16) ensure that the tail node of an arc from a route node towards an isolated node must be a DC. A DC node cannot serve more than one isolated node as per constraints (17). Constraints (18) ensure that no point is visited q = 3 times in a row (q consecutive periods). The volume of flow originated from the MW and destined to every demand node corresponds to the demand pattern in the p-th visit. Constraints (19)- (21) are the flow conservation constraints. At every period, there is an arc encompassed from MW to every designated hub nodes as stated in constraints (22). Constraints (23) ensure that flow from the MW to the DCs traverse existing arcs. Constraint (24) ensure that if k is not MW, flow does not enter any arc (k, l) unless k is a ring node (unless k belongs to the same ring that l belongs to it). The number of trucks leaving from the MW is sufficient to accommodate the volume being shipped. This is guaranteed by constraints (25). 

## _4.3. Illustrative Example_ 

In Figure 5, the evolution of network over a period of one week is depicted. The planning horizon is one _week_ and every node is served exactly 3 times. It must be noted that this is an artificial example assuming all nodes can be DCs or isolated nodes. In this figure, arrows represents the suggested routs. Dashed arrows represent routs to serve iusolated nodes by a direct shuttle and dotted nodes shows where a truch is unloaded and from that node, it discharged from the service and directly returned to the attributed DC. The rout does not end there, since there are other trucks in the fleet that continues their itinerary to finish their assignments. 

5 



<!-- Start of picture text -->
4 9 8<br>9 8<br>6<br>2 5 1<br>7<br>0 5<br>3<br>3<br>4<br>7 2<br>6<br>1 3 1<br>4<br>0 6<br>8 5 0 9 2 7<br>(a)  Monday. (b)  Tuesday. (c)  Wednesday.<br>7 1<br>6<br>5<br>5<br>2<br>3<br>4<br>9<br>0<br>1<br>3<br>8 4<br>8 6<br>0 2<br>9 7<br>(d)  Thursday. (e)  Friday.<br><!-- End of picture text -->

**Figure 4:** An illustration of network structure over the period of week. Every node is visited p = 3 times. The nodes on the left side of images correspond to the ones that were not served in the given period. The nodes 2 and 7, which were DCs in the first day, do not appear on the network of Tuesday and on Wednesday, they become normal demand points being served by the node 9 as DC to which they are allocated. While on Monday and Thursday, the node 6 is an isolated node (perhaps) it becomes a DC node on Tuesday. 

6 

## _4.4. Valid Inequalities_ 

We introduce r(δ(S)<sup>+</sup> ) =<sup>�</sup> i∈S,j∈V/ S<sup>rij,r(A(S))=�</sup> (i,j)∈A(S)<sup>rij, where A(S)={a = (i, j) ∈A:i, j ∈</sup> S} and r(P) =<sup>�</sup> (i,j)∈P<sup>rijwhere P= {(i0, i1), (i1, i2), . . ., (ik−1, ik)}.</sup> 

**Proposition 1.** _Let_ V _be the set of nodes in the network. The following inequalities are valid for (MPHLPSD):_ 



<!-- Start of picture text -->
r t (A(S)) ⩽ |S|, S ⊂ V (27)<br><!-- End of picture text -->

_Proof._ It is an obvious consequence of the definition of r(A(S)). 

**Proposition 2.** _If_ i ∈ S ⊂ V _and_ i _is a non-isolated demand node served by a DC in_ V/ S _at period_ t _, there is at least one arc going out of (entering into)_ S _:_ 



<!-- Start of picture text -->
a) r t (δ + (S)) ⩾ � z t ij , ∀i ∈ S ⊂ V, t, (28)<br>j∈V/ S<br><!-- End of picture text -->



<!-- Start of picture text -->
b) r t (δ − (S)) ⩾ � z t ij , ∀i ∈ S ⊂ V, t. (29)<br>j∈V/ S<br><!-- End of picture text -->

_Proof._ a) For a given S ⊂ V and any i ∈ S, in the absence of any arc (i, j) with the tail in S and the head in the complementary set, any path from i to the DC serving i entirely lies within S. Thus, there exists no j outside S, which serves i for any choice of j ∈ V/ S. On the contrary, if i is served by a DC in V/ S there is a unique path cutting S (at least once) towards the DC serving i. b) Analogous to the proof of a). 

See Monemi and Gelareh (2017) and Martín et al. (2014) for similar valid inequalities. 

**Proposition 3.** _In period_ t _, if_ i ∈ S ⊂ V _and_ i<sup>′</sup> ∈ V/ S _be two demand nodes where_ i _is served by a DC in_ V/ S _and_ i<sup>′</sup> _served a DC in_ S _, we have:_ 



<!-- Start of picture text -->
r t (δ + (S)) ⩾ � z t ij + � z t i ′ j ′ , ∀i ∈ S ⊂ V, i ′ ∈ V/ S, t, (30)<br>j∈V/ S j ′ ∈ S<br><!-- End of picture text -->



<!-- Start of picture text -->
r t (δ − (S)) ⩾ � z t ij + � z t i ′ j ′ , ∀i ∈ S ⊂ V, i ′ ∈ V/ S, t. (31)<br>j∈V/ S j ′ ∈ S<br><!-- End of picture text -->

_Proof._ Similar to 2. See Monemi and Gelareh (2017) and Martín et al. (2014) for similar case in different problems. 

**Proposition 4.** _If_ (i − j) _or_ (j, i) _is an arc in period_ t _and_ j _is served by DC_ k _then_ i _must be also be served by_ k _:_ 



<!-- Start of picture text -->
r t ij + rt ji + zt jk ⩽ 1 + z ik t ∀i, j, k : j � i, t. (32)<br><!-- End of picture text -->

**Proposition 5.** _For all_ S ⊆ V, t _,_ 



<!-- Start of picture text -->
|S|<br>r t (A(S)) − � z t ii ⩽ |S| − ⌈ N max ⌉ (33)<br>i∈S<br><!-- End of picture text -->

_is a valid inequality._ 

_Proof._ Given that r<sup>t</sup> (E(S)) = r<sup>t</sup> (A(S)), c.f. Proposition 2 in Martín et al. (2014). 

The so-called _chain barrier constraints_ or _path inequalities_ (see Fischetti et al. (1998a)) inequalities are valid inequalities for MPHLPSD. 

7 

**Proposition 6.** _For each_ t, S ⊆ V, {i, i<sup>′</sup> } ⊆ I _and a path_ P := {(i, i1), (i1, i2), . . . , (ik, i<sup>′</sup> )} _from_ i _to_ i<sup>′</sup> _, the inequality:_ 



<!-- Start of picture text -->
r t (P) + � z t ij + � z t i ′ j ⩽ |P| + 1 (34)<br>j∈S j�S<br><!-- End of picture text -->

_is valid for MPHLPSD polytope. Constraints_ (5) _are special case of_ (34) _when_ P := {[i, i<sup>′</sup> ]} _._ 

**Proposition 7.** _If for a given arc in a given period_ t _, its tail is in_ S _and its head is in_ V /S _(or vice versa), either the tail is allocated to a hub node in_ V/ S _or the head is allocated to a hub node in_ S _. For all_ (i, i<sup>′</sup> ) ∈ A _and_ S ⊆ V _where_ i ∈ S, i<sup>′</sup> ∈ V/ S _,_ 



<!-- Start of picture text -->
r t ij + rt ji ⩽ � z t ij + � z t i ′ j ′ (35)<br>j∈V/ S j ′ ∈S<br><!-- End of picture text -->

_is a valid inequality._ 

**Corollary 1.** _Constraints_ (7) _are special cases of constraints_ (27) _where_ |S| = 1 

Carroll et al. (2013); Carroll and McGarraghy (2013) defines the _ghost_ ring as follows. We establish the support graph of a fractional solution and identify cycles that are longer than the ring bound, if any. We call these infeasible rings _ghosts_ . In such cases, at least two edges must be removed from every such ring. 



<!-- Start of picture text -->
� re ⩽ |Gr| − max{⌈|Gr|/N max ⌉, 2}, ∀ Ghost ring Gr. (36)<br>e∈γ(Gr)<br><!-- End of picture text -->

**Proposition 8.** _The following inequalities are valid for_ P(MPHLPSD) _:_ 



<!-- Start of picture text -->
� r t a ⩾ i∈S �j�i z N t ij max+ � a∈δ ♦ (S) r a t − � z t ii (37)<br>a∈δ ♦ (S) � � i∈S �<br><!-- End of picture text -->

_for all_ S ⊂ V _. This delivers a lower bound on the number of edges encompassed from a set_ S ⊂ V _, where_ ♦∈ {+, −} _._ 

_Proof._ See the proof in Martín et al. (2014). 

**Proposition 9.** _The following 2-matching constraints for are valid for_ P(MPHLPSD) _in every period_ t _:_ 



<!-- Start of picture text -->
� r t a + � r t a ⩽ � � z t ij + ⌊ |T 2  | ⌋ (38)<br>a∈γ(H) a∈T i∈H j�i<br><!-- End of picture text -->

_for all_ H ⊂ V _and all_ T ⊂ δ<sup>♦</sup> (H) _satisfying, i)_ |{i, j} ∩ H| = 1 _,_ ∀{i, j} ∈ T _, ii)_ |{i, j} ∩ {k, l}| = ∅, {i, j} � {k, l} ∈ T _, and iii)_ |T | ⩾ 3 _and odd._ 

_where_ H ⊂ V _is a handle and_ T ⊂ δ<sup>♦</sup> (H) _are called teeth, where_ ♦∈ {+, −} _._ 

_Proof._ In every feasible solution of this problem we have, 



<!-- Start of picture text -->
2r t (γ(H)) + r t (δ + (H)) + r t (δ − (H)) = �(r t (δ + (i)) + r t (δ − (i)))<br>i∈H<br><!-- End of picture text -->

8 

and from constraints (3) and (4) one obtains: 



<!-- Start of picture text -->
� �(r t kl + rt lk ) ⩽ 2 � (� z t kj ).<br>k∈H l�k k∈H j<br><!-- End of picture text -->

Hence, 



<!-- Start of picture text -->
2 � (� z t kj ) ⩾ 2rt(γ(H)) + rt(δ+(H)) + rt(δ−(H))<br>k∈H j<br><!-- End of picture text -->



<!-- Start of picture text -->
= 2r t (γ(H)) + r t (δ + (H/ T ) + r t (δ + (T )) + r t (δ − (H/ T )) + r(δ − (T ))). (39)<br><!-- End of picture text -->

Given that r<sup>t</sup> (δ<sup>+</sup> (T ) ∪ δ<sup>−</sup> (T )) ⩽ |T | deduced from the bound constraints r<sup>t</sup> a<sup>⩽1and(7),weaddthis set</sup> of constraints to (39) and we obtain: 



<!-- Start of picture text -->
2 � (� z t kj ) + |T | ⩾ 2rt(γ(H)) + rt(δ+(H/ T ) + rt(δ−(H/ T )) + 2rt(δ+(T )) + 2rt(δ−(T )))<br>k∈H j<br>⩾ 2r t (γ(H)) + 2r t (δ + (T )) + 2r t (δ − (T )). (40)<br><!-- End of picture text -->

Again, given that |T | is an odd number, by multiplying both sides by<sup>1</sup> 2<sup>, we conclude,</sup> 



<!-- Start of picture text -->
r t (γ(H)) + r t (δ + (T ) + r t (δ − (T ))) ⩽ � (� z t kj ) + |T | 2  − 1 (41)<br>k∈H j<br><!-- End of picture text -->

and the proof is complete. 

**Proposition 10.** _The following comb inequalities are valid for_ P(MPHLPSD) _: in every period_ t 



<!-- Start of picture text -->
t t<br>� r t a + � � r t a ⩽ � � z t ij + � |Tj| − 3t + 2  1 , (42)<br>a∈γ(H) j=1 a∈γ(Tj) i∈H j j=1<br><!-- End of picture text -->

_for all_ H ⊂ V _and all_ Ti ⊂ V, ∀i ∈ {1, . . ., t} _satisfying, i)_ H, T1, T2, . . ., Tt ⊆ V _, ii)_ Tj \ H � ∅, ∀j ∈ {1, . . ., t} _, ii)_ Tj ∩ H � ∅, ∀j ∈ {1, . . ., t} _, ii)_ Ti ∩ Tj = ∅, ∀j ∈ {1, . . ., t} _, and iii)_ t ⩾ 3 _and odd._ 

_Proof._ For S ⊂ P, in every feasible solution we have, 



<!-- Start of picture text -->
r t (γ(H)) = �(� z t ij ) − rt(δ+(S)) + 2  rt(δ−(S)) , (43)<br>i∈H j<br><!-- End of picture text -->

and for every Tj ⊂ P, j ∈ {1, . . ., t} we have, 



<!-- Start of picture text -->
r t (γ(Tj)) = �(� z t ij ) − rt(δ+(Tj)) + 2  rt(δ−(Tj)) . (44)<br>i∈Tj j<br><!-- End of picture text -->

Furthermore, from (43) and (44), one yields: 



<!-- Start of picture text -->
r t (γ(H)) + � r t (γ(Ti)) = �(� z t ij ) + � �(� z t ij )−<br>i i∈H j j i∈Tj j<br>9<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br> <br>2 �(r t (δ + (Tj)) + r t (δ − (Tj))) (45)<br>(r t (δ + (H)) + r t (δ − (H))) + j  .<br><!-- End of picture text -->

Let δ<sup>+</sup> i<sup>(H)∪δ−</sup> i<sup>(H)denotethecutsetassociatedwitharcshavingoneend-pointinH∩Tiandanother</sup> end-point outside H. We know that r<sup>t</sup> (δ<sup>+</sup> (H)) + r<sup>t</sup> (δ<sup>−</sup> (H)) ⩾<sup>�</sup> i<sup>(rt(δ+</sup> i<sup>(H)) + rt(δ</sup> i<sup>−(H))).</sup> It can be easily shown that (r<sup>t</sup> (δ<sup>+</sup> i<sup>(H)) + rt(δ−</sup> i<sup>(H))) + (rt(δ+(Ti)) + rt(δ−(Ti))) ⩾3.We also know that</sup> r<sup>t</sup> (δ<sup>+</sup> (H))+ r<sup>t</sup> (δ<sup>−</sup> (H)) and r<sup>t</sup> (δ<sup>+</sup> (Ti))+ r<sup>t</sup> (δ<sup>−</sup> (Ti)) are even numbers and therefore r<sup>t</sup> (δ<sup>+</sup> (H))+ r<sup>t</sup> (δ<sup>−</sup> (H))+ �i<sup>(rt(δ+(Ti)) + rt(δ−(Ti))) ⩾3t + 1.By substituting in (45) the proof is complete.</sup> 

**Proposition 11.** _Monemi and Gelareh (2017) proposed the so-called_ moving sub-path inequalities _are valid for_ P(MPHLPSD) _. Let_ r<sup>∗</sup> _be an integer partial solution and a violated inequality of_ (36) _in the form of_ P = (v1, v2, . . ., vm, v1) : m > R _exist. We can identify some minimal subsets of variables (corresponding to a sequence of edges) in such a path for which the ring bound capacity is violated. The following valid inequalities are violated by such a solution:_ 



<!-- Start of picture text -->
� r t e ⩽ Nmax, ∀t, i1 ∈ {v1, v2, . . ., v1 + N max , . . . , vm} : i1 + N max ⩽ m − 1 (46)<br>e={i,i+1}: i∈{i1,...,i1+R}<br><!-- End of picture text -->

_where_ i _is selected as a rolling sequence basis._ 

_Proof._ See Monemi and Gelareh (2017). 

## **5. Solution Method** 

The proposed solution methods can be categorized as a Benders decomposition method. In fact, as it will be shown in this section, a Benders reformulation can help getting rid of O(|N||T ||P|) variables ζ<sup>p</sup> it<sup>as itwill</sup> implicitly take care of their role and logical implications without any need to have them explicitly present in the model and increase computational complexity. In other words, it will be shown that a Benders reformulation in addition to projecting the model onto the space of integer variable can actually help us to get rid of many integer variables that were otherwise inevitable in a compact formulation. 

Benders decomposition (Benders, 1962, 2005) is a primal decomposition method, proven to be a very efficient paradigm in dealing with large-scale MIP models arising in problems within an underlying location/network structures. Benders decomposition is based on projecting the model on the space of complicating variables and exploits the primal/dual relationship with a sub-problem to generate cuts to separate solutions of the master problem and tighten the outer approximation, until optimality is proven as a result of lower and upper bounds converging towards the same value. 

If a solution to the master problem represents direction of an improving ray in the subproblem dual, then one can generate feasibility cuts to avoid such solutions from the master problem otherwise, the primal-dual relationship can be exploited to generate optimality cuts and improve the outer approximation, iteratively. Clearly, the first class of cuts are no-good cuts to prevent infeasible solutions of master problem while the second class tend to push the bound(s) and accelerate convergence. As such, some authors have proposed to replace the actual master problem with an auxiliary/alternative ones making sure that no solution of the master problem can point to a ray direction in the subproblem dual. An example of this can be seen in Gelareh and Nickel (2011), which replaces the master problem with a different model in Maculan et al. (2003) delivering only feasible solutions. This has proven to be very efficient, depending on the way Benders is being implemented —traditional or branch-and-cut style. Other work such as those in Codato and 

10 

Fischetti (2006) and Fischetti et al. (2009) proposed other eliminatory approaches based on _minimal infeasible subsystem_ to cut off bad solutions. 

Tightening Benders standard cuts in Benders has been considered since 80’s where the first efforts were focused on finding non-dominated Benders cuts from among alternative ones resulted by multiple optimality in the subproblem dual. After the pioneering work of Magnanti and Wong (1981) in dealing with degenerate subproblems by sharpening the cuts using _relative interior points_ , Papadakos (2008) showed that the same can be done but with less difficulties —no need for the points to in the relative interior of master problem polytope. Furthermore, Papadakos (2008) proposed an iterative algorithm to update this point. Other general techniques have been proposed such as using heuristic solutions to accelerate convergence (see Sherali and Fraticelli (2002), McDaniel and Devine (1977) and Sherali and Fraticelli (2002) for instance). 

Earlier work on Benders decomposition for variants of hub location problems include Camargo et al. (2008); de Camargo et al. (2009b) for models with emphasis on economies of scale, Gelareh and Nickel (2011), Gelareh et al. (2015b) for single and multiple period hub location problems and Contreras et al. (2011a) for a classical model of the uncapacitated hub location problem. In the recent years, other successful applications have been reported in the literature. 

Some very recent work in literature dealing with Benders technique for variants of hub location problems include Mokhtar et al. (2018) for a 2-allocation p-hub median problem, Rostami et al. (2018) for a single allocation problem under breakdown reliability and Real et al. (2018) for a Gateway Location Problem. 

Rahmaniani et al. (2017) presented a sophisticated analytical literature review of the method and addressed most of the important features. 

Our proposed framework is a branch-cut-Benders approach. The fractional solutions of master problem and those that result in infeasible network structures are cut using efficiently separated valid inequalities at appropriate stages along the branch-and-cur process. We only deliver integer-feasible solutions (feasible network structures with respect to the whole problem) of MP to the Benders subproblem and we do this by efficiently separating the appropriate valid inequalities –from a portfolio of identified ones– to cut the infeasible solution of master problem. In addition, we use an inexpensive heuristic algorithm to generate feasible solutions that warm-start our solution algorithm with an optimality cut corresponding to an integer feasible solution of the heuristic. 

## _5.1. Heuristic solution_ 

Poojari and Beasley (2009) proposed to use meta-heuristics to find feasible solutions, generate Benders and add to the MP before Benders process being started hoping that this warm-start would accelerate the convergence of algorithm. Our extensive computational experiments on a wide range of problems revealed that this strategy is particularly efficient when the original compact formulation is very tight, otherwise, even by supplying the optimal solution one may not see a significant gain in the additional overhead of running this heuristic. Another interesting finding is that, in network design problems with less dense or even sparse flow matrices, this only generates overhead (again this conclusion is limited to the benchmark of our extensive computational experiments). Therefore, it is always wiser to find a trade-off between the quality of solution we expect from the heuristic and the time spent on it. Our extensive computational experiments on a variety of models let us conclude that this heuristic procedure should remain very inexpensive. 

The proposed minimalist local search is the following: Given constraints (18), we serve all nodes in periods 1 and 2, then skip the third period and again repeat this pattern until every node is visited q times. Then in every period, the non-MW nodes with demand volume in the upper N<sup>min</sup> N<sup>arechosentobethe</sup> DCs. The remaining nodes are allocated to the DCs based on the distance (ties are broken in favor of having balanced clusters with respect to the volume of demand) creating routes with N<sup>min</sup> nodes along them. The 

11 

remaining N − ⌊ N<sup>min</sup> N<sup>⌋× NminnodesareaddedonebyonetoeveryDC’scluster.Theroutesarethen</sup> constructed by connecting nodes of every cluster. 

The efficiency in computing the objective function allows us to do certain number (practically, we fixed it to 10000) of iterations for improving the initial solutions. There neighborhood are defined as in the following: (1) reordering the nodes within every route; (2) moving a whole route of a given DC to the periods where no distribution takes place, (3) let any other node in the cluster be the DC and turn the DC to a normal route node, and (4) if there are more than q period within which distribution takes place, a node can move from one period to another period and in any route there. We start the local search with the neighborhood (1) and upon encountering 2N non-improving solutions we move to the next one with the order defined by the number associated to every neighborhood. One may think of it as a naive version of a Variable Neighborhood Search (VNS) (see Hansen et al. (2008) for a general review of the method and Freitas and Penna (2019), Herrán et al. (2019) and Chagas et al. (2019) for instances of recent successful application) even though it not intended to be a full-fledged and mature heuristic or a stand-alone solution methods producing high-quality solutions. 

## _5.2. Initial relaxation_ 

We have chosen the constraints (2), (3), (4), (6), (7), (12), (13), (14), (15), (16), (17) and (18) to constitute the initial relation (or the master problem (MP)). Constraints (5) are excluded and be separated upon need, because in spite the large cardinality of this set of constraints which is O(N<sup>4</sup> T ) and deteriorates the performance of solvers very significantly, only a very tiny fraction of them may be active in an optimal (or any feasible) solution of the problem. 

ζ<sup>p</sup> it<sup>, ∀p, i, tcanbetotallyeliminatedfromtheMPasthesevariablesandallrelatedconstraintsareno</sup> longer required and their presence would be only imposing additional computational burden (branching, reduction, etc.) on the shoulders of the MIP solver solving MP. In fact, once the set of DCs and demand nodes are determined for every period t, the d-th days at which every node is visited becomes known ( _a posteiori_ ) and this information can be observed by the subproblem through the solution provided by MP. Subproblem can then determine the volume of demand to be supplied to every demand point given the percentage corresponding to the p-th visit to the node. 

Let the indicator ∆(p, t, i) be equal to 1, should the time period t correspond to the p-th visit to node i, 0 otherwise. Hence, instead of carrying ζ<sup>p</sup> jt<sup>from master to the subproblem, we may deduct this information</sup> from the resulting network structure of MP. Using this definition, although we can introduce the following capacity constraints and deal with the truck convoy capacity in the subproblem, our extensive computational experiments suggest to keep the fleet sizing part remains in the MP: 



<!-- Start of picture text -->
V cap v t 0k ⩾ �(z t ik + yt ki )wi∆(p, t, i)lp ∀i, t. (47)<br>��k p �<br><!-- End of picture text -->

In the following, we first present some separation algorithms for the Benders cuts and the aforementioned valid inequalities. 

_Separation of Benders cuts._ The remaining constraints of (19)-(25) are handled in Benders Subproblem (SP). The SP is presented in the following: 

## (SP-MPHLPSD) 



<!-- Start of picture text -->
min � � � wjckl t xt jkl<br>t j k!=l<br><!-- End of picture text -->

12 



<!-- Start of picture text -->
+ � � F t 0k v 0 t k (48)<br>t k�MW:MW=0<br>s. t.<br>u 1 : � wjx t j0k = � � lpwj∆(p, t, i), ∀t, j � 0, (49)<br>k�i,0 p k<br>u 2 : � wjx t jkj = � � lpwj∆(p, t, i), ∀t, j � 0, (50)<br>k�j p k<br>u 3 : � wjx t jkl − � wjx t jlk = 0, ∀t, j � 0, k � {i, j}, (51)<br>l�0 l�k,k�0<br>u 4 : x t j0l ⩽ r t 0l , ∀j, t, (52)<br>u 5 : x t jkl ⩽ r t kl + y t kl , ∀t, j, k � j, l � k, (53)<br>u 6 : x t jkl ⩽ � z t kj , ∀t, j, k � j, l � k, (54)<br>j<br>x t jklt ∈ (0, 1)|V|3|T |, v0kt ∈ N|v||T |. (55)<br><!-- End of picture text -->

Let η be the continuous variable providing an underestimation of the Subpoblem objective function, the optimality Benders cut looks like the following: 



<!-- Start of picture text -->
η ⩾ � u 1 jt � � lpwjz p jkt + � u 2 jt � � lpwjz p jkt + � u 4 jt r0lt<br>t,j�0 p k t,j�0 p k t,j�0<br>+ � u 5 jklt (rklt + yklt) + u6 jklt ( � z t km ) . (56)<br>t,j,k�j,k>0,l�k � m �<br><!-- End of picture text -->

and the feasibility cut follows: 



<!-- Start of picture text -->
0 ⩾ � u 1 jt � � lpwjz p jkt + � u 2 jt � � lpwjz p jkt + � u 4 jt r0lt<br>t,j�0 p k t,j�0 p k t,j�0<br>+ � u 5 jklt (rklt + yklt) + u6 jklt ( � z t km ) . (57)<br>t,j,k�j,k>0,l�k � m �<br><!-- End of picture text -->

However, as any infeasible network structure is separated using non-Benders cuts, we will not need to separate any Benders feasibility cut. 

On the other hand, as variables y<sup>t</sup> ii<sup>donotappearintheaforementionedBenderscuts,andwewould</sup> like to capture as many variables as possible from among those of MP into different cuts, the following substitution is proposed leading to cuts that also accommodate yii and yij: 

For constraints (19)-(20) we have: 



<!-- Start of picture text -->
y t jj + � z t jk = � ζ p jt ⇒ � wjxj0kt = � � lpwj∆(p, t, i)(y t jj + � z t jk ), ∀j, t, (58)<br>k p k�i,0 p k k<br>y t jj + � z t jk = � ζ p jt ⇒ � wjxjkjt = � � lpwj∆(p, t, i)(y t jj + � z t jk ), ∀j, t, (59)<br>k p k�j p k k<br>�(y t kj + zt jk ) = � ζ p jt ⇒ � wjxj0kt = � � lpwj∆(p, t, i)(�(y t kj + zt jk ) + � z t jk ), ∀j, t, (60)<br>k p k�i,0 p k k k<br>13<br><!-- End of picture text -->



<!-- Start of picture text -->
�(y t kj + z jk t ) = � ζ p jt ⇒ � wjxjkjt = � � lpwj∆(p, t, i)(�(y t kj + z jk t ) + � z t jk ). ∀j, t. (61)<br>k p k�j p k k k<br><!-- End of picture text -->

In this way, one can also accommodate variables y<sup>t</sup> ii<sup>, yt</sup> ji<sup>,∀i, j, t in the separated Benders cuts.From (58)</sup> - (61) the following optimality cuts are deduced (feasibility cuts follow the same style): 



<!-- Start of picture text -->
η ⩾ � u 1 jt � � lpwj(yii t + � z t ik ) + � u 2 jt � � lpwj(yii t + � z t ik )<br>t,j�0 p k k t,j�0 p k k<br>+ � u 4 jt r0lt + � u 5 jklt (rklt + yklt) + u jklt 6 ( � z t km ) (62)<br>t,j�0 t,j,k�j,k>0,l�k � m �<br>η ⩾ � u 1 jt � � lpwj(�(y t kj + zt jk )) + � u 2 jt � � lpwj(�(y t kj + zt jk ))<br>t,j�0 p k k t,j�0 p k k<br>+ � u 4 jt r0lt + � u 5 jklt (rklt + yklt) + u6 jklt ( � z t km ) (63)<br>t,j�0 t,j,k�j,k>0,l�k � m �<br><!-- End of picture text -->

Our extensive computational experiments does suggest the use of both type of optimality cuts (56) and (62)-(63). 

_Multi-Cut Benders decomposition._ A closer look at the subproblem and the Benders cut (56) reveals that the subproblem can be solved for every period independently and as a result one can generate up to |T | cut per subproblem. Let η<sup>t</sup> ⩾ 0 and η =<sup>�</sup> t<sup>ηt,where ηt⩾0underestimates the costcorresponding tothe period</sup> t, one can disaggregate the Benders cuts into: 



<!-- Start of picture text -->
η t ⩾ � u 1 jt � � lpwj(yi t + � z t ik ) + � u 2 jt � � lpwj(yii t + � z t ik )<br>j�0 p k k j�0 p k k<br>+ � u 4 jt r0lt + � u 5 jklt (rklt + yklt) + u6 jklt ( � z t km ) . ∀t, (64)<br>j�0 j,k�j,k>0,l�k � m �<br><!-- End of picture text -->

Multi-cut for the feasibility cut follows the same algebra. 

## _5.3. Cutting plane_ 

_Separation of valid inequalities_ (27) _._ The separation of this class of valid inequalities is reduced to solving a Knapsack Problem (KP) with two additional constraints. The weights of items correspond to r<sup>t</sup> ij<sup>.For every t</sup> we solve: 



<!-- Start of picture text -->
max � bi<br>i<br>s.t. � r t ij sij ⩾ � bi + ǫ<br>i,j i<br>sij ⩽ bi ∀i, j<br>sij ⩽ bj ∀i, j<br>bi, si,j ∈ {0, 1} (65)<br><!-- End of picture text -->

Any feasible solution to this problem identifies a set S<sup>t</sup> = {i : bi = 1, ∀i}, ∀t that is used to separate the corresponding valid inequalities from (27) (see Gendreau et al. (1998) for a different method). 

14 

_Separation of valid inequalities_ (28) _and_ (29) _._ At every period t, let s be a dummy node, V<sup>t</sup> be the set of nodes visited and G<sup>′t</sup> (V<sup>t</sup> ∪ {s}, A<sup>′t</sup> ) a directed graph. Establish an arc from s to every j with capacity z<sup>t</sup> ij<sup>,</sup> if z<sup>t</sup> ij<sup>>0.Then,addanarc(i, j)withcapacity</sup> r<sup>t</sup> ij<sup>for</sup> r<sup>t</sup> ij<sup>>0.Now,inthisperiodt,ifwepumpaflow</sup> from s and destined to a node i, then i must receive a volume of flow equivalent to<sup>�</sup> j z<sup>t</sup> ij<sup>.AsetS⊂Vt</sup> where i ∈ S, s � S defines a cut of δ<sup>+</sup> (S)(δ<sup>−</sup> (S)) if the cut capacity is less than<sup>�</sup> j z<sup>t</sup> ij<sup>.Swilldelivervalid</sup> inequalities of (28) ((29)). The complexity of separation relies on Edmonds-Karp max-flow. 

_Separation of valid inequalities_ (30) _and_ (31) _._ At every period t, let G<sup>′′t</sup> (V<sup>t</sup> , A<sup>′′t</sup> ) be defined as following: V<sup>t</sup> is the set of nodes visited and A<sup>′′t</sup> is composed of arcs (i, l) for which r<sup>t</sup> il<sup>+</sup> z<sup>t</sup> i<sup>′</sup> l<sup>> 0, arcs (i′, l) for which</sup> r<sup>t</sup> i<sup>′</sup> l<sup>+</sup> z<sup>t</sup> il<sup>>0andallotherarcs(k, l)where</sup> r<sup>t</sup> kl<sup>>0.AsetS⊂Vtdefinesacut,ifthemax-flowisless</sup> than<sup>�</sup> j∈V/ S z<sup>t</sup> ij<sup>+ �</sup> j<sup>′</sup> ∈ S z<sup>t</sup> i<sup>′</sup> j<sup>′wherei∈S, j∈Vt/S.S,Vt/S wherei∈S,j∈Vt/Sdeliversthe valid</sup> inequalities (30) and (31). One can either use Edmonds-Karp or Boykov and Kolmogorov (2001) max-flow algorithms. 

_Separation of valid inequalities_ (33) _._ In order to identify the violated inequalities of this type, it is suggested in Martín et al. (2014) to look for a cut set S of the support graph G<sup>′′′t</sup> (V<sup>t</sup> , A<sup>′′′t</sup> ) or in V<sup>t</sup> / S. Therefore in parallel with our search for the violated inequalities of (28) (29), (30) and (31), we also use the identified cut-set, say S, to search for possible violation of (33). The complexity again depends on the max-flow algorithm of Edmonds-Karp or Boykov and Kolmogorov (2001). 

_Separation of valid inequalities_ (34) _._ Our extensive computational experiment reveals that the efforts invested in the separation of inequalities for |P| ⩾ 2 do not pay off (similar conclusion has been drawn in Labbé et al. (2004)). Therefore, we would prefer to stick to the existing constraints (5). 

_Separation of valid inequalities_ (35) _._ The separation of such constraints is similar the one in Martín et al. (2014). In period t, let S = {i} ∪ {j ∈ V<sup>t</sup> − {i<sup>′</sup> } : z<sup>t</sup> ij<sup>⩾zt</sup> ij<sup>},for agivenarc(i, i′).According toMartínet al.</sup> (2014), if the inequality is not violated for this choice of S, it is neither violated for any other set S<sup>′</sup> . The complexity is O(N<sup>3</sup> ). 

_Separation of valid inequalities_ (36) _._ In period t, we establish a support graph G<sup>t‡</sup> = (V<sup>t‡</sup> , A<sup>t‡</sup> ) where V<sup>t‡</sup> is composed of all a ∈ A<sup>t</sup> for which r<sup>t</sup> a<sup>∗> 0.We then enumerate all the cycles in such a graph using Tiernan’s</sup> method (see Tiernan (1970)) and examine every cycle to identify the violated cuts. When enumerating all the cycles, one may also examine the violation of the inequalities (46). 

_Separation of valid inequalities_ (37) _._ In every period t, we can rewrite (37) as (N<sup>max</sup> − 1)<sup>�</sup> e∈δ<sup>+</sup> (S)<sup>r</sup> a<sup>t+</sup> N<sup>max �</sup> i∈S<sup>z</sup> ii<sup>t⩾�</sup> i∈S �j�i<sup>zt</sup> ij<sup>or (Nmax−1)�</sup> e∈δ<sup>+</sup> (S)<sup>r</sup> a<sup>t+Nmax �</sup> i∈S<sup>z</sup> ii<sup>t+�</sup> i�S �j<sup>zt</sup> ij<sup>⩾�</sup> i∈V �j<sup>zt</sup> ij<sup>.</sup> These can now be separated in the same way as the SEC in the traveling salesman problem. We establish a support graph G<sup>t§</sup> = (V<sup>t§</sup> , A<sup>t§</sup> ) where V<sup>t§</sup> = V<sup>t</sup> ∪ {s, d} where s and d are two dummy nodes and A<sup>t§</sup> is composed of the following edges: 1) all arcs a ∈ A<sup>t</sup> with capacity N<sup>max</sup> − 1 for all r<sup>t</sup> a<sup>>0,2)thearcs</sup> (s, i), ∀i ∈ V<sup>t</sup> with capacity N<sup>max</sup> z<sup>t</sup> ii<sup>, and 3) the edges {i, d},∀i ∈Vtwith capacity �</sup> j<sup>zt</sup> ij<sup>.A set Stwhere</sup> s ∈ S<sup>t</sup> , d � S represents a set that can potentially give a violated valid inequality (37). The complexity of this separation is equivalent to the complexity of an s-d min-cut algorithm called on G<sup>t§</sup> . 

_Separation of valid inequalities_ (38) _._ While Fischetti et al. (1998b) and other researchers proposed several heuristic separation algorithms for such constraints, our initial computational experiments suggested using the method of Padberg and Rao (1982) for separating such valid inequalities in every period t. 

_Separation of valid inequalities_ (42) _._ while polynomial-time algorithms exists for separation of these inequalities (see Letchford and Lodi (2002)) our initial computational experiments trades polynomial-time algorithm for the block decomposition technique. Therefore, we find combs using Concorde implementation (see (Applegate et al., 2007) and Cook’s). 

15 

_Separation of valid inequalities_ (46) _._ In every period t, at any integer node where an inequality of form (36) is violated, every sub-path of length N<sup>max</sup> + 1 represents such a valid inequality and is violated by 1. This separation can be done in O(n<sup>2</sup> ). 

## _5.4. Branch-and-cut algorithm_ 

As mentioned earlier, our emphasis in our branch-and-bound is on a balance between a fast lower bound improvements and quickly finding feasible solution. For that, we separate all possible violated cuts at the root node. If no inequality from among the non-Benders ones has been found we then generate Benders cuts. 

Due to the way we dealt with ζ<sup>p</sup> it<sup>variablesasindicators,themethodproposedinPapadakos(2008)</sup> becomes less intuitive. We therefore, used an alternative method as follows: Once the subproblem is solved to optimality, we move over the face of optimality and choose a solution that minimized the sum of dual values corresponding to the equality constraint (i.e., **u**<sup>**1**</sup> + **u**<sup>**2**</sup> ). This has shown to be promising. In a gap of less than 5%, we do not separate any cut for the fractional solutions. We also opted to branch on z variables first even though one may argue that r seems more trivial candidates but our choice has been confirmed by an extensive computational experiments. 

## _5.5. Preprocessing_ 

Some practice-driven rules can be used to fix some variables in the model one of which would be the following: For every node i and j = argmax cij, we can fix tij, rji, yij and yji to 0. 

## **6. Computational experiments** 

The `BENMIP` framework is written in C++ and can be compiled both in Windows (Microsoft C++ compiler) and in Linux (Ubuntu). For this project, we compile `BENMIP` using the VC++ (Visual Studio 2017) compiler in Windows 10 and run on a personal computer with an Intel Core i7-6700K CPU, 4.0 GHz and 32 GB of RAM. CPLEX 12.8 is used as an MIP solver. The max-flow algorithms are solved using the Boost library implementation of the Edmonds-Karp algorithm for directed graphs. 

Except for the case study, other instances are generate randomly for a network of size 100 nodes using the kind of aggregation proposed by Ernst and Krishnamoorthy (1996) to establish grids on the map and introduce new virtual nodes as the centers of gravity of cells in the grid with a demand equal to that of all the nodes within the grid cell. The demands are also generated randomly within the min/max range data of the case study. The random generation has been done with the aim of avoiding any obvious structure in the distance and demand matrices. 

In both cases, the transportation cost accounts for the fuel consumption per 100 km for the design speed of the a trucks. We also assumed that the fleet of transporters is homogeneous one and therefore the fuel consumption pattern is the almost the same across the fleet and corresponds to 24 liters per 100 kilometers for the type of trucks being deployed. The penalty for the supply to the isolated nodes is been set to 2 (we will see in the case study section that we use the same factor over there as well). 

Some CPLEX parameters are the following: `IloCplex::MIPEmphasis` has been set to `CPX_MIPEMPHASIS_BALANCED` . The custom termination criteria for CPLEX (UserAbort) is the following: we terminate CPLEX if a maximum of 30 hours (108000 seconds) of CPU time is passed and an incumbent solution has been identified. After an extensive preliminary computational experiments, we realized that for many instances, the time limit is reached while more than 90% of the time (currently marked by ’OptimTol’) has been spent on closing the last 0.5% gap (reducing the gap from 0.5% to zero to prove the optimality). We therefore decided to modify the criteria by adding an optimality tolerance of 0.5%. The results reported here use this combined termination criteria. 

16 

|# days|# Fraction of demand per day|
|---|---|
|1|100%|
|2|50% and 50%|
|3|38%, 24% and 38%|
|4|31%, 21%, 14% and 34%|
|5|23%, 18%, 18%, 20% and 21%|
|6|21%, 14%, 13%, 14%, 18% and 20%|
|7|19%, 13%, 12%, 13%, 13%, 12% and 18%|



**Table 4:** The demand patter for different planning horizon lengths (rounded to integer values). 

|T | is chosen from the set {3, 5, 7, 9} due to the intractability of problem. As long as Benders decomposition is concerned, we only separate cuts upon finding an optimal integer proposal being found by CPLEX. Other cuts are separated at root node and later on every 10 nodes (fractional or integer) and any integer node. The tolerance ǫ = 10<sup>−4</sup> was set as the threshold of violation of separated valid cuts. Our extensive computational experiments confirmed that the approach itself is sufficiently efficient and that further efforts to generate sharper cuts from the SP only add extra overheads without making any significant improvements. Moreover, N<sup>min</sup> and N<sup>max</sup> are set to 3 and 5, respectively, as it is less realistic to visit more than 4 locations (other that the DC itself) per day and is less likely to deploy a fleet for only 1 or two nodes on a route. 

The demand pattern (user’s behavior) for different length of planning horizon is reported in Table 4. Those rows for 6 and 7 days are obtained through simulation as we only had access to 1-5 days behavior pattern in our case study. The interpretations follows: assuming 3 deliveries, 38% of the refugees collect their demands on the first day, 24% collect on the second day and 38% on the last day. Our problem considers a planning horizon of at least 5 days long and minimum three deliveries. 

We deactivated several internal cut generation procedures of CPLEX. These include FlowCovers, FlowPaths, MIRCuts, FracCuts, LiftProjCuts, Cliques, Covers, FlowCovers, GUBCovers, FracCuts, MIRCuts, DisjCuts, ZeroHalfCuts and MCFCuts. We turned off all the presolved phases to avoid premature convergence in Benders. 

In Table 5, we report our computational experiments. The first column represents the instance name in the format ’N, T , q’, where N and T refer to the number of nodes and number of periods, and q represents the required number of visits, respectively. The column ’CPLEX’ represents the results of direct application of CPLEX to solve the instance with a time limit of 30 hours. In the column ’TimeIP’, we report the elapsed time for solving the problem at hand before CPLEX terminated. The column ’Nnodes’ represents the number of processed nodes. The columns ’Gap’ and ’MIPStatus’ stand for the integrality gap and the CPLEX status, respectively. The best known objective value (proven optimal when gap equals 0) is presented in the column ’bestObj’. In the column ’NUserCuts’, we report the number of user cuts added in the course of the branch, Benders and cut approach. 

As depicted in Table 5, using our branch, cut and Benders (BCB), we are able to solve to optimality, instance with up to 45 nodes, 9 periods and 5 visits in a very reasonable amount of time. From 57 nodes and 9 periods, up to 75 nodes and 9 periods, the optimal tolerance of 0.5% is met and for the remaining instances, bCB process failed. At the same time, given the time limit of 108,000 seconds, CPLEX can only solve 1 instance to optimality, six instances to a gap less than 1 percent within the time limit and all other cases failed even to produce any feasible solution. 

While number of separated user cuts, including Benders and non-Benders cuts –even for larger size instance– remains reasonable for smaller size instances (smaller N × T × q), this becomes excessively higher for larger size instances. The number of processed nodes is reasonable and the number of separated cuts is increasing as N × T increases. This makes the LP increasingly difficult to resolve. 

17 

We tried to let the algorithm continue even further beyond this time, but the additional time spent did not pay off with any better solution quality. The numbers of separated valid inequalities and Benders cuts are rather reasonable and increase as the size of the instance increases. 

In general, we are able to solve relatively large size instances to less than 0.5% gap and in reasonable time. 

|N, T, q|CPLEX|TimeMIP|Nnodes|Gap|IPStatus|bestObj|NUserCuts|
|---|---|---|---|---|---|---|---|
|15, 5, 3|TL (⩽1%)|7.994|180|0.00|**Optimal**|84080.337|451|
|15, 5, 5|TL (⩽1%)|12.457|3600|0.00|**Optimal**|111658.915|1249|
|20, 5, 3|TL (⩽1%)|10.673|4560|0.00|**Optimal**|37523.286|521|
|20, 7, 5|TL (⩽1%)|19.997|100|0.00|**Optimal**|76397.008|61|
|25, 5, 3|TL (⩽1%)|21.287|1950|0.00|**Optimal**|84241.285|198|
|25, 7, 5|TL (⩽1%)|27.476|12000|0.00|**Optimal**|125209.490|1049|
|25, 9, 7|Failed|27.559|6300|0.00|**Optimal**|113419.935|8247|
|30, 5, 3|Failed|42.306|10350|0.00|**Optimal**|43762.929|78|
|30, 7, 5|Failed|42.766|21750|0.00|**Optimal**|162934.996|1687|
|30, 9, 5|Failed|52.454|14280|0.00|**Optimal**|228946.761|10834|
|30, 9, 7|Failed|51.198|23220|0.00|**Optimal**|189169.091|24173|
|35, 5, 3|Failed|66.435|3675|0.00|**Optimal**|244242.668|264|
|35, 7, 5|Failed|85.371|8750|0.00|**Optimal**|62413.852|2243|
|35, 9, 5|Failed|127.431|34545|0.00|**Optimal**|260694.174|10386|
|35, 9, 7|Failed|158.242|16380|0.00|**Optimal**|197920.988|49094|
|40, 5, 3|Failed|114.198|17040|0.00|**Optimal**|199238.713|380|
|40, 7, 5|Failed|104.832|1400|0.00|**Optimal**|221238.622|2864|
|40, 9, 7|Failed|146.383|21840|0.00|**Optimal**|99243.650|9397|
|40, 11, 9|Failed|201.236|57240|0.00|**Optimal**|113640.182|48738|
|45, 5, 3|Failed|151.405|23490|0.00|**Optimal**|133406.385|157|
|45, 7, 5|Failed|274.801|11475|0.00|**Optimal**|141642.879|944|
|45, 9, 5|Failed|226.616|18270|0.00|**Optimal**|248718.573|2069|
|45, 9, 7|Failed|276.357|81405|0.22|OptimTol|324613.570|10625|
|50, 5, 3|Failed|201.975|4800|0.40|OptimTol|319585.176|569|
|<br>50, 7, 5|Failed|247.583|34500|0.33|OptimTol|317347.706|775|
|50, 9, 5|Failed|460.927|48300|0.24|OptimTol|188794.955|11819|
|50, 9, 7|Failed|643.601|92700|0.28|OptimTol|161583.087|15033|
|55, 5, 3|Failed|437.192|32670|0.21|OptimTol|240662.953|682|
|55, 7, 5|Failed|528.991|70125|0.21|OptimTol|272452.559|2326|
|55, 9, 5|Failed|546.226|32725|0.19|OptimTol|209048.260|8273|
|55, 9, 7|Failed|1083.283|90090|0.23|OptimTol|290939.990|7160|
|60, 5, 3|Failed|642.872|43920|0.45|OptimTol|97707.369|189|
|60, 7, 5|Failed|791.262|39900|0.22|OptimTol|285251.915|3169|
|60, 9, 5|Failed|1088.335|40740|0.55|OptimTol|205488.432|11111|
|60, 9, 7|Failed|1689.299|26460|0.23|OptimTol|128652.405|40725|
|65, 5, 3|Failed|1185.403|62400|0.21|OptimTol|565340.164|552|
|<br>65, 7, 5|Failed|1559.322|39650|0.44|OptimTol|226975.650|2030|
|65, 9, 5|Failed|2649.085|111930|0.17|OptimTol|180398.160|7695|
|<br>65, 9, 7|Failed|2460.353|90090|0.20|OptimTol|124551.237|34168|
|70, 5, 3|Failed|1500.802|41370|0.31|OptimTol|291988.072|521|
|70, 7, 5|Failed|2024.516|3850|0.24|OptimTol|356038.449|1239|



18 

|N, T, q|CPLEX|TimeMIP|Nnodes|Gap|IPStatus|bestObj|NUserCuts|
|---|---|---|---|---|---|---|---|
|70, 9, 5<br>70, 9, 7|Failed<br>Failed|3229.132<br>4981.246|79380<br>115290|0.18<br>0.18|OptimTol<br>OptimTol|212206.747<br>316362.074|11906<br>50449|
|75, 5, 3|Failed|4710.788|29925|0.18|OptimTol|374935.459|186|
|75, 7, 5|Failed|4032.050|65250|0.15|OptimTol|209856.169|2870|
|75, 9, 5|Failed|6931.777|182700|0.18|OptimTol|545603.181|5818|
|75, 9, 7|Failed|8153.850|122175|0.17|OptimTol|219288.648|15106|
|80, 5, 3|Failed|5456.438|62640|4.64|Failed|382013.703|277|
|80, 7, 5|Failed|7715.971|116400|1.01|Failed|643062.686|2374|
|<br>80, 9, 5|Failed|10511.407|100800|1.04|Failed|340879.407|8450|
|80, 9, 7|Failed|8042.656|25200|1.20|Failed|373209.248|1299|
|85, 5, 3|Failed|10046.642|99705|1.28|Failed|417598.357|205|
|85, 7, 5|Failed|9325.384|15300|23.47|Failed|751982.377|3078|
|<br>85, 9, 5|Failed|17163.296|111860|1.62|Failed|373611.634|8838|
|<br>85, 9, 7|Failed|12968.537|21420|1.27|Failed|560609.787|30600|
|90, 5, 3|Failed|20909.273|30510|1.12|Failed|250690.119|519|
|90, 7, 5|Failed|17782.017|202050|1.93|Failed|369989.614|179|
|90, 9, 5|Failed|17509.658|10080|6.71|Failed|651969.202|2819|
|90, 9, 7|Failed|36566.741|281880|1.61|Failed|226597.933|19589|
|95, 5, 3|Failed|24118.205|9405|2.80|Failed|407999.198|155|
|95, 7, 5|Failed|22318.252|2375|1.78|Failed|314163.261|2627|
|95, 9, 5|Failed|34497.094|93100|7.83|Failed|171951.665|129|
|95, 9, 7|Failed|42681.357|213750|4.68|Failed|891420.488|46152|
|100, 5, 3|Failed|37314.855|13500|4.36|Failed|288486.917|474|
|100, 7, 5|Failed|59853.853|80500|1.52|Failed|211461.544|617|
|100, 9, 5|Failed|70290.977|319200|6.44|Failed|433505.924|4487|
|100, 9, 7|Failed|57030.752|317700|2.88|Failed|547141.994|47010|



**Table 5:** Branch, Benders and Cut for the small to mid-size instances. 

## _6.1. Case study_ 

The Lebanese case study is composed of 26 nodes as the centers of districts and one main warehouse (MW) —27 nodes in total. The planning horizon is a week (five working days, T = 5) and every node is served in three different days, i.e. q = 3. In Table 6, the first column represents name, followed by lat/lon coordinates and the last column representing population size. In all figures, we use ’0’ (zero in the darker box) to refer to MW and all others numbers follow the order in this table. The distance table is calculated from the road transport distance (queried using Google API). As before, we assumed a homogeneous fleet of trucks and therefore the fuel consumption is approximately the same for all the trucks and equivalent to 24 litter per 100 KM. We further assumed that penalty factor for not serving a node directly is equal to 2.0 —twice more expensive per unit of volume per kilometer compared to the normal service. 

The reported solution is an optimal solution of the case-study with 26 nodes. 

The DCs and isolated node for every day are reported in Table 7 and Table 8: 

19 

|District|Name|LAT|LON|Population|
|---|---|---|---|---|
|1|Akkar|34.55495|36.19510|143,634|
|2|El Batroun|34.25484|35.65896|20,260|
|3|Bcharre|34.25043|36.01056|3,945|
|4|El Koura|34.33810|35.80584|23,097|
|5|El Minieh-Dennie|34.41000|35.96000|81,668|
|6|Tripoli|34.44536|35.82251|76,018|
|6|Zgharta|34.39630|35.89580|17,775|
|7|Rachaya|33.52851|35.89803|14,393|
|8|West Bekaa|33.42000|35.85000|91,054|
|10|Zahle|33.84756|35.90271|241,235|
|11|Baalbek|34.00965|36.21171|172,115|
|12|El Hermel|34.39620|36.38704|8,652|
|13|Beirut|33.89592|35.47843|37,271|
|14|Aley|33.80780|35.60502|86,069|
|15|Baabda|33.83392|35.54435|128,878|
|16|Chouf|33.89016|35.49363|73,270|
|17|El Meten|33.89190|35.56300|75,314|
|18|Jbeil|33.89937|35.49675|9,347|
|19|Kesrwane|34.01323|35.80083|23,641|
|20|Jezzine|33.54393|35.58439|4,379|
|21|Saida|33.56142|35.37661|62,557|
|22|Sour|33.27212|35.19640|39,573|
|23|Bent Jbeil|33.11894|35.43411|11,329|
|24|Hasbaya|33.39801|35.68202|8,020|
|25|Marjaayoun|33.24016|35.44718|10,371|
|26|El Nabatieh|33.38113|35.48260|36,136|



**Table 6:** Distribution of refugees in 26 Lebanese districts. 

20 





<!-- Start of picture text -->
(a)  Monday. (b) Tuesday.<br>(c)  Wednesday. (d)  Thursday.<br>21<br><!-- End of picture text -->

**(e)** Friday. 

**Figure 5:** An optimal solution of network in our case study. 

|Day|DCs|
|---|---|
|Monday|6,**9**,**10**,**15**,|
|Tuesday|5,**9**,**10**,**15**,**16**,**26**,|
|Wednesday|**9**,**10**,|
|Thursday|**7**,**16**, 25,|
|Friday|**7**,**15**,**16**, and**26**|



**Table 7:** The DCs in the optimal solution of Lebanese case study. 

|Day|Isolated nodes|
|---|---|
|Monday|[**3**](10), [20,21] (15), [**23**](9),|
|Tuesday|[1,**12**](5), [**3**](10), [**2**](16), [**22**,25](26),|
|Wednesday|[**23**](9), [**3**](10),|
|Thursday|[**2**,**12**](7), [**22**](25),|
|Friday|[**12**](7), [20](15), [**2**](16), and [**22**](26)|



**Table 8:** The isolated nodes in the optimal solution of Lebanese case study. 

At least two and at most 6 DCs are planned for every day. The nodes 10 (Zahle), 15 (Baabda) and 16 (Chouf) are appearing as DCs in all q times. These nodes are among the top 10 nodes with respect to the demand size. The node 10 (Zahle) is the node with highest demand while 16 (Chouf) and 15 (Baada) are among the nodes with high demand —even though not the highest. One observes in Figure 5 that, geographically speaking, these nodes are located at the interior par of the convex hull of the selected nodes of every service day. A combination of higher demand and median-like property encourage them to be the DCs of the days. 

As per Table 8, between 2 and 6 nodes are considered as isolated nodes in daily services. The nodes 2 (El Batroun), 3 (Bcharre), 12 (El Hermel) and 23 (Bent Jbeil) are among the nodes with lowest demands (among the 10 lowest in the table) and are designated as isolated in all q times visit. Moreover, as can be observed in Figure 5, geographically speaking, these nodes are located at the perimeter (say are the outliers) of the selected nodes of every service day. lower volume of demand and the geographical position of nodes is an important factor in designating them as isolated nodes in an optimal solution. 

## **7. Summary and Conclusion** 

We proposed the first _Multiperiod Hub Location Problem with Serial Demand (MPHLPSD)_ accommodating user’s demand pattern, and formulated it as a MILP. We showed that the problem of distributing humanitarian aids could be formulated as such a problem. We further showed that a Benders formulation of problem can help getting rid of some unnecessary variables and benefit from logical relationships among variables. Several classes of valid inequalities and efficient separation routines have been identified, which resulted in an efficient branch-and-cut and Benders approach capable of solving relatively lager size instances, which are far too challenging for general-purpose solvers. We also showed that while a general-purpose solver is often unable to even find a feasible solution for instances of this problem, such a solution can be generated easily and be used to warm start our branch, cut and Benders method. On a set of randomly generated instances we have tested our solution algorithm and the obtained numerical results, compared to the results obtained from CPLEX, showed a great success. Also, on a real-life case study we reported optimal solution and it revealed some very interesting observations. As a future interesting aspect, one may think of investigating the outcome of applying this method of planning the delivery network, to analyse whether following 

22 

this plan may also have any direct effect on the everyday life of refugees residing on the covered camps or not. 

From the technical and methodological points of view, further research directions include polyhedral analysis. Specially, identifying new tightening valid inequalities could count as an objective. Also, improving the performance of separation routines is of importance. Moreover, the hybridization of metaheuristic and exact methods, which can deliver solutions with known quality, deserves a great attention. From a more contextual point of view, another opportunity to investigate more in this problem is to undertake a sensitivity analysis to detect the system’s milestones and improve the efficiency and the reliability of the distribution system. Indeed, this is also desired to develop new solution algorithms to solve larger and more complicated instances of the problem. 

## **8. Acknowledgments** 

## **References** 

- Abdinnour-Helm, S., Venkataramanan, M., 1998. Solution approaches to hub location problems. Annals of Operations Research 78, 31–50. 

Alumur, S., Kara, B.Y., 2008. Network hub location problems: the state of the art. European Journal of Operational Research 190, 1–21. Alumur, S.A., Nickel, S., da Gama, F.S., 2012. Hub location under uncertainty. Transportation Research Part B: Methodological 46, 529 – 543. An, Y., Zhang, Y., Zeng, B., 2015. The reliable hub-and-spoke design problem: Models and algorithms. Transportation Research Part B: Methodological 77, 103–122. Applegate, D.L., Bixby, R.E., Chvatal, V., Cook, W.J., 2007. The Traveling Salesman Problem: A Computational Study (Princeton Series in Applied Mathematics). Princeton University Press, Princeton, NJ, USA. Aykin, T., 1994. Lagrangian relaxation based approaches to capacitated hub-and-spoke network design problem. European Journal of Operational Research 79 (3), 501–523. Benders, J., 2005. Partitioning procedures for solving mixed-variables programming problems. Computational Management Science 2, 3–19. 

Benders, J.F., 1962. Partitioning procedures for solving mixed-variables programming problems. Numerische mathematik 4, 238–252. Boonmee, C., Arimura, M., Asada, T., 2017. Facility location optimization model for emergency humanitarian logistics. International Journal of Disaster Risk Reduction 24, 485 – 498. 

Boykov, Y., Kolmogorov, V., 2001. An experimental comparison of min-cut/max-flow algorithms for energy minimization in vision, in: Energy minimization methods in computer vision and pattern recognition, Springer. pp. 359–374. 

de Camargo, R., Jr., G.M., Ferreira, R., Luna, H., 2009a. Multiple allocation hub-and-spoke network design under hub congestion. Computers & Operations Research 36, 3097 – 3106. New developments on hub location. 

- de Camargo, R.S., Miranda, G., 2012. Single allocation hub location problem under congestion: Network owner and user perspectives. Expert Systems with Applications 39, 3385–3391. 

- Camargo, R.S., Miranda Jr., G., Luna, H.P., 2008. Benders decomposition for the uncapacitated multiple allocation hub location problem. Computers & Operations Research 35, 1047–1064. 

de Camargo, R.S., de Miranda Jr, G., Luna, H.P.L., 2009b. Benders decomposition for hub location problems with economies of scale. Transportation Science 43, 86–97. 

- Campbell, J., Ernst, A., Krishnamoorthy, M., 2005b. Hub arc location problems: Part ii - formulations and optimal algorithms. Management Science 51 (10), 1556–1571. 

- Campbell, J., Stiehr, G., Ernst, A., Krishnamoorthy, M., 2003. Solving hub arc location problems on a cluster of workstations. Parallel Computing 29 (5), 555–574. 

Campbell, J.F., 1990. Locating transportation terminals to serve an expanding demand. Transportation Research Part B: Methodological 24, 173–192. 

- Campbell, J.F., Ernst, A.T., Krishnamoorthy, M., 2002. Hub location problems, in: Drezner, Z., Hamacher, H.W. (Eds.), Facility Location: Applications and Theory. Springer, pp. 373–407. 

Campbell, J.F., O’Kelly, M.E., 2012. Twenty-five years of hub location research. Transportation Science 46, 153–169. 

- Cánovas, L., García, S., Marín, A., 2007. Solving the uncapacitated multiple allocation hub location problem by means of a dual-ascent technique. European Journal of Operational Research 179, 990–1007. 

- Carroll, P., Fortz, B., Labbé, M., McGarraghy, S., 2013. A branch-and-cut algorithm for the ring spur assignment problem. Networks 61, 89–103. 

23 

Carroll, P., McGarraghy, S., 2013. A decomposition algorithm for the ring spur assignment problem. International Transactions in Operational Research 20, 119–139. Chagas, J.B.C., Silveira, U.E.F., Santos, A.G., Souza, M.J.F., 2019. A variable neighborhood search heuristic algorithm for the double vehicle routing problem with multiple stacks. International Transactions in Operational Research 0. doi: `10.1111/itor.12623` . Charles, A., Lauras, M., Van Wassenhove, L.N., Dupont, L., 2016. Designing an efficient humanitarian supply network. Journal of Operations Management 47-48, 58 – 70. Codato, G., Fischetti, M., 2006. Combinatorial Benders’ cuts for mixed-integer linear programming. OPERATIONS RESEARCHBALTIMORE THEN LINTHICUM- 54, 756. Contreras, I., Cordeau, J.F., Laporte, G., 2011a. Benders decomposition for large-scale uncapacitated hub location. Operations research 59, 1477–1490. Contreras, I., Cordeau, J.F., Laporte, G., 2011b. The dynamic uncapacitated hub location problem. Transportation Science 45, 18–32. Contreras, I., Cordeau, J.F., Laporte, G., 2011c. Stochastic uncapacitated hub location. European Journal of Operational Research 212, 518 – 528. Contreras, I., Díaz, J.A., Fernández, E., 2011d. Branch and price for large-scale capacitated hub location problems with single assignment. INFORMS Journal on Computing 23, 41–55. Cook’s, W., 2006. `://www.math.uwaterloo.ca/tsp/` . Accessed: 2017-04-25. Correia, I., Nickel, S., Saldanha-da Gama, F., 2014. Multi-product capacitated single-allocation hub location problems: formulations and inequalities. Networks and Spatial Economics 14, 1–25. De Camargo, R.S., De Miranda, G., Ferreira, R.P., 2011. A hybrid outer-approximation/benders decomposition algorithm for the single allocation hub location problem under congestion. Operations Research Letters 39, 329–337. Dufour, E., Laporte, G., Paquette, J., Rancourt, M., 2018. Logistics service network design for humanitarian response in east africa. Omega 74, 1 – 14. Ebery, J., Krishnamoorthy, M., Ernst, A., Boland, N., 2000. The capacitated multiple allocation hub location problem: Formulations and algorithms. European Journal of Operational Research 120, 614–631. Elhedhli, S., Hu, F., 2005. Hub-and-spoke network design with congestion. Computers and Operations Research 32, 1615–1632. Elçi, z., Noyan, N., 2018. A chance-constrained two-stage stochastic programming model for humanitarian relief network design. Transportation Research Part B: Methodological 108, 55 – 83. Elçi, z., Noyan, N., Bülbül, K., 2018. Chance-constrained stochastic programming under variable reliability levels with an application to humanitarian relief network design. Computers & Operations Research 96, 91 – 107. Ernst, A., Krishnamoorthy, M., 1996. Efficient algorithms for the uncapacitated single allocation p-hub median problem. Location Science 4 (3), 139–154. Ernst, A., Krishnamoorthy, M., 1998b. An exact solution approach based on shortest-paths for p-hub median problems. Informs Journal on Computing 10 (2), 149–162. Ernst, A., Krishnamoorthy, M., 1999. Solution algorithms for the capacitated single allocation hub location problem. Annals of Operations Research 86, 141–159. Farahani, R.Z., Hekmatfar, M., Arabani, A.B., Nikbakhsh, E., 2013. Survey: Hub location problems: A review of models, classification, solution techniques, and applications. Comput. Ind. Eng. 64, 1096–1109. Fischetti, M., González, J.J.S., Toth, P., 1998a. Solving the orienteering problem through branch-and-cut. INFORMS Journal on Computing 10, 133–148. Fischetti, M., Gonzalez, J.J.S., Toth, P., 1998b. Solving the orienteering problem through branch-and-cut. INFORMS J. on Computing 10, 133–148. 

Fischetti, M., Salvagnin, D., Zanette, A., 2009. Minimal infeasible subsystems and Benders cuts. Mathematical Programming to appear 

. Freitas, J.C.d., Penna, P.H.V., 2019. A variable neighborhood search for flying sidekick traveling salesman problem. International Transactions in Operational Research 0. doi: `10.1111/itor.12671` . 

Gelareh, S., 2008. Hub location models in public transport planning. Ph.D. thesis. Tecnical University of Kaiserslautern, Germany. 

Gelareh, S., Monemi, R.N., Nickel, S., 2015a. Multi-period hub location problems in transportation. Transportation Research Part E: Logistics and Transportation Review 75, 67–94. 

Gelareh, S., Neamatian Monemi, R., Nickel, S., 2015b. Multi-period hub location problems in transportation. Transportation Research 

- Part E: Logistics and Transportation Review 75, 67–94. doi: `10.1016/j.tre.2014.12.016` . 

- Gelareh, S., Nickel, S., 2011. Hub location problems in transportation networks. Transportation Research Part E 47, 1092–1111. 

- Gendreau, M., Laporte, G., Semet, F., 1998. A branch-and-cut algorithm for the undirected selective traveling salesman problem. Networks 32, 263–273. 

- Goldman, A., 1969. Optimal location for centers in a network. Transportation Science 3, 352–360. 

Hakimi, S.L., 1964. Optimum locations of switching centers and the absolute centers and medians of a graph. Operations Research 12, 450–459. 

Hansen, P., Mladenovi´c, N., Pérez, J.A.M., 2008. Variable neighbourhood search: methods and applications. 4OR 6, 319–360. 

Herrán, A., Colmenar, J.M., Marti, R., Duarte, A., 2019. A parallel variable neighborhood search approach for the obnoxious p-median 

problem. International Transactions in Operational Research 0. doi: `10.1111/itor.12510` . 

Kara, B.Y., Taner, M.R., 2011. Hub location problems: The location of interacting facilities, in: Eiselt, H.A., Marianov, V. (Eds.), 

Foundations of location analysis. Springer, pp. 273–288. 

Klincewicz, J., 1996. A dual algorithm for the uncapacitated hub location problem. Location Science 4 (3), 173–184. 

Klincewicz, J., 2002. Enumeration and search procedures for a hub location problem with economies of scale. Annals of Operations 

Research 110, 107–122. 

Labbé, M., Rodríguez-Martin, I., Salazar-Gonzalez, J., 2004. A branch-and-cut algorithm for the plant-cycle location problem. Journal of the Operational Research Society 55, 513–520. 

24 

Labbé, M., Yaman, H., Gourdin, E., 2005. A branch and cut algorithm for the hub location problems with single assignment. Mathematical Programming 102, 371–405. Letchford, A.N., Lodi, A., 2002. Integer Programming and Combinatorial Optimization: 9th International IPCO Conference Cambridge, MA, USA, May 27–29, 2002 Proceedings. Springer Berlin Heidelberg, Berlin, Heidelberg. chapter Polynomial-Time Separation of Simple Comb Inequalities. pp. 93–108. Maculan, N., Plateau, G., Lisser, A., 2003. Integer linear models with a polynomial number of variables and constraints for some classical combinatorial optimization problems. Pesquisa Operacional 23(1), 161 – 168. Magnanti, T., Wong, R., 1981. Accelerating Benders decomposition: Algorithmic enhancement and model selection criteria. Operations Research 29, 464–484. Marín, A., 2005a. Formulating and solving splittable capacitated multiple allocation hub location problems. Computers & OR 32 (12), 3093–3109. Marín, A., 2005b. Uncapacitated euclidean hub location: Strengthened formulation, new facets and a relax-and-cut algorithm. Journal of Global Optimization 33, 393–422. Martín, I.R., González, J.J.S., Yaman, H., 2014. A branch-and-cut algorithm for the hub location and routing problem. Computers & OR 50, 161–174. Mayer, G., Wagner, B., 2002. Hublocater: An exact solution method for the multiple allocation hub location problem. Computers & OR 29, 715–739. McDaniel, D., Devine, M., 1977. A modified Benders’ partitioning algorithm for mixed integer programming. Management Science 24, 312–319. Merakli, M., Yaman, H., 2016. Robust intermodal hub location under polyhedral demand uncertainty. Transportation Research Part B: Methodological 86, 66 – 85. Merakli, M., Yaman, H., 2017. A capacitated hub location problem under hose demand uncertainty. Computers & Operations Research 88, 58–70. Miranda Junior, G.d., Camargo, R.S.d., Pinto, L.R., Conceiçäo, S.V., Ferreira, R.P.M., 2011. Hub location under hub congestion and demand uncertainty: the Brazilian case study. Pesquisa Operacional 31, 319 – 349. Mohammadi, M., Jula, P., Tavakkoli-Moghaddam, R., 2019. Reliable single-allocation hub location problem with disruptions. Transportation Research Part E: Logistics and Transportation Review 123, 90–120. Mokhtar, H., Krishnamoorthy, M., Ernst, A.T., 2018. The 2-allocation p-hub median problem and a modified benders decomposition method for solving hub location problems. Computers & Operations Research . Monemi, R.N., Gelareh, S., 2017. The ring spur assignment problem: New formulation, valid inequalities and a branch-and-cut approach. Computers & Operations Research 88, 91 – 102. Monemi, R.N., Gelareh, S., Hanafi, S., Maculan, N., 2017. A co-opetitive framework for the hub location problems in transportation networks. Optimization 66, 2089–2106. O’Kelly, M., 1986a. The location of interacting hub facilities. Transportation Science 20 (2), 92–105. O’Kelly, M.E., 1986b. Activity levels at hub facilities in interacting networks. Geographical Analysis 18, 343–356. O’Kelly, M.E., 1987. A quadratic integer program for the location of interacting hub facilities. European Journal of Operational Research 32, 393–404. O’Kelly, M.E., Bryan, D.L., 1998. Hub location with flow economies of scale. Transportation Research Part B: Methodological, Elsevier 32, 605–616. O’Kelly, M.E., Luna, H.P.L., de Camargo, R.S., de Miranda, G., 2015. Hub location problems with price sensitive demands. Networks and Spatial Economics 15, 917–945. Padberg, M.W., Rao, M.R., 1982. Odd minimum cut-sets and b-matchings. Mathematics of Operations Research 7, 67–80. Papadakos, N., 2008. Practical enhancements to the Magnanti-Wong method. Operations Research Letters 36, 444–449. Pirkul, H., Schilling, D., 1998. An efficient procedure for designing single allocation hub and spoke systems. Management Science 44(12), 235–242. Poojari, C., Beasley, J., 2009. Improving benders decomposition using a genetic algorithm. European Journal of Operational Research 199, 89–97. 

Rahmaniani, R., Crainic, T.G., Gendreau, M., Rei, W., 2017. The benders decomposition algorithm: A literature review. European Journal of Operational Research 259, 801 – 817. 

Real, L.B., O’Kelly, M., de Miranda, G., de Camargo, R.S., 2018. The gateway hub location problem. Journal of Air Transport Management 73, 95 – 112. Rodriguez-Martin, I., Salazar-Gonzalez, J.J., 2008. Solving a capacitated hub location problem. European Journal of Operational Research 184, 468–479. Rodríguez-Martín, I., Salazar-González, J.J., Yaman, H., 2014. A branch-and-cut algorithm for the hub location and routing problem. Computers & Operations Research 50, 161–174. Rostami, B., Koemmerling, N., Buchheim, C., Clausen, U., 2018. Reliable single allocation hub location problem under hub breakdowns. Computers & Operations Research 96, 15 – 29. Sasaki, M., Campbell, J.F., Krishnamoorthy, M., Ernst, A.T., 2014. A stackelberg hub arc location model for a competitive environment. Computers & Operations Research 47, 27–41. 

Sasaki, M., Fukushima, M., 2003. On the hub-and-spoke model with arc capacity constraints. Journal of the Operations Research Society of Japan 46 (4), 409–428. Sasaki, M., Suzuki, A., Drezner, Z., 1999. On the selection of hub airports for the airline hub-and-spoke system. Computers & OR 26, 1411–1422. 

Sherali, H., Fraticelli, B., 2002. A modification of Benders’ decomposition algorithm for discrete subproblems: An approach for stochastic programs with integer recourse. Journal of Global Optimization 22, 319–342. Tiernan, J.C., 1970. An efficient search algorithm to find the elementary circuits of a graph. Commun. ACM 13, 722–726. 

25 

doi: `http://doi.acm.org/10.1145/362814.362819` . 

Tofighi, S., Torabi, S., Mansouri, S., 2016. Humanitarian logistics network design under mixed uncertainty. European Journal of Operational Research 250, 239 – 250. 

- Vahdani, B., Veysmoradi, D., Noori, F., Mansour, F., 2018. Two-stage multi-objective location-routing-inventory model for humanitarian logistics network design under uncertainty. International Journal of Disaster Risk Reduction 27, 290 – 306. 

- Wagner, B., 2007. An exact solution procedure for a cluster hub location problem. European Journal of Operational Research 178, 391–401. 

Yaman, H., Carello, G., 2005. Solving the hub location problem with modular link capacities. Computers & OR 32 (12), 3227–3245. Özdamar, L., Ertem, M.A., 2015. Models, solutions and enabling technologies in humanitarian logistics. European Journal of Operational Research 244, 55 – 65. 

- Zhalechian, M., Torabi, S.A., Mohammadi, M., 2018. Hub-and-spoke network design under operational and disruption risks. Transportation research part E: logistics and transportation review 109, 20–43. 

26 

