---
name: anime
description: 动漫制作项目初始化。用于创建新的动漫项目，设置风格、时长、比例等参数。当用户想要制作动漫、创建动漫视频、生成动画时使用此skill。
---

# 动漫生成 - 项目初始化

基于oiioii工作流程的自动化动漫制作工具。

## 触发条件

- 用户说 `/anime "主题"`
- 用户说 "做动漫"、"创建动漫"、"生成动画"
- 用户说 "anime project"

## 执行流程

### 1. 解析用户输入

从用户描述中提取：
- 主题/故事概念
- 时长要求（如有）
- 风格偏好（如有）

### 2. 引导参数选择

使用 AskUserQuestion 工具询问以下参数：

| 参数 | 选项 |
|------|------|
| 制作类型 | 故事短片 / 快速视频(<15s) / 音乐短片 |
| 影片长度 | 短视频(<1min) / 长视频(>=1min) |
| 影片比例 | 横版16:9 / 竖版9:16 |
| 对白语言 | 中文 / 英文 / 日文 |
| 情绪关键词 | 搞笑/慌乱/反转/尴尬/节奏 |
| 视觉风格 | 见下方风格库 |

### 3. 常用风格库

| 风格 | 英文关键词 | 适用场景 |
|------|------------|----------|
| 火柴人 | stick figure | 简约搞笑 |
| 彩铅素描 | colored pencil sketch | 文艺温馨 |
| 可爱马卡龙 | cute macaron pastel | 萌系可爱 |
| 美式喜剧 | American comedy cartoon | 搞笑夸张 |
| 蜡笔小新 | Crayon Shin-chan style | 童趣搞笑 |
| 日式动漫 | Japanese anime style | 通用动漫 |
| 像素风 | pixel art, 8-bit | 复古游戏 |
| 水彩风 | watercolor painting | 唯美意境 |
| 赛博朋克 | cyberpunk, neon | 科幻未来 |

### 4. 创建项目文件

在 `~/.claude/skills/anime/projects/{project-name}/` 目录下创建：

**project.md** 文件模板：
```markdown
# 动漫项目: {项目名}

## 元信息
- 创建时间: YYYY-MM-DD HH:MM
- 当前阶段: init
- 风格: {风格}
- 时长: {时长}秒
- 比例: {比例}
- 语言: {语言}
- 情绪: {情绪关键词}

## 剧本
### 故事梗概
[待生成]

### 角色列表
[待生成]

### 分镜概述
[待生成]

## 分镜列表
[待生成]

## 角色定妆
[待生成]

## 视频片段
[待生成]

## 最终输出
- BGM路径:
- 视频路径:
```

### 5. 输出项目摘要

```
项目创建成功！

名称：{项目名}
类型：{制作类型}
时长：{时长}秒
比例：{比例}
风格：{风格}
情绪：{情绪关键词}

项目文件：~/.claude/skills/anime/projects/{project-name}/project.md

下一步命令：
- /anime-script  → 生成剧本
- /anime-storyboard → 生成分镜
- /anime-character → 生成定妆图
- /anime-video → 生成视频
- /anime-merge → 合成最终视频
```

## 中断恢复

如果用户执行 `/anime` 不带参数，列出所有进行中的项目供选择。

## 相关命令

| 命令 | 功能 |
|------|------|
| /anime-script | 生成剧本 |
| /anime-storyboard | 生成分镜 |
| /anime-character | 生成定妆图 |
| /anime-video | 生成视频片段 |
| /anime-merge | 合成最终视频 |

## 详细Playbook

完整流程参考：`/knowledge/playbooks/anime.md`

## 关键词

动漫, 动画, anime, animation, 视频制作, 短视频, 故事短片, 分镜, 定妆图, 剧本
