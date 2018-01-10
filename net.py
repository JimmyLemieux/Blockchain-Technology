import socket
import hashlib
import threading
import logging

net_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostDetails = ('localhost',3456)
net_socket.bind(hostDetails)
net_socket.listen(5)
print 'The server is now online'

connection, address = net_socket.accept()
print 'A client has now logged into the network'

while __name__ == '__main__':
	receive = connection.recv(1)
	print receive
	if not receive:break

