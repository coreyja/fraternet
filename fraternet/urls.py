from django.conf.urls import patterns, include, url
from django.contrib import admin as django_admin

from main.forms import LoginForm
from main.views.common import dashboard_view
from main.views.admin import admin_view
from main.views.Brother import BrotherCreateView

django_admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fraternet.views.home', name='home'),
    # url(r'^fraternet/', include('fraternet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^django_admin/', include(django_admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',{'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} , name='logout'),

    url(r'^admin/$', admin_view, name='admin'),
    url(r'^admin/brother/create/$', BrotherCreateView.as_view(), name='add_brother'),

    #Homepage/Landing Page. Will probably be dynamic later
    url(r'^$', dashboard_view, name='dashboard'),
)
