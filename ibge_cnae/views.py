from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django import forms

from .forms import Secoes, SalvaBuscaForm
from .models import IbgeCNAE
from .serializers import IbgeCNAESerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import datetime


def teste(request):
    return HttpResponse('A curiosidade matou o gato.')


# Lista as Seções CNAE
@login_required
def list_secoes(request):
    form = Secoes
    return render(request, 'ibge_cnae/list-secoes.html', {'form': form})


# Lista as Divisões CNAE
@login_required
def list_divisoes(request):
    if request.POST.get('secoes') is None:
        return redirect('list_secoes_cnae')
    divisoes_collected = get_divisoes_json(request.POST.get('secoes'))
    divisoes = []
    for divisao in divisoes_collected:
        divisoes.append(
            {
                'id': divisao['id'],
                'descricao': divisao['descricao']
            }
        )
    return render(request, 'ibge_cnae/list-divisoes.html', {'divisoes': divisoes})


def get_divisoes_json(secao_id):
    url = 'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{}/divisoes'.format(secao_id)
    divisoes_json = requests.get(url)
    divisoes_collected = divisoes_json.json()
    return divisoes_collected


# Lista as Grupos CNAE
@login_required
def list_grupos(request):
    if request.POST.get('divisao') is None:
        return redirect('list_divisoes_cnae')
    grupos_collected = get_grupos_json(request.POST.get('divisao'))
    grupos = []
    for grupo in grupos_collected:
        grupos.append(
            {
                'id': grupo['id'],
                'descricao': grupo['descricao']
            }
        )
    return render(request, 'ibge_cnae/list-grupos.html', {'grupos': grupos})


def get_grupos_json(divisoes_id):
    url = 'https://servicodados.ibge.gov.br/api/v2/cnae/divisoes/{}/grupos'.format(divisoes_id)
    grupos_json = requests.get(url)
    grupos_collected = grupos_json.json()
    return grupos_collected


# Lista as Classes CNAE
@login_required
def list_classes(request):
    if request.POST.get('grupo') is None:
        return redirect('list_grupos_cnae')
    classes_collected = get_classes_json(request.POST.get('grupo'))
    classes = []
    for classe in classes_collected:
        classes.append(
            {
                'id': classe['id'],
                'descricao': classe['descricao'],
                'observacoes': classe['observacoes'],
            }
        )
    return render(request, 'ibge_cnae/list-classes.html', {'classes': classes})


def get_classes_json(grupos_id):
    url = 'https://servicodados.ibge.gov.br/api/v2/cnae/grupos/{}/classes'.format(grupos_id)
    classes_json = requests.get(url)
    classes_collected = classes_json.json()
    return classes_collected


# Mostra resultado da busca CNAE
@login_required
def merge_search(request):
    if request.POST.get('classe') is None:
        return redirect('list_grupos_cnae')
    classe_c = get_final_classe_json(request.POST.get('classe'))
    data_agora = datetime.datetime.now()
    form = SalvaBuscaForm(
        initial={
            'id_user': request.user.id,
            'secao_id': classe_c['grupo']['divisao']['secao']['id'],
            'secao_descricao': classe_c['grupo']['divisao']['secao']['descricao'],
            'divisao_id': classe_c['grupo']['divisao']['id'],
            'divisao_descricao': classe_c['grupo']['divisao']['descricao'],
            'grupo_id': classe_c['grupo']['id'],
            'grupo_descricao': classe_c['grupo']['descricao'],
            'classe_id': classe_c['id'],
            'classe_descricao': classe_c['descricao'],
            'classe_observacoes': classe_c['observacoes'][0],
            'published_date': data_agora,
            'rel_ativo': True,
        }
    )
    form.fields['id_user'] = forms.CharField()
    form.fields['id_user'].widget.attrs['readonly'] = True
    form.fields['secao_id'].widget.attrs['readonly'] = True
    form.fields['secao_descricao'].widget.attrs['readonly'] = True
    form.fields['divisao_id'].widget.attrs['readonly'] = True
    form.fields['divisao_descricao'].widget.attrs['readonly'] = True
    form.fields['grupo_id'].widget.attrs['readonly'] = True
    form.fields['grupo_descricao'].widget.attrs['readonly'] = True
    form.fields['classe_id'].widget.attrs['readonly'] = True
    form.fields['classe_descricao'].widget.attrs['readonly'] = True
    form.fields['classe_observacoes'].widget.attrs['readonly'] = True
    form.fields['published_date'].widget.attrs['readonly'] = True
    form.fields['rel_ativo'] = forms.CharField()
    form.fields['rel_ativo'].widget.attrs['readonly'] = True

    return render(request, 'ibge_cnae/salvar-pesquisa.html', {'form': form})


def get_final_classe_json(classe_id):
    url = 'https://servicodados.ibge.gov.br/api/v2/cnae/classes/{}'.format(classe_id)
    classe_json = requests.get(url)
    classe_collected = classe_json.json()
    return classe_collected


# Salva busca CNAE no banco de dados
@login_required
def save_search(request):
    if request.POST.get('classe_id') is None:
        return redirect('list_grupos_cnae')
    classe_c = get_final_classe_json(request.POST.get('classe_id'))
    data_agora = datetime.datetime.now()
    form = SalvaBuscaForm(request.POST)

    form.id_user = request.user.id
    form.secao_id = classe_c['grupo']['divisao']['secao']['id']
    form.secao_descricao = classe_c['grupo']['divisao']['secao']['descricao']
    form.divisao_id = classe_c['grupo']['divisao']['id']
    form.divisao_descricao = classe_c['grupo']['divisao']['descricao']
    form.grupo_id = classe_c['grupo']['id']
    form.grupo_descricao = classe_c['grupo']['descricao']
    form.classe_id = classe_c['id']
    form.classe_descricao = classe_c['descricao']
    form.classe_observacoes = classe_c['observacoes'][0]
    form.published_date = data_agora
    form.rel_ativo = True

    if form.is_valid():
        form.save()

    return redirect('minhas_pesquisas_cnae')


# Faz a busca dos objetos, no banco, por usuário
@login_required
def pesquisa_user(request):
    pesquisas = IbgeCNAE.objetos.filter(id_user=request.user.id)
    return render(request, 'ibge_cnae/minhas-pesquisas.html', {'pesquisas': pesquisas})


# Retorna o JSON construido do 'objeto' criado no Models
class IbgeCnaelist(APIView):

    def get(self, request):
        lista_de_pesquisas = IbgeCNAE.objetos.all()
        serializer = IbgeCNAESerializer(lista_de_pesquisas, many=True)
        return Response(serializer.data)

    def post(self):
        pass
