from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Mailing list topic", help_text="Enter the mailing list topic")
    body = models.TextField(verbose_name="Mailing text", help_text="Enter the mailing text")
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="messages", verbose_name="Mailing List Creator", blank=True, null=True
    )
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.subject