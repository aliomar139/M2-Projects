# Prescriptive analytics: spoken script

This script follows the 16 slides in `prescriptive-analytics-presentation.md`. Use the slide headings to follow the order, and speak at a steady pace.

## Slide 1: Prescriptive analytics

Hello everyone, and thank you for being here. The data science life cycle goes through several stages: understanding the problem, preparing data, building models, evaluating results, and putting them into use. Within this process, prescriptive analytics helps turn analysis into a decision.


## Slide 2: The data science life cycle

The cycle begins with the business problem. We need to know what decision matters and how we will measure success. We then explore and prepare the data, build suitable models, and evaluate whether the results meet the goal. Deployment puts the results into use.

Prescriptive analytics can support the modeling and decision-making work within this cycle. The process is iterative: if results reveal a problem, we may return to the data, the model, or even the original goal.

Source: [IBM CRISP-DM guide](https://www.ibm.com/docs/en/SS3RA7_18.5.0/pdf/ModelerCRISPDM.pdf).

## Slide 3: Four types of analytics

Descriptive analytics represents the summary of the data. It tells us what happened; for example, how much each store sold last month.

Diagnostic analytics investigates why a result occurred. If sales fell, we might examine whether stock shortages explain the decrease. A possible explanation still needs evidence.

Predictive analytics estimates future conditions. For example, it can forecast demand for each store next month.

Prescriptive analytics supports the choice of action. It can recommend how much stock to send to each store, using demand estimates and available supply. These four types can work together within the same data science project.

Source: [IBM Think: prescriptive analytics](https://www.ibm.com/think/topics/prescriptive-analytics).

## Slide 4: The role of prescriptive analytics

Let us focus on prescriptive analytics. A forecast gives us an estimate of demand; the prescriptive model helps choose a response. In retail, that response may be an allocation of stock. In delivery planning, travel-time estimates can help choose routes that meet deadlines.

The recommendation should show what to do, what result to expect, and which limits shaped the plan. That makes it easier for the decision owner to review.

## Slide 5: The decision model

A decision model has four main elements. Decision variables describe what we can change, such as the number of units sent to each store. The objective states what we want to improve. Constraints describe the limits we must respect, and inputs supply the information used in the calculation.

A feasible plan follows the constraints. An optimal plan achieves the best objective value among the feasible choices in that model. Neither term guarantees that every assumption matches reality.

## Slide 6: The recommendation process

Begin by defining the decision with the person who owns it. Prepare the data and estimate the future conditions that matter. Then build a model connecting possible actions to their expected outcomes and limits.

Compare the feasible plans and test important assumptions before presenting a recommendation. After the team acts, measure the actual result. This feedback helps improve later decisions.

## Slide 7: Methods used in prescriptive analytics

Different decisions need different methods. Mathematical optimization searches for the best value of a goal while respecting constraints. It can be useful for allocating stock. Constraint programming works with detailed assignment rules, such as staff skills and availability.

Simulation helps estimate how plans perform under changing conditions, such as different levels of demand. To choose a recommendation, those simulated results still need a selection rule or an optimization step. Teams may combine methods when the problem requires it.

Sources: [Google OR-Tools](https://developers.google.com/optimization/introduction/cpp), [IBM: Monte Carlo simulation](https://www.ibm.com/think/topics/monte-carlo-simulation).

## Slide 8: Worked example: allocating limited stock

Consider a retailer with 100 units to allocate between two stores. Store A has an expected contribution of 12 dollars per unit and can receive up to 60 units. Store B contributes 9 dollars per unit and can receive up to 80. Contribution means the amount a sale adds after variable costs.

Our decision variables are the units allocated to A and B. The objective is to maximize their total expected contribution, subject to the available supply and each store's limit. These are illustrative figures with simplified assumptions.

## Slide 9: Comparing the allocation plans

An equal allocation sends 50 units to each store and produces an expected contribution of 1,050 dollars. The optimized plan sends 60 to A and 40 to B, giving 1,080 dollars. Both plans meet the constraints, but the second adds 30 dollars by allocating more units to the higher-value store.

That result follows the model's assumptions about contribution and sales. We still need to compare actual results with expectations.

## Slide 10: Business rules change the recommendation

Now add a service commitment: Store B must receive at least 60 units. With only 100 units available, the new optimal plan sends 40 to A and 60 to B. Expected contribution becomes 1,020 dollars.

The business gives up 60 dollars of expected contribution to meet that commitment. Prescriptive analytics shows the cost of the rule; the business decides whether the commitment belongs in the model.

## Slide 11: Decisions under uncertainty

The conditions behind a plan can change. Scenario analysis compares outcomes under different demand levels. Sensitivity analysis checks how a recommendation changes when an input or limit changes.

We can also include risk limits, such as a service target or a stock reserve. The best plan on average may perform poorly in a difficult situation, so we should examine the downside as well as the average result.

## Slide 12: Applications across industries

The same decision structure appears in many industries. Supply chain teams allocate stock, delivery teams assign vehicles and routes, and manufacturers schedule production. Hospital operations teams allocate staff and rooms, while customer service teams prioritize requests.

Each case needs a specific action, a measurable goal, and clear constraints. The model should reflect the actual work rather than a generic target.

## Slide 13: Benefits and limitations

Prescriptive analytics can make resource choices more systematic and help explain why one plan is preferable to another. However, the result depends on the way we define the problem.

A cost-only objective may harm service. Incomplete data may distort expected outcomes, while missing constraints may produce an unusable plan. Conditions can also change after the recommendation. People need to review these issues before relying on the result.

## Slide 14: Putting the model into use

Start with a limited pilot and compare the recommendations with the current approach. Show the decision owner the proposed action, expected result, assumptions, and important limits.

Define who can approve the recommendation and what to do if no feasible plan exists. Once the model is in use, monitor actual results and update it when the data or operating conditions change.

## Slide 15: Evaluating a recommendation

Evaluate the recommendation through the decision it supports. Did cost, contribution, waiting time, or service improve? Did the team follow the required limits? Was the plan stable when inputs changed slightly, and could people carry it out?

Compare these results with a relevant baseline. For a pilot, consider whether other changes affected the outcome before attributing an improvement to the model.

## Slide 16: Prescriptive analytics in data science

Descriptive analytics summarizes results, diagnostic analytics investigates causes, and predictive analytics estimates future conditions. Prescriptive analytics uses this evidence to recommend an action that meets a goal within constraints.

Its usefulness depends on sound data, a clear decision model, and feedback from actual outcomes. Thank you for your attention. I am happy to take your questions.
