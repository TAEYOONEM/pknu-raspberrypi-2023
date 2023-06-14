# LED 
import RPi.GPIO as GPIO
import time

sig_pin = 18

# GPIO.Setmode(GPIO.BOARD)-4DD# 1 ~ 40
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND
GPIO.setup(sig_pin,GPIO.OUT)

while(True) :
    GPIO.output(sig_pin,True)
    time.sleep(1)
    GPIO.output(sig_pin,False)
    time.sleep(1)
