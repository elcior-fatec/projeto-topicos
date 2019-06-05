from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import SearchedCNAE
from .forms import Secoes, SaveSearchesForm

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

def get_final_classe_json(classe_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/classes/{classe_id}'
    classe_json = requests.get(url)
    classe_collected = classe_json.json()
    return classe_collected


'''
Funções para processamento das requests
'''
@login_required
def list_secoes(request):
    form = Secoes()
    return render(request, 'list-secoes.html', {'form': form})


@login_required
def list_divisoes(request):
    if request.POST.get('secoes') is None:
        return redirect('list_secoes')
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
    if request.POST.get('divisao') is None:
        return redirect('list_secoes')
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


@login_required
def list_classes(request):
    if request.POST.get('grupo') is None:
        return redirect('list_secoes')
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


@login_required
def save_search(request):
    classe_c = get_final_classe_json(request.POST.get('classe'))
    data_agora = datetime.datetime.now()

    form = SaveSearchesForm(
        initial={
            'id_user': f'{request.user.id}',
            'secao_id': f"{classe_c['grupo']['divisao']['secao']['id']}",
            'secao_descricao': f"{classe_c['grupo']['divisao']['secao']['descricao']}",
            'divisao_id': f"{classe_c['grupo']['divisao']['id']}",
            'divisao_descricao': f"{classe_c['grupo']['divisao']['descricao']}",
            'grupo_id': f"{classe_c['grupo']['id']}",
            'grupo_descricao': f"{classe_c['grupo']['descricao']}",
            'classe_id': f"{classe_c['id']}",
            'classe_descricao': f"{classe_c['descricao']}",
            'classe_observacoes': f"{classe_c['observacoes'][0]}",
            'published_date': f"{data_agora}",
            'rel_ativo': True,
        }
    )
    form.form_read_only = True

    if form.is_valid():
        form.save()
        return redirect('list_secoes')

    return render(request, 'salvar-pesquisa.html', {'form': form})
