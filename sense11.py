"""
	Test function to compute radial distance between two points on Earths surface
	Expected answer:	
	107.42891438019696 km
	66.75325607179978 m
"""

import math

# Witney, UK 51.7859° N, 1.4851° W
base_coordinates = {'location': "Witney", 'country': "UK", 'lat': 51.7859, 'long': -1.4851}

# ISS, Greenwich, UK 51.4826° N, 0.0077° W
iss_coordinates = {'location': "London", 'country': "UK", 'lat': 51.4826, 'long': -0.0077}

# Earths radius in Miles or Kilometres
earth_radius = {'miles': 3960, 'kilometres': 6373}

# Function to calculate radial distance in radians between two points ψ
# https://www.johndcook.com/lat_long_details.html
# ψ = arccos(sin φ1 sin φ2 cos(θ1-θ2) + cos φ1 cos φ2)
# Where:
# Co-ordinates MUST be expressed as latitude N (S is negative), longitude E (W is negative)
# φ (phi) is angle in radians from north pole down to geographical location
# θ (theta) is latitude in radians EAST from maridian to geographical location

def spherical_distance(coord0, coord1, radius):

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

# Test
distance = spherical_distance(base_coordinates, iss_coordinates, earth_radius['kilometres'])
print(distance, "km")
distance = spherical_distance(base_coordinates, iss_coordinates, earth_radius['miles'])
print(distance, "m")

