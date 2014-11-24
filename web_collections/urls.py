from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_collections.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^beverages/', include('beverages.urls', 'beverages')),
    url(r'^accounts/', include('users.urls', 'accounts')),
    url(r'^admin/', include(admin.site.urls)),
)
