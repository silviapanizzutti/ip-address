import requests
import json


IP_URL = 'http://ip-api.com/json/{}'


def get_location(ip_address):
    """Gets the data from the API:
       * latitude,longitude,country and city for the ip requested
       * latitude and longitude for the query (user's ip address)
    """

    re = requests.get("http://ip-api.com/json/")
    loc = re.json()
    URL = IP_URL.format(ip_address)
    r = requests.get(URL)
    info = json.loads(r.text)
    try:
        location = info['country']
        city = info['city']
        lat1 = info["lat"]
        lng1 = info["lon"]
        lat2 = loc["lat"]
        lng2 = loc["lon"]
    except KeyError:
        raise KeyError

    return lat1, lng1, lat2, lng2, location, city
