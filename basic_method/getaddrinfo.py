import socket

# https://docs.python.org/ko/3/library/socket.html#socket.getaddrinfo
# host/port 인자를 해당 서비스에 연결된 소켓을 만드는 데 필요한 모든 인자가 들어있는 5-튜플의 시퀀스로 변환합니다.
'''
(family, type, proto, canonname, sockaddr)
'''
all_addrlist = socket.getaddrinfo('typed.do', 80)
filtered_addrlist = socket.getaddrinfo('typed.do', 80, socket.AF_INET)

print(filtered_addrlist)

sock = socket.socket(*all_addrlist[0][:2])
print(sock)