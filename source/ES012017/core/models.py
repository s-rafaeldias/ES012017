from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class PerfilUsuario(models.Model):
    GENRE_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    USER_TYPE = (
        ('e', 'Empresa'),
        ('t', 'Trabalhador'),
    )
    usuario = models.OneToOneField(User)
    descricao = models.CharField(max_length=250)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True, choices=GENRE_CHOICES)
    perfil = models.CharField(max_length=1, choices=USER_TYPE)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=120)
    data_nacimento = models.DateField(blank=True, null=True)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            perfil_usuario = PerfilUsuario.objects.create(usuario=kwargs['instance'])

    post_save.connect(create_profile, sender=User)