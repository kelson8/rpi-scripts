from tkinter import *
from tkinter import ttk

from gpiozero import LED, Button, Device
import time
import RPi.GPIO as GPIO
import datetime

# https://tkdocs.com/tutorial/firstexample.html

root = Tk()
root.title("Hello World")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainFrame, text="Welcome to KCNet").grid(column=0, row=0, sticky=W)

test = StringVar()
test_entry = ttk.Entry(mainFrame, width=20, textvariable=test)
test_entry.grid(column=2, row=1, sticky=(W, E))

test1 = StringVar()
ttk.Label(mainFrame, textvariable=test1).grid(column=2, row=2, sticky=(W, E))
# ttk.Checkbutton(mainFrame)

def print_test1(username):
    print("Hello " + username)

ttk.Button(mainFrame, text="Click me", command=print_test1("kelson8")).grid(column=3, row=3, sticky=W)


for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root.mainloop()

