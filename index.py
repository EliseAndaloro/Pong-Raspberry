###Affichage d'un seul pixel###
from sense_hat import SenseHat
sense = SenseHat()
sense.clear(0,0,0)
x=4
y=6
sense.set_pixel(x,y,66, 134, 244)