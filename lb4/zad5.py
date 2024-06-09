import socket

def resolve_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "Hostname not found"
    except Exception as e:
        return f"Error: {e}"

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        ip_address = data.decode()
        print(f"Received ip address from {client_address}: {ip_address}")

        hostname = resolve_hostname(ip_address)
        print(f"Resolved hostname: {hostname}")

        server_socket.sendto(hostname.encode(), client_address)
        print(f"Hostname sent to {client_address}: {hostname}")

if __name__ == "__main__":
    start_server()