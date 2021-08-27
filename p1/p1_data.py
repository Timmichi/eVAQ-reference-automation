'''
1. Install Chocolatey: https://chocolatey.org/install
2. Install pre tesseract, and ghostcript using choco. Install ocrmypdf using pip. https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows
3. Install pdfplumber (pip install pdfplumber)
4. Install pandas https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index
5. Install business-python calendar: https://github.com/gocardless/business-python
'''
import os, subprocess
import pandas as pd
from . import get_file_info, get_data, create_docs # same as writing "from p1" but saves the refactoring if we move the file out of the package

def p1_create_files_and_get_data(input_file_name, directory_path):
    
    email_data = []
    for root, directories, files in os.walk(directory_path):
        for directory in directories:
            if "eVAQ" in directory:
                curr_directory = os.path.join(root,directory)
                file_name, file_path = get_file_info.get_file_info(curr_directory)
                print(f"\nPERFORMING ON {file_name}\n")
                command = f"ocrmypdf \"{file_name}\" \"{file_name}\" --force-ocr" # files with spaces in their name need to have quotations around them 
                p = subprocess.Popen(command, cwd=curr_directory) # going into directory where files are located
                p.wait()
                print("\nSuccessfully converted PDF using OCR (optical character recognition)! 🔃\n")
                print("\nDisplaying RAW 🥩 reference data extracted from PDF!\n")
                df = get_data.get_reference_data(file_path)
                print("\nFinished refactoring and verifying data! ✅\n")
                eVAQ_num = "".join(filter(lambda x: x.isdigit(), file_name))
                vendor_name = input(f"Please enter the name of the vendor for eVAQ #{eVAQ_num}:\n(⚠ WARNING ⚠ This is the FINAL CHECK before sending the emails! 📨)\n").strip()
                for i, [index, row] in enumerate(df.iterrows()):
                    eVAQ_info = []
                    eVAQ_info.append(eVAQ_num) # add evaq #
                    eVAQ_info.append("".join(filter(lambda x: x.isdigit(), index))) # add ref #
                    input_file_path = os.path.join(root, input_file_name) # input file path 
                    output_file_name = f"eVAQ {eVAQ_info[0]} Reference #{eVAQ_info[1]}.docx"
                    output_file_path = os.path.join(curr_directory, output_file_name) # output file path
                    ref_data = df.iloc[i] # contains ref data
                    create_docs.create_eVAQ_form(input_file_path, output_file_path, ref_data, eVAQ_info, output_file_path) # creates eVAQ form
                    data = eVAQ_info + ref_data.tolist()
                    data.extend([output_file_path, vendor_name])
                    email_data.append(data)
    email_data_df = pd.DataFrame(email_data,columns='eVAQ, ref, name, title, phone, email_address, project_title, attachment_path, vendor_name'.split(", "))
    return email_data_df
    
if __name__ == "__main__":
    # to test this module, go to the main project directory "C:\Users\timfs\Desktop\WORK\eVAQ-reference-automation" and run python -m p1.p1_data
    input_file_name = "template.docx"
    directory_path = "C:\\Users\\timfs\\Desktop\\WORK\\eVAQ-reference-automation\\test"
    email_data = p1_create_files_and_get_data(input_file_name, directory_path)
    print(email_data)