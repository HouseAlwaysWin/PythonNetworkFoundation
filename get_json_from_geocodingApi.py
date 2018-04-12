import requests,argparse

def geocode(address):
    parameters = { 'address':address,'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base,params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="get map lat and lng by address")
    parser.add_argument('-a',metavar='address',type=str,default='207 N. Defiance St, Archbold, OH')
    args = parser.parse_args()
    geocode(args.a)


