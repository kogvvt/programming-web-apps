from random import randint
import socket, select

HOST= '127.0.0.1'
PORT = 2912

connectedClientSockets = []

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(10)

connectedClientSockets.append(serverSocket)
randNumber = randint(1, 100)

while True:
    inputSockets, outputSockets, errSockets = select.select(connectedClientSockets, [], [])
    
    for sock in inputSockets:
        if sock == serverSocket:
            
            sockfd, clientAddress = serverSocket.accept()
            connectedClientSockets.append(sockfd)
            print("Client connected!\n")
        else:
            try:
                clientData = sock.recv(1024).decode('utf-8')
                if clientData:
                    
                    try:
                        userInput = int(clientData)
                        if userInput == randNumber:
                            randNumber = randint(1, 100)
                            msg = "You did it!"
                            sock.sendAll(msg.encode('utf-8'))
                              
                        elif userInput < randNumber:
                            msg = "Try bigger!"
                            sock.sendAll(msg.encode('utf-8'))
                            
                        elif userInput > randNumber:
                            msg = "Try smaller!"
                            sock.sendAll(msg.encode('utf-8'))
                            
                    except Exception as e:
                        msg = "wrong type! %s" % e
                        sock.sendAll(msg.encode('utf-8'))
            except:
                print("Client is offline")
                sock.close()
                connectedClientSockets.remove(sock)
                continue
                            
serverSocket.close()    
                            