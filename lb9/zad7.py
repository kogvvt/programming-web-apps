import socket

def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode()
    try:
        path = request_data.split()[1]
    except IndexError:
        path = "/"
    if path == "/":
        file_path = "examples/index.html"
        status_line = "HTTP/1.1 200 OK\r\n"
    else:
        file_path = "examples/404.html"
        status_line = "HTTP/1.1 404 Not Found\r\n"
    try:
        with open(file_path, "rb") as file:
            content = file.read()
    except FileNotFoundError:
        status_line = "HTTP/1.1 404 Not Found\r\n"
        content = b"<h1>404 Not Found</h1>"
    response = status_line.encode() + b"\r\n" + content
    client_socket.sendall(response)
    client_socket.close()

def start_server(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((address, port))
        server_socket.listen()
        print(f"Server is listening on {address}:{port}")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            handle_client(client_socket)

if __name__ == "__main__":
    ADDRESS = "127.0.0.1"
    PORT = 8080
    start_server(ADDRESS, PORT)