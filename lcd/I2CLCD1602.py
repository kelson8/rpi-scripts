#!/usr/bin/env python3
########################################################################
# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : freenove
# modification: 2023/05/15
########################################################################

# Modified by kelson8 10-11-2024 @ 2:38PM
import smbus
from time import sleep, strftime
from datetime import datetime
from LCD1602 import CharLCD1602

from gpiozero import Button

# TODO Define a button for this to show some text.

button1 = Button(4)



lcd1602 = CharLCD1602()    
def get_cpu_temp():     # get CPU temperature from file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C '

# Return the number without the C at the end for my needs.
def get_cpu_temp_num():
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 )
 
# If this is set to true it has the time in 12 hour format, otherwise its in 24 hour format.
def get_time_now(h12_enabled):     # get system time
    if h12_enabled:
        return datetime.now().strftime('   %I:%M:%S %p')
    else:
        return datetime.now().strftime('   %H:%M:%S')
    
# 2x2 LCD

# Run with a button on the gpio, this didn't work.
def new_loop():
    lcd1602.init_lcd()
    count = 0
    
    cpu_temp = float(get_cpu_temp_num())
    show_cpu_temp = True
    
    while button1.is_pressed:
        lcd1602.clear()
        # Somewhat clears the laggy refresh rate
        #lcd1602.write(0, 0, "")
        lcd1602.write(0, 1, "")
        
        # 
        
        # Get the cpu temps or display KCNet Systems
        # First row
        if show_cpu_temp:
            lcd1602.write(0, 0, '   CPU: ' + get_cpu_temp() )# display CPU temps
        else:
            lcd1602.write(0, 0, "   KCNet Systems")
        
        # Second row
        if cpu_temp > 57:
            lcd1602.write(0, 1, "Cpu is hot!")
        else:
            lcd1602.write(0, 1, get_time_now(True) )   # display the time
            sleep(1)
        #lcd1602.write(0, 1, "KCNet Systems")
        #sleep(1)

# Run without button
def loop():
    lcd1602.init_lcd()
    count = 0
    
    cpu_temp = float(get_cpu_temp_num())
    show_cpu_temp = True
    
    while(True):
        lcd1602.clear()
        # Somewhat clears the laggy refresh rate
        #lcd1602.write(0, 0, "")
        lcd1602.write(0, 1, "")
        
        # 
        
        # Get the cpu temps or display KCNet Systems
        # First row
        if show_cpu_temp:
            lcd1602.write(0, 0, '   CPU: ' + get_cpu_temp() )# display CPU temps
        else:
            lcd1602.write(0, 0, "   KCNet Systems")
        
        # Second row
        if cpu_temp > 57:
            lcd1602.write(0, 1, "Cpu is hot!")
        else:
            lcd1602.write(0, 1, get_time_now(True) )   # display the time
            sleep(1)
        #lcd1602.write(0, 1, "KCNet Systems")
        #sleep(1)
        
def destroy():
    lcd1602.clear()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    