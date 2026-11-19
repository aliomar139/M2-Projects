Results in Engineering 27 (2025) 105823 



Contents lists available at ScienceDirect 

# Results in Engineering 

journal homepage: www.sciencedirect.com/journal/results-in-engineering 



### Research paper 

## Cluster or tree? Toward a hybrid topology for sensor networks 



Hassan Harb<sup>a</sup> , Kassem Danach<sup>b</sup> , Mouhammad AlAkkoumi<sup>a</sup> , Ali Jaber<sup>c</sup> , Chady Abou Jaoude<sup>d</sup> , Abbass Nasser<sup>e</sup><sup>_,_</sup> _,_ ∗ 

> a _College of Engineering and Technology, American University of the Middle East, Kuwait_ 

> b _Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon_ 

> c _Faculty of Sciences, Lebanese University, Beirut 1001, Lebanon_ 

> d _Faculty of Engineering – TICKET Lab, Antonine University, Beirut 1003, Lebanon_ 

> e _USEK Business School, Holy-Spirit University of Kaslik (USEK), PoBox 446, Jounieh Lebanon_ 

#### A R T I C L E I N F O 

#### A B S T R A C T 

_Keywords:_ Wireless sensor networks Performance analysis Network topologies Energy consumption Cluster topology Tree topology 

Recently, the revolution in sensor networks has enabled the deployment of new services and applications that have made our life smarter and safer. Thanks to various types of devices (e.g. sensors) deployed in such networks, our planet has become entirely monitored while the collected data is communicated wirelessly for analysis and study. Unfortunately, integrating sensor networks into various applications is a challenging task for both researchers and industries. While the networks are characterized by their density deployment and the massive amount of collected data, the sensors have limited energy consumption that can quickly be depleted during communication operations. Subsequently, selecting the best network topology plays an essential role in improving the energy consumption in sensors which results in providing longer monitoring of a given area. The objective of this paper consists of two main parts. First, it evaluates the performance analysis of common topologies used by the researchers in sensor networks, i.e. cluster and tree schemes, while discussing their advantages and limitations. Then, it proposes a hybrid network topology, called CLEE, that takes the benefits of both topologies to enhance the network performance and save energy consumption. Typically, CLEE topology takes several parameters into consideration; among those are network dimension, number of sensors, sink position, and transmission range for efficient application surveillance. Through extensive simulations, this paper analyzes the performance of all network topologies, e.g. cluster, tree and CLEE, while evaluating their effect on different performance metrics. 

##### **1. Introduction** 

##### _1.1. Context_ 

Major changes are witnessed more often in industry, healthcare, agriculture, and other economic, social and environmental areas due to advancements in technology. This motivated researchers and markets to give more attention to surveillance technologies that allow monitoring and analysis of sensor data and understand its behavior and impact better and deeper [1,2]. Such technologies can make accessing and monitoring data in dangerous, distant and unreachable zones possible, such as monitoring underwater, forests, and human internal organs [3–5]. This valuable and crucial data is essential for experts in solving important real-world problems. Furthermore, they allow them 

to get a deeper view in order to make intelligent decisions and avoid potential risks. Wireless sensor networks (WSNs) are one of the most famous and widespread media used in monitoring systems. Typically, a WSN is a set of sensor nodes deployed in a zone of interest in order to monitor physical or environmental conditions and then transmit the collected data to the end user using wireless communication [6]. Recently, WSN has demonstrated its relevance in various applications including environmental, healthcare, military, agricultural, transportation, etc. 

##### _1.2. Challenges and research gap_ 

Indeed, WSNs face challenges such as network deployment, full coverage of the monitored zone, limited sensor resources (energy, memory, 

* Corresponding author. 

_E-mail addresses:_ hassan.harb@aum.edu.kw (H. Harb), kassem.danach@mu.edu.lb (K. Danach), mouhammad.a@aum.edu.kw (M. AlAkkoumi), ali.jaber@ul.edu.lb (A. Jaber), chady.aboujaoude@ua.edu.lb (C.A. Jaoude), abbass.nasser@usek.edu.lb (A. Nasser). 

https://doi.org/10.1016/j.rineng.2025.105823 Received 15 March 2025; Received in revised form 1 May 2025; Accepted 17 June 2025 Available online 9 July 2025 2590-1230/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

CPU), data management, and low transmission rates [7,8]. Among these challenges, energy consumption is highly related to the selection of network topology which is considered the most important parameter prior to WSN deployment [9,10]. In the literature, researchers have mainly focused on tree and cluster schemes as the most popular topologies used for WSNs. Although these topologies are efficient in conserving sensor energy, both topologies have several drawbacks and their performance highly depends on the application context and requirements. Despite the emerging efforts in evaluating both topologies [11,12], this study tackles a new trend in selecting the most suitable topology by considering a broader set of internal and external factors influencing sensor network performance. This study enables a more realistic and adaptable evaluation of topological choices, aligning better with the diverse and dynamic conditions sensor networks face in real-world applications. By moving beyond conventional criteria, this study contributes to the development of more resilient and efficient sensor network architectures tailored to specific deployment scenarios. 

##### _1.3. Contributions_ 

In this study, the main contributions are as follows: 

- It tackles a new trend in studying the energy efficiency of WSNs which is broken down in two-folds. 

- It studies the performance of tree and cluster topologies in terms of energy consumption according to some potential parameters such as zone dimensions, number of deployed sensors, sensor positions, sensor transmission range, and sink position. The idea behind such analysis is to assist experts in selecting the best topology that minimizes the sensor energy consumption and ensure long-time zone monitoring. To the best of our knowledge, the performance analysis of tree and cluster topologies is the first published one that tries to fit the needs of choosing the suitable network topology according to the application context and parameters. 

- It proposes a hybrid network topology, called CLEE, that takes the benefits of both topologies and enhances the energy efficiency of such networks. 

- It performs extensive simulations taking into considerations various sensor network conditions and factors, while providing clear insights about the importance of selecting topology in sensor networks. 

##### _1.4. Paper structure_ 

The incoming sections are organized as follows: section 2 presents some related work based on cluster and tree topologies proposed recently in the literature. Section 3 show the performance analysis study of both topologies in terms of energy saving, according to a set of defined parameters. Section 4 details the novel hybrid topology, e.g. CLEE, proposed in this work. Section 5 presents a selection algorithm to find the best topology according to a set of defined parameters. In section 6, it describes the simulation done in this paper while discussing the obtained results. Finally, section 7 summarizes this paper and provides some future work. 

##### **2. Related work** 

Network topology is a key factor in ensuring the connectivity of the sensor network as well as improving its lifetime. Thus, researchers focused their efforts in designing energy-efficient routing protocols based on various network topologies. Particularly, cluster and tree schemes are the most popular topologies used in sensor networks and are widely adapted in most work proposed in the literature. Both topologies have demonstrated their efficiency in enhancing the network performance in terms of different metrics set by experts. In [13,14], the authors give an overview of various routing protocols based on cluster and tree schemes proposed recently in the literature. 

##### _2.1. Cluster-based topology: a background_ 

In the literature, several techniques and protocols based on clustering schemes are proposed for energy-efficient sensor networks [15– 25]. In [26], the authors propose a hybrid technique that combines a memetic algorithm and the adaptive hill-climbing method for prolonging the sensor network lifetime. Particularly, the memetic algorithm introduces an improved variant of the genetic algorithm that uses a local discovery method to minimize premature convergence while the hillclimbing algorithm aims to select the optimal cluster-head (CH) in the network. The authors of [15] propose a cluster-based routing protocol for WSN following three phases. The first phase uses a honey badger algorithm to select the optimal CHs according to a set of criteria such as remaining energy, degree of a node, distance to neighbor and to sink, etc. Once CHs are selected, the second phase allows efficient communication between them and the sink by using a Fuzzy Firebug Swarm Optimization algorithm. The last phase aims to maintain clusters and remove faulty sensors in order to increase network performance. In [16], a Fuzzy based Energy Efficient Routing Protocol (E-FEERP) is proposed. The proposed protocol introduces a clustering node scheme based on the particle swarm optimization algorithm that takes, as input, a set of network features such as energy, density, communication quality, etc. The authors of [17] propose a clustering network mechanism that combines sparrow search and differential evolution algorithms with the aim to minimize the energy consumed in sensors, thus maximizing the network lifetime. The idea behind their mechanism is to elect a CH in a way that the energy distribution will be balanced over all nodes. In [18], the authors propose an energy-aware cluster-based routing protocol (ECRP) aiming at rotating the CH role among all cluster members of a cluster based on the energy parameter. ECRP is a multi-hop routing scheme for inter-cluster communications using a cost function conceived in such a way as to reduce and balance the energy consumption of sensor nodes. In [19], the authors proposed a Gateway Clustering Energy-Efficient Centroid-based Routing Protocol (GCEECRP) which selects and rotates the cluster head near the energy centroid position of the cluster. Additionally, each CH chooses the gateway node for multi-hoping itself and other CH data towards the base station, which reduces load among the CHs. In [20], the authors develop an effective framework for multiple electric energy consumption forecasting in smart buildings using Transfer Learning and Long Short-Term Memory (MEC-TLL). This framework utilizes the concept of transfer learning, and a cluster-based strategy for training the Long Short-Term Memory models to reduce the computational time. It clusters the time series training set into several clusters using the k-means clustering algorithm. The authors of [21] presented an energy-efficient routing schema combined with clustering and sink mobility. Cluster members calculated the optimal energy consumption to transmit data to their corresponding CHs. Then, the CHs form a chain for inter-cluster communication. 

