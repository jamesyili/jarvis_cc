# CS229 • Expectation Maximization Algorithms

**Source:** https://aman.ai/cs229/expectation-maximization/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Expectation Maximization Algorithms](#expectation-maximization-algorithms)
  + [Jensen’s inequality](#jensens-inequality)
  + [Theorem](#theorem)
* [The EM algorithm](#the-em-algorithm)
  + [Remarks](#remarks)
* [Mixture of Gaussians revisited](#mixture-of-gaussians-revisited)
* [Mixtures of Gaussians](#mixtures-of-gaussians)
* [References](#references)
* [Citation](#citation)

## Expectation Maximization Algorithms

* In the previous set of notes, we talked about the EM algorithm as applied to fitting a mixture of Gaussians. In this section, we give a broader view of the EM algorithm, and show how it can be applied to a large family of estimation problems with latent variables. We begin our discussion with a very useful result called Jensen’s inequality

### Jensen’s inequality

* Let \(f\) be a function whose domain is the set of real numbers. Recall that \(f\) is a convex function if \(f^{\prime \prime}(x) \geq 0\) (for all \(\left.x \in \mathbb{R}\right)\). In the case of \(f\) taking vector-valued inputs, this is generalized to the condition that its hessian \(H\) is positive semi-definite \((H \geq 0)\). If \(f^{\prime \prime}(x)>0\) for all \(x\), then we say \(f\) is strictly convex (in the vector-valued case, the corresponding statement is that \(H\) must be positive definite, written \(H>0\)). Jensen’s inequality can then be stated as follows:

### Theorem

* Let \(f\) be a convex function, and let \(X\) be a random variable. Then:

\[\mathrm{E}[f(X)] \geq f(\mathrm{E} X)\]

* Moreover, if \(f\) is strictly convex, then \(\mathrm{E}[f(X)]=f(\mathrm{E} X)\) holds true if and only if \(X=\mathrm{E}[X]\) with probability 1 (i.e., if \(X\) is a constant).
* Recall our convention of occasionally dropping the parentheses when writing expectations, so in the theorem above, \(f(\mathrm{E} X)=f(\mathrm{E}[X])\). For an interpretation of the theorem, consider the figure below.

* Here, \(f\) is a convex function shown by the solid line. Also, \(X\) is a random variable that has a 0.5 chance of taking the value \(a\), and a 0.5 chance of taking the value \(b\) (indicated on the \(x\) -axis). Thus, the expected value of \(X\) is given by the midpoint between \(a\) and \(b\).
* We also see the values \(f(a), f(b)\) and \(f(\mathrm{E}[X])\) indicated on the \(y\) -axis. Morcover, the value \(\mathrm{E}[f(X)]\) is now the midpoint on the \(y\) -axis between \(f(a)\) and \(f(b)\). From our example, we see that because \(f\) is convex, it must be the case that \(\mathrm{E}[f(X)] \geq f(\mathrm{E} X)\).
* Incidentally, quite a lot of people have trouble remembering which way the inequality goes, and remembering a picture like this is a good way to quickly figure out the answer. Remark. Recall that \(f\) is strictly concave if and only if \(-f\) is strictly convex (i.e., \(f^{\prime \prime}(x) \leq 0\) or \(H \leq 0\)). Jensen’s inequality also holds for concave functions \(f\), but with the direction of all the inequalities reversed \((\mathrm{E}[f(X)] \leq\) \(f(\mathrm{E} X)\), etc.).

## The EM algorithm

* Suppose we have an estimation problem in which we have a training set \(\left\{x^{(1)}, \ldots, x^{(m)}\right\}\) consisting of \(m\) independent examples. We wish to fit the parameters of a model \(P(x, z)\) to the data, where the likelihood is given by,

\[\begin{aligned}
\ell(\theta) &=\sum\_{i=1}^{m} \log P(x ; \theta) \\
&=\sum\_{i=1}^{m} \log \sum\_{z} P(x, z ; \theta)
\end{aligned}\]

* But, explicitly finding the maximum likelihood estimates of the parameters \(\theta\) may be hard. Here, the \(z^{(i)}\)’s are the latent random variables; and it is often the case that if the \(z^{(i)}\)’s were observed, then maximum likelihood estimation would be easy.
* In such a setting, the EM algorithm gives an efficient method for maximum likelihood estimation. Maximizing \(\ell(\theta)\) explicitly might be difficult, and our strategy will be to instead repeatedly construct a lower-bound on \(\ell\) (E-step), and then optimize that lower-bound (M-step).
* For each \(i\), let \(Q\_{i}\) be some distribution over the \(z\)’s \(\left(\sum\_{z} Q\_{i}(z)=1, Q\_{i}(z) \geq 0 \right)\). Consider the following:

\[\sum\_{i} \log P\left(x^{(i)} ; \theta\right)=\sum\_{i} \log \sum\_{z^{(i)}} P\left(x^{(i)}, z^{(i)} ; \theta\right)\tag{1}\]
\[=\sum\_{i} \log \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\tag{2}\]
\[\geq \sum\_{i} \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\tag{3}\]

* Note that if \(z\) were continuous, then \(Q\_{i}\) would be a density, and the summations over \(z\) in our discussion are replaced with integrals over \(z\).
* The last step of this derivation used Jensen’s inequality. Specifically, \(f(x)=\) \(\log x\) is a concave function, since \(f^{\prime \prime}(x)=-1 / x^{2}<0\) over its domain \(x \in \mathbb{R}^{+}\). Also, the term in the summation (below) is just an expectation of the quantity \(\left[\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\right]\) with respect to \(z^{(i)}\) drawn according to the distribution given by \(Q\_{i}\).

\[\sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right)\left[\frac{P\left(x^{(i)}, z^{(i)}; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\right]\]

* By Jensen’s inequality, we have,

  \[f\left(\mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\right]\right) \geq \mathrm{E}\_{z^{(i)} \sim Q\_{i}}\left[f\left(\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\right)\right]\]
  + where the \(“z^{(i)} \sim Q\_{i}”\) subscripts above indicate that the expectations are with respect to \(z^{(i)}\) drawn from \(Q\_{i}\). This allowed us to go from Equation \((2)\) to Equation \((3)\).
* Now, for any set of distributions \(Q\_{i}\), the Equation \((3)\) gives a lower-bound on \(\ell(\theta)\). There are many possible choices for the \(Q\_{i}\)’s. Which should we choose? Well, if we have some current guess \(\theta\) of the parameters, it seems natural to try to make the lower-bound tight at that value of \(\theta\), i.e., we’ll make the inequality above hold with equality at our particular value of \(\theta\). (We’ll see later how this enables us to prove that \(\ell(\theta)\) increases monotonically with successive iterations of EM.)
* To make the bound tight for a particular value of \(\theta\), we need for the step involving Jensen’s inequality in our derivation above to hold with equality. For this to be true, we know it is sufficient that that the expectation be taken over a “constant”-valued random variable, i.e., we require that,

\[\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}=c\]

* for some constant \(c\) that does not depend on \(z^{(i)}\). This is easily accomplished by choosing,

\[Q\_{i}\left(z^{(i)}\right) \propto P\left(x^{(i)}, z^{(i)} ; \theta\right)\]

* Actually, since we know \(\sum\_{z} Q\_{i}\left(z^{(i)}\right)=1\) (because it is a distribution), this further tells us that,

\[\begin{aligned}
Q\_{i}\left(z^{(i)}\right) &=\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{\sum\_{z} P\left(x^{(i)}, z ; \theta\right)} \\
&=\frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{P\left(x^{(i)} ; \theta\right)} \\
&=P\left(z^{(i)} \mid x^{(i)} ; \theta\right)
\end{aligned}\]

* Thus, we simply set the \(Q\_{i}\)’s to be the posterior distribution of the \(z^{(i)}\)’s given \(x^{(i)}\) and the setting of the parameters \(\theta\).
* Now, for this choice of the \(Q\_{i}\)’s, Equation \((3)\) gives a lower-bound on the loglikelihood \(\ell\) that we’re trying to maximize. This is the E-step. In the M-step of the algorithm, we then maximize our formula in Equation \((3)\) with respect to the parameters to obtain a new setting of the \(\theta\)’s. Repeatedly carrying out these two steps gives us the EM algorithm, which is as follows:
  + Repeat until convergence:
    - (E-step) For each \(i\), set,\[Q\_{i}\left(z^{(i)}\right):=P\left(z^{(i)} \mid x^{(i)} ; \theta\right)\]
    - (M-step) Set,\[\theta:=\operatorname\*{arg\,max}\_{\theta} \sum\_{i} \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\]
* How we we know if this algorithm will converge? Well, suppose \(\theta^{(t)}\) and \(\theta^{(t+1)}\) are the parameters from two successive iterations of EM. We will now prove that \(\ell\left(\theta^{(t)}\right) \leq \ell\left(\theta^{(t+1)}\right)\), which shows EM always monotonically improves the log-likelihood. The key to showing this result lies in our choice of the \(Q\_{i}\)’s. Specifically, on the iteration of \(\mathrm{EM}\) in which the parameters had started out as \(\theta^{(t)}\), we would have chosen \(Q\_{i}^{(t)}\left(z^{(i)}\right):=P\left(z^{(i)} \mid x^{(i)} ; \theta^{(t)}\right)\). We saw earlier that this choice ensures that Jensen’s inequality, as applied to get Equation \((3)\), holds with equality, and hence,

\[\ell\left(\theta^{(t)}\right)=\sum\_{i} \sum\_{z^{(i)}} Q\_{i}^{(t)}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta^{(t)}\right)}{Q\_{i}^{(t)}\left(z^{(i)}\right)}\]

* The parameters \(\theta^{(t+1)}\) are then obtained by maximizing the right hand side of the equation above. Thus,

\[\ell\left(\theta^{(t+1)}\right) \geq \sum\_{i} \sum\_{z^{(i)}} Q\_{i}^{(t)}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta^{(t+1)}\right)}{Q\_{i}^{(t)}\left(z^{(i)}\right)}\
\tag{4}\]
\[\geq \sum\_{i} \sum\_{z^{(i)}} Q\_{i}^{(t)}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta^{(t)}\right)}{Q\_{i}^{(t)}\left(z^{(i)}\right)}
\tag{5}\]
\[=\ell\left(\theta^{(t)}\right)
\tag{6}\]

* This first inequality comes from the fact that,

\[\ell(\theta) \geq \sum\_{i} \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\]

* holds for any values of \(Q\_{i}\) and \(\theta\), and in particular holds for \(Q\_{i}=Q\_{i}^{(t)}\) \(\theta=\theta^{(t+1)}\). To get Equation \((5)\), we used the fact that \(\theta^{(t+1)}\) is chosen explicitly to be,

\[\operatorname\*{arg\,max}\_{\theta} \sum\_{i} \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\]

* and thus this formula evaluated at \(\theta^{(t+1)}\) must be equal to or larger than the same formula evaluated at \(\theta^{(t)}\). Finally, the step used to get Equation \((6)\) was shown earlier, and follows from \(Q\_{i}^{(t)}\) having been chosen to make Jensen’s inequality hold with equality at \(\theta^{(t)}\).
* Hence, EM causes the likelihood to converge monotonically. In our description of the EM algorithm, we said we’d run it until convergence. Given the result that we just showed, one reasonable convergence test would be to check if the increase in \(\ell(\theta)\) between successive iterations is smaller than some tolerance parameter, and to declare convergence if \(\mathrm{EM}\) is improving \(\ell(\theta)\) too slowly.

### Remarks

* If we define,

\[J(Q, \theta)=\sum\_{i} \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q\_{i}\left(z^{(i)}\right)}\]

