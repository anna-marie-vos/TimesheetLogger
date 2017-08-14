import time
from datetime import datetime as dt
import csv
import os, inspect
import createData as CurrentWindow
import sys


class CreateCSV:
    """docstring for createCSV."""
    def __init__(self):
        self.thisYear = dt.now().year
        self.thisMonth = dt.now().month
        self.thisDay = dt.now().day
        self.filename = str(self.thisYear)+"-"+str(self.thisMonth)+"-"+str(self.thisDay)+".csv"

        self.startTime = dt.now().replace(microsecond=0)
        self.newStartTime = dt.now().replace(microsecond=0)
        self.finishTime = dt.now().replace(microsecond=0)

        self.previousWindow = ''
        self.currentWindow = ''

    def checkActiveWindow(self):
        self.startTime = self.newStartTime
        self.finishTime = dt.now().replace(microsecond=0)
        self.duration = self.finishTime - self.startTime

        if self.getActiveFile() != self.previousWindow:
            self.checkIfCsvExist()
            self.newStartTime = dt.now().replace(microsecond=0)
            self.previousWindow = self.currentWindow



    def getActiveFile(self):
        #Step3
        '''check if your on linux
        or windows and returns the active window name'''
        if sys.platform in ['linux', 'linux2']:
            self.currentWindow = CurrentWindow.activeLinuxWindow()
            return self.currentWindow
        elif sys.platform in ['Windows', 'win32', 'cygwin']:
            self.currentWindow = CurrentWindow.activeWindowsWindow()
            return self.currentWindow

    def createCSVFile(self):
        #Step2a
        '''creates a .csv file with
        year-month-date.csv'''
        with open(self.filename, 'w+', encoding='utf-8') as csvFile:
            write = csv.writer(csvFile, delimiter=",")
            write.writerow(['Start Time','Finish Time','Duration','Active Window'])
            csvFile.close()

    def addData(self):
        #Step2b
        '''adds a data line to an existing csv file'''
        start = str(self.startTime.hour)+':'+str(self.startTime.minute)+':'+str(self.startTime.second)
        finish = str(self.finishTime.hour)+':'+str(self.finishTime.minute)+':'+str(self.finishTime.second)
        dur = str(self.duration)

        with open(self.filename, 'a+', encoding='utf-8') as csvFile:
            write = csv.writer(csvFile, delimiter=',')
            write.writerows([[start,finish,dur,self.previousWindow]])
            csvFile.close()


    def checkIfCsvExist(self):
        #Step1
        ''' checks if the filesArray have today's datetime
         if it does, then addData otherwise createCSV'''
        filesArray = os.listdir('./')
        if self.filename in filesArray:
            return self.addData()
        else:
            return self.createCSVFile()
