from sense_hat import SenseHat
sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
sense.show_message("RS", text_colour=red, back_colour=green)
sense.clear()
