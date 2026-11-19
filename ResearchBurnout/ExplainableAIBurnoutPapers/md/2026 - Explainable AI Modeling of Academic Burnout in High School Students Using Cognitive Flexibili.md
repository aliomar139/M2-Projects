

## **Journal of Adolescent and Youth Psychological Studies** 



<!-- Start of picture text -->
Journal Website<br><!-- End of picture text -->

**Article history: Received 30 September 2025 Volume 7, Issue 1, pp 1-9 Revised 30 November 2025 Accepted 04 December 2025** **<u>Published online 10 January 2026</u>** 



E-ISSN: 2981-2526 

# **Explainable AI Modeling of Academic Burnout in High School Students Using Cognitive Flexibility, School Climate, and Online Learning Engagement** 

Yara. Mahfouz<sup>1</sup> , Zhang. Minyi<sup>2*</sup> 



1 Department of Counseling Psychology, Ain Shams University, Cairo, Egypt 

2 Department of Cognitive Psychology, Zhejiang University, Hangzhou, China 

**<mark>* Corresponding author email address</mark>** <mark>: minyi.zhang@zju.edu.cn</mark> 

A r t i c l e I n f o A B S T R A C T **Article type: Objective:** The objective of this study was to develop and validate an explainable _Original Research_ artificial intelligence model for predicting academic burnout among Chinese high school students based on cognitive flexibility, perceived school climate, and **How to cite this article:** online learning engagement. Mahfouz, Y., & Minyi, Z.  (2026). **Methods and Materials:** This quantitative cross-sectional study was conducted with 1,042 high school students from public schools in three major urban regions Explainable AI Modeling of Academic of eastern China using multi-stage cluster sampling. Participants completed Burnout in High School Students Using standardized measures of academic burnout, cognitive flexibility, school climate, Cognitive Flexibility, School Climate, and and online learning engagement. Data were analyzed using an ensemble machine Online Learning Engagement. _Journal of Adolescent and Youth Psychological_ learning framework combining Random Forest, Gradient Boosting, and XGBoost algorithms. Model performance was evaluated via nested cross-validation. _Studies, 7_ (1), 1-9. Explainable AI techniques including SHapley Additive exPlanations and Local http://dx.doi.org/10.61838/kman.jayps.4989 Interpretable Model-agnostic Explanations were applied to ensure transparency and interpretability of predictions. **Findings:** The ensemble model demonstrated strong predictive performance (RMSE = 0.32, MAE = 0.24) and explained 81% of the variance in academic © 2026 the authors. Published by KMAN burnout. Cognitive flexibility emerged as the most influential predictor (38.7% Publication Inc. (KMANPUB), Ontario, relative importance), followed by school climate (31.2%) and online learning Canada. This is an open access article under engagement (22.5%). The model exhibited high stability across gender and gradethe terms of the Creative Commons level subgroups, with explained variance ranging from 78% to 83%. Attribution-NonCommercial 4.0 **Conclusion:** Academic burnout among Chinese high school students is best International (CC BY-NC 4.0) License. explained through a dynamic interaction of cognitive, environmental, and behavioral factors, and the proposed explainable AI framework provides a powerful and transparent tool for early identification and targeted prevention of burnout risk in educational settings. 

**_Keywords:_** _academic burnout; cognitive flexibility; school climate; online_ _<u>learning engagement; explainable artificial intelligence; high school students</u>_ 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



### **1. Introduction** 

A 

cademic burnout has emerged as one of the most 

critical psychological and educational challenges affecting secondary school students worldwide, particularly in the post-pandemic learning environment where traditional schooling has been fundamentally reshaped by digital transformation and prolonged online instruction. Burnout in students is no longer conceptualized merely as temporary academic fatigue but as a complex multidimensional syndrome involving emotional exhaustion, cynicism toward learning, and reduced academic efficacy, which together impair motivation, performance, and psychological wellbeing. Recent international evidence indicates that burnout prevalence among adolescents has increased substantially due to heightened academic demands, prolonged screen exposure, and weakened social interaction structures inherent in online learning contexts (Hunt et al., 2023; Ye et al., 2023). In China, large-scale epidemiological investigations have confirmed that academic burnout represents a major mental health risk factor during adolescence, with strong associations to anxiety, depression, school disengagement, and long-term educational underachievement (Ye et al., 2023). Consequently, identifying protective and risk factors that shape burnout trajectories among high school students has become an urgent priority for educational systems. 

