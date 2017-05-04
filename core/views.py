from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.http import HttpResponseRedirect, request, HttpRequest
from django.db.models import Q


# Create your views here.
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from .forms import RegistrationForm, EditRegistrationForm
from django.contrib.auth.views import PasswordChangeForm
# Import das models
from models import Emprego, User


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = {}

    def get_queryset(self):
        return #vai retornar algum objeto para ser listado caso precise

# Views da Model Emprego
class EmpregoCreate(CreateView):
  model  = Emprego
  template_name = 'core/Emprego/emprego_form.html'
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
  template_name = 'core/Emprego/emprego_detail.html'

  def get_context_data(self, **kwargs):
    context = super(EmpregoDetailView, self).get_context_data(**kwargs)
    return context


def EmpregoListView(request):
    queryset_list = Emprego.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(nome__search = query)|
        Q(descricao__search=query)|
        Q(empresa__search=query)|
        Q(area_atuacao__search=query) |
        Q(salario__contains=query)
        ).distinct()

    context = {
        "emprego": queryset_list
    }
    return render(request, "core/Emprego/emprego_list.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'core/Usuario/register.html', args)


def view_profile(request):
    args = {'user': request.user}
    user = request.user
    if user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'core/Usuario/perfil.html', args)


def edit_profile(request):
    user = request.user
    if user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            form = EditRegistrationForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/perfil')
        else:
            form = EditRegistrationForm(instance=request.user)
            args = {'form': form}
            return render(request, 'core/Usuario/edit_profile.html', args)


def change_password(request):
    user = request.user
    if user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/perfil')
            else:
                return redirect('/editSenha')
        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'core/Usuario/change_password.html', args)