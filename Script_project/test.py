from tkinter import *
class frame(Frame):
    def __init__(self,display):
        Frame.__init__(self,display)
        l = Label(self,text="frame1")
        l.pack()
class frame2(Frame):
    def __init__(self,display):
        Frame.__init__(self,display)
        l = Label(self,text="frame2")
        l.pack()
class test(Tk):
    def __init__(self):
        Tk.__init__(self)
        f2 = frame2(self)
        f2.grid(row=0)
        #To raise the first frame, I used the following
        frame2.grid_remove()
        f = frame(self)
        f.grid(row=0)
t = test()
t.mainloop()