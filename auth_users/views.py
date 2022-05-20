from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from auth_users.forms import AuthUserForm, RegistrationUserForm, PassResetForm
from users.models import User


class AuthView(LoginView):
    form_class = AuthUserForm


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    success_url = reverse_lazy('index')


class PassResetView(PasswordResetView):
    form_class = PassResetForm
    is_success = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'is_success': self.is_success,
            **(self.extra_context or {})
        })
        return context

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        self.is_success = True
        form.save(**opts)
        return render(request=self.request, template_name=self.template_name, context=self.get_context_data())


class UserDetailView(DetailView):
    model = User
