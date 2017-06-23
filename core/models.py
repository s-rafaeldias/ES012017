from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

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
    # projeto = models.ManyToManyField(Projeto, blank=True)
    propostasUsers = models.ManyToManyField('self',
                                            through='PropostaUser',
                                            symmetrical=False)


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    local_trabalho = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    propostas = models.ManyToManyField(User, through='PropostaProjeto', related_name = 'propostas')

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class PropostaUser(models.Model):
    dsc_proposta = models.CharField(max_length=1000)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')

class PropostaProjeto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    oferta = models.DecimalField(max_digits=10, decimal_places=2)
    tempo = models.PositiveIntegerField()
    infos = models.CharField(max_length=500)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.id
