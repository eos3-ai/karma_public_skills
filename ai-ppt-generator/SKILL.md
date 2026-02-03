---
name: ai-ppt-generator
description: 专业的 AI PPT 制作工具，基于 Gemini 3 Pro Image 模型生成高质量演示文稿。支持多风格设计方案预览、逐页智能生成、实时预览和 PDF 导出。工作流程：1)接收用户文案 2)生成三种设计风格样例供选择 3)批量生成 PPT 图片 4)整合导出为 PDF。触发词：调用AI PPT 当用户需要创建 PPT 演示文稿、根据文案生成幻灯片、或将内容转换为可视化演示时激活
license: MIT
compatibility: 需要 Gemini API 访问权限，支持 Python 3.8+ 环境，推荐使用 google-generativeai SDK 1.0+
metadata:
  homepage: "https://ai.google.dev/gemini-api"
  repository: 
  tags:
    - PPT
    - Gemini
    - 图像生成
    - PDF
    - 演示文稿
    - 设计
  language: Python
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
  - Glob
  - Grep
  - WebFetch
  - AskUserQuestion
---

# AI PPT 智能生成器

专业的 AI PPT 制作工具，基于 Gemini 3 Pro Image 模型生成高质量演示文稿。支持多风格设计方案预览、逐页智能生成、实时预览和 PDF 导出。工作流程：1)接收用户文案 2)生成三种设计风格样例供选择 3)批量生成 PPT 图片 4)整合导出为 PDF。触发词：调用AI PPT

## 使用场景

当用户需要创建 PPT 演示文稿、根据文案生成幻灯片、或将内容转换为可视化演示时激活

**触发关键词:** 调用AI PPT, AI PPT, 生成PPT, 制作演示文稿

**激活模式:**
- `(调用|创建|生成|制作).*(AI)?PPT`
- `PPT.*(生成|制作)`
- `演示文稿.*(生成|制作)`

## 使用说明

=== AI PPT 生成器技术参考 ===

[核心技术]

1. Gemini 3 Pro Image API
   - 模型标识: gemini-3.0-pro 或 gemini-3.0-pro-image
   - 主要功能: 根据文本提示生成高质量图像，支持复杂场景和多元素构图
   - API 调用方式: 使用 google-generativeai Python SDK
   - 生成配置: 支持自定义分辨率、风格参数、内容控制

2. 图像生成工作流
   步骤1: 内容分析
   - 解析用户文案，识别主题、关键信息、章节结构
   - 确定 PPT 总页数和每页核心内容
   
   步骤2: 风格设计
   - 生成三种设计方向：商务专业风格、创意视觉风格、简约现代风格
   - 为每种风格生成1页完整样例 PPT 图片
   - 样例提示词结构: '[风格描述] + [内容摘要] + [布局要求] + [视觉元素]'
   
   步骤3: 批量生成
   - 用户选定风格后，按页码顺序逐页生成
   - 每页提示词包含: 统一风格参数 + 页面序号 + 具体内容 + 布局规范
   - 建议生成分辨率: 1920x1080 (16:9) 或 1600x1200 (4:3)
   
   步骤4: PDF 整合
   - 使用 Pillow + ReportLab 或 img2pdf 库
   - 按页码排序图片文件
   - 统一尺寸和 DPI 设置
   - 生成 PDF 文档并保存

3. Gemini API 调用示例

   安装依赖:
   pip install google-generativeai pillow reportlab

   基本调用代码:
   import google.generativeai as genai
   genai.configure(api_key='YOUR_API_KEY')
   model = genai.GenerativeModel('gemini-3.0-pro')
   
   # 生成图像
   response = model.generate_content([
       '生成一页专业商务风格的 PPT 封面，主题：AI 技术应用报告，包含标题、副标题、装饰性图形元素，使用蓝色和白色配色方案'
   ])
   
   # 保存图像
   for part in response.parts:
       if hasattr(part, 'image'):
           with open('slide_01.png', 'wb') as f:
               f.write(part.image.data)

4. PDF 生成方法

   方法A: 使用 img2pdf (推荐)
   import img2pdf
   with open('output.pdf', 'wb') as f:
       f.write(img2pdf.convert(['slide_01.png', 'slide_02.png', ...]))
   
   方法B: 使用 ReportLab
   from reportlab.lib.pagesizes import A4, landscape
   from reportlab.pdfgen import canvas
   from PIL import Image
   
   c = canvas.Canvas('output.pdf', pagesize=landscape(A4))
   for img_path in image_list:
       img = Image.open(img_path)
       c.drawImage(img_path, 0, 0, width=..., height=...)
       c.showPage()
   c.save()

