from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, redirect

from mailing.forms import MailForm
from mailing.models import Mail
from utils.email_service import EmailSender


# Create your views here.

class MailListView(ListView):
    model = Mail
    template_name = 'pages/mails_list.html'
    context_object_name = 'mails'


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


class AddMailView(CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/add_mail.html'
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        print(f"Назначенный владелец: {self.object.owner}")  # ✅ Проверяем, что `owner` не пустой
        self.object.save()
        self.object.client.set(form.cleaned_data['client'])
        return super().form_valid(form)


class UpdateMailView(UpdateView):
    model = Mail
    form_class = MailForm
    template_name = 'forms/update_mail.html'
    success_url = reverse_lazy('mailing:list')

class DeleteMailView(DeleteView):
    model = Mail
    template_name = 'forms/delete_mail.html'
    success_url = reverse_lazy('message:list')


class DetailMailView(DetailView):
    model = Mail
    template_name = 'pages/detail_mail.html'
    context_object_name = 'mail'



def start_mailing(request, pk):
    mailing = get_object_or_404(Mail, pk=pk)
    if mailing.status != "Sending":
        EmailSender.send_mailing(mailing)
        mailing.first_sending = timezone.now()
        mailing.save()
    return redirect('mailing:list')