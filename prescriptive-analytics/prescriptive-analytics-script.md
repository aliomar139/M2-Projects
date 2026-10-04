# Prescriptive analytics: spoken script

This script follows the slide order in `prescriptive-analytics-presentation.md`. The slide deck contains the points for the audience; use these notes as a natural guide rather than reading every line word for word.

## Slide 1: Prescriptive analytics

Hello, everyone. I’m going to focus on prescriptive analytics, the part of analytics that helps people decide what to do. We’ll look at what goes into a recommendation, how a system compares possible actions, and where this approach can be useful. I’ll also briefly connect it to the other analytics types you’ve just heard about.

## Slide 2: What is prescriptive analytics?

Prescriptive analytics addresses a practical question: given what we know, what should we do? A useful answer needs more than a forecast. It needs a goal, a set of possible actions, and a clear picture of the limits we have to respect. The result may be one recommended action, several choices ranked by their expected results, or an action carried out automatically within agreed rules. The point is to make the decision clearer and more deliberate.

## Slide 3: What goes into a prescription?

Let’s break that down. First, there needs to be a decision to make. Then the organization has to say what it wants to achieve. That might be reducing cost, meeting a delivery target, or using available staff effectively. Information helps describe the current situation and estimate what may happen. Constraints capture requirements such as a fixed budget, limited capacity, deadlines, or regulations. Finally, the model needs a set of actions it can compare. If any of these pieces are missing, the recommendation may not fit the real decision.

## Slide 4: How it produces a recommendation

The process begins by defining the decision and what success means. The analysis then uses data and, where useful, forecasts to estimate possible outcomes. Next, it applies the limits the organization must follow. With those boundaries in place, an optimization method can compare the actions that remain. It looks for options that meet the constraints and perform well against the chosen goal. The recommendation can then go to a person for review, or be carried out under rules the organization has approved. A different goal can lead to a different answer, even when the data stays the same.

## Slide 5: A simple example: delivery planning

Delivery planning makes the pieces concrete. Suppose a company wants to deliver orders on time while controlling fuel use. It can use locations, traffic information, vehicle capacity, and delivery windows to compare route plans. Driver hours, road restrictions, and the number of available vehicles narrow down which plans are possible. The system can recommend a route plan that works within those limits and balances the stated priorities. If the company decides that speed matters more than fuel use, or adds a new delivery deadline, the recommendation may change. The model follows the goal it was given.

## Slide 6: Where it can help

The same approach applies to many recurring decisions. A supply chain team can allocate stock among locations. A manufacturer can plan maintenance around production needs. Hospital operations teams can coordinate rooms and staff. Financial institutions can prioritize cases for investigation, while a customer service team can decide how to use limited staff time. These are different fields, but the structure is similar: there are actions to choose from, an outcome to improve, and limits to respect.

## Slide 7: How it differs from the other analytics types

You’ve already heard about descriptive, diagnostic, and predictive analytics, so I’ll keep the distinction short. Descriptive analysis summarizes what happened; diagnostic analysis examines why; predictive analysis estimates what may happen. Prescriptive analytics uses information from those kinds of analysis to evaluate possible actions. Its output is centered on a decision: a recommendation or a set of options, with goals and constraints taken into account. It builds on the earlier types, while answering a different question.

## Slide 8: Good recommendations need good judgment

A recommendation is only as sensible as the goal, data, and assumptions behind it. If the system is told to minimize cost, it may reduce spending in ways that harm service. If the data is incomplete or out of date, it may compare options using a picture of the situation that no longer applies. The recommendation may also reflect constraints that were entered incorrectly or leave out a requirement the team cares about. It’s useful to ask what the system is optimizing and what it might be missing before acting on the answer.

## Slide 9: From recommendation to responsible action

Teams need to understand the main trade-offs before they put a recommendation into practice. They should know who can approve it, who can challenge it, and how they will check whether it worked. Once actual results are available, they can compare them with expectations and update the approach. Some routine decisions can run automatically, provided the rules are clear and there is a way to monitor the results. For decisions with larger consequences, human review should match the level of impact.

## Slide 10: The central idea

To sum up, prescriptive analytics brings together information, a goal, and real-world constraints to compare possible actions. It helps people make decisions with a clearer view of the options and trade-offs. The quality of the outcome still depends on choosing the right goal, using suitable data, and reviewing what happens after the recommendation is used. Thank you. I’m happy to take your questions.
