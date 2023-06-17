from django.shortcuts import redirect
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreationForm


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('home'))
