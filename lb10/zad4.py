import socket

def handle_client(client_socket):

    while True:
        frame = client_socket.recv(1024)
        if not frame:
            break

        print("Received message:", frame)

        # Echoing the received message back to the client
        client_socket.send(frame)

    client_socket.close()


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening on", host, "port", port)

    while True:
        client_socket, address = server_socket.accept()
        print("Accepted connection from", address)
        handle_client(client_socket)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    start_server(host, port)