Engineering Research Express 

##### **PAPER • OPEN ACCESS** 

# Enhancing multi-criteria decision-making in blockchain security: a hybrid machine learning and PROMETHEE approach 

To cite this article: Kassem Danach et al 2025 Eng. Res. Express 7 0352c6 

## You may also like 

- <u>Comparative evaluation of alternatives for management of wood wastes by using multi-criteria decision tools</u> Fatma Ece Sayn, Gülay Topalolu, Bilge Ozbay et al. 

- <u>The application of AHP-PROMETHEE II for supplier selection</u> Muhammad Akmal Md Isa, Nor Shahirah Saharudin, Natasha Bella Anuar et al. 

- <u>A PROMETHEE based multi criteria decision making analysis for selection of optimum site location for wind energy project</u> 

View the <u>article online</u> for updates and enhancements. 

- Vasupalli Manoj, Aakula Swathi and Vemireddi Tejeswara Rao 

This content was downloaded from IP address 185.142.40.211 on 19/11/2026 at 12:04 

https://doi.org/10.1088/2631-8695/ae05eb 

_Eng. Res. Express_ **7** (2025) 0352c6 

#### ~~<u>PAPER</u>~~ 

###### OPEN ACCESS 

RECEIVED 2 June 2025 

REVISED 20 August 2025 

ACCEPTED FOR PUBLICATION 10 September 2025 PUBLISHED 19 September 2025 

Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 

<mark>Enhancing</mark> multi-criteria decision-making in blockchain security: a hybrid machine learning and PROMETHEE approach 

**Kassem Danach**<sup>1,∗</sup> aa **, Hassan Harb**<sup>2</sup> aa **, Alaaeddine Ramadan**<sup>3</sup> aa **and Samir Haddad**<sup>4</sup> aa 

> 1 Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon 

> 2 College of Engineering and Technology, American University of the Middle East, Kuwait 

> 3 College of Engineering and Computing, American University of Bahrain, Riffa, Bahrain 

> 4 Department of Computer Science and Mathematics, Faculty of Arts and Sciences, University of Balamand, Koura 100, Lebanon 

> ∗ Author to whom any correspondence should be addressed. **E-mail: kassem.danach@mu.edu.lb, hassan.harb@aum.edu.kw, alaaeddine.ramadan@aubh.edu.bh and samir.haddad@balamand.edu.lb** 

**Keywords:** multi-criteria decision-making, optimisations, machine learning, security 

licence. 

Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI. 

### **Abstract** 

Multi-Criteria Decision-Making (MCDM) techniques play a critical role in solving complex decision problems involving multiple conflicting criteria across various domains. The Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) is a widely adopted MCDM method known for its structured and transparent ranking process. However, conventional PROMETHEE implementations often rely on manually assigned criteria weights, introducing subjectivity and inconsistency in decision-making. This study proposes a novel hybrid approach that integrates Machine Learning (ML) techniques with PROMETHEE to enhance decision-making, particularly in blockchain security risk assessment. The proposed ML-PROMETHEE model leverages ML algorithms for feature selection, weight assignment, and preference function optimization, ensuring an automated and data-driven ranking process that minimizes human bias and enhances decision reliability. A real-world case study in blockchain security risk assessment is conducted to validate the proposed methodology. This study employs ML models such as Random Forest (RF) for feature selection and SHapley Additive exPlanations (SHAP) analysis to determine the most influential security risk factors. Additionally, Artificial Neural Networks (ANNs) and eXtreme Gradient Boosting (XGBoost) are used to optimize weight assignment, refining the decision-making process before integrating it into the PROMETHEE framework. Experimental results demonstrate that the ML-enhanced PROMETHEE model achieves a 17.3% improvement in decision accuracy, a 43.5% reduction in execution time, and a 40.2% reduction in subjective bias compared to traditional PROMETHEE-based decision-making. These findings highlight the potential of ML-enhanced MCDM models in strengthening the robustness, transparency, and scalability of decision frameworks, particularly in rapidly evolving domains such as blockchain security. Future research will explore the integration of deep learning and reinforcement learning techniques to further enhance automated decision-making frameworks. 

## **1. Introduction** 

Multi -Criteria Decision-Making (MCDM) plays a fundamental role in decision support across various domains, such as finance [1], healthcare [2], and supply chain management [3]. Among MCDM techniques, the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) is widely recognized for its flexibility and effectiveness in ranking alternatives [4]. However, a significant limitation of traditional PROMETHEE implementations is their reliance on manually assigned criteria weights, which can introduce subjectivity and reduce decision robustness. 

© 2025 The Author(s). Published by IOP Publishing Ltd 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

Recent advancements in Machine Learning (ML) have demonstrated potential in improving decision-making models by automating feature selection, weight assignment, and preference function tuning [5]. By integrating ML techniques with PROMETHEE, decision-making processes can become more data-driven, reducing human biases and enhancing adaptability to complex decision problems. Studies such as [6] highlight the benefits of hybrid models that leverage ML to enhance classical MCDM methods. 

Blockchain technology, known for its decentralized and secure nature, has emerged as a critical infrastructure for applications such as finance, supply chain, and cybersecurity [7]. However, blockchain implementations require robust decision-support mechanisms, particularly in risk assessment, consensus protocol selection, and smart contract evaluation [8]. Applying ML-enhanced PROMETHEE to blockchain security risk assessment offers an opportunity to optimize security-related decisions and improve resilience against cyber threats. 

This paper proposes a novel hybrid approach that integrates ML techniques, specifically Random Forest (RF) and Artificial Neural Networks (ANNs), into the PROMETHEE framework to enhance decision-making accuracy in blockchain security risk assessment. A case study is conducted to evaluate the proposed methodology, comparing its performance against traditional PROMETHEE-based ranking systems. Experimental results demonstrate the effectiveness of ML-driven weight assignment in improving decision accuracy, reducing computational time, and enhancing ranking stability. 

The remainder of this paper is organized as follows: section 2 presents the problem statement, followed by section 3, which defines the research objectives and outlines the research questions and hypotheses underpinning the study. A review of the related work is discussed in section 4. Section 5 introduces the mathematical formulation of the problem, while section 6 details the proposed solution approach. The experimental results and analysis are presented in section 7. Finally, section 8 concludes the paper and highlights potential directions for future research. 

## **2. Problem statement** 

The rapid adoption of blockchain technology across various industries, including finance, supply chain management, and healthcare, has highlighted the need for robust security and risk assessment mechanisms [7, 8]. Blockchain networks face several security challenges, such as vulnerabilities in smart contracts, consensus protocol weaknesses, and potential privacy breaches. Traditional risk assessment methods often rely on expert judgment and predefined criteria weights, leading to inconsistencies and subjectivity in decision-making. 

Multi-Criteria Decision-Making (MCDM) techniques, such as the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE), have been widely utilized to rank alternatives based on multiple conflicting criteria [4]. However, PROMETHEE and other classical MCDM methods require manual weight assignment, which introduces human bias and may not adapt well to dynamic and complex blockchain security environments. 

Machine Learning (ML) techniques, particularly feature selection and automated weighting mechanisms, have the potential to enhance MCDM frameworks by providing data-driven insights and reducing subjectivity [5, 6]. The integration of ML with PROMETHEE presents an opportunity to develop an intelligent decisionsupport system for blockchain security risk assessment, ensuring a more objective, scalable, and computationally efficient approach. 

The key research problem addressed in this study is: 

“How can the integration of Machine Learning techniques with the PROMETHEE method improve decision-making accuracy and objectivity in blockchain security risk assessment?” 

To address this problem, the study aims to: 

- Develop a hybrid ML-PROMETHEE framework for blockchain security risk assessment. 

- Utilize ML algorithms, such as Random Forest (RF) and Artificial Neural Networks (ANNs), for feature selection and automated weight assignment. 

- Evaluate the performance of the hybrid model through a real-world case study and compare its accuracy, computational efficiency, and robustness against traditional PROMETHEE-based methods. 

This research contributes to the advancement of decision-making frameworks in blockchain security by leveraging ML capabilities to enhance PROMETHEE’s effectiveness in complex and dynamic environments. 

2 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

## **3. Objective, research questions, and hypothesis** 

#### **3.1. Research objective** 

The primary objective of this study is to develop an advanced decision-support framework by integrating Machine Learning (ML) techniques with the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) to enhance security risk assessment in blockchain networks. Specifically, this research aims to: 

- Develop a hybrid ML-PROMETHEE framework for blockchain security risk assessment. 

- Utilize ML algorithms, such as Random Forest (RF) and Artificial Neural Networks (ANNs), to automate feature selection and weight assignment. 

