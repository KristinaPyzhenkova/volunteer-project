from django.forms import ModelForm, DateField, modelformset_factory
from django import forms
from .models import Follow, Function, Event



class EventForm(ModelForm):
    class Meta:
        model = Follow
        fields = ('function',)

    def __init__(self, *args, **kwargs):
        if 'event' in kwargs and kwargs['event'] is not None:
            event = kwargs.pop('event')
            qs = Function.objects.filter(event_id=event.pk)
            total_pk=[]
            for qs_one in qs:
                if qs_one.count>qs_one.following.count():
                    total_pk.append(qs_one.pk)
            qs=qs.filter(pk__in=total_pk)
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['function'].queryset = qs


class DateTimeInputWidget(forms.DateTimeInput):
    input_type = 'datetime'

    def format_value(self, value):
        return value

class EventFormCreate(ModelForm):
    class Meta:
        model = Event
        fields = ('name','status','avatar_url','description','date_start','date_end','project')
        widgets = {
            'date_start': DateTimeInputWidget(attrs={'type': 'datetime'}),
            'date_end': DateTimeInputWidget(attrs={'type': 'datetime'})
        }


class FunctionFormCreate(ModelForm):
    class Meta:
        model = Function
        fields = ('name','description','task','condition','count')

