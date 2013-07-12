from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from main.forms import LoginForm

from main.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fraternet.views.home', name='home'),
    # url(r'^fraternet/', include('fraternet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',{'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} , name='logout'),

    #Homepage/Landing Page. Will probably be dynamic later
    url(r'^$', dashboard_view, name='dashboard'),
)
