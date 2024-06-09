import socket
import sys

def connect_to_server(server_address, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socket.connect((server_address, server_port))
        print("Connected to server.")
        
        client_socket.close()
    except ConnectionRefusedError:
        print("Connection unsuccessful. The server can be not avaliable.")
    except socket.gaierror:
        print("Invalid IP address or hostname.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zad6.py <ip_address_or_hostname> <port_number>")
        sys.exit(1)
        
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    connect_to_server(server_address, server_port)