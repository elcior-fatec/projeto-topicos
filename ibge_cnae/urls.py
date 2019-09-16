from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste),
    path('secoes-cnae/', views.list_secoes, name='list_secoes_cnae'),
    path('divisoes-cnae/', views.list_divisoes, name="list_divisoes_cnae"),
    path('grupos-cnae/', views.list_grupos, name="list_grupos_cnae"),
    path('classes-cnae/', views.list_classes, name="list_classes_cnae"),
    path('completa-busca/', views.merge_search, name="completa_busca_cnae"),
    path('salva-busca/', views.save_search, name="salva_busca_cnae"),
    path('minhas-pesquisas/', views.pesquisa_user, name='minhas_pesquisas_cnae'),
]
