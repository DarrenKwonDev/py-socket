import socket

# family: IPv4 기반 주소 (AF_INET)
# type: 일반적으로 SOCK_STREAM과 SOCK_DGRAM만 유용합니다.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 6543))
client.send(b'Hello, world!')

print(client.recv(1024))
