from django.contrib import admin
from django.urls import path
from .views import teste


urlpatterns = [
    path('teste/', teste, name="Apagar este teste"),
]
