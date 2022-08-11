import binascii
import ipaddress
import socket

# ADRESS = '83.69.139.250'

# ip = ipaddress.ip_address(ADRESS)
# ip_network = ipaddress.ip_network(ADRESS)
# print(ip_network)
# print(ip_network.version)
# print(ip.is_private)
# print(int(ip))
hosts = [
    'pyblog.uz',
    'robocode.uz'
]
# for h in hosts:
#     print(f"{h} : {socket.gethostbyname(h)}")

# get host name and ip

# for h in hosts:
#     print(h)
#     try:
#         name, aliases, addresses = socket.gethostbyname_ex(h)
#         print(f"name : {name}\naliases : {aliases}\naddresses : {addresses}")
#     except socket.error as msg:
#         print("ERROR", msg)

# get server name

print(socket.getfqdn(hosts[0]))
