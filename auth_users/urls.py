from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.urls import path

from auth_users.views import AuthView, RegistrationView, PassResetView

app_name = 'auth_users'

urlpatterns = [
    path('login/', AuthView.as_view(template_name='auth_users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(template_name='auth_users/registration.html'), name='registration'),
    path('password/reset/', PassResetView.as_view(template_name='auth_users/password_reset.html'), name='password_reset'),
]
