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

'''
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
'''


@login_required
def list_secoes(request):
    form = Secoes()
    return render(request, 'list-secoes.html', {'form': form})\



@login_required
def list_divisoes(request):
    if request.POST is None:
        return redirect('list_secoes')

    form = Divisoes(secao=request.POST.get('secoes'))
    return render(request, 'list-divisoes.html', {'form': form})
