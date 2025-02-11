import secrets

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView
from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm, UserLoginForm, UserEditForm
from users.management.commands.add_user_to_group import UserService
from users.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    '''Класс для регистрации нового юзера'''
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


    def form_valid(self, form):
        '''Метод для валидации формы и отправки эл.почты с токеном для подтвердения аккаунта'''
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-verification/{token}/"
        send_mail(
            subject="Confirmation for registration",
            message=f"Go through the link to confirm your registration {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    '''Подтверждение аккаута и сохранение в БД'''
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    UserService.assign_service_user(user)
    user.save()
    return redirect(reverse_lazy("users:login"))


class UserLoginView(LoginView):
    '''Класс для входа в веб приложение'''
    form_class = UserLoginForm
    template_name = "users/login.html"


class UpdateCustomUser(LoginRequiredMixin, UpdateView):
    '''Класс для редактирования профиля пользователя'''
    model = CustomUser
    form_class = UserEditForm
    template_name = "users/update_user_form.html"
    success_url = reverse_lazy("clients:home")


class AllCustomUserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/all_customuser.html'
    context_object_name = 'customusers'
    permission_required = ('customuser.view_customuser')


    def get_queryset(self):
        if self.request.user.has_perm('customuser.view_customuser') and self.request.user.groups.filter(name="Managers"):
            queryset = super().get_queryset()
            return queryset
        else:
            raise PermissionDenied()


@login_required
@permission_required('customuser.change_customuser', raise_exception=True )
def block_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if user.is_active == True:
        user.is_active = False
        user.save()
    return redirect('users:all-customusers')