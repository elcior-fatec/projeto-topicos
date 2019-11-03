from django.urls import path, include
from django.contrib.auth.decorators import login_required
from ibge_noticias import views

urlpatterns = [
    path('', views.noticias, name='ibge_noticias'),
]
