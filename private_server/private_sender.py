import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '192.168.0.15'
port = 12346                 # Reserve a port for your service.

def send_file_to_public(file_name):
    s.connect((host, port))
    s.send("asdf"+"--->put")
    f = open(file_name,'rb')
    print 'Sending...'
    l = f.read(1024)
    while (l):
        print 'Sending...'
        s.send(l)
        l = f.read(1024)
    # "data------------>key"
    f.close()
    print "Done Sending"
    #print s.recv(1024)
    s.shutdown(socket.SHUT_WR)
    print s.recv(1024)
    s.close                     # Close the socket when done

send_file_to_public('test')


