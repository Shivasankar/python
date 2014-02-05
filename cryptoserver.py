#Cryptography programs
# This programs contain error
import socket               # Import socket module
import binascii				#Import binascii module
msg = ''
#emsg = NULL
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8176              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr
	#c.send('Hello World')
	print
	print c.recv(1024).decode()
	#binascii.unhexlify('%x' %dmsg)
	msg = raw_input('Enter Message')
	#emsg = bin(int(binascii.hexlify(msg),16))		#Converting char into encrypted message
	#print 'Encrypted form of message', emsg
	c.send(msg).encode()
	if msg == 'end':
		quit()
	c.close()        
