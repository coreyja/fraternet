from django.conf.urls import patterns, include, url
from django.contrib import admin as django_admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from main.forms import LoginForm, ChangePasswordForm
from main.views.common import HomepageView, ProfileView, ProfileEditView, GeneralInfoView, ContactUsView
from main.views.admin import admin_view
from main.views.Brother import BrotherCreateView, BrotherListView, BrotherDetailView, BrotherEditView

from rush import urls as rush_urls
from events import urls as event_urls
from vote import urls as vote_urls

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

    #Voting Urls import
    url(r'^vote/', include(vote_urls)),


    url(r'^login/$', 'django.contrib.auth.views.login',{'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} , name='logout'),

    url(r'^admin/$', admin_view, name='admin'),


    url(r'^brother/create/$', BrotherCreateView.as_view(), name='add_brother'),
    url(r'^brother/list/$', BrotherListView.as_view(), name='list_brothers'),
    url(r'^brother/(?P<username>[-\w]+)/$', BrotherDetailView.as_view(), name='brother_detail'),
    url(r'^brother/(?P<username>[-\w]+)/edit/$', BrotherEditView.as_view(), name='edit_brother'),

    url(r'^profile/$', ProfileView.as_view(), name="profile"),
    url(r'^profile/edit/$', ProfileEditView.as_view(), name="edit_profile"),
    # url(r'^profile/change-password/$', ChangePasswordView.as_view(), name="change_password"),
    url(r'^profile/change-password/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'profile/change_password.html', 'post_change_redirect': reverse_lazy('profile'), 'password_change_form': ChangePasswordForm},
        name="change_password"),


    url(r'^general-info/$', GeneralInfoView.as_view(), name="general-info"),
    url(r'^contact/$', ContactUsView.as_view(), name="contact"),

    #Homepage/Landing Page. Will probably be dynamic later
    url(r'^$', HomepageView.as_view(), name='dashboard'),

    url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
)
