import socket
import random

def generate_random_number():
    return random.randint(1, 100)

def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    random_number = generate_random_number()

    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode('utf-8')

        try:
            guess = int(data)
            if guess < random_number:
                response = "Your guess is too low!"
            elif guess == random_number:
                response = "Congratulations! You guessed the number!"
                client_socket.send(response.encode('utf-8'))
                client_socket.close()
                break
            else:
                response = "Your guess is too high!"
        except ValueError:
            response = "Error: Please send only numbers!"

        client_socket.send(response.encode('utf-8'))

    server_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 12345

    server(server_host, server_port)