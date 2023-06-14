# LED RGB 
import RPi.GPIO as gp
import time

red= 22
blue = 27 
green = 17

gp.setmode(gp.BCM)

gp.setup(red,gp.OUT)
gp.setup(green,gp.OUT)
gp.setup(blue,gp.OUT)

gp.output(red,False)
gp.output(blue,False)
gp.output(green,False)

   
try:
    while True :
        gp.output(red,False)
        gp.output(blue,True)
        gp.output(green,True)
        time.sleep(1)
        gp.output(red,True)
        gp.output(blue,True)
        gp.output(green,False)
        time.sleep(1)
        gp.output(red,True)
        gp.output(blue,False)
        gp.output(green,True)
        time.sleep(1)


except KeyboardInterrupt :
    gp.cleanup()    

