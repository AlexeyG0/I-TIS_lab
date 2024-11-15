from metrology.celery import app
from .models import Sensor, Measurement, Location
import random
from .api import *


@app.task
def log_sensor_data():
    sensors = Sensor.objects.all()
    for sensor in sensors:
        # Симуляция получение данных от сенсора
        if sensor.type_sensor == 'temperature':
            value = random.uniform(15.0, 25.0)  # температура
        elif sensor.type_sensor == 'humidity':
            value = random.uniform(30.0, 80.0)  # влажность
        Measurement.objects.create(sensor=sensor, value=value)


def log_sensor_data_api():
    locations = Location.objects.all()
    for location in locations:
        lat = location.lat
        lon = location.lon
        print('!!!! ЗАПРОС')
        response = get_weather(lat, lon, APY_KEY)
        print('!!!! ЗАПРОС: ', response)
        city_name = response['name']  # Название города
        country = response['sys']['country']  # Страна
        temperature = response['main']['temp']  # Температура
        feels_like = response['main']['feels_like']  # Ощущаемая температура
        humidity = response['main']['humidity']  # Влажность
        weather_description = response['weather'][0]['description']  # Описание погоды
        wind_speed = response['wind']['speed']  # Скорость ветра

        sensors = Sensor.objects.filter(location=location)
        for sensor in sensors:
            if sensor.type_sensor == 'temperature':
                Measurement.objects.create(sensor=sensor, value=temperature)
            elif sensor.type_sensor == 'humidity':
                Measurement.objects.create(sensor=sensor, value=humidity)
            elif sensor.type_sensor == 'wind_speed':
                Measurement.objects.create(sensor=sensor, value=wind_speed)

