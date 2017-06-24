import time
from datetime import datetime as dt
import csv
import os, inspect
import createData as CurrentWindow
import sys

thisYear = dt.now().year
thisMonth = dt.now().month
thisDay = dt.now().day

filename = str(thisYear)+"-"+str(thisMonth)+"-"+str(thisDay)+".csv"

def getTimeStamp():
    thisHour = dt.now().hour
    thisMinute = dt.now().minute
    thisSeconds = dt.now().second
    currentTimeInstance = str(thisHour)+":"+str(thisMinute)+":"+str(thisSeconds)
    return currentTimeInstance

def createCSVFile():
    '''creates a .csv file with
    year-month-date.csv'''
    with open(filename, 'wb') as csvFile:
        write = csv.writer(csvFile, delimiter=",")
        write.writerow([getTimeStamp(),getActiveFile()])
        csvFile.close()

def addData():
    # adds a data line to an existing csv file
    with open(filename, 'a+') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        write.writerows([[getTimeStamp(),getActiveFile()]])
        csvFile.close()

def getActiveFile():
    if sys.platform in ['linux', 'linux2']:
        return CurrentWindow.activeLinuxWindow()
    elif sys.platform in ['Windows', 'win32', 'cygwin']:
        return CurrentWindow.activeWindowsWindow()


getTimeStamp()
addData()
# createCSVFile()
