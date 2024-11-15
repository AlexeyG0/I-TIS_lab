import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'metrology.settings')

app = Celery('metrology')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

# Выполняемые задачи
app.conf.beat_schedule = {
    'log_sensor_data': { 
        'task': 'data_collection.tasks.log_sensor_data',
        'schedule': crontab(minute='*/1'),
    }
}