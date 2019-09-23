"""projeto_topicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from sobre_projeto.views import sobre
from filtro_cnae import urls as cnae_urls
from pesquisas import urls as pesquisas_urls
from edit_users import urls as edit_users_urls

from ibge_cnae import urls as ibge_cnae_urls


urlpatterns = [
    path('', include(ibge_cnae_urls)),
    path('ibge-cnae/', include(ibge_cnae_urls)),
    path('sobre/', sobre, name='sobre'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('perfil/', include(pesquisas_urls)),
    path('edit/', include(edit_users_urls)),
]
