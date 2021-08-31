from docx import Document
from docx.shared import Pt


def create_eVAQ_form(input_file_path, output_file_path, ref_data, eVAQ_info, output_file_name):
    document = Document(docx=input_file_path)
    style = document.styles['Heading 1'] # will make all heading 1 documents headers
    font = style.font
    font.name = 'Calibri Light (Headings)'
    font.size = Pt(12)
    font.bold = True
    for index, p in enumerate(document.paragraphs):
        if index == 0:
            p.text = p.text.replace("[eVAQ #]", eVAQ_info[0])
            p.text = p.text.replace("[Ref #]", f"#{eVAQ_info[1]}")
        elif index == 1:                      
            p.text = p.text.replace("[Contact Name]", ref_data[0])
            p.text = p.text.replace("[Title]", ref_data[1])
        elif index == 2:
            p.text = p.text.replace("[Phone #]", ref_data[2])
            p.text = p.text.replace("[Email Address]", ref_data[3])
        elif index == 3:
            p.text = p.text.replace("[Project Title]", ref_data[4])
        elif index == 4:
            p.text = p.text.replace("[Summary]", ref_data[5])
            break
    
    document.save(output_file_path)
    print(f"{output_file_name} was successfully created!")

if __name__ == "__main__":
    ref_data = ["Timothy Simanhadi", "Software Engineer", "916-826-5334","timfsim@gmail.com", "Dashboard for Internal Users", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
    eVAQ_info = ["0000000", "1"]
    input_file_path = r".\test\template.docx"
    output_file_name = f"eVAQ {eVAQ_info[0]} Reference #{eVAQ_info[1]}.docx"
    output_file_path = f".\\test\\eVAQ {eVAQ_info[0]}\\" + output_file_name
    print(output_file_path)
    create_eVAQ_form(input_file_path, output_file_path, ref_data, eVAQ_info, output_file_name)