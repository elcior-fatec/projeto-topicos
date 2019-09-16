from django import forms
from .models import IbgeCNAE

import requests


def get_secoes_json():
    url = 'https://servicodados.ibge.gov.br/api/v2/cnae/secoes'
    secoes_json = requests.get(url)
    secoes_collected = secoes_json.json()
    return secoes_collected


class Secoes(forms.Form):
    SECOES = []
    secoes_collected = get_secoes_json()

    for secao in secoes_collected:
        SECOES_ID = secao['id']
        SECOES_DESC = secao['descricao']
        SECOES.append(('{}'.format(SECOES_ID), '{}'.format(SECOES_DESC)))

    secoes = forms.ChoiceField(choices=SECOES, widget=forms.RadioSelect)


class SalvaBuscaForm(forms.ModelForm):
    class Meta:
        model = IbgeCNAE
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
