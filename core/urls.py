from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Urls Freela
    url(r'^newFreela/$', views.FreelaCreate.as_view(), name='freela-create'),
    url(r'^editFreela/(?P<pk>\d+)/$', views.FreelaUpdate.as_view(), name='freela-update'),
    url(r'^deleteFreela/(?P<pk>\d+)/$', views.FreelaDelete.as_view(), name='freela-delete'),
    url(r'^viewFreela/(?P<pk>\d+)/$', views.FreelaDetailView.as_view(), name='freela-detail'),
    url(r'^listFreela/$', views.FreelaListView, name='freela-list'),
    url(r'^signinFreela/(?P<signin>\d+)/$', views.signin_freela, name="signin-freela"),

    # Urls Usuario
    url(r'^registrar/$', views.register, name='registrar'),
    url(r'^listUser/$', views.UserListView, name='user-list'),
    url(r'^login/$', login,{'template_name': 'core/Usuario/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^perfil/(?P<pk>\d+)$', views.view_profile, name='perfil'),
    url(r'^editPerfil/(?P<pk>\d+)$', views.UserUpdate.as_view(), name='perfil-editar'),
    url(r'^editSenha/$', views.change_password, name='senha-editar'),

]
