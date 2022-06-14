import re

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

    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]

    gender = forms.ChoiceField(label='Пол', choices=GENDER_CHOICES)

    error_messages = {
        'invalid first_letters': "Первая буква должна быть заглавной.",
        'invalid_alphabet': "Поле должно содержать только кириллицу.",
        'invalid phone': 'Формат номера 89991112233'
    }

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'date_birthday', 'info', 'direction', 'phone', 'telegram_url', 'vk_url')
        widgets = {
            'date_birthday': DateInputWidget(attrs={'type': 'date'}),
            'direction': CheckboxSelectMultiple(attrs={}),
            'avatar': AvatarInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name[0].islower():
            raise forms.ValidationError(
                self.error_messages['invalid first_letters'],
                code='invalid first_letters',
            )
        elif not re.fullmatch(r'[а-яА-ЯёЁ]+', first_name):
            raise forms.ValidationError(
                self.error_messages['invalid_alphabet'],
                code='invalid_alphabet',
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name[0].islower():
            raise forms.ValidationError(
                self.error_messages['invalid first_letters'],
                code='invalid first_letters',
            )
        elif not re.fullmatch(r'[а-яА-ЯёЁ]+', last_name):
            raise forms.ValidationError(
                self.error_messages['invalid_alphabet'],
                code='invalid_alphabet',
            )
        return last_name
