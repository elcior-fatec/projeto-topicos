from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import requests
import os


# TODO função para baixar o json e salvar no diretorio
# TODO função para verificar se o diretorio json esta vazio ou se existe arquivo do dia atual
# TODO funções para realizar a busca pela classe CNAE

def get_cnae_json():
    classes_json = requests.get(url=f'https://servicodados.ibge.gov.br/api/v2/cnae/classes')
    return classes_json


@login_required
def search_classes(request):
    classes_collected = get_cnae_json().json()
    # return HttpResponse(classes_collected)
    return render(request,
                  'list-classes.html',
                  {'classes_collected': classes_collected})
