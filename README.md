# IP Address Geolocator
## Implementation of an IP address Geolocator

By running this program you will be able to discover the location of an IP address and see the geographical representation and how far it is from yours. 

## Requirements

In order to run the code properly you need at least [Python 3.9](https://www.python.org/downloads/) and to install the following packets by running this code on your terminal.

```
python3 -m pip install -r re.txt
```

## Running the program

In order to run our project you need to open from this repository the file named ```main.py```
The function ```getOptions(args=sys.argv[1:])``` uses argparse to validate the input. When you call the function you can either specify all the arguments when you call the function like in example 1, if you do not the system wll ask you for the fundamental imputs one after the other like in EX.2
 
EX.1
```
python3 main.py -v -s 1 -u admin -p admin -ip 153.138.24.18 
```
EX.2
```
python3 main.py 
press 1 to sign and 2 to sign up: 1
insert username: admin
Password: admin
User is present, password is valid
insert an ip address 153.138.24.18
```

The function gives you an input option: "press 1 if you want to sign in and 2 if you want to sign up ". the function ```save_new_username_correct```  will save your data. If you are a new user press 2 and insert a username and a password. If you are not a new user press 1 and insert yor username and your password the function ```check_for_username_correct``` in ```database.py``` file will check the correctness of the input.

If your inputs are correct, the program will ask you the IP address you want to localize. Using the function ```get_location```in ```ip_address.py``` file and ```getDistanceFromLatLonInKm()``` in ```distance.py``` file, it will return the location of the IP address and how far it is from yours. 
The function ```show_map``` from ```maps.py``` opens locally in your browser a new page with a map showing the two IP locations.

In this repository you can also find other files that allow the program to properly run:

* ```database.py``` that implements the ```open_and_create()``` function that uses sqlite3 to create a user table; the ```save_new_username_correct(username,password)``` that uses secrets and package to generate salt and hashlib to hash the password; ```check_for_username_correct(username, password)```that computing the hash check if the username is present and the password is correct.

* ```ip_address.py``` that implements the ```get_location(ip_address)``` function that queries the [ip-api](https://ip-api.com/docs/api:json) website to fetch data about the location of the given input ```ip_address``` (lat, lon, country and city)

* ```distance.py``` that implements the ```getDistanceFromLatLonInKm()``` that, using geopy measures the distance in Km from the IP address requested and yours, using the data from```get_location(ip_address)``` function in ```ip_address.py``` file. 

* ```maps.py``` that implements the ```show_map(data)``` function that uses plotly.express to create a map showing the locations of the requested IP address and your IP address.


## Licence 
In this project we used the [GNU Licence](https://www.gnu.org/licenses/gpl-3.0.html). You can find all its details of usage in the file LICENCE.


## Tests 
We tested the correctness of the code and how it responds to wrong inputs through the module unittest. We used ```test_correct_values(self)``` function to verify if a correct input returns the expected results, the ```test_wrong_values(self)``` function to verify if an invalid input raises a KeyError and ```test_empty_string(self)``` to verify if an empty string raises a KeyError as well.
