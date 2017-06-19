from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Freela(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    local_trabalho = models.CharField(max_length=100)
    jornada_trabalho = models.PositiveIntegerField()
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class User(AbstractUser):
    GENRE_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nao aplicavel'),
    )
    descricao = models.CharField(max_length=250)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True, choices=GENRE_CHOICES)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=120)
    freela = models.ManyToManyField(Freela)
