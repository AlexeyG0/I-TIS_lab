import requests
from django.conf import settings

APY_KEY = settings.API_KEY

def get_coordinates(city_name, country_code, api_key, limit=1):
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city_name},{country_code}",
        "limit": limit,
        "appid": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_weather(lat, lon, api_key, units="metric"):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()