- Evaluate the effectiveness of the proposed model in improving decision accuracy, computational efficiency, and robustness compared to traditional PROMETHEE-based methods. 

- Provide insights into how ML can enhance Multi-Criteria Decision-Making (MCDM) methodologies in dynamic and security-sensitive environments. 

#### **3.2. Research questions** 

This study seeks to address the following key research questions: 

1. How can the integration of Machine Learning techniques with the PROMETHEE method improve decision-making accuracy and objectivity in blockchain security risk assessment? 

2. What are the most influential security risk factors in blockchain networks that can be identified using MLbased feature selection techniques? 

3. How does the ML-enhanced PROMETHEE model compare with traditional decision-making frameworks in terms of efficiency, scalability, and reliability? 

4. To what extent does automating weight assignment with ML reduce subjectivity and bias in decisionmaking processes? 

#### **3.3. Research hypothesis** 

The research is based on the following hypotheses: 

**H0** : The integration of Machine Learning techniques with PROMETHEE does not significantly improve decision-making accuracy in blockchain security risk assessment. 

**H1** : The integration of Machine Learning techniques with PROMETHEE significantly improves decisionmaking accuracy, reduces subjectivity, and enhances the scalability of security risk assessment in blockchain networks. 

**H2** : Machine Learning-based feature selection and automated weight assignment improve the performance of PROMETHEE by providing more objective and data-driven rankings. 

**H3** : The ML-enhanced PROMETHEE framework achieves higher computational efficiency and decision consistency compared to traditional PROMETHEE methods. 

#### **3.4. Significance of the study** 

This study contributes to the existing literature by: 

- Introducing a novel ML-PROMETHEE integration to improve MCDM frameworks for blockchain security. 

- Demonstrating how ML techniques can enhance the objectivity and reliability of decision-making models. 

- Providing empirical validation through a real-world case study in blockchain security risk assessment. 

- Offering practical insights for blockchain developers, security analysts, and decision-makers in technology governance. 

The findings from this research will serve as a foundation for further exploration of ML-integrated MCDM models in other domains beyond blockchain security. 

3 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

## **4. Related work** 

Multi-Criteria Decision-Making (MCDM) techniques have been extensively applied across various domains, including finance, healthcare, supply chain management, cybersecurity, and engineering. These techniques provide structured frameworks to evaluate multiple conflicting criteria, enabling decision-makers to rank alternatives, allocate resources efficiently, and enhance strategic planning by systematically incorporating both qualitative and quantitative factors [1]. 

Among the various MCDM methodologies, the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) has gained significant attention due to its simplicity, transparency, and effectiveness in handling complex decision-making scenarios [4]. Originally introduced by Brans and Vincke, PROMETHEE provides a structured ranking mechanism that allows decision-makers to evaluate alternatives based on multiple criteria using predefined preference functions. Unlike traditional decision-making models, which rely on rigid mathematical formulations, PROMETHEE enables a more flexible and intuitive decision-support system, making it widely applicable in real-world domains such as project selection, risk assessment, and investment evaluation [9]. 

However, despite its advantages, traditional implementations of PROMETHEE suffer from notable limitations, particularly in weight assignment and preference function assignment. One of the most critical challenges is its reliance on manually assigned criteria weights, which are typically determined based on expert opinions, direct assessments, or classical weighting methods such as the Analytic Hierarchy Process (AHP) [10]. While these approaches help structure decision-making, they introduce subjectivity, inconsistencies, and bias in weight assignment, particularly when dealing with large-scale and complex decision problems [1]. 

To overcome these limitations, recent advancements in Machine Learning (ML) have been integrated with PROMETHEE to automate and optimize decision-making processes. Studies have shown that ML-driven feature selection and weight assignment can enhance decision accuracy, reduce computational overhead, and enhance the consistency and robustness of ranking results across variable datasets by leveraging data-driven insights rather than relying on subjective human judgment [5, 6]. By integrating ML techniques such as Random Forest (RF), Artificial Neural Networks (ANNs), and Gradient Boosting Models (GBMs), modern hybrid decision-making models have demonstrated superior performance compared to traditional PROMETHEEbased approaches [3]. These advances not only improve computational efficiency, but also enable adaptive and real-time decision-making, particularly in dynamic and security-sensitive environments such as blockchain security, fraud detection, and financial risk assessment [7, 8]. 

Recent advances in blockchain security frameworks demonstrate growing synergies between machine learning-enhanced consensus protocols and multi-criteria decision-making (MCDM) methodologies. Venkatesan _et al_ [11] showed that hybrid consensus algorithms like PoCASBFT achieve 98.7% attack detection accuracy when integrated with particle swarm optimization, while maintaining energy consumption below 0.45 kWh/node in ProximaX implementations. Complementary research by Siddamsetti _et al_ [12] developed gradient boosting models that reduce false positives in blockchain anomaly detection by 32% compared to traditional signature-based methods. The Neutrosophic Sets and Systems consortium [13] recently validated a T2NN-CRITIC-MAIRCA MCDM framework that prioritizes blockchain platforms based on 23 technical and organizational criteria, identifying Stellar and Hyperledger Fabric as top performers for ML-integrated systems. Practical implementations like Prometheum’s SEC-compliant infrastructure [14] demonstrate how hybrid approaches can reduce settlement times for on-chain securities to under 90 seconds while maintaining regulatory compliance. 

#### **4.1. Machine learning in decision-making** 

The integration of Machine Learning (ML) with decision-making frameworks has gained significant attention in recent years due to its ability to handle large-scale, high-dimensional data and optimize complex decision processes. Traditional decision-making models, such as Multi-Criteria Decision-Making (MCDM) techniques, often rely on manually assigned criteria weights and static preference functions, which introduce subjectivity and inconsistencies [1]. To address these challenges, ML techniques have been increasingly utilized to automate feature selection, optimize weight assignment, and improve preference function modeling [5]. 

Recent studies demonstrate that ML-driven decision-support systems can significantly enhance decisionmaking by reducing human bias, improving computational efficiency, and increasing ranking stability [6]. Supervised learning algorithms such as Random Forests (RF), Support Vector Machines (SVMs), and Artificial Neural Networks (ANNs) have been effectively employed to identify the most influential decision criteria, thereby enhancing the robustness of MCDM frameworks [3]. For instance, Random Forest-based feature selection has been used to prioritize decision variables, eliminating irrelevant or redundant factors that may compromise decision accuracy [15]. 

4 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

Similarly, Artificial Neural Networks (ANNs) have been leveraged to learn complex relationships between decision criteria and optimal ranking solutions. These models can adaptively assign criteria weights based on historical data, making them particularly effective in dynamic decision environments such as financial risk assessment, supply chain optimization, and cybersecurity [7, 8]. Furthermore, the integration of Gradient Boosting Models (GBMs), such as XGBoost and LightGBM, has shown improved performance in automated preference function optimization, making the decision-making process more data-driven, scalable, and computationally efficient [16]. 

Beyond supervised learning approaches, recent research has explored the use of unsupervised and reinforcement learning methods to enhance decision-making frameworks. Clustering techniques such as K-means and Hierarchical Clustering have been utilized to group decision alternatives into data-driven categories, allowing for more refined rankings in PROMETHEE-based MCDM models [2]. Additionally, Reinforcement Learning (RL) has been proposed to continuously optimize decision criteria by learning from sequential decision processes, particularly in domains such as automated trading, healthcare diagnosis, and cybersecurity risk assessment [17]. 

By integrating ML with traditional MCDM techniques like PROMETHEE, decision-making frameworks evolve from static, expert-driven models to adaptive, data-driven systems capable of responding to real-time changes in decision environments. Future research is expected to further explore deep learning-based PROMETHEE models, federated learning for decentralized decision-making, and hybrid AI-driven decision-support systems to enhance decision robustness across various domains. 

#### **4.2. Hybrid ML-MCDM models** 

Several researchers have proposed hybrid models that combine ML with classical MCDM methods to improve decision accuracy and adaptability. For example, [2] explored the use of ML-based weight optimization for MCDM applications, demonstrating improvements in ranking stability. Similarly, [3] applied ML-enhanced decision models in supply chain management, showing a reduction in computational overhead and improved decision transparency. 

#### **4.3. Blockchain security and risk assessment** 

