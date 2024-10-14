from tkinter import *
from tkinter import ttk, messagebox
from gpiozero import LED, Button
from time import sleep

green_led = LED(16)
yellow_led = LED(20)
red_led = LED(21)
button = Button(4)

# https://tkdocs.com/tutorial/firstexample.html
# https://realpython.com/python-gui-tkinter/

root = Tk()
root.title("KCNet Led Control")

# New for tabs
# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
# tabControl = ttk.Notebook(root)
#
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
#
#
# tabControl.add(tab1, text="Tab 1")
# tabControl.add(tab2, text="Tab 2")
#
# tabControl.pack(expand=1, fill="both")

# End tabs

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainFrame, text="Welcome to the LED Controller.").grid(column=0, row=0, sticky=(W, N))

# Begin of label box
ttk.Label(mainFrame, text="Test: ").grid(column=0, row=1, sticky=NE)

# Adds the label box to write in
test = StringVar()
test_entry = ttk.Entry(mainFrame, width=20, textvariable=test)
test_entry.grid(column=2, row=1, sticky=(W, E))

test1 = StringVar()
ttk.Label(mainFrame, textvariable=test1).grid(column=2, row=2, sticky=(W, E))
# ttk.Checkbutton(mainFrame)

def print_test1(username):
    print("Hello " + username)

# TODO Setup this to toggle on/off the leds on the rpi, attach this to the touch screen when I buy it.
def toggle_green_led():
    green_led.toggle()

def toggle_yellow_led():
    yellow_led.toggle()

def toggle_red_led():
    red_led.toggle()

def show_message_box():
    messagebox.showinfo("Info test", "Test message")

def blink_leds():
    green_led.blink()
    yellow_led.blink()
    red_led.blink()

ttk.Button(mainFrame, text="Click me", command=print_test1("kelson8")).grid(column=3, row=3, sticky=W)
ttk.Button(mainFrame, text="Message Box", command=show_message_box).grid(column=3, row=3, sticky=W)

# Led toggles
# ttk.Button(root, text="Turn on green led").grid(column=0, row=2, sticky=E)

ttk.Checkbutton(mainFrame, text="Toggle Green led", onvalue=1, offvalue=0, command=toggle_green_led).grid(column=2, row = 2)
ttk.Checkbutton(mainFrame, text="Toggle Yellow led", onvalue=1, offvalue=0, command=toggle_yellow_led).grid(column=2, row = 3)
ttk.Checkbutton(mainFrame, text="Toggle Red led", onvalue=1, offvalue=0, command=toggle_red_led).grid(column=2, row = 4)

ttk.Button(mainFrame, text="Blink leds", command=blink_leds).grid(column=2, row=5, sticky=W)
ttk.Button(mainFrame, text="Stop blinking leds", command=blink_leds).grid(column=2, row=5, sticky=W)

# ttk.Checkbutton(mainFrame, text="Test", onvalue=1, offvalue=0, command=print_test).grid(column=2, row = 2)



# Add a quit button to this
ttk.Button(mainFrame, text="Quit", command=root.destroy).grid(column=3, row=4)

for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root.mainloop()

