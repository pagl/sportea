from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_tournament, name='add'),
    url(r'^new/$', views.new_tournament, name='new'),
    url(r'^search/$', views.search, name='search'),
    url(r'^refresh/$', views.refresh, name='refresh'),
    url(r'^join/(?P<join_id>.+)/$', views.join_tournament, name='join'),
    url(r'^score/$', views.score, name='score'),
    url(r'^register/(?P<register_id>.+)/$', views.register_to_tournament, name='register'),
    url(r'^update/(?P<update_id>.+)/$', views.update_tournament, name='update'),
    url(r'^registered/$', views.registered, name='registered'),
    url(r'^history/$', views.history, name='history'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^edit/(?P<edit_id>.+)/$', views.edit, name='edit_id'),
    url(r'^tournament/(?P<tournament_id>.+)/$', views.tournament, name='tournament_id'),
    url(r'^(?P<current_page>.+)/$', views.tournaments_list, name='current_page'),
]
