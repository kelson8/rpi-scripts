# Turn on/off the leds
from gpiozero import LED, Button
from time import sleep

green_led = LED(16)
yellow_led = LED(17)
red_led = LED(18)

import RPi.GPIO as GPIO
import time

green_led = 36
yellow_led = 38
red_led = 40
button = 4

# GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def turn_led_on(led):
    GPIO.setup(led, GPIO.OUT)
    print("LED on")
    GPIO.output(led, GPIO.HIGH)

def turn_led_off(led):
    GPIO.setup(led, GPIO.OUT)
    print("LED off")
    GPIO.output(led, GPIO.LOW)

#
#def toggle_led(led):
#    GPIO.setup(led, GPIO.OUT)
#    if GPIO.output(led, GPIO.HIGH):
#        turn_led_off(led)
#    elif GPIO.output(led, GPIO.LOW):
#        turn_led_on(led)

# This works now
# https://forums.raspberrypi.com/viewtopic.php?t=228350
def toggle_led(led):
    GPIO.setup(led, GPIO.OUT)
    led_state = GPIO.input(led)

    if led_state:
        turn_led_off(led)
    else:
        turn_led_on(led)

# I'll need to figure out how to use gpiozero for this.
#def main_old():
    #print("Turn which leds on?")
    #led_input = input("Turn which leds on?: ")
    
    #if led_input == "green":
    #    if not green_led.on:
    #        print("Green led turned on")
    #    else:
    #        print("Green led turned off")
    #if led_input == "yellow":
    #    pass
    #if led_input == "red":
    #    pass
    #else:
    #    print("Invalid input")

# Copied idea from toggle_led.py from my code.

# Idea for checking for an int from here:
# https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number

# I couldn't remember how to do it myself.
def main():
    #led_input = int(input("Toggle which leds? (1 Green, 2 Yellow, 3 Red): "))
    
    #if led_input == "green":
    try:
        led_input = int(input("Toggle which leds? (1 Green, 2 Yellow, 3 Red): "))
        if led_input == 1:
            toggle_led(green_led)
        #elif led_input == "yellow"
        elif led_input == 2:
            toggle_led(yellow_led)
        #elif led_input == "red":
        elif led_input == 3:
            toggle_led(red_led)
        else:
            print("Invalid input")
    except ValueError:
        print("Error, value is not a number!")
    
def check_leds():
    print(green_led)
        
    
if __name__ == '__main__':
    try:
        while True:
            main()
            sleep(0.5)
        #check_leds()
    except KeyboardInterrupt:
        pass