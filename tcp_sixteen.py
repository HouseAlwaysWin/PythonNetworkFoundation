import argparse,socket

def recvall(sock,length):
    data = b''
    while len(data) < length:
        more = ock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only recived'
            ' %d bytes before the socket closed' % (length,len(data)))
        data += more
    return data

def server(interface,port):
             