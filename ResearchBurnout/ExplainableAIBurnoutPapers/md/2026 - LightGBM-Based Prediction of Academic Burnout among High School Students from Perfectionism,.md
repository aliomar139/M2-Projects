

<!-- Start of picture text -->
Journal of Adolescent and Youth<br>Journal Website Psychological Studies<br>Article history:<br>Received 12 February 2026  Volume 7, Issue 6, pp 1-11<br>Revised 28 March 2026<br>Accepted 11 April 2026  E-ISSN: 2981-2526<br>Published Online 10 June 2026<br><!-- End of picture text -->

## **LightGBM-Based Prediction of Academic Burnout among High School Students from Perfectionism, Test Anxiety, Academic SelfEfficacy, and School Climate Indicators** 

Ricardo. Fúnez<sup>1</sup> , Søren. Mikkelsen<sup>2*</sup> , Jihyun. Park<sup>3</sup> 



- 1 Department of Clinical Psychology, National Autonomous University of Honduras, Tegucigalpa, Honduras 

      - 2 Department of Cognitive Psychology, Aarhus University, Aarhus, Denmark 

   - 3 Department of Counseling Psychology, Seoul National University, Seoul, South Korea 

      - **<mark>Corresponding author email address</mark>** <mark>: soren.mikkelsen@au.dk</mark> 

A r t i c l e I n f o A B S T R A C T **Article type: Objective:** To develop and evaluate a machine learning model using LightGBM _Original Research_ to predict academic burnout among high school students based on psychological and school environment factors. **How to cite this article: Methods and Materials:** A total of 1,248 high school students from Denmark Fúnez, R., Mikkelsen, S., & Park, J.  (2026). participated in this cross-sectional study. Data were collected on perfectionism, test anxiety, academic self-efficacy, and perceptions of school climate using LightGBM-Based Prediction of Academic validated self-report instruments. Academic burnout was measured with the Burnout among High School Students from Maslach Burnout Inventory–Student Survey. Demographic data including age, Perfectionism, Test Anxiety, Academic Self-Efficacy, and School Climate gender, grade level, and school type were also obtained. Data were cleaned, standardized, and analyzed using Python and LightGBM algorithms. The dataset Indicators. _Journal of Adolescent and Youth_ was divided into training (80%) and testing (20%) sets, and five-fold cross- _Psychological Studies, 7_ (6), 1-11. validation was employed for model optimization. Model performance was http://dx.doi.org/10.61838/kman.jayps.5458 assessed using accuracy, precision, recall, F1-score, ROC-AUC, and feature importance via SHAP values. **Findings:** The LightGBM model accurately classified students into low- and high-risk burnout categories with 89.1% accuracy on the testing dataset. Test © 2026 the authors. Published by KMAN anxiety emerged as the strongest predictor, followed by academic self-efficacy, Publication Inc. (KMANPUB), Ontario, school climate, and perfectionism. Higher test anxiety and perfectionism were Canada. This is an open access article under associated with increased burnout risk, whereas higher self-efficacy and more the terms of the Creative Commons positive school climate perceptions were protective. The SHAP summary plot Attribution-NonCommercial 4.0 revealed the individual contributions of each predictor and indicated International (CC BY-NC 4.0) License. heterogeneity in their effects across students. Demographic variables contributed minimally to predictive performance. **Conclusion:** This study demonstrates the effectiveness of a LightGBM-based model for predicting academic burnout using psychological and environmental factors. Findings emphasize the importance of addressing test anxiety, promoting academic self-efficacy, and fostering supportive school climates to reduce burnout risk among adolescents. Machine learning approaches can inform targeted interventions and early identification of at-risk students. **_Keywords:_** _Academic burnout, Perfectionism, Test anxiety, Academic self-_ _<u>efficacy, School climate, Machine learning, LightGBM, Adolescents</u>_ 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



# **1. Introduction** A 

cademic burnout has emerged as one of the most 

significant psychological and educational challenges affecting adolescents in contemporary educational systems. Characterized by emotional exhaustion, cynicism toward academic activities, and feelings of reduced academic competence, academic burnout negatively influences students’ psychological well-being, academic achievement, school engagement, and long-term educational trajectories. Although initially conceptualized within occupational contexts, burnout has increasingly been recognized as a critical issue among students, particularly during secondary education when academic demands intensify and educational expectations become more pronounced. Research has consistently demonstrated that burnout is associated with diminished motivation, increased psychological distress, reduced academic performance, and elevated risk for mental health difficulties, making its early identification and prevention a priority for educators and mental health professionals (Ma, 2021; Qin et al., 2022; Setiyowati et al., 2024). 

The prevalence of academic burnout among adolescents has attracted growing scholarly attention due to substantial changes in educational environments, increasing academic competition, and heightened performance expectations. Recent evidence suggests that burnout is not solely a consequence of excessive workload but rather reflects a complex interaction among personal, emotional, motivational, and environmental factors. Students experiencing chronic educational stress often report diminished enthusiasm for learning, emotional fatigue, and feelings of inefficacy that compromise both academic functioning and psychological adjustment. Furthermore, burnout has been linked to broader indicators of mental health vulnerability, including anxiety, depression, loneliness, hopelessness, and emotional dysregulation, highlighting its multidimensional nature and far-reaching consequences (Al-Awad, 2024; Cully et al., 2025; Lin & Guo, 2024; Mahsood et al., 2025). 

Among the psychological characteristics associated with academic burnout, perfectionism has emerged as one of the most influential predictors. Perfectionism refers to the tendency to establish excessively high personal standards accompanied by overly critical self-evaluation and concerns regarding mistakes. Although adaptive forms of striving for excellence may facilitate achievement, maladaptive perfectionism frequently contributes to psychological 

