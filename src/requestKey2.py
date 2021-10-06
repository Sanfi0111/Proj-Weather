import requests
#Esta es la llave para poder acceder a la API
key ='2b0ff9efcaee48c07cf27c16e77eb756'
#URL para revisar si la llave sirve bien
url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid='+key
resp = requests.get(url).json()