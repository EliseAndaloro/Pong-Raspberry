from sense_hat import SenseHat
sense = SenseHat()
import time
sense.clear(0,0,0)
x=0
y=6
sense.set_pixel(x,y,66, 134, 244)
while x<7:
    sense.clear(0,0,0)
    sense.set_pixel(x,y,66,134,244)
    time.sleep(0.5)
    x= x+1
    y=y-1