One of the most powerful psychological resources implicated in students’ adaptation to academic stress is cognitive flexibility, defined as the capacity to shift perspectives, generate alternative solutions, and adjust thinking patterns in response to changing situational demands. Contemporary cognitive science research demonstrates that flexibility supports self-regulation, problem solving, emotional control, and resilience, enabling individuals to cope more effectively with complex cognitive loads and environmental uncertainty (Mendl et al., 2024). Within educational contexts, cognitive flexibility has been shown to buffer against academic exhaustion and stress by enhancing students’ capacity to reinterpret challenges, sustain engagement, and maintain adaptive learning strategies (Arı, 2025). Empirical studies in sport psychology and academic domains converge in demonstrating that higher cognitive flexibility significantly reduces burnout symptoms, while rigidity and inflexible cognitive patterns exacerbate emotional exhaustion and disengagement (Arı, 2025). Moreover, longitudinal research in developmental psychology suggests that flexibility plays a foundational role 

in executive functioning, which directly influences learning persistence and performance across adolescence (Rocha et al., 2022). 

Parallel to individual cognitive resources, the quality of the school climate represents a decisive environmental determinant of students’ psychological functioning and academic well-being. School climate encompasses students’ perceptions of teacher support, peer relationships, academic expectations, safety, fairness, and institutional belonging. A growing body of evidence indicates that supportive, inclusive, and structured school climates significantly mitigate academic burnout, whereas negative climates characterized by high pressure, poor relationships, and limited autonomy exacerbate emotional exhaustion and cynicism (Liu, 2023; Yu et al., 2023). Studies among Chinese and international student populations consistently demonstrate that school climate influences burnout both directly and indirectly through mediating mechanisms such as school identity, psychological capital, collective selfesteem, and academic motivation (Yu et al., 2023; X. Yu et al., 2022). Furthermore, large-scale educational reforms increasingly emphasize school climate as a core driver of sustainable school improvement and student mental health (Mafratoğlu et al., 2023). 

The digitalization of education following the COVID-19 pandemic has introduced a third central dimension shaping students’ burnout experiences: online learning engagement. Online learning environments require students to maintain attention, self-discipline, emotional involvement, and cognitive investment in contexts often lacking immediate social feedback and structured routines. While online education offers flexibility and accessibility, numerous studies document that inadequate engagement in digital learning contexts is strongly associated with academic fatigue, motivational decline, and burnout (Du, 2023; Dyatlov et al., 2023; Li et al., 2025). High school students, in particular, face significant challenges in sustaining engagement during remote instruction, including technological barriers, reduced teacher interaction, assessment difficulties, and emotional isolation (Garcia et al., 2024; Li et al., 2025). Empirical investigations in Asia and Europe reveal that students with higher behavioral, emotional, and cognitive engagement in online learning report significantly lower burnout levels and greater academic satisfaction (Kuluşaklı, 2025; Wijaya et al., 2023). 

Recent educational research further demonstrates that online learning engagement is closely intertwined with cognitive and environmental factors. Students with stronger 



2 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



self-regulation, attentional control, and cognitive flexibility adapt more successfully to digital learning demands, whereas those lacking these capacities experience accelerated academic exhaustion (H.-H. Yu et al., 2022; W. Yu et al., 2022). Moreover, positive school climate factors, such as supportive teacher communication and transparent assessment practices, significantly enhance online engagement and buffer the negative psychological effects of remote education (Garcia et al., 2024; Park et al., 2023). Thus, academic burnout emerges from a dynamic interaction between individual cognitive resources, environmental conditions, and learning behavior patterns. 

While the psychological and educational correlates of burnout are well documented, methodological limitations persist in accurately modeling their complex interactions. Traditional regression-based approaches assume linearity and independence among predictors, which inadequately capture the nonlinear, hierarchical, and interactive structure underlying burnout development. In response, contemporary educational research increasingly adopts artificial intelligence and machine learning techniques to model complex educational phenomena with higher precision and predictive validity (Wang et al., 2022). Machine learning algorithms have demonstrated substantial advantages in predicting learning performance, engagement trajectories, and psychological outcomes by identifying nonlinear patterns and high-order interactions beyond the reach of conventional statistical models (Wang et al., 2022). However, a persistent limitation of many AI models is their lack of interpretability, which restricts their practical application in educational policy and psychological intervention contexts. 

