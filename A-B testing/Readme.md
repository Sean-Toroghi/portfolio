# A/B testing

In this depository, I provide some sample of running A/B test on variety of topics.

## 10 steps of running an A/B test
1. define a goal and form the hyp.
2. identify control and treatment groups
3. identify metrics
4. identy the needed data to be collected
5. determine the scale of desire difference to be detected
6. determine size of sample (power analysis) and length of the test
7. collect data (run the test)
8. run an A/A test (dummy test) to identify any systematic bias

References:
- Practical A/B Testing 92023) by Leemay Nassery
- Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing (2020) by Ron Kohavi, Diane Tang, Ya Xu
---
# A/B testing foundation

## Form a goal and define hypothesis

A good hypothesis needs to include the following
- the outcome we are predicting to happen by applying the experiment/change to a subset of users
- result of applying the change
- reason this outcome is desirable

A template for hypothesis: __We bevieve__ (the proposed solution (the variable we want to evaluate)); __will then__ (the result of introducing the change (what does sucess mean)), __because__ (evidence for the prediction). 

__Example__: _I/We believe_ adding this summary about A/B testing, will increase the chance of getting a position as a data scientist, because the hiring team could observe my knowledge and capability to run a successful A/B test.

---

## Measure the impact of an experiment

