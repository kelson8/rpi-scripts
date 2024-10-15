# rpi-scripts

Scripts and code that I use for my raspberry pi, mostly in python but there may be some C++ in this also.

# Files

### Root folder
* clock_test.py - Show the clock in 24 hour time in a loop on a terminal, I need to set this up to work with 12 hour time also.
* convert_file_sizes.py - Convert file size from bytes to other sizes
* cpu_temp.py - Show the cpu temperature on Linux and possibly Mac, currently not compatible with Windows.

### CPlusPlus folder
* Curl test - Basic test with curl in C++, only tested on Raspberry pi and Linux.
* Rpi test - Toggle leds in C++, and lua testing in C++. 

### Lcd folder
* I2LCD1602.py - Display text on a LCD screen attached to the rasperry pi GPIO pins.
* LCD1602.py - Controller for the LCD that I have in my Freenove RFID kit.
* clear_lcd.py - Clear the lcd screen attached to the Raspberry pi.

### Lcd folder
* button_test.py - Toggle a LED with a button.
* test.py - Misc led testing.
* toggle_led.py - Toggle a LED using terminal input and gpiozero.
* turn_leds_off.py - Turn all LEDs off that are connected
* turn_leds_on.py - Turn all LEDs on that are connected

### Test folder
* header-info-rpi.py - Shows the pinout for the current Raspberry Pi Board.
* os_check.py - Show your operating system, should work for Windows, Linux, and Mac.
* ping_test.py - This pings my website, I'm quite sure this requires root though.
* rpi_info.py - Show a list of all details about the current Raspberry Pi Board.
* send_email.py - Test sending an email with python, I couldn't get it to work with gmail.
* system_info.py - Show the cpu frequency, disk usage, ram usage, network usage and more, I would like to set this up to show 
 on my screen for the Raspberry pi 4
* system_info_old.py - Old version of above file
* whois-lookup.py - Show websites whois info, currently set to my website.

### Tkinter (Under test folder)
* led_control.py - Contains a led controller using tkinter. 
* tab_test.py - Most of my testing in tkinter, password hashing, dialog boxes and more.