[设计风格方案模板]

方案A: 商务专业风格
- 配色: 深蓝 (#003366) + 白色 + 金色点缀
- 字体: 无衬线粗体标题 + 细体正文
- 布局: 左右分栏，重点信息突出
- 视觉元素: 几何图形、数据图表、简洁图标

方案B: 创意视觉风格
- 配色: 渐变色 (紫色到橙色) + 高对比度
- 字体: 现代艺术字体 + 动态排版
- 布局: 非对称构图，视觉焦点明确
- 视觉元素: 插画、抽象图形、创意图标

方案C: 简约现代风格
- 配色: 黑白灰 + 单一强调色 (#FF6B35)
- 字体: 极简无衬线字体，大字号标题
- 布局: 大量留白，中心对齐
- 视觉元素: 细线框、极简图标、高质量摄影图

[最佳实践]

1. 提示词工程技巧
   - 明确指定 'PPT slide' 或 'presentation slide' 关键词
   - 包含具体的视觉元素描述 (颜色、布局、字体风格)
   - 使用 '16:9 aspect ratio' 确保正确比例
   - 添加 'professional', 'clean', 'modern' 等质量描述词

2. 内容组织原则
   - 每页信息量适中 (标题 + 3-5 个要点)
   - 保持视觉层次清晰 (标题 > 副标题 > 正文)
   - 使用图表和图标增强可读性
   - 避免文字过多，优先使用视觉化表达

3. 性能优化
   - 批量生成时添加适当延迟 (避免 API 限流)
   - 使用异步调用提高效率
   - 缓存已生成的样例图片
   - 图片压缩优化 PDF 文件大小

4. 用户交互设计
   - 样例生成后立即展示缩略图
   - 提供风格对比预览功能
   - 支持单页重新生成
   - 导出前提供最终预览确认

[技术限制]

- Gemini API 调用频率限制: 根据配额管理请求频率
- 图像生成时间: 单页约 5-15 秒
- 图片质量: 依赖提示词质量，可能需要多次迭代
- 文字渲染: AI 生成的图片中文字可能存在拼写错误，建议提示词中明确文字内容
- PDF 文件大小: 高分辨率图片会导致较大文件，建议压缩

## 示例

### 基础示例：单主题 PPT 生成

**用户输入:**
```
undefined
```

### 高级示例：自定义风格 PPT

**用户输入:**
```
undefined
```

### Python 实现核心代码

**用户输入:**
```
undefined
```

## 资源文件

### 参考文档

- `resources/gemini-api-docs.md`: Google Gemini API 完整技术文档，包含图像生成、模型配置和最佳实践
- `resources/image-generation-guide.md`: AI 图像生成提示词工程和质量优化指南
- `resources/pdf-generation-python.md`: 使用 Python 将图片整合为 PDF 的多种方案
- `resources/ppt-design-principles.md`: 专业演示文稿设计的核心原则和视觉规范

### 脚本

- `undefined`: 配置 Python 环境并安装所需依赖
- `undefined`: AI PPT 生成器主程序

### 模板

- `undefined`: 商务专业风格提示词模板集合
- `undefined`: 创意视觉风格提示词模板集合
- `undefined`: 简约现代风格提示词模板集合

## 常见问题

**问: 如何获取 Gemini API Key？**

答: 访问 Google AI Studio (ai.google.dev) 并登录 Google 账号，在 API keys 页面创建新的 API key。免费层每分钟有请求限制，建议升级到付费计划以获得更高配额。

**问: 生成的图片中文字出现错误怎么办？**

答: AI 生成的图片中文字渲染可能不准确。解决方法：1) 在提示词中明确列出需要显示的文字内容，用引号包裹；2) 使用更详细的文字描述；3) 生成后使用图像编辑工具手动修正文字；4) 考虑生成纯视觉设计，后期添加文字图层。

**问: 如何保持多页 PPT 风格一致？**

答: 在批量生成时保持提示词的风格参数完全一致。建议：1) 创建风格描述模板并在所有页面复用；2) 明确指定配色方案的 HEX 色值；3) 使用相同的布局和字体描述；4) 在提示词中添加 'consistent with previous slides' 等描述。

