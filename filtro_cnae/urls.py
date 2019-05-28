from django.contrib import admin
from django.urls import path
from .views import search_classes


urlpatterns = [
    path('list-classes/', search_classes, name="list-classes"),
]
