# CS229 • Independent Component Analysis

**Source:** https://aman.ai/cs229/ica/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Overview](#overview)
* [ICA ambiguities](#ica-ambiguities)
* [Densities and linear transformations](#densities-and-linear-transformations)
  + [Remarks](#remarks)
* [ICA algorithm](#ica-algorithm)
  + [Remarks](#remarks-1)
* [References](#references)
* [Citation](#citation)

## Overview

* Our next topic is Independent Components Analysis (ICA). Similar to PCA, this will find a new basis in which to represent our data. However, the goal is very different.
* As a motivating example, consider the “cocktail party problem.” Here, \(n\) speakers are speaking simultaneously at a party, and any microphone placed in the room records only an overlapping combination of the \(n\) speakers’ voices.
* But let’s say we have \(n\) different microphones placed in the room, and because each microphone is a different distance from each of the speakers, it records a different combination of the speakers’ voices.
* Using these microphone recordings, can we separate out the original \(n\) speakers’ speech signals? To formalize this problem, we imagine that there is some data \(s \in \mathbb{R}^{n}\) that is generated via \(n\) independent sources. What we observe is,

  \[x=A s\]
  + where \(A\) is an unknown square matrix called the mixing matrix. Repeated observations gives us a dataset \(\left\{x^{(i)} ; i=1, \ldots, m\right\}\), and our goal is to recover the sources \(s^{(i)}\) that had generated our data \(\left(x^{(i)}=A s^{(i)}\right)\).
* In our cocktail party problem, \(s^{(i)}\) is an \(n\)-dimensional vector, and \(s\_{j}^{(i)}\) is the sound that speaker \(j\) was uttering at time \(i\). Also, \(x^{(i)}\) in an \(n\)-dimensional vector, and \(x\_{j}^{(i)}\) is the acoustic reading recorded by microphone \(j\) at time \(i\) Let \(W=A^{-1}\) be the unmixing matrix.
* Our goal is to find \(W\), so that given our microphone recordings \(x^{(i)}\), we can recover the sources by computing \(s^{(i)}=W x^{(i)}\). For notational convenience, we also let \(w\_{i}^{T}\) denote the \(i\)-th row of \(W\), so that,

\[W=\left[\begin{array}{c}
-w\_1^{T}- \\
\vdots \\
-w\_{n}^{T}-
\end{array}\right]\]

* Thus, \(w\_{i} \in \mathbb{R}^{n}\), and the \(j\)-th source can be recovered by computing \(s\_{j}^{(i)}=\) \(w\_{j}^{T} x^{(i)}\).

## ICA ambiguities

* To what degree can \(W=A^{-1}\) be recovered? If we have no prior knowledge about the sources and the mixing matrix, it is not hard to see that there are some inherent ambiguities in \(A\) that are impossible to recover, given only the,

\[x^{(i)} \text {'s. }\]

* Specifically, let \(P\) be any \(n\) -by- \(n\) permutation matrix. This means that each row and each column of \(P\) has exactly one “1.” Here’re some examples of permutation matrices:

\[P=\left[\begin{array}{lll}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{array}\right] ; \quad P=\left[\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right] ; \quad P=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]\]

* If \(z\) is a vector, then \(P z\) is another vector that’s contains a permuted version of \(z\)’s coordinates. Given only the \(x^{(i)}\)’s, there will be no way to distinguish between \(W\) and \(P W\). Specifically, the permutation of the original sources is ambiguous, which should be no surprise. Fortunately, this does not matter for most applications.
* Further, there is no way to recover the correct scaling of the \(w\_{i}\)’s. For instance, if \(A\) were replaced with \(2 A\), and every \(s^{(i)}\) were replaced with \((0.5) s^{(i)}\), then our observed \(x^{(i)}=2 A \cdot(0.5) s^{(i)}\) would still be the same. More broadly, if a single column of \(A\) were scaled by a factor of \(\alpha\), and the corresponding source were scaled by a factor of \(\frac{1}{\alpha}\), then there is again no way, given only the \(x^{(i)}\)’s to determine that this had happened. Thus, we cannot recover the “correct” scaling of the sources.
* However, for the applications that we are concerned with-including the cocktail party problem-this ambiguity also does not matter. Specifically, scaling a speaker’s speech signal \(s\_{j}^2\) by some positive factor \(\alpha\) affects only the volume of that speaker’s speech. Also, sign changes do not matter, and \(s\_{j}^{(i)}\) and \(-s\_{j}^{(i)}\) sound identical when played on a speaker. Thus, if the \(w\_{i}\) found by an algorithm is scaled by any non-zero real number, the corresponding recovered source \(s\_{i}=w\_{i}^{T} x\) will be scaled by the same factor; but this usually does not matter. (These comments also apply to ICA for the brain/MEG data example.)
* Are these the only sources of ambiguity in ICA? It turns out that they are, so long as the sources \(s\_{i}\) are non-Gaussian. To see what the difficulty is with Gaussian data, consider an example in which \(n=2\), and \(s \sim \mathcal{N}(0, I)\). Here, \(I\) is the \(2 \times 2\) identity matrix. Note that the contours of the density of the standard normal distribution \(\mathcal{N}(0, I)\) are circles centered on the origin, and the density is rotationally symmetric.
* Now, suppose we observe some \(x=A s\), where \(A\) is our mixing matrix. The distribution of \(x\) will also be Gaussian, with zero mean and covariance \(\mathrm{E}\left[x x^{T}\right]=\mathrm{E}\left[A s s^{T} A^{T}\right]=A A^{T}\).
* Now, let \(R\) be an arbitrary orthogonal (less formally, a rotation/reflection) matrix, so that \(R R^{T}=R^{T} R=I\), and let \(A^{\prime}=AR\). Then if the data had been mixed according to \(A^{\prime}\) instead of \(A\), we would have instead observed \(x^{\prime}=A^{\prime}s\). The distribution of \(x^{\prime}\) is also Gaussian, with zero mean and covariance \(\mathrm{E}\left[x^{\prime}\left(x^{\prime}\right)^{T}\right]=\mathrm{E}\left[A^{\prime} s s^{T}\left(A^{\prime}\right)^{T}\right]=\mathrm{E}\left[A R s s^{T}(A R)^{T}\right]=A R R^{T} A^{T}=A A^{T}\). Hence, whether the mixing matrix is \(A\) or \(A^{\prime}\), we would observe data from a \(\mathcal{N}\left(0, A A^{T}\right)\) distribution. Thus, there is no way to tell if the sources were mixed using \(A\) and \(A^{\prime}\). So, there is an arbitrary rotational component in the mixing matrix that cannot be determined from the data, and we cannot recover the original sources.
* Our argument above was based on the fact that the multivariate standard normal distribution is rotationally symmetric. Despite the bleak picture that this paints for ICA on Gaussian data, it turns out that, so long as the data is not Gaussian, it is possible, given enough data, to recover the \(n\) independent sources.

## Densities and linear transformations

* Before moving on to derive the ICA algorithm proper, we first digress briefly to talk about the effect of linear transformations on densities.
* Suppose we have a random variable \(s\) drawn according to some density \(p\_{s}(s)\). For simplicity, let us say for now that \(s \in \mathbb{R}\) is a real number. Now, let the random variable \(x\) be defined according to \(x=A s\) (here, \(x \in \mathbb{R}, A \in \mathbb{R}\)). Let \(p\_{x}\) be the density of \(x\). What is \(p\_{x}\)?
* Let \(W=A^{-1}\). To calculate the “probability” of a particular value of \(x\), it is tempting to compute \(s=W x\), then evaluate \(p\_{s}\) at that point, and conclude that \(“p\_{x}(x)=p\_{s}(W x)”\). However, this is incorrect. For example, let \(s \sim \text{Uniform} [0,1]\), so that \(s\)’s density is \(p\_{s}(s)=1{0 \leq s \leq 1}\). Now, let \(A=2\), so that \(x=2 s\). Clearly, \(x\) is distributed uniformly in the interval \([0,2]\). Thus, its density is given by \(p\_{x}(x)=(0.5) 1\{0 \leq x \leq 2\}\). This does not equal \(p\_{s}(W x)\), where \(W=0.5=A^{-1}\). Instead, the correct formula is \(p\_{x}(x)=p\_{s}(W x)|W|\).
* More generally, if \(s\) is a vector-valued distribution with density \(p\_{s}\), and \(x=A s\) for a square, invertible matrix \(A\), then the density of \(x\) is given by,

  \[p\_{x}(x)=p\_{s}(W x) \cdot|W|\]
  + where \(W=A^{-1}\).

### Remarks

* If you’ve seen the result that \(A\) maps \([0,1]^{n}\) to a set of volume \(|A|\) then here’s another way to remember the formula for \(p\_{x}\) given above, that also generalizes our previous 1-dimensional example. Specifically, let \(A \in \mathbb{R}^{n \times n}\) be given, and let \(W=A^{-1}\) as usual. Also let \(C=[0,1]^{n}\) be the \(n\)-dimensional hypercube, and define \(C\_2=\left\{A s: s \in C\_1\right\} \subseteq \mathbb{R}^{n}\) to be the image of \(C\_1\) under the mapping given by \(A\). Then it is a standard result in linear algebra (and, indeed, one of the ways of defining determinants) that the volume of \(C\_2\) is given by \(|A|\).
* Now, suppose \(s\) is uniformly distributed in \([0,1]^{n}\), so its density is \(p\_{s}(s)=\mathbb{1}\left\{s \in C\_1\right\}\). Then clearly \(x\) will be uniformly distributed in \(C\_2\). Its density is therefore found to be \(p\_{x}(x)=\frac{\mathbb{1}\{x \in C\_2\}}{\operatorname{vol}(C\_2)}\) (since it must integrate over \(C\_2\) to 1). But using the fact that the determinant of the inverse of a matrix is just the inverse of the determinant, we have \(\frac{1}{\operatorname{vol}\left(C\_2\right)}=\frac{1}{|A|}=\left|A^{-1}\right| = |W|\). Thus, \(p\_{x}(x)=\mathbb{1}\{x \in C\_2\}|W|=\mathbb{1}\{W x \in C\_1\}|W|=p\_{s}(W x)|W|\).

## ICA algorithm

* We are now ready to derive an ICA algorithm. The algorithm we describe is due to Bell and Sejnowski, and the interpretation we give will be of their algorithm as a method for maximum likelihood estimation. (This is different from their original interpretation, which involved a complicated idea called the infomax principal, that is no longer necessary in the derivation given the modern understanding of ICA.)
* We suppose that the distribution of each source \(s\_{i}\) is given by a density \(p\_{s}\), and that the joint distribution of the sources \(s\) is given by,

\[P(s)=\prod\_{i=1}^{n} p\_{s}\left(s\_{i}\right)\]

* Note that by modeling the joint distribution as a product of the marginal, we capture the assumption that the sources are independent. Using our formulas from the previous section, this implies the following density on \(x=A s=W^{-1} s\):

\[P(x)=\prod\_{i=1}^{n} p\_{s}\left(w\_{i}^{T} x\right) \cdot|W|\]

* All that remains is to specify a density for the individual sources \(p\_{s}\) Recall that, given a real-valued random variable \(z\), its cumulative distribution function (cdf) \(F(\cdot)\) is defined by \(F\left(z\_{0}\right)=P\left(z \leq z\_{0}\right)=\int\_{-\infty}^{z\_{0}} p\_{z}(z) d z\) Also, the density of \(z\) can be found from the cdf by taking its derivative:
  \(p\_{z}(z)=F^{\prime}(z)\).
* Thus, to specify a density for the \(s\_{i}\)’s, all we need to do is to specify some cdf for it. A cdf has to be a monotonic function that increases from zero to one. Following our previous discussion, we cannot choose the cdf to be the cdf of the Gaussian, as ICA doesn’t work on Gaussian data. What we’ll choose instead for the cdf, as a reasonable “default” function that slowly increases from 0 to 1, is the sigmoid function \(g(s)=\frac{1}{1+e^{-s}}\). Hence, \(p\_{s}(s)=g^{\prime}(s)\).
  + If you have prior knowledge that the sources’ densities take a certain form, then it is a good idea to substitute that in here. But in the absence of such knowledge, the sigmoid function can be thought of as a reasonable default that seems to work well for many problems. Also, the presentation here assumes that either the data \(x^{(i)}\) has been preprocessed to have zero mean, or that it can naturally be expected to have zero mean (such as acoustic signals).
  + This is necessary because our assumption that \(p\_{s}(s)=g^{\prime}(s)\) implies \(\mathrm{E}[s]=0\) (the derivative of the logistic function is a symmetric function, and hence gives a density corresponding to a random variable with zero mean), which implies \(\mathrm{E}[x]=\mathrm{E}[A s]=0\).
* The square matrix \(W\) is the parameter in our model. Given a training \(\operatorname{set}\left\{x^{(i)} ; i=1, \ldots, m\right\}\), the log likelihood is given by,

\[\ell(W)=\sum\_{i=1}^{m}\left(\sum\_{j=1}^{n} \log g^{\prime}\left(w\_{j}^{T} x^{(i)}\right)+\log |W|\right)\]

* We would like to maximize this in terms \(W\). By taking derivatives and using the fact (from the first set of notes) that \(\nabla\_{W}|W|=|W|\left(W^{-1}\right)^{T}\), we easily derive a stochastic gradient ascent learning rule. For a training example \(x^{(i)}\), the update rule is:

  \[\left.W:=W+\alpha\left(\begin{array}{c}
  1-2 g\left(w\_1^{T} x^{(i)}\right) \\
  1-2 g\left(w\_2^{T} x^{(i)}\right) \\
  \vdots \\
  1-2 g\left(w\_{n}^{T} x^{(i)}\right)
  \end{array}\right] x^{(i)^{T}+\left(W^{T}\right)^{-1}}\right)\]
  + where \(\alpha\) is the learning rate.
* After the algorithm converges, we then compute \(s^{(i)}=W x^{(i)}\) to recover the original sources.

### Remarks

* When writing down the likelihood of the data, we implicity assumed that the \(x^{(i)}\)’s were independent of each other (for different values of \(i\); note this issue is different from whether the different coordinates of \(x^{(i)}\) are independent \()\), so that the likelihood of the training set was given by,

\[\prod\_{i} P\left(x^{(i)} ; W\right)\]

* This assumption is clearly incorrect for speech data and other time series where the \(x^{(i)}\)’s are dependent, but it can be shown that having correlated training examples will not hurt the performance of the algorithm if we have sufficient data.
* But, for problems where successive training examples are correlated, when implementing stochastic gradient ascent, it also sometimes helps accelerate convergence if we visit training examples in a randomly permuted order (i.e., run stochastic gradient ascent on a randomly shuffled copy of the training set.)

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledIndependentComponentAnalysis,
  title   = {Independent Component Analysis},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
