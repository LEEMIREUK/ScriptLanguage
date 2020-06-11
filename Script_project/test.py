from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
window_width = 1000
window_height = 600
root = Tk()
global_fig = None
def create_draw(x_dots, y_dots):
    global global_fig
    if global_fig is not None:
        global_fig.clf()
    global_fig = Figure(figsize=(5, 4), dpi=100)
    global_fig.add_subplot(111).plot(x_dots, y_dots)
    canvas = FigureCanvasTkAgg(global_fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    root.update()
    global_fig.canvas.draw()

create_draw([3, 4], [2, 3])
root.mainloop()
