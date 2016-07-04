from django.conf.urls import patterns, url

from spy import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='spy'),
)
