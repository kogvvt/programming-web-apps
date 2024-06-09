import socket

hex_data = ("0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29")

segment = bytes.fromhex(hex_data)

src_port = int.from_bytes(segment[0:2], byteorder='big')
dst_port = int.from_bytes(segment[2:4], byteorder='big')

data_offset = (segment[12] >> 4) * 4

data = segment[data_offset:]

data_length = len(data)

data_str = data.decode('utf-8')

result = f"zad13odp;src;{src_port};dst;{dst_port};data;{data_str}"

server_address = ('212.182.24.27', 2909)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(result.encode(), server_address)

response, _ = sock.recvfrom(4096)
print("Odpowiedź od serwera:", response.decode())

sock.close()