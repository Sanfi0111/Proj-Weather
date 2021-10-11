import requests
import time
from readerCsv import readerCsv
class requestKey:
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
    def printForm(self,weather):
        cadenaCiu = "Ciudad: " +weather[0]+" \n"
        cadenaCli = "Clima: "+str(weather[1])+ " Temperatura mínima: "+str(weather[2])+ "°, Temperatura máxima : "+str(weather[3])+"° \n"
        cadenaSens = "Sensación térmica:"+str(weather[4])+"° \n"
        cadenaHume = "Humedad: "+str(weather[4])+"% \n"
        cadenaCompleta = cadenaCiu + cadenaCli + cadenaSens + cadenaHume 
        print(cadenaCompleta)

    """ Checks if a dictionary contains a certain key
        dic: the dictionary to check
        dicKey: the key
        return: a Boolean indicating if the key is contained in the dictionary
    """
    def containsKeyBool(self, dicCache, dicKey):
        i = 0
        for key in dicCache:
            if(key == dicKey):
                return True
            else :
                return False
            i += 1

    """ Checks if a dictionary contains a certain key
        dic: the dictionary to check
        dicKey: the key
        return: the element with the key
    """
    def containsKey(self, dicCache, dicKey):
        i = 0
        keyList = []
        for key in dicCache:
            if(key == dicKey):
                keyList = dicCache[dicKey] 
                return keyList
            else:
                print("No encontre esta llave en mi diccionario ")
            i += 1
    """ Request a city weather by coordenates
        dicDataSet: the complete dictionary that contains all the information from dataset1.csv
        return: The weather of the requested city """
    def request(self,dicDataSet):
        i = 0
        for row in dicDataSet:
            urlCompIda = self.url+'lat=' +dicDataSet[i]['origin_latitude']+"&lon=" +dicDataSet[i]['origin_longitude']+ '&appid=' + self.key + '&lang=es&units=metric'
            urlCompDest = self.url+'lat=' +dicDataSet[i]['destination_latitude']+"&lon=" +dicDataSet[i]['destination_longitude']+ '&appid=' + self.key + '&lang=es&units=metric'
            latLonORi =  dicDataSet[i]['origin_latitude']+dicDataSet[i]['origin_longitude']
            latLonDes = dicDataSet[i]['destination_latitude']+dicDataSet[i]['destination_longitude']
            try:
                m = 0
                # Primer caso, checamos el clima en la ciudad de origen
                if(containsKeyBool(self.cache, latLonORi) == True):
                    # Tomamos la lista que tiene los valores del clima de una ciudad
                    keyList = containsKey(self.cache, latLonORi)
                    printForm(keyList)
                else:
                    compDatOrigin = requests.get(urlCompIda).json()    
                    cadenasOri = inList(compDatOrigin)
                    cache[latLonORi] = cadenasOri
                    printForm(cadenasOri)
                    m +=1
                if(containsKeyBool(cache, latLonDes)):
                    keyList1 = containsKey(cache, latLonDes)
                    printForm(keyList1)
                else:
                    print("no entre destino")
                    compDatDestin = requests.get(urlCompDest).json()
                    print("Ciudad de Destino:")
                    cadenasDest = inList(compDatDestin)
                    cache[latLonDes] = cadenasDest
                    printForm(cadenasDest)
                    m += 1
                if(m > 1):
                    time.sleep(1)
            except(KeyError):
                print("No se pudo encontrar una ciudad con las coordenadas ingresadas")
            i += 1
    """ Add elements from a request into a List 
        dicRequests: A dictionary containing the requests"""
    def inList(self,dicRequests):
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

    if __name__ == "__main__":
        reques1t = requestKey
        csv = readerCsv
        reques1t.request(csv.readDataSet('src\dataset1.csv'))
        


