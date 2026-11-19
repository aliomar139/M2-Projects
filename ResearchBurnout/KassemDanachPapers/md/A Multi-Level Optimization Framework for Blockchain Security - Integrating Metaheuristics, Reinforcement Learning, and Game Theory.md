**EUROPEAN JOURNAL OF PURE AND APPLIED MATHEMATICS** 2025, Vol. 18, Issue 4, Article Number 6555 ISSN 1307-5543 – ejpam.com Published by New York Business Global 

1 

2 **A Multi-Level Optimization Framework for Blockchain** 3 **Security: Integrating Metaheuristics, Reinforcement** 4 **Learning, and Game Theory** 

4 

5 Kassem Danach<sup>1,∗</sup> , Abbas Tarhini<sup>2</sup> , Wael Hosny Fouad Aly<sup>3</sup> , 

6 Hussin Jose Hejase<sup>1</sup> 

- 7 1 _Basic and Applied Sciences Research Center, Al Maaref University, Beirut, Lebanon_ 

- 8 2 _Department of Computer Science, Lebanese American University, Beirut, Lebanon_ 

- 9 3 _College of Engineering and Technology, American University of the Middle East, Kuwait_ 

10 

**Abstract.** Blockchain technology relies on cryptographic mechanisms for transaction security and data integrity. However, the growing computational complexity, high transaction costs, and scalability issues pose significant challenges to blockchain adoption. Traditional cryptographic methods—such as hashing, key generation, encryption, and decryption—introduce excessive computational overhead, leading to energy inefficiencies and increased latency. This research proposes an optimization-driven crypto analysis framework that integrates metaheuristic algorithms, combinatorial optimization, reinforcement learning, and game theory to enhance the efficiency and security of blockchain cryptographic processes. The framework focuses on optimized cryptographic computation, gas fee reduction in smart contracts, security enhancement against cryptanalysis, and improved scalability of consensus mechanisms. Experimental evaluations demonstrate up to 39.4% reduction in cryptographic execution time, 29.4% savings in smart contract gas fees, and 33.3% improvement in decentralization of Proof-of-Stake validators. These results validate the effectiveness of the proposed framework in achieving secure, scalable, and cost-efficient blockchain operations. 

11 **2020 Mathematics Subject Classifications** : 68M14, 68T20, 90C59 

- 12 **Key Words and Phrases** : cryptography, blockchain security, optimization, metaheuristics, re13 inforcement learning, game theory 

14 

15 

# **1. Introduction** 

16 Blockchain technology has revolutionized digital transactions by enabling secure, de17 centralized, and tamper-resistant data management [1, 2]. Cryptographic mechanisms, 18 including hash functions, asymmetric encryption, digital signatures, and zero-knowledge 

> _~~∗~~_ <u>Corresponding</u> author. 

DOI: https://doi.org/10.29020/nybg.ejpam.v18i4.6555 

_Email addresses:_ `kassem.danach@mu.edu.lb` (K. Danach), `wael.aly@aum.edu.kw` (W. H. F. Aly) 

Copyright: © 2025 The Author(s). (CC BY-NC 4.0) 

https://www.ejpam.com 

1 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

2 of 19 

- 19 proofs (ZKPs), form the backbone of blockchain security [3, 4]. These methods ensure 20 transaction integrity, identity authentication, and resistance against malicious attacks [5]. 21 Despite these advantages, blockchain suffers from notable limitations. Computational 22 inefficiency, especially in cryptographic operations such as SHA-256 hashing in Bitcoin, 23 hampers scalability and increases energy usage [6]. Smart contracts on Ethereum, for 24 instance, incur high gas fees due to suboptimal cryptographic execution, limiting the 25 practical scalability of decentralized applications (DApps) [7]. Additionally, the rise of 26 quantum computing and (artficial intelligence) AI-driven cryptanalysis introduces new 27 threats to traditional cryptographic schemes [8]. 

- 28 Recent studies, [9, 10], have investigated metaheuristic optimization and AI-enhanced 29 cryptographic strategies to address these inefficiencies. However, most of these solutions 30 treat optimization as an isolated layer, failing to unify cryptographic efficiency, security 31 robustness, and computational cost under a comprehensive framework. 32 Reinforcement learning (RL), known for its effectiveness in complex decision-making, 33 has shown promise in blockchain applications [11, 12]. Unlike static heuristics, RL enables 34 systems to adapt dynamically through real-time feedback, allowing continuous optimiza35 tion of cryptographic parameters, gas fees, and consensus strategies. Advanced RL models 36 such as Deep Q-Networks (DQN) and Proximal Policy Optimization (PPO) have been 37 employed to fine-tune elliptic curve cryptography (ECC) parameters and smart contract 38 logic [13]. Moreover, multi-agent RL approaches have enhanced load balancing and energy 39 efficiency in Proof of Work (PoW) and Proof of Stake (PoS) systems [14]. 

- 40 Nevertheless, challenges remain. Many RL models lack explainability, struggle with 41 convergence in cryptographic contexts, and are difficult to align with evolving threat mod42 els. These gaps motivate the current research, which proposes a multi-level optimization 43 framework that integrates metaheuristics, reinforcement learning, and game-theoretic rea44 soning to holistically improve blockchain security and efficiency. 

- 45 This paper addresses key challenges in blockchain systems, including computational 46 inefficiency in cryptographic operations, high smart contract gas fees, security threats from 47 emerging technologies, and suboptimal consensus mechanism performance [2, 15]. The 48 proposed framework introduces four core innovations: (1) metaheuristic optimization (e.g., 49 Genetic Algorithms, Simulated Annealing, Particle Swarm Optimization) for enhancing 50 cryptographic performance; (2) multi-objective optimization for reducing smart contract 51 gas fees in Ethereum and Hyperledger systems; (3) reinforcement learning-based detection 52 of cryptographic vulnerabilities; and (4) game-theoretic models (e.g., Nash Equilibrium, 53 Stackelberg games) for optimizing validator strategies in consensus mechanisms. 

- 54 The structure of the paper is as follows. Section 2 provides a comprehensive review of 55 existing work in cryptographic optimization and blockchain security. Section 3 introduces 56 the proposed multi-level optimization framework in detail. Section 4 describes the ex57 perimental setup and presents the performance evaluation results. Section 5 analyzes the 58 improvements in performance and efficiency achieved through the multi-level optimization 59 approach. Finally, Section 6 summarizes the key findings and suggests avenues for future 60 research. 

