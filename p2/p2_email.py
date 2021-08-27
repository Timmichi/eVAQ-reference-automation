'''
Since we don't want to pass in credentials directly into code, follow these instructions:
Configure Credentials: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
Code referenced from here: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html
Information on importing bewteen modules: https://stackoverflow.com/questions/47319423/import-a-module-from-both-within-same-package-and-from-outside-the-package-in-py
'''

import os, boto3, glob, mimetypes
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.utils import make_msgid
from dotenv import load_dotenv
from collections import namedtuple
from . import html_body # same as writing "from p2" but saves the refactoring if we move the file out of the package
from business.calendar import Calendar
from datetime import date

# Create Calendar object
calendar = Calendar(
  working_days=["monday", "tuesday", "wednesday", "thursday", "friday"],
  # array items are either parseable date strings, or real datetime.date objects
  holidays=["September 6th, 2021", "November 11th, 2021", "November 25 2021", "November 26 2021", "December 25 2021"], # state holidays 2021
  extra_working_dates=[],)

# Helper Function
def get_first_check_date():
    today = date.today()
    start_date = Calendar.parse_date(today)
    due_date = calendar.add_business_days(start_date, 3).strftime("%m/%d/%y")
    return due_date

def p2_send_email(tup):
    load_dotenv() # load environment variables containing credentials
    DATE = get_first_check_date()
    SENDER_NAME = "Timothy Simanhadi"
    SENDER = f"{SENDER_NAME} <timothy.simanhadi@state.ca.gov>"
    RECIPIENT = tup.email_address
    AWS_REGION = "us-west-1"
    SUBJECT = f"eVAQ Reference for {tup.vendor_name}"
    ATTACHMENT = tup.attachment_path
    BODY_TEXT = f'''\
    Hi {tup.name},

    I am {SENDER_NAME} from the California Department of Technology (CDT) and I am contacting you for a reference check for {tup.vendor_name} because this vendor has listed you as a reference for their eVAQ application with CDT. I have attached a one-page questionnaire for your review and comment. Could you please provide your answers to me so that I may have your reference on file for this vendor?  

    At the top of the attached questionnaire is {tup.vendor_name}’s information that they provided for their contract with your organization.  Question #1 is a verification that all of this information is correct which would give them a Pass rating.  If this information were incorrect, then they would receive a Fail rating.  The next 6 questions are explained in the attachment.  If you could return this questionnaire to me by {DATE}, it would be greatly appreciated.  Please let me know if you have any questions regarding this matter.
    '''
    BODY_HTML = html_body.format_html(tup, SENDER, DATE)
    CHARSET = "utf-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT 
    msg['From'] = SENDER 
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML, 'html')

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)


    img_dir = ".\\images" # Enter Directory of all images. Depending on which directory we run the script in our terminal, this "." is relative to that. E.g. if we run script from "C:\Users\timfs\Desktop\WORK\eVAQ-reference-automation", script will run from "." as the home directory.
    data_path = os.path.join(img_dir,'*g') 
    files = glob.glob(data_path) 
    names = ["blog_img", "facebook_img", "line_img", "logo_img", "twitter_img", "youtube_img"]
    for index, f1 in enumerate(files): 
        with open(f1, "rb") as f: 
            msg_image = MIMEImage(f.read())
            # Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
            msg_image.add_header('Content-ID', f'<{names[index]}>')
            msg_body.attach(msg_image)

    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    # Add the attachment to the parent container.
    msg.attach(att)
    try:
        #Provide the contents of the email.
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=[RECIPIENT],
            RawMessage={
                'Data':msg.as_string(),
            },
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email sent for eVAQ #{tup.eVAQ} Ref #{tup.ref}, {tup.name}, at {tup.email_address}! 📧 🎯"),
        # print(response['MessageId'])

if __name__ == "__main__":
    # to test this module, go to the main project directory "C:\Users\timfs\Desktop\WORK\eVAQ-reference-automation" and run python -m p2.p2_email
    # We go up to the main project so that the p2 package is in the SEARCH PATH. This allows us to have the other modules in the p2 package in the search path which allows us to properly import or reference it when we run THIS script. 
    # In our main project, we can run our (main.py) script with no problem since we are referencing the specific package (absolute or relatively) for the imports in THIS module. Thus, there is no confusion in our main.py script where we are importing certain modules as everything is referenced properly (not ambiguously like "import html_body"). Doing an import without specifying the package (absolutely or relatively) is ONLY okay if we are in the main script as it will grab the closest module in the search path with the same name. Note, that this is also NOT recommended UNLESS the main.py script and the other module we are importing are on the SAME LEVEL.
    Data = namedtuple('Data', 'Index eVAQ ref name title phone email_address project_title attachment_path vendor_name')
    data_tup = Data(Index='1', eVAQ='0000000', ref='1', name='John Smith', title='Software Engineer', phone='123-456-7891', email_address='timfsim@gmail.com', project_title='Website Remediation', attachment_path='.\\test\\eVAQ 0000000\\eVAQ 0000000.pdf', vendor_name='Timothy Technologies, Inc.')
    p2_send_email(data_tup)