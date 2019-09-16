from django.shortcuts import render
from django.http import HttpResponse


def teste(request):
    return HttpResponse('Ola gente bonita do meu Brasil!')