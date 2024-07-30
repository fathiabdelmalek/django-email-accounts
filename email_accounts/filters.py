import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['iexact', 'icontains'],
            'email': ['iexact', 'icontains'],
            'is_staff': ['exact'],
            'is_superuser': ['exact'],
        }
