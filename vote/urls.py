from django.conf.urls import patterns, include, url

from .views.VotingStatusView import VotingStatusView


urlpatterns = patterns('',

    url(r'^status/$', VotingStatusView.as_view(), name="vote_status"),


)

