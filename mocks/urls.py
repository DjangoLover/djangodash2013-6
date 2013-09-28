from django.conf.urls import patterns, url

from views import services

urlpatterns = patterns('',
                       url('', services)
)
