import socket               # Import socket module
from private_sender import send_file_to_public

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
file_name = 'test_private.txt'
f = open(file_name,'wb')
s.listen(5)                 # Now wait for client connection.

while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    if 'put' in l.split('--->')[1]:
        while (l):
            print "Receiving..."
            f.write(l)
            l = c.recv(1024)
        #send_file_to_public(file_name)
        f.close()
        send_file_to_public(file_name)
        print "Done Receiving"
        c.send('Thank you for connecting')
        c.close()                # Close the connection
    if 'get' in l.split('--->')[1]:
        print 'download_request'
