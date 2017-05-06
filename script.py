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

# creates a .csv file with the year-month-date.csv
with open(filename, 'r+', newline='') as csvFile:
    a = csv.writer(csvFile, delimiter=',')
    data=[['hello','hello2'],[123,12345]]
    a.writerows(data)

print (filename)
