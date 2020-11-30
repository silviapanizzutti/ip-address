import requests
import json


IP_URL ='http://ip-api.com/json/{}'

def get_location(ip_address):

    URL = IP_URL.format(ip_address)
    r = requests.get(URL)
    info = json.loads(r.text)
    #print(info)
    try:
        location = info['country']
        city = info['city']
    except KeyError:
        print('Error')

    return location, city
