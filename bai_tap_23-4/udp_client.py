import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Lò Đức Công:")
    s.sendto(data.encode("utf-8"), ("26.203.147.138", 9090))
    data, addr = s.recvfrom(1024)
    print(data.decode("utf-8"))
    s.close()