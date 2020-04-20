from src.df_computation import *
from src.functions import *


def getVegan(row):
    r = 2000
    kw = "vegan"
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


def countVegan(row):
    if row.vegan == "no":
        return 0
    else:
        return len(row.vegan)//2