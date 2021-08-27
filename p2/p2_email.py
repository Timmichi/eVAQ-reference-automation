'''
Since we don't want to pass in credentials directly into code, follow these instructions:
Configure Credentials: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
Code referenced from here: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html
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
import html_body 

def p2_send_email(tup):
    load_dotenv() # load environment variables containing credentials
    DATE = "8/23/2021"
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


    img_dir = ".\\p2\\images\\" # Enter Directory of all images  
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
    #print(msg)
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
        print("Email sent! Message ID:"),
        print(response['MessageId'])

if __name__ == "__main__":
    Data = namedtuple('Data', 'Index eVAQ ref name title phone email_address project_title attachment_path vendor_name')
    data_tup = Data(Index='3', eVAQ='0001113', ref='3', name='Amy Roman', title='Speech Language Pathologist', phone='415-518-0592', email_address='timfsim@gmail.com', project_title='Cabling', attachment_path='C:\\Users\\timfs\\Desktop\\eVAQ-reference-automation\\eVAQs\\eVAQ 0001113\\eVAQ 0001113 Reference #3.docx', vendor_name='Smartbox Assistive Technologies, Inc.')
    p2_send_email(data_tup)