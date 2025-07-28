---
layout: page
permalink: /research/
title: Research Areas
description:
nav: true
nav_order: 2
---

My research topics of interest, past and present.

## Topic List
- [Topic List](#topic-list)
  - [Intrinsic Properties and Statistics of Training Data and their Effects on Neural Network Generalization Ability](#intrinsic-properties-and-statistics-of-training-data-and-their-effects-on-neural-network-generalization-ability)
  - [Image Distribution Similarity Metrics and Generative Models](#image-distribution-similarity-metrics-and-generative-models)
  - [Vision Foundation Models for Segmentation and Beyond](#vision-foundation-models-for-segmentation-and-beyond)
  - [Neural Network Interpretability and Explainability](#neural-network-interpretability-and-explainability)
  - [Domain Adaptation and Analysis](#domain-adaptation-and-analysis)
  - [Anomaly Detection and Localization](#anomaly-detection-and-localization)
  - [Misc. Breast Imaging Analysis](#misc-breast-imaging-analysis)

---

### Intrinsic Properties and Statistics of Training Data and their Effects on Neural Network Generalization Ability

Research exploring how geometric and statistical properties of datasets, such as intrinsic dimension and label sharpness, influence neural network generalization across different imaging domains, particularly in how these differ betweeen natural and medical image models.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[intrinsicproperties=true]* %}
</div>

---

### Image Distribution Similarity Metrics and Generative Models

Development of novel perceptual metrics and generative models for medical imaging, including controllable image generation methods and specialized distance measures that better capture anatomical features than traditional computer vision metrics.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[generativemodels=true]* %}
</div>

---

### Vision Foundation Models for Segmentation and Beyond

Investigation of the capabilities and limitations of large-scale foundation models for medical image analysis, including enhanced architectures and performance evaluation across diverse downstream tasks.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[foundationmodels=true]* %}
</div>

---

### Neural Network Interpretability and Explainability

Methods for understanding what neural networks learn and how concepts are formed, including data attribution techniques and representation analysis to improve model transparency and trustworthiness, and others.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[interpretability=true]* %}
</div>

---

### Domain Adaptation and Analysis

Techniques for adapting models across different imaging domains, scanners, and acquisition parameters, addressing the challenge of domain shift that commonly affects medical AI systems in practice, as well as understanding the nature of the domain shift problem itself.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[domainadaptation=true]* %}
</div>

---

### Anomaly Detection and Localization

Unsupervised and self-supervised approaches for detecting abnormalities in medical images, with applications ranging from breast cancer screening to general outlier detection in high-resolution imaging data.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[anomalydetection=true]* %}
</div>

### Misc. Breast Imaging Analysis

Specialized methods for breast imaging applications, including lesion detection algorithms, registration techniques, and style transfer methods tailored to the unique challenges of breast MRI and tomosynthesis.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[breastimaging=true]* %}
</div>

---