from src.df_computation import *
from src.functions import *


def getStarbucks(row):
    r = 2000
    kw = "starbucks"
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


def countStarbucks(row):
    if row.starbucks == "no":
        return 0
    else:
        return len(row.starbucks)//2


def starbucksOK(starbucks):
    if starbucks == "no":
        starbucks_ok = starbucks
    else:
        starbucks_ok = normPlaces(starbucks)
    
    return starbucks_ok