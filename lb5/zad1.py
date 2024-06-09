import socket

serverAddress = '212.182.24.236'
serverPort = 2912
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = serverSocket.connect_ex((serverAddress, serverPort))

if result == 0:
    print("It works!")
    message = input()
    serverSocket.send(message.encode('utf-8'))
    data = serverSocket.recv(20)
    print(data.decode('utf-8'))
else:
    print("There is a problem with the connection.")

serverSocket.close