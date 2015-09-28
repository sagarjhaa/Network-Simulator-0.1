__author__ = 'sjha1'

import ctypes
from Tkinter import *
user32 = ctypes.windll.user32
WIDTH,HEIGHT = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)
canvasWidth,canvasHeight,margin_x, margin_y = WIDTH, HEIGHT,WIDTH/2,HEIGHT/2
WIDTH -= 20
HEIGHT -= 75
#canvasWidth,canvasHeight,margin_x, margin_y = WIDTH, HEIGHT,WIDTH, HEIGHT
BACKGROUND = "Grey"



def writeCalculations(widget,text,error,NB):
    if error:
        widget.tag_configure('error',foreground='red')
        widget.insert(END,text,'error')
    else:widget.insert(END,text)
    NB.select(1)
    widget.insert(END,"\n")

