from tkinter import *
from createCSV import CreateCSV
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk as gtk

csv = CreateCSV()

class UI:
    def __init__(self, window):
        self.window = window
        self.timeit = False
        self.interval = 5000
        self.window.wm_title("Timesheet Logger")

        inputLabel = Label(window, text= "Set the time interval:")
        inputLabel.grid(row = 0, column = 0 )

        self.timeInput = IntVar()
        timeEntry = Entry(self.window, textvariable = self.timeInput)
        timeEntry.insert(INSERT,6)
        timeEntry.grid(row = 0, column = 1)

        unitLabel = Label(self.window, text="seconds")
        unitLabel.grid(row = 0, column = 2)

        self.logLabel = Label(self.window, text = 'currentWindow')
        self.logLabel.grid(row = 1, columnspan=3)

        startBtn = Button(self.window, text = "Start", width = 12, command=self.start)
        startBtn.grid(row = 2, column = 0)

        startBtn = Button(self.window, text = "Pause", width = 12, command=self.quitit)
        startBtn.grid(row = 2, column = 1)

        quitBtn = Button(self.window, text = "Quit", width = 12, command=self.window.destroy)
        quitBtn.grid(row = 2, column = 2)

    def start(self):
        self.timeit=True
        self.getInterval()
        self.timeLoop()

    def quitit(self):
        self.timeit=False
        self.timeLoop()

    def timeLoop(self):
        csv.checkActiveWindow()
        self.logLabel['text'] = csv.currentWindow

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