distress, self-criticism, chronic stress, and emotional exhaustion. Contemporary theoretical perspectives emphasize that perfectionistic individuals often evaluate their self-worth through academic performance, creating persistent pressure that can eventually culminate in burnout symptoms (Flett & Hewitt, 2022; Liu & Berzenski, 2022). Research has demonstrated that perfectionism is associated with increased academic stress, reduced psychological flexibility, impaired well-being, and elevated vulnerability to emotional exhaustion among students (Gaudreau & Benoît, 2024, 2025). 

Evidence from adolescent populations further supports the central role of perfectionism in educational outcomes. Chasetareh et al. reported that perfectionistic tendencies significantly influenced learning processes through motivational and self-regulatory mechanisms (Chasetareh et al., 2022). Similarly, Choi et al. found that perfectionism contributed to academic burnout through motivational pathways, suggesting that internalized performance pressures may undermine healthy academic engagement (Choi et al., 2022). Additional studies have demonstrated direct associations between perfectionism and burnout across diverse educational settings, indicating that students who perceive academic success as a prerequisite for selfworth experience higher levels of emotional exhaustion and disengagement (Dobos et al., 2024; Faiman & Strouse, 2025; Ramadhana et al., 2023). Furthermore, socially prescribed perfectionism has been linked to external pressures from parents, teachers, and peers, which may further intensify burnout risk among adolescents (Zhang et al., 2025). 

Another critical factor implicated in academic burnout is test anxiety. Test anxiety encompasses emotional, physiological, and cognitive reactions associated with evaluative situations and academic examinations. Students experiencing high levels of test anxiety often report excessive worry, concentration difficulties, physiological arousal, and fear of failure, all of which may impair academic performance and psychological well-being. The educational environment increasingly emphasizes standardized testing and competitive evaluation, potentially exacerbating anxiety-related responses among adolescents. Persistent anxiety can deplete cognitive and emotional resources, increasing susceptibility to burnout over time (Chung & Shin, 2024; Journault et al., 2023). 

The relationship between anxiety and burnout is supported by extensive theoretical and empirical evidence. Anxiety consumes attentional resources and increases emotional strain, reducing students’ ability to cope 



2 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



effectively with academic challenges. Studies have shown that students with elevated test anxiety are more likely to experience exhaustion, academic disengagement, and decreased satisfaction with learning experiences. Contextual factors such as classroom climate, teacher expectations, and competitive educational environments further influence anxiety development, emphasizing the importance of examining test anxiety within broader educational frameworks (Journault et al., 2023; Yaacob et al., 2023). Moreover, investigations of stress-related conditions have demonstrated strong associations between symptom severity and emotional exhaustion, reinforcing the conceptual links between anxiety and burnout processes (Cully et al., 2025). 

In contrast to risk factors such as perfectionism and anxiety, academic self-efficacy has consistently been identified as a protective psychological resource. Derived from social cognitive theory, academic self-efficacy refers to students’ beliefs regarding their ability to successfully perform academic tasks and overcome educational challenges. Individuals with high self-efficacy typically demonstrate greater persistence, adaptive coping, effective self-regulation, and resilience when confronted with academic stressors. Consequently, self-efficacy has been widely recognized as an important buffer against burnout and psychological distress (Sanseverino et al., 2023; Yin et al., 2024). 

A growing body of literature indicates that students who possess stronger academic self-efficacy report lower levels of emotional exhaustion and greater academic engagement. Sanseverino et al. demonstrated that self-efficacy serves as a crucial resource that reduces emotional exhaustion and maladaptive study behaviors among university students (Sanseverino et al., 2023). Similarly, Yin et al. identified distinct burnout profiles characterized by variations in selfefficacy, highlighting the importance of efficacy beliefs in educational adjustment (Yin et al., 2024). Research has further shown that self-efficacy mediates or moderates the relationships between stress, perfectionism, and burnout, suggesting that confidence in one’s academic abilities may attenuate the negative impact of psychological vulnerabilities (Hawkins & Mackinnon, 2024, 2025). Studies conducted among medical and higher education students have similarly emphasized the protective role of self-efficacy in fostering resilience and maintaining academic well-being (Azim et al., 2025; Ok et al., 2025). 

Beyond individual psychological characteristics, educational researchers increasingly recognize the importance of contextual influences on student well-being. 

School climate represents one of the most comprehensive environmental constructs affecting adolescent development. School climate encompasses students’ perceptions of safety, teacher support, peer relationships, fairness, connectedness, and overall educational atmosphere. Positive school climates are associated with enhanced engagement, stronger academic motivation, improved mental health, and reduced behavioral problems. Conversely, negative educational environments may contribute to stress, alienation, and burnout (Journault et al., 2023; Kim, 2022). 

Theoretical models of burnout emphasize that environmental resources can either mitigate or amplify the effects of individual vulnerabilities. Students who perceive their schools as supportive and inclusive may be better equipped to cope with academic pressures, whereas those experiencing unsupportive or highly competitive environments may encounter greater emotional strain. Longitudinal evidence suggests that contextual educational factors significantly contribute to the development and maintenance of school burnout over time (Cengiz & Peker, 2024). Systematic reviews examining educational wellbeing have likewise highlighted the importance of social and institutional support systems in promoting mental health and reducing exhaustion among students (Aalto et al., 2024; Klein & McCarthy, 2022). Moreover, literature concerning impostor phenomenon and achievement-related stress indicates that environmental validation and supportive learning conditions can substantially influence students’ emotional adjustment and academic functioning (Blondeau, 2024; Ménard & Chittle, 2023). 

