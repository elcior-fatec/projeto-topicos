from django.contrib import admin
from django.urls import path
from .views import list_secoes, list_divisoes, list_grupos, list_classes


urlpatterns = [
    path('list-secoes/', list_secoes, name="list_secoes"),
    path('list-divisoes/', list_divisoes, name="list_divisoes"),
    path('list-grupos/', list_grupos, name="list_grupos"),
    path('list-classes/', list_classes, name="list_classes"),
    path('save-search/', list_classes, name="list_classes"),
]
