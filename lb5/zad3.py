import socket
import time

def knock_ports(ip, ports):
    for port in ports:
        print(f"Knocking on port {port}...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(b'PING', (ip, port))
        response, _ = client_socket.recvfrom(1024)
        if response == b'PONG':
            print(f"Port {port} knocked successfully!")
        else:
            print(f"Port {port} did not respond correctly.")
        client_socket.close()

def main():
    target_ip = '212.182.24.27'
    target_tcp_port = 2913
    udp_sequence = [1111, 2222, 3333, 4444] 

    knock_ports(target_ip, udp_sequence)
    time.sleep(10)

    try:
        print(f"Trying to connect to TCP port {target_tcp_port}...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_tcp_port))
        message = client_socket.recv(1024)
        print("Received message from server:", message.decode())
        client_socket.close()
    except Exception as e:
        print("Failed to connect to TCP port:", e)

if __name__ == "__main__":
    main()