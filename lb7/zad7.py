import socket

def check_mail_size(server, port, username, password):
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
        total_size = 0
        for line in lines:
            _, size = line.split()
            total_size += int(size)

        print(f"Total size of messages in the mailbox: {total_size} bytes")

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
    check_mail_size(server, port, username, password)