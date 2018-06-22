from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# Create RGB colours
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

def formatValue(get_sensor_value, calibration_value=0, units=None):
    value = get_sensor_value - calibration_value
    value = round(value)
    value = str(value) + units
    return value

sense.clear()
colour = white
message = formatValue(sense.get_temperature(), 10, "C")
while True:
  sense.show_message(message, text_colour=colour)
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      if event.direction == "up":
        colour = red
        message = formatValue(sense.get_temperature(), 10, "C") # Up arrow
      elif event.direction == "down":
        pass      # Down arrow
      elif event.direction == "left":
        colour = green 
        message = formatValue(sense.get_pressure(), 0, "kPa")   # Left arrow
      elif event.direction == "right":
        colour = blue
        message = formatValue(sense.get_humidity(), 0, "%") # Right arrow
      elif event.direction == "middle":
        pass      # Enter key
      
      # Wait a while
      sleep(0.5)
      sense.clear()