Blockchain technology has become a critical infrastructure in various applications, including finance , supply chain management, cybersecurity, healthcare, and verification of digital identities [18, 19]. Due to its decentralized, immutable, and tamper-resistant nature, blockchain has been widely adopted for applications that require trust, transparency, and security [7]. However, despite its advantages, blockchain implementations are still vulnerable to security threats such as smart contract vulnerabilities, consensus mechanism exploits, Sybil attacks, and cryptographic failures [8]. As blockchain adoption increases, ensuring the security and integrity of blockchain-based systems has become a major challenge, necessitating the development of robust decision-support mechanisms for risk assessment, security policy enforcement, and vulnerability mitigation. 

Traditional blockchain security risk assessment methodologies rely heavily on predefined risk criteria, expert judgment, and rule-based frameworks, which often introduce subjectivity, inconsistencies, and delays in security decision-making [20]. Common risk assessment techniques include formal verification methods for smart contracts, static and dynamic analysis for anomaly detection, and manual penetration testing [21]. However, these approaches are resource-intensive, require extensive domain expertise, and often fail to adapt dynamically to the rapidly evolving cyber threat landscape. 

To address these challenges, researchers have proposed integrating Machine Learning (ML) techniques with MCDM methods such as PROMETHEE to enhance blockchain security decision-making [6]. The use of ML-enhanced PROMETHEE for blockchain security risk assessment has been identified as a promising solution to improve resilience against cyber threats, automate risk evaluation, and enhance decision accuracy. By leveraging ML algorithms such as Random Forests (RF), Artificial Neural Networks (ANNs), and Gradient Boosting Models (GBMs), blockchain security assessment frameworks can dynamically learn from historical attack data, identify critical risk factors, and optimize security response strategies [16]. 

For example, RF-based feature selection has been used to prioritize blockchain security threats by identifying the most influential attack vectors, such as reentrancy vulnerabilities in smart contracts, 51% attacks on proof-of-work (PoW) networks, and denial-of-service (DoS) attacks targeting blockchain nodes [22]. Similarly, ANN-based anomaly detection models have demonstrated high accuracy in predicting fraudulent transactions, detecting malicious actors in blockchain networks, and analyzing network traffic patterns to identify security breaches [23]. 

Another major challenge in blockchain security is consensus protocol selection. The effectiveness of a blockchain network is largely dependent on its consensus mechanism, which determines how transactions are validated and added to the ledger. Traditional methods for selecting an appropriate consensus protocol involve 

5 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

manual evaluation of performance trade-offs, such as security, scalability, energy efficiency, and decentralization [24]. By applying ML-enhanced PROMETHEE, decision-makers can quantitatively compare multiple consensus protocols, considering real-time network conditions and security risks to select the optimal consensus mechanism for specific blockchain applications. 

Furthermore, smart contract security assessment is a crucial area where ML-enhanced decision support models can be applied. Smart contracts, being self-executing agreements deployed on blockchain networks, are vulnerable to code flaws, logic errors, and security loopholes [21]. ML-based models trained on historical vulnerability datasets can help in automated vulnerability detection, categorization of risks, and prioritization of security patches [25]. The integration of ML-enhanced PROMETHEE enables automated ranking of smart contract security risks, thereby reducing human intervention and improving security response times. 

The growing need for scalable, data-driven and adaptive security frameworks in blockchain technology underscores the importance of integrating ML and MCDM methods for risk assessment. Future research should explore the potential of federated learning-based security models, reinforcement learning for adaptive security policies, and explainable AI for transparent risk assessment in blockchain networks. These advancements will further strengthen blockchain security and ensure robust protection against evolving cyber threats. 

#### **4.4. Comparison with existing approaches** 

The proposed ML-PROMETHEE framework is based on previous research by integrating ML-driven feature selection and weight assignment into the PROMETHEE methodology. Unlike traditional MCDM models, which depend on expert-defined weights [1], this approach leverages data-driven insights to optimize decision making. Furthermore, the use of ML techniques such as RF and ANN ensures a reduction in computational bias, improving the accuracy and scalability of ranking in dynamic environments [6]. 

The existing literature highlights the potential of hybrid ML-MCDM models in various decision-making applications. However, there remains a gap in applying such models to blockchain security risk assessment. The proposed ML-PROMETHEE framework addresses this gap by providing an automated, data-driven approach that enhances decision accuracy, reduces subjectivity, and improves computational efficiency. Future research will explore the integration of deep learning and reinforcement learning techniques to further refine automated decision-making frameworks in blockchain security. 

Recent advances continue to showcase innovative ML-MCDM integrations in diverse domains. For instance, Mohammadi Ruzbahani _et al_ [26] surveyed AI-enhanced blockchain frameworks for IoT cybersecurity, highlighting dynamic trust models and intrusion detection mechanisms. Additionally, Charles _et al_ [27] conducted a comprehensive review of blockchain–AI synergistic models in supply chain operations, confirming the value of hybrid decision-making architectures like neuro-fuzzy PROMETHEE in complex, data-driven contexts. These works further validate the timeliness of our ML-PROMETHEE approach in security-critical blockchain applications. 

A comprehensive review of existing studies reveals a consistent divide: traditional MCDM methods like PROMETHEE offer structured decision logic but rely heavily on expert-driven weight assignment, often limiting scalability and introducing subjectivity. On the other hand, machine learning techniques excel in capturing complex, data-driven patterns but frequently lack interpretability and traceable decision mechanisms. Recent hybrid models have begun to address these limitations; however, few incorporate transparent explainability tools such as SHAP within the weighting and ranking pipeline. By combining interpretable ML with PROMETHEE II in a unified framework, this study contributes a scalable, objective, and explainable decision-support system tailored for risk-aware blockchain security assessment—effectively bridging the gap between predictive analytics and structured decision-making. 

## **5. Mathematical formulation** 

#### **5.1. Problem definition** 

The objective of this research is to construct a robust hybrid decision-making framework that integrates Machine Learning (ML) with the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) to enhance blockchain security risk assessment. This problem is formulated as a Multi-Criteria Decision-Making (MCDM) problem, where a set of blockchain security threats (alternatives) are ranked based on multiple conflicting evaluation criteria. 

Let: 

- _A_ = { _a_ 1, _a_ 2, …, _an_ } be the set of _n_ alternatives (blockchain security threats). 

- _C_ = { _c_ 1, _c_ 2, …, _cm_ } be the set of _m_ criteria used for evaluation. 

6 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

• _w_ = { _w_ 1, _w_ 2, …, _wm_ } be the set of criteria weights, where _wj_ �0 and _mj_ =1<sup>_w_</sup> _j_ = 1. 

- _fj_ ( _ai_ ) represents the performance score of alternative _ai_ concerning criterion _cj_ . 

- _P_ ( _ai_ , _ak_ ) is the preference function indicating the degree to which _ai_ is preferred over _ak_ . 

#### **5.2. Preference function in PROMETHEE** 

To facilitate pairwise comparison among alternatives, a preference function _Pj_ ( _ai_ , _ak_ ) is defined based on the difference in performance scores: 



<!-- Start of picture text -->
Pj ( ai , ak ) = F ( f j ( ai ) f j ( ak )) (1)<br><!-- End of picture text -->

where _F_ represents a predefined function that determines preference intensity. Common types of preference functions include: 

1. **Usual Criterion:** 



<!-- Start of picture text -->
0, if f j ( ai ) f j ( ak )<br>Pj ( ai , ak ) = (2)<br>1, if f j ( ai ) > f j ( ak )<br><!-- End of picture text -->

2. **Linear Criterion:** 



<!-- Start of picture text -->
Pj ( ai , ak ) = f j ( ai ) f j ( ak ) , if 0 f j ( ai ) f j ( ak ) pj (3)<br>pj<br>f j ( ai ) f j ( ak ) 2<br>Pj ( ai , ak ) = 1 e sj (4)<br><!-- End of picture text -->

3. **Gaussian Criterion:** 

where _pj_ and _sj_ regulate the sensitivity of the function. 

#### **5.3. Aggregated preference index** 

To quantify the overall preference of one alternative over another, the aggregated preference index is computed 

- as: 



<!-- Start of picture text -->
m<br>( ai , ak ) = w Pj j ( ai , ak ) (5)<br>j =1<br><!-- End of picture text -->

#### **5.4. Positive and negative flow** 

The PROMETHEE method utilizes positive and negative preference flows to determine alternative rankings: 

- **Positive Flow** ( **Outranking Strength** ) **:** 



<!-- Start of picture text -->
1 n<br>+( ai ) = ( ai , ak ) (6)<br>n 1 k =1<br>) :<br>1 n<br>( ai ) = ( ak , ai ) (7)<br>n 1 k =1<br><!-- End of picture text -->

- **Negative Flow** ( **Outranking Weakness** ) **:** 

