import django_filters
from django import forms
from datetime import datetime

from .models import *
from projects.models import Project


class Event_Filter(django_filters.FilterSet):
    PROJECT = (
        ('Животные', 'Животные'),
        ('Культура и искусство', 'Культура и искусство'),
        ('Здравоохранение', 'Здравоохранение'),
        ('Образование', 'Образование'),
        ('Другое', 'Другое'),
        ('Природа', 'Природа'),
        ('Поиск пропавших', 'Поиск пропавших'),
        ('Дети и молодежь', 'Дети и молодежь'),
        ('Спорт и здоровье', 'Спорт и здоровье'),
    )
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains',
                                     widget=forms.TextInput(attrs={"class": "form-edit-user",
                                                                   'placeholder': 'Поиск'}))
    date_start = django_filters.DateFilter(field_name='date_start', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date',"class": "form-edit-user"}),
                                     initial=datetime.today(), label='Дата начала не раньше чем:'
    )
    date_end = django_filters.DateFilter(field_name='date_end', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date',"class": "form-edit-user"}),
                                     initial=datetime.today(), label='Дата окончания не позднее чем:'
    )
    project__name = django_filters.MultipleChoiceFilter(choices=PROJECT, label='Направление проекта',
                                                widget=forms.CheckboxSelectMultiple(attrs={"class": "form-edit-user"}))

    class Meta:
        model = Event
        fields = ['name', 'date_start', 'date_end', 'project__name']
