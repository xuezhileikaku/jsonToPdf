#!/usr/bin/env python3
#
from datetime import datetime
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line
import re
from db_tool import Question,Option
from peewee import IntegrityError
import time
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def generate_pdf1(data, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y_position = height - 40  # Starting position for text

    for key, value in data.items():
        text = f"{key}: {value}"
        c.drawString(40, y_position, text)
        y_position -= 20  # Move to the next line
        if y_position < 40:  # Create a new page if the current one is full
            c.showPage()
            y_position = height - 40

    c.save()


def generate_pdf(data, output_path):
    # 使用自定义中文字体
    pdfmetrics.registerFont(TTFont('Alibaba_PuHuiTi', './aliicon/Alibaba_PuHuiTi_2.0_55_Regular_55_Regular.ttf'))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomHeading2', fontName='Alibaba_PuHuiTi', fontSize=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontName='Alibaba_PuHuiTi', fontSize=12, spaceAfter=10))

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    module_name = data.get('module', {}).get('name', '')
    elements.append(Paragraph(module_name, styles['CustomHeading2']))

    sections = data.get('module', {}).get('sections', [])
    for section in sections:
        title = section.get('title', '')
        name = section.get('name', '')
        elements.append(Paragraph(title, styles['CustomHeading2']))
        elements.append(Paragraph(name, styles['CustomBodyText']))
        elements.append(Spacer(1, 12))

    doc.build(elements)


def parse_json(data, output_path):
    # 使用英文字体
    pdfmetrics.registerFont(TTFont('Times_New_Roman', './aliicon/Times_New_Roman.ttf'))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomHeading2', fontName='Times_New_Roman', fontSize=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontName='Times_New_Roman', fontSize=12, spaceAfter=10))

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    for sec in data:
        print(f"Section {sec['sectionOrder']}")
        elements.append(Paragraph("Section " + str(sec['sectionOrder']), styles['CustomHeading2']))
        elements.append(Paragraph(sec['directions'], styles['CustomBodyText']))
        passage = ''
        for item in sec['items']:
            print(f"Question {item['itemPosition']}")
            elements.append(Paragraph("Question " + str(item['itemPosition']), styles['CustomHeading2']))
            # print(passage,item['stimulusText'])
            if passage != item['stimulusText']:
                passage = item['stimulusText']
                elements.append(Paragraph(passage, styles['CustomBodyText']))

            elements.append(Paragraph(item['stemText'], styles['CustomBodyText']))
            if 'options' in item:
                for op in item['options']:
                    op_label = op['optionLetter']
                    op_val = op['optionContent']
                    op_val = op_val.replace("<p>", "<p>" + op_label + ". ")
                    elements.append(Paragraph(op_val, styles['CustomBodyText']))
            if 'correctAnswer' in item:
                elements.append(Paragraph("Answer:" + item['correctAnswer'], styles['CustomBodyText']))
        elements.append(Spacer(1, 12))  # 在每个题目后添加换行
    # 添加横线分割
    line = Drawing(500, 1)
    line.add(Line(0, 0, 500, 0))
    elements.append(line)
    elements.append(Spacer(1, 12))  # 添加一个间隔
    elements.append(Spacer(1, 12))  # 添加一个间隔

    doc.build(elements)


def replace_tags(context):
    pattern = r"<p[^>]*>(.*?)<\/p>"
    new_text = re.sub(pattern, r"\1", context, flags=re.DOTALL)
    return new_text


def get_prefix_with_dash(input_string):
    prefix = input_string.split('-')[0]
    return prefix


def add_ques(print_num, ques_data):
    # 添加问题到数据库的逻辑
    # print(print_num)
    # print(ques_data)
    try:
        question, created = Question.get_or_create(printNum=print_num, defaults=ques_data)
        if created:
            return question
        else:
            return question
    except Exception as e:
        return str(e)


def add_option(qu_id, ops_data):
    # 检查是否已经存在选项
    if Option.select().where(Option.ques_id == qu_id).exists():
        # 如果存在，获取选项实例
        existing_option = Option.get(Option.ques_id == qu_id)
        return existing_option

    try:
        # 使用 create 方法插入新选项
        new_option = Option.create(**ops_data)
        return new_option
    except IntegrityError as e:
        # 处理可能的数据库完整性错误，例如外键约束失败
        return f"插入失败：{e}"

def get_type_id(input_string):
    prefix = input_string.split('-')[0]
    sec_id=112
    # 检查前缀长度是否足够
    if len(prefix) > 2:
        # 取前两位和最后一位进行拼接
        sec_type = prefix[:2] + prefix[-1]
        if sec_type=='LRA':
            sec_id=113
        elif sec_type=='LRB':
            sec_id=114
        elif sec_type == 'RCA':
            sec_id = 115

    else:
        # 如果前缀长度不足，可能需要返回一个错误或特定的值
        type_id = "Invalid input"
    return sec_id

def json_ques(data):
    ques = []
    for sec in data:
        # qu = {
        #     "passage": "", "title": "", "fromId": "", "groupId": "",
        #     "ops_a": "", "ops_b": "", "ops_c": "", "ops_d": "", "ops_e": "",
        #     "answer": "", "sec": "", "sec_tag": "", "type": "", "order": ""
        # }
        current_time = int(time.time())
        # ques_data = {
        #     'ques_title': '',
        #     'ques_section': 1,
        #     'ques_ans': '',
        #     'ques_type': '',
        #     'ques_create_time': current_time,
        #     'passage': '',
        #     'print_num': '',  # 假设print_num是问题的唯一标识符
        # }
        # 'print_num': '',
        # qu['sec'] = str(sec['sectionOrder'])
        # print(f"Section {sec['sectionOrder']}")
        # qu['sec_tag'] = sec['sectionId']
        sec_id = get_type_id(sec['sectionId'])
        passage = ''
        for item in sec['items']:
            ques_data = {
                'ques_title': replace_tags(item['stemText']),
                'ques_section': sec_id,
                'ques_ans': item.get('correctAnswer', ''),
                'ques_type': 118 if sec_id in [113, 114] else 119,
                'ques_create_time': current_time,
                'passage': replace_tags(item['stimulusText']),
                'printNum': f"{sec['sectionId']}_q{item['itemPosition']}_{item['itemId']}",
            }

            # qu.update({
            #     'sec': str(sec['sectionOrder']),
            #     'sec_tag': sec['sectionId'],
            #     'passage': ques_data['passage'],
            #     'title': ques_data['ques_title'],
            #     'fromId': item['itemId'],
            #     'groupId': item['groupId'],
            #     'type': get_prefix_with_dash(item['groupId']),
            #     'order': str(item['itemPosition']),
            #     'answer': ques_data['ques_ans'],
            # })
            print(f"Processing question: {ques_data['printNum']}")
            # 调用函数
            result = add_ques(ques_data['printNum'], ques_data)
            print(result)
            if isinstance(result, Question):
                print(f"问题已成功插入，ID：{result.ques_id}")
            else:
                print(f"问题已存在，ID：{result.ques_id}")

            ques_id = result.ques_id

            if 'options' in item:
                op_data = {'ques_id': ques_id}
                for op in item['options']:
                    op_k = f"op{op['optionLetter'].lower()}"
                    op_val = replace_tags(op['optionContent'])
                    op_data[op_k] = op_val
                # print(op_data)

                res = add_option(ques_id, op_data)
                if isinstance(res, Option):
                    print(f"选项已成功插入，ID：{res.id}, ques_id:{res.ques_id}")
                else:
                    print(res)
            # break

        # ques.append(qu)
        # break


def main(json_path, pdf_path):
    for nu in range(101, 159):
        if nu not in [140, 141, 157, 158]:
            json_file = json_path + str(nu) + '.json'
            pdf_file = pdf_path + str(nu) + '.pdf'
            data = read_json(json_file)
            # parse_json(data, pdf_file)
            json_ques(data)
            print(f"read from pt{nu}.json")
            # print(f"PDF generated successfully and saved to {pdf_file}")
            # break


if __name__ == "__main__":
    json_file_path = './json/pt'  # 替换为你的JSON文件路径
    pdf_file_path = './pdf/'  # 替换为你想要的PDF文件路径
    main(json_file_path, pdf_file_path)
