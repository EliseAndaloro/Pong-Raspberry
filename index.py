from sense_hat import SenseHat
sense = SenseHat()
import time
import random
sense.clear(0,0,0)

x=random.randint(1,6)
y=random.randint(1,6)

x_sens=1
y_sens=1


sense.set_pixel(x,y,66, 134, 244)
while True:
    sense.clear(0,0,0)
    sense.set_pixel(x,y,66,134,244)
    time.sleep(0.2)
    x = x+x_sens
    y=y+y_sens
    
    
    if x==7:
      
      x_sens=-1
    
    if y==0:
      y_sens=1 

      
    if y==7:
      y_sens=-1
    
    if x==0:
      x_sens=1