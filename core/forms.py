# -*- coding: utf-8 -*-
from core import models
from .models import Projeto, User, PropostaUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome',
                  'descricao',
                  'local_trabalho',
                  'duracao',
                  'remuneracao',
                  'status']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'cpf',
                  'genero',
                  'telefone',
                  'endereco',
                  'descricao']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class PropostaUserForm(forms.ModelForm):
    class Meta:
        model = PropostaUser
        fields = ['from_user',
                  'to_user',
                  'dsc_proposta']
