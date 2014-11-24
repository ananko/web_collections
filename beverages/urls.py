from django.conf.urls import patterns, url

from beverages import views

urlpatterns = patterns('',
    url(r'^$', views.hello, name='hello'),
)
