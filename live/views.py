import json

from django.views.generic import ListView
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from events.models import Event
from users.models import User
from projects.models import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'avatar', 'first_name', 'last_name')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('pk', 'name')


class EventSerializer(serializers.ModelSerializer):
    contact_user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('pk', 'name', 'date_end', 'date_start', 'coordinates_latitude', 'coordinates_longitude', 'address', 'project', 'contact_user')


class HomeView(ListView):
    model = Event
    template_name = 'index.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        serializer = EventSerializer(context['events'], many=True)
        context['events_json'] = json.loads(JSONRenderer().render(serializer.data))

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_queryset = queryset.order_by('date_start')[:6]
        return filter_queryset
