from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path

from . import views

app_name = 'auth_users'

urlpatterns = [
    path('login/', views.AuthView.as_view(template_name='auth_users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(template_name='auth_users/registration.html'), name='registration'),
    path('password_reset/', views.PassResetView.as_view(template_name='auth_users/password_reset.html'), name='password_reset'),
]
