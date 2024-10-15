import tkinter as tk
from tkinter import ttk, messagebox, Entry
import hashlib
import binascii
import os

# Add my password hashing file.
# from password_hasherSHA512 import hash_password, verify_password, password_checker
from password_hasherSHA512 import *

# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/

root = tk.Tk()
root.title("KCNet Systems")
tabControl = ttk.Notebook(root)

# I plan on using this on the screen once I get it for the Rpi4
root.geometry('640x400')

#######
# Tabs and names
#######

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Main')
tabControl.add(tab2, text ='Test')
tabControl.add(tab3, text ='Login')
tabControl.add(tab4, text ='Register')
tabControl.add(tab5, text ='Led Control')

tabControl.pack(expand = 1, fill ="both")

#######
# End Tabs and names
#######

#######
# Tab grids
#######

ttk.Label(tab1).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab2).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab3).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab4).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab5).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

#######
# End Tab grids
#######

#######
# Functions
#######

# def show_message_box(message):
def show_message_box():
    messagebox.showinfo("Info test", "Test message")
    # messagebox.showinfo("Info test", message)

# def show_error_message(message):
def show_error_message():
    messagebox.showerror("Error test", "Error, mistake made.")

# def show_continue_dialog(message):
def show_continue_dialog():
    # messagebox.askokcancel("Continue?", message)
    messagebox.askokcancel("Continue?", "Continue the download?")

def print_test():
    print(f"Hello user kelson8")

def welcome_message():
    print("Welcome to KCNet Systems")

#######
# End functions
#######

#######
# String vars
#######

# https://www.geeksforgeeks.org/python-tkinter-entry-widget/
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()

user_name_var = tk.StringVar()
password_var = tk.StringVar()

#######
# End string vars
#######

#######
# Misc functions
#######

def submit():
    # Get the values
    first_name = first_name_var.get()
    last_name = last_name_var.get()

    # Print the values
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")

    # Reset the values
    first_name_var.set("")
    last_name_var.set("")

# debug_mode = False
def login():
    user_name = user_name_var.get()
    password = password_var.get()

    # SHA512 hash of the password "test"
    tmp_password_hash = "64c6167a48f9d45f2da8073ba569d605ac6d12cece7aeec7b38a4db4bf782051f15554c83de5c757c0ae1db563c90c163f3132c869cacdf03bb2fe94ac62321c455e480fcf7fb7791acb2d2945c87b4171e5599c38d3691fcb957185d8fc9bc1"
    # Print the values
    # TODO Figure out how to store these in a text file, hashing the password,
    #  eventually figure out how to hook this up to a Mariadb or MySql DB.
    print(f"Username: {user_name}")
    print(f"Password (Hashed): {hash_password(password)}")
    # Possibly remove the clear password from this, it's only really for testing and should never be used in production.
    # if debug_mode:
    #     print(f"Password (Clear): {password}")

    # Verify the password with the above hash, this is only needed for auth and i'll disable it for now.

    if verify_password(tmp_password_hash, password):
        print("Password is valid.")
    else:
        print("Password is invalid.")
    # print(f"Is password valid: {verify_password(tmp_password_hash, password)}")

    # Reset the values
    user_name_var.set("")
    password_var.set("")

#######
# End misc functions
#######

#######
# Led controller tab
#######

# ttk.Label(tab1, text="Welcome to the LED Controller.").grid(column=0, row=0)

ttk.Label(tab1, text="Welcome to KCNet Systems.").grid(column=0, row=0)

# led_controller_label = ttk.Label(tab1, text="Welcome to the LED Controller.", justify="center")
# Align the items to the grid.
# https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside
# led_controller_label.grid()

# Add a quit button to this
ttk.Button(tab1, text="Quit", command=root.destroy).grid(column=1, row=1)

# quit_button = ttk.Button(tab1, text="Quit", command=root.destroy)

# quit_button.grid()

#######
# End led controller tab
#######

# Spacer
# https://stackoverflow.com/questions/39555194/how-to-add-space-between-two-widgets-placed-in-grid-in-tkinter-python
spacer1 = tk.Label(tab2, text="")
spacer1.grid(column=0, row=4)

#######
# Test tab
#######
ttk.Label(tab2, text="Welcome to the test tab.").grid(column=0, row=0)

# Column 1
# TODO Figure out how to get the values for this from a text box.
ttk.Button(tab2, text="Info message", command=show_message_box).grid(column=1, row=1, padx=10, pady=5)
ttk.Button(tab2, text="Error message", command=show_error_message).grid(column=1, row=2, padx=10, pady=5)
ttk.Button(tab2, text="Ok/Cancel Dialog", command=show_continue_dialog).grid(column=1, row=3, padx=10, pady=5)

# Adding padx and pady seems to add spacing to these, I set a value of 10 for x and 5 for y for now.
ttk.Button(tab2, text="Print #1", command=print_test).grid(column=1, row=4, padx=10, pady=5)
ttk.Button(tab2, text="Print #2", command=welcome_message).grid(column=1, row=5, padx=10, pady=5)



# Column 2
ttk.Label(tab2, text="First Name").grid(column=2, row=1, padx=10, pady=5)
ttk.Label(tab2, text="Last Name").grid(column=2, row=2, padx=10, pady=5)

# Column 3
# Oops I forgot to add textvariable to these to store the variables
tk.Entry(tab2, textvariable=first_name_var).grid(column=3, row=1, padx=10, pady=5)
tk.Entry(tab2, textvariable=last_name_var).grid(column=3, row=2, padx=10, pady=5)
ttk.Button(tab2, text="Submit", command=submit).grid(column=3, row=3, padx=10, pady=5)

# b1 = tk.Button(tab2, text="Submit", command=submit)

#######
# End test tab
#######

#######
# Login tab
#######

# ttk.Button(tab2, text="Print #2", command=welcome_message).grid(column=2, row=5, padx=10, pady=5)
ttk.Label(tab3, text="Username").grid(column=2, row=4, padx=10, pady=5)
ttk.Label(tab3, text="Password").grid(column=2, row=5, padx=10, pady=5)

ttk.Entry(tab3, textvariable=user_name_var).grid(column=3, row=4, padx=10, pady=5)
ttk.Entry(tab3, textvariable=password_var, show="*").grid(column=3, row=5, padx=10, pady=5)

# Login test
ttk.Button(tab3, text="Login", command=login).grid(column=3, row=6, padx=10, pady=5)
# b1.grid(column=3, row=3, padx=10, pady=5)

#######
# End login tab
#######

root.mainloop()
