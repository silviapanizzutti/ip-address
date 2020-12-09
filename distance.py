from geopy import distance


def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    return distance.distance((lat1, lon1), (lat2, lon2)).km  # this function measures the difference in km from one ip to the other using their coordinates