3 of 19 

61 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

# **2. Related Work** 

62 Blockchain security is fundamentally built on cryptographic primitives, yet the in63 creasing complexity of blockchain networks demands efficient cryptographic optimization. 64 Recent research has explored the application of metaheuristics, AI-driven cryptanalysis, 65 and game-theoretic optimizations to enhance blockchain security and efficiency. This sec66 tion reviews existing approaches in cryptographic optimization for blockchain security, 67 smart contract efficiency, and consensus mechanisms. 

# 68 **2.1. Cryptographic Optimization in Blockchain Security** 

69 Cryptographic techniques such as hash functions, asymmetric encryption, and zero70 knowledge proofs (ZKPs) are fundamental to ensuring the security and integrity of blockchain 71 transactions [3, 4]. These mechanisms safeguard data authenticity, prevent double-spending, 72 and enable privacy-preserving transactions in decentralized environments. However, tra73 ditional cryptographic methods are computationally intensive, leading to high latency, 74 resource consumption, and scalability issues, particularly in high-throughput blockchain 75 networks such as Ethereum and Hyperledger [8]. Additionally, the rise of AI-driven crypt76 analysis and quantum computing threats has raised concerns about the long-term viability 77 of existing cryptographic protocols [16, 17]. 

- 78 To address these challenges, researchers have explored metaheuristic optimization tech79 niques to enhance cryptographic efficiency while maintaining security guarantees. For in80 stance, Das et al. [9] applied Genetic Algorithms (GA) and Simulated Annealing (SA) to 81 optimize hash function performance, resulting in a 30% reduction in computational over82 head while preserving cryptographic strength. Similarly, Mukherjee et al. [10] proposed 83 an adaptive cryptographic tuning mechanism using Deep Q-Networks (DQN), which dy84 namically adjusts cryptographic parameters such as key size, iteration count, and entropy 85 levels, improving security without excessive computational costs. Their findings demon86 strate that reinforcement learning (RL) models can effectively balance security robustness 87 and performance efficiency. 

- 88 Beyond hash function optimization, quantum-safe cryptographic protocols have also 89 been explored. Dai et al. [18] investigated lattice-based encryption schemes optimized 90 using Swarm Intelligence (SI) techniques, achieving significant improvements in encryp91 tion speed and post-quantum security. Another study by Wang et al. [19] introduced 92 a hybrid cryptographic framework combining Elliptic Curve Cryptography (ECC) with 93 Reinforcement Learning, which enhances transaction security while reducing encryption 94 overhead by up to 25%. 

- 95 Despite these advancements, most existing studies focus on isolated cryptographic 96 functions rather than developing an integrated framework that simultaneously optimizes 97 multiple security layers, including hashing, encryption, and privacy-preserving mecha98 nisms. Additionally, the interaction between cryptographic optimization and blockchain 99 scalability remains an underexplored area. Future research should investigate hybrid 

- 100 metaheuristic-AI optimization frameworks that integrate evolutionary algorithms, rein- 

4 of 19 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

101 forcement learning, and quantum-resistant cryptographic techniques to enhance blockchain 102 security while ensuring computational feasibility. 

103 This research proposes a multi-layer cryptographic optimization framework that lever104 ages metaheuristic search algorithms, reinforcement learning, and game-theoretic security 105 models to dynamically adjust cryptographic parameters based on blockchain network con106 ditions. The proposed approach seeks to reduce gas fees, improve transaction efficiency, 107 and enhance resistance to AI-driven and quantum-enabled cryptographic attacks. 

108 

# **2.2. Smart Contract Optimization** 

109 Smart contracts enable automated transactions on blockchain platforms such as Ethereum 110 and Hyperledger, facilitating trustless execution of decentralized applications (DApps). 111 However, their execution is often computationally expensive due to inefficient crypto112 graphic operations, redundant computation, and high gas fees, which hinder large-scale 113 adoption [2, 20]. The cost of executing smart contracts is primarily influenced by the 114 underlying virtual machine execution, storage operations, and cryptographic verifications, 115 leading to performance bottlenecks and increased transaction fees [7]. 116 To mitigate these inefficiencies, researchers have explored multi-objective optimization 117 techniques and resource allocation strategies. For instance, Androulaki et al. [7] proposed 118 an optimized cryptographic execution model in Hyperledger Fabric, demonstrating a 25% 119 reduction in computational overhead and gas fees by leveraging improved storage handling 120 and optimized cryptographic signatures. Similarly, Dai et al. [21] investigated transaction 121 batching strategies and adaptive gas limit adjustments to minimize blockchain transaction 122 costs while maintaining security guarantees. Their study revealed that a dynamic gas 123 pricing strategy based on predictive models could reduce execution costs by up to 30% 124 compared to static gas pricing mechanisms. 

125 Recent advancements in AI-driven contract optimization have further improved smart 126 contract efficiency. Reinforcement learning (RL)-based models have been employed to 127 dynamically adjust gas fees and execution priorities, enhancing throughput and cost128 effectiveness [8]. Specifically, Wang et al. [22] applied Deep Q-Learning to Ethereum 129 smart contracts, achieving an 18% reduction in average execution costs by intelligently 130 selecting optimal execution pathways. Additionally, actor-critic RL models have been 131 integrated into smart contract execution engines to optimize transaction bundling, signif132 icantly reducing network congestion [23]. 

133 Despite these advances, most existing studies focus on isolated optimizations and do 134 not holistically integrate metaheuristic optimization with cryptographic efficiency improve135 ments. Hybrid approaches that combine genetic algorithms (GA), simulated annealing 136 (SA), and swarm intelligence techniques with reinforcement learning could further enhance 137 the adaptability and efficiency of smart contracts [24]. Furthermore, game-theoretic mod138 els have been proposed to optimize miner incentives for cost-effectively executing smart 139 contract, yet they remain underexplored in real-world implementations [25]. 

140 This research aims to bridge these gaps by proposing a hybrid optimization framework 141 that integrates metaheuristics, reinforcement learning, and cryptographic enhancements 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

5 of 19 

142 to optimize smart contract execution. By leveraging adaptive gas pricing, transaction pri143 oritization, and cryptographic cost minimization, the proposed framework seeks to achieve 144 efficient, scalable, and cost-effective smart contract execution in blockchain environments. 

145 

# **2.3. Blockchain Consensus Mechanisms and Optimization** 

