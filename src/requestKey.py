import requests
import time
from readerCsv import readDataSet
#Esta es la llave para poder acceder a la API
key ='a00bd54d69b3cdd04b682f93586e3512'
#URL para revisar si la llave sirve bien
url = 'http://api.openweathermap.org/data/2.5/weather?'
resp = requests.get(url).json()
# lon = '-99.566'
#lat = '19.337'
#resp1= 'http://api.openweathermap.org/data/2.5/weather?lat=19.337&lon=-99.566&appid='+key
#resp3=requests.get(resp1).json()
#print(resp3)

def printForm(con, weath, sens, tempmax, tempmin, hume):
    cadenaCiu = con+": \n"
    cadenaCli = "Clima: "+ weath+" Temperatura máxima:"+tempmax+", Temperatura mínima :"+tempmin
    cadenaSens = "Sensación térmica:"+sens
    cadenaHume = "Humedad: "+hume
    cadenaCompleta = cadenaCiu + cadenaCli + cadenaSens + cadenaHume 
    
""" Request a city weather by coordenates
    dicDataSet: the complete dictionary that contains all the information from dataset1.csv
    return: The weather of the requested city """
def request(dicDataSet):
    compDatOrigin = {}
    compDatDestin = {}
    cadenasOri = []
    cadenasDest = []
    i = 0
    for row in dicDataSet:
        urlCompIda = url+'lat=' +dicDataSet[i]['origin_latitude']+"&lon=" +dicDataSet[i]['origin_longitude']+ '&appid=' + key + '&lang=es&units=metric'
        urlCompDest = url+'lat=' +dicDataSet[i]['destination_latitude']+"&lon=" +dicDataSet[i]['destination_longitude']+ '&appid=' + key + '&lang=es&units=metric'
        try:
            compDatOrigin = requests.get(urlCompIda).json()
            cadenasOri = inList(compDatOrigin)
            print(cadenasOri)
            time.sleep(1)
            compDatDestin = requests.get(urlCompDest).json()
            cadenasDest = inList(compDatDestin)
        except(KeyError):
            print("No se pudo encontrar una ciudad con las coordenadas ingresadas")
        i += 1
    print(cadenasOri)

""" Add elements from a request into a List 
    dicRequests: A dictionary containing the requests"""
def inList(dicRequests):
    cadenas = []
    cadenaciuOr = (dicRequests['name'])
    cadenas.append(cadenaciuOr)
    cadenaMinOr = (dicRequests['main']['temp_min'])
    cadenas.append(cadenaMinOr)
    cadenaMaxOr = (dicRequests['main']['temp_max'])
    cadenas.append(cadenaMaxOr)
    cadeaHumOr = (dicRequests['main']['humidity'])
    cadenas.append(cadeaHumOr)
    cadenaSensOr = (dicRequests['main']['feels_like'])
    cadenas.append(cadenaSensOr)
    return cadenas 


request(readDataSet())


