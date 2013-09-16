from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView, View, TemplateView
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from datetime import datetime
import json

from rush.models import ClosedRush, RushEvent
from events.views import EventsView


class ClosedRushEventsView(EventsView):
    model = ClosedRush


class RushEventsView(EventsView):
    model = RushEvent