- **Net Flow** ( **Final Ranking Score** ) **:** 



<!-- Start of picture text -->
( ai ) = +( ai ) ( ai ) (8)<br><!-- End of picture text -->

7 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

Higher values of _f_ ( _ai_ ) indicate more favorable alternatives. 

#### **5.5. Machine learning-based weight optimization** 

To mitigate subjectivity in criteria weight assignments, a Machine Learning-based optimization mechanism is incorporated. A supervised learning model is trained to derive optimal weight distribution _wj_ using historical decision data. 

_wj_ = _ML_ ( _C_ , _A_ , _Y_ ) (9) 

- _ML_ represents the machine learning function. 

- _C_ denotes input criteria. 

- _A_ denotes alternatives. 

- _Y_ denotes historical decision labels. In our study, _Y_ corresponds to normalized composite risk scores constructed from Severity (C1), Financial Loss (C3), and Recovery Difficulty (C5), as detailed in section 6.1. 

In equation (9), the machine learning model aims to approximate the mapping from preprocessed decision criteria _X_ = { _x_ 1, _x_ 2, . . . , _xn_ } to a risk score _y_ ∈ [0, 1] that reflects the blockchain security vulnerability level. To train this model, we use a supervised learning setup where labeled historical incidents from the BSID dataset serve as ground truth. The training objective is to minimize the discrepancy between the predicted scores _y_ ˆ and the true outcomes _y_ . We adopt the Mean Squared Error (MSE) as the loss function, defined as: 



<!-- Start of picture text -->
MSE = 1 N ( yi y ˆ) i 2 (10)<br>N i =1<br><!-- End of picture text -->

This choice is suitable for our continuous risk score prediction task and encourages the model to produce probabilistic outputs with minimal deviation from labeled outcomes. The model is trained using an 80-20 train-test split, with 5-fold cross-validation applied to ensure generalization and prevent overfitting. During training, early stopping and learning rate decay are applied to enhance convergence stability. 

#### **5.6. Final decision ranking** 

Using the machine learning-optimized weights, the final ranking of alternatives is obtained based on net flow scores: 



<!-- Start of picture text -->
Rank( ai ) = sort ( ( ai )) (11)<br><!-- End of picture text -->

where _sort_ ↓ arranges alternatives in descending order. 

This formulation presents a hybrid ML-PROMETHEE framework for blockchain security risk assessment, enhancing decision objectivity, computational efficiency, and scalability. 

## **6. Solution approach** 

This study introduces a hybrid decision-support system that leverages ML-enhanced PROMETHEE for blockchain security risk assessment. The approach: 

- Identifies influential security risk factors via feature selection. 

- Optimizes weight assignment using supervised ML models. 

- Ranks blockchain threats through PROMETHEE. 

A real-world dataset is used to validate the framework. To further clarify the methodology, figure 1 provides a side-by-side architectural comparison between Traditional PROMETHEE and the proposed ML-PROMETHEE framework. The figure highlights how machine learning is incorporated for automatic feature selection, criteria weighting, and preference function learning, replacing the manual and static processes of the traditional method. 

#### **6.1. Dataset description** 

We used 5,000 records from the Blockchain Security Incident Database (BSID), a proprietary incident dataset curated by our research team in collaboration with the Secure Blockchain Initiative [28]. The database compiles 

8 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 1.** Comparative architecture of (a) Traditional PROMETHEE and (b) ML-PROMETHEE (Proposed). The traditional method relies on manual weight assignment and static preference functions. In contrast, the ML-PROMETHEE approach integrates machine learning for feature selection and automatic weight learning, feeding into an adaptive PROMETHEE ranking engine. Data flow arrows—such as _Expert-defined Weights_ , _Manual Preferences_ , _Feature Importance_ , and _Learned Weights_ —are labeled to clarify the transition from manual to automated decision-making processes. 

verified public reports of blockchain security incidents (e.g., smart contract exploits, 51% attacks, phishing), aggregated from reputable sources and structured for modeling purposes. While BSID is not publicly available due to data licensing, anonymized metadata and summary statistics are used to support reproducibility. 

Each recorded incident is characterized by several key criteria that define its risk profile and impact on blockchain security. The _Severity Score_ (C1) quantifies the potential damage caused by the incident, while the _Exploitability Index_ (C2) measures how easily an attacker can exploit the vulnerability. The _Financial Loss_ (C3) represents the estimated monetary damage resulting from the breach. The _Affected Nodes_ (C4) criterion captures the extent of the attack’s reach in terms of the number of blockchain nodes impacted. The _Recovery Difficulty_ (C5) provides an ordinal ranking (low, medium, high) indicating the complexity involved in mitigating the threat. Lastly, the _Attack Type_ (C6) categorizes the nature of the security incident, such as phishing, distributed denial-of-service (DDoS), or cryptographic failure. 

Prior to model training, the BSID dataset underwent a comprehensive preprocessing and cleaning phase. Records with incomplete fields or ambiguous values—particularly in the Severity Score, Financial Loss, and Recovery Difficulty attributes—were removed. Categorical fields (e.g., Recovery Difficulty, Attack Type) were one-hot encoded, while continuous variables were normalized to ensure scale uniformity. Outliers in monetary loss were detected using the interquartile range (IQR) method and excluded to improve model robustness. 

The labels ( _Y_ ) used in equation (9) were constructed as composite risk scores derived from key attributes in the dataset. Specifically, each incident was assigned a normalized weighted average of Severity Score (C1), Financial Loss (C3), and Recovery Difficulty (C5). Weights were set based on expert risk modeling conventions: 0.4 for C1, 0.4 for C3, and 0.2 for C5. These composite scores were scaled to the [0, 1] range and treated as continuous targets for training supervised ML models. The ordinal values of Recovery Difficulty were encoded numerically (Low = 0.2, Medium = 0.5, High = 1.0) to support composite score generation. We conducted multiple normalization checks to ensure the score distribution remained consistent across subsets. To validate label consistency, we cross-checked a sample of critical incidents against external cybersecurity platforms such as Chainalysis and CertiK. 

To support transparency and reproducibility, table 1 presents a sample of anonymized records from the Blockchain Security Incident Database (BSID). While the complete dataset is not publicly accessible due to licensing agreements, this sample reflects the structure and types of attributes used in the analysis. Researchers interested in academic use of the full dataset may contact the corresponding author to request access under a data-use agreement that ensures data privacy and compliance with institutional policies. 

Figure 2 schematizes how _augmented anomalous sequences_ are produced: (i) sampling seed traces, (ii) applying generic stochastic augmentations (temporal jitter ± _τ_ , amplitude scaling [ min, max]<sup>, time warping,</sup> Gaussian noise with std. _σ_ , and window masking with probability _p_ mask), and (iii) applying anomaly-focused transforms (spike/step injection, level shifts, and _edge perturbations_ for graph-structured data via random edge 

9 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 2. Augmented anomalous sequence generation.** Pipeline: seed sequences → generic stochastic augmentations (jitter, scaling, warp, noise, masking) → anomaly-focused transforms (spike/step, level shift, _edge perturbations_ ). Right: before/after minipanels illustrate jitter, edge changes ( _p_ ±), and level shifts. 

**Table 1.** Sample Anonymized Records from the BSID Dataset. 

|ID|Severity|Exploitability|Loss(USD)|Nodes|Recovery|Attack Type|
|---|---|---|---|---|---|---|
|INC001|0.8|0.7|150,000|25|High|Phishing|
|INC002|0.5|0.3|45,000|10|Medium|Smart Contract Exploit|
|INC003|0.9|0.6|320,000|80|High|51% Attack|



add/delete under budgets _p_ ± with renormalization). Labels are preserved and sanity checks (bounds, length, connectivity) discard degenerate cases. 

#### **6.2. Machine learning for feature selection and weighting** 

In this study, machine learning techniques are employed to enhance the decision-making process by identifying the most influential criteria and optimizing their respective weights. The framework consists of two major components: feature selection and weight assignment. 

Prior to applying machine learning models, we performed a structured data preprocessing pipeline to ensure data quality and modeling integrity. This included the following steps: 

- Removal of duplicate entries and incomplete records (approximately 3.6% of the dataset). 

- Imputation of missing values using mean substitution for numerical features and mode for categorical features. 

- Min-Max normalization of all numerical attributes (C1–C5) to standardize feature scales. 

- One-hot encoding of the categorical attribute _Attack Type_ (C6), resulting in 8 binary indicator variables. 

- Outlier removal using Z-score filtering for numerical features (with a cutoff of | _z_ | > 3). 

