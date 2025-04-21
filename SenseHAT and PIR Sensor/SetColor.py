# Imports the sense hat module
from sense_hat import SenseHat
# Imports the sleep function from time module
from time import sleep
# Imports random module and random interger function
import random
from random import randint
from csv import writer

# Creates sensehat variable
sense = SenseHat()
# Clears sense hat led
sense.clear()

# Sets the colors to a variable 
r = (255,0,0)
g = (0,255,0)
w = (255,255,255)


# List to set the color on let matrix 
denied = [r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r,
		r,r,r,r,r,r,r,r]


approved = [g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g,
		g,g,g,g,g,g,g,g]

waiting = [w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w,
		w,w,w,w,w,w,w,w]

current_state = "waiting"

# Sets the pixed to red or green if user is approved or denied
def display_state(state):
    if state == "approved":
        sense.set_pixels(approved)
    elif state == "denied":
        sense.set_pixels(denied)
    elif state == "waiting": 
        sense.set_pixels(waiting)  
    else:
        print("Invalid state")


display_state(current_state)

# Gets user input for the joystick
def get_user_input():
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    return "approved"
                elif event.direction == "down":
                    return "denied"
                elif event.direction == "left":
                    return "waiting"
                
# Updates led matrix for the current state
try:
    while True:
        new_state = get_user_input()
        if new_state != current_state: 
            current_state = new_state
            display_state(current_state)
            print("Current State:", current_state)  

# clears led martix 
except KeyboardInterrupt:
    sense.clear()  
    print("Exiting...")