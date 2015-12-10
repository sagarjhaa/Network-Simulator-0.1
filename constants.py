__author__ = 'sjha1'

import ctypes
from Tkinter import *
user32 = ctypes.windll.user32
WIDTH,HEIGHT = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)

canvasWidth,canvasHeight,margin_x, margin_y = WIDTH-940, HEIGHT-60,WIDTH/2 - 400,HEIGHT/2
WIDTH -= 20
HEIGHT -= 75
BACKGROUND = "Grey"

def writeCalculations(widget,text,error,NB=None):
    if error:
        widget.tag_configure('error',foreground='red')
        widget.insert(END,text,'error')
        NB.select(1)
    else:widget.insert(END,text)

    widget.insert(END,"\n")

