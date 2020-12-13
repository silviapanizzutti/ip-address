from geopy import distance


# this function measures the difference in km
# from one ip to the other using their coordinates
def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    """Returns the distance between the ip of the user and the ip requested"""
    return distance.distance((lat1, lon1), (lat2, lon2)).km
