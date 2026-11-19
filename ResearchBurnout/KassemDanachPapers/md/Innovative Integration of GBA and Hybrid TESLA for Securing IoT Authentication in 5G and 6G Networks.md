

Received 8 September 2025, accepted 7 October 2025, date of publication 10 October 2025, date of current version 16 October 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3620017_ 

# Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication in 5G and 6G Networks 



<!-- Start of picture text -->
KHOULOUD ELEDLEBI 1, (Member, IEEE), DAVID KHOURY 2, (Member, IEEE),<br>SAMIR HADDAD 3, PATRICK SONDI 4, (Member, IEEE), HYERAN MUN 1,<br>KASSEM M. DANACH 5, (Member, IEEE), JINANE SAYAH 6,<br>ERNESTO DAMIANI 1, (Senior Member, IEEE), AND<br>CHAN YEOB YEUN 1, (Senior Member, IEEE)<br><!-- End of picture text -->

1Center for Secure Cyber-Physical Systems, Department of Computer Science, Khalifa University, Abu Dhabi, United Arab Emirates 

2Laboratoire d’Informatique Signal et Image de la Côte d’Opale (LISIC UR 4491), Université du Littoral Côte d’Opale, 59375 Calais, France 

3Department of Computer Science and Mathematics, Faculty of Arts and Sciences, University of Balamand, Koura 100, Lebanon 

4Center for Digital Systems, IMT Nord Europe, Institut Mines-Télécom, 59650 Lille, France 

5Basic and Applied Sciences Research Center, Al Maaref University, Beirut 1600, Lebanon 

6Department of Telecom and Networks, Issam Fares Faculty of Technology, University of Balamand, Koura 100, Lebanon 

Corresponding author: Chan Yeob Yeun (chan.yeun@ku.ac.ae) 

This work was supported in part by the Center for Cyber-Physical Systems (C2PS), Khalifa University; and in part by the Technology Innovation Institute (TII) under Grant 8434000386-TII-ATM-2035-2020. 

- **ABSTRACT** This paper presents a novel enhancement in the Hybrid TESLA protocol, integrating the Generic Bootstrapping Architecture (GBA) to replace public-key cryptography in the synchronization phase. The proposed protocol securely establishes communication between IoT devices and application servers without transmitting sensitive credentials over the network by leveraging GBA’s symmetric encryption and session key generation. Utilizing the existing mobile network infrastructure, GBA ensures secure authentication, making the protocol highly suitable for resource-constrained IoT environments. A simulation analysis conducted using Java demonstrated successful synchronization between clients and servers, with previous GBA experimental results confirming the protocol’s efficiency in terms of authentication time and power consumption. The Hybrid TESLA protocol’s use of SHA-2 and SHA-3 hashing functions ensures minimal computational demands while maintaining robust cybersecurity. This integration expands Hybrid TESLA’s utility in metaverse environments, enabling secure, seamless interactions across mobile networks. 

**INDEX TERMS** Constrained IoT, continuous authentication, GBA, hybrid TESLA, session key generation, symmetric encryption. 

## **I. INTRODUCTION** 

The Internet of Things (IoT) is a vast network of interconnected devices. These devices collect, transmit, and analyze data to streamline operations and improve efficiency. They also enhance user interactions with complex industrial systems. All IoT applications rely on continuous connectivity to function effectively. With the advent of mobile networks, 

The associate editor coordinating the review of this manuscript and approving it for publication was Binit Lukose . 

particularly 5G and the anticipated 6G, IoT devices have gained unprecedented capabilities. These include higher speed, improved reliability, and greater scalability. [1]. This evolution is crucial as the world moves towards more immersive and integrated digital environments, such as the metaverse. [2]. 

IoT devices utilize mobile networks to ensure seamless communication and data transfer across wide areas. Traditional connectivity methods like Wi-Fi or wired networks can be limited in range and flexibility, making mobile 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

176097 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



networks an ideal solution for devices operating in diverse or remote environments. The low latency and high throughput offered by 5G networks enable real-time data processing and decision-making, which is critical for many IoT applications. [1]. 

Constrained IoT devices are typically designed with limited computational power, memory, and energy resources, making them cost-effective and suitable for a variety of applications [3]. IoT devices that operate on mobile networks and utilize SIM/eSIM cards are designed to maintain connectivity in a wide range of environments [4], [5]. These IoT devices benefit from the widespread coverage of mobile networks. This coverage ensures they remain connected even in remote or mobile environments. Such connectivity is essential for real-time data transmission and control. Mobile networks provide an efficient means to offload data processing to cloud or edge servers, thereby conserving local resources of constrained IoT devices. 

Generic Bootstrapping Architecture (GBA) is a cybersecurity framework designed to facilitate secure authentication and key establishment between mobile devices (including constrained IoT devices) and application servers [6]. GBA is based on the authentication and key agreement (AKA) protocol used in network access authentication, and it can provide device authentication and support communication security at the transport layer [7]. It leverages the existing infrastructure of mobile networks, particularly the SIM/eSIM, which are already embedded in many IoT devices. GBA utilizes the network’s Home Subscriber Server (HSS) to authenticate IoT devices securely. It derives a shared session key between the device and the server. This process does not transmit sensitive credentials, such as private keys or authentication secrets, over the network. GBA integrates seamlessly with existing mobile networks, eliminating the need for additional infrastructure or costly upgrades. This makes it a cost-effective solution for IoT devices, particularly in large-scale deployments where managing the cybersecurity of individual devices can be challenging. The scalability of GBA makes it suitable for a wide range of IoT applications, from simple sensors to more complex devices. 

The SIM/eSIM in IoT devices provides robust cybersecurity features, including tamper resistance and secure key storage. This robustness facilitates the initial establishment and sharing of a secret key between the constrained IoT device and the HSS. [8]. Using GBA for authentication between IoT devices and new application servers offers several advantages. It integrates seamlessly with existing mobile networks, eliminating the need for additional infrastructure. This makes it cost-effective for IoT deployments. GBA also ensures that sensitive credentials, such as shared secrets or private keys, are never transmitted over the network. This significantly reduces the risk of interception or leakage. In addition, the framework offloads complex authentication tasks to the mobile network infrastructure. This is crucial for constrained devices with limited computational and energy resources. 

However, GBA faces several challenges. These include secure key management, which requires practices such as periodic key refreshment and secure storage. GBA is also vulnerable to cybersecurity threats like man-in-the-middle (MITM) and denial-of-service (DoS) attacks. To address these issues, we propose integrating GBA with the Hybrid TESLA protocol. This integration enhances GBA’s functionality and broadens the Hybrid TESLA protocol’s applicability in various IoT applications, including the metaverse. The Hybrid TESLA protocol is known for its strong defense against DoS and MITM attacks. It provides efficient key management through its disclosure time delay and multilevel keychains. It also enables unique user identification and continuous monitoring with low computational demands. [9]. By replacing public cryptography in Hybrid TESLA’s synchronization phase with GBA, we aim to create a fully symmetric protocol. This protocol uses GBA’s symmetric encryption and session key generation to enable secure communication between IoT devices and application servers. The session keys are not transmitted over the network during this process, thereby preserving sensitive credentials and enhancing security. It also expands Hybrid TESLA’s utility in metaverse environments. As a result, it facilitates seamless and secure interactions over mobile networks in diverse scenarios beyond traditional authentication or public cryptography. The contributions of the work are as follows: 

- 1- Utilizing SIM/eSIM Infrastructure for efficient bootstrapping and key establishment with no additional hardware. 

- 2- Expanding Hybrid TESLA’s Applicability by replacing PKI with GBA bootstrapping mechanism for a fully symmetric protocol. 

- 3- Mitigating GBA Cybersecurity Risks and reducing attack vulnerabilities with Hybrid TESLA integration. 

- 4- Enhancing IoT devices’ cybersecurity without Transmitting Sensitive Credentials. 

