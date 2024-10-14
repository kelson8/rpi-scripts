from gpiozero import LED
from time import sleep

green_led = LED(16)


def turn_off_green_led():
    green_led.off()
    
def turn_on_green_led():
    green_led.on()
    
# Well this didn't work right.
def toggle_green_led():
    if not green_led.is_lit:
        green_led.on()
    else:
        green_led.off()
    
    #turn_off_green_led()
    #sleep(1)
    #turn_on_green_led()
 
toggle_green_led()

print(green_led.is_lit)