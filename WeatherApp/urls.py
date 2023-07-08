
from django.contrib import admin
from django.urls import path
from WeatherApp import views
urlpatterns = [
    path('',views.home),
    path('about/',views.About)
]
