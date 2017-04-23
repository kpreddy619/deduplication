#_________________
'''
to do :-
collect user input
send file name to server
send option to server
handle socket error
receive file from server
'''
'''
socket numbers
private receiver - 12345
'''
#_________________
import socket 
import errno
import sys
import os
import ntpath

class ClientCli(object):

    def __init__(self):
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.private_port = 12345

    def get_file_name(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def set_connection(self):
        try:
            self.sock.connect((self.host, self.private_port))
        except socket.error, v:
            errorcode=v[0]
            if errorcode==errno.ECONNREFUSED:
                print "Connection Refused to private server"
                sys.exit()

    def get_args(self):
        while True:
            print 'Select operation to perform'
            print '___________________________'
            print '\n1.Upload\n2.Download\n3.Quit'
            print '___________________________'
            opt = ''
            while opt not in ['1','2','3']:
                opt = raw_input('Select an option: ')
            if opt == '1':
                self.put_file()
                break
            elif opt == '2':
                self.get_file()
                break
            else:
                print 'Exiting cli...'
                sys.exit()

    def put_file(self):
        file_path = raw_input('Provide absolute path of file to upload: ')
        if not os.path.isfile(file_path):
            print 'File {filename} does not exist'.format(filename=file_path)
        name = self.get_file_name(file_path)
        
        # send file name and arg type
        # 
        self.sock.send(name+'--->get')
        

    def get_file(self):
        pass

obj = ClientCli()
obj.set_connection()
obj.get_args()
'''

#s.send("Hello server!")
f = open('test.txt','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close                     # Close the socket when done
'''
