# Assignment 2
# This is a Client program for simple chat application.


import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8113                # Reserve a port for your service.
msg1 = ''
s.connect((host, port))
#s.send('Hello World')
while True:
	msg = raw_input('Enter Message')
	s.send(msg)
	msg1 = s.recv(1024)
	print msg1
	if msg1 == 'end':
		quit()
s.close
