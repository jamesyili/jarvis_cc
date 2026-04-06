# CS229 • Naive Bayes

**Source:** https://aman.ai/cs229/naive-bayes/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-theory

---

* [Overview](#overview)
  + [Laplace smoothing](#laplace-smoothing)
  + [Event models for text classification](#event-models-for-text-classification)
* [Further reading](#further-reading)
* [Citation](#citation)

## Overview

* In GDA, the feature vectors \(x\) were continuous, real-valued vectors. Let’s now talk about a different learning algorithm in which the \(x\_{i}\)’s are discrete-valued, for say, a spam vs. no-spam classifier or sentiment classification using tweets.
* For our motivating example, consider the spam classification example. Here, we wish to classify messages according to whether they are unsolicited commercial (spam) email, or non-spam email. After learning to do this, we can then have our mail reader automatically filter out the spam messages and perhaps place them in a separate mail folder. Classifying emails is one example of a broader set of problems called text classification.
* Let’s say we have a training set (a set of emails labeled as spam or non-spam). We’ll begin our construction of our spam filter by specifying the features \(x\_{i}\) used to represent an email.
* We will represent an email via a feature vector whose length is equal to the number of words in the dictionary. Specifically, if an email contains the \(i^{th}\) word of the dictionary, then we will set \(x\_{i}=1\); otherwise, we let \(x\_{i}=0\) For instance, the vector is used to represent an email that contains the words “a” and “buy,” but not “aardvark,” “aardwolf” or “zygmurgy.”

\[x = \left[ \begin{array}{l}
1\\
0\\
0\\
\vdots\\
1\\
\vdots\\
0
\end{array} \right] \begin{array}{\*{20}{c}}
\text{a}\\
\text{aardvark}\\
\text{aardwolf}\\
\vdots\\
\text{buy}\\
\vdots\\
\text{zygmurgy}
\end{array}\]

* Actually, rather than looking through an English dictionary for the list of all English words, in practice it is more common to look through our training set and encode in our feature vector only the words that occur at least once there.
* Apart from reducing the number of words modeled and hence reducing our computational and space requirements, this also has the advantage of allowing us to model/include as a feature many words that may appear in your email but that you won’t find in a dictionary. Sometimes, we also exclude the very high frequency words (which will be words like “the,” “of,” “and,”; these high frequency, “content free” words are called stop words) since they occur in so many documents and do little to indicate whether an email is spam or non-spam.
* The set of words encoded into the feature vector is called the vocabulary, so the dimension of \(x\) is equal to the size of the vocabulary.
* Having chosen our feature vector, we now want to build a generative model. So, we have to model \(P(x \mid y)\). But if we have, say, a vocabulary of 50000 words, then \(x \in\{0,1\}^{50000}\) (\(x\) is a 50000-dimensional vector of 0’s and 1’s), and if we were to model \(x\) explicitly with a multinomial distribution over the \(2^{50000}\) possible outcomes, then we’d end up with a \((2^{50000}-1)\)-dimensional parameter vector. This is clearly too many parameters.
* To model \(P(x \mid y)\), we will therefore make a very strong assumption. We will assume that the \(x\_{i}\)’s are conditionally independent given \(y\). This assumption is called the Naive Bayes (NB) assumption, and the resulting algorithm is called the Naive Bayes classifier.
  + For instance, if \(y=1\) means spam email; “buy” is word 2087 and “price” is word 39831; then we are assuming that if “I tell you” \(y=1\) (that a particular piece of email is spam), then knowledge of \(x\_{2087}\) (knowledge of whether “buy” appears in the message) will have no effect on your beliefs about the value of \(x\_{39831}\) (whether “price” appears). More formally, this can be written \(P\left(x\_{2087} \mid y\right)=P\left(x\_{2087} \mid y, x\_{39831}\right)\). (Note that this is not the same as saying that \(x\_{2087}\) and \(x\_{39831}\) are independent, which would have been written \(“P\left(x\_{2087}\right)=P\left(x\_{2087} \mid x\_{39831}\right)”\); rather, we are only assuming that \(x\_{2087}\) and \(x\_{39831}\) are conditionally independent given \(y\).)
* Formally,

\[\begin{array}{l}
P\left(x\_{1}, \ldots, x\_{50000} \mid y\right) \\
\quad=P\left(x\_{1} \mid y\right) P\left(x\_{2} \mid y, x\_{1}\right) P\left(x\_{3} \mid y, x\_{1}, x\_{2}\right) \cdots P\left(x\_{50000} \mid y, x\_{1}, \ldots, x\_{49999}\right) \\
=P\left(x\_{1} \mid y\right) P\left(x\_{2} \mid y\right) P\left(x\_{3} \mid y\right) \cdots P\left(x\_{50000} \mid y\right) \\
=\prod\_{i=1}^{n} P\left(x\_{i} \mid y\right)
\end{array}\]

* The first equality simply follows from the usual properties of probabilities, and the second equality used the NB assumption. We note that even though the Naive Bayes assumption is an extremely strong assumptions, the resulting algorithm works well on many problems.
* Our model is parameterized by \(\phi\_{i \mid y=1}=P(x\_{i}=1 \mid y=1), \phi\_{i \mid y=0}=P(x\_{i}=1\mid y=0)\), and \(\phi\_{y}=P(y=1)\). As usual, given a training set \(\{(x^{(i)}, y^{(i)}); i=1, \ldots, m\}\), we can write down the joint likelihood of the data:

\[\mathcal{L}\left(\phi\_{y}, \phi\_{j \mid y=0}, \phi\_{j \mid y=1}\right)=\prod\_{i=1}^{m} P\left(x^{(i)}, y^{(i)}\right)\]

* Maximizing this with respect to \(\phi\_{y}, \phi\_{i \mid y=0}\) and \(\phi\_{i \mid y=1}\) gives the maximum likelihood estimates:

\[\begin{aligned}
\phi\_{j \mid y=1} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{j}^{(i)}=1 \wedge y^{(i)}=1\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\}} \\
\phi\_{j \mid y=0} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{j}^{(i)}=1 \wedge y^{(i)}=0\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=0\right\}} \\
\phi\_{y} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\}}{m}
\end{aligned}\]