- 5- Reducing latency in device authentication and ensuring continuous authentication and device monitoring based on Hybrid TESLA properties. 

- 6- Enabling scalable and resilient authentication for 5G/6G IoT deployments by aligning with key requirements such as ultra-low latency, energy efficiency, loss tolerance, and secure integration with mobile network infrastructure. 

The paper is structured as follows: Section II reviews recent related work. Section III provides a brief explanation of the synchronization phase in the Hybrid TESLA protocol. Section IV details the proposed integration of GBA with the Hybrid TESLA protocol for the bootstrapping process. Section V presents the simulation analysis and the results obtained. Section VI discusses the cybersecurity analysis of the proposed protocol, and Section VII concludes the paper and outlines future work plans. 

176098 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



## **II. REVIEW OF RELATED WORK** 

Several methods are employed to authenticate constrained IoT devices over mobile networks, each with varying degrees of efficiency and cybersecurity. CoAP (Constrained Application Protocol) is a lightweight protocol specifically designed for constrained environments [10], [11]. Operating over UDP (User Datagram Protocol), CoAP offers functionality similar to HTTP but is optimized for low-bandwidth, lowenergy devices. Authentication in CoAP typically relies on pre-shared keys between the server and the IoT devices. Alternatively, token-based mechanisms can be used, where a token is exchanged with each request to verify the client’s authenticity. While efficient, transmitting cybersecurity credentials such as tokens can expose the system to cyberattacks, including masquerading or Man-in-the-Middle (MITM) attacks. 

TLS (Transport Layer Security) is a widely used protocol that ensures data confidentiality, integrity, and authenticity through digital certificates [12]. TLS supports both mutual authentication and server-side authentication. However, the computational overhead involved in TLS is significant, making it unsuitable for highly constrained devices due to the energy and processing resources required. DTLS (Datagram Transport Layer Security), a derivative of TLS, is adapted to fit the needs of constrained devices by operating over UDP rather than TCP [13]. DTLS can utilize digital certificates for authentication, but it can also employ lighter alternatives, such as CoAP or GBA, for a more resource-efficient approach. Despite these adaptations, DTLS still involves exchanging cybersecurity credentials and using pre-shared keys to establish secure sessions. The computational demands of DTLS, although lower than TLS, can still be burdensome for constrained devices, affecting their battery life and overall performance. Additionally, using CoAP and DTLS in lossy networks can lead to high latency, which is a significant challenge for constrained devices. The issue is especially critical in the emerging metaverse environment, where seamless connectivity is essential. 

Researchers have explored combining various authentication methods to enhance cybersecurity levels for IoT devices. One example is the proposed implementation of GBA over CoAP to secure communications for IoT devices. [8]. CoAP, being a lightweight protocol, is well-suited to the constraints of IoT devices, offering an efficient alternative to heavier protocols like HTTP. Integrating GBA with CoAP can establish a secure bootstrapping process, effectively minimizing overhead while ensuring robust device authentication. However, while CoAP is efficient, it does not offer the same resilience against certain cybersecurity threats as other lightweight protocols, such as the Hybrid TESLA protocol. Furthermore, adapting GBA for use with CoAP can introduce implementation challenges. This is especially true when maintaining compatibility with existing GBA infrastructure. These challenges may complicate the deployment in practical environments. 

In [14], GBA was integrated with CoAP and DTLS to provide a lightweight bootstrapping service, specifically adapted for IoT devices. This integration maps traditional GBA protocols to their IoT counterparts, making the bootstrapping process more efficient for constrained devices. The use of CoAP and DTLS in this context is an innovative approach. It enables a smooth transition to IoT-specific protocols while maintaining the core functionalities of GBA. However, while DTLS is lighter than TLS, it still demands significant resources, which is not ideal for highly constrained devices with limited computational and energy capabilities. Although the cybersecurity model is effective in many cases, it is not as resilient to more sophisticated attacks, such as MITM or DoS attacks, compared to protocols like Hybrid TESLA. This is due to the fact that key exchanges and initial setup are still exposed to the network, which introduces additional complexity and potential vulnerabilities. Additionally, while CoAP and DTLS are robust for securing datagram communications, they are not inherently optimized for mobile networks. These protocols have more general purposes and typically operate over the internet. On the other hand, GBA is designed to leverage the specific infrastructure of cellular networks, making it more suitable for mobile IoT devices. 

Blockchain technology has been explored to enhance the cybersecurity and efficiency of IoT devices. In [15], a novel authentication mechanism leverages blockchain to improve certificate management in constrained IoT environments. The system uses blockchain to manage the lifecycle of lightweight certificates, including their issuance, updates, and revocation. It also introduces Lightweight Elliptic Curve Qu-Vanstone (L-ECQV) implicit certificates, designed to minimize message overhead and energy consumption, making them suitable for resource-constrained devices. Smart contracts automate certificate processes, improving cybersecurity and efficiency by reducing manual interventions. However, while blockchain provides decentralization benefits, it can introduce latency and computational overhead, posing challenges for highly constrained IoT devices. Scalability is also a concern, especially as the number of IoT devices increases. The complexity of implementing blockchain and smart contracts may require additional resources and expertise, increasing deployment costs and time. 

In [16] blockchain was integrated with CoAP and DTLS to enhance cybersecurity in IoT environments. The study proposes using lightweight certificates instead of traditional X.509 certificates. These certificates are better suited for resource-constrained IoT devices to reduce computational and storage demands. Blockchain is employed to manage and verify the authenticity of these certificates, ensuring trust without relying on centralized Certificate Authorities. Additionally, the handshake protocol in DTLS was modified to streamline the authentication process. While these mechanisms offer cybersecurity and efficiency benefits, practical deployment raises concerns about implementation complexity, scalability, and compatibility. The added complexity may 

176099 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



pose challenges to deployment and maintenance, especially for constrained devices. Moreover, the system’s performance may degrade as the number of devices grows. 

The papers reviewed offer valuable insights into adapting various authentication protocols for constrained IoT environments. However, they often overlook broader cybersecurity needs and resource limitations. In contrast, the Hybrid TESLA protocol has proven resilient against cyberattacks by avoiding the transmission of cybersecurity credentials over the network [9]. It ensures strong protection in lossy environments, effectively maintaining connections and recovering lost packets even under challenging conditions [17]. Additionally, it provides continuous, real-time authentication of IoT devices, aligning with the zero-trust approach [18]. This makes Hybrid TESLA a strong candidate for secure, lowlatency communication in constrained IoT devices, especially as demand for reliable protocols grows in the metaverse and other advanced applications. 

Furthermore, the GBA mechanism is well-suited for securing IoT devices with minimal computational power. By leveraging existing mobile infrastructure, GBA reduces the need for additional resources and processing on IoT devices. This is unlike CoAP, DTLS, or Blockchain, which require more cybersecurity management and higher resource usage. GBA also centralizes key management with mobile network operators. This reduces complexity for IoT manufacturers and ensures that sensitive credentials are not exposed. These advantages help in making the Hybrid TESLA protocol fully symmetric for mobile IoT devices, broadening its applicability across various use cases. 

While Hybrid TLI- _µ_ TESLA and GBA have been individually studied, their integration for fully symmetric IoT bootstrapping remains novel. Therefore, combining GBA with Hybrid TESLA offers a balanced solution, merging the strengths of both protocols. This integration ensures secure, scalable, and efficient authentication tailored to the specific needs of constrained IoT devices, especially in emerging environments like the metaverse. 

## **III. OVERVIEW OF HYBRID TESLA PROTOCOL** 

