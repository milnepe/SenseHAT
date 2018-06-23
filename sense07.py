# Print formated Temperature with units

# Import SenseHAT library module
from sense_hat import SenseHat
sense = SenseHat()

# Function to format Temperature sensor value
def formatTemperature():
    temperature = sense.get_temperature() - 10
    temperature = round(temperature)
    temperature = str(temperature) + "C"
    return temperature

# Print nicely formated temperature value with units
print(formatTemperature())

# Print a more descriptive temperature
print("Room temperature is: " + formatTemperature())

# Display temperature in red on LED Matrix
red = (255,0,0)
sense.show_message(formatTemperature(),text_colour=red)
