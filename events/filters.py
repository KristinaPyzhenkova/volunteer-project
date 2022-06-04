import django_filters
from django_filters import CharFilter, DateFilter
from django import forms

from .models import *


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
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Проект')
    date_start = DateFilter(field_name='date_start', lookup_expr='gte', widget=forms.SelectDateWidget(
        empty_label=("Выбери год", "Выбери месяц", "Выбери число"),), label='Дата начала'
    )
    date_end = DateFilter(field_name='date_end', lookup_expr='lte', widget=forms.SelectDateWidget(
        empty_label=("Выбери год", "Выбери месяц", "Выбери число"),), label='Дата окончания'
    )
    project__name = django_filters.ChoiceFilter(choices=PROJECT, label='Направление проекта')

    class Meta:
        model = Event
        fields = ['name', 'date_start', 'date_end', 'project__name']
