---
name: anime-video
description: 动漫分镜视频生成。基于分镜列表和定妆图，调用Veo API生成每个镜头的视频片段。需要先执行 /anime-character 生成定妆图。
---

# 动漫分镜视频生成

为动漫项目的每个分镜生成视频片段，使用 Google Veo 3.1 API。

## 触发条件

- 用户说 `/anime-video`
- 用户说 "生成视频"、"分镜视频"

## 前置条件

定妆图已通过 `/anime-character` 生成。

## Veo API 配置

```
API_BASE: https://llm.tokencloud.ai
API_KEY: sk-RPo8Q8Lf9_SKoNMSjo5DNA
MODEL: google/veo-3.1-generate-preview
```

## 执行流程

### 1. 读取分镜列表

从 `project.md` 读取每个镜头的：
- 场景
- 画面描述
- 对白/音效
- 时长
- 镜头类型和运动

### 2. 生成视频提示词

为每个镜头生成英文提示词：

**提示词模板**：
```
[Style: {风格}], {场景描述},
{角色} {角色动作},
{光线/氛围}, {镜头角度},
camera: {镜头运动}
```

### 3. 调用 Veo API 生成视频

**Step 1: 发起生成请求**

```bash
curl -X POST 'https://llm.tokencloud.ai/videos' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-RPo8Q8Lf9_SKoNMSjo5DNA' \
  -d '{
    "model": "google/veo-3.1-generate-preview",
    "prompt": "{视频提示词}",
    "seconds": "{时长}"
  }'
```

**返回示例**：
```json
{
  "id": "video_xxx...",
  "status": "processing"
}
```

**Step 2: 轮询查询状态**

```bash
curl -X GET 'https://llm.tokencloud.ai/v1/videos/{video_id}' \
  -H 'x-litellm-api-key: sk-RPo8Q8Lf9_SKoNMSjo5DNA'
```

等待 `status` 变为 `completed`。

**Step 3: 下载视频**

```bash
curl -X GET 'https://llm.tokencloud.ai/v1/videos/{video_id}/content' \
  -H 'x-litellm-api-key: sk-RPo8Q8Lf9_SKoNMSjo5DNA' \
  -o '{输出路径}'
```

输出路径：`assets/videos/shot_{镜号}.mp4`

### 4. 视频生成脚本

为每个镜头执行以下脚本：

```bash
# 1. 发起生成请求
RESPONSE=$(curl -s -X POST 'https://llm.tokencloud.ai/videos' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-RPo8Q8Lf9_SKoNMSjo5DNA' \
  -d '{
    "model": "google/veo-3.1-generate-preview",
    "prompt": "'"${PROMPT}"'",
    "seconds": "'"${DURATION}"'"
  }')

# 2. 提取 video_id
VIDEO_ID=$(echo $RESPONSE | jq -r '.id')

# 3. 轮询等待完成
while true; do
  STATUS=$(curl -s -X GET "https://llm.tokencloud.ai/v1/videos/${VIDEO_ID}" \
    -H 'x-litellm-api-key: sk-RPo8Q8Lf9_SKoNMSjo5DNA' | jq -r '.status')

  if [ "$STATUS" = "completed" ]; then
    break
  fi
  echo "Status: $STATUS, waiting..."
  sleep 10
done

# 4. 下载视频
curl -X GET "https://llm.tokencloud.ai/v1/videos/${VIDEO_ID}/content" \
  -H 'x-litellm-api-key: sk-RPo8Q8Lf9_SKoNMSjo5DNA' \
  -o "${OUTPUT_PATH}"
```

### 5. 镜头运动关键词

| 中文 | 英文提示词 |
|------|------------|
| 固定 | static camera |
| 推进 | camera slowly zooms in |
| 拉远 | camera slowly zooms out |
| 左摇 | camera pans left |
| 右摇 | camera pans right |
| 跟随 | camera follows the character |

### 6. 风格关键词

| 中文风格 | 英文提示词 |
|----------|------------|
| 火柴人 | minimalist stick figure animation, simple black lines on white background |
| 美式喜剧 | American cartoon style, expressive animation |
| 日式动漫 | Japanese anime style, detailed animation |
| 蜡笔小新 | Crayon Shin-chan style animation |

### 7. 展示结果

为每个镜头展示：
- 生成的提示词
- 视频状态（processing/completed）
- 生成的视频预览
- 用户可选择：
  - 确认使用
  - 重新生成（调整提示词）
  - 跳过（稍后处理）

### 8. 更新项目状态

将视频片段信息写入 `project.md`：

```markdown
## 视频片段

| 镜号 | 提示词 | 视频路径 | 状态 |
|------|--------|----------|------|
| 1 | [提示词] | assets/videos/shot_01.mp4 | done |
| 2 | [提示词] | assets/videos/shot_02.mp4 | done |
| ... | ... | ... | ... |
```

更新阶段为 `merge`。

## 示例提示词（火柴人风格）

### 镜头1（小明疯狂敲键盘）

```
Minimalist stick figure animation, simple black lines on white background,
office cubicle scene, stick figure man sitting at desk typing frantically,
arms moving rapidly like blur motion lines, coffee cup vibrating on desk,
medium shot, static camera, comedic exaggerated typing animation
```

### 镜头3（贪吃蛇游戏屏幕）

```
Computer screen close-up, retro snake game interface,
very long snake filling most of the screen,
"NEW RECORD! 9999" text appearing with sparkle effects,
zoom in slowly on the score, pixel game aesthetic
```

### 镜头5（发现老板）

```
Minimalist stick figure animation, office scene,
thin stick figure slowly turning head with fear expression,
larger stick figure boss standing behind with arms crossed,
sweat drops appearing, dramatic lighting from behind boss,
medium shot transitioning to close-up on scared face
```

## 注意事项

1. **时长限制**：Veo API 仅支持 4、6、8 秒时长，5秒或7秒不支持，需要调整分镜时长为这些值
2. **轮询间隔**：建议 10-15 秒轮询一次状态
3. **超时处理**：如果 5 分钟未完成，提示用户检查
4. **风格一致**：所有镜头使用相同的风格前缀确保一致性

## 下一步

所有视频片段确认后，执行 `/anime-merge` 合成最终视频。

## 关键词

视频, video, Veo, Vertex AI, 分镜, animation
