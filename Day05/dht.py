import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 24

try :
    while True:
        humi, temp = dht.read_retry(sensor, pin)
        if humi is not None and temp is not None : 
            print(f"Tempurature:　{temp}C, Humidity: {humi}%")
        else :
            print("sensor error")
        time.sleep(1)
except Exception as ex :
    print(ex)
finally :
    print('Exit Programm')
    