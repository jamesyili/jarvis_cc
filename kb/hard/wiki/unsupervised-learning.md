---
concept: Unsupervised Learning & Clustering
tags: [unsupervised-learning, clustering, kmeans, pca, dimensionality-reduction]
sources:
  - kb/hard/raw/aman-ai/cs229-k-means-clustering-algorithm.md
  - kb/hard/raw/aman-ai/cs229-principal-component-analysis.md
  - kb/hard/raw/aman-ai/primers-clustering.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings & Representation Learning]]"
  - "[[hard/wiki/supervised-learning|Supervised Learning]]"
  - "[[hard/wiki/self-supervised-contrastive|Self-Supervised & Contrastive Learning]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 0  # not obviously relevant
knowledge_updated: 2026-09-07
---

# Unsupervised Learning & Clustering

Unsupervised learning discovers structure in data without predefined labels. Unlike supervised learning — which requires (x, y) pairs — unsupervised methods work only from inputs {x}. The goals range from grouping similar items together (clustering), to finding compact representations of data (dimensionality reduction), to modeling the underlying distribution (generative models).

This article covers the major approaches: partitioning clustering (K-means), hierarchical clustering, density-based clustering (DBSCAN), the Expectation-Maximization framework (EM/GMM), and Principal Component Analysis (PCA).

## K-Means Clustering

K-means is the canonical partitioning clustering algorithm. Given a dataset {x^(1), ..., x^(m)} ⊂ ℝⁿ, it partitions data into k clusters by minimizing **within-cluster sum of squares (WCSS)**:

`J(c, μ) = Σᵢ ||x^(i) - μ_{c(i)}||²`

where c(i) is the cluster assignment for example i and μⱼ are cluster centroids.

**Algorithm:**
1. Initialize k centroids μ₁, ..., μₖ randomly (or using k-means++ for better initialization)
2. Repeat until convergence:
   - **Assignment step**: assign each point to its nearest centroid
     `c^(i) := argmin_j ||x^(i) - μⱼ||²`
   - **Update step**: recompute each centroid as the mean of assigned points
     `μⱼ := (Σᵢ 1{c^(i)=j} x^(i)) / (Σᵢ 1{c^(i)=j})`

**Convergence**: K-means is coordinate descent on J — each step monotonically decreases J, guaranteeing convergence. However, J is non-convex, so convergence is to a local minimum. Running with multiple random initializations and keeping the best (lowest J) is standard practice.

**Complexity**: O(n · k · t) per iteration, where n = points, k = clusters, t = iterations. Fast in practice.

**Limitations:**
- Requires specifying k upfront
- Assumes spherical, isotropic clusters (fails on elongated or non-convex clusters)
- Sensitive to outliers — outliers can drag centroids away from the true cluster center
- K-medoids (PAM) is more outlier-robust, using actual data points (medoids) as representatives at higher compute cost

**K-means++ initialization** (practical improvement): instead of random initialization, choose centroids sequentially with probability proportional to distance from existing centroids. This produces better starting points and reduces the chance of poor local minima.

## Hierarchical Clustering

Hierarchical clustering builds a nested tree of clusters (dendrogram) without requiring k upfront. The user can choose the number of clusters after the fact by cutting the dendrogram at the appropriate level.

### Agglomerative (Bottom-Up)

Start with each point as its own cluster. Iteratively merge the closest pair of clusters. Termination: when a desired number of clusters is reached or a distance threshold is exceeded.

The **linkage criterion** defines "distance between clusters":
- **Single linkage**: min distance between any two points in the clusters. Tends to create long, chained clusters.
- **Complete linkage**: max distance. Tends to create compact, balanced clusters.
- **Average linkage**: mean pairwise distance. A balanced middle ground.
- **Ward linkage**: merge clusters that minimize increase in total within-cluster variance. Often the best default.

**Complexity**: O(n³) in general, O(n² log n) for some linkage methods. Expensive for large datasets.

### Divisive (Top-Down)

Start with all data in one cluster. Recursively split. Less common — theoretically O(2ⁿ) in the worst case, though practical implementations prune aggressively.

**When to use hierarchical clustering**: when you need interpretable structure, don't know k in advance, and the dataset is small-to-medium scale (< 10K points).

## DBSCAN (Density-Based Clustering)

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) clusters points based on local density rather than distance to a centroid. It finds arbitrarily shaped clusters and naturally identifies noise points.

**Two parameters:**
- ε (epsilon): neighborhood radius
- minPts: minimum number of points to form a dense region

**Point types:**
- **Core point**: has ≥ minPts points within radius ε
- **Border point**: within ε of a core point but doesn't have minPts neighbors itself
- **Noise point**: neither core nor border

