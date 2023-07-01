from django.urls import path
from .views import GetCSRFToken, IsAuthenticated, LoginView, LogoutView, UserViewSet

urlpatterns = [
    path('csrf-cookie/', GetCSRFToken.as_view()),
    path('is-authenticated/', IsAuthenticated.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
