# step 1: create a .csv file with the date as the filename
# step 2: log the activity your currently doing
# step 3: write it to the .csv file with a timestamp

import time
from datetime import datetime as dt
import csv

thisYear = dt.now().year
thisMonth = dt.now().month
thisDay = dt.now().day
filename = str(thisYear)+"-"+str(thisMonth)+"-"+str(thisDay)+".csv"
dummyData = [['meme file','13:15'],['another name', '14:33']]

def createCSV():
    # creates a .csv file with the year-month-date.csv
    with open(filename, 'w', newline='') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        data = [['hello','hello2'],[123,12345]]
        write.writerows(data)
        csvFile.close()

def addData(data):
    with open(filename, 'a') as csvFile:
        write = csv.writer(csvFile, delimiter=',')
        write.writerows(data)
        csvFile.close()

createCSV()
addData(dummyData)

print (filename)
