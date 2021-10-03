import csv
# Este ya tiene la informacion de las latitudes y longitudes de las cuidades de origen y destino, sin repeticiones
def readDataNoRep():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)
    dictCoorOrigin = {}
    dictCoorDest = {}
    for row in csvreader:
        dictCoorOrigin[row['origin']] = (row['origin_latitude'],row['origin_longitude'])
        dictCoorDest[row['destination']] = (row['destination_latitude'],row['destination_longitude'])
    print(dictCoorOrigin)
    print(dictCoorDest)
    return (dictCoorOrigin, dictCoorDest)
    file.close()

# Este lee el csv completo y nos regresa el diccionario donde se guardó toda la información
def readDataSet():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)
    rows = {}
    i = 0
    for row in csvreader:
        row[i] = row
        i += 1
    return rows
readDataSet()



        


