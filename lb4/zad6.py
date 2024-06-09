import socket

def resolve_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "IP not found"
    except Exception as e:
        return f"Error: {e}"

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        hostname = data.decode()
        print(f"Host name received from {client_address}: {hostname}")

        ip_address = resolve_ip_address(hostname)
        print(f"Resolved IP address: {ip_address}")

        server_socket.sendto(ip_address.encode(), client_address)
        print(f"Sent IP address to: {client_address}: {ip_address}")

if __name__ == "__main__":
    start_server()