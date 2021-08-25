import os
import pdfplumber
import re
import pandas as pd

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

def create_dataframe(references):
    reference_list = []
    for key, value in references.items():
        reference_list.append(value)
    df = pd.DataFrame(reference_list,index='Ref 1:,Ref 2:,Ref 3:'.split(","),columns='Name,Title,Phone #,Email Address,Project Title'.split(","))
    return df

# main function

def get_reference_data(file_name):
    references = {1: [None]*5, 2: [None]*5, 3: [None]*5}
    ref_number = -1
    with pdfplumber.open(file_name) as pdf:
        page = pdf.pages[1]
        text = page.extract_text()
        text = text.split("\n")
        for line in text:
            ref_number = get_ref(line, ref_number)
            if 1 <= ref_number <= 3:
                if "Name:" in line and "Title:" in line: 
                    line = re.split('Name:|Title:', line)
                    references[ref_number][0] = " ".join(line[1].split()).strip()
                    references[ref_number][1] = " ".join(line[2].split()).strip()
                elif "Phone" in line and "Address:" in line:
                    line = re.split('#:|#|Email  Address:|Email Address:|Adderss:', line)
                    references[ref_number][2] = phone_format("" .join(list(filter(lambda char: char.isdigit(), "".join(line[1].split())))))
                    references[ref_number][3] = " ".join(line[2].split()).strip().replace(" ", "")
                elif "Project" in line and "Title" in line and "Summary:" in line:
                    line = re.split('Summary:', line)
                    references[ref_number][4] = " ".join(line[1].split()).strip()
    incorrect = True
    df = create_dataframe(references)
    while incorrect:
        print(df)
        answer = input("If there ARE mistakes, enter the reference #, followed by the column name (e.g. \"1,Phone #\"). If NO mistakes, enter \"Finished\".\n")
        answer = answer.split(",")
        if len(answer) == 2:
            row = f"Ref {answer[0]}:"
            column = answer[1].strip()
            if row in df.index and column in df.columns:
                df.at[row, column] = input("Type in the correct value for this cell: ") 
            else:
                print("Please enter a valid row and column name!")
        elif answer == ["Finished"]:
            incorrect = False
        else:
            print("Please enter selection in correct format!")
    return df

# checking if the module being ran is imported or is directly being ran
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__": 
    file_name = "output.pdf"
    get_reference_data(file_name) 





        
        


