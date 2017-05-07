# step 1: create a .csv file with the date as the filename
# step 2: log the activity your currently doing
# step 3: write it to the .csv file with a timestamp
import os, inspect
import time
from datetime import datetime as dt
import csv

thisYear = dt.now().year
thisMonth = dt.now().month
thisDay = dt.now().day
thisHour = dt.now().hour
thisMinute = dt.now().minute
thisSeconds = dt.now().second

currentTimeInstance = str(thisHour)+":"+str(thisMinute)+":"+str(thisSeconds)
filename = str(thisYear)+"-"+str(thisMonth)+"-"+str(thisDay)+".csv"

print(currentTimeInstance)

currentFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
currentfileName = inspect.getfile(inspect.currentframe())
currentLog = currentFilePath+"/"+currentfileName

print (currentLog)

dataStamp = [[currentLog,currentTimeInstance]]

def createCSV():
    # creates a .csv file with the year-month-date.csv
    with open(filename, 'w', newline='') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        data = [['hello','hello2'],[123,12345]]
        write.writerows(data)
        csvFile.close()

def addData(data):
    # adds a data line to an existing csv file
    with open(filename, 'a') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        write.writerows(data)
        csvFile.close()

def checkFileName():
    # checks if the filesArray have today's datetime
    # if it does, then addData otherwise createCSV
    filesArray = os.listdir()
    if filename in filesArray:
        print('file already exists')
        return addData(dataStamp)
    else:
        print('new file')
        return createCSV()

while True:
    checkFileName()
    time.sleep(5)
