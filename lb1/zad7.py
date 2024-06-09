import socket
import sys

def scan_ports(server_address):
    try:
        server_ip = socket.gethostbyname(server_address)
        print(f"Scanning open ports for host: {server_address} ({server_ip})")
        
        for port in range(1, 65536):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(0.1) 
            
            result = client_socket.connect_ex((server_ip, port))
            if result == 0:
                print(f"Port {port} is opened.")

            client_socket.close()
    except socket.gaierror:
        print("Invalid IP or hostname.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python zad7.py <ip_address_or_hostname>")
        sys.exit(1)
        
    server_address = sys.argv[1]
    scan_ports(server_address)