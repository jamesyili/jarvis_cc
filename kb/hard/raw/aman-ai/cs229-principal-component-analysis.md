# CS229 • Principal Component Analysis

**Source:** https://aman.ai/cs229/pca/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Overview](#overview)
  + [Remarks](#remarks)
* [References](#references)
* [Citation](#citation)

## Overview

* In our discussion of factor analysis, we gave a way to model data \(x \in \mathbb{R}^{n}\) as “approximately” lying in some \(k\)-dimensional subspace, where \(k \ll n\). Specifically, we imagined that each point \(x^{(i)}\) was created by first generating some \(z^{(i)}\) lying in the \(k\)-dimensional affine space \(\left\{\Lambda z+\mu ; z \in \mathbb{R}^{k}\right\}\), and then adding \(\Psi\)-covariance noise.
* Factor analysis is based on a probabilistic model, and parameter estimation used the iterative EM algorithm.
* In this section, we will develop a method, Principal Components Analysis (PCA), that also tries to identify the subspace in which the data approximately lies. However, PCA will do so more directly, and will require only an eigenvector calculation (easily done with the [`numpy.linalg.eig` function in NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html) or the [`eig` function in MATLAB](https://www.mathworks.com/help/matlab/ref/eig.html)), and does not need to resort to EM.
* Suppose we are given a dataset \(\left\{x^{(i)} ; i=1, \ldots, m\right\}\) of attributes of \(m\) different types of automobiles, such as their maximum speed, turn radius, and so on. Let \(x^{(i)} \in \mathbb{R}^{n}\) for each \(i\,(n \ll m)\). But unknown to us, two different attributes – some \(x\_{i}\) and \(x\_{j}\) – respectively give a car’s maximum speed measured in miles per hour, and the maximum speed measured in kilometers per hour.
* These two attributes are therefore almost linearly dependent, up to only small differences introduced by rounding off to the nearest mph or kph. Thus, the data really lies approximately on an \(n-1\) dimensional subspace. How can we automatically detect, and perhaps remove, this redundancy?
* For a less contrived example, consider a dataset resulting from a survey of pilots for radio-controlled helicopters, where \(x\_{1}^{(i)}\) is a measure of the piloting skill of pilot \(i\), and \(x\_{2}^{(i)}\) captures how much he/she enjoys flying. Because RC helicopters are very difficult to fly, only the most committed students, ones that truly enjoy flying, become good pilots. So, the two attributes \(x\_{1}\) and \(x\_{2}\) are strongly correlated.
* Indeed, we might posit that that the data actually likes along some diagonal axis (the \(u\_{1}\) direction) capturing the intrinsic piloting “karma” of a person, with only a small amount of noise lying off this axis. Looking at the figure below, how can we automatically compute this \(u\_{1}\) direction?

* We will shortly develop the PCA algorithm. But prior to running PCA per se, typically we first pre-process the data to normalize its mean and variance, as follows:

  1. Let \(\mu=\frac{1}{m} \sum\_{i=1}^{m} x^{(i)}\)
  2. Replace each \(x^{(i)}\) with \(x^{(i)}-\mu\)
  3. Let \(\sigma\_{j}^{2}=\frac{1}{m} \sum\_{i}\left(x\_{j}^{(i)}\right)^{2}\)
  4. Replace each \(x\_{j}^{(i)}\) with \(x\_{j}^{(i)} / \sigma\_{j}\)
* Steps \((1-2)\) zero out the mean of the data, and may be omitted for data known to have zero mean (for instance, time series corresponding to speech or other acoustic signals). Steps \((3-4)\) rescale each coordinate to have unit variance, which ensures that different attributes are all treated on the same “scale”.
  + For instance, if \(x\_{1}\) was cars’ maximum speed in mph (taking values in the high tens or low hundreds) and \(x\_{2}\) were the number of seats (taking values around \(2-4\)), then this renormalization rescales the different attributes to make them more comparable.
* Steps \((3-4)\) may be omitted if we had apriori knowledge that the different attributes are all on the same scale. One example of this is if each data point represented a grayscale image, and each \(x\_{j}^{(i)}\) took a value in \({0,1, \ldots, 255}\) corresponding to the intensity value of pixel \(j\) in image \(i\).
* Now, having carried out the normalization, how do we compute the “major axis of variation” \(u-\) that is, the direction on which the data approximately lies? One way to pose this problem is as finding the unit vector \(u\) so that when the data is projected onto the direction corresponding to \(u\), the variance of the projected data is maximized.
* Intuitively, the data starts off with some amount of variance/information in it. We would like to choose a direction \(u\) so that if we were to approximate the data as lying in the direction/subspace corresponding to \(u\), as much as possible of this variance is still retained.
* Consider the following dataset, on which we have already carried out the normalization steps:

* Now, suppose we pick \(u\) to correspond the the direction shown in the figure below. The circles denote the projections of the original data onto this line.

* We see that the projected data still has a fairly large variance, and the points tend to be far from zero. In contrast, suppose had instead picked the following direction:

* Here, the projections have a significantly smaller variance, and are much closer to the origin.
* We would like to automatically select the direction \(u\) corresponding to the first of the two figures shown above. To formalize this, note that given a unit vector \(u\) and a point \(x\), the length of the projection of \(x\) onto \(u\) is given by \(x^{T} u\), i.e., if \(x^{(i)}\) is a point in our dataset (one of the crosses in the plot), then its projection onto \(u\) (the corresponding circle in the figure) is distance \(x^{T} u\) from the origin. Hence, to maximize the variance of the projections, we would like to choose a unit-length \(u\) so as to maximize:

\[\begin{aligned}
\frac{1}{m} \sum\_{i=1}^{m}\left(x^{(i)^{T}} u\right)^{2} &=\frac{1}{m} \sum\_{i=1}^{m} u^{T} x^{(i)} x^{(i)^{T}} u \\
&=u^{T}\left(\frac{1}{m} \sum\_{i=1}^{m} x^{(i)} x^{(i)^{T}}\right) u
\end{aligned}\]

* We easily recognize that maximizing this subject to \(\mid u\mid\_2=1\) gives the principal eigenvector of \(\Sigma=\frac{1}{m} \sum\_{i=1}^{m} x^{(i)} x^{(i)^{T}}\), which is just the empirical covariance matrix of the data (assuming it has zero mean).
  + If you haven’t seen this before, try using the method of Lagrange multipliers to maximize \(u^{T} \Sigma u\) subject to that \(u^{T} u=1\). You should be able to show that \(\Sigma u=\lambda u\), for some \(\lambda\), which implies \(u\) is an eigenvector of \(\Sigma\), with eigenvalue \(\lambda\).
* To summarize, we have found that if we wish to find a 1-dimensional subspace with with to approximate the data, we should choose \(u\) to be the principal eigenvector of \(\Sigma\).
* More generally, if we wish to project our data into a \(k\)-dimensional subspace \((k<n)\), we should choose \(u\_{1}, \ldots, u\_{k}\) to be the top \(k\) eigenvectors of \(\Sigma\). The \(u\_{i}\)’s now form new, orthogonal basis for the data. Because \(\Sigma\) is symmetric, the \(u\_{i}\)’s will (or always can be chosen to be) orthogonal to each other.
* Then, to represent \(x^{(i)}\) in this basis, we need only compute the corresponding vector

\[y^{(i)}=\left[\begin{array}{c}
u\_{1}^{T} x^{(i)} \\
u\_{2}^{T} x^{(i)} \\
\vdots \\
u\_{k}^{T} x^{(i)}
\end{array}\right] \in \mathbb{R}^{k}\]

* Thus, whereas \(x^{(i)} \in \mathbb{R}^{n}\), the vector \(y^{(i)}\) now gives a lower, \(k\)-dimensional, approximation/representation for \(x^{(i)}\). PCA is therefore also referred to as a dimensionality reduction algorithm. The vectors \(u\_{1}, \ldots, u\_{k}\) are called the first \(k\) principal components of the data.

### Remarks

* Although we have shown it formally only for the case of \(k=1\) using well-known properties of eigenvectors it is straightforward to show that of all possible orthogonal bases \(u\_{1}, \ldots, u\_{k}\), the one that we have chosen maximizes \(\sum\_{i}\left|y^{(i)}\right|\_{2}^{2}\). Thus, our choice of a basis preserves as much variability as possible in the original data.
* \(\mathrm{PCA}\) can also be derived by picking the basis that minimizes the approximation error arising from projecting the data onto the \(k\)-dimensional subspace spanned by them.
* PCA has many applications; we will close our discussion with a few examples. First, compression -representing \(x^{(i)}\)’s with lower dimension \(y^{(i)}\)’s \(-\) is an obvious application. If we reduce high dimensional data to \(k=2\) or 3 dimensions, then we can also plot the \(y^{(i)}\)’s to visualize the data.
  + For instance, if we were to reduce our automobiles data to 2 dimensions, then we can plot it (one point in our plot would correspond to one car type, say) to see what cars are similar to each other and what groups of cars may cluster together.
* Another standard application is to preprocess a dataset to reduce its dimension before running a supervised learning learning algorithm with the \(x^{(i)}\)’s as inputs. Apart from computational benefits, reducing the data’s dimension can also reduce the complexity of the hypothesis class considered and help avoid overfitting (e.g., linear classifiers over lower dimensional input spaces will have smaller VC dimension).
* Lastly, as in our RC pilot example, we can also view PCA as a noise reduction algorithm. In our example it estimates the intrinsic “piloting karma” from the noisy measures of piloting skill and enjoyment. In class, we also saw the application of this idea to face images, resulting in eigenfaces method. Here, each point \(x^{(i)} \in \mathbb{R}^{100 \times 100}\) was a 10000 dimensional vector, with each coordinate corresponding to a pixel intensity value in a \(100 \times 100\) image of a face.
* Using PCA, we represent each image \(x^{(i)}\) with a much lower-dimensional \(y^{(i)}\) In doing so, we hope that the principal components we found retain the interesting, systematic variations between faces that capture what a person really looks like, but not the “noise” in the images introduced by minor lighting variations, slightly different imaging conditions, and so on. We then measure distances between faces \(i\) and \(j\) by working in the reduced dimension, and computing \(\left|y^{(i)}-y^{(j)}\right|\_{2}\). This resulted in a surprisingly good face-matching and retrieval algorithm.

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).
* [numpy.linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
* [Eigenvalues and eigenvectors in MATLAB](https://www.mathworks.com/help/matlab/ref/eig.html)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledPrincipalComponentAnalysis,
  title   = {Principal Component Analysis},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
