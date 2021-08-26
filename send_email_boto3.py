'''
Since we don't want to pass in credentials directly into code, follow these instructions:
Configure Credentials: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
Code referenced from here: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html
'''

import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

load_dotenv() # load environment variables containing credentials
SENDER = "timothy.simanhadi@state.ca.gov"
RECIPIENT = ["timfsim@gmail.com", "tsimanha@uci.edu"]
AWS_REGION = "us-west-1"
SUBJECT = "Customer service contact info"
ATTACHMENT = r"C:\Users\timfs\Desktop\eVAQ-reference-automation\eVAQs\eVAQ 0001113\eVAQ 0001113 Reference #1.docx"
BODY_TEXT = "Hello,\r\nPlease see the attached file for a list of customers to contact."
BODY_HTML = """\
<html>
<head></head>
<body>
<h1>Hello!</h1>
<p>Please see the attached file for a list of customers to contact.</p>
</body>
</html>
"""
CHARSET = "utf-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Create a multipart/mixed parent container.
msg = MIMEMultipart('mixed')
# Add subject, from and to lines.
msg['Subject'] = SUBJECT 
msg['From'] = SENDER 
msg['To'] = ", ".join(RECIPIENT)

# Create a multipart/alternative child container.
msg_body = MIMEMultipart('alternative')

# Encode the text and HTML content and set the character encoding. This step is
# necessary if you're sending a message with characters outside the ASCII range.
textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

# Add the text and HTML parts to the child container.
msg_body.attach(textpart)
msg_body.attach(htmlpart)

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
        Destinations=RECIPIENT,
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