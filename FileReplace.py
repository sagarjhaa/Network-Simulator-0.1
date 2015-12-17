__author__ = 'sjha1'
'''
It is a fix to replace the text.py file of nltk to the nltk folder in the user's machine
Please provde the path to the nltk folder in your machine.
It is by default installed in the Python27/Lib/site-package/nltk
and by default python27 is installed in C drive
'''
from Tkinter import *
import tkFileDialog
import shutil
root = Tk()
root.withdraw()
directory=tkFileDialog.askdirectory()#askopenfilename(filetypes=[("text","*.py")])

if directory != "":
    try:
        #print directory
        shutil.copy2("text.py",directory)
    except Exception as e:
        print e
