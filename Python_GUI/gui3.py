
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03 10:10:14
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : PYTHON_GUI_PROGRAMMING_COOKBOOK_SECOND_EDITION.pdf
# @Version : 1.0.0

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GuI")
#win.resizable(True, False)
ttk.Label(win, text="A Label").grid(column=0, row=0)



win.mainloop()
