#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公文格式检查器
检查公文是否符合GB/T 9704-2012国家标准
"""

import sys
import re
from typing import List, Dict, Tuple

class FormatChecker:
    """格式检查器类"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def check(self, content: str, doc_type: str) -> Tuple[bool, List[str], List[str]]:
        """检查公文格式"""
        self.errors = []
        self.warnings = []
        
        # 基础检查
        self.check_title(content)
        self.check_structure(content, doc_type)
        self.check_language(content)
        self.check_punctuation(content)
        self.check_date_format(content)
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def check_title(self, content: str):
        """检查标题"""
        lines = content.split('\n')
        if not lines:
            self.errors.append("缺少标题")
            return
        
        title = lines[0].strip()
        if not title:
            self.errors.append("标题不能为空")
            return
        
        # 检查标题标点
        if title.endswith(('。', '！', '？')):
            self.warnings.append("标题一般不使用句末标点符号")
        
        # 检查标题长度
        if len(title) > 40:
            self.warnings.append("标题过长，建议控制在40字以内")
    
    def check_structure(self, content: str, doc_type: str):
        """检查文书结构"""
        required_elements = {
            '通知': ['特此通知'],
            '报告': ['特此报告'],
            '请示': ['请批示', '妥否'],
            '讲话稿': []
        }
        
        elements = required_elements.get(doc_type, [])
        for element in elements:
            if element not in content:
                self.warnings.append(f"建议添加'{element}'等结束语")
    
    def check_language(self, content: str):
        """检查语言规范"""
        # 检查口语化表达
        informal_words = ['搞', '弄', '挺', '蛮', '挺好', '还行']
        for word in informal_words:
            if word in content:
                self.warnings.append(f"建议避免口语化表达'{word}'")
        
        # 检查网络用语
        internet_slang = ['给力', '点赞', '666', '厉害了']
        for slang in internet_slang:
            if slang in content:
                self.errors.append(f"不应使用网络用语'{slang}'")
    
    def check_punctuation(self, content: str):
        """检查标点符号"""
        # 检查是否有英文标点
        english_punctuation = [',', ';', ':', '!', '?', '(', ')']
        for punct in english_punctuation:
            if punct in content:
                self.warnings.append(f"发现英文标点'{punct}'，建议使用中文标点")
        
        # 检查连续标点
        if re.search(r'[。！？]{2,}', content):
            self.warnings.append("存在连续标点符号")
    
    def check_date_format(self, content: str):
        """检查日期格式"""
        # 查找阿拉伯数字日期
        date_pattern = r'\d{4}[年.-]\d{1,2}[月.-]\d{1,2}[日]?'
        if re.search(date_pattern, content):
            self.warnings.append("成文日期建议使用汉字书写")
    
    def generate_report(self) -> str:
        """生成检查报告"""
        report = "\n=== 公文格式检查报告 ===\n\n"
        
        if not self.errors and not self.warnings:
            report += "✓ 未发现格式问题\n"
        else:
            if self.errors:
                report += f"错误 ({len(self.errors)}项):\n"
                for i, error in enumerate(self.errors, 1):
                    report += f"  {i}. {error}\n"
                report += "\n"
            
            if self.warnings:
                report += f"建议 ({len(self.warnings)}项):\n"
                for i, warning in enumerate(self.warnings, 1):
                    report += f"  {i}. {warning}\n"
        
        return report

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python format_checker.py <文书类型> <文件路径>")
        sys.exit(1)
    
    doc_type = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"错误：无法读取文件 - {e}")
        sys.exit(1)
    
    checker = FormatChecker()
    is_valid, errors, warnings = checker.check(content, doc_type)
    
    print(checker.generate_report())
    
    sys.exit(0 if is_valid else 1)

if __name__ == '__main__':
    main()