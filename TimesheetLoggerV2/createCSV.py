import time
from datetime import datetime as dt
import csv
import os, inspect

thisYear = dt.now().year
thisMonth = dt.now().month
thisDay = dt.now().day

filename = str(thisYear)+"-"+str(thisMonth)+"-"+str(thisDay)+".csv"

def createData():
    thisHour = dt.now().hour
    thisMinute = dt.now().minute
    thisSeconds = dt.now().second

    currentTimeInstance = str(thisHour)+":"+str(thisMinute)+":"+str(thisSeconds)

    currentFilePath = os.getcwd()

    currentFileName = inspect.getfile(inspect.currentframe())

    currentLog = currentFilePath+"/"+currentFileName

    print("current File Path",currentFilePath)
    print("current File Name",currentFileName)
    print("current log",currentLog)


def createCSVFile():
    '''creates a .csv file with
    year-month-date.csv'''
    with open(filename, 'wb') as csvFile:
        write = csv.writer(csvFile, delimiter=",")
        write.writerow(["hello"])
        csvFile.close()

createCSVFile()
