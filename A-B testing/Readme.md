# A/B testing

In this depository, I provide some sample of running A/B test on variety of topics.

Here I provide a brief summary about A/B testing. On separate Jupiter notebooks in this depository, you could find statistical summary for A/B testing, including confidence interval, selecting sample size, different types of error, and different statistical inference methods.


__10 steps of running an A/B test__
1. define a goal and form the hyp.
2. identify control and treatment groups
3. identify metrics
4. identy the needed data to be collected
5. determine the scale of desire difference to be detected
6. determine size of sample (power analysis) and length of the test
7. collect data (run the test)
8. run an A/A test (dummy test) to identify any systematic bias

References:
- Practical A/B Testing (2023) by Leemay Nassery
- Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing (2020) by Ron Kohavi, Diane Tang, Ya Xu
---
# A/B testing foundation

## Form a goal and define hypothesis

A good hypothesis needs to include the following
- the outcome we are predicting to happen by applying the experiment/change to a subset of users
- result of applying the change
- reason this outcome is desirable

A template for hypothesis: __We believe__ (the proposed solution (the variable we want to evaluate)); __will then__ (the result of introducing the change (what does success mean)), __because__ (evidence for the prediction). 

__Example__: _I/We believe_ adding this summary about A/B testing, will increase the chance of getting a position as a data scientist, because the hiring team could observe my knowledge and capability to run a successful A/B test.

---

## Measure the impact of an experiment: define a metric

A metric for A/B testing demonstrates the impact of the change, and needs to have the following characteristics:
- easy to understand (could be easily interpreted)
- simple to compute (not being a composite metric)
- actionable (the result ignites taking an action)
- reliable to produce (not being too complex to implement)

__Types of metrics__

- Success metric is also reffered to as a _primary metric_. This is the metric shows if the intended change in the hypothesis statement succeed. Example: if we introduce a new feature to increase view of a website, increase the average number of viewers over a period of time could be a success metric.
- Guardrail metric/s also called secondary metric/s: are defined to make sure a change does not bring an unintended effect (positive or negative, but perhaps more so a negative). Example: adding this summary to the portfolio, will increase the change of getting a position other than data scientist!

__Common guardrail metrics__
- user retention
- revenue
- click-trough-rate (CTR)
- return visits
- weekly active users
- monthly active users
- daily active users
- pageviews
- web performance speed

  __Trade-off between metrics__

  In case we have multiple success and secondary metrics, they may conflict with each other. For example, if I spend too much time making this summary a comprehensive one that attracts more viewers, I will cut the time I spend developing ML models. Another example is introducing a fansy feature, may increase the implementation cost that leads to decrease in revenue. 
 
__Establish a Baseline__

It is always a good idea to start with a baseline. In case of A/B testing, we could establish a baseline for the metric, by recording the reuslts before implementing a change. 

__Proxity metrics__

In case the ideal metrics are not measurable or difficult to measure, or are not trustworthy with the data in hand, we employ proxy metrics. 

---

## Define test and control variants

Variant (or segment) is a subset of population we have access to for running our test on and collect information about. Sample is chosen randomly from the target population.
- Test (treatment) variant is a sample that receives a different experiment than what we plan to investigate
- Control variant is a sample that receives the existing or unchanged functionality

Note: any user in the sample requires to satisfy a pre-defined list of eligibility criteria. For example run a test on generating an ads leading to increase subscription, one eligibility criteria is the user need to be a new user without any existing account and finishes the registration.

__Randomize user allocation__

To form a valid result, we need to allocate users randomly to each variant. It decreases statistical bias, as each user has the same chance of being subject to the experiment. Also each variant will have an evently distributed users with co-variates attributes, such as location and demographic.

There are several common randomization units including: 
- pageview randomization: randomly assign users to a page with the change that is subject to the test.
- session randomization: defined a session and assign users to the variant during the session period.
- user randomization: based on eligibility, assign random users to the variant for a predefined period.


--- 

## Confidence in A/B testing and computing sample size

