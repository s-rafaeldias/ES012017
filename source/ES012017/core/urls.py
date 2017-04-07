from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^newEmprego/$', views.EmpregoCreate.as_view(), name='emprego_create'),
]