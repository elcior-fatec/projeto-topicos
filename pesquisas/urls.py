from django.urls import path
from .views import pesquisa_user, deletar_pesquisa, detalhar_pesquisa, desabilitar_item_pesquisa, export_json

urlpatterns = [
    path('pesquisas/', pesquisa_user, name='pesquisa_user'),
    path('delete-pesquisa/<int:id>/', deletar_pesquisa, name='deletar_pesquisa'),
    path('detalhar-pesquisa/<int:id>/', detalhar_pesquisa, name='detalhar_pesquisa'),
    path('desabilitar-item/<int:id>/', desabilitar_item_pesquisa, name='desabilitar_item_pesquisa'),
    path('export-json/', export_json, name='export_json'),
]
