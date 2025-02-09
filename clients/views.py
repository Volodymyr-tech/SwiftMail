from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from clients.forms import ClientForm
from clients.models import Client
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from mailing.models import Mail
from message.models import Message


# Create your views here.
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'pages/client_list.html'
    context_object_name = 'clients'


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

class AddClientView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/add_client.html'
    success_url = reverse_lazy('clients:list')

class UpdateClientView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/edit_client.html'
    success_url = reverse_lazy('clients:list')

class DeleteClientView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'forms/delete_client.html'
    success_url = reverse_lazy('clients:list')


class DetailClientView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'pages/client_detail.html'
    context_object_name = 'client'