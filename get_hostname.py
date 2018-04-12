import socket
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Get Ip Address from Host Name")
    parser.add_argument('-n', metavar='hostname',
                        type=str, default='www.python.org')
    args = parser.parse_args()
    hostname= args.n;
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {} '.format(hostname, addr))
