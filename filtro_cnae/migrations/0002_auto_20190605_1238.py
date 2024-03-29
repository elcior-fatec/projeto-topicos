# Generated by Django 2.2.1 on 2019-06-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtro_cnae', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchedcnae',
            options={'verbose_name': 'Histórico de pesquisas', 'verbose_name_plural': 'Históricos de pesquisas'},
        ),
        migrations.AlterField(
            model_name='searchedcnae',
            name='classe_descricao',
            field=models.CharField(max_length=150, verbose_name='nome da classe'),
        ),
        migrations.AlterField(
            model_name='searchedcnae',
            name='divisao_descricao',
            field=models.CharField(max_length=150, verbose_name='nome da divisão'),
        ),
        migrations.AlterField(
            model_name='searchedcnae',
            name='grupo_descricao',
            field=models.CharField(max_length=150, verbose_name='nome do grupo'),
        ),
        migrations.AlterField(
            model_name='searchedcnae',
            name='secao_descricao',
            field=models.CharField(max_length=150, verbose_name='nome da seção'),
        ),
    ]
