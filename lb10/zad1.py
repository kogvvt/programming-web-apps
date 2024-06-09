import socket

server_address = ('echo.websocket.events', 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    handshake_request = (
        "GET /chat HTTP/1.1\r\n"
        "Host: %s:%s\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r\n"
        "Origin: http://example.com"
        "Sec-WebSocket-Protocol: chat"
        "Sec-WebSocket-Version: 13\r\n"
        )
    sock.send(handshake_request)

    handshake_response = sock.recv(4096)
    print('Response: ', handshake_response)
except Exception as e:
    print("Error!: ", e)
finally:
    sock.close()
