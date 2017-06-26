from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RegistrationForm
# Import das models
from .models import Projeto, User, PropostaUser, PropostaProjeto


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = {}

    def get_queryset(self):
        return #vai retornar algum objeto para ser listado caso precise

# Views da Model Projeto
class ProjetoCreate(CreateView):
  model  = Projeto
  template_name = 'core/Projeto/projeto_form.html'
  fields = ['nome',
            'descricao',
            'local_trabalho',
            'duracao',
            'remuneracao',
            'user',
            'status']
  success_url = reverse_lazy('index')

class ProjetoUpdate(UpdateView):
  model = Projeto
  fields = ['nome',
            'descricao',
            'local_trabalho',
            'duracao',
            'remuneracao',
            'status']
  success_url = reverse_lazy('index')


class ProjetoDelete(DeleteView):
  model = Projeto
  success_url = reverse_lazy('index')


class ProjetoDetailView(DetailView):
  model = Projeto
  template_name = 'core/Projeto/projeto_detail.html'

  def get_context_data(self, **kwargs):
    context = super(ProjetoDetailView, self).get_context_data(**kwargs)
    user = self.request.user
    context['inscrito'] = User.objects.filter(projeto=kwargs['object'].id, id=user.id).count()
    return context


def ProjetoListView(request):
    queryset_list = Projeto.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(nome__search = query)|
        Q(descricao__search=query)|
        Q(local_trabalho__search=query) |
        Q(remuneracao__contains=query)
        ).distinct()

    context = {
        "projeto": queryset_list
    }
    return render(request, "core/Projeto/projeto_list.html", context)


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
            return redirect('/registrar')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'core/Usuario/register.html', args)


def UserListView(request):
    queryset_list = User.objects.filter(is_superuser=False).order_by("id")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(first_name__search=query) |
            Q(last_name__search=query) |
            Q(descricao__icontains=query) |
            Q(email__contains=query) |
            Q(cpf__search=query)
        ).distinct()

    context = {
        "user": queryset_list
    }
    return render(request, "core/Usuario/user_list.html", context)


def view_profile(request,pk):
    user = User.objects.get(pk=pk)
    if user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'core/Usuario/perfil.html', {"user":user})


class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/Usuario/edit_profile.html'
    model = User
    fields = ['username',
              'first_name',
              'last_name',
              'email',
              'cpf',
              'genero',
              'telefone',
              'endereco',
              'descricao']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('perfil', args=(self.object.id,))


def change_password(request):
    user = request.user
    if user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return render(request, 'core/Usuario/perfil.html', {"user":user})
            else:
                return redirect('/editSenha', {"user":user})

        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'core/Usuario/change_password.html', args)


def signin_projeto(request, signin):
    user = request.user

    if user.is_anonymous:
        return redirect('/login')
    else:
        userdb = User.objects.get(pk=user.id)
        projetodb = Projeto.objects.get(pk=signin)
        userdb.projeto.add(projetodb)

        userdb.save()
        return redirect('projeto-list')

class PropostaUserCreate(CreateView):
    model = PropostaUser
    template_name = 'core/PropostaUser/proposta_user_form.html'
    fields = ['dsc_proposta']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(PropostaUserCreate, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        form.instance.to_user = User.objects.get(pk=self.kwargs.get('pk'))
        return super(PropostaUserCreate, self).form_valid(form)

class PropostaProjetoCreate(CreateView):
    model = PropostaProjeto
    template_name = 'core/PropostaProjeto/proposta_projeto_form.html'
    fields = ['oferta',
            'tempo',
            'infos']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.projeto = Projeto.objects.get(pk=self.kwargs.get('pk'))
        return super(PropostaProjetoCreate, self).form_valid(form)

class UserPropostasList(ListView):
    template_name = 'core/Usuario/user_offer_list.html'
    model = PropostaUser

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(UserPropostasList, self).get_context_data(**kwargs)
        projetos = Projeto.objects.filter(user__id=user.id)
        context['projects_offer_to_me'] = PropostaProjeto.objects.filter(projeto_id=projetos)
        context['projects_offer_by_me'] = PropostaProjeto.objects.filter(user_id=user.id)
        context['from_user'] = PropostaUser.objects.filter(from_user=user.id)
        context['to_user']   = PropostaUser.objects.filter(to_user=user.id)
        return context
