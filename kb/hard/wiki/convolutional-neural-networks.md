---
concept: Convolutional Neural Networks
tags: [cnn, convolution, pooling, resnet, image-classification]
sources:
  - kb/hard/raw/aman-ai/cnns-for-visual-recognition.md
  - kb/hard/raw/aman-ai/coursera-dl-convolutional-neural-network.md
  - kb/hard/raw/aman-ai/primers-skip-connections.md
last_compiled: 2026-04-05
related: [neural-network-fundamentals, transfer-learning, vision-language-models]
---

# Convolutional Neural Networks

Convolutional Neural Networks (CNNs) are the foundational architecture for computer vision. Inspired by Hubel and Wiesel's 1959 discovery that the mammalian visual cortex processes visual input hierarchically — early neurons detect edges, deeper neurons detect complex objects — CNNs replicate this structure in silicon. The 2012 AlexNet breakthrough demonstrated CNNs so decisively outperforming all other image recognition approaches on ImageNet that it triggered the modern deep learning era.

## The Core Intuition

A CNN treats an image as a spatially organized tensor (`H × W × C`, where C is channels) and learns a hierarchy of features through stacked convolutional layers:

- **Early layers**: Detect low-level features (edges, corners, color gradients)
- **Middle layers**: Detect mid-level patterns (textures, shapes, object parts)
- **Deep layers**: Detect high-level semantic concepts (faces, wheels, buildings)

This mirrors the visual cortex pathway: simple cells → complex cells → object recognition.

## Convolution Operation

A convolutional layer applies a learned **filter** (kernel) across the spatial dimensions of the input. For a 2D grayscale case, the filter slides over the image and computes the dot product between filter weights and the image patch at each position. The output is a 2D **activation map** (or feature map).

**Output dimension formula**:
```
output = floor((N + 2P - F) / S) + 1
```
where N = input size, P = padding, F = filter size, S = stride.

**For volume (color images with C channels)**: The filter extends through all input channels — a 3×3 filter on an RGB image is actually 3×3×3 = 27 parameters (plus 1 bias). Multiple filters are applied in parallel, producing a volume with depth = number of filters.

**Two key advantages over fully connected layers**:

1. **Parameter sharing**: One filter is reused across all spatial positions. A vertical edge detector useful in the upper-left is equally useful in the lower-right. A 3×3×3 filter with 10 output channels has only 280 parameters vs. ~14M for a fully connected layer on the same spatial dimensions.

2. **Translation invariance**: The same feature is recognized regardless of where it appears in the image — because the filter scans the entire image.

## Padding and Stride

**Padding** adds zeros around the image boundary. Without padding (`valid` convolution), repeated operations shrink spatial dimensions and discard edge information. `same` padding preserves input dimensions by setting `p = (F-1)/2`. Odd filter sizes (3×3, 5×5, 7×7) are preferred because they allow symmetric padding with a well-defined center pixel.

**Stride** controls step size. Stride > 1 downsamples the spatial dimensions — useful for reducing resolution and computation in deeper layers without pooling. A stride-2 convolution roughly halves spatial dimensions.

## Pooling Layers

Pooling compresses spatial representations without learning parameters.

**Max pooling** takes the maximum value in each window (typically 2×2, stride 2). Intuition: if a feature detector fires anywhere in the region, the feature is present — its precise location is less important. Max pooling preserves the most prominent feature signal while discarding exact position.

**Average pooling** computes the mean. Less common for spatial downsampling; used in later network layers (global average pooling to collapse spatial dimensions before classification).

Pooling has no learnable parameters: filter size and stride are hyperparameters set by the designer.

## Standard CNN Architecture Pattern

A classic CNN alternates convolutional and pooling layers, then flattens to fully connected layers for classification:

```
Input [32×32×3]
→ Conv + ReLU [28×28×6]     (5×5 filters, 6 of them)
→ MaxPool     [14×14×6]     (2×2, stride 2)
→ Conv + ReLU [10×10×16]    (5×5 filters, 16 of them)
→ MaxPool     [5×5×16]      (2×2, stride 2)
→ Flatten     [400]
→ FC          [120]
→ FC          [84]
→ Softmax     [10 classes]
```

This is LeNet-5 (LeCun, 1998) — the template every architecture since has extended.

**Key pattern**: Spatial dimensions decrease; depth (number of channels/filters) increases as you go deeper.

## Canonical Architecture Evolution

### LeNet-5 (1998)
- Purpose: handwritten digit recognition
- Parameters: ~60K
- Novel: proved CNNs work end-to-end for vision

### AlexNet (2012) — The Watershed
- Input: 227×227×3
- 8 layers (5 conv + 3 FC), ~60M parameters, trained on 2 GPUs
- Introduced: **ReLU** activations (replacing sigmoid/tanh, solving vanishing gradients), **Dropout** regularization (0.5 in FC layers), **data augmentation**, **max pooling**, **Local Response Normalization**
- Won ImageNet 2012 with 16% top-5 error vs. 26% for the runner-up — a shock to the field

### VGGNet (2014)
- Key insight: depth + uniform 3×3 filters beats larger filters
- VGG-16 and VGG-19 (16 and 19 weight layers)
- Two stacked 3×3 convolutions have the same receptive field as one 5×5 convolution but with fewer parameters and more non-linearities
- ~138M parameters (mostly in FC layers) — large but very influential

