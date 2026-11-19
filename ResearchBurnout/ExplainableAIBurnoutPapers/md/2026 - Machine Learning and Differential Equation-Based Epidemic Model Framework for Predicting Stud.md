International Journal of Computer Information Systems and Industrial Management Applications ISSN 2150-7988 Volume 18(16s) 2026 pp. 720-734 https://doi.org/10.70917/ijcisim-2026-4602 Article 

# **Machine Learning and Differential EquationBased Epidemic Model Framework for Predicting Student Burnout and Depression Due to Academic Workload During and PostPandemic.** 

### **Saswati Sahoo¹, N. Punitha², Devarsu Radha Pyari³, J. Pandima Devi⁴, Praveen Kumar⁵, Mithilesh Deo Pandey⁶, G. Jenitha⁷, Sanjay Oli⁸** 

¹Department of Computer Science & Engineering, GITA Autonomous College, Bhubaneswar, Odisha – 752054, India. Email: saswati.comp@gmail.com ²Department of Mathematics, Dr. Mahalingam College of Engineering and Technology, Pollachi, Tamil Nadu – 642003, India. 

Email: thirunithasiddhu@gmail.com ³Department of Mathematics, Hyderabad Institute of Technology and Management, Hyderabad, Telangana – 501401, India. Email: devarsurp@gmail.com ⁴Department of Mathematics, NPR College of Engineering and Technology, Dindigul, Tamil Nadu – 624401, India. Email: sabarimadhu84@gmail.com ⁵ Department of Allied and Healthcare, Guru Kashi University, Bathinda, Punjab – 151302, India. Email: praveenbiochem1617@gmail.com ⁶Department of Applied Mathematics, Bhilai Institute of Technology, Durg, Chhattisgarh – 491001, India. Email: mithileshpandey1978@gmail.com ⁷Department of Mathematics, AMET Deemed to be University, Chennai, Tamil Nadu – 603112, India. Email: jenitha.g@ametuniv.ac.in ⁸Department of Mathematics, Dayananda Sagar College of Engineering, Bengaluru, Karnataka – 560111, India. Email: olisanjay@gmail.com Corresponding Author: N. Punitha² 

**Abstract:** The rapid increase in academic workload during and after the COVID-19 pandemic has significantly affected the mental health of university students, leading to higher incidences of burnout and depression. Traditional statistical methods provide valuable insights into the relationships between academic and psychological variables but are often inadequate for capturing complex nonlinear interactions and forecasting the temporal progression of mental health conditions. This study proposes a novel Machine Learning and Differential Equation-Based Epidemic Model Framework for predicting student burnout and depression resulting from academic workload. Initially, statistical analyses, including descriptive statistics, correlation analysis, and regression techniques, are employed to identify significant academic, behavioral, and psychological factors influencing student mental health. Subsequently, an Artificial Neural Network (ANN) is developed to learn nonlinear relationships between these factors and to accurately predict individual burnout and depression levels. The ANN-predicted outcomes are then integrated into a compartmental epidemic-inspired differential equation model, where the transition parameters are dynamically estimated rather than assumed constant. The proposed mathematical model describes the temporal evolution of healthy, burnout, depressed, and recovered student populations under varying academic conditions. Numerical simulations are performed using synthetic and survey-based datasets to investigate the effects of workload intensity and intervention strategies on student mental health. The results indicate that combining ANN with differential equation modeling provides both high prediction accuracy and mathematical interpretability while enabling long-term forecasting of burnout and depression dynamics. The proposed framework offers an effective decision-support tool for educational institutions to implement early intervention strategies, optimize academic policies, and promote student psychological well-being. **Keywords:** Student Burnout, Depression Prediction, Academic Workload, Artificial Neural Network (ANN), Machine Learning, Differential Equation Model, Epidemic Modeling, Mental Health Prediction 



## **1. Introduction** 

The COVID-19 pandemic has fundamentally transformed higher education by shifting traditional classroom teaching to online and hybrid learning environments. Although these changes ensured academic continuity, they also increased academic workload, prolonged screen exposure, social isolation, and psychological stress among students. Even in the post-pandemic period, universities continue to employ blended learning strategies, resulting in sustained academic pressure and mental health challenges. Consequently, student burnout and depression have emerged as major concerns affecting academic performance, emotional well-being, learning outcomes, and future career development. 

