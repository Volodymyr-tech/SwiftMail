from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, redirect

from mailing.forms import MailForm
from mailing.models import Mail
from utils.email_service import EmailSender


# Create your views here.

class MailListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mail
    template_name = 'pages/mails_list.html'
    context_object_name = 'mails'
    permission_required = ('mailing.view_mail')


    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.request.GET.get("filter")  # Получаем параметр `filter`

        print("GET parameters:", self.request.GET)  # Логируем параметры

        if filter_param == "Sent":
            return queryset.filter(status="Sent")  # Фильтр по статусу
        elif filter_param == "Sending":
            return queryset.filter(status="Sending")
        elif filter_param == "Created":
            return queryset.filter(status="Created")
        else:
            return queryset.order_by("-first_sending")

        return queryset  # Без фильтрации

class AllMailListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mail
    template_name = 'pages/all_mail.html'
    context_object_name = 'mails'
    permission_required = ('mail.view_mail')


    def get_queryset(self):
        if self.request.user.has_perm('mail.view_mail') and self.request.user.groups.filter(name="Managers"):
            queryset = super().get_queryset()
            return queryset
        else:
            raise PermissionDenied()

class AddMailView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/add_mail.html'
    success_url = reverse_lazy('mailing:list')
    permission_required = ('mailing.add_mail')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        print(f"Назначенный владелец: {self.object.owner}")  # Проверяем, что `owner` не пустой
        self.object.save()
        self.object.client.set(form.cleaned_data['client'])
        return super().form_valid(form)


class UpdateMailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/update_mail.html'
    success_url = reverse_lazy('mailing:list')
    permission_required = ('mailing.change_mail')


    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner == self.request.user and self.request.user.has_perm('mailing.change_mail'):
            return object
        else:
            raise PermissionDenied()

class DeleteMailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mail
    template_name = 'forms/delete_mail.html'
    success_url = reverse_lazy('message:list')
    permission_required = ('mailing.delete_mail')


    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if not self.request.user.has_perm('mailing.delete_mail') and object.owner != self.request.user:
                raise PermissionDenied()
        return object


class DetailMailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mail
    template_name = 'pages/detail_mail.html'
    context_object_name = 'mail'
    permission_required = ('mailing.view_mail')

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner == self.request.user and self.request.user.has_perm('mailing.view_mail'):
            return object
        else:
            raise PermissionDenied()

@login_required
@permission_required('mailing.change_mail',raise_exception=True )
def start_mailing(request, pk):
    mailing = get_object_or_404(Mail, pk=pk)
    if mailing.status != "Sending":
        EmailSender.send_mailing(mailing)
        mailing.first_sending = timezone.now()
        mailing.save()
    return redirect('mailing:list')