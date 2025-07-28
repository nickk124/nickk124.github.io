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

## Medical Image Generation & Translation

I work on developing generative models for medical imaging applications, with a focus on controllable image generation and cross-domain translation.

### Selected Recent Papers

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* --query @*[title~=*generation*]* --query @*[title~=*translation*]* --query @*[title~=*diffusion*]* --query @*[title~=*segmentation-guided*]* %}
</div>

---

## Foundational Deep Learning & Generalization

Research into how fundamental deep learning principles apply to specialized domains, particularly exploring intrinsic properties of datasets and their impact on model behavior.

### Selected Recent Papers

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* --query @*[title~=*intrinsic*]* --query @*[title~=*generalization*]* --query @*[title~=*properties*]* %}
</div>

---

## Evaluation Metrics & Model Assessment

Development of novel metrics and frameworks for evaluating deep learning models in medical imaging contexts.

### Selected Recent Papers

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* --query @*[title~=*metric*]* --query @*[title~=*distance*]* --query @*[title~=*FRD*]* --query @*[title~=*evaluation*]* %}
</div>

---

## Anomaly Detection & Medical Applications

Application-oriented work focusing on anomaly detection in medical images and specific clinical applications.

### Selected Recent Papers

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* --query @*[title~=*anomaly*]* --query @*[title~=*breast*]* --query @*[title~=*detection*]* --query @*[title~=*completion*]* %}
</div>

---

## All Selected Publications

<div class="publications">
{% bibliography -f {{ site.scholar.bibliography }} --query @*[selected=true]* %}
</div>