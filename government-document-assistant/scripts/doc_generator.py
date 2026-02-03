#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
政务文书生成器
根据模板和用户输入生成符合GB/T 9704-2012标准的公文
"""

import sys
import json
from datetime import datetime
from typing import Dict, Any

class DocumentGenerator:
    """公文生成器类"""
    
    DOCUMENT_TYPES = {
        '通知': 'notice',
        '讲话稿': 'speech',
        '工作报告': 'report',
        '请示': 'request',
        '工作方案': 'plan',
        '心得体会': 'reflection',
        '调研报告': 'research',
        '邀请函': 'invitation'
    }
    
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        try:
            with open('assets/config.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'version': '1.0.0', 'settings': {}}
    
    def generate(self, doc_type: str, params: Dict[str, Any]) -> str:
        """生成公文"""
        if doc_type not in self.DOCUMENT_TYPES:
            return f"错误：不支持的文书类型 {doc_type}"
        
        type_key = self.DOCUMENT_TYPES[doc_type]
        template = self.load_template(type_key)
        
        # 填充基本信息
        params['current_date'] = self.format_date(datetime.now())
        
        # 渲染模板
        content = self.render_template(template, params)
        
        return content
    
    def load_template(self, template_type: str) -> str:
        """加载文书模板"""
        templates = {
            'notice': '{{title}}\n\n{{recipient}}：\n\n{{content}}\n\n特此通知。\n\n{{sender}}\n{{current_date}}',
            'speech': '{{title}}\n\n{{salutation}}：\n\n{{content}}\n\n谢谢大家！',
            'report': '{{title}}\n\n{{recipient}}：\n\n{{content}}\n\n特此报告。\n\n{{sender}}\n{{current_date}}',
            'request': '{{title}}\n\n{{recipient}}：\n\n{{content}}\n\n妥否，请批示。\n\n{{sender}}\n{{current_date}}',
            'plan': '{{title}}\n\n{{content}}',
            'reflection': '{{title}}\n\n{{content}}\n\n{{sender}}\n{{current_date}}',
            'research': '{{title}}\n\n{{content}}',
            'invitation': '邀请函\n\n{{salutation}}：\n\n{{content}}\n\n敬请光临！\n\n{{sender}}\n{{current_date}}'
        }
        return templates.get(template_type, '')
    
    def render_template(self, template: str, params: Dict[str, Any]) -> str:
        """渲染模板"""
        result = template
        for key, value in params.items():
            placeholder = '{{' + key + '}}'
            result = result.replace(placeholder, str(value))
        return result
    
    def format_date(self, date: datetime) -> str:
        """格式化日期为公文标准格式"""
        year = self.num_to_chinese(date.year)
        month = self.num_to_chinese(date.month)
        day = self.num_to_chinese(date.day)
        return f"{year}年{month}月{day}日"
    
    def num_to_chinese(self, num: int) -> str:
        """数字转中文"""
        chinese_nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        if num < 10:
            return chinese_nums[num]
        elif num < 20:
            return '十' + (chinese_nums[num - 10] if num > 10 else '')
        elif num < 100:
            tens = num // 10
            ones = num % 10
            return chinese_nums[tens] + '十' + (chinese_nums[ones] if ones > 0 else '')
        else:
            result = ''
            thousands = num // 1000
            if thousands > 0:
                result += chinese_nums[thousands] + '千'
                num %= 1000
            hundreds = num // 100
            if hundreds > 0:
                result += chinese_nums[hundreds] + '百'
                num %= 100
            elif result:
                result += '零'
            tens = num // 10
            if tens > 0:
                result += chinese_nums[tens] + '十'
                num %= 10
            elif result and num > 0:
                result += '零'
            if num > 0:
                result += chinese_nums[num]
            return result

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python doc_generator.py <文书类型> <参数JSON>")
        print("文书类型: 通知|讲话稿|工作报告|请示|工作方案|心得体会|调研报告|邀请函")
        sys.exit(1)
    
    doc_type = sys.argv[1]
    try:
        params = json.loads(sys.argv[2])
    except:
        print("错误：参数必须是有效的JSON格式")
        sys.exit(1)
    
    generator = DocumentGenerator()
    result = generator.generate(doc_type, params)
    print(result)

if __name__ == '__main__':
    main()