##### _2.2. Tree-based topology: a background_ 

In [27–35], the authors focused on a tree-based communication scheme for prolonging WSN lifetime. In [27], the authors proposed a tree architecture WSN mathematical model that ensures the quality of service and the fairness requirements of a given application. The proposed model minimizes the overall network energy by calculating the Lagrangian Relaxation probability of different network characteristics such as packet size, communication distance, and the activity of the nodes. In [28], a collection tree-based mesh communication protocol has been proposed. By considering the remaining node energies as the key factor, the proposed protocol uses an optimization algorithm to find the optimal routing path and data forwarding scheme for the WSN. The authors of [29] introduce a Dynamic Spanning Tree with Mobile Sink (DSTMS) routing protocol for reducing node energy consumption and congestion in WSN. Typically, DSTMS consists of two phases: the first one aims to improve the data communication path by proposing a 

2 

_Results in Engineering 27 (2025) 105823_ 

###### _H. Harb, K. Danach, M. AlAkkoumi et al._ 

new multi-layer framework that combines between minimum spanning tree and LEACH protocol, i.e. Low Energy Adaptive Clustering Hierarchy Protocol. Subsequently, the communication path calculated in the framework is mainly based on the distribution of the node’s residual energies along with the motion parameters of the mobile sink to construct the hierarchical transmission of the network. In [30], a robust and selforganizing routing protocol that combines between scheduling method, local node density and virtual residual energy is proposed. The protocol finds the shortest path between each node and the sink to transmit the collected data, and each node may dynamically switch on or off according to a sleep-active scheduling mechanism to save its energy. In [31], the authors present a minimum spanning tree with a particle optimization algorithm for transmitting data in mobile WSN. The tree construction is based on the Weiner index and improves the energy consumption in the network and the packet delay. In [32], the authors analyze the performance of different tree types, advantages, disadvantages, and effects on energy, especially how the Red-Black tree (RBT) improves energy efficiency and network lifetime compared with Minimum Spanning Trees (MST) and Binary Search Trees (BST). In [33], the authors propose the Lightweight and Secure Tree-based Routing protocol (LSTR) to provide sensors’ authenticity and data confidentiality along the transmission path from the sensor to the base station using tree-based schema. It also aims to reduce resource usage, especially energy dissipation. In [34], the authors propose a new algorithm based on tree topology, where the aim is to improve the transmission of heterogeneous data in heterogeneous networks by optimizing the network topology based on local tree reconstruction, in which there is a real-time updating of the tree topology to ensure better transmission and longer network lifetime. 

##### _2.3. Hybrid-based topology: a background_ 

Recently, several authors have focused on developing hybrid routing protocols for WSNs [36–42]. In [36], the authors propose a VKECE3D mechanism to overcome energy and coverage challenges in WSNs. VKECE-3D is applied in three steps: the first one deploys the sensors in a random way and aims to ensure the uniformity of the network. The second step improves the quality coverage by computing the best perceptual radius using 3D-Voronoi partitioning and the K-means algorithm. The last step introduces a multi-hop routing mechanism that minimizes energy consumption and maximizes the network lifetime. The authors of [37] present the DNN-HR algorithm that enhances the learning process of sensor networks in several ways. Firstly, the algorithm partitions the node network into two levels based on the geographical positions of the nodes, where a set of CHs are selected in each zone to form incremental trees. Secondly, reinforcement learning based on the neural networks is performed by each node to communicate with its neighbors. In [38], an energy-conserving routing scheme is proposed. In such a scheme, A* and ant colony optimization methods are used to find the optimal routing path of each node based on the residual sensor energy and the node-sink distance. Additionally, the proposed scheme uses a clustering-based aggregation scheme to optimize energy utilization and minimize transmission costs. The authors of [39] propose a hybrid cluster and tree communication protocol called hybrid tree-based and cluster-based routing protocol for raw data collection (HTC-RDC) for collecting data in WSNs. Besides prolonging network lifetime, HTC-RDC aims to introduce novel scenarios and applications in sensor networks where the data collected by the sensors are free of redundancy. In [40], the authors propose a new Tree Clustering Algorithm with Mobile Data Collector (TCAMDC), where the objective is to increase network life by minimizing energy consumption. The authors combine tree topology (specifically MST) and clustering to determine the best network topology in terms of energy consumption while building and updating the network topology. In [41], a Cluster-Tree based Energy-Efficient Data Gathering (CTEEDG) protocol has been proposed. The authors used Fuzzy logic to select the cluster head and constructed 

a tree-based topology to perform the inter-cluster communication. In [42], the authors present a cluster tree-based energy-efficient routing protocol called CTEER to alleviate the rapid energy loss of the ordinary nodes in the traditional static routing tree mechanism. The protocol is suitable for time-sensitive applications such as network live broadcast systems, automatic train operation systems, ticketing software, and intelligent house systems. 

##### _2.4. Literature review: a summary_ 

Table 1 shows a summary of the literature review according to some metrics such as work year, topology type considered for the sensor network, and the methods used in the paper. 

##### **3. Cluster vs tree topologies: performance analysis study** 

Indeed, controlling network topology is one of the biggest challenges facing the deployment of sensor networks. This is because the selection of topology will highly affect all performance metrics in WSNs such as node connectivity, packet delay, network scalability, data reliability, and most importantly the network lifetime. This paper studies the topology control from the energy-efficiency point of view because sensors are usually equipped with a small battery power that cannot be mostly recharged or replaced, especially in inaccessible areas. In the literature, various energy-efficient topologies are proposed for WSNs. Particularly, researchers focused on cluster and tree structures as the most popular and efficient topologies used in sensor networks. The next sections describe both topologies while highlighting the advantages and limitations of each one. 

##### _3.1. Cluster-based WSN topology_ 

This section discusses the system model of sensor networks based on the cluster scheme along with its advantages and limitations. 

##### _3.1.1. Cluster topology: system model_ 

Cluster-based typologies have been widely used in WSNs for various types of protocols, such as data gathering and target tracking. Clustering is considered as one of the most important network schemes for extending sensor network lifetime and it is particularly useful for applications that require scalability to thousands of nodes. Typically, a cluster is composed of a number of sensor nodes (SNs) and has one or more cluster heads (CHs) to manage the members. The main task of an SN in a sensor field is to detect events, perform quick local data processing, and then transmit the data to a specified CH. CH acts as a gateway between the SNs and the base station. It collects the data from the respective cluster’s nodes and forwards all the aggregated data to the sink. Additionally, a CH can be selected among sensor nodes or be a more powerful node assigned prior to network deployment. Fig. 1 shows a typical cluster topology used in WSNs. 

##### _3.1.2. Cluster construction: mathematical reformulation_ 

Generally, the problem of cluster construction in WSN is reformulated as follows: given a WSN with _𝑛_ sensor nodes and one base station (sink), the goal is to form clusters and assign cluster heads (CHs) such that the total energy consumption of intra-cluster communication and CH-to-sink communication is minimized. Accordingly, the following parameters and variables are defined: 

- _𝑆_ = { _𝑠_ 1 _,𝑠_ 2 _,_ … _,𝑠𝑛_ }: Set of sensor nodes. 

- _𝑏_ : Index of the base station (sink). 

- _𝐸𝑡𝑥_ ( _𝑖,𝑗_ ): Energy required to transmit data from node _𝑠𝑖_ to _𝑠𝑗_ . 

- _𝐸𝑟𝑥_ : Energy required to receive one unit of data. 

- _𝐷𝑖_ : Data generated by node _𝑠𝑖_ (in bits). 

- _𝑥𝑖𝑗_ ∈{0 _,_ 1}: 1 if node _𝑠𝑖_ is assigned to cluster head _𝐶𝑗_ , 0 otherwise. 

- _𝑦𝑗_ ∈{0 _,_ 1}: 1 if node _𝑠𝑗_ is selected as a cluster head, 0 otherwise. 

3 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

**Table 1** 

A summary for the literature review on energy-efficient WSN topologies. 