* then we know \(\ell(\theta) \geq J(Q, \theta)\) from our previous derivation. The EM can also be viewed a coordinate ascent on \(J\), in which the E-step maximizes it with respect to \(Q\) (check this yourself), and the M-step maximizes it with respect to \(\theta\).

## Mixture of Gaussians revisited

* Armed with our general definition of the EM algorithm, let’s go back to our old example of fitting the parameters \(\phi, \mu\) and \(\Sigma\) in a mixture of Gaussians. For the sake of brevity, we carry out the derivations for the M-step updates only for \(\phi\) and \(\mu\_{j}\), and leave the updates for \(\Sigma\_{j}\) as an exercise for the reader. The E-step is easy. Following our algorithm derivation above, we simply calculate,

\[w\_{j}^{(i)}=Q\_{i}\left(z^{(i)}=j\right)=P\left(z^{(i)}=j \mid x^{(i)} ; \phi, \mu, \Sigma\right)\]

* Here, \(“Q\_{i}\left(z^{(i)}=j\right)”\) denotes the probability of \(z^{(i)}\) taking the value \(j\) under the distribution \(Q\_{i}\).
* Next, in the M-step, we need to maximize, with respect to our parameters \(\phi, \mu, \Sigma\), the quantity,

\[\begin{aligned}
\sum\_{i=1}^{m} & \sum\_{z^{(i)}} Q\_{i}\left(z^{(i)}\right) \log \frac{P\left(x^{(i)}, z^{(i)} ; \phi, \mu, \Sigma\right)}{Q\_{i}\left(z^{(i)}\right)} \\
&=\sum\_{i=1}^{m} \sum\_{j=1}^{k} Q\_{i}\left(z^{(i)}=j\right) \log \frac{P\left(x^{(i)} \mid z^{(i)}=j ; \mu, \Sigma\right) P\left(z^{(i)}=j ; \phi\right)}{Q\_{i}\left(z^{(i)}=j\right)} \\
&=\sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)} \log \frac{\frac{1}{(2 \pi)^{n / 2}\left|\Sigma\_{j}\right|^{1 / 2}} \exp \left(-\frac{1}{2}\left(x^{(i)}-\mu\_{j}\right)^{T} \Sigma\_{j}^{-1}\left(x^{(i)}-\mu\_{j}\right)\right) \cdot \phi\_{j}}{w\_{j}^{(i)}}
\end{aligned}\]