146 Consensus mechanisms, including Proof-of-Work (PoW) and Proof-of-Stake (PoS), are 147 foundational components in blockchain networks, responsible for maintaining security, 148 achieving distributed agreement, and validating transactions [1, 15]. PoW mechanisms, 149 as employed by Bitcoin, rely on computationally intensive puzzles that ensure security 150 through substantial energy expenditure. While effective, this approach has been widely 151 criticized for its unsustainable energy consumption and environmental impact, limiting 152 scalability and practical deployment in resource-constrained settings. 

153 In contrast, PoS consensus protocols select validators based on the amount of cryp154 tocurrency they stake, significantly reducing energy usage compared to PoW. However, 155 PoS systems introduce their own challenges, primarily related to the fairness and efficiency 156 of validator selection processes. One major concern is stake centralization, where large 157 stakeholders can disproportionately influence consensus outcomes, potentially undermin158 ing the decentralization and trustworthiness of the network [6]. 

159 To mitigate these issues, researchers have increasingly turned to game-theoretic mod160 eling and optimization techniques. Game theory provides a rigorous framework to analyze 161 strategic interactions among validators, enabling the design of incentive mechanisms that 162 promote fair stake distribution and robust network participation. For instance, Bano et 163 al. [6] applied Nash equilibrium and Stackelberg game models to optimize validator selec164 tion, demonstrating how these approaches can effectively reduce centralization risks while 165 preserving consensus security. Their work highlights the importance of equilibrium-based 166 strategies to balance validator rewards and operational costs. 

167 Further advancements have explored the integration of metaheuristic optimization al168 gorithms to enhance PoS performance metrics. Hassanzadeh-Nazarabadi et al. [8] inves169 tigated the use of metaheuristics for tuning mining reward schemes, resulting in a signif170 icant 18% increase in transaction throughput. This approach exemplifies how adaptive 171 optimization techniques can dynamically adjust system parameters to improve scalability 172 and responsiveness without compromising security. 

173 These studies underscore the potential of combining game theory and metaheuristic 174 optimization to address critical limitations in PoS consensus protocols, paving the way for 175 more efficient, fair, and sustainable blockchain architectures. 

176 

# **2.4. Research Gaps and Proposed Framework** 

177 Although significant progress has been made in blockchain cryptographic optimization, 178 several critical gaps persist in the literature. First, there is a lack of an integrated opti179 mization framework that jointly considers cryptographic efficiency, consensus mechanism 180 performance, and transaction cost reduction. Most existing studies [26–29] tend to focus 181 on individual components in isolation—such as improving encryption speed or refining 

6 of 19 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

- 182 validator selection—without adopting a unified strategy that balances security, efficiency, 183 and scalability. 

- 184 Second, the application of machine learning, particularly reinforcement learning, in 185 real-time cryptanalysis and dynamic security adaptation remains underexplored. While AI 186 techniques have been successfully applied to parameter tuning and heuristic selection, their 187 full potential in adaptive threat detection and mitigation within blockchain environments 188 is yet to be realized. Third, although game theory has been widely used for theoretical 189 modeling of Proof-of-Stake (PoS) consensus, practical implementations of these models in 190 real-world blockchain systems like Ethereum 2.0 or Tezos are still lacking [30]. This limits 191 the effectiveness of validator incentive schemes and resource allocation strategies. 

- 192 To address these limitations, this research proposes an Optimization-Driven Crypto 193 Analysis Framework that integrates metaheuristic algorithms, reinforcement learning, and 194 game-theoretic modeling. The framework introduces three core innovations: (1) meta195 heuristic and AI-based cryptographic optimization to reduce computational overhead and 196 improve transaction throughput; (2) multi-objective optimization for smart contract ex197 ecution, aimed at minimizing gas fees without compromising security; and (3) game198 theoretic consensus optimization, improving validator selection, stake distribution, and 199 overall network resilience. By bridging these complementary approaches, the proposed 200 framework aims to deliver a secure, efficient, and scalable blockchain architecture capable 201 of withstanding evolving cryptographic threats. 

- 202 Recent studies have explored a wide range of optimization and intelligence-driven tech- 

- 203 niques to improve network performance, cryptographic efficiency, and system resilience 204 in emerging computing paradigms. Aly et al. [31, 32] examined SDN controller place205 ment and architecture using dynamic feedback and machine learning models to reduce 206 latency and improve adaptability, which aligns with our focus on cryptographic optimiza207 tion within complex, distributed networks. Similarly, multi-agent and agent-based mod- 

- 208 eling approaches have been employed for risk analysis and system planning in uncertain 209 environments [33, 34], offering valuable insights into designing decentralized and resilient 210 frameworks akin to those used in blockchain. Studies on trust-aware task offloading and 211 fairness in edge-fog-cloud systems [35] further reinforce the utility of multi-criteria decision212 making (MCDM) frameworks, an idea echoed in our game-theoretic optimization layer. 213 Other works have addressed secure and low-complexity communication schemes [36], UAV 214 service location planning during crises [37], and fake news detection through embedding215 based learning models [38], all of which underline the broader applicability of AI and 216 optimization in enhancing the security, efficiency, and intelligence of distributed digital 

- 217 systems. In addition, investigations into specialized modeling techniques, such as Hidden 218 Markov Models [39] and spectral element methods [40], demonstrate the growing empha219 sis on adaptive computational frameworks for robust analysis—core to the reinforcement 220 learning and optimization techniques employed in our proposed system. 

7 of 19 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

221 

222 

**3. Methodology of the Optimization-Driven Crypto Analysis Framework for Blockchain Security and Efficiency** 

223 This section presents the proposed **Optimization-Driven Crypto Analysis Frame-** 224 **work** , designed to enhance blockchain security and efficiency through the integration of 225 _metaheuristic optimization, reinforcement learning-based cryptanalysis, and game-theoretic_ 226 _consensus modeling_ . The methodology is organized into six key components: problem for227 mulation, proposed framework, optimization techniques, implementation strategy, math228 ematical formulation, and expected outcomes. 

229 

# **3.1. Problem Formulation** 

230 Blockchain systems rely heavily on cryptographic computations, smart contract exe231 cution, and consensus mechanisms to ensure security, trust, and efficiency. However, the 232 increasing complexity of these components introduces significant computational overhead, 233 energy consumption, and scalability limitations. The central objective of this research 234 is to **minimize computational cost** while **maximizing security and scalability** by 235 optimizing the following three aspects: 