Recent scholarship has increasingly advocated for integrated models that simultaneously examine multiple psychological and contextual predictors of burnout. Burnout rarely emerges from a single causal factor; instead, it develops through interactions among personality characteristics, emotional experiences, motivational beliefs, and environmental conditions. Studies have demonstrated that perfectionism interacts with stress and self-efficacy to influence burnout outcomes, supporting multidimensional conceptualizations of student well-being (Hawkins & Mackinnon, 2024, 2025). Similarly, investigations examining perfectionism and burnout have identified protective mechanisms such as self-compassion and resilience that can attenuate maladaptive outcomes (AlAwad, 2024; Pereira et al., 2022). These findings collectively suggest that comprehensive predictive approaches are necessary to fully understand burnout risk among adolescents. 



3 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



While conventional statistical approaches have substantially advanced burnout research, they may be limited in their ability to model complex nonlinear relationships and high-order interactions among predictors. Machine learning methods provide powerful alternatives for identifying patterns within large datasets and generating accurate predictive models. In educational and psychological research, machine learning techniques have increasingly been employed to detect at-risk individuals, predict academic outcomes, and identify critical risk factors underlying mental health difficulties. Unlike traditional regression-based methods, machine learning algorithms can accommodate complex interactions and nonlinear associations without requiring restrictive assumptions regarding data structure. 

Among machine learning approaches, Light Gradient Boosting Machine (LightGBM) has gained considerable attention due to its computational efficiency, predictive accuracy, and ability to manage large-scale datasets. LightGBM employs gradient boosting decision trees and advanced optimization techniques to generate highly accurate predictive models while maintaining interpretability through feature importance analyses. Despite growing interest in machine learning applications within educational psychology, relatively few studies have applied LightGBM to predict academic burnout among adolescents using an integrated set of psychological and school-related variables. Existing research has primarily focused on traditional explanatory models, leaving important opportunities for predictive investigations capable of informing early identification and intervention efforts. 

Given the increasing prevalence of academic burnout among adolescents and the demonstrated importance of perfectionism, test anxiety, academic self-efficacy, and school climate, there is a need for advanced predictive models capable of identifying students at elevated risk. Furthermore, understanding the relative contribution of these factors may provide valuable insights for educators, counselors, and policymakers seeking to develop targeted prevention and intervention strategies. Therefore, the present study aimed to develop and evaluate a LightGBMbased predictive model of academic burnout among Danish high school students using perfectionism, test anxiety, academic self-efficacy, and school climate indicators as primary predictors. 

### **2. Methods and Materials** 

### _2.1. Study Design and Participants_ 

This study employed a cross-sectional predictive research design to develop and evaluate a Light Gradient Boosting Machine (LightGBM) model for the classification and prediction of academic burnout among high school students. The study was conducted in Denmark during the 2025–2026 academic year and focused on identifying the relative contribution of perfectionism, test anxiety, academic selfefficacy, and school climate indicators to the prediction of burnout risk. A total of 1,248 students were recruited from public and private secondary schools located in Copenhagen, Aarhus, Odense, and Aalborg through a multistage cluster sampling procedure. Initially, schools were randomly selected from regional educational directories, and subsequently, classrooms within each participating school were randomly chosen. Students aged between 15 and 19 years were eligible to participate if they were currently enrolled in upper secondary education and provided informed consent along with parental consent for participants younger than 18 years. The final sample consisted of 648 female students (51.9%) and 600 male students (48.1%), with a mean age of 16.84 years (SD = 1.12). Participation was voluntary, and students were assured that their responses would remain anonymous and confidential. 

### _2.2. Measures_ 

Academic burnout was assessed using the Maslach Burnout Inventory–Student Survey (MBI-SS), developed by Schaufeli and colleagues. The instrument consists of 15 items measuring three dimensions of student burnout: emotional exhaustion, cynicism toward school activities, and reduced academic efficacy. Participants responded to each item using a seven-point Likert scale ranging from 0 (never) to 6 (always). Higher scores indicated greater levels of academic burnout. The MBI-SS has demonstrated strong psychometric properties across adolescent and educational populations, with previous studies reporting satisfactory construct validity, convergent validity, and internal consistency coefficients exceeding .80. 

Perfectionism was measured using the Child and Adolescent Perfectionism Scale (CAPS), developed by Flett, Hewitt, Boucher, Davidson, and Munro. The scale contains 22 items evaluating self-oriented perfectionism and socially prescribed perfectionism. Responses are recorded on a five- 



4 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



point Likert scale ranging from 1 (false—not at all true of me) to 5 (very true of me). Higher scores reflect greater perfectionistic tendencies. The CAPS has been extensively validated among adolescent populations and has consistently demonstrated adequate reliability and factorial validity across different cultural contexts. 

Test anxiety was evaluated using the Test Anxiety Inventory (TAI), developed by Spielberger. The instrument consists of 20 items assessing emotionality and worry components associated with examination-related anxiety. Participants rated each statement on a four-point Likert scale ranging from 1 (almost never) to 4 (almost always). Higher total scores indicate elevated levels of test anxiety. Previous studies have confirmed the instrument’s strong internal consistency, test–retest reliability, and criterion-related validity among secondary school students. 

Academic self-efficacy was measured using the Academic Self-Efficacy Scale developed by Midgley and colleagues as part of the Patterns of Adaptive Learning Scales framework. The scale includes 8 items designed to assess students’ confidence in their ability to successfully complete academic tasks, overcome learning challenges, and achieve educational goals. Responses are provided on a fivepoint Likert scale ranging from 1 (strongly disagree) to 5 (strongly agree). Higher scores indicate stronger academic self-efficacy beliefs. Numerous studies have demonstrated the scale’s reliability and validity in adolescent educational settings. 