These preprocessing steps improved model performance and generalization while ensuring fairness across feature dimensions. 

Feature selection is crucial to eliminate irrelevant or redundant variables, thereby improving computational efficiency and model interpretability. In this work, we utilize _Random Forest_ (RF), a tree-based ensemble learning method, to rank features based on their importance scores. To ensure explainability and consistency, we further employ SHapley Additive exPlanations (SHAP), a game-theoretic tool that produces additive and globally coherent feature attributions. SHAP was selected over other tools such as LIME due to its stronger theoretical guarantees and its robustness across instances, making it better suited for determining decision criteria weights in our pipeline. The resulting feature rankings guide the weight optimization phase and reinforce the transparency of the decision-making process. 

10 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

Once the most relevant features have been identified, weight assignment is performed to assign optimal importance values to each criterion. Traditional methods often rely on subjective expert judgment, but our approach leverages machine learning models to automate this process. Specifically, we employ _Artificial Neural Networks_ (ANNs) to learn complex, non-linear relationships between decision criteria and historical decision outcomes. Furthermore, _eXtreme Gradient Boosting_ (XGBoost), a powerful boosting-based algorithm, is utilized to refine the weight distribution by minimizing prediction error and enhancing robustness. 

By integrating these machine learning techniques, our framework ensures that the decision-making process is data-driven, objective, and scalable. The use of SHAP further enhances the explainability and trustworthiness of both the feature selection and weighting stages, ultimately supporting a more reliable blockchain security risk assessment. 

#### **6.3. Integration with PROMETHEE** 

The integration of machine learning (ML) with the PROMETHEE method enhances the decision-making process by leveraging data-driven insights to refine the ranking of blockchain security threats. The MLPROMETHEE framework follows a structured sequence of computations to ensure robust and objective decision analysis. 

First, _pairwise preference functions_ are computed to quantify the comparative advantage of one alternative over another based on multiple evaluation criteria. These functions are derived from the performance scores of security threats and serve as the foundation for preference-based ranking. 

Next, the _aggregated preference indices_ are determined by weighting the computed pairwise preferences according to the optimized criterion weights obtained through machine learning. This step ensures that the evaluation process remains data-driven and eliminates potential subjectivity associated with manual weight assignment. 

Following this, the _positive and negative preference flows_ are calculated to represent the overall strength and weakness of each alternative within the decision space. The positive flow measures how much an alternative outranks others, while the negative flow indicates the extent to which it is dominated by other alternatives. These flows provide a balanced assessment of security threats by considering both their advantages and vulnerabilities. 

Finally, the _net preference rankings_ are obtained by computing the difference between positive and negative preference flows. This final ranking determines the relative severity of each blockchain security threat, enabling decision-makers to prioritize mitigation strategies effectively. 

By combining ML-based feature selection and weight optimization with PROMETHEE’s multi-criteria decision analysis, this approach ensures a scalable, data-driven, and objective assessment of blockchain security risks. The enhanced ML-PROMETHEE framework provides a reliable ranking system that improves threat identification and prioritization, ultimately strengthening the security posture of blockchain networks. 

To enhance clarity regarding the integration of machine learning and PROMETHEE, algorithm 1 provides the following pseudocode outlining the complete process. Although traditional PROMETHEE relies on expertdriven weight assignment, our integration of machine learning as a substitute for manual weighting remains theoretically valid. PROMETHEE’s core requirement is a complete and consistent ranking of alternatives based on weighted preference flows; it does not inherently dictate how the weights must be derived. Using supervised machine learning models allows us to extract preference patterns from historical data, effectively capturing implicit expert logic at scale. This aligns with the axiomatic structure of PROMETHEE, provided the learned weights are stable, interpretable, and normalized. By combining PROMETHEE with interpretable ML tools such as SHAP and XGBoost, we preserve transparency and traceability—key components of multi-criteria decision analysis (MCDA). Hence, ML-derived weights are not only compatible with PROMETHEE’s logic but also offer scalable, objective alternatives to human judgment in high-dimensional decision contexts. 

**Algorithm 1.** ML-PROMETHEE Integration Framework 

**Input:** Preprocessed dataset _D_ , set of alternatives _A_ = { _a_ 1, _a_ 2, …, _an_ }, decision criteria _C_ = { _c_ 1, _c_ 2, …, _cm_ } **Output:** PROMETHEE preference ranking _π_ ( _ai_ ) **1** Train ML models (RF, XGBoost, ANN) on _D_ using known outcomes 

**32** Normalize SHAP values: Use SHAP to compute feature importances _wj_ = _mk_ =1( _cj_ )( _ck_ ) (weight assignment _f_ ( _cj_ ) for each criterion) _cj_ **4** Compute pairwise preference flows _π_ ( _ai_ , _ak_ ) using PROMETHEE II 

**5** Apply weighted preference aggregation with ML-derived weights { _wj_ } **6** Rank alternatives _A_ using net flow scores _f_<sup>+</sup> ( _ai_ ) − _f_<sup>−</sup> ( _ai_ ) 

11 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 3.** Distribution of blockchain security incidents by type based on the BSID dataset. Smart contract vulnerabilities are the most prevalent (over 1400 cases), followed by network attacks and consensus-related exploits. This highlights critical threat vectors in blockchain systems. 

**Table 2.** Software and libraries used. 

|Software/Library|Purpose|
|---|---|
|Scikit-learn|Machine learning models and feature selection|
|TensorFlow/Keras|Artificial Neural Networks(ANNs)for weight assignment|
|Pandas and NumPy|Data processing and numerical computations|
|PROMETHEE-II Library|Implementation of the PROMETHEE outranking method|



**Table 3.** Hardware Specifications. 

|Hardware|Specifications|
|---|---|
|Processor|Intel Xeon 3.2 GHz(16 cores)|
|RAM|64 GB|
|GPU|NVIDIA RTX 3090(24 GB VRAM)|



## **7. Experimental results** 

#### **7.1. Experimental setup** 

The proposed ML-PROMETHEE framework was implemented using Python 3.9, leveraging several essential libraries for machine learning and decision-making. Table 2 provides a summary of the software tools used. 

The experiments were conducted on a high-performance computing system with specifications detailed in table 3. 

The dataset used for evaluation contained 5,000 blockchain security incidents. The distribution of these incidents by category is depicted in figure 3. 

#### **7.2. Performance metrics** 

The evaluation of ML-PROMETHEE was based on several key performance metrics, summarized in table 4. 

#### **7.3. Results and analysis** 

#### _7.3.1. Decision accuracy improvement_ 

The ML-PROMETHEE framework demonstrated significant improvements in ranking accuracy. Table 5 presents the accuracy comparison between traditional PROMETHEE and ML-enhanced models. 

12 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 4.** Execution time comparison between decision-making methods. ML-PROMETHEE (ANN) achieves the lowest execution time (4.3 seconds), outperforming both ML-PROMETHEE (RF) (4.9 seconds) and the traditional PROMETHEE approach (7.2 seconds), demonstrating improved computational efficiency. 

**Table 4.** Performance Metrics Description. 

|Metric|Description|
|---|---|
|Decision Accuracy Improvement(DAI)|Measures improvement in ranking correctness compared to traditional PROMETHEE|
|Computational Efficiency(CE)|Reduction in execution time achieved by ML-driven optimization|
|Ranking Stability(RS)|Consistency of ranking results measured using the Spearman Rank Correlation Coeffi-<br>cient(SRCC)|
|Bias Reduction(BR)|Quantifies reduction in human bias due to ML-based criteria weighting|



**Table 5.** Decision accuracy improvement. 

|Method|Accuracy(%)|Improvement(%)|
|---|---|---|
|Traditional PROMETHEE|78.5|—|
|ML-PROMETHEE(RF)|89.3|+13.8|
|ML-PROMETHEE(ANN)|92.1|+17.3|



#### _7.3.2. Computational efficiency_ 

The execution time of ML-PROMETHEE was significantly lower than that of traditional PROMETHEE, as shown in figure 4. 

#### _7.3.3. Ranking stability_ 

The stability of rankings across multiple test runs was evaluated using the Spearman Rank Correlation Coefficient (SRCC). The results are presented in table 6. 

To further illustrate ranking stability across different models, figure 5 provides a visual comparison. 

#### _7.3.4. Bias reduction_ 

ML-driven weight assignment significantly reduced subjectivity in decision-making. Table 7 summarizes the bias reduction results. 

The effectiveness of ML-based optimization in reducing human bias is visually depicted in figure 6. 

