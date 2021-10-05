from sys import argv
import socket

if len(argv) != 3:
    print("usage python3 smtp_vry <IP> <file-name>")
    exit(0)
    
print("\n\n##########################################\n\n")

target = argv[1]
users = open(argv[2], "r").read().splitlines()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection = s.connect((target, 25))

banner = s.recv(2048)

print(banner.decode())

print("\n##########################################\n\n")

for user in users :
    statment = "VRFY " + user + "\r\n"
    s.send(statment.encode())
    result = s.recv(1024)
    print(result.decode())