School climate was assessed using the School Climate Measure developed by Zullig and colleagues. This multidimensional instrument evaluates students’ perceptions of teacher support, academic expectations, safety, peer relationships, school connectedness, and overall learning environment. The version used in the present study contained 30 items rated on a five-point Likert scale ranging from 1 (strongly disagree) to 5 (strongly agree). Higher scores represented more positive perceptions of school climate. Previous research has provided substantial evidence regarding the scale’s construct validity, criterion validity, and reliability among high school populations. 

### _2.3. Data Analysis_ 

Data analysis was conducted using Python programming language and machine learning libraries including LightGBM, Scikit-learn, NumPy, and Pandas. Prior to model development, the dataset was screened for missing values, outliers, and inconsistencies. Missing data 

constituted less than 3% of all observations and were handled using multiple imputation techniques. Continuous variables were standardized where appropriate, and categorical variables were encoded for machine learning processing. Descriptive statistics including means, standard deviations, frequencies, and percentages were calculated to characterize the sample and study variables. 

Academic burnout scores derived from the MBI-SS were used to classify students into low-risk and high-risk burnout categories based on established percentile thresholds. The dataset was randomly divided into training and testing subsets using an 80:20 ratio. To optimize model performance and reduce overfitting, five-fold crossvalidation was implemented within the training dataset. Hyperparameter tuning was performed using grid search optimization procedures, examining combinations of learning rate, maximum tree depth, number of estimators, feature fraction, bagging fraction, and minimum data in leaf nodes. 

The predictive performance of the LightGBM model was evaluated using multiple classification metrics, including accuracy, precision, recall, F1-score, area under the receiver operating characteristic curve (AUC-ROC), and confusion matrix indicators. Feature importance analysis was subsequently performed using gain-based importance scores and SHapley Additive exPlanations (SHAP) values to determine the relative contribution of perfectionism, test anxiety, academic self-efficacy, school climate indicators, and demographic variables in predicting academic burnout risk. Statistical analyses and machine learning procedures were conducted using a significance threshold of p < .05 where applicable, and model robustness was assessed through repeated validation procedures to ensure generalizability and stability of the predictive findings. 

### **3. Findings and Results** 

A total of 1,248 high school students from Denmark participated in the study. The sample consisted of 648 female students (51.9%) and 600 male students (48.1%). The mean age of participants was 16.84 years (SD = 1.12), with ages ranging from 15 to 19 years. Regarding grade level, 32.4% of students were enrolled in the first year of upper secondary education, 34.8% in the second year, and 32.8% in the third year. Most participants attended public schools (78.5%), while 21.5% attended private institutions. Approximately 44.1% of students reported that at least one parent possessed a university degree. Based on the established academic 



5 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



burnout classification threshold, 366 students (29.3%) were classified as high-risk for academic burnout, whereas 882 students (70.7%) were classified as low-risk. Preliminary 

inspection of the data indicated acceptable distributional characteristics, with no severe violations of normality and less than 3% missing data across all variables. 

#### **Table 1** 

_Descriptive Statistics and Correlations Among Study Variables_ 

|Variable|Mean|SD|1|2|3|4|5|
|---|---|---|---|---|---|---|---|
|Academic Burnout|41.86|12.41|1.00|||||
|Perfectionism|71.54|13.26|.58**|1.00||||
|Test Anxiety|49.28|11.74|.63**|.49**|1.00|||
|Academic Self-Efficacy|28.92|5.47|-.61**|-.42**|-.55**|1.00||
|SchoolClimate|102.35|17.88|-.57**|-.36**|-.41**|.53**|1.00|



Table 1 presents descriptive statistics and Pearson correlation coefficients among the primary study variables. Academic burnout demonstrated strong positive associations with perfectionism (r = .58, p < .01) and test anxiety (r = .63, p < .01), indicating that students reporting higher levels of perfectionistic tendencies and examination-related anxiety were more likely to experience burnout symptoms. Conversely, academic burnout exhibited substantial negative correlations with academic self-efficacy (r = -.61, p < .01) and school climate (r = -.57, p < .01), suggesting that 

stronger beliefs in academic competence and more favorable perceptions of the school environment were associated with lower burnout levels. The strongest bivariate relationship was observed between test anxiety and academic burnout, highlighting anxiety-related factors as particularly important correlates of student exhaustion and disengagement. The correlation matrix also revealed moderate interrelationships among predictors, supporting their theoretical relevance while indicating the absence of problematic multicollinearity. 

#### **Table 2** 

_Performance Metrics of the LightGBM Classification Model_ 

|Metric|Training Set|Testing Set|
|---|---|---|
|Accuracy|0.912|0.891|
|Precision|0.894|0.876|
|Recall|0.901|0.868|
|F1-Score|0.897|0.872|
|ROC-AUC|0.948|0.926|
|Specificity|0.919|0.902|
|Balanced Accuracy|0.910|0.885|



The predictive performance of the LightGBM classifier is summarized in Table 2. The model demonstrated excellent classification capability across all evaluation metrics. On the testing dataset, the model achieved an overall accuracy of 89.1%, indicating that nearly nine out of ten students were correctly classified into burnout-risk categories. Precision reached 87.6%, suggesting a low false-positive rate, while recall was 86.8%, indicating strong sensitivity in identifying students genuinely at risk for burnout. The F1-score of 0.872 

