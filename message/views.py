from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from message.forms import CreateMessageForm
from message.models import Message


# Create your views here.
class MessageListView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    model = Message
    template_name = 'pages/messages_list.html'
    context_object_name = 'messages'


class CreateMessageView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/add_message.html'
    success_url = reverse_lazy('message:list')


class ReadMessageView(LoginRequiredMixin, DetailView, PermissionRequiredMixin):
    model = Message
    template_name ='pages/detail_message.html'
    context_object_name ='message'


class UpdateMessageView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/update_message.html'
    success_url = reverse_lazy('messages:list')


class DeleteMessageView(LoginRequiredMixin, DetailView, PermissionRequiredMixin):
    model = Message
    template_name ='forms/delete_message.html'



