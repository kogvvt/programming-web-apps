import socket

def tcp_client_no_verification(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        while True:
            message = input("Enter message to send (type 'quit' to exit): ")

            if message.lower() == 'quit':
                break

            client_socket.sendall(message.encode())

            response = client_socket.recv(4096).decode()
            print(f"Received response from server: {response}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    host = "212.182.24.27"
    port = 29443
    tcp_client_no_verification(host, port)