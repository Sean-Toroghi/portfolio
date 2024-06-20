This is a summary of the book: Trustworthy Online Controlled Experiments (A Practical Guide to A/B Testing) 2020 by Ron Kohavi, Microsoft, Diane Tang, Google, Ya Xu, LinkedIn

# 1-

## Why conducting A/B testing: correlations vs causality

A/B testing is a go to approach for organizations that want to make data-driven decisions, or want to ensure having a trustworthy test of whether or not to invest in an infrastructure, or want to evaluate and identify ideas to filter poor/un-successful ones, before implementing them.

Perhaps the first and most important reason for running an A/B test is the best scientific way to establish causality with high probability. Also, in many cases, it is not easy to detect the effect of a small change. Specifically, of the change occurs over time. Moreover, detect an unexpected effect of a change on metrics other than the original metric used for detecting a change subject to the target of the experiment. 

To run a successful A/B test (control test) the following requirements are needed:
- experimental units assigned to different variant be independent from each other.
- to gain a result with confidence we need to have enough experimental units (min sample size)
- we could define measurable goals by defining key metrics
- the proposed changes be feasible

It is still possible to run other modeling and experimental techniques if due to lack of any/all of the above requirement, we cannot run a controlled experiment. However, controlled experiment is the most reliable technique to evaluate changes.

## A/B testing pipeline


__Step 1: define a goal and changes we have in mind to achieve the goal__

An example of a goal is to increase revenue. Some examples for changes could be introducing a new feature, changing the user interface, a back-end-change, remove a feature that carries a high cost to maintain, and so on. 

__Step 2: define goal or success metrics__

After defining goal/s and potential changes, we need to define metrics. One important consideration here is to normalize metrics by sample sizes. For example. if _increase revenue_ be our gool and _sum of revenue_ be the metric, then the result will be affected by the sample size. A better metric is revenue-per-user.

Furthermore, the metric needs to be specific and clear. In the example of revenue-per-user, we need to define which users are we going to include in the computation of the metric: all users who visited the site, only those who made a purchase, or only those who started the purchase process.

__Step 3: stablishing statistical significance - form hypothesis testing__

The following elements to form a hypothesis test:
- a baseline mean and standard error of mean for the metric. This is required to pick a proper sample size before running the test, and calculate statistical significance during the analysis. A lower standard error value improves sensitivity (ability to detect statistically significant differences)
- form alternative and null hypothesis.
- run the test to examine if the difference between a pair of treatment and control samples is unlikely, given null hypothesis that their means are the same. If it is unlikely, we reject the null hypothesis and claim the difference is statistically significant.
- To measure whether the difference is statistically significant is using p-value. Another way of checking the significance is to examinee if the confidence interval overlaps with zero. For example, a 98% CI is the range that covers the true difference 98% of the time. For a large enough sample size, it is centered around the difference between control and treatment with an extension of 2.5 standard errors on each side. 
- Statistical power (probability of detecting a meaningful difference between the variants when there really is one) is used to stablish the sample size. The statistical power of an experiment gives it the ability to conclude with high probability if the experiment has resulted in a change bigger than what we care about.

 __Step 4: design the experiment__

 Given the hypothesis and significance boundary, and characteristics of the metric, we are able to design the experiment:
 - establish randomization unit
 - specify the population of randomization units we want to target
 - compute sample size
 - define experiment duration


__Step 5: running the experiment and collecting data__

To run a successful experiment, we need instrumentation to get logs data and infrastructure to run it. 

__Step6: interpret the results and making decision__

First step in interpreting the results is sanity check. We employ guardrail metrics (invariants) to make sure any detected change is caused by the feature subject to the tested.

After the sanity check, we either reject or fail to reject the null hypothesis. 

Finally based on the outcome of the experiment and considering other elements/factors such as tradeoff between different metrics, cost of a change, and potential consequences of making a wrong decision, we derive the final decision.







