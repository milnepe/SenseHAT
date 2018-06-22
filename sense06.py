# Import SenseHAT library module
from sense_hat import SenseHat
# Create SensHAT object
sense = SenseHat()
# Value used to correct temperature measurement
calibration_value = 10
# Read temperature in celsius and adjust
temp_c = sense.get_temperature() - calibration_value
# Print the raw value with lots of decimal places!
print(temp_c)
# Round up reading to integer value
temp_c = int(round(temp_c,0))
# Print text description and value
print("Temperature in Celsius: ", temp_c)