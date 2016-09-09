from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_tournament, name='add'),
    url(r'^new/$', views.new_tournament, name='new'),
    url(r'^join/(?P<join_id>.+)/$', views.join_tournament, name='join'),
    url(r'^register/(?P<register_id>.+)/$', views.register_to_tournament, name='register'),
    url(r'^update/(?P<update_id>.+)/$', views.update_tournament, name='update'),
    url(r'^mytournaments/$', views.mytournaments, name='mytournaments'),
    url(r'^mymatches/$', views.mymatches, name='mymatches'),
    url(r'^edit/(?P<edit_id>.+)/$', views.edit, name='edit_id'),
    url(r'^tournament/(?P<tournament_id>.+)/$', views.tournament, name='tournament_id'),
    url(r'^(?P<current_page>.+)/$', views.tournaments_list, name='current_page'),
]
