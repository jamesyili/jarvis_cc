# CNNs for Visual Recognition

**Source:** https://aman.ai/cs231n/test/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** computer-vision

---

# CNNs for Visual Recognition

```
Stanford CS2 31 n
```

## Matt Deitke

```
Last updated: February 15, 2020
```

# Acknowledgements

This set of notes follows the lectures from Stanford’s graduate-level course on computer
vision, CS231n: Convolutional Neural Networks for Visual Recognition. The course is
taught by Fei-Fei Li, Justin Johnson, and Serena Yeung, and originally developed by
Andrej Karpathy. The cover art neural network was created with the PlotNeuralNet
package. With some exceptions and modifications for correctness, many of the photos used
come from the lecture slides or papers referenced in the caption. The course website is
cs231n.stanford.edu.

```
i
```

## Contents

* 1 Introduction to computer vision
* 2 Image classification
  + 2.1 KNN: K-nearest neighbors
  + 2.2 Linear classifiers
* 3 Loss functions and optimization
  + 3.1 Multiclass SVM loss (“Hinge loss”)
  + 3.2 Softmax classifier (multinomial logistic regression)
  + 3.3 Optimization
  + 3.4 Image features
* 4 Introduction to neural networks
  + 4.1 Computational graphs
  + 4.2 Backpropagation
    - 4.2.1 Gradients of vectors and matricies
    - 4.2.2 Modularized implementation
  + 4.3 Neural Networks
    - 4.3.1 Introduction
    - 4.3.2 Connection to the brain
* 5 CNNs: Convolutional neural networks
  + 5.1 The history of neural networks
  + 5.2 Convolutional neural networks
  + 5.3 Spatial dimensions
  + 5.4 Pooling layers
* 6 Training neural networks I
  + 6.1 Activation functions
    - 6.1.1 Sigmoid activation function
    - 6.1.2 Hyperbolic tangent activation function
    - 6.1.3 ReLU: Rectified linear unit
    - 6.1.4 Leaky ReLU, PReLU, and ELU CONTENTS iii
    - 6.1.5 Maxout neuron
  + 6.2 Data preprocessing
  + 6.3 Weight initialization
  + 6.4 Batch normalization
* 7 Training neural networks II
  + 7.1 Optimization
    - 7.1.1 Problems with stochastic gradient descent (SGD)
    - 7.1.2 SGD with momentum
    - 7.1.3 Nesterov momentum
    - 7.1.4 AdaGrad
    - 7.1.5 RMSProp
    - 7.1.6 Adam optimization
    - 7.1.7 More on learning rates
    - 7.1.8 Second-order optimization
    - 7.1.9 Model Ensembles
  + 7.2 Regularization
    - 7.2.1 Dropout regularization
    - 7.2.2 Data augmentation
  + 7.3 Transfer learning
* 8 Deep learning hardware and software
  + 8.1 CPU, GPU, and TPU
  + 8.2 Deep learning frameworks
    - 8.2.1 PyTorch
    - 8.2.2 TensorFlow
* 9 CNN Architectures
  + 9.1 AlexNet
  + 9.2 ZFNet
  + 9.3 VGGNet
  + 9.4 GoogLeNet
  + 9.5 ResNet
  + 9.6 Comparisons between network architectures
  + 9.7 Additional architectures
    - 9.7.1 NiN: Network in Network
    - 9.7.2 Improving ResNets
    - 9.7.3 FractalNet
    - 9.7.4 DenseNet
    - 9.7.5 SqueezeNet
* 10 RNNs: Recurrent neural networks iv CONTENTS
  + 10.1 Introduction
  + 10.2 Image captioning
* Bibliography

Chapter 1

## 1 Introduction to computer vision

Computer vision, at its core, attempts to have a computer learn about images. With the
increasing amount of image data we now have access to, computer vision has heated up as
a field of study because of its broad applications. Much of this new data is due to cameras
going on a lot more devices, such as smartphones, drones, and cars. To put the amount of
data we have access to in perspective, Cisco predicted in its visual networking index that
by 2022, around 82% of internet traffic will be caused by videos. From YouTube alone,
500 hours of new content is produced each minute (as of 2019). Humans alone fall short
of being able to monitor even a small portion of this data, which is why it is crucial to
develop algorithms to analyze this data. The field of computer vision touches on many
other fields, such as neuroscience, optics, NLP, robotics, machine learning, graphics, image
processing, and cognitive sciences and is at the cross section of many broader topics such as
mathematics, computer science, psychology, biology, physics, and engineering.

Around 540 million years ago, animals began to appear on the planet. At the time, the
planet mainly consisted mainly of water, and these animals would eat by sensing that there
was food near them and grabbing it. In the relatively short 10 million year period that
followed, the number of animal species grew from only a few to hundreds of thousands.
This ten year period is known as evolutions big bang. Over time, theories began to arise
as to why this event happened, and more recently, Andrew Parker gave the most plausable
reason, which stated that evolutions big bang occured because animals began to have vision
[1]. Once animals began to see, they could more easily find and go after pray. This forced
species to evolve quickly due only having the most advanced species survive.

```
Figure 1. 0. 1 : Fossils of animals that existed around 540 million years ago.
```

The way vision worked in the earliest of animals led to the development of the camera in
the mid 1550s. This first camera was known as camera obscura and worked with a pinhole
capturing the source then projecting that source. Now, cameras have evolved to the point
that it is likely that there are more cameras on earth than there are humans.

##### 1

##### 2 CHAPTER 1. INTRODUCTION TO COMPUTER VISION

```
Figure 1. 0. 2 : Work from 1544 on the creation of the pinhole image or camera obscura.
```

More recently, biologists have studied how the brain processes information and in 1959
Hubel and Wiesel published a paper that forms much of the methodology as to how we
work with computer vision today. In particular, they modeled that human visual cortex by
putting sensors into a cats visual cortex and observing the responses of the neurons. What
they found, in the millions of cells that for a pathway to make up the visual cortex, was
that earlier cells along the pathway represented simple information, such as detecting edges,
and deeper cells represented more complex information that eventually allowed the visual
cortex to detect objects and behave intelligently in the world [2].

```
Figure 1. 0. 3 : Hubel and Wiesel cat experiment.
```

At around the same time of the findings from Hubel and Wiesel, the field of computer vision
began. From many accounts, the first Ph.D. thesis in the field came from Larry Roberts in
1963, in which he attempted to reconstruct and recognize primitive shapes in a simulated
world [3]. A few years later, in 1966, the artificial intelligence group at Massachusetts
Institute of Technology propsed The Summer Vision Project, in which they stated they
wanted to “use our summer workers effectively [in order to construct] a significant part of
a visual system” [4]. It is safe to say that this project was a little ambitious, although from
that time until present day, many significant developments have occurred in computer vision
and pattern recognition.

In the 1970s, researchers began to move beyond focusing on extracting information from a
simulated environment made up of geometric primitives and moved onto working to rep-
resent everyday objects. Some of the most significant work during this time period came
from finding ways to break objects up into multiple pieces, using techniques like generalized
cylinders or creating a pictorial structure as shown in Figure 1.0.4 [5, 6].

In 1982, David Marr published a book describing Marr’s framework. His framework de-
scribes the process of how to represent visual information, where starting with an input
image, we detect the edges, curves, boundaries, and other low level details of the image.
With the low level details, we can then extract what is known as a 21 / 2 -D sketch in which
we take apart the pieces of an image based on depth. With all the pieces takeapart, we can

##### 3

```
(a) Generalized cylinder [5] (b) Pictorial structure [6]
```

Figure 1. 0. 4 : Different ways of representing an object using a generalized cylinder and pictorial
structure.

then form a 3-D model for each piece using geometric primitives [7]. Later in the 1980s,
researchers began to develop novel ways of finding edges in an image, and using those edges
to help recognize the image [8, 9].

### Input image Edge image 2 - D sketch 3 - D model

```
Figure 1. 0. 5 : The Marr framework, which describes the process of visual representation.
```

All of the approaches described thusfar do not truly get at the task of identifying images
developing vision on a computer. So, in the late 1990s, researchers began to focus on image
segmentation as a starting point for computer vision. Image segmentation breaks up the
image into multiple groups, where each group rpresents a component of the image [10]. For
example, a self-driving car would segment an image based on pedestrians, other cars, street
lights, and other objects on the road.

```
Figure 1. 0. 6 : Original image (left) with the segmented image (right).
```

At the start of the 2000s, statistical machine learning methods were explored most heavily
by researchers in computer vision. During this time, the first significant face detection
algorithm came onto the scene from Paul Viola and Michael Jones, where they used boosting
for a real-time detection algorithm with relatively cheap computing power [11]. This work
led to cameras having face detectors within just a couple of years.

##### 4 CHAPTER 1. INTRODUCTION TO COMPUTER VISION

The study of object recognition, in general, has shown to be a very difficult task because of
the variance that between two images that can represent the same object. One approach to
the task was introduced by David Lowe in 1999, where he attempted to match individual
features in two images of the same object, regardless of the variance between the images.
This method is known as object recognition with scale-invariant features (SIFT) [12]. Similar
work of using the features in an image to identify the entire image has occurred in human
recognition tasks [13, 14].

```
Figure 1. 0. 7 : Identifying features on two images of the same object with different variance.
```

As the field of computer vision has progressed, computers and cameras have advanced
rapidly, allowing us to work with more and high-quality images. In the 2000s, benchmarks
data sets began to become widely adapted to test different types of learning algorithms in
the task of object recognition. One data set that became a popular benchmark during this
time was the PASCAL data set, which consisted of 20 different object categories [15].

```
Airplane
```

```
Train
```

```
Person
```

Figure 1. 0. 8 : A few PASCAL database instances (left) and the performance of state-of-the-art
algorithms against the database (right).

More recently, it has been shown that smaller databases of just a couple thousand instances
cannot easily cause overfitting in a model and these state-of-the-art approaches fail on easier
tasks with more variance [16]. For this reason, researchers set out on to create the largest
possible data set they could to represent every object category that appears in the world.
The primary data set to achieve this task was called ImageNet and consisted of 22 thousand
categories with a total of 14 million images [17]. With the creation of ImageNet came a
challenge to the research community to develop the best algorihtms with the benchmark
being that the top 5 guesses from the algorithm contains the correct class. This led to
the seminal work by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in 2012, that
came to be known as AlexNet, where they showed that convolutional neural networks far
outperformed any other image recognition algorithms, and led to a surge of research in
artificial intelligence, because of how much it blew away the other state-of-the-art approaches
[18]. Since AlexNet was published, object recognition algorithms has began to outperform
human-level vision as shown in Figure 1.0.9.

##### 5

Figure 1. 0. 9 : ImageNet top-5 results year-after-year

## Chapter 2

# Image classification

Image classification tasks deal with taking an image as input and producing a single output
as to the object inside of the image, given a discrete set potential output labels. This task
turns out to be difficult, in part, because of how we represent images. Most images are
represented using pixels, which can be thought of as the smallest unit of an image that is
formed when zooming into a photograph. Each pixel contains a corresponding value of how
much red, green, and blue make up the color in the pixel. The combination of all red, green,
and blue pixels give a great approximation for all of the colors we can see. We therefore can
represent the entire image as a matrix of 3 dimensional pixels as shown in Figure 2.0.1. We
often refer to a matrix that holds an array as a tensor.

```
What the computer sees
```

```
Figure 2. 0. 1 : On a computer, we represent images as a matrix of pixels.
```

However, by representing an image as a tensor of numbers, we lose much of our human
intuitions as to what the image represents and it is difficult to extract meaningful information
a tensor full of numbers. We refer to the gap between what a human sees in an image and
what the computer sees as a semantic gap problem. This task becomes even more difficult
with variations in the image, such as changes to the illumination, formation, and background
as shown in Figures 2.0.2, 2.0.3, and 2.0.4, respectively.

##### 6

##### 2.1. KNN: K-NEAREST NEIGHBORS 7

```
Figure 2. 0. 2 : Different illuminations for a single object.
```

```
Figure 2. 0. 3 : Different formations for a single object.
```

```
Figure 2. 0. 4 : Changing the background of images that come from the same object category.
```

Hard-coding the image classification problem with if-then statements has been show to be
an incredibly difficult task that did not go very far. Some of the attemps at hard-coding
solutions included finding edges and corners of an image and trying to identify objects soley
based on the separation and scale of those details. This was not only hard because of the
variance in the images, as we just discussed, but also because it would require defining a set
of features for each possible class label.

Supervised learning approaches to the problem of image classification have worked much
better and are the most widely used techniques today. With supervised learning, we start
with a set of labeled images for each category, then use a statistical machine learning algo-
rithm to build a classifier that trains on the images and labels we collected. Once our model
is trained, we can deploy it on new examples where the label is hidden and the classifier
must identify the object inside of the image.

### 2.1 KNN: K-nearest neighbors

As a walkthough, one of the most basic models we could use for image recognition is a
nearest neighbors classifier, which looks for the image that has the closest pixel values based
on Euclidean distance, and then assigns the output label to be the same output label as the
one with the closest pixel values. This approach fails terribly at the variance problem, since

##### 8 CHAPTER 2. IMAGE CLASSIFICATION

```
Find edges Find corners
```

Figure 2. 0. 5 : Finding edges and corners of an object was an attempt at hard-coding the image
classification problem.

images of the same category can be represented very differently by changing illumination,
formation, background, and other attributes.

```
Test images and nearest neighbors
```

```
10 classes
50 , 000 training images
10 , 000 testing images
```

Figure 2. 1. 1 : The CIFAR10 data set (left) and the nearest neighbors for a few training examples
(right) [19].

With the nearest neighbors approach we have discussed, training a data will have a runtime
of O(1) and predicting labels with new data will have a runtime of O(n). However, this
turns out to be the opposite of what we would like, since we want a deployed model running
in practice to be as fast as possible and it does not matter a great deal if it took a while to
train the model. Modern approaches, such as convolutional neural networks, which will be
talked about soon, have a great runtime on predictions and a worse runtime on training.

##### 2.1. KNN: K-NEAREST NEIGHBORS 9

If we use a nearest neighbors algorithm in R^2 , we would end up with hard edged region
bounding, such as what is shown in Figure 2.1.2. Here, we can see that the algorithm will
be prone to overfit nearly any set of training data. To help reduce some of the overfitting
in the model, we can use a model known as K-nearest neighbors, which finds the K closest
points and makes the prediction whatever the majority class is, amongst the K closest
points. Using the same training data as in the nearest neighbors graphic, the results using
different values of K in K-nearest neighbors are shown in 2.1.3.

Figure 2. 1. 2 : Nearest neighbors algorithm in R^2 with the dots representing training instances and
the colored regions representing the predictions given if a point were to be tested in that region.

##### K = 1 K = 3 K = 5

Figure 2. 1. 3 : Using a K-nearest neighbors model for different values of K, where the white regions
represent ties.

##### 10 CHAPTER 2. IMAGE CLASSIFICATION

Depending on how we define the distance metric could also change how labels are predicted.
For example, we could have also defined the distance metric to be any Ln, where

```
Ln=
```

##### ”

##### X

```
P
```

##### 

##### IP 1 − IP 2

```
n
```

```
# 1 /n
, ∀n ∈ Z (2.1.1)
```

with I 1 and I 2 representing the first and second image and P representing a pixels value.
We have previously been using the Euclidean distance, which is also the L 2 distance. The
other popularly used distance is the L 1 distance, known as the Manhattan distance. We
can compare the results when using the Manhattan distances versus the Euclidean distance
in Figure 2.1.4.

### K = 1

### Manhattan distance

### K = 1

### Euclidean distance

```
Figure 2. 1. 4 : How using a different distance metric changes the predictions.
```

The L 1 distance also depends on the orientation of the coordinate system, while the L 2
distance does not. We can show this by finding the set of all points that have an equal
distance from the origin. When using the L 1 distance, the set of all points form a diamond,
while the set of all points when using the L 2 distance form a circle as shown in Figure 2.1.5.

```
Manhattan distance Euclidean distance
```

Figure 2. 1. 5 : The shapes formed by looking at the set of points with an equal distance from the
origin.

The set of choices that we make about the model, such as the type of learning algorithm,
value of K in K-nearest neighbors, and the distance metric, are known as hyperparame-
ters. It is often difficult to determine choices for hyperparameters, and the choice depends
primarily on the problem and data that is used. Most researchers end up testing a lot of
different choices for hyperparameters and stick with the one that produces the best results.

Determining the best results, however, is counterintuitive to most people first learning about
machine learning. Na ̈ıvely, one could choose the hyperparameters that perform best on the
training data set, such as setting K = 1 with K-nearest neighbors, but this turns out to
cause severe overfitting. Another approach would be to break the data up into two groups:
a training group and a testing group. Then, we will choose the hyperparameters that best

##### 2.2. LINEAR CLASSIFIERS 11

fit the data in the testing group after the model has been trained on the training data. This
approach, of breaking the data up into a training and testing group, will still likely cause
overfitting, but this time on the testing data instead of the training data. A better approach
would be to break data up into three groups, a training set, testing set, and validation set.
This time, we will choose the best hyperparameters that fit the validation set and determine
if it will work well on real world data by evaluating it on the testing set. In practice, it is
common to see some people break their data up into a training set and a testing set and
use the testing set for validation and testing purposes. It is also important to note that
the distribution of data is not even. Typically, validation and testing sets only need around
10 , 000 instances from an evenly distributed strata and the training set will recieve the rest
of the data.

Another approach to breaking up data in statistical machine learning is by using cross-
validation, however, this method is rarely used with deep learning models. Cross-validation
breaks the data up into two parts, a training and testing set. Then, with the training set,
we further break the data up into K-folds, or K evenly divided groups. Note that this
hyperparameter choice of K has nothing to do with the hyperparameter choice of K with
K-nearest neighbors. We then then set the validation data to be one of the folds and train
the model on the data that is neither the validation data nor the testing data. Once we
have trained the model, we change the validation set to be a different fold and continue this
process until each fold has been tested. Collectively, we can summarize the data for the
number of correct predictions and the number of incorrect predictions on the validation data
with a given model to compare between which model would be best to use. Cross-validation
typically works better than the other approaches to breaking up the data, however, it is
much more computationally expensive, so we typically would only use it when working with
small data sets.

Regardless of how we choose to break the data up, K-nearest neighbors would require an
immense amount of training data for learning even a small fraction of all possible images. If
we are working with a small image, of size 128 × 128 ×3, where the third dimension comes
from having three channels, red, green, and blue, then the total number of possible images
we could potentially see would be (128 × 128 × 3) · (256 × 256 × 256) ≈ 825 billion, since
each pixel be be one of 256 values. We refer to this problem, where changing the number of
in our input causes exponential increases to the number of possible responses, as the curse
of dimensionality.

### 2.2 Linear classifiers

Neural networks often are formed by stacking up many different layers of classifications.
One of the most common classification types used is a linear classifier. Using the CIFAR 10
data set, which has images of size 32 × 32 × 3, we can input an image and pass it through
a function parameterized by a set of weights W and a bias b that will output 10 numbers,
where each number corresponds to a class. Therefore, we can represent this information as

```
f(x; W, b) = W x + b, (2.2.1)
```

where x represents the flattened pixels on the input image, W represents the weights tensor,
and b represents the bias term. We also use the ; character to say that a function is
parameterized by a set of inputs. If we work out the dimensions for a CIFAR 10 image,
where the output must be 10 × 1, stretching out x will result in an array of size 3072 × 1,
so W must be of size 10 × 3072 and b must be of size 10 × 1.

It is relatively easy to interpret a linear classifier as well. If we take each row of the weight
matrix and undo the reshaping that flattened the tensor of pixels into an array, then what
we can observe are the activations most highly fired for each particular label. This is shown
in Figure 2.2.2 after training on the CIFAR 10 data set. Each image for each label can be
thought of as a template for the model. With a linear classifier, we are only able to learn
one template, although, as we study more complex models, we will be able to learn more
representations of a class.

##### 12 CHAPTER 2. IMAGE CLASSIFICATION

```
1. 5
```

```
0. 2 - 0. 5 0. 1 2. 0
```

```
1. 3 2. 1 0. 0
```

```
0 0. 25 0. 2 - 0. 3
```

```
W
x
```

**b** *f* ( **x** ; *W* ,^ **b** )

```
Input image
```

```
56
```

```
231
```

```
24
```

```
2
```

```
56 231
```

```
24 2
```

```
Stretch pixels into column
```

```
1. 1
```

+^3**.**^2

**- 1. 2**
**- 96. 8**

```
437. 9
```

```
61. 95
```

=

```
Cat score
```

```
Dog score
```

```
Ship score
```

Figure 2. 2. 1 : Representing a small version of a linear classifier with a 2 × 2 image with 3 class
labels (cat, dog, and ship).

Figure 2. 2. 2 : The activations that are fired most heavily for each pixel in each category using a
linear classifier.

If we plot each pixel of our image in its own dimension, then we can think of out linear
classifiers as setting hyperplanes that will separate the space into different regions, where a
new instance will be classified based on which hyperplane it is closest to.

Figure 2. 2. 3 : By representing images in a graph, the weights learned by the model will form a
hyperplane that separates the graph. Then, new images will be assigned based on which hyperplane
they fall closest to.

If we think about images as plots, then it is fairly easy to see that linear classifiers will fail
as classifiers on almost all models that cannot be represented using a linear relationship.
For example, the graphs in Figure 2.2.4 show examples of when a linear classifier would
perform poorly.

##### 2.2. LINEAR CLASSIFIERS 13

Figure 2. 2. 4 : The non-linear boundaries for two different classes, one class is in blue, the other
class is in pink. On these examples, a linear classifier would fail badly.

## Chapter 3

# Loss functions and optimization

cat

frog

car

## 3. 2

## 5. 1

## - 1. 7

## 4. 9

## 1. 3

## 2. 0 - 3. 1

## 2. 5

## 2. 2

```
Figure 3. 0. 1 : Arbitrary examples of different outputs produced from our linear classifier.
```

From last section, when working with our linear classifier we saw that there was an entry
for each class in the array produced by f(x; W, b). What we would like to do with each
entry would be to maximize the value of the correct class and minimize the value of the
incorrect classes. We can define what is known as a loss function, which describes how well
our model performs on a data set that consists of

{(xi, yi)}Ni= 1 , (3.0.1)
where xiis an image, yiis the label for the image, and N is the number of images in the
data set. We can now define a general loss function as the average of each loss over the
dataset, where

```
L =
```

##### 1

##### N

##### X

```
i
```

```
Li(f (xi; W, b) , yi). (3.0.2)
```

### 3.1 Multiclass SVM loss (“Hinge loss”)

The first specific loss function we will discuss is the multiclass SVM loss. The multiclass
SVM loss takes the summation over all of the incorrect categories that are close to, or above
the correct classes outputted score. If we denote the score of the jth class as sj, where
s = f(xi; W, b), then we can write the SVM loss as

