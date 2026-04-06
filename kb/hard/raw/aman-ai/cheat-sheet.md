# Cheat Sheet

**Source:** https://aman.ai/sysdes/MLCheatSheet/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
  + [Offline objectives:](#offline-objectives)
  + [Online evaluation:](#online-evaluation)
  + [Feature Engineering:](#feature-engineering)
  + [Training:](#training)
  + [Models:](#models)
  + [Deep Learning:](#deep-learning)
  + [Recommendation Systems:](#recommendation-systems)

## Overview

Quick Cheat Sheet:

### Offline objectives:

* Distances: These are measurement methods used to determine the similarity or dissimilarity between data points. Common distance metrics include cosine similarity, dot product similarity, Hamming distance, Jaccard similarity, and Levenshtein distance (for strings).
* Precision, recall, F1, calibration: These are evaluation metrics commonly used in classification tasks. Precision measures the proportion of correctly predicted positive instances out of the total predicted positive instances, while recall measures the proportion of correctly predicted positive instances out of the total actual positive instances. F1 score is the harmonic mean of precision and recall, providing a balanced measure. Calibration refers to the agreement between predicted probabilities and the actual probabilities of class membership.
* RMSE (Root Mean Square Error), SSE (Sum of Squared Errors): These are commonly used metrics to evaluate regression models. RMSE measures the average deviation of predicted values from the actual values, while SSE sums the squared differences between predicted and actual values.
* Ranking metrics: These metrics assess the quality of ranked lists. NDCG (Normalized Discounted Cumulative Gain) takes into account both relevance and ranking position of items. p@k measures precision at a given cutoff k, while r@k measures recall at cutoff k. MAP (Mean Average Precision) averages the average precision scores over different rankings.

### Online evaluation:

* A/B testing: A statistical method used to compare two or more versions of a webpage, feature, or algorithm (A and B) to determine which performs better based on predefined metrics.
* Business KPIs (Key Performance Indicators): These are specific metrics used to evaluate the performance of a business. Common KPIs include revenue, customer retention rate, user engagement, conversion rate, and churn rate.

### Feature Engineering:

* Continuous data: Techniques like demeaning (subtracting the mean) and normalization (scaling to a specific range) are often applied to handle continuous numeric features and improve model performance.
* Discrete data: One-hot encoding converts categorical variables into binary vectors, where each category becomes a separate binary feature. Embeddings are dense representations of categorical variables, learned from data using techniques like word2vec or GloVe.
* Principal Component Analysis (PCA): A dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional space while preserving the most important information.

### Training:

* Test, train, holdout split: The dataset is divided into training, testing, and holdout (validation) sets. The training set is used to train the model, the testing set is used to evaluate performance during model development, and the holdout set is used for final evaluation on unseen data.
* K-folds cross-validation: The dataset is split into k subsets (folds), and the model is trained and evaluated k times, each time using a different fold as the validation set and the remaining folds as the training set.
* Training sample selection: In some cases, such as in recommendation systems, negative sampling is used to create training samples with a balanced distribution of positive and negative instances.

### Models:

* Linear regressions: Linear models that aim to establish a linear relationship between the independent variables and the target variable.
* Boosted Trees: Ensemble models that combine multiple decision trees to make predictions, where subsequent trees focus on correcting the errors of previous trees.
* Deep learning: Neural networks with multiple hidden layers, capable of learning complex patterns and representations from data.

### Deep Learning:

* Understand theoretical background: It involves gaining knowledge of concepts such as optimizers (e.g., gradient descent-based methods), backpropagation (the process of calculating gradients and updating weights), and activation functions used in deep learning models.

### Recommendation Systems:

* Collaborative Filtering: A technique that predicts user preferences based on similarities or patterns observed among users or items in a dataset.
* Candidate Selection: The process of selecting potential recommendations for users based on their preferences or characteristics.
* Ranking metrics for evaluation: These metrics assess the quality of the recommendation list presented to the user, considering factors like relevance, diversity, and user satisfaction.
