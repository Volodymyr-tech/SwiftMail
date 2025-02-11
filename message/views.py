from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from message.forms import CreateMessageForm
from message.models import Message


# Create your views here.
class MessageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Message
    template_name = 'pages/messages_list.html'
    context_object_name = 'messages'
    permission_required = ('message.view_message',)

    def get_queryset(self):
        if self.request.user.has_perm('message.view_message'):
            queryset = super().get_queryset()
            return queryset.filter(owner=self.request.user)


class CreateMessageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/add_message.html'
    success_url = reverse_lazy('message:list')
    permission_required = ('message.add_message',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        print(f"Назначенный владелец: {self.object.owner}")  # Проверяем, что `owner` не пустой
        self.object.save()
        return super().form_valid(form)


class ReadMessageView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Message
    template_name ='pages/detail_message.html'
    context_object_name ='message'
    permission_required = ('message.view_message',)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner == self.request.user and self.request.user.has_perm('message.view_message'):
            return object
        else:
            raise PermissionDenied()


class UpdateMessageView(LoginRequiredMixin , PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = CreateMessageForm
    template_name ='forms/update_message.html'
    success_url = reverse_lazy('messages:list')
    permission_required = ('message.change_message',)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner == self.request.user and self.request.user.has_perm('message.change_message'):
            return object
        else:
            raise PermissionDenied()

class AllCMessageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Message
    template_name = 'pages/all_message.html'
    context_object_name = 'messages'
    permission_required = ('message.view_message')


    def get_queryset(self):
        if self.request.user.has_perm('message.view_message') and self.request.user.groups.filter(name="Managers"):
            queryset = super().get_queryset()
            return queryset
        else:
            raise PermissionDenied()

class DeleteMessageView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Message
    template_name ='forms/delete_message.html'
    permission_required = ('message.delete_message',)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if not self.request.user.has_perm('message.delete_message') and object.owner != self.request.user:
                raise PermissionDenied()
        return object



