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

# def rgb_false():
#     gp.output(red,False)
#     gp.output(blue,False)
#     gp.output(green,False)
    
try:
    while True :
        # rgb_false()
        # time.sleep(3)       
        # gp.output(red,True)
        # time.sleep(3)
        # rgb_false()
        # time.sleep(3)       
        # gp.output(green,True)
        # time.sleep(3)       
        # rgb_false()
        # time.sleep(3)       
        # gp.output(blue,True)
        # time.sleep(3)
        gp.output(red,False)
        gp.output(blue,True)
        gp.output(green,True)

except KeyboardInterrupt :
    gp.cleanup()    

