import socket

def start_echo_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Echo server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            data = client_socket.recv(1024)
            if data:
                print(f"Data received: {data.decode()}")
                client_socket.sendall(data)
                print(f"Data sent: {data.decode()}")
        except Exception as e:
            print(f"Error! : {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_echo_server()