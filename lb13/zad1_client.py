import socket
import os

def send_file(file_path, server_host, server_port):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    client_socket.send("UPLOAD".encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    if response != "READY":
        print("Server is not ready to receive file")
        return

    client_socket.send(file_name.encode('utf-8'))
    client_socket.send(str(file_size).encode('utf-8'))

    with open(file_path, 'rb') as f:
        file_data = f.read()
        client_socket.sendall(file_data)

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    client_socket.close()

if __name__ == "__main__":
    file_path = "example.jpg"
    server_host = "127.0.0.1"
    server_port = 12345

    send_file(file_path, server_host, server_port)