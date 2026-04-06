---
concept: Object Detection
tags: [object-detection, yolo, r-cnn, bounding-box, computer-vision]
sources:
  - kb/hard/raw/lilian-weng/object-detection-for-dummies-part-1-gradient-vector-hog-and-ss.md
  - kb/hard/raw/lilian-weng/object-detection-for-dummies-part-2-cnn-dpm-and-overfeat.md
  - kb/hard/raw/lilian-weng/object-detection-part-4-fast-detection-models.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/convolutional-neural-networks|Convolutional Neural Networks]]"
  - "[[hard/wiki/vision-language-models|Vision-Language Models]]"
---

# Object Detection

Object detection is the task of locating and classifying one or more objects in an image. It is strictly harder than image classification: a classifier need only assign a label to an image, while a detector must output both a class label and a bounding box (or pixel mask) for every instance it finds. This distinction shapes the entire design space of detection architectures.

## Classical Foundations

Before deep learning, detection relied on handcrafted features. The **Histogram of Oriented Gradients (HOG)** is the canonical example. HOG divides an image into 8x8 pixel cells, bins the gradient magnitudes into 9 orientation buckets, then aggregates over 2x2 cell blocks to form a normalized 36-value descriptor. Sliding a window of these descriptors across the image and feeding the concatenated vector into a linear SVM gave competitive pedestrian detection accuracy in the mid-2000s. HOG's key insight is that local gradient orientation distributions encode shape robustly against illumination change.

