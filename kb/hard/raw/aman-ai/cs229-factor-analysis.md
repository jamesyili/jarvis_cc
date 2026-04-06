# CS229 • Factor Analysis

**Source:** https://aman.ai/cs229/factor-analysis/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Overview](#overview)
* [Restrictions of \(\Sigma\)](#restrictions-of-sigma)
* [Marginals and conditionals of Gaussians](#marginals-and-conditionals-of-gaussians)
* [The Factor analysis model](#the-factor-analysis-model)
* [EM for factor analysis](#em-for-factor-analysis)
* [References](#references)
* [Citation](#citation)

## Overview

* When we have data \(x^{(i)} \in \mathbb{R}^{n}\) that comes from a mixture of several Gaussians, the EM algorithm can be applied to fit a mixture model. In this setting, we usually imagine problems where we have sufficient data to be able to discern the multiple-Gaussian structure in the data. For instance, this would be the case if our training set size \(m\) was significantly larger than the dimension \(n\) of the data.
* Now, consider a setting in which \(n \gg m\). In such a problem, it might be difficult to model the data even with a single Gaussian, much less a mixture of Gaussian. Specifically, since the \(m\) data points span only a low-dimensional subspace of \(\mathbb{R}^{n}\), if we model the data as Gaussian, and estimate the mean and covariance using the usual maximum likelihood estimators,

\[\begin{aligned}
\mu &=\frac{1}{m} \sum\_{i=1}^{m} x^{(i)} \\
\Sigma &=\frac{1}{m} \sum\_{i=1}^{m}\left(x^{(i)}-\mu\right)\left(x^{(i)}-\mu\right)^{T}
\end{aligned}\]

* we would find that the matrix \(\Sigma\) is singular. This means that \(\Sigma^{-1}\) does not exist, and \(\frac{1}{|\Sigma|^{1/2}}=\frac{1}{0}=\infty\). But both of these terms are needed in computing the usual density of a multivariate Gaussian distribution. Another way of stating this difficulty is that maximum likelihood estimates of the parameters result in a Gaussian that places all of its probability in the affine space spanned by the data, and this corresponds to a singular covariance matrix.
  + The data is the set of points \(x\) satisfying \(x=\sum\_{i=1}^{m} \alpha\_{i} x^{(i)}\), for some \(\alpha\_{i}\)’s so that \(\sum\_{i=1}^{m} \alpha\_{1}=1\).
* More generally, unless \(m\) exceeds \(n\) by some reasonable amount, the maximum likelihood estimates of the mean and covariance may be quite poor. Nonetheless, we would still like to be able to fit a reasonable Gaussian model to the data, and perhaps capture some interesting covariance structure in the data. How can we do this?
* In the next section, we begin by reviewing two possible restrictions on \(\Sigma\), ones that allow us to fit \(\Sigma\) with small amounts of data but neither of which will give a satisfactory solution to our problem. We next discuss some properties of Gaussians that will be needed later; specifically, how to find marginal and conditional distributions of Gaussians. Finally, we present the factor analysis model, and EM for it.

## Restrictions of \(\Sigma\)

* If we do not have sufficient data to fit a full covariance matrix, we may place some restrictions on the space of matrices \(\Sigma\) that we will consider. For instance, we may choose to fit a covariance matrix \(\Sigma\) that is diagonal. In this setting, the reader may easily verify that the maximum likelihood estimate of the covariance matrix is given by the diagonal matrix \(\Sigma\) satisfying,

\[\Sigma\_{j j}=\frac{1}{m} \sum\_{i=1}^{m}\left(x\_{j}^{(i)}-\mu\_{j}\right)^{2}\]

* Thus, \(\Sigma\_{j j}\) is just the empirical estimate of the variance of the \(j\)-th coordinate of the data.
* Recall that the contours of a Gaussian density are ellipses. A diagonal \(\Sigma\) corresponds to a Gaussian where the major axes of these ellipses are axis aligned.
* Sometimes, we may place a further restriction on the covariance matrix that not only must it be diagonal, but its diagonal entries must all be equal. In this setting, we have \(\Sigma=\sigma^{2} I\), where \(\sigma^{2}\) is the parameter under our control. The maximum likelihood estimate of \(\sigma^{2}\) can be found to be:

\[\sigma^{2}=\frac{1}{m n} \sum\_{j=1}^{n} \sum\_{i=1}^{m}\left(x\_{j}^{(i)}-\mu\_{j}\right)^{2}\]

* This model corresponds to using Gaussians whose densities have contours that are circles (in 2 dimensions; or spheres/hyperspheres in higher dimensions).
* If we were fitting a full, unconstrained, covariance matrix \(\Sigma\) to data, it was necessary that \(m \geq n+1\) in order for the maximum likelihood estimate of \(\Sigma\) not to be singular. Under either of the two restrictions above, we may obtain non-singular \(\Sigma\) when \(m \geq 2\).
* However, restricting \(\Sigma\) to be diagonal also means modeling the different coordinates \(x\_{i}, x\_{j}\) of the data as being uncorrelated and independent. Often, it would be nice to be able to capture some interesting correlation structure in the data. If we were to use either of the restrictions on \(\Sigma\) described above, we would therefore fail to do so. In this section, we will describe the factor analysis model, which uses more parameters than the diagonal \(\Sigma\) and captures some correlations in the data, but also without having to fit a full covariance matrix.

## Marginals and conditionals of Gaussians

* Before describing factor analysis, we digress to talk about how to find conditional and marginal distributions of random variables with a joint multivariate Gaussian distribution. Suppose we have a vector-valued random variable,

  \[x=\left[\begin{array}{l}
  x\_{1} \\
  x\_{2}
  \end{array}\right]\]
  + where \(x\_{1} \in \mathbb{R}^{r}, x\_{2} \in \mathbb{R}^{s}\), and \(x \in \mathbb{R}^{r+s}\). Suppose \(x \sim \mathcal{N}(\mu, \Sigma)\), where,\[\mu=\left[\begin{array}{l}
  \mu\_{1} \\
  \mu\_{2}
  \end{array}\right], \quad \Sigma=\left[\begin{array}{ll}
  \Sigma\_{11} & \Sigma\_{12} \\
  \Sigma\_{21} & \Sigma\_{22}
  \end{array}\right]\]
* Here, \(\mu\_{1} \in \mathbb{R}^{r}, \mu\_{2} \in \mathbb{R}^{s}, \Sigma\_{11} \in \mathbb{R}^{r \times r}, \Sigma\_{12} \in \mathbb{R}^{r \times s}\), and so on. Note that since
  covariance matrices are symmetric, \(\Sigma\_{12}=\Sigma\_{21}^{T}\).
* Under our assumptions, \(x\_{1}\) and \(x\_{2}\) are jointly multivariate Gaussian. What is the marginal distribution of \(x\_{1}\)? It is not hard to see that \(\mathrm{E}\left[x\_{1}\right]=\mu\_{1}\) and that \(\operatorname{Cov}\left(x\_{1}\right)=\mathrm{E}\left[\left(x\_{1}-\mu\_{1}\right)\left(x\_{1}-\mu\_{1}\right)\right]=\Sigma\_{11}\). To see that the latter is
  true, note that by definition of the joint covariance of \(x\_{1}\) and \(x\_{2}\), we have that,

\[\begin{aligned}
\operatorname{Cov}(x) &=\Sigma \\
&=\left[\begin{array}{cc}
\Sigma\_{11} & \Sigma\_{12} \\
\Sigma\_{21} & \Sigma\_{22}
\end{array}\right] \\
&=\mathrm{E}\left[(x-\mu)(x-\mu)^{T}\right] \\
&=\mathrm{E}\left[\left(\begin{array}{c}
x\_{1}-\mu\_{1} \\
x\_{2}-\mu\_{2}
\end{array}\right)\left(\begin{array}{c}
x\_{1}-\mu\_{1} \\
x\_{2}-\mu\_{2}
\end{array}\right)^{T}\right] \\
&=\mathrm{E}\left[\begin{array}{c}
\left(x\_{1}-\mu\_{1}\right)\left(x\_{1}-\mu\_{1}\right)^{T} \\
\left(x\_{2}-\mu\_{2}\right)\left(x\_{1}-\mu\_{1}\right)^{T} & \left(x\_{2}-\mu\_{2}\right)\left(x\_{2}-\mu\_{2}\right)^{T}
\end{array}\right]
\end{aligned}\]

* Matching the upper-left subblocks in the matrices in the second and the last lines above gives the result. since marginal distributions of Gaussians are themselves Gaussian, we therefore have that the marginal distribution of \(x\_{1}\) is given by \(x\_{1} \sim \mathcal{N}\left(\mu\_{1}, \Sigma\_{11}\right)\). Also, we can ask, what is the conditional distribution of \(x\_{1}\) given \(x\_{2}\)? By referring to the definition of the multivariate Gaussian distribution, it can be shown that \(x\_{1} \mid x\_{2} \sim \mathcal{N}\left(\mu\_{1 \mid 2}, \Sigma\_{1 \mid 2}\right)\), where,

\[\mu\_{1 \mid 2} =\mu\_1+\Sigma\_{12} \Sigma\_{22}^{-1}\left(x\_2-\mu\_2\right)
\tag{1}\]
\[\Sigma\_{1 \mid 2} =\Sigma\_{11}-\Sigma\_{12} \Sigma\_{22}^{-1} \Sigma\_{21}
\tag{2}\]

* When working with the factor analysis model in the next section, these formulas for finding conditional and marginal distributions of Gaussians will be very useful.

## The Factor analysis model

* In the factor analysis model, we posit a joint distribution on \((x, z)\) as follows, where \(z \in \mathbb{R}^{k}\) is a latent random variable:

\[\begin{aligned}
z & \sim \mathcal{N}(0, I) \\
x \mid z & \sim \mathcal{N}(\mu+\Lambda z, \Psi)
\end{aligned}\]

* Here, the parameters of our model are the vector \(\mu \in \mathbb{R}^{n}\), the matrix \(\Lambda \in \mathbb{R}^{n \times k}\), and the diagonal matrix \(\Psi \in \mathbb{R}^{n \times n}\). The value of \(k\) is usually chosen to be smaller than \(n\).
* Thus, we imagine that each datapoint \(x^{(i)}\) is generated by sampling a \(k\) dimension multivariate Gaussian \(z^{(i)}\). Then, it is mapped to a \(k\)-dimensional affine space of \(\mathbb{R}^{n}\) by computing \(\mu+\Lambda z^{(i)}\). Lastly, \(x^{(i)}\) is generated by adding covariance \(\Psi\) noise to \(\mu+\Lambda z^{(i)}\).
* Equivalently, we can therefore also define the factor analysis model according to,

  \[\begin{array}{l}
  z \sim \mathcal{N}(0, I) \\
  \epsilon \sim \mathcal{N}(0, \Psi) \\
  x=\mu+\Lambda z+\epsilon
  \end{array}\]
  + where \(\epsilon\) and \(z\) are independent. Let’s work out exactly what distribution our model defines. Our random variables \(z\) and \(x\) have a joint Gaussian distribution.

\[\left[\begin{array}{l}
z \\
x
\end{array}\right] \sim \mathcal{N}\left(\mu\_{z x}, \Sigma\right)\]

* We will now find \(\mu\_{z x}\) and \(\Sigma\). We know that \(\mathrm{E}[z]=0\), from the fact that \(z \sim \mathcal{N}(0, I)\). Also, we have that,

\[\begin{aligned}
\mathrm{E}[x] &=\mathrm{E}[\mu+\Lambda z+\epsilon] \\
&=\mu+\Lambda \mathrm{E}[z]+\mathrm{E}[\epsilon] \\
&=\mu
\end{aligned}\]

* Putting these together, we obtain
  \(\mu\_{z x}=\left[\begin{array}{l}
  \overrightarrow{0} \\
  \mu
  \end{array}\right]\)
* Next, to find, \(\Sigma\), we need to calculate \(\Sigma\_{z z}=\mathrm{E}\left[(z-\mathrm{E}[z])(z-\mathrm{E}[z])^{T}\right]\) (the upper-left block of \(\Sigma\)), \(\Sigma\_{z x}=\mathrm{E}\left[(z-\mathrm{E}[z])(x-\mathrm{E}[x])^{T}\right]\) (upper-right block), and \(\Sigma\_{x x}=\mathrm{E}\left[(x-\mathrm{E}[x])(x-\mathrm{E}[x])^{T}\right]\) (lower-right block).
  Now, since \(z \sim \mathcal{N}(0, I)\), we easily find that \(\Sigma\_{z z}=\operatorname{Cov}(z)=I\). Also,

\[\begin{aligned}
\mathrm{E}\left[(z-\mathrm{E}[z])(x-\mathrm{E}[x])^{T}\right] &=\mathrm{E}\left[z(\mu+\Lambda z+\epsilon-\mu)^{T}\right] \\
&=\mathrm{E}\left[z z^{T}\right] \Lambda^{T}+\mathrm{E}\left[z \epsilon^{T}\right] \\
&=\Lambda^{T}
\end{aligned}\]

* In the last step, we used the fact that \(\mathrm{E}\left[z z^{T}\right]=\operatorname{Cov}(z)\) (since \(z\) has zero \(\operatorname{mean})\), and \(\mathrm{E}\left[z \epsilon^{T}\right]=\mathrm{E}[z] \mathrm{E}\left[\epsilon^{T}\right]=0\) (since \(z\) and \(\epsilon\) are independent, and hence the expectation of their product is the product of their expectations). Similarly, we can find \(\Sigma\_{x x}\) as follows:

\[\begin{aligned}
\mathrm{E}\left[(x-\mathrm{E}[x])(x-\mathrm{E}[x])^{T}\right] &=\mathrm{E}\left[(\mu+\Lambda z+\epsilon-\mu)(\mu+\Lambda z+\epsilon-\mu)^{T}\right] \\
&=\mathrm{E}\left[\Lambda z z^{T} \Lambda^{T}+\epsilon z^{T} \Lambda^{T}+\Lambda z \epsilon^{T}+\epsilon \epsilon^{T}\right] \\
&=\Lambda \mathrm{E}\left[z z^{T}\right] \Lambda^{T}+\mathrm{E}\left[\epsilon \epsilon^{T}\right] \\
&=\Lambda \Lambda^{T}+\Psi
\end{aligned}\]

* Putting everything together, we therefore have that,

\[\left[\begin{array}{l}
z \\
x
\end{array}\right] \sim \mathcal{N}\left(\left[\begin{array}{l}
\overrightarrow{0} \\
\mu
\end{array}\right],\left[\begin{array}{cc}
I & \Lambda^{T} \\
\Lambda & \Lambda \Lambda^{T}+\Psi
\end{array}\right]\right)
\tag{3}\]

* Hence, we also see that the marginal distribution of \(x\) is given by \(x \sim\) \(\mathcal{N}\left(\mu, \Lambda \Lambda^{T}+\Psi\right)\). Thus, given a training set \(\left\{x^{(i)} ; i=1, \ldots, m\right\}\), we can write down the log likelihood of the parameters:

\[\ell(\mu, \Lambda, \Psi)=\log \prod\_{i=1}^{m} \frac{1}{(2 \pi)^{n / 2}\left|\Lambda \Lambda^{T}+\Psi\right|^{1 / 2}} \exp \left(-\frac{1}{2}\left(x^{(i)}-\mu\right)^{T}\left(\Lambda \Lambda^{T}+\Psi\right)^{-1}\left(x^{(i)}-\mu\right)\right)\]

* To perform maximum likelihood estimation, we would like to maximize this quantity with respect to the parameters. But maximizing this formula explicitly is hard (try it yourself), and we are aware of no algorithm that does so in closed-form. So, we will instead use to the EM algorithm. In the next section, we derive EM for factor analysis.

## EM for factor analysis

* The derivation for the E-step is easy. We need to compute \(Q\_{i}\left(z^{(i)}\right)=\) \(P\left(z^{(i)} \mid x^{(i)} ; \mu, \Lambda, \Psi\right)\). By substituting the distribution given in Equation \((3)\) into the formulas \((1-2)\) used for finding the conditional distribution of a Gaussian, we find that \(z^{(i)} \mid x^{(i)} ; \mu, \Lambda, \Psi \sim \mathcal{N}\left(\mu\_{z^{(i)} \mid x^{(i)}}, \Sigma\_{z^{(i)} \mid x^{(i)}}\right)\), where,

\[\begin{aligned}
\mu\_{z^{(i)} \mid x^{(i)}} &=\Lambda^{T}\left(\Lambda \Lambda^{T}+\Psi\right)^{-1}\left(x^{(i)}-\mu\right) \\
\Sigma\_{z^{(i)} \mid x^{(i)}} &=I-\Lambda^{T}\left(\Lambda \Lambda^{T}+\Psi\right)^{-1} \Lambda
\end{aligned}\]

* So, using these definitions for \(\mu\_{z^{(i)} \mid x^{(i)}}\) and \(\Sigma\_{z^{(i)} \mid x^{(i)}}\), we have,

\[Q\_{i}\left(z^{(i)}\right)=\frac{1}{(2 \pi)^{k / 2}\left|\Sigma\_{z^{(i)} \mid x^{(i)}}\right|^{1 / 2}} \exp \left(-\frac{1}{2}\left(z^{(i)}-\mu\_{z^{(i)} \mid x^{(i)}}\right)^{T} \Sigma\_{z^{(i)} \mid x^{(i)}}^{-1}\left(z^{(i)}-\mu\_{z^{(i)} \mid x^{(i)}}\right)\right)\]

* Let’s now work out the M-step. Here, we need to maximize,

\[\sum\_{i=1}^{m} \int\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \mu, \Lambda, \Psi\right)}{Q\_{i}\left(z^{(i)}\right)} d z^{(i)}
\tag{4}\]

* with respect to the parameters \(\mu, \Lambda, \Psi\). We will work out only the optimization with respect to \(\Lambda\), and leave the derivations of the updates for \(\mu\) and \(\Psi\) as an exercise to the reader. We can simplify Equation \((4)\) as follows:

\[\sum\_{i=1}^{m} \int\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right)\left[\log P\left(x^{(i)} \mid z^{(i)} ; \mu, \Lambda, \Psi\right)+\log P\left(z^{(i)}\right)-\log Q\_{i}\left(z^{(i)}\right)\right] d z^{(i)}
\tag{5}\]
\[\quad=\sum\_{i=1}^{m} \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[\log P\left(x^{(i)} \mid z^{(i)} ; \mu, \Lambda, \Psi\right)+\log P\left(z^{(i)}\right)-\log Q\_{i}\left(z^{(i)}\right)\right]
\tag{6}\]

* Here, the “ \(z^{(i)} \sim Q\_{i}\) “ subscript indicates that the expectation is with respect to \(z^{(i)}\) drawn from \(Q\_{i}\). In the subsequent development, we will omit this subscript when there is no risk of ambiguity. Dropping terms that do not depend on the parameters, we find that we need to maximize:

\[\begin{array}{l}
\sum\_{i=1}^{m} \mathrm{E}\left[\log P\left(x^{(i)} \mid z^{(i)} ; \mu, \Lambda, \Psi\right)\right] \\
=\sum\_{i=1}^{m} \mathrm{E}\left[\log \frac{1}{(2 \pi)^{n / 2}|\Psi|^{1 / 2}} \exp \left(-\frac{1}{2}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)^{T} \Psi^{-1}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)\right)\right] \\
=\sum\_{i=1}^{m} \mathrm{E}\left[-\frac{1}{2} \log |\Psi|-\frac{n}{2} \log (2 \pi)-\frac{1}{2}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)^{T} \Psi^{-1}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)\right]
\end{array}\]

