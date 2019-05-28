from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# TODO função para baixar o json e salvar no diretorio
# TODO função para verificar se o diretorio json esta vazio ou se existe arquivo do dia atual
# TODO funções para realizar a busca pela classe CNAE

def teste(request):
    return HttpResponse('hello world!')
