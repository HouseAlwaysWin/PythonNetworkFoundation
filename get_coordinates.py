# This Python file uses the following encoding: utf-8
from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
