import socket

def send_email():
    sender = input("Enter sender's email address: ")
    recipient = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    message_body = input("Enter email message (use HTML tags for formatting): ")

    email_message = f"From: {sender}\r\n"
    email_message += f"To: {recipient}\r\n"
    email_message += f"Subject: {subject}\r\n"
    email_message += "MIME-Version: 1.0\r\n"
    email_message += "Content-Type: text/html\r\n\r\n"
    email_message += f"{message_body}\r\n"

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print("Email sent successfully!")
        else:
            print("An error occurred while sending the email.")

        client_socket.sendall(b"QUIT\r\n")
        client_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    send_email()