The emergence of explainable artificial intelligence (XAI) provides a critical methodological advancement by integrating high predictive performance with transparent interpretability. XAI techniques such as SHapley Additive exPlanations, local interpretable model-agnostic explanations, and partial dependence visualization allow researchers and practitioners to understand not only what the model predicts but also why it makes specific predictions. This transparency is particularly vital in educational psychology, where ethical accountability and actionable insights are essential for intervention design. Recent educational technology studies emphasize that explainable models significantly enhance trust, usability, and decisionmaking in academic contexts (Nidhom et al., 2022; Wang et al., 2022). Yet, despite their promise, XAI applications in 

modeling academic burnout among adolescents remain extremely limited. 

Existing burnout prediction research in China has largely relied on classical statistical techniques, focusing on demographic and psychological correlates such as gender, grade level, stress, self-efficacy, and emotional regulation (Ye et al., 2023). Although these studies provide valuable insights, they do not sufficiently integrate cognitive flexibility, school climate, and online engagement into a unified predictive framework, nor do they employ modern explainable AI methods capable of uncovering nonlinear dynamics and personalized risk profiles. Moreover, current burnout models rarely examine how cognitive and environmental protective factors interact dynamically within digital learning ecosystems. 

The integration of cognitive flexibility research with online learning engagement literature further underscores the importance of adopting sophisticated analytical approaches. Cognitive teleintervention studies conducted during pandemic lockdowns demonstrate that cognitive enrichment programs enhance executive functioning, emotional regulation, and academic resilience among school-age children (Vita‐Barrull et al., 2023). Simultaneously, large-scale investigations of online learning during COVID-19 reveal that students’ perceptions of learning quality, assessment fairness, and teacher feedback significantly influence engagement and psychological outcomes (Du, 2023; Nitiasih et al., 2022; Nursulistyo et al., 2022). These multidimensional relationships necessitate modeling strategies capable of capturing their complexity with both precision and interpretability. 

Furthermore, burnout research increasingly recognizes the central role of psychological environments and organizational structures in shaping student well-being. Studies in medical and secondary education demonstrate that school psychological environments significantly influence burnout through collective self-esteem, institutional identity, and psychological capital (Yu et al., 2023; X. Yu et al., 2022). These findings align with broader organizational health research indicating that positive emotional climates and institutional support structures reduce occupational burnout and promote psychological sustainability (Oliveira et al., 2022; W. Yu et al., 2022). Consequently, academic burnout should be conceptualized not merely as an individual psychological outcome but as an emergent property of cognitive, environmental, and behavioral systems. 



3 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



Despite these theoretical advancements, empirical gaps remain. There is currently no comprehensive model that integrates cognitive flexibility, school climate, and online learning engagement into an explainable AI framework for predicting academic burnout among high school students in China. Existing studies examine these constructs largely in isolation, limiting their capacity to inform holistic prevention strategies. Moreover, few investigations explicitly address interpretability, leaving educators and policymakers without actionable guidance for targeted intervention. 

Addressing these gaps is especially critical in China, where high academic pressure, intense competition, and rapid digitalization of education converge to create heightened burnout vulnerability among adolescents. National educational reforms emphasize both technological innovation and student well-being, making the development of transparent, data-driven burnout prediction models particularly relevant for contemporary policy implementation. 

Therefore, the aim of this study is to develop and validate an explainable artificial intelligence model for predicting academic burnout among Chinese high school students based on cognitive flexibility, school climate, and online learning engagement. 

### **2. Methods and Materials** 

### _2.1. Study Design and Participants_ 

This study employed a quantitative, cross-sectional predictive modeling design integrating explainable artificial intelligence techniques to examine the influence of cognitive flexibility, perceived school climate, and online learning engagement on academic burnout among high school students in China. The target population consisted of fulltime secondary school students enrolled in grades 10 through 12 across public high schools in three major urban regions of eastern China, including Shanghai, Hangzhou, and Nanjing. A multi-stage cluster sampling strategy was used to ensure adequate demographic and academic representation. In the first stage, six high schools were randomly selected from official municipal education lists. In the second stage, intact classrooms within each school were randomly chosen. All students within selected classrooms were invited to participate. After exclusion of incomplete questionnaires and responses failing attention-check criteria, the final analytic sample consisted of 1,042 students, of whom 512 were female and 530 were male, with a mean age of 16.41 

