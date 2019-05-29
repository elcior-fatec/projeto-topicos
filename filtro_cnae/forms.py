from django.forms import ModelForm
from .models import SearchedCNAE


class Secoes(ModelForm):
    class Meta:
        model = SearchedCNAE
        fields = [
            'secao_id',
        ]