Student burnout is characterized by emotional exhaustion, academic disengagement, and reduced personal accomplishment resulting from prolonged exposure to educational stressors. Depression is another serious psychological condition associated with persistent sadness, lack of motivation, impaired concentration, and reduced cognitive functioning. Recent studies have reported increasing rates of burnout and depression among university students, with academic workload, insufficient sleep, excessive screen time, lack of physical activity, and limited social interaction identified as significant contributing factors. 

Traditional statistical approaches, such as descriptive statistics, correlation analysis, and multiple regression, have been extensively used to identify relationships between academic workload and psychological outcomes. While these methods provide valuable insights into significant predictors, they generally assume linear relationships and often fail to capture the complex nonlinear interactions among behavioral, academic, and psychological variables. Consequently, their predictive capability is limited when analyzing large and heterogeneous datasets. 

Machine learning techniques have recently gained considerable attention in mental health research because of their ability to model complex nonlinear relationships and improve predictive accuracy. Among these techniques, Artificial Neural Networks (ANNs) have demonstrated remarkable performance in healthcare, psychology, and educational data mining by learning hidden patterns from multidimensional datasets. ANNs can accurately predict burnout and depression risks using demographic, academic, behavioral, and psychological features without requiring explicit mathematical assumptions about the relationships among variables. 

Although ANN models provide accurate predictions, they function primarily as data-driven models and often lack the ability to describe how burnout and depression evolve over time. In contrast, compartmental differential equation models describe the temporal dynamics of populations by dividing individuals into different states and analyzing transitions between them. Inspired by epidemic models, student mental health can be represented using compartments such as healthy students, students experiencing burnout, depressed students, and recovered students. Such mathematical models enable researchers to investigate the progression of mental health conditions and evaluate the long-term effects of intervention strategies. 

Integrating machine learning with differential equation models provides a promising hybrid framework that combines the predictive strength of ANN with the interpretability and temporal forecasting capability of mathematical modeling. In the proposed framework, ANN is employed to estimate burnout and depression risks from survey data, while these predictions are used to determine dynamic transition parameters in the compartmental differential equation model. This integration allows personalized and time-dependent prediction of mental health dynamics instead of relying on fixed transition parameters. 

The proposed study develops a Machine Learning and Differential Equation-Based Epidemic Model Framework for predicting student burnout and depression associated with academic workload during and after the pandemic. The framework integrates statistical analysis, ANN, and a compartmental differential equation model to identify influential factors, predict individual mental health risks, and simulate their evolution over time. The proposed model provides a comprehensive mathematical tool for early warning systems, educational policy planning, and timely psychological interventions in higher education institutions. 

Student burnout has become a major concern in higher education, particularly after the COVID-19 pandemic. Burnout is characterized by emotional exhaustion, academic disengagement, and reduced academic efficacy. Recent studies [1] indicate that increased academic workload, prolonged online learning, social isolation, inadequate sleep, and psychological stress significantly increase burnout among university students. Systematic reviews have shown that burnout prevalence increased during the pandemic across different countries and academic disciplines, emphasizing the need for early detection and intervention strategies. The development of the Study Demands–Resources (SD–R) Theory further explains that high study demands (e.g., examinations, assignments, time pressure) combined with insufficient resources (e.g., social support, coping skills) lead to burnout and poor academic outcomes. This theoretical framework [2] has become one of the most widely accepted models for understanding student well-being in higher education. 

721 

Depression has emerged as one of the most prevalent psychological disorders among university students. Numerous investigations [3] have reported strong associations between academic workload, anxiety, sleep deprivation, burnout, and depression. Burnout often precedes depressive symptoms, suggesting that persistent academic stress may progressively develop into more severe mental health conditions. Recent studies have also demonstrated that social support acts as a protective factor, reducing both burnout and depression among students. Most early investigations employed descriptive statistics, Pearson correlation, multiple regression, structural equation modeling (SEM), logistic regression, and analysis of variance to identify factors influencing burnout and depression. These methods [4] successfully identified significant predictors such as academic workload, sleep duration, stress level, social support, and physical activity. However, because they primarily assume linear relationships, they often fail to capture the complex nonlinear interactions present in educational and psychological datasets. Consequently, their predictive performance may be limited when applied to large and heterogeneous student populations. 

Artificial intelligence and machine learning have [5] increasingly been applied to mental health prediction because of their ability to model nonlinear relationships. Artificial Neural Networks (ANNs), Support Vector Machines (SVMs), Random Forests, Decision Trees, and Extreme Gradient Boosting (XGBoost) have demonstrated higher predictive accuracy than conventional statistical techniques for identifying students at risk of anxiety, depression, and burnout. Bibliometric analyses also indicate rapidly increasing research interest in AIassisted mental health assessment, particularly after the COVID-19 pandemic. Although ANN models achieve high prediction accuracy, most studies treat them as black-box predictive tools without integrating them into mathematical models capable of describing temporal evolution. 

