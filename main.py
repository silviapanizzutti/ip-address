from ip_address import get_location

ip_address = '153.138.24.18'

country, city = get_location(ip_address)

print("IP address {} is from {}, {} ".format(ip_address, city,  country))
