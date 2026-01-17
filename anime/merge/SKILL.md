---
name: anime-merge
description: 动漫视频合成。将所有分镜视频片段合并，添加BGM和字幕，导出最终视频。需要先执行 /anime-video 生成视频片段。
---

# 动漫视频合成

合并所有分镜视频，生成最终动漫视频。

## 触发条件

- 用户说 `/anime-merge`
- 用户说 "合成视频"、"导出视频"

## 前置条件

视频片段已通过 `/anime-video` 生成。

## 执行流程

### 1. 检查素材完整性

从 `project.md` 读取并验证：
- 所有视频片段是否存在
- BGM是否已生成
- 是否有对白需要字幕

### 2. 创建视频列表文件

```bash
# 在项目目录下创建 videos.txt
echo "file 'assets/videos/shot_01.mp4'" > videos.txt
echo "file 'assets/videos/shot_02.mp4'" >> videos.txt
echo "file 'assets/videos/shot_03.mp4'" >> videos.txt
# ... 所有镜头
```

### 3. 合并视频片段

使用 FFmpeg 拼接视频：

```bash
ffmpeg -f concat -safe 0 -i videos.txt -c copy merged.mp4
```

### 4. 添加背景音乐

```bash
ffmpeg -i merged.mp4 -i assets/audio/bgm.mp3 \
  -c:v copy -c:a aac \
  -map 0:v:0 -map 1:a:0 \
  -shortest \
  with_bgm.mp4
```

### 5. 添加字幕（如有对白）

**字幕文件格式** (`subtitles.srt`)：
```
1
00:00:25,000 --> 00:00:30,000
"这种节奏感..."
```

**添加字幕命令**：
```bash
ffmpeg -i with_bgm.mp4 \
  -vf "subtitles=subtitles.srt:force_style='FontSize=24,FontName=Microsoft YaHei'" \
  -c:a copy \
  final.mp4
```

### 6. 导出设置

**推荐导出参数**：

| 参数 | 竖版9:16 | 横版16:9 |
|------|----------|----------|
| 分辨率 | 1080x1920 | 1920x1080 |
| 帧率 | 24fps | 24fps |
| 编码 | H.264 | H.264 |
| 音频 | AAC 128kbps | AAC 128kbps |

**高质量导出**：
```bash
ffmpeg -i final.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  output/{project-name}_final.mp4
```

### 7. 质量检查

- [ ] 所有镜头按顺序拼接
- [ ] 镜头间过渡自然
- [ ] BGM节奏与画面匹配
- [ ] 字幕清晰可读
- [ ] 导出格式正确
- [ ] 文件大小合理

### 8. 更新项目状态

```markdown
## 最终输出
- BGM路径: assets/audio/bgm.mp3
- 视频路径: output/{project-name}_final.mp4
- 导出时间: YYYY-MM-DD HH:MM
- 文件大小: XX MB
- 时长: XX秒
```

更新阶段为 `done`。

## FFmpeg 常用命令参考

### 裁剪视频
```bash
ffmpeg -i input.mp4 -ss 00:00:00 -t 00:00:05 -c copy output.mp4
```

### 调整速度
```bash
# 2倍速
ffmpeg -i input.mp4 -filter:v "setpts=0.5*PTS" -filter:a "atempo=2.0" output.mp4
```

### 添加淡入淡出
```bash
ffmpeg -i input.mp4 -vf "fade=t=in:st=0:d=1,fade=t=out:st=4:d=1" output.mp4
```

### 调整音量
```bash
ffmpeg -i input.mp4 -filter:a "volume=0.8" output.mp4
```

### 添加水印
```bash
ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=10:10" output.mp4
```

## 输出路径

最终视频保存在：
`~/.claude/skills/anime/projects/{project-name}/output/{project-name}_final.mp4`

## 完成提示

```
视频合成完成！

项目：{项目名}
时长：{时长}秒
格式：{比例}
文件：{输出路径}
大小：{文件大小}

恭喜完成动漫制作！
```

## 关键词

合成, merge, 导出, export, FFmpeg, 视频编辑