**Selective Search** sits one level up: instead of an exhaustive pixel-level sliding window, it proposes candidate regions by iteratively merging visually similar image segments (using Felzenszwalb's graph-based segmentation as initialization). The merge uses four complementary similarity measures—color, texture, size, and shape—so it generates a diverse set of region proposals at a fraction of the cost of scanning all windows. This proposal-then-classify structure became the template for the R-CNN family.

**Deformable Parts Model (DPM)** extended the HOG framework to handle articulated objects. DPM uses a coarse root filter for the whole object plus high-resolution part filters scored at twice the resolution, with a spatial deformation cost penalizing parts that stray from their canonical positions. The final score is the root match plus the sum of best-positioned part matches minus deformation penalties. DPM won PASCAL VOC detection for several years; interestingly, it can be reformulated as a CNN by unrolling the inference algorithm.

## The R-CNN Family: Two-Stage Detectors

The R-CNN family operationalized the proposal-then-classify pipeline in deep learning.

**R-CNN** (2014) ran Selective Search to generate ~2,000 region proposals, warped each to a fixed size, ran it through a CNN to extract a feature vector, and fed the features to per-class SVMs. The system was accurate but painfully slow — each proposal required a separate CNN forward pass.

**Fast R-CNN** fixed the computational bottleneck by running the CNN once on the full image to produce a shared convolutional feature map. A **RoI Pooling** layer extracted a fixed-size feature vector for each proposal directly from this shared map, enabling end-to-end training with a multi-task loss (classification + bounding-box regression) and cutting inference time dramatically.

**Faster R-CNN** closed the remaining bottleneck — the proposal stage — by replacing Selective Search with a **Region Proposal Network (RPN)** that slides over the shared feature map and simultaneously predicts objectness scores and bounding-box offsets for a set of predefined anchor boxes. Because the RPN reuses the same convolutional features, nearly all computation is shared between proposal and detection. Faster R-CNN set the standard two-stage paradigm: RPN generates sparse proposals, detection head classifies and refines them.

**Mask R-CNN** extended Faster R-CNN to instance segmentation by adding a parallel binary mask branch that predicts a per-pixel mask for each detected object. The key engineering change was replacing RoI Pooling with **RoI Align**, which uses bilinear interpolation to avoid quantization artifacts that degrade mask quality. Mask R-CNN is the go-to backbone for segmentation tasks.

## Anchor Boxes and NMS

Anchor boxes are predefined bounding boxes at multiple scales and aspect ratios tiled across the feature map. Every location predicts offsets relative to these priors rather than absolute coordinates. This parametrization makes regression easier and gives the network strong shape priors. The number and sizes of anchors are typically tuned to the target dataset; YOLOv2 uses k-means clustering on training box dimensions to set them empirically.

**Non-Maximum Suppression (NMS)** collapses the many overlapping detections produced by dense prediction into a clean set. The canonical algorithm: sort detections by confidence, greedily pick the highest-confidence box, suppress all remaining boxes with IoU above a threshold (typically 0.5), repeat. NMS is simple but fails when objects are densely packed; **Soft-NMS** decays rather than removes overlapping boxes and is more robust in crowded scenes.

## One-Stage Detectors: Speed vs. Accuracy

Two-stage detectors are accurate but slow. One-stage detectors skip the proposal step and densely predict over all candidate locations in a single forward pass.

**YOLO (You Only Look Once, v1)** divides the image into an S×S grid. Each cell predicts B bounding boxes (with confidence scores) and one set of class probabilities. The final prediction tensor is S×S×(5B+K) and is produced by two fully connected layers over the feature map. YOLO is fast — real-time on a GPU — but struggles with small objects and irregular shapes because each cell predicts only one class regardless of how many boxes it generates.

**YOLOv2 / YOLO9000** improved accuracy substantially: batch normalization on all conv layers, higher-resolution fine-tuning, anchor-box priors from k-means clustering, a passthrough layer for fine-grained features, and multi-scale training (random input size every 10 batches). YOLO9000 extended to 9,000 classes by training jointly on COCO and ImageNet using a WordTree hierarchical label structure that factors class probabilities along taxonomy paths.

**YOLOv3** added multi-scale prediction at three feature pyramid levels, replaced the softmax class head with independent logistic classifiers (handles multi-label), and adopted Darknet-53 (residual blocks in the backbone). Overall faster than SSD, slightly slower than RetinaNet, and more accurate than YOLOv2.

**SSD (Single Shot MultiBox Detector)** applies detection at multiple feature pyramid levels simultaneously. Built on VGG-16, SSD adds several convolutional layers of decreasing spatial size. Anchor boxes of different scales are tiled at each pyramid level so the detector is naturally multi-scale: fine-grained early layers detect small objects, coarse later layers detect large ones. SSD uses hard negative mining to keep the foreground/background ratio at 1:3.

**RetinaNet** introduced **Focal Loss** to address the fundamental class imbalance problem in one-stage detection. Standard cross-entropy gives equal weight to easy background examples, which dominate the loss and destabilize training. Focal loss downweights well-classified examples via a factor (1 − p_t)^γ, concentrating learning on hard, misclassified examples. RetinaNet pairs focal loss with a Feature Pyramid Network (FPN) backbone that merges bottom-up (feedforward) and top-down (semantically enriched) pathways via lateral connections, achieving accuracy competitive with two-stage detectors at one-stage speeds.

## Anchor-Free Detection

Anchor-based methods require careful anchor design and produce many redundant predictions. Anchor-free approaches (e.g., CornerNet, CenterNet, FCOS) instead detect objects via keypoints (corners, centers) or directly from feature map locations without predefined shapes. This simplifies the pipeline and reduces hyperparameter sensitivity, and has become increasingly common in modern architectures.

## Evaluation: mAP

The standard detection metric is **mean Average Precision (mAP)**. A detection is a true positive if its IoU with any unmatched ground-truth box exceeds a threshold (commonly 0.5, written mAP@0.5). For each class, a precision-recall curve is drawn over all detections on the test set; Average Precision (AP) is the area under this curve. mAP averages AP across all classes. COCO-style mAP averages over IoU thresholds from 0.5 to 0.95, giving a stricter measure of localization quality.

## Transformer-Based Detection

DETR (Detection Transformer, 2020) eliminated anchors and NMS entirely. It uses a CNN backbone to extract features, flattens them into a sequence for a Transformer encoder, then decodes a fixed set of object queries through a Transformer decoder with cross-attention to the encoder output. Each query predicts one object or a "no object" token; bipartite matching between predictions and ground truths during training removes the need for NMS. DETR is elegant but slow to converge on small objects; subsequent work (Deformable DETR, DINO) addresses these issues with sparse attention over deformable sampling points.

## Sources

- Weng, Lilian. "Object Detection for Dummies Part 1: Gradient Vector, HOG, and SS." 2017. https://lilianweng.github.io/posts/2017-10-29-object-recognition-part-1/
- Weng, Lilian. "Object Detection for Dummies Part 2: CNN, DPM and Overfeat." 2017. https://lilianweng.github.io/posts/2017-12-15-object-recognition-part-2/
- Weng, Lilian. "Object Detection Part 4: Fast Detection Models." 2018. https://lilianweng.github.io/posts/2018-12-27-object-recognition-part-4/
