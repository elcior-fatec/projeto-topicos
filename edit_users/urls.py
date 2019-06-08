from django.urls import path
from .views import edit_user


urlpatterns = [
    path('user/', edit_user, name='edit_user'),
]