**问: 生成速度太慢，如何优化？**

答: 优化策略：1) 使用异步并发调用 API（注意不要超过速率限制）；2) 降低图片分辨率（如使用 1280x720 代替 1920x1080）；3) 简化提示词，去除不必要的描述；4) 升级到更高配额的 API 计划；5) 考虑分批生成并缓存中间结果。

**问: PDF 文件太大怎么处理？**

答: 减小 PDF 文件大小的方法：1) 生成图片时使用适中的分辨率（1280x720 或 1600x900）；2) 使用图片压缩工具（如 Pillow 的 optimize 参数）；3) 在 img2pdf 转换时启用压缩选项；4) 使用 Ghostscript 等工具进一步压缩 PDF；5) 考虑降低 DPI 设置（72 或 96 DPI 适合屏幕显示）。

**问: 如何处理 API 调用限流错误？**

答: 应对限流的策略：1) 实现指数退避重试机制；2) 在请求之间添加延迟（建议 1-2 秒）；3) 监控 API 配额使用情况；4) 升级到更高的 API 计划；5) 使用队列系统管理批量请求；6) 缓存已生成的样例避免重复调用。

**问: 可以生成中文内容的 PPT 吗？**

答: 可以生成中文 PPT，但需注意：1) 提示词可以混合使用中英文，建议关键描述用英文以提高准确性；2) 中文文字渲染可能不完美，建议在提示词中明确指定需要显示的中文内容；3) 字体风格描述建议用英文（如 'Chinese sans-serif font'）；4) 生成后可能需要人工校对和修正中文文字。

**问: 如何添加公司 Logo 到 PPT？**

答: 添加 Logo 的方法：1) 在提示词中描述 Logo 的位置和风格（如 'company logo in top right corner'）；2) 生成基础设计后，使用 Pillow 等图像库将 Logo 图片叠加到每页上；3) 使用 ReportLab 在生成 PDF 时添加 Logo 水印；4) 在提示词中包含品牌色彩和视觉元素，让 AI 生成符合品牌风格的设计。

## 调试指南

[调试指南]

问题1: API 认证失败
症状: 'API key not valid' 错误
排查步骤:
1. 检查环境变量 GEMINI_API_KEY 是否正确设置
2. 确认 API key 在 Google AI Studio 中是否有效
3. 检查 API key 是否有足够的配额
4. 尝试在浏览器中直接访问 API 端点测试

问题2: 图片生成失败
症状: generate_content 返回空结果或无图片数据
排查步骤:
1. 检查提示词是否包含图像生成相关描述
2. 确认使用的模型是否支持图像生成（需要 gemini-3.0-pro 或 image 变体）
3. 查看 API 响应中的错误信息
4. 尝试简化提示词测试
5. 检查 API 配额是否耗尽

问题3: PDF 生成错误
症状: img2pdf 转换失败或 PDF 无法打开
排查步骤:
1. 确认所有图片文件存在且格式正确（PNG/JPEG）
2. 检查图片文件是否损坏（尝试手动打开）
3. 验证图片列表顺序是否正确
4. 尝试使用 Pillow 验证图片格式
5. 检查磁盘空间是否充足

问题4: 风格不一致
症状: 生成的多页 PPT 视觉风格差异大
排查步骤:
1. 检查每页提示词是否包含相同的风格描述
2. 确认配色方案在所有提示词中一致
3. 尝试在提示词中添加 'part of a series' 描述
4. 考虑减少提示词的变化部分，只修改内容描述
5. 使用更具体的风格参数（如精确的 HEX 色值）

问题5: 内存不足
症状: 批量生成时程序崩溃或变慢
排查步骤:
1. 减少并发请求数量
2. 在生成后及时释放图片对象
3. 降低图片分辨率
4. 分批处理大量页面
5. 监控系统内存使用情况

调试技巧:
- 启用详细日志记录（logging.DEBUG）
- 保存 API 响应以供分析
- 单独测试每个组件（生成、保存、转换）
- 使用小规模测试集验证流程
- 检查网络连接稳定性

---

## 元数据

| 字段 | 值 |
|------|----|
| 版本 | 1.0.0 |
| 作者 | Anonymous |
| 分类 | content-creation, productivity |
| 技能类型 | workflow, generation |

## 更新日志

- **v1.0.0** (2026-01-22): added - 初始版本发布，包含核心功能：风格样例生成、批量 PPT 生成、PDF 导出