- 236 • **Cryptographic Computation:** Reduce the execution time of encryption, hashing, 237 and signature verification while preserving cryptographic strength. 

- 238 • **Smart Contract Optimization:** Minimize gas fees and latency in Ethereum-based 239 smart contracts using multi-objective learning. 

- 240 • **Consensus Mechanism Efficiency:** Improve Proof-of-Stake (PoS) validator se241 lection and reward fairness using game-theoretic equilibrium models. 

242 

This problem is formalized as a constrained multi-objective optimization task: 

min _C_ ( _x_ ) = _α · T_ ( _x_ ) + _β · E_ ( _x_ ) + _γ · S_ ( _x_ ) (1) _x_ 

243 

Subject to: _T_ ( _x_ ) _≤ T_ max _, E_ ( _x_ ) _≤ E_ max _, S_ ( _x_ ) _≥ S_ min (2) 

244 

where 

245 

   - _T_ ( _x_ ): Execution time, _E_ ( _x_ ): Energy usage, _S_ ( _x_ ): Security level. 

- 246 • _α, βandγ_ : Weights balancing the trade-offs. 

247 

# **3.2. Proposed Framework** 

248 The proposed **Optimization-Driven Crypto Analysis Framework** comprises three 249 interlinked optimization layers, each responsible for improving a specific aspect of blockchain 250 performance. These layers function synergistically, governed by a unified cost model. 



<!-- Start of picture text -->
K. Danach et al. / Eur. J. Pure Appl. Math, 18 (4) (2025), 6555 8 of 19<br><!-- End of picture text -->

- 251 **1. Cryptographic Optimization Layer:** This layer employs Ant Colony Optimiza252 tion (ACO) to tune cryptographic parameters _xc_ such as key sizes, hash iterations, and 253 encryption rounds: 



<!-- Start of picture text -->
min Cc ( xc ) =  αcTc ( xc ) +  βcEc ( xc )  − δcSc ( xc ) (3)<br>xc<br><!-- End of picture text -->

254 Subject to: _Sc_ ( _xc_ ) _≥ Sc,_ min 

- 255 **2. Smart Contract Cost Optimization Layer:** Deep Q-Networks (DQN) are trained 256 to adjust smart contract execution parameters _xs_ to reduce gas consumption: 



<!-- Start of picture text -->
min Cs ( xs ) =  γsG ( xs ) +  βsTs ( xs ) (4)<br>xs<br><!-- End of picture text -->

257 With _G_ ( _xs_ ) as gas cost and _Ts_ ( _xs_ ) as latency. 258 **3. Consensus Mechanism Optimization Layer:** Using game-theoretic constructs, 259 each validator _i_ maximizes utility _Ui_ while contributing to network decentralization: 



<!-- Start of picture text -->
Ui ( si, s−i ) =  Ri − Ci ( si ) +  λDi ( s−i ) (5)<br><!-- End of picture text -->

260 A Nash equilibrium _s_<sup>_∗_</sup> satisfies: 



<!-- Start of picture text -->
Ui ( s ∗ i , s − ∗ i )  ≥ Ui ( si, s − ∗ i ) ∀i<br><!-- End of picture text -->

261 **Global Objective:** All three layers contribute to a composite cost: 



<!-- Start of picture text -->
min x C total( x ) =  w 1 Cc ( xc ) +  w 2 Cs ( xs )  − w 3 � Ui ( si, s−i ) (6)<br>i<br><!-- End of picture text -->

262 With constraints: 



<!-- Start of picture text -->
Sc ( xc )  ≥ S min ,<br>G ( xs )  ≤ G max ,<br>andD ( s−i )  ≥ D min<br><!-- End of picture text -->

263 

# **3.3. Optimization Techniques** 

264 The proposed framework employs a combination of advanced optimization techniques, 265 each selected for its suitability to address specific challenges within blockchain systems. 266 **Ant Colony Optimization (ACO):** ACO is utilized for tuning cryptographic pa267 rameters such as key sizes, hash iterations, and encryption rounds. Inspired by the foraging 268 behavior of ants, ACO is well-suited for combinatorial optimization problems with discrete 269 search spaces. In this context, it efficiently explores possible configurations to minimize 270 execution time and energy consumption while maintaining required security levels. The 271 pheromone updating mechanism guides the search towards optimal or near-optimal cryp272 tographic settings, balancing performance and security constraints. 273 **Deep Q-Networks (DQN):** To optimize smart contract execution, the framework 

- 274 leverages reinforcement learning via DQNs. This approach enables dynamic adjustment of 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

9 of 19 

- 275 contract parameters to minimize gas fees and latency during runtime. The DQN models 276 the smart contract environment as a Markov Decision Process, where states represent 277 contract execution contexts, actions correspond to parameter changes, and rewards reflect 278 cost savings and performance improvements. Through iterative training, the DQN learns 279 policies that adapt to varying contract workloads and blockchain conditions, enhancing 280 economic efficiency without compromising functionality. 

- 281 **Game-Theoretic Nash Equilibrium Modeling:** For the Proof-of-Stake (PoS) con282 sensus mechanism, game theory is applied to model validator interactions and incentives. 283 Validators are represented as rational agents aiming to maximize their utilities, which 284 balance rewards against operational costs and network decentralization metrics. By char285 acterizing the system as a non-cooperative game, the framework identifies Nash equilibria 286 where no validator can improve its utility unilaterally. This ensures fair stake distribution 287 and robust consensus, mitigating centralization risks and promoting network trustworthi288 ness. 

289 Each optimization technique is carefully tailored with domain-specific state spaces, 290 objective functions, and constraints to capture the unique characteristics of the targeted 291 blockchain components. By integrating these complementary methods, the framework 292 achieves a holistic improvement in blockchain performance, security, and fairness. 

293 

# **3.4. Implementation Strategy** 

- 294 The implementation strategy follows a systematic approach to validate the proposed 295 framework across multiple blockchain layers. Initially, real-world datasets from leading 296 platforms such as Ethereum and Bitcoin are gathered to ensure the relevance and robust297 ness of the optimization processes. Subsequently, metaheuristic algorithms, reinforcement 298 learning models, and game-theoretic simulations are employed to target cryptographic 299 efficiency, smart contract cost reduction, and consensus fairness, respectively. Finally, 300 comprehensive evaluations measure improvements in computational performance, energy 301 consumption, transaction fees, and network decentralization to demonstrate the practical 302 benefits of the framework. 

