from django.urls import path, include
from django.contrib.auth.decorators import login_required
from ibge_cnae import views

urlpatterns = [
    path('', login_required(views.IndexTemplateView.as_view()), name='index_cnae'),
    path('logout/', views.logout_sys, name='logout'),
    path('secoes-cnae/', views.list_secoes, name='list_secoes_cnae'),
    path('divisoes-cnae/', views.list_divisoes, name="list_divisoes_cnae"),
    path('grupos-cnae/', views.list_grupos, name="list_grupos_cnae"),
    path('classes-cnae/', views.list_classes, name="list_classes_cnae"),
    path('completa-busca/', views.merge_search, name="completa_busca_cnae"),
    path('salva-busca/', views.save_search, name="salva_busca_cnae"),
    path('minhas-pesquisas/', views.pesquisa_user, name='minhas_pesquisas_cnae'),
    path('deletar/item/<int:pk>', views.PesquisaDeleteView.as_view(), name='deletar_item_cnae'),
    # TODO: Migrar o "Detalhes" de pesquisas para o modulo ibge_cnae
    # API REST
    path('api-rest/', login_required(views.IbgeCnaeList.as_view()), name='api_cnae')
]
