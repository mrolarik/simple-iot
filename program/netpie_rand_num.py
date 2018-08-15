import microgear.client as netpie
import base64, zlib, time
import random

key = 'ZKFCxN5skXCGqsG'
secret = 'L54fMRJQOE0BYUPGNKdDrwPUS'
app = 'olarikRPi'

netpie.create(key,secret,app,{'debugmode': True})

def connection():
	print "Now I am connected with netpie"

def subscription(topic,message):
	print topic+" "+message

netpie.setname("RPi")
netpie.on_connect = connection
netpie.on_message = subscription
netpie.subscribe("/mails")

netpie.connect()

# random.randint(0,100) instead of temperature 
# random.randint(0,50) instead of Humidity

while True:
	netpie.chat("RPi",str(random.randint(0,100))+","+str(random.randint(0,50)))
	time.sleep(2)

