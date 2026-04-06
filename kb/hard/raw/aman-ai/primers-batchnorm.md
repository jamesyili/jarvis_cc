# Primers • Batchnorm

**Source:** https://aman.ai/primers/ai/batchnorm/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Introduction](#introduction)
* [The problem of Internal Covariate Shift](#the-problem-of-internal-covariate-shift)
* [Standardize Layer Inputs](#standardize-layer-inputs)
* [How to Standardize Layer Inputs](#how-to-standardize-layer-inputs)
* [Examples of Using Batch Normalization](#examples-of-using-batch-normalization)
* [Summary: BatchNorm during Training vs. Testing/Inference](#summary-batchnorm-during-training-vs-testinginference)
  + [BatchNorm during Training:](#batchnorm-during-training)
  + [BatchNorm during Testing (Inference):](#batchnorm-during-testing-inference)
  + [Why the Distinction?](#why-the-distinction)
* [Tips for Using Batch Normalization](#tips-for-using-batch-normalization)
  + [Use With Different Network Types](#use-with-different-network-types)
  + [Probably Use Before the Activation](#probably-use-before-the-activation)
  + [Use Large Learning Rates](#use-large-learning-rates)
  + [Less Sensitive to Weight Initialization](#less-sensitive-to-weight-initialization)
  + [Alternate to Data Preparation](#alternate-to-data-preparation)
  + [Don’t Use With Dropout](#dont-use-with-dropout)
* [RMSNorm](#rmsnorm)
* [FAQs](#faqs)
  + [Does BatchNorm lead to a standard normal distribution among layer outputs?](#does-batchnorm-lead-to-a-standard-normal-distribution-among-layer-outputs)
  + [Related: Does LayerNorm seek to obtain a normal distribution at the output of a layer?](#related-does-layernorm-seek-to-obtain-a-normal-distribution-at-the-output-of-a-layer)
  + [Does BatchNorm normalize at a “per-feature” level?](#does-batchnorm-normalize-at-a-per-feature-level)
* [Further Reading](#further-reading)
  + [Books](#books)
  + [Papers](#papers)
  + [Articles](#articles)
* [Key takeaways](#key-takeaways)
* [Citation](#citation)

## Introduction

* Training deep neural networks with tens of layers is challenging as they can be sensitive to the initial random weights and configuration of the learning algorithm.
* One possible reason for this difficulty is the distribution of the inputs to layers deep in the network may change after each mini-batch when the weights are updated. This can cause the learning algorithm to forever chase a moving target. This change in the distribution of inputs to layers in the network is referred to the technical name “internal covariate shift.”
* Batch normalization (BatchNorm) is a popular technique in deep learning for training very deep neural networks that standardizes the inputs to a layer for each mini-batch (in other words, normalizes the activations of neurons in a network). This has the effect of stabilizing the learning process and speeding up the convergence of training by dramatically reducing the number of training epochs required to train deep networks.
* In this article, you will discover the batch normalization method used to accelerate the training of deep learning neural networks.

## The problem of Internal Covariate Shift

* Training deep neural networks, e.g. networks with tens of hidden layers, is challenging.
* One aspect of this challenge is that the model is updated layer-by-layer backward from the output to the input using an estimate of error that assumes the weights in the layers prior to the current layer are fixed.

> Very deep models involve the composition of several functions or layers. The gradient tells how to update each parameter, under the assumption that the other layers do not change. In practice, we update all of the layers simultaneously. — Page 317, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

* Because all layers are changed during an update, the update procedure is forever chasing a moving target.
* For example, the weights of a layer are updated given an expectation that the prior layer outputs values with a given distribution. This distribution is likely changed after the weights of the prior layer are updated.

> Training Deep Neural Networks is complicated by the fact that the distribution of each layer’s inputs changes during training, as the parameters of the previous layers change. This slows down the training by requiring lower learning rates and careful parameter initialization, and makes it notoriously hard to train models with saturating nonlinearities. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* The authors of the paper introducing batch normalization refer to change in the distribution of inputs during training as “internal covariate shift.”

> We refer to the change in the distributions of internal nodes of a deep network, in the course of training, as Internal Covariate Shift. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

## Standardize Layer Inputs

* Batch normalization, or batchnorm for short, proposed in [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167) by Ioffe and Szegedy (2015) as a technique to help coordinate the update of multiple layers in the model.

> Batch normalization provides an elegant way of reparametrizing almost any deep network. The reparametrization significantly reduces the problem of coordinating updates across many layers. — Page 318, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

* It does this scaling the output of the layer, specifically by standardizing the activations of each input variable per mini-batch, such as the activations of a node from the previous layer. Recall that standardization refers to rescaling data to have a mean of zero and a standard deviation of one, e.g. a standard Gaussian.

> Batch normalization reparametrizes the model to make some units always be standardized by definition. — Page 319, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

* This process is also called “whitening” when applied to images in computer vision.

> By whitening the inputs to each layer, we would take a step towards achieving the fixed distributions of inputs that would remove the ill effects of the internal covariate shift. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* Standardizing the activations of the prior layer means that assumptions the subsequent layer makes about the spread and distribution of inputs during the weight update will not change, at least not dramatically. This has the effect of stabilizing and speeding-up the training process of deep neural networks.

> Batch normalization acts to standardize only the mean and variance of each unit in order to stabilize learning, but allows the relationships between units and the nonlinear statistics of a single unit to change. - Page 320, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

* Normalizing the inputs to the layer has an effect on the training of the model, dramatically reducing the number of epochs required. It can also have a regularizing effect, reducing generalization error much like the use of activation regularization.

> Batch normalization can have a dramatic effect on optimization performance, especially for convolutional networks and networks with sigmoidal nonlinearities. — Page 425, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

* Although reducing “internal covariate shift” was a motivation in the development of the method, there is some suggestion that instead batch normalization is effective because it smooths and, in turn, simplifies the optimization function that is being solved when training the network.

> … BatchNorm impacts network training in a fundamental way: it makes the landscape of the corresponding optimization problem be significantly more smooth. This ensures, in particular, that the gradients are more predictive and thus allow for use of larger range of learning rates and faster network convergence. — How Does Batch Normalization Help Optimization? (No, It Is Not About Internal Covariate Shift), 2018.

## How to Standardize Layer Inputs

* Batch normalization can be implemented during training by calculating the mean and standard deviation of each input variable to a layer per mini-batch and using these statistics to perform the standardization.
* Alternately, a running average of mean and standard deviation can be maintained across mini-batches, but may result in unstable training.

> It is natural to ask whether we could simply use the moving averages […] to perform the normalization during training […]. This, however, has been observed to lead to the model blowing up. — Batch Renormalization: Towards Reducing Minibatch Dependence in Batch-Normalized Models, 2017.

* After training, the mean and standard deviation of inputs for the layer can be set as mean values observed over the training dataset. The Batchnorm algorithm is as shown below (diagram taken from [Ioffe and Szegedy](https://arxiv.org/abs/1502.03167), 2015).

* For small mini-batch sizes or mini-batches that do not contain a representative distribution of examples from the training dataset, the differences in the standardized inputs between training and inference (using the model after training) can result in noticeable differences in performance. This can be addressed with a modification of the method called Batch Renormalization (or BatchRenorm for short) that makes the estimates of the variable mean and standard deviation more stable across mini-batches.

> Batch Renormalization extends batchnorm with a per-dimension correction to ensure that the activations match between the training and inference networks. — Batch Renormalization: Towards Reducing Minibatch Dependence in Batch-Normalized Models, 2017.

* This standardization of inputs may be applied to input variables for the first hidden layer or to the activations from a hidden layer for deeper layers.
* In practice, it is common to allow the layer to learn two new parameters, namely a new mean and standard deviation, \(\beta\) and \(\gamma\) respectively, that allow the automatic scaling and shifting of the standardized layer inputs. These parameters are learned by the model as part of the training process.

> Note that simply normalizing each input of a layer may change what the layer can represent. […] These parameters are learned along with the original model parameters, and restore the representation power of the network. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* Importantly the backpropagation algorithm is updated to operate upon the transformed inputs, and error is also used to update the new scale and shifting parameters learned by the model.
* The standardization is applied to the inputs to the layer, namely the input variables or the output of the activation function from the prior layer. Given the choice of activation function, the distribution of the inputs to the layer may be quite non-Gaussian. In this case, there may be benefit in standardizing the summed activation before the activation function in the previous layer.

> We add the BN transform immediately before the nonlinearity […] We could have also normalized the layer inputs \(u\), but since \(u\) is likely the output of another nonlinearity, the shape of its distribution is likely to change during training, and constraining its first and second moments would not eliminate the covariate shift. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

## Examples of Using Batch Normalization

* This section provides a few examples of milestone papers and popular models that make use of batch normalization.
* In the 2015 paper that introduced the technique titled “[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167),” the authors Sergey Ioffe and Christian Szegedy from Google demonstrated a dramatic speedup of an Inception-based convolutional neural network for photo classification over a baseline method.

> By only using Batch Normalization […], we match the accuracy of Inception in less than half the number of training steps.

* Kaiming He, et al. in their 2015 paper titled [“Deep Residual Learning for Image Recognition”](https://arxiv.org/abs/1512.03385) used batch normalization after the convolutional layers in their very deep model referred to as ResNet and achieve then state-of-the-art results on the ImageNet dataset, a standard photo classification task.

> We adopt batch normalization (BN) right after each convolution and before activation …

* Christian Szegedy, et al. from Google in their 2016 paper titled [“Rethinking the Inception Architecture for Computer Vision”](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.html) used batch normalization in their updated inception model referred to as GoogleNet Inception-v3, achieving then state-of-the-art results on the ImageNet dataset.

> BN-auxiliary refers to the version in which the fully connected layer of the auxiliary classifier is also batch-normalized, not just the convolutions.

* Dario Amodei from Baidu in their 2016 paper titled [“Deep Speech 2 : End-to-End Speech Recognition in English and Mandarin”](http://proceedings.mlr.press/v48/amodei16.html) use a variation of batch normalization recurrent neural networks in their end-to-end deep model for speech recognition.

> … we find that when applied to very deep networks of RNNs on large data sets, the variant of BatchNorm we use substantially improves final generalization error in addition to accelerating training.

## Summary: BatchNorm during Training vs. Testing/Inference

* To summarize how BatchNorm operates differs between the training and testing (or inference) phases. Let’s break down these differences:

### BatchNorm during Training:

* **Compute Mean and Variance**: For each feature in the mini-batch, compute the mean and variance.
  + \[\mu\_{batch} = \frac{1}{m} \sum\_{i=1}^{m} x\_i\]
  + \[\sigma\_{batch}^2 = \frac{1}{m} \sum\_{i=1}^{m} (x\_i - \mu\_{batch})^2\]

  where \(x\_i\) is the feature vector of a single data point, and \(m\) is the number of data points in the mini-batch.
* **Normalize**: Normalize the activations using the computed mean and variance:
  + \[\hat{x}\_i = \frac{x\_i - \mu\_{batch}}{\sqrt{\sigma\_{batch}^2 + \epsilon}}\]

  where \(\epsilon\) is a small constant added for numerical stability.
* **Scale and Shift**: This is a crucial step which allows the model to learn the optimal scale and mean for each feature. Two learnable parameters, gamma (\(\gamma\)) and beta (\(\beta\)), are introduced.
  + \[y\_i = \gamma \hat{x}\_i + \beta\]
* **Update Running Statistics**: To use during inference, maintain a running mean and variance (usually via an exponential moving average) of the features during training. These statistics are updated every time a batch is processed.

### BatchNorm during Testing (Inference):

* **Use Running Statistics**: Instead of computing the mean and variance for the current batch of data (which might not make sense, especially if you’re processing one example at a time), use the running mean and variance statistics computed during training.
* **Normalize**: Normalize the activations using the running mean and variance:
  + \[\hat{x}\_i = \frac{x\_i - \mu\_{running}}{\sqrt{\sigma\_{running}^2 + \epsilon}}\]
* **Scale and Shift**: Use the learned gamma (\(\gamma\)) and beta (\(\beta\)) values from training to scale and shift the normalized activations:
  + \[y\_i = \gamma \hat{x}\_i + \beta\]

### Why the Distinction?

* BatchNorm’s behavior difference between training and testing ensures a few things:

  + **Stability**: Using running statistics during inference ensures that the network behaves more predictably. If we were to normalize using batch statistics during inference, the network’s output could vary significantly based on the composition and size of the input batch.
  + **Scalability**: During inference, you might not always have a “batch” of data. Sometimes, you might want to make predictions for a single data point. Using running statistics from training allows you to do this without any issues.
* In frameworks like TensorFlow and PyTorch, the distinction between training and inference for BatchNorm is handled automatically as long as you appropriately set the model’s mode (`model.train()` vs. `model.eval()` in PyTorch, for instance).

## Tips for Using Batch Normalization

* This section provides tips and suggestions for using batch normalization with your own neural networks.

### Use With Different Network Types

* Batch normalization is a general technique that can be used to normalize the inputs to a layer.
* It can be used with most network types, such as Multilayer Perceptrons, Convolutional Neural Networks and Recurrent Neural Networks.

### Probably Use Before the Activation

* Batch normalization may be used on the inputs to the layer before or after the activation function in the previous layer.
* It may be more appropriate **after** the activation function if for s-shaped functions like the hyperbolic tangent and logistic function.
* It may be appropriate **before** the activation function for activations that may result in non-Gaussian distributions like the rectified linear activation function (ReLU), the modern default for most network types.

> The goal of Batch Normalization is to achieve a stable distribution of activation values throughout training, and in our experiments we apply it before the nonlinearity since that is where matching the first and second moments is more likely to result in a stable distribution. - [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* Perhaps test both approaches with your network.

### Use Large Learning Rates

* Using batch normalization makes the network more stable during training.
* This may require the use of much larger than normal learning rates, that in turn may further speed up the learning process.

> In a batch-normalized model, we have been able to achieve a training speedup from higher learning rates, with no ill side effects — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* The faster training also means that the decay rate used for the learning rate may be increased.

### Less Sensitive to Weight Initialization

* Deep neural networks can be quite sensitive to the technique used to initialize the weights prior to training.
* The stability to training brought by batch normalization can make training deep networks less sensitive to the choice of weight initialization method.

### Alternate to Data Preparation

* Batch normalization could be used to standardize raw input variables that have differing scales.
* If the mean and standard deviations calculated for each input feature are calculated over the mini-batch instead of over the entire training dataset, then the batch size must be sufficiently representative of the range of each variable.
* It may not be appropriate for variables that have a data distribution that is highly non-Gaussian, in which case it might be better to perform data scaling as a pre-processing step.

### Don’t Use With Dropout

* Batch normalization offers some regularization effect, reducing generalization error, perhaps no longer requiring the use of dropout for regularization.

> Removing Dropout from Modified BN-Inception speeds up training, without increasing overfitting. — [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015.

* Further, it may not be a good idea to use batch normalization and dropout in the same network.
* The reason is that the statistics used to normalize the activations of the prior layer may become noisy given the random dropping out of nodes during the dropout procedure.

> Batch normalization also sometimes reduces generalization error and allows dropout to be omitted, due to the noise in the estimate of the statistics used to normalize each variable. — Page 425, [Deep Learning](https://amzn.to/2NJW3gE), 2016.

## RMSNorm

* RMSNorm is a normalization technique designed for deep networks. Like other normalization methods such as Batch Normalization and Layer Normalization, the goal of RMSNorm is to stabilize and potentially accelerate the training of deep neural networks.
* RMSNorm works by normalizing the root mean square (RMS) of the activations. The key formula for RMSNorm is:

\[y=\frac{x}{\sqrt{\frac{1}{N} \sum\_{i=1}^N x\_i^2+\epsilon}+b}\]

* where:
  + \(y\) is the output after normalization.
  + \(x\) is the input activation.
  + \(N\) is the number of elements in $x$.
  + \(\epsilon\) is a small constant to prevent division by zero.
  + \(b\) is a bias term.
* This normalization technique is relatively simple and does not require maintaining moving averages like in Batch Normalization, making the implementation straightforward. The method scales the activations by the inverse of their RMS value, which can help in stabilizing the magnitudes of activations throughout the network.
* When considering RMSNorm or any other normalization technique, it’s essential to test it in the context of your specific application and compare its performance to other methods to determine its suitability.

## FAQs

### Does BatchNorm lead to a standard normal distribution among layer outputs?

* Batch Normalization (BatchNorm) in deep learning does not directly lead to a standard normal distribution among layer outputs, but it does move the outputs closer to a normal distribution. The primary purpose of BatchNorm is to normalize the inputs of each layer, i.e., to shift and scale the inputs so that they have a mean of zero and a standard deviation of one. This is somewhat similar to a standard normal distribution.
* Here’s a breakdown of how BatchNorm works and its effects:
  1. **Normalizing Layer Inputs:** BatchNorm normalizes the inputs for each mini-batch. This normalization is done per feature (i.e., independently for each channel in the case of CNNs or each feature in fully connected layers). The normalization ensures that the mean of the inputs is close to 0 and the variance is close to 1.
  2. **Learnable Parameters:** After normalization, BatchNorm introduces two learnable parameters for each feature: a scale factor (\(\gamma\)) and a shift factor (\(\beta\)). These parameters allow the network to scale and shift the normalized feature and even to undo the normalization if that is what the learned behavior dictates, providing flexibility to learn if normalization is beneficial for that specific feature. This means the layer can learn the optimal scale and mean of the inputs for the activations.
  3. **Improving Training Stability:** By normalizing the inputs, BatchNorm helps in stabilizing the learning process and reduces the sensitivity of the network to the initial weights and learning rate.
  4. **Effect on Distribution:** While BatchNorm makes the inputs to a layer more normalized, it does not force them to strictly follow a standard normal distribution (mean 0, variance 1). The actual distribution of layer outputs can vary depending on the data, the network architecture, and the stage of training. BatchNorm ensures that the distribution of the inputs to each layer does not change drastically during training, which is known as reducing internal covariate shift.
  5. **Impact on Training and Activation Functions:** BatchNorm helps in stabilizing the learning process by ensuring that the distribution of inputs to each layer does not change drastically during training, a concept known as reducing internal covariate shift. BatchNorm can also make non-linear activation functions (like sigmoid or tanh) work more effectively by preventing the inputs from falling into the saturated regions of the function.
* In summary, BatchNorm helps in normalizing the inputs to each layer, making them have properties similar to a standard normal distribution, but it does not enforce a strict standard normal distribution. The learnable parameters in BatchNorm give the network flexibility to learn the most effective distribution of inputs for each layer.

### Related: Does LayerNorm seek to obtain a normal distribution at the output of a layer?

* Layer Normalization (LayerNorm) does not specifically seek to obtain a normal distribution at the output of a layer. Instead, its primary goal is to normalize the inputs across the features for each data sample independently. This means that for each sample in a batch, LayerNorm computes the mean and variance used for normalization across the features (i.e., across the neurons in a layer).
* The normalization process involves subtracting the mean and dividing by the standard deviation, which could make the data more normally distributed in a statistical sense. However, the main intent of LayerNorm is to stabilize the learning process and to help with faster convergence during training of deep neural networks, rather than enforcing a strict normal distribution of the layer outputs.
* This stabilization is achieved by reducing the internal covariate shift, which refers to the change in the distribution of network activations due to the change in network parameters during training. LayerNorm, like other normalization techniques, makes the training process less sensitive to the learning rate and other hyper-parameters and can lead to improved generalization performance in deep learning models.

### Does BatchNorm normalize at a “per-feature” level?

* BatchNorm normalizes is indeed applied normalization is done per feature” in the context of Batch Normalization (BatchNorm) in deep learning, it refers to how the normalization process is applied independently to each feature within a batch of data.
* To elaborate:
  1. **Definition of a Feature:** In deep learning, a “feature” typically refers to a single measurable property or characteristic of the data. For instance:
     + In a Convolutional Neural Network (CNN), a “feature” typically refers to the output of a filter applied to the input. When working with images, these features correspond to different aspects of the image, such as edges, textures, or colors. Specifically, in the context of image data, a feature often corresponds to a specific channel at a particular layer. For example, in an RGB image, there are three primary channels: Red, Green, and Blue.
     + In a fully connected layer, a feature refers to an individual neuron’s input or output.
  2. **Treating Channels as Features in Image Data:** In the case of image data in CNNs, treating each channel output of a filter as a feature for BatchNorm is more effective than treating each individual pixel as a feature. This approach maintains the spatial structure of image data and recognizes the importance of spatial correlations.
  3. **Normalization Process:** BatchNorm normalizes the data for each feature (or channel) separately. This means that for each filter output (channel at that layer), BatchNorm calculates the mean and variance across the mini-batch. The steps are:
     + **Compute Mean and Variance:** For a given feature, calculate the mean and variance across all the samples in the mini-batch. This calculation is not across the entire dataset but just the current batch of data being processed.
     + **Normalize:** Subtract the mean and divide by the standard deviation (derived from the variance) for each feature. This step ensures that this particular feature (across all the samples in the batch) now has a mean close to zero and a standard deviation close to one.
  4. **Per Feature Processing:** This per-feature processing means that each feature (like each filter/channel output in an image or each neuron in a layer) is normalized independently of other features. This is crucial because different features can have different scales and ranges. Normalizing them individually allows the model to treat each feature on a comparable scale.
  5. **Batch Dependent:** The normalization is dependent on the batch, which means it can vary from one batch of data to the next. During training, this can add a form of noise to the learning process, which can actually help with generalization.
  6. **Learnable Parameters:** After normalization, BatchNorm introduces two learnable parameters for each feature: a scale factor and a shift factor. These parameters allow the network to scale and shift the normalized feature, thus providing the flexibility for the network to learn if it actually benefits from the normalization or not.
* This per-feature normalization is a key aspect of BatchNorm and is instrumental in stabilizing the training process, accelerating convergence, and improving the overall performance of deep neural networks.

## Further Reading

* This section provides more resources on the topic if you are looking to go deeper.

### Books

* Section – 8.7.1 Batch Normalization, [Deep Learning](https://amzn.to/2NJW3gE), 2016
* Section 7.3.1. Advanced architecture patterns, [Deep Learning With Python](https://amzn.to/2wVqZDq), 2017

### Papers

* [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167), 2015
* [Batch Renormalization: Towards Reducing Minibatch Dependence in Batch-Normalized Models](https://arxiv.org/abs/1702.03275), 2017
* [How Does Batch Normalization Help Optimization? (No, It Is Not About Internal Covariate Shift)](https://arxiv.org/abs/1805.11604), 2018

### Articles

* [Batch normalization, Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization)
* [Why Does Batch Norm Work?, deeplearning.ai](https://www.youtube.com/watch?v=nUUqwaxLnWs), Video
* [Batch Normalization](https://www.youtube.com/watch?v=Xogn6veSyxA), OpenAI, 2016
* [Batch Normalization before or after ReLU?, Reddit](https://www.reddit.com/r/MachineLearning/comments/67gonq/d_batch_normalization_before_or_after_relu/)

## Key takeaways

* In this post, you discovered the batch normalization method used to accelerate the training of deep learning neural networks.
* Specifically, you learned:

  + Deep neural networks are challenging to train, not least because the input from prior layers can change after weight updates.
  + Batch normalization is a technique to standardize the inputs to a network, applied to ether the activations of a prior layer or inputs directly.
  + Batch normalization accelerates training, in some cases by halving the epochs or better, and provides some regularization, reducing generalization error.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledBatchNorm,
  title   = {Batchnorm},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
