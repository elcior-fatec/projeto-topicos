from django import forms
import requests


def get_secoes_json():
    secoes_json = requests.get(url='https://servicodados.ibge.gov.br/api/v2/cnae/secoes')
    secoes_collected = secoes_json.json()
    return secoes_collected


def get_divisoes_json(secao_id):
    divisoes_json = requests.get(url=f'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao_id}/divisoes')
    divisoes_collected = divisoes_json.json()
    return divisoes_collected


class Secoes(forms.Form):
    SECOES = []
    secoes_collected = get_secoes_json()

    for secao in secoes_collected:
        SECOES_ID = secao['id']
        SECOES_DESC = secao['descricao']
        SECOES.append((f'{SECOES_ID}', f'{SECOES_DESC}'))

    secoes = forms.CharField(widget=forms.RadioSelect(choices=SECOES))


class Divisoes(forms.Form):
    def __init__(self, *args, **kwargs):
        self.secao = kwargs.pop('secao')
        super(Divisoes, self).__init__(*args, **kwargs)

        '''divisoes_collected = get_divisoes_json(self.secao)
        DIVISOES = []

        for divisao in divisoes_collected:
            DIVISOES_ID = divisao['id']
            DIVISOES_DESC = divisao['descricao']
            DIVISOES.append((f'{DIVISOES_ID}', f'{DIVISOES_DESC}'))

        divisoes = forms.CharField(widget=forms.RadioSelect(choices=DIVISOES))'''

    divisoes_collected = get_divisoes_json('A')
    DIVISOES = []

    for divisao in divisoes_collected:
        DIVISOES_ID = divisao['id']
        DIVISOES_DESC = divisao['descricao']
        DIVISOES.append((f'{DIVISOES_ID}', f'{DIVISOES_DESC}'))

    divisoes = forms.CharField(widget=forms.RadioSelect(choices=DIVISOES))
