#!/usr/bin/env python3
"""
	Flash the SenseHAT Matrix
"""

import time, sys
from sense_hat import SenseHat

sense = SenseHat()

# Setup colours
r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

# Set exch LED to a colour
flash_red = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]

flash_green = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g
]

print("Press Ctrl+C to exit")

# Keep flashing
while True:
	try: 
		sense.set_pixels(flash_red)
		time.sleep(1)
		sense.clear()
		sense.set_pixels(flash_green)
		time.sleep(1)
		sense.clear()
	except KeyboardInterrupt:
		sense.clear()
		sys.exit()

