from gpiozero import LED, Button
from time import sleep
import random

# Setup
led = LED(18)
right_button = Button(4, bounce_time=0.2)  # Added bounce time to avoid false presses
left_button = Button(17, bounce_time=0.2)
player1 = "Player 1"
player2 = "Player 2"
score_player1 = 0
score_player2 = 0
game_rounds = 5
round_counter = 1

# Function to handle button presses
def pressed(button):
    global score_player1, score_player2
    if button.pin.number == 4:  # Player 1 pressed
        if led.is_lit:
            score_player1 += 1
            print(f"{player1} pressed first! Score: {score_player1} - {score_player2}")
            led.off()
        else:
            score_player1 -= 1
            print(f"{player1} pressed too early! Score: {score_player1} - {score_player2}")
            led.off()
    elif button.pin.number == 17:  # Player 2 pressed
        if led.is_lit:
            score_player2 += 1
            print(f"{player2} pressed first! Score: {score_player1} - {score_player2}")
            led.off()
        else:
            score_player2 -= 1
            print(f"{player2} pressed too early! Score: {score_player1} - {score_player2}")
            led.off()

right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Function to start a round
def start_round():
    global round_counter
    print(f"Round {round_counter}")
    round_counter += 1
    wait_time = random.randint(2, 8)  # Random wait time between 2 and 8 seconds
    print(f"Wait for the light to turn on... it will come on in {wait_time} seconds.")
    sleep(wait_time)
    led.on()  # Turn on the LED
    print("GO!")

# Game loop
while round_counter <= game_rounds:
    start_round()
    sleep(1)  # Give a moment before the round resets for next player to press
    led.off()  # Turn off the LED after the round

    # Check for win condition (best out of 5)
    if score_player1 > (game_rounds // 2):
        print(f"{player1} wins the game with a score of {score_player1}!")
        break
    elif score_player2 > (game_rounds // 2):
        print(f"{player2} wins the game with a score of {score_player2}!")
        break