reflected an effective balance between precision and recall. Most notably, the ROC-AUC value of 0.926 demonstrated outstanding discriminatory power, indicating that the model was highly successful in distinguishing between high-risk and low-risk students. The small differences between training and testing performance further suggested minimal overfitting and strong generalizability of the LightGBM approach. 

#### **Table 3** 

_Confusion Matrix Results for the Testing Dataset_ 

|Actual Classification<br>Low Risk|Predicted Low Risk<br>163|Predicted High Risk<br>18|
|---|---|---|





6 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 

<u>High Risk</u> 

<u>60</u> 



<u>9</u> 

The confusion matrix presented in Table 3 provides a detailed overview of classification outcomes on the testing dataset. Among students who truly belonged to the low-risk group, 163 were correctly classified, whereas only 18 were incorrectly identified as high-risk. Similarly, among students who genuinely belonged to the high-risk category, 60 were correctly detected, while only 9 were incorrectly classified as low-risk. These findings indicate that the LightGBM 

model maintained high sensitivity and specificity simultaneously. From a practical perspective, the relatively small number of false-negative classifications is particularly important because failing to identify students experiencing severe burnout may prevent timely intervention. The low frequency of classification errors demonstrates the practical utility of machine learning techniques for early identification of vulnerable students in educational settings. 

#### **Table 4** 

_Feature Importance Rankings Based on SHAP Values and LightGBM Gain Scores_ 

|Predictor|SHAP Importance|Relative Contribution (%)|Rank|
|---|---|---|---|
|Test Anxiety|0.312|31.2|1|
|Academic Self-Efficacy|0.256|25.6|2|
|School Climate|0.198|19.8|3|
|Perfectionism|0.167|16.7|4|
|Age|0.034|3.4|5|
|Gender|0.021|2.1|6|
|School Type|0.012|1.2|7|



#### **Figure 1** 

_SHAP Summary Plot Illustrating the Relative Impact of Predictor Variables on Academic Burnout Classification_ 



Table 4 presents the relative importance of predictors within the final LightGBM model. Test anxiety emerged as the most influential variable, accounting for 31.2% of total predictive importance. This finding indicates that students experiencing elevated levels of anxiety related to examinations and academic evaluation were substantially more likely to be classified as belonging to the high-burnout 

group. Academic self-efficacy was identified as the second most important predictor, contributing 25.6% of overall predictive power. Higher levels of academic confidence consistently reduced burnout risk across the sample. School climate represented the third most influential factor, contributing 19.8% of predictive importance, suggesting that supportive, safe, and academically encouraging educational 



7 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



environments play a critical role in preventing burnout. Perfectionism ranked fourth, contributing 16.7% of model performance. Demographic variables including age, gender, and school type exhibited comparatively limited predictive value. Overall, psychological and educational variables accounted for over 93% of the model’s predictive capacity, emphasizing their central role in understanding academic burnout among adolescents. 

Figure 1 illustrates the SHAP summary analysis generated from the final LightGBM model. The figure demonstrates that high values of test anxiety and perfectionism substantially increased the probability of classification into the high-burnout category. In contrast, elevated levels of academic self-efficacy and positive school climate perceptions consistently reduced burnout risk. The visualization further revealed considerable heterogeneity in predictor effects across individuals, indicating that burnout develops through complex interactions among personal and environmental factors. Test anxiety displayed the widest distribution of SHAP values, confirming its dominant role in model decision-making. Academic self-efficacy showed a strong protective pattern, whereas school climate exerted a moderately strong buffering effect. Collectively, the SHAP analysis enhanced the interpretability of the machine learning model and provided valuable insights regarding the mechanisms through which psychological and contextual factors contribute to academic burnout among high school students. 

### **4. Discussion** 

The present study employed a LightGBM-based machine learning model to predict academic burnout among Danish high school students using perfectionism, test anxiety, academic self-efficacy, and school climate indicators as predictors. The findings from this research offer substantial insights into both the individual and contextual factors that contribute to burnout and highlight the utility of advanced predictive modeling in educational psychology. Overall, the model demonstrated high accuracy and robust classification performance, indicating that a combination of psychological and environmental variables can effectively predict students at risk for burnout. Feature importance analysis revealed that test anxiety emerged as the most influential predictor, followed by academic self-efficacy, school climate, and perfectionism, while demographic variables such as age, gender, and school type contributed minimally. These results are consistent with prior research emphasizing the central 

role of cognitive-emotional and motivational variables in adolescent burnout. 

The prominence of test anxiety as the primary predictor aligns with a wealth of evidence demonstrating the detrimental impact of evaluative stress on student wellbeing. High test anxiety depletes cognitive and emotional resources, impairing concentration, motivation, and performance, thereby increasing susceptibility to burnout (Cully et al., 2025; Journault et al., 2023). The current findings corroborate previous studies indicating that examination-related apprehension constitutes a core risk factor for emotional exhaustion and academic disengagement (Yaacob et al., 2023). The present model's identification of test anxiety as the dominant contributor underscores the critical need for interventions targeting emotional regulation and stress management within educational settings, particularly during high-stakes testing periods. 

Academic self-efficacy emerged as the second most influential predictor, exerting a strong protective effect against burnout. Consistent with prior research, students who perceive themselves as capable of successfully managing academic tasks exhibit lower levels of emotional exhaustion and disengagement (Sanseverino et al., 2023; Yin et al., 2024). The observed negative relationship between self-efficacy and burnout supports social-cognitive models suggesting that confidence in one’s academic abilities fosters adaptive coping strategies, perseverance, and resilience, thereby mitigating the adverse effects of stressors such as perfectionistic tendencies and test anxiety (Hawkins & Mackinnon, 2024, 2025). These results align with previous findings in both adolescent and university populations demonstrating that self-efficacy not only directly reduces burnout risk but may also buffer the impact of external pressures, including high parental expectations and competitive educational environments (Al-Awad, 2024; Pereira et al., 2022). 

