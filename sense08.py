# Print formatted sensor values
 
from sense_hat import SenseHat
sense = SenseHat()

# Function returning value as string rounded to whole number
def formatValue(value, units=""):
    value = round(value)
    value_str = str(value) + units
    return value_str 

# Get humidity value  
humidity = sense.get_humidity()

# Print raw humidity value
print(humidity)

# Print formatted relative humidity
print(formatValue(humidity,"%"))
 
# Display relative humidity on LED Matrix
sense.show_message(formatValue(humidity,"%"))

# Get pressure value 
pressure = sense.get_pressure()

# Print raw pressure value
print(pressure)

# Print formatted pressure in kPa
print(formatValue(pressure,"kPa"))
 
# Display relative pressure on LED Matrix
sense.show_message(formatValue(pressure,"kPa"))
