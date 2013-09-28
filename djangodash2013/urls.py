from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^mocks/', include('mocks.urls')),
                       url(r'^admin/', include(admin.site.urls))
)
