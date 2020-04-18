import requests
import os
from dotenv import load_dotenv

def get_api():
    load_dotenv()
    apiKey = os.getenv("crunch")
    #"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=38.8976763%2C-77.0365298&radius=50000&keyword=mcdonalds&key={apiKey}
    url = f"https://api.crunchbase.com/odm/v4/odm.tar.gz?user_key={apiKey}"
    res = requests.get(url)
    print(res.status_code, res.url)
    return res.json()


test=get_api()
print(test)