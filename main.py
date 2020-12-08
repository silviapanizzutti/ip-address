from ip_address import get_location
from distance import getDistanceFromLatLonInKm as getdistlat
import argparse
from maps import show_map
import sys


def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-ip", "--ip_address", help="insert the ip address")
    args = parser.parse_args()
    return args
args = getOptions()


if args.ip_address is None:
    ip_address = input("insert an ip address ")
else:
    ip_address = args.ip_address
try:
    lat1, lng1, lat2, lng2, country, city = get_location(ip_address)
except:
    if args.verbose:
        print("ip address is not valid")
    quit()
try:
    show_map({"lat": [lat1, lat2], "lon": [lng1, lng2], "IP":["Requested IP", "Your IP"]})
except:
    import traceback
    traceback.print_exc()
print("IP address {} is from {}, {} {:10.3f}Km".format(ip_address,
                                                       city,
                                                       country,
                                                       getdistlat(lat1,
                                                                  lng1,
                                                                  lat2,
                                                                  lng2)))