* Let’s maximize this with respect to \(\mu\_{l}\). If we take the derivative with respect to \(\mu\_{l}\), we find,

\[\begin{aligned}
\nabla\_{\mu\_{l}} & \sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)} \log \frac{\frac{1}{(2 \pi)^{n / 2}\left|\Sigma\_{j}\right|^{1 / 2}} \exp \left(-\frac{1}{2}\left(x^{(i)}-\mu\_{j}\right)^{T} \Sigma\_{j}^{-1}\left(x^{(i)}-\mu\_{j}\right)\right) \cdot \phi\_{j}}{w\_{j}^{(i)}} \\
&=-\nabla\_{\mu\_{l}} \sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)} \frac{1}{2}\left(x^{(i)}-\mu\_{j}\right)^{T} \Sigma\_{j}^{-1}\left(x^{(i)}-\mu\_{j}\right) \\
&=\frac{1}{2} \sum\_{i=1}^{m} w\_{l}^{(i)} \nabla\_{\mu\_{l}} 2 \mu\_{l}^{T} \Sigma\_{l}^{-1} x^{(i)}-\mu\_{l}^{T} \Sigma\_{l}^{-1} \mu\_{l} \\
&=\sum\_{i=1}^{m} w\_{l}^{(i)}\left(\Sigma\_{l}^{-1} x^{(i)}-\Sigma\_{l}^{-1} \mu\_{l}\right)
\end{aligned}\]

