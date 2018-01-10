import socket
import logging

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	client_socket.connect('localhost',3456)
	print 'The connection has been made'
	client_socket.sendall('This is the text')
except:
	print 'Connection Failed'
	print 'There is no connection because this is over ethernet?'