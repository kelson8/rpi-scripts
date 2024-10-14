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

toggle_led(green_led)
#turn_led_off(green_led)
#turn_led_on(green_led)
