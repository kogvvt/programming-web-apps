import socket

def client(server_ip, server_port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        server_address = (server_ip, server_port)
        
        client_socket.sendto(message.encode(), server_address)
        
        response, _ = client_socket.recvfrom(1024)
        
        print("Server response:", response.decode())
        
        client_socket.close()
    except Exception as e:
        print(f"Error ocurred: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2901
    message = "Henlo :33"
    client(server_ip, server_port, message)