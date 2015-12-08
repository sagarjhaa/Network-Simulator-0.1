'''
Created on May 15,2015
@author: Sagar Jha
'''

import nltk as nltk
from Tkinter import *
from constants import writeCalculations

class analysisWidget(object):
    def __init__(self,master,text,textWidget,NB):
        top=self.top=Toplevel(master)

        self.textWidget = textWidget
        self.NB = NB

        self.text = text
        self.top.title("Text Analysis")
        self.top.geometry('%dx%d+%d+%d' % (300,250,10,500))
        self.top.resizable(False,False)

        self.inputbox = Entry(top,font = "Helvetica 16")
        # self.inputbox.grid(row=0,column=0,columnspan=2)
        # self.inputbox.configure(fill=BOTH)
        self.inputbox.pack(fill=BOTH,expand=1)
         
        self.searchText = Button(top,text="SearchText",command=self.__searchText)
        # self.searchText.grid(row=1,column=0)
        # self.searchText.configure(fill=BOTH)
        self.searchText.pack(fill=BOTH,expand=1)

        self.searchSText = Button(top,text="Search Similar Text",command=self.__searchSimilarText)
        # self.searchSText.grid(row=2,column=0)
        # self.searchSText.configure(fill=BOTH)
        self.searchSText.pack(fill=BOTH,expand=1)

        self.searchCText = Button(top,text="Search Common Context Text",command=self.__seachCommonConText)
        # self.searchCText.grid(row=1,column=1)
        # self.searchCText.configure(fill=BOTH)
        self.searchCText.pack(fill=BOTH,expand=1)

        self.dPlot = Button(top,text="Dispersion Plot",command=self.__dispersionPlot)
        # self.dPlot.grid(row=2,column=1)
        # self.dPlot.configure(fill=BOTH)
        self.dPlot.pack(fill=BOTH,expand=1)
        
        self.fDist = Button(top,text="Frequency Distribution",command=self.__frequencyDistribution)
        # self.fDist.grid(row=3,column=0)
        # self.fDist.configure(fill=BOTH)
        self.fDist.pack(fill=BOTH,expand=1)

    def findValue(self):
        return self.Choice.get()
        
    def cleanup(self):
        self.top.destroy()

    def readTextbox(self):
        inputtext = self.inputbox.get()
        self.inputlist = []
       
        if inputtext <> "":
            self.inputlist = inputtext.split(",")
        else:
            writeCalculations(self.textWidget,"Please enter words into the textbox!!!",True,self.NB)

    def __searchText(self):
        """

        :type self: object
        """
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        writeCalculations(self.textWidget,"Search Text" ,False,self.NB)
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        self.readTextbox()
        for word in self.inputlist:
            values = self.text.concordance(word)
            writeCalculations(self.textWidget,"*"*100 ,False,self.NB)
            writeCalculations(self.textWidget,"Displaying %d of %d matches for %s" % (len(values),len(values),word),False,self.NB)
            writeCalculations(self.textWidget,"*"*100 ,False,self.NB)
            for i in range(len(values)):
                writeCalculations(self.textWidget,values[i][0]+" "+values[i][1]+" "+values[i][2],False,self.NB)

    def __searchSimilarText(self):
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        writeCalculations(self.textWidget,"Search Similar Text" ,False,self.NB)
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        self.readTextbox()
        for word in self.inputlist:
            writeCalculations(self.textWidget,"*"*100 ,False,self.NB)
            writeCalculations(self.textWidget,"Similar text search for %s " % (word) ,False,self.NB)
            writeCalculations(self.textWidget,"*"*100 ,False,self.NB)
            value = self.text.similar(word)
            writeCalculations(self.textWidget,value,False,self.NB)

    def __seachCommonConText(self):
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        writeCalculations(self.textWidget,"Search common context" ,False,self.NB)
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        self.readTextbox()
        value = self.text.common_contexts(self.inputlist)
        writeCalculations(self.textWidget,value,False,self.NB)
       
    def __dispersionPlot(self):
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        writeCalculations(self.textWidget,"Dispersion Plot" ,False,self.NB)
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)

        self.readTextbox()
        self.text.dispersion_plot(self.inputlist)

    def __frequencyDistribution(self):
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)
        writeCalculations(self.textWidget,"Frequency Distribution" ,False,self.NB)
        writeCalculations(self.textWidget,"-"*100 ,False,self.NB)

        fdist1 = nltk.FreqDist(self.text)
        vocab1 = fdist1.keys()

        iNum = 50
        if len(vocab1) < iNum:
            iNum = len(vocab1)

        fdist1.plot(iNum,cumulative=True)





      
      
