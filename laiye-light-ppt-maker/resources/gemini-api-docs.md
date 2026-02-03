[Gemini API 核心能力]
- 模型: gemini-2.0-flash-exp 支持图像生成
- 输入: 文本 prompt 描述所需图像内容和风格
- 输出: 高质量图像，支持多种分辨率
- 多模态能力: 可结合文本和图像输入

[API 调用示例]
使用 Python SDK:
import google.generativeai as genai
genai.configure(api_key='YOUR_API_KEY')
model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content(['生成一张赖耶浅色风格的PPT封面...'])

[Prompt 工程最佳实践]
1. 具体明确: 详细描述视觉元素、色彩、布局
2. 风格一致: 在所有 prompt 中保持统一的风格描述
3. 分辨率指定: 明确图像尺寸要求
4. 迭代优化: 根据输出结果调整 prompt

[限制与配额]
- 免费层: 每分钟 15 次请求
- 付费层: 根据订阅计划有不同配额
- 图像生成: 每次调用耗时约 3-10 秒

更多信息: https://ai.google.dev/gemini-api/docs/models/generative-models