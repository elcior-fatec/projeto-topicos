from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SearchedCNAE
from .forms import Secoes, Divisoes

import requests
import os


'''
Funções para captura dos json
'''
def get_divisoes_json(secao_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao_id}/divisoes'
    divisoes_json = requests.get(url)
    divisoes_collected = divisoes_json.json()
    return divisoes_collected


def get_grupos_json(divisoes_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/divisoes/{divisoes_id}/grupos'
    grupos_json = requests.get(url)
    grupos_collected = grupos_json.json()
    return grupos_collected


def get_classes_json(grupos_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/grupos/{grupos_id}/classes'
    classes_json = requests.get(url)
    classes_collected = classes_json.json()
    return classes_collected


'''
Funções para processamento das requests
'''
@login_required
def list_secoes(request):
    form = Secoes()
    return render(request, 'list-secoes.html', {'form': form})


@login_required
def list_divisoes(request):
    divisoes_collected = get_divisoes_json(request.POST.get('secoes'))
    divisoes = []
    for divisao in divisoes_collected:
        divisoes.append(
            {
                'id': f"{divisao['id']}",
                'descricao': f"{divisao['descricao']}"
            }
        )
    return render(request, 'list-divisoes.html', {'divisoes': divisoes})


@login_required
def list_grupos(request):
    grupos_collected = get_grupos_json(request.POST.get('divisao'))
    grupos = []
    for grupo in grupos_collected:
        grupos.append(
            {
                'id': f"{grupo['id']}",
                'descricao': f"{grupo['descricao']}"
            }
        )
    return render(request, 'list-grupos.html', {'grupos': grupos})


def list_classes(request):
    classes_collected = get_classes_json(request.POST.get('grupo'))
    classes = []
    for classe in classes_collected:
        classes.append(
            {
                'id': f"{classe['id']}",
                'descricao': f"{classe['descricao']}",
                'observacoes': classe['observacoes'],
            }
        )
    return render(request, 'list-classes.html', {'classes': classes})
