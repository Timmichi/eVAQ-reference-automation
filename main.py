'''
Naming Convention:
1. Create a folder named "eVAQs"
2. Inside, create folders for each EVAQ and use this naming convention: e.g. "eVAQ 0001113"
3. Within each eVAQ folder, make sure the original pdf from the company is renamed to "eVAQ 000113.pdf" and the "eVAQ.docx" containing the template is inside as well.
4. Set the correct Global Variables below to find the main "eVAQs" folder and the "eVAQ.docx"

columns='eVAQ, ref, name, title, phone, email_address, project_title, summary, attachment_path, vendor_name, date'
'''
from p1 import p1_data
from p2 import p2_email, html_body
import pandas as pd

# Globals
INPUT_FILE_NAME = "template.docx"
DIRECTORY_PATH = "C:\\Users\\timfs\\Desktop\\WORK\\eVAQ-reference-automation\\eVAQs"

def main():
    data_df = p1_data.p1_create_files_and_get_data(INPUT_FILE_NAME, DIRECTORY_PATH)
    for row in data_df.itertuples():
        p2_email.p2_send_email(row)

if __name__ == "__main__":
    main()