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

            html_content = response.split(b"\r\n\r\n", 1)[1]

            with open("page.html", "wb") as file:
                file.write(html_content)

            print("Page saved as page.html")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server = "httpbin.org"
    port = 80
    path = "/html"
    headers = {
        "Host": server,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Safari/7.0.3"
    }
    send_http_request(server, port, path, headers)