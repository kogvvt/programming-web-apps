import socket

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def start(self):
        self.server_socket.listen(1)
        print(f"SMTP server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        client_socket.sendall(b"220 Welcome to the SMTP server\r\n")
        while True:
            request = client_socket.recv(1024).decode().strip()
            if not request:
                break

            if request.startswith("HELO") or request.startswith("EHLO"):
                client_socket.sendall(b"250 Hello\r\n")
            elif request.startswith("MAIL FROM"):
                client_socket.sendall(b"250 Sender OK\r\n")
            elif request.startswith("RCPT TO"):
                client_socket.sendall(b"250 Recipient OK\r\n")
            elif request.startswith("DATA"):
                client_socket.sendall(b"354 Start mail input; end with <CRLF>.<CRLF>\r\n")
                client_socket.recv(1024)  
                client_socket.sendall(b"250 Message accepted for delivery\r\n")
            elif request.startswith("QUIT"):
                client_socket.sendall(b"221 Bye\r\n")
                break
            else:
                client_socket.sendall(b"500 Command not recognized\r\n")

        client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 25
    server = SMTPServer(HOST, PORT)
    server.start()