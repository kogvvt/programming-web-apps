import socket
import os

def save_file(file_data, file_name):
    with open(file_name, 'wb') as f:
        f.write(file_data)

def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    if request != "UPLOAD":
        client_socket.send("Error: Invalid protocol command".encode('utf-8'))
        return

    client_socket.send("READY".encode('utf-8'))

    file_name = client_socket.recv(1024).decode('utf-8')
    file_size = int(client_socket.recv(1024).decode('utf-8'))

    file_data = client_socket.recv(file_size)
    save_file(file_data, file_name)

    client_socket.send("File uploaded successfully".encode('utf-8'))

def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        handle_client_connection(client_socket)
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 12345

    server(server_host, server_port)