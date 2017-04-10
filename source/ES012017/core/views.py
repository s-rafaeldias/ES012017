from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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
  success_url = reverse_lazy('index')


class EmpregoUpdate(UpdateView):
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
  success_url = reverse_lazy('index')


class EmpregoDelete(DeleteView):
  model = Emprego
  success_url = reverse_lazy('index')


class EmpregoDetailView(DetailView):
  model = Emprego
  template_name = 'core/emprego_detail.html'

  def get_context_data(self, **kwargs):
    context = super(EmpregoDetailView, self).get_context_data(**kwargs)
    return context

class EmpregoListView(ListView):
  model = Emprego
  context_object_name = 'lista_empregos'
  template_name = 'core/emprego_list.html'

  def get_queryset(self):
    return Emprego.objects.all()



