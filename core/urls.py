from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Urls Projeto
    url(r'^newProjeto/$', views.ProjetoCreate.as_view(), name='projeto-create'),
    url(r'^editProjeto/(?P<pk>\d+)/$', views.ProjetoUpdate.as_view(), name='projeto-update'),
    url(r'^deleteProjeto/(?P<pk>\d+)/$', views.ProjetoDelete.as_view(), name='projeto-delete'),
    #url(r'^viewProjeto/(?P<pk>\d+)/$', views.ProjetoDetailView.as_view(), name='projeto-detail'),
    url(r'^listProjeto/$', views.ProjetoListView, name='projeto-list'),
    url(r'^signinProjeto/(?P<signin>\d+)/$', views.signin_projeto, name="signin-projeto"),

    # Urls Usuario
    url(r'^registrar/$', views.register, name='registrar'),
    url(r'^listUser/$', views.UserListView, name='user-list'),
    url(r'^login/$', login,{'template_name': 'core/Usuario/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^perfil/(?P<pk>\d+)$', views.view_profile, name='perfil'),
    url(r'^editPerfil/(?P<pk>\d+)$', views.UserUpdate.as_view(), name='perfil-editar'),
    url(r'^editSenha/$', views.change_password, name='senha-editar'),

    # Urls PropostaUser
    url(r'^propostaUser/$', views.PropostaUserCreate.as_view(), name='fazer-proposta-user'),

    #Urls PropostaProjeto
    url(r'^newPropostaProjeto/(?P<pk>\d+)$', views.PropostaProjetoCreate.as_view(), name='projeto-proposta-create')

]
