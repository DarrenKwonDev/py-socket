import socket

# family: IPv4 기반 주소 (AF_INET)
# type: 일반적으로 SOCK_STREAM과 SOCK_DGRAM만 유용합니다.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 6543))
server.listen()

conn, addr = server.accept()

data = conn.recv(1024) # bufsize 1024 bytes
print("server got data:", data)

conn.send(data)