from django.urls import reverse_lazy

from clients.forms import ClientForm
from clients.models import Client
from django.views.generic import ListView, UpdateView, CreateView, DeleteView


# Create your views here.

class HomeView(ListView):
    model = Client
    template_name = 'pages/main_page.html'
    context_object_name = 'clients'


class AddClientView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/add_client.html'
    success_url = reverse_lazy('clients:home')

class UpdateClientView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'forms/edit_client.html'
    success_url = reverse_lazy('clients:home')

class DeleteClientView(DeleteView):
    model = Client
    template_name = 'forms/delete_client.html'
    success_url = reverse_lazy('clients:home')


class DetailClientView(DeleteView):
    model = Client
    template_name = 'pages/client_detail.html'
    context_object_name = 'client'