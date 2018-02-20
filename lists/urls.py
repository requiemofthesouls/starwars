from django.contrib import admin
from django.urls import path
from lists import views
from django.conf.urls import include


urlpatterns = [
    path('', views.ships, name='ships')
]
