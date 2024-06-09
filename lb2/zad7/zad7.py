import socket
import sys

def connect_to_server(server_address, server_port):
    try:
        service_info = None
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socket.settimeout(1)
        
        result = client_socket.connect_ex((server_address, server_port))
        
        if result == 0:
            print(f"Port {server_port} is open.")
            service_info = client_socket.recv(1024)
            print(f"Service running on port {server_port}: {service_info.decode()}")
        else:
            print(f"Port {server_port} is closed.")
        
        client_socket.close()
    except socket.timeout:
        print(f"Connection to port {server_port} timed out.")
    except ConnectionRefusedError:
        print(f"Connection to port {server_port} unsuccessful. The server may be not available.")
    except socket.gaierror:
        print("Invalid IP address or hostname.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zad7.py <ip_address_or_hostname> <port_number>")
        sys.exit(1)
        
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    connect_to_server(server_address, server_port)