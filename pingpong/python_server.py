import socket

# family: IPv4 기반 주소 (AF_INET)
# type: 일반적으로 SOCK_STREAM과 SOCK_DGRAM만 유용합니다.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 6543))
server.listen(3) # backlog 3. conn 객체 3개까지만 허용. 초과시 거부

while True:
    conn, addr = server.accept()

    print(conn.getpeername()) # accept 메서드가 반환하는 addr와 같다.
    print(conn.getsockname()) # ('127.0.0.1', 6543)

    data = conn.recv(1024) # bufsize 1024 bytes
    print("server got data:", data, type(data))
    print(f"host {addr[0]}, port {addr[1]}")

    conn.send(data)