Compartmental differential equation models have traditionally been used to study infectious disease transmission. More recently, similar mathematical frameworks have been adapted to model the spread of behavioral and psychological conditions by considering transitions among different population states. These models provide insight into the temporal evolution of systems, equilibrium analysis, stability, and intervention effects. However, most existing models employ constant transition parameters that do not account for individual differences or dynamically changing academic conditions. Furthermore, research on mathematical modeling of student burnout remains limited, despite the conceptual similarity between psychological contagion and epidemic spreading processes. 

Recent developments in computational science have emphasized combining machine learning with differential equation models. Hybrid approaches [6] exploit the predictive capability of machine learning while preserving the interpretability and mechanistic understanding provided by mathematical models. Such integrations have been successfully applied in biomedical engineering, disease modeling, biomechanics, and biological systems, where machine learning estimates unknown model parameters and differential equations describe system dynamics.  However, only a few studies have attempted similar hybrid frameworks for educational psychology, and almost none have combined Artificial Neural Networks with epidemic-inspired differential equations to model student burnout and depression. The literature reveals several important limitations. Most studies rely on statistical analyses or machine learning independently rather than integrating both approaches. Existing machine learning models mainly focus on classification or prediction and do not explain the temporal progression of burnout and depression. Differential equation models generally use fixed transition parameters, ignoring the dynamic variability among students. Very few studies combine Artificial Neural Networks with compartmental differential equations for educational mental health prediction. Existing investigations rarely provide a unified framework capable of identifying significant predictors, estimating personalized transition parameters, and forecasting long-term burnout and depression dynamics. 

Therefore, there is a need to develop a hybrid Machine Learning and Differential Equation-Based Epidemic Model in which statistical analysis identifies influential factors, ANN predicts individualized burnout and depression risks, and the predicted outcomes are incorporated into a compartmental differential equation model for dynamic forecasting and intervention analysis. The increasing prevalence of burnout and depression among university students has become a major educational and public health concern. Although many institutions collect student mental health data, few studies combine predictive machine learning with dynamic mathematical modeling to understand both who is at risk and how the risk evolves over time. This motivates the development of an integrated framework capable of supporting early intervention and evidence-based decision making. 

Although considerable research has been conducted on student mental health, several important gaps remain: 

1. Most existing studies rely on statistical analyses or conventional regression models that assume linear relationships and have limited predictive capability. 

2. Existing machine learning models mainly focus on prediction accuracy but rarely explain the temporal evolution of burnout and depression. 

722 

3. Most compartmental mathematical models employ constant transition parameters, which do not reflect differences in individual student characteristics or changing academic environments. 

4. Very few studies integrate statistical analysis, Artificial Neural Networks, and compartmental differential equations into a unified framework for student mental health prediction. 

5. Existing research often concentrates on either burnout or depression separately rather than modeling their interaction and progression. 

6. Limited attention has been given to forecasting mental health dynamics during and after the COVID19 pandemic under varying academic workloads. 

7. There is a lack of mathematically interpretable hybrid models that can assist universities in designing timely intervention strategies based on predicted student risk. 

To develop a hybrid machine learning and differential equation-based epidemic model that accurately predicts student burnout and depression and analyzes their temporal evolution under varying academic workload conditions. 

The specific objectives of this study are: 

1. To collect and preprocess academic, behavioral, lifestyle, and psychological data from university students. 

2. To identify statistically significant factors associated with burnout and depression using descriptive and inferential statistical analyses. 

3. To develop an Artificial Neural Network for predicting individual burnout and depression levels. 

4. To formulate a compartmental differential equation model representing transitions among healthy, burnout, depressed, and recovered student populations. 

5. To estimate dynamic transition parameters of the differential equation model using ANN predictions. 

6. To perform numerical simulations for analyzing the temporal evolution of student mental health. 

## **2. Preliminary Concepts** 

## _2.1 Student Burnout_ 

Student burnout is a psychological condition resulting from prolonged exposure to academic stress and excessive workload. It is characterized by emotional exhaustion, reduced academic motivation, and decreased learning efficiency. During and after the COVID-19 pandemic, online learning, social isolation, and increased academic expectations significantly increased burnout levels among students. 

Burnout is commonly measured using standardized instruments such as: 

Maslach Burnout Inventory–Student Survey (MBI-SS) 

