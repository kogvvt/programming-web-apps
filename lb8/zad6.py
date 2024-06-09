import socket

class IMAPServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.is_running = False

    def start(self):
        self.is_running = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.address, self.port))
            server_socket.listen(1)
            print(f"IMAP Server running on {self.address}:{self.port}")
            while self.is_running:
                conn, addr = server_socket.accept()
                print(f"Connection from {addr}")
                with conn:
                    conn.sendall(b"* OK IMAP4 server ready\r\n")
                    while True:
                        data = conn.recv(1024).decode().strip()
                        if not data:
                            break
                        print(f"Received: {data}")
                        command = data.split()[0]
                        if command == "LOGIN":
                            conn.sendall(b"* OK Login successful\r\n")
                        elif command == "SELECT":
                            conn.sendall(b"* OK [READ-WRITE] Selected mailbox\r\n")
                        elif command == "LIST":
                            conn.sendall(b"* LIST () \"/\" INBOX\r\n")
                        elif command == "FETCH":
                            conn.sendall(b"* FETCH 1 BODY[HEADER] {50}\r\n")
                            conn.sendall(b"From: krystian@poczta.pl\r\nTo: krystian_odb@poczta.pl\r\nSubject: test\r\n\r\n")
                        elif command == "LOGOUT":
                            conn.sendall(b"* BYE Logging out\r\n")
                            break
                        else:
                            conn.sendall(b"BAD Unknown command\r\n")

    def stop(self):
        self.is_running = False

if __name__ == "__main__":
    address = "127.0.0.1"
    port = 143
    server = IMAPServer(address, port)
    server.start()