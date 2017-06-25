from tkinter import *
import createCSV as csv
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk as gtk

class UI:
    def __init__(self, window):
        self.window = window
        self.timeit = False

        self.window.wm_title("Timesheet Logger")

        startBtn = Button(window, text = "Start", width = 12, command=self.start)
        startBtn.grid(row = 1, column = 0)

        startBtn = Button(window, text = "Pause", width = 12, command=self.quitit)
        startBtn.grid(row = 1, column = 1)

        quitBtn = Button(window, text = "Quit", width = 12, command=self.window.destroy)
        quitBtn.grid(row = 2, column = 0)

    def start(self):
        self.timeit=True
        self.timeLoop()

    def quitit(self):
        self.timeit=False
        self.timeLoop()

    def timeLoop(self):
        csv.checkIfCsvExist()
        if self.timeit:
            self.window.after(5000, self.timeLoop)


root = Tk()
app = UI(root)
root.mainloop()
