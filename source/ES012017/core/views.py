from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.views.generic.edit import CreateView

# Import das models
from models import Emprego


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = {}

    def get_queryset(self):
        return #vai retornar algum objeto para ser usado

# Views da Model Emprego
class EmpregoCreate(CreateView):
    model  = Emprego
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
    success_url = '/'
