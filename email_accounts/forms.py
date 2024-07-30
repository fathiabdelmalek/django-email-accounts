from django.forms import EmailField, CharField, EmailInput, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(BaseUserCreationForm):
    email = EmailField(
        label=_("Email Address"),
        widget=EmailInput(attrs={'class': 'input-field', 'placeholder': _('Enter your email'), 'required': True}),
    )
    username = CharField(
        label=_("Username"),
        widget=TextInput(attrs={'class': 'input-field', 'placeholder': _('Choose a username'), 'required': True}),
    )
    password = CharField(
        label=_("Password"),
        widget=PasswordInput(attrs={'class': 'input-field', 'placeholder': _('Enter your password'), 'required': True}),
    )
    re_password = CharField(
        label=_("Confirm Password"),
        widget=PasswordInput(attrs={'class': 'input-field', 'placeholder': _('Confirm your password'), 'required': True}),
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 're_password']
