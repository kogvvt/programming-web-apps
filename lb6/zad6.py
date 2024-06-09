import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    sender = input("Sender e-mail: ")
    recipient = input("Enter recipients email addresses separated by comma: ").split(',')
    subject = input("Enter email subject: ")
    message_body = input("Enter email message: ")
    attachment_path = input("Enter attachment filename path (if no attachments, leave empty): ")

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    message.attach(MIMEText(message_body, 'plain'))

    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + attachment_path.split('/')[-1])
        message.attach(part)

    try:
        server = smtplib.SMTP('interia.pl', 587)
        server.starttls()
        server.login(sender, input("Enter e-mail password: "))
        text = message.as_string()
        server.sendmail(sender, recipient.split(','), text)
        print("E-mail sent!")
        server.quit()
    except Exception as e:
        print("Error ocurred when sending message: ", e)

if __name__ == "__main__":
    send_email()