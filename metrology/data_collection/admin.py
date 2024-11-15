from django.contrib import admin
from .models import Location, Sensor, Measurement, Report

admin.site.register(Location)
admin.site.register(Sensor)
admin.site.register(Measurement)
admin.site.register(Report)