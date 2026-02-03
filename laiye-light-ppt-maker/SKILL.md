---
name: laiye-light-ppt-maker
description: "专业的赖耶浅色风格 PPT 制作助手，遵循白色背景、青绿高亮色系统（#2ABAB7、#00DA90）、思源黑体+Montserrat 字体系统、线性图标风格、Punch 配色法则和苹果简约设计理念。调用 Gemini 3 pro Image 生成高质量 PPT 图片，支持企业 logo 嵌入，最终导出为 PDF 文件。使用触发词「调用赖耶浅色风格 PPT 助手」即可启动完整制作流程。 当用户需要创建符合赖耶视觉规范的专业 PPT 演示文稿时激活"
license: proprietary
compatibility: 需要 Gemini 3 pro Image API 访问权限，支持 Linux/macOS/Windows 环境，需要 Python 3.8+ 和图像处理库（Pillow）支持
metadata:
  homepage: "https://ai.google.dev/gemini-api/docs"
  repository: 
  tags:
    - PPT制作
    - 设计自动化
    - 企业演示
    - PDF导出
    - Gemini生图
  language: Python
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - WebFetch
  - WebSearch
  - AskUserQuestion
  - TodoWrite
---

# 赖耶浅色风格 PPT 制作助手

专业的赖耶浅色风格 PPT 制作助手，遵循白色背景、青绿高亮色系统（#2ABAB7、#00DA90）、思源黑体+Montserrat 字体系统、线性图标风格、Punch 配色法则和苹果简约设计理念。调用 Gemini 3 pro Image 生成高质量 PPT 图片，支持企业 logo 嵌入，最终导出为 PDF 文件。使用触发词「调用赖耶浅色风格 PPT 助手」即可启动完整制作流程。

## 使用场景

当用户需要创建符合赖耶视觉规范的专业 PPT 演示文稿时激活

**触发关键词:** 调用赖耶浅色风格 PPT 助手, 赖耶PPT, 制作PPT, 浅色风格PPT

**激活模式:**
- `调用.*赖耶.*PPT`
- `制作.*赖耶.*风格.*PPT`
- `生成.*浅色.*PPT`

## 使用说明

=== 赖耶浅色风格 PPT 制作技术参考 ===

[核心技术栈]
- Gemini 2.0 Flash Image API: 用于生成高质量 PPT 页面图片
- Pillow (PIL): Python 图像处理库，用于 logo 嵌入和图片处理
- ReportLab 或 img2pdf: 用于将图片序列转换为 PDF 文档

[视觉设计规范]
1. 色彩系统
   - 主背景色: #FFFFFF (白色)
   - 高亮色1: #2ABAB7 (青绿色)
   - 高亮色2: #00DA90 (荧光绿)
   - 遵循 Punch 配色法则: 主色占60%，辅助色30%，强调色10%

2. 字体系统
   - 中文字体: 思源黑体 (Source Han Sans)
   - 英文/数字字体: Montserrat
   - 标题建议使用 Bold 或 SemiBold 字重
   - 正文使用 Regular 字重

3. 图标规范
   - 风格: 线性图标 (Line Icons)
   - 线条粗细: 2-3px
   - 圆角: 适度圆角，保持现代感

4. 设计理念
   - 苹果简约设计: 留白充足，信息层级清晰
   - 视觉层级构建: 标题>副标题>正文>辅助信息
   - 信息架构: 每页聚焦单一主题，避免信息过载

[Gemini API 调用规范]
1. 模型选择: gemini-2.0-flash-exp (图像生成能力)
2. Prompt 构建原则:
   - 明确指定设计风格: '赖耶浅色风格，白色背景，青绿色(#2ABAB7)和荧光绿(#00DA90)高亮'
   - 描述字体系统: '使用思源黑体和Montserrat字体组合'
   - 图标要求: '线性风格图标，2-3px线条粗细'
   - 布局要求: '简约设计，充足留白，清晰视觉层级'
3. 图片参数:
   - 尺寸: 1920x1080 (16:9标准PPT比例)
   - 格式: PNG (支持透明背景)
   - 质量: 高清输出

[工作流程技术实现]
步骤1: 文案解析与方案生成
- 使用 NLP 技术分析用户文案主题和结构
- 基于内容自动生成 3 个设计方向的 Prompt
- 每个方向生成 1 页完整样例供用户选择