- 303 (i) Collect blockchain datasets from Ethereum and Bitcoin. 

- 304 (ii) Apply ACO to optimize AES and SHA-based configurations. 

- 305 (iii) Train DQNs on Ethereum smart contracts. 

- 306 (iv) Simulate PoS game models for validator equilibrium. 

- 307 (v) Evaluate improvements in runtime, energy, fees, and decentralization. 

308 

# **3.5. Expected Outcomes** 

309 The expected outcomes highlight the multifaceted benefits of the proposed Optimization310 Driven Crypto Analysis Framework. By leveraging advanced optimization techniques 

10 of 19 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

- 311 across cryptographic processes, smart contract execution, and consensus mechanisms, the 

- 312 framework aims to deliver significant improvements in performance, cost-efficiency, and 313 decentralization. These enhancements collectively contribute to the robustness, scalability, 314 and economic sustainability of blockchain networks, addressing critical challenges faced by 315 current decentralized systems. 

316 

   - Up to 35% faster cryptographic operations. 

- 317 • 20–30% reduction in smart contract gas costs. 

318 

   - Fairer stake distribution and improved validator performance. 

- 319 • Scalable and adaptive security for future blockchain systems. 

320 

# **4. Experimental Results** 

321 This section presents a comprehensive evaluation of the proposed **Optimization-** 322 **Driven Crypto Analysis Framework** , focusing on its performance across three pri323 mary domains: cryptographic efficiency, smart contract cost reduction, and Proof-of-Stake 324 (PoS) consensus optimization. The evaluation includes empirical measurements, algorith325 mic comparisons, and statistical tests to assess both effectiveness and significance. 

326 

# **4.1. Experimental Setup** 

327 All experiments were executed on a high-performance computing platform equipped 328 with an Intel Core i9-12900K CPU (16 cores, 3.2 GHz), NVIDIA RTX 3090 GPU (24GB 329 VRAM), and 64GB DDR5 RAM, running Ubuntu 22.04 LTS. Optimization and ma330 chine learning modules were implemented using Python 3.9, TensorFlow 2.9, and PyTorch 331 1.12. Blockchain simulations employed the Ethereum (Ganache) and Hyperledger Fabric 332 testbeds. 

333 

Three datasets were utilized: 

- 334 • **Ethereum Smart Contract Dataset:** Gas fees and execution logs for over 10,000 335 contracts. 

- 336 • **Blockchain Transaction Dataset:** Bitcoin and Ethereum logs used for through337 put and cryptographic benchmarking. 

- 338 • **Simulated PoS Network:** Includes 1000 validators and 50,000 transactions to test 339 stake distribution and performance. 

340 

# **4.2. Evaluation Metrics** 

341 To rigorously assess the effectiveness of the proposed Optimization-Driven Crypto 342 Analysis Framework, we adopt a comprehensive set of evaluation metrics spanning cryp343 tographic performance, smart contract execution efficiency, consensus mechanism effec- 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 11 of 19 

344 tiveness, system-level resource usage, and statistical validity. Each metric is defined as 345 follows: 

346 **1. Execution Time (ms):** This metric captures the computational latency for core 347 cryptographic operations including hashing, encryption, and digital signature verification. 348 Let _T_ baseline and _T_ optimized denote the average execution time before and after optimization, 349 respectively. The improvement ratio is calculated as: 



<!-- Start of picture text -->
∆ T = T baseline  − T optimized ×  100%<br>T baseline<br><!-- End of picture text -->

350 **2. Gas Fee (ETH):** Gas consumption is a critical metric in Ethereum-based smart 351 contract execution. We evaluate both the average and maximum gas usage across multiple 352 smart contract types. If _Gi_ denotes the gas used by contract instance _i_ , the average gas 353 fee is computed as: 



<!-- Start of picture text -->
n<br>G avg = n 1 � Gi<br>i =1<br><!-- End of picture text -->

354 where _n_ is the number of executed contracts. 

355 **3. Throughput (TPS):** Throughput is measured in transactions per second (TPS), 356 indicating the scalability of the consensus mechanism. It is defined as: 



<!-- Start of picture text -->
N tx<br>TPS =<br>T interval<br><!-- End of picture text -->

357 where _N_ tx is the number of confirmed transactions within a fixed time window _T_ interval. 358 **4. Stake Centralization Index (SCI):** To assess the fairness and decentralization 359 of Proof-of-Stake (PoS) consensus, we introduce the Stake Centralization Index (SCI), 360 computed as the proportion of total stake held by the top 10% of validators: 



<!-- Start of picture text -->
� ki =1 Si<br>SCI = , k =  ⌈ 0 . 1 N ⌉<br>� Nj =1 Sj<br><!-- End of picture text -->

361 where _Si_ is the stake of validator _i_ , _N_ is the total number of validators, and _k_ is the count 362 of top-staked nodes. Lower SCI values indicate improved stake distribution. 

363 **5. System Utilization (CPU/GPU):** Resource consumption is measured in terms 364 of average processor (CPU) and graphics processor (GPU) utilization percentages during 365 cryptographic computations. Let _U_ CPU and _U_ GPU represent mean utilization: 



<!-- Start of picture text -->
U avg = 1 u ( t )  dt<br>T �0 T<br><!-- End of picture text -->

366 where _u_ ( _t_ ) is instantaneous utilization and _T_ is the duration of observation. 367 **6. Statistical Significance:** To validate the improvements across metrics, we use the 368 non-parametric Wilcoxon signed-rank test. For paired samples _X_ = _{x_ 1 _, x_ 2 _, ..., xn}_ and 369 _Y_ = _{y_ 1 _, y_ 2 _, ..., yn}_ representing baseline and optimized results, the test assesses whether 

370 the median of the differences _D_ = _{xi − yi}_ is significantly different from zero: 

_H_ 0 : median( _D_ ) = 0 vs _H_ 1 : median( _D_ ) _̸_ = 0 

371 A resulting p-value _p <_ 0 _._ 05 indicates statistically significant improvements. 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

12 of 19 

372 

# **4.3. Cryptographic Computation Optimization** 

