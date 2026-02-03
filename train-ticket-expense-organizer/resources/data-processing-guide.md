数据处理与统计指南

[使用pandas进行数据处理]
import pandas as pd
from datetime import datetime

[创建DataFrame]
df = pd.DataFrame(ticket_records)
df.columns = ['购买方名称', '出发日期', '出发站点', '到达站点', '票价', '乘车人姓名', '开票日期', '发票号码']

[日期格式转换]
df['出发日期'] = pd.to_datetime(df['出发日期'])
df['开票日期'] = pd.to_datetime(df['开票日期'])

[排序操作]
df_sorted = df.sort_values(by=['购买方名称', '出发日期'], ascending=[True, True])

[提取月份]
df_sorted['月份'] = df_sorted['出发日期'].dt.to_period('M')

[按月份统计]
monthly_summary = df_sorted.groupby(['月份', '购买方名称']).agg({
    '票价': ['sum', 'count']
}).reset_index()
monthly_summary.columns = ['月份', '购买方名称', '报销总额', '票据数量']

[格式化金额]
df_sorted['票价'] = df_sorted['票价'].apply(lambda x: round(float(x), 2))
monthly_summary['报销总额'] = monthly_summary['报销总额'].apply(lambda x: round(float(x), 2))

[导出到Excel]
with pd.ExcelWriter('火车票费用报销台账.xlsx', engine='openpyxl') as writer:
    df_sorted.to_excel(writer, sheet_name='明细表', index=False)
    monthly_summary.to_excel(writer, sheet_name='汇总表', index=False)