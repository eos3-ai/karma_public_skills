#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime
from typing import Dict, Any

class GovernmentDocumentGenerator:
    def __init__(self):
        self.doc_types = {
            'notice': '通知',
            'speech': '讲话稿',
            'report': '工作报告',
            'request': '请示',
            'plan': '工作方案',
            'reflection': '心得体会'
        }
    
    def generate_title(self, doc_type: str, subject: str, issuer: str = '') -> str:
        if doc_type == 'notice':
            return f'{issuer}关于{subject}的通知' if issuer else f'关于{subject}的通知'
        elif doc_type == 'speech':
            return f'在{subject}上的讲话'
        elif doc_type == 'report':
            return f'{issuer}关于{subject}的报告' if issuer else f'关于{subject}的报告'
        elif doc_type == 'request':
            return f'{issuer}关于{subject}的请示' if issuer else f'关于{subject}的请示'
        elif doc_type == 'plan':
            return f'{subject}工作方案'
        elif doc_type == 'reflection':
            return f'{subject}心得体会'
        else:
            return subject
    
    def format_date(self, date_obj: datetime = None) -> str:
        if date_obj is None:
            date_obj = datetime.now()
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        cn_nums = ['〇', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        year_cn = ''.join([cn_nums[int(d)] for d in str(year)])
        month_cn = ''.join([cn_nums[int(d)] for d in str(month)])
        day_cn = ''.join([cn_nums[int(d)] for d in str(day)])
        return f'{year_cn}年{month_cn}月{day_cn}日'
    
    def generate_notice_structure(self, data: Dict[str, Any]) -> str:
        title = self.generate_title('notice', data.get('subject', ''), data.get('issuer', ''))
        recipient = data.get('recipient', '各有关单位')
        content = data.get('content', '')
        issuer = data.get('issuer', 'XX单位')
        date = self.format_date()
        
        structure = f'{title}\n\n{recipient}：\n\n{content}\n\n特此通知。\n\n{issuer}\n{date}'
        return structure
    
    def generate_speech_structure(self, data: Dict[str, Any]) -> str:
        title = self.generate_title('speech', data.get('subject', ''))
        salutation = data.get('salutation', '同志们')
        content = data.get('content', '')
        
        structure = f'{title}\n\n{salutation}：\n\n{content}\n\n谢谢大家！'
        return structure
    
    def generate(self, doc_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        result = {
            'success': True,
            'doc_type': self.doc_types.get(doc_type, doc_type),
            'content': '',
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'standard': 'GB/T 9704-2012'
            }
        }
        
        try:
            if doc_type == 'notice':
                result['content'] = self.generate_notice_structure(data)
            elif doc_type == 'speech':
                result['content'] = self.generate_speech_structure(data)
            else:
                result['content'] = f'{self.generate_title(doc_type, data.get("subject", ""), data.get("issuer", ""))}\n\n{data.get("content", "")}'
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
        
        return result

def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': '缺少参数：文书类型'}, ensure_ascii=False))
        sys.exit(1)
    
    doc_type = sys.argv[1]
    data = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    
    generator = GovernmentDocumentGenerator()
    result = generator.generate(doc_type, data)
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()