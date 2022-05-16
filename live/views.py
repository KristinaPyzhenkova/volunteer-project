from django.views.generic import ListView

from events.models import Event


class HomeView(ListView):
    model = Event
