# Concepts • Causal Inference

**Source:** https://aman.ai/primers/ai/causalInference/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* Table of Contents
  {toc}

## Overview

* Causality in data science refers to the study and identification of cause-and-effect relationships between variables. While correlations can identify relationships or associations between variables, causality goes a step further by explaining how a change in one variable (the cause) will change another variable (the effect).
* Understanding causality is critical for making predictions, policy decisions, and interventions.
* Causal inference is inferring the effects of any treatment/policy/intervention on another thing.

## Simpson’s paradox

* Simpson’s Paradox is a statistical phenomenon where a trend or relationship that appears within several different groups disappears or reverses when the groups are combined. This can lead to misleading or counterintuitive conclusions if not properly recognized and analyzed.
* Example of Simpson’s Paradox:
* Imagine a university that is evaluating gender bias in admissions to two different departments, A and B. The data might look like this:
* Department A:
  + Men: 800 applied, 400 accepted (50% acceptance rate)
  + Women: 100 applied, 80 accepted (80% acceptance rate)
* Department B:
  + Men: 100 applied, 10 accepted (10% acceptance rate)
  + Women: 800 applied, 200 accepted (25% acceptance rate)
* Looking at each department separately, women have a higher acceptance rate in both. However, if you combine the data:
* Overall:
  + Men: 900 applied, 410 accepted (approximately 45.6% acceptance rate)
  + Women: 900 applied, 280 accepted (approximately 31.1% acceptance rate)
* Suddenly, the overall acceptance rate for men is higher, even though women had a higher acceptance rate within each department. This is Simpson’s Paradox in action.
* Causes:
* Simpson’s Paradox can occur when there is a lurking or confounding variable that isn’t accounted for in the analysis. In the example above, the confounding variable is the department to which the applicants applied. Department A might be easier to get into, and more women might apply to that department, skewing the overall acceptance rates.
* Implications:
* Misleading Conclusions: If not recognized, Simpson’s Paradox can lead to incorrect or misleading conclusions, potentially affecting decision-making in various fields, including public policy, healthcare, and business.
* Importance of Context: Understanding the context and considering all relevant variables is vital in analyzing data to avoid falling into the trap of Simpson’s Paradox.
* Need for Careful Analysis: It emphasizes the need for careful statistical analysis, including stratification of data by relevant groups, to understand the underlying relationships properly.
* Simpson’s Paradox illustrates the complexities of statistical interpretation and the importance of careful and nuanced analysis. It shows that aggregated data can sometimes hide or even reverse trends that are present at the group level, and serves as a reminder that correlation does not always imply causation, especially when confounding variables are present.

## Correlation does not imply causation

* The statement “correlation does not imply causation” emphasizes that just because two variables are correlated (i.e., they move together in a predictable way) does not mean that changes in one variable cause changes in the other and we will see why below:
  1. Confounding Variables: There might be a third variable that influences both variables, creating a correlation between them without a direct causal link. For example, ice cream sales and outdoor swimming incidents might be correlated, but both are influenced by the weather, not each other.
  2. Directionality Problem: Even if there’s a correlation between two variables, it’s not always clear which variable might be causing the other, or if they’re influencing each other simultaneously. Correlation does not provide information on the direction of the causal relationship.
  3. Coincidental Correlations: Sometimes, correlations occur purely by chance, without any underlying causal connection. This can lead to spurious correlations, where the relationship is coincidental or due to random fluctuations in the data.
  4. Simpson’s Paradox: As previously discussed, correlations within subgroups may not hold when the data are aggregated, or the direction of the relationship may reverse. This can make it challenging to infer causation based on correlation alone.
* While correlation is a valuable statistical tool for identifying relationships between variables, it doesn’t provide evidence of a cause-and-effect relationship. Proper causal inference requires more rigorous investigation and methods, considering potential confounding variables, the directionality of relationships, and the overall context in which the data are collected and analyzed.

### Then what does imply causation?

