# 发票OCR识别模块
import requests
import base64
import json
from typing import Dict, Optional

class InvoiceOCR:
    def __init__(self, api_key: str, api_type: str = 'baidu'):
        self.api_key = api_key
        self.api_type = api_type
    
    def recognize(self, image_path: str) -> Optional[Dict]:
        '''识别发票图片并返回结构化数据'''
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        if self.api_type == 'baidu':
            return self._baidu_ocr(image_data)
        # 可扩展支持其他OCR服务
        return None
    
    def _baidu_ocr(self, image_data: str) -> Dict:
        '''调用百度OCR API'''
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice'
        params = {'access_token': self.api_key}
        data = {'image': image_data}
        response = requests.post(url, params=params, data=data)
        return response.json()
    
    def extract_fields(self, ocr_result: Dict) -> Dict:
        '''从OCR结果中提取关键字段'''
        fields = {
            'buyer_name': '',
            'invoice_date': '',
            'amount': 0.0,
            'tax': 0.0,
            'invoice_number': '',
            'invoice_type': ''
        }
        # 解析OCR结果并填充字段
        if 'words_result' in ocr_result:
            result = ocr_result['words_result']
            fields['buyer_name'] = result.get('PurchaserName', '')
            fields['invoice_date'] = result.get('InvoiceDate', '')
            fields['amount'] = float(result.get('AmountInFiguers', '0'))
            fields['tax'] = float(result.get('TotalTax', '0'))
            fields['invoice_number'] = result.get('InvoiceNum', '')
            fields['invoice_type'] = result.get('InvoiceType', '')
        return fields