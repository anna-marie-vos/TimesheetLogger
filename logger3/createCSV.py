import time
from datetime import datetime as dt
import csv
import os, inspect
import createData as CurrentWindow
import sys


thisYear = dt.now().year
thisMonth = dt.now().month
thisDay = dt.now().day
startTimeStamp = dt.now().replace(microsecond=0)
duration = ''
finishTimeStamp = dt.now().replace(microsecond=0)

filename = str(thisYear)+"-"+str(thisMonth)+"-"+str(thisDay)+".csv"

def getTimeStamp(dataType):
    '''getTimeStamp returns the hh:mm:ss'''
    thisHour = dt.now().hour
    thisMinute = dt.now().minute
    thisSeconds = dt.now().second
    startTimeStamp = dt.now().replace(microsecond=0)
    if dataType is 'string':
        currentTimeInstance = str(thisHour)+":"+str(thisMinute)+":"+str(thisSeconds)
        return currentTimeInstance
    else:
        return startTimeStamp

def getTimeDuration():
    timestamp = getTimeStamp('notaString')
    duration = dt.now().replace(microsecond=0) - timestamp
    return duration


def createCSVFile():
    '''creates a .csv file with
    year-month-date.csv'''
    with open(filename, 'w+', encoding='utf-8') as csvFile:
        write = csv.writer(csvFile, delimiter=",")
        write.writerow([getTimeStamp('string'),getTimeDuration(),getActiveFile()])
        csvFile.close()

def addData():
    '''adds a data line to an existing csv file'''
    with open(filename, 'a+', encoding='utf-8') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        write.writerows([[getTimeStamp('string'),getTimeDuration(),getActiveFile()]])
        csvFile.close()

def getActiveFile():
    '''check if your on linux
    or windows and returns the active window name'''
    if sys.platform in ['linux', 'linux2']:
        return CurrentWindow.activeLinuxWindow()
    elif sys.platform in ['Windows', 'win32', 'cygwin']:
        return CurrentWindow.activeWindowsWindow()

def checkIfCsvExist():
    ''' checks if the filesArray have today's datetime
     if it does, then addData otherwise createCSV'''
    filesArray = os.listdir('./')
    if filename in filesArray:
        return addData()
    else:
        return createCSVFile()
