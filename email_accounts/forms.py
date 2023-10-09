from django.forms import EmailField, CharField, EmailInput, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreationForm(UserCreationForm):
    email = EmailField(
        label="Email Address",
        widget=EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email', 'required': True}),
    )
    username = CharField(
        label="Username",
        widget=TextInput(attrs={'class': 'input-field', 'placeholder': 'Choose a username', 'required': True}),
    )
    password1 = CharField(
        label="Password",
        widget=PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter your password', 'required': True}),
    )
    password2 = CharField(
        label="Confirm Password",
        widget=PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm your password', 'required': True}),
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
