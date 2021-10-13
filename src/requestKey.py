import requests
import time
from readerCsv import readerCsv
class RequestKey:
    #Key to access OpenWeather API
    key ='a00bd54d69b3cdd04b682f93586e3512'
    #Open Weather URL 
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    # A list that contains the weather from the origin cities of a flight
    request = url+"lat=19.3371&lon=-99.566&appid="+key
    # Check if the key works to acces the openweather api
    request1=requests.get(request).json()
    print(request1)