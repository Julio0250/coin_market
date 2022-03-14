from django.contrib import admin
from django.urls import path
from apps.coins.views import setup

app_name = 'coins'
urlpatterns = [
    path('setup/', setup, name='setup'),
]
