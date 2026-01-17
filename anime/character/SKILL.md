---
name: anime-character
description: 动漫角色定妆图生成。基于角色描述生成图像提示词，调用Gemini CLI生成角色定妆图。需要先执行 /anime-storyboard 生成分镜。
---

# 动漫角色定妆图生成

为动漫项目生成角色定妆图（Character Design Sheet）。

## 触发条件

- 用户说 `/anime-character`
- 用户说 "生成定妆图"、"角色设计"

## 前置条件

分镜已通过 `/anime-storyboard` 生成。

## 执行流程

### 1. 读取角色列表

从 `project.md` 读取每个角色的：
- 名称
- 外观描述
- 性格特点
- 服装描述
- 项目风格

### 2. 生成图像提示词

为每个角色生成 Character Design Sheet 提示词：

**提示词模板**：
```
[Style: {风格英文}], CHARACTER DESIGN SHEET,
{角色名英文}, {年龄} years old {性别},
{外观描述英文},
{服装描述英文},
multiple views: front view, side view, 3/4 view,
multiple expressions: neutral, happy, surprised, {情绪相关表情},
white background, full body, high detail,
anime style, clean lines, professional character sheet
```

### 3. 风格关键词对照

| 中文风格 | 英文提示词 |
|----------|------------|
| 美式喜剧 | American comedy cartoon style |
| 日式动漫 | Japanese anime style |
| 蜡笔小新 | Crayon Shin-chan style |
| 火柴人 | stick figure, simple lines |
| 彩铅素描 | colored pencil sketch |
| 可爱马卡龙 | cute macaron pastel colors |
| 像素风 | pixel art, 8-bit style |
| 水彩风 | watercolor painting style |
| 赛博朋克 | cyberpunk, neon lights |

### 4. 调用 Gemini CLI

使用 gemini-cli skill 生成图像：

```bash
gemini -p "{提示词}" -o "{输出路径}"
```

输出路径：`~/.claude/skills/anime/projects/{project-name}/assets/characters/{角色名}.png`

### 5. 展示结果

为每个角色展示：
- 生成的提示词
- 生成的图像
- 用户可选择：
  - 确认使用
  - 重新生成（调整提示词）

### 6. 更新项目状态

将角色定妆信息写入 `project.md`：

```markdown
## 角色定妆

| 角色名 | 提示词 | 图片路径 | 状态 |
|--------|--------|----------|------|
| 阿杰 | [提示词] | assets/characters/ajie.png | done |
| 老板 | [提示词] | assets/characters/boss.png | done |
```

更新阶段为 `video`。

## 示例提示词

### 阿杰（美式喜剧风格）

```
[Style: American comedy cartoon], CHARACTER DESIGN SHEET,
Ah Jie, 25 years old male office worker,
slim build, slight dark circles under eyes, messy short black hair, wearing glasses,
wrinkled white button-up shirt, dark navy trousers, simple wristwatch, black leather shoes,
multiple views: front view, side view, 3/4 view,
multiple expressions: tired, intensely focused, shocked, embarrassed,
white background, full body, high detail,
cartoon style, clean lines, expressive face, professional character sheet
```

### 老板（美式喜剧风格）

```
[Style: American comedy cartoon], CHARACTER DESIGN SHEET,
The Boss, 50 years old male,
overweight with big beer belly, bald head, stern face, small eyes,
gray-blue suit jacket, white shirt, dark gray trousers, black leather shoes,
multiple views: front view, side view, 3/4 view,
multiple expressions: stern, surprised, secretly amused, smirking,
white background, full body, high detail,
cartoon style, clean lines, imposing presence, professional character sheet
```

## 定妆图要求

- **多角度**：正面、侧面、3/4侧面
- **多表情**：根据角色性格和剧情需要
- **服装细节**：清晰展示服装设计
- **配色说明**：标注关键颜色
- **比例一致**：所有角色比例统一

## 下一步

定妆图确认后，执行 `/anime-video` 生成分镜视频。

## 关键词

定妆图, character design, 角色设计, character sheet, Gemini
