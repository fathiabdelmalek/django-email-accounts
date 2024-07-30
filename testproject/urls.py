from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from email_accounts.views import UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('email_accounts.urls')),
    path('api/', include(router.urls)),
    path('api/accounts/', include('email_accounts.api_urls')),
    path('', include('testapp.urls')),
]
