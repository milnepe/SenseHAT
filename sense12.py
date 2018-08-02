"""
	Test function to obtain ISS co-ordinates from Web Service
"""

import urllib.request, json

url="https://api.wheretheiss.at/v1/satellites/25544"

# Function to obtain ISS co-ordinates from service
def get_iss_coordinates(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
    coordinates = {'location': "ISS", 'country': "Space", 'lat':0, 'long':0}
    coordinates['lat'] = data['latitude']
    coordinates['long'] = data['longitude']
    return coordinates

#Test
iss_coordinates = get_iss_coordinates(url)

print("Location: ", iss_coordinates['location'])
print("Country: ", iss_coordinates['country'])
print("Lat: ", iss_coordinates['lat'])
print("Long: ", iss_coordinates['long'])

