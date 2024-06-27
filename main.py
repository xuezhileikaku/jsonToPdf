#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
@Project ：jsonToPdf 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：xuezhileikaku
@Date    ：2024/6/25 21:03 
'''
from datetime import datetime
import json
import re
from db_tool import Paper,Question, Detail
from peewee import IntegrityError
import time


def add_paper(paper_name, paper_data):
    # 添加问题到数据库的逻辑
    try:
        paper, created = Paper.get_or_create(paper_name=paper_name, defaults=paper_data)
        if created:
            return paper
        else:
            return paper
    except Exception as e:
        return str(e)
def add_detail(ques_id,det_data):
    try:
        det, created = Detail.get_or_create(ques_id=ques_id, defaults=det_data)
        if created:
            return det
        else:
            return det
    except Exception as e:
        return str(e)
def paper():
    current_time = int(time.time())
    for id in range(101, 159):
        paper_name = f"NewPrepTest {id}"
        pdata = {
            'paper_name': paper_name,
            'paper_order': 1,
            'paper_status': 0,
            'paper_longtime': 140,
            'paper_createtime': current_time,
            'paper_note': None,
            'paper_group': None,
            'paper_type': 134,
            'test_mode': 0,
            'paper_section': '112,113,114,115',
            'exam_type': 8
        }
        paper = add_paper(paper_name, pdata)
        print(paper)
        # break
def extract_number_from_string(input_string):
    # 匹配LR或RC后面跟的三位数字
    match = re.search(r'(LR|RC)(\d+)', input_string)
    if match:
        return match.group(2)  # 返回匹配到的数字部分
    else:
        return None
def get_print_num(qid):
    try:
        if Question.select().where(Question.ques_id == qid).exists():
            # 如果存在，获取选项实例
            ques = Question.get(Question.ques_id == qid)
            return ques
        else:
            return None
    except Exception as e:
        return str(e)
def get_paper_id(paper_name):
    try:
        if Paper.select().where(Paper.paper_name == paper_name).exists():
            # 如果存在，获取选项实例
            paper = Paper.get(Paper.paper_name == paper_name)
            return paper.paper_id
        else:
            return None
    except Exception as e:
        return str(e)

def main():
    current_time = int(time.time())
    for qid in range(9671, 15263):
        ques=get_print_num(qid)
        printNum =ques.printNum
        pid=extract_number_from_string(printNum)
        paper_name = f"NewPrepTest {pid}"
        paper_id=get_paper_id(paper_name)
        if paper_id>584:
            ddata= {
                'paper_id': paper_id,
                'ques_id': qid,
                'paper_status': 1,
                'paper_modu': ques.ques_section,
                'create_time': current_time
            }
            det=add_detail(qid,ddata)
            print(det)
        # break
if __name__ == "__main__":
    main()