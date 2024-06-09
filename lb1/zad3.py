import ipaddress

def check_ip_address(ip):
    try:
        ip_address = ipaddress.ip_address(ip)
        print(f"IP address {ip} is correct.")
    except ValueError:
        print(f"IP address {ip} is incorrect.")

if __name__ == "__main__":
    ip_address_input = input("Enter the IP address: ")
    check_ip_address(ip_address_input)