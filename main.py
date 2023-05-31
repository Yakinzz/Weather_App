import requests
from pprint import pprint

APY_Key = 'a15b9dd0f9883530419a8ea31618ea0d'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+APY_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)