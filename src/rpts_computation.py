from src.df_computation import *
from src.functions import *


def getAirports(row):
    r = 2000
    kw = "airports"
    results = []
    lat = row.latitude
    lng = row.longitude
    result = geoPlaces(lat,lng,r,kw)
    results.append(result)
    for e in results:
        if e["results"]!=[]:
            i = e["results"]
            rr = []
            for c in i:
                j = c["name"]
                k = c["geometry"]["location"]
                rr.extend([j,k])
            return rr
        else:
            return "no"


def countAirports(row):
    if row.airports == "no":
        return 0
    else:
        return len(row.airports)//2


def stationsOK(stations):
    if stations == "no":
        stations_ok = stations
    else:
        stations_ok = normPlaces(stations)
        
    return stations_ok