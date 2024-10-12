import RPi.GPIO as GPIO
import time

green_led = 36
yellow_led = 38
red_led = 40
button = 4

# GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# The message seems to output but it isn't changing the led output.


def program_loop():
    while True:
        time.sleep(1)
        GPIO.setup(green_led, GPIO.OUT)

        print("LED on")

        GPIO.output(green_led, GPIO.HIGH)
        time.sleep(1)

        print("LED off")
        GPIO.output(green_led, GPIO.LOW)


def stop_light():
    while True:
        time.sleep(1)
        GPIO.setup(green_led, GPIO.OUT)
        # print("Green LED on")
        GPIO.output(green_led, GPIO.HIGH)
        
        time.sleep(1)
        # print("Green LED off")
        GPIO.output(green_led, GPIO.LOW)
    
        time.sleep(1)
        
        GPIO.setup(yellow_led, GPIO.OUT)
        # print("Yellow LED on")
        GPIO.output(yellow_led, GPIO.HIGH)
    
    
        time.sleep(1)
        # print("Yellow LED off")
        GPIO.output(yellow_led, GPIO.LOW)
        
        time.sleep(1)
        GPIO.setup(red_led, GPIO.OUT)
        # print("Red LED on")
        GPIO.output(red_led, GPIO.HIGH)
        
        time.sleep(1)
        # print("Red LED off")
        GPIO.output(red_led, GPIO.LOW)
    
# Turn off all the leds when the program exits
def cleanup():
    GPIO.setup(green_led, GPIO.OUT)
    GPIO.output(green_led, GPIO.LOW)
    
    GPIO.setup(yellow_led, GPIO.OUT)
    GPIO.output(yellow_led, GPIO.LOW)
    
    GPIO.setup(red_led, GPIO.OUT)
    GPIO.output(red_led, GPIO.LOW)

# program_loop()
# stop_light()

def gpio_zero_test():
    pass

def button_test():
    GPIO.setup(button, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    while True: # Run forever
        if GPIO.input(button) == GPIO.HIGH:
            print("Button was pushed!")

button_test()

# if __name__  == '__main__':
#     try:
#         print("Program starting... ")
#         stop_light()
#     except KeyboardInterrupt:
#         print("Program exiting and turning off leds.")
#         cleanup()
    


