import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=500)
frm.grid()
ttk.Label(frm, text="text.txt").grid(column=0, row=0)
ttk.Button(frm, text="implode", command=root.destroy).grid(column=25, row=25)
btn = ttk.Button(frm,)
print(btn.configure().keys())
print(btn.configure(width=10))
root.mainloop()