import requests
#Esta es la llave para poder acceder a la API
key ='a00bd54d69b3cdd04b682f93586e3512'
#URL para revisar si la llave sirve bien
url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid='+key
resp = requests.get(url).json()
print(resp)