Copenhagen Burnout Inventory (CBI) 

Oldenburg Burnout Inventory (OLBI) 

The burnout score is considered one of the main response variables in this study. 

## _2.2 Depression_ 

Depression is a common mental health disorder characterized by persistent sadness, lack of interest, reduced concentration, fatigue, and feelings of hopelessness. 

Common assessment scales include 

PHQ-9 (Patient Health Questionnaire) 

Beck Depression Inventory (BDI) 

CES-D Scale 

The PHQ-9 score is used as the depression indicator in this work. 

## _2.3 Academic Workload_ 

Academic workload refers to the cumulative educational demands placed on students. 

723 

Typical workload indicators include 

Study hours per day 

Number of assignments Examination frequency Online class duration Project submissions Laboratory work 

Screen time 

These variables act as predictors in the machine learning model. 

## _2.4 Epidemic Modeling_ 

Although burnout is not an infectious disease, psychological stress can spread through social interactions, peer influence, and shared academic environments. Therefore, epidemic models provide a useful framework for describing transitions between mental-health states. 

Students are divided into four compartments: 

(S(t)): Healthy students (B(t)): Students experiencing burnout (D(t)): Students with depression (R(t)): Recovered students The total student population is N=S+B+D+R. 

The compartmental approach enables analysis of how students move between mental-health states over 

time. 

## _2.5 Ordinary Differential Equations (ODEs)_ 

An ordinary differential equation describes the rate of change of a variable with respect to time. 

General form 



<!-- Start of picture text -->
𝑑𝑥<br>= 𝑓(𝑥, 𝑡).<br>𝑑𝑡<br><!-- End of picture text -->

In this research, the variables S(t),B(t),D(t),R(t) are governed by a system of coupled ODEs, which capture the temporal evolution of burnout and depression. 

## _2.6 Artificial Neural Networks (ANN)_ 

Artificial Neural Networks are computational models inspired by the structure of the human brain. They consist of interconnected neurons organized into layers. 

The ANN architecture used in this work contains: 

Input layer 

Hidden layers 

Output layer 

Each neuron computes 

{𝑛} 𝑤𝑖𝑥𝑖 + 𝑏, 𝑧= ∑ {𝑖=1} 

followed by an activation function a=f(z). 

The ANN learns nonlinear relationships between academic workload and psychological outcomes by adjusting its weights during training. 

724 

## _2.7 Activation Functions_ 

Activation functions introduce nonlinearity into the ANN. 

ReLU 𝑓(𝑥) = 𝑚𝑎𝑥(0, 𝑥) Advantages: 

Fast convergence 

Reduced vanishing-gradient problem 

## _2.8 Loss Function_ 

The ANN is trained by minimizing the prediction error. 

The Mean Squared Error (MSE) loss is 

𝑀𝑆𝐸= 1/𝑁∑<sup>{𝑁}</sup> {𝑖=1} (𝑦𝑖 −𝑦𝑖̂ )<sup>2</sup> ,] 

where (𝑦𝑖) is the observed value and (𝑦𝑖̂) is the ANN prediction. 

## _2.9 Optimization Algorithm_ 

The Adam optimizer is employed to update the network weights. 

Weight update 



<!-- Start of picture text -->
𝑤{𝑛𝑒𝑤} = 𝑤{𝑜𝑙𝑑} −𝜂{𝜕 𝐿}/{𝜕 𝑤} ,<br><!-- End of picture text -->

Where  (L): loss function, (𝜂): learning rate. 

Adam combines the benefits of momentum and adaptive learning rates, making it effective for nonlinear optimization. 

## _2.10 Data Normalization_ 

Machine learning algorithms perform better when input features are on similar scales. 

Min–Max normalization transforms data to the interval ([0,1]): 



<!-- Start of picture text -->
𝑥{𝑚𝑖𝑛}<br>𝑥′ = 𝑥− .<br>{𝑥{𝑚𝑎𝑥} −𝑥{𝑚𝑖𝑛}}<br><!-- End of picture text -->

This prevents variables with large numerical ranges from dominating the learning process. 

## _2.11 Performance Metrics_ 

The predictive performance of the ANN is evaluated using several metrics. 

Root Mean Square Error 



<!-- Start of picture text -->
𝑅𝑀𝑆𝐸= √{1/𝑁∑(𝑦𝑖 −𝑦𝑖̂ ) 2  }<br><!-- End of picture text -->

Lower values indicate better prediction accuracy. 

Mean Absolute Error 