```
Li=
```

##### X

```
j 6 =yi
```

##### (

```
0 if syi≥ sj+ c
sj− syi+ c otherwise
```

##### (3.1.1)

##### =

##### X

```
j 6 =yi
```

```
max (0, sj− syi+ c) , (3.1.2)
```

##### 14

##### 3.1. MULTICLASS SVM LOSS (“HINGE LOSS”) 15

where c is a nonnegative term to make sure that the correct class is sufficiently higher than
the incorrect classes. In practice, the value of c tends not to matter and is usually set to
the value 1. Here, notice that if our score is correctly identified by at least a margin of c,
then Li= 0 and the individual values for each classes score does not matter, so long as they
are less than syi− c. This is why some refer to the mutliclass SVM loss as “Hinge loss,”
because of the graph this forms as shown in Figure 3.1.1.

“Hinge loss”

*c*

Figure 3. 1. 1 : The name Hinge loss comes from the shape of the graph when plotting Lias a
function of syi, parameterized by sjand c.

As a concrete example, let us walk though the calculations with the scores given in Figure
3.0.1, where we will set c = 1. For the cat figure, we will have
Li= max(0, 5. 1 − 3. 2 + 1) + max(0, − 1. 7 − 3. 2 + 1), (3.1.3)
= 2. 9 +0, (3.1.4)
= 2. 9. (3.1.5)
Since the score for the frog class was sufficiently lower than the score for the cat class, it
did not contribute to the loss for the training example. However, since the score from the
car class was higher than the score of the cat class, the car class added to the loss.

Stepping through the car example in a similar fashion, we will have
Li= max(0, 1. 3 − 4. 9 + 1) + max(0, 2. 0 − 4. 9 + 1), (3.1.6)
= 0 +0, (3.1.7)
= 0, (3.1.8)
which means that we are satisfied with the scores and nothing needs to be adjusted for this
instance. Looking at the frog example, we should expect that our loss function is high,
due to the correct class having the lowest score by a large margin. Going through the
calculations, we find the loss to be
Li= max(0, 2. 2 − (− 3 .1) + 1) + max(0, 2. 5 − (− 3 .1) + 1), (3.1.9)
= 6. 3 +6. 6 , (3.1.10)
= 12. 9 , (3.1.11)
which confirms our goal of having a large loss when the scores are assigned badly.

We can write the Python code to compute a vectorized multiclass SVM loss as follows.

```
def L_i(x, y, W):
scores = W.dot( x)
margins = np.maximum(0, scores - scores[y] + 1)
margins[y] = 0
loss_i = np.sum (margins)
return loss_i
```

Since there are multiple possible ways in which we could form W and b to result in 0 loss,
such as scaling them either of them by a constant factor, it is not entirely clear which set
of weight and bias combination work the best. Further, we also do not want to perfectly fit
the model to the training data, since that would cause overfitting. One approach to solve
the overfitting problem is to add a regularization term to our loss function

```
L(X; W, b) =
```

##### 1

##### N

##### X

```
i
```

```
Li(f(xi, W ), yi) + λR(W ), (3.1.12)
```

##### 16 CHAPTER 3. LOSS FUNCTIONS AND OPTIMIZATION

where λ is our regularization parameter and R(W ) is a regularization function that attempts
to make our model simplier. In around the 1300s, William of Ockham showed that “among
competing hypotheses, the simplest is the best,” and this came to be known as Occam’s
Razor. The primary types of regularization functions used in practice are L2 regularization

```
R(W ) =
```

##### X

```
k
```

##### X

```
l
```

```
Wk^2 ,l, (3.1.13)
```

L1 regularization
R(W ) =

##### X

```
k
```

##### X

```
l
```

```
|Wk,l|, (3.1.14)
```

elastic net (L1 + L2)
R(W ) =

##### X

```
k
```

##### X

```
l
```

```
βWk^2 ,l+ |Wk,l|, (3.1.15)
```

max norm regularization, dropout, batch normalization, and stochastic depth. We will focus
on L2 regularization for now, which is really taking the square of the Frobenius norm of
the weights matrix. By adding in the L2 regularization term, we are adding more loss for
the values in the matrix that are further from 0. This corresponds to making the values
in the weight matrix closer together, which would make the model simplier. Consider, for
example, if we had two rows of weights

```
w 1 =
```

```
h
1 0 0 0
```

```
i
(3.1.16)
```

```
w 2 =
```

```
h
0. 25 0. 25 0. 25 0. 25
```

```
i
, (3.1.17)
```

coupled with an image
x =

```
h
1 1 1 1
```

```
i
```

. (3.1.18)

If we take wT 1 and wT 2 , they will both result in the same value of 1 and our SVM loss would
score them the same. However, if we added an L2 regularization term, the regularization
functions for each row would be

R(w 1 ) = 1, (3.1.19)
R(w 2 ) = 0. 25 , (3.1.20)
which would penalize the weights that form w 1 more than w 2. What we have showed is
that even if the scores produced are the same, a model that is more evenly distributed and
closer to 0 will have less L2 regularization than a model that has one, or a few, large values
contributing significantly to the score and a bunch of smaller ones that make little impact.
By contrast, if we used L1 regularization, the model would prefer the weights matrix to be
sparse, with only a few values making significant contributions.

### 3.2 Softmax classifier (multinomial logistic regression)

The multiclass SVM loss is certainly not the only loss function that we can define, and
another popular choice, maybe the most popular choice in deep learning, is known as the
softmax classifier (or multinomial logistic regression). With a softmax classifier, we will
exponentiate each score and then normalize that score by dividing by the sum of all the
exponentiated scores. After passing the scores through the softmax classifier, we can better
interpret the scores as representing the probability of the class, given an image. We can
write our softmax classifier as

```
P (Y = k | X = xi) =
Pesk
jesj
```

##### , (3.2.1)

where
s = f(xi; W, b). (3.2.2)
Now, we would like to maximize the log likelihood Y = k for the correct class yi, or minimize
the negative log likelihood for the correct class, which we can write as our loss function
arg min
W,b

```
Li= −log P (Y = yi| X = xi). (3.2.3)
```

##### 3.3. OPTIMIZATION 17

We use log here because it is simplier to maximize the log likelihood rather than the natural
probability. We can rewrite Equation 3.2.3 by subbing in the value for the probability
defined in Equation 3.2.1, which gives us

```
Li= −log
Pesyi
jesj
```

##### !

##### . (3.2.4)

Similar to the walkthrough done for the multiclass SVM loss, we will walkthrough an exam-
ple of calculating the loss using a softmax classifier, again using the scores in Figure 3.0.1.
We refer to these scores as the unnormalized log probabilities. The log part comes from us
first needing to exponentiate the scores and the unnormalized part comes from the sum of
each set of scores for a given image not needing to sum to 1. Starting with the image of a
cat, we have the score of the correct class as 3. 2 and the scores of the incorrect classes as
{ 5. 1 , − 1. 7 }. If we exponentiate all the scores, we will have

```
e^3.^2 ≈ 24. 5 , e^5.^1 ≈ 164. 0 , e−^1.^7 ≈ 0. 18 , (3.2.5)
```

which we can refer to as the unnormalized probabilities. Summing over the unnormalized
probabilities gives us X

```
j
```

```
esj= 24. 5 + 164. 0 + 0 .18 = 188. 68. (3.2.6)
```

Now if we divide each of the unnormalized probabilities by the sum of the sum of the
unnormalized probabilities, we will have the normalized probabilities of

1. 5
2. 68 ≈^0.^13 ,

##### 164. 0

##### 188. 68 ≈^0.^87 ,

##### 0. 18

##### 188. 68 ≈^0.^00.^ (3.2.7)

Here, the first probability (0.13) corresponds to the model’s prediction that the object in
the image is a cat, the second probability (0.87) corresponds to the model’s prediction that
the object is a car, and the third probability (0.00) corresponds to the model’s prediction
that the object is a frog. Since we know that the correct class is a cat, our loss, as defined
in Equation 3.2.4, will be
L = −log(0.13) = 0. 89. (3.2.8)
The calculations for the other examples would follow in the same manner, which we will not
address.

By using the softmax loss, the minimum and maximum values of the loss are the same as
they were with the multiclass SVM loss as 0 and ∞, respectively. However, the only way
to get a loss of 0 would be to have the probability of 1 with the correct class and 0 for the
incorrect classes, which could only come if we had the unnormalized log probability for the
correct class as ∞ and the unnormalized log probability for each of the incorrect classes as
−∞. Similarily, we could never have a loss of ∞ without the unnormalized log proability of
the correct class at −∞.

The differences in the calculations for the loss are shown in Figure 3.2.1. In contrast to the
multiclass SVM loss function, the softmax loss does not have a set of values that will all
produce no loss, once the score of the correct class c higher than the other classes. This
means that if we change the scores very little, the multiclass SVM loss is not guaranteed to
be affected, but the softmax loss will be affected.

### 3.3 Optimization

Now that we have discussed ways to determine the quality of the weights and bias on a set
of training examples, if follows that we would like to make them better, which corresponds
to decreasing the loss function. We can think of our loss function as a valley, where each
piece of land corresponds to the loss parameterized by a selection for W and b and we, as
the human, start at somewhere on the valley as shown in Figure 3.3.1. Our goal, as the
human, is to find a path that will lead to the bottom of the valley.

A na ̈ıve approach to try and find the bottom of the valley would be to randomly search for
it, which is equivalent to randomly sampling a bunch of weight and bias terms and checking

##### 18 CHAPTER 3. LOSS FUNCTIONS AND OPTIMIZATION

```
Figure 3. 2. 1 : How the loss is calculated using the multiclass SVM loss versus the softmax loss.
```

Figure 3. 3. 1 : We can think of optimization problems as starting on top of a valley and looking
for a path down to the bottom. Here, optimizing a function means finding the weights and bias
that correspond to the minimum loss function.

what the loss is for each of them. This will generally never work well considering the possible
landscape for weights we can set often may run into the hundreds of millions on modern
neural networks, so we would need to make tons of phenomenal predictions.

A better approach would be to look at the slope of our location on the hill, and then travel
in downward direction from the slope. This approach tends to work better and faster than
the na ̈ıve approach introduced earlier, but we are left with the problem of calculating slope
from a grid of numbers. In one dimension, recall that the derivative of a function from one
direction is defined as
d
dx

```
f(x) = lim
h→ 0
```

```
f(x + h) − f(x)
h
```

##### . (3.3.1)

In more dimensions, we can store how much changes in each direction will affect the output
into a vector. Here, the change in each direction is a partial derivative and the vector
containing all the partial derivatives is the gradient. We can then calculate the slope in a
direction by taking the dot product between the gradient and the direction’s unit vector.
It then follows that the direction of steepest descent will be in the direction of the negative
gradient.

If we think about the definition of the gradient, a na ̈ıve approach to make the calculation
would be to analytically set h to be a finite number near 0 and calculate how each value in
the weights changes if we add h to it as shown in Figure 3.3.2.

##### 3.3. OPTIMIZATION 19

```
?,
?,
?,
?,
?,...]
```

```
= - 2. 5
```

```
( 1. 2532 - 1. 25347 )/ 0. 0001
```

```
gradient dW:
```

```
[ - 2. 5 ,
?,
?,
2
```

```
current W:
```

```
[ 0. 34 ,
```

* 1. 11 ,
     1. 78 ,
     2. 12 ,
     3. 55 ,
     4. 81 ,
* 1. 1 ,
* 1. 5 ,
     1. 33 ,…]
        **loss 1. 25347**
        + 1. 11 ,

```
W + h (first dim) :
```

```
[ 0. 34 + 0. 0001 ,
```

```
0. 78 ,
0. 12 ,
0. 55 ,
2. 81 ,
```

* 1. 1 ,
* 1. 5 ,
     1. 33 ,…]
        **loss 1. 25322**

Figure 3. 3. 2 : Analytically calculating the partial derivatives to form the gradient by setting
h = 0.0001.

We can carry this operation out for each individual weight and will get a really close approx-
imation to the true value of the gradient, which tends to work well in practice. However,
this turns out to be an incredibly slow approach to calculating the gradient and is therefore
only used in practice for debugging purposes. We call this process the gradient check, which
more formally is using the analytical gradient to check if our calculations for the gradient
are correct.

A different approach would be to use calculus to compute the exact changes to the loss
function with respect to the weights and bias. For now, let us just focus on the weights
and similar methods could be used to calculate the changes in the bias. If we start with a
multiclass SVM loss function

```
L =
```

##### 1

##### N

##### XN

```
i= 1
```

```
Li+
```

##### X

```
k
```

```
Wk^2 , (3.3.2)
```

where
Li=

##### X

```
j 6 =yi
```

```
max(0, sj− syi+ 1), (3.3.3)
```

and
s = f(xi; W ) = W xi, (3.3.4)

then what we would like to find is ∇LW. What this corresponds to is finding a function
that takes as input our weights W and produces the gradient vector ∇LW. Once we find
the gradient, we update our weights using

```
W := W − α∇LW, (3.3.5)
```

where α controls the amount we step in each direction and is commonly referred to as the
learning rate. We can interpret Equation 3.3.5 as finding the minimum value in the contour
plot of our loss function as shown in Figure 3.3.3.

When calculating gradient descent in practice, the number of images inside of our training
set, N , may be extremely large and it is not always best to calculate the true direction of
the gradient, because of the computational cost. Instead, we often approximate the gradient
using a small portion of the training data. It is typical to use 32, 64, or 128 samples from
the training data for each calculation of gradient descent. We say that we are breaking the
data up into mini batches, and this process is known as mini batch gradient descent. If our
batch size is 1, then we are using what is known as stochastic gradient descent (SGD). It is
important, however, that the batches are chosen so that they represent the training data as
a whole.

##### 20 CHAPTER 3. LOSS FUNCTIONS AND OPTIMIZATION

original W

negative gradient direction

```
W 1
```

```
W 2
```

Figure 3. 3. 3 : Computing the gradient at a point to find the direction of steepest descent. We
then can take a step along that path, where the size of the step is controlled by our learning rate
α, to try and minimize our function.

### 3.4 Image features

Before deep learning models dominated computer vision, it was common to first extract
features from the images and then pass those features into a model, instead of passing in
the raw pixel values. By extracting features, the goal was to reframe the problem so that it
is easier for a learning algorithm to be able to solve it, such as the example shown in Figure
3.4.1.

```
x
```

```
y
```

```
r
```

```
θ
```

### f(x, y) = (r(x, y), θ(x, y))

Figure 3. 4. 1 : The goal behind extracting features from an image was to make it easier for a
classifier to correctly identify the points. With a linera classifier, we would not be able to learn the
representations for the plot on the right, however, we would be able to learn representations for the
plot on the right.

For images, a few feature extractions that we may would be to create color histograms,
histograms of oriented graidnets (HoG) [12, 13], and bag of words [20], shown in Figures
3.4.2, 3.4.3, and 3.4.4, respectively

##### 3.4. IMAGE FEATURES 21

```
+ 1
```

```
Figure 3. 4. 2 : Feature extraction for an image using a color histogram for each pixel.
```

```
Figure 3. 4. 3 : Feature extraction using a histogram of gradients (HoG) [12, 13].
```

```
Extract random
patches
```

```
Step 1: Build codebook
Cluster patches to form “codebook”
of “visual words”
```

```
Step 2: Encode images
```

```
Figure 3. 4. 4 : Feature extraction using a bag of words [20].
```

Convolutional neural networks, which will be discussed in more detail soon, work in a similar
manner to extracting features to make predictions, except in the case of using convolutional
neural networks, humans are not hand picking the features, the model is learning its own
set of features.

## Chapter 4

# Introduction to neural networks

### 4.1 Computational graphs

Before discussing the backpropagation algorithm that forms a fundamental building block
in neural networks, we must discuss computational graphs. Computational graphs give us a
way to represent any function with a set of inputs and ordered operations on those inputs
to arrive at the output. For example, we can represent the hinge loss calculation by first
taking the multiplication between W and x and passing those scores into the hinge loss,
which subsequently gets added to the regularization term as shown in Figure 4.1.1. Notice
that in this figure, we could use a bunch of different computational graphs to represent the
same function, if we were to expand out the hinge loss calculation. This is to say that there
is no single “correct” answer on how to represent a computational graph. We want to use
a computational graph in order to string together a set of operations and functions so that
we can find how the output changes due to each intermediate calculation. The process of
finding how the input changes the output of a function with a computational graph is known
as backpropagation.

```
x
```

```
W
```

```
hloinsgse
```

```
R
```

## \* s^ (scores) + L

```
Figure 4. 1. 1 : Computational graph to calculate hinge loss.
```

### 4.2 Backpropagation

With knownledge of how a computational graph is setup, we can use it in order to find how
each parameter affects the output using backpropagation. As an example, let us consider
the function
f(x, y, z) = (x + y)z, (4.2.1)

where x = −2, y = 5, and z = − 4 with the computation graph shown in Figure 4.2.1a.
Here, we can set an set an intermediate variable in the computation graph for

```
q = x + y, (4.2.2)
```

##### 22

##### 4.2. BACKPROPAGATION 23

where q is an arbitrary choice for a variable. Subbing in q to the original equation, we will
have
f = qz, (4.2.3)

which cannot futher be simplified with fewer variables, without setting f equal to another
variable or f = f. Here, we can now easily calculate

```
∂f
∂q = z^ and
```

```
∂f
∂z= q.^ (4.2.4)
```

Since we have the initial values of x = − 2 and y = 5, we know that q = 3 which implies

```
∂f
∂z= 3.^ (4.2.5)
```

Now, to calculate x and y, we can use the mutlivariate chain rule, which tells us

```
∂f
∂x
```

##### =

```
∂f
∂q
```

##### ·

```
∂q
∂x
and
∂f
∂y
```

##### =

```
∂f
∂q
```

##### ·

```
∂q
∂y
```

##### . (4.2.6)

Since we know that q = x + y, we also know that

```
∂q
∂x= 1^ and
```

```
∂q
∂y= 1.^ (4.2.7)
```

Subbing both of these values back into Equation 4.2.6, along with

```
∂f
∂q
= z = − 4 , (4.2.8)
```

gives us

```
∂f
∂x
=∂f
∂q ·
```

```
∂q
∂x
and ∂f
∂y
=∂f
∂q·
```

```
∂q
∂y
```

##### , (4.2.9)

```
∂f
∂x
= z · 1 and
∂f
∂y
= z · 1 , (4.2.10)
```

```
∂f
∂x
```

```
= − 4 and ∂f
∂y
```

##### = − 4. (4.2.11)

Putting all the partial derivates together, we have the computational graph in Figure 4.2.1b,
which has the derivatives at each step in red and the values in green.

```
(a) Computation graph example (b) Computation graph with derivatives
```

Figure 4. 2. 1 : Computation graph with for f(x, y, z) = (x+y)z, where x = − 2 , y = 5 , and z = − 4.

Notice that at each node in our computational graph, we are only concerned with the
neighboring nodes, as better shown in Figure 4.2.2. By breaking the task up of calculating
the derivative of the input up into subproblems, we can can scale this algorithm up into
tons of layers inside of our computational graph with relative ease, where it might be hard
to calculate the derivative of a complicated function.

##### 24 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

f

```
“local gradient”
```

```
gradients
```

Figure 4. 2. 2 : For both the forward and back propagation steps, each node can be isolated and
calculated using only its neighboring nodes.

As a more complicated example, let us consider the function

```
f(w, x) =^1
1 + e−(w^0 x^0 +w^1 x^1 +w^2 )
```

##### , (4.2.12)

where we have the initial values 



```


```

```
w 0 = 2
x 0 = − 1
w 1 = − 3
x 1 = − 2
w 2 = − 3
```

##### . (4.2.13)

The intermediate points on the computational graph and the calculations are shown in
Figure 4.2.3. After forward propagating through the computation graph and obtaining the
values shown in green, which just requires us to use the operation with the input at each
step, we start backward propagaion at the end of the of the function. The last step consists
of calculating^1 /x, where x = 1.37. From single-variate calculus, we know that

```
∂
∂x
```

##### 

##### 1

```
x
```

##### 

##### 

```
x= 1. 37 = −
```

##### 1

```
x^2
```

##### 

```
x= 1. 37 = −^0.^53.^ (4.2.14)
```

This now gives us an analytical value we can multiply backwards for the chain rule that
we can multiply backwards, without needing to setup a more function based on inputs.
Continuing to move backwards, the plus one to our value, that is x + 1, where x = 0. 37 will
give us a constant derivative
∂
∂x(x^ +^ 1)

##### 

```
x= 0. 37 = 1.^ (4.2.15)
```

Using the chain rule, we see that changes to the input at this step will change f by a factor
of 1 ·− 0 .53 = − 0 .53. Moving back to the exponentiation operator that has an input of −1,
we can find its relative change to the output as

```
∂
∂x
(ex)
```

##### 

##### 

```
x=− 1
```

```
= ex
```

##### 

##### 

```
x=− 1
```

##### =

##### 1

```
e
```

##### ≈ 0. 37. (4.2.16)

Again using the chain rule, multiplying 0. 37 by − 0. 53 gives us − 0 .2, which represents how
much nudges to the value of our input to the exponentiation operator will affect f. Going
backward to the next step, where we mutliply our input x = 1 by −1, we calculate

```
∂
∂x
(−x)
```

##### 

```
x= 1 = −^1 ,^ (4.2.17)
```

where we can use the chain rule to show small changes to x at this step change f by
− 0. 2 · − 1 = 0 .2. Next we have an operator with two inputs, lets call x = 4 and y = −3,
where we are calculating how changes in the input affect x + y, which gives us

```
∂
∂x
(x + y) = 1 and
```

##### ∂

```
∂y
(x + y) = 1. (4.2.18)
```

##### 4.2. BACKPROPAGATION 25

Since multiplying a number by 1 will give us the same number back, the changes to the x
and y at this step will still be 0 .2. Here, we have reached our first input to the function
where the variable y corresponds to w 2 , so

```
∂f
∂w 2 = 0.^2.^ (4.2.19)
```

We still, however, need to continue moving backwards through the graph in order to calculate
how the other inputs to the function affect f. The next step is another addition operator,
and because of the symmetry of the operator, we have already shown that this operator will
not change how each input will affect the output, so we can continue backward propagating
the value of 0 .2 to each side of the operator. We now have arrived at our two multiplication
operators. We will start with w 0 x 0 , where w 0 = 2 and x 0 = −1. Here, we can calculate the
partial derivatives to be

```
∂
∂w 0
(w 0 x 0 ) = x 0 = − 1 and
```

##### ∂

```
∂x 0
(w 0 x 0 ) = w 0 = 2. (4.2.20)
```

