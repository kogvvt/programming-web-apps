import socket
import os
import base64

def save_attachment(server, port, username, password, attachment_dir):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server, port))

        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(f"USER {username}\r\n".encode())
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(f"PASS {password}\r\n".encode())
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(b"LIST\r\n")
        response = client_socket.recv(1024).decode()
        print(response)

        lines = response.split('\r\n')[1:-2]
        for line in lines:
            msg_num, _ = line.split()
            client_socket.sendall(f"RETR {msg_num}\r\n".encode())
            response = client_socket.recv(1024).decode()
            print(response)

            message_content = ""
            while True:
                data = client_socket.recv(1024).decode()
                if data.endswith(".\r\n"):
                    message_content += data[:-3]
                    break
                else:
                    message_content += data

            lines = message_content.split('\r\n')
            attachment_found = False
            attachment_name = None
            attachment_data = None
            for i in range(len(lines)):
                if lines[i].startswith("Content-Disposition: attachment"):
                    attachment_found = True
                    attachment_name = lines[i].split('filename=')[1].strip('"')
                    attachment_data = base64.b64decode(''.join(lines[i+2:-1]))
                    break

            if attachment_found and attachment_name and attachment_data:
                attachment_path = os.path.join(attachment_dir, attachment_name)
                with open(attachment_path, 'wb') as f:
                    f.write(attachment_data)
                print(f"Attachment '{attachment_name}' saved to '{attachment_path}'")
            else:
                print("No attachment found in the message")

        client_socket.sendall(b"QUIT\r\n")
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "interia.pl"
    port = 110
    username = "pas2017@interia.pl"
    password = "P4SInf2017"
    attachment_dir = "attachments"
    if not os.path.exists(attachment_dir):
        os.makedirs(attachment_dir)
    save_attachment(server, port, username, password, attachment_dir)