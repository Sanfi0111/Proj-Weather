import requests
#Esta es la llave para poder acceder a la API
key ='a00bd54d69b3cdd04b682f93586e3512'
#URL para revisar si la llave sirve bien
url = 'http://api.openweathermap.org/data/2.5/weather?'
resp = requests.get(url).json()
lon = '-99.566'
lat = '19.337'
resp1= 'http://api.openweathermap.org/data/2.5/weather?lat=19.337&lon=-99.566&appid='+key
resp3=requests.get(resp1).json()
print(resp3)

def printForm(con, weath, sens, tempmax, tempmin, hume):
    cadenaCiu = con+": \n"
    cadenaCli = "Clima: "+ weath+" Temperatura máxima:"+tempmax+", Temperatura mínima :"+tempmin
    cadenaSens = "Sensación térmica:"+sens
    cadenaHume = "Humedad: "+hume
    cadenaCompleta = cadenaCiu + cadenaCli + cadenaSens + cadenaHume 
    
# Con readDataSet() voy accediendo a 
def request(latlonOri, latlonDes, dicDataSet):
    completCoor = latlon.split(',')
    urlComp = url+'lat='+latlon[0]+"&lon="+latlon[0]+'&appid='+key+'&lang=es&units=metric'
    request = requests.get(urlComp).json()


