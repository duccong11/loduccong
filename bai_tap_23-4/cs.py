import socket
s = socket.socket()
host = '26.203.147.138'
port = 6666
s.connect((host, port)) 
s.send('Lò Đức Công'.encode())   
s.close()