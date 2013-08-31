from django.conf.urls import patterns, include, url

from .views.Rushie import RushieCreateView, RushieListView

urlpatterns = patterns('',

    url(r'^rushie/list/$', RushieListView.as_view(), name="rushie_list"),
    url(r'^rushie/create/$', RushieCreateView.as_view(), name="create_rushie"),

)

