from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_view, name='data_view'),
    path('', views.index, name='index_view'),
    path('test', views.test, name='test'),
]
