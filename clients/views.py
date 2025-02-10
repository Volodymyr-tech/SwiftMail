from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from clients.forms import ClientForm
from clients.models import Client
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from mailing.models import Mail
from message.models import Message


# Create your views here.
class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    template_name = 'pages/client_list.html'
    context_object_name = 'clients'


    def get_queryset(self):
        if self.request.user.has_perm('clients.view_client'):
            queryset = super().get_queryset()
            return queryset.filter(owner=self.request.user)
        else:
            raise PermissionDenied()


class HomeView(ListView):
    model = Client
    template_name = 'pages/main_page.html'

    def get_context_data(self, **kwargs):
        # Получаем базовый контекст
        context = super().get_context_data(**kwargs)

        # Добавляем дополнительные данные в контекст
        context["message_count"] = Message.objects.count()
        context["client_count"] = Client.objects.count()
        context["mailing_count"] = Mail.objects.count()

        return context

class AddClientView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/add_client.html'
    success_url = reverse_lazy('clients:list')
    permission_required = ('clients.add_client',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        print(f"Назначенный владелец: {self.object.owner}")  # Проверяем, что `owner` не пустой
        self.object.save()
        return super().form_valid(form)

class UpdateClientView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/edit_client.html'
    success_url = reverse_lazy('clients:list')
    permission_required = ('clients.change_client',)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner == self.request.user and self.request.user.has_perm('clients.change_client'):
            return object
        else:
            raise PermissionDenied()


class DeleteClientView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'forms/delete_client.html'
    success_url = reverse_lazy('clients:list')
    permission_required = ('clients.delete_client',)


    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if not self.request.user.has_perm('clients.delete_client') and object.owner != self.request.user:
                raise PermissionDenied()
        return object


class DetailClientView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'pages/client_detail.html'
    context_object_name = 'client'