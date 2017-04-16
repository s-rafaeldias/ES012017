from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #Urls para o CRUD de Emprego
    url(r'^newEmprego/$', views.EmpregoCreate.as_view(), name='emprego-create'),
    url(r'^editEmprego/(?P<pk>\d+)/$', views.EmpregoUpdate.as_view(), name='emprego-update'),
    url(r'^deleteEmprego/(?P<pk>\d+)/$', views.EmpregoDelete.as_view(), name='emprego-delete'),
    url(r'^viewEmprego/(?P<pk>\d+)/$', views.EmpregoDetailView.as_view(), name='emprego-detail'),
    url(r'^listEmprego/$', views.EmpregoListView.as_view(), name='emprego-list'),

]