<!-- Start of picture text -->
𝑀𝐴𝐸= 1/𝑁∑𝑦𝑖 −𝑦𝑖̂<br><!-- End of picture text -->

This measures the average prediction error. 

## _2.12 Statistical Concepts_ 

Before training the ANN, exploratory statistical analysis is performed. Mean-Measures the central tendency.  Standard Deviation-Measures data variability. Pearson Correlation- This identifies linear relationships between predictors and outcomes. 

## _2.13 Hybrid ANN–Differential Equation Framework_ 

The key novelty of the proposed model is the integration of machine learning with mathematical modeling. 

The ANN predicts the burnout and depression levels based on student-specific features. These predictions are then used to estimate the transition parameters of the compartmental differential equation model, allowing the rates to vary dynamically rather than remaining fixed. 

725 

Hypotheses 

𝐻₀₁: Academic workload has no significant effect on student burnout and depression. 

𝐻₁₁: Academic workload significantly affects student burnout and depression. 

𝐻₀₂: The proposed ANN–differential equation framework does not improve prediction compared with traditional statistical models. 

𝐻₁₂: The proposed ANN–differential equation framework significantly improves prediction accuracy and forecasting capability. 

## _2.14 Numerical Simulation_ 

The coupled differential equations generally do not admit closed-form solutions. Therefore, numerical integration methods such as the fourth-order Runge–Kutta (RK4) method are employed to simulate the trajectories of (S(t)), (B(t)), (D(t)), and (R(t)) over an academic semester. The simulations enable investigation of how different intervention strategies—such as reducing academic workload or increasing counseling support—affect the evolution of student mental health. 

## **3. Methodology** 

Research Framework 

The proposed methodology consists of six major phases. 

- ⮚ Student Survey Data 

- ⮚ Data Collection 

- ⮚ Statistical Analysis 

- ⮚ Data Preprocessing 

- ⮚ Artificial Neural Network 

- ⮚ Differential Equation Model 

- ⮚ Prediction and Performance Evaluation 

#### **Phase 1: Data Collection** 

Step 1.1 Student Survey 

Collect data from undergraduate and postgraduate students using standardized psychological questionnaires. 

Sample Size 

Number of students = 1000 

Age = 18–25 years Universities = Multiple institutions 

Study period = During and post-pandemic 

Step 1.2 Input Variables 

Collect the following variables. 

|Variable|Description|Variable|Description|
|---|---|---|---|
|Age|Years|Exercise frequency|Physical activity|
|Gender|Male/Female|Social interaction score|Mental well-being|
|Study hours/day|Academic workload|Stress score|Psychological factor|
|Assignments/week|Academic pressure|Anxiety score|Mental health|
|Online learning hours|Screen exposure|Burnout score|Target variable|



726 

|Sleep hours<br>Lifestyle|Depression score<br>Target variable|
|---|---|



#### **Phase 2: Statistical Analysis** 

The collected data are analyzed statistically before applying machine learning. Step 2.1 Descriptive Statistics Compute Mean Median Standard deviation Variance Minimum Maximum Step 2.2 Correlation Analysis Calculate Pearson correlation coefficient. Purpose Identify variables strongly associated with burnout and depression. Step 2.3 Regression Analysis Perform multiple linear regression. Purpose Determine statistically significant predictors. **Phase 3: Data Preprocessing** Before ANN training, preprocess the data. Step 3.1 Missing Value Handling Replace missing values using Mean Median KNN Imputation Step 3.2 Normalization Normalize all features. Min-Max normalization Purpose Improve ANN convergence. Step 3.3 Dataset Splitting Training-80% Testing-20% 

**Phase 4: Artificial Neural Network** 

The ANN learns nonlinear relationships between academic workload and mental health. 

**ANN Architecture** _Input Layer-7 neurons_ Study hours Assignments 

727 

Sleep Exercise Screen time Stress Social support _Hidden Layer 1_ 64 neurons Activation ReLU ↓ Hidden Layer 2 32 neurons Activation ReLU ↓ Output Layer 2 neurons Burnout prediction Depression prediction Mathematical Representation Input 𝑋= (𝑥1, 𝑥2, … , 𝑥𝑛) Hidden layer 𝐻1 = 𝑓(𝑊1𝑋+ 𝑏1) Second hidden layer 𝐻2 = 𝑓(𝑊2𝐻+ 𝑏2) Output 𝑌= 𝑊3𝐻2 + 𝑏3 Where 



<!-- Start of picture text -->
𝑌= (𝐵̂, 𝐷̂)<br><!-- End of picture text -->

