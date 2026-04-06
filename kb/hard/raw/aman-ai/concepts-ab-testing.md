# Concepts • A/B Testing

**Source:** https://aman.ai/primers/ai/ABTest/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview of A/B Testing](#overview-of-ab-testing)
* [Benefits of A/B Testing](#benefits-of-ab-testing)
* [Delving into Metrics](#delving-into-metrics)
  + [Incorporating Sampling Methods in A/B Testing](#incorporating-sampling-methods-in-ab-testing)
    - [Simple Random Sampling](#simple-random-sampling)
    - [Systematic Sampling](#systematic-sampling)
    - [Stratified Sampling](#stratified-sampling)
* [Designing an AB Test: Summary](#designing-an-ab-test-summary)
* [Key terms](#key-terms)
  + [1. Null Hypothesis (( H\_0 )):](#1-null-hypothesis--h_0-)
  + [2. RCT (Randomized Controlled Trial):](#2-rct-randomized-controlled-trial)
  + [3. Controlling for Confounders:](#3-controlling-for-confounders)
  + [4. Instrumental Variables:](#4-instrumental-variables)
  + [5. Treatment and Control:](#5-treatment-and-control)
  + [6. Bias:](#6-bias)
  + [7. Alpha:](#7-alpha)
  + [8. Beta:](#8-beta)
  + [9. Power:](#9-power)
  + [Effect Size:](#effect-size)
  + [P-value:](#p-value)
  + [Confidence Intervals (CI):](#confidence-intervals-ci)
  + [External vs. Internal Validity:](#external-vs-internal-validity)
  + [FDR (False Discovery Rate):](#fdr-false-discovery-rate)
* [Running an A/B Test: The Process](#running-an-ab-test-the-process)
* [Switchback Experiments](#switchback-experiments)
  + [Summary](#summary)
* [Conclusion](#conclusion)
* [From Statistical to Causal Learning](#from-statistical-to-causal-learning)
* [References](#references)
* [Further Reading](#further-reading)

## Overview of A/B Testing

* Experimentation, particularly A/B testing, offers a strategic method to make informed decisions about product and service improvements. Instead of relying solely on expert opinions or executive decisions, A/B testing provides a platform for users or customers to express their preferences through their interactions.
* The Scientific Approach: A/B testing operates on the scientific method. It starts with forming hypotheses, collecting empirical data through experiments, and then drawing conclusions based on evidence. This method promotes a cyclical pattern of deduction and induction, propelling further hypotheses and tests.

## Benefits of A/B Testing

1. Gives Users a Voice: A/B testing ensures that user feedback is central to product changes, emphasizing the importance of user experience in decision-making.
2. Facilitates Causal Inferences: By randomly assigning users to different groups, and introducing changes only to specific groups, it’s possible to determine the causal effects of a change. This approach isolates the introduced variables, making results more reliable.
3. Confidence in Decisions: By gathering concrete data on user preferences, companies can confidently implement changes, knowing they are backed by real user feedback.

## Delving into Metrics

* Tailored Metrics: The metrics chosen for evaluation vary depending on the experiment. For instance, a test focused on improving search results might measure user engagement with search functions. Other experiments could assess technical performance, like app loading times or video streaming quality under varied conditions.
* Interpreting Metrics Carefully: Surface metrics, like click-through rates, might not always give a comprehensive view. For example, increased clicks might only indicate users trying to understand a feature rather than genuine interest. Hence, a multi-metric approach can provide a holistic view, gauging overall user satisfaction and engagement levels.

### Incorporating Sampling Methods in A/B Testing

* Sampling methods significantly influence the reliability and relevance of A/B testing outcomes. The choice of sampling method hinges on various factors, including data quality, precision requirements, and cost considerations.

#### Simple Random Sampling

* Simple Random Sampling (SRS) ensures every potential sample stands an equal chance of selection. While this method can mitigate bias, it might sometimes fail to represent the population adequately.

#### Systematic Sampling

* Systematic Sampling involves periodic selection from an ordered list. This approach can efficiently represent populations, but it’s essential to be wary of biases that might arise due to the structure of the data.

#### Stratified Sampling

* In scenarios where the testing population spans distinct categories, Stratified Sampling becomes relevant. By dividing the population into individual strata and sampling each independently, this method can provide richer insights, more accurate statistical estimates, and flexibility.

## Designing an AB Test: Summary

* Statistical Considerations in A/B Testing
  1. Understanding the 5% Significance Level:
  + The standard practice in A/B testing is to set the acceptable false positive rate at 5%. This means that even if there is no actual difference between treatment and control groups, the test will indicate a significant difference 5% of the time.
  + This convention is akin to mistaking non-cat photos for cat photos 5% of the time.
  + The concept of the 5% false positive rate is deeply connected to “statistical significance” and the p-value. The p-value calculates how probable it is to observe a result as extreme as the one from the A/B test, under the assumption that there’s no real difference between the groups.
* Reasons for the 5% Standard in A/B Testing:
  1. Balancing Errors:
  + Statistical testing involves balancing Type I (false positives) and Type II (false negatives) errors. The 5% rate ensures a manageable balance between these errors.
    1. Tradition and Convention:
  + The 5% significance level has become an accepted threshold across many research fields, primarily because of historical reasons and its practical implications.
    1. Risk Tolerance:
  + Using a 5% significance level is essentially expressing comfort with a 5% chance of making a false positive error.
    1. Historical Precedence:
  + Influential statisticians, notably Ronald A. Fisher, have advocated for this 5% level, and it has since become a norm.
    1. Practical Considerations:
  + Setting the threshold too low could result in overlooking genuine effects, while setting it too high could lead to many false discoveries.
* Statistical Decision Framework Using Coin Flips:
  1. Objective and Experiment:
  + The goal is to determine if a coin is unfair. This is analogous to business situations where one wishes to see if a new feature changes user behavior.
  + The decision framework helps decide when there’s enough evidence to reject the assumption that the coin is fair.
    1. Decision Making with p-value:
  + A p-value less than 0.05 would typically be considered strong evidence against the fairness of the coin.
    1. False Positives and Confidence Intervals:
  + The rejection region consists of outcomes that are deemed too extreme under the null hypothesis, leading to its rejection.
  + Confidence intervals, conversely, are ranges within which the true parameter value is believed to lie with a certain level of confidence.
    1. Understanding False Negatives and Power:
  + Power refers to the probability of correctly detecting a genuine effect. It’s connected to the concept of false negatives and is expressed as 1 minus the false negative rate.
    1. Improving Power in A/B Tests:
  + Power can be enhanced by:
    - Effect Size: Larger differences between groups are easier to detect.
    - Sample Size: More data helps in achieving a more accurate representation of the population.
    - Reducing Variability: Making metrics more consistent within groups makes true effects easier to spot.
* A/B tests, when grounded in statistical principles, provide valuable insights. While they offer rigorous evidence about variations in treatment effects, these insights often form just a piece of a broader decision-making process.

## Key terms

### 1. Null Hypothesis (( H\_0 )):

* The null hypothesis is a central concept in statistical hypothesis testing. It posits that there’s no significant difference between specified populations or that a particular parameter is equal to a specific value. In A/B testing, ( H\_0 ) typically states that there’s no difference between treatment and control groups. It’s the default assumption, and statistical tests aim to challenge and possibly reject it.

### 2. RCT (Randomized Controlled Trial):

* RCTs are experiments used to assess the efficacy of interventions. Participants are randomly assigned to treatment (experimental) or control groups to ensure that any observed effects can be attributed to the intervention itself and not other external factors.

### 3. Controlling for Confounders:

* A confounder is a third factor in an experiment that could cause variations. If not controlled, confounders can lead to incorrect conclusions about the relationship between the independent and dependent variables. By controlling these confounders, researchers can be more confident that the results observed are due to the treatment itself.

### 4. Instrumental Variables:

* In situations where direct experimentation isn’t possible due to ethical or practical reasons, instrumental variables can be used. They are variables that don’t directly affect the outcome but are related to the cause of interest and can help determine causality.

### 5. Treatment and Control:

* In A/B testing or experiments:
* Treatment Group: Receives the intervention or change being tested.
* Control Group: Continues without any intervention, serving as a baseline for comparison.

### 6. Bias:

* Bias refers to any systematic error in an experiment or study that skews the results. In A/B testing, it’s crucial to identify and minimize biases to ensure the test’s conclusions are valid.

### 7. Alpha:

* In hypothesis testing, alpha is the probability of rejecting the null hypothesis when it is actually true. This is known as a Type I error. Typically, an alpha of 0.05 is used, meaning there’s a 5% chance of falsely rejecting the null hypothesis.

### 8. Beta:

* Beta represents the probability of accepting the null hypothesis when it is false. This is termed a Type II error. The power of a test is 1 minus beta, representing the probability of rejecting the null hypothesis when it’s false.

### 9. Power:

* Power measures the ability of a test to detect an effect if one truly exists. It’s the probability that a test will reject the null hypothesis when it should (i.e., when the alternative hypothesis is true). A high-powered test is more likely to detect significant differences.
* Sure! We can further expand on some aspects and add more depth to the technical side of these concepts. Then, we’ll wrap it up with a conclusion.

### Effect Size:

* Effect size is a measure of the magnitude of a phenomenon or intervention’s effect. While p-values tell us if an effect exists, effect size gives us the magnitude of that effect. It’s particularly important because a statistically significant result doesn’t necessarily mean it’s practically significant. Common measures include Cohen’s d for t-tests and the odds ratio for chi-squared tests.

### P-value:

* The p-value measures the strength of the evidence against a null hypothesis. A smaller p-value indicates stronger evidence against the null hypothesis, leading researchers to reject it. However, it’s worth noting that a p-value doesn’t provide the probability that either hypothesis is true; it merely indicates the strength of evidence against ( H\_0 ).

### Confidence Intervals (CI):

* A confidence interval gives an estimated range of values that’s likely to include an unknown population parameter. If you have a 95% CI of (2, 8), it means that if you were to conduct the experiment numerous times, you’d expect the parameter to fall within this range 95% of the time. It’s a way of expressing the reliability of an estimate.

### External vs. Internal Validity:

* External Validity: Refers to the extent to which the results of a study generalize to settings, people, times, and measures other than the ones used in the study.
* Internal Validity: Concerns whether the intervention (and not other factors) caused the observed effect. High internal validity is often achieved by controlling for confounders, randomizing participants, and using proper blinding techniques.

### FDR (False Discovery Rate):

* In multiple hypothesis testing, the FDR controls the expected proportion of false positives. It’s a method used to correct for multiple comparisons and is especially important in fields like genomics where thousands of hypotheses are tested simultaneously.

## Running an A/B Test: The Process

* Here’s a step-by-step breakdown:
  + **Planning:** Before launching the test, you’ll decide on what change you’re going to test (e.g., a new feature, a different user interface, etc.), determine the success metrics (e.g., click-through rate, conversion rate), and decide how many users you need for statistical significance.
  + **Allocation:**
    - **Before Launch:** You’ll decide on the method of allocation (e.g., random assignment, stratified sampling, etc.) and the proportion of users to allocate to each group (e.g., 50% to A and 50% to B, or maybe 90% to A and 10% to B if you’re doing a more cautious rollout). You’ll also set up the infrastructure to assign users to groups.
    - **During Launch:** When the test is actually launched, users will be dynamically allocated to one of the groups based on the predetermined methodology. For example, if it’s random allocation, each user entering the site might have a 50% chance of being in group A and a 50% chance of being in group B.
    - Note that the strategy and methodology for allocation are decided before the test is launched, but the actual allocation of individual users to groups occurs dynamically as part of the test execution as users interact with the platform during the test period.
  + **Execution:** Once users are allocated, they’ll experience either the original version (Group A) or the changed version (Group B) of the website/app/feature.
  + **Analysis:** After enough data is collected, you’ll analyze the results based on the metrics you’ve chosen.
  + **Conclusion:** Based on the results, you’ll decide whether to implement the change for all users, iterate and run another test, or reject the change.

## Switchback Experiments

* **Development and Popularity:**
  + Used by companies like Uber, Lyft, Doordash, Amazon, and Rover, highlighting switchback tests’ widespread adoption and effectiveness.
* **Why Switchback Tests?**
  + Designed to measure impact in scenarios with strong network effects and user interdependence.
  + Particularly relevant in social media apps and two-sided marketplaces, where traditional A/B testing can be misleading.
  + Example: In ridesharing services, changes affecting rider behavior can also impact driver supply, demonstrating the interconnectedness in such marketplaces.
* **Key Features of Switchback Tests:**
  + **Mechanism:** Involves alternating between test and control treatments over time, ensuring uniform treatment across a network at any given moment.
  + **Advantages:** Effective in situations with immediate test effects and strong interference, overcoming limitations of traditional A/B tests.
* **Implementation Details:**
  + **Time Interval Determination:** Essential for successful experiments, balancing the need to capture effects with the requirement for ample test and control samples.
  + **Schedule Creation:** Involves assigning test and control intervals, with strategies ranging from simple randomization to complex, product-specific algorithms.
  + **Segmentation and Clustering:** Enhances sampling and data point collection by dividing users into independent clusters, like cities.
  + **Burn-In and Burn-Out Periods:** Excludes data near switching boundaries to prevent contamination between test and control effects.
* **Analysis Techniques:**
  + **Challenges with Traditional Methods:** The interdependence of users makes standard statistical tests like t-tests unsuitable.
  + **Preferred Approaches:** Regression analysis for specific metrics and products, and bootstrapping analysis for a more generalizable solution.
* **Practical Considerations and Limitations:**
  + **Suitability for Short-Term Effects:** Optimal for assessing transactional behaviors within single sessions, not for long-term impacts.
  + **Importance of Setup:** Effective implementation relies on selecting appropriate time windows and clustering parameters, necessitating deep domain knowledge.
* This comprehensive summary emphasizes the unique aspects, development history, implementation strategies, and practical applications of switchback experiments, highlighting their critical role in scenarios where traditional A/B testing falls short due to network effects.
* For more, refer [Switchback experiments: Overview and considerations](https://statsig.com/blog/switchback-experiments).

### Summary

* By popular demand, we partnered with existing Statsig customers to build this novel mode of experimentation.
* Why Switchback tests?
  + A switchback test is a type of experimentation that can measure impact when network effects are in play. It applies to situations where user behavior is not independent, and the actions of one user can affect another (commonly referred to as interference). This is common in social media apps and 2-sided marketplaces where simple A/B tests can produce inaccurate results.
  + A canonical example of this scenario comes from ridesharing services like Lyft: All the riders in an area share the same supply of drivers, and vice versa. In these cases, a test that impacts the probability of riders booking a ride (e.g., providing a discount code) also affects the supply of drivers available to the control group.
* Switchback solves this problem by switching the user experience back and forth by randomizing on units of time, instead of users! This method was popularized by Uber and Lyft, and used by companies like Doordash, Amazon, and Rover. It’s great for situations where the test effect is immediate, and interference is strong.

## Conclusion

* Understanding the intricacies of statistical and experimental concepts is paramount in research. Whether one is conducting A/B tests, clinical trials, or social science experiments, having a solid grasp of hypothesis testing, the importance of controlling confounders, and the implications of biases can significantly affect the outcomes. These tools, combined with an appreciation for both the magnitude (effect size) and the significance (p-value) of results, ensure that research findings are both scientifically robust and practically relevant. Furthermore, recognizing the balance between internal and external validity can guide research design, allowing for results that are both causally accurate and generalizable. As research continues to evolve with technological advancements, maintaining a foundational understanding of these concepts is essential for producing reliable, actionable, and impactful insights.

## [From Statistical to Causal Learning](https://arxiv.org/abs/2204.00607)

* In [From Statistical to Causal Learning](https://arxiv.org/abs/2204.00607), Schölkopf and Kügelgen describe basic ideas underlying research to build and understand artificially intelligent systems: from symbolic approaches via statistical learning to interventional models relying on concepts of causality. Some of the hard open problems of machine learning and AI are intrinsically related to causality, and progress may require advances in our understanding of how to model and infer causality from data.

## References

* [Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing](https://experimentguide.com/)
* [HBR: The Surprising Power of Online Experiments](https://hbr.org/2017/09/the-surprising-power-of-online-experiments)
* [HBR: Avoid the Pitfalls of A/B Testing](https://hbr.org/2020/03/avoid-the-pitfalls-of-a-b-testing)
* [A Crash Course on Online Experiments](https://www.coursera.org/lecture/recommender-metrics/introduction-to-online-evaluation-and-user-studies-TA1rp)
* [A/B/n Testing](https://www.split.io/glossary/a-b-n-testing/)
* [Goals Gone Wild: The Systematic Side Effects of Over-Prescribing Goal Setting](https://www.hbs.edu/ris/Publication%20Files/09-083.pdf) and [Goodhart’s Law](https://towardsdatascience.com/unintended-consequences-and-goodharts-law-68d60a94705c)
* [Reliance on Metrics is a Fundamental Challenge for AI](https://arxiv.org/pdf/2002.08512.pdf)
* [Statistical Power Analysis](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/)
* [Type III Error](https://www.statistics.com/type-iii-err/)
* [Adobe Target: Sample Size Calculator](https://experienceleague.adobe.com/tools/calculator/testcalculator.html)
* [Sample Size Calculation with Both Confidence Level and Power](https://select-statistics.co.uk/calculators/sample-size-calculator-two-means/)
* [The Significance of Size & Power Calculation in A/B Tests](https://blog.developer.adobe.com/significance-of-size-power-calculation-in-a-a-b-test-8c21ab9ce171)
* [UNICEF’s Report on Impact Evaluation Using Randomized Controlled Trials](https://www.unicef-irc.org/publications/pdf/brief_7_randomized_controlled_trials_eng.pdf)
* [How long should you run an A/B Test?](https://experienceleague.adobe.com/docs/target/using/activities/abtest/sample-size-determination.html?lang=en)
* [The essential guide to Sample Ratio Mismatch for your A/B tests](https://towardsdatascience.com/the-essential-guide-to-sample-ratio-mismatch-for-your-a-b-tests-96a4db81d7a4)
* [Metaflow: quick and easy real-life data science and ML projects](https://metaflow.org/)

## Further Reading

* Netflix:
  + [Decision Making at Netflix](https://netflixtechblog.com/decision-making-at-netflix-33065fa06481)
  + [What is an A/B Test?](https://netflixtechblog.com/what-is-an-a-b-test-b08cc1b57962)
  + [Interpreting A/B test results: false positives and statistical significance](https://netflixtechblog.com/interpreting-a-b-test-results-false-positives-and-statistical-significance-c1522d0db27a)
  + [Interpreting A/B test results: false negatives and power](https://netflixtechblog.com/interpreting-a-b-test-results-false-negatives-and-power-6943995cf3a8)
  + [Building confidence in a decision](https://netflixtechblog.com/building-confidence-in-a-decision-8705834e6fd8)
  + [Experimentation is a major focus of Data Science across Netflix](https://netflixtechblog.com/experimentation-is-a-major-focus-of-data-science-across-netflix-f67923f8e985)
  + [Computational Causal Inference at Netflix](https://netflixtechblog.com/computational-causal-inference-at-netflix-293591691c62)
  + [It’s All A/Bout Testing: The Netflix Experimentation Platform](https://netflixtechblog.com/its-all-a-bout-testing-the-netflix-experimentation-platform-4e1ca458c15)
  + [A Survey of Causal Inference Applications at Netflix](https://netflixtechblog.com/a-survey-of-causal-inference-applications-at-netflix-b62d25175e6f)
  + [A/B Testing and Beyond: Improving the Netflix Streaming Experience with Experimentation and Data Science](https://netflixtechblog.com/a-b-testing-and-beyond-improving-the-netflix-streaming-experience-with-experimentation-and-data-5b0ae9295bdf)
  + [Quasi Experimentation at Netflix](https://netflixtechblog.com/quasi-experimentation-at-netflix-566b57d2e362)
* LinkedIn: [Experimentation tag on engineering blog](https://engineering.linkedin.com/blog/topic/experimentation); notably, [building inclusive products through A/B testing](https://engineering.linkedin.com/blog/2020/building-inclusive-products-through-a-b-testing) and [“no production release at the company happens without experimentation”](https://engineering.linkedin.com/blog/2020/making-the-linkedin-experimentation-engine-20x-faster)
* Google: [Decision Intelligence with Cassie Kozyrkov](https://www.gcppodcast.com/post/episode-128-decision-intelligence-with-cassie-kozyrkov/)
* Uber: [“Experimentation is at the core of how Uber improves the customer experience”](https://eng.uber.com/xp/)
* Airbnb: [Experimentation tag on engineering blog](https://medium.com/airbnb-engineering/tagged/experimentation)
* Intuit: [Meet Wasabi, an Open Source A/B Testing Platform](https://www.intuit.com/blog/innovative-thinking/meet-wasabi-an-open-source-ab-testing-platform/)
* Microsoft: [Online Experimentation at Microsoft](https://ai.stanford.edu/~ronnyk/ExPThinkWeek2009Public.pdf)
* Disney: [Universal Holdout Groups at Disney Streaming](https://medium.com/disney-streaming/universal-holdout-groups-at-disney-streaming-2043360def4f)
* [Sudeep Das & Aish Fenton at Netflix on Causal Inference](https://www.youtube.com/watch?v=V5KYt-Pqdno)