步骤2: 批量图片生成
- 根据选定方案，逐页调用 Gemini API
- 实现进度追踪和错误重试机制
- 生成的图片临时保存到工作目录

步骤3: Logo 嵌入处理
- 使用 Pillow 读取用户上传的 logo 图片
- 自动缩放 logo 至 PPT 宽度的 8-10%
- 定位到右上角，留出适当边距（如 40px）
- 处理透明背景和图层混合

步骤4: PDF 导出
- 按页码顺序整理所有图片文件
- 使用 img2pdf 或 ReportLab 库转换为 PDF
- 保持原始图片分辨率和质量
- 设置 PDF 元数据（标题、作者等）

[API 认证与配置]
- Gemini API Key 配置: 通过环境变量 GEMINI_API_KEY 设置
- API 调用限制: 注意 QPM (Queries Per Minute) 和 RPD (Requests Per Day) 限制
- 错误处理: 实现指数退避重试策略

[文件管理]
- 工作目录结构:
  /current_folder/
    ppt_images/          # 生成的 PPT 图片
      page_01.png
      page_02.png
      ...
    output/              # 最终输出
      final_presentation.pdf
    temp/                # 临时文件
      logo_resized.png

[质量控制]
1. 图片质量检查: 验证生成图片的分辨率和清晰度
2. 设计一致性: 确保所有页面遵循统一视觉风格
3. Logo 位置校验: 检查 logo 大小和位置的一致性
4. PDF 输出验证: 确认页面顺序和完整性

## 示例

### 完整 PPT 制作流程示例

**用户输入:**
```
undefined
```

### Gemini API 调用示例

**用户输入:**
```
undefined
```

### Logo 嵌入处理示例

**用户输入:**
```
undefined
```

### PDF 导出示例

**用户输入:**
```
undefined
```

## 资源文件

### 参考文档

- `resources/gemini-api-docs.md`: Google Gemini 2.0 Flash 图像生成 API 的完整技术文档，包含模型能力、API 调用方法、参数配置和最佳实践
- `resources/image-processing-guide.md`: 使用 Pillow 进行图像处理的技术指南，涵盖图像读取、缩放、合成和保存等操作
- `resources/pdf-generation.md`: 使用 Python 将图片序列转换为 PDF 文档的方法，包括 img2pdf 和 ReportLab 两种方案
- `resources/design-principles.md`: 赖耶浅色风格的完整设计规范，包括色彩理论、排版原则和视觉层级构建方法

### 脚本

- `undefined`: 环境配置脚本，安装所有必需的 Python 依赖
- `undefined`: 完整的 PPT 批量生成脚本，包含方案选择、图片生成、logo 嵌入和 PDF 导出

### 模板

- `undefined`: PPT 文案模板，指导用户如何组织 PPT 内容
- `undefined`: 设计需求模板，用于用户描述定制化设计要求

## 常见问题

**问: Gemini API 调用失败，提示 'API key not valid'**

答: 请检查以下内容：1) 确认已设置环境变量 GEMINI_API_KEY；2) 验证 API key 是否正确且未过期；3) 检查 API key 是否有图像生成权限；4) 尝试在浏览器中访问 Google AI Studio 确认账户状态。解决方法：重新生成 API key 或联系 Google Cloud 支持。

**问: 生成的 PPT 图片不符合赖耶浅色风格**

答: Gemini 生成结果可能存在随机性。改进方法：1) 在 prompt 中更详细地描述色彩要求，明确指定 HEX 色值；2) 多次生成并选择最佳结果；3) 使用温度参数（temperature）控制生成的一致性；4) 提供视觉参考图片作为输入；5) 如果多次尝试仍不理想，可考虑使用图像编辑工具进行后期调整。

**问: Logo 嵌入后图片质量下降或出现锯齿**

答: 图像质量问题通常由缩放算法引起。解决方法：1) 确保使用 Image.LANCZOS 或 Image.Resampling.LANCZOS 进行缩放；2) Logo 原图应使用高分辨率（建议至少 1000px 宽）；3) 使用 PNG 格式保存，避免 JPEG 压缩损失；4) 如果 logo 包含文字，考虑使用矢量格式（SVG）转换为高分辨率 PNG；5) 检查 Pillow 版本，建议使用最新版本。

