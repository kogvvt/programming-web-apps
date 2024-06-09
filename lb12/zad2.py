import socket
import threading
import logging
from datetime import datetime

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def handle_client(client_socket, client_address):
    logging.info(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()

def echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    logging.info(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 12345

    echo_server(server_host, server_port)