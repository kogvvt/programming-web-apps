import socket

def check_mail_count(server, port, username, password):
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

        client_socket.sendall(b"STAT\r\n")
        response = client_socket.recv(1024).decode()
        print(response)

        mail_count = response.split()[1]
        print(f"Number of messages in the mailbox: {mail_count}")

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
    check_mail_count(server, port, username, password)