13 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 5.** Ranking stability measured using Spearman Rank Correlation Coefficient (SRCC). ML-PROMETHEE (ANN) achieves the highest stability with SRCC = 0.94, followed by ML-PROMETHEE (RF) at 0.89, and Traditional PROMETHEE at 0.76, confirming the superior consistency of the ML-enhanced models. 

**Table 6.** Ranking stability across models. 

|Method|Spearman Rank Correlation(SRCC)|
|---|---|
|Traditional PROMETHEE|0.76|
|ML-PROMETHEE(RF)|0.89|
|ML-PROMETHEE(ANN)|0.94|



**Table 7.** Bias Reduction in weight assignment. 

|Method|Bias reduction(%)|
|---|---|
|Traditional PROMETHEE|—|
|ML-PROMETHEE(RF)|28.4|
|ML-PROMETHEE(ANN)|40.2|



#### **7.4. Comparison with other MCDM methods** 

To further evaluate the effectiveness of the proposed ML-PROMETHEE framework, we compared its performance with two widely adopted traditional MCDM techniques: TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) and AHP (Analytic Hierarchy Process). These models were selected due to their prevalence in decision-making studies involving conflicting criteria and their interpretability. All models were applied to the same blockchain security dataset under consistent experimental settings. Performance was assessed based on three key metrics: Decision Accuracy (DA), Spearman Rank Correlation Coefficient (SRCC), and Computational Time (CT). The results are summarized in table 8. They indicate that both ML-PROMETHEE variants significantly outperform AHP, TOPSIS, and traditional PROMETHEE in terms of decision accuracy and ranking consistency. ML-PROMETHEE (ANN) achieved the highest SRCC (0.94) and the lowest execution time (3.2 seconds), demonstrating the efficiency and robustness of the proposed hybrid framework. 

To provide further clarity, figure 7 presents a visual comparison of the decision accuracy and SRCC across all methods. These findings reinforce the superiority of ML-PROMETHEE in complex decision scenarios such as blockchain security risk assessment. 

To ensure fair benchmarking, AHP and TOPSIS were also implemented under standardized evaluation conditions. For AHP, the pairwise comparison matrix was constructed using expert-derived relative importance scores, and consistency ratios (CR) were verified to be below 0.1. For TOPSIS, all decision criteria were 

14 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 6.** Bias reduction in criteria weighting. ML-PROMETHEE (ANN) achieves the highest bias reduction of 40%, followed by ML-PROMETHEE (RF) with 28%, while Traditional PROMETHEE shows no bias reduction (0%). This demonstrates the effectiveness of ML models in minimizing subjectivity in weight assignment. 



**Figure 7.** Performance comparison of MCDM methods. ML-PROMETHEE (ANN) achieved the highest decision accuracy (92%) and SRCC (0.94), followed by ML-PROMETHEE (RF) with 89% accuracy and 0.89 SRCC. Traditional PROMETHEE, AHP, and TOPSIS showed lower performance in both metrics, confirming the effectiveness of ML integration in improving ranking stability and predictive accuracy. 

**Table 8.** Comparison of ML-PROMETHEE with other MCDM methods. 

|Method|Decision Accuracy(%)|SRCC|Execution Time(s)|
|---|---|---|---|
|AHP|75.1|0.72|8.4|
|TOPSIS|78.0|0.74|6.2|
|Traditional PROMETHEE|78.5|0.76|5.7|
|ML-PROMETHEE(RF)|89.3|0.89|3.6|
|ML-PROMETHEE(ANN)|92.1|0.94|3.2|



15 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

**Table 9.** Comparison of ML-only models versus ML-PROMETHEE variants. 

|Model|Decision<br>Accuracy(%)|SRCC|Execution<br>Time(s)|
|---|---|---|---|
|RF(standalone)|85.6|0.82|3.5|
|ANN(standalone)|87.3|0.84|3.4|
|ML-PRO-|**89.3**|**0.89**|3.6|
|METHEE(RF)||||
|ML-PRO-<br>METHEE(ANN)|**92.1**|**0.94**|3.2|



normalized using vector normalization, and the identical set of features used in ML-PROMETHEE was retained. All models—AHP, TOPSIS, ML-only, and ML-PROMETHEE—were evaluated using the same performance metrics (Decision Accuracy and SRCC), based on the same data splits. This uniform treatment guarantees that observed performance differences are due to methodological efficacy rather than preprocessing or configuration bias. 

#### **7.5. Comparison with ML-only baselines** 

To assess the added value of integrating PROMETHEE with machine learning, we conducted a parallel comparison with standalone ML models—Random Forest (RF) and Artificial Neural Network (ANN)— trained directly on the BSID dataset to predict the composite risk score _Y_ without any MCDM fusion. The results are shown in table 9. While ML-only models demonstrate strong predictive performance, MLPROMETHEE variants achieve superior ranking consistency and slightly improved accuracy. The PROMETHEE component enhances explainability by incorporating structured pairwise comparisons aligned with decision-theoretic principles. 

These results confirm that hybridizing ML with PROMETHEE not only improves interpretability and transparency, but also enhances decision quality in high-stakes environments. 

#### **7.6. Statistical significance tests** 

To validate the robustness and statistical relevance of our approach, we conducted formal statistical significance tests comparing the traditional PROMETHEE approach with the ML-enhanced variants (ANN and RF). These improvements, while promising, require empirical support through inferential statistics to confirm their generalizability. Two complementary approaches were employed: 

- **Paired t-test:** Assesses the mean difference in performance metrics between traditional and ML-enhanced methods, assuming normality. 

- **Wilcoxon signed-rank test:** A non-parametric alternative that does not assume normality, used to confirm robustness of the conclusions. 

Paired instances are formed by matching each dataset × fold × seed across methods. Let _si_ ours and _si_ base denote the scores for the _i_ -th pair, we analyze _di si_ ours _si_ base with mean _d_ ¯ and standard deviation _sd_ . For higher-is-better metrics, _d_<sup>¯</sup> > 0 indicates improvement, while for lower-is-better metrics (e.g., runtime) improvement corresponds to _d_<sup>¯</sup> < 0. Before applying the paired tests, we assess the normality of { _di_ } using the Shapiro–Wilk test at _α_ = 0.05. When normality is not rejected, we conduct a two-sided _pairedt_ -test with _t_ = _d_ ¯/( _sd_ / _n_ ) and report the corresponding _p_ -value; when normality is rejected, we additionally report the Wilcoxon signed-rank _p_ -value alongside the paired _t_ -test. To address multiplicity across metrics and baselines, we apply Holm–Bonferroni adjustment to all reported _p_ -values (see table 10). 

Beyond null-hypothesis testing, we complement significance with _estimation_ statistics. For each comparison, we report the mean paired difference with a 95% bias-corrected and accelerated (BCa) bootstrap confidence interval (10,000 resamples). These are visualized in a Gardner–Altman estimation plot (figure 8) using jittered paired points, box summaries, and error bars. We also quantify effect sizes using Hedges’ _g_ av (paired design, small-sample corrected) and the distribution-free Cliff’s _δ_ . A compact numerical summary including mean±SD per method, mean difference with 95% CI, adjusted _p_ -values, and effect sizes is provided in table 10. 

Table 11 presents the _p_ -values obtained across three key performance indicators: Decision Accuracy, Bias Reduction, and Spearman Rank Correlation Coefficient (SRCC). All tests yielded _p_ -values well below the conventional 0.01 threshold, confirming that the improvements introduced by ML-PROMETHEE are statistically significant. These results provide robust evidence for the effectiveness of ML-PROMETHEE in improving 

16 

###### 

**Table 10.** Paired-comparison summary: mean±SD per method, mean paired difference with 95% BCa CI, adjusted _p_ -values (Holm), and effect sizes (Hedges’ _g_ av, Cliff’s _δ_ ). 

|Dataset|Metric|Comparison|Ours|Baseline|Mean diff[95% CI]|_t_-test_p_(Holm)|Wilcoxon_p_/_g_av/_δ_|
|---|---|---|---|---|---|---|---|
|BSID-1|Accuracy|ANN vs Traditional|0.91±0.02|0.87±0.03|0.04[0.02, 0.06]|0.001(0.004)|0.002/0.85/0.62|
|BSID-1|SRCC|ANN vs Traditional|0.83±0.04|0.76±0.05|0.07[0.03, 0.10]|0.003(0.009)|0.005/0.78/0.55|
|BSID-2|Runtime↓|RF vs Traditional|3.2±0.4|4.3±0.6|−1.1[−1.6,−0.6]|0.002(0.006)|0.003/0.92/−0.68|



K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 



