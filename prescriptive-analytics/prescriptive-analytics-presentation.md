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

The data science life cycle includes understanding a problem, preparing data, building models, checking results, and using them in practice.

**Prescriptive analytics uses data, goals, and limits to suggest what to do.**

<!-- Speaker opening: Hello everyone, and thank you for being here. -->

---

<!-- Slide 2 -->
## The data science life cycle

| Stage | Purpose |
|:--|:--|
| Business understanding | Understand the problem and set the goal |
| Data understanding and preparation | Study, clean, and organize the data |
| Modeling | Build models to answer the business questions |
| Evaluation | Check whether the results meet the goal |
| Deployment | Use the results in practice and check how well they work |

Prescriptive analytics helps teams make decisions during this cycle. Teams can return to earlier stages when the data, goals, or results change.

<!-- Source: IBM CRISP-DM guide, https://www.ibm.com/docs/en/SS3RA7_18.5.0/pdf/ModelerCRISPDM.pdf -->

---

<!-- Slide 3 -->
## Four types of analytics

| Type | Role in data science | Store example |
|:--|:--|:--|
| Descriptive | Show what happened | Show last month's sales for each store |
| Diagnostic | Explain why it happened | Check whether stores sold less because products were not available |
| Predictive | Estimate what may happen | Predict next month's demand |
| **Prescriptive** | **Suggest what to do** | **Decide how much stock to send using the available supply** |

These types answer different questions in a project. They can work together, and teams do not always use them in the same order.

*Stock means the products available. Demand means how much customers want to buy.*

<!-- Source: IBM Think, https://www.ibm.com/think/topics/prescriptive-analytics -->

---

<!-- Slide 4 -->
## The role of prescriptive analytics

A forecast is a prediction, such as how much people may buy. A prescriptive model suggests what to do using that information.

**Stores:** use demand estimates to decide how much stock to send to each store.

**Delivery:** use predicted travel times to choose roads that allow delivery at the agreed time.

A suggestion should explain what to do, what result to expect, and which limits affected the choice.

---

<!-- Slide 5 -->
## The decision model

| Part | Meaning | Stock example |
|:--|:--|:--|
| Decision variables | What the model can change | Number of products sent to each store |
| Objective | The goal to improve | Meet as much demand as possible |
| Constraints | Rules and limits the plan must follow | Available stock and how much each store can use |
| Inputs | Information the model uses | Expected demand and current stock |

A feasible plan follows all the rules. An optimal plan gives the best result for the goal within the model.

---

<!-- Slide 6 -->
## The recommendation process

1. Agree on the decision, goal, and rules with the person responsible.
2. Prepare the data and estimate what may happen next.
3. Build a model that connects choices, results, and limits.
4. Compare plans that follow the rules and check what the model assumes.
5. Check the suggestion, use the plan, and measure the result.

Use the actual results to improve the next decision.

---

<!-- Slide 7 -->
## Methods used in prescriptive analytics

| Method | What it does | Example |
|:--|:--|:--|
| Mathematical optimization | Finds the best result for a goal while following the rules | Decide how to share limited stock |
| Constraint programming | Finds a plan that follows detailed rules | Choose working hours based on workers' skills and availability |
| Simulation | Estimates results when conditions change or are uncertain | Compare staff plans for different demand levels |

Simulation helps test a plan. A rule for choosing plans or an optimization method decides which one to suggest.

<!-- Sources: Google OR-Tools, https://developers.google.com/optimization/introduction/cpp; IBM Monte Carlo simulation, https://www.ibm.com/think/topics/monte-carlo-simulation -->

---

<!-- Slide 8 -->
## What does the model produce?

The result should tell the team what action to take. It may be:

- A work plan showing who works and when
- An order plan showing which products to buy and how much
- A list showing which customer requests to answer first
- Several possible plans, with the expected result of each

The team should also see the main reasons for the suggestion.

---

<!-- Slide 9 -->
## Decisions prescriptive analytics can support

| Question | Possible action |
|:--|:--|
| What should we buy? | Choose products and order amounts |
| When should work happen? | Choose times for tasks or repairs |
| Where should products go? | Decide how much each store receives |
| Which request should come first? | Choose the order for answering requests |

Each question leads to a choice the team can act on.

---

<!-- Slide 10 -->
## The meaning of the best choice

The best choice depends on the goal.

| Main goal | What matters most when comparing plans |
|:--|:--|
| Lower cost | Spending less money |
| Faster service | Reducing waiting time |
| Less waste | Using fewer materials unnecessarily |
| Better customer service | Meeting more customer needs |

A business may have several goals. It must decide how to balance them, while keeping the rules the plan must follow.

---

<!-- Slide 11 -->
## Short-term and long-term decisions

Prescriptive analytics can support decisions for different periods of time.

| Time period | Example decision |
|:--|:--|
| Today | Which tasks should the team complete first? |
| Next week | How should working hours be planned? |
| Next month | How much stock should each store receive? |
| Next year | Where should the business add more storage space? |

Long-term decisions need estimates about conditions further into the future.

---

<!-- Slide 12 -->
## Connected decisions

One decision can affect another.

For a store:

- Ordering more products needs more storage space.
- Selling more products may need more workers.
- Faster delivery may cost more money.

A model can consider these connections together. This helps avoid a plan that solves one problem but creates another.

---

<!-- Slide 13 -->
## How machine learning helps

Machine learning uses patterns in data to make predictions.

| Machine learning may estimate | A prescriptive model may suggest |
|:--|:--|
| How much customers will buy | How much stock to order |
| When a machine may fail | When to plan a repair |
| How many requests may arrive | How many workers to assign |

The prediction becomes information for the decision model. Prescriptive analytics can also use estimates from people or other methods.

---

<!-- Slide 14 -->
## Levels of automation

Automation means allowing a computer to do an action.

| Level | What happens |
|:--|:--|
| Suggestion only | The system gives options; a person chooses and acts |
| Approval needed | The system prepares a plan; a person approves it before action |
| Automatic action | The system acts within agreed rules and records what it does |

The team chooses the level based on the decision and its possible effects. It should be able to stop automatic actions when a problem occurs.

---

<!-- Slide 15 -->
## Fairness in decision-making

A plan can meet a business goal and still affect people unfairly.

For example, a work plan might give the same workers the busiest hours every week.

The team can include rules for breaks, reasonable working hours, and sharing difficult tasks fairly.

**People must decide what fairness means for the decision and include it in the goals or rules.**