Lightweight cryptographic protocols have been developed to address the growing cybersecurity needs of resource-constrained IoT devices [13], [19], [20]. These protocols are specifically designed to minimize computational complexity, making them ideal for IoT systems with limited processing power and energy resources [21], [22]. They ensure essential cybersecurity functions while effectively managing the constraints of such devices. One prominent method for lightweight broadcast authentication is the timed-efficient stream loss-tolerant authentication (TESLA) protocol, which ensures confidentiality, integrity, and user authentication [23], [24]. TESLA achieves this by integrating robust cryptographic functions while minimizing communication and computational overhead, which is crucial for resource-limited IoT devices. Variants of TESLA, such as the newly developed Hybrid TLI- _µ_ TESLA protocol, use 

symmetric cryptography, employing symmetric keys to authorize broadcasted packets and generate MAC values to verify packet integrity [9], [23]. 

During the synchronization phase, TESLA protocols rely on asymmetric cryptography to securely transmit key parameters, such as the commitment key and disclosure time delay, which are essential for preserving symmetric keys [25], [26]. However, asymmetric cryptography presents challenges, including the need for computationally intensive operations that can deplete the energy resources of lightweight devices [27], [28]. Additionally, it remains vulnerable to attacks such as MITM, replay attacks, and brute-force attacks, which can undermine its cybersecurity [29], [30]. In our previous work, we made the Hybrid TESLA protocol fully symmetric by integrating biometric authentication using distorted fingerprint and EEG templates to establish a non-shared symmetric session key during the synchronization phase [31]. This approach successfully ensured synchronization, privacy preservation, and low computational demands, marking a significant advancement in IoT authentication. We propose integrating GBA during the synchronization phase to further expand the Hybrid TESLA protocol’s applicability in mobile IoT devices. By leveraging existing mobile network infrastructure, GBA will establish a secure, non-shared symmetric key to serve as the session key for transmitting essential Hybrid TESLA credentials. This process will occur only once during synchronization, significantly reducing the computational load on IoT devices. 

Before exploring the implementation of GBA for generating a secret shared session key between the client and server, it is essential to understand the synchronization process established between them using TESLA protocols. This synchronization is achieved through the use of digital signatures, which not only initiate the new client but also determine the upper synchronization bound. [23]. The synchronization process is critical for exchanging key parameters between the communicating parties. 

The synchronization process begins when the client sends a request to the server. This request includes the receiver’s transmission time ( _TR_ ) and a challenging nonce value, structured as follows: 



<!-- Start of picture text -->
Request :( TR, nonce ) (1)<br><!-- End of picture text -->

Upon receiving the request from the client, the server proceeds by recording the time of message reception ( _TS_ ). Subsequently, the server generates a new message that incorporates the challenged nonce, the received time ( _TS_ ), and crucial configuration information, such as the commitment key ( _K_ 0), time delay ( _d_ ), and salt values ( _S_ ). This message is then signed using the server’s private key ( _Kp_ ). The structure of this message is as follows: 



<!-- Start of picture text -->
Response :  (TS , nonce, K 0 , d, S) Kp (2)<br><!-- End of picture text -->

When the client receives the server’s message, it records the reception time (t). The client then uses the server’s public key ( _KP_ ) to decrypt the message and verify the nonce. The 

176100 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



values of _TR_ and _TS_ received from the server are saved, and the client calculates the upper synchronization bound using the following formula: 

_Upper Synchronization Bound_ = _t_ − _TR_ + _TS_ (3) 

Understanding these synchronization bounds allows the client to estimate the maximum allowable time window within which it can expect a packet from the server. If the waiting time exceeds this upper bound, the connection is terminated, necessitating a new synchronization process to protect against potential MITM attacks. FIGURE illustrates the synchronization process initiated between the sender and receiver to implement the TESLA protocol [32]. 



**FIGURE 1.** Initial synchronization between sender and receiver in the first stage of all TESLA protocol variants for exchanging key parameters. 

## **IV. PROPOSED SYNCHRONIZATION PHASE OF HYBRID TESLA PROTOCOL USING GBA** 

As previously mentioned, digital signatures rely on public key cryptography, which is computationally heavy and demands significant energy from devices. [33]. This is particularly challenging for resource-constrained IoT devices, which have limited processing power and battery life. By replacing public key cryptography with symmetric cryptography for synchronization, we can significantly improve the efficiency and battery life of these devices, particularly when continuous monitoring is necessary. However, the main challenge in symmetric cryptography is managing key distribution and ensuring secure key management. [34], [35]. A secure method must be established to allow the client and server to agree on a symmetric key without exposing it to cybersecurity risks. A highly secure process must also transmit critical TESLA protocol parameters from the server to the client. 

We propose integrating GBA as a bridge between the client and server to address these challenges. This approach serves multiple purposes: it provides user authentication, generates a non-shared secure symmetric session key between the parties, and facilitates the secure transfer of crucial protocol parameters from the sender to the receiver, all without relying on Public Key Infrastructure. It also enables the applicability of the Hybrid TESLA protocol to be implemented with Mobile networks while achieving a highly secure channel and a continuous authentication mechanism. 

Generic Bootstrapping Architecture (GBA), standardized by the 3rd Generation Partnership Project (3GPP), facilitates client and server authentication using the existing mobile network operator infrastructure. [6]. Designed for constrained IoT devices with limited processing power, memory, and battery life, GBA’s lightweight authentication mechanism significantly reduces these devices’ computational, and energy demands by offloading cryptographic operations to the mobile network infrastructure. This is especially advantageous for devices that need to function efficiently over extended periods with minimal power consumption. A key benefit of GBA is that sensitive credentials or keys are never transmitted over the network. Instead, the IoT device and the application server independently derive the session key through the secure mobile network infrastructure, minimizing the risk of interception or leakage and enhancing cybersecurity in untrusted environments. GBA also leverages the inherent cybersecurity features of SIM/eSIM technology, such as tamper-resistant storage and secure key management, eliminating the need for complex cybersecurity implementations within the IoT device [8] This ensures high trust and cybersecurity without requiring additional hardware or infrastructure, making it ideal for resource-constrained IoT deployments. It should be noted that the GBA requires IP connectivity and does not necessarily need to be executed over 3GPP access. Figure 2 illustrates the high-level system architecture scenario of GBA. It is worth noting that GBA requires IP connectivity and does not necessarily need to be executed over 3GPP access. 



**FIGURE 2.** High-level system architecture of GBA framework illustrating the secure interaction between a user device with 3GPP credentials and network entities. 

The main components of GBA are: 

1) User Identity Card (UICC) or Embedded User Identity Card (eUICC), Which are Referred to as SIM/eSIM. 

2) Home Subscriber Server (HSS): The network database that stores the permanent credentials of the IoT device, such as the secret keys associated with the SIM/eSIM card. 

3) The Network Application Function (NAF) is a module that forms the server-side authentication function. 

4) Bootstrapping Server Function (BSF): A network entity that facilitates the bootstrapping process and communicates with the HSS to authenticate the IoT device. 

176101 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



NAF and BSF can function as software modules within the Hybrid TESLA server, interfacing with the HSS inside the mobile network, and serving as authentication servers for IoT devices. Since the GBA authentication process involves only a few HTTP messages, using full HTTP client libraries is often unnecessary. Instead, these messages can be manually crafted and sent directly over TCP, reducing the memory overhead associated with a full HTTP stack. The plaintext nature of the HTTP/1.1 protocol ensures compatibility with various constrained devices, regardless of their hardware and software limitations. A permanent secret key shared between the UICC, and the mobile network operator is used to generate a time-limited main key (Ks), which is shared between the User Equipment (UE) and the Bootstrapping Server Function (BSF). The BSF then derives a session-specific key (KsNAF) for the Network Application Function (NAF), facilitating mutual authentication and secure communication between the UE and NAF. In our proposal, the NAF will be linked with the Hybrid TESLA protocol to initiate the secure communication channel and transmission of packets as described in details in [9]. 

This process involves several steps, as illustrated in Figure 3. Each step is numbered and explained as follows: 



**FIGURE 3.** GBA authentication process between user device (registered in the HSS) and NAF server imbedded with Hybrid TESLA Protocol [36]. 

