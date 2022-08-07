from django.shortcuts import render,reverse
from django.contrib.auth.views import LoginView
from .forms import CreateUserForm
from django.views.generic import CreateView
# Create your views here.
class UserSignupView(CreateView):
    template_name = "user/signup.html"
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('')


class LoginView(LoginView):
    template_name = "user/login.html"
            