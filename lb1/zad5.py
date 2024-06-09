import socket
import sys

def get_ip_address(hostname):
    try:
        ip_addresses = socket.gethostbyname_ex(hostname)[-1]
        for ip_address in ip_addresses:
            print(f"IP address for hostname {hostname} is: {ip_address}")
    except socket.gaierror:
        print(f"Cannot find IP address for hostname {hostname}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python zad5.py <hostname>")
        sys.exit(1)
        
    hostname = sys.argv[1]
    get_ip_address(hostname)