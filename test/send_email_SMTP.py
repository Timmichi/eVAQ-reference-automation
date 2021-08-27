'''
1. Go Here to see/create an IAM User: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console 
2. Add user to group that has access to SES (Simple Email Service)
3. Download your Access Key ID and Secret Key. (Create a new one if lost)
4. pip install boto3
5. Follow this tutorial: https://www.youtube.com/watch?v=H0dN0vlyF4M
6. Go here to get code to send emails: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/examples-send-using-smtp.html
'''
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails():
    SENDER = 'timothy.simanhadi@state.ca.gov'  
    SENDERNAME = 'Timothy Simanhadi'
    RECIPIENT  = ['timfsim@gmail.com', 'tsimanha@uci.edu']

    HOST = "email-smtp.us-west-1.amazonaws.com"
    PORT = 587
    USERNAME_SMTP = "smtp_username"
    PASSWORD_SMTP = "smtp_password"
    SUBJECT = 'Amazon SES Test (Python smtplib)'

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test\r\n"
                "This email was sent through the Amazon SES SMTP "
                "Interface using the Python smtplib package."
                )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Amazon SES SMTP Email Test</h1>
    <p>This email was sent with Amazon SES using the
        <a href='https://www.python.org/'>Python</a>
        <a href='https://docs.python.org/3/library/smtplib.html'>
        smtplib</a> library.</p>
    </body>
    </html>
                """

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = ", ".join(RECIPIENT)
    # Comment or delete the next line if you are not using a configuration set
    #msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

    # Record the MIME types of both parts - text/plain and text/html.
    body1 = MIMEText(BODY_TEXT, 'plain')
    body2 = MIMEText(BODY_HTML, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(body1)
    msg.attach(body2)

    # Try to send the message.
    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")

if __name__ == "__main__":
    send_emails()