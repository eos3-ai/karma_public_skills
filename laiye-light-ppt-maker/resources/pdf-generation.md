[方案1: img2pdf（推荐用于纯图片转PDF）]
import img2pdf
from pathlib import Path

# 获取所有 PPT 图片并排序
image_files = sorted(Path('ppt_images').glob('page_*.png'))
image_paths = [str(f) for f in image_files]

# 转换为 PDF
with open('output.pdf', 'wb') as f:
    f.write(img2pdf.convert(image_paths))

优点: 简单快速，保持原始图片质量，无需额外渲染

[方案2: ReportLab（适合需要额外处理的场景）]
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from PIL import Image

c = canvas.Canvas('output.pdf', pagesize=landscape(A4))
width, height = landscape(A4)

for img_path in image_paths:
    img = Image.open(img_path)
    # 保持宽高比缩放至页面大小
    c.drawImage(str(img_path), 0, 0, width=width, height=height, preserveAspectRatio=True)
    c.showPage()

c.save()

优点: 更多自定义选项，可添加元数据和交互元素

[PDF 元数据设置]
使用 PyPDF2 或 ReportLab 设置 PDF 属性:
- 标题: PPT 主题
- 作者: 用户名称或企业名称
- 主题: PPT 用途描述
- 创建日期: 自动生成时间戳