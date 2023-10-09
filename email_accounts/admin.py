from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_admin', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
    )


admin.site.register(models.User, UserAdmin)
