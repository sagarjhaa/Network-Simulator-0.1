__author__ = 'sjha1'

'''
The module is developed to read the .csv file from tweeter and
prepare graphs on the network based in the file
'''

from Tkinter import Tk
from tkFileDialog import askopenfilename

import csv
##from igraph import *
import igraph as igraph
import numpy as np

SOURCE_COL = 0
TARGET_COL = 1

#Open the dialog box to read the file path
Tk().withdraw()

#filepath = "C:/Users/sjha1/Desktop/sb277-new.csv"
#print(filepath)

def Generate_Graph(Source_Target_Dict):
    print "Received Data"
    #print Source_Target_Dict
    g = igraph.Graph(directed=False)
    Completed_Nodes = []
    Source_Target_List = []
    Node_Counter = 0
    visual_style = {}

    for key,values in Source_Target_Dict.items():
        if key not in Completed_Nodes:
            g.add_vertices(1)
            Completed_Nodes.append(key)
            Source_Target_List.append("Source")
            Node_Counter = Node_Counter + 1
        else:
            Node_Counter = Completed_Nodes.index(key) + 1

        for value in values:
            if value not in Completed_Nodes:
                g.add_vertices(1)
                g.add_edges([(Node_Counter-1,Node_Counter)])
                Node_Counter = Node_Counter + 1
                Completed_Nodes.append(value)
                Source_Target_List.append("Target")
            else:
                g.add_edges([(Node_Counter-1,Completed_Nodes.index(value))])

    # Adding all the Source Nodes with attribute Name
    g.vs["label"] = Completed_Nodes
    g.vs["Identity"] = Source_Target_List

    #color_dict = {"Source":"Blue","Target":"Black"}
    #g.vs["color"] = [color_dict[Identity] for Identity in g.vs["Identity"]]

    outdegree = g.outdegree()
    indegree = g.indegree()
    colours = ['#fecc5c', '#a31a1c']
    bins = np.linspace(0, max(outdegree), len(colours))
    digitized_degrees =  np.digitize(outdegree, bins)
    g.vs["color"] = [colours[x-1] for x in digitized_degrees]

    # Also color the edges
    for ind, color in enumerate(g.vs["color"]):
        edges = g.es.select(_source=ind)
        edges["color"] = [color]

    communities = g.community_edge_betweenness(directed=True)
    #fix_dendrogram(g,communities)
    #clusters = communities.as_clustering()
    #print clusters

    # Set edge weights based on communities
    #weights = {v: len(c) for c in clusters for v in c}
    g.es["weight"] = list(indegree)#[weights[e.tuple[0]] + weights[e.tuple[1]] for e in g.es]

    #visual_style["layout"] = "kk"
    visual_style["vertex_size"] = [x/max(outdegree)*25+50 for x in outdegree]
    visual_style['edge_width']= 3
    visual_style['edge_curved'] = True
    visual_style['arrow_size'] = 1
    visual_style['vertex_label_dist']=1
    visual_style['bbox']=(1500,1000)
    visual_style['margin']=200

    #layout = g.layout("kk")
    N = Node_Counter
    visual_style["layout"] = g.layout_fruchterman_reingold(weights=g.es["weight"], maxiter=1000, area=N**5, repulserad=N**3)

    for e in g.es:
        print e.tuple,e["weight"],g.vs['label'][e.tuple[0]]

    g.write_graphml("abc.graphml")
    igraph.plot(g, **visual_style)
    # graph_calculation(g)

def fix_dendrogram(graph, cl):
    already_merged = set()
    for merge in cl.merges:
        already_merged.update(merge)

    num_dendrogram_nodes = graph.vcount() + len(cl.merges)
    not_merged_yet = sorted(set(xrange(num_dendrogram_nodes)) - already_merged)
    if len(not_merged_yet) < 2:
        return

    v1, v2 = not_merged_yet[:2]
    cl._merges.append((v1, v2))
    del not_merged_yet[:2]

    missing_nodes = xrange(num_dendrogram_nodes,
            num_dendrogram_nodes + len(not_merged_yet))
    cl._merges.extend(izip(not_merged_yet, missing_nodes))
    cl._nmerges = graph.vcount()-1

def graph_calculation(g):

    print "Graph Calculations:"
    print max(g.outdegree())
    print max(g.indegree())
    # print "-"* 50
    # btwE = g.edge_betweenness()
    # print "Betweenness index for edges: ",btwE
    # print "Maximum betweenness; ",max(btwE)
    # print "Minimum betweenness; ",min(btwE)
    #
    # print "-" *50
    # dge = g.vs.degree()
    # print "Degree: ",dge
    # print "Maximum Degree: ",max(dge)
    # print "Minimum Degree: ",min(dge)

    answer = 'y'
    while answer <> 'n':
        name1= raw_input("Enter first name: ")
        name2= raw_input("Enter second name: ")

        try:
            start = g.vs.find(label=name1).index
            end = g.vs.find(label=name2).index
            print g.shortest_paths_dijkstra(source=start, target=end, weights=None, mode=OUT)
        except:
            pass
        answer = raw_input("Do you want to continue")

def Generate_Dictionary(Source_Target,flag=None):
    if flag:
        print Source_Target
        print "Sagar"
    else:
        Source_Target.sort()
        Completed_Node = []
        Source_Target_Dict = {}

        for i in range(len(Source_Target)):
            if Source_Target[i][0] not in Completed_Node:
                Source_Target_Dict[Source_Target[i][0]] = []
                Completed_Node.append(Source_Target[i][0])

            Source_Target_Dict[Source_Target[i][0]].append(Source_Target[i][1])

        print "Completed reading Source and Target"
        return Source_Target_Dict

def Generate_Dictionary_Simulation(Node_List):
    Source_Target_Dict = {}

    for Node in Node_List:
        Source_Target_Dict[Node.id] = []
        for Followers in Node.followers:
            Source_Target_Dict[Node.id].append(Followers.id)

    return Source_Target_Dict

def main():
    filepath = askopenfilename()
    if filepath <> "":
        Source_Target_List = []
        Target_List = []
        iRowCount = 1 # First Line Counter , No need to read header
        with open(filepath,"rb") as file:
            reader = csv.reader(file)

            for row in reader:
                if iRowCount <> 1:
                    Source_Target_List.append((row[SOURCE_COL],row[TARGET_COL])) #[4:]
                    # print row[SOURCE][4:], row[TARGET]
                    iRowCount = iRowCount + 1
                else:
                    iRowCount = 2

                if iRowCount ==500:
                    break
            Generate_Graph(Generate_Dictionary(Source_Target_List))

    else:
        print "Please select a file"

