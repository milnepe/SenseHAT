# Show environmental sensor readings selected with Joystick

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# Create RGB colours
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

# Function returning calibrated value
def calibrateValue(value, calibration_value=0):
    calibrated_value = value + calibration_value
    return calibrated_value

# Function returning value as string rounded to whole number 
def formatValue(value, units=""):
    value = round(value)
    value_str = str(value) + units
    return value_str

# Function displaying temperature
def showTemperature():
    value = calibrateValue(sense.get_temperature(),-10)
    message = formatValue(value,"C")
    sense.show_message(message, text_colour=red)
    print(value)

# Function displaying pressure
def showPressure():
    value = sense.get_pressure()
    message = formatValue(value,"kPa")
    sense.show_message(message, text_colour=green)
    print(value)

# Function displaying humidity
def showHumidity():
    value = sense.get_humidity()
    message = formatValue(value,"%")
    sense.show_message(message, text_colour=blue)
    print(value)

# Function showing a sensor
def show(sensor):
    sensor()

# Default to showing temperature
sensor = showTemperature

# Loop checking joystick events
while True:
    show(sensor) # show sensor reading
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            # Check which direction
            if event.direction == "up":
                sensor = showPressure # Set to Pressure
            elif event.direction == "down":
                sensor = showHumidity # Set to Humidity
            elif event.direction == "left":
                sense.set_rotation(0)   # Rotate display
            elif event.direction == "right":
                sense.set_rotation(90) # Rotate display
            elif event.direction == "middle":
                sensor = showTemperature  # Set to Temperature

            # Wait a while
            sleep(0.5)

