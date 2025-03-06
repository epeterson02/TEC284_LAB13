from gpiozero import LED, Button
from time import sleep
import random

led = LED(18)

for i in range (0, 10):
    led.on()
    sleep(1)
    led.off()
    sleep(1)