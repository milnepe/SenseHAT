from sense_hat import SenseHat
sense = SenseHat()
temp_c = sense.get_temperature()
print(temp_c)
temp_f = (temp_c * 9 / 5) + 32
print("Temperature in Fahrenheit: {0:.1f}F".format(temp_f))
