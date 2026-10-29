# Model plan review

Recommendation: keep ridge as the main candidate and add one limited Random Forest regression comparison. Keep linear regression and the constant-score baselines as reference points.

Reviewed: 29 October 2026. This is a recommendation before training, not a result or an approved experiment change.

## What I checked

I read the current [model plan](prediction-experiment.md) and all 49 titles in [papers.csv](../references/papers.csv). I examined the burnout and stress records, then checked selected original publisher pages, abstracts, and available full text. This is a focused review, not a systematic review or a complete audit of every paper's methods.

The CSV summaries help find papers, but they should not replace reading the original sources. The studies below use different outcomes, samples, and inputs. Their results are not expected performance targets for our dataset.

## Models in relevant papers

| Paper in the CSV | Sample | Models reported | What it means for us |
|---|---|---|---|
| B and Jeyachidra, 2026: university burnout framework | 1,250 university students | XGBoost, Random Forest, SVM, Explainable Boosting Machine | Supports considering a nonlinear comparison; its risk-classification accuracy does not estimate performance on our continuous score. Checked publisher abstract. [Paper](https://ieeexplore.ieee.org/abstract/document/11484289/figures) |
| Yeskuatov et al., 2025: computing-student burnout | 565 analyzed records, after recruiting 688 | Logistic regression, SVM, naive Bayes, decision tree, XGBoost | Logistic regression achieved the highest exhaustion F1, 68.4%. A more complex algorithm did not automatically win. Inputs were university records, not our questionnaire. Checked publisher text. [Paper](https://doi.org/10.3390/healthcare13233182) |
| Mahfouz and Minyi, 2026: high-school burnout | 1,042 high-school students | An ensemble combining Random Forest, Gradient Boosting, and XGBoost | Reports continuous-score errors and nested cross-validation. This is closer to our outcome type, but uses a different population and much more data. Checked publisher abstract. [Paper](https://journals.kmanpub.com/index.php/jayps/article/view/4989) |
| Omarbekova et al., 2026: student stress | Two datasets: 777 and 1,100 | Logistic regression, Random Forest, Gradient Boosting, RBF SVM, multilayer perceptron | Uses stress categories. The authors report the highest accuracy for Random Forest and highest AUC for logistic regression. Checked full text. [Paper](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1886274/full) |
| Feher et al., 2024: teacher burnout | 1,576 teachers | Random Forest, SVM, decision tree, logistic baseline; also elastic net regression for continuous scores | A useful example of regularized regression for burnout scores, although teachers differ from our students. Checked full text. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11348772/) |

SVM means support vector machine. EBM means Explainable Boosting Machine. Elastic net is a regression method that restrains weights and can also remove some inputs.

Other relevant CSV records include Pereira et al. (Random Forest, XGBoost, SVM; 274 psychology students) and Rahmadani and Sriani (C5.0 classification; 306 students). These reinforce that tree and support-vector methods appear in this literature. They do not establish which model will work best here. See [Pereira et al.](https://doi.org/10.3390/bs15040505) and [Rahmadani and Sriani](https://ejurnal.stmik-budidarma.ac.id/index.php/jurikom/article/view/9550). Pereira's model list and sample here come from the local CSV abstract; its complete methods were not accessible in this review.

Do not copy every statistical procedure from a published paper. For example, the Omarbekova article treats repeated validation-fold scores as independent in its model-comparison testing. Shared students make those scores dependent, so that approach should not be copied into our single-dataset experiment.

## Are the current models enough?

They are defensible for an initial exploratory prediction study. Their actual usefulness is still unknown. Only evaluation can show whether they predict well enough for the intended use, and that use needs a defined improvement criterion.

The mean-score baseline is a reference: it ignores student answers and predicts the training average. Beating it shows that a learned model adds information. Linear regression tests simple average trends; ridge tests similar trends while limiting large weights.

The main gap is that both learned models are linear in the encoded inputs. They can miss curved relationships and interactions, such as a workload association that differs by sleep category. Such patterns are possibilities to test, not findings from our data.

With only 97 students, a five-fold outer training group contains about 77 or 78 students. Category encoding also increases the number of input columns: the eight Set B questions become about 11 columns with the observed sleep and study-hour categories, before the intercept. This supports a limited comparison and careful regularization. It does not create a rule that complex models are forbidden below a fixed sample size.

## Recommended comparison

| Approach | Role |
|---|---|
| Training-mean and training-median baselines | References for whether questionnaire inputs help |
| Linear regression | Simple, interpretable comparison |
| Ridge regression | Preferred starting candidate, pending evaluation |
| Random Forest regressor with small trees | One nonlinear challenger |

Add the median baseline because MAE is our primary measure: the median minimizes absolute error for a constant prediction. Keep the mean baseline for continuity and squared-error comparisons. Both must use the training students alone. The software supports [both constant strategies](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html).

My choice of Random Forest is a practical judgment based on the research question and literature, not evidence that it will beat ridge on our data. Limit tree depth and require several training students per final branch. For example, depths of 2 or 3 and minimum leaf sizes of 5 or 10 could form a small proposed tuning grid. Fix the grid before evaluation and tune inside training groups. These settings are starting proposals, not validated optimum values. The [Random Forest documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) explains these controls.

I would leave XGBoost, EBM, neural networks, stacking, and a large SVM search outside the first experiment. They remain possible later comparisons with a clear purpose. More algorithms mean more opportunities to select a chance result; [Cawley and Talbot](https://www.jmlr.org/beta/papers/v11/cawley10a.html) study this selection problem.

## What to keep from the plan

Keep the continuous BAT score, both input sets, and identical outer validation splits. Exclude all BAT-derived inputs and keep preprocessing and tuning within training groups. Compare Set A with Set B within each algorithm so adding AI questions is the only input-set change.

Document why Set A omits other measured context variables such as academic stress and GPA. Any added value from Set B is relative to the chosen Set A, not proof that AI habits matter beyond every possible study condition. Do not select additions from the earlier p-values or interpret predictive improvement as a causal AI effect.

Use MAE as primary, RMSE and R-squared as supporting measures, and report paired error differences for the same students. Select ridge and Random Forest settings inside the inner validation step. If choosing the algorithm itself is part of the final training procedure, that choice also belongs inside the inner step when estimating the selected procedure's performance. Reporting the smallest outer error as an unbiased estimate of a selected winner would be optimistic.

A 97-response dataset can support an exploratory comparison. It cannot establish readiness for a student-support application by itself. A simpler model that predicts as well and is more stable is a reasonable final choice; the intended use and uncertainty still matter.

Next: record whether to add the limited Random Forest comparison and median baseline before implementing the experiment.
