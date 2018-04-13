import http.client
import json
import argparse
import logging
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base,quote_plus(address))

    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET',path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use HttpConnection to connect google map')
    parser.add_argument('-a',metavar='address',type=str,default='207 N. Defiance St, Archbold, OH')
    args = parser.parse_args()
    geocode(args.a)