__author__ = 'sjha1'

from  Tkinter import *
from constants import *
import random as rd
from Node import *

DIRECTION_LIST = [[0.1,0], [0, 0.1], [-0.1, 0], [0, -0.1]]
Nodes_List = []
COLOR_LIST = ["Red", "Green", "Blue", "White"]
COUNTER=1


class simulatorWidget():
    def __init__(self,master,pre_canvas):
        top = self.top = Toplevel(master)

        self.top.title("Simulator Settings")
        self.top.geometry('%dx%d+%d+%d' % (300,250,10,500))
        self.top.resizable(False,False)
        self.top.configure(background=BACKGROUND)

        self.pre_canvas = pre_canvas
        self.canvas = pre_canvas.mainCanvas

        self.lb_nodes = Label(top,text="No. of Nodes",background=BACKGROUND)
        self.lb_nodes.grid(row = 0,column = 0,sticky=(N,W),padx=10)

        self.txt_nodes = Entry(top,font="Helvetica 16")
        self.txt_nodes.grid(row = 0,column = 1,sticky= (N,E),padx=10)

        self.drawNodes = Button(top,text="Draw Nodes",command=self.draw)
        self.drawNodes.grid(row=1,column=0)

        self.readButton = Button(top,text="Reset",command=self.reset)
        self.readButton.grid(row=1,column=1)

    def read_nodes(self):
        self.Nodes = self.txt_nodes.get()
        if self.Nodes <> "":
            self.lst_Nodes = self.Nodes.split(",")
        else:
            print "Please enter nodes"

    def create_nodes(self):
        global Nodes_List
        self.read_nodes()

        for PARTICLE in self.lst_Nodes:


            for i in range(int(PARTICLE)):
                color = rd.choice(COLOR_LIST)
                polygon = rd.randint(1,len(self.pre_canvas.polygon_dict))
                direction = self.pre_canvas.polygon_dict[polygon]
                x = rd.randint(direction[0][0],direction[0][1])
                y = rd.randint(direction[1][0],direction[1][1])
                p = Node([x,y], color)
                Nodes_List.append(p)

    def draw(self):
        global Nodes_List
        self.create_nodes()
        itemNo = []
        for i in Nodes_List:
            print i
            i.draw(self.canvas)
            #itemNo.append()



    def reset(self):
        global COUNTER,Nodes_List
        self.canvas.delete(ALL)
        COUNTER = 1
        Nodes_List = []


def maindraw():
    pass




