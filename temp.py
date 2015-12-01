# from Tkinter import *
#
# master = Tk()
#
# w = Canvas(master, width=200, height=100)
# w.pack()
#
# l1 = w.create_line(0, 0, 200, 100)
# l2 = w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#
# w.itemconfig(l1,state=DISABLED,fill="red")
#
# w.create_polygon(609, 416 ,614 ,416, 614, 421 ,609, 421, fill="blue")
#
# mainloop()

# disable_cb_test.py

from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=LEFT)

        self.en = Button(frame, text="Enable", command=self.enable_cb)
        self.en.pack(side=LEFT)

        self.dis = Button(frame, text="Disable", command=self.disable_cb)
        self.dis.pack(side=LEFT)

        self.var = IntVar()
        self.cb = Checkbutton(frame,text="Check",variable = self.var,command=self.value)
        self.cb.pack(side=LEFT)

    def enable_cb(self):
        self.cb.configure(state='normal')

    def disable_cb(self):
        self.cb.configure(state='disabled')

    def value(self):
        print self.var.get()


root = Tk()
app = App(root)
root.mainloop()






# import snap
# g = snap.GenRndGnm(snap.PUNGraph, 10, 2)
#
# #['GetDeg', 'GetId', 'GetInDeg', 'GetInEdges', 'GetInNId', 'GetNI', 'GetNbrNId', 'GetOutDeg', 'GetOutEdges', 'GetOutNId', 'IsInNId', 'IsNbrNId', 'IsOutNId', 'Next', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__lt__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__swig_destroy__', '__weakref__', 'this', 'thisown']
#
# # Node in g.Nodes():
# #    print dir(Node)
#
#
# for node in g.Nodes():
#     follower = []
#     for EI in g.Edges():
#         if EI.GetSrcNId() == node.GetId():
#             if EI.GetSrcNId() <> EI.GetDstNId():
#                 follower.append(EI.GetDstNId())
#     print node.GetId(),node.GetDeg(),follower