import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import CustomUserCreationForm, UserLoginForm, UserEditForm
from users.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    '''Класс для регистрации нового юзера'''
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserLoginView(LoginView):
    '''Класс для входа в веб приложение'''
    form_class = UserLoginForm
    template_name = "users/login.html"


class UpdateCustomUser(LoginRequiredMixin, UpdateView):
    '''Класс для редактирования профиля пользователя'''
    model = CustomUser
    form_class = UserEditForm
    template_name = "users/update_user_form.html"
    success_url = reverse_lazy("catalog:home")