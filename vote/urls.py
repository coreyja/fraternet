from django.conf.urls import patterns, include, url

from .views.VotingStatusView import VotingStatusView
from .views.VotingView import VotingView


urlpatterns = patterns('',

    url(r'^status/$', VotingStatusView.as_view(), name="vote_status"),
    url(r'^$', VotingView.as_view(), name='voting'),


)

