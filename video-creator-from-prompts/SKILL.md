---
name: video-creator-from-prompts
description: "专业的视频批量创作工具，通过读取提示词文件自动调用Gemini API生成多个视频片段，并使用ffmpeg合成完整视频。支持项目初始化、提示词解析、批量视频生成、自动命名和视频合成等完整工作流。当用户说'批量生成视频'、'根据提示词创建视频'、'合成多个视频片段'、'AI视频制作'时触发。适用于自媒体内容创作、广告视频批量制作、教学视频生成等场景。 当用户需要根据提示词文件批量生成视频、使用AI生成多个视频片段并合成、或需要自动化视频创作工作流时激活"
license: MIT
compatibility: 需要Python 3.9+环境，必须安装ffmpeg工具。需要配置Gemini API密钥。支持Linux/macOS/Windows系统。生成的视频格式支持mp4、avi、mov等常见格式。
metadata:
  homepage: 
  repository: 
  tags:
    - 视频生成
    - AI创作
    - 批量处理
    - ffmpeg
    - Gemini
  language: python
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - WebFetch
---

# AI视频批量创作助手

专业的视频批量创作工具，通过读取提示词文件自动调用Gemini API生成多个视频片段，并使用ffmpeg合成完整视频。支持项目初始化、提示词解析、批量视频生成、自动命名和视频合成等完整工作流。当用户说'批量生成视频'、'根据提示词创建视频'、'合成多个视频片段'、'AI视频制作'时触发。适用于自媒体内容创作、广告视频批量制作、教学视频生成等场景。

## 使用场景

当用户需要根据提示词文件批量生成视频、使用AI生成多个视频片段并合成、或需要自动化视频创作工作流时激活

**触发关键词:** 批量生成视频, 根据提示词创建视频, AI视频制作, 合成视频片段, 视频批量创作, 提示词生成视频, ffmpeg合成视频

**激活模式:**
- `.*视频.*批量.*生成.*`
- `.*提示词.*视频.*`
- `.*合成.*视频.*`
- `.*ffmpeg.*视频.*`
- `.*Gemini.*视频.*`

## 使用说明

## 视频批量创作参考文档

### 功能概述
本技能实现了完整的视频批量创作工作流，包括项目初始化、提示词文件读取、调用Gemini API生成视频、自动命名和ffmpeg合成。

### 工作流程
1. 项目初始化：创建项目文件夹结构（prompts/、videos/、output/）
2. 读取提示词：从prompts.txt或prompts.yaml读取视频制作计划
3. 批量生成：按顺序调用Gemini API生成视频片段，命名为01.mp4、02.mp4等
4. 视频合成：使用ffmpeg将所有片段合成为最终视频

### Gemini API配置
需要在环境变量或配置文件中设置GEMINI_API_KEY。支持的Gemini模型包括gemini-3-pro-video和相关视频生成模型。

### ffmpeg合成参数
默认使用concat demuxer进行无损合成。可选参数包括：分辨率统一、帧率对齐、编码格式转换等。

### 文件命名规范
生成的视频片段按提示词顺序命名：01.mp4、02.mp4、03.mp4...，最终合成视频为final_video.mp4。

### 错误处理
API调用失败自动重试3次，超时时间60秒。视频生成失败会跳过该片段并记录日志。

### 性能优化
支持并行API调用（可配置并发数），支持断点续传（已生成的视频不会重复生成）。

## 示例

### 基础视频批量创作

**场景:** 自媒体创作者需要快速产出系列短视频内容

**用户输入:**
```
我有一个prompts.txt文件，里面有10个视频创意，帮我批量生成视频并合成
```

**预期输出:**
```
系统会：1) 初始化项目文件夹（video_project/）；2) 读取prompts.txt中的10个提示词；3) 依次调用Gemini API生成01.mp4到10.mp4；4) 使用ffmpeg合成为final_video.mp4；5) 输出合成视频路径和总时长
```

### 使用YAML配置文件创作

**场景:** 专业视频制作需要精细控制每个片段的参数

**用户输入:**
```
根据我的prompts.yaml配置生成视频，每个片段要不同时长和分辨率
```

**预期输出:**
```
系统会：1) 解析prompts.yaml中的详细配置（提示词、时长、分辨率）；2) 按配置调用Gemini API生成视频；3) 自动处理不同分辨率的视频统一化；4) 合成最终视频；5) 生成详细的制作报告
```

### 断点续传功能

**场景:** 网络中断或API限流导致任务中断后恢复

**用户输入:**
```
之前生成到第5个视频时中断了，继续完成剩余视频的生成
```

**预期输出:**
```
系统会：1) 检测已存在的01.mp4到05.mp4；2) 从第6个提示词开始继续生成；3) 生成完成后合成所有视频；4) 节省时间和API调用次数
```

### 添加转场效果合成

**场景:** 需要制作更专业的视频作品，提升观看体验

**用户输入:**
```
生成视频后，在每个片段之间添加1秒淡入淡出转场效果
```

**预期输出:**
```
系统会：1) 完成所有视频片段生成；2) 使用ffmpeg的xfade滤镜在片段间添加转场；3) 输出带转场效果的流畅视频；4) 可选择多种转场样式（淡入淡出、擦除、缩放等）
```

### 批量压缩优化

**场景:** 需要上传到平台或分享，对文件大小有限制

**用户输入:**
```
生成的视频文件太大，帮我压缩优化后再合成
```

