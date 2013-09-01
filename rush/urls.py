from django.conf.urls import patterns, include, url

from .views.Rushie import RushieCreateView, RushieListView, RushieDetailView

urlpatterns = patterns('',

    url(r'^rushie/list/$', RushieListView.as_view(), name="list_rushies"),
    url(r'^rushie/create/$', RushieCreateView.as_view(), name="create_rushie"),
    url(r'^rushie/(?P<username>[-\w]+)/$', RushieDetailView.as_view(), name='rushie_detail'),

)