Therefore, using the chainrule, we can show that

```
∂f
∂w 0 = −^0.^2 and
```

```
∂f
∂x 0 = 0.^4.^ (4.2.21)
```

Going to the other multiplication operation with w 1 x 1 , where w 1 = − 3 and x 1 = −2, we
can use a similar process to calculate the partial derivatives with

```
∂
∂w 1 (w^1 x^1 ) = x^1 = −^2 and
```

##### ∂

```
∂x 1 (w^1 x^1 ) = w^1 = −^3.^ (4.2.22)
```

Finally, using the chainrule, we have showed that

```
∂f
∂w 1
= − 0. 4 and ∂f
∂x 1
```

##### = − 0. 6. (4.2.23)

Figure 4. 2. 3 : Representing a relatively more complicated function using a computational graph,
where the values calculated using forward propagation are shown in green and the values calculated
using backward propagation are shown in red.

On this example, notice that it would have been a lot more complicated to derive an ana-
lytical solution to f with respect to each input, and using the process of back propagation,
we only needed to calculate the partial derivatives for simple functions that we could then
chain together. We also could have defined the sigmoid function to be

```
σ(x) =
```

##### 1

```
1 + e−x
```

##### , (4.2.24)

##### 26 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

which has the nice property of being able to define the derivate based on the output as
derived here

```
dσ(x)
dx
= e
```

```
−x
(1 + e−x)^2
```

##### , (4.2.25)

##### =

```
1 + e−x− 1
(1 + e−x)^2
```

##### , (4.2.26)

##### =

##### 

```
1 + e−x− 1
1 + e−x
```

##### 

##### 1

```
1 + e−x
```

##### 

##### , (4.2.27)

```
= (1 − σ(x)) · σ(x). (4.2.28)
```

Here, we could have subbed in the sigmoid function in for the last four nodes defined in
Figure 4.2.3, which would have simplified a few early backward propagation calculations.

With computation graphs, we may also run into functions like

```
f = max(w, z). (4.2.29)
```

Here, if w > z, then∂f/∂w = 1 and∂f/∂z = 0. Other common gates are shown in Figure
4.2.4.

```
Figure 4. 2. 4 : How the inputs to a max gate, multiply gate, and addition gate affect the output.
```

We also may have inputs that go to two or more branches as shown in Figure 4.2.5. Here,
if we define our input as x, which is passed into two functions, a and b and we know how
changes to both a and b will affect the final output f, then we can again use the definition
of the multivariate chain rule to show that

```
∂f
∂x
```

##### =

```
∂f
∂a
```

##### ·

```
∂a
∂x
```

##### +

```
∂f
∂b
```

##### ·

```
∂b
∂x
```

##### . (4.2.30)

##### 4.2. BACKPROPAGATION 27

```
+
```

```
a
```

```
b
```

```
x
```

```
Figure 4. 2. 5 : An input x that is passed into both a function a and a function b.
```

#### 4.2.1 Gradients of vectors and matricies

In most applications of deep learning, our inputs will not be scalar values, instead they
will be vectors or matricies. To understand how backpropagation works with matricies and
vectors, we must first look at what it means to take a deriviatve of a non-scalar value.
Suppose, for example, that we are working with the function

```
f(x, W ) = ||W · x||^2 =
```

```
Xn
```

```
i= 1
```

```
(W · x)^2 i, (4.2.31)
```

where the initial values are

```
W =
```

##### ”

##### 0. 1 0. 5

##### 0. 3 0. 8

##### #

```
, x =
```

##### ”

##### 0. 2

##### 0. 4

##### #

```
, and f(x, W ) = 0. 116. (4.2.32)
```

For now, let us define the intermediate calculation

```
q = W · x =
```

##### ”

##### 0. 22

##### 0. 26

##### #

##### , (4.2.33)

and try to find how each element of x changes each element of q; that is

```
∂qi
∂xj,^ ∀i,^ j^ ∈^ {^0 ,^1 }.^ (4.2.34)
```

Let us start with finding∂q^0 /∂x 0 , where we can explicitly expand out the matrix multiplica-
tion that forms q 0 to be

```
q 0 = W 0 ,:· x, (4.2.35)
= W 0 , 0 x 0 + W 0 , 1 x 1. (4.2.36)
```

Here, we easily derive Equation 4.2.36 with respect to x 0 , which will give us

```
∂q 0
∂x 0
```

##### = W 0 , 0. (4.2.37)

Plugging in our initial value for W 0 , 0 , we have

```
∂q 0
∂x 0
```

##### = 0. 1. (4.2.38)

Next, we can look for∂q^1 /∂x 0 , where we can explicitly write q 1 as

```
q 1 = W 1 ,:· x, (4.2.39)
= W 1 , 0 x 0 + W 1 , 1 x 1. (4.2.40)
```

##### 28 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

Using a similar process, we can derive Equation 4.2.40 with respect to x 0 to get

```
∂q 1
∂x 0 = W^1 ,^0 ,^ (4.2.41)
= 0. 3. (4.2.42)
```

By the symmetry of the problem, it is easy to show that
∂q 0
∂x 1
= 0. 5 and
∂q 1
∂x 1

##### = 0. 8. (4.2.43)

Many people may combine all the derivatives between q and x into a matrix

```
J(q, x) =
```

##### ”

∂q (^0) /∂x 0 ∂q (^0) /∂x 1
∂q (^1) /∂x 0 ∂q (^1) /∂x 1

##### #

##### , (4.2.44)

##### =

##### ”

##### 0. 1 0. 5

##### 0. 3 0. 8

##### #

##### . (4.2.45)

The matrix J(q, x) is known as the Jacobian matrix. Now, we can use the same properties
of the chain rule as we did in Equation 4.2.30 to find

```
∂q
∂x 0
```

##### =

```
∂q 0
∂x 0
```

##### +

```
∂q 1
∂x 0
```

##### , (4.2.46)

which is saying to sum up all the unique ways changes to x 0 will affect q. We can also write

```
∂q
∂x 1
```

##### =

```
∂q 0
∂x 1
```

##### +

```
∂q 1
∂x 1
```

##### , (4.2.47)

where plugging in the values of the partial derivatives we previously found will give us

```
∂q
∂x 0
= 0. 4 and
∂q
∂x 1
```

##### = 1. 3. (4.2.48)

Now we can represent this information as

```
∇qx=
```

##### ”

##### 0. 4

##### 1. 3

##### #

##### . (4.2.49)

Notice that the gradient of with respect to x is the same size as x. This will always be
the case and is what allows us to use gradient descent. (Of course we do not use gradient
descent to calculate changes to x, since that is our input.)

After understanding how to find ∇qx, it will be easier to find ∇qW. In Equations 4.2.36
and 4.2.40, we wrote a system of linear equations that gave us q 0 and q 1. Using those
equations, we can write







```
∂q 0
∂W 0 , 0
```

##### =

##### ∂

##### ∂W 0 , 0

```
(W 0 , 0 x 0 + W 0 , 1 x 1 ) = x 0
```

```
∂q 1
∂W 0 , 0
```

##### =

##### ∂

##### ∂W 0 , 0

```
(W 1 , 0 x 0 + W 1 , 1 x 1 ) = 0
```

##### 

##### 

##### 

##### 

##### 

```
∂q 0
∂W 0 , 1
```

##### =

##### ∂

##### ∂W 0 , 1

```
(W 0 , 0 x 0 + W 0 , 1 x 1 ) = x 1
```

```
∂q 1
∂W 0 , 1
```

##### =

##### ∂

##### ∂W 0 , 1

```
(W 1 , 0 x 0 + W 1 , 1 x 1 ) = 0
```

##### 

##### 

##### 

##### 

##### 

```
∂q 0
∂W 1 , 0
```

##### =

##### ∂

##### ∂W 1 , 0

```
(W 0 , 0 x 0 + W 0 , 1 x 1 ) = 0
```

```
∂q 1
∂W 1 , 0 =
```

##### ∂

```
∂W 1 , 0 (W^1 ,^0 x^0 +^ W^1 ,^1 x^1 ) = x^0
```

##### 

##### 

##### 

##### 

##### 

```
∂q 0
∂W 1 , 1
```

##### =

##### ∂

##### ∂W 1 , 1

```
(W 0 , 0 x 0 + W 0 , 1 x 1 ) = 0
```

```
∂q 1
∂W 1 , 1 =
```

##### ∂

```
∂W 1 , 1 (W^1 ,^0 x^0 +^ W^1 ,^1 x^1 ) = x^1
```

##### .

If we reshape the matrix using row-major ordering, which is equivalent to writing W as the
vector
W^0 =
h

##### W 0 , 0 W 0 , 1 W 1 , 0 W 1 , 1

```
i
```

```
>
, (4.2.50)
```

##### 4.2. BACKPROPAGATION 29

then we can write the Jacobian matrix for J(q, W^0 ) as

```
J(q, W^0 ) =
```

##### 

##### 

∂q (^0) /∂W 0 , 0 ∂q (^0) /∂W 0 , 1 ∂q (^0) /∂W 1 , 0 ∂q (^0) /∂W 1 , 1
∂q (^1) /∂W 0 , 0 ∂q (^1) /∂W 0 , 1 ∂q (^1) /∂W 1 , 0 ∂q (^1) /∂W 1 , 1

##### 

##### , (4.2.51)

##### =

##### ”

```
x 0 x 1 0 0
0 0 x 0 x 1
```

##### #

##### , (4.2.52)

##### =

##### ”

##### 0. 2 0. 4 0 0

##### 0 0 0. 2 0. 4

##### #

##### . (4.2.53)

The Jacobian matrix, in general, takes a system of functions (each function of q in this case)
and a set of elements (elements of W in this case) and checks how the partial derivatives of
each element will affect each function. We rewrote W as a vector W^0 in order to more easily
show we are passing in a set of set of elements into J(q, W^0 ). Notice that summing up the
rows in the Jacobian matrix will give us how each element of W changes q. This gives us
an easy way to calculate

```
∇qW =
```

##### ”

```
∂q/∂W 0 , 0 ∂q/∂W 0 , 1
∂q/∂W 1 , 0 ∂q/∂W 1 , 1
```

##### #

##### , (4.2.54)

##### =

##### ”

##### 0. 2 0. 4

##### 0. 2 0. 4

##### #

##### . (4.2.55)

Now, to find∂f/∂q 0 and∂f/∂q 1 , we can start by writing

```
f = q 02 + q^21 , (4.2.56)
```

where it follows that the partial derivatives are
∂f
∂q 0
= 2q 0 and
∂f
∂q 1
= 2q 1. (4.2.57)

Writing the partial deriviates in the same shape as q will give us the gradient

```
∇fq=
```

##### ”

```
∂f/∂q 0
∂f/∂q 1
```

##### #

##### , (4.2.58)

##### =

##### ”

```
2 q 0
2 q 1
```

##### #

##### , (4.2.59)

##### =

##### ”

##### 0. 44

##### 0. 52

##### #

##### . (4.2.60)

With both ∇fqand ∇qW, we can now find ∇fW. Recall that we earlier found

```
∂qk
∂Wi,j= xj and
```

```
∂f
∂qk = 2qk.^ (4.2.61)
```

Putting both of these together, we can use the chain rule to show
∂f
∂Wi,j

##### =

##### X

```
k
```

```
∂f
∂qk
```

##### ·

```
∂qk
∂Wi,j
```

##### , (4.2.62)

##### =

##### X

```
k
```

```
(2qk) · (xj) , (4.2.63)
```

```
= 2xj
X
```

```
k
```

```
qk. (4.2.64)
```

##### 30 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

Since any row vector Wi,:will only affect row i of q, we can further simplify

##### P

kqk=^ qi,
giving us
∂f
∂Wi,j
= 2qixj. (4.2.65)

Equation 4.2.65 gives us an easy formula to calculate

```
∇fW=
```

##### ”

```
∂f/∂W 0 , 0 ∂f/∂W 0 , 1
∂f/∂W 1 , 0 ∂f/∂W 1 , 1
```

##### #

##### , (4.2.66)

##### =

##### ”

```
2 q 0 x 0 2 q 0 x 1
2 q 1 x 0 2 q 1 x 1
```

##### #

##### , (4.2.67)

##### =

##### ”

##### 0. 088 0. 176

##### 0. 104 0. 208

##### #

##### . (4.2.68)

Now if f was our loss function, we could use gradient descent to update our weights with

```
W := W − α · ∇fW. (4.2.69)
```

If we worked in terms of vectors, we could have also written Equation 4.2.67 as

```
∇fW= 2q · x>, (4.2.70)
```

which would have given us the same result. The computation graph for the setup we have
been working with is shown in Figure 4.2.6.

```
2
```

```
Figure 4. 2. 6 : Computation graph for f(x, W ) = ||W · x||^2.
```

#### 4.2.2 Modularized implementation

So far, our computational graphs can be thought of as two separate functions, a forward pass
function and a backward pass function as shown in Figure 4.2.7. Here, both the forward and
backward passes go through the complete graph, going through each node, or gate. For each
particular type of gate, such as a multiplication gate, we can create a class that contains
the forward and backward step as shown in Figure 4.2.8

Plenty of deep learning frameworks follow this same type of structure when implementing
backpropagation. For example, the deep learning framework Caffe [21], which has bindings
for both Python and Matlab, works by creating a class for each possible layer that is found
in a computational graph, some of which are shown in Figure 4.2.9.

On each layer in the Caffe framework there is a function for both a forward and backward
pass as shown in Figre 4.2.10 with the sigmoid layer.

##### 4.2. BACKPROPAGATION 31

Figure 4. 2. 7 : The pseudocode for a modularized implementation of a Computational Graph class
that consists of a forward and backward pass through the entire graph.

y

### (x,y,z are scalars)

```
x
z
*
```

Figure 4. 2. 8 : For a multiplication gate with z = x · y, we can create two methods: one for
calculating the forward pass through the gate and one for calculating the backward pass through
the gate.

Figure 4. 2. 9 : A few layers that are on the deep learning framework, Caffe. More layers can be
found at
https://github.com/BVLC/caffe/tree/master/src/caffe/layers.

##### 32 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

```
* top_diff (chain rule)
```

Caffe Sigmoid Layer

Figure 4. 2. 10 : The sigmoid layer inside of the Caffe framework con-
tains functions for a forward and backward pass. Functions available at
https://github.com/BVLC/caffe/blob/master/src/caffe/layers/sigmoid layer.cpp.

### 4.3 Neural Networks

#### 4.3.1 Introduction

Currently, we have been working with our weights W as a linear function of our input x;
that is
f = W x. (4.3.1)
We can extend our linear function into a neural network by first passing it through a non-
linear function and then multiplying by another set of weights as shown

```
f = W 2 max(0, W 1 x). (4.3.2)
```

The function max(0, W 1 x) is known as the ReLU (rectified linear unit) function [22] and it is
the most commonly used non-linear function. We must pass the function W 1 x through a non-
linear function in order represent more complicated functions than simple linear classifiers.
If we were to not pass the function through a nonlinearity, which would mean

```
f = W 2 (W 1 x) , (4.3.3)
```

then we could use the associativity properties of matrix multiplication to show that

```
f = (W 2 W 1 ) x, (4.3.4)
```

which can then be simplified down into a linear function with one set of weights W = W 2 W 1.
We call Equation 4.3.2 a 2-layer neural network because it has two sets of weights. Each
additional layer that is neither the output layer nor the input layer is known as a hidden
layer. In each hidden layer, we have a hyperparameter choice for the number of neurons we
want it to have. Starting with a CIFAR 10 image of size 3072 × 1 when put into a vector, if
we wanted to have 100 hidden neurons in the hidden layer for a two layer neural network,
then we can set W 1 to be of size 100 × 3072 and W 2 to be of size 10 × 100, where the 10
corresponds to the number of classes in CIFAR 10. We can represent this neural network
using the diagram shown in Figure 4.3.1.

With a linear network, recall that we were only able to find templates for each class as shown
in Figure 2.2.2. However, a single templates is not very robust to variances that arise. With
a 2-layer neural network, we can start representing more than just a single image as our
template for a given class. To represent a broader range of functions, more easily, we can
increase the number of layers in a neural network. If we wanted a 3-layer neural network,
for example, then we could write

```
f = W 3 max(0, W 2 max(0, W 1 x)). (4.3.5)
```

##### 4.3. NEURAL NETWORKS 33

s

3072

x W1 h W2

100 10

Figure 4. 3. 1 : Structure of a 2-layer neural network that has a hidden layer containing 100 neurons.

```
Impulses carried toward cell body
```

```
Impulses carried away
from cell body
```

```
dendrite
```

```
cell body
```

```
axon
```

```
presynaptic
terminal
```

```
Figure 4. 3. 2 : Labeled image of a neuron [23].
```

#### 4.3.2 Connection to the brain

Neural networks get their name from the broad connections they have with how a neuron
works in the brain. More recently, however, modern variations to the traditional neural
network have tended to veer further and further from the connections to the brain, but it
can still be interesting to see where the name comes from and some inspiration behind how
they were first created. When looking at a neuron, as shown in Figure 4.3.2, the dendrites
start by receiving the impulses from other neurons, which are all collected inside of the cell
body. Once all the signals are in the cell body, the axon passes them to the presynaptic
terminal, which is connected to more neurons.

##### 34 CHAPTER 4. INTRODUCTION TO NEURAL NETWORKS

How a neuron compares to a neural network is shown in Figure 4.3.3. Notice that our
weights act similar to the dendrites, the axons act like the the non-linear form of f (x; W, b),
the activation function acts like the cell body, and this process is continued for each layer
of the neural network.

```
Figure 4. 3. 3 : The comparisons for each part of the neuron with a neural network.
```

As we briefly mentioned earlier, the connections between a biological neuron and a neural
network are broad. With biological neurons, we have many many different types and they
can represent more complex non-linear computations in the dendrites. More on the topic of
neuron computations can be found from London and H ̈ausser [24].

## Chapter 5

# CNNs: Convolutional neural

# networks

### 5.1 The history of neural networks

Figure 5. 1. 1 : The Harvard Mark I Computer used for early calculations with the perceptron
algorithm [25].

The origins of a neural network trace back to around 1958 when Frank Rosenblatt created
the perceptron algorithm [26]. The goal of the original perceptron was image classification
with letters in the alphabet. First used on the Mark I Computer, as shown in Figure 5.1.1,
the original tests used a camera that produced 20 × 20 pixel images and calculated recognized
letters based on the linear test

```
f(x) =
```

##### 

```
1 if w · x + b ≥ 0
0 otherwise
```

##### . (5.1.1)

At the time, the backpropagation algorithm had not yet been invented, so to update the
parameters a different method was employed, which attempted at finding the direction of
the gradient.

##### 35

##### 36 CHAPTER 5. CNNS: CONVOLUTIONAL NEURAL NETWORKS

A few years later, at around 1959 Bernard Widrow and Marcian Hoff build adaline and
madaline (many adaline) [27]. Here, we began to stack layers inside of the network, but
there was still no solution as to how the weights should be updated. A few images from the
original paper are shown in Figure 5.1.2.

Figure 5. 1. 2 : The first known paper where researchers began to stack multiple perceptrons to-
gether to form more complex networks [28].

It was not until 1986 that backpropagation was introduced by David Rumelhart and Geoffrey
Hinton [29]. The method they used for backpropagation follows much of what is done today
as shown in Figure 5.1.3 and the math resembles what we have learned earlier.

```
Figure 5. 1. 3 : Recreation of Rumelhart et al. 1986 [29].
```

However, even after backpropagation was introduced, the neural networks built with only a
few layers, or shallow neural networks, that researchers used in their algorithms performed
far less-superior to many statistical machine learning approaches. In the early 2000s, re-
searchers began to look more at using deep learning techniques and in 2006 Geoffrey Hinton
and Rusland R Salakhutdinov published work showing that deeper neural networks could
work in theory [30].

State-of-the-art results using deep neural networks did not appear until around the early
2010s, where there were breakthroughs in both natural language processing [31, 32] and
computer vision with the the infamous AlexNet paper [18]. AlexNet was revolutionary at
the time because it showed that a deep convolutional neural network could be used to crush
the ImageNet classification challenge that we discussed earlier. The architecture for AlexNet
is shown in Figure 5.1.5 along with the filters learned in the first layer of the network in
Figure 5.1.6.

##### 5.2. CONVOLUTIONAL NEURAL NETWORKS 37

Figure 5. 1. 4 : Summary of the work shown by Hinton and Salakhutdinov, where they showed that
deep neural networks could be built.

```
  
```

```
        
       
 
```

```
  
```

```
Figure 5. 1. 5 : AlexNet architecture.
```

```
Figure 5. 1. 6 : Filters learned in the first layer of the AlexNet paper.
```

Following AlexNet, convolutional neural networks have been widely applied to many tasks
in computer vision, such as real-time image detection [33, 34, 35], image segmentation [36],
self-driving cars [37], pose estimation [38], games [39], image captioning [40, 41], mimicking
artistic styles [42, 43], and much more.

### 5.2 Convolutional neural networks

Previously, we have been working with fully connected layers, where we first flattened our
image into a vector and passed it through a set of weights that were connected to each
element of the image vector as shown in Figure 5.2.1.

##### 38 CHAPTER 5. CNNS: CONVOLUTIONAL NEURAL NETWORKS

```
Figure 5. 1. 7 : A few examples of generated art using convolutional neural networks [ 44 ].
```

```
3072
```

```
1
```

```
32 x 32 x 3 image - > stretch to 3072 x 1
```

```
10 x 3072
weights
```

```
input activation
```

```
1
10
```

```
Figure 5. 2. 1 : Fully connected layer in a neural network.
```

In contrast to a fully connect layer, a convolutional layer keeps the neighboring pixels intact
and slides a filter around the image, where the depth of the filter matches the depth of the
image. The filter is typically a tensor of size 1 ×1, 3 ×3, 5 ×5, 7 ×7, or 9 ×9, with a depth
that matches the input depth. A filter may also be referred to as a kernal or receptive field
in some texts. We call the process of sliding the filter over the image a convolution. (Here,
the term convolution differs from how a convolution works in image processing. In image
processing, the convolution operation that we are refering to is known as cross-correlation.
However, we stick with the term convolution because it is most widely used in the field of
computer vision.) Each time we convolve the filter over the image, we take the dot product
between the pixels of the image and the weights inside of the filter as shown in Figure 5.2.2a.
The entire process of convolving a filter across an image involves going over each unique
spatial location as shown in Figure 5.2.2b. Notice, here, that the dimensions for the width,
height, and depth (commonly referred to as channels) have all changed from those in the
input image.

##### 5.2. CONVOLUTIONAL NEURAL NETWORKS 39

```
32
```

```
32
```

```
3
```

```
32x32x3 image
5x5x3 filter
```

