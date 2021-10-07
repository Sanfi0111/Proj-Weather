import csv
# Este ya tiene la informacion de las latitudes y longitudes de las cuidades de origen y destino, sin repeticiones
# i)Hacer un test por si no se encontro alguna ciudad que está en el diccionario proveniente de readDataSet()+
#ii) longitud no existe o latitud
def readDataNoRep():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)
    dictCoorOrigin = {}
    for row in csvreader:
        dictCoorOrigin[row['origin']] = (row['origin_latitude'],row['origin_longitude'])
        dictCoorOrigin[row['destination']] = (row['destination_latitude'],row['destination_longitude'])
    print(dictCoorOrigin)
    print(str(len(dictCoorOrigin)))
    return (dictCoorOrigin)

    file.close()
# Este lee el csv completo y nos regresa el diccionario donde se guardó toda la información
def readDataSet():
    file = open('src\dataset1.csv')
    csvreader = csv.DictReader(file)
    rows = {}
    i = 0
    for row in csvreader:
        rows[i] = row
        i += 1
    return rows



        


