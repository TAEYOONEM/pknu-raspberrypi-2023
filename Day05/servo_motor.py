import RPi.GPIO as GPIO
import time

pwm_pin = 18
degree = 0
step = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 100)

SERVO_MIN_DUTY = 3
SERVO_MAX_DUTY = 12

pwm.start(0)

while True :
    # cmd = input('Input Key [f|r]')
    # direction = cmd[0]
    # if direction == 'f' : 
    #     angle += 1
    # else :
    #     angle -= 1

    # if angle < 3 :
    #     angle = 3
    # elif angle > 20 :
    #     angle = 20
    # print(f"angle = {(angle-3)*10}")
    # pwm.ChangeDutyCycle(angle)

    degree += step
    
    if degree == 0 or degree == 180 :
        step *= -1

    duty = SERVO_MIN_DUTY+(degree * (SERVO_MAX_DUTY - SERVO_MIN_DUTY)/180.0)
    time.sleep(0.01)
    pwm.ChangeDutyCycle(duty)
    
