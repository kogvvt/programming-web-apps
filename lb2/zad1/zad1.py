import socket
import struct
import time

def get_ntp_time(server, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        client_socket.sendto(b'\x1b' + 47 * b'\0', (server, port))
        
        data, _ = client_socket.recvfrom(1024)
        
        client_socket.close()
        
        ntp_time = struct.unpack("!12I", data)[10] - 2208988800
        
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ntp_time))
        
        print(f"Date and time (from server {server}:{port}): {local_time}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    server = "ntp.task.gda.pl"
    port = 123
    get_ntp_time(server, port)