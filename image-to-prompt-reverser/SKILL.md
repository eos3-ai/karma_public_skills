---
name: image-to-prompt-reverser
description: 专业的图片反向工程工具，通过Gemini 3 pro分析用户上传或已生成的图片，提取详细的视觉信息并生成结构化的中英文对照JSON数据。包含图片尺寸、构图、主体描述、风格、色彩、光影等完整元数据，方便后续图片调整和再创作。使用触发词「分析图片提示词」或「反向提取图片信息」启动完整分析流程 当用户需要理解图片构成细节、提取AI绘画提示词、或将图片转换为结构化描述时激活 (user) 当用户需要从图片中提取详细描述信息、将图片转换为结构化JSON数据以便后续编辑时激活
license: MIT
compatibility: "支持主流图片格式(PNG/JPG/WEBP等),需要多模态视觉理解能力的AI模型(如Claude Sonnet 4.5/GPT-4V/Gemini 2.0 Flash等),适用于AI绘画、内容创作、图片管理等场景"
metadata:
  homepage:
  repository:
  tags:
    - 图像分析
    - 提示词工程
    - 反向工程
    - 多模态AI
    - 结构化输出
    - JSON生成
  language: JavaScript/Python
allowed-tools:
  - Read
  - Write
  - Bash
  - WebFetch
  - AskUserQuestion
---

# 图片反向提示词生成器

专业的图片反向工程工具，通过Gemini 3 pro分析用户上传或已生成的图片，提取详细的视觉信息并生成结构化的中英文对照JSON数据。包含图片尺寸、构图、主体描述、风格、色彩、光影等完整元数据，方便后续图片调整和再创作。使用触发词「分析图片提示词」或「反向提取图片信息」启动完整分析流程 当用户需要理解图片构成细节、提取AI绘画提示词、或将图片转换为结构化描述时激活 (user)

## 使用场景

当用户需要从图片中提取详细描述信息、将图片转换为结构化JSON数据以便后续编辑时激活

## 使用说明

=== 图片反向提示词生成技术参考 ===

## 资源文件

### 参考文档

- `resources/multimodal-vision-apis.md`: 资源: multimodal-vision-apis.md
- `resources/prompt-engineering-for-vision.md`: 资源: prompt-engineering-for-vision.md
- `resources/image-metadata-standards.md`: 资源: image-metadata-standards.md
- `resources/color-theory-analysis.md`: 资源: color-theory-analysis.md

### 脚本

- `scripts/analyze-image-to-json.py`: 脚本: analyze-image-to-json.py
- `scripts/batch-analyze.py`: 脚本: batch-analyze.py

### 模板

- `templates/image-analysis-template.json`: 模板: image-analysis-template.json
- `templates/ai-prompt-extraction-template.json`: 模板: ai-prompt-extraction-template.json

## 调试指南

=== 调试指南 ===

---

## 元数据

| 字段 | 值 |
|------|----|
| 版本 | 1.0.0 |
| 作者 |  |

## 更新日志

- **v1.0.0** (2026-01-21): added - 初始版本发布,支持单图和批量图片分析,输出中英文对照JSON,提取AI绘画提示词