* Let’s maximize this with respect to \(\Lambda\). Only the last term above depends on \(\Lambda\). Taking derivatives, and using the facts that \(\operatorname{tr} a=a\) (for \(a \in \mathbb{R}\)), \(\operatorname{tr} A B=\operatorname{tr} B A\), and \(\nabla\_{A} \operatorname{tr} A B A^{T} C=C A B+C^{T} A B\), we get:

\[\begin{aligned}
\nabla\_{\Lambda} \sum\_{i=1}^{m}-\mathrm{E}\left[\frac{1}{2}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)^{T} \Psi^{-1}\left(x^{(i)}-\mu-\Lambda z^{(i)}\right)\right] \\
&= \sum\_{i=1}^{m} \nabla\_{\Lambda} \mathrm{E}\left[-\operatorname{tr} \frac{1}{2} z^{(i)^{T}} \Lambda^{T} \Psi^{-1} \Lambda z^{(i)}+\operatorname{tr} z^{(i)^{T}} \Lambda^{T} \Psi^{-1}\left(x^{(i)}-\mu\right)\right] \\
&= \sum\_{i=1}^{m} \nabla\_{\Lambda} \mathrm{E}\left[-\operatorname{tr} \frac{1}{2} \Lambda^{T} \Psi^{-1} \Lambda z^{(i)} z^{(i)^{T}}+\operatorname{tr} \Lambda^{T} \Psi^{-1}\left(x^{(i)}-\mu\right) z^{(i)^{T}}\right] \\
&= \sum\_{i=1}^{m} \mathrm{E}\left[-\Psi^{-1} \Lambda z^{(i)} z^{(i)^{T}}+\Psi^{-1}\left(x^{(i)}-\mu\right) z^{(i)^{T}}\right]
\end{aligned}\]

