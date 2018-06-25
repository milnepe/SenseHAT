# Print calibrated sensor values

from sense_hat import SenseHat
sense = SenseHat()

# Function returning calibrated value
def calibrateValue(value, calibration_value=0):
    value = value + calibration_value
    return value

# Get a raw temperature value
temperature = sense.get_temperature()

# Print raw temperature value
print(temperature)

# Print calibrated temperature using defaut calibration (no calibration)
print(calibrateValue(temperature))

# Print temperature increased by +2 degrees celsius
print(calibrateValue(temperature, 2))

# Print temperature reduced by -10 degrees celsius
print(calibrateValue(temperature,-10))
