# DeepMind

**Source:** https://aman.ai/h/deepmind/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overviews](#overviews)
  + [Initial Interview with a Recruiter](#initial-interview-with-a-recruiter)
    - [Applied DM](#applied-dm)
    - [Background](#background)
    - [Questions](#questions)
  + [Coding Interview](#coding-interview)
  + [Machine Learning Design Interview](#machine-learning-design-interview)
  + [System Design Interview](#system-design-interview)
  + [Technical Management Interviews](#technical-management-interviews)
  + [People & Culture Interview](#people--culture-interview)
    - [Question answers:](#question-answers)
  + [machine operation information](#machine-operation-information)
  + [Bayes](#bayes)
  + [L2 vs L1](#l2-vs-l1)
    - [GNN loss function by task](#gnn-loss-function-by-task)
    - [1. **Node Classification**](#1-node-classification)
    - [2. **Graph Classification**](#2-graph-classification)
    - [3. **Link Prediction**](#3-link-prediction)
    - [4. **Graph Generation**](#4-graph-generation)
    - [5. **Graph Reconstruction**](#5-graph-reconstruction)
    - [6. **Regularization Loss**](#6-regularization-loss)
    - [Additional Considerations](#additional-considerations)
  + [CNN Receptive Field](#cnn-receptive-field)
    - [Example:](#example)
  + [CNN vs RNN](#cnn-vs-rnn)
    - [1. **Model Architecture and Data Type**:](#1-model-architecture-and-data-type)
    - [2. **Training Complexity**:](#2-training-complexity)
    - [3. **Memory and Computational Requirements**:](#3-memory-and-computational-requirements)
    - [4. **Scalability**:](#4-scalability)
    - [5. **Stability of Training**:](#5-stability-of-training)
    - [6. **Use in Large-scale Models**:](#6-use-in-large-scale-models)
    - [Conclusion:](#conclusion)
  + [Backprop vs Inductive Bias vs Mixed precision training](#backprop-vs-inductive-bias-vs-mixed-precision-training)
    - [1. Backpropagation:](#1-backpropagation)
    - [2. Inductive Bias:](#2-inductive-bias)
    - [3. Mixed Precision Training:](#3-mixed-precision-training)
  + [Mixed precision vs Quantization](#mixed-precision-vs-quantization)
    - [1. Mixed Precision Training:](#1-mixed-precision-training)
    - [2. Quantization:](#2-quantization)
  + [KD Tree vs Octree](#kd-tree-vs-octree)
    - [1. KD-Tree (K-dimensional Tree):](#1-kd-tree-k-dimensional-tree)
    - [2. Octree:](#2-octree)
    - [Comparison:](#comparison)
  + [Transformer vs CNN](#transformer-vs-cnn)
    - [1. **Fundamental Concept**:](#1-fundamental-concept)
    - [2. **Primary Applications**:](#2-primary-applications)
    - [3. **Handling of Sequential Data**:](#3-handling-of-sequential-data)
    - [4. **Parameter Count & Computational Demands**:](#4-parameter-count--computational-demands)
    - [5. **Inductive Biases**:](#5-inductive-biases)
    - [6. **Adaptability**:](#6-adaptability)
    - [Conclusion:](#conclusion-1)
  + [General](#general)
  + [my interview](#my-interview)

# Overviews

## Initial Interview with a Recruiter

**What to expect:**  
This stage of our interview is an Initial Chat with one of the Talent Acquisition team. The conversation aims to gain an understanding about you and the work that you’ve been involved in up to this point, your motivation for applying, and what you are looking for in your next position. This stage will also give you an opportunity to gain a better understanding about DeepMind and Applied Engineering, and answer any questions you may have about the position.

**How to prepare:**

* Read about DeepMind’s mission and research. You can learn more about the Applied team projects on our blog.
* Reflect on your relevant skills and experience, and on what you plan to do in the future.
* It is your chance to ask any questions, so we would recommend preparing some in advance of the conversation.
* Give time, pauses for writing

### Applied DM

* What I really love about this team is that it takes research and uses it in actual applications which is parallel to my role at Amazon.
* AlphaDev uncovered a faster algorithm for sorting, which has so many real world use cases from web ranking of search items or social media posts to how data is processed on computers and phones.
* AlphaZero, which AlphaDev, is based on, which is trained with reinforcement learning and has beat the world champions on games like chess.
* Open source aspect, to help the AI community build on top of each others innovation.
* MuZero for video compression
* Flamingo: DeepMind introduced the Flamingo visual language model to automatically generate descriptions for YouTube Shorts, enhancing searchability.
  + Additionally, DeepMind’s collaborations with YouTube have improved video compression, brand safety, and automated chapter suggestions for creators.
* GNN based traffic predictions for Google Maps, that use case is very relevant for the bay area especially with everyone returning back to office.

### Background

1. Amazon:
   * Machine Learning Manager at Amazon Music where I manage a team of research engineers and scientists.
   * Our work is mostly in recommender systems and NLP and my team works on both, exploring new problem areas and then finding ways to apply it to our current products and problem space.
   * Under music, we have not only music, we have podcast, and we have collaborations with Prime Video, Amazon.com retail space, Audible, as well as Alexa.
   * So we have a lot of cross-collaboration with other research teams, product managers, project managers to
   * My responsibilities include, mentoring my reports and making sure they are enjoying and growing in their career,
   * finding new avenues of research we can pursue, I really enjoy staying current in the field, I have about 5 publications in NLP
   * Some of the work we’re looking to do is how to add guardrails around these models that we develop, cant allow hallucination to happen for our customers
2. NuAIg:
   * Leading a team in NLP with a focus on healthcare.
3. Oracle:
   * NLP as well as general ML in making the cloud storage space more robust

### Questions

* A bit more about the role, is this on the applied side or the research side
* I am so excited about this opportunity, do you have any recommendations or tips that could help me through the process if I were to move through.
* I am enamoured by the research coming out of DeepMind, I follow research coming out of Meta, OpenAI, Anthropic, recommender space with Pinterest, and nothing is parallel to what DM has produced.
* I also really appreciate their mission with making ethical advances in AI and acting as responsible pioneers in the field.
* Interview process: I’m so excited about this role

## Coding Interview

**What to expect:**  
One 45-minute coding interview conducted via Google Meet, giving you an opportunity to screen share. These will involve writing some code in your preferred language and working through a few questions and a specific problem with the end goal to come to a solution.

**How to prepare:**

* Familiarize yourself with the Sandbox environment before the interview: [CoderPad Sandbox](https://coderpad.io/sandbox).
* If you haven’t done an interactive coding exercise before, practice with a friend, or do one online, e.g. with pramp or codewars.

## Machine Learning Design Interview

**What to expect:**  
One 60-minute technical exercise will be conducted via Google Hangouts to assess your Machine Learning knowledge.

**How to prepare:**

* Be prepared to explain your past work succinctly and with an emphasis on the various options available to you at key junctures and why you made particular decisions.
* Think about where you see machine learning being most useful in real-world applications.

## System Design Interview

**What to expect:**  
One 60-minute technical interview with one of our senior engineers. This will also be conducted via Google Hangouts.

**How to prepare:**

* Familiarize yourself with tools and frameworks for large scale machine learning such as Jax, Memcached, and others mentioned.

**Tips and Expectations:**

1. The system design interview will require that you take an abstract question in a formerly unseen problem and present a high level framework to solve the presented problem.
2. Identify the major components of an overall system design and deep dive in two of them.

## Technical Management Interviews

**What to expect:**  
Three (3x) 60-minute interviews with Applied Team Leads & Managers.

**How to prepare:**

* Be prepared to discuss anything on your resume to showcase your technical depth.
* Ponder what daily life at DeepMind is probably like and what challenges you might face.

## People & Culture Interview

**What to expect:**  
30-minute non-technical interview with a People & Culture Partner.

**How to prepare:**

* DeepMind is committed to solving intelligence to advance science and benefit humanity. During the People & Culture interview, be prepared to discuss your working style, career aspirations, and other important factors when it comes to what is important to you in a job and a company.
* Familiarize yourself with DeepMind’s mission and research before this interview.

### Question answers:

**Stage 1: What’s the difference between dependence and correlation?**

* Answer:
* Dependence refers to any statistical relationship between two variables, regardless of its nature or strength. This means one variable can be predicted to some extent from the other.
* Correlation, on the other hand, specifically measures the linear relationship between two variables. A correlation of 0 does not necessarily imply independence, as there could be a non-linear relationship between the variables.

**Stage 1: What is a conjugate prior?**

* Answer:
* A conjugate prior is a concept in Bayesian statistics. When the prior distribution and the likelihood function are from the same family of distributions, the resulting posterior distribution will also belong to that same family. Using conjugate priors can simplify the computation of the posterior distribution.

**Stage 1: The Bayes theorem**

* Answer:
* Bayes’ theorem relates the conditional and marginal probabilities of two random events. It is formally expressed as:
  \(P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}\)
  Where:
* |  |  |
  | --- | --- |
  | $$ P(A | B) $$ is the posterior probability. |
* |  |  |
  | --- | --- |
  | $$ P(B | A) $$ is the likelihood. |
* \(P(A)\) is the prior probability.
* \(P(B)\) is the marginal likelihood or evidence.

**Stage 1: Describe the Newton algorithm**
1 Answer:
The Newton-Raphson algorithm, often simply called the Newton algorithm, is an iterative method used to find successively better approximations to the roots (or zeros) of a real-valued function. Given an initial guess \(x\_0\) for a root, the algorithm updates the guess using:
\(x\_{n+1} = x\_n - \frac{f(x\_n)}{f'(x\_n)}\)
Where \(f'\) is the derivative of \(f\).

**Stage 1: Central Limit Theorem**

* Answer:
* The Central Limit Theorem (CLT) states that, for a sufficiently large sample size, the distribution of the sample mean of a random variable will approach a normal distribution, regardless of the original distribution of the variable. This foundational theorem provides the basis for many statistical methods and tests.

**Stage 1: What are autoencoders**

* Answer:
* Autoencoders are a type of neural network used for unsupervised learning tasks, primarily data compression and noise reduction.
* An autoencoder consists of two main parts: an encoder, which compresses the input data, and a decoder, which reconstructs the original data from the compressed form. The aim is to minimize the difference (loss) between the original data and the reconstructed data.

**Stage 1: An example of an RL algorithm**
1 Answer:
An example of a Reinforcement Learning (RL) algorithm is Q-learning. It is an off-policy algorithm that learns the value of an action in a given state, aiming to find the best action to take under a particular circumstance.

**Stage 1: What is Turing Machine**
1 Answer:
A Turing Machine is a hypothetical computational device, introduced by Alan Turing in 1936, which provides a mathematical description of computation. It consists of an infinite tape, a tape head that moves left or right, and a set of rules that dictate how it reads and writes data. It is considered foundational in the theory of computation and is used to determine if a problem is computable.

**Stage 2: Write a code calculating a pi number using RNG**
1 Answer:
Using Monte Carlo method:

```
import random

def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()  # Uniformly sampled from [0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

print(estimate_pi(1000000))
```

**Stage 2: Subjects covered on the programming interview questions**

* Answer:
* The subjects covered during programming interviews can vary widely depending on the company and role, but commonly include data structures (e.g., arrays, linked lists, trees, graphs), algorithms (e.g., sorting, searching), system design, object-oriented design, databases, and sometimes domain-specific questions like machine learning algorithms or web technologies.

**Stage 3: The interviewer asked me if I had ideological objections to work in Google - clearly, not; if I believed the AGI would ever be achieved and if it’s dangerous to humans**

## machine operation information

1. **Temperature**: In ML, temperature could metaphorically represent the training conditions of a machine learning model. It refers to factors like the learning rate or the pace at which the model adapts to the data. Setting the right “temperature” is crucial to prevent the model from overfitting (getting too hot) or underfitting (too cold) the data.
2. **Machine Model**: This refers to the specific type of machine learning model being used, such as a neural network, decision tree, or support vector machine. The choice of the machine model significantly impacts the model’s performance and suitability for a particular task.
3. **Read and Write**: In ML, “read” typically means the process of ingesting and preprocessing data for training, while “write” relates to saving and persisting trained models for later use or deployment. Proper data reading and writing procedures are essential for efficient ML workflows.
4. **Load**: In ML, “load” can represent the computational workload or resource demand of training a machine learning model. Training complex models or processing large datasets can be computationally intensive and may require sufficient computational resources like GPUs or cloud computing.
5. **Other Signals**: ML models often depend on various input features or signals, and these features may come from a wide range of sources. These “other signals” could represent any additional data points or features used in the ML model, which could include text, images, sensor data, or any other relevant information.
6. **Functional Analysis**:
   * Functional analysis is a branch of mathematics and a subfield of linear algebra that deals with vector spaces of functions. It focuses on studying and understanding spaces of functions and operators defined on these spaces.
   * In machine learning and data analysis, functional analysis can be relevant when dealing with function spaces or when considering how different functions interact with data.
7. **Reinforcement Learning**:
   * Reinforcement learning (RL) is a type of machine learning paradigm where an agent learns to make decisions by interacting with an environment. The agent takes actions to maximize a cumulative reward signal.
   * It is commonly used in scenarios where an agent needs to learn a sequence of actions to achieve a goal, such as game playing, robotics, autonomous driving, and recommendation systems.
8. **Deep Learning**:
   * Deep learning is a subfield of machine learning that focuses on neural networks with multiple layers, known as deep neural networks. These networks are capable of learning complex patterns from data.
   * Deep learning has been particularly successful in tasks like image and speech recognition, natural language processing, and reinforcement learning due to its ability to automatically discover hierarchical features from raw data.
9. **Three-Dimensional Search for Nearest Neighbors (NN)**:
   * In this context, “nearest neighbors” refers to finding data points that are closest to a given query point in a three-dimensional space.
   * Three-dimensional search problems commonly arise in various fields, including computer graphics, computer vision, and geographic information systems (GIS).
   * The goal is to efficiently locate and retrieve data points that are geometrically close to the query point.
10. **Use of K-Means to Find the Nearest Cluster**:
    * K-means is a clustering algorithm used to partition data points into clusters based on their similarity.
    * In the context of a three-dimensional search, one approach is to use K-means to group data points into clusters.
    * When a query is made, the first step is to identify the nearest cluster to the query point using K-means. This narrows down the search space.
11. **Using Sorted Distance to Find the Top K in That Cluster**:
    * Once the nearest cluster is identified, the next step is to determine the closest data points within that cluster to the query point.
    * Sorted distance refers to arranging data points in the cluster based on their distance from the query point in ascending order.
    * By sorting the distances, it becomes straightforward to select the top K data points that are closest to the query point within the cluster.
12. **Considering Clustering (K-Means) or Building an Index (kNN, KD-Tree, LSH) for NN**:
    * When solving nearest neighbor search problems, there are various techniques available, including clustering and indexing.
    * Clustering, as mentioned earlier, involves grouping similar data points into clusters.
    * Indexing methods like k-nearest neighbors (kNN), KD-trees, and Locality-Sensitive Hashing (LSH) offer alternative approaches to efficiently retrieve nearest neighbors based on predefined data structures and distance metrics.
13. **Exploring Additional Aspects or Techniques Related to NN**:
    * Beyond clustering and indexing, there are other aspects to consider when working with nearest neighbor search:
    * Choice of distance metric: Different distance metrics (e.g., Euclidean, Manhattan, cosine similarity) may be suitable for different applications.
    * Scalability: For large datasets, scalability and optimization become crucial to ensure efficient search.
    * Approximate nearest neighbor search: In some cases, it may be acceptable to find an approximate nearest neighbor to speed up the search process while sacrificing a small degree of accuracy.

## Bayes

Bayes’ theorem is a fundamental concept in probability theory and statistics, often used to solve problems related to conditional probability. It’s frequently applied in scenarios where you have incomplete information and want to update your beliefs or probabilities based on new evidence. One common application is in “balls in urns” problems, where you have an urn with colored balls and you want to calculate probabilities related to drawing certain balls under specific conditions. Here are a few examples of Bayes’ theorem applied to such problems:

**Example 1 - A Two-Urn Problem:**

* You have two urns, Urn A and Urn B. Urn A contains 3 red balls and 2 green balls, while Urn B contains 2 red balls and 4 green balls. You randomly choose one urn (both urns have equal chances of being chosen) and then draw a red ball.
* What is the probability that you chose Urn A?

**Solution:**

* Let:
* A: The event that you chose Urn A.
* B: The event that you chose Urn B.
* R: The event that you drew a red ball.
* |  |  |
  | --- | --- |
  | We want to find P(A | R), the probability that you chose Urn A given that you drew a red ball. |

Using Bayes’ theorem:
\(P(A | R) = \frac{P(A) \cdot P(R | A)}{P(A) \cdot P(R | A) + P(B) \cdot P(R | B)}\)

* P(A) = Probability of choosing Urn A = 1/2 (since both urns are equally likely to be chosen).
* |  |  |
  | --- | --- |
  | P(R | A) = Probability of drawing a red ball from Urn A = 3/5 (since Urn A has 3 red balls out of 5 total). |
* P(B) = Probability of choosing Urn B = 1/2.
* |  |  |
  | --- | --- |
  | P(R | B) = Probability of drawing a red ball from Urn B = 2/6 (since Urn B has 2 red balls out of 6 total). |
* |  |  |
  | --- | --- |
  | Now, plug these values into the formula to calculate P(A | R). |

**Example 2 - A Deck of Cards:**

* You have a deck of 52 playing cards. The deck contains 4 aces (hearts, diamonds, clubs, spades) and 48 non-aces. You draw a card at random and it’s an ace.
* What is the probability that the card you drew is a heart?

**Solution:**
Let:

* A: The event that the drawn card is an ace.
* H: The event that the drawn card is a heart.
* |  |  |
  | --- | --- |
  | We want to find P(H | A), the probability that the drawn card is a heart given that it’s an ace. |
* Using Bayes’ theorem:
  \(P(H | A) = \frac{P(H) \cdot P(A | H)}{P(H) \cdot P(A | H) + P(\neg H) \cdot P(A | \neg H)}\)
* P(H) = Probability of drawing a heart = 13/52 (since there are 13 hearts out of 52 cards).
* |  |  |
  | --- | --- |
  | P(A | H) = Probability of drawing an ace given that it’s a heart = 1/13 (since there’s one ace of hearts out of 13 hearts). |
* P(\neg H) = Probability of drawing a non-heart = 39/52 (since there are 39 non-hearts out of 52 cards).
* |  |  |
  | --- | --- |
  | P(A | \neg H) = Probability of drawing an ace given that it’s not a heart = 3/39 (since there are 3 non-heart aces out of 39 non-hearts). |

|  |  |
| --- | --- |
| Now, plug these values into the formula to calculate P(H | A). |

## L2 vs L1

Certainly, I can provide a more detailed mathematical intuition for why L1 regularization tends to produce sparse feature vectors compared to L2 regularization. Let’s explore this in terms of how gradients affect the weights in L1 regularization:

In machine learning, regularization is a technique used to prevent overfitting and control the complexity of a model. L1 and L2 regularization are two common methods, and they differ in how they penalize large weight values.

**L2 Regularization (Ridge Regression):**

In L2 regularization, the regularization term added to the loss function is proportional to the square of the weights:

Regularized Loss (L2): L(w) = Loss(w) + λ \* Σ(w\_i^2)

Where:

* Loss(w) is the original loss function.
* λ (lambda) is the regularization strength.

The gradient of this regularization term with respect to the weights w is:

∇(L2) = 2λ \* w

Now, consider what happens when we update the weights during training. The gradient term (2λ \* w) is directly proportional to the current weight values w. As a result:

* Larger weights lead to larger gradients.
* Smaller weights lead to smaller gradients.

This means that in L2 regularization, all weights are pushed towards being smaller, but they are not driven to exactly zero.

**L1 Regularization (Lasso Regression):**

In contrast, L1 regularization uses the absolute values of weights in the regularization term:

|  |  |
| --- | --- |
| Regularized Loss (L1): L(w) = Loss(w) + λ \* Σ | w\_i |

The gradient of this regularization term with respect to the weights w is:

∇(L1) = λ \* sign(w)

Here, “sign(w)” is the sign function, which is equal to 1 when w is positive, -1 when w is negative, and 0 when w is zero.

Now, let’s consider the impact of this gradient on weight updates:

* When a weight w is positive, the gradient is λ.
* When a weight w is negative, the gradient is -λ.
* When a weight w is zero, the gradient is 0.

In L1 regularization, the gradient encourages weights to be exactly zero because it doesn’t just penalize large weights; it actively pushes them towards zero. This property of L1 regularization promotes sparsity in the weight vector, effectively selecting a subset of the most important features while setting others to zero.

In summary, the mathematical intuition behind L1 regularization causing sparsity lies in its gradient. L1’s gradient, which is proportional to the sign of the weights, actively encourages many weights to be exactly zero during training, resulting in a sparse feature vector.

### GNN loss function by task

Graph Neural Networks (GNNs) are neural networks designed to perform learning on graph-structured data. Several loss functions are used in GNNs, depending on the task at hand such as node classification, graph classification, and link prediction.

### 1. **Node Classification**

For node classification tasks, Cross-Entropy loss is commonly used, especially when the classes are exclusive.
\(L = -\sum\_{i=1}^{N} y\_i \log(\hat{y}\_i)\)
Where:

* \(N\) is the number of nodes.
* \(y\_i\) is the true label of node \(i\).
* \(\hat{y}\_i\) is the predicted label of node \(i\).

### 2. **Graph Classification**

For graph classification tasks, Cross-Entropy or Mean Squared Error (MSE) loss can be used, depending on whether the task is a classification or a regression task, respectively.

* **Cross-Entropy Loss**:
  \(L = -\sum\_{i=1}^{N} y\_i \log(\hat{y}\_i)\)
* **Mean Squared Error Loss**:
  \(L = \frac{1}{N} \sum\_{i=1}^{N} (y\_i - \hat{y}\_i)^2\)

### 3. **Link Prediction**

For link prediction tasks, the Binary Cross-Entropy loss is often used, as the task is usually to predict whether a link exists (1) or not (0) between two nodes.
\(L = -\frac{1}{N} \sum\_{i=1}^{N} [y\_i \log(\hat{y}\_i) + (1 - y\_i) \log(1 - \hat{y}\_i)]\)

### 4. **Graph Generation**

When generating graphs, the Negative Log Likelihood (NLL) loss is often used to maximize the likelihood of generating real graphs.

### 5. **Graph Reconstruction**

For graph reconstruction tasks, reconstruction loss such as Mean Squared Error between the adjacency matrices of the original and reconstructed graphs can be used.
\(L = \frac{1}{N^2} \sum\_{i=1}^{N} \sum\_{j=1}^{N} (A\_{ij} - \hat{A}\_{ij})^2\)
Where:

* \(A\_{ij}\) is the original adjacency matrix.
* \(\hat{A}\_{ij}\) is the reconstructed adjacency matrix.

### 6. **Regularization Loss**

Regularization terms like L1 or L2 regularization are also often added to the loss function to avoid overfitting.

* **L1 Regularization**:
  \(L\_{\text{reg}} = \lambda \sum\_{i} |w\_i|\)
* **L2 Regularization**:
  \(L\_{\text{reg}} = \lambda \sum\_{i} w\_i^2\)

### Additional Considerations

* The choice of a loss function also depends on the kind of graph involved (directed, undirected, weighted, etc.) and the specific requirements of the task.
* The above loss functions might be combined or modified based on the specific needs of the task, and some tasks might require designing a custom loss function.

## CNN Receptive Field

The receptive field of a convolutional neural network (CNN) refers to the size or region of the input space that affects a particular feature in the output. In simple terms, it’s the region in the input image that “contributed” to a feature’s computation. As you go deeper into the layers of a CNN, each neuron “sees” or “is affected by” a larger portion of the input image, i.e., it has a larger receptive field.

The size of the receptive field for each layer in a CNN depends on:

1. **Kernel Size**: The size of the filter being used. For example, a 3x3 kernel has a receptive field of 3x3.
2. **Stride**: The step size taken when moving the filter across the input. A larger stride increases the receptive field.
3. **Pooling Layers**: Pooling operations, like max pooling, can also affect the receptive field. For instance, a 2x2 max-pooling operation with stride 2 will double the receptive field’s size.

To compute the receptive field (RF) at any given layer, you can use the following formula:

\[\text{RF} = \text{RF}\_{\text{prev}} + (\text{kernel size} - 1) \times \text{dilation rate} \times \text{stride}^{\text{layer depth}}\]

Where:

* \(\text{RF}\_{\text{prev}}\) is the receptive field of the previous layer.
* \(\text{kernel size}\) is the size of the convolutional kernel/filter.
* \(\text{dilation rate}\) (also known as atrous rate) is the spacing between the kernel points, used in dilated convolutions. It’s 1 for standard convolutions.
* \(\text{stride}^{\text{layer depth}}\) accounts for the compounded effects of stride in previous layers.

### Example:

Consider a CNN with the following layers:

1. Convolutional layer with 3x3 kernel, stride of 1.
2. Convolutional layer with 3x3 kernel, stride of 1.
3. Max-pooling layer with 2x2 kernel, stride of 2.
4. Convolutional layer with 3x3 kernel, stride of 1.

To compute the receptive field at the last layer:

* After the first convolutional layer: \(\text{RF} = 3\)
* After the second convolutional layer: \(\text{RF} = 3 + (3-1) \times 1 \times 1^1 = 5\)
* After the max-pooling layer: \(\text{RF} = 5 + 2 \times 1 \times 1^2 = 7\) (pooling with 2x2 kernel increases the RF by 2 units)
* After the third convolutional layer: \(\text{RF} = 7 + (3-1) \times 1 \times 2^1 = 11\)

So, the receptive field of the last layer is 11x11.

Understanding receptive fields is important because it gives insight into the region of the input that influences a particular feature. If the receptive field is too small compared to the scale of important features in your data, your network may not be able to recognize those features effectively.

## CNN vs RNN

* Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) are specialized types of neural network architectures designed for specific tasks. When it comes to large-scale model training, there are distinct considerations for each:

### 1. **Model Architecture and Data Type**:

* **CNNs**: Best suited for grid-like data, such as images, where spatial hierarchies and local patterns (like edges, textures) matter. CNNs leverage weight sharing and spatial invariance through convolution operations, making them more parameter-efficient when handling such data.
* **RNNs**: Designed for sequential data like time series or natural language, where temporal dynamics and order of data points are important. RNNs maintain a hidden state from timestep to timestep, allowing them to “remember” previous inputs in the sequence.

### 2. **Training Complexity**:

* **CNNs**: Generally, CNNs can be trained in parallel over each position in the spatial grid (like over each pixel in an image or patch of an image), which means they can benefit significantly from parallel processing hardware such as GPUs.
* **RNNs**: Due to their sequential nature, RNNs are inherently harder to parallelize. The computation for step `t` generally depends on the result from step `t-1`, causing potential bottlenecks in training. However, certain strategies like truncated backpropagation through time can be used to make the training more efficient.

### 3. **Memory and Computational Requirements**:

* **CNNs**: The memory and computational requirements largely depend on the depth and width of the network, the size of the input, and the number of filters in each layer. Typically, deeper networks with larger filters require more memory and computation.
* **RNNs**: Memory and computation are largely influenced by sequence length. Very long sequences can make training RNNs computationally intensive and can also lead to issues like vanishing and exploding gradients. Techniques like gradient clipping and architectures like LSTM or GRU have been introduced to mitigate some of these issues.

### 4. **Scalability**:

* **CNNs**: Scalability often depends on the availability of labeled data. Transfer learning using pre-trained models is a common strategy for training large-scale CNNs, where a network trained on a large dataset (like ImageNet) is fine-tuned on a smaller, task-specific dataset.
* **RNNs**: Transfer learning is less prevalent compared to CNNs. However, RNNs, especially transformers, which can be seen as a generalization of RNNs, have shown great success in NLP by pre-training on large text corpora and then fine-tuning on task-specific datasets.

### 5. **Stability of Training**:

* **CNNs**: Training is generally stable, especially with normalization techniques like Batch Normalization.
* **RNNs**: Training can be unstable due to the aforementioned vanishing and exploding gradient problems. LSTMs and GRUs, or more recent architectures like transformers, have largely replaced vanilla RNNs because of these challenges.

### 6. **Use in Large-scale Models**:

* **CNNs**: Often used in state-of-the-art models in computer vision, including architectures like ResNet, VGG, and EfficientNet.
* **RNNs**: The transformer architecture, which utilizes self-attention mechanisms, has become the standard in many large-scale NLP models, overshadowing traditional RNNs. Examples include BERT, GPT, and T5.

### Conclusion:

When considering large-scale model training, the choice between CNN and RNN isn’t just about scale but rather the type of data and problem at hand. CNNs excel in tasks related to image processing, while RNNs (and their more modern counterparts like transformers) are dominant in processing sequences, such as text or time series data.

## Backprop vs Inductive Bias vs Mixed precision training

Certainly! Let’s explore each of these concepts in detail:

### 1. Backpropagation:

**Backpropagation** (short for “backward propagation of errors”) is a method used to calculate the gradient of the loss function concerning each weight in a neural network. It’s the cornerstone of training most deep learning models. Here’s how it works:

1. **Forward Pass**: Input is passed through the network to compute the prediction.
2. **Compute Loss**: The prediction is compared to the true labels to compute the loss.
3. **Backward Pass**: The gradient of the loss with respect to each weight is computed. This is done by applying the chain rule of calculus, working backward from the output layer to the input layer.
4. **Update Weights**: The weights of the network are then updated in the direction that decreases the loss, typically using optimization algorithms like Gradient Descent or its variants.

### 2. Inductive Bias:

**Inductive bias** refers to the set of assumptions that a learner (an algorithm or model) uses to predict outputs given inputs it has not encountered. Every machine learning algorithm has some form of inductive bias, which guides the learning process and affects its generalization to new data. Some examples:

* **Decision Trees**: The bias is that the data can be partitioned recursively based on feature values.
* **k-Nearest Neighbors**: Assumes that data points that are close in input space have similar outputs.
* **Neural Networks**: The choice of architecture itself (like the number of layers or the type of layers used) introduces bias. For example, a convolutional layer assumes that local patterns are relevant throughout the input (like in images).

Inductive bias is crucial as it enables models to generalize from limited data. However, if the bias does not align well with the true data-generating process, it can lead to poor performance.

### 3. Mixed Precision Training:

**Mixed precision training** is a technique used to speed up the training of deep neural networks. Instead of using single precision (32-bit) floating point numbers throughout the training process, mixed precision training utilizes both 16-bit (half-precision) and 32-bit (single precision) floating point numbers. Here’s why and how it’s beneficial:

* **Memory Requirements**: Half-precision floating point numbers require half the memory, allowing for larger batch sizes or models.
* **Computational Speed**: Modern GPUs are optimized to perform operations faster with 16-bit compared to 32-bit numbers.
* **Regularization Effect**: The noise introduced by the reduced precision can have a slight regularizing effect, potentially improving generalization in some cases.

However, naively switching all operations to half precision can lead to issues like underflow (values too small) or overflow (values too large). Therefore, in mixed precision training:

1. The model maintains a copy of weights in 32-bit for accumulating gradients.
2. Computations, especially forward and backward passes, use 16-bit precision.
3. Weight updates can be performed in 32-bit precision.

Libraries like NVIDIA’s Apex and native support in deep learning frameworks like TensorFlow and PyTorch make mixed precision training relatively straightforward.

In summary, backpropagation is the backbone of training deep networks, inductive bias provides them with the ability to generalize, and mixed precision training offers a method to train faster and sometimes more efficiently.

## Mixed precision vs Quantization

* Both mixed precision training and quantization deal with the precision of numbers in neural networks. However, their purposes, implementations, and the stages at which they are applied can be quite different. Here’s a breakdown:

### 1. Mixed Precision Training:

* **Purpose**: To speed up training without significantly impacting the accuracy of the model.
* **Implementation**: Involves using both 16-bit (half-precision) and 32-bit (single precision) floating point numbers during the training process.
  + Computations, especially the forward and backward passes, are done using 16-bit precision.
  + A master copy of weights is maintained in 32-bit for accumulating gradients and updates.
* **Stage of Application**: Applied during the training phase.
* **Benefits**:
  + Faster training due to reduced precision computations.
  + Decreased memory usage, allowing for larger batch sizes or models.
  + Potential regularization effect due to the reduced precision.
* **Challenges**: Risk of numerical instability, like underflow and overflow. Proper scaling and management are needed to handle these issues.

### 2. Quantization:

* **Purpose**: To reduce the memory footprint and computational demands of a model during inference (deployment). This is especially important for edge devices with limited computational resources.
* **Implementation**: Involves reducing the precision of the model’s weights (and sometimes activations) from floating-point numbers (like 32-bit) to lower bit-widths, which could be fixed-point representations like 8-bit integers or even lower.
* **Types**:
  + **Weight Quantization**: Only the weights are quantized.
  + **Activation Quantization**: Both weights and activations are quantized.
  + **Dynamic Quantization**: Weights are quantized ahead of time, but activations are quantized on-the-fly during inference.
  + **Quantization Aware Training (QAT)**: The model is trained with the knowledge that it will be quantized later. This typically leads to better performance post-quantization compared to quantizing a pre-trained model.
* **Stage of Application**: Applied post-training for quantization or during training for QAT.
* **Benefits**:
  + Significantly reduced model size.
  + Faster inference, especially on hardware that supports low-precision computations.
* **Challenges**: Loss of accuracy due to the reduction in precision. The goal is to minimize this loss while gaining the benefits of reduced size and increased speed.

In summary:

* **Mixed Precision Training** is about speeding up the training process while maintaining accuracy.
* **Quantization** is primarily about compressing a trained model for faster and more efficient inference, especially on resource-constrained devices.
* Both techniques reflect the broader trend in deep learning towards making models more efficient without compromising too much on performance.

## KD Tree vs Octree

Both KD-trees and Octrees are data structures that help organize spatial data for faster querying. While they serve similar goals, their structures, applications, and use-cases can differ.

### 1. KD-Tree (K-dimensional Tree):

* **Structure**: A KD-tree is a binary tree in which every node is a k-dimensional point. Each non-leaf node generates a splitting hyperplane that divides the space into two half-spaces. Points to the left of this hyperplane are represented by the left subtree of that node, and points to the right are represented by the right subtree.
* **Construction**: Typically, the axis for splitting is chosen in a round-robin fashion between the dimensions or based on the variance in the data.
* **Applications**:
  + Nearest neighbor search in k-dimensional space.
  + Range queries: Finding all points that lie within a given range.
* **Advantages**:
  + Efficient for lower-dimensional data.
* **Disadvantages**:
  + The efficiency decreases for high-dimensional data due to the curse of dimensionality. For very high dimensions, structures like Ball Trees or hashing techniques might be more effective.

### 2. Octree:

* **Structure**: An Octree is a tree data structure where each internal node has exactly eight children. It is commonly used to partition a three-dimensional space by recursively subdividing it into eight octants.
* **Construction**: The space is recursively divided into eight octants until a certain condition is met (e.g., the number of points in the octant is below a threshold, or the tree reaches a certain depth).
* **Applications**:
  + Spatial indexing and fast geometric searches in 3D applications, including computer graphics and 3D computer games.
  + Collision detection in 3D environments.
  + Representing sparse 3D data, such as in volumetric graphics.
* **Advantages**:
  + Efficient for spatial partitioning in 3D space.
  + Can handle unevenly distributed data well.
* **Disadvantages**:
  + Can become memory-intensive if not managed properly, especially if the depth of the tree is large.
  + Specific to 3D space, whereas KD-trees are more general for k-dimensional spaces.

### Comparison:

1. **Dimensionality**:
   * KD-Tree can be used in any k-dimensional space.
   * Octree is specific to 3D space.
2. **Structure**:
   * KD-Tree is a binary tree, where each split divides space into two parts based on a chosen dimension.
   * Octree always divides space into eight octants.
3. **Applications**:
   * KD-Tree is versatile and can be applied across various domains requiring k-dimensional searches.
   * Octree is specifically tailored for 3D applications, especially in computer graphics.
4. **Performance**:
   * KD-Trees work well for low-dimensional data but can become less effective as dimensionality increases.
   * Octrees maintain consistent performance characteristics in 3D applications but can be memory-intensive.

Both structures aim to optimize spatial queries by organizing data in a hierarchical manner. The choice between them depends on the specific problem, dimensionality, and data distribution.

## Transformer vs CNN

* Transformers and Convolutional Neural Networks (CNNs) are both powerful neural architectures, but they are designed with different principles and for different types of data and tasks. Here’s a comparison between the two:

### 1. **Fundamental Concept**:

* **Transformers**: They are based on self-attention mechanisms, where the importance of different parts of the input is weighed depending on the context. In essence, transformers allow each element in the input to attend to every other element, capturing long-range dependencies.
* **CNNs**: These are designed to process grid-like data structures such as images. They utilize convolutional layers to scan local regions of the input in a sliding window fashion, making them particularly adept at detecting local patterns and hierarchies of features.

### 2. **Primary Applications**:

* **Transformers**: Initially introduced for Natural Language Processing (NLP) tasks, transformers have become the state-of-the-art architecture for a wide range of NLP problems, from translation to text generation. They are also being increasingly used in computer vision and other domains due to their flexibility.
* **CNNs**: Primarily used for image-related tasks, such as image classification, object detection, and image generation. They have been a cornerstone of deep learning advances in computer vision.

### 3. **Handling of Sequential Data**:

* **Transformers**: Transformers handle sequences very well, with each element in a sequence capable of attending to all other elements, regardless of distance. This global context gives transformers an edge in tasks like NLP where long-range dependencies can be crucial.
* **CNNs**: While they can be applied to sequences (e.g., 1D convolutions for time series or text), CNNs are inherently local due to their convolutional nature. They might require deeper architectures or recurrent connections to handle long-range dependencies.

### 4. **Parameter Count & Computational Demands**:

* **Transformers**: Generally, they tend to have a large number of parameters, especially in models like BERT, GPT, etc. The self-attention mechanism has a quadratic computational complexity concerning sequence length, making it computationally intensive for long sequences.
* **CNNs**: The parameter count can be controlled based on the number and size of filters, layers, and other architectural decisions. CNNs can be computationally more efficient than transformers for certain tasks, especially with the help of techniques like pooling and skip connections.

### 5. **Inductive Biases**:

* **Transformers**: They possess fewer inductive biases. The architecture doesn’t assume any inherent structure in the data, making it more data-driven and adaptable but sometimes requiring more data to train effectively.
* **CNNs**: They carry a strong inductive bias, assuming that local patterns are important and that features are hierarchically structured in the data (especially images). This bias can make CNNs more sample-efficient for certain tasks.

### 6. **Adaptability**:

* **Transformers**: Due to their lack of strong inductive biases, transformers have shown versatility across different domains, from NLP to computer vision, to protein folding, and more.
* **CNNs**: While adaptable across a range of tasks within computer vision, CNNs are tailored more specifically for grid-like data and may not generalize as broadly as transformers without modifications.

### Conclusion:

While both transformers and CNNs have their strengths and weaknesses, the choice between them depends on the specific task, available data, and computational resources. CNNs continue to dominate many computer vision tasks due to their efficiency and strong performance, while transformers are reshaping the landscape of NLP and are being explored in various other domains.

## General

* Coding Screens:
* Two rounds, Google style questions which I’m pretty sure were picked from Google’s internal question bank.
* First round: LC medium. Follow up was a LC medium/hard which I was not asked to code once I explained the solution. Then was asked to code a LC easy. Follow up was a LC easy/medium which I was again asked not to code once I explained the solution
* Second round: LC Hard and the question is not on LC. I gave a factorial solution, improved it to an exponential solution with memoization. Later found that there is a polynomial solution, apparent to those who have a strong competitive programming experience. I don’t think they expect the polynomial solution though.
* Different from google as you have to run the code and it’s expected that by the end you have a solution which runs in CoderPad.

ML screens:

* If one clears the coding rounds, they move forward to ML rounds
* 2 ML design style rounds
* First round probed the depth of ML knowledge. Started with questions around probability. Was asked a number of balls style question on bayes theorem. Proceeded to the design question. It’s not enough to know things, you should know the mathematical intuition as well. E.g. it’s not enough to say that you prefer L1 regularization over L2 since L1 results in sparse features, you need to give the mathematical intuition in terms of how gradients affect the weights in L1 to cause sparsity.
* Second probed width of ML knowledge. Hardest ML round I ever gave. Another design style question, but they kept adding constraints once I gave a solution. In total, we discussed like 7-8 different techniques across the board. Over the course of the interview at least 7-8 constraints were added over every solution I gave.

Virtual Onsite:

* If you clear the ML rounds, they move forward to virtual onsite.
* Two non technical interviews with TLs where they asked about my background and my experience with ML experimentation. I have some experience from Amazon in ML experimentation, so I told them whatever experience I had. Got the feeling during the interview they want someone with more modeling experience than mine.
* One behavioral with their people & culture partner (fancier term for HRBP). Standard questions like why do you wanna join DeepMind.

In total the process took about 6-7 weeks. I was able to expedite a little by telling them I have deadlines due to google and salesforce.

Edit: Removed an earlier section ranting about the process. I thought that since I was forwarded to the onsite, my ML screen performance was strong. But based on some of the comments here, it doesn’t look like that’s the case.

TC: 195K (L5)
YOE: 4 + MS (2 YOE in US)
Background: My experience at Amazon was in the intersection of ML and engineering with more bias towards engineering

## my interview

* Coding Leet code grids
* System design: search text and retrieve image
* ML System design: design a dubbing system for international videos to dub to any language and its cartoons
* TLM: how do you manage a team
