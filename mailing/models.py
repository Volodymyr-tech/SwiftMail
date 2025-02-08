from django.db import models

from clients.models import Client
from message.models import Message


# Create your models here.
class Mail(models.Model):
    SENT = 'Sent' #данные поля отображаются в БД
    SENDING = 'Sending'
    CREATED = 'Created'

    STATUS_CHOICES = [
        (SENT, 'Sent'), #данные поля отображаются в админке Django
        (SENDING, 'Sending'),
        (CREATED, 'Created'),
    ]

    first_sending = models.DateTimeField(null=True)
    end_sending = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CREATED)
    message = models.ForeignKey(Message, related_name="mails", on_delete=models.CASCADE)
    client = models.ManyToManyField(Client)

    class Meta:
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'
        ordering = ['-first_sending']

    def __str__(self):
        return f'Mail to {", ".join([client.name for client in self.client.all()])}...'


class MailingAttempt(models.Model):
    SUCCESS = 'Success'
    ERROR = 'Error'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (ERROR, 'Error'),
    ]

    date_attempt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True, null=True)
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mailing Attempt'
        verbose_name_plural = 'Mailing Attempts'
        ordering = ['-date_attempt']