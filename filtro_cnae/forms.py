from django import forms
import requests


def get_secoes_json():
    secoes_json = requests.get(url='https://servicodados.ibge.gov.br/api/v2/cnae/secoes')
    secoes_collected = secoes_json.json()
    return secoes_collected


class Secoes(forms.Form):
    SECOES = []
    secoes_collected = get_secoes_json()

    for secao in secoes_collected:
        SECOES_ID = secao['id']
        SECOES_DESC = secao['descricao']
        SECOES.append((f'{SECOES_ID}', f'{SECOES_DESC}'))

    secoes = forms.CharField(widget=forms.RadioSelect(choices=SECOES))


class Divisoes(forms.Form):
    pass
