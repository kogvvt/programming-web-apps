import socket

def non_blocking_echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")
    client_sockets = {}

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")
            client_sockets[client_socket] = client_address
        except BlockingIOError:
            pass

        for client_socket in list(client_sockets.keys()):
            try:
                message = client_socket.recv(4096).decode()
                if message:
                    print(f"Received message from {client_sockets[client_socket]}: {message}")
                    client_socket.sendall(message.encode())
                else:
                    print(f"Connection closed by {client_sockets[client_socket]}")
                    del client_sockets[client_socket]
                    client_socket.close()
            except BlockingIOError:
                pass

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    non_blocking_echo_server(host, port)