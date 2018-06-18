from sense_hat import SenseHat
sense = SenseHat()
temp_c = sense.get_temperature()
print("Temperature in Celsius: {0:.1f}C".format(temp_c))
temp_f = (temp_c * 9 / 5) + 32
print("Temperature in Fahrenheit: {0:.1f}F".format(temp_f))
pressure = sense.get_pressure()
print("Pressure in millibar: {0:.1f}mbar".format(pressure))
humidity = sense.get_humidity()
print("Relative Humidity: {0:.0f}%".format(humidity))
