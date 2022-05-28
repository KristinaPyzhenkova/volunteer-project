from django.forms import ModelForm, DateField

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


class EventFormCreate(ModelForm):
    date_start = DateField()
    date_end = DateField()

    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'name': 'Наименование',
            'status': 'Местоположение',
            'project': 'Проект'
        }
