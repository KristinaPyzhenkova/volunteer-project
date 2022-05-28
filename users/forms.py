from django.forms import ModelForm, CheckboxSelectMultiple

from django import forms
from users.models import User


class DateInputWidget(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'date_birthday', 'info', 'direction', 'phone', 'telegram_url', 'vk_url')
        widgets = {
            'date_birthday': DateInputWidget(attrs={'type': 'date'}),
            'direction': CheckboxSelectMultiple(attrs={})
        }
