from __future__ import unicode_literals

from django.core.validators import MinValueValidator

from django.db import models

# Create your models here.

class Emprego(models.Model):
    nome             = models.CharField(max_length=100)
    descricao        = models.CharField(max_length=250)
    empresa          = models.CharField(max_length=100)
    area_atuacao     = models.CharField(max_length=100)
    local_trabalho   = models.CharField(max_length=100)
    quantidade_vagas = models.PositiveIntegerField()
    jornada_trabalho = models.PositiveIntegerField()
    salario          = models.DecimalField(max_digits=8, decimal_places=2)
    atribuicoes      = models.TextField()
    status           = models.BooleanField()
    # Provavel tabela nova
    # area_formacao
    # conhecimentos_exigidos