**问: PDF 导出后文件过大，如何优化？**

答: PDF 文件大小主要取决于图片分辨率和压缩。优化方法：1) 在保存 PNG 时使用适当的压缩：image.save(path, 'PNG', optimize=True)；2) 考虑使用稍低的分辨率（如 1600x900 而非 1920x1080）；3) 使用 img2pdf 时指定 DPI 参数；4) 如果 PDF 仅用于屏幕演示，可使用 JPEG 格式（quality=85）替代 PNG；5) 使用 PDF 压缩工具如 Ghostscript 进行二次压缩。

**问: 批量生成 PPT 时遇到 API 限流（Rate Limit）**

答: Gemini API 有请求频率限制。解决方法：1) 在每次 API 调用之间添加延迟：time.sleep(2)；2) 实现指数退避重试策略；3) 使用 API 配额管理，监控使用情况；4) 对于大型 PPT（>20 页），分批处理；5) 考虑升级到付费计划以获得更高配额；6) 使用异步调用并控制并发数量。

**问: 在 macOS 上运行脚本时，Pillow 无法加载图片**

答: 这可能是 Pillow 依赖库的问题。解决方法：1) 重新安装 Pillow：pip uninstall Pillow && pip install Pillow；2) 安装系统级图像库：brew install libjpeg libpng；3) 确认图片文件路径正确且文件未损坏；4) 使用绝对路径而非相对路径；5) 检查文件权限：chmod 644 image.png。

**问: 如何确保所有 PPT 页面的视觉风格一致？**

答: 保持一致性的方法：1) 为所有页面使用相同的 base prompt 模板；2) 在 prompt 中明确引用前一页的风格；3) 使用固定的随机种子（如果 API 支持）；4) 生成样式参考图并在后续 prompt 中引用；5) 对于关键页面，使用图像编辑工具统一调整色调和对比度；6) 建立详细的风格指南文档，在每次生成时参考。

**问: 生成的 PPT 中文字不清晰或字体不正确**

答: 字体和清晰度问题的解决方法：1) 在 prompt 中明确强调字体要求：'必须使用思源黑体显示中文'；2) 提高生成分辨率以确保文字清晰；3) 如果 Gemini 无法正确渲染字体，考虑生成背景图后使用 Pillow 或 ReportLab 添加文字；4) 使用 OCR 检测生成图片的文字质量；5) 对于重要文字内容，可采用图文分离策略：背景由 AI 生成，文字后期叠加。

## 调试指南

[调试指南]

1. 启用详细日志
在脚本中添加日志记录：
import logging
logging.basicConfig(level=logging.DEBUG)

2. API 调用调试
打印完整的 API 请求和响应：
print(f'Prompt: {prompt}')
print(f'Response: {response}')

3. 图像处理调试
在每个处理步骤后保存中间结果：
image.save(f'debug_step_{step_number}.png')

4. 检查文件系统
验证所有必要的目录和文件存在：
for path in [ppt_images_dir, output_dir, logo_path]:
    assert path.exists(), f'路径不存在: {path}'

5. 测试单页生成
先测试生成单页 PPT，确认流程正常后再批量生成：
maker.generate_single_page(content, 'test_page.png')

6. 内存监控
对于大批量生成，监控内存使用：
import psutil
print(f'内存使用: {psutil.virtual_memory().percent}%')

7. 网络连接检查
确认可以访问 Gemini API：
import requests
response = requests.get('https://generativelanguage.googleapis.com')
print(f'API 连接状态: {response.status_code}')

8. 版本兼容性
检查所有依赖包的版本：
pip list | grep -E 'google-generativeai|Pillow|img2pdf'

如果问题仍未解决，请收集以下信息并寻求技术支持：
- 完整的错误堆栈跟踪
- Python 版本和操作系统信息
- 使用的 prompt 内容
- API 调用的响应数据（脱敏后）

---

## 元数据

| 字段 | 值 |
|------|----|
| 版本 | 1.0.0 |
| 作者 | Viveka |
| 分类 | content-creation, design, productivity |
| 技能类型 | workflow, creative |

## 更新日志

- **v1.0.0** (2026-01-22): added - 初始版本发布，支持完整的赖耶浅色风格 PPT 制作流程，包括方案生成、批量生图、logo 嵌入和 PDF 导出功能

