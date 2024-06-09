import socket


hex_data = ("ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e")

datagram = bytes.fromhex(hex_data)

src_port = int.from_bytes(datagram[0:2], byteorder='big')
dst_port = int.from_bytes(datagram[2:4], byteorder='big')
data = datagram[8:]

data_length = len(data)

data_str = data.decode('utf-8')

result = f"zad14odp;src;{src_port};dst;{dst_port};data;{data_str}"

server_addr = ('212.182.24.27', 2910)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(result.encode(), server_addr)

response, _ = sock.recvfrom(4096)
print("Response: ", response.decode())

sock.close()