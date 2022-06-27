from django.forms import ModelForm, DateField, modelformset_factory
from django import forms
from .models import Follow, Function, Event
from datetime import datetime
from django.forms.widgets import ClearableFileInput, DateTimeInput


class EventForm(ModelForm):
    class Meta:
        model = Follow
        fields = ('function',)

    def __init__(self, *args, **kwargs):
        if 'event' in kwargs and kwargs['event'] is not None:
            event = kwargs.pop('event')
            qs = Function.objects.filter(event_id=event.pk)
            total_pk = []
            for qs_one in qs:
                if qs_one.count > qs_one.following.count():
                    total_pk.append(qs_one.pk)
            qs = qs.filter(pk__in=total_pk)
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['function'].queryset = qs


class EventInput(ClearableFileInput):
    template_name = "includes/event_input.html"


class EventFormCreate(ModelForm):
    date_start = forms.DateTimeField(
        label='Дата начала')

    date_end = forms.DateTimeField(
        label='Дата окончания')

    class Meta:
        model = Event
        fields = ('coordinates_latitude', 'coordinates_longitude', 'address', 'avatar_url', 'name', 'status', 'description', 'date_start', 'date_end', 'project')
        widgets = {
            'avatar_url': EventInput
        }


class FunctionFormCreate(ModelForm):
    class Meta:
        model = Function
        fields = ('name', 'description', 'task', 'condition', 'count')