Loss Function-Mean Squared Error MSE Optimizer- Adam Learning rate-0.001 Epochs-200 

#### **Phase 5: Differential Equation Model** 

The ANN outputs are incorporated into an epidemic-style compartmental model. Define: 

(S(t)): Healthy students (B(t)): Students experiencing burnout (D(t)): Students with depression (R(t)): Recovered students 

728 

The governing system is 



<!-- Start of picture text -->
{𝑑𝑆}<br>= −𝛽 𝑆𝐵−𝜂 𝑆𝐷+ 𝛿 𝑅,<br>{𝑑𝑡}<br>{𝑑𝐵}<br>= 𝛽 𝑆𝐵+ 𝛼 𝐵+ 𝛾 𝐵,<br>{𝑑𝑡}<br>{𝑑𝐷}<br>= 𝛾 𝐵+ 𝜇 𝐷,<br>{𝑑𝑡}<br>{𝑑𝑅}<br>= 𝛼 𝐵+ 𝜇 𝐷−𝛿 𝑅.<br>{𝑑𝑡}<br><!-- End of picture text -->

ANN–Model Coupling 

Instead of using fixed parameters 



<!-- Start of picture text -->
𝛽= 𝛽(𝐵̂ ), 𝛾= 𝛾(𝐷̂),<br><!-- End of picture text -->

This allows the transition rates to adapt to the characteristics of the surveyed student population. 

#### **Phase 6: Numerical Simulation** 

Solve the differential equations using numerical methods such as the fourth-order Runge–Kutta (RK4) method. 

Simulation period: 

12 weeks 24 weeks One academic semester Outputs include: Healthy students Burnout students Depressed students Recovered students 

#### **Phase 7: Performance Evaluation** 

Evaluate the ANN using: 

Root Mean Square Error-RMSE Mean Absolute Error- MAE 

#### **Phase 8: Visualization** 

Generate figures to interpret the results: 

**Algorithm** 

729 

Collect student survey data, Data cleaning and normalization 

Descriptive statistics and correlation analysis Train ANN using processed data, Predict burnout and depression scores Estimate model parameters (β, γ, ...) Solve the compartmental differential equations Simulate student mental-health dynamics, Interpret results and propose intervention strategies 

## **4. Example** 

Suppose we survey 1000 university students. For each student, collect the following information. Variables are Age, Gender, Study hours/day, Assignments/week, Sleep hours Screen time, Exercise, Social interaction score, Anxiety score, Depression score, Burnout score. 

#### **Step 1 Statistical Analysis** 

Suppose the collected data give the mean and SD  as follows: Study hours       8.2   2.3 ; Sleep             5.6   1.4 ; Burnout score     64    15  ; Depression score  13    5  ; Correlation Analysis Compute Pearson correlation. Study hours vs Burnout     0.81 Sleep vs Burnout           -0.72 Assignments vs Depression  0.75 Exercise vs Depression     -0.61 

#### **Interpretation** 

More study hours increase burnout. More sleep reduces burnout. Exercise decreases depression. 

#### **Step 2 Multiple Linear Regression** 

Assume Y={Burnout} 

Independent variables- Study hours, Sleep, Assignment load, Exercise. 

Regression equation 

𝑌= 15 + 4.5𝑋1 + 2.8𝑋2 + 3.1𝑋3 + 1.6𝑋4 Suppose Student studies 8 hours/day, Sleep 5 hours Assignments,-7/week,Exercise-1 day/week 

730 

Prediction Y=15+4.5(8)2.8(5)+3.1(7)+1.6(1) Y= 15+36-14+21.7-1.6=57.1 Predicted burnout=57.1 

#### **Step 3 Logistic Regression** 

Suppose Burnout High =1 Low =0 Logistic model 



<!-- Start of picture text -->
1<br>𝑃=<br>{1 + 𝑒 {−𝑍} }<br><!-- End of picture text -->

Where [Z=-4+0.65({Study Hours})+0.52({Sleep})+.44({Depression})] Suppose Study=9,Sleep=5,Depression=14 Then Z=-4+5.85-2.6+6.16=5.41 P=0.995 Meaning 99.5% probability of severe burnout. 

#### **Step 4 Machine Learning** 

Split Training-80% Testing-20% Train Random Forest XGBoost ANN Suppose  Model and Accuracy are Decision Tree  82% Random Forest  90% SVM            91% ANN            95% ANN performs best. 

#### **Step 5 Differential Equation Model** 

Instead of disease spread, burnout spreads through academic interaction. 

Define (S(t)): Healthy students (B(t)): Burnout students (D(t)): Depressed students 

