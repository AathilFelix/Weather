import requests as rq
import json
import city_api
import weather_api

valid = 0

while True:
    city = input("City Name: ")
    if city_api.get_valid(city) == True:
        valid = 1
    else:
        valid = 0


    while valid == 1:
        weather_api.get_weather_data(city)
        break


    while valid == 0:
        print("Invalid City Name/Not enlisted in our database")
        break

