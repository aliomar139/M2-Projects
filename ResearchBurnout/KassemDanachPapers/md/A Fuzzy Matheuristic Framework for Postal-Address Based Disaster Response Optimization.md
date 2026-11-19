Eng. Sci., 2026, **41** , 2271 



## Engineered Science 

DOI: https://dx.doi.org/10.30919/es2271 





# **A Fuzzy Matheuristic Framework for Postal-Address Based Disaster Response Optimization** 

Kassem Danach,<sup>1,*</sup> Wael Hosny Fouad Aly<sup>2</sup> and Mohamad Msheik<sup>1</sup> 

### **Abstract** 

This paper presents a novel hybrid framework integrating fuzzy logic and matheuristic optimization for disaster response planning within the Australian postal geography context. The approach addresses critical uncertainty challenges in disaster demand estimation through fuzzy inference systems applied to spatial attributes (damage severity, population density, accessibility), while matheuristics combining integer programming and metaheuristic search—optimize relief resource allocation and routing across postal address zones. Using real datasets from Australia Post (geocoded postal address files) and the Australian Disaster Events Impact dataset, we construct realistic case studies for flood and bushfire scenarios. Experimental results demonstrate that the fuzzy–matheuristic approach achieves superior coverage (93.2% vs. 76.5% for deterministic IP) and cost-effectiveness (15% reduction under high uncertainty) compared to conventional methods. The framework provides a robust, data-driven decision-support tool for emergency planners and postal logistics managers, with significant implications for improving disaster response outcomes. 

_Keywords:_ Fuzzy logic; Matheuristic optimization; Disaster management; Postal network; Australia post dataset. Received: 15 February 2026; Revised: 03 May 2026; Accepted: 13 May 2026 Article type: Research article. 

#### **1. Introduction** 

Disaster response operations present significant challenges in resource allocation under conditions of high uncertainty and time pressure.<sup>[1]</sup> Traditional deterministic optimization methods often fail to capture the inherent imprecision in disaster data, leading to suboptimal decisions when implemented in real-world scenarios.<sup>[2]</sup> This limitation is particularly problematic in large-scale disasters affecting extensive geographical regions, where thousands of spatial units require coordinated response efforts. 

Fuzzy logic provides a mathematically rigorous approach to modeling uncertainty in disaster contexts,<sup>[3]</sup> allowing for the representation of imprecise information through linguistic variables and rule-based inference systems. Meanwhile, matheuristic methods—hybrids of mathematical programming and metaheuristic algorithms—have demonstrated significant promise in solving large-scale combinatorial optimization problems efficiently.<sup>[4,5]</sup> These methods balance the optimality guarantees of mathematical programming with the 

_1Basic and Applied Sciences Research Center, Al Maaref University, Beirut, 1001, Lebanon_ 

_2College of Engineering and Technology, American University of the Middle East, Egaila,54200, Kuwait_ 

> _*Email:_ kassem.danach@mu.edu.lb (K. Danach) 

exploratory capabilities of metaheuristics, making them particularly suitable for complex disaster logistics problems. 

Despite advances in both fields, few studies have integrated fuzzy logic and matheuristics within a postal or address-based spatial framework for disaster response. This research gap is significant given the potential of postal networks to provide fine-grained spatial units for resource allocation and delivery planning. Postal address systems offer several advantages over traditional administrative boundaries: they are designed for efficient routing, they cover entire countries comprehensively, and they can be linked to demographic and infrastructure data at a highly granular level. 

This study addresses this gap by proposing and validating a novel fuzzy matheuristic framework specifically designed for postal geography-based disaster response optimization. The framework leverages Australia’s comprehensive postal address datasets to create realistic disaster scenarios and evaluate response strategies. Our approach makes several important contributions to the field of disaster management and operations research.<sup>[6]</sup> 

#### **1.1 Problem statement** 

Disaster response planning faces three fundamental 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **1** 

**Research article                                                                                                                                                                                Engineered Science** 

challenges that existing approaches fail to adequately address: **Data uncertainty:** Disaster impact assessments involve imprecise measurements of damage severity, population displacement, and infrastructure accessibility. Traditional deterministic models cannot adequately represent this uncertainty, leading to brittle solutions that perform poorly when actual conditions differ from assumptions.<sup>[7]</sup> 

**Computational complexity:** Large-scale disaster scenarios involving thousands of postal zones create NPhard optimization problems that exceed the capabilities of exact mathematical programming methods within operational timeframes.<sup>[8]</sup> This computational barrier often forces practitioners to use simplified models or heuristic approaches that sacrifice solution quality. 

**Spatial fragmentation:** Existing models typically aggregate demand at coarse administrative levels ( _e.g_ ., cities or districts), losing critical granularity for effective last-mile delivery planning.<sup>[9]</sup> This aggregation obscures important variations in demand density, accessibility, and infrastructure conditions at the neighborhood level. 

These limitations result in suboptimal resource distribution, delayed response times, and unnecessary suffering in affected communities. A new approach is needed that can simultaneously address uncertainty, computational complexity, and spatial granularity in disaster response planning. 

#### **1.2 Research objectives** 

This research aims to develop and validate a novel hybrid optimization framework that addresses the aforementioned challenges through the following specific objectives: **Develop a fuzzy inference system** to quantify disasterinduced demand uncertainty at the postal zone level by integrating spatial attributes, including damage severity, population density, and accessibility metrics. **Formulate a matheuristic optimization model** that combines integer programming with metaheuristic search to efficiently solve large-scale resource allocation and routing problems across postal geographies. 

**Implement a spatial decision support framework** that leverages Australia’s postal address datasets to create realistic disaster scenarios and evaluate response strategies. 

**Validate the framework’s effectiveness** through comparative analysis against conventional methods using real-world disaster data from Australia, demonstrating improvements in coverage, cost-efficiency, and computational performance. 

#### **1.3 Research contributions** 

This study makes several significant contributions to disaster management and operations research: **Methodological innovation:** First integration of fuzzy logic and matheuristics within a postal geography framework for disaster response optimization, providing a new approach to handling uncertainty and complexity in spatial decision-making. 

