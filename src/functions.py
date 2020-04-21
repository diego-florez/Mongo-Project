import requests
import os
from dotenv import load_dotenv
from math import sqrt
from pandas.io.json import json_normalize
from src.df_computation import *


def geoPlaces(lat,lng,r,kw):
    load_dotenv()
    api_key = os.getenv("google")
    res = requests.get(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={r}&keyword={kw}&key={api_key}")
    data = res.json()
    return data


def normalize(comps):
    return json_normalize(comps, "offices", ["name","category_code","total_money_raised","founded_year"])


def checkCoord(row):
    lat = row.latitude
    lng = row.longitude
    lat1 = [e for e in dfo.latitude]
    lng1 = [e for e in dfo.longitude]
    a = [e - lat for e in lat1]
    b = [e - lng for e in lng1]
    c = [sqrt(e * e  +  i * i) for e,i in zip(a,b)]
    radius = 2
    test =  any(i <= radius for i in c)
    return "inside" if test==True else "outside"


def normPlaces(x):
    data = pd.DataFrame({'place': x[0::2], 'coords': x[1::2]})
    normalize = json_normalize(data.coords)
    predf = pd.concat([data, normalize], axis=1, sort=False)
    df = predf.rename(columns={"lat": "latitude", "lng": "longitude"})
    finaldf = df.drop(columns=['coords'])
    return finaldf






