import tkinter as tk
from tkinter import ttk, messagebox, Entry
from tkinter.ttk import *

root = tk.Tk()
root.title("KCNet Systems")
tabControl = ttk.Notebook(root)

# I plan on using this on the screen once I get it for the Rpi4
root.geometry('640x400')

# Main
tab1 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Main')

tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1).grid(column = 0,
row = 0,
padx = 30,
pady = 30)

ttk.Label(tab1, text="Big font test", font=("Times", 16)).grid(column=0, row=0, padx=10, pady=5)
ttk.Label(tab1, text="Big font test", font=("Times", 16)).grid(column=0, row=1, padx=10, pady=5)
ttk.Label(tab1, text="Big font test", font=("Times", 16)).grid(column=0, row=2, padx=10, pady=5)
ttk.Label(tab1, text="Big font test", font=("Times", 16)).grid(column=0, row=3, padx=10, pady=5)
ttk.Label(tab1, text="Big font test", font=("Times", 16)).grid(column=0, row=4, padx=10, pady=5)

root.mainloop()