# -*- coding: utf-8 -*-
from core import models
from models import Emprego, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EmpregoForm(forms.ModelForm):
    class Meta:
        model = Emprego
        fields = ['nome',
                  'descricao',
                  'empresa',
                  'area_atuacao',
                  'local_trabalho',
                  'quantidade_vagas',
                  'jornada_trabalho',
                  'salario',
                  'atribuicoes',
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
                  'descricao',
                  'cpf',
                  'cnpj',
                  'genero',
                  'perfil',
                  'telefone',
                  'endereco']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditRegistrationForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'descricao',
                  'cpf',
                  'cnpj',
                  'genero',
                  'perfil',
                  'telefone',
                  'endereco']

    def save(self, commit=True):
        user = super(EditRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
