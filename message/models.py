from django.db import models

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Mailing list topic", help_text="Enter the mailing list topic")
    body = models.TextField(verbose_name="Mailing text", help_text="Enter the mailing text")

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.subject