|Reference|Year|Topology|Type||Methods|
|---|---|---|---|---|---|
|||Cluster|Tree|Hybrid||
|Wang et al. [21]|2019|X|||Inter-Cluster Communication,<br>Mobile Sink|
|Moussa et al. [18]|2020|X|||ECRP|
|Qureshi et al. [19]|2020|X|||GCEECRP|
|Le et al. [20]|2020|X|||LSTM, K-means|
|Arian et al. [31]|2020||X||Particle Swarm<br>Optimization Algorithm|
|Pranesh et al. [32]|2020||X||RBL, MST, BST|
|Hamouid et al. [33]|2020||X||LSTR|
|Zhang et al. [34]|2020||X||Local Tree Reconstruction|
|Karunanithy et al. [41]|2020|||X|CTEEDG|
|Lu et al. [42]|2020|||X|CTEER|
|He et al. [30]|2021||X||Sleep-Active Scheduling|
|Kathiroli et al. [17]|2022|X|||Sparrow Search,<br>Differential Evolution|
|Yuan et al. [28]|2022||X||Optimization Algorithm|
|Wei et al. [29]|2022||X||Minimum Spanning Tree,<br>LEACH Protocol|
|Ibrahim et al. [38]|2022|||X|A*, Ant Colony Optimization|
|Zhang et al. [39]|2022|||X|HTC-RDC|
|Meddah et al. [40]|2022|||X|TCAMDC|
|Manikandanet al. [26]|2023|X|||Memetic Algorithm,<br>Hill-Climbing|
|Suresh et al. [15]|2023|X|||Honey badger algorithm,<br>Fuzzy Firebug Swarm<br>Optimization Algorithm|
|Narayan et al. [16]|2023|X|||Particle Swarm<br>Optimization Algorithm|
|Tai et al. [27]|2023||X||Lagrangian Relaxation<br>Probability|
|Gou et al. [36]|2023|||X|3D-Voronoi, K-means|
|Liu et al. [37]|2023|||X|Neural Networks|





**Fig. 1.** A typical cluster topology used in WSNs. 

Based on the above notations, the objective function is defined as follows: 



<!-- Start of picture text -->
min ∑ ∑ 𝑥𝑖𝑗 ( 𝐸𝑡𝑥 ( 𝑖,𝑗 ) ⋅ 𝐷𝑖 +  𝐸𝑟𝑥 ⋅ 𝐷𝑖 )<br>𝑖 ∈ 𝑉 𝑗 ∈ 𝑉<br>+ ∑ 𝑦𝑗 𝐸𝑡𝑥 ( 𝑗,𝑏 ) ⋅ ∑ 𝑥𝑖𝑗 ⋅ 𝐷𝑖<br>𝑗 ∈ 𝑉 ( 𝑖 ∈ 𝑉 )<br><!-- End of picture text -->

where the first term of the objective function represents energy for intracluster communication, and the second one captures energy consumed by CHs to forward aggregated data to the sink. Furthermore, the function is subjected to the following constraints: 



