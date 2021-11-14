from os import name
from django.urls import path
from .views import home, tts

urlpatterns = [
    path("", home, name="home"),
    path("speachsound", tts, name="tts")
]