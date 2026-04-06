# Primers • Partial Derivative of the Cost Function for Logistic Regression

**Source:** https://aman.ai/primers/backprop/derivative-logistic-regression/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* The partial derivative of the logistic regression cost function with respect to \(\theta\) is:

\[\frac{\partial J(\theta)}{\partial \theta\_j} = \nabla\_{\theta\_j}J(\theta) = \sum\_{i=1}^{m}\left(h\_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) x\_{j}^{(i)}\]

---

* Let’s begin with the cost function used for logistic regression, which is the **average of the log loss** across all training examples, as given below:

  \[J(\theta)=-\frac{1}{m} \sum\_{i=1}^{m} y^{(i)} \log \left(h\_{\theta}\left(x^{(i)}\right)\right)+\left(1-y^{(i)}\right) \log \left(1-h\_{\theta}\left(x^{(i)}\right)\right)\]
  + where the logs are natural logarithms and \(h\_{\theta}(x)\) is defined as:\[\begin{array}{l}
  h\_{\theta}(x)=g(\theta^{T} x) \\
  g(z)=\frac{1}{1+e^{-z}}
  \end{array}\]

---

* We use the notation:

\[\theta x^{(i)} = \theta\_{0}+\theta\_{1} x\_{1}^{(i)}+\cdots+\theta\_{n} x\_{n}^{(i)}\]

* Since our original cost function is the form of:

\[J(\theta)=-\frac{1}{m} \sum\_{i=1}^{m} y^{(i)} \log \left(h\_{\theta}\left(x^{(i)}\right)\right)+\left(1-y^{(i)}\right) \log \left(1-h\_{\theta}\left(x^{(i)}\right)\right)\]

* Now,

\[\begin{array}{c}
\log h\_{\theta}\left(x^{(i)}\right)=\log \frac{1}{1+e^{-\theta x^{(i)}}}=-\log \left(1+e^{-\theta x^{(i)}}\right) \\
\log \left(1-h\_{\theta}\left(x^{(i)}\right)\right)=\log \left(1-\frac{1}{1+e^{-\theta x^{(i)}}}\right)=\log \left(e^{-\theta x^{(i)}}\right)-\log \left(1+e^{-\theta x^{(i)}}\right)=-\theta x^{(i)}-\log \left(1+e^{-\theta x^{(i)}}\right)
\end{array}\\
\text{because, }\left(1=\frac{\left(1+e^{-\theta x^{(i)}}\right)}{\left(1+e^{-\theta x^{(i)}}\right)}, \text { the 1's in numerator cancel, then we used: } \log \left(\frac{x}{y}\right)=\log (x)-\log (y)\right)\]

---

* Plugging in the two simplified expressions above in our original cost function, we obtain:

\[J(\theta)=-\frac{1}{m} \sum\_{i=1}^{m}\left[-y^{(i)}\left(\log \left(1+e^{-\theta x^{(i)}}\right)\right)+\left(1-y^{(i)}\right)\left(-\theta x^{(i)}-\log \left(1+e^{-\theta x^{(i)}}\right)\right)\right]\]

* which can be simplified to:

  \[\boxed{J(\theta)=-\frac{1}{m} \sum\_{i=1}^{m}\left[y\_{(i)} \theta x^{(i)}-\theta x^{(i)}-\log \left(1+e^{-\theta x^{(i)}}\right)\right]=-\frac{1}{m} \sum\_{i=1}^{m}\left[y\_{(i)} \theta x^{(i)}-\log \left(1+e^{\theta x^{(i)}}\right)\right]}\]
  + where the second equality follows from:\[-\theta x^{(i)}-\log \left(1+e^{-\theta x^{(i)}}\right)=-\left[\log e^{\theta x^{(i)}}+\log \left(1+e^{-\theta x^{(i)}}\right)\right]=-\log \left(1+e^{\theta x^{(i)}}\right)\]
  \[\text { because, } \log (x)+\log (y)=\log (x y)\]

---

* Now, all you need is to compute the partial derivative of the boxed equation above w.r.t. \(\theta\_{j}\), using the following:

\[\begin{array}{c}
\frac{\partial}{\partial \theta\_{j}} y\_{(i)} \theta x^{(i)}=y\_{(i)} x\_{j}^{(i)} \\
\frac{\partial}{\partial \theta\_{j}} \log \left(1+e^{\theta x^{(i)}}\right)=\frac{x\_{j}^{(i)} e^{\theta x^{(i)}}}{1+e^{\theta x^{(i)}}}=x\_{j}^{(i)} h\_{\theta}\left(x^{(i)}\right)
\end{array}\]

* Finally, plugging in the two components above in the expression for \(\frac{\partial J(\theta)}{\partial \theta\_j}\), we obtain the end result:

\[\boxed{\frac{\partial J(\theta)}{\partial \theta\_j}=\sum\_{i=1}^{m}\left(h\_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) x\_{j}^{(i)}}\]

## References

* [Derivative of cost function for Logistic Regression](https://math.stackexchange.com/questions/477207/derivative-of-cost-function-for-logistic-regression)
* [Properties of logarithms](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-prop/a/properties-of-logarithms)
