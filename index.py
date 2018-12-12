###Affichage d'un seul pixel###
from sense_hat import SenseHat
sense = SenseHat()
sense.clear(0,0,0)
sense.set_pixel(5,5,66, 134, 244)