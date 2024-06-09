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
        
        total_sent = 0
        while total_sent < max_length:
            sent = client_socket.send(message[total_sent:].encode())
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            total_sent += sent
        
        response = b''
        total_received = 0
        while total_received < max_length:
            chunk = client_socket.recv(max_length - total_received)
            if len(chunk) == 0:
                raise RuntimeError("Socket connection broken")
            response += chunk
            total_received += len(chunk)
        
        print("Server response:", response.decode())
        
        client_socket.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    server_ip = "212.182.24.27"
    server_port = 2908
    message = "Hello"
    client(server_ip, server_port, message)