import socket

# port -> service
print(socket.getservbyport(80))
print(socket.getservbyport(443))
print(socket.getservbyport(21))
print(socket.getservbyport(990))

# service name -> protocol port number
print(socket.getservbyname('http'))
print(socket.getservbyname('https'))
print(socket.getservbyname('ftp'))
print(socket.getservbyname('ftps'))
print(socket.getservbyname('ssh'))