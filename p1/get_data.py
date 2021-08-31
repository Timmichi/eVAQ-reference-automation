import re
import pdfplumber
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
    df = pd.DataFrame(reference_list,index='Ref 1:,Ref 2:,Ref 3:'.split(","),columns='Name,Title,Number,Email,Project,Summary'.split(","))
    for i, summary in enumerate((df.get('Summary'))):
        print(f"Ref {i+1} Summary:")
        print(summary, end="\n\n")
    return df

# main function

def get_reference_data(file_path):
    references = {1: [None]*6, 2: [None]*6, 3: [None]*6}
    ref_number = -1
    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[1]
        text = page.extract_text().split("\n")
        i = 0
        while i < len(text):
            ref_number = get_ref(text[i], ref_number)
            if 1 <= ref_number <= 3:
                line = text[i]
                if "Name:" in line and "Title:" in line: 
                    line = re.split('Name:|Title:', line)
                    references[ref_number][0] = " ".join(line[1].split()).strip()
                    references[ref_number][1] = " ".join(line[2].split()).strip()
                elif "Phone" in line and "Address:" in line:
                    line = re.split('#:|#|Email  Address:|Email Address:|Address:', line)
                    references[ref_number][2] = phone_format("" .join(list(filter(lambda char: char.isdigit(), "".join(line[1].split())))))
                    references[ref_number][3] = " ".join(line[2].split()).strip().replace(" ", "")
                elif ("Project" in line and "Title" in line) or ("&" in line and "Summary:" in line):
                    line = re.split(':', line)
                    try:
                        references[ref_number][4] = " ".join(line[1].split()).strip()
                        i += 1
                        while i < len(text) and "Reference" not in text[i] and "#" not in text[i]:
                            if references[ref_number][5] == None:
                                references[ref_number][5] = text[i]
                            else:
                                references[ref_number][5] += text[i]
                            i += 1
                        references[ref_number][5] = " ".join(references[ref_number][5].split())
                        continue
                    except IndexError:
                        i += 1
                        references[ref_number][4] = " ".join(text[i].split()).strip()
                        i += 1
                        while i < len(text) and "Reference" not in text[i] and "#" not in text[i]:
                            if references[ref_number][5] == None:
                                references[ref_number][5] = text[i]
                            else:
                                references[ref_number][5] += text[i]
                            i += 1
                        references[ref_number][5] = " ".join(references[ref_number][5].split())
                        continue
                i += 1
    incorrect = True
    df = create_dataframe(references)
    while incorrect:
        print(df)
        answer = input("\nIf there ARE mistakes, enter the reference #, followed by the column name (e.g. \"1 Phone #\"). If NO mistakes, enter \"Finished\".\n").strip()
        answer = answer.split(" ")
        if len(answer) == 2:
            row = f"Ref {answer[0]}:"
            column = answer[1]
            if row in df.index and column in df.columns:
                df.at[row, column] = input("Type in the correct value for this cell: ").strip() 
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
    file_path = ".\\test\\eVAQ 0000000\\eVAQ 0000000.pdf"
    get_reference_data(file_path) 





        
        


