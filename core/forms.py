# -*- coding: utf-8 -*-
from core import models
from models import Freela, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class FreelaForm(forms.ModelForm):
    class Meta:
        model = Freela
        fields = ['nome',
                  'descricao',
                  'local_trabalho',
                  'jornada_trabalho',
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
                  'cpf_cnpj',
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