School climate was also identified as a significant predictor, emphasizing the importance of contextual educational factors in shaping student well-being. Positive school environments characterized by supportive teacherstudent relationships, strong peer connectedness, fairness, and overall safety contribute to lower burnout risk by providing students with emotional and social resources necessary for coping with academic stress (Journault et al., 2023; Kim, 2022). These findings reinforce longitudinal research indicating that adverse school climates exacerbate stress and disengagement, highlighting the interactive role of 



8 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



environmental conditions with individual vulnerabilities in determining burnout outcomes (Aalto et al., 2024; Cengiz & Peker, 2024). The present study extends prior work by quantitatively demonstrating the relative contribution of school climate within a predictive model framework, illustrating its practical relevance alongside cognitiveemotional variables. 

Perfectionism, while slightly less influential than test anxiety, self-efficacy, and school climate, remained a notable predictor of academic burnout. Maladaptive perfectionism, particularly socially prescribed and selforiented forms, has consistently been linked to higher levels of emotional exhaustion, worry, and disengagement (Faiman & Strouse, 2025; Flett & Hewitt, 2022). The current findings are consistent with prior evidence demonstrating that perfectionistic students are more vulnerable to stressinduced burnout due to heightened sensitivity to evaluation, fear of failure, and internalized standards of achievement (Choi et al., 2022; Chung & Shin, 2024; Ramadhana et al., 2023). Importantly, the integration of perfectionism into the LightGBM model highlights its complex interactions with both internal resources (e.g., self-efficacy) and environmental supports (e.g., school climate), emphasizing that risk and protective factors jointly contribute to burnout processes. 

The use of SHAP values provided a nuanced understanding of how individual predictors influence burnout probability across the student population. High test anxiety and perfectionism values were associated with increased likelihood of being classified as high-risk, whereas high self-efficacy and positive perceptions of school climate corresponded to decreased probability of burnout. This finding demonstrates the practical value of interpretable machine learning in educational settings, allowing educators and psychologists to identify which students may benefit most from targeted interventions. Moreover, the observed heterogeneity in predictor effects suggests that individualized approaches may be more effective than uniform strategies, supporting the application of precision education frameworks (Dobos et al., 2024; Gaudreau & Benoît, 2025). 

From a methodological perspective, the high accuracy and robust performance of the LightGBM model validate the utility of gradient boosting algorithms for psychological prediction. Unlike traditional regression models, LightGBM effectively captures nonlinear relationships and complex interactions among predictors, offering an advanced tool for early identification of at-risk students (Liu & Berzenski, 

2022; Osenk et al., 2022). The combination of psychological (perfectionism, test anxiety, self-efficacy) and environmental (school climate) variables within a single predictive framework provides a comprehensive approach to understanding burnout, highlighting the multidimensional nature of this phenomenon. 

### **5. Conclusion** 

The implications of these findings extend to intervention and prevention strategies. Targeting test anxiety through cognitive-behavioral techniques, stress-management training, and mindfulness-based interventions may directly reduce one of the most salient risk factors for burnout. Similarly, enhancing academic self-efficacy via goal-setting, skill-building, and feedback interventions could buffer the impact of stressors, fostering resilience among students (Pereira et al., 2022; Sanseverino et al., 2023). Improvements in school climate, including fostering supportive teacher-student relationships, peer collaboration, and a safe and inclusive environment, may further reinforce protective mechanisms, reducing burnout prevalence at the institutional level (Aalto et al., 2024; Kim, 2022). 

### **6. Limitations & Suggestions** 

Despite its strengths, this study has several limitations. First, the cross-sectional design precludes causal inference; the identified associations reflect predictive relationships but cannot definitively establish temporal causality. Second, all variables were self-reported, which may introduce bias due to social desirability, perceptual distortion, or commonmethod variance. Third, the sample, while large and diverse within Denmark, may not generalize to students in other cultural, educational, or national contexts. Additionally, although LightGBM provides interpretable feature importance metrics, the complexity of tree-based models may obscure subtler interactions or nonlinearities that were not fully captured. Finally, the study focused primarily on psychological and school-related predictors, and other relevant factors such as familial stressors, peer dynamics, or extracurricular demands were not included, potentially limiting model comprehensiveness. 

Future research should consider longitudinal designs to track burnout development over time, which would allow for stronger causal inferences and examination of temporal dynamics among perfectionism, anxiety, self-efficacy, and school climate. Multi-informant assessments, including teacher reports, peer evaluations, and objective academic 



9 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



records, could enhance measurement validity and reduce self-report bias. Expanding the model to include additional psychosocial and environmental variables, such as parental involvement, peer support, and sleep or lifestyle factors, may increase predictive accuracy and provide a more comprehensive understanding of burnout risk. Crosscultural replication studies are also warranted to determine whether the identified predictors hold across diverse educational systems, providing generalizable insights. Finally, experimental or intervention studies can examine whether targeted modification of key predictors identified by machine learning models effectively reduces burnout incidence. 

From a practical standpoint, the findings highlight the importance of early identification and support for students at risk of burnout. Schools should consider implementing systematic screening programs that integrate assessments of test anxiety, perfectionism, and self-efficacy. Interventions focusing on stress management, resilience-building, and development of adaptive coping skills could be incorporated into curricula. Teacher training programs should emphasize the creation of positive school climates and supportive learning environments. Individualized approaches tailored to student profiles may be more effective than one-size-fitsall programs, ensuring that resources are directed toward those who are most vulnerable. Finally, collaboration between educators, counselors, and parents can facilitate comprehensive strategies to prevent burnout and promote student well-being, enhancing both academic outcomes and psychological resilience. 

