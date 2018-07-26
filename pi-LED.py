from gpiozero import LED
from time import sleep

led = LED(17)

while True:
        led.on()
        print("ON")
        sleep(2)
        led.off()
        print("OFF")
        sleep(2)
