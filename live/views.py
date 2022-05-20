from django.views.generic import ListView

from events.models import Event


class HomeView(ListView):
    model = Event
    template_name = 'index.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_queryset = queryset.order_by('date_start')[:6]
        return filter_queryset
