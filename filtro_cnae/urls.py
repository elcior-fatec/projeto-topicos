from django.urls import path
from .views import (
    list_secoes,
    list_divisoes,
    list_grupos,
    list_classes,
    save_search,
    save_search_final,
    logout_sys
)


urlpatterns = [
    path('', list_secoes, name='home'),
    path('logout/', logout_sys, name='logout'),
    path('list-secoes/', list_secoes, name="list_secoes"),
    path('list-divisoes/', list_divisoes, name="list_divisoes"),
    path('list-grupos/', list_grupos, name="list_grupos"),
    path('list-classes/', list_classes, name="list_classes"),
    path('save-search/', save_search, name="save_search"),
    path('save-search-final/', save_search_final, name="save_search_final"),
]
