import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
class MyGUI(tk.Tk):
    def __init__(self,master):
        self.fig=Figure(figsize=(5,5),dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig,master)
        self.toolbar=NavigationToolbar2Tk(self.canvas,master)
        #self.toolbar.update()
        self.canvas._tkcanvas.pack(padx=20, pady=20)
root =tk.Tk()
window=MyGUI(root)
root.mainloop()