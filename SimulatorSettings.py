__author__ = 'sjha1'

from  Tkinter import *
from constants import *
import random as rd
from Node import *
import snap
from shortestpath import *

#Nodes_List = []
COLOR_LIST = ["Red", "Green", "Blue", "White"]
COUNTER=1

class simulatorWidget():
    def __init__(self,master,pre_canvas):
        top = self.top = Toplevel(master)

        self.top.title("Simulator Settings")
        self.top.geometry('%dx%d+%d+%d' % (300,300,10,500))
        self.top.resizable(False,False)
        self.top.configure(background=BACKGROUND)
        self.Nodes_List = []

        self.pre_canvas = pre_canvas
        self.canvas = pre_canvas.mainCanvas

        self.lb_nodes = Label(top,text="No. of Nodes",background=BACKGROUND)
        self.lb_nodes.grid(row = 0,column = 0,sticky=(N,W),padx=10)

        self.txt_nodes = Entry(top,font="Helvetica 16",width=10)
        self.txt_nodes.grid(row = 0,column = 1,sticky= (N,W),padx=10)

        self.lbl_Network = Label(top,text="Network ",background=BACKGROUND)
        self.lbl_Network.grid(row=1,column=0,sticky=(N,W),padx=10,pady=10)

        self.var_network = StringVar(top)
        self.var_network.set("Select Network")

        self.network_option = OptionMenu(top,self.var_network,"GenStar","GenRndGnm","GenForestFire","GenFull")
        self.network_option.grid(row=1,column=1,sticky=(N,W),padx=10,pady=10)

        self.drawNodes = Button(top,text="Viz. Network",command=self.draw,background=BACKGROUND)
        self.drawNodes.grid(row=2,column=0,sticky=(N,W),padx=10,pady=10)

        self.lbl_commDetect = Label(top,text="Community Detection",background=BACKGROUND)
        self.lbl_commDetect.grid(row=3,column=0,sticky=(N,W),padx=10,pady=10)

        self.txt_commDetect = Entry(top,font="Helvetica 16",width=10)
        self.txt_commDetect.grid(row=3,column=1,sticky=(N,W),padx=10,pady=10)

        self.btn_commDetect = Button(top,text="Detect Community",background=BACKGROUND,command=self.commDetection)
        self.btn_commDetect.grid(row=4,column=0,sticky=(N,W),padx=10,pady=10)

        self.resetButton = Button(top,text="Reset",command=self.reset,background=BACKGROUND)
        self.resetButton.grid(row=5,column=0,sticky=(N,W),padx=10,pady=10)

        self.shortDButton = Button(top,text="Shortest Path",background=BACKGROUND,command=self.find_short_path)
        self.shortDButton.grid(row=5,column=1,sticky=(N,W),padx=10,pady=10)

    def read_nodes(self):
        self.Nodes = self.txt_nodes.get()
        if self.Nodes <> "":
            self.lst_Nodes =self.Nodes.split(",")
        else:
            print "Please enter nodes"

    def create_nodes(self,Graph):
        color = rd.choice(COLOR_LIST)
        for node in Graph.Nodes():
            polygon = rd.randint(1,len(self.pre_canvas.polygon_dict))
            direction = self.pre_canvas.polygon_dict[polygon]

            if direction[0][0] == direction[0][1]:
                direction[0][0] = direction[0][0] - 1
            if (direction[1][0] == direction[1][1]):
                direction[1][0] = direction[1][0] - 1

            tempVar = False
            i = 1
            while not tempVar:
                x = rd.randrange(direction[0][0],direction[0][1])
                y = rd.randrange(direction[1][0],direction[1][1])
                tempVar =  self.point_inside_polygon(x,y,direction[2])
                i = i + 1
                if i >25:
                    break

            #print "x ",x," y ",y,
            p = Node(node.GetId(),[x,y],color)
            p.draw(self.canvas)
            self.canvas.tag_bind(p.itemNo, '<ButtonPress-1>', self.__showAttriInfo)
            self.Nodes_List.append(p)

        for node in Graph.Nodes():
            follower = []
            for EI in Graph.Edges():
                if EI.GetSrcNId() == node.GetId():
                    if EI.GetSrcNId() <> EI.GetDstNId():
                        follower.append(self.Nodes_List[EI.GetDstNId()])
            nodeid = node.GetId()
            self.Nodes_List[nodeid].followers = follower
            self.Nodes_List[nodeid].draw_edges(self.canvas)
            #print nodeid,len(follower)

    def draw(self):
        self.read_nodes()
        self.Network = self.var_network.get()
        self.nPoints = sum(int(i) for i in self.lst_Nodes)

        if self.Network == "GenStar":
            print "GenStar is the network with points ",self.nPoints
            graph = snap.GenStar(snap.PNGraph, self.nPoints, True)

        if self.Network == "GenRndGnm":
            print "GenRndGnm is the network with points ",self.nPoints
            graph = snap.GenRndGnm(snap.PNGraph,self.nPoints, self.nPoints)

        if self.Network == "GenForestFire":
            print "GenForestFire is the network with points ",self.nPoints
            graph = snap.GenForestFire(self.nPoints, 0.5,0.5)

        if self.Network == "GenFull":
            print "GenFull is the network with points ",self.nPoints
            graph = snap.GenFull(snap.PNGraph,self.nPoints)

        if self.Network == "GenCircle":
            print "GenCircle is the network with points ",self.nPoints
            graph = snap.GenCircle(snap.PNGraph,self.nPoints,10,10)

        self.create_nodes(graph)

        # for node in Graph.Nodes():
        #     follower = []
        #     for EI in Graph.Edges():
        #         if EI.GetSrcNId() == node.GetId():
        #             if EI.GetSrcNId() <> EI.GetDstNId():
        #                 follower.append(EI.GetDstNId())
        #     print node.GetId(),follower
        #
        #
        # for node in self.Nodes_List:
        #     str1 = ""
        #     for foll in node.followers:
        #         str1 = str1 + "," + str(foll.id)
        #     print node.id,str1

    def commDetection(self):
        #print "Community Detection Function"
        threshold = self.txt_commDetect.get()
        try:
            threshold = int(threshold)
            if threshold > 0 and type(threshold) == int:
                g = {}
                for node in self.Nodes_List:
                    if len(node.followers) > 0:
                        g[node.id]=[]
                        #print node.id,node.followers
                        for foll in node.followers:
                            g[node.id].append(foll.id)

                #print g
                graph = Graph(g,self.Nodes_List,self.canvas,threshold)
                graph.find_community()
                graph.change_color()
            #else:
            #    print "Enter positive threshold"
        except:
            print "Enter positive threshold"

    def point_inside_polygon(self,x,y,poly):

        n = len(poly)/2
        inside =False

        p1x = poly[0]
        p1y = poly[1]
        #print p1x,p1y
        for i in range(0,n+1,1):
            p2x = poly [(i%n)*2]
            p2y = poly [(i%n)*2 +1]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside

    def find_short_path(self):
        dict = Generate_Dictionary_Simulation(self.Nodes_List)
        Generate_Graph(dict)

    def reset(self):
        for node in self.Nodes_List:
            self.canvas.delete(node.itemNo)
            for edges in node.lineItemNo:
                self.canvas.delete(edges)
        self.Nodes_List = []

    def __showAttriInfo(self,event):
        """
        Show attribute information of clicked unit
        """
        widget_id=event.widget.find_closest(event.x, event.y)

        print "x ",self.canvas.gettags(widget_id)[0]," y ",self.canvas.gettags(widget_id)[1]

