from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Urls Emprego
    url(r'^newEmprego/$', views.EmpregoCreate.as_view(), name='emprego-create'),
    url(r'^editEmprego/(?P<pk>\d+)/$', views.EmpregoUpdate.as_view(), name='emprego-update'),
    url(r'^deleteEmprego/(?P<pk>\d+)/$', views.EmpregoDelete.as_view(), name='emprego-delete'),
    url(r'^viewEmprego/(?P<pk>\d+)/$', views.EmpregoDetailView.as_view(), name='emprego-detail'),
    url(r'^listEmprego/$', views.EmpregoListView, name='emprego-list'),

    # Urls Usuario
    url(r'^registrar/$', views.register, name='registrar'),
    url(r'^login/$', login,{'template_name': 'core/Usuario/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^perfil/$', views.view_profile, name='perfil'),
    url(r'^editPerfil/$', views.UserUpdate.as_view(success_url='/perfil'), name='perfil-editar'),
    url(r'^editSenha/$', views.change_password, name='senha-editar'),

]