years (SD = 0.92). Participation was voluntary, with written informed consent obtained from students and their parents or legal guardians prior to data collection. 

### _2.2. Measures_ 

Data were collected using a battery of validated selfreport instruments administered in classroom settings under the supervision of trained research assistants. Academic burnout was assessed using the Chinese version of the Maslach Burnout Inventory–Student Survey, which measures emotional exhaustion, academic cynicism, and reduced academic efficacy across fifteen items rated on a seven-point Likert scale. Cognitive flexibility was measured using the Cognitive Flexibility Inventory, consisting of twenty items evaluating perceived control, alternative generation, and adaptive thinking. Perceived school climate was assessed with the Comprehensive School Climate Inventory, which captures dimensions of teacher support, peer relationships, academic expectations, safety, and institutional connectedness. Online learning engagement was measured using the Online Student Engagement Scale, encompassing behavioral, emotional, cognitive, and social engagement during digital learning activities. All instruments demonstrated strong internal consistency in the present sample, with Cronbach’s alpha coefficients ranging from 0.86 to 0.93. Demographic information including age, gender, grade level, parental education, academic track, and daily internet use was also collected and included as control variables in subsequent modeling. 

### _2.3. Data Analysis_ 

Data analysis was conducted using Python and R statistical environments. Initial preprocessing included handling missing values via multiple imputation, normalization of continuous variables, and removal of multicollinearity through variance inflation factor screening. The primary predictive model of academic burnout was developed using an ensemble learning framework combining gradient boosting machines, random forests, and extreme gradient boosting algorithms. Model performance was evaluated using nested cross-validation with an 80–20 train-test split and five-fold cross-validation, employing root mean squared error, mean absolute error, and explained variance as performance metrics. To enhance interpretability and ensure model transparency, explainable artificial intelligence techniques were integrated into the analysis pipeline. Feature importance was examined using SHapley 



4 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



Additive exPlanations (SHAP), partial dependence plots, and local interpretable model-agnostic explanations (LIME). These methods enabled both global and individual-level interpretation of how cognitive flexibility, school climate, and online learning engagement contributed to predicted burnout outcomes. Robustness checks were conducted by testing alternative model specifications and performing sensitivity analyses across demographic subgroups. Statistical significance of feature contributions was assessed 

using permutation importance testing with 1,000 iterations. All analyses were conducted at a significance threshold of p < 0.05, ensuring high analytical rigor and reproducibility of findings. 

### **3. Findings and Results** 

First, descriptive statistics and bivariate correlations among the core study variables are summarized in Table 1. 

#### **Table 1** 

_Descriptive Statistics and Correlations Among Study Variables (N = 1,042)_ 

|Variable|Mean|SD|1|2|3|4|
|---|---|---|---|---|---|---|
|1. Academic Burnout|3.78|1.02|—||||
|2. Cognitive Flexibility|3.95|0.84|−0.61**|—|||
|3. School Climate|4.12|0.73|−0.57**|0.54**|—||
|4. Online Learning Engagement|3.88|0.79|−0.52**|0.49**|0.58**|—|



As shown in Table 1, students reported moderate levels of academic burnout and relatively high levels of cognitive flexibility, perceived school climate, and online learning engagement. Academic burnout demonstrated strong negative correlations with cognitive flexibility (r = −0.61), school climate (r = −0.57), and online learning engagement (r = −0.52), indicating that students who perceived 

themselves as more cognitively adaptable, who experienced a more supportive school environment, and who were more engaged in online learning reported substantially lower burnout. The predictor variables were also significantly and positively correlated with one another, suggesting interrelated protective mechanisms against academic exhaustion. 

#### **Table 2** 

_Predictive Performance of the Explainable AI Models_ 

|Model|RMSE|MAE|Explained Variance|
|---|---|---|---|
|Random Forest|0.41|0.32|0.68|
|Gradient Boosting|0.38|0.29|0.72|
|XGBoost|0.35|0.27|0.76|
|EnsembleModel|0.32|0.24|0.81|



The results in Table 2 indicate that all machine learning models achieved strong predictive accuracy, with the ensemble model demonstrating the best overall performance. The ensemble approach reduced prediction error to an RMSE of 0.32 and MAE of 0.24 while explaining 

