import RPi.GPIO as gp
import time

red= 22
blue = 27 
green = 17

btn = 10
cnt = 0 

gp.setmode(gp.BCM)
gp.setup(red,gp.OUT)
gp.setup(green,gp.OUT)
gp.setup(blue,gp.OUT)

def clickHandler(ch) :
    global cnt
    cnt = cnt + 1
    
    if cnt % 2 == 0 :
        gp.output(red, gp.LOW)
    else :
        gp.output(red, gp.HIGH)

gp.setwarnings(False) # Disappvear Warning Log 
gp.setmode(gp.BCM)
gp.setup(btn, gp.IN, pull_up_down=gp.PUD_DOWN)
gp.add_event_detect(btn, gp.RISING, callback = clickHandler)

while True :
    time.sleep(1)