#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
@Project ：gmat 
@File    ：ls.py.py
@IDE     ：PyCharm 
@Author  ：xuezhileikaku
@Date    ：2024/6/20 21:47 
'''
import pdfkit
from pdfkit import from_url


options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
}


if __name__ == '__main__':
    for id in range(101,159):
        url = 'http://localhost/tools/prep.php?id='+str(id)
        pdfkit.from_url(url, './pdf/pt'+str(id)+'.pdf', options=options)
        break