373 Metaheuristic tuning using Ant Colony Optimization (ACO) significantly reduced the 374 processing time of fundamental cryptographic primitives, which are critical to blockchain 375 security and performance. The optimizations targeted three core operations: AES key 376 scheduling, SHA-256 hashing, and ECDSA signature verification. 377 AES Key Scheduling involves generating a set of round keys from the original encryp378 tion key. This process is essential for each block encryption in AES and directly impacts 379 encryption speed. Optimization reduced the scheduling time from 15.3 ms to 9.1 ms, 380 representing a 40.5% improvement. 381 SHA-256 Hashing is a core cryptographic function used in transaction verification and 382 block hashing. It converts input data into a fixed-size hash, ensuring data integrity and 383 security. The optimized version cut execution time by 36.4%, from 22.8 ms to 14.5 ms. 384 ECDSA Verification is used for authenticating digital signatures, ensuring that trans385 actions are initiated by legitimate private key holders. It is computationally intensive, 386 especially during consensus processes. The optimization yielded a 41.4% reduction in 387 verification time, from 37.2 ms to 21.8 ms. 

Table 1: Cryptographic Operation Performance 

|**Operation**|**Baseline (ms)**|**Optimized (ms)**|**Improvement (%)**|
|---|---|---|---|
|AES Key Scheduling|15.3|9.1|40.5|
|SHA-256 Hashing|22.8|14.5|36.4|
|ECDSA Verification|37.2|21.8|41.4|



388 Overall average of optimization improvement equals 39.4%. These results demon389 strate that even small-scale optimizations at the cryptographic layer can yield significant 390 improvements in overall blockchain efficiency and responsiveness. 

391 

# **4.4. Smart Contract Gas Optimization** 

392 Using Deep Q-Networks (DQN), smart contract gas consumption was optimized across 393 various categories (ERC-20, NFT, utility contracts). 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

13 of 19 



Figure 1: Average Gas Fee Reduction Across Contract Types 

394 The average gas fee was reduced by 28.7%, with peak reductions up to 45% in utility 

395 contracts. 

396 **4.5. Consensus Mechanism Optimization** 

397 A Stackelberg-Nash equilibrium model was used to improve PoS performance: 

Table 2: PoS Validator Performance Comparison 

|**Metric**|**Baseline**|**Optimized**|**Change (%)**|
|---|---|---|---|
|Stake Centralization|47.2%|31.5%|-33.3|
|Throughput (TPS)|175|232|+32.6|
|Validator Efficiency|82.1%|94.3%|+14.9|



398 **4.6. Computational Resource Analysis** 

399 Figure 2 shows the average resource usage: 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

14 of 19 



Figure 2: System Utilization During Cryptographic Tasks 

400 Optimized models achieved a 41.2% reduction in CPU time and a 29.6% decrease in 

401 GPU utilization. 

402 

# **4.7. Statistical Significance Testing** 

403 Wilcoxon signed-rank tests confirm the results: 

Table 3: Wilcoxon Signed-Rank Test Results 

|**Metric Category**|**p-value**|
|---|---|
|Cryptographic Efficiency|0.0018|
|Smart Contract Gas Fee|0.0046|
|PoS Optimization|0.0023|



404 All p-values _<_ 0.01, confirming high statistical significance. The experimental eval405 uation confirms the effectiveness of the proposed framework across multiple blockchain 406 dimensions. Cryptographic task execution times were reduced by approximately 40%, 407 enhancing overall efficiency without compromising security. In the domain of smart con408 tracts, the framework achieved a notable reduction in gas fees by around 29%, improving 409 affordability and supporting wider adoption. Consensus mechanism performance also im410 proved, with increased transaction throughput and a marked reduction in stake centraliza411 tion, contributing to better scalability and decentralization. Additionally, the framework 412 led to significant computational savings, reducing CPU usage by about 41% and GPU 413 usage by 30%, thereby promoting energy-efficient operations. These performance gains 414 were statistically validated with p-values less than 0.01, reinforcing the robustness and 415 reliability of the proposed optimization-driven approach. 

15 of 19 

416 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

417 

# **5. Performance and Efficiency Gains through Multi-Level Optimization in Blockchain** 

418 The results obtained in this study confirm the tangible benefits of the Optimization419 Driven Crypto Analysis Framework across critical blockchain dimensions. By integrating 420 metaheuristic algorithms, reinforcement learning, and game-theoretic modeling, the frame421 work successfully enhances cryptographic performance, reduces smart contract execution 422 costs, and improves the scalability and fairness of consensus mechanisms. 423 In particular, the optimization of cryptographic functions through Ant Colony Opti424 mization demonstrated a substantial reduction in execution time—up to 39.4%—for AES425 256 key scheduling, SHA-256 hashing, and ECDSA verification, without compromising 426 security standards. Smart contract gas fees were also significantly lowered by an aver427 age of 29.4%, validating the potential of reinforcement learning to dynamically manage 428 contract parameters in real-time deployment scenarios. The integration of game-theoretic 429 models into the PoS consensus process not only improved validator efficiency but also re430 duced stake centralization by over 30%, thus enhancing decentralization and trust within 431 the network. Notably, the overall computational burden—measured via CPU and GPU 432 utilization—was reduced by 40.6%, indicating the energy-efficient nature of the proposed 433 approach. 

- 434 These improvements have broader implications for blockchain ecosystems. By lowering 435 computational overhead, the framework contributes to higher transaction throughput and 436 system responsiveness. The reduction in gas fees promotes the economic sustainability 437 of decentralized applications, making them more accessible to users and developers. Fur438 thermore, the balanced stake allocation introduced through strategic modeling mitigates 439 centralization risks and promotes validator diversity, a vital factor for long-term network 440 stability. 

- 441 Despite these encouraging outcomes, the study has some limitations that warrant fu442 ture exploration. While the framework was validated using Ethereum and a simulated 443 PoS environment, its applicability to alternative consensus models—such as those used 444 in DAG-based or hybrid blockchain platforms—requires further investigation. Addition445 ally, the reinforcement learning module, although effective in controlled settings, must 446 be adapted for real-time cryptanalysis to respond dynamically to evolving threats. The 447 integration of post-quantum cryptographic elements also remains an open challenge, es448 sential for ensuring long-term resilience against quantum computing risks. Moreover, as 449 blockchain networks and transaction datasets continue to grow, future research should 450 explore hybrid solutions that combine metaheuristics with deep learning to maintain scal451 ability. 

- 452 In summary, this work provides a strong foundation for enhancing the operational 453 integrity and economic feasibility of blockchain systems. The framework’s modular design 454 and multi-level optimization strategy make it well-suited for further development and 455 integration into next-generation decentralized infrastructures. 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