1. The IoT device sends an HTTP request to the NAF **(1)** . 2. The NAF responds with a message prompting the IoT device to initiate the bootstrapping process with the BSF **(2)** . 

3. The device contacts the BSF with its temporary identity as a parameter in 4G **(3)** . In 5G, the user’s permanent Subscription Permanent Identifier (SUPI) is used and sent encrypted. 

4. The BSF forwards the device’s authentication request to the HSS, requesting verification of the SIM/eSIM credentials **(4)** . 

5. The HSS generates an authentication challenge, which includes a random nonce number (RAND), an authentication token (AUTN) performed through Message Authentication 

Code (MAC), and an expected response (XRES). This challenge is sent back to the BSF **(5)** . 

6. The BSF forwards AUTN and RAND to the device based on its credentials **(6)** . 

7. The device calculates the response to the challenge using its secret key from the eSIM/SIM, RAND, and AUTN and sends it to BSF through an HTTP request **(7)** . 

8. The BSF authenticates the device by verifying the response using the 3GPP AKA protocol. Through this process, the BSF confirms the device’s 3GPP subscription, as the SIM/eSIM card resides within the device. Therefore, the successful authentication of the SIM/eSIM implies the device’s authentication. This mutual authentication between the SIM/eSIM and the network results in the independent generation of a session key (Ks) at both the device and the BSF. This session key (Ks) is then used to secure communication between the device and the BSF. 

9. The BSF returns a Bootstrapping Transaction Identifier (BTID) to the device linked with Ks **(8)** . 

10. The BSF derives an NAF-specific key (KsNAF) from Ks using a Key Derivative Function (KDF) and links it with BTID. Usually, there is a table that links the KsNAF with an encrypted BTID using the same key for later steps. 

11. The device derives a session-specific key (KsNAF) using the BTID to be linked together. 

12. The device sends an HTTP request to the NAF, including the BTID encrypted with KsNAF and a MAC challenge **(9)** . 

13. The NAF requests the corresponding session key (KsNAF) from the BSF using the device’s encrypted BTID **(10)** . 

14. The BSF checks the encrypted BTID against the table and maps it with the corresponding KsNAF. It then communicates securely to the NAF (encrypt it with a secret key shared between BSF and NAF). Note that a secure channel between the NAF and the BSF is a precondition for GBA, as explained in Section V **(11)** . 

15. The NAF retrieves the KsNAF. It checks the MAC number associated with the device challenge message and responds to the device with a confirmation message, indicating readiness for secure data transmission using KsNAF **(12)** . 

Figure 4 illustrates a typical configuration of a hybrid TESLA-GBA network. The NAF and the BSF may operate as software modules within a manager node, cluster node, or gateway for multiple sensors or wireless sensor networks (WSNs). The manager node, containing the NAF and BSF, interfaces with the Home Subscriber Server (HSS). Constrained devices may connect to the Internet or an enterprise intranet through a 3GPP gateway (GW). The NAF (Network Authentication Function) will be integrated with the Hybrid TESLA protocol to authenticate users and establish a secure channel for packet transmission between the user and the application server. 

After establishing a secure connection using the session key _KsNAF_ [32] with the GBA, the IoT device 

176102 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 





**FIGURE 4.** Proposed GBA-Hybrid TESLA scenario illustrating the authentication configuration of the GBA-TESLA network to establish a secure connection between the parties. 



**FIGURE 5.** Simulation result illustrates the exchange of messages transferred from and to the client during the GBA-Hybrid TESLA synchronization phase. 



**FIGURE 6.** Simulation result illustrates the exchange of messages transferred from and to the NAF server during the GBA-Hybrid TESLA synchronization phase. 

and the Hybrid-TESLA server securely exchange TESLA parameters, such as the commitment key, disclosure delay, salt values, and keychain length. Once this exchange is complete, _KsNAF_ is no longer used, and the Hybrid TESLA protocol takes over, ensuring continuous authentication and monitoring through communication between the IoT device and the server. The Hybrid TESLA protocol provides robust 



**FIGURE 7.** The simulation result illustrates the exchange of messages transferred between the BSF and the BS during the GBA-Hybrid TESLA synchronization phase. 



**FIGURE 8.** Simulation result illustrates the exchange of messages transferred from and to the HSS during the GBA-Hybrid TESLA synchronization phase. 

authentication and monitoring independent of the mobile network, making it particularly suitable for resource-constrained IoT environments. The integration of GBA enhances cybersecurity and simplifies the initial setup process, thereby increasing the protocol’s applicability and efficiency across various IoT ecosystems. 

The hybrid TESLA-GBA system integrates the GBA protocol. [37] with TESLA. The primary objective of GBA is to establish symmetric encryption and session key generation capabilities during the TESLA synchronization phase, rather than relying on public key encryption. By utilizing the existing mobile network infrastructure, GBA ensures secure authentication, making the protocol highly suitable for resource-constrained IoT environments [3], [4], [5], [6]. This integration enhances the utility of Hybrid TESLA in metaverse environments, enabling secure and seamless interactions across mobile networks [2] 

Scalability: The mobile network’s structure offers scalability for mobile devices, with IoT devices categorized as User Equipment (UE) in 3GPP. It is well established in the literature that GBA is highly scalable, as it relies on the mobile network, and the BSF is a component of this network. Its capacity can be increased, or more BSF nodes can be added seamlessly. 

176103 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



## **V. SIMULATION ANALYSIS AND RESULTS DISCUSSION** 

We performed a comprehensive simulation analysis using Java to evaluate the integration of GBA authentication into the Hybrid TESLA protocol for bootstrapping and generating the non-shared session key. ( _KsNAF_ ). In our setup, a typical scenario involved a client (device) initiating a connection request with an application server (NAF), BSF, and HSS, facilitating the secure transmission of encrypted messages through the GBA-Hybrid TESLA protocol. 

The simulation was conducted on a Windows 11 Enterprise system with an Intel Core i5-1145G7 processor at 2.60 GHz (1.50 GHz base frequency) and 16 GB of RAM. We developed the Java code using IntelliJ IDEA version 2022.1.1, incorporating libraries essential for pairing and symmetric encryption/decryption. The cryptographic libraries support symmetric encryption and hashing (SHA-2 and SHA-3), which were applied during session key derivation and TESLA parameter exchanges. Key handling in Java memory was performed within the Java runtime environment. The disclosure time delay was set to two interval durations, and the UDP buffer size was configured to 1024 bits. Each operation was executed 50 times, with the average results calculated to ensure accuracy and reliability. 

Fig.s 5 through 8 present screenshots showcasing the successful establishment of a symmetric session key between the client and application server, using BSF and HSS, as outlined in Section IV. This process is achieved without the explicit transmission of the _KsNAF_ Key over the network or the sharing of sensitive credentials. The established session key facilitates the secure transmission of critical Hybrid TESLA protocol parameters and ensures the continuation of the authentication process. 

Considering the limitations of IoT devices, it is essential to track both power consumption and the time required for successful synchronization using the GBA-Hybrid TESLA protocol. Therefore, we referred to the comprehensive analysis of the GBA authentication process that is presented in [6], where experimental evaluations were conducted to assess GBA implementation against standard 3GPP BSF and NAF interfaces, utilizing Ericsson’s public servers. The experiments used an Arduino Mega board with an Ethernet shield for internet connectivity. This board features an 8- bit ATmega2560 microprocessor, 8 KB of RAM, 4 KB of EEPROM, and 256 KB of flash memory. Power consumption was measured using a Monsoon Power Monitor connected via USB passthrough mode, with readings logged to a workstation. Each test was repeated 15 times, and average values were calculated to ensure accuracy. 

The results demonstrated that the device could securely authenticate with an application server in under 1.5 seconds, using less than 8 KB of memory and consuming approximately 70 millijoules of energy. These findings emphasize the protocol’s efficiency, making it well-suited for resourceconstrained IoT devices by ensuring secure authentication with minimal computational and energy requirements. The experimental results are shown in Table 1 

