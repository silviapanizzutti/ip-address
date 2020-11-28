

from geopy import distance

def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2): 
    return distance.distance((lat1,lon1),(lat2,lon2)).km




