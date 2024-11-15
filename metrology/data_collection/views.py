from django.shortcuts import render, HttpResponse
from .models import *
from .tasks import log_sensor_data_api


def data_view(request):
    measurements = Measurement.objects.all().order_by('-timestamp')
    return render(request, 'data_view.html', {'measurements': measurements})


def index(request):
    # Получаем все локации
    locations = Location.objects.all()

    # Формируем данные с последними измерениями для каждого сенсора
    location_data = []
    for location in locations:
        sensors = Sensor.objects.filter(location=location)
        sensors_with_measurements = []
        for sensor in sensors:
            # Получаем последнее измерение для сенсора
            latest_measurement = Measurement.objects.filter(sensor=sensor).order_by('-timestamp').first()
            sensors_with_measurements.append({
                'sensor': sensor,
                'latest_measurement': latest_measurement
            })
        location_data.append({
            'location': location,
            'sensors_with_measurements': sensors_with_measurements
        })

    return render(request, 'index.html', {'location_data': location_data})

def test(request):
    log_sensor_data_api()
    return HttpResponse('Запрос успешен')