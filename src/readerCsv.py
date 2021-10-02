import csv
def readDataSet():
    file = open('src\dataset1.csv')
    csvreader = csv.reader(file)
    rows = {}
    i=0
    for row in csvreader:
        rows[i]=row
        i+=1
    print(rows)
    return rows
    file.close()

