---
name: government-document-assistant
description: "专业的政务文书撰写助手，严格遵循《党政机关公文处理工作条例》和《党政机关公文格式》国家标准（GB/T 9704-2012），支持心得体会、通知、讲话稿、工作报告、请示、工作方案等6种常用文书类型的撰写。提供标准公文格式、规范政务语言、完整写作指导，支持Word、PDF、Markdown多种格式输出。当用户说'写通知'、'起草讲话稿'、'写工作报告'、'撰写请示'、'制定工作方案'、'写心得体会'时触发。 当用户需要撰写符合党政机关公文规范的各类政务文书，包括通知、讲话稿、工作报告、请示、工作方案、心得体会等文件时触发"
license: MIT
compatibility: 适用于各级党政机关、事业单位、国有企业等需要撰写规范政务文书的场景。基于Python 3.9+环境，支持Linux、Windows、macOS操作系统。输出文档兼容Microsoft Word 2016+、Adobe Acrobat Reader、主流Markdown编辑器。
metadata:
  homepage:
  repository:
  tags:
    - 政务
    - 公文
    - 文书
    - 党政机关
    - 规范写作
  language: Python
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebSearch
---

# 政务文书助手

专业的政务文书撰写助手，严格遵循《党政机关公文处理工作条例》和《党政机关公文格式》国家标准（GB/T 9704-2012），支持心得体会、通知、讲话稿、工作报告、请示、工作方案等6种常用文书类型的撰写。提供标准公文格式、规范政务语言、完整写作指导，支持Word、PDF、Markdown多种格式输出。当用户说'写通知'、'起草讲话稿'、'写工作报告'、'撰写请示'、'制定工作方案'、'写心得体会'时触发。

## 使用场景

当用户需要撰写符合党政机关公文规范的各类政务文书，包括通知、讲话稿、工作报告、请示、工作方案、心得体会等文件时触发

## 使用说明

# 政务文书助手参考文档

## 资源文件

### 参考文档

- `resources/terminology-dictionary.md`: 资源: terminology-dictionary.md
- `resources/format-standards.md`: 资源: format-standards.md

### 脚本

- `scripts/generate_document.py`: 脚本: generate_document.py
- `scripts/export_formats.py`: 脚本: export_formats.py

### 模板

- `templates/notice.md`: 模板: notice.md
- `templates/speech.md`: 模板: speech.md
- `templates/report.md`: 模板: report.md
- `templates/request.md`: 模板: request.md
- `templates/plan.md`: 模板: plan.md
- `templates/reflection.md`: 模板: reflection.md

## 调试指南

# 调试指南

---

## 元数据

| 字段 | 值 |
|------|----|
| 版本 | 1.0.0 |
| 作者 |  |

## 更新日志

- **v1.0.0** (2026-01-26): added - 初始版本发布，支持6种常用政务文书类型的撰写，严格遵循GB/T 9704-2012国家标准

