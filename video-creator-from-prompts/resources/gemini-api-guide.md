# Gemini视频生成API指南

## API认证
在调用前需要设置环境变量：
export GEMINI_API_KEY='your_api_key_here'

## 支持的模型
- gemini-3-pro-video: 高质量视频生成
- gemini-3-flash-video: 快速视频生成

## 请求格式
POST https://generativelanguage.googleapis.com/v1/models/gemini-3-pro-video:generate

请求体：
{
  "prompt": "视频内容描述",
  "duration": 5,
  "resolution": "1920x1080",
  "fps": 30
}

## 响应格式
返回视频URL或base64编码的视频数据。

## 速率限制
每分钟最多20个请求，建议添加重试逻辑。

## 最佳实践
1. 提示词要具体明确，包含场景、动作、风格描述
2. 视频时长建议5-15秒
3. 分辨率建议1920x1080或1280x720
4. 使用异步请求提高效率