from django.conf.urls import patterns, include, url

from .views.Rushie import RushieCreateView

urlpatterns = patterns('',

    url(r'^rushie/create/$', RushieCreateView.as_view(), name="create_rushie"),

)
