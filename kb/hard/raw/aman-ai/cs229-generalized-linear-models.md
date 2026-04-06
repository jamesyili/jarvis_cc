# CS229 • Generalized Linear Models

**Source:** https://aman.ai/cs229/glm/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Overview](#overview)
* [The exponential family](#the-exponential-family)
  + [Bernoulli distribution](#bernoulli-distribution)
  + [Gaussian distribution](#gaussian-distribution)
  + [Other members of the exponential family](#other-members-of-the-exponential-family)
  + [Distributions and their use-cases](#distributions-and-their-use-cases)
  + [(Desirable) properties of the exponential family](#desirable-properties-of-the-exponential-family)
* [Generalized Linear Models (GLMs)](#generalized-linear-models-glms)
  + [The beauty of GLMs: update rule](#the-beauty-of-glms-update-rule)
  + [Terminology](#terminology)
  + [Parameter spaces](#parameter-spaces)
* [Constructing GLMs](#constructing-glms)
  + [Linear regression](#linear-regression)
  + [Logistic regression](#logistic-regression)
  + [Softmax regression](#softmax-regression)
* [Graphical intuition](#graphical-intuition)
  + [Regression](#regression)
  + [Classification](#classification)
  + [Softmax regression](#softmax-regression-1)
* [Further reading](#further-reading)
* [References](#references)
* [Citation](#citation)

## Overview

* In our discussion of [linear regression](../linear-regression), we had \(y \mid x; \theta \sim \mathcal{N}(\mu, \sigma^{2})\), while in [logistic regression](../logistic-regression), \(y \mid x ; \theta \sim \operatorname{Bernoulli} (\phi)\), for some appropriate definitions of \(\mu\) and \(\phi\) as functions of \(x\) and \(\theta\).
* In this topic, we will show that both of these methods are special cases of a broader family of models, called **Generalized Linear Models (GLMs)**. We will also show how other models in the GLM family can be derived and applied to other classification and regression problems.

## The exponential family

* To work our way up to GLMs, we will begin by defining exponential family distributions. We say that a class of distributions is in the exponential family if their probability density function (PDF) can be written in the form:

  \[P(y ; \eta)=b(y) \exp \left(\eta^{T} T(y)-a(\eta)\right)
  \tag{1}\]
  + where,
    - \(y\) is the data that probability distribution given by equation \((1)\) is trying to model. Note that we use exponential families to model the output of your model in a supervised learning setting (note that when we move over to GLMs, we’ll be dealing with \(x\)).
    - \(\eta\) is called the **natural parameter** (also called the **canonical parameter** of the distribution).
    - \(T(y)\) is called the sufficient statistic (for the distributions we’ll be considering, it will often be the case that \(T(y)=y\)).
    - \(b(y)\) is called the base measure.
    - \(a(\eta)\) is called the log partition function.
      * The reason why \(a(\eta)\) is called the log partition function by rewriting equation \((1)\) as \(P(y ; \eta)=b(y) \frac{exp(\eta^{T} T(y))}{exp(a(\eta))}\). Because the quantity \(e^{-a(\eta)}\) essentially plays the role of a normalization constant, that makes sure the distribution \(P(y ; \eta)\) integrates over \(y\) to 1. The log of the denominator in this equation is \(a(\eta)\), hence the name.
      * Generally speaking, the partition function is a common term to indicate the normalizing constant of probability distributions.
* Note that:
  + \(y\) is a scalar.
  + \(\eta\) will be a vector when we consider [Softmax regression](#softmax-regression), else it is usually a scalar.
  + \(T(y)\) and \(y\) are vectors, and their dimensions need to match.
  + \(b(y)\) and \(a(\eta)\) are scalars.
* For any choice of \(T(\cdot), a\) and \(b\) (as long as the expression integrates to 1), we may define a family (or set) of distributions that are parameterized by \(\eta\); as we vary \(\eta\), we then get different distributions within this family.
  + For instance, with a fixed choice of \(T(\cdot), a\) and \(b\), we can obtain the PDF of say, a family of Gaussian distributions, such that for a particular value of the \(\eta\) parameter, you get a member of the Gaussian family.
* Next, we show that the Bernoulli and the Gaussian distributions are examples of exponential family distributions.

### Bernoulli distribution

* The Bernoulli distribution is typically used to model **binary data**. It has a parameter \(\phi\) (called “phi”), which represents the mean probability of the event.
* The Bernoulli distribution with mean \(\phi\), denoted by \(\operatorname{Bernoulli}(\phi)\), specifies a distribution over \(y \in\{0,1\}\), such that,

\[\begin{aligned}
P(y=1 ; \phi)&=\phi\\
P(y=0 ; \phi)&=1-\phi
\end{aligned}\]

* As we vary \(\phi\), we obtain Bernoulli distributions with different means. We now show that this class of Bernoulli distributions, obtained by varying \(\phi\), is a member of the exponential family, i.e., there is a choice of \(T, a\) and \(b\) so that Equation \((1)\) becomes exactly the class of Bernoulli distributions.
* The PDF of the Bernoulli distribution can be written as:

\[P(y ; \phi)=\phi^{y}(1-\phi)^{1-y}
\tag{2}\]

* Note that this exponential trick is just a programmatic way of writing the if-else statement in math. When \(y = 1\), the \((1 - \phi)\) term cancels out, so the equation would yield \(\phi\). When \(y = 0\), \(\phi\) cancels out and the equation reduces to \((1 - \phi)\).
* Now, recall that our goal is to take Equation \((2)\) and massage it into the form given by Equation \((1)\). Given the current form of the PDF equation, a natural technique would be to wrap Equation \((2)\) with a \(\log\) and then \(\exp\), since the \(\log\) and \(\exp\) operations essentially cancel out.

\[\begin{aligned}
P(y ; \phi)&=\exp (y \log \phi+(1-y) \log (1-\phi)) \\
P(y ; \phi)&=\exp \left(\left(\log \left(\frac{\phi}{1-\phi}\right)\right) y+\log (1-\phi)\right)
\end{aligned}\]

* Inspecting the above equation visually and doing some pattern matching, we see that:
  + Base measure \(b(y)\) is given by 1.
  + Sufficient statistic \(T(y)\) is given by \(y\).
  + Log partition function \(a(\eta)\) is given by \(\log (1-\phi)\).
  + Natural parameter \(\eta\) is given by \(\log \frac{\phi}{1-\phi}\).
    - Interestingly, if we invert this definition for \(\eta\) by solving for \(\phi\) in terms of \(\eta\), we obtain \(\phi=\frac{1}{1+e^{-\eta}}\). This is the familiar **sigmoid function**! This will come up again when we derive [logistic regression](#logistic-regression) as a GLM.
* As the last step in completing the formulation of the Bernoulli distribution as an exponential family distribution, let’s rewrite \(a(\eta) = \log (1-\phi)\) by plugging in the sigmoid equation for \(\phi\),

\[\begin{aligned}
a(\eta) &=-\log (1-\phi) \\
&=-\log \left(1-\frac{1}{1+e^{-\eta}}\right) \\
&=\log (1+e^{\eta}) \\
\end{aligned}\]

* This shows that the Bernoulli distribution can be written in the form of Equation \((1)\), using an appropriate choice of \(T, a\) and \(b\) and is thus a member of the exponential family.

### Gaussian distribution

* Next, let’s consider the Gaussian distribution which is used to model **real-valued data** \(\mathbb{R}\). A Gaussian distribution two parameters: (i) the mean \(\mu\) and, (ii) the variance \(\sigma^{2}\).
* Recall that in our [derivation for linear regression](../linear-regression/#probabilistic-interpretation-why-squared-error), the value of the distribution’s variance \(\sigma^{2}\) had no effect on our final choice of \(\theta\) and \(h\_{\theta}(x)\). We thus limit our discussion to the Gaussian distribution with a fixed variance \(\sigma^{2}\) (but a variable mean \(\mu\)) by choosing an arbitrary constant value for \(\sigma^{2}\) as 1 to simplify our derivation below. As such,

\[\begin{aligned}
P(y ; \mu) &=\frac{1}{\sqrt{2 \pi}} \exp \left(-\frac{(y-\mu)^2}{2}\right) \\
&=\frac{1}{\sqrt{2 \pi}} \exp \left(-\frac{y^2}{2}\right) \cdot \exp \left(\mu y-\frac{\mu^2}{2}\right)
\end{aligned}\]

* With some pattern matching, we see that the Gaussian is a member of the exponential family, with:

\[\begin{aligned}
\eta &=\mu \\
T(y) &=y \\
a(\eta) &=\mu^{2} / 2 \\
&=\eta^{2} / 2 \\
b(y) &=\frac{1}{\sqrt{2 \pi}} \exp (- \frac{y^{2}}{2})
\end{aligned}\]

* Note that the Gaussian distribution with **both** a variable mean \(\mu\) and variance \(\sigma^{2}\) can also be shown as a member of the exponential family, where \(\eta \in \mathbb{R}^{2}\) is now a 2-dimensional vector containing \(\eta\_1\) and \(\eta\_2\) that depends on both \(\mu\) and \(\sigma^2\) (rather than a scalar as seen in the above case with fixed variance). For the purposes of GLMs, however, the \(\sigma^{2}\) parameter can also be treated by considering a more general definition of the exponential family:

  \[P(y ; \eta, \tau)=b(a, \tau) \frac{\exp \left(\eta^{T} T(y)-a(\eta)\right)}{c(\tau)}\]
  + where \(\tau\) is called the **dispersion parameter**, and for the Gaussian, \(c(\tau)=\sigma^{2}\) but given our simplification above, we won’t need the more general definition for the examples we will consider here.
* **Key takeaway**

  + To show that a distribution is in the exponential family, the most straightforward way is to write out the PDF of the distribution and just do some algebraic massaging to bring it into the form denoted by Equation \((1)\). Once that is done, do a pattern match to conclude that it’s a member of the exponential family.

### Other members of the exponential family

* Some other popular distributions that are members of the exponential family:
  + The **multinomial distribution** (which we’ll see in our discussion on [Softmax regression](#softmax-regression)).
  + The **Poisson distribution** (for modelling count data which consists of non-negative integers).
  + The **gamma and the exponential distributions** (for modelling continuous, non-negative real-valued random variables \(\mathbb{R^{+}}\), such as time intervals or the volume of an object).
    - Note that the exponential distribution and exponential family are two distinct things. The exponential distribution happens to be a member of the exponential family, but to be clear, they don’t represent the same thing.
  + The **beta and the Dirichlet distributions** (for modeling distributions over probabilities).
    - These distributions represent distributions over probability distributions and mostly show up in Bayesian machine learning or Bayesian statistics.

### Distributions and their use-cases

* Depending on the task at hand (and thus, the nature of your data), you can choose an appropriate distribution that is a member of the exponential family.
* If you’re looking to do a **regression**, then your output \(y\) can be modeled as a Gaussian distribution (which is a member of the exponential family).
  + For e.g., modeling real valued numbers such as the price of a house.
* If you’re looking to do **binary classification**, then your output \(y\) can be modeled as a Bernoulli distribution (which is again, a member of the exponential family).
  + For e.g., building a spam vs. ham classifier.
* If you’re looking to **model count data**, then your output \(y\) can be modeled as a Poisson distribution (which is yet another member of the exponential family).
  + For e.g., estimating the number of customers arriving in your store (or say, the number of page-views on your website) in any given hour, based on certain features \(x\) such as store promotions, recent advertising, weather, day-of-week, etc.

### (Desirable) properties of the exponential family

* The reason why the fact that a particular distribution belongs to the exponential family is desirable is because the exponential family offer sought-after mathematical properties. In this section, we detail some of those qualities.
* If we perform maximum likelihood on the exponential family when the distribution is parameterized with the natural parameters, the optimization problem turns out to be **concave**.
  + Similarly, if you take the negative log likelihood (NLL) of the PDF expression (i.e., take the log of the expression and negate it), so instead of maximizing the original expression, you minimize the negative log likelihood, the NLL is therefore **convex**. Note that the NL is essentially the cost function equivalent of doing MLE.
  + Put simply, the MLE function with respect to \(\eta\) is concave. On the other hand, the NLL function with respect to \(\eta\) is convex.
* Differentiating the log partition function with respect to \(\eta\) yields the expected value (i.e., mean) of \(y\) as parameterized by \(\eta\). Formally,

\[\mathrm{E}[y; \eta] = \frac{\partial}{\partial \eta}a(\eta)\]

* Also,

\[Var[y; \eta] = \frac{\partial^2}{\partial \eta^2}a(\eta)\]

* Note that the second derivative is used to calculate the variance, while the first order derivative is used to calculate the expected value.
* In the case of a multi-variate Gaussian, \(\eta\) would be a vector and the second order derivative term would be the **Hessian** (for more details on the Hessian, refer to our discussion on [Newton’s method](../newton-method)).
* The reason why the last two properties are desirable is because, generally speaking calculating the mean and the variance of probability distributions require you to integrate an expression, but with exponential families, you just need to differentiate, which is a computationally easier operation.

## Generalized Linear Models (GLMs)

* GLMs are a natural extension of the exponential family. They build powerful models using a distribution that belongs to the exponential family and plugging it in at the output of a linear model, which models the output \(y\) as a linear function of the input features \(x\).
* Pictorially speaking,

* The visualization above represents a top-level picture of the GLM, and how they are an extension of exponential families. In the diagram, the model and the exponential family distribution represent our building blocks. We’re assuming the model to be a linear model of the input \(x\) parameterized by \(\theta\), which is a learnable parameter. The distribution is a member of the exponential family. The parameter for this distribution is the output of the linear model.
* Depending on the task at hand, say classification or regression or a time-to-win problem, you would choose a set of parameters \(b\), \(a\) and \(T(\cdot)\), to model your data using an appropriate distribution which is a member of the exponential family.
* During test time, the expected value of distribution \(E[y \mid \eta]\), which is equivalent to \(E[y \mid \theta^T x]\), is our hypothesis function \(h\_{\theta}(x)\).
* During training time, we’re learning the parameters of the model \(\theta\), using gradient descent. The point here to note is that you’re not learning any the parameters in the exponential family distribution, say \(\mu\), \(\sigma^2\) or \(\eta\). The output of the model will become the **natural parameter** of the distribution. Put simply, we are learning \(\theta\) to predict the parameter \(\eta\) of the exponential family distribution whose mean is the prediction \(y\).
  + We train the model by maximizing the log likelihood \(\mathop {\max }\limits\_\theta \log P({y^{(i)}};{\theta ^T}{x^{(i)}})\). In other words, you’re doing gradient ascent on \(\theta\) to maximize the log probability of \(y\).
* In summary, GLMs carry out the following steps:
  + Re-parameterize the parameters of a linear model \(\theta\) to the natural parameter \(\eta\) and,
  + Model \(\eta\) as a distribution that is a member of exponential family, which yields the final output \(y=E[y \mid \eta]\).

### The beauty of GLMs: update rule

* At train time, rather than take the derivatives of the log likelihood expression, and come up with an update rule, the beauty with GLMs is that no matter your choice of exponential family distribution, the update rule remains the same.

\[\theta\_j := \theta\_j + \alpha\left(y^{(i)} - h\_{\theta}(x^{(i)})\right)x\_{j}^{(i)}\]

* You can simply apply this learning rule without ever having to figure out what the gradients are, or even what the loss is. Just **initialize** your \(\theta\) using random values and **plug in the appropriate \(h(\theta x)\)** depending on the choice of your distribution, and you can start learning right away!
* For batch gradient descent, simply sum over all your examples as follows:

\[\theta\_j := \theta\_j + \alpha \sum\_{i=1}^{m} \left(y^{(i)} - h\_{\theta}(x^{(i)})\right)x\_{j}^{(i)}\]

* However, now that Newton’s method is probably the most common MLE algorithm you would use with GLMs, assuming the dimensionality of your data is not extremely high. As long as the number of features is less than a few thousand, Newton’s method is computationally tractable and converges faster than gradient descent. For more details on Newton’s method, refer to our discussion [here](../newton-method).

### Terminology

* To introduce some terminology, the function \(g(\cdot)\) that yields the distribution’s mean as a function of the natural parameter \(g(\eta) = \mathrm{E}[T(y) ; \eta] = \mathrm{E}[y ; \eta]\) is called the canonical response function. Note that \(\mathrm{E}[y ; \eta]\) is essentially the mean of the distribution, which is denoted by \(\mu\) in case of the Gaussian distribution and \(\phi\) in case of the Bernoulli distribution. Furthermore, note that \(\mathrm{E}[y ; \eta]\) is equivalent to the first derivative of the log parition function, per our discussion in the section on [desirable properties of the exponential family](#desirable-properties-of-the-exponential-family). Recall that \(\eta\) is called the natural parameter. Thus,

\[g(\eta) = \mathrm{E}[T(y) ; \eta] = \mathrm{E}[y ; \eta] = \mu = \frac{\partial}{\partial \eta}a(\eta)\]

* The inverse of \(g(\cdot)\), \(g^{-1}(\cdot)\), which lets you go from \(\mu\) back to \(\eta\) is called the canonical link function. As such, the canonical response function for the Gaussian family is just the identity function; and the canonical response function for the Bernoulli is the logistic function.
  + Note that many texts use \(g(\cdot)\) to denote the link function, and \(g^{-1}(\cdot)\) to denote the response function; but the notation we’re using here has been inherited from early machine learning literature.

### Parameter spaces

* At this point, it would be worthwhile to explicitly state the distinction between the three different kinds of parameterizations we have available.

| Model parameters | Natural parameters | Canonical parameters |
| --- | --- | --- |
| \(\theta\) | \(\eta\) | \(\text{Bernoulli: }\phi\) \(\text{Gaussian: }(\mu, \sigma^2)\) \(\text{Poisson: }\lambda\) |

* It’s important to understand the spaces in which the parameters of a GLM exist and the process through which they get re-parameterized. We offer a summary below:
* **Model parameter \(\theta\)**
  + During the training phase of a GLM, we’re learning the parameters \(\theta\) of the linear model.
* **Natural parameter \(\eta\)**
  + The connection between these the model parameter \(\theta\) and natural parameter \(\eta\) is linear, i.e., \(\eta = \theta^T x\). Note that this is a design choice. In other words, we choose to re-parameterize \(\eta\) by a linear model.
* **Canonical parameters \(\phi, (\mu, \sigma^2), \lambda\)**
  + The function that connects the natural parameter \(\eta\) to the canonical parameters \(\phi, (\mu, \sigma^2), \lambda\) is the canonical response function \(g(\cdot)\).
  + Conversely, the function that connects canonical parameters \(\phi, (\mu, \sigma^2), \lambda\) to the natural parameter \(\eta\) is the link response function \(g^{-1}(\cdot)\).

## Constructing GLMs

* In this section, we will describe a general “recipe” for constructing models in which the output \(y\) (given \(x\) and \(\theta\)) can be modeled as a distribution that is belongs to the exponential family.
* Considering our store foot-traffic estimation problem discussed in the section on [“other members of the exponential family”](#other-members-of-the-exponential-family), we can come up with a model for our problem by constructing a GLM atop the Poisson distribution. In this section, we will describe a method for constructing GLMs for similar problems.
* More generally, consider a classification or regression problem where we would like to predict the value of some random variable \(y\) as a function of \(x\). To derive a GLM for this problem (i.e., to transform our distribution which is a member of the exponential family, to a GLM), we will make the following three assumptions about the conditional distribution of \(y\) given \(x\) and about our model:

  1. \(y \mid x ; \theta \sim \operatorname{ExponentialFamily} (\eta)\). This implies that the distribution of \(y\), given \(x\) and \(\theta\) (or conditioned on \(x\) and parametrized by \(\theta\)), follows some exponential family distribution, with parameter \(\eta\).
  2. The natural parameter \(\eta\) and the inputs \(x\) are related linearly: \(\eta=\theta^{T} x\). If \(\eta\) is vector-valued, then \(\eta\_{i}=\theta\_{i}^{T} x\).
     + where \(\theta \in \mathbb{R^n}\) and \(x \in \mathbb{R^n}\). Note that \(n\) represents the dimensions of your input data \(x\) and has nothing to do with any of the parameters in the exponential family.
  3. At test time, given a new \(x\), our goal is to output a prediction given by the mean of our distribution, denoted by \(\mathrm{E}[T(y) \mid x; \theta]\). Since we have \(T(y)=y\) for most of our examples, we would like our prediction \(h\_{\theta}(x)\) output by our learned hypothesis \(h\) to satisfy \(h\_{\theta}(x)=\mathrm{E}[y \mid x; \theta]\).
     + Note that this assumption is satisfied in the choices for \(h\_{\theta}(x)\) for both logistic regression and linear regression. For instance, in logistic regression, we had \(h\_{\theta}(x)=P(y=1 \mid x ; \theta)=0 \cdot P(y=0 \mid x ; \theta)+1 \cdot P(y=1 \mid x ; \theta)=\mathrm{E}[y \mid x ; \theta]\).
* The second of these assumptions might seem the least well justified of the above, and it might be better thought of as a “design choice” in our recipe for designing GLMs, rather than an assumption. These three assumptions/design choices will allow us to derive a very elegant class of learning algorithms, namely GLMs, that have many desirable properties such as ease of learning. Since the log-likelihood function of GLMs is a concave function, this implies that GLMs do not have a local maxima, and the only maximum is a global maxima.
* Furthermore, the resulting models are often very effective for modelling different types of distributions over \(y\); for example, we will shortly show that both logistic regression and ordinary least squares can both be derived as GLMs.

### Linear regression

* To show that (least squares) linear regression is a special case of the GLM family of models, consider the setting where the target variable \(y\) (also called the **response variable** in GLM terminology) is continuous, and we model the conditional distribution of \(y\) given \(x\) as a Gaussian \(\mathcal{N}(\mu, \sigma^{2})\).
* If \(y \mid x ; \theta \sim \operatorname{Gaussian}(\mu, \sigma^{2})\), then \(\mathrm{E}[y \mid x ; \theta]=\mu\). Furthermore, in our formulation of the Gaussian distribution as a member of the exponential family, we had \(\mu=\eta\). As such,

\[\begin{aligned}
h\_{\theta}(x) &=E[y \mid x ; \theta] \\
&=\mu \\
&=\eta \\
&=\theta^{T} x
\end{aligned}\]

* The first equality follows from Assumption 1 in the section on [constructing GLMs](#constructing-glms); the second equality follows from the fact that \(y \mid x ; \theta \sim \mathcal{N}(\mu, \sigma^{2})\), and so its expected value is given by \(\mu\); the third equality follows from our [earlier derivation](#gaussian-distribution) in the formulation of the Gaussian as an exponential family distribution showing that \(\mu=\eta\); and the last equality follows from Assumption 2.

### Logistic regression

* We now consider logistic regression. Here we are interested in binary classification, so \(y \in\{0,1\}\). Given that \(y\) is binary-valued, it therefore seems natural to choose the Bernoulli family of distributions to model the conditional distribution of \(y\) given \(x\).
* If \(y \mid x ; \theta \sim \operatorname{Bernoulli}(\phi)\), then \(\mathrm{E}[y \mid x ; \theta]=\phi\). Furthermore, in our formulation of the Bernoulli distribution as a member of the exponential family, we had \(\phi=\frac{1}{1+e^{-\eta}}\). As such,

\[\begin{aligned}
h\_{\theta}(x) &=E[y \mid x ; \theta] \\
&=\phi \\
&=\frac{1}{1+e^{-\eta}} \\
&=\frac{1}{1+e^{-\theta^{T} x}}
\end{aligned}\]

* Thus, we obtain a hypothesis function of the form \(h\_{\theta}(x)=\frac{1}{1+e^{-\theta^{T} x}}\). The form of the logistic function \(\frac{1}{1+e^{-z}}\) arises as a consequence of the definition of GLMs and exponential family distributions once we assume that \(y\) conditioned on \(x\) follows a Bernoulli distribution, as shown in the section on [Bernoulli distribution](#bernoulli-distribution).

### Softmax regression

* In this section, we delve into another example of a GLM. Consider a classification problem in which the response variable \(y\) can take on any one of \(k\) values, so \(y \in\) \(\{1,2, \ldots, k\}\). For example, rather than classifying email into the two classes, spam or not-spam, which would have been a binary classification problem, we might want to classify it into three classes, such as spam, personal mail, and work-related mail. The response variable is still discrete, but can now take on more than two values. We will thus model it according to a multinomial distribution.
* Let’s derive a GLM for modelling this type of multinomial data. To do so, we will begin by expressing the multinomial as an exponential family distribution.
* To parameterize a multinomial over \(k\) possible outcomes, one could use \(k\) parameters \(\phi\_{1}, \ldots, \phi\_{k}\) specifying the probability of each of the outcomes. However, these parameters would be redundant, or more formally, would not be independent (since knowing any \(k-1\) of the \(\phi\_{i}\)’s uniquely determines the last one, as they must satisfy \(\sum\_{i=1}^{k} \phi\_{i}=1\)).
  + As such, we will instead parameterize the multinomial with only \(k-1\) parameters, \(\phi\_{1}, \ldots, \phi\_{k-1}\), where \(\phi\_{i}=P(y=i ; \phi)\), and \(P(y=k ; \phi)=1-\sum\_{i=1}^{k-1} \phi\_{i}\). For notational convenience, we will also let \(\phi\_{k}=1-\sum\_{i=1}^{k-1} \phi\_{i}\), but we should keep in mind that this is not a parameter, and that it is fully specified by \(\phi\_{1}, \ldots, \phi\_{k-1}\).
* To express the multinomial as an exponential family distribution, we will define \(T(y) \in \mathbb{R}^{k-1}\) as follows:

\[T(1)=\left[\begin{array}{c}
1 \\
0 \\
0 \\
\vdots \\
0
\end{array}\right], T(2)=\left[\begin{array}{c}
0 \\
1 \\
0 \\
\vdots \\
0
\end{array}\right], T(3)=\left[\begin{array}{c}
0 \\
0 \\
1 \\
\vdots \\
0
\end{array}\right], \cdots, T(k-1)=\left[\begin{array}{c}
0 \\
0 \\
0 \\
\vdots \\
1
\end{array}\right], T(k)=\left[\begin{array}{c}
0 \\
0 \\
0 \\
\vdots \\
0
\end{array}\right]\]

* Unlike our previous examples, here we do not have \(T(y)=y\); also, \(T(y)\) is now a \(k-1\) dimensional vector, rather than a real number. We will write \((T(y))\_{i}\) to denote the \(i^{th}\) element of the vector \(T(y)\).
* We introduce one more very useful piece of notation. An indicator function \(1\{\cdot\}\) takes on a value of 1 if its argument is true, and 0 otherwise. Formally, \(1\{True\}=1\) and \(1\{False\}=0\).
  + For example, \(1\{2=3\}=0\), and \(1\{3=\) \(5-2\}=1\). So, we can also write the relationship between \(T(y)\) and \(y\) as \({\left(T(y)\right)}\_i\) \(= 1 \{y=i\}\).
  + Further, we have that \(\mathrm{E}[\)\({\left(T(y)\right)}\_{i}\)\(]=P(y=i)=\phi\_i\).
* We are now ready to show that the multinomial is a member of the exponential family. We have,

  \[\begin{aligned}
  P(y ; \phi) &=\phi\_{1}^{1\{y=1\}} \phi\_{2}^{1\{y=2\}} \cdots \phi\_{k}^{1\{y=k\}} \\
  &=\phi\_{1}^{1\{y=1\}} \phi\_{2}^{1\{y=2\}} \cdots \phi\_{k}^{1-\sum\_{i=1}^{k-1} 1\{y=i\}} \\
  &=\phi\_{1}^{(T(y))\_{1}} \phi\_{2}^{(T(y))\_{2}} \cdots \phi\_{k}^{1-\sum\_{i=1}^{k-1}(T(y))\_{i}} \\
  &=\exp \left((T(y))\_{1} \log \left(\phi\_{1}\right)+(T(y))\_{2} \log \left(\phi\_{2}\right)+\right.\\
  &\left.\cdots+\left(1-\sum\_{i=1}^{k-1}(T(y))\_{i}\right) \log \left(\phi\_{k}\right)\right) \\
  &=\exp \left((T(y))\_{1} \log \left(\phi\_{1} / \phi\_{k}\right)+(T(y))\_{2} \log \left(\phi\_{2} / \phi\_{k}\right)+\right.\\
  &\left.\cdots+(T(y))\_{k-1} \log \left(\phi\_{k-1} / \phi\_{k}\right)+\log \left(\phi\_{k}\right)\right) \\
  &=b(y) \exp \left(\eta^{T} T(y)-a(\eta)\right)
  \end{aligned}\]
  + where,\[\begin{aligned}
  \eta &=\left[\begin{array}{c}
  \log \left(\phi\_{1} / \phi\_{k}\right) \\
  \log \left(\phi\_{2} / \phi\_{k}\right) \\
  \vdots \\
  \log \left(\phi\_{k-1} / \phi\_{k}\right)
  \end{array}\right] \\
  a(\eta) &=-\log \left(\phi\_{k}\right) \\
  b(y) &=1
  \end{aligned}\]
* This completes our formulation of the multinomial as an exponential family distribution. The link function is given (for \(i=1, \ldots, k\)) by,

\[\eta\_{i}=\log \frac{\phi\_{i}}{\phi\_{k}}\]

* For convenience, we have also defined \(\eta\_{k}=\log \frac{\phi\_{k}}{\phi\_{k}}=\log 1=0\). To invert the link function and derive the response function,

\[\begin{aligned}
e^{\eta\_{i}} &=\frac{\phi\_{i}}{\phi\_{k}} \\
\phi\_{k} e^{\eta\_{i}} &=\phi\_{i} \\
\phi\_{k} \sum\_{i=1}^{k} e^{\eta\_{i}} &=\sum\_{i=1}^{k} \phi\_{i}=1
\end{aligned}
\tag{3}\]

* This implies that \(\phi\_{k}=\frac{1}{\sum\_{i=1}^{k} e^{\eta\_{i}}}\), which can be substituted back into Equation \((3)\) to give the response function,

\[\phi\_{i}=\frac{e^{\eta\_{i}}}{\sum\_{j=1}^{k} e^{\eta\_{j}}}\]

* This function mapping from the \(\eta\)’s to the \(\phi\)’s is called the softmax function. To complete our model, we use Assumption 3, given earlier, that the \(\eta\_{i}\)’s are linearly related to the \(x\)’s. So, have \(\eta\_{i}=\theta\_{i}^{T} x\) (for \(i=1, \ldots, k-1\)), where \(\theta\_{1}, \ldots, \theta\_{k-1} \in \mathbb{R}^{n+1}\) are the parameters of our model. For notational convenience, we can also define \(\theta\_{k}=0\), so that \(\eta\_{k}=\theta\_{k}^{T} x=0\), as given previously. Hence, our model assumes that the conditional distribution of \(y\) given \(x\) is given by,

\[\begin{aligned}
P(y=i \mid x ; \theta) &=\phi\_{i} \\
&=\frac{e^{\eta\_{i}}}{\sum\_{j=1}^{k} e^{\eta\_{j}}} \\
&=\frac{e^{\theta\_{i}^{T} x}}{\sum\_{j=1}^{k} e^{\theta\_{j}^{T} x}}
\end{aligned}
\tag{4}\]

* This model, which applies to classification problems where \(y \in\{1, \ldots, k\}\), is called **softmax regression**. It is a generalization of logistic regression. Our hypothesis will output:

\[\begin{aligned}
h\_{\theta}(x) &=\mathrm{E}[T(y) \mid x ; \theta] \\
&=\mathrm{E}\left[\begin{array}{c}
1\{y=1\} \\
1\{y=2\} \\
\vdots \\
1\{y=k-1\}
\end{array} \mid x ; \theta \right]\\
&=\left[\begin{array}{c}
\phi\_{1} \\
\phi\_{2} \\
\vdots \\
\phi\_{k-1}
\end{array}\right] \\
&=\left[\begin{array}{c}
\frac{\exp \left(\theta\_{1}^{T} x\right)}{\sum\_{j=1}^{k} \exp \left(\theta\_{j}^{T} x\right)} \\
\frac{\exp \left(\theta\_{2}^{T} x\right)}{\sum\_{j=1}^{k} \exp \left(\theta\_{j}^{T} x\right)} \\
\vdots \\
\frac{\exp \left(\theta\_{k-1}^{T} x\right)}{\sum\_{j=1}^{k} \exp \left(\theta\_{j}^{T} x\right)}
\end{array}\right]
\end{aligned}\]

* In other words, our hypothesis will output the estimated probability that \(P(y=i \mid x ; \theta)\), for every value of \(i=1, \ldots, k\). Even though \(h\_{\theta}(x)\) as defined above is only \(k-1\) dimensional, clearly \(P(y=k \mid x ; \theta)\) can be obtained as,

\[1-\sum\_{i=1}^{k-1} \phi\_{i}\]

* Lastly, let’s discuss parameter fitting. Similar to our original derivation of ordinary least squares and logistic regression, if we have a training set of \(m\) examples \(\{(x^{(i)}, y^{(i)}); i=1, \ldots, m\}\) and would like to learn the parameters \(\theta\_{i}\) of this model, we would begin by writing down the log-likelihood,

\[\ell(\theta)=\sum\_{i=1}^{m} \log P\left(y^{(i)} \mid x^{(i)} ; \theta\right) \\\]

* Plugging in the definition for \(P(y \mid x ; \theta)\) from Equation \((4)\),

\[\ell(\theta)=\sum\_{i=1}^{m} \log \prod\_{l=1}^{k}\left(\frac{e^{\theta\_{l}^{T} x^{(i)}}}{\sum\_{j=1}^{k} e^{\theta\_{j}^{T} x^{(i)}}}\right)^{1\left\{y^{(i)}=l\right\}}\]

* We can now obtain the maximum likelihood estimate of the parameters by maximizing \(\ell(\theta)\) in terms of \(\theta\), using a method such as gradient ascent or Newton’s method.

## Graphical intuition

### Regression

* Let’s delve into the task of regression. Assume an input vector \(x\), shown on the left-hand side of the below figure. For simplicity, let’s assume \(x\) as one dimensional but, \(x\) could be multi-dimensional.
* The plot on the right hand side of the below figure shows us a linear hyperplane (or decision boundary) \(\theta^T x\) using a set of parameters \(\theta\) for our linear model. For GLMs, \(\theta^T x\) is equal to the natural parameter \(\eta\) of the exponential family distribution. Furthermore, note that in case of a regression being modeled as a Gaussian distribution, \(\eta\) is equal to the mean of the distribution \(\mu\).
* For every \(x^{(i)} \in x\), you have a corresponding \(\eta = \theta^T x\). For each value of \(\eta\) as the mean \(\mu\), we define a Gaussian distribution to model the output \(y\) corresponding to the input value \(x^{(i)}\) (as shown in the diagram below). We assume a variance of 1 following our discussion in the section on [Gaussian distribution](#gaussian-distribution).
* Our aim is to find the value of \(\theta\) that leads to a line that represents the means of the distributions that are centered at the \(\mu = \eta\) for the corresponding input \(x^{(i)}\). In doing so, we’re assuming that the output \(y\) is sampled from these Gaussian distributions. Under the hood, this is essentially what’s happening when you do MLE with the GLM.

### Classification

* Let’s dissect the task of binary classification. Assume an input vector \(x\), which consists of data that belongs to two classes, shown on the left-hand side of the below figure.
* In the diagram on the right-hand side of the below figure, we’re trying to learn \(\theta^T x\), which is equal to the natural parameter \(\eta\) as shown by the line in the graph. For a classification problem being modeled as a Bernoulli distribution, \(\eta\) is related to the mean of the distribution \(\phi\) as \(\log \frac{\phi}{1-\phi}\), which implies \(\phi = \frac{1}{1+e^{-\eta}}\), i.e., the sigmoid function.
* Note that we’ve shown the individual \(\eta\) for each individual input sample \(x^{(i)} \in x\) in the right-hand side diagram below. Since each input sample \(x^{(i)}\) has a corresponding Bernoulli distribution, the \(\eta\) corresponding to each \(x^{(i)}\) is run through the sigmoid function \(\frac{1}{1 + e^{-\eta}}\) (curve shown in the figure) to get the probability \(\phi\) parameter of its Bernoulli distribution. Note that when \(\eta = 0\), the sigmoid function yields \(0.5\) as shown in the diagram on the right.
* In the figure below, for each value of \(\eta\), the black columns (the height to the sigmoid line) indicate the probability \(\phi\) of each \(\eta\) belonging to the positive class, which represents our output \(y\).
* Our goal is to learn the optimum value of \(\theta\) that can recreate the distribution from which the target labels \(y\) were sampled. Given our input data \(x^{(i)}\), figuring out the Bernoulli distribution that can maximize the likelihood of \(y\) is the central idea behind doing binary classification using logistic regression.

### Softmax regression

* In contrast to the earlier section on [Softmax regression](#softmax-regression) which offers a GLM-based treatment on the topic, let’s understand the cross entropy minimization approach in this section. This approach serves to have a much more intuitive and graphical approach compared to the other interpretation. Note that we’ll end up with the same equations in both cases.
* Let’s assume we have a multi-class classification problem at hand where we’re trying to classify three classes of data. Let’s call them circles, squares, and triangles.

* The above diagram visualizes the output space \(y\) in terms of the input features \(x\_1\) and \(x\_2\).
* The goal of our multi-class classification problem is to learn a model that can make a prediction of whether a datapoint point is a circle, square or a triangle. Note that while we limit our discussion in this section to a multi-class problem with three classes, the same concepts apply to as many classes as we desire to perform classification on.
* Assume \(k\) is the number of classes. The input features for a particular input sample \(x^{(i)}\), \(x\_1^{(i)}\) and \(x\_2^{(i)}\) consist of real numbers, i.e., \(x^{(i)} \in \mathbb{R}^n\).
* \(y\) is a one-hot vector that holds the target labels, i.e., only the element corresponding to the class which \(x^{(i)}\) corresponds to is set to 1, else 0. Each element in the vector corresponds to one of the classes. For e.g., if the circle, square and triangle classes corresponding to class numbers \(0, 1\) and 2 respectively, then \(y^{(i)}\) would be \([0, 0, 1]\) for an input sample \(x^{(i)}\) that belongs to the triangle class. Formally,

\[y = [{0, 1}^k]\]

* In softmax regression, each class has its own set of parameters. Note that in contrast, logistic regression had just one \(\theta\) which would be used for carrying out binary (yes vs. no) classification. On the other hand, in softmax regression, we have one such vector of \(\theta\) per class. Formally,

\[\theta\_{class} \in \mathbb{R}^n\text{ where class = 1, \ldots, k}\]

* As such, you could also optionally represent \(\theta\) as an \(k \times n\) matrix of the following form:

\[\left[ \begin{array}{l}
\theta \_0 \\
\theta \_1 \\
\vdots \\
\theta \_k
\end{array} \right]\]

* In this sense, softmax regression is a **generalization of logistic regression** for the multi-class classification problem where you have a set of parameters per class.
* Corresponding to each class of parameters that exists, there exists a decision boundary (or an hyperplane) which separates that class from other classes.

* For e.g., for the triangle class (#2), the decision boundary is given by \(\theta\_2^T x = 0\) so the direction of the triangle samples is given by \(\theta\_2^T x > 0\), while the other direction would correspond to \(\theta\_2^T x < 0\).
* Let’s walk through the process of fielding a new example, which has a target label of a square.
* The left-hand side diagram of the below figure shows a plot of \(\theta^T x\) for each of our classes. The diagram shows that \(\theta^T x\) for the triangle class is highly positive, while that for the circle class is negative and for the square class is slightly positive. The \(\theta^T x\) values are called logits, and hence this space is called the logit space. Note that \(\theta^T x\) are real numbers \(\in [\infty, -\infty]\). Our goal is to compress this space to get a probability distribution over the classes, i.e., \(\in [0, 1]\).
* Next, we exponentiate the logits \(\exp({\theta\_{class}^Tx})\). This transforms all the \(\theta^T x\) values to positive numbers. This yields the diagram on the right-hand side of the below figure.

* Lastly, we normalize the exponential versions of the logits using \(\frac{\exp({\theta\_{class}^Tx})}{\sum\_{i = 0}^{k}\exp({\theta\_{i}^Tx})}\). This operation yields get a probability distribution where the sum of the heights will add up to 1.

* Thus, if we run a new datapoint through this pipeline, we get a probability output over all our classes, and the maximum of that result vector yields the class that this example most likely belongs to. In this case, the example would be misclassified as a triangle, even though it is a square.
* Let’s work on figuring out how to make our model learn from this misclassification. In case of logistic regression, the output of the hypothesis function, generally outputs a scalar or a single probability value. In case of softmax regression, our hypothesis \(h\_{\theta}(x) = \hat{p}(y)\), given an \(x\) thus yields a hypothesis function will output a probability distribution over all the classes.
* The left-hand side diagram of the below figure shows the probability distribution obtained from the model while the right-hand side diagram of the below figure shows the target label probability distribution \(y\). The below diagrams are essentially representing the one-hot representation as a probability distribution.

* Since the ground truth label for this sample is a square, then \(p\_1(y) = 1\) while \(p\_0(y) = p\_2(y) = 1\).
* Now the goal of our learning algorithm is to minimize the distance between these two distributions. Put simply, we want the distribution obtained from our model’s output to look like the ground truth distribution. This process is referred to as minimizing the cross entropy between the two distributions.
* Formally, the cross entropy between \(P(y)\) and \(\hat{P}(y)\) is given by,

\[CrossEnt(p, \hat{p}) = \sum\_{y = 1}^k P(y) \log{\hat{P}(y)}\]

* Since \(P(y)\) will be one for just one of the classes and zero for the others,

\[CrossEnt(p, \hat{p}) = - \log{\hat{p}(y)}\]

* Thus, our cross-entropy expression has essentially boiled down to,

\[CrossEnt(p, \hat{p}) = - \log{\frac{\exp({\theta\_{class}^Tx})}{\sum\_{i = 0}^{k}\exp({\theta\_{i}^Tx})}}\]

* We treat the above expression as our loss and perform gradient descent with respect to the parameters.

## Further reading

Here are some (optional) links you may find interesting for further reading:

## References

* [CS229 Notes](http://cs229.stanford.edu/syllabus-summer2020.html).

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledGeneralizedLinearModels,
  title   = {Generalized Linear Models},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
