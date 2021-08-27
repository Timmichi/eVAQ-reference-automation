'''
1. Install Chocolatey: https://chocolatey.org/install
2. Install pre tesseract, and ghostcript using choco. Install ocrmypdf using pip. https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows
3. Install pdfplumber (pip install pdfplumber)
4. Install pandas https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index
'''
import os, subprocess
import pandas as pd
from p1 import get_file_info, get_data, create_docs

def p1_create_files_and_get_data(input_file_name, directory_path):
    email_data = []
    for root, directories, files in os.walk(directory_path):
        for directory in directories:
            if "eVAQ" in directory:
                curr_directory = os.path.join(root,directory)
                file_name, file_path = get_file_info.get_file_info(curr_directory)
                print(f"\nPerforming on {file_name}\n")
                command = f"ocrmypdf \"{file_name}\" \"{file_name}\" --force-ocr" # files with spaces in their name need to have quotations around them 
                p = subprocess.Popen(command, cwd=curr_directory) # going into directory where files are located
                p.wait()
                print("Successfully converted PDF using OCR (optical character recognition)!\n")
                print("\nDisplaying RAW reference data extracted from PDF!\n")
                df = get_data.get_reference_data(file_path)
                print("\nFinished refactoring and verifying data!\n")
                for i, [index, row] in enumerate(df.iterrows()):
                    eVAQ_info = []
                    eVAQ_info.append("".join(filter(lambda x: x.isdigit(), file_name))) # add evaq #
                    eVAQ_info.append("".join(filter(lambda x: x.isdigit(), index))) # add ref #
                    input_file_path = os.path.join(curr_directory, input_file_name) # input file path 
                    output_file_name = f"eVAQ {eVAQ_info[0]} Reference #{eVAQ_info[1]}.docx"
                    output_file_path = os.path.join(curr_directory, output_file_name) # output file path
                    ref_data = df.iloc[i] # contains ref data
                    create_docs.create_eVAQ_form(input_file_path, output_file_path, ref_data, eVAQ_info, output_file_path) # creates eVAQ form
                    print(ref_data.tolist())
                    data = eVAQ_info + ref_data.tolist()
                    data.append(output_file_path)
                    email_data.append(data)
            email_data_df = pd.DataFrame(email_data,index='1, 2, 3'.split(", "),columns='eVAQ, ref, name, title, phone, email_address, project_title, attachment_path'.split(", "))
    return email_data_df
    
if __name__ == "__main__":
    input_file_name = "eVAQ.docx"
    directory_path = r"C:\Users\timfs\Desktop\eVAQ-reference-automation\eVAQs"
    email_data = p1_create_files_and_get_data(input_file_name, directory_path)
    print(email_data)