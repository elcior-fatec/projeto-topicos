from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SearchedCNAE
from .forms import Secoes, Divisoes

import requests
import os


# TODO funções para realizar a busca pela classe CNAE

def get_classes_json():
    classes_json = requests.get(url='https://servicodados.ibge.gov.br/api/v2/cnae/classes')
    return classes_json


def get_divisoes_json(secao_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao_id}/divisoes'
    divisoes_json = requests.get(url)
    divisoes_collected = divisoes_json.json()
    return divisoes_collected


@login_required
def list_secoes(request):
    form = Secoes()
    return render(request, 'list-secoes.html', {'form': form})


@login_required
def list_divisoes(request):
    divisoes_collected = get_divisoes_json(request.POST.get('secoes'))
    divisoes = []
    for divisao in divisoes_collected:
        divisoes.append({'id': f"{divisao['id']}", 'discricao': f"{divisao['descricao']}"})
    return render(request, 'list-divisoes.html', {'divisoes': divisoes})
