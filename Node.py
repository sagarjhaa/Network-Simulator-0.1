'''
Created on March 17, 2015
@author: sagar jha
'''
from Tkinter import *

PARTICLE_RADIUS = 10
H_PARTICLE_RADIUS = PARTICLE_RADIUS/2
class Node:
    '''
    classdocs
    '''
  
    def __init__(self,id,position,color):
        '''
        Constructor
        '''
        self.id=id
        self.position = position
        self.color = color
        self.itemNo = 0
        self.followers = 0
        self.lineItemNo = []

    # draw method for particles
    def draw(self,canvas,radius=0):
        if radius == 0:
            self.itemNo = canvas.create_oval(self.position[0],self.position[1],self.position[0]+PARTICLE_RADIUS,
                                             self.position[1]+PARTICLE_RADIUS,fill=self.color,tags = (self.position[0],self.position[1]))
        else:
            self.itemNo = canvas.create_oval(self.position[0],self.position[1],self.position[0]+radius,
                                             self.position[1] + radius,fill=self.color)

    def drawRectangle(self,canvas):
        x1 = self.position[0]
        y1 = self.position[1]

        x2 = x1 + 20
        y2 = y1

        x3 = x2
        y3 = y2 + 20

        x4 = x1
        y4 = y1 + 20

        self.itemNo = canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,fill = self.color)

    #Update Coordinate
    def update(self,canvas):
        canvas.coords(self.itemNo,self.position[0],self.position[1],self.position[0]+PARTICLE_RADIUS,self.position[1]+PARTICLE_RADIUS)

    def draw_edges(self,canvas):
        if len(self.followers) <> 0:
            for eNode in self.followers:
                itemNo = canvas.create_line(self.position[0]+H_PARTICLE_RADIUS,self.position[1]+H_PARTICLE_RADIUS,eNode.position[0]+H_PARTICLE_RADIUS,eNode.position[1]+H_PARTICLE_RADIUS,fill="red",dash=(4,4))
                self.lineItemNo.append(itemNo)

    def show_edges_toggle(self,canvas,toggle):
        if toggle:
            for line in self.lineItemNo:
                canvas.itemconfig(line,state=HIDDEN)
        else:
            for line in self.lineItemNo:
                canvas.itemconfig(line,state=NORMAL)

    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color




    