81% of the variance in academic burnout. This confirms the robustness and generalizability of the integrated explainable AI framework for modeling complex psychological outcomes in educational settings. 

#### **Table 3** 

_Global Feature Importance Derived from SHAP Values_ 

|Predictor|Mean Absolute SHAPValue|RelativeImportance (%)|
|---|---|---|
|Cognitive Flexibility|0.41|38.7|
|School Climate|0.33|31.2|
|Online Learning Engagement|0.24|22.5|
|Gender|0.05|4.8|
|GradeLevel|0.03|2.8|





5 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



Table 3 reveals that cognitive flexibility was the most influential predictor of academic burnout, accounting for nearly 39% of total explanatory power, followed by school climate and online learning engagement. Demographic variables contributed minimally to prediction accuracy. 

These findings demonstrate that psychological and environmental factors dominate the formation of burnout risk, substantially outweighing basic demographic characteristics. 

#### **Table 4** 

_Model Stability Across Subgroups_ 

|Subgroup|RMSE|Explained Variance|
|---|---|---|
|Male Students|0.33|0.79|
|Female Students|0.31|0.82|
|Grade 10|0.34|0.78|
|Grade 11|0.32|0.81|
|Grade12|0.31|0.83|



As shown in Table 4, the ensemble model remained highly stable across gender and grade-level subgroups. Explained variance ranged from 78% to 83%, indicating that the model maintained consistent predictive performance 

regardless of demographic segmentation. This stability supports the reliability of the proposed modeling framework for diverse student populations. 

#### **Figure 1** 

_Interpretable Explainable AI Framework for Predicting Academic Burnout_ 



The results collectively demonstrate that academic burnout among Chinese high school students can be predicted with high accuracy through an explainable AI framework, with cognitive flexibility, school climate, and online learning engagement serving as dominant and interpretable determinants of risk. 

### **4. Discussion** 

The present study aimed to develop an explainable artificial intelligence framework for predicting academic burnout among Chinese high school students using cognitive flexibility, school climate, and online learning engagement as primary predictors. The findings demonstrated that the ensemble explainable AI model achieved high predictive accuracy, explaining over 80% of the variance in burnout, 



6 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



and that cognitive flexibility emerged as the strongest protective factor, followed by school climate and online learning engagement. These results provide strong empirical confirmation of the central role of cognitive, environmental, and behavioral systems in shaping adolescents’ academic well-being, and they significantly extend existing burnout research by integrating advanced explainable modeling with established educational psychology theory. 

The dominant predictive role of cognitive flexibility aligns closely with contemporary cognitive and developmental research emphasizing flexibility as a foundational executive function supporting emotional regulation, adaptive coping, and academic persistence. Mendl et al. demonstrated that flexible cognitive control facilitates voluntary task switching and efficient management of competing cognitive demands, processes that are essential in high-pressure academic environments (Mendl et al., 2024). Similarly, Arı’s investigation of student-athletes revealed that higher cognitive flexibility substantially reduces burnout symptoms and anxiety while enhancing performance stability (Arı, 2025). The present findings extend this evidence to the high school population in China, indicating that cognitively flexible students are significantly less vulnerable to emotional exhaustion and academic disengagement even under intensive academic pressure and prolonged digital learning conditions. 

The strong influence of school climate observed in this study further corroborates extensive literature documenting the protective function of supportive educational environments. Liu’s analysis of English as a Foreign Language learners demonstrated that positive school climate factors, including teacher support and academic growth mindset, significantly reduce burnout risk (Liu, 2023). Parallel findings among medical students revealed that school psychological environments influence burnout both directly and indirectly through school identity and collective self-esteem (X. Yu et al., 2022). More recently, Yu and colleagues confirmed that school climate exerts a robust effect on academic burnout via psychological capital and collective self-esteem (Yu et al., 2023). The current study strengthens these conclusions by showing that school climate remains a major predictor even when modeled alongside cognitive and engagement factors within a highperformance explainable AI system. 

Online learning engagement emerged as the third major determinant of burnout, reflecting the profound transformation of educational contexts following the COVID-19 pandemic. Li’s systematic review of high school 

