import requests
import time
from readerCsv import readerCsv

class Request:

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
        Parameters:
        Weather: a list containing the weather of a city """
    def printForm(self,weather):
        cadenaCiu = "Ciudad: " +weather[0]+" \n"
        cadenaCli = "Clima: "+str(weather[1])+ " Temperatura mínima: "+str(weather[2])+ "°, Temperatura máxima : "+str(weather[3])+"° \n"
        cadenaSens = "Sensación térmica:"+str(weather[4])+"° \n"
        cadenaHume = "Humedad: "+str(weather[4])+"% \n"
        cadenaCompleta = cadenaCiu + cadenaCli + cadenaSens + cadenaHume 
        print(cadenaCompleta)

    """ Checks if a dictionary contains a certain key
        Parameters:
        dic: the dictionary to check
        dicKey: the key
        Returns: 
        a Boolean indicating if the key is contained in the dictionary
    """
    def containsKeyBool(self, dicCache, dicKey):
        i = 0
        for key in dicCache:
            if(key == dicKey):
                return True
            i += 1

    """ Checks if a dictionary contains a certain key
        Parameters :
        dic: the dictionary to check
        dicKey: the key
        Returns:
        The element with the key
    """
    def containsKey(self, dicCache, dicKey):
        i = 0
        keyList = []
        for key in dicCache:
            if(key == dicKey):
                keyList = dicCache[dicKey] 
                return keyList
            i += 1
    
    """ Checks if a element is in cache, if it is contained, then we use the element instead of make a request
        Parameters: 
        latlonOri(int) = latitude and longitude from origin city
        latlonDes(int) = latitude and longitude from destiny city
        urlCompIda(String) = the url of the openWeather from the requested origin city
        urlCompDest(String) = the url of the openWeather from the requested destination city
        """
    def checkCache(self,latlonOri, latlonDes,urlCompIda,urlCompDest):
        if(self.containsKeyBool(self.cache, latlonOri) == True):
            keyList = self.containsKey(self.cache, latlonOri)
            print("Ciudad de Origen")
            self.printForm(keyList)
        else:
            compDatOrigin = requests.get(urlCompIda).json()    
            cadenasOri = self.inList(compDatOrigin)
            self.cache[latlonOri] = cadenasOri
            print("Ciudad de Oigen")
            self.printForm(cadenasOri)
        if(self.containsKeyBool(self.cache, latlonDes)):
            keyList1 = self.containsKey(self.cache, latlonDes)
            print("Ciudad de Destino")
            self.printForm(keyList1)
        else:
            compDatDestin = requests.get(urlCompDest).json()
            print("Ciudad de Destino:")
            cadenasDest = self.inList(compDatDestin)
            self.cache[latlonDes] = cadenasDest
            self.printForm(cadenasDest)

    """ Add elements from a request into a List 
        Parameters:
        dicRequests: A dictionary containing the requests
        Returns:
        A list with all the information of the weather from a city """
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

    """ Request a city weather by coordenates
        Parameters: 
        dicDataSet: the complete dictionary that contains all the information from dataset1.csv
        Returns: The weather of the requested city """
    def request(self,dicDataSet):
        i = 0
        for row in dicDataSet:
            urlCompIda = self.url+'lat=' +dicDataSet[i]['origin_latitude']+"&lon=" +dicDataSet[i]['origin_longitude']+ '&appid=' + self.key + '&lang=es&units=metric'
            urlCompDest = self.url+'lat=' +dicDataSet[i]['destination_latitude']+"&lon=" +dicDataSet[i]['destination_longitude']+ '&appid=' + self.key + '&lang=es&units=metric'
            latLonORi =  dicDataSet[i]['origin_latitude']+dicDataSet[i]['origin_longitude']
            latLonDes = dicDataSet[i]['destination_latitude']+dicDataSet[i]['destination_longitude']
            try:
                self.checkCache(latLonORi,latLonDes,urlCompIda,urlCompDest)
                time.sleep(1)
            except(KeyError):
                print("No se pudo encontrar una ciudad con las coordenadas ingresadas")
            i += 1