* Setting this to zero and simplifying, we get:

\[\sum\_{i=1}^{m} \Lambda \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)} z^{(i)^{T}}\right]=\sum\_{i=1}^{m}\left(x^{(i)}-\mu\right) \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)^{T}}\right]\]

* Hence, solving for \(\Lambda\), we obtain

\[\Lambda=\left(\sum\_{i=1}^{m}\left(x^{(i)}-\mu\right) \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)^{T}}\right]\right)\left(\sum\_{i=1}^{m} \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)} z^{(i)^{T}}\right]\right)^{-1}
\tag{7}\]

* It is interesting to note the close relationship between this equation and the normal equation that we’d derived for least squares regression,

\[\theta^{T}=\left(y^{T} X\right)\left(X^{T} X\right)^{-1}\]

* The analogy is that here, the \(x\)’s are a linear function of the \(z\)’s (plus noise). Given the “guesses” for \(z\) that the E-step has found, we will now try to estimate the unknown linearity \(\Lambda\) relating the \(x\)’s and \(z\)’s. It is therefore no surprise that we obtain something similar to the normal equation. There is, however, one important difference between this and an algorithm that performs least squares using just the “best guesses” of the \(z\)’s; we will see this difference shortly.
* To complete our M-step update, let’s work out the values of the expectations in Equation \((7)\). From our definition of \(Q\_{i}\) being Gaussian with mean \(\mu\_{z^{(i)} \mid x^{(i)}}\) and covariance \(\Sigma\_{z^{(i)} \mid x^{(i)}}\), we easily find,

