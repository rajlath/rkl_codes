
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03 10:10:14
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : PYTHON_GUI_PROGRAMMING_COOKBOOK_SECOND_EDITION.pdf
# @Version : 1.0.0

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

win = tk.Tk()
win.title("Python GuI")
a_label = ttk.Label(win, text="Please enter your name.")
a_label.grid(column= 0, row= 0)



def click_me():
    action.configure(text="Hello " + name.get() +" "+ number_choosen.get())

action = ttk.Button(text="Click Me.", command=click_me)
action.grid(column=2, row=1)
#action.configure(state="disabled")

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable= name)
name_entered.grid(column=0, row=1)

numbers = tk.StringVar()
number_choosen = ttk.Combobox(win, width=12, textvar=numbers, state="readonly")
number_choosen["values"] = (1, 2, 3, 4, 5)
number_choosen.grid(column = 1, row = 1)
number_choosen.current(0)

chVarDis = tk.Checkbutton()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()

chVarUn = tk.Checkbutton()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=4, sticky = tk.W)

chVarUn = tk.Checkbutton()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check1.deselect()
check2.grid(column=1, row=4, sticky = tk.W)

chVarEn = tk.Checkbutton()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky = tk.W)

#!Radio button globals
COLOR = ["Blue","Gold","Red"]

#*Radio Button Callback
def radCall():

    radSel = radVar.get()
    if   radSel  == 1: win.configure(background=COLOR1)
    elif radSel  == 2: win.configure(background=COLOR2)
    elif radSel  == 3: win.configure(background=COLOR3)

radVar = tk.IntVar()
#radVar = set(99)
for col in range(3):
    curRad = tk.Radiobutton(win, text = COLOR[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column = 0, row=5, sticky = tk.W, columnspan = 3)


scroll_W = 30
scroll_h = 3

scr = ScrolledText(win, width=scroll_W, height=scroll_h, wrap=tk.WORD)
scr.grid(column = 0, columnspan=3)




name_entered.focus()











win.mainloop()