```
1 number:
the result of taking a dot product between the
filter and a small 5x5x3 chunk of the image
(i.e. 5*5*3 = 75-dimensional dot product + bias)
```

```
(a) A single step in convolving a filter across an
image.
```

```
32
```

```
32
```

```
3
```

```
32 x3 2 x3 image
5 x5x3 filter
```

```
convolve (slide) over all
spatial locations
```

```
activation map
```

```
1
```

```
28
```

```
28
```

```
(b) Convolving the filter over the entire image.
```

```
Figure 5. 2. 2 : Convolution layers
```

We also have the option of applying multiple different filters to an image as shown in Figure
5.2.3. For each new filter we add, we add a layer of depth to the output image of activation
map.

```
32
```

```
32
```

```
3
```

```
3 2 x 32 x 3 image
5 x 5 x 3 filter
```

```
convolve (slide) over all
spatial locations
```

```
activation maps
```

```
1
```

```
28
```

```
28
```

```
(a) 2 filters produces a new image of depth 2.
```

```
32
```

```
32
```

```
Convolution Layer
```

```
activation maps
```

```
28
```

```
28
```

```
(b) 6 filters produces a new image of depth 6.
```

Figure 5. 2. 3 : Using multiple different types of filters can change the depth of the convolutional
neural network.

Similar to what we had with a fully connected neural network, we apply a nonlinearity
function and stack multiple layers in a sequence in order to form a convolutional neural
network as shown in Figure 5.2.4.

```
32
```

```
32
```

```
3
```

```
CONV,
ReLU
e.g. 6
5x5x 3
filters^28
```

```
28
```

```
6
```

```
CONV,
ReLU
e.g. 10
5x5x 6
filters
```

```
CONV,
ReLU
```

##### ….

```
10
```

```
24
```

```
24
```

Figure 5. 2. 4 : A convolutional neural network is formed by stacking multiple convolution layers
in a sequence, and passing them through a nonlinearity function.

Recall the work from Hubel and Wiesel when analyzing parts of the cat brain and finding
that the beginning neurons that fire are for low-level visual details, like corner and edge
detection, and neurons at the back of the visual cortex represent high-level visual details.
It has been shown that a similar pattern occurs in the filters with a convolutional neural
network as shown in Figure 5.2.5.

##### 40 CHAPTER 5. CNNS: CONVOLUTIONAL NEURAL NETWORKS

Figure 5. 2. 5 : Earlier layers of a convolutional neural network typically represent low-lew features
of an image, such as edge or corner detection, while later layers in a neural network represent
high-level features, such as a face or object [45, 46].

If we slide different filters across an image, we will pick up different types of activation maps
as shown in Figure 5.2.6. If we think of, for example, a filter that picks up corners, then we
will have the most positive or negative values when our filter is covering a part on the image
that contains a corner. With activation maps, the most positive values are shown in white,
the most negative values are shown in black, and the neural values are shown in gray.

```
example 5 x 5 filters
( 32 total)
```

```
one filter =>
one activation map
```

```
Figure copyright Andrej Karpathy.
```

Figure 5. 2. 6 : What each activation map looks like after convolving a filter across an image. The
white pixels represent positive values, the black pixels represent negative values, and the gray pixels
represent zero values.

If we stack together more layers, forming a deeper convolutional neural network, then we
can observe how the activation maps change as the network goes deeper, as shown in Figure
5.2.7. We will go more in-depth on this topic soon, but it is worth pointing out, as shown
in the convolutional neural network architecture in Figure 5.2.7, that we use pooling layers
and a fully-connected layer, along with convolutional layers. Pooling layers are primarily
used in order to shrink the size of our layers.

##### 5.3. SPATIAL DIMENSIONS 41

```
Figure 5. 2. 7 : The activation maps for each layer in a larger convolutional neural network.
```

### 5.3 Spatial dimensions

```
7
```

```
7
```

Figure 5. 3. 1 : The output from convolving a 7 × 7 image with a 3 × 3 filter is of size 5 × 5. Above
are the horizontal convolutions and using the symmetry of the problem, the number of horizontal
convolutions will be the same as the number of vertical convolutions.

Suppose we start with a 7 × 7 image and convolve it using a 3 ×3 filter. As shown in Figure
5.3.1, we can see that the output produced will be of size 5 × 5. Currently, we have been
using convolutions with a stride length of 1; that is, we move out filter by one pixel in each
direction for each slide (or convolution). However, we can modify our stride length. If we
use a stride length of 2, we will end up with a 3 × 3 output, as shown in Figure 5.3.2.

```
7
```

```
7
```

Figure 5. 3. 2 : Convolving a 7 × 7 image with a 3 × 3 filter and a stride length of 2 will give us a
3 × 3 output.

In practice, we try not to set our convolution filters or step size to result in the filter not
cleanly covering the entire image. For example, if we used the same setup, having a 7 × 7
image convolved with a 3×3 filter, but this time set the stride length to be 3, our filter would
run off the page, as shown in Figure 5.3.3. When we can, we try to avoid any instances of
our filter running off of the page, which can often be controlled by changing the filter size
or the stride length.

##### 42 CHAPTER 5. CNNS: CONVOLUTIONAL NEURAL NETWORKS

```
7
```

```
7
```

Figure 5. 3. 3 : Using a step size of 3 does not fit our 7 × 7 image convolved with a 3 × 3 filter. We
tend to try an avoid filters that do not fit, in practice.

More generally, given filter and stride that do not run off of the image, our output size will
be

```
output size =N^ −^ F
stride
```

##### + 1 , (5.3.1)

where our image is of size N × N and our filter is of size F × F. Testing this with our
previous examples that had N = 7, F = 3, and stride as 1, 2, and 3, we can show

```
stride = 1 =⇒
```

##### 7 − 3

##### 1

##### + 1 = 5, (5.3.2)

```
stride = 2 =⇒
```

##### 7 − 3

##### 2

##### + 1 = 3, (5.3.3)

```
stride = 3 =⇒
```

##### 7 − 3

##### 3

##### + 1 = 2. 33. (5.3.4)

It is also common to add a border to the image, in order to make the input and output be
the same size. If we add a border around the entire image of 1 pixel, then we say that the
padding is 1. It is most typical to add 0 to each element added due to padding, which is
known as zero padding. Convolutions that have no padding are known as valid convolutions,
while convolutions that have a padding that allows the dimensions of the input to match
the dimensions of the output are known as same convolutions. For example, if we add a
padding of 1 to our 7 × 7 image that gets convolved with a 3 × 3 filter having a step size of
1, then we have a same convolution, as shown in Figure 5.3.4.

```
00 0 0 0 0 0
0
```

(^00)
00 0 0 0 0 0
0
(^00)
00 0 0 0 0 0
0
(^00)
00 0 0 0 0 0
0
(^00)
00 0 0 0 0 0
0
(^00)
00 0 0 0 0 0
0
(^00)
00 0 0 0 0 0
0
(^00)
Figure 5. 3. 4 : Adding a padding of 1 to a 7 × 7 image convolved with a 3 × 3 filter with a stride
length of 1 will give us a 7 × 7 output. Since the input is the same size as the output, we call this
a same convolution.

### 5.4 Pooling layers

As we saw in the convolutional neural network shown in Figure 5.2.7, pooling layers may
follow convolutional layers in a convolutional neural network. Pooling layers are primarily
used in order to shrink the height and width of an input, as shown in 5.4.1. We would
often like to shrink the size of our input in order to speed up computation, although there
is a tradeoff between how many pixels we can make the input and how fast we can train
the entire network. The two most common ways to pool layers are with max pooling and
average pooling.

##### 5.4. POOLING LAYERS 43

```
Figure 5. 4. 1 : Following a pooling layer, the input is shrunk and downsampled.
```

With any type of pooling, we typically keep the stride length equal to the size of the
filter, which means that no pixel will ever convolved twice. With max pooling, we take the
maximum number at each depth slice as shown in Figure 5.4.2.

```
1 1 2 4
5 6 7 8
```

```
3 2 1 0
1 2 3 4
```

```
Single depth slice
```

```
x
```

```
y
```

```
max pool with 2x2 filters
and stride 2 6 8
3 4
```

```
Figure 5. 4. 2 : Max pooling using a 2 × 2 filter size with a stride length of 2.
```

Average pooling would work similar to max pooling, except, of course, average pooling
would take the average of each number at each depth slice. We can intuitively think of
max pooling as determining if a signal occurs in a region, where having a high number in
that region indicates that something has occurred at that pixel. With average pooling, this
signal may get drowned out from the noise of other pixels inside of the region. In practice,
using a filter size of 2 ×2 and a stride length of 2, or using a filter size of 3 × 3 with a stride
length of 3 is most common.

Chapter 6

## 7 Training neural networks II

### 6.1 Activation functions

```
After our linear step in each layer of the neural network, we almost always pass the result
through a non-linear activation function in order to represent more complex functions. Some
of the most common activation functions are shown in Figure 6.1.1.
```

#### 6.1.1 Sigmoid activation function

```
We will start by focusing on the sigmoid activation function, which is defined as
```

```
σ(x) =
```

##### 1

```
1 + e−x
```

##### . (6.1.1)

```
The graph for the function is also shown in Figure 6.1.1. Here, the output will range
between 0 and 1. We can interpret the output both from a probabilistic point of view and
for determining a “firing rate” for each neuron. Because of this simple interpretation, the
sigmoid function has historically been one of the most popular activation functions.
```

### Sigmoid

### tanh

### ReLU

### Leaky ReLU

### Maxout

### ELU

```
Figure 6. 1. 1 : Common activation functions
```

##### 44

##### 6.1. ACTIVATION FUNCTIONS 45

However, when using the sigmoid activation function, problems often arise. First, consider
that when calculating∂σ/∂x, this number will be multiplied by a set of different numbers
in order to determine how to update the weights by finding the gradients with respect to
the weights. The idea of chaining multiple layers together is shown in Figure 6.1.2, which
is looking at a single layer in a neural network.

```
gate
```

x sigmoid

Figure 6. 1. 2 : Inside of a neural network,∂σ/∂x will make part of many separate contributions
when calculating how the loss changes with respect to the input.

Suppose that our input x is something around −10. Here, our∂σ/∂x will be approximately

1. Now also consider that when our input x is around 10,∂σ/∂x will also be near 0. Because
   multiplying any real number by 0 will produce 0, we are effectively making the entire chaining
   sequence 0 when our input is somewhat away from x = 0.

Secondly, our output is not centered at 0, so later layers in the neural network will have data
the is not zero-centered. So, if we pass non zero-centered values through the neural network,
then during backpropagation we will have only all positive values or all negative values in
our weights because f = w · x + b will have∂f/∂w = x. So, we will only be able to have a
gradient that is either all positive or all negative as shown in Figure 6.1.3. However, if our
output was zero-centered, then x, which is the activation from the previous layer, would
have a mean of 0 with both positive and negative values. Thus, if x was both positive and
negative∂f/∂w would also be both positive and negative, so we could move in any direction.

Third, the exponentiation step is computationally expensive when dealing with large inputs.
While not as expensive as the linear step in each layer of a neural network, it is still an
inconvenience to calculate.

```
zig zag path
```

```
hypothetical
optimal w
vector
```

```
allowed
gradient
update
directions
```

```
allowed
gradient
update
directions
```

Figure 6. 1. 3 : The gradient of our weights will only ever be all positive or all negative when using
a sigmoid activation function that has all positive inputs.

#### 6.1.2 Hyperbolic tangent activation function

The hyperbolic tangent function works similar to the sigmoid function, except instead of
the output being between 0 and 1, the output is between -1 and 1. We often refer to the

##### 46 CHAPTER 6. TRAINING NEURAL NETWORKS I

hyperbolic tangent function as tanh and it is defined as

```
tanh x =
sinh x
cosh x (6.1.2)
```

```
=e
```

```
x− e−x
ex+ e−x
```

##### (6.1.3)

##### =

```
e^2 z− 1
e^2 z+ 1
```

##### , (6.1.4)

as show in Figure 6.1.1. With the hyperbolic tangent function, we have a zero-centered
output, although the gradients still are likely to saturate with values near 0 and we still
have the computationally expensive exponentiation calculation.

#### 6.1.3 ReLU: Rectified linear unit

The ReLU function calculates
f(x) = max(0, x), (6.1.5)
which is shown in Figure 6.1.1. With ReLU, the biggest benefits are that it does not saturate
(in the positive region), it is computationally inexpensive, typically converges faster than
sigmoid and tanh, and it mimics our knowledge of how the biological neurons work better
than the other types of activation functions. However, our output is no-longer zero-centered
and with negative input data our output will always be 0. If we choose poorly initialized
weights, where w · x + b is negative for many inputs, then while using the ReLU activation
function, our weights will never be updated. Setting the initial bias b to a small positive
value, such as 0. 01 may help with the weights initialization problem. The ReLU tends to
be used most in practice because of its computational efficiency and results it has produced
when training large scale neural networks.

6.1.4 Leaky ReLU, PReLU, and ELU

The leaky ReLU works the same as the ReLU with positive values, but has a linear multi-
plication factor to negative values. The leaky ReLU is defined as

```
f(x) = max(0. 01 x, x), (6.1.6)
```

as shown in Figure 6.1.1. The parametric rectifier, PReLU, is defined as

```
f(x) = max(αx, x), (6.1.7)
```

where α is an additional parameter that is to be learned during backpropagation. Both the
PReLU and leaky ReLU do not saturate, are computationally efficient, and converge faster
than both the hyperbolic tangent and sigmoid functions [47, 48]. There is also a function
called exponential linear units, ELU, that is defined as

```
f(x) =
```

##### 

```
x if x > 0
α(exp(x) − 1) if x ≤ 0
```

##### . (6.1.8)

ELU is more robust to noise and has an output closer to zero-mean, however it requires an
exponentiation calculation [49].

#### 6.1.5 Maxout neuron

The maxout neuron works differently than any of the previous activation functions in that
there is no linear calculation done beforehand. Instead, maxout neuron sets the activation
to
max(w 1 · x + b 1 , w 2 · x + b 2 ). (6.1.9)
In theory, this generalizes both the ReLU and leaky ReLU functions and will not saturate.
However, we would need to learn twice the number of representations, so it is often not used
in practice [50].

##### 6.2. DATA PREPROCESSING 47

### 6.2 Data preprocessing

In many applications of machine learning we typically want to normalize our data by cen-
tering the data at 0 and setting the standard deviation to be 1, as shown in Figure 6.2.1.
By having both positive and negative inputs, we avoid the trap discussed in Section 6.1.1
where our gradients can only fall into the all positive or all negative directions.

Figure 6. 2. 1 : Normalizing the data by setting the mean to be 0 and the standard deviation to be
1.

There are also other ways to normalize the data using statistical methods such as PCA and
whitening (Figure 6.2.2), however neither are used a great deal in computer vision.

```
(data has diagonal
covariance matrix)
```

```
(covariance matrix is the
identity matrix)
```

```
Figure 6. 2. 2 : Additional statistical methods for normalizing data.
```

With most computer vision applications, we usually keep the variance between the pixels
the same. However, it is common that the mean of an image is subtracted. The two ways
this is typically done is by subtracting the entire mean of the image (done on AlexNet) or
by subtracting the mean in each channel of the image (done on VGGNet). The mean is
taken from all of the training data, and that same mean is subtracted come test time.

### 6.3 Weight initialization

When designing a neural network, we must decide what the initial values should be for each
weight. If we initialize all the weights to be the same value from the beginning, then
they will all have the same gradients during backpropagation and every neuron in the layer
will behave the same way.

Another approach might be to initalize each weight to be a random small number.
Here, we may set the mean of the numbers to be 0 and the standard deviation to be 10 −^2.
However, recall that the gradient in each layer depends on the activations, x, passed in from
the previous layer. If each layer is computing w·x, where w is say 1 deviation from the mean
at 0.01, then when the 10th layer comes around the activations will be 0. 0110 ·x = 10−^20 ·x.

##### 48 CHAPTER 6. TRAINING NEURAL NETWORKS I

With the activations becoming exponentially smaller as the number of layers increase, the
gradients will also become exponentially smaller to the point that they are rounded to 0 by
a computer.

Suppose instead that we initialize our weights to be random large numbers, where we
keep the mean at 0 and set the standard deviation to be 1. In this situation, when using a
hyperbolic tangent activation function, it is most likely that our neurons will saturate with
activation values of − 1 and 1 and the gradients will be 0.

Instead of choosing the variation of the weights to be standard for any neural network, we
could change it based on the number of neurons in the previous layer, which we will call n.
If we want the variance to be the same before and after calculating w · x, then we can use
the properties of variance to find

```
var
```

##### X

```
i
```

```
wixi
```

##### !

##### =

##### X

```
i
```

```
var(wixi) (6.3.1)
```

```
=
```

##### X

```
i
```

##### 

```
E(wi)
```

#####  2

```
var(x 1 ) + E
```

##### 

```
x^2 i
```

##### 

```
var(wi) + var(xi)var(wi) (6.3.2)
```

```
=
```

##### X

```
i
```

```
var(xi)var(wi) (6.3.3)
```

```
= (n · var(w))var(x). (6.3.4)
```

Equation 6.3.4 shows us that if we would like to have the variance of the input be the same
as the variance of our output, then we must multiply w by^1 /√n, because

n · var

##### 

```
√w
n
```

##### 

```
var(x) =
```

```
n
n
· var(w)
```

##### 

```
var(x) (6.3.5)
= var(w)var(x). (6.3.6)
```

Other popular choices for variance selection are^2 /n, which is known as He initialization [51],

and^2 /( (^2) in+nout), which is known as Xavier initialization [52]. Here, ninand nout are the
number of inputs and outputs, respectively, and n is also the number of input neurons. In
practice when we have a ReLU activation function, we typically use He initialization; thus,
we set the weights to be
w = np.ran dom.randn(n) \* sqrt(2. 0 / n)

### 6.4 Batch normalization

Batch normalization attempts to normalize the activations in each layer of the neural net-
work. If our activations in layer k are x(k), then batch normalization calculates

```
bx(k)=
```

```
x(k)− E
```

##### 

```
x(k)
```

##### 

```
q
var
```

##### 

```
x(k)
```

#####  ,^ (6.4.1)

where E

##### 

```
x(k)
```

##### 

is the expected value of the activations in the k-th layer. Batch normalization
is typically added after the fully-connected of convolutional layer, but before the nonlinearity.
In practice, when we are training a network broken up into batches B = {x 1 ,… , xm}, we
set the expected value of x(k)to be the mean of the mini-batch

```
E
```

##### 

```
x(k)
```

##### 

```
← μB=
```

##### 1

```
m
```

```
Xm
i= 1
```

```
xi, (6.4.2)
```

and the variance of x(k)to be the variance of the mini-batch

```
var

```

```
x(k)

```

```
← σB^2 =
```

##### 1

```
m
```

```
m
```

##### X

```
i= 1
```

```
(xi− μB)^2. (6.4.3)
```

##### 6.4. BATCH NORMALIZATION 49

Putting both of these equations together, we have

```
bxi←
pxi−^ μB
σ^2 B+ 
```

##### , (6.4.4)

where  is a constant added to make the variance between each mini-batch more stable.
When applying batch normalization, we want to make sure that we are not losing information
in each layer. If we set the mean to be 0 and the variance to be 1 in a sigmoid layer, then
we would lose a lot of information by constraining the input to be nearly all linear. We
therefore introduce new parameters that could learn the inverse of the normalization step.
More specifically, we introduce the terms γ(k)and β(k), where

```
y(k)= γ(k)bx(k)+ β(k). (6.4.5)
```

Notice that if γ(k)=

```
q
var
```

##### 

```
x(k)
```

##### 

```
and β(k)= E
```

##### 

```
x(k)
```

##### 

, then we have effectively undone the
normalization step. Come test time, we use a pre-set mean and variance from the training
data. This mean and variance can be calculated, for example, using a running average of
both the mean and variance over each mini-batch. The seminal paper introducing batch
normalization was published in 2015 by Sergey Ioffe and Christian Szegedy at Google [53].

## Chapter 7

# Training neural networks II

### 7.1 Optimization

#### 7.1.1 Problems with stochastic gradient descent (SGD)

Currently, we have been using gradient descent to decrement our weights by subtracting
the weights gradient multiplied by the learning rate, from the weights in each direction.
However, consider what happens if the loss function changes slowly in one direction, but
faster in another, as shown in Figure 7.1.1. If this occurs, then the loss function has a large
condition number, which is the ratio between the largest and smallest values in a Hessian
matrix, which is made up between the second partial derivatives between the weights and
the loss.

Figure 7. 1. 1 : The contour plot of a loss function in R^2 that is more sensitive to changes in the
vertical direction than the horizontal direction. A potential stochastic gradient descent (SGD)
updates to the weights is in red.

In higher dimensions, this turns out to be an even bigger problem. For example, if we have
100 million different weights, then it is quite likely that the condition number is high and
stochastic gradient descent will not step in the optimal direction.

With stochastic gradient descent, we run into the problem of a 0-gradient at saddle points
or local minima as shown in Figure 7.1.2. Around each of those point, we will also not be
making much progress, due to the gradients being so small. In pratice, saddle points tend
to be more problematic in high dimensions, since it only requires that in some directions
the loss goes up and some directions the loss goes down [54].

In addition, with stochastic gradient descent with mini-batches, the direction of the gradient
in the batch will only be a rough estimate for the direction of the gradient in the entire
training data. Therefore, we may go on a skewed path to converge at the minimum as
shown in Figure 7.1.3.

##### 50

##### 7.1. OPTIMIZATION 51

```
Figure 7. 1. 2 : The gradient gets stuck at saddle points (left) and local minima (right).
```

Figure 7. 1. 3 : Possible steps when using stochastic gradient descent when the mini-batch size is
less than the entire training sample.

#### 7.1.2 SGD with momentum

SGD with momentum uses a running mean of the gradients to better step in the correct
direction. With momentum, we introduce a new hyperparameters, ρ, where we now calculate
vt+ 1 = ρvt+ ∇f(xt) (7.1.1)
xt+ 1 = xt− αvt+ 1. (7.1.2)
From a physics perspective, there are loose analogies between v as velocity and ρ as friction.
Typical choices for ρ are 0. 9 and 0.99. Since momentum takes the weighted average in each
direction, we can think of it as a ball moving with a velocity, where the ball represents the
choice of weights. As the ball moves, it will have an inertia, making it harder to change the
direction it has previously been moving, which will help with all the problems introduced
with SGD as shown in Figure 7.1.4.

#### 7.1.3 Nesterov momentum

There have been variations of momentum that have come up in the optimization literature,
such as Nesterov momentum. With Nesterov momentum, we take the gradient after stepping
in the direction of the velocity, and then add that gradient direction to the velocity[55, 56],
as shown in Figure 7.1.5. Mathematically, we can write Nesterov momentum as
vt+ 1 = ρvt− α∇f(xt+ ρvt) (7.1.3)
xt+ 1 = xt+ vt+ 1. (7.1.4)

