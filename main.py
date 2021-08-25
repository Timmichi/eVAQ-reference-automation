'''
1. Install Chocolatey: https://chocolatey.org/install
2. Install pre tesseract, and ghostcript using choco. Install ocrmypdf using pip. https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows
3. Install pdfplumber (pip install pdfplumber)
4. Install pandas https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index
'''
import os
import pdfplumber
import re
import pandas as pd
import get_data

def main():
    # Use os to find all files in the folder and loop through
    # pdf_name = "eVAQ.pdf" # make this an input() later
    # os.system(f'ocrmypdf {pdf_name} output.pdf --force-ocr')
    df = get_data.get_reference_data("output.pdf")
    
    
if __name__ == "__main__":
    main()