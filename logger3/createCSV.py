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
        self.startTimeStamp = dt.now().replace(microsecond=0)
        self.duration = ''
        self.finishTimeStamp = dt.now().replace(microsecond=0)
        self.filename = str(self.thisYear)+"-"+str(self.thisMonth)+"-"+str(self.thisDay)+".csv"


    def getTimeStamp(self,dataType):
        '''getTimeStamp returns the hh:mm:ss'''
        self.thisHour = dt.now().hour
        self.thisMinute = dt.now().minute
        self.thisSeconds = dt.now().second

        if dataType is 'string':
            currentTimeInstance = str(self.thisHour)+":"+str(self.thisMinute)+":"+str(self.thisSeconds)
            print('getTimeStamp: ', currentTimeInstance)
            return currentTimeInstance
        else:
            print('startTimeStamp', self.startTimeStamp)
            return self.startTimeStamp

    def getTimeDuration(self):
        timestamp = self.getTimeStamp('notaString')
        duration = dt.now().replace(microsecond=0) - timestamp
        print('getTimeDuration: ',timestamp,'duration', duration)
        return duration


    def createCSVFile(self):
        '''creates a .csv file with
        year-month-date.csv'''
        with open(self.filename, 'w+', encoding='utf-8') as csvFile:
            write = csv.writer(csvFile, delimiter=",")
            write.writerow([self.getTimeStamp('string'),self.getTimeDuration(),self.getActiveFile()])
            csvFile.close()

    def addData(self):
        '''adds a data line to an existing csv file'''
        with open(self.filename, 'a+', encoding='utf-8') as csvFile:
            write = csv.writer(csvFile, delimiter=',')
            write.writerows([[self.getTimeStamp('string'),self.getTimeDuration(),self.getActiveFile()]])
            csvFile.close()

    def getActiveFile(self):
        '''check if your on linux
        or windows and returns the active window name'''
        if sys.platform in ['linux', 'linux2']:
            return CurrentWindow.activeLinuxWindow()
        elif sys.platform in ['Windows', 'win32', 'cygwin']:
            return CurrentWindow.activeWindowsWindow()

    def checkIfCsvExist(self):
        ''' checks if the filesArray have today's datetime
         if it does, then addData otherwise createCSV'''
        filesArray = os.listdir('./')
        if self.filename in filesArray:
            return self.addData()
        else:
            return self.createCSVFile()
