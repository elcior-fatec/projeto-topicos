#!/usr/bin/python3.6
from django.db import models
from django.utils import timezone


class SearchedCNAE(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    secao_id = models.CharField(max_length=2, verbose_name='id da seção')
    secao_descricao = models.CharField(max_length=150, verbose_name='nome da seção')
    divisao_id = models.CharField(max_length=5, verbose_name='id da divisão')
    divisao_descricao = models.CharField(max_length=150, verbose_name='nome da divisão')
    grupo_id = models.CharField(max_length=5, verbose_name='id do grupo')
    grupo_descricao = models.CharField(max_length=150, verbose_name='nome do grupo')
    classe_id = models.CharField(max_length=5, verbose_name='id da classe')
    classe_descricao = models.CharField(max_length=150, verbose_name='nome da classe')
    classe_observacoes = models.TextField(verbose_name='descrição da classe')
    published_date = models.DateTimeField(verbose_name='data da publicação')
    rel_ativo = models.BooleanField(verbose_name='ativo')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'pesquisa nº {self.pk}'

    class Meta:
        verbose_name = "Histórico de pesquisas"
        verbose_name_plural = "Históricos de pesquisas"