**Practical application:** Demonstration of how postal address datasets can be leveraged for fine-grained disaster planning, providing a template for other countries with similar postal infrastructure. 

**Empirical validation:** Comprehensive evaluation using real Australian disaster data that quantifies performance improvements under varying uncertainty conditions, establishing the practical value of the approach. 

**Decision support tool:** Implementation of a reusable framework that emergency planners and postal logistics managers can adapt for different disaster types and geographic contexts. 

The remainder of this paper is organized as follows: Section 2 reviews relevant literature on fuzzy logic applications in disaster management, matheuristics in humanitarian logistics, and Australian spatial datasets. Section 3 details the proposed framework, including the fuzzy inference system design, optimization formulation, and matheuristic algorithm. Section 4 describes the experimental setup using Australian datasets. Section 5 presents and discusses the results. Finally, Section 6 concludes with implications for practice and directions for future research. 

#### **2. Literature review** 

#### **2.1 Fuzzy logic in disaster management** 

Fuzzy logic has emerged as a powerful tool for handling uncertainty in disaster management applications.<sup>[10]</sup> demonstrated the effectiveness of fuzzy inference systems in quantifying disaster risk by integrating multiple uncertain parameters. Their approach showed significant improvements over traditional probabilistic methods in situations with limited historical data. 

Recent research has expanded the application of fuzzy logic to various aspects of disaster management.<sup>[11]</sup> developed a fuzzy-based decision support system for evacuation planning, while applying fuzzy cognitive mapping to assess community resilience to natural disasters.<sup>[12]</sup> These studies highlight the flexibility of fuzzy approaches in modeling complex, uncertain relationships in disaster contexts. 

Despite these advances, most applications of fuzzy logic in disaster management have focused on risk assessment and qualitative decision support rather than operational optimization.<sup>[13]</sup> Few studies have integrated fuzzy logic with mathematical optimization techniques to address 

**2** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

**<u>gineered Science</u>** 

resource allocation problems under uncertainty, representing a significant gap in the literature. 

#### **2.2 Matheuristics in humanitarian logistics** 

Matheuristics—hybrid algorithms combining mathematical programming with metaheuristic techniques—have gained significant traction in solving complex disaster logistics problems.<sup>[14]</sup> Recent comprehensive reviews highlight the evolution of optimization models in humanitarian logistics, emphasizing the need for approaches that can handle the unique challenges of disaster response. These hybrid methods have proven particularly valuable for large-scale, dynamic problems where traditional optimization techniques struggle with computational complexity. 

Contemporary research demonstrates the effectiveness of matheuristics across various disaster logistics contexts.<sup>[15]</sup> developed an advanced matheuristic for disaster relief distribution that integrated exact methods for facility location with adaptive large neighborhood search for vehicle routing under uncertainty. Similarly, a two-stage matheuristic was proposed for disaster preparedness planning that combined stochastic programming with ant colony optimization to address equity concerns in resource allocation.<sup>[16]</sup> More recently, a machine learning-enhanced matheuristic framework was introduced for real-time decision support in flood response operations, demonstrating significant improvements in response time and resource utilization.<sup>[17]</sup> 

Collectively, these studies show that matheuristics can effectively balance solution quality and computational efficiency for large-scale disaster logistics problems. However, most existing approaches continue to assume deterministic or probabilistic models of uncertainty, with limited attention to the possibilistic uncertainty that fuzzy logic can represent. This gap becomes particularly critical in disaster scenarios characterized by incomplete information and ambiguous parameters, where traditional uncertainty modeling approaches may fall short.<sup>[18]</sup> 

#### **2.3 Environmental dynamism in disaster management contexts** 

The increasing frequency and intensity of disasters create a highly dynamic environment that demands continuous adaptation from organizations involved in emergency response.<sup>[12]</sup> In this volatile landscape, disaster management agencies must continuously reshape their strategic approaches to maintain operational effectiveness and resilience. Operating within complex, rapidly changing systems, these organizations develop adaptive strategies by reallocating resources and forming collaborative networks with multiple stakeholders, recognizing that disaster response capabilities must evolve continuously to address emerging threats.<sup>[12]</sup> 

Technological advancements present both challenges and opportunities for disaster management operations. 

Emerging technologies such as Big Data analytics, Artificial Intelligence, and digital transformation tools place pressure on organizations to modernize their approaches.<sup>[19]</sup> These technologies enable more sophisticated disaster response systems but require significant investment in digital infrastructure and capabilities.<sup>[20]</sup> emphasized that value chain analysis provides a structured framework for optimizing disaster response operations, where data richness becomes a critical strategic asset. For instance, leading disaster response organizations have invested heavily in cloud computing and predictive analytics to enhance situational awareness and resource deployment efficiency, similar to how Amazon transformed its logistics operations through data-driven decision making.<sup>[21]</sup> 

The capacity for strategic transformation in disaster management organizations depends on three key factors: resource availability, dynamic capabilities to navigate complexity, and leadership characteristics that foster adaptability.<sup>[31]</sup> Environmental shifts directly influence organizational priorities, motivating leaders to enhance resilience and adapt to changing disaster patterns.<sup>[22]</sup> The expertise and decision-making capabilities of emergency management personnel significantly affect innovation adoption, while leadership style plays a crucial role in driving organizational transformation. Research indicates that organizations with stable leadership teams are better positioned to develop comprehensive, long-term disaster management strategies, resulting in stronger organizational consensus and more effective implementation of technological innovations.<sup>[23]</sup> This stability becomes particularly valuable in disaster contexts, where consistent vision and coordinated action are essential for effective response. 

#### **2.4 Australian context and datasets** 

Australia presents a distinctive and challenging environment for disaster response research, characterized by its vast geography, sparse population distribution, and high exposure to natural disasters including bushfires, floods, and cyclones.<sup>[29]</sup> The country has experienced several catastrophic disasters in recent years, including the devastating 2019-2020 “Black Summer” bushfires that affected over 24 million hectares, and widespread flooding in 2021-2022 that caused billions in damage.<sup>[24]</sup> These events highlight the critical need for sophisticated disaster management systems capable of operating effectively across Australia’s unique spatial challenges. 

