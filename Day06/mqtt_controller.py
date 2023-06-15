# paho-matt
# sudo pip install paho-matt
## publish / subscribe

from threading import Thread, Timer
import time
import json
import datetime as dt

import paho.mqtt.client as mqtt

import Adafruit_DHT as dht

import RPi.GPIO as GPIO

sensor = dht.DHT11
rcv_pin = 24
green = 17
servo_pin = 18

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3) 

# SEND
class publisher(Thread) :
    def __init__(self) :
        Thread.__init__(self) 
        self.host = '210.119.12.82'
        self.port = 1883
        self.cnt = 0
        self.clientId = 'IOT82'
        
        print('publisher thread start')
        self.client = mqtt.Client(client_id=self.clientId)

    def run(self) :
        self.client.connect(self.host, self.port)
        # self.client.username_pw_set() # when id/ pwd are needed
        self.publish_data_auto()

    def publish_data_auto(self) :
        humi, temp = dht.read_retry(sensor, rcv_pin)
        curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 2023-06-14 10:39:24
        origin_data = { 'DEV_ID' : self.clientId,
                        'CURR_DT' : curr,
                        'TYPE' : 'TEMPHUMID',
                        'STAT' : f'{temp}|{humi}' } # sample data
        pub_data = json.dumps(origin_data) # convert to json that is sent mqtt
        self.client.publish(topic='pknu/rpi/control/', payload=pub_data)
        self.cnt += 1
        print(f'Data published #{self.cnt}')
        Timer(2.0, self.publish_data_auto).start() # publish per 2sec
    
# RECEIVE    
class subscriber(Thread) :
    def __init__(self) :
        Thread.__init__(self)
        self.host = '210.119.12.82'
        self.port = 1883
        self.clientId = 'IOT82_SUB'
        self.topic = 'pknu/monitor/control/'
        print('subcriber thread start')
        self.client = mqtt.Client(client_id=self.clientId)
    
    def run(self) :
        self.client.on_connect = self.onConnect
        self.client.on_message = self.onMessage
        self.client.connect(self.host, self.port)
        self.client.subscribe(topic=self.topic)
        self.client.loop_forever() 

    def onConnect(self, mqttc, obj, flags, rc) :
        print(f'subscriber connected rc > {rc}')

    def onMessage(self, mqttc, obj, msg) :
        rcv_msg = str(msg.payload.decode('utf-8'))
        # print(f'{msg.topic} / {rcv_msg}')
        data = json.loads(rcv_msg) # convert to json
        stat = data['STAT']
        print(f'NOW STAT : {stat}')
        if stat == 'OPEN' :
            GPIO.output(green, GPIO.LOW)
            pwm.ChangeDutyCycle(12) # 90 degree
            
        elif stat == 'CLOSE' :
            GPIO.output(green, GPIO.HIGH)
            pwm.ChangeDutyCycle(3) # 0 degree
            
        time.sleep(1.0)

if __name__ == '__main__' :
    thPub = publisher()
    thSub = subscriber()
    
    thPub.start() # run() is auto started
    thSub.start()

    












