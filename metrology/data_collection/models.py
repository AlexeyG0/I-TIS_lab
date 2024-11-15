from django.db import models
from django.core.validators import RegexValidator

class Location(models.Model):
    lat_validator = RegexValidator(
        regex=r'^-?\d{1,2}\.\d+$',
        message="Latitude must be in the format like '44.5609447'."
    )
    lon_validator = RegexValidator(
        regex=r'^-?\d{1,3}\.\d+$',
        message="Longitude must be in the format like '44.5609447'."
    )

    name = models.CharField(max_length=255)
    lat = models.FloatField(validators=[lat_validator])
    lon = models.FloatField(validators=[lon_validator])
    description = models.TextField(blank=True)

class Sensor(models.Model):
    type_sensor_choices = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('wind_speed', 'Wind_speed')
    ]
    type_sensor = models.CharField(max_length=20, choices=type_sensor_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.type_sensor} sensor at {self.location}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor} - {self.value} at {self.timestamp}'

class Report(models.Model):
    user = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f'Report from {self.timestamp} for {self.location}'