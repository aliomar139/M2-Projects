---
marp: true
theme: gaia
paginate: true
backgroundColor: #f8fafc
color: #1e293b
style: |
  section {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    padding: 40px 60px;
  }
  h1 { color: #0f172a; }
  h2 {
    color: #034fa6;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
  }
  footer { font-size: 0.55rem; color: #64748b; }
  table { font-size: 0.75rem; }
---

<!-- Slide 1 -->
# Prescriptive analytics
### Decision-making in the data science life cycle

The data science life cycle includes defining a problem, preparing data, building models, evaluating results, and putting them into use.

**Prescriptive analytics uses data, goals, and constraints to recommend an action.**

<!-- Speaker opening: Hello everyone, and thank you for being here. -->

---

<!-- Slide 2 -->
## The data science life cycle

| Phase | Purpose |
|:--|:--|
| Business understanding | Define the problem and what success means |
| Data understanding and preparation | Explore, clean, and organize the data |
| Modeling | Build models to answer the business questions |
| Evaluation | Check whether the results meet the goal |
| Deployment | Put the results into use and review their performance |

Prescriptive analytics supports decision-making within this cycle. Teams revisit earlier phases when data, goals, or results change.

<!-- Source: IBM CRISP-DM guide, https://www.ibm.com/docs/en/SS3RA7_18.5.0/pdf/ModelerCRISPDM.pdf -->

---

<!-- Slide 3 -->
## Four types of analytics

| Type | Role in data science | Retail example |
|:--|:--|:--|
| Descriptive | Summarize what happened | Report last month's sales by store |
| Diagnostic | Investigate why it happened | Examine whether stock shortages explain lower sales |
| Predictive | Estimate what may happen | Forecast next month's demand |
| **Prescriptive** | **Recommend what to do** | **Allocate stock to meet demand within supply limits** |

These types answer different questions within a project; they can work together rather than form a fixed sequence.

<!-- Source: IBM Think, https://www.ibm.com/think/topics/prescriptive-analytics -->

---

<!-- Slide 4 -->
## The role of prescriptive analytics

A forecast estimates demand. A prescriptive model recommends how to respond.

**Retail:** use demand estimates to decide how much stock each store receives.

**Delivery:** use travel-time estimates to select routes that meet delivery deadlines.

A recommendation should explain the proposed action, the expected result, and the main limits behind it.

---

<!-- Slide 5 -->
## The decision model

| Element | Meaning | Stock allocation example |
|:--|:--|:--|
| Decision variables | Choices the model can change | Units sent to each store |
| Objective | The outcome to improve | Maximize expected contribution |
| Constraints | Limits the solution must respect | Available stock and store capacity |
| Inputs | Data and estimates used in the model | Demand estimates and value per unit |

A feasible plan meets the constraints. An optimal plan achieves the best objective value within the model.

---

<!-- Slide 6 -->
## The recommendation process

1. Define the decision, goal, and rules with the decision owner.
2. Prepare the data and estimate relevant future conditions.
3. Build a model of actions, outcomes, and constraints.
4. Compare feasible plans and test important assumptions.
5. Review the recommendation, act, and measure the result.

Actual results feed back into the next decision.

---

<!-- Slide 7 -->
## Methods used in prescriptive analytics

| Method | What it does | Example |
|:--|:--|:--|
| Mathematical optimization | Searches for the best objective value within constraints | Allocate a limited stock supply |
| Constraint programming | Finds assignments that satisfy detailed rules | Schedule staff with different skills and availability |
| Simulation | Estimates outcomes under changing or uncertain conditions | Compare staffing plans under different demand levels |

Simulation helps evaluate a plan; a selection rule or optimization method decides which plan to recommend.

<!-- Sources: Google OR-Tools, https://developers.google.com/optimization/introduction/cpp; IBM Monte Carlo simulation, https://www.ibm.com/think/topics/monte-carlo-simulation -->

---

<!-- Slide 8 -->
## Worked example: allocating limited stock

A retailer has **100 units** to allocate. The goal is to maximize expected contribution, the amount each sale adds after variable costs.

| Store | Expected contribution per unit | Maximum allocation |
|:--|--:|--:|
| A | $12 | 60 units |
| B | $9 | 80 units |

Let **xA** and **xB** be the units sent to each store.

**Maximize:** 12xA + 9xB

**Subject to:** xA + xB <= 100; 0 <= xA <= 60; 0 <= xB <= 80.

*Illustrative figures; whole units, constant contribution, and expected sales up to the stated limits.*

---

<!-- Slide 9 -->
## Comparing the allocation plans

| Plan | Store A | Store B | Expected contribution |
|:--|--:|--:|--:|
| Equal allocation | 50 units | 50 units | $1,050 |
| Optimized allocation | 60 units | 40 units | $1,080 |

Both plans respect the constraints. The optimized plan adds **$30** in expected contribution because more units go to the higher-value store.

The result is optimal for this model and its assumptions. Actual sales may differ.

---

<!-- Slide 10 -->
## Business rules change the recommendation

Suppose Store B must receive **at least 60 units** to meet a service commitment.

| Rules | Store A | Store B | Expected contribution |
|:--|--:|--:|--:|
| Original constraints | 60 | 40 | $1,080 |
| New minimum for B | 40 | 60 | $1,020 |

The new rule reduces expected contribution by **$60** while meeting the service commitment.

Prescriptive analytics makes this trade-off visible. The business decides which requirements to include.

---

<!-- Slide 11 -->
## Decisions under uncertainty

Demand, travel times, and available capacity can change. Test the recommendation against several plausible conditions.

- **Scenario analysis:** compare outcomes under low, expected, and high demand.
- **Sensitivity analysis:** check how the recommendation changes when an input or limit changes.
- **Risk limits:** set a service target or reserve to reduce the effect of a shortage.

A plan with the best average result may expose the business to a larger loss in a difficult scenario.

---

<!-- Slide 12 -->
## Applications across industries

| Area | Prescriptive decision | Goal and limits |
|:--|:--|:--|
| Supply chain | Allocate and replenish stock | Meet demand within supply and storage limits |
| Transport | Assign vehicles and routes | Reduce cost while meeting delivery windows |
| Manufacturing | Schedule production | Meet orders within machine and labor capacity |
| Hospital operations | Assign staff and rooms | Meet care needs within skills and availability |
| Customer service | Prioritize requests | Reduce waiting while handling urgent cases |

Each application links a specific action to a measurable goal.

---

<!-- Slide 13 -->
## Benefits and limitations

Prescriptive analytics can help teams use limited resources, compare alternatives, and explain the trade-offs behind a plan.

Its value depends on the model:

- A narrow objective can overlook service quality or fairness.
- Incomplete data can distort expected outcomes.
- Missing constraints can produce a plan the team cannot carry out.
- Conditions may change after the recommendation.

Human judgment remains part of the decision.

---

<!-- Slide 14 -->
## Putting the model into use

Start with a limited pilot and compare recommendations with the current approach.

Give the decision owner a clear view of the action, expected result, assumptions, and important constraints.

Define who can approve a recommendation and what happens when the model cannot find a feasible plan.

Monitor actual results and update the data or model when conditions change.

---

<!-- Slide 15 -->
## Evaluating a recommendation

Success means improving the real decision, so evaluate both the plan and the results.

| Measure | What to check |
|:--|:--|
| Business outcome | Cost, contribution, waiting time, or service level |
| Feasibility | Whether the plan respects required limits |
| Stability | Whether small input changes cause large plan changes |
| Practical use | Whether the team can understand and carry out the plan |

Compare with a relevant baseline and use actual results to improve the next recommendation.

---

<!-- Slide 16 -->
## Prescriptive analytics in data science

Descriptive analytics summarizes results. Diagnostic analytics investigates causes, while predictive analytics estimates future conditions.

**Prescriptive analytics uses this evidence to recommend actions that meet a goal within constraints.**

Its usefulness depends on sound data, a well-defined decision, and feedback from actual outcomes.

### Thank you. Questions?
