# ML System Design Framework

**Source:** https://aman.ai/mlsysdes/framework/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-system-design

---

* [Overview](#overview)
* [Clarifying requirements](#clarifying-requirements)
* [Frame the problem as an ML task](#frame-the-problem-as-an-ml-task)
* [Specify System input and output](#specify-system-input-and-output)
* [Choose the right ML category](#choose-the-right-ml-category)
* [Data prep](#data-prep)
  + [Data engineering](#data-engineering)
  + [Data sources](#data-sources)
  + [Data storage](#data-storage)
  + [Feature engineering- ML context not DL](#feature-engineering--ml-context-not-dl)
  + [Feature engineering operations](#feature-engineering-operations)
* [Model Development](#model-development)
  + [Model Selection](#model-selection)
* [Model Training](#model-training)
  + [Constructing the dataset](#constructing-the-dataset)
  + [Choosing the loss function](#choosing-the-loss-function)
  + [Regularization Techniques:](#regularization-techniques)
  + [Backpropagation:](#backpropagation)
  + [Optimization Methods:](#optimization-methods)
* [Evaluation](#evaluation)
  + [Offline Metrics for Various Tasks:](#offline-metrics-for-various-tasks)
    - [Classification](#classification)
    - [Regression](#regression)
    - [Ranking](#ranking)
    - [Image Generation](#image-generation)
    - [Natural Language Processing (NLP)](#natural-language-processing-nlp)
  + [Online Eval](#online-eval)
* [Deployment and Serving](#deployment-and-serving)
* [Model compression](#model-compression)
* [Test in production](#test-in-production)
* [Prediction pipeline](#prediction-pipeline)
* [Monitoring in Machine Learning Systems](#monitoring-in-machine-learning-systems)
  + [Why a System Fails in Production](#why-a-system-fails-in-production)
  + [What to Monitor](#what-to-monitor)
* [Infrastructure in ML](#infrastructure-in-ml)

## Overview

1. Clarifying requirements
2. Framing the problem as an ML task
3. Data preparation
4. Model development
5. Evaluation
6. Deployment and serving
7. Monitoring and infrastructure

## Clarifying requirements

* ML system design questions are usually intentionally vague, with the bare minimum of information. For example, an interview question could be: “design an event recommendation system”. The first step is to ask clarifying questions. But what kind of questions to ask? Well, we should ask questions to understand the exact requirements. Here is a list of categorized questions to help us get started:
* Business objective. If we are asked to create a system to recommend vacation rentals, two possible motivations are to increase the number of bookings and increase the revenue.
* Features the system needs to support. What are some of the features that the system is expected to support which could affect our ML system design? For example, let’s assume we’re asked to design a video recommendation system. We might want to know if users can “like” or “dislike” recommended videos, as those interactions could be used to label training data.
* Data. What are the data sources? How large is the dataset? Is the data labeled?
* Constraints. How much computing power is available? Is it a cloud-based system, or should the system work on a device? Is the model expected to improve automatically over time?
* Scale of the system. How many users do we have? How many items, such as videos, are we dealing with? What’s the rate of growth of these metrics?
* Performance. How fast must prediction be? Is a real-time solution expected? Does accuracy have more priority or latency?

## Frame the problem as an ML task

* Effective problem framing plays a critical role in solving ML problems. Suppose an interviewer asks you to increase the user engagement of a video streaming platform. Lack of user engagement is certainly a problem, but it’s not an ML task. So, we should frame it as an ML task in order to solve it. In reality, we should first determine whether or not ML is necessary for solving a given problem. In an ML system design interview, it’s safe to assume that ML is helpful. So, we can frame the problem as an ML task by doing the following:
  + Defining the ML objective
  + Specifying the system’s input and output
  + Choosing the right ML category
* Defining the ML objective
  + A business objective can be to increase sales by 20% or to improve user retention. But the objective may not be well defined, and we cannot train a model simply by telling it, “increase sales by 20%”. For an ML system to solve a task, we need to translate the business objective into a well-defined ML objective. A good ML objective is one that ML models can solve. Let’s look at some examples as shown in Table 1.1. In later chapters, we will see more examples.

## Specify System input and output

* Once we decide on the ML objective, we need to define the system’s inputs and outputs. For example, for a harmful content detection system on a social media platform, the input is a post, and the output is whether this post is considered harmful or not.

* In some cases, the system may consist of more than one ML model. If so, we need to specify the input and output of each ML model. For example, for harmful content detection, we may want to use one model to predict violence and another model to predict nudity. The system depends on these two models to determine if a post is harmful or not.
* Another important consideration is that there might be multiple ways to specify each model’s input-output. Figure 1.4 shows an example.

## Choose the right ML category

* There are many different ways to frame a problem as an ML task. Most problems can be framed as one of the ML categories (leaf nodes) shown in Figure 1.5. As most readers are likely already familiar with them, we only provide an outline here.

* Supervised learning. A supervised learning model learns a task by using a training dataset. In reality, many problems fall into this category, since learning from a labeled dataset usually leads to better results.
* Unsupervised learning. Unsupervised learning models make predictions by processing data that contain no correct answers. The goal of an unsupervised learning model
* Reinforcement learning. In reinforcement learning, a computer agent learns to perform a task through repeated trial-and-error interactions with the environment. For example, robots can be trained to walk around a room using reinforcement learning, and software programs like AlphaGo can compete in the game of Go by using reinforcement learning.
* Compared to supervised learning, unsupervised learning and reinforcement learning are less popular in real-world systems, as ML models usually learn a specific task better when training data is available. As a result, the majority of problems we tackle in this book rely on supervised learning. Let’s take a closer look at the different categories of supervised learning.
* Classification model. Classification is the task of predicting a discrete class label; for example, whether an input image should be classified as “dog”, “cat”, or “rabbit”. Classification models can be divided into two groups:
* Binary classification models predict a binary outcome. For example, the model predicts whether an image contains a dog or not
* Multiclass classification models classify the input into more than one class. For example, we can classify an image as a dog, cat, or rabbit
* In this step, you are expected to choose the correct ML category. Later chapters provide examples of how to choose the right category during an interview.
* Talking points
  + Here are some topics we might want to talk about during an interview:
  + What is a good ML objective? How do different ML objectives compare? What are the pros and cons?
  + What are the inputs and outputs of the system, given the ML objective?
  + If more than one model is involved in the ML system, what are the inputs and outputs of each model?
  + Does the task need to be learned in a supervised or unsupervised way?
  + Is it better to solve the problem using a regression or classification model? In the case of classification, is it binary or multiclass? In the case of regression, what is the output range?

## Data prep

* ML models learn directly from data, meaning that data with predictive power is essential for training an ML model. This section aims to prepare high-quality inputs for ML models via two essential processes: data engineering and feature engineering. We will cover the important aspects of each process.

### Data engineering

* collecting, storing, retrieving data
* Extract, transform, and load (ETL)
* ETL consists of three phases:
* Extract. This process extracts data from different data sources.
* Transform. In this phase, data is often cleansed, mapped, and transformed into a specific format to meet operational needs.
* Load. The transformed data is loaded into the target destination, which can be a file, a database, or a data warehouse [1].
* Take the data stored from MySql, extract and transform into DataFrames via PySpark, Load onto a new db
* Data engineering is the practice of designing and building pipelines for collecting, storing, retrieving, and processing data. Let’s briefly review data engineering fundamentals to understand the core components we may need.

### Data sources

* An ML system can work with data from many different sources. Knowing the data sources is a good way to answer many context questions, which may include: who collected it? How clean is the data? Can the data source be trusted? Is the data user-generated or system generated?

### Data storage

* Data storage, also called a database, is a repository for persistently storing and managing collections of data. Different databases are built to satisfy different use cases, so it’s important to understand at a high level how different databases work. You are usually not expected to know database internals during ML system design interviews.

### Feature engineering- ML context not DL

* Feature engineering contains two processes:
* Using domain knowledge to select and extract predictive features from raw data
* Transforming predictive features into a format usable by the model
* Choosing the appropriate features is one of the most important decisions when developing and training ML models. It’s essential to choose features that bring the most value, and this feature engineering process requires subject matter expertise and is also highly dependent upon the task at hand. To help you master this process, we give many examples throughout this book.
* Once the predictive features are chosen, they need to be transformed into suitable formats using feature engineering operations, which we examine next.

### Feature engineering operations

* It’s quite common for some of the selected features to not be in a format the model can use. Feature engineering operations transform the selected features into a format the model can use. Techniques include handling missing values, scaling values that have skewed distributions, and encoding categorical features. The following list is not comprehensive, but it contains some of the most common operations for structured data.
* Handling missing values:
  + Data in production often has missing values, which can generally be addressed in two ways: deletion or imputation.
* Deletion:
  + This method removes any records with a missing value in any of the features. Deletion can be divided into row deletion and column deletion. In column deletion, we remove the whole column representing a feature, if the feature has too many missing values. In row deletion, we remove a row representing a data point if the data point has many missing values.

* The drawback of deletion is that it reduces the quantity of data the model can potentially use for training. This is not ideal since ML models tend to work better when they are exposed to more data.
* Imputation. Alternatively, we can impute the missing values by filling them with certain values. Some common practices include:
  + Filling in missing values with their defaults
  + Filling in missing values with the mean, median, or mode (the most common value)
* The drawback of imputation is it may introduce noise to the data. It’s important to note that no technique is perfect for handling missing values, as each has its trade-offs
* Feature scaling
  + Feature scaling refers to the process of scaling features to have a standard range and distribution. Let’s first look at why feature scaling might be needed.
* Many ML models struggle to learn a task when the features of the dataset are in different ranges. For example, features such as age and income might have different value ranges. In addition, some models may struggle to learn the task when a feature has a skewed distribution. What are some of the feature scaling techniques? Let’s take a look.
* Normalization (min-max scaling). In this approach, the features are scaled, so all values are within the range [0,1] using the following formula:

\[z = \frac{x - x\_{\text{min}}}{x\_{\text{max}} - x\_{\text{min}}}\]

* Note that normalization does not change the distribution of the feature. In order to change the distribution of a feature to follow a standard distribution, standardization is used.
* Standardization (Z-score normalization). Standardization is the process of changing the distribution of a feature to have a 0 mean and a standard deviation of 1.
* Log scaling. To mitigate the skewness of a feature, a common technique called log scaling can be used. Log transformation can make data distribution less skewed, and enable the optimization algorithm to converge faster.
* Discretization (Bucketing)
  + Discretization is the process of converting a continuous feature into a categorical feature. For example, instead of representing height as a continuous feature, we can divide heights into discrete buckets and represent each height by the bucket to which it belongs. This allows the model to focus on learning only a few categories instead of attempting to learn an infinite number of possibilities.

* Discretization can also be applied to discrete features. For example, a user’s age is a discrete feature, but discretizing it reduces the number of categories, as shown in Table 1.3.

* Encoding categorical features
  + In most ML models, all inputs and outputs must be numerical. This means if a feature is categorical, we should encode it into numbers before sending it to the model. There are three common methods for converting categorical features into numeric representations: integer encoding, one-hot encoding, and embedding learning.
* Integer encoding. An integer value is assigned to each unique category value. For example, “Excellent” is 1, “Good” is 2, and “Bad” is 3. This method is useful if the integer values have a natural relationship with each other.
* However, when there is no ordinal relationship between categorical features, integer encoding is not a good choice. One-hot encoding, which we will examine next, addresses this issue.
* One-hot encoding. With this technique, a new binary feature is created for each unique value. As shown in Figure 1.14, we replace the original feature (color) with three new binary features (red, green, and blue). For example, if a data point has a “red” color, we replace it with “1,0,0”.
* Embedding learning. Another way to encode a categorical feature is to use embedding learning. An embedding is a mapping of a categorical feature into an N-dimensional vector. Embedding learning is the process of learning an N-dimensional vector for each unique value that the categorical feature may take. This approach is useful when the number of unique values the feature takes is very large. In this case, one-hot encoding is not a good option because it leads to very large vector sizes. We will see more examples in later chapters.
* Talking points
* Here are some topics we might want to discuss during the interview:
  + Data availability and data collection: What are the data sources? What data is available to us, and how do we collect it? How large is the data size? How often do new data come in?
  + Data storage: Where is the data currently stored? Is it on the cloud or on user devices? Which data format is appropriate for storing the data? How do we store multimodal data, e.g., a data point that might contain both images and texts?
  + Feature engineering: How do we process raw data into a form that’s useful for the models? What should we do about missing data? Is feature engineering required for this task? Which operations do we use to transform the raw data into a format usable by the ML model? Do we need to normalize the features? Which features should we construct from the raw data? How do we plan to combine data of different types, such as texts, numbers, and images?
  + Privacy: How sensitive are the available data? Are users concerned about the privacy of their data? Is anonymization of user data necessary? Is it possible to store users’ data on our servers, or is it only possible to access their data on their devices?
  + Biases: Are there any biases in the data? If yes, what kinds of biases are present, and how do we correct them?

## Model Development

* Model development refers to the process of selecting an appropriate ML model and training it to solve the task at hand.

### Model Selection

* Model selection is the process of choosing the best ML algorithm and architecture for a predictive modeling problem. In practice, a typical process for selecting a model is to:
  + Establish a simple baseline. For example, in a video recommendation system, the baseline can be obtained by recommending the most popular videos.
  + Experiment with simple models. After we have a baseline, a good practice is to explore ML algorithms that are quick to train, such as logistic regression.
  + Switch to more complex models. If simple models cannot deliver satisfactory results, we can then consider more complex models, such as deep neural networks.
  + Use an ensemble of models if we want more accurate predictions. Using an ensemble of multiple models instead of only one may improve the quality of predictions. Creating an ensemble can be accomplished in three ways: bagging [3], boosting [4], and stacking [5], which will be discussed in later chapters.
* In an interview setting, it’s important to explore various model options and discuss their pros and cons. Some typical model options include:
  + Logistic regression
  + Linear regression
  + Decision trees
  + Gradient boosted decision trees and random forests
  + Support vector machines
  + Naive Bayes
  + Factorization Machines (FM)
  + Neural networks
* When examining different options, it’s good to briefly explain the algorithm and discuss the trade-offs. For example, logistic regression may be a good option for learning a linear task, but if the task is complex, we may need to choose a different model. When choosing an ML algorithm, it’s important to consider different aspects of a model. For example:
  + The amount of data the model needs to train on
  + Training speed
  + Hyperparameters to choose and hyperparameter tuning techniques
  + Possibility of continual learning
  + Compute requirements. A more complex model might deliver higher accuracy, but might require more computing power, such as a GPU instead of a CPU
  + Model’s interpretability. A more complex model can give better performance, but its results may be less interpretable
* There is no single best algorithm that solves all problems. The interviewer wants to see if you have a good understanding of different ML algorithms, their pros and cons, and your ability to choose a model based on requirements and constraints. To help you improve model selection, this book contains a variety of model selection examples. This book assumes you are familiar with common ML algorithms.

## Model Training

* loss function
* Training from scratch vs finetuning
* Once the model selection is complete, it’s time to train the model. During this step, there are various topics you may want to discuss at an interview, such as:
  + Constructing the dataset
  + Choosing the loss function
  + Training from scratch vs. fine-tuning
  + Distributed training
* Let’s look at each one

### Constructing the dataset

* At an interview, it’s usually a good idea to talk about constructing the dataset for model training and evaluation. As Figure 1.15 illustrates, there are 5 steps in constructing the dataset.
* All the steps except “identify features and labels” are generic operations, which can be applied to any ML system design task. In this chapter, we will take a close look at each step, but in later chapters, we will mainly focus on “identify features and labels,” which is task-specific.
* Collect the raw data
  + This is extensively discussed in the data preparation step, so we do not repeat it here.
* Identify features and labels
  + During the feature engineering step, we have already discussed which features to use. So, let’s focus on creating labels for the data. There are two common ways to get labels: hand labeling and natural labeling.
* Hand labeling. This means individual annotators label the data by hand. For example, an individual annotator labels whether a post contains misinformation or not. Hand labeling leads to accurate labels since a human is involved in the process. However, hand labeling has many drawbacks; it is expensive and slow, introduces bias, requires domain knowledge, and is a threat to data privacy.
* Natural labeling. In natural labeling, the ground truth labels are inferred automatically without human annotations. Let’s see an example to better understand natural labels.
* Suppose we want to design an ML system that ranks news feeds based on relevance. One possible way to solve this task is to train a model which takes a user and a post as input, and outputs the probability that the user will press the ``like” button after seeing this post. In this case, the training data are pairs of ⟨ user, post ⟩ and their corresponding label, which is 1 if the user liked the post, and 0 if they did not. This way, we are able to naturally label the training data without relying on human annotations.
* In this step, it is important to clearly communicate how we obtain training labels and what the training data looks like.
* Select a sampling strategy
  + It is often impractical to collect all the data, so sampling is an efficient way to reduce the amount of data in the system. Common sampling strategies include convenience sampling, snowball sampling, stratified sampling, reservoir sampling, and importance sampling. To learn more about sampling methods, you can refer to [8].
* Split the data
  + Data splitting refers to the process of dividing the dataset into training, evaluation (validation), and test dataset. To learn more about data splitting techniques, refer to [9].
* Address any class imbalances
  + A dataset with skewed class labels is called an imbalanced dataset. The class that makes up a larger proportion of the dataset is called the majority class, and the class which comprises a smaller proportion of the dataset is known as the minority class.
* An imbalanced dataset is a serious issue in model training, as it means a model may not have enough data to learn the minority class. There are different techniques to mitigate this issue. Let’s take a look at two commonly used approaches: resampling training data and altering the loss function.
* Resampling training data
  + Resampling refers to the process of adjusting the ratio between different classes, making the data more balanced. For example, we can oversample the minority class (Figure 1.17) or undersample the majority class (Figure 1.18)
* Altering the loss function
  + This technique alters the loss function to make it more robust against class imbalance. The high-level idea is to give more weight to data points from the minority class. A higher weight in the loss function penalizes the model more when it makes a wrong prediction about a minority class. This forces the model to learn minority classes more effectively. Two commonly used loss functions to mitigate class imbalance are class-balanced loss [10] and focal loss [11][12].

### Choosing the loss function

* Once the dataset is constructed, we need to choose a proper loss function to train the model. A loss function is a measurement of how accurate the model is at predicting an expected outcome. The loss function allows the optimization algorithm to update the model’s parameters during the training process in order to minimize the loss.
* Designing a novel loss function is not easy. In ML interviews, you are usually expected to select a loss function from a list of existing loss functions based on how you framed the problem. Sometimes, you might need to make minor changes to the loss function to make it specific to the problem. We will provide more examples in later chapters.
* Training from scratch vs. fine-tuning
  + One topic that might be useful to discuss briefly is training from scratch vs. fine-tuning. Fine-tuning means continuing to train the model on new data by making small changes to its learned parameters. This is a design decision you may need to discuss with the interviewer.
* Distributed training
  + Training at scale becomes increasingly important because models grow bigger over time, and the size of the dataset also increases dramatically. Distributed training is commonly used to train the model, by dividing the work among multiple worker nodes. These worker nodes operate in parallel in order to speed up model training. There are two main types of distributed training: data parallelism [13] and model parallelism [14].
* Depending on which task we are solving, employing distributed training may be necessary. In such cases, it’s important to discuss this topic with the interviewer. Note that distributed training is a generic topic you can talk about irrespective of the specific task.
* Talking points
  + Some talking points are listed below:
* Model selection: Which ML models are suitable for the task, and what are their pros and cons. Here’s a list of topics to consider during model selection:
  + The time it takes to train
  + The amount of training data the model expects
  + The computing resources the model may need
  + Latency of the model at inference time
  + Can the model be deployed on a user’s device?
  + Model’s interpretability. Making a model more complex may increase its performance, but the results might be harder to interpret
  + Can we leverage continual training, or should we train from scratch?
  + How many parameters does the model have? How much memory is needed?
  + For neural networks, you might want to discuss typical architectures/blocks, such as ResNet or Transformer-based architectures. You can also discuss the choice of hyperparameters, such as the number of hidden layers, the number of neurons, activation functions, etc.
* Dataset labels: How should we obtain the labels? Is the data annotated, and if so, how good are the annotations? If natural labels are available, how do we get them? How do we receive user feedback on the system? How long does it take to get natural labels?
* Model training.
  + What loss function should we choose? (e.g., Cross-entropy [15], MSE [16], MAE [17], Huber loss [18], etc.)
  + What regularization should we use? (e.g., L1 [19], L2 [19], Entropy Regularization [20], K-fold CV [21], or dropout [22])
  + What is backpropagation?
  + You may need to describe common optimization methods [23] such as SGD [24], AdaGrad [25], Momentum [26], and RMSProp [27].
  + What activation functions do we want to use and why? (e.g., ELU [28], ReLU [29], Tanh [30], Sigmoid [31]).
  + How to handle an imbalanced dataset?
  + What is the bias/variance trade-off?
  + What are the possible causes of overfitting and underfitting? How to address them?
* Continual learning: Do we want to train the model online with each new data point? Do we need to personalize the model to each user? How often do we retrain the model? Some models need to be retrained daily or weekly, and others monthly or yearly.

### Regularization Techniques:

1. **L1 Regularization**: Penalizes the absolute values of the weights, encourages sparsity in the model (i.e., small weights are driven to zero).
2. **L2 Regularization**: Penalizes the squared values of the weights, discourages large weights and helps prevent overfitting.
3. **Entropy Regularization**: Often used in classification tasks to penalize deviations from a predefined distribution, which can introduce additional stability or enforce desired properties.
4. **K-fold Cross Validation (CV)**: A technique for assessing a model’s performance where the data is split into K subsets, and the model is trained K times, each time using K-1 folds for training and a different fold for validation.
5. **Dropout**: A regularization technique for neural networks where randomly selected neurons are ignored (i.e., set their weights to zero) during training, which helps to prevent overfitting.

### Backpropagation:

* **Backpropagation**: An algorithm used in training neural networks, where the error is computed at the output and distributed back through the network’s layers to update the weights, thus minimizing the error by adjusting all weights by gradient descent (or another optimization algorithm).

### Optimization Methods:

1. **Stochastic Gradient Descent (SGD)**: An optimization method where updates to the weights are made after each training example, which can be computationally efficient and allows for online learning.
2. **AdaGrad**: An adaptive gradient algorithm that adjusts the learning rates of all parameters, scaling them inversely proportional to the square root of the sum of all of their historical squared values, which can be beneficial for optimizing problems with noisy or sparse gradients.
3. **Momentum**: A method that helps accelerate SGD by navigating along the relevant directions and dampening oscillations, it does this by accumulating an exponentially decaying moving average of past gradients and continues to move in their direction.
4. **RMSProp**: An adaptive learning rate optimization method, which divides the learning rate by an exponentially decaying average of squared gradients; it is known for being effective in non-convex optimization problems of neural networks.

## Evaluation

* The next step after the model development is evaluation, which is the process of using different metrics to understand an ML model’s performance. In this section, we examine two evaluation methods, offline and online.

### Offline Metrics for Various Tasks:

* Offline evaluation refers to evaluating the performance of ML models during the model development phase. To evaluate a model, we usually first make predictions using the evaluation dataset. Next, we use various offline metrics to measure how close the predictions are to the ground truth values. Table 1.4 shows some of the commonly used metrics for different tasks.

* During an interview, it’s important to identify suitable metrics for offline evaluation. This depends on the task at hand and how we have framed it. For example, if we try to solve a ranking problem, we might need to discuss ranking metrics and their trade-offs.

#### Classification

* **Metrics**: Precision (true positives among predicted positives), Recall (true positives among actual positives), F1 Score (harmonic mean of precision and recall), Accuracy (correct predictions over total predictions), ROC-AUC (area under the Receiver Operating Characteristic curve), PR-AUC (area under the Precision-Recall curve), and Confusion Matrix (a table used to evaluate the performance by comparing predicted and actual values).

#### Regression

* **Metrics**: Mean Squared Error (MSE, average of squared differences between predicted and actual values), Mean Absolute Error (MAE, average of absolute differences between predicted and actual values), Root Mean Squared Error (RMSE, square root of MSE, providing error in the same units as the dependent variable).

#### Ranking

* **Metrics**: Precision@k (proportion of relevant items among the top-k), Recall@k (proportion of top-k items that are relevant), Mean Reciprocal Rank (MRR, average of the reciprocal ranks of the first relevant item), Mean Average Precision (mAP, mean of average precision scores for each query), and Normalized Discounted Cumulative Gain (nDCG, measures the performance of a recommendation system based on the query).

#### Image Generation

* **Metrics**: Fréchet Inception Distance (FID, measures the distance between feature vectors calculated for original and generated images using the Inception v3 model), Inception Score (quantifies how realistic generated images are based on the quality and diversity using the Inception model).

#### Natural Language Processing (NLP)

* **Metrics**: BLEU (Bilingual Evaluation Understudy, evaluates machine-translated text by comparing it to a set of reference translations), METEOR (Metric for Evaluation of Translation with Explicit ORdering, evaluates translation hypothesis by aligning it to one or more reference translations), ROUGE (Recall-Oriented Understudy for Gisting Evaluation, used for evaluating automatic summarization and machine translation), CIDEr (Consensus-based Image Description Evaluation, correlates human and machine scores in image description), SPICE (Semantic Propositional Image Caption Evaluation, evaluates image captions by comparing sets of semantic tuples).

### Online Eval

* Online evaluation refers to the process of evaluating how the model performs in production after deployment. To measure the impact of the model, we need to define different metrics. Online metrics refer to those we use during an online evaluation and are usually tied to business objectives. Table 1.5 shows various metrics for different problems.

* In practice, companies usually track many online metrics. At an interview, we need to select some of the most important ones to measure the impact of the system. As opposed to offline metrics, choosing online metrics Online metrics is subjective and depends upon product owners and business stakeholders.
* In this step, the interviewer gauges your business sense. So, it is helpful to communicate your thought process and your reasons for choosing certain metrics.
* Talking points
* Here are some talking points for the evaluation step:
  + Online metrics: Which metrics are important for measuring the effectiveness of the ML system online? How do these metrics relate to the business objective?
  + Offline metrics: Which offline metrics are good at evaluating the model’s predictions during the development phase?
  + Fairness and bias: Does the model have the potential for bias across different attributes such as age, gender, race, etc.? How would you fix this? What happens if someone with malicious intent gets access to your system?

## Deployment and Serving

* A natural next step after choosing the appropriate metrics for online and offline evaluations is to deploy the model to production and serve millions of users. Some important topics to cover include:
  + Cloud vs. on-device deployment
  + Model compression
  + Testing in production
  + Prediction pipeline
* Let’s take a look at each.

## Model compression

* Model compression refers to the process of making a model smaller. This is necessary to reduce the inference latency and model size. Three techniques are commonly used to compress models:
  + Knowledge distillation: The goal of knowledge distillation is to train a small model (student) to mimic a larger model (teacher).
  + Pruning: Pruning refers to the process of finding the least useful parameters and setting them to zero. This leads to sparser models which can be stored more efficiently.
  + Quantization: Model parameters are often represented with 32-bit floating numbers. In quantization, we use fewer bits to represent the parameters, which reduces the model’s size. Quantization can happen during training or post-training [39].
* To learn more about model compression, you are encouraged to read [40].

## Test in production

* A/B testing
* Bandit method
* Have guardrail metrics to watch here for friction
* The only way to ensure the model will perform well in production is to test it with real traffic. Commonly used techniques to test models include shadow deployment [41], A/B testing [42], canary release [43], interleaving experiments [44], bandits [45], etc.
* To demonstrate that we understand how to test in production, it’s a good idea to mention at least one of these methods. Let’s briefly review shadow deployment and A/B testing.
* Shadow deployment
  + In this method, we deploy the new model in parallel with the existing model. Each incoming request is routed to both models, but only the existing model’s prediction is served to the user.
  + By shadow deploying the model, we minimize the risk of unreliable predictions until the newly developed model has been thoroughly tested. However, this is a costly approach that doubles the number of predictions.
* A/B Testing
  + With this method, we deploy the new model in parallel with the existing model. A portion of the traffic is routed to the newly developed model, while the remaining requests are routed to the existing model.
  + In order to execute A/B testing correctly, there are two important factors to consider. First, the traffic routed to each model has to be random. Second, A/B tests should be run on a sufficient number of data points in order for the results to be legitimate.

## Prediction pipeline

* To serve requests in production, we need a prediction pipeline. An important design decision to make is the choice between online prediction and batch prediction.
* Batch prediction
  + With batch prediction, the model makes predictions periodically. Because predictions are pre-computed, we don’t need to worry about how long it takes the model to generate predictions once they are pre-computed.
  + However, the batch prediction has two major drawbacks. First, the model becomes less responsive to the changing preferences of users. Secondly, batch prediction is only possible if we know in advance what needs to be pre-computed. For example, in a language translation system, we are not able to make translations in advance as it entirely depends on the user’s input.
* Online prediction
  + In online prediction, predictions are generated and returned as soon as requests arrive. The main problem with online prediction is that the model might take too long to generate predictions.
  + This choice of batch prediction or online prediction is mainly driven by product requirements. Online prediction is generally preferred in situations where we do not know what needs to be computed in advance. Batch prediction is ideal when the system processes a high volume of data, and the results are not needed in real time.
  + As previously discussed, ML system development involves more than just ML modeling. Proposing an overall ML system design in an interview demonstrates a deep understanding of how different components work together as a whole. Interviewers often take this as a critical signal.

* Talking points
* Is model compression needed? What are some commonly used compression techniques?
* Is online prediction or batch prediction more suitable? What are the trade-offs?
* Is real-time access to features possible? What are the challenges?
* How should we test the deployed model in production?
* An ML system consists of various components working together to serve requests. What are the responsibilities of each component in the proposed design?
* What technologies should we use to ensure that serving is fast and scalable?

## Monitoring in Machine Learning Systems

* Monitoring involves tracking, measuring, and logging different metrics. It plays a crucial role in diagnosing failures in ML systems once they’re in production.

### Why a System Fails in Production

* An ML system can encounter various issues post-deployment. One of the prevalent reasons is **data distribution shift**.
* **Data Distribution Shift**: This arises when the data the model faces in production deviates from its training data. For instance, a model trained on front-view images of cups might struggle with images showcasing different angles (Figure 1.24). The dynamic nature of real-world data means training data becomes outdated over time, resulting in a model’s performance decline. To combat this:

  1. **Train on Large Datasets**: This ensures the model captures a broad distribution, prepping it for most data it encounters in production.
  2. **Frequent Model Retraining**: Update the model using labeled data from the evolving distribution.

### What to Monitor

* Post-production monitoring aims at pinpointing failures and recognizing shifts in the ML system.

1. **Operation-related Metrics**: These ensure the system’s operational integrity, comprising metrics like average serving times, throughput, CPU/GPU utilization, and more.
2. **ML-specific Metrics**:
   * **Monitoring I/O**: The quality of model predictions hinges on its input data.
   * **Detecting Drifts**: Keeping tabs on input and model output for potential distributional changes.
   * **Model Accuracy**: Ensuring the accuracy remains within an acceptable range.
   * **Versioning**: Observing the deployed model version.

## Infrastructure in ML

* Infrastructure forms the bedrock for training, deploying, and sustaining ML systems. While many ML interviews might bypass infrastructure inquiries, specific roles, especially in DevOps and MLOps, emphasize it. Interested readers can delve deeper into ML infrastructure through references [46], [47], and [48].
