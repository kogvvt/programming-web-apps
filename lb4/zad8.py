import socket
import sys

def connect_to_server(server_address, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)

        result = client_socket.connect_ex((server_address, server_port))

        if result == 0:
            print(f"Port {server_port} is open.")

            message = "Hello, this is a test"
            message = message.ljust(20)  
            client_socket.sendall(message.encode())

            received_message = b""
            while len(received_message) < 20:
                chunk = client_socket.recv(20 - len(received_message))
                if not chunk:
                    raise RuntimeError("Socket connection broken")
                received_message += chunk
            
            print(f"Service running on port {server_port}: {received_message.decode().strip()}")
        else:
            print(f"Port {server_port} is closed.")
        
        client_socket.close()
    except socket.timeout:
        print(f"Connection to port {server_port} timed out.")
    except ConnectionRefusedError:
        print(f"Connection to port {server_port} unsuccessful. The server may be not available.")
    except socket.gaierror:
        print("Invalid IP address or hostname.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zad8.py <ip_address_or_hostname> <port_number>")
        sys.exit(1)
        
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    connect_to_server(server_address, server_port)