from django.forms import ModelForm, CheckboxSelectMultiple, CheckboxInput
from django.forms.widgets import ClearableFileInput
from django import forms

from users.models import User


class AvatarInput(ClearableFileInput):
    template_name = "includes/avatar_input.html"


class DateInputWidget(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'date_birthday', 'info', 'direction', 'phone', 'telegram_url', 'vk_url')
        widgets = {
            'date_birthday': DateInputWidget(attrs={'type': 'date'}),
            'direction': CheckboxSelectMultiple(attrs={}),
            'avatar': AvatarInput
        }
