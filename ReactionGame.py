from gpiozero import LED, Button
from time import sleep
import random

led = LED(18)
right_button = Button(4)
left_button = Button(17)
player1 = "name"
player2 = "name2"

def pressed(button):
    if button.pin.number ==4:
        print(player1 + ' pressed first!')
    elif button.pin.number ==17:
        print(player2 + ' pressed first!')
right_button.when_pressed = pressed
left_button.when_pressed = pressed

