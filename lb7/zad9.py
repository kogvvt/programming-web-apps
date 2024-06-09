import socket

def get_largest_mail(server, port, username, password):
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
        max_size = 0
        max_size_msg_num = None
        for line in lines:
            msg_num, size = line.split()
            size = int(size)
            if size > max_size:
                max_size = size
                max_size_msg_num = msg_num

        if max_size_msg_num:
            client_socket.sendall(f"RETR {max_size_msg_num}\r\n".encode())
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
        else:
            print("No messages found.")

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
    get_largest_mail(server, port, username, password)