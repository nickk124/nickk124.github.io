---
layout: page
permalink: /research/
title: Research Areas
description:
nav: true
nav_order: 2
---

My research topics of interest, past and present.

## Table of Contents

- [Intrinsic Dataset Properties/Statistics and Neural Network Generalization Ability](#intrinsic-dataset-propertiesstatistics-and-neural-network-generalization-ability)
- [Image Distribution Similarity Metrics and Generative Models](#image-distribution-similarity-metrics-and-generative-models)
- [Neural Network Interpretability and Explainability](#neural-network-interpretability-and-explainability)
- [Vision Foundation Models for Segmentation and Beyond](#vision-foundation-models-for-segmentation-and-beyond)
- [Domain Adaptation and Analysis](#domain-adaptation-and-analysis)
- [Misc. Breast Imaging Analysis](#misc-breast-imaging-analysis)
- [Anomaly Detection and Localization](#anomaly-detection-and-localization)

---

### Intrinsic Dataset Properties/Statistics and Neural Network Generalization Ability 

I study how geometric and statistical properties of datasets, such as intrinsic dimension and label complexity, influence neural network generalization across different imaging domains, particularly comparing natural and medical images.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[intrinsicproperties=true]* %}
</div>

---

### Image Distribution Similarity Metrics and Generative Models

I develop novel perceptual metrics and generative models for medical imaging, including controllable image generation methods and specialized distance measures that better capture anatomical features than traditional computer vision metrics.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[generativemodels=true]* %}
</div>

---

### Neural Network Interpretability and Explainability

I explore methods for understanding what neural networks learn and how concepts are formed, including data attribution techniques and representation analysis to improve model transparency and trustworthiness.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[interpretability=true]* %}
</div>

---

### Vision Foundation Models for Segmentation and Beyond

I investigate the capabilities and limitations of large-scale foundation models like SAM and SAM 2 for medical image analysis, developing enhanced architectures and evaluating their performance across diverse clinical tasks.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[foundationmodels=true]* %}
</div>

---

### Domain Adaptation and Analysis

I work on techniques for adapting models across different imaging domains, scanners, and acquisition parameters, addressing the challenge of domain shift that commonly affects medical AI systems in practice.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[domainadaptation=true]* %}
</div>

---

### Misc. Breast Imaging Analysis

I develop specialized methods for breast imaging applications, including lesion detection algorithms, registration techniques, and style transfer methods tailored to the unique challenges of breast MRI and tomosynthesis.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[breastimaging=true]* %}
</div>

---

### Anomaly Detection and Localization

I create unsupervised and self-supervised approaches for detecting abnormalities in medical images, with applications ranging from breast cancer screening to general outlier detection in high-resolution imaging data.

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[anomalydetection=true]* %}
</div>