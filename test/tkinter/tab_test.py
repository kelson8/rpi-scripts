
import tkinter as tk
from tkinter import ttk, messagebox

# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Led Controller')
tabControl.add(tab2, text ='Test')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab2).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

def show_message_box():
    # messagebox.showinfo("Info test", "Test message")
    messagebox.showerror("Error test", "Error message")

# Led controller tab

ttk.Label(tab1, text="Welcome to the LED Controller.").grid(column=0, row=0)
# Add a quit button to this
ttk.Button(tab1, text="Quit", command=root.destroy).grid(column=3, row=4)


# End led controller tab

# Test tab
ttk.Button(tab2, text="Test", command=show_message_box).grid(column=3, row=4)
ttk.Label(tab2, text="Welcome to the test tab.").grid(column=0, row=0)

# End test tab

root.mainloop()
