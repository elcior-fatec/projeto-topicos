from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

import requests


def get_noticias():
    url = 'http://servicodados.ibge.gov.br/api/v3/noticias'
    noticias_collected = requests.get(url).json()
    return noticias_collected


@login_required
def noticias(request):
    noticias_view = []
    noticias_collected = get_noticias()
    for noticia in noticias_collected['items']:
        noticias_view.append(
            {
                'titulo': noticia['titulo'],
                'introducao': noticia['introducao'],
                'link': noticia['link'],
                'data': noticia['data_publicacao'],
            }
        )
        if len(noticias_view) > 9:
            return render(request, 'ibge_noticias/noticias.html', {'noticias': noticias_view})