### **Acknowledgments** 

We would like to express our appreciation and gratitude to all those who cooperated in carrying out this study. 

### **Declaration of Interest** 

The authors of this article declared no conflict of interest. 

### **Ethical Considerations** 

The study protocol adhered to the principles outlined in the Helsinki Declaration, which provides guidelines for ethical research involving human participants. 

### **Transparency of Data** 

In accordance with the principles of transparency and open research, we declare that all data and materials used in this study are available upon request. 

### **Funding** 

This research was carried out independently with personal funding and without the financial support of any governmental or private institution or organization. 

### **Authors’ Contributions** 

All authors equally contributed to this article. 

### **References** 

- Aalto, E. P., Pons, J., Alcaraz, S., Zamora‐Solé, R., & Ramis, Y. (2024). Psychological and Social Factors Associated With Mental Health of European Dual Career Athletes: A Systematic Review. _European Journal of Sport Science_ , _24_ (12), 1844-1864. https://doi.org/10.1002/ejsc.12218 

- Al-Awad, F. A. (2024). Academic Burnout, Stress, and the Role of Resilience in a Sample of Saudi Arabian Medical Students. _Medical Archives_ , _78_ (1), 39. https://doi.org/10.5455/medarh.2024.78.39-43 

- Azim, S. R., Yusoff, M. S. B., & Roslan, N. S. (2025). Mapping the Multidimensional Factors of Medical Student Resilience Development: A Scoping Review. _BMC Medical Education_ , _25_ (1). https://doi.org/10.1186/s12909-025-07290-9 

- Blondeau, L. A. (2024). The Impostor Phenomenon’s Relation to Achievement at School and Work. 111-130. https://doi.org/10.1037/0000397-006 

- Cengiz, S., & Peker, A. (2024). Antecedents of School Burnout: A Longitudinal Mediation Study. _Social Psychology of Education_ , _27_ (4), 1901-1919. https://doi.org/10.1007/s11218024-09887-2 

- Chasetareh, F., Barabadi, E., Khajavy, G. H., & Flett, G. L. (2022). Perfectionism and L2 Achievement: The Mediating Roles of Motivation and Self-Regulated Learning Among Iranian High School Students. _Journal of Psychoeducational Assessment_ , _41_ (1), 3-21. https://doi.org/10.1177/07342829221096916 

- Choi, H.-j., Cho, S., Kim, J., Kim, E. J., Chung, J., & Lee, S. M. (2022). The Mediating Effect of Introjected Motivation on the Relation Between Perfectionism and Academic Burnout. _Journal of Psychologists and Counsellors in Schools_ , _32_ (2), 207-219. https://doi.org/10.1017/jgc.2020.8 

- Chung, Y., & Shin, J. Y. (2024). Profiles of Perfectionism and Their Relations to Task Disengagement, Test Anxiety, and Depression in South Korean High School Students: The Mediating Role of Achievement Goals. _European Journal of Education_ , _60_ (1). https://doi.org/10.1111/ejed.12894 

- Cully, S., Hatinova, K., Jakob Clason van de, L., & Björnsdotter, M. (2025). Factors Associated With Symptom Severity in Stress-Induced Exhaustion Disorder: Cohort Characterization and Cross-Sectional Correlations. _Frontiers in Psychiatry_ , _16_ . https://doi.org/10.3389/fpsyt.2025.1548967 

- Dobos, B., Mellor, D., & Pikó, B. (2024). Exploring Fear of Happiness Among University Students: The Role of Perfectionism, Academic Burnout, Loneliness, and 



10 

**E-ISSN: 2981-2526** 

Fúnez et al.                                                                                                           Journal of Adolescent and Youth Psychological Studies 7:6 (2026) 1-11 



Hopelessness. _Scandinavian journal of psychology_ , _65_ (3), 559-567. https://doi.org/10.1111/sjop.13001 

- Faiman, H. B., & Strouse, G. A. (2025). Perfectionism and Academic Burnout in High-Achieving Undergraduate Students. _Gifted Child Quarterly_ , _69_ (3), 269-284. https://doi.org/10.1177/00169862251326467 

- Flett, G. L., & Hewitt, P. L. (2022). Perfectionism and Problems in Learning, Performance, and Achievement. 173-199. https://doi.org/10.1037/0000289-009 

- Gaudreau, P., & Benoît, A. (2024). Be Careful What You Wish For: The Double-Edged Sword of Perfectionism During Graduate Studies. https://doi.org/10.31234/osf.io/zxqvf 

- Gaudreau, P., & Benoît, A. (2025). Distinguishing Perfectionism and Excellencism in Graduate Students: Contrasting Links With Performance Satisfaction, Research Self‐efficacy, Burnout, and Dropout Intentions. _British Journal of Psychology_ , _116_ (4), 907-929. https://doi.org/10.1111/bjop.12798 

- Hawkins, S., & Mackinnon, S. P. (2024). Perfectionism and Stress as Predictors of Academic Self-Efficacy, Self-Concept, and Burnout: A Test of the Vulnerability Stress Model. https://doi.org/10.31234/osf.io/g2r95 

- Hawkins, S., & Mackinnon, S. P. (2025). Does Perfectionism Moderate the Relationship Between Postsecondary Student Stress and Academic Self-Efficacy, Self-Concept, and Burnout? _Canadian Journal of Behavioural Science/Revue canadienne des sciences du comportement_ . https://doi.org/10.1037/cbs0000466 

