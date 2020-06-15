import numpy
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk
import time

def Print_worldMap(window):
    worldmap = Label(window)
    file_image = Image.open('image/세계지도.png')
    worldmap.image = ImageTk.PhotoImage(file_image)
    worldmap = Label(image = worldmap.image)
    worldmap.place(x=100, y=150)

def Show_PieGraph(window):
    g_continent = ['Africa', 'Europe', 'America', 'Middle East', 'Asia', 'Oceania']
    g_value = [10, 20, 30, 10, 25, 5]
    g_color = ['#aa5555', '#27b920', '#ca88ab', '#a2a2a2', '#f1ff9f', '#78c4fc']
    plt.pie(g_value, labels=g_continent, colors=g_color, shadow=True, startangle=90)
    plt.show(window)


def Show_Graph(window):
    x_country = ()
    y_value =()
    index = numpy.arange()

#    plt.bar(index, y1_value, bar_width,