* where,
  + the “\(\wedge\)” symbol means the “and” operation.
  + \(\mathbb{1}\{\cdot\}\) represents the indicator function which returns 1 if its argument is true, otherwise 0. In other words, the indicator of a true statement is equal to 1 while that of a false statement is equal to 0.
* The parameters have a very natural interpretation. For instance, \(\phi\_{j \mid y=1}\) is just the fraction of the spam \((y=1)\) emails in which word \(j\) does appear.
* Having fit all these parameters, to make a prediction on a new example with features \(x\), we then simply calculate

\[\begin{aligned}
P(y=1 \mid x) &=\frac{P(x \mid y=1) P(y=1)}{P(x)} \\
&=\frac{\left(\prod\_{i=1}^{n} P\left(x\_{i} \mid y=1\right)\right) P(y=1)}{\left(\prod\_{i=1}^{n} P\left(x\_{i} \mid y=1\right)\right) P(y=1)+\left(\prod\_{i=1}^{n} P\left(x\_{i} \mid y=0\right)\right) P(y=0)}
\end{aligned}\]

* and pick whichever class has the higher posterior probability. Lastly, we note that while we have developed the Naive Bayes algorithm mainly for the case of problems where the features \(x\_{i}\) are binary-valued, the generalization to where \(x\_{i}\) can take values in \(\left\{1,2, \ldots, k\_{i}\right\}\) is straightforward. Here, we would simply model \(P\left(x\_{i} \mid y\right)\) as multinomial rather than as Bernoulli. Indeed, even if some original input attribute (say, the living area of a house, as in our earlier example) were continuous valued, it is quite common to discretize it – that is, turn it into a small set of discrete values – and apply Naive Bayes. For instance, if we use some feature \(x\_{i}\) to represent living area, we might discretize the continuous values as follows:

