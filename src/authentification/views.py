from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from authentification.forms import SignUpForm


class Login(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("tasks:list")


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("index")


def logout_view(request):
    logout(request)
    return redirect("index")