* Setting this to zero and solving for \(\mu\_{l}\) therefore yields the update rule,

\[\mu\_{l}:=\frac{\sum\_{i=1}^{m} w\_{l}^{(i)} x^{(i)}}{\sum\_{i=1}^{m} w\_{l}^{(i)}}\]

* which was what we had in the previous set of notes. Let’s do one more example, and derive the M-step update for the parameters \(\phi\_{j}\). Grouping together only the terms that depend on \(\phi\_{j}\), we find that we need to maximize,

\[\sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)} \log \phi\_{j}\]

* However, there is an additional constraint that the \(\phi\_{j}\)’s sum to 1, since they represent the probabilities \(\phi\_{j}=P\left(z^{(i)}=j ; \phi\right)\). To deal with the constraint that \(\sum\_{j=1}^{k} \phi\_{j}=1\), we construct the Lagrangian,

  \[\mathcal{L}(\phi)=\sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)} \log \phi\_{j}+\beta\left(\sum\_{j=1}^{k} \phi\_{j}-1\right)\]
  + where \(\beta\) is the Lagrange multiplier. We don’t need to worry about the constraint that \(\phi\_{j} \geq 0\), because as we’ll shortly see, the solution we’ll find from this derivation will automatically satisfy that anyway.
* Taking derivatives, we get,

\[\frac{\partial}{\partial \phi\_{j}} \mathcal{L}(\phi)=\sum\_{i=1}^{m} \frac{w\_{j}^{(i)}}{\phi\_{j}}+1\]

* Setting this to zero and solving, we get,

\[\phi\_{j}=\frac{\sum\_{i=1}^{m} w\_{j}^{(i)}}{-\beta}\]

