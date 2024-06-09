import socket

def send_http_request(server, port, path, headers):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server, port))

            request = f"GET {path} HTTP/1.1\r\n"
            for header, value in headers.items():
                request += f"{header}: {value}\r\n"
            request += "\r\n"

            client_socket.sendall(request.encode())

            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data

            headers, body = response.split(b"\r\n\r\n", 1)
            content_type = None
            for header in headers.split(b"\r\n"):
                if header.startswith(b"Content-Type:"):
                    content_type = header.split(b":")[1].strip()
                    break

            if content_type == b"image/png":
                with open("image.png", "wb") as file:
                    file.write(body)

                print("Image saved as image.png")
            else:
                print("Unexpected content type received:", content_type.decode())

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "httpbin.org"
    port = 80
    path = "/image/png"
    headers = {
        "Host": server,
        "Accept": "image/png"
    }
    send_http_request(server, port, path, headers)