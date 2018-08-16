import paho.mqtt.client as mqtt
import time
import datetime

mqttc = mqtt.Client()
mqttc.connect("192.168.1.55", 1883)
topic = "mqtt-CocoBot"

while True:
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = "Hello World! " + dt
    mqttc.publish(topic, msg)
    print("publisher", msg)
    time.sleep(2)
