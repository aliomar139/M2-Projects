# Prescriptive analytics: spoken script

This script follows the 15 slides in `prescriptive-analytics-presentation.md`. Use the slide headings to follow the order, and speak slowly and clearly.

## Slide 1: Prescriptive analytics

Hello everyone, and thank you for being here. The data science life cycle has several stages: understanding the problem, preparing data, building models, checking results, and using them in practice. Prescriptive analytics helps us use this work to make a decision.


## Slide 2: The data science life cycle

The cycle starts with the business problem. We need to know what decision to make and how we will tell if it worked. We then study and prepare the data, build models, and check whether the results meet the goal. Deployment means using the results in practice.

Prescriptive analytics helps with modeling and decision-making during this cycle. We can go back to earlier stages: if the results show a problem, we may need to change the data, the model, or even the goal.

Source: [IBM CRISP-DM guide](https://www.ibm.com/docs/en/SS3RA7_18.5.0/pdf/ModelerCRISPDM.pdf).

## Slide 3: Four types of analytics

Descriptive analytics gives a summary of the data. It tells us what happened, such as how much each store sold last month.

Diagnostic analytics looks for reasons behind a result. If stores sold fewer products, we might check whether they had enough products available. We need evidence to show whether this explains the lower sales.

Predictive analytics estimates what may happen next. For example, it can predict how much each store may sell next month. Demand means how much customers want to buy.

Prescriptive analytics suggests what to do. Stock means the products available. The model can use expected demand and available stock to suggest how much to send to each store. All four types can work together in the same data science project.

Source: [IBM Think: prescriptive analytics](https://www.ibm.com/think/topics/prescriptive-analytics).

## Slide 4: The role of prescriptive analytics

Let us focus on prescriptive analytics. A forecast is a prediction, such as how much people may buy. A prescriptive model helps us choose an action using that information. For stores, it may suggest how much stock to send. For deliveries, it can use predicted travel times to choose roads that allow delivery at the agreed time.

The suggestion should show what to do, what result to expect, and which limits affected the choice. This helps the person responsible check the plan.

## Slide 5: The decision model

A decision model has four main parts. Decision variables are what we can change, such as the number of products sent to each store. The objective is the goal we want to improve. Constraints are the rules and limits we must follow. Inputs are the information the model uses.

A feasible plan follows all the rules. An optimal plan gives the best result for the goal among the choices allowed by the model. Assumptions are things the model treats as true, such as the available working hours. We still need to check whether these match the real situation.

## Slide 6: The recommendation process

First, agree on the decision with the person responsible. Prepare the data and estimate what may happen next. Then build a model that connects possible choices to their expected results and limits.

Compare the plans that follow the rules, and check what the model assumes before suggesting a plan. After the team uses the plan, measure what happened. Use these results to improve the next decision.

## Slide 7: Methods used in prescriptive analytics

Different decisions need different methods. Mathematical optimization finds the best result for a goal while following the rules. It can help decide how to share stock. Constraint programming finds plans that follow detailed rules, such as choosing working hours based on workers' skills and availability.

Simulation estimates how plans may work when conditions change, such as when demand rises or falls. We still need a rule or an optimization step to choose which plan to suggest. Teams can use these methods together when needed.

Sources: [Google OR-Tools](https://developers.google.com/optimization/introduction/cpp), [IBM: Monte Carlo simulation](https://www.ibm.com/think/topics/monte-carlo-simulation).

## Slide 8: What does the model produce?

The result should be something the team can use. It might be a work plan showing who works and when, an order plan showing what to buy, or a list showing which customer requests to answer first.

Sometimes the model gives several possible plans and their expected results. The team should also see the main reasons behind the suggestion, so people can understand and check it.

## Slide 9: Decisions prescriptive analytics can support

Prescriptive analytics can help answer practical questions. What should we buy? When should work happen? Where should products go? Which request should come first?

Each question leads to an action. For example, deciding when work should happen can produce a plan for tasks or repairs. The important point is that the team can use the answer to do something.

## Slide 10: The meaning of the best choice

The best choice depends on the goal. If we want lower costs, we compare how much each plan costs. If we want faster service, we compare waiting times. Other goals may include less waste or meeting more customer needs.

A business can have several goals at once. People must decide how to balance them. The model then compares plans using those priorities and the rules it must follow.

## Slide 11: Short-term and long-term decisions

Prescriptive analytics can support decisions for today, next week, or further into the future. A daily decision might be choosing which tasks to complete first. A weekly decision might be planning working hours. A longer-term decision might be choosing where to add storage space.

The time period changes the information we need. For a decision about next year, we need estimates about conditions further into the future.

## Slide 12: Connected decisions

Decisions often affect each other. If a store orders more products, it needs space to keep them. If it expects more sales, it may need more workers. Faster delivery may also cost more money.

A decision model can consider these connections together. This helps the team avoid solving one problem in a way that creates another.

## Slide 13: How machine learning helps

Machine learning uses patterns in data to make predictions. It may estimate how much customers will buy, when a machine may fail, or how many customer requests will arrive.

A prescriptive model can use those predictions to suggest how much stock to order, when to plan a repair, or how many workers to assign. It can also use estimates from people or other methods. Machine learning is one possible source of information for the decision model.

## Slide 14: Levels of automation

Automation means allowing a computer to do an action. At one level, the system only gives suggestions, and a person chooses and acts. At another level, the system prepares a plan but waits for approval. With automatic action, the system acts within agreed rules and records what it does.

The team chooses the level based on the decision and its possible effects. It should also be able to stop automatic actions if a problem occurs.

## Slide 15: Fairness in decision-making

A plan may meet the business goal but still affect people unfairly. For example, a work plan might give the same workers the busiest hours every week.

The team can include rules for breaks, reasonable working hours, and sharing difficult tasks fairly. People must decide what fairness means in that situation and include it in the model's goals or rules.


