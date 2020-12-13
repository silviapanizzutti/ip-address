from ip_address import get_location
from distance import getDistanceFromLatLonInKm as getdistlat
from maps import show_map
from database import open_and_create
from database import save_new_username_correct
from database import check_for_username_correct
import argparse
from getpass import getpass
import sys


def getOptions(args=sys.argv[1:]):
    """ Requests the arguments the user can insert when calling the function:
        * requires a choice between signup and sign in
        * requires a username and a password
        * requires an ip address 
        and returns:
        * distance from the query and map displaying the position of the ip adresses
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-ip", "--ip_address", help="insert the ip address")
    parser.add_argument('-u',
                        "--username",
                        help="insert a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', "--password", help="the username's password",
                        required=False)
    parser.add_argument('-s', "--signup",
                        help="are you a new user?select 2,
                        otherwise press 1",
                        required=False)
    args = parser.parse_args()
    return args
args = getOptions()

if args.signup is None:
    signup = input("press 1 to sign and 2 to sign up ")
    if signup == "2":
        # this connects the psw database module with the main
        open_and_create()
        user = input("insert a new username ")
        passwd = input("insert a new password ")
        save_new_username_correct(user, passwd)
    elif signup == "1":
        if args.username is None:
            user = input("insert username ")
            passwd = getpass()
            open_and_create()
            chec = check_for_username_correct(user, passwd)
            if chec == -1:
                print("Password not valid")
                while chec != 1:
                    user = input("insert a username ")
                    passwd = input("insert a password ")
                    chec = check_for_username_correct(user, passwd)
        else:
            if args.password is None:
                print("insert the password")
                quit(0)
                user = args.username
                passwd = args.password
                chec = check_for_username_correct(user, passwd)
            if chec == -1:
                quit(1)
    else:
        print("you just put a wrong input ")
        quit()
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
    show_map({"lat": [lat1, lat2],
              "lon": [lng1, lng2],
              "IP": ["Requested IP",
                     "Your IP"]})  # this opens up the map in another page
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
