#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import RPi.GPIO as GPIO
import time
import datetime

# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = '<your LINE token>'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

pir_sensor_pin = 17
led_pin = 4

GPIO.setup(pir_sensor_pin, GPIO.IN)    #Read output from PIR motion sensor
GPIO.setup(led_pin, GPIO.OUT)           #LED output pin

for i in range(0,3):
        GPIO.output(led_pin,True)
        #print("LED ON")
        time.sleep(1)

        GPIO.output(led_pin,False)
        #print("LED OFF")
        time.sleep(0.5)

print("Starting PIR motion sensor...")

while(True):
        if(GPIO.input(pir_sensor_pin)):
                for i in range(0,2):
                        GPIO.output(led_pin, True)
                        time.sleep(1)
                        GPIO.output(led_pin, False)
                        time.sleep(0.5)

                # MSG
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                msg = 'Motion Detected: ' + dt

                r = requests.post(url, headers=headers, data = {'message':msg})
                print r.text

                print msg
                time.sleep(3)
        time.sleep(1) #loop delay

GPIO.cleanup()