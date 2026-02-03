// HTML构建器
interface HTMLConfig {
  title: string;
  content: string;
  images: string[];
  platform: string;
  template?: string;
}

class HTMLBuilder {
  build(config: HTMLConfig): string {
    const template = this.getTemplate(config.template || config.platform);
    const styledContent = this.insertImages(config.content, config.images);
    
    return this.renderTemplate(template, {
      title: config.title,
      content: styledContent,
      meta: this.generateMeta(config)
    });
  }
  
  getTemplate(name: string): string {
    const templates = {
      'wechat': this.wechatTemplate(),
      'zhihu': this.zhihuTemplate(),
      'default': this.defaultTemplate()
    };
    return templates[name] || templates['default'];
  }
  
  wechatTemplate(): string {
    return `<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>{{title}}</title>
  <style>
    body { max-width: 800px; margin: 0 auto; padding: 20px; font-family: -apple-system, system-ui, sans-serif; }
    h1 { font-size: 24px; font-weight: bold; margin: 20px 0; }
    p { line-height: 1.8; font-size: 16px; margin: 15px 0; text-align: justify; }
    img { width: 100%; height: auto; margin: 20px 0; border-radius: 8px; }
    h2 { font-size: 20px; margin: 25px 0 15px; color: #333; }
  </style>
</head>
<body>
  <article>
    <h1>{{title}}</h1>
    <div>{{content}}</div>
  </article>
</body>
</html>`;
  }
  
  zhihuTemplate(): string {
    return `<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>{{title}}</title>
  <style>
    body { max-width: 720px; margin: 0 auto; padding: 40px 20px; font-family: -apple-system, system-ui, sans-serif; }
    h1 { font-size: 28px; font-weight: 600; margin: 30px 0; }
    p { line-height: 1.8; font-size: 17px; margin: 20px 0; color: #444; }
    img { width: 100%; height: auto; margin: 25px 0; }
    h2 { font-size: 22px; margin: 30px 0 20px; font-weight: 600; }
  </style>
</head>
<body>
  <article>
    <h1>{{title}}</h1>
    <div>{{content}}</div>
  </article>
</body>
</html>`;
  }
  
  defaultTemplate(): string {
    return this.wechatTemplate();
  }
  
  insertImages(content: string, images: string[]): string {
    // 智能插入图片到段落之间
    const paragraphs = content.split('\n\n');
    const imageInterval = Math.floor(paragraphs.length / (images.length + 1));
    
    let result = '';
    let imageIndex = 0;
    
    paragraphs.forEach((para, index) => {
      result += para + '\n\n';
      if ((index + 1) % imageInterval === 0 && imageIndex < images.length) {
        result += `<img src='${images[imageIndex]}' alt='配图${imageIndex + 1}'>\n\n`;
        imageIndex++;
      }
    });
    
    return result;
  }
  
  renderTemplate(template: string, data: any): string {
    return template
      .replace('{{title}}', data.title)
      .replace('{{content}}', data.content)
      .replace('{{meta}}', data.meta || '');
  }
  
  generateMeta(config: HTMLConfig): string {
    return `<meta name='description' content='${config.title}'>
<meta property='og:title' content='${config.title}'>
<meta property='og:type' content='article'>`;
  }
}

export default HTMLBuilder;