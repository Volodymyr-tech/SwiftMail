from msilib.schema import ListView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from message.forms import CreateMessageForm
from message.models import Message


# Create your views here.
class MessageListView(ListView):
    model = Message
    template_name = 'pages/list.html'
    context_object_name = 'messages'


class CreateMessageView(CreateView):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/add_message.html'
    success_url = reverse_lazy('message:list')


class ReadMessageView(DetailView):
    model = Message
    template_name ='pages/detail_message.html'
    context_object_name ='message'


class UpdateMessageView(UpdateView):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/update_message.html'
    success_url = reverse_lazy('messages:list')


class DeleteMessageView(DetailView):
    model = Message
    template_name ='forms/delete_message.html'



