from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sport_app>.+)/$', views.index, name='sport_app'),
    url(r'^/login/$', views.log_in, name='login')
]