students’ online learning experiences highlighted widespread challenges related to motivation, attention, and emotional involvement in digital learning environments (Li et al., 2025). Complementary qualitative investigations among Chinese learners reported substantial learning difficulties, technological stress, and emotional fatigue during remote instruction (Du, 2023). Dyatlov’s study further demonstrated that reduced engagement and instructional quality in online learning significantly undermine students’ motivation and academic endurance (Dyatlov et al., 2023). The present findings confirm that sustained behavioral, emotional, and cognitive engagement in online learning serves as a powerful buffer against burnout, particularly when supported by flexible cognition and a positive school climate. 

Importantly, the explainable AI approach employed in this study advances existing methodological paradigms by revealing the nonlinear and interactive structure underlying burnout formation. Traditional statistical models have been limited in their capacity to capture such complexity. In contrast, the current model not only achieved superior predictive accuracy but also provided transparent interpretability through SHAP and LIME analyses, offering actionable insights into individual risk profiles. This aligns with recent work by Wang et al., who demonstrated the value of machine learning in predicting learning performance and delivering personalized educational feedback (Wang et al., 2022). However, unlike previous studies, the present research explicitly integrates interpretability, addressing a major limitation of many AI applications in education. 

The robustness of the model across gender and gradelevel subgroups further underscores the generalizability of the proposed framework. The stability of predictive performance suggests that the psychological mechanisms underlying burnout operate consistently across demographic categories, reinforcing theoretical perspectives that conceptualize burnout as an emergent property of cognitiveenvironmental systems rather than demographic traits. This observation resonates with large-scale investigations of burnout in Chinese adolescents, which identify psychological and environmental variables as primary determinants of risk (Ye et al., 2023). 

The integration of cognitive flexibility, school climate, and online engagement also reflects the broader ecological framework of adolescent development, wherein individual capacities, social environments, and behavioral patterns dynamically interact. Cognitive teleintervention research conducted during pandemic lockdowns demonstrates that 



7 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



enhancing executive functions and adaptive cognition substantially improves emotional regulation and academic resilience (Vita‐Barrull et al., 2023). Simultaneously, organizational and institutional health research shows that supportive environments and emotional competence training reduce burnout and promote psychological sustainability among educators and learners (Oliveira et al., 2022). The current findings situate academic burnout within this interconnected system and provide empirical evidence for its multifactorial structure. 

### **5. Conclusion** 

Collectively, the results confirm that academic burnout cannot be effectively addressed through isolated interventions targeting only academic workload or emotional symptoms. Instead, comprehensive prevention strategies must strengthen cognitive flexibility, cultivate supportive school climates, and enhance students’ engagement in both physical and digital learning contexts. By demonstrating how these components interact within a transparent predictive model, the present study offers a powerful analytical framework for early identification and targeted intervention. 

designed to enhance cognitive flexibility, improve school climate, and increase online engagement should be evaluated using explainable AI frameworks to test causal mechanisms and optimize individualized prevention strategies. 

Educational policymakers and school administrators should prioritize programs that cultivate cognitive flexibility through problem-based learning, metacognitive training, and executive function development. Schools should systematically assess and improve school climate by strengthening teacher-student relationships, promoting psychological safety, and fostering inclusive academic cultures. Digital learning systems should be redesigned to maximize engagement by incorporating interactive content, personalized feedback, and social collaboration features. Finally, explainable AI tools should be adopted by educational institutions to identify students at risk of burnout early and to guide personalized intervention planning in a transparent and ethically responsible manner. 

### **Acknowledgments** 

We would like to express our appreciation and gratitude to all those who cooperated in carrying out this study. 

### **Declaration of Interest** 

### **6. Limitations & Suggestions** 

The authors of this article declared no conflict of interest. 

Despite its strengths, the study has several limitations. First, the cross-sectional design restricts causal inference and limits understanding of how burnout trajectories evolve over time. Second, reliance on self-report instruments may introduce response bias, social desirability effects, and common method variance. Third, although the sample was large and diverse, it was limited to urban regions of eastern China, which may constrain generalizability to rural areas or other cultural contexts. Fourth, while the explainable AI model achieved high predictive accuracy, it remains dependent on the quality and scope of input variables, and unmeasured factors such as family dynamics, personality traits, and socioeconomic stressors may further contribute to burnout risk. 

