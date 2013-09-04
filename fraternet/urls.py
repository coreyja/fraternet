from django.conf.urls import patterns, include, url
from django.contrib import admin as django_admin
from django.contrib.auth.decorators import login_required

from main.forms import LoginForm
from main.views.common import dashboard_view, ProfileView, ProfileEditView, GeneralInfoView, ContactUsView
from main.views.admin import admin_view
from main.views.Brother import BrotherCreateView, BrotherListView, BrotherDetailView, BrotherEditView

from rush import urls as rush_urls
from events import urls as event_urls

import settings

django_admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fraternet.views.home', name='home'),
    # url(r'^fraternet/', include('fraternet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^django_admin/', include(django_admin.site.urls)),

    #Rush Urls
    url(r'^rush/', include(rush_urls)),
    url(r'^events/', include(event_urls)),


    url(r'^login/$', 'django.contrib.auth.views.login',{'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} , name='logout'),

    url(r'^admin/$', admin_view, name='admin'),


    url(r'^brother/create/$', BrotherCreateView.as_view(), name='add_brother'),
    url(r'^brother/list/$', BrotherListView.as_view(), name='list_brothers'),
    url(r'^brother/(?P<username>[-\w]+)/$', BrotherDetailView.as_view(), name='brother_detail'),
    url(r'^brother/(?P<username>[-\w]+)/edit/$', BrotherEditView.as_view(), name='edit_brother'),

    url(r'^profile/$', ProfileView.as_view(), name="profile"),
    url(r'^profile/edit/$', ProfileEditView.as_view(), name="edit_profile"),

    url(r'^general-info/$', GeneralInfoView.as_view(), name="general-info"),
    url(r'^contact/$', ContactUsView.as_view(), name="contact"),

    #Homepage/Landing Page. Will probably be dynamic later
    url(r'^$', dashboard_view, name='dashboard'),

    url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
)
