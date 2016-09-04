from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tournament/(?P<tournament_id>.+)/$', views.tournament, name='tournament_id'),
    url(r'^(?P<current_page>.+)/$', views.tournaments_list, name='current_page'),
]
