from django.forms import ModelForm

from .models import Organization


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('full_name', 'name', 'description','email','address','phone','avatar_url','website', 'legal_form')
        labels = {
            'full_name': 'Полное наименование',
            'name': 'Наименование',
            'description': 'Описание'
        }