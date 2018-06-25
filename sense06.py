# Print raw Temperature in degrees celsius

# Import SenseHAT library module
from sense_hat import SenseHat

# Create SensHAT object
sense = SenseHat()

# Read temperature in celsius
temperature = sense.get_temperature()

# Print the raw value with lots of decimal places!
print(temperature)
