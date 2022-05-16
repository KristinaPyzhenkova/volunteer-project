import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.template.defaultfilters import capfirst

from users.models import User


class AuthUserForm(forms.Form):

    email = forms.EmailField(label="email", max_length=256, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    error_messages = {
        'invalid_login': "Неправильный Email и/или пароль.",
        'inactive': "Аккаунт неактивен.",
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': self.email_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthUserForm, self).__init__(*args, **kwargs)

        UserModel = User
        self.email_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegistrationUserForm(UserCreationForm):

    email = forms.EmailField(label="email", max_length=256, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label="first_name", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(label="last_name", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label="confirm_password", widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))

    error_messages = {
        'password_mismatch': "Введеные пароли не совпадают.",
        'invalid first_letters': "Первая буква должна быть заглавной.",
        'invalid_alphabet': "Поле должно содержать только кириллицу.",
        'invalid_email': "Данные email уже используется."
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['invalid_email'],
                code='invalid_email',
            )
        return email


class PassResetForm(PasswordResetForm):
    email = forms.EmailField(label="email", max_length=256, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    error_messages = {
        'invalid_email': "Email не существует."
    }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['invalid_email'],
                code='invalid_email',
            )
        return email