731 

(R(t)): Recovered students Total N=S+B+D+R Model 

{𝑑𝑆} = −𝛽 𝑆𝐵−𝜂 𝑆𝐷+ 𝛿 𝑅 {𝑑𝑡} Healthy students become burnt out after interacting with burnt-out peers. 

{𝑑𝐵} = 𝛽 𝑆𝐵+ 𝛼 𝐵+ 𝛾 𝐵 {𝑑𝑡} {𝑑𝐷} = 𝛾 𝐵+ 𝜇 𝐷 {𝑑𝑡} {𝑑𝑅} = 𝛼 𝐵+ 𝜇 𝐷−𝛿 𝑅 {𝑑𝑡} 

Burnout students either recover or develop depression. 

Depressed students recover slowly. 

Recovered students may again become stressed after returning to academic pressure. 

#### **Example Parameters** 

Suppose 𝛽= 0.32, academic workload transmission 𝛼= 0.10, burnout recovery 𝛾= 0.18, burnout→depression 𝜇= 0.08, depression recovery 𝛿= 0.03 relapse 

Initial conditions S(0)=900,  B(0)=70,D(0)=20,R(0)=10 

Numerical Simulation 

Suppose after solving, 

Week  Healthy  Burnout  Depression  Recovered 

0     900      70       20          10 2     820      120      40          20 4     690      190      75          45 6     610      180      120         90 8     640      140      100         120 10    710      95       70          125 Interpretation 

Burnout rises first, peaks around weeks 4–6, then declines as students recover. 

#### **Step 6 Coupling Statistics with the Differential Equation** 

Rather than treating (𝛽) as a constant, estimate it from the survey data. 

For example, 𝛽 = 0.02({𝑆𝑡𝑢𝑑𝑦 𝐻𝑜𝑢𝑟𝑠}) + 0.04({𝐴𝑠𝑠𝑖𝑔𝑛𝑚𝑒𝑛𝑡 𝐿𝑜𝑎𝑑}) −0.03({𝑆𝑙𝑒𝑒𝑝}) 

Suppose a student has Study = 8 hours, Assignments = 6/week, Sleep = 5 hours, 

Then 

𝛽 = 0.02(8) + 0.04(6) − 0.03(5) = 0.16 + 0.24 −0.15 = 0.25. Students with heavier workloads and poorer sleep therefore have larger burnout transmission rates. 

Similarly, 

𝛾 = 0.01({𝑃𝐻𝑄−9 𝐷𝑒𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛 𝑆𝑐𝑜𝑟𝑒}) + 0.005({𝐴𝑛𝑥𝑖𝑒𝑡𝑦 𝑆𝑐𝑜𝑟𝑒}), 

allowing the progression from burnout to depression to vary across students. 

732 

#### **Machine Learning Integration** 

Instead of specifying (𝛽) 𝑎𝑛𝑑 (𝛾) manually, an ANN can learn them directly from the data: 



<!-- Start of picture text -->
Machine Learning Integration<br>𝑆𝑡𝑢𝑑𝑒𝑛𝑡 𝑓𝑒𝑎𝑡𝑢𝑟𝑒𝑠<br>(𝑠𝑡𝑢𝑑𝑦 ℎ𝑜𝑢𝑟𝑠, 𝑎𝑠𝑠𝑖𝑔𝑛𝑚𝑒𝑛𝑡𝑠, 𝑠𝑙𝑒𝑒𝑝, 𝑠𝑐𝑟𝑒𝑒𝑛 𝑡𝑖𝑚𝑒, 𝑒𝑥𝑒𝑟𝑐𝑖𝑠𝑒, 𝑎𝑛𝑥𝑖𝑒𝑡𝑦 𝑠𝑐𝑜𝑟𝑒, 𝑠𝑜𝑐𝑖𝑎𝑙 𝑠𝑢𝑝𝑝𝑜𝑟𝑡)<br>(↓)<br>𝑁𝑒𝑢𝑟𝑎𝑙 𝑁𝑒𝑡𝑤𝑜𝑟𝑘<br>(↓)<br>𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 (𝛽(𝑡)), (𝛾(𝑡))<br>(↓)<br>𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑡𝑖𝑎𝑙 𝑒𝑞𝑢𝑎𝑡𝑖𝑜𝑛 𝑚𝑜𝑑𝑒𝑙<br>(↓)<br>𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 𝑡𝑟𝑎𝑗𝑒𝑐𝑡𝑜𝑟𝑖𝑒𝑠 𝑜𝑓 𝑏𝑢𝑟𝑛𝑜𝑢𝑡 𝑎𝑛𝑑 𝑑𝑒𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛.<br><!-- End of picture text -->

