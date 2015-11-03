'''
Created on March 17, 2015

@author: sagar jha
'''
PARTICLE_RADIUS = 10
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
                                             self.position[1]+PARTICLE_RADIUS,fill=self.color)
        else:
            self.itemNo = canvas.create_oval(self.position[0],self.position[1],self.position[0]+radius,
                                             self.position[1] + radius,fill=self.color)

#Update Coordinate
    def update(self,canvas):
        canvas.coords(self.itemNo,self.position[0],self.position[1],self.position[0]+PARTICLE_RADIUS,self.position[1]+PARTICLE_RADIUS)


    def draw_edges(self,canvas):
        if len(self.followers) <> 0:
            for eNode in self.followers:
                itemNo = canvas.create_line(self.position[0],self.position[1],eNode.position[0],eNode.position[1],fill="red")
                self.lineItemNo.append(itemNo)


    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color




    
