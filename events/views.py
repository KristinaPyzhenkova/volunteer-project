from django.views.generic import DetailView, ListView

from .models import Event


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class EventsList(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'