class Graph():
    def __init__(self,g,Node_List,canvas,threshold):
        self.g = g
        self.total_community = []
        self.weights = []
        self.keys = []
        self.Node_List = Node_List
        self.canvas = canvas
        self.threshold = threshold

    def max_weight(self):
        self.weights = []
        self.keys = []
        for node,connections in self.g.items():

            self.keys.append(node)
            self.weights.append(len(connections))
        try:
            #print len(self.keys),self.keys
            maximum_weight = max(self.weights)
            temp = self.weights.index(maximum_weight)

            return self.keys[temp]
        except:
            return None

    def find_community(self):
        while len(self.g.keys()) <> 0:
            node = self.max_weight()
            self.delete(node)
            self.c = Community(node,self.threshold)
            while self.c.members(self.g):
                node = self.max_weight()
                self.c.add_descendants(node)
                self.delete(node)
            self.total_community.append(self.c)
            print self.c
        print "Completed finding community"

    def change_color(self):

        for node in self.Node_List:
            item = node.itemNo
            self.canvas.itemconfig(item,fill="white")


        for community in self.total_community:
            r = lambda: rd.randint(0,255)
            a = ('#%02X%02X%02X' % (r(),r(),r()))

            if None not in community.descendants:
                parent = community.parent

                i = self.Node_List[parent].itemNo
                self.canvas.delete(i)
                self.Node_List[parent].drawRectangle(self.canvas) #,6*len(community.descendants)

                i = self.Node_List[parent].itemNo
                self.canvas.itemconfig(i,fill=a)

                for foll in community.descendants:
                    #print parent,foll
                    i = self.Node_List[foll].itemNo
                    self.canvas.itemconfig(i,fill=a)

            else:
                pass
                #print "sagar ", community

    def delete(self,node):
        try:
            self.g.pop(node)
        except:
            pass
            #print "Cannot delete None Key"

    def followers(self,node):
        return self.g[node]

class Community():
    def __init__(self,parent,threshold):
        self.parent = parent
        self.descendants =  []
        self.threshold = threshold

    def __str__(self):
        string = "Parent: "+str(self.parent)+ " Decendents: " +str(self.descendants)
        return string

    def add_descendants(self,node):
        self.descendants.append(node)

    def members(self,g):
        global threshold
        if g.keys() <> 0 and len(self.descendants) < self.threshold:
            return True
        return False

def maindraw():
    pass




