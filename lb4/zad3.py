import socket

def start_echo_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Echo server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Data received from {client_address}: {data.decode()}")
        server_socket.sendto(data, client_address)
        print(f"Data sent to {client_address}: {data.decode()}")

if __name__ == "__main__":
    start_echo_server()