\[\begin{array}{c|c|c|c|c|c}
\text { Living area (sq. feet) } & <400 & 400-800 & 800-1200 & 1200-1600 & >1600 \\
\hline x\_{i} & 1 & 2 & 3 & 4 & 5
\end{array}\]

* Thus, for a house with living area 890 square feet, we would set the value of the corresponding feature \(x\_{i}\) to 3. We can then apply the Naive Bayes algorithm, and model \(P\left(x\_{i} \mid y\right)\) with a multinomial distribution, as described previously. When the original, continuous-valued attributes are not wellmodeled by a multivariate normal distribution, discretizing the features and using Naive Bayes (instead of GDA) will often result in a better classifier.

### Laplace smoothing

* The Naive Bayes algorithm as we have described it will work fairly well for many problems, but there is a simple change that makes it work much better, especially for text classification. Let’s briefly discuss a problem with the algorithm in its current form, and then talk about how we can fix it.
* Consider spam/email classification, and let’s suppose that, after having done excellent work on an ML project, you decide to submit the work you did to the [NeurIPS](https://neurips.cc/) conference for publication, which is one of the top machine learning conferences.
* Because you end up discussing the conference in your emails, you also start getting messages with the word “neurips” in it. But this is your first NeurIPS paper, and until this time, you had not previously seen any emails containing the word “neurips”; in particular “neurips” did not ever appear in your training set of spam/non-spam emails. Assuming that “neurips” was the \(35000^{th}\) word in the dictionary, your Naive Bayes spam filter therefore had picked its maximum likelihood estimates of the parameters \(\phi\_{35000 \mid y}\) to be,

\[\begin{aligned}
\phi\_{35000 \mid y=1} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{35000}^{(i)}=1 \wedge y^{(i)}=1\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\}}=0 \\
\phi\_{35000 \mid y=0} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{35000}^{(i)}=1 \wedge y^{(i)}=0\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=0\right\}}=0
\end{aligned}\]

* i.e., because it has never seen “neurips” before in either spam or non-spam training examples, it thinks the probability of seeing it in either type of email is zero. Hence, when trying to decide if one of these messages containing “neurips” is spam, it calculates the class posterior probabilities, and obtains

\[\begin{aligned}
P(y=1 \mid x) &=\frac{\prod\_{i=1}^{n} P\left(x\_{i} \mid y=1\right) P(y=1)}{\prod\_{i=1}^{n} P\left(x\_{i} \mid y=1\right) P(y=1)+\prod\_{i=1}^{n} P\left(x\_{i} \mid y=0\right) P(y=0)} \\
&=\frac{0}{0}
\end{aligned}\]

* This is because each of the terms \(“\prod\_{i=1}^{n} P\left(x\_{i} \mid y\right)”\) includes a term \(P\left(x\_{35000} \mid y\right)=\) 0 that is multiplied into it. Hence, our algorithm obtains \(0 / 0\), and doesn’t know how to make a prediction.
* Stating the problem more broadly, it is statistically a bad idea to estimate the probability of some event to be zero just because you haven’t seen it before in your finite training set. Take the problem of estimating the mean of a multinomial random variable \(z\) taking values in \({1, \ldots, k}\). We can parameterize our multinomial with \(\phi\_{i}=P(z=i)\). Given a set of \(m\) independent observations \(\left\{z^{(1)}, \ldots, z^{(m)}\right\}\), the maximum likelihood estimates are given by

\[\phi\_{j}=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{z^{(i)}=j\right\}}{m}\]

* As we saw previously, if we were to use these maximum likelihood estimates, then some of the \(\phi\_{j}\)’s might end up as zero, which was a problem. To avoid this, we can use Laplace smoothing, which replaces the above estimate with