These equations are kind of annoying, since what we would like to do is update ∇f(xt) and
xtat each step. If we change our variable to be x ̃t= xt+ ρvt, then we can rearrange the
system to get

```
vt+ 1 = ρvt− α∇f(x ̃t) (7.1.5)
x ̃t+ 1 − ρvt= x ̃t− ρvt+ vt+ 1 (7.1.6)
̃xt+ 1 = x ̃t− ρvt+ (1 + ρ)vt+ 1 (7.1.7)
= x ̃t+ vt+ 1 + ρ(vt+ 1 − vt). (7.1.8)
```

##### 52 CHAPTER 7. TRAINING NEURAL NETWORKS I I

```
Gradient Noise
Local Minima Saddle points
```

Poor Conditioning

Figure 7. 1. 4 : Momentum helps with each of the problems introduced with stochastic gradient
descent. Starting in the upper left, we can think of a local minima and a saddle point as a ball
rolling down a hill, where the height of the hill is the loss and the ball is the weights. As the
ball rolls, it picks up velocity, and once it reaches its local minimum value, it will still continue to
move due to the velocity it picked up. For the other examples of poor conditioning and gradient
noise, the velocity term will take the weighted average, in each direction, for which the weights
have previously moved; thus, in each direction the weights will move in a more direct path towards
the minimum.

From Equation 7.1.8, we can think of Nesterov momentum as a way of checking for potential
errors in the velocity because of the addition of the term ρ(vt+ 1 − vt).

```
Gradient
```

```
Velocity
```

```
actual step
```

```
Momentum update:
```

```
Gradient
Velocity
```

```
actual step
```

```
Nesterov Momentum
```

Figure 7. 1. 5 : Momentum (left) calculates the gradient of the current weights and takes a step in
the direciton combined from the directions of both the running velocity and the gradient. Nesterov
momentum (right), by contrast, calculates the gradient from the veloctiy and then add that gradient
to the velocity vector to form each step.

We can compare potential paths for SGD, SGD with momentum, and SGD with Nesterov
momentum as shown in Figure 7.1.6. Notice that with a momentum term, we often overshoot
the minimum and then come back to it. However, Nesterov may not overshoot the the
minimum by quite as much.

#### 7.1.4 AdaGrad

With AdaGrad [57], we keep a running total of the squared gradients divide each step by
the square root of the running total. We initially squar each gradient to make the values
positive. The complete algorithm is shown in Algorithm 1. Notice that we also add 10 −^7 to
ensure that we are not dividing by 0 at the start.

##### 7.1. OPTIMIZATION 53

##### SGD

```
SGD+Momentum
```

```
Nesterov
```

Figure 7. 1. 6 : Paths for how SGD, SGD with momentum, and SGD with Nesterov momentum
may behave.

Algorithm 1 AdaGrad

```
running total ← 0
while w has not converged do
dw ← gradient(w)
running total += dw^2
w = w −
α dw
√
running total + 10 −^7
end while
```

In theory, AdaGrad is supposed to take larger steps in the direction that is less prone to
changes and shorter steps in the directions that change a lot. This is because dividing by
a small running total will result in a large number and dividing by a large running total
will severly decrease the step size. The problem with AdaGrad is that the running total
continues to grow and will eventually be so large that w will effectively not be changing.

#### 7.1.5 RMSProp

RMSProp [58] is a variation to AdaGrad that improves on its flaws of not changing w after
many iterations. With RMSProp, we add a decay term β to the running total of the gradient
that will more heavily affect the gradients computed at the beginning. It is common to see
values of β as 0.9 and 0.99. The updated algorithm is shown in Algorithm 2.

Algorithm 2 RMSProp
running total ← 0
while w has not converged do
dw ← gradient(w)
running total = β (running total) +(1 − β)dw^2
w = w −
√ α^ dw
running total + 10 −^7
end while

We compare the potential paths for SGD, SGD with momentum, and RMSProp in Figure
7.1.7.

#### 7.1.6 Adam optimization

Adam optimization [59] brings together both momentum and RMSProp into a single algo-
rithm. With Adam, we create two moments, the first one for the momentum term, which

##### 54 CHAPTER 7. TRAINING NEURAL NETWORKS I I

##### SGD

```
SGD+Momentum
```

```
RMSProp
```

Figure 7. 1. 7 : Potential paths of the weights over the loss function for SGD, SGD with momentum,
and RMSProp.

starts at 0 and iteratively sets

```
M 1 = β 1 M 1 + (1 − β 1 )dw (7.1.9)
```

and the second moment for the RMSProp term, which also starts at 0 and sets

```
M 2 = β 2 M 2 + (1 − β 2 )dw^2. (7.1.10)
```

In Equation 7.1.9, β 1 can be thought of as the friction coefficient and in Equation 7.1.10 β 2
can be thought of as the weight decay. However, if we set

```
w = w −
αM 1
√
M 2 + 10 −^7
```

##### , (7.1.11)

where β 2 is 0.9 or 0.99 and M 2 starts at 0, then we end up taking a very large step at the
beginning because of the small size of M 2. To mitigate the large step size at the beginning,
we introduce the bias terms

```
b 1 =
```

##### M 1

```
1 − βt 1
```

##### (7.1.12)

```
b 2 =
```

##### M 2

```
1 − βt 2 ,^ (7.1.13)
```

where t is the number of iterations. Notice that as t increases, the bias term appears
increasily more similar to the moments. With the bias terms, we now write the update to
our weights as

```
w = w −
αb 1
√
b 2 + 10 −^7
```

##### . (7.1.14)

The complete Adam optimization algorithm is shown in Algorithm 3. For plenty of deep
learning models, Adam optimization works well and is a great starting point. In particular,
it is often a good starting point to choose Adam optimization with the hyperparameters
β 1 = 0 .9, β 2 = 0 .999, and α = 10 −^3 or α = 5 × 10 −^4. The updated potential paths of
convergence for the weights are shown in Figure 7.1.8.

##### 7.1. OPTIMIZATION 55

Algorithm 3 Adam optimization

```
first moment ← 0
second moment ← 0
for t in the range of iterations do
dw ← gradient(w)
first moment = β 1 (first moment) + (1 − β 1 )dw
second moment = β 2 (second moment) + (1 − β 2 )dw^2
first bias ←
first moment
1 − βt 1
second bias ←
second moment
1 − βt 2
w = w −
√ α(first^ bias)
second bias + 10 −^7
end for
```

##### SGD

```
SGD+Momentum
```

```
RMSProp
```

```
Adam
```

Figure 7. 1. 8 : Updated paths of convergence of our weights with the addition of Adam optimiza-
tion.

#### 7.1.7 More on learning rates

Figure 7. 1. 9 : How the learning rate could be categorized based on the plot of the loss over epochs
(the number of complete iterations over the training set).

##### 56 CHAPTER 7. TRAINING NEURAL NETWORKS I I

With a constant learning rate, we can assess how well it performs by plotting the loss over
the epochs, as shown in Figure 7.1.9. Epochs refers to the number of iterations over the
entire training set. We can modify the learning rate to decay over time using a few different
methods such as step decay, exponential decay, and 1 /t decay. With step decay, we set
the learning rate to be the value of a decreasing step function that halves every couple of
epochs. With exponential decay, we set

```
α = α 0 e−kt, (7.1.15)
```

where k is a hyperparameter that controls the amount of decay. And with 1/t decay, we set

```
α = α^0
1 + kt
```

##### , (7.1.16)

where t is the number of epochs and k again controls the amount of decay. Learning rate
decay may give us a plot like the one shown in Figure 7.1.10.

```
Loss
```

```
Epoch
```

```
Learning rate decay!
```

Figure 7. 1. 10 : When using learning rate decay, we may end up with a plot that makes relatively
large decreases to the loss each time the learning rate is updated.

Learning rate decay is more frequently seen when using SGD with momentum and less
common when using Adam optimization. It is often hard to tell which hyperparameters are
set well when using learning rate decay. To avoid confusion when assessing, we typically do
not use a learning rate decay at the beginning of training a model. Instead, we use it after
good values for more crucial hyperparameters, such as the α and β terms, have been found.

```
Loss
```

```
w 1
```

```
(1) Use gradient form linear approximation
(2) Step to minimize the approximation
```

Figure 7. 1. 11 : With all the optimization techniques we have introduced thusfar, we have only
looked at how the first order gradient can minimize the loss function.

##### 7.1. OPTIMIZATION 57

#### 7.1.8 Second-order optimization

Currently, we have only been analyzing how the first-order gradient affects the loss function
as shown in Figure 7.1.11. Instead of simply looking at the first-order changes, we could use
the Hessian matrix to find a quadratic approximation of the minimum as shown in Figure
7.1.12.

```
Loss
```

```
w1
```

```
(1) Use gradient and Hessian to form quadratic approximation
(2) Step to the minima of the approximation
```

Figure 7. 1. 12 : Using second-order optimization to step in the direction that minimizes the second
order taylor series of the loss function.

When using second-order minimization, we step in the direction that minimizes the second
order taylor polynomial. Here, if we start with the weights w 0 and a cost function J, we
can write the polynomial taylor expansion as

```
J(w) ≈ J(w 0 ) + (w − w 0 )>∇Jw(w 0 ) +
```

##### 1

```
2 (w^ −^ w^0 )
```

```
>H(w − w 0 ), (7.1.17)
```

where H is the Hessian matrix formed by all of the second partial derivatives with respect
to the weights. If we want to solve Equation 7.1.17 for the minimum value, then we can
calculate
w = w 0 − H−^1 ∇Jw(w 0 ), (7.1.18)

which is referred to as the Newton parameter update. Notice that we no longer have a learning
rate hyperparameter that we need to manually adjust, although when using second-order
methods some people may throw on a learning rate if they wanted more control of the step
size.

The Newton parameter update works well in theory, although when we have 100 million
weights, then it is currently impractical to store a matrix that is 100 million by 100 million
and take its inverse for each step, which is O(N^3 ) time. In practice, it is more common to
use Quasi-Newton methods, in particular the BFGS and L-BFGS (limited memory BFGS)
methods [60].

#### 7.1.9 Model Ensembles

Our optimization methods we have currently discussed focus on decreasing the training
error. However, when training a neural network, we care much less about the training error
than we care about the validation error. A method for improving the validation error is
model ensembling. With model ensembling, we train several different models and set the
output to be the average over the each models output. Model ensembling is frequently
used in competitions to built state-of-the-art models. We can also vary our approach to
model ensembling by taking different snapshots of our model while it is training, instead
of building independent models. Another approach, known as Polyak averaging, takes a
weighted average of the parameter vector as more data is trained, and use that as the
parameter vector [61].

##### 58 CHAPTER 7. TRAINING NEURAL NETWORKS I I

### 7.2 Regularization

The idea of regularization is to add a term to the loss function that may increase the
training error rate, but decrease the validation error rate. Regularization is used to prevent
overfitting, and we have already seen L2 regularization, L1 regularization, and Elastic net
(L1 + L2) regularization to name a few. When using neural networks, it makes less sense
to use these types of regularization because we do not want the weights to be near 0.

#### 7.2.1 Dropout regularization

A separate approach to regularization is to use dropout regularization [62]. During the
forward pass with dropout regularization, we randomly set particular neurons in the net-
work to be 0 as illustrated in Figure 7.2.1. The probability of droppping each neuron is a
hyperparameter and a typical value is 0.5.

Figure 7. 2. 1 : Dropout regularization randomly chooses particular neurons to shut off during the
training phase.

One interpretation of why dropout works is because we are shutting off separate neurons
that each hold features, where we are forcing the output to not rely heavily on a single
neuron. For instance, in a cat classification neural network that does not use dropout, we
could have a neuron pick up the ears, tail, furr, claws, and look on the cat and then take
a weighted sum over each of those features to determine if the object is a cat. But, when
using dropout, we shut off some of those features during each iteration as shown in Figure
7.2.2.

```
For ces the network to have a redundant representation;
Prevents co-adaptation of features
has an ear
has a tail
is furry
has claws
mischievous
look
```

```
cat
score
```

```
X
```

```
X
```

```
X
```

Figure 7. 2. 2 : Dropout prevents the network from relying too heavily on a single neuron to affect
the score.

Another interpretation of dropout regularization connects back to model ensembles. Here,
we can think of dropout as training a large number of ensembles (that share parameters)
because at each forward pass, it will likely be looking at a completely new ensemble. With
a fully connected neural network that has 4096 units, there would be 24096 ≈ 101233. To
put this gigantic number into perspective, there are only around 1082 atoms in the entire
universe.

##### 7.3. TRANSFER LEARNING 59

Come test time, it is often more difficult to initially determine how to choose the output of
a model because we have to calculate the expected value of the model with respect to the
dropout probability and the input; that is

```
y = f(x) = Ez[f(x, z)] =
```

##### Z

```
p(z)f(x, z)dz, (7.2.1)
```

where z is the dropout probability.

a

x y

```
w 1 w
2
```

Figure 7. 2. 3 : Simple neural network with an output a and two inputs x and y that are parame-
terized by w 1 and w 2 , respectively.

We no longer want to randomly drop different neurons int he network, because that will
lead to inconsistent results. Instead, let us consider the simple neural network shown in
Figure 7.2.3. During training, if we set the dropout probability to be^1 / 2 , then our expected
value for a is

```
E[a] =
```

##### 1

##### 4

```
(w 1 x + w 2 y) +
```

##### 1

##### 4

```
(w 1 x + 0 y) +
```

##### 1

##### 4

```
(0x + w 2 y) +
```

##### 1

##### 4

```
(0x + 0 y) (7.2.2)
```

```
=^1
2
(w 1 x + w 2 y) (7.2.3)
= z(w 1 x + w 2 y). (7.2.4)
```

Equation 7.2.4 gives us a solid approximation for calculating the output during testing to
have the same expected value as the output during training, where we simply multiply each
output produced by keeping all the neurons activation by the dropout probability.

Another method, which slightly increases the computational efficiency come test time is
known as inverted dropout. Here, we divide each output by the dropout probability during
training and no longer multiply by the dropout probability come test time. Mathematically,
these are equivalent approaches! Inverted dropout is most commonly used in practice.

#### 7.2.2 Data augmentation

With data augmentation, we may train our model by first adjusting the images we are
training on, as shown in Figure 7.2.4. For example, during training we might first adjust
each image by flipping it horizontally, taking random crops and scales, and color jittering.
Come test time, we may take the average of a fixed number of crops. For instance, ResNet
resizes the image at 5 scales { 224 , 256 , 384 , 480 , 640 } and then with each size it takes an
additional 10 crops at 244 × 244, where 4 crops are from the corners, one crop is from the
center, and then the image is flipped horizontally with 4 corner crops and 1 center crop.

### 7.3 Transfer learning

Transfer learning is used as a starting point when developing many modern neural networks
and helps with the problem of not having a ton of training data. The idea behind transfer
learning is that we will take a pretrained model, used to train a similar problem, and then
freeze the earlier layers of the neural network and retrain the later layers with our specific
problem. With a larger dataset, we typically train more of the later layers in a neural

##### 60 CHAPTER 7. TRAINING NEURAL NETWORKS I I

```
Load image
and label
```

### “cat”

### CNN

### Compute

### loss

```
Transform image
```

Figure 7. 2. 4 : Data augmentation trains on visually modified images rather than the original
images themselves.

network [63, 64], as shown in Figure 7.3.1. Recall from the secion on convolutional neural
networks that earlier layers of the neural network will pick up low-level features of an image,
while later levels of the network for pick up more high level detail. If we have already trained
an image classifier, then the low-level features will likely remain the same from task to task,
while the high-level features need to be adjusted.

```
Freeze these
```

```
Lower learning rate
when finetuning;
1/10 of original LR
is good starting
```

**CImonvag-** (^6) **e** (^4) point
**Conv- 64
MaxPool
Conv- 128
Conv- 128
MaxPool
Conv- 256
Conv- 256
MaxPool
Conv- 512
Conv- 512
MaxPool
Conv- 512
Conv- 512
MaxPool
FC- 4096
FC- 4096
FC- 1000**

1. Train on Imagenet

```
Image
```

```
Conv- 64
Conv- 64
```

```
MaxPool
```

```
Conv- 128
```

```
Conv- 128
```

```
MaxPool
```

```
Conv- 256
Conv- 256
```

```
MaxPool
```

```
Conv- 512
Conv- 512
```

```
MaxPool
```

```
Conv- 512
```

```
Conv- 512
```

```
MaxPool
```

```
FC- 4096
```

```
FC- 4096
FC-C
```

1. Small Dataset (C classes)

```
Freeze these
```

```
Reinitialize
this and train
```

```
Image
```

1. Bigger dataset
   **FC-C
   FC- 4096
   FC- 4096
   MaxPool
   Conv- 512
   Conv- 512
   MaxPool
   Conv- 512
   Conv- 512
   MaxPool
   Conv- 256
   Conv- 256
   MaxPool
   Conv- 128
   Conv- 128
   MaxPool
   Conv- 64
   Conv- 64**

```
Train these
```

```
With bigger
dataset, train
more layers
```

Figure 7. 3. 1 : An overview of transfer learning, where we take a pretrained model, freeze its earlier
layer and train its later layers.

We can think of the potential scenarios when using transfer learning based on the combina-
tions of data available and similarity to the dataset. Our model typically works best with a
very similar dataset, or if the dataset is very different, then we may need to finetune more
layers. Each combination is shown in Figure 7.3.2.

An important note is that transfer learning is the norm, not an exception. On most
computer vision models, even for a variety of tasks, we do not retrain a CNN model on
ImageNet; we instead use transfer learning to adapt a model to our specific task [45, 65].

##### 7.3. TRANSFER LEARNING 61

```
Image
```

```
Conv-64
Conv-64
```

```
MaxPool
```

```
Conv-128
Conv-128
MaxPool
```

```
Conv-256
Conv-256
MaxPool
```

```
Conv-512
Conv-512
MaxPool
```

```
Conv-512
Conv-512
```

```
MaxPool
```

```
FC-4096
FC-4096
FC-1000
```

```
More generic
```

```
More specific
```

```
very similar
dataset
```

```
very little data Use Linear
Classifier on
top layer
```

```
quite a lot of
data
```

```
Finetune a
few layers
```

```
very different
dataset
```

```
You’re in
trouble... Try
linear classifier
from different
stages
```

```
Finetune a
larger number
of layers
```

Figure 7. 3. 2 : How to use transfer learning based on the combinations of data available and dataset
similarity.

## Chapter 8

# Deep learning hardware and

# software

### 8.1 CPU, GPU, and TPU

Among other things, the inside of some computers contains a CPU (central processing unit)
and GPU (graphical processing unit). If we compare the different components by size, the
GPU tends to be a lot larger than the CPU. For deep learning, NVIDIA GPUs are used
almost exclusively, because of how the company has positioned in the field. Figure 8.1.1
shows a comparison between a modern CPU and GPU.

```
Speed
```

```
Clock Memory Price Speed
```

##### RAM

```
CPU 4.2 GHz System $385 ~540 GFLOPs FP32
(Intel Core
i7-7700k)
```

```
GPU
(NVIDIA
RTX 2080 Ti)
```

```
Cores
```

##### 4

```
(8 threads with
hyperthreading)
```

```
3584
GDDR6
```

```
1.6 GHz 11 GB $1199 ~13.4 TFLOPs FP32
```

```
CPU : Fewer cores,
but each core is
much faster and
much more
capable; great at
sequential tasks
```

```
GPU : More cores,
but each core is
much slower and
“dumber”; great for
parallel tasks
```

```
Figure 8. 1. 1 : A brief comparison between a state-of-the-art GPU and a state-of-the-art CPU.
```

For a task that would work well on a GPU, consider matrix multiplication. With matrix
multiplication, we can break each element of the resulting matrix into the dot product
between a particular row vector and a particular column vector as shown in Figure 8.1.2.
Since it does not matter which elements are calculated first in matrix multiplication, it would
be best to calculate each element in parallel, which is where the GPU becomes useful.

From the recent rise of deep learning, GPUs have become increasingly popular. There is
now hardward developed specificially for deep learning, which is known as a TPU (Tensor
Processing Unit). TPUs are specifically designed to speed up tensor operations. The com-

##### 62

##### 8.2. DEEP LEARNING FRAMEWORKS 63

```
A x B
B x C
```

```
A x C
```

=

Figure 8. 1. 2 : Matrix multiplication can be broken down into parallel steps, where each step
computes the dot product between a row and a column; thus, a GPU performs matrix multiplication
well.

parison between TPUs, a CPU, and a GPU is shown in Figure 8.1.3. It can also be observed
that the GigaFLOPs (which measures the number of floating point operations for a piece of
hardware) per Dollar has exploaded over the last few years as shown in Figure 8.1.4.

```
Speed
```

```
Clock Memory Price Speed
```

```
RAM
```

```
4.2 GHz System $385 ~540 GFLOPs FP32
```

```
GDDR6
```

```
1.6 GHz 11 GB $1199 ~13.4 TFLOPs FP32
```

```
HBM2
```

```
1.5 GHz 12GB $2999 ~14 TFLOPs FP32
~112 TFLOP FP16
```

```
?
HBM
```

```
64 GB $4.50
hour
```

```
per
```

```
~180 TFLOP
```

```
Cores
```

```
4
(8 threads with hyperthreading)
```

```
3584
```

```
5120 CUDA,
640 Tensor
```

```
?
```

```
CPU
(Intel Core
i7-7700k)
GPU
(NVIDIA
RTX 2080 Ti)
TPU
NVIDIA
TITAN V
TPU
Google Cloud
TPU
```

```
CPU : Fewer cores,
but each core is
much faster and
much more
capable; great at
sequential tasks
```

```
GPU : More cores,
but each core is
much slower and
“dumber”; great for
parallel tasks
```

```
TPU : Specialized
hardware for deep
learning
```

```
Figure 8. 1. 3 : Comparison between a CPU, a GPU, and TPUs.
```

NVIDIA also makes it relatively easy to write C-like code that runs directly on their GPUs
using the programming language CUDA. More recently, there are higher-level APIs for
CUDA that make it easier to write optimized code, such as cuBLAS, cuFFT, and cuDNN.
These high-level packages are useful because of how hard it is to write perfectly optimized
code in CUDA. CNN benchmarks when using optimized CUDA code, non-optimized CUDA
code, and a CPU are shown in Figure 8.1.5. OpenCL is another programming framework
that lets us write directly on any GPU, although it typically runs slower than CUDA when
using NVIDIA GPUs. In practice, we do not usually write their own code that runs directly
on the GPU. Instead, we use high-level deep learning frameworks such as PyTorch and
TensorFlow.