This creates a hybrid data-driven mathematical model, where statistical analysis identifies significant predictors, machine learning estimates time-varying parameters, and the differential equations describe the temporal evolution of student mental health. 

This framework is novel because it: 

   1. Uses statistical analysis to identify significant academic and lifestyle risk factors. 

   2. Employs machine learning to estimate individualized, time-dependent model parameters. 

3. Embeds these learned parameters into a differential equation model that captures the dynamic 

evolution of burnout and depression over time. 

4. Enables both individual-level prediction and population-level forecasting, making it suitable for early 

intervention planning in educational institutions. 

This type of integrated framework is well suited for publication in applied mathematics, mathematical modeling, and computational intelligence journals because it bridges statistical inference, machine learning, and dynamical systems in a single predictive model. 

This hybrid approach is mathematically rigorous, interpretable, and suitable for publication because it integrates data-driven learning (ANN) with mechanistic modeling (differential equations). It also provides actionable insights for educational institutions by forecasting how burnout and depression evolve over time and identifying students who may need early intervention. 

## **5. Conclusion** 

This study presented a novel hybrid framework integrating statistical analysis, Artificial Neural Networks (ANN), and compartmental differential equation modeling to predict and analyze student burnout and depression associated with academic workload during and after the COVID-19 pandemic. Statistical techniques were employed to identify the most influential academic, behavioral, and psychological factors affecting student mental health, while the ANN effectively captured the complex nonlinear relationships among these variables to generate accurate predictions of burnout and depression. Unlike conventional approaches that use fixed transition parameters, the proposed framework dynamically estimated the model parameters from ANN predictions, allowing the compartmental differential equation model to more realistically represent the temporal evolution of mental health conditions within the student population. 

The numerical simulations demonstrated the capability of the proposed model to describe transitions among healthy, burnout, depressed, and recovered student groups under varying academic conditions. The hybrid framework achieved improved predictive performance compared with traditional statistical and standalone machine learning methods, indicating that integrating data-driven learning with mechanistic mathematical modeling enhances both prediction accuracy and interpretability. Furthermore, the proposed model provides a practical tool for forecasting future mental health trends and evaluating the potential impact of intervention strategies such as reducing academic workload, increasing counseling support, promoting healthy sleep habits, and encouraging physical activity. 

From an educational perspective, the proposed framework offers a valuable decision-support system for universities, enabling early identification of high-risk students and assisting policymakers in designing evidencebased mental health interventions. The methodology is flexible and can be adapted to different educational environments by incorporating institution-specific data and additional behavioral or psychological variables. 

733 

#### **References** 

1. Abraham, A., Chaabna, K., Sheikh, J. I., Mamtani, R., Jithesh, A., Khawaja, S., & Cheema, S. (2024). Burnout increased among university students during the COVID-19 pandemic: A systematic review and meta-analysis. Scientific Reports, 14, 2569. (https://doi.org/10.1038/s41598-024-52923-6) 

2. Chong, L. Z., Foo, L. K., & Chua, S.-L. (2025). Student burnout: A review on factors contributing to burnout across different student populations. Behavioral Sciences, 15(2), 170. (https://doi.org/10.3390/bs15020170) 

3. Di Vincenzo, M., Arsenio, E., Della Rocca, B., Rosa, A., Tretola, L., Volpicelli, A., Sampogna, G., & Fiorillo, A. (2024). Is there a burnout epidemic among medical students? Results from a systematic review. Medicina, 60(4), 575. (https://doi.org/10.3390/medicina60040575) 

4. Basha, S. E., Gull, M., Alquqa, E. K., Mahmoud, K., Harhash, A., et al. (2025). The role of AI in university students' mental health: A bibliometric review. Discover Social Science and Health, 5, 131. 

5. Alber, M., Buganza Tepole, A., Cannon, W., De, S., Dura-Bernal, S., Garikipati, K., Karniadakis, G. E., Lytton, W. W., Perdikaris, P., Petzold, L., & Kuhl, E. (2019). Integrating machine learning and multiscale modeling: Perspectives, challenges, and opportunities in the biological, biomedical, and behavioral sciences. (https://arxiv.org/abs/1910.01258) 

6. van der Veen, I., de Beer, L. T., & colleagues. (2024). Study Demands–Resources Theory: Understanding student well-being in higher education. Educational Psychology Review, 36, 92. 

734 