<!-- Start of picture text -->
∑ 𝑥𝑖𝑗 = 1 , ∀ 𝑖 ∈ 𝑉 (each node assigned to one CH) (1)<br>𝑗 ∈ 𝑉<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖𝑗 ≤ 𝑦𝑗 , ∀ 𝑖,𝑗 ∈ 𝑉 (can assign only to selected CHs) (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑦𝑗 ∈{0 , 1} , ∀ 𝑗 ∈ 𝑉 (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖𝑗 ∈{0 , 1} , ∀ 𝑖,𝑗 ∈ 𝑉 (4)<br><!-- End of picture text -->

##### _3.1.3. Clustering algorithm_ 

Among all the clustering algorithms proposed in the literature, K- means [43] is considered the most popular algorithm used in WSNs. Typically, K-means is an unsupervised machine learning algorithm where the classes and labels are not predefined. The aim is to cluster and group sets of input data points into _𝐾_ clusters, depending on their features. The result of K-means will be _𝐾_ clusters where each cluster contains a set of data points. Applying K-means on WSN, the data points are the sensors with their position ( _𝑥_ , _𝑦_ ). The cluster head sensor of each cluster is chosen as the nearest sensor to the cluster centroid. Each sensor node will communicate directly with its cluster head. Regarding the number 

4 

_Results in Engineering 27 (2025) 105823_ 

###### _H. Harb, K. Danach, M. AlAkkoumi et al._ 

of clusters _𝐾_ , it is considered as a hyper-parameter which needs to be tested in order to get the best value. 

Algorithm 1 shows the process of the K-means algorithm applied in WSNs. The algorithm takes, as input, the set of sensor nodes along with the number of desired clusters, and returns accordingly, as output, the sensor network map. First, each sensor starts by broadcasting a message including a random number, where only the sensors in the senders’ transmission range will be able to receive this message. Then the receivers will reply with a message including their generated random number to the sender (sender of broadcast). After that, _𝐾_ sensors are elected as the CHs where they have generated the highest random numbers. Then each sensor will join the cluster having the nearest relative cluster head. After each sensor determines its cluster, the cluster heads are updated. The sensors with the minimal distance to all the cluster members are grouped. The assigning of each sensor cluster and the updating of the cluster head is repeated until convergence is reached. 

##### **Algorithm 1** Clustering Algorithm. 

**Require:** Set of Sensors: _𝑆_ = { _𝑠_ 1, _𝑠_ 2, ..., _𝑠𝑛_ }, Number of Clusters: _𝐾_ . **Ensure:** Wireless Sensor Network: WSN 

- 1: **for each** sensor in _𝑆_ **do** 2: sensor.myRandomNumber = RandomNumber(); 3: sensor.broadcastMessage(sensor.myRandomNumber); 4: **end for** 5: **for each** sensor in _𝑆_ **do** 6: numbers = sensor.RecievedNumbers(); 7: numbers.add(sensor.myRandomNumber); 8: **if** sensor.myRandomNumber is in Greatest _𝐾_ numbers and Number Of CHs _< 𝐾_ **then** 

- 9: WSN.addClusterHead(sensor); 

- 10: **end if** 11: **end for** 12: **while** (no convergence) **do** 13: **for each** sensor in _𝑆_ **do** 14: clusterId = sensor.NearestCH().clusterId; 15: WSN.updateClustersMembers(clusterId, sensor); 16: **end for** 17: **for each** cluster in WSN.Clusters **do** 18: clusterHead = cluster.nearestSensortoAllMembers(); 19: cluster.setCH(clusterHead); 20: **end for** 21: **end while** 22: **return** WSN 



**Fig. 2.** A typical tree topology used in WSNs. 

that clustering is dependent on each cluster head; if this CH was dysfunctional, it would cause the entire system to fail. Therefore, it needs to reconfigure all the networks starting from the beginning. 

##### _3.2. Tree-based WSN topology_ 

This section discusses the system model of sensor networks based on the tree scheme along with its advantages and limitations. 

##### _3.2.1. Tree topology: system model_ 

Tree-based topology is a famous topology in sensor networks, where all the deployed sensors construct a logical tree. For instance, the minimum spanning tree (MST), which is used to design various protocols for WSNs, spans over all the sensor nodes without any cycle and consists of a minimum sum of weights over all the included edges. Data is passed from a leaf node to its parent node. In turn, a receiver node receives data from the child nodes and sends them to its parent node after aggregating data with its own data. As a result, the data flow will be from leaf to root nodes that, in turn, send the collected data to the specified sink. Fig. 2 shows a typical tree topology used in WSNs. 

##### _3.2.2. Tree construction: mathematical reformulation_ 

##### _3.1.4. Cluster topology: advantages and limitations_ 

The cluster-based topology has several advantages but also some drawbacks. On one hand, such topology greatly increases the scalability of a sensor network and the overall energy consumption of the nodes compared with the flat topology protocols. Additionally, the organization of the network into clusters enables the efficient aggregation of data, which in turn results in better use of the bandwidth of the channel. For many-to-one and one-to-many communication paradigms, which are common in sensor networks, cluster-based routing holds good promise. On the other hand, non-uniform clustering is the main problem for this topology. In clustering, the energy dissipation rate varies significantly from one sensor to another, even if they are in the same cluster, thus the energy distribution is not balanced. Furthermore, due to the longdistance communication between cluster members and cluster heads, the total energy consumption may increase, resulting in sensor death and a decrease in network lifetime. Moreover, selecting a cluster head is considered a big challenge during network formation since it largely affects the WSN lifetime. Mostly, the cluster heads can be randomly selected among sensor nodes according to some criteria, or a more powerful node assigned prior to network deployment. Subsequently, one of the most significant disadvantages of using a cluster-based scheme is 

The tree construction is one of the major challenges when deploying a senor network. Mathematically, a WSN is represented by a graph _𝐺_ = ( _𝑆,𝐿_ ), where _𝑆_ is the set of sensor nodes (including the sink node _𝐵_ ), and _𝐿_ is the set of communication links. The goal of this study is to construct a data aggregation tree rooted at the sink _𝐵_ that minimizes the total energy consumption for data transmission and reception. The following parameters and variables are needed for the problem reformulation: 

- _𝑆_ : Set of sensor nodes, where _𝐵_ is the sink node. 

- _𝐿⊆𝑆_ × _𝑆_ : Set of communication links. 

- _𝐷𝑖_ : Amount of data generated by node _𝑠𝑖_ ∈ _𝑆_ (in bits). 

- _𝐸𝑡𝑥_ ( _𝑖,𝑗_ ): Energy consumed to transmit data from node _𝑠𝑖_ to node 

- _𝑠𝑗_ . 

- _𝐸𝑟𝑥_ : Energy consumed to receive data at a node (assumed constant per bit). 

- _𝑥𝑖𝑗_ ∈{0 _,_ 1}: Binary variable, 1 if node _𝑠𝑖_ sends data to node _𝑠𝑗_ , 0 otherwise. 

- _𝑓𝑖𝑗_ ≥ 0: Flow variable indicating the amount of data transmitted from node _𝑠𝑖_ to node _𝑠𝑗_ . 

According to above notations, the following objective function is defined: 

5 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

min ∑ ( _𝐸𝑡𝑥_ ( _𝑖,𝑗_ ) ⋅ _𝑓𝑖𝑗_ + _𝐸𝑟𝑥_ ⋅ _𝑓𝑖𝑗_ ) ( _𝑖,𝑗_ )∈ _𝐸_ 

where: 

- The objective function minimizes the total energy consumed for both transmitting and receiving data. 

- The flow conservation constraint ensures that each node sends its 

- data and relays data from its children. 

- The binary variable _𝑥𝑖𝑗_ encodes the tree structure: a parent-child link exists only if _𝑥𝑖𝑗_ = 1. 

- The formulation inherently constructs a tree because each node (except the sink) sends data to exactly one parent. 

Furthermore, the defined function considers the following constraints: 



<!-- Start of picture text -->
Flow conservation: ∑ 𝑓𝑗𝑖 − ∑ 𝑓𝑖𝑗 =  𝐷𝑖, ∀ 𝑖 ∈ 𝑆 ⧵ { 𝐵 } (5)<br>𝑗 ∈ 𝑆 𝑗 ∈ 𝑆<br><!-- End of picture text -->



<!-- Start of picture text -->
∑ 𝑓𝑗𝑠 − ∑ 𝑓𝑠𝑗 = − ∑ 𝐷𝑖 (6)<br>𝑗 ∈ 𝑆 𝑗 ∈ 𝑆 𝑖 ∈ 𝑆 ⧵{ 𝐵 }<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑓𝑖𝑗 ≤ 𝑀 ⋅ 𝑥𝑖𝑗 , ∀( 𝑖,𝑗 ) ∈ 𝐿 (7)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑥𝑖𝑗 ∈{0 , 1} , ∀( 𝑖,𝑗 ) ∈ 𝐿 (8)<br>𝑓𝑖𝑗 ≥ 0 , ∀( 𝑖,𝑗 ) ∈ 𝐿 (9)<br><!-- End of picture text -->

Where _𝑀_ is a large constant representing the upper bound on possible flow between nodes. 

##### _3.2.3. Tree algorithm_ 

Similar to clustering topology, researchers have proposed lots of algorithms to build the tree in the sensor network. Particularly, it focuses on the Kruskal algorithm as one of the most used graph theory algorithms in WSNs. Basically, the Kruskal algorithm aims to find the tree with the smallest total weight in a weighted graph. Applying the Kruskal algorithm on WSN, the vertices represent the sensor nodes, the edges are the connections between them, which are limited by the transmission range, and the weight represents the geographical distances between the sensors. 

Algorithm 2 shows the process of constructing the tree topology in WSN. Similar to that used in clustering, the algorithm takes the set of sensors as input, including each sensor position and transmission range, and returns a WSN. The process starts by broadcasting a message by each sensor, where only the sensors in the senders’ transmission range will be able to receive. Then, the receivers will reply with a message informing the sender (sender of broadcast) that there is an ability to establish a connection. After that, the connections are established while taking into account the minimal distances over all the connections and that no cycle should be created. Finally, each pair of adjacent sensors decide which one of them will be the parent according to the sensor having the lower number of hopes to the root. 

##### _3.2.4. Tree topology: advantages and limitations_ 

One of the major advantages of tree topology is that it consumes less energy than flat topology since it does not require flooding for data communication. Furthermore, it can save a bit more energy than some protocols for data acquisition. However, tree-based topology suffers from several disadvantages: 

- Formation of trees is time-consuming and costly. 

- It is susceptible to node failures. If a parent node fails, then its entire sub-tree will be cut off from the complete tree, which needs reconfiguration of the tree. 

- Power consumption is uneven across network nodes. The nodes closer to the root may consume a lot of power while forwarding packets from all the nodes in their sub-tree. 

- Data transmission from the leaf to the root node takes a long time. 

##### **Algorithm 2** Tree Algorithm. 

**Require:** Set of Sensors: _𝑆_ = { _𝑠_ 1, _𝑠_ 2, ..., _𝑠𝑛_ } **Ensure:** Wireless Sensor Network: WSN 

- 1: Graph _𝐺_ 2: WSN ← _𝜙_ 

- 3: **for each** sensor in _𝑆_ **do** 

- 4: sensor.broadcastMessage(); 

- 5: sensorsInSensorRange = sensor.ReciveReplies(); 6: adjacentSensor = sensorsInSensorRange.nearestSensor 7: _𝐺_ .addEdge(sensor, adjacentSensor, distance(sensor, adjacentSensor)) 8: **end for** 9: **for each** ( _𝑠𝑖_ , _𝑠𝑗_ ) in _𝐺_ .edges increasing order of weight **do** 

- 10: **if** _𝑠𝑖_ and _𝑠𝑗_ does not create cycle **then** 11: WSN.add( _𝑠𝑖_ , _𝑠𝑗_ ) 12: **end if** 13: **end for** 14: **for each** _𝑠𝑖_ in WSN.Sensors **do** 15: _𝑠𝑖_ .setParent = _𝑠𝑖_ .adajcentSenors.nearestSensorToSink 16: **end for** 17: **return** WSN 

- Tree maintenance overhead is high. 

##### _3.3. Research methodology_ 

For the sake of easy to follow and simplification, this paper adapted the following methodology in this study: 

- Research questions: experts are usually facing a big challenge when deploying a sensor network. Assume that the number of sensors to be deployed and the monitored zone area are already known to the experts, the following research questions are eminent: 

- _RQ1_ : what is the best topology to use in the network deployment that minimizes the energy consumption and ensures a long time monitoring of the zone? 

- _RQ2_ : how the position of the sink could affect the performance of the network? 

- Topology selection: in the literature, one can find several topologies considered by researchers such as chain, mesh, tree, cluster, etc. This study mainly focused on tree and cluster schemes as the most used topologies in WSNs that enhance various performance metrics. Thus, our objective is to validate 

- Research gap: most of the existing studies adapt either tree or cluster scheme in their methodologies without justifying the selection or validating the performance in other scheme type. In order to fill such research gap, our objective in this study is to perform simulations for both tree and cluster and provide clear indicators about their performance under different conditions and application circumstances. 

- Contribution: this study tackles a new trend in energy consumption in WSNs and proposes a new algorithm that takes, as input, some well-known parameters to the experts prior to network deployment and provide, as output, the best topology to be deployed. Then, this study proofs that neither tree or cluster could be considered as the best for all application environments. Thus, it then introduces a new hybrid topology that acts as a compromise solution that optimizes all performance metrics for a given WSN application. 

- Recommendations: through extensive simulations and results discussion, this study gives a clear image about the performance of different network topologies while providing some recommendations for the upcoming researches. 

##### **4. CLEE-based WSN topology** 

Cluster and tree topologies may help in overcoming several challenges in WSNs as well as enhancing the network performance in terms of different metrics. This section aims to combine both topologies in 

6 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 



**Fig. 3.** CLEE topology proposed for WSNs. 

order to take advantage of both of them and further improve the network performance, particularly in terms of lowering the sensor energy consumption and prolonging the network lifetime. Thus, it proposes a hybrid-based topology called CLEE derived from CLuster and trEE, that can gather and send data of sensor networks in an energy-efficient way. Subsequently, the network is divided into clusters where each one is composed of several sensor nodes (SNs) and has one or more cluster heads (CHs) to manage the members. Then, SNs belonging to the same cluster are organized into a tree scheme where parent nodes collect data from their children and send it to the appropriate CHs. Finally, the CHs forward the data to the sink node (Fig. 3). 

##### _4.1. CLEE topology: advantages and limitations_ 

Compared to cluster and tree topologies, CLEE topology brings new network advantages and overcomes some limitations of each of the two topologies. On one hand, the size of the tree built in the CLEE topology is less than that in the tree-based topology, which can decrease the tree building when deploying the network as well as the reconfiguration time in case of node failures. Additionally, CLEE topology provides network scalability where it becomes easier to add a new cluster without the need to reconfigure the other ones. Moreover, the energy consumption in the CLEE topology is different between nodes, where nodes closer to the CH (e.g. tree root) will consume more energy compared with leaf nodes. Lastly, the long distance between leaf nodes and CHs and the need to propagate messages through the specified hops may lead to transmission delays. 

##### _4.2. CLEE algorithm_ 

Algorithm 3 shows the hybrid process of the CLEE algorithm that combines cluster and tree schemes in the WSN context. Mainly, the network is divided into clusters while the connection between cluster nodes is not necessary to be direct from the cluster member (i.e. sensor node) to the cluster head. Additionally, the topology of each cluster is based on the tree scheme where the CH represents the root of the tree and the other tree nodes are the cluster members. 

##### **5. Topology selection algorithm** 

This section aims to create a new tool that can help in selecting the best sensor topology prior to the network deployment. The idea behind such a tool is to ensure a longer network lifetime and lower energy consumption while taking into account the application context and conditions. Thus, it develops a new algorithm that takes various potential parameters as input and provides the best network topology, according to the energy consumption. The taken parameters are listed as follows: 

- Zone area: since the function of the deployed sensors is to monitor a given zone, one of the most relevant parameters regarding the 

##### **Algorithm 3** CLEE Algorithm. 

- **Require:** Set of Sensors: _𝑆_ = { _𝑠_ 1, _𝑠_ 2, ..., _𝑠𝑛_ }, Number of Clusters: _𝐾_ . **Ensure:** Wireless Sensor Network: WSN. 1: WSNCluster ← _𝜙_ 2: **for each** sensor in _𝑆_ **do** 3: sensor.broadcastMessage(sensor.myRandomNumber); 4: **end for** 5: **for each** sensor in _𝑆_ **do** 6: numbers = sensor.RecievedNumbers(); 7: numbers.add(sensor.myRandomNumber); 8: **if** sensor.myRandomNumber is in Greatest _𝐾_ numbers and Number Of CHs _< 𝐾_ **then** 

- 9: WSNCluster.addClusterHead(sensor); 

- 10: **end if** 11: **end for** 12: **while** (no convergence) **do** 13: **for each** sensor in _𝑆_ **do** 14: clusterId = sensor.NearestCH().clusterId; 15: WSNCluster.updateMembers(clusterId, sensor); 16: **end for** 17: **for each** cluster in WSNCluster.Clusters **do** 18: clusterHead = cluster.nearestSensortoAllMembers(); 19: cluster.setCH(clusterHead); 20: **end for** 21: **end while** 22: **for each** cluster in WSNCluster.Clusters **do** 23: WSNTree ← _𝜙_ , Graph _𝐺_ ← _𝜙_ 24: **for each** sensor in cluster.sensors **do** 25: sensor.broadcastMessage(); 26: adjacents = sensor.ReciveRelpies().FromMyCluster(); 27: adjacentSensor = adjacents.nearestSensor; 28: _𝐺_ .addEdge(sensor, adjacentSensor, distance(sensor, adjacentSensor)); 29: **end for** 30: **for each** ( _𝑠𝑖_ , _𝑠𝑗_ ) in _𝐺_ .edges increasing order of weight **do** 31: **if** _𝑠𝑖_ and _𝑠𝑗_ doesnot create cycle **then** 32: WSNTree.add( _𝑠𝑖_ , _𝑠𝑗_ ) 33: **end if** 34: **end for** 35: **for each** _𝑠𝑖_ in WSNTree.Sensors **do** 36: _𝑠𝑖_ .setParent = _𝑠𝑖_ .adajcentSenors.nearestSensorToSink(); 37: **end for** 38: WSN.add(WSNTree); 39: **end for** 

- zone is its dimension, which is defined by its width and height in meters. 

- Sink position: the distance between the sink and the cluster heads or tree root may have a great impact on the energy consumption, where the maximum data quantity is transformed from the cluster heads or tree root to the sink. 

- Sensors number: the number of deployed sensors used to monitor the targeted zone plays a vital role in WSN since it can affect the number of clusters and data flow. 

- Sensor positions: they represent the location of all the deployed sensors where the position of each sensor is defined by ( _𝑥_ , _𝑦_ ). The positions of the sensors and their distribution are the main keys that are used while building the tree and the clusters and determining the data flow. Additionally, the distance between the sender and receiver is one of the essential parameters that are used in calculating the energy consumed in sensor networks. 

- Sensor transmission range: it represents the range at which the sensor can send the data that mainly depends on the sensor capabilities and hardware. 

##### _5.1. Energy consumption evaluation_ 

Our simulations used the Heinzelman model [44,45] which is the most popular model for energy consumption estimation to evaluate the energy consumption in the network under different scenarios. In such 

7 

_Results in Engineering 27 (2025) 105823_ 

###### _H. Harb, K. Danach, M. AlAkkoumi et al._ 

model, energy consumption is highly dependent on the data transmission and reception in the network. The energy consumption is calculated as follows: 

##### _5.1.1. Energy consumed during data transmission_ 



<!-- Start of picture text -->
𝐸𝑇 ( 𝑘,𝑑 ) =  𝐸𝑒𝑙𝑒𝑐 ×  𝑘 +  𝛽𝑎𝑚𝑝 ×  𝑘 ×  𝑑 2 (10)<br><!-- End of picture text -->

where: 

- _𝐸𝑇_ is the consumed energy by the sensor during the transmission. 

- _𝑘_ is the number of bits that must be sent. 

- _𝑑_ is the distance between the sender and the receiver. 

- _𝛽𝑎𝑚𝑝_ is a constant with a value of 100 pJ/bit/ _𝑚_<sup>2</sup> 

- _𝐸𝑒𝑙𝑒𝑐_ is a constant with a value of 50 nJ/bit 

##### _5.1.2. Energy consumed during data reception_ 

##### _𝐸𝑅_ ( _𝑘_ ) = _𝐸𝑒𝑙𝑒𝑐_ × _𝑘_ (11) 

where: 

**Table 2** 

Simulation parameters. 

|Parameter|Values|
|---|---|
|Number of Sensors (_𝑁_)|_𝑁_1= 30<br>_𝑁_2= 50<br>_𝑁_3= 100<br>_𝑁_4=<br>1000|
|Monitored Area (_𝑀_<sup>2</sup>)|_𝑀_<sup>2</sup><br>1 <sup>= 100</sup><br>_𝑀_<sup>2</sup><br>2 <sup>= 500</sup><br>_𝑀_<sup>2</sup><br>3 <sup>= 1000</sup><br>_𝑀_<sup>2</sup><br>4 <sup>=</sup><br>10000|
|Sink position (_𝑥_, _𝑦_)|random, where (0,0)≤(_𝑥_,_𝑦_) ≤(_𝑀_,_𝑀_)|
|Number of Clusters (_𝐾_)|_𝐾_1= 0_._05 ×_𝑁_<br>_𝐾_2= 0_._1 ×_𝑁_<br>_𝐾_3= 0_._2 ×_𝑁_|
||_𝐾_4= 0_._3 ×_𝑁_|
||_𝐾_5= 0_._4 ×_𝑁_|
||_𝐾_6= 0_._5 ×_𝑁_<br>_𝐾_7=<br>√<br>_𝑁_∕2|



- _𝐸𝑅_ is the consumed energy by the sensor during the receiving. 

- _𝑘_ is the number of received bits. 

- _𝐸𝑒𝑙𝑒𝑐_ is a constant with a value of 50 nJ/bit. 

##### _5.2. Simulation scenarios_ 

Our algorithm passes through 3 main stages where, at each stage, it tries to examine the different parameters and then update and improve our algorithm based on the obtained results to reach our goal. 

##### _5.2.1. Scenario_ 1 

This scenario compares classical tree topology versus classical clustering topology. Accordingly, it creates sensor nodes and examine the energy consumption of the tree and clusters. 

##### _5.2.2. Scenario_ 2 

In this scenario, a significant and effective change was made to the tree algorithm while keeping the classical clustering algorithm. Regarding the tree algorithm, since the largest amount of data will be transmitted from the tree root to the sink, it applies the following constraint while choosing the tree root: The root of the tree should be the nearest sensor to the sink, so the data flow should be toward this node. 

##### _5.2.3. Scenario_ 3 

The last scenario implements the CLEE topology, then it compares the results with the classical clustering and tree topologies shown in the second scenario. 

##### **6. Results and discussions** 

The main goal of the simulation described in this section is to measure the performance of energy consumption and network lifetime on different network topologies. The algorithm implementation and simulation are written in Python language using Jupyter Notebook software. The WSN is represented by a different number of sensors generated randomly and deployed over a squared area of ( _𝑁_ × _𝑁_ ) with a linear increase in width and height. The number of sensor nodes increases with the increase in area. The sink node is generated randomly over the area at position [ _𝑥_ , _𝑦_ ], where 0 ≤ _𝑥,𝑦_ ≤ _𝑁_ . It is assumed that the data generated by each sensor node is equal to 1. The proposed simulation parameters are shown in Table 2. In our simulation, it is considered the three scenarios described in the previous section, where each scenario runs will all the different parameters mentioned in Table 2. Each run is tested four times on different random sink positions, e.g. scenarios 1 

and 2, to improve the robustness of the algorithm, while in scenario 3 the CLEE-topology is added. 

##### _6.1. Scenario_ 1 _: evaluation and discussion_ 

This scenario compared the energy consumption of tree-based versus seven cluster-based typologies, where each simulation is tested with four different random sink positions (Fig. 4). In Fig. 4(a), 30 sensors were deployed randomly over a squared area of 100 meters. It notices that cluster-based topology is better than tree-based in saving energy in all cases. In Fig. 4(b), it is randomly deployed 50 sensors over a squared area of 500 meters, and it is noticed that cluster-based topology is better than tree-based in some cases, while the tree-topology is better in other ones. In Fig. 4(c), 100 sensors have been randomly deployed over 1000 squared area, and cluster topology performs better than a tree in almost all cases. In Fig. 4(d), 1000 sensors are randomly deployed over a 10000 squared area, and it has been shown that both topologies give similar results, except for the last case. 

This scenario does not give a significant conclusion to decide which topology is better. Overall, neither the tree nor the clustering is always the best. However, one of the most important insights shown in this simulation is that the sink position has a high impact on energy consumption, especially in large WSNs. This is justified since the larger amount of data is transmitted from the tree root or CHs to the sink, where the needed energy to transmit this data is directly affected by the distance between the sender (e.g. tree root or CHs) and the receiver (e.g. sink). As shown in Fig. 4, when the sink position was more to the edge of the tree then the energy consumption increased. When it was at a more intermediate position then it decreased through balancing the energy consumption of nodes. The more balanced positioning the lower the energy consumption. 

##### _6.2. Scenario_ 2 _: evaluation and discussion_ 

This scenario adapted the same simulation environment as that in the previous scenario with one significant change to the tree algorithm where the tree root is selected as the nearest sensor to the sink. The idea behind such modification is that, in tree-based topology, the tree root of the WSN carries all the data aggregated by the tree along with its data and transmits it to the sink. Therefore, the distance between the root and the sink can affect the network lifetime and the energy consumed by sensors. 

Fig. 5 (a to d) shows the energy consumption in the sensor network through the function of the sink position, the number of sensors 

8 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 





**Fig. 4.** Scenario 1: energy consumption evaluation. 





**Fig. 5.** Scenario 2: energy consumption evaluation. 

and the network dimension. In Fig. 5(a), it is observed that the clusterbased topology consumes less energy than the tree because there are no long distances between clusters during data transmission. Otherwise, in Fig. 5(b), it is observed that the tree-based topology performs better than the cluster-based in all cases. The same observation is noticed in Figs. 5(c) and 5(d) where the tree performance gives better results compared to the clusters in all cases. 

This scenario can clearly demonstrate the importance of the tree root selection in sensor networks. It saves more energy compared to clustering, especially in large areas. This is due to the large distance of transmission between the cluster heads and the sink, which was canceled in the tree. Overall, the tree is better than clustering when the number of sensors is greater than 50, and this is due to the high impact on energy consumption when selecting the tree root. It can also 

9 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 



**Fig. 6.** Scenario 3: energy consumption evaluation. 

be concluded that the impact of the sink position on the overall energy consumption decreases significantly. 

either extend the network lifetime or reduce it. In the case of using clustering, sink position has a high impact on the energy consumption of the network, and can also extend or reduce its lifetime. 

##### _6.3. Scenario_ 3 _: evaluation and discussion_ 

This scenario combines cluster and tree topologies together in a hybrid architecture called CLEE. As described before, in the CLEE topology, the cluster members form a tree shape where each cluster head acts as the root of the tree. The second change occurred in the testing simulation where each iteration tests the consumption for one time on one random sink position on the three different topologies (Fig. 6). Overall, the CLEE topology has a significant added value compared to the previous scenarios. It is noticed that the clustering topology outperforms the tree and hybrid topologies when the number of sensors is less than or equal to 30 (Figs. 6(a) and 6(b)). Whilst, the CLEE topology outperforms the other schemes for a bigger network size, where the number of sensors is greater than 100 (Figs. 6(c) and 6(d)). 

This scenario can deduce that integrating a hybrid topology is beneficial for energy conservation in sensor networks. Additionally, the range root-sink and CH-sink play a big role in the energy consumption of the whole network; selecting a tree root is a very critical step which can 

##### _6.4. Simulation scenarios: main findings and further discussion_ 

This section gives further consideration to various topologies studied while summarizing the obtained results and analyzing their performance regarding several metrics and under various conditions. 

From the sink position point of view, our simulation demonstrated a high impact of sink position, either random (scenario 1) or determined (scenario 2), to the energy consumption in the network. On one hand, the first scenario shows that cluster-based topology outperforms better than tree-based one in case of less-dense network size. Consequently, when the experts target a small sensor network deployment, it is advised to adapt cluster topology in order to save the sensor energies and extend the network lifetime. Whilst, the tree-based topology demonstrated its superiority when the tree root is near the sink and for a large monitoring zone. Thus, adapting tree topology under such conditions will highly preserving the network energy. 

10 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

**Table 3** 

An analytical comparison of various sensor network topologies. 

|Performance Metric|Topology|Type||
|---|---|---|---|
||Cluster|Tree|CLEE|
|Reconfiguration Time|Low|High|Medium|
|Energy Consumption|Low|Low|Low|
|Scalability|High|Medium|High|
|Node Failure Recovery|Easy|Difficult|Moderate|
|Network Congestion|Medium|High|Medium|
|Packet Loss|Medium|High|Medium|
|Transmission Delay|Low|High|Low|



From the data transmission point of view, our simulation demonstrated that CLEE topology offers a robustness and compromised solution compared to tree and cluster topologies. It allows to avoid the long distance transmission between node-sink or node-CH as in clustering scheme, and reduce simultaneously the number of packets forwarded in the network as in tree scheme. Such improvement in data transmission will highly affect some important metrics in wireless networks such as scalability, congestion, energy consumption and network lifetime. Consequently, CLEE topology is considered as the most suitable solution for experts independent from the network size. 

As a summary, Table 3 shows an analytical comparison among various topologies evaluated in this study for upcoming research directions and investigations. 

##### _6.5. Study limitations and future research directions_ 

Despite the promising results and insights presented in this study, several limitations are eminent that may open directions for future works. Particularly, it is focused on the following points: 

- _Security_ : indeed, ensuring a secure data communication is a critical operation in sensor networks [46,47]. Particularly, security becomes more important when the sensor network is deployed in sensitive and mission-critical applications such as healthcare monitoring, environmental surveillance, military operations, and industrial automation [48,49]. Thus, deploying sensor networks in these environments makes them vulnerable to a wide range of threats including poisoning attack, data interception, node compromise, denial-of-service attacks, and false data injection [50,51]. Given that sensor nodes typically have limited computation resources, implementing robust yet lightweight security mechanisms becomes essential to ensure data integrity, confidentiality, and network availability [52,53]. Although researchers have proposed a wide range of security mechanisms (such as SIKE [54]), cryptography methods (such as CRC and Hamming code [55], and number theoretic transform [56]), encryption standards (such as S-boxes [57] and AES [58]), and secure hash functions [59], strengthening the security of sensor networks is becoming more essential due to the limited hardware of the sensor design, the huge numbers of deployed sensor devices, and the exponential emerging attack types. 

- _Heterogeneity_ : this study focused our attention to homogenous networks where all sensors are monitoring the same physical condition and have the same resources. However, this study may not have explored the heterogeneity of sensor networks, whether vertical or horizontal. On one hand, the vertical heterogeneity indicates the ability of each node to monitor various physical conditions at the same time while, on the other hand, the horizontal heterogeneity indicates the ability of network of having devices with different resources capabilities. Future directions should evaluate the performance of various network topologies considering both types of heterogeneity. 

- _Complexity_ : certain assumptions were made in this study to simplify the modeling and analysis evaluation, which might not fully capture the complexity of real-life sensor network applications. For instance, idealized network conditions such as uniform node distribution, stable communication links, and consistent energy consumption rates were considered to streamline the simulation process. However, real-world sensor networks often face dynamic environmental factors, unpredictable node failures, heterogeneous hardware capabilities, and varying energy constraints, all of which can significantly influence network performance. While the current findings provide valuable insights, further studies incorporating more realistic scenarios and adaptive models are necessary to ensure broader applicability and robustness of the proposed approach. 

##### **7. Conclusions and future works** 

Selecting the best sensor network topology is a crucial decision for experts due to its severe impact on energy consumption and network lifetime. In this paper, our objective was to study the performance of the most commonly used topologies, e.g. cluster and tree, in sensor networks. Then, it has demonstrated the importance of taking advantage of both topologies to introduce a hybrid one (CLEE topology). Then, it has proposed a novel selection algorithm that provides practical means to choose which adequate topology is better to use for WSN applications and under which circumstances. The performance of each topology in terms of energy consumption has been shown through different extensive simulation scenarios where, in each scenario, some changes were made to the implemented algorithm. Our algorithm is upgraded and developed to get a stronger conclusion and to cover more possible scenarios that may be faced by experts deploying WSNs. 

It seeks to include more topologies and algorithms to be covered to get a stronger conclusion and cover more possible scenarios; more tests will be done on larger parameters to get higher accuracy. It also plans to validate the findings of this work in heterogeneous sensor networks where each sensor node may have different resources compared to other ones. 

##### **CRediT authorship contribution statement** 

**Hassan Harb:** Writing – review & editing, Writing – original draft, Validation, Investigation, Formal analysis, Data curation, Conceptualization. **Kassem Danach:** Writing – review & editing, Investigation, Formal analysis, Data curation, Conceptualization. **Mouhammad AlAkkoumi:** Validation, Supervision, Resources, Investigation, Conceptualization. **Ali Jaber:** Writing – review & editing, Validation, Supervision, Software, Resources, Conceptualization. **Chady Abou Jaoude:** Writing – review & editing, Methodology, Investigation, Formal analysis, Conceptualization. **Abbass Nasser:** Writing – review & editing, Supervision, Project administration, Methodology, Formal analysis, Conceptualization. 

##### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

##### **Data availability** 

No data was used for the research described in the article. 

##### **References** 

> [1] R. Shyamsundar, M. Harshavarthan, et al., A cluster based routing for maximizing the lifetime of underwater wireless sensor network using gravitational search algorithm, Results Eng. 25 (2025) 104470. 

11 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

- [2] Faran Awais Butt, Madiha Jalil, Salman Liaquat, Saleh Ahmed Alawsh, Ijaz Haider Naqvi, Nor Muzlifah Mahyuddin, Ali Hussein Muqaibel, Self-calibration of wireless sensor networks using adaptive filtering techniques, Results Eng. 25 (2025) 103775. 

- [3] Mohammad Reza Najarzadegan, Ramtin Moeini, Maximizing the coverage of quality sensors in the water distribution network (case studies: Lee and deininger and the second and the third epanet networks), Results Eng. (2025) 104334. 

- [4] Taher Alzahrani, Saima Rashid, Unlocking the potential of secure communications: a comprehensive systematic review of the network design model for topology control and routing synergy in wireless sensor networks for prolonged longevity, Results Eng. (2025) 104450. 

- [5] Hassan Kanj, Abdullah Aljeri, Tarek Khalifa, Agent-based model for oil storage monitor and control system using IoT, in: International Conference on Computing, Intelligence and Data Analytics, Springer, 2023, pp. 241–250. 

- [6] Hassan Harb, Abdallah Makhoul, Chady Abou Jaoude, En-route data filtering technique for maximizing wireless sensor network lifetime, in: 2018 14th International Wireless Communications & Mobile Computing Conference (IWCMC), IEEE, 2018, pp. 298–303. 

- [7] Marwa Ibrahim, Hassan Harb, Ali Mansour, Abbass Nasser, Christophe Osswald, Allin-one: toward hybrid data collection and energy saving mechanism in sensing-based IoT applications, Peer-to-Peer Netw. Appl. 14 (3) (2021) 1154–1173. 

- [8] Hassan Harb, Chady Abou Jaoude, Abdallah Makhoul, An energy-efficient data prediction and processing approach for the Internet of things and sensing based applications, Peer-to-Peer Netw. Appl. 13 (3) (2020) 780–795. 

- [9] Kawthar Zaraket, Ismail Bennis, Hassan Harb, Ali Jaber, Abdelhafid Abouaissa, Outlier detection based model for event pattern recognition in vehicular networks, in: 2024 20th International Conference on Wireless and Mobile Computing, Networking and Communications (WiMob), IEEE, 2024, pp. 56–61. 

- [10] Kawthar Zaraket, Hassan Harb, Ismail Bennis, Ali Jaber, Abedalhafid Abouaissa, Hyper-flophet: a neural prophet-based model for traffic flow forecasting in transportation systems, Simul. Model. Pract. Theory 134 (2024) 102954. 

- [11] Suoping Li, Youyi Yuan, Guodong Pan, An efficient ss-mac protocol for IEEE 802.15. 4-based wsns of cluster tree topology, Electronics 13 (13) (2024) 2520. 

- [12] R. Lalitha, A.V. Senthil Kumar, Improving the reliability of wireless sensor network assisted IoT network with a cluster-based chain-tree routing protocol, J. Intell. Syst. Internet Things 16 (2) (2025). 

- [13] Fakhrosadat Fanian, Marjan Kuchaki Rafsanjani, Cluster-based routing protocols in wireless sensor networks: a survey based on methodology, J. Netw. Comput. Appl. 142 (2019) 111–142. 

- [14] Trupti Mayee Behera, Umesh Chandra Samal, Sushanta Kumar Mohapatra, Mohammad S. Khan, Bhargav Appasani, Nicu Bizon, Phatiphat Thounthong, Energy-efficient routing protocols for wireless sensor networks: architectures, strategies, and performance, Electronics 11 (15) (2022) 2282. 

- [15] K. Suresh, S.S. Sreeja Mole, A. Joseph Selva Kumar, F2so: an energy efficient cluster based routing protocol using fuzzy firebug swarm optimization algorithm in wsn, Comput. J. 66 (5) (2023) 1126–1138. 

- [16] Vipul Narayan, A.K. Daniel, Pooja Chaturvedi, E-feerp: enhanced fuzzy based energy efficient routing protocol for wireless sensor network, Wirel. Pers. Commun. (2023) 1–28. 

- [17] Panimalar Kathiroli, Kanmani Selvadurai, Energy efficient cluster head selection using improved sparrow search algorithm in wireless sensor networks, J. King Saud Univ, Comput. Inf. Sci. 34 (10) (2022) 8564–8575. 

- [18] Noureddine Moussa, Zakaria Hamidi-Alaoui, Abdelbaki El Belrhiti El Alaoui, ECRP: an energy-aware cluster-based routing protocol for wireless sensor networks, Wirel. Netw. 26 (2020) 2915–2928. 

- [19] Kashif Naseer Qureshi, Muhammad Umair Bashir, Jaime Lloret, Antonio Leon, Optimized cluster-based dynamic energy-aware routing protocol for wireless sensor networks in agriculture precision, J. Sens. 2020 (2020) 1–19. 

- [20] Le Tuong, Minh Thanh Vo, Tung Kieu, Eenjun Hwang, Seungmin Rho, Sung Wook Baik, Multiple electric energy consumption forecasting using a cluster-based strategy for transfer learning in smart building, Sensors 20 (9) (2020) 2668. 

- [21] Jin Wang, Yu Gao, Wei Liu, Arun Kumar Sangaiah, Hye-Jin Kim, Energy efficient routing algorithm with mobile sink support for wireless sensor networks, Sensors 19 (7) (2019) 1494. 

- [22] Bechir Ben Gouissem, Rahma Gantassi, Salem Hasnaoui, Energy efficient grid based k-means clustering algorithm for large scale wireless sensor networks, Int. J. Commun. Syst. 35 (14) (2022) e5255. 

- [23] Ganesh Jayaraman, V.R. Sarma Dhulipala, Feecs: fuzzy-based energy-efficient cluster head selection algorithm for lifetime enhancement of wireless sensor networks, Arab. J. Sci. Eng. 47 (2) (2022) 1631–1641. 

- [24] P. Vijayaragavan, V. Saravanan, Chalumuru Suresh, D. Manikavelan, A. Maheshwari, K. Vijayalakshmi, Roman Hrbac, Lukas Demel, Vaclav Kolar, R. Narayanamoorthi, Foaeauc-sarp: a novel energy-efficient protocol integrating unequal clustering and intelligent routing for sustainable wireless sensor networks, Results Eng. 25 (2025) 103806. 

- [25] Lucia K. Ketshabetswe, Adamu Murtala Zungeru, Caspar K. Lebekwe, Bokani Mtengi, A compression-based routing strategy for energy saving in wireless sensor networks, Results Eng. 23 (2024) 102616. 

- [26] M. Manikandan, S. Sakthivel, V. Vivekanandhan, Efficient clustering using memetic adaptive hill climbing algorithm in wsn, Intell. Autom. Soft Comput. 35 (3) (2023). 

- [27] Kuang-Yen Tai, Bo-Chen Liu, Chiu-Han Hsiao, Ming-Chi Tsai, Frank Yeong-Sung Lin, A near-optimal energy management mechanism considering qos and fairness requirements in tree structure wireless sensor networks, Sensors 23 (2) (2023) 763. 

- [28] Li-Yong Yuan, Fei-Long Lin, Collection tree-oriented mesh routing optimization for extending the lifetime of wireless sensor networks, Int. J. Distrib. Sens. Netw. 18 (3) (2022) 15501329221085495. 

- [29] Qian Wei, Ke Bai, Lin Zhou, An improved approach for wireless sensor networks with mobile sink using dynamic minimum spanning tree, IEEE Sens. J. 22 (11) (2022) 10918–10930. 

- [30] Qinbin He, Jinping Mou, Bin Lin, A robust self-organizing tree-based routing protocol for wireless sensor networks, Math. Probl. Eng. 2021 (2021) 1–13. 

- [31] Arian Yousefiankalareh, Ali Najari, Mehdi Hosseynzadeh, Tree-based routing protocol in wireless sensor networks using optimization algorithm batch particles with a mobile sink, in: 2020 IEEE 17th International Conference on Smart Communities: Improving Quality of Life Using ICT, IoT and AI (HONET), IEEE, 2020, pp. 1–5. 

- [32] Pranesh, Santhosh L. Deshpande, Tree-based approaches for improving energy efficiency and life time of wireless sensor networks (wsn): a survey and future scope for research, in: Inventive Communication and Computational Technologies: Proceedings of ICICCT 2019, Springer, 2020, pp. 583–590. 

- [33] Khaled Hamouid, Salwa Othmen, Amine Barkat, Lstr: lightweight and secure treebased routing for wireless sensor networks, Wirel. Pers. Commun. 112 (2020) 1479–1501. 

- [34] Zhaohui Zhang, Jing Li, Xiaoli Yang, Data aggregation in heterogeneous wireless sensor networks by using local tree reconstruction algorithm, Complexity 2020 (2020) 1–14. 

- [35] Mohammad-Salar Shahryari, Leili Farzinvash, Mohammad-Reza Feizi-Derakhshi, Amir Taherkordi, High-throughput and energy-efficient data gathering in heterogeneous multi-channel wireless sensor networks using genetic algorithm, Ad Hoc Netw. 139 (2023) 103041. 

- [36] Pingzhang Gou, Baoyong Guo, Miao Guo, Shun Mao, Vkece-3d: energy-efficient coverage enhancement in three-dimensional heterogeneous wireless sensor networks based on 3d-Voronoi and k-means algorithm, Sensors 23 (2) (2023) 573. 

- [37] Zhibin Liu, Yuhan Liu, Xinshui Wang, Intelligent routing algorithm for wireless sensor networks dynamically guided by distributed neural networks, Comput. Commun. (2023). 

- [38] Mostafa EA Ibrahim, Alaa ES Ahmed, Energy-aware intelligent hybrid routing protocol for wireless sensor networks, Concurr. Comput., Pract. Exp. 34 (3) (2022) e6601. 

- [39] Yangbin Zhang, Lihua Liu, Mao Wang, Jibing Wu, Hongbin Huang, An improved routing protocol for raw data collection in multihop wireless sensor networks, Comput. Commun. 188 (2022) 66–80. 

- [40] Meriem Meddah, Rim Haddad, Tahar Ezzedine, An efficient mobile data gathering method with tree clustering algorithm in wireless sensor networks balanced and unbalanced topologies, Wirel. Pers. Commun. (2022) 1–19. 

- [41] Karunanithy Kalaivanan, Bhanumathi Velusamy, Cluster-tree based energy efficient data gathering protocol for industrial automation using wsns and IoT, J. Ind. Inf. Integr. 19 (2020) 100156. 

- [42] JiaYu Lu, KongFa Hu, XiChen Yang, ChenJun Hu, TianShu Wang, A cluster-treebased energy-efficient routing protocol for wireless sensor networks with a mobile sink, J. Supercomput. 77 (2021) 6078–6104. 

- [43] Kristina P. Sinaga, Miin-Shen Yang, Unsupervised k-means clustering algorithm, IEEE Access 8 (2020) 80716–80727. 

- [44] Wendi Rabiner Heinzelman, Anantha Chandrakasan, Hari Balakrishnan, Energyefficient communication protocol for wireless microsensor networks, in: Proceedings of the 33rd Annual Hawaii International Conference on System Sciences, IEEE, 2000, pp. 3005–3014. 

- [45] Wendi Beth Heinzelman, Application-specific protocol architectures for wireless networks, PhD thesis, Massachusetts Institute of Technology, 2000. 

- [46] Daniel Owens, Rabih El Khatib, Mojtaba Bisheh-Niasar, Reza Azarderakhsh, Mehran Mozaffari Kermani, Efficient and side-channel resistant ed25519 on arm cortex-m4, IEEE Trans. Circuits Syst. I, Regul. Pap. (2024). 

- [47] Mila Anastasova, Reza Azarderakhsh, Mehran Mozaffari Kermani, Fully hybrid tlsv1. 3 in wolfssl on cortex-m4, in: International Conference on Applied Cryptography and Network Security, Springer, 2024, pp. 376–395. 

- [48] Mehran Mozaffari Kermani, Reza Azarderakhsh, Mehdi Mirakhorli, Education and Research Integration of Emerging Multidisciplinary Medical Devices Security, Rochester Institute of Technology, 2016, pp. 1–14. 

- [49] Arsalan Mohsen Nia, Mehran Mozaffari-Kermani, Susmita Sur-Kolay, Anand Raghunathan, Niraj K. Jha, Energy-efficient long-term continuous personal health monitoring, IEEE Trans. Multi-Scale Comput. Syst. 1 (2) (2015) 85–98. 

- [50] Mehran Mozaffari-Kermani, Susmita Sur-Kolay, Anand Raghunathan, Niraj K. Jha, Systematic poisoning attacks on and defenses for machine learning in healthcare, IEEE J. Biomed. Health Inform. 19 (6) (2014) 1893–1905. 

- [51] Mehran Mozaffari-Kermani, Arash Reyhani-Masoleh, Concurrent structureindependent fault detection schemes for the advanced encryption standard, IEEE Trans. Comput. 59 (5) (2010) 608–622. 

- [52] Brian Koziel, Reza Azarderakhsh, Mehran Mozaffari Kermani, David Jao, Postquantum cryptography on fpga based on isogenies on elliptic curves, IEEE Trans. Circuits Syst. I, Regul. Pap. 64 (1) (2016) 86–99. 

- [53] Rami Elkhatib, Brian Koziel, Reza Azarderakhsh, Mehran Mozaffari Kermani, Cryptographic engineering a fast and efficient sike in fpga, ACM Trans. Embed. Comput. Syst. 23 (2) (2024) 1–25. 

12 

_H. Harb, K. Danach, M. AlAkkoumi et al._ 

_Results in Engineering 27 (2025) 105823_ 

- [54] Mila Anastasova, Reza Azarderakhsh, Mehran Mozaffari Kermani, Fast strategies for the implementation of sike round 3 on arm cortex-m4, IEEE Trans. Circuits Syst. I, Regul. Pap. 68 (10) (2021) 4129–4141. 

- [55] Alvaro Cintas-Canto, Mehran Mozaffari Kermani, Reza Azarderakhsh, Error detection constructions for ita finite field inversions over gf2m on fpga using crc and Hamming codes, IEEE Trans. Reliab. 72 (2) (2022) 651–661. 

- [56] Mojtaba Bisheh-Niasar, Reza Azarderakhsh, Mehran Mozaffari-Kermani, High-speed ntt-based polynomial multiplication accelerator for post-quantum cryptography, in: 2021 IEEE 28th Symposium on Computer Arithmetic (ARITH), IEEE, 2021, pp. 94–101. 

marked on asic, in: 2018 IEEE 61st International Midwest Symposium on Circuits and Systems (MWSCAS), IEEE, 2018, pp. 574–577. 

   - [58] Mehran Mozaffari-Kermani, Arash Reyhani-Masoleh, A low-cost s-box for the advanced encryption standard using normal basis, in: 2009 IEEE International Conference on Electro/Information Technology, IEEE, 2009, pp. 52–55. 

   - [59] Mehran Mozaffari Kermani, Reza Azarderakhsh, Siavash Bayat-Sarmadi, Reliable hardware architectures for efficient secure hash functions echo and fugue, in: Proceedings of the 15th ACM International Conference on Computing Frontiers, 2018, pp. 204–207. 

- [57] Anita Aghaie, Mehran Mozaffari Kermani, Reza Azarderakhsh, Design-for-errordetection in implementations of cryptographic nonlinear substitution boxes bench- 

13 

