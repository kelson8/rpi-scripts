from gpiozero import LED, Button, Device
import time
import RPi.GPIO as GPIO
import datetime

def write_text(file, text):
    with open(file, "a") as f:
        f.write(text)
    

# GPIO.setmode(GPIO.BCM)

button1 = Button(4)
green_led = LED(36)


file = "log.txt"

def toggle_green_led():
    while True:
        current_time = datetime.datetime.now()
        current_year = current_time.year
        current_month = current_time.month
        current_day = current_time.day

        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second
        date_string = str(current_year) + "/" + str(current_month) + "/" + str(current_day) + " " + str(current_hour) + ":" + str(current_minute) + ":" + str(current_second)

        if button1.is_pressed:
            green_led.on()
            write_text(file, "[ " + date_string + "] " + "Green LED toggled on\n")
            print("[ " + date_string + "] " + "Green LED toggled on\n")
            # print("Hello")
            time.sleep(0.5)
        else:
            green_led.off()
            # write_text(file, "[ " + date_string + "] " + "Green LED toggled off\n")
            # print("[ " + date_string + "] " + "Green LED toggled off\n")
            # print("Goodbye")
            time.sleep(0.5)

# This works for a button counter but the value always increases if the button is held
# I would like it to only increase each time the button is pressed.
def button_press_check():
    button_counter = 0
    while True:
        # if button1.when_activated():
        # if button1.is_pressed():
        if button1.is_active:
            time.sleep(0.5)
            button_counter += 1
            print("Button counter: " + str(button_counter))

# print(str(current_year) + "/" + str(current_month) + "/" + str(current_day))
# print(date_string)
toggle_green_led()

# button_press_check()

# button1.when_activated = print("Hello")
# button1.when_deactivated = print("Goodbye")

# print("Hello")