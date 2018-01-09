import time
import csv
import os, inspect

class GetProjectList:
    def __init__(self):
        self.filename = "projectsList.csv"
        self.projectRefs = []

    def checkIFCsvExist(self):
        filesArr = os.listdir('./')
        if self.filename in filesArr:
            return self.checkForProject()
        else:
            print('could not find '+self.filename)
            return 0

    def checkForProject(self):
        with open(self.filename, 'r', encoding='utf-8' ) as csvFile:
            content = csv.reader(csvFile, dialect='excel',quotechar='|')
            for row in content:
                newRow = []
                for cell in row:
                    newRow.append(str(cell).lower())
                self.projectRefs.append(newRow)

    def compareEntry(self, entry):
        splitByBacklash = entry.lower().split('\\')
        for snippet in splitByBacklash:
            for row in self.projectRefs:
                for synonym in row:
                    if str(synonym) in str(snippet) and str(synonym) is not '':
                        return row[0]
