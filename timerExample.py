from Tkinter import *
##from sys import exit

class Timer:
    def __init__(self, master):
        self.master=master
        buttonstart = Button(master, text = "Start", fg = "blue", command = self.start)
        buttonstart.grid(row = 1, column = 0)

        buttonquit = Button(master, text = "Quit", fg = "blue", command=self.quitit)
        buttonquit.grid(row = 1, column = 2)

        self.timertext = DoubleVar()
        self.timertext.set(0)
        display = Label(master, textvariable = self.timertext)
        display.grid(row = 0, column = 0)
##        timertext.set(timertext)  ## Huh!!
        self.timeit=False

    def increment_timer(self):
        ctr=int(self.timertext.get())
        self.timertext.set(ctr+1)
        if self.timeit:
            self.master.after(500, self.increment_timer)

    def start(self):
        self.timeit=True
        self.increment_timer()

    def quitit(self):
        self.timeit=False

root = Tk()
app = Timer(root)
root.mainloop()
