from tkinter import scrolledtext as tkst
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk


matplotlib.use('TkAgg')

ww = tk.Tk()

datalst = [31, 41, 59, 26, 53, 58, 97, 96, 36]
ff = Figure(figsize=(6,6), dpi=100)
xx = ff.add_subplot(111)
ind = np.arange(len(datalst))
rects1 = xx.bar(ind, datalst, 0.8)
canvas = FigureCanvasTkAgg(ff, master=ww)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT)


ww.mainloop()