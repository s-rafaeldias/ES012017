from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth.views import PasswordChangeForm
# Import das models
from models import Freela, User


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = {}

    def get_queryset(self):
        return #vai retornar algum objeto para ser listado caso precise

# Views da Model Freela
class FreelaCreate(CreateView):
  model  = Freela
  template_name = 'core/Freela/freela_form.html'
  fields = ['nome',
            'descricao',
            'local_trabalho',
            'jornada_trabalho',
            'remuneracao',
            'status']
  success_url = reverse_lazy('index')


class FreelaUpdate(UpdateView):
  model = Freela
  fields = ['nome',
            'descricao',
            'local_trabalho',
            'jornada_trabalho',
            'remuneracao',
            'status']
  success_url = reverse_lazy('index')


class FreelaDelete(DeleteView):
  model = Freela
  success_url = reverse_lazy('index')


class FreelaDetailView(DetailView):
  model = Freela
  template_name = 'core/Freela/freela_detail.html'

  def get_context_data(self, **kwargs):
    context = super(FreelaDetailView, self).get_context_data(**kwargs)
    user = self.request.user
    context['inscrito'] = User.objects.filter(freela=kwargs['object'].id, id=user.id).count()
    return context


def FreelaListView(request):
    queryset_list = Freela.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(nome__search = query)|
        Q(descricao__search=query)|
        Q(area_atuacao__search=query) |
        Q(remuneracao__contains=query)
        ).distinct()

    context = {
        "freela": queryset_list
    }
    return render(request, "core/Freela/freela_list.html", context)


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


class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/Usuario/edit_profile.html'
    model = User
    fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'cpf_cnpj',
                  'genero',
                  'telefone',
                  'endereco',
                  'descricao']

    def get_object(self, queryset=None):
        return self.request.user


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


def signin_freela(request, signin):
    user = request.user

    if user.is_anonymous:
        return redirect('/login')
    else:
        userdb = User.objects.get(pk=user.id)
        freeladb = Freela.objects.get(pk=signin)
        userdb.freela.add(freeladb)

        userdb.save()
        return redirect('freela-list')