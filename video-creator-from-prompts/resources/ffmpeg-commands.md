# ffmpeg视频合成命令参考

## 基础合成命令
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4

## 文件列表格式（filelist.txt）
file '01.mp4'
file '02.mp4'
file '03.mp4'

## 转码合成（统一编码格式）
ffmpeg -f concat -safe 0 -i filelist.txt -c:v libx264 -c:a aac output.mp4

## 分辨率统一
ffmpeg -i input.mp4 -vf scale=1920:1080 output.mp4

## 帧率对齐
ffmpeg -i input.mp4 -r 30 output.mp4

## 添加转场效果
ffmpeg -i 01.mp4 -i 02.mp4 -filter_complex xfade=transition=fade:duration=1:offset=4 output.mp4

## 压缩视频
ffmpeg -i input.mp4 -crf 23 -preset medium output.mp4

## 批量处理脚本示例
for f in *.mp4; do
  ffmpeg -i "$f" -c:v libx264 -crf 20 "processed_$f"
done