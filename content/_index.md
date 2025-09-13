---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '🧠 My Research'
      subtitle: ''
      text: |-
        I am focused on explainable deep learning, machine learning, and optimization theory research. As a research assistant at CUHK-Shenzhen Research Institute of Big Data, I am committed to applying chaos dynamics theory to financial forecasting and time series analysis.

        Current research focuses include: developing chaotic neural network architectures based on Lee oscillators, designing multifractal feature extraction algorithms, and constructing robust deep learning prediction models. My work has been submitted to several top-tier journals, including Chaos, Solitons & Fractals and IEEE TNNLS.

        Welcome academic exchanges and collaboration 😃
    design:
      columns: '1'
  - block: collection
    id: projects
    content:
      title: My Projects
      filters:
        folders:
          - project
    design:
      view: article-grid
      columns: 2
---