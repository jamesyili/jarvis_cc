# Primers • Clustering

**Source:** https://aman.ai/primers/ai/clustering/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview of Clustering](#overview-of-clustering)
* [Types of Clustering](#types-of-clustering)
  + [Partitioning Clustering](#partitioning-clustering)
    - [Overview](#overview)
    - [K-Means Clustering](#k-means-clustering)
      * [Algorithm](#algorithm)
      * [Advantages](#advantages)
      * [Disadvantages](#disadvantages)
    - [K-Medoids Clustering (PAM)](#k-medoids-clustering-pam)
      * [Algorithm](#algorithm-1)
      * [Advantages](#advantages-1)
      * [Disadvantages](#disadvantages-1)
    - [Fuzzy C-Means Clustering](#fuzzy-c-means-clustering)
      * [Algorithm](#algorithm-2)
      * [Advantages](#advantages-2)
      * [Disadvantages](#disadvantages-2)
    - [Comparison of Partitioning Methods](#comparison-of-partitioning-methods)
    - [Applications](#applications)
  + [Hierarchical Clustering](#hierarchical-clustering)
    - [Agglomerative Clustering](#agglomerative-clustering)
      * [Overview](#overview-1)
      * [Algorithm](#algorithm-3)
      * [Example](#example)
        + [Data](#data)
        + [Steps](#steps)
      * [Advantages](#advantages-3)
      * [Disadvantages](#disadvantages-3)
    - [Divisive Clustering](#divisive-clustering)
      * [Overview](#overview-2)
      * [Algorithm](#algorithm-4)
      * [Example](#example-1)
        + [Data](#data-1)
        + [Steps](#steps-1)
      * [Advantages](#advantages-4)
      * [Disadvantages](#disadvantages-4)
    - [Comparison](#comparison)
      * [Key Equations](#key-equations)
      * [Use Cases](#use-cases)
    - [Summary](#summary)
      * [Agglomerative Clustering (Bottom-Up)](#agglomerative-clustering-bottom-up)
      * [Divisive Clustering (Top-Down)](#divisive-clustering-top-down)
  + [K-Means Clustering](#k-means-clustering-1)
    - [Overview](#overview-3)
    - [Algorithm Description](#algorithm-description)
    - [Objective Function](#objective-function)
    - [Parameters](#parameters)
    - [Advantages](#advantages-5)
    - [Disadvantages](#disadvantages-5)
  + [Example: Applying K-Means Clustering](#example-applying-k-means-clustering)
    - [Dataset](#dataset)
    - [Step-by-Step Execution](#step-by-step-execution)
* [FAQ: What are some methods that do not require a predefined \(k\) value for clustering?](#faq-what-are-some-methods-that-do-not-require-a-predefined-k-value-for-clustering)
  + [Hierarchical Clustering](#hierarchical-clustering-1)
  + [DBSCAN (Density-Based Spatial Clustering of Applications with Noise)](#dbscan-density-based-spatial-clustering-of-applications-with-noise)
  + [OPTICS (Ordering Points To Identify the Clustering Structure)](#optics-ordering-points-to-identify-the-clustering-structure)
  + [Mean-Shift Clustering](#mean-shift-clustering)
  + [Affinity Propagation](#affinity-propagation)
  + [Gaussian Mixture Models (GMM) with Model Selection](#gaussian-mixture-models-gmm-with-model-selection)
  + [Self-Organizing Maps (SOMs)](#self-organizing-maps-soms)
  + [Spectral Clustering with Eigen Gap Analysis](#spectral-clustering-with-eigen-gap-analysis)
  + [Birch (Balanced Iterative Reducing and Clustering Using Hierarchies)](#birch-balanced-iterative-reducing-and-clustering-using-hierarchies)
  + [Autoencoders for Clustering](#autoencoders-for-clustering)
  + [Comparison of Approaches](#comparison-of-approaches)
* [Comparison: k-Nearest Neighbors vs. k-Means Clustering](#comparison-k-nearest-neighbors-vs-k-means-clustering)
  + [Key Takeaways](#key-takeaways)
* [Citation](#citation)

## Overview of Clustering

* Clustering is an unsupervised machine learning technique used to group data points into clusters based on their similarity or dissimilarity. It identifies patterns or structures in a dataset without predefined labels, making it particularly useful in exploratory data analysis. Applications include market segmentation, image segmentation, document categorization, anomaly detection, and more.

## Types of Clustering

* Clustering techniques vary widely, but they generally aim to reveal the underlying structure of data by grouping similar items together. Some methods focus on flat partitions, while others explore hierarchical relationships among data points.
* **Partitioning Clustering:** These methods divide data into non-overlapping subsets (clusters) such that each data point belongs to exactly one cluster. K-means and K-medoids are popular examples of this type, where the goal is to optimize an objective function like minimizing within-cluster variance.
* **Hierarchical Clustering:** This approach organizes data into a tree-like structure, where clusters are nested within larger clusters. It can be further categorized into:
  + **Agglomerative Clustering (Bottom-Up):** Starts with each data point as its own cluster and merges clusters iteratively.
  + **Divisive Clustering (Top-Down):** Starts with all data points in a single cluster and splits them recursively into smaller clusters.
* **Density-Based Clustering:** These techniques, like DBSCAN and OPTICS, group data points based on density. Clusters are formed where the data is dense, and points in low-density regions are considered noise.
* **Grid-Based Clustering:** This method divides the data space into a grid structure and forms clusters based on the density of points within the grid cells. Examples include STING and CLIQUE.
* **Model-Based Clustering:** Assumes that data is generated from a mixture of underlying probability distributions. Gaussian Mixture Models (GMMs) are a typical example, where each cluster corresponds to a Gaussian distribution.

### Partitioning Clustering

* Partitioning clustering is a popular approach in unsupervised learning used to divide a dataset into \(k\) distinct, non-overlapping clusters. Each data point is assigned to exactly one cluster, with the goal of optimizing a specific objective function, such as minimizing the sum of squared distances between data points and their respective cluster centers. This method is particularly effective when the number of clusters is known or can be reasonably estimated.
* Partitioning clustering is highly versatile, making it suitable for a wide range of datasets. Different techniques within this framework offer unique advantages. For instance, K-means is favored for its simplicity and computational efficiency, while K-medoids is more robust to outliers. Additionally, fuzzy clustering methods, such as Fuzzy C-means, are useful for capturing overlaps and handling uncertainty in cluster assignments. The choice of method depends on the characteristics of the data and the specific objectives of the clustering task.

#### Overview

* **Approach**: Flat clustering (as opposed to hierarchical methods).
* **Objective**: Assign data points to clusters to optimize a criterion, typically the within-cluster variance or dissimilarity.
* **Examples**:
  + **K-means Clustering**: Uses centroids as cluster representatives.
  + **K-medoids Clustering (PAM)**: Uses medoids (actual data points) as representatives.
  + Variants include fuzzy clustering (e.g., Fuzzy C-means) where points can belong to multiple clusters with varying degrees.

#### K-Means Clustering

##### Algorithm

1. **Initialization**:
   * Select \(k\), the number of clusters.
   * Randomly initialize \(k\) cluster centroids or choose them from the data points.
2. **Assignment Step**:
   * Assign each data point \(x\_i\) to the nearest cluster based on a distance metric (typically Euclidean distance):
     \(\text{Cluster}(x\_i) = \arg\min\_{j} \|x\_i - \mu\_j\|^2\)
     where \(\mu\_j\) is the centroid of the \(j\)-th cluster.
3. **Update Step**:
   * Recalculate the centroids of each cluster as the mean of all points assigned to the cluster:
     \(\mu\_j = \frac{1}{|C\_j|} \sum\_{x \in C\_j} x\)
4. **Repeat**:
   * Alternate between the assignment and update steps until centroids converge or a stopping criterion is met (e.g., maximum iterations or minimal change in centroids).

##### Advantages

* Simple and fast, with a time complexity of \(O(n \cdot k \cdot t)\), where \(n\) is the number of data points, \(k\) is the number of clusters, and \(t\) is the number of iterations.
* Works well for compact, spherical clusters.

##### Disadvantages

* Requires specifying \(k\) in advance.
* Sensitive to outliers and initialization.
* Assumes clusters are convex and isotropic (spherical).

#### K-Medoids Clustering (PAM)

* K-medoids, or Partitioning Around Medoids, is similar to K-means but uses actual data points (medoids) as cluster representatives, making it more robust to outliers.

##### Algorithm

1. **Initialization**:
   * Select \(k\) data points as the initial medoids.
2. **Assignment Step**:
   * Assign each data point to the cluster represented by the nearest medoid.
3. **Update Step**:
   * For each cluster, choose the data point that minimizes the sum of distances to all other points in the cluster as the new medoid.
4. **Repeat**:
   * Alternate between assignment and update steps until medoids stabilize.

##### Advantages

* More robust to outliers than K-means.
* Does not assume cluster shapes.

##### Disadvantages

* Computationally expensive for large datasets due to pairwise distance calculations.

#### Fuzzy C-Means Clustering

* Unlike K-means or K-medoids, Fuzzy C-means allows data points to belong to multiple clusters with varying degrees of membership.

##### Algorithm

1. **Initialization**:
   * Select \(k\) and initialize membership matrix \(U\), where \(U\_{ij}\) represents the membership degree of point \(x\_i\) to cluster \(j\).
2. **Membership Update**:
   * Update membership degrees based on cluster centroids and distance:
     \(U\_{ij} = \frac{1}{\sum\_{k=1}^{c} \left(\frac{\|x\_i - \mu\_j\|}{\|x\_i - \mu\_k\|}\right)^{\frac{2}{m-1}}}\)
     + where \(m > 1\) controls the fuzziness.
3. **Centroid Update**:
   * Update centroids using the weighted average:
     \(\mu\_j = \frac{\sum\_{i=1}^{n} U\_{ij}^m x\_i}{\sum\_{i=1}^{n} U\_{ij}^m}\)
4. **Repeat**:
   * Iterate until convergence.

##### Advantages

* Captures uncertainty and overlapping clusters.
* Flexible for non-spherical clusters.

##### Disadvantages

* Sensitive to initialization and requires selecting \(m\) and \(k\).
* Slower than K-means for large datasets.

#### Comparison of Partitioning Methods

| **Feature** | **K-Means** | **K-Medoids** | **Fuzzy C-Means** |
| --- | --- | --- | --- |
| Cluster Representative | Centroid (mean) | Medoid (actual point) | Weighted average |
| Robustness | Sensitive to outliers | Robust to outliers | Handles overlapping |
| Speed | Fast (\(O(nkt)\)) | Slower (\(O(k(n-k)^2)\)) | Moderate |
| Cluster Shape | Spherical | Arbitrary | Arbitrary |
| Output | Hard partitions | Hard partitions | Soft partitions |

#### Applications

* **K-Means**:
  + Image segmentation.
  + Market segmentation.
  + Document clustering.
* **K-Medoids**:
  + Gene expression analysis.
  + Anomaly detection.
* **Fuzzy C-Means**:
  + Medical imaging.
  + Weather pattern analysis.

### Hierarchical Clustering

* Hierarchical clustering, one of the key clustering techniques, can be performed in two primary ways: Agglomerative Clustering (bottom-up) and Divisive Clustering (top-down). Let’s explore both methods, their algorithms, mathematical formulations, and use cases, along with examples.

#### Agglomerative Clustering

##### Overview

* Agglomerative clustering starts with each data point as its own cluster and iteratively merges clusters until a stopping criterion is met (e.g., a desired number of clusters).
* **Approach**: Bottom-up
* **Process**:
  1. Treat each data point as a singleton cluster.
  2. Compute pairwise similarity (or dissimilarity) between clusters.
  3. Merge the two most similar clusters.
  4. Repeat until the termination condition is met.

##### Algorithm

1. **Initialization**: Start with \(n\) clusters, where \(n\) is the number of data points.
2. **Distance Matrix Computation**:
   * Compute the distance \(d(C\_i, C\_j)\) between all pairs of clusters \(C\_i\) and \(C\_j\).
   * Common metrics:
     + **Euclidean Distance**:
       \(d(x, y) = \sqrt{\sum\_{i=1}^{p} (x\_i - y\_i)^2}\)
     + **Manhattan Distance**:
       \(d(x, y) = \sum\_{i=1}^{p} |x\_i - y\_i|\)
     + **Cosine Similarity**:
       \(\text{similarity}(x, y) = \frac{x \cdot y}{\|x\| \|y\|}\)
3. **Cluster Merging**:
   * Merge the two clusters with the smallest distance/similarity.
   * Update the distance matrix to reflect the newly formed cluster.
   * Use **linkage criteria** to determine cluster distance:
     + **Single Linkage** (Minimum Distance):
       \(d(C\_i, C\_j) = \min\_{x \in C\_i, y \in C\_j} d(x, y)\)
     + **Complete Linkage** (Maximum Distance):
       \(d(C\_i, C\_j) = \max\_{x \in C\_i, y \in C\_j} d(x, y)\)
     + **Average Linkage**:
       \(d(C\_i, C\_j) = \frac{1}{|C\_i||C\_j|} \sum\_{x \in C\_i} \sum\_{y \in C\_j} d(x, y)\)
     + **Centroid Linkage**:
       \(d(C\_i, C\_j) = d(\mu(C\_i), \mu(C\_j))\)
       where \(\mu(C)\) is the centroid of cluster \(C\).
4. **Repeat**: Continue merging until the stopping criterion is satisfied.

##### Example

###### Data

* Points: \(A = (1, 1), B = (2, 2), C = (5, 5), D = (6, 6)\)

###### Steps

1. **Initial Distance Matrix** (Euclidean Distance):

|  | **A** | **B** | **C** | **D** |
| --- | --- | --- | --- | --- |
| **A** | 0 | 1.41 | 5.66 | 7.07 |
| **B** | 1.41 | 0 | 4.24 | 5.66 |
| **C** | 5.66 | 4.24 | 0 | 1.41 |
| **D** | 7.07 | 5.66 | 1.41 | 0 |

1. **Merge Closest Clusters**: \(A\) and \(B\).
2. **Update Distance Matrix**: Using single linkage, merge \(\{A, B\}\).

|  | **AB** | **C** | **D** |
| --- | --- | --- | --- |
| **AB** | 0 | 4.24 | 5.66 |
| **C** | 4.24 | 0 | 1.41 |
| **D** | 5.66 | 1.41 | 0 |

1. **Repeat Until All Clusters Merged**.

##### Advantages

* Does not require the number of clusters beforehand.
* Suitable for hierarchical relationships.

##### Disadvantages

* Computationally expensive (\(O(n^3)\)).
* Sensitive to noisy data and outliers.

#### Divisive Clustering

##### Overview

Divisive clustering starts with all data points in a single cluster and recursively splits clusters until a stopping criterion is met.

* **Approach**: Top-down
* **Process**:
  1. Treat all data points as one cluster.
  2. Split the cluster into two sub-clusters using a splitting criterion.
  3. Repeat recursively for each sub-cluster.

##### Algorithm

1. **Initialization**: Start with a single cluster containing all data points.
2. **Splitting**:
   * Choose the cluster to split.
   * Divide into two clusters based on a measure like:
     + **K-means clustering**.
     + **Principal Component Analysis (PCA)** to project and split.
3. **Repeat**: Continue splitting until a termination condition is met:
   * A fixed number of clusters.
   * Minimum intra-cluster variance.

##### Example

###### Data

* Points: \(A = (1, 1), B = (2, 2), C = (5, 5), D = (6, 6)\)

###### Steps

1. Start with \(\{A, B, C, D\}\).
2. Split using k-means:
   * Cluster 1: \(\{A, B\}\)
   * Cluster 2: \(\{C, D\}\).
3. Recurse:
   * \(\{A, B\}\) splits into \(A\) and \(B\).
   * \(\{C, D\}\) splits into \(C\) and \(D\).

##### Advantages

* Can be more efficient than agglomerative for large datasets.
* Handles global structure better.

##### Disadvantages

* Computationally expensive (\(O(2^n)\) in the worst case).
* Requires splitting criteria, which may not always be straightforward.

#### Comparison

| **Feature** | **Agglomerative Clustering** | **Divisive Clustering** |
| --- | --- | --- |
| **Approach** | Bottom-up | Top-down |
| **Initialization** | Start with \(n\) clusters | Start with 1 cluster |
| **Merging/Splitting** | Merge closest clusters | Split clusters recursively |
| **Computational Cost** | Higher for large datasets | More scalable for large datasets |
| **Cluster Formation** | Fine-grained at start | Coarse-grained at start |
| **Algorithmic Flexibility** | Easier to implement, multiple linkage criteria | Requires effective splitting strategy |

##### Key Equations

1. **Distance Calculation**:
   * \(d(x, y) = \sqrt{\sum (x\_i - y\_i)^2}\) (Euclidean Distance).
2. **Linkage Criteria**:
   * Single Linkage: \(d\_{\text{min}} = \min\_{i,j} d(x\_i, y\_j)\).
   * Complete Linkage: \(d\_{\text{max}} = \max\_{i,j} d(x\_i, y\_j)\).
3. **Cluster Variance (for Divisive)**:
   * \(\text{Intra-cluster variance} = \sum\_{i=1}^k \sum\_{x \in C\_i} \|x - \mu(C\_i)\|^2\).

##### Use Cases

1. **Agglomerative Clustering**:
   * Social network analysis.
   * Gene expression analysis.
   * Customer segmentation.
2. **Divisive Clustering**:
   * Document classification.
   * Large-scale hierarchical data organization.

#### Summary

##### Agglomerative Clustering (Bottom-Up)

* Starts with each data point as its own cluster.
* Iteratively merges the closest pairs of clusters until a single cluster (or a predefined number of clusters) remains.
* Common linkage criteria:
  + **Single Linkage:** Minimum distance between points in two clusters.
  + **Complete Linkage:** Maximum distance between points in two clusters.
  + **Average Linkage:** Average distance between points in two clusters.

##### Divisive Clustering (Top-Down)

* Begins with all data points in one cluster.
* Recursively splits clusters into smaller groups based on dissimilarity.
* Less common than agglomerative clustering due to its computational complexity.

### K-Means Clustering

#### Overview

* Clustering is a versatile tool in data analysis, used to group data points into meaningful subsets based on their characteristics. Among the various clustering methods, K-means is a widely used partitioning-based approach. It divides \(n\) data points into \(k\) clusters, assigning each point to the cluster with the nearest mean. This method aims to minimize intra-cluster variance, resulting in compact and well-separated clusters.
* Despite its simplicity and efficiency, K-means is often best complemented by other techniques to accommodate the diverse characteristics and complexities of different datasets.

#### Algorithm Description

* The K-means algorithm consists of the following steps:

1. **Initialization:** Randomly initialize \(k\) centroids (cluster centers) or select \(k\) random points from the dataset.
2. **Assignment:** Assign each data point to the nearest centroid based on the Euclidean distance:
   \(d(x, c) = \sqrt{\sum\_{i=1}^{n} (x\_i - c\_i)^2}\)
   where \(x\) is the data point, \(c\) is the centroid, and \(n\) is the number of features.
3. **Update:** Recompute the centroids of the clusters as the mean of all points assigned to each cluster:
   \(c\_j = \frac{1}{|C\_j|} \sum\_{x \in C\_j} x\)
   where \(C\_j\) is the set of points in cluster \(j\), and \(|C\_j|\) is the number of points in \(C\_j\).
4. **Repeat:** Iterate steps 2 and 3 until the centroids stabilize (i.e., no significant change in their positions) or a maximum number of iterations is reached.

#### Objective Function

* The goal of K-means is to minimize the within-cluster sum of squares (WCSS):
  \(J = \sum\_{j=1}^{k} \sum\_{x \in C\_j} \|x - c\_j\|^2\)
  + where, \(J\) represents the total variance within clusters.

#### Parameters

* \(k\): Number of clusters.
* Initialization method for centroids.
* Distance metric (Euclidean distance is standard but other metrics like Manhattan distance can be used).
* Maximum number of iterations.

#### Advantages

* Simple to implement and computationally efficient.
* Works well with compact, spherical clusters.
* Scales to large datasets.

#### Disadvantages

* Sensitive to the initial placement of centroids; poor initialization can lead to suboptimal solutions.
* Assumes clusters are spherical and equally sized.
* Struggles with non-linear separability and varying cluster densities.
* Requires specifying \(k\), which may not be known in advance.

### Example: Applying K-Means Clustering

#### Dataset

* Consider a 2D dataset with the following points:

\[(1, 1), (1.5, 2), (3, 4), (5, 7), (3.5, 5), (4.5, 5), (3.5, 4.5)\]

#### Step-by-Step Execution

1. **Initialization:** Let \(k = 2\). Randomly initialize centroids at \(c\_1 = (1, 1)\) and \(c\_2 = (5, 7)\).

   * Initial centroids:
     \(c\_1 = (1, 1), \ c\_2 = (5, 7)\)
2. **Assignment:** Compute the Euclidean distance of each point to the centroids and assign points to the nearest centroid. The Euclidean distance for each point to both centroids is calculated as follows:

   * For point \((1, 1)\):
     \(d((1, 1), c\_1) = \sqrt{(1-1)^2 + (1-1)^2} = 0\)
     \(d((1, 1), c\_2) = \sqrt{(1-5)^2 + (1-7)^2} = \sqrt{16 + 36} = \sqrt{52}\)
   * Repeat the above for all points in the dataset:

     + Point \((1.5, 2)\): Closest to \(c\_1\)
     + Point \((3, 4)\): Closest to \(c\_1\)
     + Point \((5, 7)\): Closest to \(c\_2\)
     + Point \((3.5, 5)\): Closest to \(c\_2\)
     + Point \((4.5, 5)\): Closest to \(c\_2\)
     + Point \((3.5, 4.5)\): Closest to \(c\_2\)
3. **Update:** Recalculate the centroids as the mean of the points assigned to each cluster:

   * For \(c\_1\):
     \(c\_1 = \text{mean of points assigned to } c\_1 = \frac{(1, 1) + (1.5, 2) + (3, 4)}{3} = (1.833, 2.333)\)
   * For \(c\_2\):
     \(c\_2 = \text{mean of points assigned to } c\_2 = \frac{(5, 7) + (3.5, 5) + (4.5, 5) + (3.5, 4.5)}{4} = (4.125, 5.375)\)
4. **Repeat:** Reassign points to the nearest updated centroids and recalculate the centroids again. Continue until centroids converge or maximum iterations are reached.

## FAQ: What are some methods that do not require a predefined \(k\) value for clustering?

* In clustering, most algorithms require the user to specify the number of clusters (\(k\)), but there are several methods that do not rely on a predefined \(k\). These methods determine the number of clusters dynamically or use a different approach. Below are some clustering techniques that do not require a predefined \(k\):

#### Hierarchical Clustering

* **Description**: Hierarchical clustering constructs a hierarchy of clusters in a recursive manner. It begins by treating each data point as an individual cluster (agglomerative) or starts with all data points in a single cluster and progressively splits them (divisive). The resulting hierarchy is visualized in a dendrogram.
* **No Need for \(k\)**: Instead of needing \(k\) upfront, the dendrogram allows users to determine the appropriate number of clusters post hoc by setting a threshold on the linkage distance.
* **Examples**:
  + Agglomerative clustering (merging clusters bottom-up).
  + Divisive clustering (splitting clusters top-down).

#### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

* **Description**: DBSCAN groups points that are closely packed together based on a specified density threshold and marks points in sparse regions as noise. It is especially effective for identifying clusters of arbitrary shapes.
* **Parameters**: Requires two key inputs:
  + \(\epsilon\): Maximum radius for a neighborhood.
  + \(minPts\): Minimum number of points required to form a dense cluster.
* **No Need for \(k\)**: Clusters are formed dynamically based on density conditions without requiring the number of clusters to be predefined.

#### OPTICS (Ordering Points To Identify the Clustering Structure)

* **Description**: OPTICS builds upon DBSCAN to address its sensitivity to the \(\epsilon\) parameter. It orders data points in a way that captures cluster structures of varying densities and avoids strict reliance on a single density threshold.
* **No Need for \(k\)**: The algorithm produces a reachability plot, enabling identification of clusters with varying densities, without a predefined \(k\).

#### Mean-Shift Clustering

* **Description**: Mean-shift identifies clusters by iteratively shifting each data point toward the region of highest density within a defined radius. It converges to local maxima of the density function, effectively partitioning the data.
* **Parameters**:
  + Bandwidth: Determines the size of the neighborhood considered for density estimation.
* **No Need for \(k\)**: The algorithm adapts to the data, converging on a set of centroids that correspond to the clusters, dynamically determining the number of clusters.

#### Affinity Propagation

* **Description**: This method relies on message passing between data points to identify exemplars, which act as cluster centers. Data points are assigned to clusters based on the identified exemplars.
* **Parameters**:
  + Preference: A parameter influencing the number of exemplars; it can be tuned based on data properties.
* **No Need for \(k\)**: The number of clusters is discovered automatically during the exemplar identification process.

#### Gaussian Mixture Models (GMM) with Model Selection

* **Description**: GMM assumes data is generated from a mixture of Gaussian distributions. It estimates the parameters of these distributions and assigns probabilities to data points for belonging to each component.
* **Model Selection**:
  + Uses information criteria such as Bayesian Information Criterion (BIC) or Akaike Information Criterion (AIC) to evaluate models with different numbers of components.
* **No Need for Predefined \(k\)**: The model selection process determines the optimal number of components (clusters).

#### Self-Organizing Maps (SOMs)

* **Description**: SOMs are a type of neural network that map high-dimensional data onto a lower-dimensional grid. The grid topology imposes a structure on the data, enabling cluster identification.
* **No Need for \(k\)**: The topology of the grid itself influences the clustering outcome, dynamically revealing clusters without explicitly requiring \(k\).

#### Spectral Clustering with Eigen Gap Analysis

* **Description**: Spectral clustering uses the eigenvalues of a similarity matrix derived from the data to partition it into clusters. It leverages graph theory principles to create natural divisions in the data.
* **Dynamic \(k\)**: The eigen gap analysis method identifies the number of clusters by observing significant drops in the sorted eigenvalue spectrum.

#### Birch (Balanced Iterative Reducing and Clustering Using Hierarchies)

* **Description**: Birch uses a hierarchical clustering tree (CF-tree) structure to cluster large datasets incrementally and dynamically. It is particularly efficient for handling massive datasets.
* **No Need for \(k\)**: Clusters are formed dynamically in the initial stage without requiring \(k\), although it can optionally refine clusters if \(k\) is specified later.

#### Autoencoders for Clustering

* **Description**: Autoencoders are neural networks designed to learn compressed representations of input data. These representations capture essential features that can be used for clustering using secondary algorithms such as DBSCAN or hierarchical clustering.
* **Dynamic \(k\)**: The latent space produced by the autoencoder often reveals intrinsic cluster structures, making it possible to identify clusters without a predefined \(k\).

#### Comparison of Approaches

| **Clustering Method** | **Description** | **Key Parameters** | **How $$k$$ is Determined** | **Strengths** | **Weaknesses** |
| --- | --- | --- | --- | --- | --- |
| Hierarchical Clustering | Builds a hierarchy of clusters visualized in a dendrogram. | Linkage method, distance metric | Determined post hoc by cutting the dendrogram at a desired distance threshold. | No need for predefining $$k$$; interpretable dendrogram. | Computationally expensive for large datasets; sensitive to noise. |
| DBSCAN | Groups densely packed points and identifies noise. | \(\epsilon\) (neighborhood radius), \(minPts\) | Clusters formed dynamically based on density conditions. | Identifies clusters of arbitrary shapes; handles noise. | Sensitive to $$\epsilon$$ and $$minPts$$; struggles with varying densities. |
| OPTICS | Orders points to identify clusters with varying densities. | \(\epsilon\) (optional), \(minPts\) | Clusters inferred from reachability plot without fixed $$k$$. | Handles varying densities; less sensitive to $$\epsilon$$ than DBSCAN. | Computationally intensive; interpretation of reachability plot required. |
| Mean-Shift Clustering | Iteratively shifts data points toward regions of highest density. | Bandwidth (radius for density estimation) | Centroids determined dynamically based on data density. | No predefined $$k$$; handles arbitrary cluster shapes. | Bandwidth selection is critical; can be computationally expensive. |
| Affinity Propagation | Uses message passing to identify exemplars as cluster centers. | Preference (affects number of exemplars) | Automatically identifies the number of clusters during message-passing process. | No $$k$$ required; adaptable to data structure. | High memory and computation cost; sensitive to preference parameter. |
| GMM with Model Selection | Fits data to a mixture of Gaussian distributions, selecting the best model using information criteria. | Initial guesses for parameters | Model selection (BIC/AIC) identifies optimal number of components (clusters). | Flexible probabilistic clustering; works well for elliptical clusters. | Assumes Gaussian distribution; sensitive to initialization. |
| Self-Organizing Maps (SOMs) | Maps high-dimensional data to a grid, revealing cluster structures. | Grid topology (e.g., size, shape) | Clusters emerge dynamically based on grid topology and data distribution. | Effective for dimensionality reduction and clustering; visual insights from the grid. | Requires expertise in setting grid parameters; less precise than other methods for irregularly shaped clusters. |
| Spectral Clustering (Eigen Gap) | Uses graph theory to partition data, with clusters inferred from eigenvalue spectrum analysis. | Similarity matrix construction parameters | Eigen gap analysis determines the number of clusters dynamically. | Handles non-convex clusters; robust for complex data structures. | Computationally expensive for large datasets; requires constructing a similarity graph. |
| Birch | Uses CF-tree structure for efficient clustering of large datasets. | Threshold for branching/merging | Dynamically forms clusters during initial phase; $$k$$ optional for refinement. | Scalable for large datasets; can incorporate $$k$$ refinement. | Struggles with non-spherical clusters and datasets with significant noise. |
| Autoencoders for Clustering | Neural network learns compressed latent space, revealing intrinsic cluster structures. | Network architecture, training parameters | Latent space often reveals clusters dynamically; secondary clustering methods used. | Captures complex patterns in high-dimensional data; flexible combination with clustering methods. | Requires extensive tuning; dependent on secondary clustering method for final cluster assignment. |

## Comparison: k-Nearest Neighbors vs. k-Means Clustering

* Here is a detailed comparative analysis of k-Nearest Neighbors and k-Means Clustering:

| **Aspect** | **k-Nearest Neighbors (kNN)** | **k-Means Clustering** |
| --- | --- | --- |
| Type of Algorithm | Supervised learning algorithm (classification or regression). | Unsupervised learning algorithm (clustering). |
| Purpose | Predicts the label or value for a given data point based on its neighbors. | Groups data into \(k\) clusters based on similarity. |
| Input Requirements | Labeled data for training (requires both features and target values). | Unlabeled data (only features are required). |
| Working Mechanism | Finds the \(k\)-nearest points in the training dataset to a given query point and uses their labels to make predictions. | Iteratively partitions data into \(k\) clusters by minimizing intra-cluster variance. |
| Distance Metric | Typically uses Euclidean distance, but other metrics like Manhattan or Minkowski can also be used. | Uses Euclidean distance (or other metrics) to compute cluster centroids. |
| Output | Predicted label (classification) or value (regression). | Cluster assignments for each data point. |
| Training Phase | No explicit training; kNN is a lazy learner and computes distances during prediction. | Training involves multiple iterations to adjust centroids and assign clusters. |
| Prediction Phase | Involves computing distances from the query point to all training points. | Assigns new data points to the nearest cluster based on the trained centroids. |
| Scalability | Not scalable; high computational cost for large datasets due to distance calculations during prediction. | Scalable with optimizations; faster for large datasets after training. |
| Parameters | Number of neighbors (\(k\)) and distance metric. | Number of clusters (\(k\)) and initialization of centroids. |
| Sensitivity to Parameters | Sensitive to the choice of \(k\); inappropriate \(k\) can lead to overfitting or underfitting. | Sensitive to the choice of \(k\) and initialization of centroids; poor initialization can lead to suboptimal clustering. |
| Interpretability | Intuitive; directly uses neighboring points for prediction. | Less intuitive; requires interpreting clusters. |
| Handling of Outliers | Outliers can strongly influence predictions by affecting the nearest neighbors. | Outliers can distort cluster centroids and lead to poor clustering. |
| Applications | Classification (e.g., image recognition, fraud detection) and regression. | Clustering (e.g., customer segmentation, document classification). |
| Strengths | Simple, effective, and easy to implement; no need for explicit training. | Works well for clustering large datasets; discovers inherent structure. |
| Weaknesses | Computationally expensive during prediction; performance decreases with irrelevant features. | Sensitive to the choice of \(k\); may converge to local minima. |

### Key Takeaways

* **kNN:** A supervised algorithm used for prediction tasks, often with low computational overhead in the training phase but expensive at prediction time.
* **k-Means:** An unsupervised algorithm used to discover groupings in data, efficient for partitioning compact clusters but sensitive to initialization.
* Both algorithms rely heavily on distance metrics, making feature scaling (e.g., normalization or standardization) critical for their performance.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledClustering,
  title   = {Clustering},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