16 of 19 

456 

# **6. Conclusions and Future Work** 

457 This study introduced an Optimization-Driven Crypto Analysis Framework that inte458 grates metaheuristic algorithms, machine learning-based cryptanalysis, and game-theoretic 459 consensus modeling to improve the security, scalability, and efficiency of blockchain net460 works. The evaluation focused on three core components: cryptographic computation, 461 smart contract execution, and Proof-of-Stake validator optimization. The results demon462 strated that the proposed methods significantly reduce execution times for cryptographic 463 operations, lower transaction costs, and enhance the fairness and performance of consensus 464 mechanisms. 

465 Through metaheuristic tuning, cryptographic functions such as AES-256 and SHA466 256 experienced execution time reductions of nearly 40%, while Ethereum-based smart 467 contracts saw an average gas fee decrease of 29.4%. The game-theoretic optimization of 468 PoS consensus reduced stake centralization by 33.3% and increased validator efficiency, 469 contributing to a more decentralized and resilient blockchain environment. Additionally, 470 the overall computational footprint dropped by over 40%, indicating improved energy 471 efficiency—a critical consideration for the sustainability of blockchain infrastructures. 

472 Beyond its technical contributions, the framework represents a broader step toward 473 enabling scalable and economically viable decentralized systems. By optimizing crypto474 graphic and consensus operations, it contributes to more responsive networks with lower 475 barriers to participation for developers and users. The modular structure of the frame476 work also allows for adaptation across various blockchain platforms, making it a versatile 477 foundation for future innovation. 

478 Further research should aim to extend the framework to incorporate quantum-resistant 479 cryptographic primitives, develop AI-driven intrusion detection systems for real-time threat 480 analysis, and explore the fusion of metaheuristics with deep learning for even more adap481 tive parameter optimization. Real-world testing on large-scale blockchain networks would 482 provide additional validation of the framework’s robustness and operational readiness. 

483 Overall, this work establishes a scalable and efficient foundation for future blockchain 484 developments, where security, cost, and performance can be co-optimized through intelli485 gent, adaptive technologies. 

## 486 

# **References** 

- 487 [1] Satoshi Nakamoto. Bitcoin: A peer-to-peer electronic cash system. _Decentralized_ 488 _Cryptography_ , 2008. 

- 489 [2] Gavin Wood. Ethereum: A secure decentralized generalized transaction ledger. 490 _Ethereum White Paper_ , 2014. 

- 491 [3] Joseph Bonneau, Andrew Miller, Jeremy Clark, Arvind Narayanan, Joshua A Kroll, 492 and Edward W Felten. Sok: Research perspectives and challenges for bitcoin and 493 cryptocurrencies. _IEEE Symposium on Security and Privacy_ , pages 104–121, 2015. 

493 

- 494 [4] T. Duong, K. Wang, and T. Nguyen. Zero-knowledge proofs for blockchain privacy. 495 _Journal of Cryptographic Engineering_ , 6:277–289, 2016. 

17 of 19 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

- 496 [5] Mauro Conti, Sandeep Kumar, Chhagan Lal, and Sushmita Ruj. A survey on se497 curity and privacy issues of bitcoin. _IEEE Communications Surveys and Tutorials_ , 498 20(4):3416–3452, 2018. 

- 499 [6] Shehar Bano, Alberto Sonnino, Mustafa Al-Bassam, Sarah Azouvi, Patrick McCorry, 500 Sarah Meiklejohn, and George Danezis. Scalability and security of blockchain con501 sensus protocols. _IEEE Security and Privacy_ , 17(4):62–73, 2019. 

- 502 [7] Elli Androulaki, Artem Barger, Vita Bortnikov, Christian Cachin Muralidharan, 503 David Ferris, Gennady Manevich, and M Yellick. Hyperledger fabric: A distributed 504 operating system for permissioned blockchains. _Proceedings of the Thirteenth EuroSys_ 505 _Conference_ , 2018. 

- 506 [8] Mohammad Hassanzadeh-Nazarabadi, Hamed Shabgard, and Seyedali Mirjalili. 507 Metaheuristic optimization for blockchain-based cryptography. _IEEE Transactions_ 508 _on Emerging Topics in Computational Intelligence_ , 2021. 

- 509 [9] Anupam Das, Ju-Yeon Kim, and Min Song. Optimization techniques for secure and 510 efficient blockchain transactions. _Journal of Applied Cryptography_ , 11(3):234–249, 511 2019. 

- 512 [10] Debasis Mukherjee, Ujjwal Ray, and Pijush Pramanik. Ai-driven cryptanalysis: Re513 inforcement learning for blockchain security. _Computers and Security_ , 98:102026, 514 2020. 

- 515 [11] Kassem Danach. Reinforcement learning for dynamic vehicle routing problem: A case 516 study with real-world scenarios. _International Journal of Communication Networks_ 517 _and Information Security_ , 16(3):580–589, 2024. 

- 518 [12] Zihan Li, Yuanfeng Liu, and Jianping Yu. Deep reinforcement learning for blockchain 519 optimization: A survey. _IEEE Internet of Things Journal_ , 7(5):3982–3995, 2020. 

- 520 [13] Tianyi Wang, Sheng Zheng, and Limin Sun. Reinforcement learning-based cryp521 tographic parameter optimization for blockchain security. _IEEE Transactions on_ 522 _Information Forensics and Security_ , 17:843–858, 2022. 

- 523 [14] Yifan Zhang, Mingxuan Han, and Qingwei Liu. Adaptive multi-agent reinforcement 524 learning for proof-of-stake blockchain optimization. _Journal of Cryptographic Engi-_ 525 _neering_ , 12(3):295–314, 2022. 

- 526 [15] Sunny King and Scott Nadal. Ppcoin: Peer-to-peer crypto-currency with proof-of527 stake. In _Bitcoin Forum_ , 2012. 

- 528 [16] Peter W. Shor. Algorithms for quantum computation: Discrete logarithms and factor529 ing. _Proceedings of the 35th Annual Symposium on Foundations of Computer Science_ , 530 pages 124–134, 1994. 

- 531 [17] Michele Mosca. Cybersecurity in an era with quantum computers: Will we be ready? 532 _IEEE Security & Privacy_ , 16(1):38–41, 2018. 

