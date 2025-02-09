from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailing.forms import MailForm
from mailing.models import Mail


# Create your views here.

class MailListView(ListView):
    model = Mail
    template_name = 'pages/mails_list.html'
    context_object_name = 'mails'

    def get_queryset(self):
        queryset = Mail.objects.select_related('message')
        print(queryset.query)  # Выведет SQL-запрос в консоль для проверки
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context:", context)  # Выведет в консоль данные, передаваемые в шаблон
        return context


class AddMailView(CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/add_mail.html'
    success_url = reverse_lazy('message:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Cleaned data:", form.cleaned_data)
        self.object.client.set(form.cleaned_data['client'])
        print("Assigned clients:", self.object.client.all())  # Проверь, добавляются ли клиенты
        return response


class UpdateMailView(UpdateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/update_mail.html'
    success_url = reverse_lazy('message:list')

class DeleteMailView(DeleteView):
    model = Mail
    template_name = 'forms/delete_mail.html'
    success_url = reverse_lazy('message:list')


class DetailMailView(DetailView):
    model = Mail
    template_name = 'pages/detail_mail.html'
    context_object_name = 'mail'