from docx import Document
from docx.shared import Pt


def create_eVAQ_form(file_name, output_file_name, ref_data):
    document = Document(docx=file_name)
    style = document.styles['Heading 1'] # will make all heading 1 documents headers
    font = style.font
    font.name = 'Calibri Light (Headings)'
    font.size = Pt(12)
    font.bold = True

    for index, p in enumerate(document.paragraphs):
        if index == 0:
            p.text = p.text.replace("[eVAQ]", ref_data[0])
            p.text = p.text.replace("[Ref#]", f"#{ref_data[1]}")
        elif index == 1:                      
            p.text = p.text.replace("[Contact Name]", ref_data[2])
            p.text = p.text.replace("[Title]", ref_data[3])
        elif index == 2:
            p.text = p.text.replace("[Phone #]", ref_data[4])
            p.text = p.text.replace("[Email Address]", ref_data[5])
        elif index == 3:
            p.text = p.text.replace("[Project Title]", ref_data[6])
            break

    document.save(output_file_name)

if __name__ == "__main__":
    ref_data = ["0001113", "1", "Timothy Simanhadi", "Software Engineer", "916-826-5334","timfsim@gmail.com", "Dashboard for Internal Users"]
    file_name = "eVAQ.docx"
    output_file_name = f"eVAQ {ref_data[0]} Reference #{ref_data[1]}.docx"
    create_eVAQ_form(file_name, output_file_name, ref_data)