**TABLE 1.** Time and power consumption analysis of GBA experiment [6]. 



We conducted a comprehensive comparative analysis between the proposed GBA-Hybrid TESLA protocol, our prior work on Hybrid TLI- _µ_ TESLA, and the state-of-the-art authentication protocols previously discussed in Section II. The comparison involves: computational complexity, energy efficiency, latency and loss tolerance, credential exposure risk, and compatibility with mobile network infrastructure. Moreover, we referred to the complexity analysis, energy consumption and latency performance of the Hybrid TESLA protocol from [9]. 

Each scheme shown in Tables 2 and 3 was evaluated based on its cryptographic operations (e.g., symmetric vs. asymmetric), protocol handshake mechanisms, resilience under packet loss and delay, and ability to leverage mobile-specific features, such as SIM/eSIM-based authentication and integration with 3GPP core functions like the HSS and BSF. 

Our results demonstrate that the GBA-Hybrid TESLA protocol significantly improves all key dimensions. It eliminates the computational overhead of public-key operations through a fully symmetric design, maintains robust security by never transmitting sensitive credentials, and is optimized for mobile networks by natively supporting SIM/eSIMbased bootstrapping. Compared to Hybrid TLI- _µ_ TESLA, the GBA-Hybrid TESLA reduces synchronization cost and improves deployment feasibility in real-world cellular IoT scenarios. These advantages position our protocol as a highly secure, lightweight, and mobile-network-compliant solution, particularly suited for resource-constrained IoT devices operating in latency-sensitive and lossy environments, such as smart cities, metaverse platforms, and next-generation cyberphysical systems. 

Furthermore, simulation results of the Hybrid TESLA protocol discussed in [9] Highlighted its minimal authentication time for packets and keychain and MAC generation time during communication between the client and server, even when using SHA-2 and SHA-3 hashing functions. Additionally, the proposed protocol’s capability to support large key lengths and implement SHA-3 without increasing computational demands gives it an advantage over other protocols. This makes it ideal for enhancing network lifetime and performance, especially in the context of 5G and 6G IoT applications. 

If the handshake fails during bootstrapping (e.g., due to a loss of connectivity or a timeout), the UE or IoT device cannot derive the shared key (KsNAF), and the session is 

176104 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



**TABLE 2.** Comparative analysis between GBA-Hybrid TESLA and other related work – part 1. 



terminated. Without a successful handshake, the UE and NAF cannot establish secure communication. Any service requiring GBA-derived credentials will be denied or deferred. To avoid handshaking failure, most implementations include exponential backoff and retry timers to reattempt the bootstrapping process. Retries may be limited to prevent draining the battery or overwhelming the network for constrained IoT devices. 

In the intermittent connectivity scenario, UEs often maintain a partial state (e.g., nonce or transaction ID) to resume the handshake when connectivity is restored [38]. If the UE has previously bootstrapped with the same BSF, it may reuse cached KsNAF if it is still valid. This process avoids a full re-handshake and is particularly useful in cases of intermittent connectivity. Further enhancements to the handshaking failure for constrained IoT devices will be discussed later in Section VII. Table 4 

**TABLE 3.** Comparative analysis between GBA-Hybrid TESLA and other related work – part 2. 



summarizes the key features of the proposed GBA-Hybrid TESLA protocol. 

## **VI. CYBERSECURITY ANALYSIS OF THE SYMMETRIC SESSION KEY GENERATION** 

In this section, we assessed the robustness of the proposed GBA-Hybrid TESLA protocol against several common attacks, such as brute-force, Man-in-the-Middle (MITM) attacks, Advanced Persistent Threats (APTs), side-channel attacks, and Denial-of-Service (DoS) attacks that involve message replay. We also focused on the computational demands of integrating GBA authentication into the protocol, ensuring that it remains practical for resource-constrained devices. We also highlighted key cybersecurity features achieved through the protocol, such as robust entity authentication, effective identity management, integrity verification, and data confidentiality. 

When implementing GBA authentication, we carefully considered the potential risks of data breaches, especially those involving server databases. A key concern was the exposure of credential information tied to the SIM/eSIM and shared with HSS. Such breaches could seriously compromise user privacy by revealing sensitive data that attackers could exploit. To address this, our protocol prevents the storage or transmission of critical SIM/eSIM credentials. Instead, GBA securely derives session keys in real time, ensuring stronger privacy and reducing the risk of unauthorized access or credential leakage. Furthermore, the BSF, NAF, and HSS are high-capacity servers, and their communication is always conducted over secure channels such as TLS or SSL. Before exchanging messages, the BSF and NAF authenticate each other—often using digital certificates- to prevent MITM 

176105 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



**TABLE 4.** Features of the hybrid TESLA-GBA protocol. 



attacks. The BSF also ensures that only authorized NAFs are granted access to the session key KsNAF, minimizing unauthorized use. 

When analyzing the message exchanges between the IoT device, NAF, and BSF, we evaluated possible risks and referenced messages by their numbering in Fig. 3. The device’s initial HTTPS request to the NAF (1) carries no sensitive information and merely initiates secure communication. Similarly, the NAF’s response (2) does not expose confidential data. However, during the bootstrapping request sent from the device to the BSF in 4G networks (3), the device must present its identity for authentication against the BSF and HSS. Two types of identities are possible: the International Mobile Subscriber Identity (IMSI) and the Temporary Mobile Subscriber Identity (TMSI). The IMSI, a unique SIM/eSIM identifier, if exposed, could allow attackers to track users or launch impersonation attacks. To reduce this risk, IMSI transmission is generally avoided unless the channel is highly secure. Instead, the TMSI—assigned by the Mobile Management Entity (MME)—is typically used. Unlike IMSI, the TMSI does not reveal permanent subscriber details. The HSS can map the TMSI back to the IMSI when needed, preserving 

the device’s privacy and preventing tracking or impersonation. In 5G networks, the Subscription Permanent Identifier (SUPI) is encrypted during transmission using a shared key set up during SIM/eSIM registration with the BSF and HSS, which ensures stronger confidentiality and privacy in modern systems. 

The challenge message from the BSF to the device (6) contains a random nonce (RAND) and an authentication token (AUTN). These are random values that do not disclose any sensitive keys or session information. Even if intercepted, they cannot be used to reconstruct the session key because additional elements—such as the secret key on the SIM/eSIM, the HSS’s key, and the Bootstrapping Transaction Identifier (BTID)—are required, with the BTID never transmitted directly. The use of RAND also prevents replay attacks by ensuring each challenge is unique to the session, thereby mitigating denial-of-service attempts. The response from the device to the BSF (7) includes a computed value that the HSS can verify using the user’s identity, RAND, and AUTN. This value does not reveal the device’s identity or keys, preserving security throughout the exchange. 

When the BSF sends the BTID to the device (8), it is encrypted using a secret key established during device registration. MAC is also included to verify the integrity and confirm the authenticity of the BTID. In the subsequent device-to-NAF request (9), the BTID is encrypted again, this time using the session key KsNAF, ensuring both the device and the NAF rely on the same key. This process prevents MITM attacks and confirms that the NAF has received the session key from the BSF (12). Importantly, the session key itself is never transmitted over the network; both the device and the NAF generate it independently in real-time. This design preserves the confidentiality of critical credentials, reinforcing the security of the GBA authentication process. 

In the unlikely event that the BTID is compromised, it does not, by itself, grant access to sensitive information or the ability to forge authentication. Specifically, even if an eavesdropper intercepts the BTID, they cannot derive the session key or perform any attacks unless they also possess other critical information, such as the secret keys used during the authentication process. Since these key elements are not transmitted over the network, they remain secure, making it highly difficult for attackers to breach the system. 

