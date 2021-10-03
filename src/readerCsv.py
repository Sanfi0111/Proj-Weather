import csv
def readDataSet():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)
    dictCoorOrigin = {}
    dictCoorDest = {}
    for row in csvreader:
        dictCoorOrigin[row['origin']] = (row['origin_latitude'],row['origin_longitude'])
        dictCoorDest[row['destination']] = (row['destination_latitude'],row['destination_longitude'])
    print(dictCoorOrigin)
    print("acabe1*********************************")
    print(dictCoorDest)
    return (dictCoorOrigin, dictCoorDest)
    file.close()
readDataSet()
def splitDataset():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)


        


