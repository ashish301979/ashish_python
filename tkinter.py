#!/usr/bin/python
from Tkinter import *
import Tkinter as ttk
root = Tk()

button = ttk.Button(root, text = 'Click Me')
button.pack()
def rang():
	print(range(0,100,5))
button.config(command = rang)


root.mainloop()
