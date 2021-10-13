import csv
# Este ya tiene la informacion de las latitudes y longitudes de las cuidades de origen y destino, sin repeticiones
# i)Hacer un test por si no se encontro alguna ciudad que está en el diccionario proveniente de readDataSet()+
#ii) longitud no existe o latitud
class readerCsv:
    """ Reads the data from a CSV.
        Parameters:
        file1: the file with the information to read
        Returns :
         a dictionary with information of all the flights in dataset1.csv"""
    def readDataSet(self,file1):
        file = open(file1)
        csvreader = csv.DictReader(file)
        rows = {}
        i = 0
        for row in csvreader:
            rows[i] = row
            i += 1
        return rows