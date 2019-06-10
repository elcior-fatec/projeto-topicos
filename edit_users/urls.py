from django.urls import path
from .views import edit_user, new_user, change_pass


urlpatterns = [
    path('user/', edit_user, name='edit_user'),
    path('password/', change_pass, name='change_pass'),
    path('novo-usuario/', new_user, name='new_user'),
]