\[\begin{aligned}
\mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)^{T}}\right] &=\mu\_{z^{(i)} \mid x^{(i)}}^{T} \\
\mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[z^{(i)} z^{(i)^{T}}\right] &=\mu\_{z^{(i)} \mid x^{(i)}} \mu\_{z^{(i)} \mid x^{(i)}}^{T}+\Sigma\_{z^{(i)} \mid x^{(i)}}
\end{aligned}\]

* The latter comes from the fact that, for a random variable \(Y, \operatorname{Cov}(Y)=\) \(\mathrm{E}\left[Y Y^{T}\right]-\mathrm{E}[Y] \mathrm{E}[Y]^{T}\), and hence \(\mathrm{E}\left[Y Y^{T}\right]=\mathrm{E}[Y] \mathrm{E}[Y]^{T}+\operatorname{Cov}(Y)\). Substituting this back into Equation \((7)\), we get the M-step update for \(\Lambda\):

\[\Lambda=\left(\sum\_{i=1}^{m}\left(x^{(i)}-\mu\right) \mu\_{z^{(i)} \mid x^{(i)}}^{T}\right)\left(\sum\_{i=1}^{m} \mu\_{z^{(i)} \mid x^{(i)}} \mu\_{z^{(i)} \mid x^{(i)}}^{T}+\Sigma\_{z^{(i)} \mid x^{(i)}}\right)^{-1}
\tag{8}\]