**Algorithm**: expand clusters from core points, absorbing all density-reachable points. Noise points are left unclustered.

**Strengths**: handles arbitrary cluster shapes, doesn't require k, robust to outliers. **Weaknesses**: sensitive to ε and minPts choices; struggles when cluster densities vary significantly.

DBSCAN is the go-to for anomaly detection and geospatial clustering where cluster shapes are irregular.

## Expectation-Maximization and Gaussian Mixture Models

**Gaussian Mixture Models (GMM)** assume data is generated from a mixture of K Gaussian distributions. Each cluster is a multivariate Gaussian with its own mean μₖ, covariance Σₖ, and mixing weight πₖ.

The **Expectation-Maximization (EM) algorithm** fits a GMM iteratively:

**E-step (Expectation)**: compute "soft assignments" — the probability that each point was generated by each component:
`r_{ik} = P(z=k | x^(i)) ∝ πₖ · N(x^(i); μₖ, Σₖ)`

**M-step (Maximization)**: update parameters using the soft assignments as weights:
- `πₖ = (1/n) Σᵢ r_{ik}`
- `μₖ = Σᵢ r_{ik} x^(i) / Σᵢ r_{ik}`
- `Σₖ = Σᵢ r_{ik}(x^(i) - μₖ)(x^(i) - μₖ)ᵀ / Σᵢ r_{ik}`

**Connection to K-means**: K-means is a hard-assignment special case of EM — it assigns each point to exactly one cluster (r_{ik} ∈ {0,1}) rather than soft probabilities.

**EM guarantees monotonically increasing log-likelihood at each step** (never decreases), but converges to a local maximum.

GMMs generalize K-means in two ways: (1) soft cluster memberships, (2) elliptical clusters via the covariance matrix.

## Principal Component Analysis (PCA)

PCA finds a lower-dimensional linear subspace that captures maximum variance in the data. It is the canonical dimensionality reduction technique.

**Preprocessing**: before running PCA, normalize the data:
1. Subtract mean (zero-center)
2. Divide by standard deviation (unit variance per feature)

**Algorithm:**
1. Compute the empirical covariance matrix: `Σ = (1/m) Σᵢ x^(i) x^(i)ᵀ`
2. Compute the top-k eigenvectors of Σ: u₁, ..., uₖ (ordered by eigenvalue, largest first)
3. Project data: `y^(i) = [u₁ᵀx^(i), ..., uₖᵀx^(i)]ᵀ ∈ ℝᵏ`

**The eigenvectors u₁, ..., uₖ are the principal components** — orthogonal directions of maximum variance. Projecting onto them retains as much variance as possible in k dimensions.

**Properties:**
- The first principal component maximizes projected variance
- Each subsequent PC is orthogonal to all preceding ones and captures the next most variance
- Total variance explained: `Σ_{i=1}^k λᵢ / Σ_{i=1}^n λᵢ` (where λᵢ are eigenvalues)

**Applications:**
1. **Compression**: represent high-d data with low-d coordinates. Reconstruct approximations as `x̂^(i) ≈ Σⱼ yⱼ^(i) uⱼ`
2. **Visualization**: reduce to 2D or 3D for plotting (e.g., visualizing word embeddings)
3. **Preprocessing**: reduce input dimensionality before a supervised learning model — reduces computational cost and can reduce overfitting
4. **Noise reduction**: principal components capture systematic variation; low-variance directions often correspond to noise

**Choosing k**: plot the cumulative explained variance ratio vs. k ("scree plot"). Choose k at the "elbow" or where 90–95% of variance is explained.

**PCA vs. autoencoders**: PCA finds linear subspaces; autoencoders can find non-linear manifolds. For most tabular data, PCA is faster and more interpretable.

## Choosing a Clustering Method

| Algorithm | When to use |
|---|---|
| K-means | Large datasets, approximately spherical clusters, k is known |
| K-means++ | Same as K-means but want better initialization |
| GMM/EM | Soft cluster membership, elliptical clusters, probabilistic model needed |
| Agglomerative | Don't know k, need interpretable hierarchy, small-medium data |
| DBSCAN | Arbitrary shapes, outlier/noise detection, density-based structure |
| Spectral | Non-convex clusters connected via graph structure |
| PCA | Dimensionality reduction (not clustering per se) |

**Scale matters**: K-means and DBSCAN are tractable at millions of points. Agglomerative clustering becomes expensive beyond ~10K. GMM scales to large datasets if diagonal covariance is assumed.

---

## Sources

- Aman Chadha, "CS229: k-Means Clustering Algorithm," aman.ai, 2026-04-05
- Aman Chadha, "CS229: Principal Component Analysis," aman.ai, 2026-04-05
- Aman Chadha, "Primers: Clustering," aman.ai, 2026-04-05