When running programs on a GPU, it may be costly to transfer data from the memory in
the computer to the GPU. A few ways to mitigate this problem are to put all the data in
RAM, use an SSD card (instead of HDD), or prefetch data using multiple CPU threads.

### 8.2 Deep learning frameworks

The primary goal for each deep learning framework is to allow programmers and researchers
to be able to quickly develop and test new ideas, automatically update the parameters of
the neural network, and run quickly on a GPU. In the field of deep learning, there are a

##### 64 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

Figure 8. 1. 4 : The number of GigaFLOPs on a piece of hardware has become cheaper since the
explosion of deep learning.

66x 67x 71x 64x 76x

```
(a) Performance comparison between optimized CUDA code versus a CPU.
```

2.8x (^) 3.0x 3.1x 3.4x (^) 2.8x
(b) Performance comparison between optimized CUDA code versus non-optimized CUDA code.
Figure 8. 1. 5 : CNN benchmark comparisons when running programs on different hardware [66].

##### 8.2. DEEP LEARNING FRAMEWORKS 65

bunch of different frameworks that have been developed. Just to name a few, researchers
at Facebook developed PyTorch [67], researchers at Google developed TensorFlow [68],
and researchers from the University of Washington, Carnegie Mellon, and Massachusetts
Institute of Technology, among others, have developed MXNet [69], which is the framework
of choice for Amazon Web Services. We will be focusing on PyTorch and TensorFlow, which
are most commonly used in practice. We also do not use NumPy for deep learning because
it cannot run on a GPU and we would have to manually update the gradients.

#### 8.2.1 PyTorch

PyTorch was originally created as a way to use NumPy with a GPU. If we compare the syntax
between the two frameworks, they are nearly identical in some respects. Let us consider a
computational graph with the matrix variables x, y, and z, where we are computing

```
c =
```

##### X

```
i,j
```

```
xi,jyi,j+ zi,j. (8.2.1)
```

The computational graph formed from Equation 8.2.1 is shown in Figure 8.2.1, along with
the specific syntax in both NumPy and PyTorch for calculating forward and backward
propagation. Notice that in PyTorch, the gradient calculation is much simplier and requires
us to set the parameter of requires grad=True in the PyTorch variable declaration.

x y z

* a + b Σ c

Numpy PyTorch

Figure 8. 2. 1 : Forward and backward propagation with NumPy versus PyTorch. Notice that for
the forward pass is nearly identical. On the backward pass PyTorch simplifies much of the manual
gradient calculations.

We could also easily change the PyTorch code specified in Figure 8.2.1 to run on a GPU by
using the code block that follows.

```
dev ice = ‘cu da:0’
```

N, D = 3 , 4

```
x = tor ch.randn(N, D, requires_grad=True, device=device)
y = tor ch.randn(N, D, device=device)
z = tor ch.randn(N, D, device=device)
```

```
a = x * y
b = a + z
c = tor ch.sum(b)
```

```
c .ba ckward()
print( x.grad)
```

##### 66 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

Notice that the only parts that needed to be updated was the device for each variable
initialized. As a working example for working with PyTorch, let us use a two-layer ReLU
neural network that trains on random data with an L2 loss function, as shown in the code
below. Here, we are manually computing the gradients and the updates to the weights.

dev ice = ‘cu da:0’ if torch.cuda.is\_available() else ‘cpu’

# CREATE RANDOM TENS ORS FOR THE DATA AND WEIGHTS

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in, device=de vice)
y = tor ch.randn(N, D *out, device=device)
w1 = to rch.randn(D\_in, H, device=device)
w2 = to rch.randn(H, D* out, device=device)

learning\_rate = 1 e- 6
for t in ran ge( 50 0):

# COMPUTE T HE FORW ARD PASS

h = x.m m(w1)
h\_relu = h.clamp(min=0)
y\_pred = h\_relu .mm(w2)
loss = (y\_pred - y).pow(2).sum()

```
# COMPUTE T HE BACKWARD PASS
grad_y_pred = 2. 0 * (y_pred - y)
grad_w2 = h_relu.t().mm(grad_y_pred)
grad_h_relu = grad_y_pred.mm(w2.t())
grad_h = grad_h_relu.clone()
grad_h[h < 0] = 0
grad_w1 = x.t() .mm(grad_h)
# UPDATE THE WEIGHTS USING GRADIENT DESC ENT
w1 -= learning_rate * g rad_w1
w2 -= learning_rate * g rad_w2
```

The above code looks like something we would see in NumPy, because of all the manual
computations. We can simplify everything stated above in the code block that follows.

dev ice = ‘cu da:0’ if torch.cuda.is\_available() else ‘cpu’

# CREATE RANDOM TENS ORS FOR THE DATA AND WEIGHTS

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in, device=de vice)
y = tor ch.randn(N, D *out, device=device)
w1 = to rch.randn(D\_in, H, device=device, requires\_grad=True)
w2 = to rch.randn(H, D* out, device=device, requires\_grad= Tr ue)

learning\_rate = 1 e- 6
for t in ran ge( 50 0):

# COMPUTE T HE FORW ARD PASS

y\_pred = x.mm(w1).clamp(min=0).mm(w2)
loss = (y\_pred - y).pow(2).sum()

# COMPUTE T HE BACKWARD PASS

loss.backward()

```
# DO NOT ADD ANY OF T HI S TO THE COMPUTATI ON GRAPH
with torch.no_grad():
w1 -= learning_rate * w1.grad
w2 -= learning_rate * w2.grad
```

##### 8.2. DEEP LEARNING FRAMEWORKS 67

```
w1.grad.zero_() # in place operation
w2.grad.zero_() # in place operation
```

A few things are imporant to notice here. First, we have specified only in the weights w1
and w2 that we would like the gradient to be computed, and not in the input x and y.
By doing this, we preemptively make less calculations when the backward pass is called.
Second, notice that we call torch.no grad() when we use gradient descent. Everything
inside of the with torch.no grad() environment will not be added to the computation
graph; thus, we are allowed to freely make updates to the leaf nodes of our graph. Third, on
the forward pass, there is no need to calculate intermediate variables, since PyTorch does all
the backward pass calculations. Lastly, after updating the weights using gradient descent,
we call grad.zero () in order to 0 out the weights. Inside of PyTorch, all operations that
end in an underscore ( ) are used for in place operations.

What we have been using in PyTorch to calculate back propagation is their autograd func-
tion. If we would like to, we can specify our own function’s forward and backward pass by
creating a subclass from the torch.autograd.Function class. Here, we must overwrite the
forward and backward function, as shown in the example below.

##### 68 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

class MyReLU(torch.autograd.Function):
@staticmethod
def forwar d(ctx, x):
ctx.save\_for\_backward(x)
return x.clamp(min=0)
@staticmethod
def backward(ct x, grad\_y):
x, = ctx.saved\_tensors
grad\_input = grad\_y.clone()
grad\_input[x < 0] = 0
return grad\_i nput

def my\_rel u(x):
return MyReLU.apply(x)

In the above example, we use the ctx object to cache values passed in from the forward
pass, that we will use in the backward pass. We also create a helper function that will
make it easier to call our autograd function. Now, instead of the forward pass being
x.mm(w1).clamp(min=0).mm(w2), we could call the following code.

my\_relu(x.mm(w1)) .mm(w2)

Most of the time, we will never actually need to create our own autograd functions, since we
can simply use Python and PyTorch functions. PyTorch also provides a high-level wrapper
for creating neural networks, where we must define the sequence of operations applied at
each layer. In each layer we create, PyTorch creates learnable weight objects that can be
called using the models parameters function. Using our running example of the two layer
neural network, the code using the neural network wrapper is shown below.

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in)
y = tor ch.randn(N, D\_out)

model = torch.nn.Sequential(
torch.nn.Linear(D\_in, H),
torch.nn.ReLU( ),
torch.nn.Linear(H, D\_out)
)

learning\_rate = 1 e- 2
for t in ran ge( 50 0):
y\_pred = model( x)
loss = torch.nn.fun ctional.mse\_loss(y\_pred, y)
loss.backward()

```
with torch.no_grad():
for param in model.parameters():
param - = learning_ra te * param.grad
```

```
model.zero_grad()
```

##### 8.2. DEEP LEARNING FRAMEWORKS 69

If we want to use a different optimizer instead of plain gradient descent, we can specify
which optimizer we want to use from the torch.optim package. For instance, to use Adam
optimization we could use the syntax that follows.

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in)
y = tor ch.randn(N, D\_out)

```
model = torch.nn.Sequential(
torch.nn.Linear(D_in, H),
torch.nn.ReLU( ),
torch.nn.Linear(H, D_out)
)
```

```
learning_rate = 1 e- 2
optimizer = torch.optim.Adam(m odel.paramete rs(), lr=learnin g_rate)
for t in ran ge( 50 0):
y_pred = model( x)
loss = torch.nn.fun ctional.mse_loss(y_pred, y)
```

```
loss.backward()
```

```
optimizer.step()
optimizer.zero_grad()
```

In addition to to creating sequential networks, we can define our own PyTorch module. A
module in PyTorch is a set of layers that inputs and outputs tensors. Within each module,
we only need to initialize the submodules and define the forward pass, as shown below.

```
class TwoLaye rNet(torch.nn.Module):
def __init__(self, D_in, H, D_ou t):
super(TwoLaye rNet, se lf).__init__()
self.linear1 = torch.nn.Lin ear(D_in, H)
self.linear2 = torch.nn.Lin ear(H, D_out)
```

```
def forwar d(self, x):
h_relu = self.linear1(x).clamp(min=0)
y_pred = self.linear2(h_relu)
return y_pred
```

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in)
y = tor ch.randn(N, D\_out)

```
model = TwoLayerNet(D_in, H, D _out)
```

```
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
for t in ran ge( 50 0):
y_pred = model( x)
loss = torch.nn.fun ctional.mse_loss(y_pred, y)
```

```
loss.backward()
```

```
optimizer.step()
optimizer.zero_grad()
```

It is also quite common to see a mix between custom PyTorch modules stored inside of a
sequential container as shown in the code block below.

##### 70 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

class ParallelBlock(torch.nn.Module):
def **init**(self, D\_in, D\_out):
super(TwoLaye rNet, se lf).**init**()
self.linear1 = torch.nn.Lin ear(D\_in, D\_out)
self.linear2 = torch.nn.Lin ear(D\_in, D\_out)
def forwar d(self, x):
h1 = self.linear 1 (x)
h2 = self.linear 2 (x)
return ( h 1 \* h2).clamp(min=0)

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in)
y = tor ch.randn(N, D\_out)

model = torch.nn.Sequential(
ParallelBlock(D\_in, H),
ParallelBlock(H, H) ,
torch.nn.Lienar(H, D\_out)
)

optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
for t in ran ge( 50 0):
y\_pred = model( x)
loss = torch.nn.fun ctional.mse\_loss(y\_pred, y)
loss.backward()
optimizer.step()
optimizer.zero\_grad()

Using a PyTorch DataLoader, we can wrap a Dataset to use mini-batches, shuffling, and
multithreading, among other things. With custom datasets, we can create a custom Dataset
class as shown below.

from torch.utils.data import TensorDataset, DataLoade r

N, D\_in, H, D\_out = 64 , 1000 , 10 0, 10
x = tor ch.randn(N, D\_in)
y = tor ch.randn(N, D\_out)

loa der = DataLoader(TensorDatas et( x,y), ba tch\_size=8)
model = TwoLayerNet(D\_in, H, D \_out)

optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)
for epoch in range( 20 ):
for x\_batch, y\_batch in loader:
y\_pred = model(x\_batch)
loss = torch.nn.fun ctional.mse\_loss(y\_pred, y\_ba tch)
loss.backward()
optimizer.step()
optimizer.zero\_grad()

Inside of the epoch iterator, we can get each particular batch by looping over the DataLoader
class.

##### 8.2. DEEP LEARNING FRAMEWORKS 71

Pytorch also gives us a simple way to load in popular pretrained models using the
torchvision package, as shown below. If any model is not already on the hardware being
used, then Python will go ahead and download it.

```
imp ort torchvision.models as models
```

```
resnet1 8 = models.resne t 1 8 (pretrained=True)
alexnet = models.alexnet(pretrained=True)
squeezenet = models.squeezenet1_ 0 (pretrained=True)
vgg1 6 = models.vgg1 6 (pretrained=True)
densenet = models.densenet1 6 1(pr etrained=True)
inception = models.inception_v3(pretrained=True)
```

From PyTorch and NumPy, we can also create interactive visuals using Facebook Research’s
visdom package. Visdom can do a lot, some of what is shown in Figure 8.2.2, however, we
cannot yet create computational graphs.

Figure 8. 2. 2 : A few visuals that can be created when using PyTorch and NumPy thanks to
Facebook Research’s visdom package.

Currently, the best way to create computation graphs on PyTorch is with the tensorboardX
package developed by Tzu-Wei Huang. The package works as a as a wrapper around how
TensorFlow visually displays their computation graphs in tensorboard. By default, the
computation graphs created in PyTorch are dynamic graphs; that is, a new graph is rebuilt
from scratch for each gradient descent iteration.

#### 8.2.2 TensorFlow

In our discussion of TensorFlow, we will be using TensorFlow 2.0 Beta 1. The main differ-
ence between TensorFlow 2.0 and previous versions of TensorFlow is that the graphs are
now, by default, dynamically created, when they used to static. With dynamic graphs,
TensorFlow made their package more user friendly. To build neural networks, we will be
using the Keras package, which is the primary method for creating networks in their current
official documentation. Much of this section comes from TensorFlow’s documentation on
TensorFlow 2.0 beta as the course lecture is outdated on this material.

A nice property about TensorFlow is that we can work directly with NumPy arrays. As
a running example, we will again use a two-layer neural network. This time, however, we

##### 72 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

will use a ReLU activation only in the hidden layer, and a softmax activation in the output
layer; although, it is easy to switch activations at any layer. We will also be using the mnist
dataset, which can be loaded using the code block that follows.

from tensorflow.keras import datasets

(train\_images, train\_l abels) , (test\_images, test \_labels) =   
datasets.mnist.load\_da ta()

In addition to the mnist dataset, Keras also comes with datasets for cifar10, cifar100,
boston housing, fashion mnist, imdb, and reuters. We can confirm that the data
is in the form of a NumPy array by calling type(train images), which will return
numpy.ndarray. As an aside, Matplotlib gives us a phenomenal way to visualize the dataset
using a subplot as shown below.

imp ort matplotlib.pyplot as plt

# CREATES A FIGURE OBJECT THAT (2 0 INCHES WIDE) X (1 0 I NCHES HIGH)

plt. figure(figsize=(2 0 , 10 ))

# ADD S THE FIRST 450 IMAG ES TO THE FIGURE

for i in ran ge( 45 0):

# ADD S THE iTH ELEMENT TO THE FIGURE US ING A SUBPLOT

# THA T IS (2 5 ROWS) X (50 COLUMNS)

plt. subplot(1 5 , 30 , i+1 )

# REMOVES T HE X AND Y TICKS

plt. xticks([])
plt. yticks([])

```
# SHOWS THE I MAGE IN BLACK AND WHITE, RESIZED TO BE 28 px X 2 8 px
plt. imshow(train_image s[i].reshape(2 8 ,28), cmap=plt.cm.binary)
```

Figure 8. 2. 3 : Output of the code block that creates a shows the first 450 images in the mnist
dataset.

Before we begin to build a neural network, it is often best to look closer at the data we are
using. At a glance, we can check the shape of numpy arrays using train images.shape and
test images.shape, which will give us (60000, 28, 28) and (10000, 28, 28), respectively.

##### 8.2. DEEP LEARNING FRAMEWORKS 73

When working with images, it is also most common to scale each pixel between [0, 1] to
make the choice of learning rate easier.

```
tra in_images, test_images = train_images / 25 5. 0 , test_images / 255 .0
```

Now, to create a neural network, we will use the Keras function models.Sequential, which is
quite similar to PyTorch’s torch.nn.Sequential as shown.

```
from tensorflow.keras import layers, models
```

```
model = models.Sequential([
layers.Flatten( input_shape=(2 8 , 28 )),
layers.Dense( 100 , activation=‘relu’),
layers.Dense( 10 , activation=‘s oftmax’)
])
```

When compiling the model, we call model.compile, which allows us to specify, among other
things, the type of opitimization, loss function, and performance metric.

```
model.compile(optimizer=‘adam’,
loss=‘sparse_categorical_crossentropy’,
metrics=[‘accuracy’])
```

If we want to display a summary of the model we have created, we can use the
model.summary method.

```
Model: "sequential"
_ ___________________________ ________ ___________________________ __
Layer (typ e) Out put Shape Para m #
= =========================== ======== =========================== ==
flatten (Flatten) (None, 784 ) 0
_ ___________________________ ________ ___________________________ __
dense (Dense) (None, 100 ) 78500
_ ___________________________ ________ ___________________________ __
dense (Dense) (None, 1 0) 1010
= =========================== ======== =========================== ==
Total params: 7 9, 510
Trainable params: 79 , 510
Non-train able params: 0
_ ___________________________ ________ ___________________________ __
```

To fit the model to the training data, we only need to call model.fit and specify the traning
data and training labels. By default, it will fit for 1 epoch, but we can specify how many
epochs we want as a parameter.

```
model.fit(train_images, train_labels, epochs=5)
```

Note here that train labels is a NumPy array that stores the corresponding digit in the
image of each train images figure. To test the model on our test data, we will use the
model.evaluate.

```
test_loss, test_acc = model.evaluate(test_ images, test_ labels)
```

Here, the test accuracy is a relatively excellent 0.9762, using a simple neural network!
Although, of course, the mnist dataset is far from a comprehensive test to determine how
well an algorithm performs [16]. Here, we have set tf.random.set seed(42) in order to
reproduce the results, since the weights are initialized randomly. It is also easy to change
the type of layers, to make them convolutional, batch normalized, or pooling, in a neural
network using the Keras layers module.

##### 74 CHAPTER 8. DEEP LEARNING HARDWARE AND SOFTWARE

We have only briefly touched on all the things that can be done while using TensorFlow
and PyTorch. It is possible, by the time this is read, that many of the techniques discussed
will be depreciated or out-dated; thus, it is often best to refer to the official documentation
for any of the deep learning frameworks to find the most up-to-date reference guide. Both
TensorFlow and PyTorch provide great sources of documentation, and more help can be
found from the large community of people that use each framework.

## Chapter 9

# CNN Architectures

In this section, we will be discussing commonly known CNN architectures. In particular,
we will focus on AlexNet [18], VGG [45], GoogLeNet [70], and ResNet [48]. We will also
talk about ZFNet [46], NiN (Network in Network) [71], Wide ResNet [72], ResNeXT [73],
Stochastic Depth [74], DenseNet [75], FractalNet [76], and SqueezeNet [77].

### 9.1 AlexNet

```
  
```

```
                
```

```
 
```

```
  
```

Figure 9. 1. 1 : AlexNet architecture (simplified from the two GPUs that were used in their paper
to one GPU).

AlexNet [18], as shown in Figure 9.1.1, is quite similar to earlier neural network architectures,
such as LeNet-5 [78]. However, there are a few significant details worth pointing out. To
start off, AlexNet was the first architecture that used a ReLU nonlinearity, which is now,
of course, the most commonly used nonlinearity. For regularization, it used plenty of data
augmentation, as well as dropout regularization and L2 weight decay, with the dropout
hyperparameter set to 0.5 and an L2 regularization hyperparameter set to 5e-4. At each
layer, a normalization was also applied. To train the network, they used SGD Momentum
with β = 0. 9 and a batch size of 128. They also use a learning rate of 1e-2 that was manually
reduced by a factor of 10 each time the validation accuracy plateaued. To improve their
results at the end, they used 7 CNN ensembles, which decreased the validation error rate
from around 18.2% to around 15.4%. In 2012, when the paper was published, their network
could not fit in the memory of a single GPU. So, to improvise, they used 2 GPUs with 3
GB of memory and split the neurons equally on each GPU.

AlexNet was the first CNN model to win the ImageNet challenge back in 2012. In ILSVRCs
ImageNet challenge, they achieved a 16.4% top-5 error-rate, which crushed the previous
years 25.8% top top-5 error-rate. Since then, all the winners have used CNNs and the depth
has grown significantly, as shown in Figure 9.1.2.

##### 75

##### 76 CHAPTER 9. CNN ARCHITECTURES

```
First CNN-based winner
```

```
Figure 9. 1. 2 : The winners of the ILSVRC ImageNet challenge from 2010 to 2015.
```

### 9.2 ZFNet

ZFNet [46] was the 2013 winner of the ImageNet challenge. The architecture used the same
number of layers as AlexNet, as well as the same order of layers. However, they made a
few better choices for hyperparameters. In particular, in the first layer, they changed the
convolutional filter from 11 × 11 with a stride length of 4 to 7 × 7 with a stride length of

1. In addition, the number of convolutional filters in layers 3, 4, and 5 were changed from
   384, 384, 256 to 512, 1024, 512, respectively. Their improvements dropped the model from a
   16.4% top-5 error-rate to an 11.7% top-5 error-rate. The fill architecture is shown in Figure
   9.2.1.

```
Figure 9. 2. 1 : ZFNet architecture.
```

### 9.3 VGGNet

In 2014, VGGNet [45] beat the ZFNet top-5 error rate, and came in second on the ImageNet’s
top-5 error-rate challenge, with a top-5 error-rate of 7.3%. VGGNet used significantly deeper
neural networks with fewer filters. They went from the 8-layer network found in AlexNet
and ZFNet to a 19-layer network. The filter size on each layer decreased as well. Each of
the convolution layers used only a 3 × 3 filter with a stride of 1 and a pad of 1. The pooling
layers used 2 × 2 pooling with a stride of 2.

If we stack multiple convolution filters on top of each other, then we will end up looking at
a larger portion of the image than the kernal size. For example, consider putting two 2 × 2
convolutional layers back-to-back with a stride length of one. As shown in Figure 9.3.1,
after two-convolutions, we will be looking at a 3 × 3 portion of the original image. VGG19
stacks multiple convolution filters back-to-back. Using a similar process, we can show that
stacking three 3 × 3 convolutional filters with a stride of 1 will be looking at a 7 × 7 portion
of the image. We call this 7 × 7 portion of the image the effective receptive field.

##### 9.4. GOOGLENET 77

```
f = 2 f = 2
```

Figure 9. 3. 1 : Following two convolution operations that have a filter size of 2 × 2, the effective
receptive field will be 3 × 3.