Future studies should employ longitudinal designs to examine the developmental pathways of academic burnout and the stability of predictive factors over time. Expanding samples across different regions, school types, and cultural contexts would enhance external validity. Researchers should also integrate physiological indicators, behavioral tracking data, and real-time learning analytics to strengthen model precision. Moreover, experimental interventions 

### **Ethical Considerations** 

The study protocol adhered to the principles outlined in the Helsinki Declaration, which provides guidelines for ethical research involving human participants. 

### **Transparency of Data** 

In accordance with the principles of transparency and open research, we declare that all data and materials used in this study are available upon request. 

### **Funding** 

This research was carried out independently with personal funding and without the financial support of any governmental or private institution or organization. 

### **Authors’ Contributions** 

All authors equally contributed to this article. 



8 

**E-ISSN: 2981-2526** 

Mahfouz & Minyi                                                                                                          Journal of Adolescent and Youth Psychological Studies 7:1 (2026) 1-9 



### **References** 

- Arı, A. E. (2025). Sport Burnout in Student-Athletes: The Role of Cognitive Flexibility, Task and Ego Orientation in Sport and Sport Anxiety. _Spor Bilimleri Dergisi_ , _36_ (2), 86-104. https://doi.org/10.17644/sbd.1625390 

- Du, Y. (2023). Online Learning During the Pandemic: A Qualitative Investigation of L2 CLIL Students Perceptions and Learning Challenges in China. _Lecture Notes in Education Psychology and Public Media_ , _2_ (1), 585-598. https://doi.org/10.54254/2753-7048/2/2022392 

- Dyatlov, A. V., Kovalev, V. V., & Diana, N. C. D. N. C. (2023). Motivation, Intensity and Quality of Educational Activity of Russian Schoolchildren in Online Learning. _International Journal of Cognitive Research in Science Engineering and Education_ , _11_ (3), 461-473. https://doi.org/10.23947/23348496-2023-11-3-461-473 

- Garcia, R. E., Macaballug, M. E. R., & Pérez, E. (2024). Remote Assessment of Learning During the Pandemic: Junior High School Teachers’ Experiences. _International Journal of Evaluation and Research in Education (Ijere)_ , _13_ (2), 731. https://doi.org/10.11591/ijere.v13i2.25973 

- Hunt, S. C., Simpson, J., Letwin, L., & MacLeod, B. (2023). Is Online Learning During the COVID-19 Pandemic Associated With Increased Burnout in Medical Learners?: A Medical School’s Experience. _PLoS One_ , _18_ (5), e0285402. https://doi.org/10.1371/journal.pone.0285402 

- Kuluşaklı, E. (2025). Student Engagement and Flexibility in Distance Learning in Higher Education. _Sage Open_ , _15_ (1). https://doi.org/10.1177/21582440251329979 

- Li, J., Roihan, N., & McGravey, M. (2025). High School Students' Perspectives on Their Online Learning Experiences: A Systematic Literature Review. _Journal of Computer Assisted Learning_ , _41_ (4). https://doi.org/10.1111/jcal.70064 

- Liu, X. (2023). Examining Student Burnout Causes Among English as a Foreign Language Students: Focus on School Climate and Student Growth Mindset. _Frontiers in psychology_ , _14_ . https://doi.org/10.3389/fpsyg.2023.1166408 

- Mafratoğlu, R., Altınay, F., Köç, A., Dağlı, G., & Altınay, Z. (2023). Developing a School Improvement Scale to Transform Education Into Being Sustainable and Quality Driven. _Sage Open_ , _13_ (1). https://doi.org/10.1177/21582440231157584 

- Mendl, J., Fröber, K., & Dreisbach, G. (2024). Flexibility by Association? No Evidence for an Influence of Cue–transition Associations on Voluntary Task Switching. _Journal of Experimental Psychology Human Perception & Performance_ , _50_ (3), 313-328. https://doi.org/10.1037/xhp0001186 

- Nidhom, A. M., Andika Bagus Nur Rahma, P., Smaragdina, A. A., Ningrum, G. D. K., & Yunos, J. M. (2022). Integration of Augmented Reality Into MOOC’s in Vocational Education to Support Education 3.0. _International Journal of Interactive Mobile Technologies (Ijim)_ , _16_ (03), 20-31. https://doi.org/10.3991/ijim.v16i03.28961 

