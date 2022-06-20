from pydoc import cli
import socket

# family: IPv4 기반 주소 (AF_INET)
# type: 일반적으로 SOCK_STREAM과 SOCK_DGRAM만 유용합니다.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 6543))
client.send('한글이다'.encode('utf-8'))
client.send(b'this is english')

print(client.recv(1024))
