import socket
from unittest.mock import DEFAULT


DEFAULT_BUFFER = 1024


class COMMUNICATOR:
    def __init__(self, sock):
        self.sock = sock
        self.sock.setblocking(False)
       
    def send(self, msg):
        if isinstance(msg, str):
            try:
                msg = msg.encode('utf-8')
            except:
                return
        elif not isinstance(msg, bytes):
            return


        self.sock.send(msg)
        
        
    def recv(self):
        global DEFAULT_BUFFER
        data = b''
        while True:
            try:
                d = self.sock.recv(DEFAULT_BUFFER)
                if d == b'':
                    return data
                data += d
            except:
                return data    


    def close(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()