from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.Index, name='index'),
    url(r'^work/', views.Work, name='work'),
    url(r'^new/', views.New, name='new'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<todo_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
