import random
import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=400)
frm.grid()
ttk.Label(frm, text="text.txt").grid(column=(random.randint(1,20)), row=(random.randint(1,20)))
ttk.Button(frm, text="implode", command=root.destroy).grid(column=(random.randint(1,20)), row=(random.randint(1,20)))
btn = ttk.Button(frm,text="click if austen",command=root.grid(c
print(btn)
root.mainloop()
