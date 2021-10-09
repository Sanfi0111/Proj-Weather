import requests
import time
from readerCsv import readDataSet

#Key to access OpenWeather API
key ='a00bd54d69b3cdd04b682f93586e3512'
#Open Weather URL 
url = 'http://api.openweathermap.org/data/2.5/weather?'
# A list that contains the weather from the origin cities of a flight
cadenasOri = []
# A list that contains the weather from the Destination cities of a flight
cadenasDest = []
# A dictionary that contains the latitude and longitude from the origin cities of a flight
compDatOrigin = {}
# A dictionary that contains the latitude and longitude from the destination cities of a flight
compDatDestin = {}
# A dictionary that works as a cache 
cache = {}
""" Prints a weather summary
    Weather: a list containing the weather of a city """
def printForm(weather):
    cadenaCiu = "Ciudad: " +weather[0]+" \n"
    cadenaCli = "Clima: "+str(weather[1])+ " Temperatura mínima: "+str(weather[2])+ "°, Temperatura máxima : "+str(weather[3])+"° \n"
    cadenaSens = "Sensación térmica:"+str(weather[4])+"° \n"
    cadenaHume = "Humedad: "+str(weather[4])+"% \n"
    cadenaCompleta = cadenaCiu + cadenaCli + cadenaSens + cadenaHume 
    print(cadenaCompleta)

""" Request a city weather by coordenates
    dicDataSet: the complete dictionary that contains all the information from dataset1.csv
    return: The weather of the requested city """
def request(dicDataSet):
    i = 0
    for row in dicDataSet:
        urlCompIda = url+'lat=' +dicDataSet[i]['origin_latitude']+"&lon=" +dicDataSet[i]['origin_longitude']+ '&appid=' + key + '&lang=es&units=metric'
        urlCompDest = url+'lat=' +dicDataSet[i]['destination_latitude']+"&lon=" +dicDataSet[i]['destination_longitude']+ '&appid=' + key + '&lang=es&units=metric'
        try:
            compDatOrigin = requests.get(urlCompIda).json()    
            print("Ciudad de Origen:")
            # Accedo a cada los elementos que hay en un request y los meto en una lista con sus elementos
            cadenasOri = inList(compDatOrigin)
            # Guardo este elemento en un cache
            cache[cadenasOri[0]] = cadenasOri
            printForm(cadenasOri)
            compDatDestin = requests.get(urlCompDest).json()
            print("Ciudad de Destino:")
            cache[cadenasDest[0]] = cadenasDest
            print(cache)
            cadenasDest = inList(compDatDestin)

            printForm(cadenasDest)
            time.sleep(1)

        except(KeyError):
            print("No se pudo encontrar una ciudad con las coordenadas ingresadas")
        i += 1
def printRequests(cadenasOri, cadenasDest):
    i= 0
    for rows in cadenasOri:
        print("Clima en la ciudad de Origen:")
        printForm(cadenasOri[i])
        print("Clima en la ciudad de Destino")
        printForm(cadenasDest[i])
        i += 1


""" Add elements from a request into a List 
    dicRequests: A dictionary containing the requests"""
def inList(dicRequests):
    cadenas = []
    cadenaciuOr = (dicRequests['name'])
    cadenas.append(cadenaciuOr)
    cadenaTemp = (dicRequests['main']['temp'])
    cadenas.append(cadenaTemp)
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


