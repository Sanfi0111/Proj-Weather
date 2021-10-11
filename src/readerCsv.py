import csv
# Este ya tiene la informacion de las latitudes y longitudes de las cuidades de origen y destino, sin repeticiones
# i)Hacer un test por si no se encontro alguna ciudad que está en el diccionario proveniente de readDataSet()+
#ii) longitud no existe o latitud
class readerCsv:
    """ Reads the data from a CSV, but there are no repeated items
        return : a dictionary with information of a flight with no repeated items"""
        
    def readDataNoRep(file1):
        file = open(file1)
        csvreader = csv.DictReader(file)
        dictCoorOrigin = {}
        for row in csvreader:
            dictCoorOrigin[row['origin']] = (row['origin_latitude'],row['origin_longitude'])
            dictCoorOrigin[row['destination']] = (row['destination_latitude'],row['destination_longitude'])
        print(dictCoorOrigin)
        return (dictCoorOrigin)
        file.close()

    """ Reads the data from a CSV.
        return : a dictionary with information of all the flights in dataset1.csv"""
    def readDataSet(file1):
        file = open(file1)
        csvreader = csv.DictReader(file)
        rows = {}
        i = 0
        for row in csvreader:
            rows[i] = row
            i += 1
        return rows



        