* It is important to note the presence of the \(\Sigma\_{z^{(i)} \mid x^{(i)}}\) on the right hand side of this equation. This is the covariance in the posterior distribution \(P\left(z^{(i)} \mid x^{(i)}\right)\) of \(z^{(i)}\) give \(x^{(i)}\), and the M-step must take into account this uncertainty about \(z^{(i)}\) in the posterior. A common mistake in deriving EM is to assume that in the E-step, we need to calculate only expectation \(E[z]\) of the latent random variable \(z\), and then plug that into the optimization in the M-step everywhere \(z\) occurs. While this worked for simple problems such as the mixture of Gaussians, in our derivation for factor analysis, we needed \(E\left[z z^{T}\right]\) as well \(\mathrm{E}[z]\); and as we saw, \(E\left[z z^{T}\right]\) and \(\mathrm{E}[z] \mathrm{E}[z]^{T}\) differ by the quantity \(\Sigma\_{z \mid x}\). Thus, the M-step update must take into account the covariance of \(z\) in the posterior distribution \(P\left(z^{(i)} \mid x^{(i)}\right)\).
* Lastly, we can also find the M-step optimizations for the parameters \(\mu\) and \(\Psi\). It is not hard to show that the first is given by,

\[\mu=\frac{1}{m} \sum\_{i=1}^{m} x^{(i)}\]

