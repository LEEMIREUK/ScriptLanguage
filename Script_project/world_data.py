from tkinter import *
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib import animation, rc

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time

def Print_worldMap(window):
    worldmap = Label(window)
    file_image = Image.open('image/세계지도.png')
    worldmap.image = ImageTk.PhotoImage(file_image)
    worldmap = Label(image = worldmap.image)
    worldmap.place(x=100, y=150)

def Pie_Graph(window):
    # lb1 = Label(window, text='대륙별 코로나 확진자 비율')
    # lb1.place(x=200, y=100)
    g_continent = ['Africa', 'Europe', 'America', 'Middle East', 'Asia', 'Oceania']
    g_value = [10, 20, 30, 10, 25, 5]
    g_color = ('coral', 'yellowgreen', 'lightcoral', 'thistle', 'orange', 'lightskyblue')
    pie = plt.pie(g_value, labels=g_continent, colors=g_color, autopct='%1.1f%%',
    shadow=True, startangle=90, textprops={'fontsize': 9})
    plt.axis('equal')

    plt.pie(g_value, labels=g_continent, colors=g_color, autopct='%1.1f%%',
            shadow=True, startangle=90, textprops={'fontsize': 9})
    plt.axis('equal')
    plt.title('대륙별 코로나 확진자 비율', fontsize=14)
    plt.show(window)


def Bar_Graph(window):
    fig, ax = plt.subplot()


#    plt.bar(index, y1_value, bar_width,
