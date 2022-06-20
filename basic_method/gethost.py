import socket

'''
FQDN
'''
# fully qualified domain name (FQDN)
print(socket.getfqdn()) # localhost name

# 만약 그대로 나온다면 자체 서버일 가능성 높음.
# In case no fully qualified domain name is available and name was provided, it is returned unchanged.
print(socket.getfqdn('typed.do'))
print(socket.getfqdn('kbs.co.kr'))
print(socket.getfqdn('cineps.net'))
print(socket.getfqdn('naver.com'))
print(socket.getfqdn('mysnu.ac.kr'))
print(socket.getfqdn('142.250.207.110'))

'''
ip 주소 반환
'''
print(socket.gethostbyname('typed.do'))
print(socket.gethostbyname('mysnu.ac.kr'))

print(socket.gethostbyname(socket.getfqdn())) # localhost의 fqdn의 ip 주소를 가져와

'''
gethostname
'''
print(socket.gethostname())


'''
getprotobyname
'''
# https://docs.python.org/ko/3/library/socket.html#socket.getprotobyname
print(socket.getprotobyname('tcp'))
print(socket.getprotobyname('udp'))
print(socket.getprotobyname('ip'))
print(socket.getprotobyname('icmp'))

# 응용
sock = socket.socket(proto=socket.getprotobyname('tcp'))