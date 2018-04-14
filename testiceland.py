from iceconnect import *

places = PlaceDB()
placelist =places.get_place_list()
for p in placelist:
    print(p)