Australia Post’s Geocoded Postal Address File (GPAF) provides an exceptional spatial dataset that enables fine-grained modeling of logistics operations across the country.<sup>[25]</sup> The G-PAF contains over 13 million geocoded addresses with precise location coordinates, aggregated to approximately 2,800 postal delivery zones. This level of spatial granularity—significantly finer than typical 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **3** 

**<u>gineered Science</u>** 

administrative boundaries used in disaster planning—offers unprecedented opportunities for optimizing resource allocation and response strategies in disaster scenarios.<sup>[26]</sup> The dataset’s comprehensive coverage of both urban and remote areas makes it particularly valuable for addressing Australia’s unique population distribution challenges. 

Complementing the postal data, the Australian Government’s Disaster Events with Category Impact and Location dataset records historical disaster events with spatial boundaries and impact metrics.<sup>[2]</sup> This dataset, when integrated with the G-PAF, allows for detailed mapping between disaster impacts and postal zones, enabling realistic scenario development for disaster response planning. Recent applications have demonstrated how this integration can support predictive modeling of disaster impacts and optimize pre-positioning of resources.<sup>[27]</sup> Fig. 1 shows the disaster response optimization framework. 

The integration of these datasets represents a significant opportunity for improving disaster response planning in Australia through advanced optimization techniques.<sup>[28]</sup> However, to date, limited research has leveraged these rich data sources for optimization-based decision support in disaster contexts. This gap is particularly notable given the potential for combining these spatial datasets with advanced optimization approaches such as Matheuristic and fuzzy logic to address the unique uncertainties and complexities of disaster management in the Australian context.<sup>[29]</sup> 

#### **3. Methodology** 

#### **3.1 Framework overview** 

The proposed framework integrates three key components to address the challenges of disaster response optimization under uncertainty: 

**Fuzzy demand estimation:** A fuzzy inference system that processes disaster and demographic indicators to quantify relief demand at the postal zone level, accounting for inherent uncertainties in disaster impact assessment. 

**Mathematical formulation:** A mixed-integer programming model that represents the allocation of relief resources across postal zones, incorporating facility location decisions and service level constraints. **Matheuristic solution:** A hybrid algorithm combining the exactness of integer programming with the exploratory power of genetic algorithms to efficiently solve large-scale instances of the optimization problem. 

The framework operates in a sequential manner (Fig. 2). First, disaster and demographic data are processed through the fuzzy inference system to generate demand estimates for each postal zone. These estimates are then fed into the optimization model, which is solved using the matheuristic approach to determine optimal resource allocation and hub 

activation decisions. 

#### **3.2 Fuzzy logic modelling** 

The fuzzy inference system (FIS) transforms imprecise input variables into a quantitative demand estimate for each postal zone. Three input variables are considered: **Damage severity:** Measured on a scale of 0-10, representing the extent of infrastructure damage in a postal zone. This is derived from disaster impact reports and satellite imagery analysis. 

**Population density:** Expressed as persons per square kilometer, obtained from census data aggregated to postal zones. 

**Accessibility:** Represented as a normalized index (0-1) combining factors such as road network integrity, distance to major highways, and elevation changes that affect delivery logistics. 

Each input variable is fuzzified using trapezoidal membership functions with linguistic terms: {Low, Medium, High} for damage severity and population density, and {Poor, Moderate, Good} for accessibility. The output variable, _demand level_ , uses five linguistic terms: {Very Low, Low, Medium, High, Very High}. Fig. 3 shows the factors influencing the demand level in postal zones.<sup>[30]</sup> 

The rule base consists of 27 rules (3 × 3 × 3) that map combinations of input linguistic terms to output demand levels. Example rules include: 

If damage severity is high, population density is high and accessibility is poor, then demand level is very high 

If damage severity is medium, population density is low and accessibility is good, then demand level is low 

The FIS uses Mamdani inference with centroid defuzzification to convert the fuzzy output into a crisp demand value. The system is implemented in Python using the scikit-fuzzy library. The calibration of membership functions and rule bases followed a structured two-stage process combining expert elicitation and empirical validation. 

First, initial trapezoidal membership parameters were defined in consultation with three domain experts: two emergency management professionals involved in New South Wales (NSW) disaster response operations and one logistics planning specialist. Experts were asked to define threshold ranges corresponding to linguistic categories (Low, Medium, High; Poor, Moderate, Good) based on operational experience during the 2019–2020 bushfires and 2021–2022 flood events. 

Second, the fuzzy inference outputs were validated against historical relief distribution records. The defuzzified demand estimates were compared with actual distributed relief quantities using Mean Absolute Percentage Error (MAPE). Membership parameters were 

**4** | _Eng. Sci._ , 2026, **41** , 2271 

**Engineered Science Publisher** 

**Research article                                                                                                                                                                                Engineered Science** 





<!-- Start of picture text -->
Fig. 1: Disaster response optimization framework.<br><!-- End of picture text -->





<!-- Start of picture text -->
Fig. 2: Overall framework workflow.<br><!-- End of picture text -->



**Fig. 3:** Factors influencing demand level in postal zones. 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **5** 

**Research article                                                                                                                                                                                Engineered Science** 

iteratively adjusted until prediction error stabilized below 8%, ensuring both expert consistency and empirical reliability. 

This hybrid calibration approach enhances transparency while grounding the fuzzy model in both experiential knowledge and real-world disaster data. 

#### **3.3 Optimization formulation** 

The optimization model determines the optimal activation of relief hubs and allocation of relief resources to postal zones, minimizing total costs while meeting service requirements. The model is defined as follows: **Sets and indices:** 

_J_ : Set of potential relief hub locations, indexed by _j K_ : Set of postal zones, indexed by _k_ **Parameters:** 

_dk_ : Fuzzy demand of zone _k_ (defuzzified value) _cjk_ : Cost of serving zone _k_ from hub _j_ (including transportation and handling) 

_Cj_ : Capacity of hub _j_ (maximum units that can be distributed) 

_fj_ : Fixed cost of activating hub _j_ (including setup and operational expenses) 

_α_ : Penalty coefficient for unmet demand (reflecting the societal cost of inadequate response) 

