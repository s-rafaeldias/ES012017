from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class User(AbstractUser):
    GENRE_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    USER_TYPE = (
        ('e', 'Empresa'),
        ('t', 'Trabalhador'),
    )
    descricao = models.CharField(max_length=250)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True, choices=GENRE_CHOICES)
    perfil = models.CharField(max_length=1, choices=USER_TYPE)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=120)
    empregos = models.ManyToManyField(Emprego)