The cybersecurity performance of the Hybrid TESLA Protocol has been demonstrated to provide a secure, low-cost solution for client-server communication. [17]. It enables immediate authentication of transmitted packets with minimal computational overhead while significantly enhancing cybersecurity. The protocol employs three keychains operating at different hierarchical and alternating levels, making it highly resilient to brute-force attacks. The likelihood of an attacker successfully compromising all three keychains within short time intervals is extremely low. The 

176106 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



Hybrid TLI- _µ_ TESLA protocol improves time complexity, extending the network’s lifespan compared to other TESLA variants. It ensures continuous authentication and synchronization between sender and receiver, reducing the need for energy-draining re-synchronizations. Additionally, the protocol supports longer key lengths to resist quantum attacks without imposing a computational burden on the receiver. Its design also includes strict criteria that prevent packet alteration or addition within the disclosure delay, enhancing resistance to Modification and Replay attacks. By incorporating the SHA-3 hash function and supporting large key lengths without increasing computational demands, the Hybrid TESLA Protocol surpasses other TESLA variants. This makes it highly suitable for 5G and 6G IoT networks, offering improved network longevity and performance. 

## **VII. CONCLUSION** 

In this paper, we propose a novel enhancement to the Hybrid TESLA protocol by integrating it with the Generic Bootstrapping Architecture (GBA), replacing the asymmetric synchronization phase with a fully symmetric, SIM/eSIM-based key establishment mechanism. The resulting GBA-Hybrid TESLA protocol leverages existing 3GPP mobile network infrastructure, including the BSF and HSS, to derive session keys securely without transmitting private keys or sensitive credentials over the network. This integration enables strong mutual authentication between constrained IoT devices and application servers, while maintaining compatibility with cellular networks and avoiding the need for additional infrastructure or digital certificates. 

We performed a simulation analysis using Java, which successfully demonstrated synchronization between a client and server using the GBA process embedded within the Hybrid TESLA protocol. We also conducted a detailed comparative analysis against a range of existing protocols, including CoAP, DTLS, TLS, blockchain-based systems, and our prior Hybrid TLI- _µ_ TESLA. The GBA-Hybrid TESLA protocol consistently outperformed these alternatives across key dimensions: low computational complexity, reduced energy consumption, minimal latency, strong resilience to packet loss, and high compatibility with mobile network infrastructure. In contrast to traditional public-key–based approaches, the proposed protocol ensures robust, continuous authentication through lightweight symmetric operations. 

Additionally, we referenced prior experimental results on GBA authentication, which showed that authentication time and power consumption were minimal, making it suitable for constrained IoT devices. Previous simulations of the Hybrid TESLA protocol also indicated that it achieves immediate and continuous authentication with low time and energy consumption for generating necessary cybersecurity parameters, even when using SHA-2 and SHA-3 hashing functions, without increasing computational demands on constrained devices. The proposed integration of GBA with the Hybrid TESLA protocol enhances security and 

efficiency for constrained IoT devices. It also aligns closely with emerging trends in IoT, 5G/6G networks, edge computing, and cyber-physical systems. By leveraging existing mobile infrastructure and lightweight symmetric operations, the protocol provides a practical and scalable solution. It supports continuous, real-time authentication, which is essential for future metaverse applications and other latency-sensitive, distributed environments. 

In future work, we plan to extend the current simulations to multi-client and multi-server scenarios to evaluate scalability and performance under realistic network loads. Experimental validation on physical IoT devices will further assess energy consumption, latency, and resilience to packet loss, refining the protocol for real-world deployments. We plan to investigate the use of session caching, which will minimize the need for repeated bootstrapping and handshake operations. We also plan to explore connectivity-aware bootstrapping, where the protocol is triggered only when network conditions meet predefined quality thresholds. This strategy prevents unnecessary energy expenditure during weak or unstable connections, making the solution more adaptive to dynamic mobile and edge computing environments. 

We also aim to explore the integration of GBA-Hybrid TESLA within edge and cloud-assisted architectures, assessing its compatibility with distributed computing frameworks and resource-constrained environments. This will include evaluating performance under heterogeneous network conditions, varying device capabilities, and mixed 5G/6G infrastructures. Furthermore, we plan to investigate advanced security scenarios, including resistance to emerging threats in cyber-physical and metaverse applications. This includes formal verification, penetration testing, and adaptive key management strategies to ensure robust authentication even in highly dynamic and potentially adversarial environments. 

## **REFERENCES** 

- [1] V. A. Thakor, M. A. Razzaque, and M. R. A. Khandaker, ‘‘Lightweight cryptography for IoT: A State-of-the-art,’’ 2020, _arXiv:2006.13813_ . 

- [2] L.-H. Lee, T. Braud, P. Zhou, L. Wang, D. Xu, Z. Lin, A. Kumar, C. Bermejo, and P. Hui, ‘‘All one needs to know about metaverse: A complete survey on technological singularity, virtual ecosystem, and research agenda,’’ 2021, _arXiv:2110.05352_ . 

- [3] A. Rizzardi, S. Sicari, and A. Coen-Porisini, ‘‘Analysis on functionalities and security features of Internet of Things related protocols,’’ _Wireless Netw._ , vol. 28, no. 7, pp. 2857–2887, Oct. 2022, doi: 10.1007/s11276-02202999-7. 

- [4] F. Pereira, R. Correia, P. Pinho, S. I. Lopes, and N. B. Carvalho, ‘‘Challenges in resource-constrained IoT devices: Energy and communication as critical success factors for future IoT deployment,’’ _Sensors_ , vol. 20, p. 6420, Nov. 2020, doi: 10.3390/s20226420. 

- [5] M. Sethi, V. Lehtovirta, and P. Salmela, ‘‘Using generic bootstrapping architecture with constrained devices,’’ _Internet-Draft_ , vol. 1, pp. 1–18, Feb. 2014. 

- [6] M. Sethi, P. Kortoci, M. Di Francesco, and T. Aura, ‘‘Secure and low-power authentication for resource-constrained devices,’’ in _Proc. 5th Int. Conf. Internet Things (IoT)_ , Oct. 2015, pp. 30–36, doi: 10.1109/iot.2015.7356545. 

- [7] (2025). _GSMA IoT Security Guidelines | Internet of Things_ . Accessed: Jan. 17, 2025. [Online]. Available: https://www.gsma.com/solutionsand-impact/technologies/internet-of-things/iot-security/iot-securityguidelines/ 

176107 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



- [8] _Generic Bootstrapping Architecture (GBA) Based Security Over Constrained Application Protocol (CoAP) for IoT Devices_ , Ericsson, Stockholm, Sweden, Feb. 2019. 

- [9] K. Eledlebi, A. A. Alzubaidi, C. Yeob Yeun, E. Damiani, V. Mateu, and Y. Al-Hammadi, ‘‘Simulation analysis and comparison of new hybrid TLI- _µ_ TESLA and variant TESLA protocols using SHA-2 and SHA3 hash functions,’’ _Sensors_ , vol. 22, no. 23, p. 9063, Nov. 2022, doi: 10.3390/s22239063. 

- [10] S. Raza, H. Shafagh, K. Hewage, R. Hummen, and T. Voigt, ‘‘Lithe: Lightweight secure CoAP for the Internet of Things,’’ _IEEE Sensors J._ , vol. 13, no. 10, pp. 3711–3720, Oct. 2013, doi: 10.1109/JSEN.2013.2277656. 

- [11] Y. Chen and T. Kunz, ‘‘Performance evaluation of IoT protocols under a constrained wireless access network,’’ in _Proc. Int. Conf. Sel. Topics Mobile Wireless Netw. (MoWNeT)_ , Apr. 2016, pp. 1–7, doi: 10.1109/MoWNet.2016.7496622. 

- [12] Y. Sheffer, P. Saint-Andre, and T. Fossati, ‘‘Recommendations for secure use of transport layer security (TLS) and datagram transport layer security (DTLS),’’ Internet Eng. Task Force (IETF), USA, Tech. Rep. RFC9325, Nov. 2022, doi: 10.17487/RFC9325. 

