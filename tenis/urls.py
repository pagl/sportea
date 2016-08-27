from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tournament_id>.+)/$', views.tournament, name='tournament_id'),
]
