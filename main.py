'''
1. Install Chocolatey: https://chocolatey.org/install
2. Install pre tesseract, and ghostcript using choco. Install ocrmypdf using pip. https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows
'''
import os
import pdfplumber
import re
import pandas as pd
import numpy as np

# Use os to find all files in the folder and loop through
# myPdf = "eVAQ.pdf"

# os.system(f'ocrmypdf {myPdf} output.pdf --force-ocr')



# Helper functions

def get_ref(line, ref_number):
    if "Reference" in line and "#1" in line:
        return 1
    elif "Reference" in line and "#2" in line:
        return 2
    elif "Reference" in line and "#3" in line:
        return 3
    elif 1 <= ref_number <= 3: # if ref_number is already valid then just return
        return ref_number
    else:
        return -1

def phone_format(n):                                                                                                                                  
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]  

def check_references(references):
    for key, value in references.items():
        answer = input(f"Is Reference #{key[-1]}'s {key[:-1]}: {value}? (If YES enter \"y\". If NO, type in the correct {key[:-1]}.)\n")
        if answer != "y":
            references[key] = answer
    
def main():
    references = {}
    ref_number = -1
    with pdfplumber.open("output.pdf") as pdf:
        page = pdf.pages[1]
        text = page.extract_text()
        text = text.split("\n")
        for line in text:
            ref_number = get_ref(line, ref_number)
            print(ref_number, line)
            if 1 <= ref_number <= 3:
                if "Name:" in line and "Title:" in line: 
                    line = re.split('Name:|Title:', line)
                    references[f"name{ref_number}"] = " ".join(line[1].split()).strip()
                    references[f"title{ref_number}"] = " ".join(line[2].split()).strip()
                elif "Phone" in line and "Address:" in line:
                    line = re.split('#:|#|Email  Address:|Email Address:|Adderss:', line)
                    references[f"phone number{ref_number}"] = phone_format("" .join(list(filter(lambda char: char.isdigit(), "".join(line[1].split())))))
                    references[f"email{ref_number}"] = " ".join(line[2].split()).strip().replace(" ", "")
                elif "Project" in line and "Title" in line and "Summary:" in line:
                    line = re.split('Summary:', line)
                    references[f"project_title{ref_number}"] = " ".join(line[1].split()).strip()
    df = pd.DataFrame(references.values(),index='Reference 1, Reference 2, Reference 3'.split(),columns='name, title, phone number, email, project_title'.split(","))
    print(df)
    check_references(references)
    print(references)


# checking if the module being ran is imported or is directly being ran
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__": 
    main() 





        
        


