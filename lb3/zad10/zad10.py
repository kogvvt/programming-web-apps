import socket

def client(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        hostname = socket.gethostname()
        
        client_socket.sendto(hostname.encode(), (server_ip, server_port))
        
        response, _ = client_socket.recvfrom(1024)
        
        print("Server response:", response.decode())
        
        client_socket.close()
    except Exception as e:
        print(f"Error ocurred: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2907
    client(server_ip, server_port)