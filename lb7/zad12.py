import socket

class POP3Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.messages = []
        self.is_running = False

    def start(self):
        self.is_running = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.address, self.port))
            server_socket.listen(1)
            print(f"POP3 Server running on {self.address}:{self.port}")
            while self.is_running:
                conn, addr = server_socket.accept()
                print(f"Connection from {addr}")
                with conn:
                    conn.sendall(b"+OK POP3 server ready\r\n")
                    while True:
                        data = conn.recv(1024).decode().strip()
                        if not data:
                            break
                        print(f"Received: {data}")
                        command = data.split()[0]
                        if command == "USER":
                            conn.sendall(b"+OK\r\n")
                        elif command == "PASS":
                            conn.sendall(b"+OK\r\n")
                        elif command == "STAT":
                            conn.sendall(b"+OK 0 0\r\n")
                        elif command == "LIST":
                            conn.sendall(b"+OK\r\n.\r\n")
                        elif command == "RETR":
                            conn.sendall(b"-ERR Message not found\r\n")
                        elif command == "QUIT":
                            conn.sendall(b"+OK Goodbye\r\n")
                            break
                        else:
                            conn.sendall(b"-ERR Unknown command\r\n")

    def stop(self):
        self.is_running = False

if __name__ == "__main__":
    address = "127.0.0.1"
    port = 110
    server = POP3Server(address, port)
    server.start()