\[\phi\_{j}=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{z^{(i)}=j\right\}+1}{m+k}\]

* Here, we’ve added 1 to the numerator, and \(k\) to the denominator. Note that \(\sum\_{j=1}^{k} \phi\_{j}=1\) still holds (check this yourself!), which is a desirable property since the \(\phi\_{j}\)’s are estimates for probabilities that we know must sum to 1 . Also, \(\phi\_{j} \neq 0\) for all values of \(j\), solving our problem of probabilities being estimated as zero. Under certain (arguably quite strong) conditions, it can be shown that the Laplace smoothing actually gives the optimal estimator of the \(\phi\_{j}\)’s.
* Returning to our Naive Bayes classifier, with Laplace smoothing, we therefore obtain the following estimates of the parameters:

\[\begin{aligned}
\phi\_{j \mid y=1} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{j}^{(i)}=1 \wedge y^{(i)}=1\right\}+1}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\}+2} \\
\phi\_{j \mid y=0} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{x\_{j}^{(i)}=1 \wedge y^{(i)}=0\right\}+1}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=0\right\}+2}
\end{aligned}\]

* In practice, it usually doesn’t matter much whether we apply Laplace smoothing to \(\phi\_{y}\) or not, since we will typically have a fair fraction each of spam and non-spam messages, so \(\phi\_{y}\) will be a reasonable estimate of \(P(y=1)\) and will be quite far from 0 anyway.

### Event models for text classification

* To close off our discussion of generative learning algorithms, let’s talk about one more model that is specifically for text classification. While Naive Bayes as we’ve presented it will work well for many classification problems, for text classification, there is a related model that does even better.
* In the specific context of text classification, Naive Bayes as presented uses the what’s called the multi-variate Bernoulli event model. In this model, we assumed that the way an email is generated is that first it is randomly determined (according to the class priors \(P(y)\) whether a spammer or non-spammer will send you your next message. Then, the person sending the email runs through the dictionary, deciding whether to include each word in that email independently and according to the probabilities \(P\left(x\_{i}=1 \mid y\right)=\) \(\phi\_{i \mid y}\). Thus, the probability of a message was given by \(P(y) \prod\_{i=1}^{n} P\left(x\_{i} \mid y\right)\)
* Here’s a different model, called the multinomial event model. To describe this model, we will use a different notation and set of features for representing emails. We let \(x\_{i}\) denote the identity of the \(i^{th}\) word in the email. Thus, \(x\_{i}\) is now an integer taking values in \({1, \ldots,|V|}\), where \(|V|\) is the size of our vocabulary (dictionary).
* An email of \(n\) words is now represented by a vector \(\left(x\_{1}, x\_{2}, \ldots, x\_{n}\right)\) of length \(n\); note that \(n\) can vary for different documents. For instance, if an email starts with “A NeurIPS …” then \(x\_1=\mathbb{1}\left(“\mathrm{a}”\right)\). is the first word in the dictionary), and \(x\_{2}=35000\) (if “nips” is the \(35000^{th}\) word in the dictionary).
* In the multinomial event model, we assume that the way an email is generated is via a random process in which spam/non-spam is first determined (according to \(P(y)\) as before. Then, the sender of the email writes the email by first generating \(x\_{1}\) from some multinomial distribution over words \(\left(P\left(x\_{1} \mid y\right)\right)\). Next, the second word \(x\_{2}\) is chosen independently of \(x\_{1}\) but from the same multinomial distribution, and similarly for \(x\_{3}, x\_{4}\), and so on, until all \(n\) words of the email have been generated.
* Thus, the overall probability of a message is given by \(P(y) \prod\_{i=1}^{n} P\left(x\_{i} \mid y\right)\). Note that this formula looks like the one we had earlier for the probability of a message under the multi-variate Bernoulli event model, but that the terms in the formula now mean very different things. In particular \(x\_{i} \mid y\) is now a multinomial, rather than a Bernoulli distribution.
* The parameters for our new model are \(\phi\_{y}=P(y)\) as before, \(\phi\_{k \mid y=1}=\) \(P\left(x\_{j}=k \mid y=1\right)(\) for any \(j)\) and \(\phi\_{i \mid y=0}=P\left(x\_{j}=k \mid y=0\right)\). Note that we have assumed that \(P\left(x\_{j} \mid y\right)\) is the same for all values of \(j\) (i.e., that the distribution according to which a word is generated does not depend on its position \(j\) within the email).
* If we are given a training set \(\left\{\left(x^{(i)}, y^{(i)}\right) ; i=1, \ldots, m\right\}\) where \(x^{(i)}=\) \(\left(x\_{1}^{(i)}, x\_{2}^{(i)}, \ldots, x\_{n\_{i}}^{(i)}\right)\) (here, \(n\_{i}\) is the number of words in the \(i^{th}\) training example), the likelihood of the data is given by,

\[\begin{aligned}
\mathcal{L}\left(\phi, \phi\_{k \mid y=0}, \phi\_{k \mid y=1}\right) &=\prod\_{i=1}^{m} P\left(x^{(i)}, y^{(i)}\right) \\
&=\prod\_{i=1}^{m}\left(\prod\_{j=1}^{n\_{i}} P\left(x\_{j}^{(i)} \mid y ; \phi\_{k \mid y=0}, \phi\_{k \mid y=1}\right)\right) P\left(y^{(i)} ; \phi\_{y}\right)
\end{aligned}\]

* Maximizing this yields the maximum likelihood estimates of the parameters:

\[\begin{aligned}
\phi\_{k \mid y=1} &=\frac{\sum\_{i=1}^{m} \sum\_{j=1}^{n\_{i}} \mathbb{1}\left\{x\_{j}^{(i)}=k \wedge y^{(i)}=1\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\} n\_{i}} \\
\phi\_{k \mid y=0} &=\frac{\sum\_{i=1}^{m} \sum\_{j=1}^{n\_{i}} \mathbb{1}\left\{x\_{j}^{(i)}=k \wedge y^{(i)}=0\right\}}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=0\right\} n\_{i}} \\
\phi\_{y} &=\frac{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\}}{m}
\end{aligned}\]

