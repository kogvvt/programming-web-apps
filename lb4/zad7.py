import socket

def client(server_ip, server_port, message):
    try:
        if len(message) > 20:
            message = message[:20]
        else:
            message = message.ljust(20)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))        
        client_socket.sendall(message.encode())
        
        response = client_socket.recv(20)
        
        print("Server response:", response.decode().strip())
        
        client_socket.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2900
    message = "Hello test test test test test"
    client(server_ip, server_port, message)