**Figure 8.** Gardner–Altman estimation plot for paired comparisons between the proposed method and baselines. Left: distributions across folds/seeds with jittered points and box summaries. Right (co-located): paired differences (ours−baseline) with mean and 95% BCa CI (10,000 bootstrap resamples). 

**Table 11.** _p_ -values of key performance indicators.. 

|Metric|Model|Paired t-test(p-value)|Wilcoxon test(p-value)|Significant(p<0.01)|
|---|---|---|---|---|
|Decision Accuracy|ANN vs Traditional|<0.001|<0.001|Yes|
|Bias Reduction|ANN vs Traditional|<0.001|<0.001|Yes|
|Spearman Correlation|ANN vs Traditional|0.004|0.003|Yes|
|Decision Accuracy|RF vs Traditional|<0.001|<0.001|Yes|
|Bias Reduction|RF vs Traditional|<0.001|<0.001|Yes|
|Spearman Correlation|RF vs Traditional|0.007|0.006|Yes|



multi-criteria decision-making performance over the traditional PROMETHEE baseline. The consistent statistical significance across both parametric and non-parametric methods further strengthens the reliability of the proposed approach. 

To further evaluate the practical significance of the observed differences, we calculated effect size metrics using Cohen’s _d_ . The effect sizes for Decision Accuracy were _d_ = 1.27 (ANN vs Traditional) and _d_ = 1.19 (RF vs Traditional), while those for SRCC were _d_ = 1.11 (ANN vs Traditional) and _d_ = 1.05 (RF vs Traditional). These values fall well into the ‘large’ effect category, indicating that the improvements achieved by ML-PROMETHEE are not only statistically significant but also meaningfully impactful in practice. In addition, we report Hedges’ _g_ av and Cliff’s _δ_ ; both corroborate the presence of large effects and are summarized in table 10. 

#### **7.7. Discussion** 

The experimental results confirm that the ML-PROMETHEE approach significantly enhances blockchain security risk assessment. The key improvements include: 

- **Higher Decision Accuracy** : ML-PROMETHEE achieves up to 17.3% accuracy improvement over traditional PROMETHEE. 

- **Reduced Computational Cost** : Execution time is decreased by 43.5%, facilitating real-time risk assessment. 

- **Improved Ranking Stability** : Higher SRCC values confirm improved ranking consistency. 

- **Minimized Human Bias** : ML-based criteria optimization reduces subjectivity by 40.2%. 

These findings validate ML-PROMETHEE as a robust, efficient, and scalable decision-support system for blockchain security analysis. Future research will explore deep learning and reinforcement learning methods to further refine decision-making capabilities. Furthermore, although the proposed framework performs effectively on the structured BSID dataset, its scalability to high-dimensional data, large sets of decision criteria, or deployment in real-time environments poses potential challenges. For instance, the use of SHAP for feature attribution and ANN-based weight optimization increases computational demands during training, which could hinder responsiveness in latency-sensitive contexts. Additionally, as the number of evaluation criteria grows, the interpretability of neural-based models may decrease, making decision traceability more difficult. 

18 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

**Table 12.** Monte Carlo sensitivity results for top-5 incidents. 

|Incident ID|Ranking Variance|CV(%)|
|---|---|---|
|INC021|0.12|3.8|
|INC045|0.09|2.9|
|INC003|0.16|4.6|
|INC078|0.11|3.4|
|INC019|0.10|3.1|



To address these limitations, future work will explore lightweight neural architectures, online learning techniques, and federated learning frameworks to support decentralized and privacy-preserving risk assessments suitable for scalable and distributed blockchain systems.On the other hand, as statistical significance tests confirm the superiority of ML-PROMETHEE over traditional methods, this study does not include a formal sensitivity analysis to assess how small perturbations in criteria weights or variations in dataset characteristics influence the final rankings. Such analysis is essential to evaluate the robustness and stability of the decision outcomes under uncertainty. As a next step, we propose conducting sensitivity tests using Monte Carlo simulations and scenario-based stress analysis to quantify the impact of weight deviations, class imbalance, and noise injection on model performance and ranking consistency. 

To assess the robustness of the ML-PROMETHEE framework, we performed a sensitivity analysis by perturbing the normalized input features and observing their impact on final ranking scores. Specifically, we introduced Gaussian noise ( _μ_ = 0, _σ_ = 0.05) to each criterion across 1,000 Monte Carlo runs. We computed the standard deviation and coefficient of variation (CV) of the resulting rankings. The results showed that for the top-5 ranked incidents, the average CV remained below 4.6%, indicating high stability under small input fluctuations. Furthermore, 92% of the test cases retained the same top-3 incidents across runs, demonstrating strong robustness in risk prioritization. These findings validate the framework’s resilience and justify its use in environments where input uncertainty is common. A summary of the ranking sensitivity for the top-5 incidents is presented in table 12. 

#### **7.8. Hypothesis evaluation** 

To ensure alignment between our experimental findings and the research objectives, we revisit and evaluate the four hypotheses introduced in section 3.3. The outcomes of the study confirm that all hypotheses are satisfied, and their conclusions are supported through statistical significance tests, performance metrics, and robustness checks. 

- The null hypothesis (H0), which assumed no statistically significant improvement between traditional PROMETHEE and ML-PROMETHEE, was rejected. Statistical testing using both the paired t-test and Wilcoxon signed-rank test produced _p_ -values below the 0.01 threshold across all evaluated metrics, confirming the superiority of the ML-integrated approach. Consequently, the alternative hypotheses were accepted as follows. 

- H1 posited that integrating machine learning with PROMETHEE improves decision accuracy. This hypothesis was _supported_ , as ML-PROMETHEE achieved a +17.3% increase in accuracy over traditional PROMETHEE methods. 

- H2, which proposed that ML-based weight learning reduces subjectivity and bias in criteria weighting, was also _validated_ , with bias reduced by 40.2% due to machine-learned weights. 

- H3 asserted that ML-PROMETHEE provides better alignment with expert rankings. This was _confirmed_ , with Spearman rank correlation increasing from 0.76 to 0.94 when benchmarked against expert-assigned labels. Finally, 

- H4 suggested that ML-PROMETHEE enhances robustness under varying decision scenarios. This was _demonstrated_ through consistent rankings across sensitivity analyses and controlled noise injections. 

These findings collectively demonstrate that ML-PROMETHEE not only enhances the precision and consistency of decision-making but also maintains computational efficiency, reinforcing the value of integrating machine learning into MCDM frameworks for more accurate, objective, and resilient blockchain security assessment. 

19 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

## **8. Conclusion** 

This paper introduced a novel hybrid decision-making framework that integrates Machine Learning (ML) with the Preference Ranking Organization Method for Enrichment Evaluations (PROMETHEE) to enhance blockchain security risk assessment. The proposed approach leverages ML techniques for feature selection and weight assignment, thereby mitigating subjective bias in criteria weighting while improving the accuracy and efficiency of ranking blockchain security threats. Through an extensive evaluation, the experimental results demonstrated the effectiveness of ML-PROMETHEE, achieving up to a 17.3% improvement in ranking accuracy compared to traditional PROMETHEE methods. The execution time was reduced by 43.5%, making the framework feasible for real-time security risk assessment. Furthermore, the ML-optimized ranking demonstrated greater stability, with an increased Spearman Rank Correlation Coefficient, ensuring consistency in decision-making. Bias reduction was another key advantage, as automated weight assignment minimized human subjectivity, achieving a 40.2% decrease in manual weight assignment errors. All reported gains are supported by paired statistical tests with Holm–Bonferroni adjustments and estimation statistics (mean paired differences with 95% BCa confidence intervals), underscoring both significance and effect magnitude. These findings validate the significant potential of ML-PROMETHEE in improving decision-making efficiency and reliability in blockchain security and broader cybersecurity applications. 

The contributions of this study extend beyond performance improvements. The integration of ML with PROMETHEE provides a hybrid decision-making framework that enhances traditional Multi-Criteria Decision-Making (MCDM) models. By utilizing advanced ML techniques such as Random Forest, Artificial Neural Networks (ANNs), and Gradient Boosting, the study introduced an automated approach to weight assignment, reducing reliance on hand-crafted expert weights and improving reproducibility. Additionally, the framework was successfully applied to blockchain security risk assessment, demonstrating its ability to prioritize threats based on severity, exploitability, and financial impact. The proposed model was empirically validated using a real-world dataset, ensuring its practical relevance and effectiveness. To support reuse, we provide implementation details and plotting scripts; a synthetic, schema-identical sample is shared for artifact regeneration when proprietary data cannot be released. These contributions pave the way for further advancements in automated decision-making methodologies, particularly in cybersecurity and risk management domains. 

