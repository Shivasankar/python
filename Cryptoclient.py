import socket               # Import socket module
import binascii
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8176                # Reserve a port for your service.
msg1 = ''
s.connect((host, port))
#s.send('Hello World')
while True:
	msg = raw_input('Enter Message')
	#emsg = bin(int(binascii.hexlify(msg)))
	#print 'Encrypted form of message', emsg
	s.send(msg).encode()
	print s.recv(1024).decode()
	#binascii.unhexlify('%x' %dmsg)	
	if msg1 == 'end':
		quit()
s.close          