**预期输出:**
```
系统会：1) 生成所有原始视频片段；2) 使用ffmpeg的CRF压缩算法优化每个片段；3) 在保持质量的前提下减少文件大小50-70%；4) 合成优化后的最终视频
```

## 资源文件

### 参考文档

- `resources/gemini-api-guide.md`: 详细的Gemini视频生成API使用说明和最佳实践
- `resources/ffmpeg-commands.md`: 常用的ffmpeg视频处理和合成命令
- `resources/prompt-format.md`: 提示词文件的编写规范和示例

### 脚本

- `scripts/generate_videos.py`: 核心脚本，实现项目初始化、提示词读取、Gemini API调用、视频生成和ffmpeg合成
  - 用法: 使用方式：python scripts/generate_videos.py prompts.txt
需要先设置环境变量 GEMINI_API_KEY
- `scripts/check_ffmpeg.sh`: 检查ffmpeg是否已安装并输出版本信息
  - 用法: 使用方式：bash scripts/check_ffmpeg.sh
- `scripts/compress_videos.py`: 批量压缩视频文件以减小文件大小
  - 用法: 使用方式：python scripts/compress_videos.py ./videos ./compressed

### 模板

- `templates/project_report.md`: 视频创作项目的完成报告模板
- `templates/prompts_template.yaml`: 标准的YAML格式提示词配置文件模板

## 常见问题

**问: Gemini API调用失败，返回401错误怎么办？**

答: 这是API密钥认证失败的问题。请检查：1) 确认已设置环境变量 GEMINI_API_KEY；2) 验证API密钥是否正确且未过期；3) 检查API密钥是否有视频生成权限。设置方法：export GEMINI_API_KEY='your_key_here'

**问: ffmpeg合成视频时报错'Invalid data found when processing input'怎么办？**

答: 这通常是视频文件损坏或格式不兼容导致的。解决方法：1) 检查所有生成的视频片段是否完整；2) 删除损坏的视频文件重新生成；3) 确保所有视频片段的编码格式一致；4) 尝试先转码再合成：ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4

**问: 视频生成速度很慢，如何提升效率？**

答: 可以尝试以下优化方法：1) 在config.json中增加max_concurrent参数值，启用并行生成（建议3-5）；2) 使用gemini-3-flash-video模型代替pro版本，速度更快；3) 减少单个视频的时长和分辨率；4) 启用断点续传功能，避免重复生成

**问: 合成的视频文件太大，如何压缩？**

答: 提供两种压缩方案：1) 使用compress_videos.py脚本批量压缩已生成的视频；2) 在config.json中设置auto_compress为true，生成时自动压缩；3) 调整compression_quality参数（18-28，越小质量越高文件越大，推荐23）；4) 降低输出分辨率或帧率

**问: 如何添加背景音乐或字幕？**

答: 这些功能需要在ffmpeg合成阶段实现：1) 添加背景音乐：ffmpeg -i video.mp4 -i music.mp3 -c:v copy -c:a aac -shortest output.mp4；2) 添加字幕：ffmpeg -i video.mp4 -vf subtitles=subtitle.srt output.mp4；3) 可以修改merge_videos函数添加这些功能，或使用专业视频编辑软件进行后期处理

**问: 提示词应该如何编写才能生成高质量视频？**

答: 优质提示词的关键要素：1) 具体描述主体对象（人物、动物、物品）；2) 明确动作和行为（在做什么）；3) 包含环境和场景信息（地点、时间、天气）；4) 描述光线和氛围（阳光、夜晚、温暖、冷色调）；5) 指定视觉风格（写实、动画、电影感）；6) 避免过于复杂的多主体场景；7) 保持单个提示词聚焦一个核心内容

## 调试指南

## 调试指南

### 日志查看
所有操作日志会输出到终端，建议使用重定向保存日志：
python scripts/generate_videos.py prompts.txt 2>&1 | tee log.txt

### 常见问题排查步骤

1. 检查环境依赖
   - 运行 bash scripts/check_ffmpeg.sh 检查ffmpeg
   - 检查Python版本：python --version（需要3.9+）
   - 检查依赖包：pip list | grep -E 'requests|yaml'

2. 验证API配置
   - 确认环境变量：echo $GEMINI_API_KEY
   - 测试API连接：curl -H 'Authorization: Bearer $GEMINI_API_KEY' API_ENDPOINT

3. 检查文件权限
   - 确保项目目录有写权限
   - 检查脚本可执行权限：chmod +x scripts/*.py

4. 逐步调试
   - 先测试单个视频生成
   - 验证提示词文件格式正确
   - 检查中间生成的视频文件是否完整
   - 单独测试ffmpeg合成命令

### 错误代码说明
- ERR_API_401: API认证失败
- ERR_API_TIMEOUT: API请求超时
- ERR_VIDEO_CORRUPT: 视频文件损坏
- ERR_FFMPEG_INVALID_DATA: ffmpeg处理数据错误
- ERR_FILE_NOT_FOUND: 文件未找到

### 获取详细错误信息
修改脚本中的日志级别，启用DEBUG模式查看详细信息

---

## 元数据

| 字段 | 值 |
|------|----|
| 版本 | 1.0.0 |
| 作者 | Ethan |
| 分类 | visual-creator, content-creator, automation |
| 技能类型 | creator, tool |
| 依赖项 | 运行时: python>=3.9, ffmpeg>=4.4; 包: requests, google-generativeai, pyyaml; 工具: ffmpeg |

## 更新日志

- **v1.0.0** (2026-01-27): added - 初始版本发布，支持项目初始化、提示词读取、Gemini API视频生成、ffmpeg合成等核心功能