* since this doesn’t change as the parameters are varied (i.e., unlike the update for \(\Lambda\), the right hand side does not depend on \(Q\_{i}\left(z^{(i)}\right)=P\left(z^{(i)} \mid x^{(i)} ; \mu, \Lambda, \Psi\right)\) which in turn depends on the parameters), this can be calculated just once and needs not be further updated as the algorithm is run. Similarly, the diagonal \(\Psi\) can be found by calculating,

\[\Phi=\frac{1}{m} \sum\_{i=1}^{m} x^{(i)} x^{(i)^{T}}-x^{(i)} \mu\_{z^{(i)} \mid x^{(i)}}^{T} \Lambda^{T}-\Lambda \mu\_{z^{(i)} \mid x^{(i)}} x^{(i)^{T}}+\Lambda\left(\mu\_{z^{(i)} \mid x^{(i)}} \mu\_{z^{(i)} \mid x^{(i)}}^{T}+\Sigma\_{z^{(i)} \mid x^{(i)}}\right) \Lambda^{T}\]

* and setting \(\Psi\_{i i}=\Phi\_{i i}\) (i.e., letting \(\Psi\) be the diagonal matrix containing only the diagonal entries of \(\Phi\)).

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledFactorAnalysis,
  title   = {Factor Analysis},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
