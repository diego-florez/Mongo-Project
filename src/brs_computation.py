from src.df_computation import *
from src.functions import *


def getBars(row):
    r = 2000
    kw = "bars"
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


def countBars(row):
    if row.bars == "no":
        return 0
    else:
        return len(row.bars)//2