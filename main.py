#David
#TODO Add buttons to reading frame to start/stop.
import tkinter as tk
from tkinter import ttk, Frame, Button
import re, time

class SpeedyReady(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack()
        self.inputFrame = Frame(self.tabs)
        self.readingFrame = Frame(self.tabs)
        self.userText = ""
        trailLength = 2
        self.readingTabSetup(trailLength)
        self.inputTabSetup()

    def readingTabSetup(self, trailLength):
        self.TL = trailLength
        self.tabs.add(self.inputFrame, text='Input')
        self.tabs.add(self.readingFrame, text='Read')
        self.textVars = []
        myFont = ("Courier",44)
        for i in range(1+(2*trailLength)):
            subText = tk.StringVar()
            self.textVars.append(subText)
        for i in range(len(self.textVars)):
            if i == trailLength:
                textLbl = tk.Label(self.readingFrame, font=myFont, textvariable=self.textVars[i])
            else:
                textLbl = tk.Label(self.readingFrame, font=myFont, textvariable=self.textVars[i], fg="gray80")
            textLbl.pack()
        button = Button(self.readingFrame, text = "Begin", command=self.speedRead)
        button.pack()  

    def inputTabSetup(self):
        self.entryField = tk.Text(self.inputFrame, height=8)
        self.entryField.pack()
        submissionBtn = Button(self.inputFrame, text="Submit", command=self.submitButton)
        submissionBtn.pack()

    def speedRead(self):
        words = re.sub("[^\w]", " ", self.userText).split()
        for i in range(len(words)+self.TL):
            try:
                
                self.textVars[0].set('{}'.format(words[i]))
            except:
                continue
        
    def submitButton(self):
        self.userText = self.entryField.get(1.0, "end-1c")
        print(self.textVars[0])

    def updateWordVars(self):
        pass

window = SpeedyReady()
window.mainloop()