__Sample size__: is the number of users exposed to a A/B test. A very small sample may provide inaccurate result (not be able to generalized to population), while a very large sample may cause issues as well (too costly, not feasible, ...). In general, a larger sample size increase the confidence level of the results.

The following factors effect the sample size:
- minimum detectable effect (MDE), also called effect size: the minimum improvement of a success metric that we want to be able to detect within the scope of the experiment. Subject matter experts and previous tests are helpful for determining the MDE.
- metric variance: metric with lower variance increases power.
- $\alpha$: represents tolerance for making a false positive. A p-value less than $\alpha$ means results are significant (not occurred by chance).
- baseline conversion rat: is the expected value for the control variant for the success metric. 
- power of the test: which represents the likelihood that your A/B test will detect an effect if one exists. Higher power translates to a decreased risk of faulty test results. As the size of sample increases, power of test also increases. In reverse, if we want to have a test with higher power, we need to increase the size of sample.

---

## Different types of A/B testing

### Superiority A/B test

When the goal of the test is to show a change improves the status quo (control group), we employ superiority A/B test. 

### Non-inferiority A/B Test

When the goal of the test is to show a change does not have a meaningful impact, or the impact is slightly inferior, we perform non-inferiority A/B Test. The null hypothesis in this test states no meaningful difference between the test and control variants. Some use cases of this test are:
- examin change in the model architecture to produce different results under the hood does not effect user experience.
- migration of a new engineering sustem.
- making changes that reduce tech debt and wanting to ensure the experience for the user has not degraded.
- making small changes, and want to make sure it does not have a negative effect on custoemr experience.
- gauging if a cheaper-to-implement solution from an engineering perspective can perform almost as well or not meaningfully worse than the current control implementation.




### Equivalence A/B Test

When the goal is to show two versions are the same or there is no meaningfull differences. The main difference between equivalence and non-infererior A/B Tests is, in non-inferior A/B Test we want to show version A is as good as version B. Even if A be slightly worse than B, still the test has a positive outcome. In equivalence test, A need to be the same as B to have a positive outcome from the test.

---

## Test duration

There are several factors affecting the duration of a test:
- evalute the impact of a change on metrics such as churn
- learn the relationship between short-term and long-term business metrics
- understand the impact of multiple changes, collectively
- observe the trend from an initial test, whether the maintians, improves, or degrades (given the initial results)

### Degradation holdbacks

IF the goal of a test is to evaluate a feature's impact on a long run, we employ degradation holdback method. Here most users will receive the feature. At the same time, the feature is unavailable for a small percentage (holdback group). Another application is to evaluate which combination of features to remove from the evaluation. Another use case is to evalute the impact of a featurn on a certain key business metrics that take longer to observe.

Note: we should not choose a degradation holdback A/B test if your feature is already available for your entire user base and removing the feature for existing users to create the holdback group results in disorientation with the product experience.

### Long-term cumulative holdbacks

A long-term cumulative holdback is similar to a long-term degradation holdback, but instead of selecting a feature to remove from the experience, the goal is to determine the impact of the cumulative product changes from a given time period—such as quarterly.

This test design involves holding back a small portion of users that will not get exposed to any product changes made over a given period of time with the intent of observing the impact of all successful changes in aggregate.

One __drawback__ of this type of test, is its cost. Maintaining multiple versions of a product or feature, especially on a longer timeline, has a cost.

---

## Summary 

- Superiority tests should be used to determine the effect of a change in any direction from the control.
- Non-inferiority tests enable you to conclude whether a change is no worse than what is already in place, the control experience.
- Equivalence tests demonstrate whether the effect of a change is the same as the control.
- Degradation and cumulative holdbacks demonstrate the effect features have on metrics that may take longer to measure, like retention or churn rate.

The following tree-based framework provides a guideline for selecting an appropriate A/B testing.
![image](https://github.com/Sean-Toroghi/portfolio/assets/50586266/f572841d-1f69-48e5-b6ea-d3d6d56687a7) Source: Practical A/B Testing (2023)