But, why not just use a 7 × 7 convolutional filter, instead of using three 3 × 3 convolutional
filters when they are both focusing on the same portion of the image. First off, with more
depth, we can represent more complex functions because of the non-linearities. Second off,
three separate layers of filters, that keep the same number of channels in the input as the
output, that each have weights of size 3 × 3 ×C and a bias for each channel C, we will have
a total of 3 · C · (3 × 3 × C + 1) parameters, where C represents the number of channels.
With a single-layer that has a 7 × 7 × C number of weights, with C bias parameters, we
will have a total of C ·(7 × 7 ×C + 1) parameters. Thus, using three separate convolutional
layers with 3 × 3 filters will use less parameters than a single 7 × 7 convolutional filter.

VGGNet consists of two separate neural network architectures: VGG16 and VGG19.
VGG16 has 16 layers and VGG19 has 19 layers. VGG19 has three extra convolutional
layers towards the end of the network. The differences between the network are not all that
significant, and VGG19 performs only slighly better while using more memory. The com-
plete architectures for VGG19 and VGG16, in comparison to AlexNet are shown in Figure
9.3.2.

### 9.4 GoogLeNet

GoogLeNet [70] won the 2014 ImageNet challenge and brought the top-5 error rate down to
6.7%. The network was made up of 22 layers with only around 4 million parameters. To is
roughly 15x less parameters than AlexNet, which had approximately 60 million parameters.
The network used no fully connected layers. Instead, they developed upon what is konwn
as an Inception Module.

Inception modules applies multiple types of transformations to the previous layer, and then
stack in depth to form a single output. The inception modules on GoogLeNet are made up
from the transformations of a 1 × 1 convolution, 3 × 3 convolution, 5 × 5 convolution, and
3 ×3 max pooling. Consider an input layer of size 28 × 28 ×256. Suppose we also arbitarary
choose to use 128 1 × 1 filters, 192 3 × 3 filters, 96 5 × 5 filters, and 3 × 3 max pooling
(that retains the same depth in the input image). We will also use same padding to make
the dimensions of the output workout; that is, the height and width of the input is equal
to the height and width of the output. Suppose we now stack each of the outputs from the
transformations as shown in Figure 9.4.1.

Stacking all of the transformations to the input depth-wise, we will have a depth of 128 +
192 + 96 + 256 = 672. We can also workout the total number of operations from the
convolutional operations. For simplicity, we will leave off the bias unit. Starting with the
1 × 1 convolution, we will have 128 (one for each channel) different (1 ×1) × 256 filters that
are each applied to a 28 × 28 image; thus, we will have 28 × 28 × 128 × 1 × 1 × 256 ≈ 26
million operations with the 1×1 convolution operation. Using a similar process, the number
of operations in the 3×3 convolutional layer will be 28× 28 × 192 × 3 × 3 × 256 ≈ 347 million.
Similarily, with the 5 × 5 convolutional operator, we will have a total of 28 × 28 × 96 × 5 ×
5 × 256 ≈ 482 million operations. Summing the total number of operations, we will have

##### 78 CHAPTER 9. CNN ARCHITECTURES

```
3 x 3 conv, 128
Pool
3 x 3 conv, 64
3 x 3 conv, 64
Input
```

```
3 x 3 conv, 128
```

```
Pool
```

```
3 x 3 conv, 256
```

```
3 x 3 conv, 256
```

```
Pool
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
Pool
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
Pool
```

```
FC 4096
```

```
FC 1000
```

```
Softmax
```

```
FC 4096
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 384
Pool
5 x 5 conv, 256
11 x 11 conv, 96
Input
```

```
Pool
```

```
3 x 3 conv, 384
```

```
3 x 3 conv, 256
```

```
Pool
```

```
FC 4096
```

```
FC 4096
```

```
Softmax
FC 1000
```

```
Pool
```

```
Input
```

```
Pool
```

```
Pool
```

```
Pool
```

```
Pool
```

```
Softmax
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 256
```

```
3 x 3 conv, 256
```

```
3 x 3 conv, 128
```

```
3 x 3 conv, 128
```

```
3 x 3 conv, 64
3 x 3 conv, 64
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
3 x 3 conv, 512
```

```
FC 4096
```

```
FC 1000
```

```
FC 4096
```

AlexNet VGG 16 VGG 19

```
conv 1 - 1
```

```
conv 1 - 2
```

```
conv 2 - 1
```

```
conv 2 - 2
```

```
conv 3 - 1
```

```
conv 3 - 2
```

```
conv 4 - 1
```

```
conv 4 - 2
```

```
conv 4 - 3
```

```
conv 5 - 1
```

```
conv 5 - 2
```

```
conv 5 - 3
```

Common names

```
fc 6
```

```
fc 7
```

```
fc 8
```

```
Figure 9. 3. 2 : The architecture differences between VGG16, VGG19, and AlexNet.
```

```
Input
```

**1 x 11 2 con 8 v, 3 x 31 con 92 v, 5 x 5 9 con 6 v,** (^3) **x 3 pool**
Filter
concatenation
Module input:
28 x 28 x 256
28 x 28 x 128 28 x 28 x 192 28 x 28 x 96 28 x 28 x 256
28 x 28 x( 128 + 192 + 96 + 256 ) = 28 x 28 x 672
Figure 9. 4. 1 : Na ̈ıve implementation of an inception module.
a total of around 850 million operations in just this layer! That is super computationally
expensive!
As a precursor, let us consider what happens when we use a 1 × 1 convolution operation.
If we were to only apply a single 1 × 1 convolution to an input that has a depth of 1, then

##### 9.4. GOOGLENET 79

we would just be scaling each element by the value inside of the 1 × 1 matrix. However,
the value of a 1 × 1 convolution does not come from applying it to an input of depth 1;
rather, the value come from applying it to any depth greater than 1. Consider if we applied
a 1 × 1 convolution with 32 separate filers to a 56 × 56 × 64 input. Here, the filter size will
be 1 × 1 × 64 and over each spatial part of the image, a dot product is computed between
the filter and teh 1 × 1 × 64 part of the image, resulting in a 56 × 56 × 32 output as shwon
in Figure 9.4.2. What we have just done keep the input and output dimensions equal (at
56 ×56), while significantly reducing the number of channels from 64 to 32. Maybe it would
be useful to reduce the depth of the inception modeule in order to reduce the number of
operations used!

##### 64

##### 56

##### 56

```
1x1 CONV
with 32 filters
```

##### 32

##### 56

##### 56

```
(each filter has size
1x1x64, and performs a
64-dimensional dot
product)
```

Figure 9. 4. 2 : Applying a 1 × 1 convolution with 32 filters to a 56 × 56 × 64 input produces a
56 × 56 × 32 output.

Continuing on with the idea of a 1 × 1 convolution operation, let us consider adding 64
1 × 1 operations before the 3 × 3 and 5 × 5 convolutions. We will also first pool the layers,
and then apply 64 1 × 1 convolutions in order to better preserve the spatial structure of
the previous layer. Both of these changes are shown in Figure 9.4.3. In total, we will have
shrunk the number of filter in the output from 672 to 480.

```
Module input:
28 x 28 x 256
```

```
1 x 1 conv,
64
```

```
Previous Layer
```

```
3 x 3 pool
```

```
5 x 5 conv,
96
```

```
3 x 3 conv,
192
```

```
Filter
concatenation
```

```
1 x 1 conv,
64
```

```
1 x 1 conv,
64
```

```
1 x 1 conv,
128
28 x 28 x 64 28 x 28 x 64 28 x 28 x 256
```

```
28 x 28 x 128 28 x 28 x 192 28 x 28 x 96 28 x 28 x 64
```

```
28 x 28 x 480
```

Figure 9. 4. 3 : Improved implementation of an inception module by stacking 1 × 1 convolution
operations.

Now, let us work out the number of calculations required from the convolution operations
in Figure 9.4.3. Starting from the left side, the 128 1 × 1 × 256 convolution operations again
require

```
1 × 1 × 256 × 28 × 28 × 128 ≈ 25 million operations, (9.4.1)
```

##### 80 CHAPTER 9. CNN ARCHITECTURES

which is the same as before. Next, looking at the 64 1 × 1 × 256 convolution operations that
are then passed to 192 3 × 3 convolution operations will require
(1 × 1 × 256 × 28 × 28 ×64) + (3 × 3 × 64 × 28 × 28 ×192) ≈ 100 million operations, (9.4.2)

conpared to the 347 million operations that we had before. The difference between 100
million operations and 347 million operations is significantly less costly! Next, looking at
the 64 1 × 1 ×256 convolution operations that are then passed through 96 5 ×5 convolution
operations, we will have a total of
(1 × 1 × 256 × 28 × 28 ×64) + (5 × 5 × 64 × 28 × 28 ×96) ≈ 133 million operations, (9.4.3)
compared to 482 million operations without using a 1 × 1 convolution. Finally, the 64
1 × 1 × 256 convolution operations following the 3 × 3 pooling will require
1 × 1 × 256 × 28 × 28 × 64 ≈ 3 million operations. (9.4.4)
In total, we have shrunk the model to have around 260 million operations, in comparison
to the 850 million previously used!

In addition to stacking inception modules as layers, GoogLeNet also uses two auxiliary
classification outputs after middle layers. Auxiliary classification outputs work as though
they are making predictions for the model, except their prediction results are never uses.
Instead, they are added to further change the weights in earlier layers of the neural network
through backpropagation. The complete network is shown in Figure 9.4.4

```
input
7x7+2(S)Conv
```

```
3x3+2(S)MaxPool
```

```
LocalRespNorm
1x1+1(V)Conv
```

```
3x3+1(S)Conv
```

```
LocalRespNorm
3x3+2(S)MaxPool
```

```
1x1+1(S)Conv
1x1+1(S)Conv1x1+1(S)Conv MaxPool3x3+1(S)
```

```
Dept Concat
3x3+1(S)Conv5x5+1(S)Conv 1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv1x1+1(S)Conv MaxPool3x3+1(S)
```

```
ConvDept Concat
3x3+1(S)5x5+1(S)Conv 1x1+1(S)Conv
```

```
3x3+2(S)MaxPool
```

```
1x1+1(S)Conv
1x1+1(S)Conv1x1+1(S)Conv MaxPool3x3+1(S)
```

```
Dept Concat
3x3+1(S)Conv5x5+1(S)Conv 1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv1x1+1(S)Conv MaxPool3x3+1(S)AveragePool5x5+3(V)
```

```
Dept ConcatConv
3x3+1(S)5x5+1(S)Conv 1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv 1x1+1(S)Conv3x3+1(S)MaxPool
```

```
Dept Concat
3x3+1(S)Conv 5x5+1(S)Conv1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv 1x1+1(S)Conv3x3+1(S)MaxPool
```

```
ConvDept Concat
3x3+1(S) 5x5+1(S)Conv1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv 1x1+1(S)Conv MaxPool3x3+1(S)AveragePool5x5+3(V)
```

```
Dept Concat
3x3+1(S)Conv 5x5+1(S)Conv 1x1+1(S)Conv
```

```
3x3+2(S)MaxPool
```

```
1x1+1(S)Conv
1x1+1(S)Conv 1x1+1(S)Conv3x3+1(S)MaxPool
```

```
Dept Concat
3x3+1(S)Conv 5x5+1(S)Conv1x1+1(S)Conv
```

```
1x1+1(S)Conv
1x1+1(S)Conv 1x1+1(S)Conv3x3+1(S)MaxPool
```

```
Dept Concat
3x3+1(S)Conv 5x5+1(S)Conv1x1+1(S)Conv
```

```
AveragePool7x7+1(V)
FC
```

```
1x1+1(S)Conv
```

```
FC
```

```
FC
```

```
SoftmaxActivation
```

```
softmax0
```

```
1x1+1(S)Conv
```

```
FC
```

```
FC
```

```
SoftmaxActivation
```

```
softmax1
```

```
SoftmaxActivation
```

```
softmax2
```

```
AveragePool5x5+3(V)
```

```
nv1(S) 1x1+1(S)Conv
```

```
FC
```

```
FC
```

```
SoftmaxActivation
```

```
softmax1
Auxiliary
classification
outputs
```

Inception module

```
1x 1 convolutions
```

```
3x 3 convolutions 5x 5 convolutions
```

```
Filter
concatenation
```

```
Previous layer
```

```
1x 1 convolutions 1x 1 convolutions 3x 3 max pooling
```

```
1x 1 convolutions
```

Figure 9. 4. 4 : The layers of GoogLeNet is made up of inception modules with two auxiliary
classification outputs.

In total, GoogLeNet had 22 separate layers with weights, none of which were fully-connected
layers, around 15x less parameters than AlexNet and won the 2014 ImageNet classification
challenge with a top-5 error rate of 6.7%.

##### 9.5. RESNET 81

### 9.5 ResNet

In 2015, ResNet [48] won the ImageNet challenge with a top-5 error rate of 3.57%. This
error-rate even beat the estimated human-level error-rate of 5% [79]. ResNet was deeper
than any successful network previously trained, with a total of 152 layers!

The ResNet paper starts off by testing what happens if the number of layers in a neural
network is increased significantly. What they found was that with more layers in a neural
network, both the training error and testing error was worse, as shown in Figure 9.5.1.
Because the training error rate is worse from the larger neural network is worse than that
of the more shallow network, overfitting of the parameters is not occuring.

```
Tr
```

```
ai
ning
```

```
e
```

```
rro
```

```
r
```

```
Iterations
```

```
56 - layer
```

```
20 - layer
```

```
Te
```

```
st
e
rro
```

```
r
```

```
Iterations
```

```
56 - layer
```

```
20 - layer
```

Figure 9. 5. 1 : By simply stacking more layers onto a neural network, the authors of ResNet showed
that the performance of the network will actually be worse.

A neural network with more layers has a larger sample space of functions than a neural
network with fewer layers. Thus, the authors hypothesised that the problem with deeper
networks are that they are harder to optimize.

The solution, that they came up with, was to have the linear activations H(x) be the
output from the convolution operation added to the input from two layers ago, as shown in
Figure 9.5.2. Here, if all of the parameters in the convolution operations were 0, then the
convolution layers would act like an identity function and not add any new information to
the input x. Thus, passing x through more layers would only allow a better representation
function to be formulated. This property of having all of the weights at 0 mapping to the
identity function works well with L2 regularization. The weights also do not have to learn
as much information as they did with “plain” layers, since they only have to decide what to
add or subtract from x.

```
relu
```

```
X
Residual block
```

```
conv
```

```
conv
X
identity
```

```
F(x) + x
```

```
F(x)
```

```
relu
```

```
conv
```

```
conv
relu
```

```
X
“Plain” layers
```

```
H(x)
```

### H(x) = F(x) + x

### Use layers to

### fit residual

### F(x) = H(x) - x

### instead of

### H(x) directly

```
Figure 9. 5. 2 : “Plain” layers versus residual blocks.
```

The full ResNet architecture is shown in Figure 9.5.3. When they tested out the network,
they used four variational models, with the depths of 34, 50, 101, and 152. For all of the

##### 82 CHAPTER 9. CNN ARCHITECTURES

models with ResNet models with over 50 layers, bottlenecking (the use of 1 × 1 convolutions
to change the depth of a network) was used to improve efficiency, as shown in Figure 9.5.4.

To train the network, the authors used Xavier initialization and batch normalization after
the convolution layers. SGD with momentum (0.9 momentum coefficient) and an initial
learning rate of 0.1 that was reduced by a factor of 10 at each plateau during validation
were used. In addition, the batch sizes were 256 and weight decay with a regularization
hyperparameter of 1e-5 were also used.

In addition to the ImageNet classification challenge, the network swept all of the other domi-
nant computer vision competitions that year. With ImageNet Detection, ResNet performed
16% better than 2nd place; with ImageNet Localization, ResNet performed 26% better than
2nd place; with COCO Detection, ResNet performed 11% better than 2nd place; and with
COCO Segmentation, ResNet performed 12% better than 2nd place.

```
Input
```

```
Softmax
```

```
3 x 3 conv, 64
```

```
7 x 7 conv, 64 , / 2
```

```
FC 1000
```

```
Pool
```

```
3 x 3 conv, 64
```

```
3 x 3 conv, 64
3 x 3 conv, 64
```

```
3 x 3 conv, 64
3 x 3 conv, 64
```

```
3 x 3 conv, 128
3x3 conv, 128, / 2
```

```
3 x 3 conv, 128
3 x 3 conv, 128
```

```
3 x 3 conv, 128
3 x 3 conv, 128
```

```
3 x 3 conv, 512
3 x 3 conv, 512 , / 2
```

```
3 x 3 conv, 512
3 x 3 conv, 512
```

```
3 x 3 conv, 512
3 x 3 conv, 512
```

```
Pool
```

relu

```
X
Residual block
```

```
3x3 conv
```

```
3x3 conv
X
identity
```

F(x) + x

F(x)

relu

```
3x3 conv, 64
filters
```

```
3x3 conv, 128
filters, /2
spatially with
stride 2
```

```
Figure 9. 5. 3 : The full ResNet architecture.
```

### 9.6 Comparisons between network architectures

If we look at many of the popular neural networks, as shown in Figure 9.6.1, we can compare
their performance based on the number of operations necessary to perform, along with their
memory storage. Figure 9.6.2 denotes the amount of times per forward pass, based on the
batch size, along with the power consumption of each network. More comparisons are looked
at in the paper An Analysis of Deep Neural Network Models for Practical Applications [80].

##### 9.7. ADDITIONAL ARCHITECTURES 83

```
1 x1 conv, 256
```

```
3 x3 conv, 64
```

```
1 x1 conv, 64
```

```
input
```

```
28 x2 8 x2 56
```

```
1x1 conv, 64 filters
to project to
28x28x64
```

```
3x3 conv operates over
only 64 feature maps
```

```
1x1 conv, 256 filters projects
back to 256 feature maps
(28x28x256)
```

```
output
```

```
28 x2 8 x2 56
```

Figure 9. 5. 4 : With all of the ResNet models that had over 50 layers, the Residual blocks used
bottleneck layers.

Figure 9. 6. 1 : The top-1 percent accuracy of each network based on the number of operations [80].
The size of the circle denotes the amount of memeory that the network uses.

Figure 9. 6. 2 : Forward propagation times (in ms) for popular networks, along with their power
usage [80].

### 9.7 Additional architectures

#### 9.7.1 NiN: Network in Network

Network in Network (NiN) [71] introduced the idea of 1 × 1 convolutions that would go on
to set-up the bottleneck layers on GoogLeNet and ResNet. The network works by first using
a convolutional filter and then downsampling it using at least a single 1 × 1 convolution, as
shown in Figure 9.7.1.

##### 84 CHAPTER 9. CNN ARCHITECTURES

Figure 9. 7. 1 : NiN architecture, where the fully-connected layers in the image represent the 1 × 1
convolution operations.

#### 9.7.2 Improving ResNets

In Identity Mapping in Deep Residual Networks [81], Kaiming He and others showed that
the residual block in Figure 9.7.2 improved the performance of the model.

```
conv
```

```
BN
```

```
ReLU
```

```
conv
```

```
ReLU
```

```
BN
```

```
Figure 9. 7. 2 : Improved residual block design.
```

Soon after, Sergey Zagoruyko and Nikos Komodakis hypothesised that the important part
of ResNet are the residual blocks themselves, and not the depth [72]. In the paper, they
significantly increased the number of filters in each layer and showed that their 50-layer
wide ResNet outperforms the 152-layer original ResNet, as shown in Figure 9.7.3. By
increasing the width of the network and decreasing the number of layers, they were able to
use parallelize more operations, which led to a more efficient algorithm.

The original authors of ResNet then looked to continue improving on their design with
ResNeXt [73]. The main contributions of ResNeXt are for creating cardinality in the net-
work. Cardinality consists of creating multiple different parallel pathways through each
layer, as shown in Figure ??. The idea of creating multiple parallel pathways for a function
to learn whatever it wants is similar to an Inception module.

Another improvement to the training time of ResNet came from using stochastic depth
during the training phase [74]. The idea is similar to dropout regularization, in that a
random set of residual blocks would be shut off on each training pass, as shown in Figure
9.7.5. Come test time, the entire network will be used.

##### 9.7. ADDITIONAL ARCHITECTURES 85

Basic residual block Wide residual block

```
3 x 3 conv, F
```

```
3 x 3 conv, F
```

```
3 x 3 conv, F x k
```

```
3 x 3 conv, F x k
```

```
Figure 9. 7. 3 : The original residual blocks versus wide residual blocks.
```

```
1 x 1 conv, 256
```

```
3 x 3 conv, 4
```

```
1 x 1 conv, 4
```

```
256 - d out
```

```
256 - d in
```

```
1 x 1 conv, 256
```

```
3 x 3 conv, 4
```

```
1 x 1 conv, 4
```

```
1 x 1 conv, 256
```

```
3 x 3 conv, 4
```

```
1 x 1 conv, 4
```

```
...
paths
```

```
32
```

```
Figure 9. 7. 4 : Adding cardinality to ResNet was the main contribution of ResNeXt.
```

Figure 9. 7. 5 : Original ResNet keeps all the residual blocks activated during the training phase
(top) and ResNet with stochastic depth turns off a random sample of residual blocks during each
training pass (bottom).

##### 86 CHAPTER 9. CNN ARCHITECTURES

#### 9.7.3 FractalNet

FractalNet argues that we should focus on the transition from shallow networks to deep
networks, instead of focusing on improving residual blocks [76]. Their proposed architecture
uses both shallow and deep paths to the output and drops particular paths at random during
training. Similar to other regularizations with stochastic depth, the entire network is used
at test time. The complete architecture is shown in Figure 9.7.6.

```
Figure 9. 7. 6 : FractalNet architecture
```

#### 9.7.4 DenseNet

DenseNet works by connecting each layer to every other layer in a feedforward manner
[75], as shown in Figure 9.7.7. The authors of the paper show that using dense blocks helps
with the problem of vanishing gradients, strengthens feature propagation, and leads to more
features being reused throughout the network.

#### 9.7.5 SqueezeNet

SqueezeNet uses 50 times fewer parameters than AlexNet and achieves nearly the same
accuracy with a model size that is less than 0.5 MB (510x smaller than AlexNet) [77].
SqueezeNet consists of fire modules, which first shrink the depth of the input using 1 × 1
convolutional filters, and then expand the depth using combinations of 1 × 1 and 3 × 3
convolutional filters, as shown in Figure 9.7.8.

##### 9.7. ADDITIONAL ARCHITECTURES 87

```
Pool
Conv
Dense Block 1
Conv
Input
```

```
Conv
```

```
Dense Block 2
```

```
Conv
```

```
Pool
```

```
Conv
```

```
Dense Block 3
```

```
Softmax
FC
Pool
```

```
Conv
```

```
1 x1 conv, 64
```

```
1 x1 conv, 64
```

```
Concat
```

```
Concat
```

```
Concat
```

```
Conv
```

```
Input
```

Dense Block

