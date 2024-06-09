import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, receivers, subject, message, server, port, password):
    server = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server.sendmail(sender, receivers, msg.as_string())
    print("Email sent successfully")

    server.quit()

if __name__ == "__main__":
    sender = input("Enter sender email address: ")
    receivers = input("Enter receiver email addresses (comma separated): ").split(',')
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")
    server = input("Enter SMTP server address: ")
    port = int(input("Enter port number: "))
    password = input("Enter sender email password: ")

    send_email(sender, receivers, subject, message, server, port, password)