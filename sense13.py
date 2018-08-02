#!/usr/bin/python3
"""
	Test function to obtain nearest country
	given location
"""

import math 

# ISS, Greenwich, UK 51.4826° N, 0.0077° W
iss_coordinates = {'location': "London", 'country': "UK", 'lat': 51.4826, 'long': -0.0077}

# Capital co-ordinates
capital_coordinates = ({'location': "London", 'country': "UK", 'lat': 51.5074, 'long': -0.1278},
                       {'location': "New York", 'country': "US", 'lat': 40.7128, 'long': -74.0060},
                       {'location': "Cape Town", 'country': "ZA", 'lat': -33.9249, 'long': 18.4241},
                       {'location': "Canberra", 'country': "AU", 'lat': -35.2809, 'long': 149.1300},
                       {'location': "Delhi", 'country': "IN", 'lat': 28.7041, 'long': 77.1025},
                       {'location': "Moscow", 'country': "RU", 'lat': 55.7558, 'long': 37.6173})


# Earths radius in Miles or Kilometres
earth_radius = {'miles': 3960, 'kilometres': 6373}

# Function to calculate radial distance in radians between two points ψ
# https://www.johndcook.com/lat_long_details.html
# ψ = arccos(sin φ1 sin φ2 cos(θ1-θ2) + cos φ1 cos φ2)
# Where:
# Co-ordinates MUST be expressed as latitude N (S is negative), longitude E (W is negative)
# φ (phi) is angle in radians from north pole down to geographical location
# θ (theta) is latitude in radians EAST from maridian to geographical location

def radial_distance(coord0, coord1, radius):

	# Calculate number of Radians per Degree - 2 * pi / 360
	degrees_to_radians = math.pi / 180.0

	# Calculate phi in radians of each point
	phi0 = (90.0 - coord0['lat']) * degrees_to_radians
	phi1 = (90.0 - coord1['lat']) * degrees_to_radians

	# Calculate theta in radians of each point
	theta0 = coord0['long'] * degrees_to_radians
	theta1 = coord1['long'] * degrees_to_radians

	arc = math.acos((math.sin(phi0) * math.sin(phi1) * math.cos(theta0 - theta1) + math.cos(phi0) * math.cos(phi1)))
	return arc * radius

flag = ""
d = 25000
for c in capital_coordinates:
	distance = radial_distance(iss_coordinates, c, earth_radius['miles'])
	if distance <= d:
		d = distance
		flag = c['country']

print(flag, d,"Miles")




