import socket
import sys

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(f"Hostname for IP {ip_address} is: {hostname[0]}")
    except socket.herror:
        print(f"Cannot find a hostname for IP address {ip_address}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python zad4.py <ip_address>")
        sys.exit(1)
        
    ip_address = sys.argv[1]
    get_hostname(ip_address)