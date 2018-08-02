#!/usr/bin/python3
"""
	Application to track ISS Space Station using web service
"""

import math, urllib.request, json 

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

url="https://api.wheretheiss.at/v1/satellites/25544"

# Create RGB colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Witney, UK 51.7859° N, 1.4851° W
base_coordinates = {'location': "Witney", 'country': "UK", 'lat': 51.7859, 'long': -1.4851}

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

# Function to obtain ISS co-ordinates from service
def get_iss_coordinates(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
    coordinates = {'location': "ISS", 'country': "Space", 'lat':0, 'long':0}
    coordinates['lat'] = data['latitude']
    coordinates['long'] = data['longitude']
    return coordinates

#Function returning value as string rounded to whole number
def format_value(value, units=""):
    value = round(value)
    value_str = str(value) + units
    return value_str

while True:
    # Calculate distance
    iss_coordinates = get_iss_coordinates(url)  
    distance = spherical_distance(base_coordinates, iss_coordinates, earth_radius['miles'])
    #distance = 1000
    # Set colour according to how far ISS is from base
    if distance < 800:
        colour = green
    elif distance < 2000:
        colour = blue
    else:
        colour = red 

    # Display results on Matrix
    sense.set_rotation(90)
    message = format_value(distance,"M")
    sense.show_message(message,text_colour=colour)

    # Show info on standard output
    print("Lat: ", iss_coordinates['lat'])
    print("Long: ", iss_coordinates['long'])
    print(distance, "miles")

    # Repeat message
    sleep(5)
    sense.show_message(message,text_colour=colour)
    sleep(5)
