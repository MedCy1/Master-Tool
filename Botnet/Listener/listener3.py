from socket import *
import _thread
import queue

SEND_FILE_BUFFER = 5120 #5kb
HOST = '127.0.0.1'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(2)

while 1:
    print ("waiting on connection")
    clientsock, addr = serversock.accept()
    print ('connected from:', addr)
    while 1:
        data = clientsock.recv(1024).decode()
        if not data: break 
        clientsock.send(data.encode())
        clientsock.close()
    clientsock.close()

##########  ACTIONS  ##########

def SendFile(self, path):
    f = open(path, 'r')
    while f:
        data = f.read(SEND_FILE_BUFFER)
        self.sock.send(data)
    f.close    

if __name__ == "__main__":
    in_ = queue.Queue()
    out_ = queue.Queue()
