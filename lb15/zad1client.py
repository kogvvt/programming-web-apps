import socket

def client_tcp(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            message = input("Enter message to send (or 'quit' to exit): ")

            client_socket.sendall(message.encode())

            if message.lower() == "quit":
                print("Closing connection...")
                break

            response = client_socket.recv(4096).decode()
            print("Received from server:", response)

    except ConnectionRefusedError:
        print(f"Failed to connect to {host}:{port}. Server may be unavailable.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    client_tcp(host, port)