- [13] M. Goworko and J. Wytre¸bowicz, ‘‘A secure communication system for constrained IoT devices-experiences and recommendations,’’ _Sensors_ , vol. 21, no. 20, p. 6906, Oct. 2021, doi: 10.3390/s21206906. 

- [14] D. Garcia-Carrillo and R. Marin-Lopez, ‘‘Lightweight CoAP-based bootstrapping service for the Internet of Things,’’ _Sensors_ , vol. 16, no. 3, p. 358, Mar. 2016, doi: 10.3390/s16030358. 

- [15] A. Garba, D. Khoury, P. Balian, S. Haddad, J. Sayah, Z. Chen, Z. Guan, H. Hamdan, J. Charafeddine, and K. Al-Mutib, ‘‘LightCert4IoTs: Blockchain-based lightweight certificates authentication for IoT applications,’’ _IEEE Access_ , vol. 11, pp. 28370–28383, 2023, doi: 10.1109/ACCESS.2023.3259068. 

- [16] D. Khoury, S. Haddad, P. Sondi, P. Balian, H. Harb, K. Danach, J. Merhej, and J. Sayah, ‘‘CoAP/DTLS protocols in IoT based on blockchain light certificate,’’ _IoT_ , vol. 6, no. 1, p. 4, Jan. 2025, doi: 10.3390/iot6010004. 

- [17] K. Eledlebi, A. Alzubaidi, E. Damiani, V. Mateu, Y. Al-Hammadi, D. Puthal, and C. Y. Yeun, ‘‘Comparative study of novel packet loss analysis and recovery capability between hybrid TLI- _µ_ TESLA and other variant TESLA protocols,’’ _Ad Hoc Netw._ , vol. 163, Oct. 2024, Art. no. 103579, doi: 10.1016/j.adhoc.2024.103579. 

- [18] K. Eledlebi, A. A. Alzubaidi, C. Y. Yeun, E. Damiani, V. Mateu, and Y. Al-Hammadi, ‘‘Enhanced inf-TESLA protocol: A continuous connectivity and low overhead authentication protocol via IoT devices,’’ _IEEE Access_ , vol. 10, pp. 54912–54921, 2022, doi: 10.1109/ACCESS.2022.3177268. 

- [19] I. K. Dutta, B. Ghosh, and M. Bayoumi, ‘‘Lightweight cryptography for Internet of Insecure Things: A survey,’’ in _Proc. IEEE 9th Annu. Comput. Commun. Workshop Conf. (CCWC)_ , Jan. 2019, pp. 0475–0481, doi: 10.1109/CCWC.2019.8666557. 

   - [27] M. S. Henriques and N. K. Vernekar, ‘‘Using symmetric and asymmetric cryptography to secure communication between devices in IoT,’’ in _Proc. Int. Conf. IoT Appl. (ICIOT)_ , May 2017, pp. 1–4, doi: 10.1109/ICIOTA.2017.8073643. 

   - [28] L. A. Tawalbeh and T. F. Somani, ‘‘More secure Internet of Things using robust encryption algorithms against side channel attacks,’’ in _Proc. IEEE/ACS 13th Int. Conf. Comput. Syst. Appl. (AICCSA)_ , Nov. 2016, pp. 1–6, doi: 10.1109/AICCSA.2016.7945813. 

   - [29] M. S. Sharbaf, ‘‘IoT driving new Bus. Model, and IoT security, privacy, and awareness challenges,’’ in _Proc. IEEE 8th World Forum Internet Things (WF-IoT)_ , Oct. 2022, pp. 1–4, doi: 10.1109/WFIoT54382.2022.10152044. 

   - [30] O. S. Althobaiti and M. Dohler, ‘‘Cybersecurity challenges associated with the Internet of Things in a post-quantum world,’’ _IEEE Access_ , vol. 8, pp. 157356–157381, 2020, doi: 10.1109/ACCESS.2020.3019345. 

   - [31] K. Eledlebi, A. Alzubaidi, E. Damiani, D. Puthal, V. Mateu, M. J. Zemerly, Y. Al-Hammadi, and C. Y. Yeun, ‘‘Bio-integrated hybrid TESLA: A fully symmetric lightweight authentication protocol,’’ _IEEE Internet Things J._ , vol. 11, no. 23, pp. 37421–37436, Dec. 2024, doi: 10.1109/JIOT.2024.3408031. 

   - [32] A. Al Dhaheri, C. Y. Yeun, and E. Damiani, ‘‘New two-level _µ_ TESLA protocol for IoT environments,’’ in _Proc. IEEE World Congr. Services (SERVICES)_ , vols. 2642–939X, Jul. 2019, pp. 84–91, doi: 10.1109/ SERVICES.2019.00029. 

   - [33] T.-Y. Wu, Q. Meng, S. Kumari, and P. Zhang, ‘‘Rotating behind security: A lightweight authentication protocol based on IoT-enabled cloud computing environments,’’ _Sensors_ , vol. 22, no. 10, p. 3858, May 2022, doi: 10.3390/s22103858. 

   - [34] P. M. Rao and B. D. Deebak, ‘‘A comprehensive survey on authentication and secure key management in Internet of Things: Challenges, countermeasures, and future directions,’’ _Ad Hoc Netw._ , vol. 146, Jul. 2023, Art. no. 103159, doi: 10.1016/j.adhoc.2023.103159. 

   - [35] M. Rana, Q. Mamun, and R. Islam, ‘‘Enhancing IoT security: An innovative key management system for lightweight block ciphers,’’ _Sensors_ , vol. 23, no. 18, p. 7678, Sep. 2023, doi: 10.3390/s23187678. 

   - [36] D. Khoury and E. Kfoury, ‘‘Generic hybrid methods for secure connections based on the integration of GBA and TLS/CA,’’ in _Proc. Sensors Netw. Smart Emerg. Technol. (SENSET)_ , Jul. 2017, pp. 1–4, doi: 10.1109/SENSET.2017.8125033. 

   - [37] (2016). _Ericsson White Paper 284 23-3284_ . [Online]. Available: https://www.gsma.com/get-involved/gsma-membership/wpcontent/uploads/2016/03/wp-iot-security.pdf 

   - [38] (2025). _Generic Authentication Architecture_ . Accessed: Aug. 30, 2025. [Online]. Available: https://www.researchgate.net/publication/228 420506_Generic_Authentication_Architecture 

- [20] A.-E.-M. Taha, A. M. Rashwan, and H. S. Hassanein, ‘‘Secure communications for resource-constrained IoT devices,’’ _Sensors_ , vol. 20, no. 13, p. 3637, Jun. 2020, doi: 10.3390/s20133637. 

- [21] A. M. Mohamad Al-Aboosi, S. Kamil, S. N. H. S. Abdullah, and K. A. Z. Ariffin, ‘‘Lightweight cryptography for resource constraint devices: Challenges and recommendation,’’ in _Proc. 3rd Int. Cyber Resilience Conf. (CRC)_ , Jan. 2021, pp. 1–6, doi: 10.1109/CRC50527.2021.9392623. 

- [22] A. Gerodimos, L. Maglaras, M. A. Ferrag, N. Ayres, and I. Kantzavelou, ‘‘IoT: Communication protocols and security threats,’’ _Internet Things Cyber-Phys. Syst._ , vol. 3, pp. 1–13, Jan. 2023, doi: 10.1016/j.iotcps.2022.12.003. 

- [23] A. Perrig, R. Canetti, J. D. Tygar, and D. Song, ‘‘The TESLA broadcast authentication protocol,’’ _CryptoBytes_ , vol. 5, no. 2, pp. 2–13, 2002. 

