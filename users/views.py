import logging

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView

from blog.apps import BlogConfig

from .models import BaseUser
from .forms import UserCreateForm, CustomAuthenticationForm

logger_views_users = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views_users.addHandler(file_handler)
logger_views_users.setLevel(logging.INFO)


class UsersCreate(CreateView):
    model = BaseUser
    form_class = UserCreateForm
    template_name = "users/create.html"
    context_object_name = "user"


class Login(LoginView):
    model = BaseUser
    form_class = CustomAuthenticationForm
    template_name = "users/log_in.html"



class Logout(LogoutView):
    model = BaseUser
    template_name = "users/log_out.html"
    success_url = reverse_lazy('users:logout')
