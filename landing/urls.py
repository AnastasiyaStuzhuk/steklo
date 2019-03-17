from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.conf.urls import url, include


urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
]
