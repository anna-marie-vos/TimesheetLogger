from tkinter import *
import createCSV as csv
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk as gtk

class UI:
    def __init__(self, window):
        self.window = window
        self.timeit = False
        self.interval = 5000
        self.window.wm_title("Timesheet Logger")

        inputLabel = Label(window, text= "Set the time interval:")
        inputLabel.grid(row = 1, column = 0 )

        self.timeInput = IntVar()
        timeEntry = Entry(window, textvariable = self.timeInput)
        timeEntry.grid(row = 1, column = 1)

        unitLabel = Label(window, text="seconds")
        unitLabel.grid(row = 1, column = 2)

        startBtn = Button(window, text = "Start", width = 12, command=self.start)
        startBtn.grid(row = 2, column = 0)

        startBtn = Button(window, text = "Pause", width = 12, command=self.quitit)
        startBtn.grid(row = 2, column = 1)

        quitBtn = Button(window, text = "Quit", width = 12, command=self.window.destroy)
        quitBtn.grid(row = 2, column = 2)

    def start(self):
        self.timeit=True
        self.getInterval()
        self.timeLoop()

    def quitit(self):
        self.timeit=False
        self.timeLoop()

    def timeLoop(self):
        csv.checkIfCsvExist()
        if self.timeit:
            self.window.after(self.interval, self.timeLoop)

    def getInterval(self):
        if self.timeInput.get() =="":
            self.interval = 5000
        else :
            self.interval = self.timeInput.get()*1000


root = Tk()
app = UI(root)
root.mainloop()