* If we were to apply Laplace smoothing (which needed in practice for good performance) when estimating \(\phi\_{k \mid y=0}\) and \(\phi\_{k \mid y=1}\), we add 1 to the numerators and \(|V|\) to the denominators, and obtain:

\[\begin{aligned}
\phi\_{k \mid y=1} &=\frac{\sum\_{i=1}^{m} \sum\_{j=1}^{n\_{i}} \mathbb{1}\left\{x\_{j}^{(i)}=k \wedge y^{(i)}=1\right\}+1}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=1\right\} n\_{i}+|V|} \\
\phi\_{k \mid y=0} &=\frac{\sum\_{i=1}^{m} \sum\_{j=1}^{n\_{i}} \mathbb{1}\left\{x\_{j}^{(i)}=k \wedge y^{(i)}=0\right\}+1}{\sum\_{i=1}^{m} \mathbb{1}\left\{y^{(i)}=0\right\} n\_{i}+|V|}
\end{aligned}\]

* While not necessarily the very best classification algorithm, the Naive Bayes classifier often works surprisingly well. It is often also a very good first thing to try, given its simplicity and ease of implementation.

## Further reading

Here are some (optional) links you may find interesting for further reading:

* [Learning in graphical models](https://mitpress.mit.edu/books/learning-graphical-models) by Michael I. Jordan and [Generalized Linear Models](https://www.amazon.com/Generalized-Chapman-Monographs-Statistics-Probability/dp/0412317605) 2nd ed. by McCullagh and Nelder served as a major inspiration for our discussion on this topic.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledNaiveBayes,
  title   = {Naive Bayes},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS229: Machine Learning},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
