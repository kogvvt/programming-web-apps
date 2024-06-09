import socket
import base64
import ssl

def send_email():
    sender = input("Enter sender's email address: ")
    recipient = input("Enter recipient's email address (you can enter multiple addresses, separated by commas): ").split(',')
    subject = input("Enter the subject of the email: ")
    message_body = input("Enter the message body: ")
    attachment_path = input("Enter the path to the attachment file (if no attachments, leave empty): ")

    email_message = ""
    email_message += f"From: {sender}\r\n"
    email_message += f"To: {recipient}\r\n"
    email_message += f"Subject: {subject}\r\n"
    email_message += "MIME-Version: 1.0\r\n"
    email_message += "Content-Type: multipart/mixed; boundary=boundary\r\n\r\n"
    email_message += "--boundary\r\n"
    email_message += f"Content-Type: text/plain\r\n\r\n{message_body}\r\n\r\n"

    with open(attachment_path, "rb") as file:
        attachment_data = file.read()

    encoded_attachment = base64.b64encode(attachment_data).decode()
    email_message += "--boundary\r\n"
    email_message += f"Content-Type: application/octet-stream; name=\"{attachment_path}\"\r\n"
    email_message += "Content-Transfer-Encoding: base64\r\n"
    email_message += f"Content-Disposition: attachment; filename=\"{attachment_path}\"\r\n\r\n"
    email_message += encoded_attachment + "\r\n"
    email_message += "--boundary--\r\n"

    try:
        context = ssl.create_default_context()
        client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        client_socket.connect(("interia.pl", 587))
        response = client_socket.recv(1024).decode()

        client_socket.sendall(b"HELO krystian\r\n")
        client_socket.recv(1024)
        client_socket.sendall(f"MAIL FROM: <{sender}>\r\n".encode())
        client_socket.recv(1024)
        client_socket.sendall(f"RCPT TO: <{recipient}>\r\n".encode())
        client_socket.recv(1024)
        client_socket.sendall(b"DATA\r\n")
        client_socket.recv(1024)
        client_socket.sendall(email_message.encode())

        client_socket.sendall(b"\r\n.\r\n")
        response = client_socket.recv(1024).decode()

        if "250" in response:
            print("The email has been sent successfully!")
        else:
            print("An error occurred while sending the email.")

        client_socket.sendall(b"QUIT\r\n")
        client_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    send_email()