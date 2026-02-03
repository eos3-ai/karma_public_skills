Excel台账生成API参考

[核心库:openpyxl]
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter

[创建工作簿]
wb = openpyxl.Workbook()
ws_detail = wb.active
ws_detail.title = '明细表'
ws_summary = wb.create_sheet('汇总表')

[写入表头]
headers_detail = ['购买方名称', '出发日期', '出发站点', '到达站点', '票价(元)', '乘车人姓名', '开票日期', '发票号码']
ws_detail.append(headers_detail)

[格式化表头]
header_font = Font(bold=True, size=11)
header_fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
for cell in ws_detail[1]:
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center', vertical='center')

[写入数据行]
for record in ticket_records:
    ws_detail.append([record['buyer'], record['date'], record['from'], record['to'], record['price'], record['passenger'], record['invoice_date'], record['invoice_no']])

[列宽自适应]
for column in ws_detail.columns:
    max_length = 0
    column_letter = get_column_letter(column[0].column)
    for cell in column:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    ws_detail.column_dimensions[column_letter].width = max_length + 2

[保存文件]
wb.save('火车票费用报销台账.xlsx')