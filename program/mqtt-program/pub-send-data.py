import paho.mqtt.client as mqtt
import time
import datetime
import random
import sys

mqttc = mqtt.Client()
mqttc.connect("192.168.1.55", 1883)
topic = "mqtt-CocoBot"

print "iot-device-no: " + str(sys.argv[1])
iot_device_no =str(sys.argv[1])

while True:
    rand_no1 = random.randint(0,99)
    rand_no2 = random.randint(0,80)
    #dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = iot_device_no + "," + str(rand_no1) + ","  + str(rand_no2)
    mqttc.publish(topic, msg)
    print("publisher", msg)
    time.sleep(2)