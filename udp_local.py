import argparse,socket
from datetime import datetime

MAX_BYTES = 65535

def server(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print('Listening at {0}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print('The client at {0} says {1}'.format(address, text))
        data = text.encode('utf-8')
        sock.sendto(data, address)

def client(ip,port,words):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = 'The time is {0},I would like to say:{1}'.format(datetime.now(),words)
    data = text.encode('utf-8')
    sock.sendto(data,(ip,port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data,address = sock.recvfrom(MAX_BYTES)
    text = data.decode('utf-8')
    print('The server {0} replied {1}'.format(address,text))

if __name__ == '__main__':
    choices = {'client': client,'server':server}
    parser = argparse.ArgumentParser(description="Send and receive UDP locally")
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='port',type=int,default=1060,help='UDP Port (default 1060)')
    parser.add_argument('-i',metavar='ip',type=str,default='127.0.0.1')
    parser.add_argument('-w',metavar='say words',type=str,default='hello')
    args = parser.parse_args()
    function = choices[args.role]
    if args.role == 'server':
        function(args.i,args.p)
    else:
        function(args.i,args.p,args.w)