- Nitiasih, P. K., Putra, I. N. A. J., Budiarta, L. G. R., Ni Luh Putu Era, A., & Suastika, G. S. (2022). A Narrative Inquiry on the Implementation of Online Learning During Covid-19 at Junior High Schools. 134-148. https://doi.org/10.2991/978-2494069-29-9_15 

   - Oliveira, S., Roberto, M. S., Simão, A. M. V., & Marques‐Pinto, A. (2022). Effects of the A+ Intervention on Elementary-School Teachers’ Social and Emotional Competence and Occupational Health. _Frontiers in psychology_ , _13_ . https://doi.org/10.3389/fpsyg.2022.957249 

   - Park, C. H., Kwon, J., Lee, J.-T., & Ahn, S. (2023). Impact of Criterion Versus Norm-Referenced Assessment on the Quality of Life in Korean Medical Students. _Journal of Korean medical science_ , _38_ (17). https://doi.org/10.3346/jkms.2023.38.e133 

   - Rocha, R. S., Castro, S. L., & Limpo, T. (2022). The Role of Transcription and Executive Functions in Writing: A Longitudinal Study in the Transition From Primary to Intermediate Grades. _Reading and Writing_ , _35_ (8), 1911-1932. https://doi.org/10.1007/s11145-022-10256-8 

   - Vita‐Barrull, N., Estrada‐Plana, V., March‐Llanes, J., Guzmán, N., Mayoral, M., & Moya, J. (2023). Cognitive Teleintervention With Board Games During the Pandemic Lockdown in School-Age Children. _International Journal of Games and Social Impact_ , _1_ (2), 8-37. https://doi.org/10.24140/ijgsi.v1.n2.01 

   - Wang, X., Zhang, L., & He, T. (2022). Learning Performance Prediction-Based Personalized Feedback in Online Learning via Machine Learning. _Sustainability_ , _14_ (13), 7654. https://doi.org/10.3390/su14137654 

   - Wijaya, R. G., Rizkyanto, W. I., Gani, I., & Iswanto, A. (2023). Analysis of the Impact of Synchronous Physical Education Online Learning on the Character, Psychology, and Physiology of High School Students in Yogyakarta. 37-47. https://doi.org/10.2991/978-94-6463-356-6_5 

   - Ye, S., Wang, R., Pan, H., Zhao, F., Li, W., Xing, J., & Wu, J. (2023). Development and Validation of a Prediction Nomogram for Academic Burnout Among Chinese Adolescents: A Cross-Sectional Study. _BMJ open_ , _13_ (5), e068370. https://doi.org/10.1136/bmjopen-2022-068370 

   - Yu, H.-H., Hu, R.-P., & Chen, M.-L. (2022). Global Pandemic Prevention Continual Learning—Taking Online Learning as an Example: The Relevance of Self-Regulation, MindUnwandered, and Online Learning Ineffectiveness. _Sustainability_ , _14_ (11), 6571. https://doi.org/10.3390/su14116571 

   - Yu, W., Yang, S., Chen, M., Zhu, Y., Meng, Q., Yao, W., & Bu, J. (2022). School Psychological Environment and Learning Burnout in Medical Students: Mediating Roles of School Identity and Collective Self-Esteem. _Frontiers in psychology_ , _13_ . https://doi.org/10.3389/fpsyg.2022.851912 

   - Yu, W., Yao, W., Chen, M., Zhu, H., & Yan, J. (2023). School Climate and Academic Burnout in Medical Students: A Moderated Mediation Model of Collective Self-Esteem and Psychological Capital. _BMC psychology_ , _11_ (1). https://doi.org/10.1186/s40359-023-01121-6 

   - Yu, X., Sun, C., Sun, B., Yuan, X., Ding, F., & Zhang, M. (2022). The Cost of Caring: Compassion Fatigue Is a Special Form of Teacher Burnout. _Sustainability_ , _14_ (10), 6071. https://doi.org/10.3390/su14106071 

- Nursulistyo, E., Indratno, T. K., Dwiastuti, E., Arifiyanti, F., Puspitasari, A. D., Abdullah, N. S. Y., & Sukarelawan, M. I. (2022). Perception Scale of Online Learning in the Indonesian Context During the Covid-19 Pandemic: Psychometric Properties Based on the Rasch Model. _Indonesian Review of Physics_ , _5_ (2), 49-56. https://doi.org/10.12928/irip.v5i2.6544 



9 

**E-ISSN: 2981-2526** 

