# Primers • Vector Databases

**Source:** https://aman.ai/primers/ai/vector-dbs/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Quantization](#quantization)
  + [Vector Quantization (VQ)](#vector-quantization-vq)
  + [Product Quantization (PQ)](#product-quantization-pq)
  + [Summary](#summary)
* [Codebook](#codebook)
  + [Codebook in Vector Quantization (VQ)](#codebook-in-vector-quantization-vq)
    - [Concept:](#concept)
    - [Construction:](#construction)
    - [Usage:](#usage)
    - [Example:](#example)
  + [Codebook in Product Quantization (PQ)](#codebook-in-product-quantization-pq)
    - [Concept:](#concept-1)
    - [Construction:](#construction-1)
    - [Usage:](#usage-1)
    - [Example:](#example-1)
  + [Advantages of Codebooks:](#advantages-of-codebooks)
  + [Limitations of Codebooks:](#limitations-of-codebooks)
  + [Summary:](#summary-1)
* [Citation](#citation)

## Quantization

* Vector quantization (VQ) and product quantization (PQ) are both techniques used in data compression and information retrieval, particularly for large-scale nearest neighbor search. Here’s a comparison of the two:

### Vector Quantization (VQ)

1. **Concept:**
   * Vector quantization is a classical quantization technique where the input vectors are partitioned into regions and each region is represented by a centroid (codeword).
2. **Process:**
   * The input space is divided into a number of regions, each associated with a centroid.
   * Each vector is approximated by the centroid of the region it falls into.
3. **Codebook:**
   * A single codebook is used, which contains all the centroids representing the regions.
   * The size of the codebook is typically \(k\), where \(k\) is the number of centroids.
4. **Encoding:**
   * Each input vector is encoded by the index of the closest centroid in the codebook.
   * The encoding process involves finding the nearest centroid for each vector.
5. **Applications:**
   * Used in lossy data compression, image compression, and pattern recognition.
6. **Limitations:**
   * VQ becomes computationally expensive and less efficient as the dimensionality of the data increases because the number of centroids needed grows exponentially with the dimension.

### Product Quantization (PQ)

1. **Concept:**
   * Product quantization is an advanced quantization technique that decomposes the original space into a Cartesian product of lower-dimensional subspaces, each quantized separately.
2. **Process:**
   * The input vector space is split into multiple subspaces (typically of equal size).
   * Each subspace is quantized independently using its own codebook.
3. **Codebooks:**
   * Multiple codebooks are used, one for each subspace.
   * If the original vector is split into \(m\) subspaces, there are \(m\) codebooks, each with \(k\) centroids.
4. **Encoding:**
   * Each vector is split into sub-vectors.
   * Each sub-vector is quantized by finding the nearest centroid in the corresponding subspace codebook.
   * The encoding results in a combination of indices from each subspace’s codebook.
5. **Applications:**
   * Particularly effective in approximate nearest neighbor search in high-dimensional spaces.
   * Used in large-scale image retrieval and deep learning for efficient similarity search.
6. **Advantages:**
   * More scalable for high-dimensional data as it reduces the complexity by handling smaller subspaces.
   * The combination of multiple subspace quantizations allows for a more compact representation and efficient search.
7. **Limitations:**
   * The choice of how to split the vector space into subspaces can impact the efficiency and accuracy of the quantization.
   * PQ assumes that the subspaces are independent, which might not hold true for all datasets.

### Summary

* **Vector Quantization (VQ)** uses a single codebook to quantize the entire vector space, making it straightforward but less efficient for high-dimensional data.
* **Product Quantization (PQ)** decomposes the vector space into smaller subspaces and uses separate codebooks for each, allowing for more efficient and scalable quantization in high-dimensional spaces.
* PQ is generally preferred in scenarios requiring efficient large-scale nearest neighbor search due to its ability to handle high-dimensional data more effectively.

## Codebook

* A codebook in the context of quantization, specifically vector quantization (VQ) and product quantization (PQ), is a critical component that contains a set of representative vectors, known as codewords or centroids. These codewords are used to approximate and encode the original high-dimensional data points. Let’s delve into the details:

### Codebook in Vector Quantization (VQ)

#### Concept:

* A codebook is a collection of \(k\) codewords, each representing a region in the vector space.
* Each codeword is essentially a centroid of a cluster of similar vectors.

#### Construction:

* The codebook is typically constructed using clustering algorithms like K-means:
  1. **Initialization:** Start with \(k\) initial centroids (these can be randomly selected points from the data).
  2. **Assignment:** Assign each data point to the nearest centroid.
  3. **Update:** Recalculate the centroids as the mean of all points assigned to each centroid.
  4. **Iteration:** Repeat the assignment and update steps until convergence (centroids no longer change significantly).

#### Usage:

* **Encoding:** For a given input vector, find the nearest codeword in the codebook and represent the vector by the index of this codeword.
* **Decoding:** The index can be used to retrieve the codeword, which approximates the original vector.

#### Example:

* Suppose you have a 2-dimensional vector space, and you create a codebook with 4 codewords. Each vector is then represented by one of these 4 centroids.

### Codebook in Product Quantization (PQ)

#### Concept:

* In PQ, the codebook is used in a more complex manner. The vector space is split into \(m\) smaller subspaces, and each subspace has its own codebook.
* Each codebook in a subspace contains \(k\) codewords representing the subspace vectors.

#### Construction:

* Similar to VQ, each subspace’s codebook is constructed using a clustering algorithm applied to the sub-vectors derived from splitting the original vectors.

#### Usage:

* **Encoding:**
  1. **Splitting:** Split the original high-dimensional vector into \(m\) smaller sub-vectors.
  2. **Quantization:** Quantize each sub-vector using the corresponding subspace codebook by finding the nearest codeword.
  3. **Indexing:** The original vector is then represented by a tuple of indices, each index referring to a codeword in the respective subspace codebook.
* **Decoding:** Use the tuple of indices to retrieve the corresponding codewords from each subspace codebook and concatenate them to approximate the original vector.

#### Example:

* Suppose you have a 4-dimensional vector space and split it into 2 subspaces (each of 2 dimensions). Each subspace has its own codebook of 4 codewords. A vector is then represented by a combination of two indices, one from each subspace.

### Advantages of Codebooks:

1. **Compression:**
   * Codebooks enable significant data compression by representing high-dimensional vectors with much smaller indices.
2. **Efficiency:**
   * Searching and comparing vectors can be done more efficiently using indices rather than full high-dimensional vectors.
3. **Scalability:**
   * Particularly in PQ, the decomposition into subspaces makes it scalable for very high-dimensional data.

### Limitations of Codebooks:

1. **Quantization Error:**
   * Approximation with codewords introduces quantization error, which can affect the accuracy of tasks such as nearest neighbor search.
2. **Complexity:**
   * The construction of codebooks, especially for large datasets and high dimensions, can be computationally intensive.
3. **Independence Assumption in PQ:**
   * PQ assumes subspaces are independent, which might not always be true, potentially affecting the effectiveness of the quantization.

### Summary:

* A codebook in quantization is a set of representative vectors (codewords) used to approximate original data points. In VQ, a single codebook represents the entire vector space, while in PQ, multiple codebooks represent different subspaces of the vector space. Codebooks are essential for data compression, efficient storage, and fast search operations, though they introduce some level of approximation error.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2021DistilledVectorDBs,
  title   = {Vector Databases},
  author  = {Jain, Vinija and Chadha, Aman},
  journal = {Distilled AI},
  year    = {2021},
  note    = {\url{https://aman.ai}}
}
```
