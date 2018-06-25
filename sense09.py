# Print joystick direction events

# Import SenseHAT library module
from sense_hat import SenseHat
sense = SenseHat()

# Loop checking joystick events
while True:
  for event in sense.stick.get_events():
      print(event.direction, event.action)
