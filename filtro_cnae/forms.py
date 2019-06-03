from django import forms
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