- 533 [18] Wei Dai, Tao Zhang, and Longfei Wu. Optimizing post-quantum cryptographic 534 schemes using swarm intelligence. _IEEE Transactions on Information Forensics and_ 535 _Security_ , 16:232–245, 2021. 

- 536 [19] Hao Wang, Sheng Zheng, and Limin Sun. Blockchain security enhancement using 537 hybrid cryptographic optimization. _ACM Transactions on Blockchain_ , 4(3):79–104, 538 2022. 

   - K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 18 of 19 

- 539 [20] Kassem Danach, Hussin Jose Hejase, Ahmad Faroukh, Hasan Fayyad-Kazan, and 540 Imad Moukadem. Assessing the impact of blockchain technology on financial reporting 541 and audit practices. _Asian Business Research_ , 9(1):30–50, 2024. 

- 541 

- 542 [21] Wei Dai, Ling Liu, and Yufei Tang. Intelligent smart contract optimization for 543 blockchain efficiency. _IEEE Transactions on Blockchain_ , 2:128–139, 2021. 

- 544 [22] Jian Wang, Xian Zhang, and Limin Sun. Reinforcement learning for smart contract 545 gas fee optimization in ethereum. _IEEE Transactions on Cloud Computing_ , 10(4):452– 546 467, 2022. 

- 547 [23] Zhen Li, Hao Chen, and Jun Wu. Optimizing smart contract execution using actor548 critic reinforcement learning. _ACM Transactions on Blockchain_ , 4(3):89–110, 2022. 

- 549 [24] Bo Yang, Yue Wang, and Chang Liu. Metaheuristic-based smart contract optimiza550 tion: A hybrid approach. _Journal of Computational Intelligence and AI in Blockchain_ , 551 8(2):104–127, 2023. 

- 552 [25] Yifan Zhang, Xin Zhang, and Jie Chen. Incentive mechanisms for cost-effective smart 553 contract execution in blockchain. _Journal of Financial Cryptography and Data Secu-_ 554 _rity_ , 11:312–334, 2023. 

- 555 [26] Anonymous Researchers. A blockchain-integrated chaotic fractal encryption scheme 556 for secure medical image transmission. _Scientific Reports_ , 15:89604, March 2025. 

- 557 [27] Everstake. Blockchain beyond 2024: Fully homomorphic encryption trends. 558 https://everstake.one/blog/blockchain-beyond-2024-trends-insights-and-predictions559 for-2025, 2025. Accessed: 2025-06-02. 

- 560 [28] Finextra Research. Layer 2 solutions and cryptographic optimization in 561 blockchain networks. https://www.finextra.com/blogposting/27701/blockchain-and562 crypto-trends-2025-further-integration-with-traditional-finance, 2025. Accessed: 563 2025-06-02. 

- 564 [29] Colton Dillion and Agustin Cruz. Quantum-resistant blockchain architectures: Opti565 mization strategies for post-quantum cryptography. Technical report, Quip Network, 566 2025. 

- 567 [30] Chien-Chih Chen and Wojciech Golab. A game theoretic analysis of validator strate568 gies in ethereum 2.0. _arXiv preprint arXiv:2405.03357_ , 2024. 569 [31] Wael Hosny Fouad Hosny Fouad Aly, Hassan Kanj, Nour Mostafa, Zakwan Al570 Arnaout, and Hassan Harb. No binding machine learning architecture for sdn con571 trollers. _Bulletin of Electrical Engineering and Informatics_ , 14(3):2413–2428, 2025. 

- 572 [32] Wael Hosny Fouad Aly, Hassan Kanj, Samer Alabed, Nour Mostafa, and Khaled 573 Safi. Dynamic feedback versus varna-based techniques for sdn controller placement 574 problems. _Electronics_ , 11(14):2273, 2022. 

- 575 [33] Hassan Kanj, Wael Hosny Fouad Aly, and Sawsan Kanj. A novel dynamic approach for 576 risk analysis and simulation using multi-agents model. _Applied Sciences_ , 12(10):5062, 577 2022. 

- 578 [34] Hassan Kanj, Ajla Kulaglic, Wael Hosny Fouad Aly, Mutaz AB Al-Tarawneh, Khaled 579 Safi, Sawsan Kanj, and Jean-Marie Flaus. Agent-based risk analysis model for road 580 transportation of dangerous goods. _Results in Engineering_ , 25:103944, 2025. 581 [35] Mutaz AB Al-Tarawneh, Hassan Kanj, and Wael Hosny Fouad Aly. An integrated 

K. Danach et al. / Eur. J. Pure Appl. Math, **18** (4) (2025), 6555 

19 of 19 

- 582 mcdm framework for trust-aware and fair task offloading in heterogeneous multi583 provider edge-fog-cloud systems. _Results in Engineering_ , page 105228, 2025. 

- 584 [36] Samer Alabed, Nour Mostafa, Wael Hosny Fouad Aly, and Mohammad Al-Rabayah. 585 A low complexity distributed differential scheme based on orthogonal space time 586 block coding for decode-and-forward wireless relay networks. _International Journal_ 587 _of Electrical & Computer Engineering (2088-8708)_ , 13(1), 2023. 

- 588 [37] Kassem Danach, Hassan Harb, Ameer Sardar Kwekha Rashid, Mutaz AB Al589 Tarawneh, and Wael Hosny Fouad Aly. Location planning techniques for inter590 net provider service unmanned aerial vehicles during crisis. _Results in Engineering_ , 591 25:103833, 2025. 

- 592 [38] Mutaz AB Al-Tarawneh, Omar Al-irr, Khaled S Al-Maaitah, Hassan Kanj, and Wael 593 Hosny Fouad Aly. Enhancing fake news detection with word embedding: A machine 594 learning and deep learning approach. _Computers_ , 13(9):239, 2024. 

- 595 [39] Khaled Safi, Wael Hosny Fouad Aly, Hassan Kanj, Tarek Khalifa, Mouna Ghedira, 596 and Emilie Hutin. Hidden markov model for parkinson’s disease patients using balance 597 control data. _Bioengineering_ , 11(1):88, 2024. 

- 598 [40] Ibrahim Mahariq, Ibrahim H Giden, Shadi Alboon, Wael Hosny Fouad Aly, Ahmed 599 Youssef, and Hamza Kurt. Investigation and analysis of acoustojets by spectral ele600 ment method. _Mathematics_ , 10(17):3145, 2022. 

