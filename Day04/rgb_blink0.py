import RPi.GPIO as gp
import time

red= 22
blue = 27 
green = 17

on = 10

gp.setmode(gp.BCM)
gp.setup(red,gp.OUT)
gp.setup(green,gp.OUT)
gp.setup(blue,gp.OUT)

gp.setup(on,gp.IN)

gp.output(red,False)
gp.output(blue,False)
gp.output(green,False)

try:
    while True :
        inputIO = gp.input(on)

        if inputIO == True :
            gp.output(red,False)
            gp.output(blue,True)
            gp.output(green,True)
            print('a')
        else :
            gp.output(red,True)
            print('b')
except KeyboardInterrupt :
    pass


