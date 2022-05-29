from django.views.generic import ListView
from django.core import serializers
from django.http import HttpResponse

from events.models import Event


class HomeView(ListView):
    model = Event
    template_name = 'index.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['events_json'] = serializers.serialize('json', context['events'])

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_queryset = queryset.order_by('date_start')[:6]
        return filter_queryset