- [24] K. Eledlebi, C. Y. Yeun, E. Damiani, and Y. Al-Hammadi, ‘‘Empirical studies of TESLA protocol: Properties, implementations, and replacement of public cryptography using biometric authentication,’’ _IEEE Access_ , vol. 10, pp. 21941–21954, 2022, doi: 10.1109/ACCESS.2022.3152895. 

- [25] Z. Wu, Y. Zhang, L. Liu, and M. Yue, ‘‘TESLA-based authentication for BeiDou civil navigation message,’’ _China Commun._ , vol. 17, no. 11, pp. 194–218, Nov. 2020, doi: 10.23919/JCC.2020.11.016. 

- [26] S. K. A. Theodore, K. R. Gandhi, and V. Palanisamy, ‘‘A novel lightweight authentication and privacy-preserving protocol for vehicular ad hoc networks,’’ _Complex Intell. Syst._ , vol. 9, no. 3, pp. 1–11, Oct. 2021, doi: 10.1007/s40747-021-00562-z. 

KHOULOUD ELEDLEBI (Member, IEEE) received the B.Sc. degree in communication engineering, and the M.Sc. and Ph.D. degrees in electrical and computer engineering from KUST in 2013, 2015, and 2019, respectively. She is currently an Assistant Professor of artificial intelligence with Abu Dhabi University and a former Postdoctoral Fellow with the Cyber Security and Physical Systems (C2PS) Group, Khalifa University. She has expertise in several areas, including lightweight broadcast authentication protocols, AI and machine learning, modeling of nanoscale devices, and wireless sensor network optimization. Her research interests include lightweight cryptography for IoT devices, AI and machine learning, cognitive radio networking, nanotechnology, lowpower semiconductor devices, and evolutionary computing methods. 

176108 

VOLUME 13, 2025 

K. Eledlebi et al.: Innovative Integration of GBA and Hybrid TESLA for Securing IoT Authentication 



DAVID KHOURY (Member, IEEE) received the M.E. degree in telecommunications from ESIB, in 1983. He is currently pursuing the Ph.D. degree with Université du Littoral Côte d’Opale, Calais, France. He held different positions at Matra and Ericsson, mainly in France and Sweden, in research and development, product, and system management. He led a group to develop a generic ISDN platform in the Ericsson main exchange AXE. He was involved in early studies of the GSM and the evolution toward an IP-based network and contributed to the early studies of 3G/WCDMA, HSPA, and LTE. In 2005, he became a Technology and Business Consultant for the sales unit of the Middle East and Africa region, driving new business opportunities and introducing new systems. In 2010, he established his own start-up company (Secumobi), developing advanced military-grade secure communications systems and security solutions based on the Ethereum blockchain and backed by hardware encryption and trusted execution environments (TEE) in Stockholm. For the past eight years, he was a full-time Faculty Member with the Computer Science Department and a Research Fellow with the American University of Science and Technology (AUST), Beirut. Since 2018, he has been a Strategy Consultant for Wone, a startup located in Switzerland. He has more than 35 years of experience in the field of telecommunications and technology. He holds five U.S. patents and has published many research papers at international and local conferences. His research interests include the IoT, information security, and blockchain technology. 

SAMIR HADDAD received the B.S. and M.S. degrees in computer engineering, the M.B.A. and D.E.A. degrees, and the Ph.D. degree in networking systems. He is currently an Assistant Professor with the Department of Computer Science and Mathematics and an IT Specialist. He is undertaking research in the fields of computer and electronics networking and network devices, but also in improving the understanding, design, performance, and optimization of wireless sensor 



networks. In the networking field, he is working on multiple areas, including the IoT, blockchain, security, and HCI. In the network science arena, he has focused on encoding and generic implementations. 

PATRICK SONDI (Member, IEEE) received the M.Sc. and Ph.D. degrees in computer science from the University of Valenciennes, in 2007 and 2010, respectively, and the Habilitation à Diriger des Recherches (H.D.R.) degree from Université du Littoral Côte d’Opale, in 2020. He joined Université du Littoral Côte d’Opale as an Associate Professor, in 2013. He has been a Professor with IMT Nord Europe, since 2022. His research interests include protocol engineering, the quality of service, safety, security, and event-based simulation of wired and wireless networks, especially in their application in industrial and transportation systems. 

HYERAN MUN received the B.S. degree in information security and computer engineering from Seoul Women’s University, Seoul, South Korea, in 2007, the M.S. degree in information and communication engineering from Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea, in 2009, and the Ph.D. degree from the Graduate School of Information Security, Korea University, Seoul, in 2022. She was a Researcher with the Electronics and Telecommunications Research Institution (ETRI), Daejeon. She is currently a Postdoctoral Fellow with Khalifa University, United Arab Emirates. Her research interests include vehicular IT security and AI security. VOLUME 13, 2025 

KASSEM M. DANACH (Member, IEEE) was born in Lebanon, in 1985. He received the Doctor of Philosophy (Ph.D.) degree in computer engineering from École Centrale de Lille, France, in 2016. He embarked on his academic journey with a fervent passion for computer engineering. Throughout his career, he has amassed a wealth of experience. He has applied his expertise in data analytics, artificial intelligence, machine learning, deep learning, educational technology, and busi- 



ness analytics to various military and professional roles. His illustrious career includes roles, such as the Chairperson of the Information Technology and Management Systems Department, Faculty of Business Administration, Al Maaref University, Lebanon. He has made substantial contributions to the field of operational research and artificial intelligence, earning him prestigious awards, including the Best Paper Award at LCIS, in 2017, and AISD, in 2019, and active participation as a Team Member in the EU-funded SOCORRO Project, from 2019 to 2021. 

JINANE SAYAH received the B.S. and master’s degrees in computer engineering, the D.E.A. degree in telecommunications, and the Ph.D. degree in networking and telecommunications. She is currently an Assistant Professor with the Department of Telecommunications and Networking, Issam Fares Faculty of Technology. In her research, she is working in the field of computer and networking and in human to computer interaction (HCI), the Internet of Things (IoT), sensor 



networking, wireless technologies, blockchain, and bioinformatics. 

ERNESTO DAMIANI (Senior Member, IEEE) received the Honorary Doctorate degree from the Institut National des Sciences Appliquées de Lyon, France, in 2017, for his contributions to research and teaching on big data analytics. He is currently a Full Professor with the Department of Computer Science, Università degli Studi di Milano, where he leads the Secure Service-Oriented Architectures Research (SESAR) Laboratory. He is also the Acting Dean of the College of Computing 



and Mathematical Sciences and the Founding Director of the Center for Cyber-Physical Systems, Khalifa University, United Arab Emirates. He is the Principal Investigator of the H2020 TOREADOR project on big data as a service. He has published more than 600 peer-reviewed articles and books. His research interests include cybersecurity, big data, and cloud/edge processing. He is a Distinguished Scientist of ACM. He was a recipient of the 2017 Stephen Yau Award. 

CHAN YEOB YEUN (Senior Member, IEEE) received the M.Sc. and Ph.D. degrees in information security from the Royal Holloway, University of London, in 1996 and 2000, respectively. He joined Toshiba TRL in Bristol, U.K., and later became the Vice President of LG Electronics’ Mobile Handset Research and Development Center, Seoul, South Korea, in 2005. During his time at LG Electronics, he was responsible for developing the Mobile TV technology and security. He left LG Electronics, in 2007, and worked with KAIST, South Korea, from 2007 to 2008, before joining Khalifa University of Science and Technology, in 2008. He is currently an Associate Professor with the Computer Science Department and an active member of the Center for Secure Cyber-Physical Systems (C2PS), researching cybersecurity, including the IoT/USN security, cyber-physical system security, cloud/fog security, and cryptographic techniques. He also enjoys teaching M.Sc. degree in information security and Ph.D. degree in engineering courses at Khalifa University. He has published numerous journal articles, conference papers, and ten book chapters, and holds ten international patent applications. He also serves as an editorial board member of several international journals and as a steering committee member of international conferences. 

176109 

