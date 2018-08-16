import paho.mqtt.client as mqtt
import mysql.connector

mydb = mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "123456",
	database = "iot_device"	
)
mycursor = mydb.cursor()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("mqtt-CocoBot")

def on_message(client, userdata, msg):
    print(msg.topic + " ", str(msg.payload))
    message_input = str(msg.payload).split(',')

    sql = "INSERT INTO iot(iot_name, iot_value1, iot_value2) VALUES (%s, %s, %s)"
    val = (message_input[0], message_input[1], message_input[2])
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.55", 1883)
client.loop_forever()
