from django.contrib import admin
from django.urls import path
from .views import list_secoes
from .views import list_divisoes


urlpatterns = [
    path('list-secoes/', list_secoes, name="list_secoes"),
    path('list-divisoes/', list_divisoes, name="list_divisoes"),
]
