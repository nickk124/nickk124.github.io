---
layout: page
permalink: /research/
title: Research
description: My research areas and contributions in machine learning for medical imaging and foundational deep learning
nav: true
nav_order: 2
---

My research focuses on deep learning for medical image analysis on a spectrum from application-oriented to foundational work, with an emphasis on topics like generative models, domain adaptation, and image-to-image translation. I am particularly interested in how foundational deep learning concepts behave in medical image analysis and other secondary computer vision domains.

---

## Research Areas

My work spans several interconnected areas in machine learning for medical imaging:

### Medical Image Generation & Translation
- Anatomically-controllable image generation using diffusion models
- Cross-domain medical image translation and evaluation metrics
- Segmentation-guided generative models

### Foundational Deep Learning & Generalization  
- Intrinsic properties of medical vs. natural image datasets
- Generalization scaling laws and representation learning
- Domain adaptation challenges in specialized imaging domains

### Evaluation Metrics & Model Assessment
- Novel perceptual metrics for medical image evaluation (e.g., Fréchet Radiomic Distance)
- Framework development for assessing generative models
- Correlation studies between metrics and downstream task performance

### Anomaly Detection & Medical Applications
- Unsupervised anomaly localization in medical images
- Pluralistic image completion for anomaly detection
- Clinical applications in breast imaging and other domains

---

## Selected Publications

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* %}
</div>