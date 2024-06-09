import socket

def client(server_ip, server_port, message):
    try:
        max_length = 20
        
        if len(message) < max_length:
            message = message.ljust(max_length)
        
        elif len(message) > max_length:
            message = message[:max_length]
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        
        client_socket.sendall(message.encode())
        
        response = client_socket.recv(max_length)
        
        print("Server response:", response.decode())
        
        client_socket.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2908
    message = "Hello"
    client(server_ip, server_port, message)