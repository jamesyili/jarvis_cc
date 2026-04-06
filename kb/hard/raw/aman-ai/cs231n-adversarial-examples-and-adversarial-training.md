# CS231n • Adversarial Examples and Adversarial Training

**Source:** https://aman.ai/cs231n/adversarial/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** computer-vision

---

* [What are adversarial examples?](#what-are-adversarial-examples)
* [How can adversarial examples compromise machine learning systems?](#how-can-adversarial-examples-compromise-machine-learning-systems)
* [Defenses](#defenses)
* [Using adversarial examples to improve machine learning](#using-adversarial-examples-to-improve-machine-learning)
* [Citation](#citation)

## What are adversarial examples?

* Since 2013, deep neural networks have matched human performance at..
  + Face recognition
  + Object recognition
  + Captcha recognition
    - Because its accuracy was higher than humans, Websites tried to find another solution than Captcha.
  + And other tasks..
* Before 2013 no body was surprised if they saw a computer made a mistake! But now the deep learning exists and its so important to know the problems and the causes.
* Adversarial are problems and unusual mistake that deep learning make.
* This topic wasn’t hot until deep learning can now do better and better than human!
* An adversarial is an example that has been carefully computed to to be misclassified.
* In a lot of cases the adversarial image isn’t changed much compared to the original image from the human perspective.
* History of recent papers:
  + Biggio [2013](https://link.springer.com/chapter/10.1007/978-3-642-40994-3_25): fool neural nets.
  + Szegedy et al 2013: fool ImageNet classifiers imperceptibly
  + Goodfellow et al [2014](https://arxiv.org/abs/1412.6572): cheap, closed form attack.
* So the first story was in 2013. When Szegedy had a CNN that can classify images very well.
  + He wanted to understand more about how CNN works to improve it.
  + He give an image of an object and by using gradient ascent he tried to update the images so that it can be another object.
  + Strangely he found that the result image hasn’t changed much from the human perspective!
  + If you tried it you won’t notify any change and you will think that this is a bug! but it isn’t if you go for the image you will notice that they are completely different!
* These mistakes can be found in almost any deep learning algorithm we have studied!
  + It turns out that RBF (Radial Basis Network) can resist this.
  + Deep Models for Density Estimation can resist this.
* Not just for neural nets can be fooled:
  + Linear models
    - Logistic regression
    - Softmax regression
    - SVMs
  + Decision trees
  + Nearest neighbors
* **How do adversarial examples come about?**
  + In the process in trying to understand what is happening, in 2016 they thought it was from overfitting models in the high dimensional data case.
    - Because in such high dimensions we could have some random errors which can be found.
    - So if we trained a model with another parameters it should not make the same mistake?
    - They found that not right. Models are reaching to the same mistakes so it doesn’t mean its overfitting.
  + In the previous mentioned experiment the found that the problem is caused by systematic thing not a random.
    - If they add some vector to an example it would misclassified to any model.
  + Maybe they are coming from underfitting not overfitting.
  + Modern deep nets are very piecewise linear
    - Rectified linear unit
    - Carefully tuned sigmoid `# Most of the time we are inside the linear curve`
    - Maxout
    - LSTM
  + Relation between the parameter and the output are non linear because it’s multiplied together thats what make training NN difficult, while mapping from linear from input and output are linear and much easier.

## How can adversarial examples compromise machine learning systems?

* If we are experimenting how easy a NN to fool, We want to make sure we are actually fooling it not just changing the output class, and if we are attackers we want to make this behavior to the NN (Get hole).
* When we build Adversarial example we use the max norm constrain to perturbation.
* The fast gradient sign method:
  + This method comes from the fact that almost all NN are using a linear activations (Like RELU) the assumption we have told before.
  + No pixel can be changed more than some amount epsilon.
  + Fast way is to take the gradient of the cost you used to train the network with respect to the input and then take the sign of that gradient multiply this by epsilon.
  + Equation:
    - `Xdash = x + epslion * (sign of the gradient)`
    - Where Xdash is the adversarial example and x is the normal example
  + So it can be detected by just using the sign (direction) and some epsilon.
* Some attacks are based on ADAM optimizer.
* Adversarial examples are not random noises!
* NN are trained on some distribution and behaves well in that distribution. But if you shift this distribution the NN won’t answer the right answers. They will be so easy to fool.
* deep RL can also be fooled.
* Attack of the weights:
  + In linear models, We can take the learned weights image, take the signs of the image and add it to any example to force the class of the weights to be true. Andrej Karpathy, “Breaking Linear Classifiers on ImageNet”
* It turns out that some of the linear models performs well (We cant get adversarial from them easily)
  + In particular Shallow RBFs network resist adversarial perturbation # By The fast gradient sign method
    - The problem is RBFs doesn’t get so much accuracy on the datasets because its just a shallow model and if you tried to get this model deeper the gradients will become zero in almost all the layers.
    - RBFs are so difficult to train even with batch norm. algorithm.
    - Ian thinks if we have a better hyper parameters or a better optimization algorithm that gradient decent we will be able to train RBFs and solve the adversarial problem!
* We also can use another model to fool current model. Ex use an SVM to fool a deep NN.
  + For more details follow the paper: “Papernot 2016”
* Transferability Attack
  1. Target model with unknown weights, machine learning algorithm, training set; maybe non differentiable
  2. Make your training set from this model using inputs from you, send them to the model and then get outputs from the model
  3. Train you own model. “Following some table from Papernot 2016”
  4. Create an Adversarial example on your model.
  5. Use these examples against the model you are targeting.
  6. You are almost likely to get good results and fool this target!
* In Transferability Attack to increase your probability by 100% of fooling a network, You can make more than just one model may be five models and then apply them. “(Liu et al, 2016)”
* Adversarial Examples are works for human brain also! for example images that tricks your eyes. They are a lot over the Internet.
* In practice some researches have fooled real models from (MetaMind, Amazon, Google)
* Someone has uploaded some perturbation into facebook and facebook was fooled :D

## Defenses

* A lot of defenses Ian tried failed really bad! Including:
  + Ensembles
  + Weight decay
  + Dropout
  + Adding noise at train time or at test time
  + Removing perturbation with an autoencoder
  + Generative modeling
* Universal approximator theorem
  + Whatever shape we would like our classification function to have a big enough NN can make it.
  + We could have train a NN that detects the Adversarial!
* Linear models & KNN can be fooled easier than NN. Neural nets can actually become more secure than other models. Adversarial trained neural nets have the best empirical success rate on adversarial examples of any machine learning model.
  + Deep NNs can be trained with non linear functions but we will just need a good optimization technique or solve the problem with using such linear activator like “RELU”

## Using adversarial examples to improve machine learning

* Universal engineering machine (model-based optimization) `#Is called Universal engineering machine by Ian`
  + For example:
    - Imagine that we want to design a car that are fast.
    - We trained a NN to look at the blueprints of a car and tell us if the blueprint will make us a fast car or not.
    - The idea here is to optimize the input to the network so that the output will max this could give us the best blueprint for a car!
  + Make new inventions by finding input that maximizes model’s predicted performance.
  + Right now by using adversarial examples we are just getting the results we don’t like but if we have solve this problem we can have the fastest car, the best GPU, the best chair, new drugs…..
* The whole adversarial is an active area of research especially defending the network!
* Conclusion
  + Attacking is easy
  + Defending is difficult
  + Adversarial training provides regularization and semi-supervised learning
  + The out-of-domain input problem is a bottleneck for model-based optimization generally
* There are a Github code that can make you learn everything about adversarial by code (Built above tensorflow):
  + An adversarial example library for constructing attacks, building defenses, and benchmarking both: https://github.com/tensorflow/cleverhans

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020AdversarialExamples,
  title   = {Adversarial Examples and Adversarial Training},
  author  = {Chadha, Aman},
  journal = {Distilled Notes for Stanford CS231n: Convolutional Neural Networks for Visual Recognition},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
