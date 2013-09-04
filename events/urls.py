from django.conf.urls import patterns, include, url

from .views import CalendarView, EventsView, SingleEventView

urlpatterns = patterns('',
    url(r'^$', CalendarView.as_view(), name='calendar_view'),
    url(r'^events/$', EventsView.as_view(), name='event_json_view'),
    url(r'^event/(?P<pk>[0-9]+)', SingleEventView.as_view(), name="single_event"),
)

