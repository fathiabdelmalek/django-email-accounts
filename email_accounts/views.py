from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from .models import User
from .forms import UserCreationForm
from .serializers import UserSerializer


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        login(self.request, form.save())
        return redirect(self.request.GET.get('next', reverse(self.request.META.get('HTTP_REFERER') if self.request.META.get('HTTP_REFERER') else 'home')))


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF Token cookie set'}, status=HTTP_200_OK)


class IsAuthenticated(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        user = request.user
        if user.is_authenticated:
            return Response({'isAuthenticated': 'Yes'}, status=HTTP_200_OK)
        return Response({'isAuthenticated': 'No'}, status=HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            if not email:
                return Response({'email_error': 'you must enter the email'}, status=HTTP_401_UNAUTHORIZED)
            if not password:
                return Response({'password_error': 'you must enter the password'}, status=HTTP_401_UNAUTHORIZED)
            user = User.objects.filter(email=email)
            if user.exists():
                user = user[0]
                if user.check_password(password):
                    login(request, user)
                    return Response({'success': 'login successfully'}, status=HTTP_201_CREATED)
                return Response({'password_error': "password isn't correct"}, status=HTTP_401_UNAUTHORIZED)
            return Response({'email_error': "email doesn't exist"}, status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutView(APIView):

    def post(self, request, format=None):
        try:
            logout(request)
            return Response({'success', 'logout successfully'}, status=HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'something went wrong when loging out'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            username = request.data.get('username')
            password = request.data.get('password')
            re_password = request.data.get('re_password')
            if not email:
                return Response({'email_error': 'you must enter the email'}, status=HTTP_400_BAD_REQUEST)
            if not username:
                return Response({'username_error': 'you must enter the username'}, status=HTTP_400_BAD_REQUEST)
            if not password:
                return Response({'password_error': 'you must enter the password'}, status=HTTP_400_BAD_REQUEST)
            if not re_password:
                return Response({'password_error': 'you must enter the password confirmation'}, status=HTTP_400_BAD_REQUEST)
            if password != re_password:
                return Response({'password_error': 'Passwords do not match'}, status=HTTP_409_CONFLICT)
            if User.objects.filter(email=email).exists():
                return Response({'email_error': 'Email already exists'}, status=HTTP_409_CONFLICT)
            if User.objects.filter(username=username).exists():
                return Response({'username_error': 'Username already exists'}, status=HTTP_409_CONFLICT)
            if len(password) < 8:
                return Response({'password_error': 'Password must be more than 8 characters'}, status=HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=self.request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({'success': 'User created successfully'}, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        serializer.save()
