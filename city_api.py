# city validity

import requests as rq
import json
import os

get_cities = rq.get("https://countriesnow.space/api/v0.1/countries")


def get_valid(city):
    cities = []

    for country in get_cities.json()["data"]:
        cities.extend(country["cities"])

    if city.capitalize() in [c.capitalize() for c in cities]:
        return True
    else:
        return False