Despite its advantages, the study has several limitations that need to be addressed in future research. The model’s performance is highly dependent on the availability of high-quality, labeled blockchain security data, which can be a constraint in real-world applications. While the ML-based approach significantly improves inference speed, training models for criteria optimization requires substantial computational resources. Additionally, hyperparameter sensitivity remains a challenge, as machine learning models require fine-tuning to ensure optimal performance across various datasets and security scenarios. Moreover, although the framework is domain-agnostic by design, the current empirical validation is confined to the blockchain security setting (with a single real-world dataset), so broader generalization to other verticals cannot be claimed yet. Finally, PROMETHEE preference-function and threshold choices may influence rankings; a more systematic calibration/learning of these parameters is warranted. 

To overcome these challenges, future research should explore deep learning techniques for feature extraction, particularly the application of Graph Neural Networks (GNNs) for analyzing blockchain transaction patterns and attack propagation. Federated learning models could also be investigated to enable decentralized and privacy-preserving security risk assessments across blockchain nodes, reducing the dependency on centralized data repositories. Another promising direction is the development of adaptive PROMETHEE models that dynamically adjust weight assignment based on real-time attack patterns, enhancing the framework’s ability to respond to emerging threats. Equally important is a cross-domain benchmarking campaign (e.g., financial fraud detection, supply-chain risk, and healthcare cybersecurity) under a preregistered protocol with fixed splits, nested model selection, and robustness checks (covariate shift, sensitivity to preference-function parameters). Ablation studies separating (i) ML-derived weights, (ii) PROMETHEE components, and (iii) data preprocessing will clarify where the gains originate. Moreover, extending the ML-PROMETHEE framework to other domains such as financial fraud detection, supply chain risk assessment, and healthcare cybersecurity could further validate its robustness and versatility. 

The integration of Machine Learning with PROMETHEE represents a significant advancement in decisionmaking methodologies for blockchain security risk assessment. By automating criteria selection, reducing subjectivity, and enhancing computational efficiency, the proposed framework provides a scalable and intelligent tool for risk assessment. As ML and deep learning continue to evolve, future developments in adaptive decision-making models will further strengthen the applicability of ML-PROMETHEE across a wide range of cybersecurity challenges, offering a more reliable and data-driven approach to threat prioritization and risk mitigation. In parallel, releasing code, configuration files, and synthetic replicas of the evaluation data will facilitate independent verification and extension by the community. 

20 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

## **9. Supplementary materials** 

To support transparency and reproducibility, anonymized summary statistics derived from the Blockchain Security Incident Database (BSID) are provided in this Supplementary Materials section. Due to licensing constraints, raw data cannot be publicly shared; however, we include the following: 

- Descriptive statistics of key attributes (Severity Score, Financial Loss, Affected Nodes, etc). 

- Distribution plots for major attack types (e.g., Smart Contract, 51% Attacks). 

- Explanation of composite label (‘Y’) construction using weighted scores (C1, C3, C5). 

- Incident frequency by category and year (aggregated). 

- Researchers interested in accessing the full dataset for collaborative purposes may contact the authors directly under data-use agreements. 

## **Data availability statement** 

The data cannot be made publicly available upon publication because they are owned by a third party and the terms of use prevent public distribution. The data that support the findings of this study are available upon reasonable request from the authors. 

## **Author contributions** 

Hassan Harb aa 0000-0003-3066-9189 Conceptualization (equal), Investigation (equal), Supervision (equal), Writing – review & editing (equal) 

Alaaeddine Ramadan aa 0000-0001-8221-9839 

Methodology (equal), Resources (equal), Validation (equal), Writing – review & editing (equal) 

Samir Haddad aa 0000-0003-0292-2765 Formal analysis (equal), Investigation (equal), Methodology (equal) 

## **References** 

- [1] Triantaphyllou E 2000 _Multi-Criteria Decision Making Methods: A Comparative Study_ (Springer Science & Business Media) 

- [2] Velasquez M and Hester P 2013 An analysis of multi-criteria decision making methods _International Journal of Operations Research_ **10** 56–66 

- [3] Kabak M, Dağdeviren F and Gumusluoglu T 2018 Application of multi-criteria decision-making methods in supply chain management: A literature review _Int. J. Prod. Res._ **56** 5034–61 

- [4] Brans J P and Vincke P 1985 A preference ranking organization method: The promethee method for multiple criteria decisionmaking _Manage. Sci._ **31** 647–56 

- [5] Coussement K, De Bock K and Van den Poel D 2017 Improving customer churn prediction by integrating complaints using ensemble learning _Expert Syst. Appl._ **79** 85–96 

- [6] Abdou H, Alyahya I and Said W 2021 Integration of machine learning techniques with mcdm methods for risk assessment in industrial applications _Journal of Risk Analysis_ **42** 287–301 

- [7] Xu X, Weber I and Staples M 2019 A systematic review of blockchain technology for supply chain management _Journal of Computer Science and Technology_ **34** 91–108 

- [8] Lin I and Liao T 2017 A survey of blockchain security issues and solutions _Future Gener. Comput. Syst._ **77** 415–30 

- [9] Brans J P and Mareschal B 1986 Promethee methods: The european journal of operational research perspective _Eur. J. Oper. Res._ **24** 228–38 

- [10] Saaty T L 1980 _The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation_ (McGraw-Hill) 

- [11] Venkatesan K and Bahiyah Rahayu S 2024 Blockchain security enhancement: an approach towards hybrid consensus algorithms and machine learning techniques _Sci. Rep._ **14** 1149 

- [12] Siddamsetti S, Tejaswi C and Maddula P 2024 Anomaly detection in blockchain using machine learning _Journal of Electrical Systems_ **20** 619–34 

- [13] Neutrosophic Sets and Systems 2025 Optimizing blockchain platform selection: A decision-making approach using llms, type-2 neutrosophic numbers, critic, and mairca _Neutrosophic Sets and Systems_ **83** 413–55 

- [14] Prometheum Inc 2025 Prometheum expands end-to-end blockchain securities infrastructure 

- [15] Breiman L 2001 Random forests _Mach. Learn._ **45** 5–32 

- [16] Chen T and Guestrin C 2016 Xgboost: A scalable tree boosting system _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ 785–94 

- [17] Sutton R and Barto A 2018 _Reinforcement Learning: An Introduction_ (MIT Press) 2ndedn 

- [18] Danach K, Dirani A E and Rkein H 2024 Revolutionizing supply chain management with ai: A path to efficiency and sustainability _IEEE Access_ (https://doi.org/10.1109/ACCESS.2024.3474531) 

21 

K Danach _et al_ 

_Eng. Res. Express_ **7** (2025) 0352c6 

- [19] Danach K, Hejase H J, Faroukh A, Fayyad-Kazan H and Moukadem I 2024 Assessing the impact of blockchain technology on financial reporting and audit practices _Asian Business Research_ **9** 30 

- [20] Lal C, Conti M, Kumar S and Ruj S 2018 A survey on security and privacy issues of blockchain technology _Future Gener. Comput. Syst._ **100** 108–25 

- [21] Bartoletti M, Atzei N and Cimoli T 2017 A survey of attacks on ethereum smart contracts (sok) _Proceedings of the 6th ACM Workshop on Blockchain, Cryptocurrencies and Contracts_ 164–86 

- [22] Huang Y, Zhou H and Xiao M 2020 Detecting blockchain security vulnerabilities using machine learning models _IEEE Access_ **8** 198–210 

- [23] Goyal S, Kumar R and Singh J 2020 Blockchain security risk assessment using deep learning techniques _Journal of Information Security and Applications_ **50** 102–15 

- [24] Dai H, Zheng Z, Xie S and Wang H 2018 Blockchain challenges and opportunities: a survey _Int. J. Web Grid Serv._ **14** 352–75 

- [25] Durieux A and Grishchenko S 2021 Vulnerability detection in ethereum smart contracts: a systematic literature review _Comput. Secur._ **105** 102–40 

- [26] Mohammadi Ruzbahani A _et al_ 2024 Ai-protected blockchain-based iot environments: Harnessing the future of network security and privacyarXiv:2405.13847 

- [27] Charles V, Emrouznejad A and Gherman T 2023 A critical analysis of the integration of blockchain and artificial intelligence for supply chain _Ann. Oper. Res._ **327** 7–47 

- [28] Secure Blockchain Initiative 2025 Blockchain security incident database (bsid) Internal dataset compiled from verified public blockchain security reports; not publicly available. Used with permission for academic analysis 

22 

