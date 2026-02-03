[Pillow 核心功能]
1. 图像加载: Image.open('path/to/image.png')
2. 图像缩放: image.resize((new_width, new_height), Image.LANCZOS)
3. 图像合成: background.paste(logo, (x, y), logo) # 支持透明度
4. 图像保存: image.save('output.png', 'PNG', quality=95)

[Logo 嵌入技术]
# 1. 加载背景和 logo
background = Image.open('ppt_page.png')
logo = Image.open('company_logo.png')

# 2. 计算 logo 目标尺寸（PPT 宽度的 8-10%）
target_width = int(background.width * 0.09)
aspect_ratio = logo.height / logo.width
target_height = int(target_width * aspect_ratio)

# 3. 缩放 logo
logo_resized = logo.resize((target_width, target_height), Image.LANCZOS)

# 4. 计算右上角位置（留 40px 边距）
x = background.width - target_width - 40
y = 40

# 5. 粘贴 logo（保持透明度）
background.paste(logo_resized, (x, y), logo_resized)
background.save('final_page.png', 'PNG')

[图像质量优化]
- 使用 LANCZOS 插值算法进行高质量缩放
- PNG 格式保持透明度和无损质量
- 避免多次缩放导致的质量损失