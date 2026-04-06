# Primers • Naive Bayes

**Source:** https://aman.ai/primers/ai/naive-bayes/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [From Bayes’ theorem \(\rightarrow\) Naive Bayes](#from-bayes-theorem-rightarrow-naive-bayes)
* [Example: Applying Bayes’ Theorem with All Terms](#example-applying-bayes-theorem-with-all-terms)
  + [Given Data](#given-data)
  + [Calculating Posterior Probabilities](#calculating-posterior-probabilities)
  + [Conclusion](#conclusion)
* [Key Concepts](#key-concepts)
  + [Bayesian Probability](#bayesian-probability)
  + [Conditional Independence Assumption](#conditional-independence-assumption)
  + [Types of Naive Bayes Classifiers](#types-of-naive-bayes-classifiers)
  + [Parameter Estimation](#parameter-estimation)
* [Loss Function](#loss-function)
* [Applications](#applications)
  + [Text Classification and Sentiment Analysis](#text-classification-and-sentiment-analysis)
  + [Medical Diagnosis](#medical-diagnosis)
  + [Email Spam Filtering](#email-spam-filtering)
  + [Recommendation Systems](#recommendation-systems)
  + [Real-time Prediction](#real-time-prediction)
* [Pros and Cons](#pros-and-cons)
  + [Pros](#pros)
  + [Cons](#cons)
* [Example](#example)
  + [Problem: Spam Detection](#problem-spam-detection)
    - [Step 1: Compute Priors](#step-1-compute-priors)
    - [Step 2: Compute Likelihoods](#step-2-compute-likelihoods)
    - [Step 3: Compute Posterior](#step-3-compute-posterior)
    - [Step 4: Classification](#step-4-classification)
* [Citation](#citation)

## Overview

* Naive Bayes is a family of probabilistic algorithms based on Bayes’ theorem, with the “naive” assumption of conditional independence between every pair of features given the class label. It is widely used for classification tasks due to its simplicity, efficiency, and interpretability.
* Naive Bayes algorithms are primarily used in supervised learning tasks for classification problems. The approach applies Bayes’ theorem to calculate the probability of a given sample belonging to each possible class and assigns the sample to the class with the highest posterior probability.
* Despite its simplifying assumptions, Naive Bayes remains a robust and efficient tool for a wide range of practical applications, particularly in domains like text analysis and medical diagnostics. Its simplicity and interpretability make it a popular choice for baseline models and quick analyses.

## From Bayes’ theorem \(\rightarrow\) Naive Bayes

* Bayes’ theorem is expressed as:

  \[P(C|X) = \frac{P(X|C)P(C)}{P(X)}\]
  + where:
    - \(P(C \mid X)\) is the posterior probability of the class \(C\) given the data \(X\).
    - \(P(X \mid C)\) is the likelihood of data \(X\) given class \(C\).
    - \(P(C)\) is the prior probability of class \(C\).
    - \(P(X)\) is the marginal probability of data \(X\).
* The “naive” assumption simplifies the likelihood \(P(X \mid C)\) by assuming that features are conditionally independent given the class. For \(n\) features \(x\_1, x\_2, \dots, x\_n\), this assumption allows us to express:

\[P(X|C) = P(x\_1, x\_2, \dots, x\_n | C) = \prod\_{i=1}^n P(x\_i | C)\]

## Example: Applying Bayes’ Theorem with All Terms

* To understand the terms in Bayes’ theorem, consider a simple spam email classification problem. Suppose we want to classify an email as either “Spam” (S) or “Not Spam” (\(\neg S\)) based on a feature \(X\), which is the presence of the word “offer” in the email.

### Given Data

1. **Prior probabilities**:

   * \(P(S) = 0.2\) (20% of emails are spam).
   * \(P(\neg S) = 0.8\) (80% of emails are not spam).
2. **Likelihoods**:

   * \(P(X \mid S) = 0.9\) (90% of spam emails contain the word “offer”).
   * \(P(X \mid \neg S) = 0.1\) (10% of non-spam emails contain the word “offer”).
3. **Marginal probability**:

   * \(P(X) = P(X \mid S)P(S) + P(X \mid \neg S)P(\neg S)\):
     \(P(X) = (0.9 \cdot 0.2) + (0.1 \cdot 0.8) = 0.18 + 0.08 = 0.26.\)

### Calculating Posterior Probabilities

* Using Bayes’ theorem:

1. **For Spam**:
   \(P(S | X) = \frac{P(X | S)P(S)}{P(X)} = \frac{0.9 \cdot 0.2}{0.26} = \frac{0.18}{0.26} \approx 0.692.\)
2. **For Not Spam**:
   \(P(\neg S | X) = \frac{P(X | \neg S)P(\neg S)}{P(X)} = \frac{0.1 \cdot 0.8}{0.26} = \frac{0.08}{0.26} \approx 0.308.\)

### Conclusion

* The posterior probabilities indicate that the email is more likely to be spam (\(P(S \mid X) \approx 0.692\)) than not spam (\(P(\neg S \mid X) \approx 0.308\)). Thus, the email would be classified as spam based on this model.
* This example demonstrates the roles of all terms in Bayes’ theorem:
  + **Prior probabilities** (\(P(S)\) and \(P(\neg S)\)) represent the base rates of each class.
  + **Likelihoods** (\(P(X \mid S)\) and \(P(X \mid \neg S)\)) quantify the probability of observing the feature given each class.
  + **Marginal probability** (\(P(X)\)) ensures proper normalization of posterior probabilities.
  + **Posterior probability** (\(P(S \mid X)\)) provides the final classification decision.

## Key Concepts

### Bayesian Probability

* The foundation of Naive Bayes lies in Bayesian probability, where we update our prior beliefs based on new evidence.

### Conditional Independence Assumption

* The algorithm assumes that features are independent given the class. This assumption simplifies computation but may not always hold in real-world data.

### Types of Naive Bayes Classifiers

* Depending on the type of data, different variations of Naive Bayes are used:
  + **Gaussian Naive Bayes**: Assumes continuous data is normally distributed.
  + **Multinomial Naive Bayes**: Suitable for discrete count data, such as word frequencies in text classification.
  + **Bernoulli Naive Bayes**: Suitable for binary/boolean features.

### Parameter Estimation

* Parameters \(P(C)\) (prior) and \(P(x\_i \mid C)\) (likelihood) are estimated using Maximum Likelihood Estimation (MLE), which counts the occurrences in the training data to compute probabilities.

## Loss Function

* The goal of Naive Bayes is to maximize the posterior probability. Alternatively, we minimize a loss function based on the log-likelihood. The negative log-likelihood (NLL) is commonly used as the loss function:

  \[\text{NLL} = - \sum\_{i=1}^N \log P(C\_i | X\_i)\]
  + where \(N\) is the number of training samples, \(C\_i\) is the true class label for sample \(i\), and \(P(C\_i \mid X\_i)\) is the predicted probability for the correct class.

## Applications

### Text Classification and Sentiment Analysis

* Naive Bayes is frequently used in Natural Language Processing (NLP) tasks such as spam detection, sentiment analysis, and document classification due to its efficiency with high-dimensional data.

### Medical Diagnosis

* Useful for predicting diseases based on symptoms, assuming conditional independence between symptoms.

### Email Spam Filtering

* Detects spam emails by analyzing the frequency of specific words in the email content.

### Recommendation Systems

* Predicts user preferences based on past behaviors.

### Real-time Prediction

* Due to its computational efficiency, Naive Bayes is effective in real-time applications.

## Pros and Cons

### Pros

1. **Simplicity**: Easy to implement and interpret.
2. **Efficiency**: Computationally fast, especially with large datasets.
3. **Scalability**: Handles high-dimensional data well, such as text data.
4. **No Iterative Parameter Estimation**: Training involves simple computations.

### Cons

1. **Conditional Independence Assumption**: Rarely holds in practice, which may degrade performance.
2. **Limited Expressiveness**: Assumes simple relationships between features and the target variable.
3. **Data Imbalance**: Sensitive to imbalanced datasets, as probabilities can be dominated by frequent classes.
4. **Feature Engineering**: May require careful preprocessing and feature selection for optimal performance.

## Example

### Problem: Spam Detection

* Suppose we have two classes: \(C\_1\) (Spam) and \(C\_2\) (Not Spam). The features are words in an email (\(X = \{x\_1, x\_2, x\_3, \dots, x\_n\}\)).

#### Step 1: Compute Priors

\[P(C\_1) = \frac{\text{Number of Spam Emails}}{\text{Total Emails}}\]
\[P(C\_2) = \frac{\text{Number of Not Spam Emails}}{\text{Total Emails}}\]

#### Step 2: Compute Likelihoods

* For each word \(x\_i\), compute \(P(x\_i \mid C\_1)\) and \(P(x\_i \mid C\_2)\) using word frequencies.

#### Step 3: Compute Posterior

* For a new email, compute:

\[P(C\_1 | X) \propto P(C\_1) \prod\_{i=1}^n P(x\_i | C\_1)\]
\[P(C\_2 | X) \propto P(C\_2) \prod\_{i=1}^n P(x\_i | C\_2)\]

#### Step 4: Classification

* Assign the email to the class with the highest posterior probability.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledNaiveBayes,
  title   = {Naive Bayes},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
