<h1>Marketing through data science perspective</h1>
<h2>My personal notes, summaries, approaches, tips, and takeawyas</h2>


__References
- [Hands-On Data Science for Marketing (2019) by Y.H. Hwang](https://learning.oreilly.com/library/view/hands-on-data-science/9781789346343)
- 

# A/B testing for marketing
While A/B testing plays an important role across various induestries, it is a cruisial method in the marketing field. In the nutshell, it is a method for comparing and testing effectiveness and benefits of two different business strategies. In marketing, it helps to remove guesswork out of a decision-making, and save resouces/time, while increase performance of a policy or strategy. In this capacity, a typical A/B testing creates and tests two or more versions of marketing strategies for their effectiveness in achieving your marketing goal. A standard procedure is to randomly select/assign a sample of users in two groups. Then, for a predefined period of time, introduce service/product/bid to one group and collect predefined metrics from both groups. Once the tests are complete, we analyze and evaluate the experiment results. This requires checking whether there is a statistically significant difference between the results of the two versions. 

# Statitstical hypothesis testing

Forming hypothesis requieres to define null and alternative hypothsis. The null hypothesis indicates the two groups are not statistically significant different. The alternative hypothsis indicates the two groups shows a statistially significant difference. 




There are several statistical test methods, each suitable for a specific configuration. 

__Parametric test__
- T-test (student test) compares two averages and exmines if they are significantly different from each other. Two important statistics in t-test are t-value and p-value.
  - The t-value measures the degree of difference relative to the variation in the data. Larger t-value indicates more difference.
  - The p-value measures the probability that the results would occur by chance. Smaller p-value indicates higher statistically significance difference is between two groups. 
  Two types of t-test:
  - paired t-test
  - independent t-test
- ANOVA
- MANOVA

Testing relashipship - correlation
- pearson's r

__Non-parametric tests__
- Spearman
- Chi-square test of independence
- Sign test
- Kruskal-Wallis H: testing 3 or more groups.
- ANOSIM: testing 3 or more groups. 
- Wilcoxon Rank-Sum test
- Wilcoxon Signed-rank test

- 