### GoogLeNet / Inception (2014)
- Key insight: multi-scale processing within a layer via **Inception modules** (parallel 1×1, 3×3, 5×5 convolutions + max pooling, concatenated)
- **1×1 convolutions** for channel dimension reduction before expensive 3×3/5×5 convolutions (reduces compute significantly)
- Only 5M parameters — 20× fewer than AlexNet despite deeper network
- Replaced FC layers with global average pooling

### ResNet (2015) — The Skip Connection Revolution
- Key insight: very deep networks degrade even on training data due to **vanishing gradients** — adding layers hurts
- Solution: **residual connections** (skip connections): `H(x) = F(x) + x`
- The model learns the **residual** `F(x) = H(x) - x`, which is easier to optimize (learning identity = setting F(x) to zero)
- Mathematically, the gradient now has an additive identity path: `∂L/∂x = ∂L/∂H * (∂F/∂x + 1)` — the "+1" ensures gradient flows even if `∂F/∂x ≈ 0`
- ResNet-50, ResNet-101, ResNet-152 trained stably; first to surpass human-level ImageNet performance
- Batch normalization + skip connections are the two pillars enabling very deep training

### DenseNet (2017)
- Extends skip connections: each layer connects to **all subsequent layers** (concatenation, not addition)
- Dense connectivity enables extreme feature reuse, compact models, and strong gradient flow
- Tradeoff: feature dimension grows rapidly in later layers

### EfficientNet (2019)
- Key insight: simultaneously scaling width, depth, and resolution with a fixed ratio (compound scaling) is optimal
- NAS-discovered baseline architecture, then scaled via the compound coefficient
- EfficientNet-B7 achieves 84.4% top-1 on ImageNet at 66M parameters — significantly more efficient than equivalent-accuracy ResNets

## Skip Connections: The Deep Dive

Skip connections are the single most important architectural innovation since convolution itself. They address vanishing gradients — when backpropagation multiplies many terms < 1 together across layers, gradients shrink exponentially, making early layers unable to learn.

**ResNet-style (additive)**: `H(x) = F(x) + x`
- Requires matching dimensions; used for short connections within a block
- Loss landscape becomes smoother and more convex with skip connections (Li et al., 2017)
- Batch normalization complements: normalizes layer inputs, reducing internal covariate shift

**DenseNet-style (concatenative)**: Concatenates feature maps along the channel dimension
- Preserves all prior feature maps; more memory-intensive but maximizes feature reuse
- Natural for tasks needing fine-grained detail preservation

**Long skip connections (U-Net style)**: In encoder-decoder architectures, skip connections bridge encoder layers to their symmetric decoder layers
- Encoder compresses spatial information; decoder upsamples via transposed convolution
- Long skips recover spatial detail lost during downsampling
- Critical for dense prediction tasks: semantic segmentation, optical flow, medical image analysis
- Principle: global context from decoder resolves "what" is present; local detail from encoder resolves "where"

The LAUREL framework (2024) generalizes residual connections further: `x_{i+1} = α*f(x_i) + g(x_i, x_{i-1}, ..., x_0)` — learnable weights on both the transformed and identity paths, plus optional previous-activation terms. Achieves better accuracy than naively adding another layer.

## Receptive Field

The **receptive field** is the region of the input that influences a particular neuron. It grows with depth. Two stacked 3×3 conv layers have a 5×5 effective receptive field (each 3×3 convolution in layer 2 sees the output of a 3×3 region from layer 1). Three stacked 3×3 layers = 7×7 effective receptive field.

Deep networks build large receptive fields through local connections — a global context emerges from stacked local operations, without needing large (expensive) filters.

## Object Detection Extensions

CNNs serve as the backbone for object detection architectures:

- **R-CNN family**: Selective search → region proposals → per-region CNN features → classification. Faster R-CNN adds a Region Proposal Network (RPN) trained end-to-end.
- **YOLO**: Single-pass detection — divides image into grid cells, each predicts bounding boxes and class probabilities simultaneously. Much faster than two-stage methods.
- **Sliding window (convolutional)**: Instead of repeatedly passing sub-images through a FC classifier, reformulate FC layers as convolutions — the entire image is processed in one forward pass.

**IoU (Intersection over Union)**: Standard metric for bounding box quality. `IoU = area(A ∩ B) / area(A ∪ B)`. Threshold of 0.5+ typically considered a correct detection.

**Non-max suppression**: After detection, multiple overlapping boxes may fire for the same object. NMS suppresses all but the highest-confidence box when IoU with the best box exceeds a threshold.

## Transfer Learning

CNNs trained on ImageNet learn general visual features reusable across tasks. Standard practice:

1. Start from pretrained ImageNet weights (ResNet-50, EfficientNet-B4, etc.)
2. Remove final classification head
3. Either freeze all backbone layers (feature extraction) or fine-tune top layers + new head
4. Add domain-specific head and train

Transfer learning dramatically reduces data and compute requirements. Works especially well when target domain (medical images, satellite imagery) is visually distant from ImageNet — fine-tune more layers. Works with minimal fine-tuning when target domain is close.

## Sources

- Stanford CS231n notes via Aman Chadha, [CNNs for Visual Recognition](https://aman.ai/cs231n/test/)
- Aman Chadha, [Coursera DL: Convolutional Neural Networks](https://aman.ai/coursera-dl/convolutional-neural-networks/)
- Aman Chadha, [Primers: Skip Connections](https://aman.ai/primers/ai/skip-connections/)
