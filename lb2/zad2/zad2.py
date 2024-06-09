import socket

def client(server_ip, server_port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        
        client_socket.sendall(message.encode())
        
        response = client_socket.recv(1024)
        
        print("Server response:", response.decode())
        
        client_socket.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2900
    message = "Henlo :333"
    client(server_ip, server_port, message)