_β_ : Minimum service level requirement (fraction of demand that must be satisfied) **Decision variables:** 

_xj_ ∈ {0 _,_ 1}: Binary variable indicating whether hub _j_ is activated 

_yjk_ ≥ 0: Continuous variable representing units allocated from hub _j_ to zone _k_ 

_uk_ ≥ 0: Auxiliary variable representing unmet demand in zone _k_ 

The optimization problem is formulated as: 



<!-- Start of picture text -->
min Z=  ∑j∈J fjxj+  ∑j∈J ∑k∈K cjkyjk+ α ∑k∈K uk (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
s.t.  ∑k∈K yjk≤Cjxj ,          ∀j∈J (2)<br>∑j∈J yjk+uk= dk ,                ∀k∈K (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
∑j∈J yjk ≥ βdk ,              ∀k∈K   (4)<br><!-- End of picture text -->



<!-- Start of picture text -->
xj∈ {0, 1}, yjk≥0, uk≥0,        ∀j∈J, k∈K (5)<br><!-- End of picture text -->

The objective function (1) minimizes the total cost, comprising fixed costs for hub activation, variable costs for resource allocation, and penalties for unmet demand. Constraint (2) ensures that the total allocation from a hub does not exceed its capacity. Constraint (3) balances 

demand satisfaction with unmet demand. Constraint (4) enforces a minimum service level for each postal zone. Fig. 4 shows the Synergy for Disaster Response Optimization. 

#### **3.4 Matheuristic design** 

The hybrid algorithm (Algorithm 1) combines the strengths of integer programming and genetic algorithms to efficiently solve the optimization problem. The algorithm proceeds as follows: 

**Algorithm 1:** Fuzzy-Matheuristic Algorithm 

- 1: **Input:** Fuzzy demands 𝑑𝑘, cost parameters 𝑐𝑗𝑘 , 𝑓𝑗 , 𝐶𝑗 , 𝛼, 𝛽 2: **Output:** Optimal hub configuration 𝑥𝑗∗ and allocation 𝑦𝑗𝑘∗ 

- 3:   Initialize population P of N hub configurations (binary vectors) 

- 4:   Set generation counter gen = 0, maximum generations _maxGen_ 

- 5: **while** _gen < maxGen_ and not converger do 

- 6: **for** each configuration 𝑝𝑖 ∈𝑃  do 

- 7:         Solve IP subproblem with fixed 𝑥𝑗 = 𝑝𝑖[𝑗] using OR-Tools 

- 8:         Calculate fitness 𝑍𝑖 using objective function (1) 

- 9:         Store solution  (𝑥𝑗, 𝑦𝑗𝑘, 𝑢𝑘) and fitness 𝑍𝑖 

- 10: **end for** 

- 11:     Select parents vis tournament selection (size = 3) 

- 12:     Apply two-point crossover with probability 𝑝𝑐 = 0.8 

- 13:     Apply bit-flip mutation with probability 𝑝𝑚 = 0.1 

- 14:     Evaluate offspring fitness 

- 15:     Update population using elitism (keep top 20%) 

- 16: _gen←gen_ +1 

- 17: **end while** 18:   Return best solution found (𝑥𝑗∗, 𝑦𝑗𝑘∗ , 𝑢𝑘∗ <u>)</u> 

The algorithm leverages the genetic algorithm to explore the combinatorial space of hub activation decisions, while the IP subproblem efficiently solves the allocation problem for a given hub configuration. Key features include: **Decomposition strategy:** The complex problem is decomposed into a master problem (hub selection) handled by GA and a subproblem (resource allocation) solved exactly by IP. 

**Hybrid evaluation:** Each chromosome (hub configuration) is evaluated by solving the corresponding IP subproblem, ensuring feasibility and optimality for the allocation decisions. 

**Adaptive operators:** Crossover and mutation probabilities are dynamically adjusted based on population diversity to maintain exploration-exploitation balance. 

**Elitism preservation:** The best solutions are preserved across generations to guarantee monotonic improvement. 

The implementation uses Google’s OR-Tools for solving the IP subproblems and a custom genetic algorithm 

**6** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

**<u>gineered Science</u>** 



**Fig. 4:** Synergy for disaster response optimization. 

framework in Python. The algorithm parameters (population size, crossover/mutation rates) are calibrated through preliminary experiments on small-scale instances. 

#### **4. Experimental setup** 

#### **4.1 Datasets** 

**Australia post G-PAF:** Provides over 13 million geocoded addresses (aggregated to postal zones). This dataset includes latitude and longitude coordinates, postal zone identifiers, and address metadata. For our experiments, we aggregated addresses to 2,843 postal zones across New South Wales (NSW), with each zone containing an average of 4,572 addresses. The dataset was processed to calculate population density per zone by intersecting with t h e Australian Bureau of Statistics census data. **Australian disaster events impact dataset:** Records disaster type, location, and severity from 2000–2024. This dataset contains 8,742 disaster events with spatial boundaries (when available) and impact metrics including affected population, economic loss, and infrastructure damage severity scores (0-10). We filtered this dataset to include only flood and bushfire events in NSW, resulting in 342 events for analysis. 

#### **4.2 Data preprocessing** 

To prepare the datasets for our framework, we performed several preprocessing steps: **Spatial integration:** We spatially joined disaster event boundaries with postal zones using GIS operations. For events without precise boundaries, we created impact buffers based on event magnitude and type (flood: 5-20km radius, bushfire: 2-15km radius). 

**Damage severity calculation:** For each postal zone, we computed a composite damage severity score by 

#### combining: 

Direct impact score from disaster records (0-10 scale) Proximity-weighted impact for nearby events Historical frequency of disasters in the zone **Accessibility index:** We developed an accessibility metric for each postal zone, incorporating: Road network density (from OpenStreetMap) Distance to major highways and distribution centers Elevation and terrain ruggedness (from SRTM elevation data) 

Historical disruption data (road closures during past disasters) 

**Demand calibration:** We calibrated our fuzzy demand estimation model using historical relief distribution data from the 2019-2020 NSW bushfires and 2021-2022 NSW floods, adjusting membership functions to minimize prediction error. 

#### **4.3 Scenarios** 

Experiments focus on flood and bushfire events in New South Wales. Scenarios simulate: 

Demand for relief units (water, food, medical supplies) Capacity constraints at distribution hubs Travel disruptions (road closures, increased travel times) Uncertainty levels (low, medium, high) in damage assessment 

We designed five scenarios to test our framework under different conditions (Table 1). The uncertainty levels were implemented by varying the precision of input parameters: **Low uncertainty:** Damage assessments with ±5% error, accessibility with ±2% error 

**Medium uncertainty:** Damage assessments with ±15% error, accessibility with ±8% error 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **7** 

**Research article                                                                                                                                                                                Engineered Science** 

**<u>Table 1:</u>** <u>Experimental scenarios.</u> 

|Scenario|Type|Unc.|Zones|Days|
|---|---|---|---|---|
|NSW-FL-L|Flood|Low|150|7|
|NSW-FL-H|Flood|High|150|7|
|NSW-BF-M|Bushfire|Medium|200|10|
|NSW-BF-H|Bushfire|High|200|10|
|NSW-CMP|Flood+BF|High|250|14|



**<u>Table 2:</u>** <u>Model and algorithm parameters.</u> 

|Parameter|Symbol|Value|
|---|---|---|
|Hub fixed cost|fj|$5k–$15k|
|Hub capacity|Cj|500–2000 units|
|Transport cost|cjk|$0.5–$2/unit/km|
|Unmet demand penalty|α|$100/unit|
|Min. service level|β|0.7|
|GA population size|N|50|
|Crossover prob.|pc|0.8|
|Mutation prob.|pm|0.1|
|Max. generations|Gmax|100|



**High uncertainty:** Damage assessments with ±30% error, accessibility with ±20% error 

The compound scenario (NSW-Compound) simulates a cascading disaster where a bushfire event is followed by flooding in the same region, creating complex demand patterns and infrastructure disruptions. 

#### **4.4 Parameter settings** 

For the optimization model and matheuristic algorithm, we used the following parameter values: 

The parameter values (Table 2) were determined through preliminary experiments and consultation with emergency management experts. The fixed costs and capacities for hubs reflect three tiers of distribution facilities: temporary depots ($5,000, 500 units), regional centers ($10,000, 1,000 units), and main distribution hubs ($15,000, 2,000 units). 

#### **4.5 Performance metrics** 

To evaluate the effectiveness of our fuzzy-matheuristic framework, we measured the following performance 

#### indicators: 

**Total cost:** Sum of fixed costs, transportation costs, and penalties for unmet demand 

**Coverage rate:** Percentage of total demand satisfied across all postal zones 

**Service equity:** Measured by the Gini coefficient of demand satisfaction across zones (lower values indicate more equitable distribution) 

**Computational time:** Time required to reach a solution (in seconds) 

**Solution quality gap:** Percentage difference from the best-known solution (for small instances where exact solutions are available) 

We compared our framework against two baseline approaches: 

**Deterministic IP model:** Uses expected demand values (defuzzified without uncertainty modeling) and solves the optimization problem exactly using commercial solvers. 

**Greedy heuristic:** Allocates resources iteratively based 

**8** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

**Research article                                                                                                                                                                                Engineered Science** 

on a priority score combining demand density and accessibility, without optimization. 

All experiments were conducted on a server with Intel Xeon Gold 6248R processors (3.0 GHz) and 128 GB RAM, running Ubuntu 20.04. The optimization models were implemented in Python 3.8 using OR-Tools and scikitfuzzy libraries. 

#### **5. Results and discussion** 

The fuzzy matheuristic framework is compared against: Baseline deterministic IP model 

Greedy heuristic allocation 

#### **5.1 Rationale for baseline selection** 

The selection of these two baseline methods is strategically designed to evaluate the fuzzy-matheuristic framework across complementary dimensions of optimization performance. Each baseline represents a distinct approach to disaster response planning, enabling a comprehensive assessment of our framework’s advantages. 

#### **5.1.1 Baseline deterministic IP model** 

The deterministic Integer Programming (IP) model serves as the theoretical benchmark for optimization quality. This approach solves the exact same mathematical formulation as our framework but with crisp, deterministic inputs rather than fuzzy uncertainty modeling. **Key Characteristics:** 

**Mathematical rigor:** Uses commercial solvers (CPLEX/Gurobi) to find provably optimal solutions to the mixed-integer programming formulation **Deterministic inputs:** Treats demand estimates as exact values rather than uncertain ranges 

**Complete optimization:** Simultaneously optimizes hub activation and resource allocation decisions **Computational intensity:** May require significant time for large-scale instances due to NP-hard complexity **Rationale for inclusion:** 

**Optimality benchmark:** Provides the best possible solution under deterministic assumptions, establishing an upper bound on solution quality 

**Uncertainty isolation:** By using identical demand estimates but without fuzzy uncertainty modeling, it quantifies the specific value added by the fuzzy component 

**Computational comparison:** Demonstrates whether the matheuristic approach can match or exceed exact methods in efficiency 

**Sensitivity test:** Reveals how deterministic models perform when real-world uncertainty exists, highlighting their brittleness. 

#### **5.1.2 Greedy heuristic allocation** 

The greedy heuristic represents a simple, rule-based approach commonly used in practice due to its simplicity and speed. It makes locally optimal decisions at each step without considering global optimality or uncertainty. **Key characteristics:** 

**Rule-based decision making:** Uses simple heuristics such as “serve highest demand zones first” or nearest hub allocation” 

**Sequential processing:** Makes decisions incrementally without backtracking or global optimization 

**Computational efficiency:** Produces solutions very quickly, even for large instances **Simplicity:** Easy to implement and understand, requiring minimal computational resources **Rationale for inclusion:** 

**Practical benchmark:** Represents approaches commonly used in emergency management due to their simplicity and speed 

**Computational contrast:** Highlights the trade-off between solution quality and computational efficiency **Optimality gap:** Demonstrates how much improvement is possible through more sophisticated optimization 

**Real-world relevance:** Many organizations use simple heuristics due to time constraints during disasters 

#### **5.2 Overall performance comparison** 

Table 3 presents the aggregate performance across all experimental scenarios. The fuzzy-matheuristic approach demonstrates superior performance across all metrics, achieving the lowest total cost, highest coverage rate, and minimal unmet demand while maintaining computational efficiency. 

Results show that the proposed hybrid: Reduces unmet demand by 18–27% compared to baseline 

methods 

Achieves 15% lower total cost under high-uncertainty scenarios 

Maintains computational efficiency (under 70 seconds). 

#### **5.3 Scenario-specific analysis** 

Table 4 provides detailed results for each experimental scenario. The fuzzy-matheuristic framework consistently outperforms alternatives across all scenarios, with particularly significant advantages in high-uncertainty situations. 

The compound disaster scenario (NSW-Compound) demonstrates the framework’s ability to handle complex, multi-event situations. Despite the increased complexity, the fuzzy-matheuristic approach maintained high coverage rates (94.9%) while reducing costs by 16.3% compared to the deterministic IP model. 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **9** 

**Research article                                                                                                                                                                                Engineered Science** 

**<u>Table 3:</u>** <u>Performance comparison (average across scenarios).</u> 

|Method|Cost|Unmet (%)|Cover. (%)|Time(s)|
|---|---|---|---|---|
|DeterministicIP|142,300|23.5|76.5|89|
|Greedy Heuristic|138,750|31.2|68.8|12|
|Fuzzy-MH|118,420|6.8|93.2|67|



**<u>Table 4:</u>** <u>Scenario-specific performance results.</u> 

|Scenario||Total Cost ($)<br>|<br>|Cove<br>|rage(%)<br>|
|---|---|---|---|---|---|
||Det.IP|Greedy|Fuzzy-Mat.|Det.IP|Fuzzy-Mat.|
|NSW-Flood-Low|125,400|121,800|108,200|82.3|95.7|
|NSW-Flood-High|148,700|143,200|121,500|71.2|91.4|
|NSW-Bushfire-Med|132,500|129,300|110,800|78.6|94.2|
|NSW-Bushfire-High|156,800|151,400|127,300|69.5|89.8|
|NSW-Compound|148,600|148,050|124,300|81.0|94.9|





**Fig. 5:** Service equity comparison (Gini coefficient). 

#### **5.4 Service equity analysis** 

Beyond cost and coverage, we evaluated service equity using the Gini coefficient of demand satisfaction across postal zones (lower values indicate more equitable distribution). Fig. 5 shows that the fuzzy-matheuristic framework achieves superior equity across all scenarios. 

The fuzzy-matheuristic approach achieved an average Gini coefficient of 0.18, compared to 0.31 for the deterministic IP and 0.42 for the greedy heuristic. This indicates that our framework not only improves overall performance but also ensures more equitable distribution of 

relief resources across postal zones. 

#### **5.5 Component contribution analysis** 

To understand the contribution of each component in our hybrid framework, we conducted ablation studies by disabling individual components: 

Results in Table 5 demonstrate that both components contribute significantly to performance. Removing fuzzy logic increased costs by 13.7% and reduced coverage by 10.8 percentage points, while removing the matheuristic component (using standard IP) increased costs by 20.1% 

**10** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

**Research article                                                                                                                                                                                Engineered Science** 

**<u>Table 5:</u>** <u>Component contribution analysis.</u> 

|Frameworkvariant|Total cost|Coverage(%)|Time (s)|
|---|---|---|---|
|Full Fuzzy-Matheuristic|118,420|93.2|67|
|Without Fuzzy Logic|134,600|82.4|65|
|Without Matheuristic (IP only)|142,300|76.5|89|
|Without Both (Greedy)|138,750|68.8|12|





**Fig. 6:** Sensitivity to penalty coefficient for unmet demand. 

and reduced coverage by 16.7 percentage points. 

#### **5.6 Sensitivity analysis** 

We conducted sensitivity analysis to evaluate the robustness of our framework to variations in key parameters: 

**Fuzzy membership functions:** We tested variations in membership function shapes (triangular vs. trapezoidal) and parameter ranges. The framework showed consistent performance with less than 5% variation in total cost across different configurations. 

**Cost parameters:** We varied the penalty coefficient for unmet demand ( _α_ ) from $50 to $200 per unit. The framework adapted effectively, maintaining coverage rates above 90% even at the lowest penalty value. **Service level requirements:** We tested minimum service levels ( _β_ ) from 0.5 to 0.9. The framework successfully met all requirements while minimizing costs, demonstrating flexibility in policy implementation. 

Fig. 6 illustrates the framework’s robustness to variations in the penalty coefficient for unmet demand. 

#### **5.7 Computational performance** 

The matheuristic approach demonstrated excellent computational scalability. Fig. 7 shows solution times 

as a function of problem size (number of postal zones). The hybrid approach maintained solution times under 120 seconds even for the largest instances (500+ postal zones), while the deterministic IP became computationally intractable beyond 300 zones. 

**Projected national-level scalability:** While experiments were conducted up to 500+ postal zones, the structural decomposition of the fuzzy-matheuristic framework supports larger-scale deployment. The master problem (hub activation) scales primarily with | _J_ |, while the allocation subproblem scales with | _J_ | × | _K_ |. For full-state deployment in NSW (approximately 2,800 postal zones) or potential national-scale implementation (8,000+ zones), computational performance can be maintained through parallel evaluation of independent IP subproblems within the genetic algorithm. Because each chromosome evaluation is independent, the framework is inherently suitable for distributed or cloud-based parallelization. Preliminary runtime extrapolation suggests that, with multi-core parallel execution, national-scale planning would remain within operational planning timeframes (under 10–15 minutes), which is acceptable for strategic disaster logistics deployment. 

#### **5.8 Practical and managerial implications** 

The findings provide several actionable insights for emergency management agencies and postal logistics 

**Engineered Science Publisher** _Eng. Sci._ , 2026, **41** , 2271 | **11** 

**Research article                                                                                                                                                                                Engineered Science** 



**Fig. 7:** Computational scalability comparison. 

#### Planners. 

**Uncertainty-responsive planning:** Results indicate that deterministic optimization models exhibit significant coverage degradation when uncertainty in damage assessment exceeds approximately 15%. Agencies operating under high-impact disasters should therefore adopt uncertainty-aware planning frameworks, such as fuzzy-based optimization, to avoid systematic underallocation. 

**Equity-oriented resource allocation:** The integration of equity measurement (Gini coefficient) enables policymakers to explicitly incorporate fairness objectives into disaster response planning. Emergency agencies may define acceptable equity thresholds to prevent systematic under-service of remote or vulnerable communities. **Integration with real-time data systems:** The modular design of the framework allows integration with GIS dashboards, satellite-based damage assessment, and IoTenabled road status updates. This enables near real-time re-optimization as new information becomes available during active disaster response. 

**Strategic infrastructure planning:** Postal-address granularity provides a scalable spatial backbone for national disaster planning. Agencies may leverage postal datasets to design pre-positioning strategies and simulate cascading disaster scenarios before events occur. 

#### **5.9 Limitations and future work** 

Despite its strong performance, the framework has several limitations that provide directions for future research: The current model assumes static demand patterns and does not explicitly account for the temporal dynamics of evolving disasters. 

The framework focuses on a single type of relief resource; extending to multiple resource types with 

interdependencies would enhance practical applicability. The fuzzy membership functions and rule bases were calibrated using historical data; adaptive mechanisms for real-time calibration could improve performance in novel disaster scenarios. 

Sensitivity analysis confirms robustness to variations in fuzzy membership functions and cost parameters, suggesting that the framework can be reliably deployed across a range of disaster scenarios and policy contexts. 

#### **6. Conclusion and future work** 

This study demonstrates the feasibility and effectiveness of combining fuzzy logic and matheuristic optimization for disaster response planning at postal-address granularity. Our framework successfully addresses uncertainty and computational complexity challenges through hybrid modeling, validated using real Australian datasets. Key contributions include methodological innovation in fuzzy-matheuristic integration, practical application of postal geography for disaster planning, empirical validation showing 18-27% reduction in unmet demand and 15% lower costs under high uncertainty, and a decision support tool balancing efficiency, equity, and robustness. The findings demonstrate the potential of hybrid approaches for complex optimization under uncertainty and provide a new spatial paradigm for disaster logistics. Practically, the framework enables improved resource allocation decisions and near real-time decision support for emergency management. 

Future work will explore dynamic reallocation strategies, machine learning integration for adaptive fuzzy tuning, multi-modal transportation networks, IoT data integration, multi-resource coordination, cross-border response, and climate change adaptation. This research bridges theoretical optimization and practical disaster 

**12** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

**Research article                                                                                                                                                                                Engineered Science** 

response, providing a foundation for more resilient emergency management systems to address evolving challenges in the 21<sup>st</sup> century. 

#### **Conflict of Interest** 

The authors declare that they have no competing interests. 

#### **Supporting Information** 

Not applicable. 

#### **CRediT Statement** 

**Kassem Danach** , **Wael Hosny Fouad Aly** , and **Mohamad Msheik:** Contributed equally to this work. All authors participated in the study conception and design. **Kassem Danach:** Led the methodology development and experimental implementation. **Wael Hosny Fouad Aly:** Contributed to data analysis and validation of the results. **Mohamad Msheik:** Contributed to theoretical analysis helped in the interpretation of the findings. All authors contributed to drafting and revising the manuscript and approved the final version. 

#### **References** 

[1] N. Altay, W. G. Green. Or/ms research in disaster operations management, _European Journal of Operational Research_ , 2006, **175** , 475–493, doi: 10.1016/j.ejor.2005.05.016. 

[2] E. Grass, K. Fischer. Two-stage stochastic programming in disaster management: A survey, _Surveys in Operations Research and Management Science_ , 2014, **36** , 935–965, doi: 10.1016/j.sorms.2016.11.002. [3] C. Kahraman, B. Oztaysi, I. U. Sari, E. Turanoglu. Fuzzy analytic hierarchy process with interval type-2 fuzzy sets, _Knowledge-Based Systems_ , 2021, **214** , 106748, doi: 10.1016/j.knosys.2014.02.001. 

[4] Kassem Danach, Wael Hosny Fouad Aly, Abbas Tarhini, Saad Laouadi, Toward transparent optimization: A systematic review of explainable ai in decision-making systems, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6707–6707, doi: 10.29020/nybg.ejpam.v18i4.6707. 

[5] Kassem Danach, Hassan Harb, Alaaeddine Ramadan, Samir Haddad, Enhancing multi-criteria decision- making in blockchain security: a hybrid machine learning and promethee approach, _Engineering Research Express_ , 2025, **7** , 0352c6, doi: 10.1088/2631-8695/ae05eb. 

[6] D. Manerba, R. Mansini, G. Perboli, Matheuristics for the vehicle routing problem and its extensions: A survey, _European Journal of Operational Research_ , 2022, **298** , 789–805, doi: 10.1007/978-0-387-77778-8_7. 

[7] D. Dubois, H. Prade, Possibility theory, probability theory and multiple-valued logics: A clarification, _Annals of Mathematics and Artificial Intelligence_ , 2011, **32** , 35–66, doi: 10.1023/A:1016740830286. 

[8] A. J. Keith, D. K. Ahner, A survey of decision making and optimization under uncertainty, _Annals of Operation Research_ , 2021, **300** , 319–353, doi: 10.1007/s10479-019-03431-8. [9] J. Holgu´ın-Veras, M. Jaller, L. N. Van Wassenhove, N. P´erez, 

T. Wachtendorf, On the unique features of post-disaster humanitarian logistics, _Journal of Operations Management_ , 2012, **30** , 494–506, doi: 10.1016/j.jom.2012.08.003. 

[10] S. M. Chen, Y. C. Chang, Weighted fuzzy rule interpolation based on ga-based weight-learning techniques, _IEEE Transactions on Fuzzy System_ s, 2011, **19** , 729–744, doi: 10.1109/TFUZZ.2011.2142314. 

[11] H. Kanj, W. H. F. Aly, S. Kanj, A Novel Dynamic Approach for Risk Analysis and Simulation Using Multi-Agents Model, _Applied Sciences_ , 2022, **12** , 5062, doi: 10.3390/app12105062. [12] Q. Zhou, H. Pandzic, P. Mancarella, A framework for assessment of climate change impacts on power system resilience, _IEEE Transactions on Power Systems_ , 2021, **36** , 2292–2302. 

[13] H. Kanj, A. Kulaglic, W. H. F. Aly, M. A. Al-Tarawneh, K. Safi, S. Kanj, J. M. Flaus, Agent-based risk analysis model for road transportation of dangerous goods, _Results in Engineering_ , 2025, **25** , 103944, doi: 10.1016/j.rineng.2025.103944 

[14] Kassem Danach, Abbas Rammal, Imad Moukadem, Hassan Harb, Abbass Nasser, Advanced optimization in e-commerce logistics: Combining matheuristics with random forests for hub location efficiency, _IEEE Access_ , 2025, **13** , 1, doi: 10.1109/ACCESS.2025.3550560. 

[15] E. Grass, K. Fischer, A. Rams, Matheuristic approaches for the integrated location-routing problem in disaster relief, _European Journal of Operational Research_ , 2022, **298** , 927–941, doi: 10.1007/s00291-015-0427-0. 

[16] Walter J. Gutjahr, Klaus Fischer, Equity and deprivation costs in humanitarian logistics, _European Journal of Operational Research_ , 2018, **270** , 185–197, doi: 10.1016/j.ejor.2018.03.019. [17] M. A. B. Al-Tarawneh, O. Al-irr, K. S. Al-Maaitah, H. Kanj, W. H. F. Aly, Enhancing Fake News Detection with Word Embedding: A Machine Learning and Deep Learning Approach, _Computers_ , 2024, **13** , 239, doi: 10.3390/computers13090239. 

[18] Rameshwar Dubey, Angappa Gunasekaran, Stephen J. Childe, David J. Bryde, Mihalis Giannakis, Constantin Foropon, Big data analytics and artificial intelligence pathway to operational performance under the effects of disruptive innovations in supply chains, _International Journal of Production Economics_ , 2020, **226** , 107684, doi: 10.1016/j.ijpe.2019.107599. [19] C. Yuan, T. Xiao, C. Geng, Y. Sheng, Digital transformation and division of labor between enterprises: Vertical specialization or vertical integration, _China Industrial Economy_ , 2021, **9** , 137– 155, doi: 10.19581/j.cnki.ciejournal.2021.09.007. 

[20] Danach, Kassem, Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems, _European Journal of Pure and Applied Mathematics_ , 2025, **18** , 6707-6707 doi: 10.29020/nybg.ejpam.v18i4.6707. [21] X. Guo, C. Fan, Y. Chen, Executive cognitive styles and enterprise digital strategic change under environmental dynamism: The mediating role of absorptive capacity in a complex adaptive system, _Systems_ , 2025, **13** , 775, doi: 10.3390/systems13090775. [22] R. Kohli, N. P. Melville, Digital innovation: A review and 

_Eng. Sci._ , 2026, **41** , 2271 | **13** 

**Engineered Science Publisher** 

**Research article                                                                                                                                                                                Engineered Science** 

synthesis, _Information Systems Journal_ , 2019, **29** , 200–223, doi: 10.1111/isj.12101. 

[23] C. Hay, R. Meldrum, W. Forrest, E. Ciaravolo, Stability and change in risk seeking: Investigating the effects of an intervention program, _Youth Violence and Juvenile Justice_ , 2010, **8** , 91-106, doi: 10.1177/1541204009349398. 

your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/. 

©The Author(s) 2026. 

[24] J. Freeman L. Hancock Energy and communication infrastructure for disaster resilience in rural and regional Australia, _Regional Studies_ , 2017 **51** , 933-44, doi: 10.1080/00343404.2016.1146403. 

[25] Li, Lixu, Big data and big disaster: a mechanism of supply chain risk management in global logistics industry, _International Journal of Operations & Production Management_ , 2023, **43** , 274307, doi: 10.1108/IJOPM-04-2022-0266. 

[26] Xia, Jing, High-resolution population distribution prediction considering the spatiotemporal heterogeneity of geolocated behavior, _International Journal of Geographical Information Science_ , 2026, **40** , 1618-1650, doi: 10.1080/13658816.2025.2569746. 

[27] P. Taylor, R. Anderson, J. White, Integrating spatial datasets for predictive disaster impact modeling in Australia, _Natural Hazards Review_ , 2023, **24** , 04022038, doi: 10.5194/nhess-201069-2020. 

[28] G. Martin, H. Clark. Optimization opportunities in australian disaster management: Unexplored potential of spatial datasets, _Journal of Contingencies and Crisis Management_ , 2023, **31** , 78– 92, doi: 10.1111/1468-5973.12487. 

[29] March, Alan, Integrated planning to reduce disaster risks: Australian challenges and prospects, _Built Environment_ , 2016, **42** , 158-173, doi: 10.2148/benv.42.1.158. 

[30] Verhoef, C. Peter, Digital transformation: A multidisciplinary reflection and research agenda, _Journal of Business Research_ , 2021, **122** , 889-901, doi: 10.1016/j.jbusres.2019.09.022. [31] P. C. Verhoef, T. Broekhuizen, Y. Bart, A. Bhattacharya, J. Q. Dong, N. Fabian, M. Haenlein, Digital transformation: A multidisciplinary reflection and research agenda, _Journal of Business Research_ , 2021, **122** , 889–901, doi: 10.1016/j.jbusres.2019.09.022. 

**Publisher's Note:** Engineered Science Publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

#### **Open Access** 

This article is licensed under a Creative Commons Attribution 4.0 International License, which permits the use, sharing, adaptation, distribution and reproduction in any medium or format, as long as appropriate credit to the original author(s) and the source is given by providing a link to the Creative Commons license and changes need to be indicated if there is any. The images or other third-party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and 

**14** | _Eng. Sci._ , 2026, **41** , 2271 **Engineered Science Publisher** 

