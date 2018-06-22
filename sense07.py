# Import SenseHAT library module
from sense_hat import SenseHat
sense = SenseHat()

# Create RGB colours
red = (255,0,0)
blue = (0,0,255)

# Function displaying calibrated celsius temperature
def displayCalibratedTemp():
    calibration_value = 10
    temp_c = sense.get_temperature()- calibration_value
    temp_c = int(round(temp_c))
    message = str(temp_c) + "C"
    if temp_c > 20:
        sense.show_message(message,text_colour=red)
    else:
        sense.show_message(message,text_colour=blue)

displayCalibratedTemp()