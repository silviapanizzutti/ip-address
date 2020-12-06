from ip_address import get_location
from distance import getDistanceFromLatLonInKm
from database import *
import argparse
from getpass import getpass
import sys

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-ip", "--ip_address", help="insert the ip address")
    parser.add_argument('-u', "--username", help="insert a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p',"--password", help="the username's password",
                        required=False)
    args = parser.parse_args()
    return args
args=getOptions()

open_and_create()
#save_new_username_correct("admin","admin")
if args.username is None:
    user=input("insert username ")
    passwd = getpass()
    chec= check_for_username_correct(user,passwd)
    if chec == -1:
        print("Password not valid")
        while chec != 1:
            user=input("insert a username ")
            passwd=input ("insert a password ")
            chec= check_for_username_correct(user,passwd)
else:
    if args.password is None:
        print("insert the password")
        quit(0)
    user=args.username
    passwd=args.password
    chec= check_for_username_correct(user,passwd)
    if chec == -1:
        quit(1)
if  args.ip_address is None:
    ip_address=input("insert an ip address ")
else:
    ip_address = args.ip_address
try:
    lat1,lng1,lat2,lng2,country, city = get_location(ip_address)
except:
    if args.verbose:
        print("ip address is not valid")
    quit()


print("IP address {} is from {}, {} {:10.3f}Km".format(ip_address, city,  country,getDistanceFromLatLonInKm(lat1,lng1,lat2,lng2)))
