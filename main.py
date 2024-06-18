import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line

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
    # 使用自定义中文字体
    pdfmetrics.registerFont(TTFont('Times_New_Roman', './aliicon/Times_New_Roman.ttf'))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomHeading2', fontName='Times_New_Roman', fontSize=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontName='Times_New_Roman', fontSize=12, spaceAfter=10))

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    for sec in data:
        print(f"Section {sec['sectionOrder']}")
        elements.append(Paragraph("Section "+str(sec['sectionOrder']), styles['CustomHeading2']))
        elements.append(Paragraph(sec['directions'], styles['CustomBodyText']))
        passage=''
        for item in sec['items']:
            print(f"Question {item['itemPosition']}")
            elements.append(Paragraph("Question " + str(item['itemPosition']), styles['CustomHeading2']))
            # print(passage,item['stimulusText'])
            if passage!=item['stimulusText']:
                passage=item['stimulusText']
                elements.append(Paragraph(passage, styles['CustomBodyText']))

            elements.append(Paragraph(item['stemText'], styles['CustomBodyText']))
            if 'options' in item:
                for op in item['options']:
                    op_label = op['optionLetter']
                    op_val = op['optionContent']
                    op_val = op_val.replace("<p>", "<p>" + op_label + ". ")
                    elements.append(Paragraph(op_val, styles['CustomBodyText']))
            if 'correctAnswer' in item:
                elements.append(Paragraph("Answer:" +item['correctAnswer'], styles['CustomBodyText']))
        elements.append(Spacer(1, 12))  # 在每个题目后添加换行
    # 添加横线分割
    line = Drawing(500, 1)
    line.add(Line(0, 0, 500, 0))
    elements.append(line)
    elements.append(Spacer(1, 12))  # 添加一个间隔
    elements.append(Spacer(1, 12))  # 添加一个间隔

    doc.build(elements)

def main(json_path, pdf_path):
    for nu in range(114, 159):
        json_file = json_path + str(nu) + '.json'
        pdf_file = pdf_path + str(nu) + '.pdf'
        data = read_json(json_file)
        parse_json(data, pdf_file)
        print(f"PDF generated successfully and saved to {pdf_file}")
        # break

if __name__ == "__main__":
    json_file_path = './json/pt'  # 替换为你的JSON文件路径
    pdf_file_path = './pdf/'  # 替换为你想要的PDF文件路径
    main(json_file_path, pdf_file_path)
