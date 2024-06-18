import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, Line

def read_json(file_path):
    """Read JSON file from the given file path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def parse_json(data, output_path):
    """Parse JSON data and generate a PDF with the given output path."""
    # Register custom font
    pdfmetrics.registerFont(TTFont('Times_New_Roman', './aliicon/Times_New_Roman.ttf'))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomHeading2', fontName='Times_New_Roman', fontSize=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontName='Times_New_Roman', fontSize=12, spaceAfter=10))

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    for sec in data:
        elements.append(Paragraph("Section " + str(sec['sectionOrder']), styles['CustomHeading2']))
        elements.append(Paragraph(sec['directions'], styles['CustomBodyText']))
        elements.append(Spacer(1, 12))  # Add space after section directions

        passage = ''
        for item in sec['items']:
            elements.append(Paragraph("Question " + str(item['itemPosition']), styles['CustomHeading2']))
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
                elements.append(Spacer(1, 12))  # Add space after each option

            if 'correctAnswer' in item:
                elements.append(Paragraph("Answer: " + item['correctAnswer'], styles['CustomBodyText']))

            elements.append(Spacer(1, 12))  # Add space after each question

        # Add a line separator after each section
        line = Drawing(500, 1)
        line.add(Line(0, 0, 500, 0))
        elements.append(line)
        elements.append(Spacer(1, 12))  # Add space after the line

    doc.build(elements)

def main(json_path, pdf_path):
    """Main function to read JSON files and generate corresponding PDFs."""
    for nu in range(114, 159):
        json_file = json_path + str(nu) + '.json'
        pdf_file = pdf_path + str(nu) + '.pdf'
        data = read_json(json_file)
        parse_json(data, pdf_file)
        print(f"PDF generated successfully and saved to {pdf_file}")

if __name__ == "__main__":
    json_file_path = './json/prefix'  # Replace with your JSON file path
    pdf_file_path = './pdf/'  # Replace with your desired PDF file path
    main(json_file_path, pdf_file_path)
