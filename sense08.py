# Display Temperature, Pressure & Humidity on LED Matrix

# Import SenseHAT library module
from sense_hat import SenseHat
sense = SenseHat()

# Function to format sensor value as a message
def formatValue(get_sensor_value, calibration_value=0, units=None):
    value = get_sensor_value - calibration_value
    value = round(value)
    value = str(value) + units
    return value

# Display formtated sensor readings on LED Matrix
sense.clear()
sense.show_message(formatValue(sense.get_temperature(), 10, "C"))
sense.show_message(formatValue(sense.get_pressure(), 0, "kPa"))
sense.show_message(formatValue(sense.get_humidity(), 0, "%"))
