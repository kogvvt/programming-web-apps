import socket

def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 3:
            return "Bad expression!"

        num1, operator, num2 = parts
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error! : cannot divide by zero!"
            result = num1 / num2
        else:
            return "Wrong operator"

        return str(result)
    except Exception as e:
        return f"Error: {e}"

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Calculator server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        expression = data.decode()
        print(f"Expression received from {client_address}: {expression}")

        # Obliczenie wyniku wyrażenia
        result = calculate(expression)
        print(f"Calculation result: {result}")

        # Odesłanie wyniku do klienta
        server_socket.sendto(result.encode(), client_address)
        print(f"Result sent to {client_address}: {result}")

if __name__ == "__main__":
    start_server()