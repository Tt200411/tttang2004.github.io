---
title: "交互式振荡器控制器"
summary: "一个用于实时控制和可视化振荡器参数的交互式工具，展示频率、振幅和相位对波形的影响。"
tags:
- 信号处理
- 可视化
- 交互式工具
- 机器学习
date: "2024-09-13T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "振荡器参数控制界面"
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: GitHub代码
  url: "#"
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

这是一个交互式的振荡器参数控制工具，专门为学习和研究信号处理、优化理论和机器学习中的周期性现象而设计。

## 功能特性

- **实时参数调节**：通过滑块实时调整频率(0.1-10 Hz)、振幅(0.5-5.0)和相位(0-2π)
- **即时可视化**：参数变化时立即更新波形图
- **响应式设计**：支持各种屏幕尺寸的设备
- **现代UI组件**：使用noUiSlider提供流畅的用户体验

## 技术实现

- **前端**：原生JavaScript + noUiSlider
- **后端API**：Python Flask + Matplotlib
- **部署**：支持GitHub Pages + Vercel Functions

## 应用场景

这个工具在以下领域具有应用价值：

- **信号处理教学**：帮助学生理解正弦波参数对波形的影响
- **优化理论研究**：可视化目标函数的周期性特征
- **深度学习**：理解周期性激活函数和循环神经网络
- **可解释性AI**：展示模型中周期性模式的可视化方法