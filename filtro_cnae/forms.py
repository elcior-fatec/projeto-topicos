#!/usr/bin/python3.6
from django import forms
from django.forms import ModelForm, CharField
from .models import SearchedCNAE
import requests


def get_secoes_json():
    secoes_json = requests.get(url='https://servicodados.ibge.gov.br/api/v2/cnae/secoes')
    secoes_collected = secoes_json.json()
    return secoes_collected


def get_divisoes_json(secao_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao_id}/divisoes'
    divisoes_json = requests.get(url)
    divisoes_collected = divisoes_json.json()
    return divisoes_collected


class Secoes(forms.Form):
    SECOES = []
    secoes_collected = get_secoes_json()

    for secao in secoes_collected:
        SECOES_ID = secao['id']
        SECOES_DESC = secao['descricao']
        SECOES.append((f'{SECOES_ID}', f'{SECOES_DESC}'))

    secoes = forms.ChoiceField(choices=SECOES, widget=forms.RadioSelect)


class Divisoes(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Divisoes, self).__init__(*args, **kwargs)
        secao_id = args[0]['secoes']
        divisoes_collected = get_divisoes_json(secao_id)
        DIVISOES = []
        for divisao in divisoes_collected:
            DIVISOES.append((f"{divisao['id']}", f"{divisao['descricao']}"))

        self.divisoes = forms.ChoiceField(choices=DIVISOES, widget=forms.RadioSelect)


class SaveSearchesForm(ModelForm):
    class Meta:
        model = SearchedCNAE
        fields = (
            'id_user',
            'secao_id',
            'secao_descricao',
            'divisao_id',
            'divisao_descricao',
            'grupo_id',
            'grupo_descricao',
            'classe_id',
            'classe_descricao',
            'classe_observacoes',
            'published_date',
            'rel_ativo',
        )
