from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import requests
import os


# TODO funções para realizar a busca pela classe CNAE

def get_classes_json():
    classes_json = requests.get(url=f'https://servicodados.ibge.gov.br/api/v2/cnae/classes')
    return classes_json


def get_secoes_json():
    secoes_json = requests.get(url=f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes')
    return secoes_json


def get_divisoes_json(secao_id):
    divisoes_json = requests.get(url=f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao_id}/divisoes')
    return divisoes_json


@login_required
def list_secoes(request):
    secoes_collected = get_secoes_json().json()
    return render(request,
                  'list-secoes.html',
                  {'secoes_collected': secoes_collected})


@login_required
def list_divisoes(request, secao_id):

    divisao_collected = get_divisoes_json(secao_id).json()
    secoes_collected = get_secoes_json().json()
    road = {'secao_id': secao_id}
    return render(request,
                  'list-divisoes.html',
                  {'divisao_collected': divisao_collected},
                  {'secoes_collected': secoes_collected},
                  {'road': road})
