---
layout: page
title: Research Journey
permalink: /research-journey/
description: Interactive exploration of my research evolution, connections, and key contributions
nav: true
nav_order: 2
---

<div class="research-journey-page">
  <!-- Interactive Research Timeline -->
  {% include research_timeline.html %}
  
  <!-- Animated Research Connections -->
  {% include research_connections.html %}
  
  <!-- Research Bubbles Visualization -->
  {% include research_bubbles.html %}
  
  <!-- Ask Nick Chatbot -->
  {% include ask_nick_chatbot.html %}
</div>

<style>
.research-journey-page {
  margin-top: -20px;
}

.research-journey-page section {
  margin-bottom: 0;
}

/* Smooth transitions between sections */
.research-journey-page section:not(:last-child) {
  position: relative;
}

.research-journey-page section:not(:last-child)::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100px;
  background: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,0.05) 100%);
}

/* Section transitions */
.research-timeline-section {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.research-connections-section {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
}

.research-bubbles-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.chatbot-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .research-journey-page section {
    padding: 40px 0;
  }
}
</style>