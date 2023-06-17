from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
