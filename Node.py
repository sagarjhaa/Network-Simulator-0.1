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

    # draw method for particles
    def draw(self,canvas):
        self.itemNo = canvas.create_oval(self.position[0],self.position[1],self.position[0]+PARTICLE_RADIUS,self.position[1]+PARTICLE_RADIUS,fill=self.color)

    #Update Coordinate
    def update(self,canvas):
        canvas.coords(self.itemNo,self.position[0],self.position[1],self.position[0]+PARTICLE_RADIUS,self.position[1]+PARTICLE_RADIUS)


    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color




    
