import socket

def fetch_all_messages(server, port, username, password):
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

            print("Message content:")
            print(message_content)

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
    fetch_all_messages(server, port, username, password)