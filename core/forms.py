# -*- coding: utf-8 -*-

from models import Emprego
from django import forms

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
