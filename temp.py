from Tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

#w.create_line(0, 0, 200, 100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_polygon(609, 416 ,614 ,416, 614, 421 ,609, 421, fill="blue")

mainloop()