* i.e., \(\phi\_{j} \propto \sum\_{i=1}^{m} w\_{j}^{(i)}\). Using the constraint that \(\sum\_{j} \phi\_{j}=1\), we easily find that \(-\beta=\sum\_{i=1}^{m} \sum\_{j=1}^{k} w\_{j}^{(i)}=\sum\_{i=1}^{m} 1=m\). (This used the fact that \(w\_{j}^{(i)}=\) \(Q\_{i}\left(z^{(i)}=j\right)\), and since probabilities sum to \(1, \sum\_{j} w\_{j}^{(i)}=1\).) We therefore have our M-step updates for the parameters \(\phi\_{j}\):

\[\phi\_{j}:=\frac{1}{m} \sum\_{i=1}^{m} w\_{j}^{(i)}\]

* The derivation for the M-step updates to \(\Sigma\_{j}\) are also entirely straightforward.

## Mixtures of Gaussians

* In this section, we discuss the EM (Expectation-Maximization) algorithm for density estimation, as applied to fitting a mixture of Gaussians.
* Suppose that we are given a training set \(\left\{x^{(1)}, \ldots, x^{(m)}\right\}\) as usual. Since we are in the unsupervised learning setting, these points do not come with any labels.
* We wish to model the data by specifying a joint distribution \(P\left(x^{(i)}, z^{(i)}\right)=\) \(P\left(x^{(i)} \mid z^{(i)}\right) P\left(z^{(i)}\right)\). Here, \(z^{(i)} \sim\) Multinomial \((\phi)\) (where \(\phi\_{j} \geq 0, \sum\_{j=1}^{k} \phi\_{j}=1\).
  and the parameter \(\phi\_{j}\) gives \(P\left(z^{(i)}=j\right)\), and \(x^{(i)} \mid z^{(i)}=j \sim \mathcal{N}\left(\mu\_{j}, \Sigma\_{j}\right)\). We let \(k\) denote the number of values that the \(z^{(i)}\)’s can take on. Thus, our model posits that each \(x^{(i)}\) was generated by randomly choosing \(z^{(i)}\) from \(\{1, \ldots, k\}\), and then \(x^{(i)}\) was drawn from one of \(k\) Gaussians depending on \(z^{(i)}\). This is called the mixture of Gaussians model. Also, note that the \(z^{(i)}\)’s are latent random variables, meaning that they’re hidden/unobserved. This is what will make our estimation problem difficult.
* The parameters of our model are thus \(\phi, \mu\) and \(\Sigma\). To estimate them, we can write down the likelihood of our data:

\[\begin{aligned}
\ell(\phi, \mu, \Sigma) &=\sum\_{i=1}^{m} \log P\left(x^{(i)} ; \phi, \mu, \Sigma\right) \\
&=\sum\_{i=1}^{m} \log \sum\_{z^{(i)}=1}^{k} P\left(x^{(i)} \mid z^{(i)} ; \mu, \Sigma\right) P\left(z^{(i)} ; \phi\right)
\end{aligned}\]

* However, if we set to zero the derivatives of this formula with respect to the parameters and try to solve, we’ll find that it is not possible to find the maximum likelihood estimates of the parameters in closed form. (Try this yourself at home.)
* The random variables \(z^{(i)}\) indicate which of the \(k\) Gaussians each \(x^{(i)}\) had come from. Note that if we knew what the \(z^{(i)}\)’s were, the maximum likelihood problem would have been easy. Specifically, we could then write down the likelihood as

\[\ell(\phi, \mu, \Sigma)=\sum\_{i=1}^{m} \log P\left(x^{(i)} \mid z^{(i)} ; \mu, \Sigma\right)+\log P\left(z^{(i)} ; \phi\right)\]

* Maximizing this with respect to \(\phi, \mu\) and \(\Sigma\) gives the parameters:

\[\begin{aligned}
\phi\_{j} &=\frac{1}{m} \sum\_{i=1}^{m} 1\left\{z^{(i)}=j\right\} \\
\mu\_{j} &=\frac{\sum\_{i=1}^{m} 1\left\{z^{(i)}=j\right\} x^{(i)}}{\sum\_{i=1}^{m} 1\left\{z^{(i)}=j\right\}} \\
\Sigma\_{j} &=\frac{\sum\_{i=1}^{m} 1\left\{z^{(i)}=j\right\}\left(x^{(i)}-\mu\_{j}\right)\left(x^{(i)}-\mu\_{j}\right)^{T}}{\sum\_{i=1}^{m} 1\left\{z^{(i)}=j\right\}}
\end{aligned}\]

* Indeed, we see that if the \(z^{(i)}\)’s were known, then maximum likelihood estimation becomes nearly identical to what we had when estimating the parameters of the Gaussian discriminant analysis model, except that here the \(z^{(i)}\)’s playing the role of the class labels.
  + There are other minor differences in the formulas here from what we’d obtained in PS1 with Gaussian discriminant analysis, first because we’ve generalized the \(z^{(i)}\)’s to be multinomial rather than Bernoulli, and second because here we are using a different \(\Sigma\_{j}\) for each Gaussian.
* However, in our density estimation problem, the \(z^{(i)}\)’s are not known. What can we do?
* The EM algorithm is an iterative algorithm that has two main steps. Applied to our problem, in the E-step, it tries to “guess” the values of the \(z^{(i)}\)’s. In the M-step, it updates the parameters of our model based on our guesses. since in the M-step we are pretending that the guesses in the first part were correct, the maximization becomes easy. Here’s the algorithm:
  + Repeat until convergence:
    - (E-step) For each \(i, j\), set,\[w\_{j}^{(i)}:=P\left(z^{(i)}=j \mid x^{(i)} ; \phi, \mu, \Sigma\right)\]
    - (M-step) Update the parameters:\[\begin{aligned}
    \phi\_{j} &:=\frac{1}{m} \sum\_{i=1}^{m} w\_{j}^{(i)} \\
    \mu\_{j} &:=\frac{\sum\_{i=1}^{m} w\_{j}^{(i)} x^{(i)}}{\sum\_{i=1}^{m} w\_{j}^{(i)}} \\
    \Sigma\_{j} &:=\frac{\sum\_{i=1}^{m} w\_{j}^{(i)}\left(x^{(i)}-\mu\_{j}\right)\left(x^{(i)}-\mu\_{j}\right)^{T}}{\sum\_{i=1}^{m} w\_{j}^{(i)}}
    \end{aligned}\]
* In the E-step, we calculate the posterior probability of our parameters the \(z^{(i)}\)’s, given the \(x^{(i)}\) and using the current setting of our parameters, i.e.,, using Bayes rule, we obtain:

\[P\left(z^{(i)}=j \mid x^{(i)} ; \phi, \mu, \Sigma\right)=\frac{P\left(x^{(i)} \mid z^{(i)}=j ; \mu, \Sigma\right) P\left(z^{(i)}=j ; \phi\right)}{\sum\_{l=1}^{k} P\left(x^{(i)} \mid z^{(i)}=l ; \mu, \Sigma\right) P\left(z^{(i)}=l ; \phi\right)}\]

* Here, \(P\left(x^{(i)} \mid z^{(i)}=j ; \mu, \Sigma\right)\) is given by evaluating the density of a Gaussian with mean \(\mu\_{j}\) and covariance \(\Sigma\_{j}\) at \(x^{(i)} ; P\left(z^{(i)}=j ; \phi\right)\) is given by \(\phi\_{j}\), and so on. The values \(w\_{j}^{(i)}\) calculated in the E-step represent our “soft” guesses for the values of \(z^{(i)}\).
  + The term “soft” refers to our guesses being probabilities and taking values in \([0,1]\); in contrast, a “hard” guess is one that represents a single best guess (such as taking values \(\operatorname{in}{0,1}\) or \({1, \ldots, k})\).
* Also, you should contrast the updates in the M-step with the formulas we had when the \(z^{(i)}\)’s were known exactly. They are identical, except that instead of the indicator functions \(“ 1\left\{z^{(i)}=j\right\} “\) indicating from which Gaussian each datapoint had come, we now instead have the \(w\_{j}^{(i)}\)’s.
* The EM-algorithm is also reminiscent of the K-means clustering algorithm, except that instead of the “hard” cluster assignments \(c(i)\), we instead have the “soft” assignments \(w\_{j}^{(i)}\). Similar to K-means, it is also susceptible to local optima, so reinitializing at several different initial parameters may be a good idea.
* It’s clear that the EM algorithm has a very natural interpretation of repeatedly trying to guess the unknown \(z^{(i)}\)’s; but how did it come about, and can we make any guarantees about it, such as regarding its convergence? In the next set of notes, we will describe a more general view of \(\mathrm{EM}\), one that will allow us to easily apply it to other estimation problems in which there are also latent variables, and which will allow us to give a convergence guarantee.

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledExpectationMaximizationAlgorithms,
  title   = {Expectation Maximization Algorithms},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