* Establishing causation is a complex process that goes beyond simple correlations. Here are some ways researchers and scientists try to infer causality:
  1. Randomized Controlled Trials (RCTs): RCTs are often considered the gold standard for establishing causation. By randomly assigning subjects to different groups (e.g., treatment and control), researchers can help ensure that the groups are comparable, thereby isolating the effect of the treatment. Any difference in outcomes between the groups can then be attributed to the treatment, rather than to confounding variables.
  2. Longitudinal Studies with Temporal Precedence: To establish causation, the cause must precede the effect in time. Longitudinal studies that follow subjects over time can help establish this temporal order, especially when combined with controls for potential confounders.
  3. Granger Causality: In time-series data, Granger causality tests can be used to infer if one time-series can predict another. This doesn’t establish true causality but can provide evidence of a predictive causal relationship.
  4. Control for Confounding Variables: Using statistical methods such as regression analysis with careful control for potential confounding variables can strengthen causal inferences. Instrumental variables and propensity score matching are techniques used to control for unobserved confounders.
  5. Use of Natural Experiments: Sometimes, researchers can take advantage of “natural experiments” where a change occurs in the environment that affects one group but not another. By comparing these groups, researchers may be able to infer causation.
  6. Mechanistic Understanding: Understanding the underlying mechanisms that explain how one variable could cause another can also provide evidence of causation. This might include laboratory experiments or theoretical models that elucidate the cause-and-effect process.
  7. Criteria like Bradford Hill’s Criteria: In epidemiology, criteria such as consistency, specificity, dose-response relationship, biological plausibility, and others are used as guidelines to support causal inferences.
  8. Combination of Evidence: Often, causality is best supported by a combination of evidence, including correlations, experimental data, mechanistic understanding, and theoretical consistency.
* In essence, inferring causation requires careful experimental design, rigorous statistical methods, and often a combination of different types of evidence. Even with these tools, establishing causation can be challenging and often requires ongoing validation and replication. It’s a nuanced process that must consider the complex interplay of variables, the context in which they operate, and the underlying mechanisms that might connect them.

## Spurious Correlation

* Spurious correlation refers to a situation where two or more variables appear to be related to each other, but the relationship is either coincidental or caused by a third, unobserved variable. In other words, the observed correlation between the variables does not imply a direct cause-and-effect relationship.
* Examples of Spurious Correlation:
  1. Coincidental Relationships: Sometimes, two variables may appear to be correlated simply due to chance. For example, there may be a correlation between the number of movies Nicolas Cage has appeared in a given year and the number of swimming pool drownings in that same year. Clearly, these two factors have no causal relationship, but the correlation might exist in the data.
  2. Confounding Variables: A spurious correlation can also be caused by a third variable that affects both of the correlated variables. For example, suppose ice cream sales and outdoor swimming incidents both increase in the summer. The correlation between ice cream sales and swimming incidents might be high, but it’s spurious because both are affected by the weather (temperature). The weather is the confounding variable causing the spurious correlation.
* Implications and Considerations:
  1. Misinterpretation: If not recognized, spurious correlations can lead to incorrect conclusions and poor decision-making. Assuming a causal relationship where none exists can lead to misguided actions and wasted resources.
  2. Statistical Analysis: Proper statistical analysis, including controlling for potential confounding variables and understanding the context of the data, is vital to recognize and avoid spurious correlations.
  3. Critical Thinking: A healthy dose of skepticism and domain knowledge can help identify potential spurious correlations. Understanding the underlying mechanisms and logic behind relationships is crucial to distinguishing genuine correlations from spurious ones.
* Spurious correlation is a common statistical phenomenon that underscores the importance of the maxim “correlation does not imply causation.” Identifying and understanding spurious correlations is essential in both academic research and practical applications to avoid drawing incorrect conclusions from data. It requires careful data analysis, consideration of potential confounders, and an understanding of the underlying subject matter.

## Causal Effects

### Stratification

## Attribution analysis

## Ladder of Causation

* The image below, [(source)](https://subscription.packtpub.com/book/data/9781804612989/3/ch03lvl1sec09/from-associations-to-logic-and-imagination-the-ladder-of-causation)

## References

* [Data Science at Microsoft](https://medium.com/data-science-at-microsoft/causal-inference-part-1-of-3-understanding-the-fundamentals-816f4723e54a)
* [Towards Data Science](https://towardsdatascience.com/a-complete-guide-to-causal-inference-8d5aaca68a47)
