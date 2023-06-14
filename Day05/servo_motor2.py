import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUTwL)
pwm = GPIO.PWM(pin, 50)
pwm.start(3.0)

for i in range(0, 3) :
    for high in range(30, 125):
        pwm.ChangeDutyCycle(high/10.0)
        time.sleep(0.02)

    for low in range(124, 30, -1) :
        pwm.ChangeDutyCycle(low/10.0)
        time.sleep(0.02)

pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()
