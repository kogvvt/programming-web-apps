import socket
from datetime import datetime

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")

    while True:
        
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
           
            message = client_socket.recv(1024).decode()
            print(f"Message received: {message}")

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            client_socket.sendall(current_time.encode())
            print(f"Date and time sent: {current_time}")
        except Exception as e:
            print(f"Error! : {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()