import os, pdfplumber
file_name = "eVAQ 0001114.pdf"

print(command)
os.system(command)
with pdfplumber.open(file_name) as pdf:
        page = pdf.pages[1]
        text = page.extract_text().split("\n")
print(text)