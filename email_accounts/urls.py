from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import RegisterView
from .utils import anonymous_required

urlpatterns = [
    path('register/',
         anonymous_required(RegisterView.as_view(template_name='email_accounts/register.html')),
         name='register'),
    path('login/',
         anonymous_required(LoginView.as_view(template_name='email_accounts/login.html')),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
    path('password_change/',
         PasswordChangeView.as_view(template_name='email_accounts/password/change/1.html'),
         name='password_change'),
    path('password_change/done',
         PasswordChangeDoneView.as_view(template_name='email_accounts/password/change/2.html'),
         name='password_change_done'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='email_accounts/password/reset/1.html'),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='email_accounts/password/reset/2.html'),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='email_accounts/password/reset/3.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(template_name='email_accounts/password/reset/4.html'),
         name='password_reset_complete'),
]