- Journault, A. A., Bilodeau-Houle, A., Duplessis-Marcotte, F., Plante, I., Giguère, C. É., & Lupien, S. (2023). Beyond Individual Factors: Contextual Factors Matter for Students’ Test Anxiety_Preprint. https://doi.org/10.31219/osf.io/y45h9 

- Kim, S. (2022). Students’ Perceptions of the Learning Environment at a Medical School in Korea: Comparisons of the Most Recent 4 Years’ Results Using the Dundee Ready Education Environment Measure (DREEM). _Kosin Medical Journal_ , _37_ (4), 299-310. https://doi.org/10.7180/kmj.22.129 

- Klein, H. J., & McCarthy, S. M. (2022). Student Wellness Trends and Interventions in Medical Education: A Narrative Review. _Humanities and Social Sciences Communications_ , _9_ (1). https://doi.org/10.1057/s41599-022-01105-8 

- Lin, J., & Guo, W. (2024). The Research on Risk Factors for Adolescents’ Mental Health. _Behavioral Sciences_ , _14_ (4), 263. https://doi.org/10.3390/bs14040263 

- Liu, C., & Berzenski, S. R. (2022). College Academic Perfectionism Scale: Development and Validation. _Journal of Psychoeducational Assessment_ , _40_ (4), 465-481. https://doi.org/10.1177/07342829211069799 

   - Pereira, A. T., Brito, M. J., Cabaços, C., Carneiro, M., Carvalho, F., Manão, A. A., Araújo, A. I., Pereira, D., & Macedo, A. (2022). The Protective Role of Self-Compassion in the Relationship Between Perfectionism and Burnout in Portuguese Medicine and Dentistry Students. _International journal of environmental research and public health_ , _19_ (5), 2740. https://doi.org/10.3390/ijerph19052740 

   - Qin, L., Lü, J., Zhou, Y., Wijaya, T. T., Huang, Y., & Fauziddin, M. (2022). Reduction of Academic Burnout in Preservice Teachers: PLS-SEM Approach. _Sustainability_ , _14_ (20), 13416. https://doi.org/10.3390/su142013416 

   - Ramadhana, D., Basthomi, Y., & Zen, E. L. (2023). Correlation Analysis of Academic Perfectionism, Self-Efficacy, and Burnout Among English Department Learners. _Voices of English Language Education Society_ , _7_ (2), 300-311. https://doi.org/10.29408/veles.v7i2.18309 

   - Sanseverino, D., Molinaro, D., Spagnoli, P., & Ghislieri, C. (2023). The Dynamic Between Self-Efficacy and Emotional Exhaustion Through Studyholism: Which Resources Could Be Helpful for University Students? _International journal of environmental research and public health_ , _20_ (15), 6462. https://doi.org/10.3390/ijerph20156462 

   - Setiyowati, A. J., Rachmawati, I., Wiyono, B. B., Indreswari, H., & Laksana, E. P. (2024). Analysis of the Structural Relationship Emotional Regulation, Academic Procrastination, and Academic Burnout. _International Journal of Evaluation and Research in Education (Ijere)_ , _13_ (3), 1895. https://doi.org/10.11591/ijere.v13i3.26778 

   - Yaacob, Z., Zakaria, N., Mokhtar, M., Jalal, S. F., Pati, K. M. I., & Rahmat, N. H. (2023). Exploring Students’ Fatigue: Is There a Relationship Between Outcome With Effort and Performance? _International Journal of Academic Research in Business and Social Sciences_ , _13_ (9). https://doi.org/10.6007/ijarbss/v13-i9/17731 

   - Yin, Y., Parpala, A., & Toom, A. (2024). International Students’ Burnout and Self-Efficacy Profiles and Their Relation to Writing Conceptions. _Research in Comparative and International Education_ , _19_ (2), 175-196. https://doi.org/10.1177/17454999241232241 

   - Zhang, L., Liu, L., Wang, P., Wu, X., & Wang, W. (2025). Parents’ Behavioural Control Affects Chinese College Students’ School Burnout and Perceived Employment Stress: Different Effects via Self-Oriented, Other-Oriented, and Socially Prescribed Perfectionism. _Emerging Adulthood_ , _13_ (2), 395409. https://doi.org/10.1177/21676968241312263 

- Ma, Y. (2021). Analysis on the Reasons of Academic Burnout Among Chinese Adolescents. https://doi.org/10.2991/assehr.k.211217.002 

- Mahsood, N., Mahboob, U., Asim, M., & Shaheen, N. (2025). Assessing the Well-Being of PhD Scholars: A Scoping Review. _BMC psychology_ , _13_ (1). https://doi.org/10.1186/s40359-025-02668-2 

- Ménard, A. D., & Chittle, L. (2023). The Impostor Phenomenon in Post‐secondary Students: A Review of the Literature. _Review of Education_ , _11_ (2). https://doi.org/10.1002/rev3.3399 

- Ok, F., Karip, B., & Baydili, K. N. (2025). Impostor Syndrome and Its Association With Anatomical Self‐efficacy in Medical Students in Turkiye. _Anatomical Sciences Education_ . https://doi.org/10.1002/ase.70116 

- Osenk, I., Johnson, C., & Wade, T. (2022). A Pragmatic Randomized Controlled Trial Targeting Perfectionism in Young Adolescents. _School Mental Health_ , _15_ (1), 151-164. https://doi.org/10.1007/s12310-022-09540-3 



11 

**E-ISSN: 2981-2526** 

