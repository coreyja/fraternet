from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView, View, TemplateView
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from datetime import datetime
import json

from .models import Event
from .forms import EventForm


class CalendarView(TemplateView):
    template_name = 'events/calendar.html'


class EventsView(View):

    def get(self, request, *args, **kwargs):
        start = int(request.GET['start'])
        end = int(request.GET['end'])

        start = datetime.fromtimestamp(start)
        end = datetime.fromtimestamp(end)

        events = Event.objects.filter(start_datetime__gte=start, end_datetime__lte=end)

        events_json = []

        for event in events:
            events_json.append({
                'title': event.name,
                'start': str(event.start_datetime),
                'end': str(event.end_datetime),
                'url': reverse('single_event', kwargs={'pk':event.id}),
            })

        return HttpResponse(json.dumps(events_json), mimetype='application/json')


class SingleEventView(DetailView):
    model = Event
    template_name = 'events/single.html'


class EditEventView(UpdateView):
    model = Event
    template_name = 'events/edit.html'
    form_class = EventForm

    def get_success_url(self):
        return reverse('single_event', kwargs={'pk': self.object.id})

    @method_decorator(permission_required('events.can_edit'))
    def dispatch(self, *args, **kwargs):
        return super(EditEventView, self).dispatch(*args, **kwargs)

class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm

    def get_success_url(self):
        return reverse('single_event', kwargs={'pk': self.object.id})

    @method_decorator(permission_required('events.add_event'))
    def dispatch(self, *args, **kwargs):
        return super(CreateEventView, self).dispatch(*args, **kwargs)

