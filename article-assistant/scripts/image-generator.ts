// 图片生成器
interface ImageConfig {
  prompt: string;
  aspectRatio?: string;
  style?: string;
}

class ImageGenerator {
  private apiKey: string;
  private baseUrl = 'https://generativelanguage.googleapis.com/v1beta';
  
  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }
  
  async generate(config: ImageConfig): Promise<string> {
    // 构建请求
    const prompt = this.enhancePrompt(config.prompt, config.style);
    
    const response = await fetch(`${this.baseUrl}/models/gemini-2.0-flash-image-exp:generateContent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-goog-api-key': this.apiKey
      },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: {
          responseModalities: ['image'],
          aspectRatio: config.aspectRatio || '16:9'
        }
      })
    });
    
    const data = await response.json();
    return this.extractImageUrl(data);
  }
  
  enhancePrompt(prompt: string, style?: string): string {
    const stylePrefix = style ? `${style} style, ` : '';
    return `${stylePrefix}${prompt}, high quality, professional, clean composition`;
  }
  
  extractImageUrl(response: any): string {
    // 从API响应中提取图片URL或base64
    return response.candidates[0].content.parts[0].inlineData.data;
  }
  
  async generateBatch(prompts: string[], config: Partial<ImageConfig>): Promise<string[]> {
    // 批量生成图片
    return Promise.all(prompts.map(prompt => this.generate({ ...config, prompt })));
  }
}

export default ImageGenerator;