```
Figure 9. 7. 7 : Dense blocks concatenate all of the previous inputs into the input in later layers.
```

Figure 9. 7. 8 : Fire modules that squeeze each layer using 1×1 convolution filters, and then expand
those layers using both 1 × 1 and 3 × 3 convolution filters.

## Chapter 10

# RNNs: Recurrent neural

# networks

### 10.1 Introduction

Up until this point, we have only dealt with vanilla neural networks that are in the form of
fixed input sizes mapping to fixed output sizes. For example with CIFAR10 classification,
all of our input images are 32 × 32 × 3 and our output is a vector of length 10, where each
element of the output corresponds to a particular class. With recurrent neural networks
(RNNs), we are able to use a variable length for both our input and output as shown in
Figure 10.1.1. With RNNs, we can represent one to many models, such as image captioning;
many to one models, such as sentiment classificaiton; and many to many models, such as
language translation and video classification frame-by-frame. Even with a one to one model,
RNNs still may be useful. For example, suppose we are trying to classify images. Instead of
using a traditional feedforward neural network, we can take a variable number of “glimpses”
of the image to then use in order to classify the image [82, 83].

```
Figure 10. 1. 1 : RNNs are able to use a variable length for our input and output.
```

The basic form of a recurrent neural network is to take in some input x, then update a
hidden state inside of a model, and then produce an output y. We can represent recurrent
neural networks using a recursive formula
ht= f(ht− 1 , xt; W ), (10.1.1)
where htis the new hidden state, ht− 1 is the previous state, xtis an input vector at timestep
t, and f is a function parameterized by W. A vanilla RNN may look something like
ht= tanh(Whhht− 1 + Wxhxt). (10.1.2)
The hidden state h can then be passed into a function to produce the output predictions.
The function is typically a matrix multiplication in the form
yt= Whyht. (10.1.3)

##### 88

##### 10.1. INTRODUCTION 89

```
h 0 fW h 1 fW h 2 fW h 3
```

```
x 3
```

```
yT
```

…

```
W x^1 x^2
```

```
hT
```

```
y 1 L 1 y 2 L 2 y 3 L 3 LT
```

```
L
```

```
(a) Many-to-many
```

```
h 0 fW h 1 fW h 2 fW h 3
```

```
x 3
```

```
y
```

…

```
W x^1 x^2
```

```
hT
```

```
(b) Many-to-one
```

```
h 0 fW h 1 fW h 2 fW h 3
```

```
yT
```

…

```
W x
```

```
hT
```

```
y 3 y 3 y 3
```

```
(c) One-to-many
```

```
h
0 fW
```

```
h
1 fW
```

```
h
2 fW
```

```
h
3
x
3
```

```
...
x
2
```

```
x
W 1 1
```

```
h
T
```

```
y
1
```

```
y
2
...
```

```
M sequence in a single vector any to one : Encode input
```

```
O sequence from single input vector ne to many : Produce output
```

```
fW h 1 fW h 2 fW
W
2
```

```
(d) Many-to-one-to-many
Figure 10. 1. 2 : The computation graphs for different types of models.
```

The computation graphs for different types of RNNs are shown in Figure 10.1.2. A common
use for RNNs are to build language models that predict the next word or character, given
the previous characters. We can encode our input with one-hot encoding, given a set of
all possible inputs. For example, if we have the vocabulary list [h, e, l, o] with the sequence
“hello”, then the steps for our vanilla RNN are shown in Figure 10.1.4. After we have trained
a character-level language model, we can use it to generate new text, which is similar to
the text it trained on. To sample by characters, we take in as input all of the previously
sampled characters and output a probablity distribution that we will sample our character
from, as shown in Figure 10.1.3.

**..** (^0133)
**..** (^0804)
**..** (^2250)
**..** (^0550)
**..** (^1117)
**..** (^6083)
**..** (^1012)
Softmax **..** (^0789)
Sample “e” “l” “l” “o”
Figure 10. 1. 3 : Using our language model for sampling after it has been trained.

##### 90 CHAPTER 10. RNNS: RECURRENT NEURAL NETWORKS

```
(a) The input uses one-hot encoding to de-
note each letter that is present.
```

```
(b) The hidden states are calculated.
```

```
(c) The outputs are predicted.
Figure 10. 1. 4 : The general structure of our vanilla RNN.
```

The idea of calculating the loss at the end of the time series and then going backwards
through the time steps is often referred to as backpropagation through time.

```
Loss
```

```
Figure 10. 1. 5 : Backpropagation through time
```

Backpropataion through time is often not the best idea due to the memory and time con-
straints on computers. Consider training all of Wikipedia, for example, using backpropaga-
tion through time; it would just take too long for our model to converge and would be too

##### 10.1. INTRODUCTION 91

computationally expensive. Instead, we commonly use truncated backpropagation through
time, where we calculate forward and backward passes over chunks of the sequence as shown
in Figure 10.1.6. In practice, the size of the chuck may be around 100. We can compare
trucated backpropataion through time to the use of a mini-batch with gradient descent, as
apposed to using the entire training batch.

```
Loss Loss Loss
```

```
Figure 10. 1. 6 : Truncated backpropagation through time
```

If we train our RNN model for a while, we may generate what is shown in Figure 10.1.7.
Andrej Karpathy wrote an amazing blog back in 2015 that goes over more results [84].

```
train more
```

```
train more
```

```
train more
```

```
at first:
```

Figure 10. 1. 7 : A Shakesphere trained model that is showing the results produced at a select few
training phases.

We can interpret these results by looking inside of the hidden state. In the few examples
shown in Figure 10.1.8, we can see where the model is confident in its character preditions
and where it is not confident.

##### 92 CHAPTER 10. RNNS: RECURRENT NEURAL NETWORKS

Figure 10. 1. 8 : Characters that the model is confident it chose correctly are shown in red and
characters the model is not confident about are shown in blue.

### 10.2 Image captioning

With RNNs, we can caption images of variable lengths. The general structure that has
worked well for image captioning is to first pass an image through a convolutional neural
network, and then pass one of the layers towards the end into a one-to-many recurrent neural
network [41, 85, 86, 87, 88], as shown in Figure 10.2.1. We typically pass the activations
from one of the later layers, that still have many neurons, into the RNN, since that layer
captures high-level semantic information about an image. To train the network, we can
backpropagate through both the CNN and RNN to update the weights.

##### 10.2. IMAGE CAPTIONING 93

**Convolutional Neural Network**

**Recurrent Neural Network**

Figure 10. 2. 1 : Image captioning network that passes an inputted image through a CNN, with a
later layer passed into a one-to-many RNN [41]

## Bibliography

[1] A. Parker, In the blink of an eye: how vision sparked the big bang of evolution. Basic
Books, 2003.
[2] D. H. Hubel and T. N. Wiesel, “Receptive fields of single neurones in the cat’s striate
cortex,” The Journal of physiology, vol. 148, no. 3, pp. 574–591, 1959.
[3] L. G. Roberts, Machine perception of three-dimensional solids. PhD thesis, Mas-
sachusetts Institute of Technology, 1963.
[4] S. A. Papert, “The summer vision project,” 1966.
[5] R. A. Brooks, R. Creiner, and T. O. Binford, “The acronym model-based vision sys-
tem,” in Proceedings of the 6th international joint conference on Artificial intelligence-
Volume 1 , pp. 105–113, Morgan Kaufmann Publishers Inc., 1979.
[6] M. A. Fischler and R. A. Elschlager, “The representation and matching of pictorial
structures,” IEEE Transactions on computers, no. 1, pp. 67–92, 1973.
[7] D. Marr et al., Vision: A computational investigation into the human representation
and processing of visual information. San Francisco: WH Freeman, 1982.
[8] J. Canny, “A computational approach to edge detection,” in Readings in computer
vision, pp. 184–203, Elsevier, 1987.
[9] D. G. Lowe, “Three-dimensional object recognition from single two-dimensional im-
ages,” Artificial intelligence, vol. 31, no. 3, pp. 355–395, 1987.
[10] J. Shi and J. Malik, “Normalized cuts and image segmentation,” IEEE Transactionson
Pattern Analysis and Machine Intelligence, vol. 22, no. 8, pp. 888–905, 2000.
[11] P. Viola, M. Jones, et al., “Rapid object detection using a boosted cascade of simple
features,” CVPR (1), vol. 1, pp. 511–518, 2001.
[12] D. G. Lowe et al., “Object recognition from local scale-invariant features.,” in iccv,
vol. 99, pp. 1150–1157, 1999.
[13] N. Dalal and B. Triggs, “Histograms of oriented gradients for human detection,” 2005.
[14] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan, “Object detec-
tion with discriminatively trained part-based models,” IEEE transactions on pattern
analysis and machine intelligence, vol. 32, no. 9, pp. 1627–1645, 2009.
[15] M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zisserman, “The pascal
visual object classes (voc) challenge,” International journal of computer vision, vol. 88,
no. 2, pp. 303–338, 2010.
[16] N. Pinto, D. D. Cox, and J. J. DiCarlo, “Why is real-world visual object recognition
hard?,” PLoS computational biology, vol. 4, no. 1, p. e27, 2008.
[17] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-scale
hierarchical image database,” in 2009 IEEE conference on computer vision and pattern
recognition, pp. 248–255, Ieee, 2009.
[18] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with deep
convolutional neural networks,” in Advances in neural information processing systems,
pp. 1097–1105, 2012.
[19] A. Krizhevsky, “Learning multiple layers of features from tiny images,” tech. rep.,
Citeseer, 2009.

##### 94

##### BIBLIOGRAPHY 95

[20] L. Fei-Fei and P. Perona, “A bayesian hierarchical model for learning natural scene cat-
egories,” in 2005 IEEE Computer Society Conference on Computer Vision and Pattern
Recognition (CVPR’05), vol. 2, pp. 524–531, IEEE, 2005.

[21] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick, S. Guadarrama,
and T. Darrell, “Caffe: Convolutional architecture for fast feature embedding,” arXiv
preprint arXiv:1408.5093, 2014.
[22] V. Nair and G. E. Hinton, “Rectified linear units improve restricted boltzmann
machines,” in Proceedings of the 27th international conference on machine learning
(ICML-10), pp. 807–814, 2010.
[23] F. Perucho, “Neuron.” https://thenounproject.com/term/neuron/214105/.
[24] M. London and M. H ̈ausser, “Dendritic computation,” Annu. Rev. Neurosci., vol. 28,
pp. 503–532, 2005.
[25] R. Acosta, “Ibm automatic sequence controlled calculator sequence indicators.”
https://en.wikipedia.org/wiki/File:IBM\_Automatic\_Sequence\_Controlled\_
Calculator\_Sequence\_Indicators.jpg.
[26] F. Rosenblatt, “The perceptron: a probabilistic model for information storage and
organization in the brain.,” Psychological review, vol. 65, no. 6, p. 386, 1958.
[27] B. Widrow and M. A. Lehr, “30 years of adaptive neural networks: perceptron, mada-
line, and backpropagation,” Proceedings of the IEEE, vol. 78, no. 9, pp. 1415–1442,
1990.

[28] B. Widrow and M. E. Hoff, “Adaptive switching circuits,” tech. rep., Stanford Univ Ca
Stanford Electronics Labs, 1960.
[29] D. E. Rumelhart and G. E. Hintonf, “Learning representations by back-propagating
errors,” NATURE, vol. 323, p. 9, 1986.
[30] G. E. Hinton and R. R. Salakhutdinov, “Reducing the dimensionality of data with
neural networks,” science, vol. 313, no. 5786, pp. 504–507, 2006.
[31] A.-r. Mohamed, G. E. Dahl, and G. Hinton, “Acoustic modeling using deep belief
networks,” IEEE transactions on audio, speech, and language processing, vol. 20, no. 1,
pp. 14–22, 2011.
[32] G. E. Dahl, D. Yu, L. Deng, and A. Acero, “Context-dependent pre-trained deep neural
networks for large-vocabulary speech recognition,” IEEE Transactions on audio, speech,
and language processing, vol. 20, no. 1, pp. 30–42, 2011.
[33] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look once: Unified,
real-time object detection,” in Proceedings of the IEEE conference on computer vision
and pattern recognition, pp. 779–788, 2016.

[34] J. Redmon and A. Farhadi, “Yolov3: An incremental improvement,” arXiv preprint
arXiv:1804.02767, 2018.
[35] S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-cnn: Towards real-time object de-
tection with region proposal networks,” in Advances in neural information processing
systems, pp. 91–99, 2015.
[36] C. Farabet, C. Couprie, L. Najman, and Y. LeCun, “Learning hierarchical features
for scene labeling,” IEEE transactions on pattern analysis and machine intelligence,
vol. 35, no. 8, pp. 1915–1929, 2012.
[37] M. Bojarski, D. Del Testa, D. Dworakowski, B. Firner, B. Flepp, P. Goyal, L. D. Jackel,
M. Monfort, U. Muller, J. Zhang, et al., “End to end learning for self-driving cars,”
arXiv preprint arXiv:1604.07316, 2016.
[38] A. Toshev and C. Szegedy, “Deeppose: Human pose estimation via deep neural net-
works,” in Proceedings of the IEEE conference on computer vision and pattern recogni-
tion, pp. 1653–1660, 2014.
[39] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves,
M. Riedmiller, A. K. Fidjeland, G. Ostrovski, et al., “Human-level control through deep
reinforcement learning,” Nature, vol. 518, no. 7540, p. 529, 2015.

##### 96 BIBLIOGRAPHY

[40] K. Xu, J. Ba, R. Kiros, K. Cho, A. Courville, R. Salakhudinov, R. Zemel, and Y. Bengio,
“Show, attend and tell: Neural image caption generation with visual attention,” in
International conference on machine learning, pp. 2048–2057, 2015.
[41] A. Karpathy and L. Fei-Fei, “Deep visual-semantic alignments for generating image
descriptions,” in Proceedings of the IEEE conference on computer vision and pattern
recognition, pp. 3128–3137, 2015.
[42] L. A. Gatys, A. S. Ecker, M. Bethge, A. Hertzmann, and E. Shechtman, “Controlling
perceptual factors in neural style transfer,” in Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition, pp. 3985–3993, 2017.
[43] L. A. Gatys, A. S. Ecker, and M. Bethge, “Image style transfer using convolutional
neural networks,” in Proceedings of the IEEE conference on computer vision and pattern
recognition, pp. 2414–2423, 2016.
[44] A. Mordvintsev, C. Olah, and M. Tyka, “Inceptionism: Going deeper into neural net-
works,” 2015.
[45] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image
recognition,” arXiv preprint arXiv:1409.1556, 2014.
[46] M. D. Zeiler and R. Fergus, “Visualizing and understanding convolutional networks,”
in European conference on computer vision, pp. 818–833, Springer, 2014.
[47] A. L. Maas, A. Y. Hannun, and A. Y. Ng, “Rectifier nonlinearities improve neural
network acoustic models,”
[48] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,”
in Proceedings of the IEEE conference on computer vision and pattern recognition,
pp. 770–778, 2016.
[49] D.-A. Clevert, T. Unterthiner, and S. Hochreiter, “Fast and accurate deep network
learning by exponential linear units (elus),” arXiv preprint arXiv:1511.07289, 2015.
[50] I. J. Goodfellow, D. Warde-Farley, M. Mirza, A. Courville, and Y. Bengio, “Maxout
networks,” arXiv preprint arXiv:1302.4389, 2013.
[51] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectifiers: Surpassing human-
level performance on imagenet classification,” in Proceedings of the IEEE international
conference on computer vision, pp. 1026–1034, 2015.
[52] X. Glorot and Y. Bengio, “Understanding the difficulty of training deep feedforward
neural networks,” in Proceedings of the thirteenth international conference on artificial
intelligence and statistics, pp. 249–256, 2010.
[53] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by
reducing internal covariate shift,” arXiv preprint arXiv:1502.03167, 2015.
[54] Y. N. Dauphin, R. Pascanu, C. Gulcehre, K. Cho, S. Ganguli, and Y. Bengio, “Iden-
tifying and attacking the saddle point problem in high-dimensional non-convex opti-
mization,” in Advances in neural information processing systems, pp. 2933–2941, 2014.
[55] Y. Nesterov, “Introductory lectures on convex programming volume i: Basic course,”
1998.
[56] I. Sutskever, J. Martens, G. Dahl, and G. Hinton, “On the importance of initialization
and momentum in deep learning,” in International conference on machine learning,
pp. 1139–1147, 2013.
[57] J. Duchi, E. Hazan, and Y. Singer, “Adaptive subgradient methods for online learning
and stochastic optimization,” Journal of Machine Learning Research, vol. 12, no. Jul,
pp. 2121–2159, 2011.
[58] T. Tieleman and G. Hinton, “Lecture 6.5-rmsprop: Divide the gradient by a running
average of its recent magnitude,” COURSERA: Neural networks for machine learning,
vol. 4, no. 2, pp. 26–31, 2012.
[59] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” arXiv preprint
arXiv:1412.6980, 2014.
[60] D. C. Liu and J. Nocedal, “On the limited memory bfgs method for large scale opti-
mization,” Mathematical programming, vol. 45, no. 1-3, pp. 503–528, 1989.

##### BIBLIOGRAPHY 97

[61] B. T. Polyak and A. B. Juditsky, “Acceleration of stochastic approximation by averag-
ing,” SIAM Journal on Control and Optimization, vol. 30, no. 4, pp. 838–855, 1992.
[62] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout:
a simple way to prevent neural networks from overfitting,” The Journal of Machine
Learning Research, vol. 15, no. 1, pp. 1929–1958, 2014.
[63] J. Donahue, Y. Jia, O. Vinyals, J. Hoffman, N. Zhang, E. Tzeng, and T. Darrell, “Decaf:
A deep convolutional activation feature for generic visual recognition,” in International
conference on machine learning, pp. 647–655, 2014.
[64] A. Sharif Razavian, H. Azizpour, J. Sullivan, and S. Carlsson, “Cnn features off-the-
shelf: an astounding baseline for recognition,” in Proceedings of the IEEE conference
on computer vision and pattern recognition workshops, pp. 806–813, 2014.
[65] R. Girshick, “Fast r-cnn,” in Proceedings of the IEEE international conference on com-
puter vision, pp. 1440–1448, 2015.
[66] J. Johnson, “cnn-benchmarks.” https://github.com/jcjohnson/cnn-benchmarks.
[67] A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, A. Desmaison,
L. Antiga, and A. Lerer, “Automatic differentiation in pytorch,” 2017.
[68] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghe-
mawat, G. Irving, M. Isard, et al., “Tensorflow: A system for large-scale machine
learning,” in 12th {USENIX} Symposium on Operating Systems Design and Imple-
mentation ({OSDI} 16), pp. 265–283, 2016.
[69] T. Chen, M. Li, Y. Li, M. Lin, N. Wang, M. Wang, T. Xiao, B. Xu, C. Zhang, and
Z. Zhang, “Mxnet: A flexible and efficient machine learning library for heterogeneous
distributed systems,” arXiv preprint arXiv:1512.01274, 2015.
[70] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Van-
houcke, and A. Rabinovich, “Going deeper with convolutions,” in Proceedings of the
IEEE conference on computer vision and pattern recognition, pp. 1–9, 2015.
[71] M. Lin, Q. Chen, and S. Yan, “Network in network,” arXiv preprint arXiv:1312.4400,
2013.
[72] S. Zagoruyko and N. Komodakis, “Wide residual networks,” arXiv preprint
arXiv:1605.07146, 2016.
[73] S. Xie, R. Girshick, P. Doll ́ar, Z. Tu, and K. He, “Aggregated residual transformations
for deep neural networks,” in Proceedings of the IEEE conference on computer vision
and pattern recognition, pp. 1492–1500, 2017.
[74] G. Huang, Y. Sun, Z. Liu, D. Sedra, and K. Q. Weinberger, “Deep networks with
stochastic depth,” in European conference on computer vision, pp. 646–661, Springer,
2016.
[75] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, “Densely connected
convolutional networks,” in Proceedings of the IEEE conference on computer vision
and pattern recognition, pp. 4700–4708, 2017.
[76] G. Larsson, M. Maire, and G. Shakhnarovich, “Fractalnet: Ultra-deep neural networks
without residuals,” arXiv preprint arXiv:1605.07648, 2016.
[77] F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf, W. J. Dally, and K. Keutzer,
“Squeezenet: Alexnet-level accuracy with 50x fewer parameters and¡ 0.5 mb model
size,” arXiv preprint arXiv:1602.07360, 2016.
[78] Y. LeCun, L. Bottou, Y. Bengio, P. Haffner, et al., “Gradient-based learning applied to
document recognition,” Proceedings of the IEEE, vol. 86, no. 11, pp. 2278–2324, 1998.
[79] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang, A. Karpathy,
A. Khosla, M. Bernstein, et al., “Imagenet large scale visual recognition challenge,”
International journal of computer vision, vol. 115, no. 3, pp. 211–252, 2015.
[80] A. Canziani, A. Paszke, and E. Culurciello, “An analysis of deep neural network models
for practical applications,” arXiv preprint arXiv:1605.07678, 2016.
[81] K. He, X. Zhang, S. Ren, and J. Sun, “Identity mappings in deep residual networks,”
in European conference on computer vision, pp. 630–645, Springer, 2016.

##### 98 BIBLIOGRAPHY

[82] J. Ba, V. Mnih, and K. Kavukcuoglu, “Multiple object recognition with visual atten-
tion,” arXiv preprint arXiv:1412.7755, 2014.
[83] K. Gregor, I. Danihelka, A. Graves, D. J. Rezende, and D. Wierstra, “Draw: A recurrent
neural network for image generation,” arXiv preprint arXiv:1502.04623, 2015.
[84] A. Karpathy, “The unreasonable effectiveness of recurrent neural networks.” <http:>
//karpathy.github.io/2015/05/21/rnn-effectiveness/.
[85] J. Mao, W. Xu, Y. Yang, J. Wang, and A. L. Yuille, “Explain images with multimodal
recurrent neural networks,” arXiv preprint arXiv:1410.1090, 2014.
[86] O. Vinyals, A. Toshev, S. Bengio, and D. Erhan, “Show and tell: A neural image
caption generator,” in Proceedings of the IEEE conference on computer vision and
pattern recognition, pp. 3156–3164, 2015.
[87] J. Donahue, L. Anne Hendricks, S. Guadarrama, M. Rohrbach, S. Venugopalan,
K. Saenko, and T. Darrell, “Long-term recurrent convolutional networks for visual
recognition and description,” in Proceedings of the IEEE conference on computer vi-
sion and pattern recognition, pp. 2625–2634, 2015.
[88] X. Chen and C. L. Zitnick, “Learning a recurrent visual representation for image caption
generation,” arXiv preprint arXiv:1411.5654, 2014.
